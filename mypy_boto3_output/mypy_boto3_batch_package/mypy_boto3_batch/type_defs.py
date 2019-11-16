"Main interface for batch type defs"
from __future__ import annotations

from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateComputeEnvironmentResponseTypeDef",
    "ClientCreateComputeEnvironmentcomputeResourceslaunchTemplateTypeDef",
    "ClientCreateComputeEnvironmentcomputeResourcesTypeDef",
    "ClientCreateJobQueueResponseTypeDef",
    "ClientCreateJobQueuecomputeEnvironmentOrderTypeDef",
    "ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentscomputeResourceslaunchTemplateTypeDef",
    "ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentscomputeResourcesTypeDef",
    "ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentsTypeDef",
    "ClientDescribeComputeEnvironmentsResponseTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesenvironmentTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertieslinuxParametersdevicesTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertieslinuxParametersTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesmountPointsTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesresourceRequirementsTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesulimitsTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesvolumeshostTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesvolumesTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumesTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiesTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsretryStrategyTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionstimeoutTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsTypeDef",
    "ClientDescribeJobDefinitionsResponseTypeDef",
    "ClientDescribeJobQueuesResponsejobQueuescomputeEnvironmentOrderTypeDef",
    "ClientDescribeJobQueuesResponsejobQueuesTypeDef",
    "ClientDescribeJobQueuesResponseTypeDef",
    "ClientDescribeJobsResponsejobsarrayPropertiesTypeDef",
    "ClientDescribeJobsResponsejobsattemptscontainernetworkInterfacesTypeDef",
    "ClientDescribeJobsResponsejobsattemptscontainerTypeDef",
    "ClientDescribeJobsResponsejobsattemptsTypeDef",
    "ClientDescribeJobsResponsejobscontainerenvironmentTypeDef",
    "ClientDescribeJobsResponsejobscontainerlinuxParametersdevicesTypeDef",
    "ClientDescribeJobsResponsejobscontainerlinuxParametersTypeDef",
    "ClientDescribeJobsResponsejobscontainermountPointsTypeDef",
    "ClientDescribeJobsResponsejobscontainernetworkInterfacesTypeDef",
    "ClientDescribeJobsResponsejobscontainerresourceRequirementsTypeDef",
    "ClientDescribeJobsResponsejobscontainerulimitsTypeDef",
    "ClientDescribeJobsResponsejobscontainervolumeshostTypeDef",
    "ClientDescribeJobsResponsejobscontainervolumesTypeDef",
    "ClientDescribeJobsResponsejobscontainerTypeDef",
    "ClientDescribeJobsResponsejobsdependsOnTypeDef",
    "ClientDescribeJobsResponsejobsnodeDetailsTypeDef",
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef",
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef",
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef",
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef",
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef",
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef",
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef",
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainervolumesTypeDef",
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerTypeDef",
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiesTypeDef",
    "ClientDescribeJobsResponsejobsnodePropertiesTypeDef",
    "ClientDescribeJobsResponsejobsretryStrategyTypeDef",
    "ClientDescribeJobsResponsejobstimeoutTypeDef",
    "ClientDescribeJobsResponsejobsTypeDef",
    "ClientDescribeJobsResponseTypeDef",
    "ClientListJobsResponsejobSummaryListarrayPropertiesTypeDef",
    "ClientListJobsResponsejobSummaryListcontainerTypeDef",
    "ClientListJobsResponsejobSummaryListnodePropertiesTypeDef",
    "ClientListJobsResponsejobSummaryListTypeDef",
    "ClientListJobsResponseTypeDef",
    "ClientRegisterJobDefinitionResponseTypeDef",
    "ClientRegisterJobDefinitioncontainerPropertiesenvironmentTypeDef",
    "ClientRegisterJobDefinitioncontainerPropertieslinuxParametersdevicesTypeDef",
    "ClientRegisterJobDefinitioncontainerPropertieslinuxParametersTypeDef",
    "ClientRegisterJobDefinitioncontainerPropertiesmountPointsTypeDef",
    "ClientRegisterJobDefinitioncontainerPropertiesresourceRequirementsTypeDef",
    "ClientRegisterJobDefinitioncontainerPropertiesulimitsTypeDef",
    "ClientRegisterJobDefinitioncontainerPropertiesvolumeshostTypeDef",
    "ClientRegisterJobDefinitioncontainerPropertiesvolumesTypeDef",
    "ClientRegisterJobDefinitioncontainerPropertiesTypeDef",
    "ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef",
    "ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef",
    "ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef",
    "ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainermountPointsTypeDef",
    "ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef",
    "ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerulimitsTypeDef",
    "ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef",
    "ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainervolumesTypeDef",
    "ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerTypeDef",
    "ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiesTypeDef",
    "ClientRegisterJobDefinitionnodePropertiesTypeDef",
    "ClientRegisterJobDefinitionretryStrategyTypeDef",
    "ClientRegisterJobDefinitiontimeoutTypeDef",
    "ClientSubmitJobResponseTypeDef",
    "ClientSubmitJobarrayPropertiesTypeDef",
    "ClientSubmitJobcontainerOverridesenvironmentTypeDef",
    "ClientSubmitJobcontainerOverridesresourceRequirementsTypeDef",
    "ClientSubmitJobcontainerOverridesTypeDef",
    "ClientSubmitJobdependsOnTypeDef",
    "ClientSubmitJobnodeOverridesnodePropertyOverridescontainerOverridesenvironmentTypeDef",
    "ClientSubmitJobnodeOverridesnodePropertyOverridescontainerOverridesresourceRequirementsTypeDef",
    "ClientSubmitJobnodeOverridesnodePropertyOverridescontainerOverridesTypeDef",
    "ClientSubmitJobnodeOverridesnodePropertyOverridesTypeDef",
    "ClientSubmitJobnodeOverridesTypeDef",
    "ClientSubmitJobretryStrategyTypeDef",
    "ClientSubmitJobtimeoutTypeDef",
    "ClientUpdateComputeEnvironmentResponseTypeDef",
    "ClientUpdateComputeEnvironmentcomputeResourcesTypeDef",
    "ClientUpdateJobQueueResponseTypeDef",
    "ClientUpdateJobQueuecomputeEnvironmentOrderTypeDef",
    "DescribeComputeEnvironmentsPaginatePaginationConfigTypeDef",
    "DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentscomputeResourceslaunchTemplateTypeDef",
    "DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentscomputeResourcesTypeDef",
    "DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentsTypeDef",
    "DescribeComputeEnvironmentsPaginateResponseTypeDef",
    "DescribeJobDefinitionsPaginatePaginationConfigTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesenvironmentTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertieslinuxParametersdevicesTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertieslinuxParametersTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesmountPointsTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesresourceRequirementsTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesulimitsTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesvolumeshostTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesvolumesTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumesTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiesTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionsretryStrategyTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionstimeoutTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionsTypeDef",
    "DescribeJobDefinitionsPaginateResponseTypeDef",
    "DescribeJobQueuesPaginatePaginationConfigTypeDef",
    "DescribeJobQueuesPaginateResponsejobQueuescomputeEnvironmentOrderTypeDef",
    "DescribeJobQueuesPaginateResponsejobQueuesTypeDef",
    "DescribeJobQueuesPaginateResponseTypeDef",
    "ListJobsPaginatePaginationConfigTypeDef",
    "ListJobsPaginateResponsejobSummaryListarrayPropertiesTypeDef",
    "ListJobsPaginateResponsejobSummaryListcontainerTypeDef",
    "ListJobsPaginateResponsejobSummaryListnodePropertiesTypeDef",
    "ListJobsPaginateResponsejobSummaryListTypeDef",
    "ListJobsPaginateResponseTypeDef",
)


_ClientCreateComputeEnvironmentResponseTypeDef = TypedDict(
    "_ClientCreateComputeEnvironmentResponseTypeDef",
    {"computeEnvironmentName": str, "computeEnvironmentArn": str},
    total=False,
)


class ClientCreateComputeEnvironmentResponseTypeDef(
    _ClientCreateComputeEnvironmentResponseTypeDef
):
    """
    Type definition for `ClientCreateComputeEnvironment` `Response`

    - **computeEnvironmentName** *(string) --*

      The name of the compute environment.

    - **computeEnvironmentArn** *(string) --*

      The Amazon Resource Name (ARN) of the compute environment.
    """


_ClientCreateComputeEnvironmentcomputeResourceslaunchTemplateTypeDef = TypedDict(
    "_ClientCreateComputeEnvironmentcomputeResourceslaunchTemplateTypeDef",
    {"launchTemplateId": str, "launchTemplateName": str, "version": str},
    total=False,
)


class ClientCreateComputeEnvironmentcomputeResourceslaunchTemplateTypeDef(
    _ClientCreateComputeEnvironmentcomputeResourceslaunchTemplateTypeDef
):
    """
    Type definition for `ClientCreateComputeEnvironmentcomputeResources` `launchTemplate`

    The launch template to use for your compute resources. Any other compute resource parameters
    that you specify in a  CreateComputeEnvironment API operation override the same parameters in
    the launch template. You must specify either the launch template ID or launch template name in
    the request, but not both. For more information, see `Launch Template Support
    <https://docs.aws.amazon.com/batch/latest/userguide/launch-templates.html>`__ in the *AWS Batch
    User Guide* .

    - **launchTemplateId** *(string) --*

      The ID of the launch template.

    - **launchTemplateName** *(string) --*

      The name of the launch template.

    - **version** *(string) --*

      The version number of the launch template.

      Default: The default version of the launch template.
    """


_RequiredClientCreateComputeEnvironmentcomputeResourcesTypeDef = TypedDict(
    "_RequiredClientCreateComputeEnvironmentcomputeResourcesTypeDef",
    {
        "type": str,
        "minvCpus": int,
        "maxvCpus": int,
        "instanceTypes": List[str],
        "subnets": List[str],
        "instanceRole": str,
    },
)
_OptionalClientCreateComputeEnvironmentcomputeResourcesTypeDef = TypedDict(
    "_OptionalClientCreateComputeEnvironmentcomputeResourcesTypeDef",
    {
        "allocationStrategy": str,
        "desiredvCpus": int,
        "imageId": str,
        "securityGroupIds": List[str],
        "ec2KeyPair": str,
        "tags": Dict[str, str],
        "placementGroup": str,
        "bidPercentage": int,
        "spotIamFleetRole": str,
        "launchTemplate": ClientCreateComputeEnvironmentcomputeResourceslaunchTemplateTypeDef,
    },
    total=False,
)


class ClientCreateComputeEnvironmentcomputeResourcesTypeDef(
    _RequiredClientCreateComputeEnvironmentcomputeResourcesTypeDef,
    _OptionalClientCreateComputeEnvironmentcomputeResourcesTypeDef,
):
    """
    Type definition for `ClientCreateComputeEnvironment` `computeResources`

    Details of the compute resources managed by the compute environment. This parameter is required
    for managed compute environments. For more information, see `Compute Environments
    <https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html>`__ in the *AWS
    Batch User Guide* .

    - **type** *(string) --* **[REQUIRED]**

      The type of compute environment: ``EC2`` or ``SPOT`` .

    - **allocationStrategy** *(string) --*

      The allocation strategy to use for the compute resource in case not enough instances of the
      best fitting instance type can be allocated. This could be due to availability of the instance
      type in the region or `Amazon EC2 service limits
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html>`__ . If this is
      not specified, the default is ``BEST_FIT`` , which will use only the best fitting instance
      type, waiting for additional capacity if it's not available. This allocation strategy keeps
      costs lower but can limit scaling. ``BEST_FIT_PROGRESSIVE`` will select an additional instance
      type that is large enough to meet the requirements of the jobs in the queue, with a preference
      for an instance type with a lower cost. ``SPOT_CAPACITY_OPTIMIZED`` is only available for Spot
      Instance compute resources and will select an additional instance type that is large enough to
      meet the requirements of the jobs in the queue, with a preference for an instance type that is
      less likely to be interrupted.

    - **minvCpus** *(integer) --* **[REQUIRED]**

      The minimum number of Amazon EC2 vCPUs that an environment should maintain (even if the compute
      environment is ``DISABLED`` ).

    - **maxvCpus** *(integer) --* **[REQUIRED]**

      The maximum number of Amazon EC2 vCPUs that an environment can reach.

    - **desiredvCpus** *(integer) --*

      The desired number of Amazon EC2 vCPUS in the compute environment.

    - **instanceTypes** *(list) --* **[REQUIRED]**

      The instances types that may be launched. You can specify instance families to launch any
      instance type within those families (for example, ``c5`` or ``p3`` ), or you can specify
      specific sizes within a family (such as ``c5.8xlarge`` ). You can also choose ``optimal`` to
      pick instance types (from the C, M, and R instance families) on the fly that match the demand
      of your job queues.

      - *(string) --*

    - **imageId** *(string) --*

      The Amazon Machine Image (AMI) ID used for instances launched in the compute environment.

    - **subnets** *(list) --* **[REQUIRED]**

      The VPC subnets into which the compute resources are launched. For more information, see `VPCs
      and Subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ in the
      *Amazon VPC User Guide* .

      - *(string) --*

    - **securityGroupIds** *(list) --*

      The Amazon EC2 security groups associated with instances launched in the compute environment.
      One or more security groups must be specified, either in ``securityGroupIds`` or using a launch
      template referenced in ``launchTemplate`` . If security groups are specified using both
      ``securityGroupIds`` and ``launchTemplate`` , the values in ``securityGroupIds`` will be used.

      - *(string) --*

    - **ec2KeyPair** *(string) --*

      The Amazon EC2 key pair that is used for instances launched in the compute environment.

    - **instanceRole** *(string) --* **[REQUIRED]**

      The Amazon ECS instance profile applied to Amazon EC2 instances in a compute environment. You
      can specify the short name or full Amazon Resource Name (ARN) of an instance profile. For
      example, `` *ecsInstanceRole* `` or ``arn:aws:iam::*<aws_account_id>*
      :instance-profile/*ecsInstanceRole* `` . For more information, see `Amazon ECS Instance Role
      <https://docs.aws.amazon.com/batch/latest/userguide/instance_IAM_role.html>`__ in the *AWS
      Batch User Guide* .

    - **tags** *(dict) --*

      Key-value pair tags to be applied to resources that are launched in the compute environment.
      For AWS Batch, these take the form of "String1": "String2", where String1 is the tag key and
      String2 is the tag value—for example, { "Name": "AWS Batch Instance - C4OnDemand" }.

      - *(string) --*

        - *(string) --*

    - **placementGroup** *(string) --*

      The Amazon EC2 placement group to associate with your compute resources. If you intend to
      submit multi-node parallel jobs to your compute environment, you should consider creating a
      cluster placement group and associate it with your compute resources. This keeps your
      multi-node parallel job on a logical grouping of instances within a single Availability Zone
      with high network flow potential. For more information, see `Placement Groups
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html>`__ in the *Amazon
      EC2 User Guide for Linux Instances* .

    - **bidPercentage** *(integer) --*

      The maximum percentage that a Spot Instance price can be when compared with the On-Demand price
      for that instance type before instances are launched. For example, if your maximum percentage
      is 20%, then the Spot price must be below 20% of the current On-Demand price for that Amazon
      EC2 instance. You always pay the lowest (market) price and never more than your maximum
      percentage. If you leave this field empty, the default value is 100% of the On-Demand price.

    - **spotIamFleetRole** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a ``SPOT``
      compute environment. For more information, see `Amazon EC2 Spot Fleet Role
      <https://docs.aws.amazon.com/batch/latest/userguide/spot_fleet_IAM_role.html>`__ in the *AWS
      Batch User Guide* .

    - **launchTemplate** *(dict) --*

      The launch template to use for your compute resources. Any other compute resource parameters
      that you specify in a  CreateComputeEnvironment API operation override the same parameters in
      the launch template. You must specify either the launch template ID or launch template name in
      the request, but not both. For more information, see `Launch Template Support
      <https://docs.aws.amazon.com/batch/latest/userguide/launch-templates.html>`__ in the *AWS Batch
      User Guide* .

      - **launchTemplateId** *(string) --*

        The ID of the launch template.

      - **launchTemplateName** *(string) --*

        The name of the launch template.

      - **version** *(string) --*

        The version number of the launch template.

        Default: The default version of the launch template.
    """


_ClientCreateJobQueueResponseTypeDef = TypedDict(
    "_ClientCreateJobQueueResponseTypeDef",
    {"jobQueueName": str, "jobQueueArn": str},
    total=False,
)


class ClientCreateJobQueueResponseTypeDef(_ClientCreateJobQueueResponseTypeDef):
    """
    Type definition for `ClientCreateJobQueue` `Response`

    - **jobQueueName** *(string) --*

      The name of the job queue.

    - **jobQueueArn** *(string) --*

      The Amazon Resource Name (ARN) of the job queue.
    """


_ClientCreateJobQueuecomputeEnvironmentOrderTypeDef = TypedDict(
    "_ClientCreateJobQueuecomputeEnvironmentOrderTypeDef",
    {"order": int, "computeEnvironment": str},
)


class ClientCreateJobQueuecomputeEnvironmentOrderTypeDef(
    _ClientCreateJobQueuecomputeEnvironmentOrderTypeDef
):
    """
    Type definition for `ClientCreateJobQueue` `computeEnvironmentOrder`

    The order in which compute environments are tried for job placement within a queue. Compute
    environments are tried in ascending order. For example, if two compute environments are
    associated with a job queue, the compute environment with a lower order integer value is tried
    for job placement first.

    - **order** *(integer) --* **[REQUIRED]**

      The order of the compute environment.

    - **computeEnvironment** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the compute environment.
    """


_ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentscomputeResourceslaunchTemplateTypeDef = TypedDict(
    "_ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentscomputeResourceslaunchTemplateTypeDef",
    {"launchTemplateId": str, "launchTemplateName": str, "version": str},
    total=False,
)


class ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentscomputeResourceslaunchTemplateTypeDef(
    _ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentscomputeResourceslaunchTemplateTypeDef
):
    """
    Type definition for `ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentscomputeResources` `launchTemplate`

    The launch template to use for your compute resources. Any other compute resource
    parameters that you specify in a  CreateComputeEnvironment API operation override the
    same parameters in the launch template. You must specify either the launch template ID
    or launch template name in the request, but not both. For more information, see `Launch
    Template Support
    <https://docs.aws.amazon.com/batch/latest/userguide/launch-templates.html>`__ in the
    *AWS Batch User Guide* .

    - **launchTemplateId** *(string) --*

      The ID of the launch template.

    - **launchTemplateName** *(string) --*

      The name of the launch template.

    - **version** *(string) --*

      The version number of the launch template.

      Default: The default version of the launch template.
    """


_ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentscomputeResourcesTypeDef = TypedDict(
    "_ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentscomputeResourcesTypeDef",
    {
        "type": str,
        "allocationStrategy": str,
        "minvCpus": int,
        "maxvCpus": int,
        "desiredvCpus": int,
        "instanceTypes": List[str],
        "imageId": str,
        "subnets": List[str],
        "securityGroupIds": List[str],
        "ec2KeyPair": str,
        "instanceRole": str,
        "tags": Dict[str, str],
        "placementGroup": str,
        "bidPercentage": int,
        "spotIamFleetRole": str,
        "launchTemplate": ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentscomputeResourceslaunchTemplateTypeDef,
    },
    total=False,
)


class ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentscomputeResourcesTypeDef(
    _ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentscomputeResourcesTypeDef
):
    """
    Type definition for `ClientDescribeComputeEnvironmentsResponsecomputeEnvironments` `computeResources`

    The compute resources defined for the compute environment.

    - **type** *(string) --*

      The type of compute environment: ``EC2`` or ``SPOT`` .

    - **allocationStrategy** *(string) --*

      The allocation strategy to use for the compute resource in case not enough instances of
      the best fitting instance type can be allocated. This could be due to availability of
      the instance type in the region or `Amazon EC2 service limits
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html>`__ . If
      this is not specified, the default is ``BEST_FIT`` , which will use only the best
      fitting instance type, waiting for additional capacity if it's not available. This
      allocation strategy keeps costs lower but can limit scaling. ``BEST_FIT_PROGRESSIVE``
      will select an additional instance type that is large enough to meet the requirements
      of the jobs in the queue, with a preference for an instance type with a lower cost.
      ``SPOT_CAPACITY_OPTIMIZED`` is only available for Spot Instance compute resources and
      will select an additional instance type that is large enough to meet the requirements
      of the jobs in the queue, with a preference for an instance type that is less likely to
      be interrupted.

    - **minvCpus** *(integer) --*

      The minimum number of Amazon EC2 vCPUs that an environment should maintain (even if the
      compute environment is ``DISABLED`` ).

    - **maxvCpus** *(integer) --*

      The maximum number of Amazon EC2 vCPUs that an environment can reach.

    - **desiredvCpus** *(integer) --*

      The desired number of Amazon EC2 vCPUS in the compute environment.

    - **instanceTypes** *(list) --*

      The instances types that may be launched. You can specify instance families to launch
      any instance type within those families (for example, ``c5`` or ``p3`` ), or you can
      specify specific sizes within a family (such as ``c5.8xlarge`` ). You can also choose
      ``optimal`` to pick instance types (from the C, M, and R instance families) on the fly
      that match the demand of your job queues.

      - *(string) --*

    - **imageId** *(string) --*

      The Amazon Machine Image (AMI) ID used for instances launched in the compute
      environment.

    - **subnets** *(list) --*

      The VPC subnets into which the compute resources are launched. For more information,
      see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ in the *Amazon
      VPC User Guide* .

      - *(string) --*

    - **securityGroupIds** *(list) --*

      The Amazon EC2 security groups associated with instances launched in the compute
      environment. One or more security groups must be specified, either in
      ``securityGroupIds`` or using a launch template referenced in ``launchTemplate`` . If
      security groups are specified using both ``securityGroupIds`` and ``launchTemplate`` ,
      the values in ``securityGroupIds`` will be used.

      - *(string) --*

    - **ec2KeyPair** *(string) --*

      The Amazon EC2 key pair that is used for instances launched in the compute environment.

    - **instanceRole** *(string) --*

      The Amazon ECS instance profile applied to Amazon EC2 instances in a compute
      environment. You can specify the short name or full Amazon Resource Name (ARN) of an
      instance profile. For example, `` *ecsInstanceRole* `` or
      ``arn:aws:iam::*<aws_account_id>* :instance-profile/*ecsInstanceRole* `` . For more
      information, see `Amazon ECS Instance Role
      <https://docs.aws.amazon.com/batch/latest/userguide/instance_IAM_role.html>`__ in the
      *AWS Batch User Guide* .

    - **tags** *(dict) --*

      Key-value pair tags to be applied to resources that are launched in the compute
      environment. For AWS Batch, these take the form of "String1": "String2", where String1
      is the tag key and String2 is the tag value—for example, { "Name": "AWS Batch Instance
      - C4OnDemand" }.

      - *(string) --*

        - *(string) --*

    - **placementGroup** *(string) --*

      The Amazon EC2 placement group to associate with your compute resources. If you intend
      to submit multi-node parallel jobs to your compute environment, you should consider
      creating a cluster placement group and associate it with your compute resources. This
      keeps your multi-node parallel job on a logical grouping of instances within a single
      Availability Zone with high network flow potential. For more information, see
      `Placement Groups
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html>`__ in the
      *Amazon EC2 User Guide for Linux Instances* .

    - **bidPercentage** *(integer) --*

      The maximum percentage that a Spot Instance price can be when compared with the
      On-Demand price for that instance type before instances are launched. For example, if
      your maximum percentage is 20%, then the Spot price must be below 20% of the current
      On-Demand price for that Amazon EC2 instance. You always pay the lowest (market) price
      and never more than your maximum percentage. If you leave this field empty, the default
      value is 100% of the On-Demand price.

    - **spotIamFleetRole** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a
      ``SPOT`` compute environment. For more information, see `Amazon EC2 Spot Fleet Role
      <https://docs.aws.amazon.com/batch/latest/userguide/spot_fleet_IAM_role.html>`__ in the
      *AWS Batch User Guide* .

    - **launchTemplate** *(dict) --*

      The launch template to use for your compute resources. Any other compute resource
      parameters that you specify in a  CreateComputeEnvironment API operation override the
      same parameters in the launch template. You must specify either the launch template ID
      or launch template name in the request, but not both. For more information, see `Launch
      Template Support
      <https://docs.aws.amazon.com/batch/latest/userguide/launch-templates.html>`__ in the
      *AWS Batch User Guide* .

      - **launchTemplateId** *(string) --*

        The ID of the launch template.

      - **launchTemplateName** *(string) --*

        The name of the launch template.

      - **version** *(string) --*

        The version number of the launch template.

        Default: The default version of the launch template.
    """


_ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentsTypeDef = TypedDict(
    "_ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentsTypeDef",
    {
        "computeEnvironmentName": str,
        "computeEnvironmentArn": str,
        "ecsClusterArn": str,
        "type": str,
        "state": str,
        "status": str,
        "statusReason": str,
        "computeResources": ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentscomputeResourcesTypeDef,
        "serviceRole": str,
    },
    total=False,
)


class ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentsTypeDef(
    _ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentsTypeDef
):
    """
    Type definition for `ClientDescribeComputeEnvironmentsResponse` `computeEnvironments`

    An object representing an AWS Batch compute environment.

    - **computeEnvironmentName** *(string) --*

      The name of the compute environment.

    - **computeEnvironmentArn** *(string) --*

      The Amazon Resource Name (ARN) of the compute environment.

    - **ecsClusterArn** *(string) --*

      The Amazon Resource Name (ARN) of the underlying Amazon ECS cluster used by the compute
      environment.

    - **type** *(string) --*

      The type of the compute environment.

    - **state** *(string) --*

      The state of the compute environment. The valid values are ``ENABLED`` or ``DISABLED`` .

      If the state is ``ENABLED`` , then the AWS Batch scheduler can attempt to place jobs from
      an associated job queue on the compute resources within the environment. If the compute
      environment is managed, then it can scale its instances out or in automatically, based on
      the job queue demand.

      If the state is ``DISABLED`` , then the AWS Batch scheduler does not attempt to place
      jobs within the environment. Jobs in a ``STARTING`` or ``RUNNING`` state continue to
      progress normally. Managed compute environments in the ``DISABLED`` state do not scale
      out. However, they scale in to ``minvCpus`` value after instances become idle.

    - **status** *(string) --*

      The current status of the compute environment (for example, ``CREATING`` or ``VALID`` ).

    - **statusReason** *(string) --*

      A short, human-readable string to provide additional details about the current status of
      the compute environment.

    - **computeResources** *(dict) --*

      The compute resources defined for the compute environment.

      - **type** *(string) --*

        The type of compute environment: ``EC2`` or ``SPOT`` .

      - **allocationStrategy** *(string) --*

        The allocation strategy to use for the compute resource in case not enough instances of
        the best fitting instance type can be allocated. This could be due to availability of
        the instance type in the region or `Amazon EC2 service limits
        <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html>`__ . If
        this is not specified, the default is ``BEST_FIT`` , which will use only the best
        fitting instance type, waiting for additional capacity if it's not available. This
        allocation strategy keeps costs lower but can limit scaling. ``BEST_FIT_PROGRESSIVE``
        will select an additional instance type that is large enough to meet the requirements
        of the jobs in the queue, with a preference for an instance type with a lower cost.
        ``SPOT_CAPACITY_OPTIMIZED`` is only available for Spot Instance compute resources and
        will select an additional instance type that is large enough to meet the requirements
        of the jobs in the queue, with a preference for an instance type that is less likely to
        be interrupted.

      - **minvCpus** *(integer) --*

        The minimum number of Amazon EC2 vCPUs that an environment should maintain (even if the
        compute environment is ``DISABLED`` ).

      - **maxvCpus** *(integer) --*

        The maximum number of Amazon EC2 vCPUs that an environment can reach.

      - **desiredvCpus** *(integer) --*

        The desired number of Amazon EC2 vCPUS in the compute environment.

      - **instanceTypes** *(list) --*

        The instances types that may be launched. You can specify instance families to launch
        any instance type within those families (for example, ``c5`` or ``p3`` ), or you can
        specify specific sizes within a family (such as ``c5.8xlarge`` ). You can also choose
        ``optimal`` to pick instance types (from the C, M, and R instance families) on the fly
        that match the demand of your job queues.

        - *(string) --*

      - **imageId** *(string) --*

        The Amazon Machine Image (AMI) ID used for instances launched in the compute
        environment.

      - **subnets** *(list) --*

        The VPC subnets into which the compute resources are launched. For more information,
        see `VPCs and Subnets
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ in the *Amazon
        VPC User Guide* .

        - *(string) --*

      - **securityGroupIds** *(list) --*

        The Amazon EC2 security groups associated with instances launched in the compute
        environment. One or more security groups must be specified, either in
        ``securityGroupIds`` or using a launch template referenced in ``launchTemplate`` . If
        security groups are specified using both ``securityGroupIds`` and ``launchTemplate`` ,
        the values in ``securityGroupIds`` will be used.

        - *(string) --*

      - **ec2KeyPair** *(string) --*

        The Amazon EC2 key pair that is used for instances launched in the compute environment.

      - **instanceRole** *(string) --*

        The Amazon ECS instance profile applied to Amazon EC2 instances in a compute
        environment. You can specify the short name or full Amazon Resource Name (ARN) of an
        instance profile. For example, `` *ecsInstanceRole* `` or
        ``arn:aws:iam::*<aws_account_id>* :instance-profile/*ecsInstanceRole* `` . For more
        information, see `Amazon ECS Instance Role
        <https://docs.aws.amazon.com/batch/latest/userguide/instance_IAM_role.html>`__ in the
        *AWS Batch User Guide* .

      - **tags** *(dict) --*

        Key-value pair tags to be applied to resources that are launched in the compute
        environment. For AWS Batch, these take the form of "String1": "String2", where String1
        is the tag key and String2 is the tag value—for example, { "Name": "AWS Batch Instance
        - C4OnDemand" }.

        - *(string) --*

          - *(string) --*

      - **placementGroup** *(string) --*

        The Amazon EC2 placement group to associate with your compute resources. If you intend
        to submit multi-node parallel jobs to your compute environment, you should consider
        creating a cluster placement group and associate it with your compute resources. This
        keeps your multi-node parallel job on a logical grouping of instances within a single
        Availability Zone with high network flow potential. For more information, see
        `Placement Groups
        <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html>`__ in the
        *Amazon EC2 User Guide for Linux Instances* .

      - **bidPercentage** *(integer) --*

        The maximum percentage that a Spot Instance price can be when compared with the
        On-Demand price for that instance type before instances are launched. For example, if
        your maximum percentage is 20%, then the Spot price must be below 20% of the current
        On-Demand price for that Amazon EC2 instance. You always pay the lowest (market) price
        and never more than your maximum percentage. If you leave this field empty, the default
        value is 100% of the On-Demand price.

      - **spotIamFleetRole** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a
        ``SPOT`` compute environment. For more information, see `Amazon EC2 Spot Fleet Role
        <https://docs.aws.amazon.com/batch/latest/userguide/spot_fleet_IAM_role.html>`__ in the
        *AWS Batch User Guide* .

      - **launchTemplate** *(dict) --*

        The launch template to use for your compute resources. Any other compute resource
        parameters that you specify in a  CreateComputeEnvironment API operation override the
        same parameters in the launch template. You must specify either the launch template ID
        or launch template name in the request, but not both. For more information, see `Launch
        Template Support
        <https://docs.aws.amazon.com/batch/latest/userguide/launch-templates.html>`__ in the
        *AWS Batch User Guide* .

        - **launchTemplateId** *(string) --*

          The ID of the launch template.

        - **launchTemplateName** *(string) --*

          The name of the launch template.

        - **version** *(string) --*

          The version number of the launch template.

          Default: The default version of the launch template.

    - **serviceRole** *(string) --*

      The service role associated with the compute environment that allows AWS Batch to make
      calls to AWS API operations on your behalf.
    """


_ClientDescribeComputeEnvironmentsResponseTypeDef = TypedDict(
    "_ClientDescribeComputeEnvironmentsResponseTypeDef",
    {
        "computeEnvironments": List[
            ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeComputeEnvironmentsResponseTypeDef(
    _ClientDescribeComputeEnvironmentsResponseTypeDef
):
    """
    Type definition for `ClientDescribeComputeEnvironments` `Response`

    - **computeEnvironments** *(list) --*

      The list of compute environments.

      - *(dict) --*

        An object representing an AWS Batch compute environment.

        - **computeEnvironmentName** *(string) --*

          The name of the compute environment.

        - **computeEnvironmentArn** *(string) --*

          The Amazon Resource Name (ARN) of the compute environment.

        - **ecsClusterArn** *(string) --*

          The Amazon Resource Name (ARN) of the underlying Amazon ECS cluster used by the compute
          environment.

        - **type** *(string) --*

          The type of the compute environment.

        - **state** *(string) --*

          The state of the compute environment. The valid values are ``ENABLED`` or ``DISABLED`` .

          If the state is ``ENABLED`` , then the AWS Batch scheduler can attempt to place jobs from
          an associated job queue on the compute resources within the environment. If the compute
          environment is managed, then it can scale its instances out or in automatically, based on
          the job queue demand.

          If the state is ``DISABLED`` , then the AWS Batch scheduler does not attempt to place
          jobs within the environment. Jobs in a ``STARTING`` or ``RUNNING`` state continue to
          progress normally. Managed compute environments in the ``DISABLED`` state do not scale
          out. However, they scale in to ``minvCpus`` value after instances become idle.

        - **status** *(string) --*

          The current status of the compute environment (for example, ``CREATING`` or ``VALID`` ).

        - **statusReason** *(string) --*

          A short, human-readable string to provide additional details about the current status of
          the compute environment.

        - **computeResources** *(dict) --*

          The compute resources defined for the compute environment.

          - **type** *(string) --*

            The type of compute environment: ``EC2`` or ``SPOT`` .

          - **allocationStrategy** *(string) --*

            The allocation strategy to use for the compute resource in case not enough instances of
            the best fitting instance type can be allocated. This could be due to availability of
            the instance type in the region or `Amazon EC2 service limits
            <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html>`__ . If
            this is not specified, the default is ``BEST_FIT`` , which will use only the best
            fitting instance type, waiting for additional capacity if it's not available. This
            allocation strategy keeps costs lower but can limit scaling. ``BEST_FIT_PROGRESSIVE``
            will select an additional instance type that is large enough to meet the requirements
            of the jobs in the queue, with a preference for an instance type with a lower cost.
            ``SPOT_CAPACITY_OPTIMIZED`` is only available for Spot Instance compute resources and
            will select an additional instance type that is large enough to meet the requirements
            of the jobs in the queue, with a preference for an instance type that is less likely to
            be interrupted.

          - **minvCpus** *(integer) --*

            The minimum number of Amazon EC2 vCPUs that an environment should maintain (even if the
            compute environment is ``DISABLED`` ).

          - **maxvCpus** *(integer) --*

            The maximum number of Amazon EC2 vCPUs that an environment can reach.

          - **desiredvCpus** *(integer) --*

            The desired number of Amazon EC2 vCPUS in the compute environment.

          - **instanceTypes** *(list) --*

            The instances types that may be launched. You can specify instance families to launch
            any instance type within those families (for example, ``c5`` or ``p3`` ), or you can
            specify specific sizes within a family (such as ``c5.8xlarge`` ). You can also choose
            ``optimal`` to pick instance types (from the C, M, and R instance families) on the fly
            that match the demand of your job queues.

            - *(string) --*

          - **imageId** *(string) --*

            The Amazon Machine Image (AMI) ID used for instances launched in the compute
            environment.

          - **subnets** *(list) --*

            The VPC subnets into which the compute resources are launched. For more information,
            see `VPCs and Subnets
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ in the *Amazon
            VPC User Guide* .

            - *(string) --*

          - **securityGroupIds** *(list) --*

            The Amazon EC2 security groups associated with instances launched in the compute
            environment. One or more security groups must be specified, either in
            ``securityGroupIds`` or using a launch template referenced in ``launchTemplate`` . If
            security groups are specified using both ``securityGroupIds`` and ``launchTemplate`` ,
            the values in ``securityGroupIds`` will be used.

            - *(string) --*

          - **ec2KeyPair** *(string) --*

            The Amazon EC2 key pair that is used for instances launched in the compute environment.

          - **instanceRole** *(string) --*

            The Amazon ECS instance profile applied to Amazon EC2 instances in a compute
            environment. You can specify the short name or full Amazon Resource Name (ARN) of an
            instance profile. For example, `` *ecsInstanceRole* `` or
            ``arn:aws:iam::*<aws_account_id>* :instance-profile/*ecsInstanceRole* `` . For more
            information, see `Amazon ECS Instance Role
            <https://docs.aws.amazon.com/batch/latest/userguide/instance_IAM_role.html>`__ in the
            *AWS Batch User Guide* .

          - **tags** *(dict) --*

            Key-value pair tags to be applied to resources that are launched in the compute
            environment. For AWS Batch, these take the form of "String1": "String2", where String1
            is the tag key and String2 is the tag value—for example, { "Name": "AWS Batch Instance
            - C4OnDemand" }.

            - *(string) --*

              - *(string) --*

          - **placementGroup** *(string) --*

            The Amazon EC2 placement group to associate with your compute resources. If you intend
            to submit multi-node parallel jobs to your compute environment, you should consider
            creating a cluster placement group and associate it with your compute resources. This
            keeps your multi-node parallel job on a logical grouping of instances within a single
            Availability Zone with high network flow potential. For more information, see
            `Placement Groups
            <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html>`__ in the
            *Amazon EC2 User Guide for Linux Instances* .

          - **bidPercentage** *(integer) --*

            The maximum percentage that a Spot Instance price can be when compared with the
            On-Demand price for that instance type before instances are launched. For example, if
            your maximum percentage is 20%, then the Spot price must be below 20% of the current
            On-Demand price for that Amazon EC2 instance. You always pay the lowest (market) price
            and never more than your maximum percentage. If you leave this field empty, the default
            value is 100% of the On-Demand price.

          - **spotIamFleetRole** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a
            ``SPOT`` compute environment. For more information, see `Amazon EC2 Spot Fleet Role
            <https://docs.aws.amazon.com/batch/latest/userguide/spot_fleet_IAM_role.html>`__ in the
            *AWS Batch User Guide* .

          - **launchTemplate** *(dict) --*

            The launch template to use for your compute resources. Any other compute resource
            parameters that you specify in a  CreateComputeEnvironment API operation override the
            same parameters in the launch template. You must specify either the launch template ID
            or launch template name in the request, but not both. For more information, see `Launch
            Template Support
            <https://docs.aws.amazon.com/batch/latest/userguide/launch-templates.html>`__ in the
            *AWS Batch User Guide* .

            - **launchTemplateId** *(string) --*

              The ID of the launch template.

            - **launchTemplateName** *(string) --*

              The name of the launch template.

            - **version** *(string) --*

              The version number of the launch template.

              Default: The default version of the launch template.

        - **serviceRole** *(string) --*

          The service role associated with the compute environment that allows AWS Batch to make
          calls to AWS API operations on your behalf.

    - **nextToken** *(string) --*

      The ``nextToken`` value to include in a future ``DescribeComputeEnvironments`` request. When
      the results of a ``DescribeJobDefinitions`` request exceed ``maxResults`` , this value can be
      used to retrieve the next page of results. This value is ``null`` when there are no more
      results to return.
    """


_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesenvironmentTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesenvironmentTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesenvironmentTypeDef
):
    """
    Type definition for `ClientDescribeJobDefinitionsResponsejobDefinitionscontainerProperties` `environment`

    A key-value pair object.

    - **name** *(string) --*

      The name of the key-value pair. For environment variables, this is the name of the
      environment variable.

    - **value** *(string) --*

      The value of the key-value pair. For environment variables, this is the value of
      the environment variable.
    """


_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertieslinuxParametersdevicesTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertieslinuxParametersdevicesTypeDef",
    {"hostPath": str, "containerPath": str, "permissions": List[str]},
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertieslinuxParametersdevicesTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertieslinuxParametersdevicesTypeDef
):
    """
    Type definition for `ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertieslinuxParameters` `devices`

    An object representing a container instance host device.

    - **hostPath** *(string) --*

      The path for the device on the host container instance.

    - **containerPath** *(string) --*

      The path inside the container at which to expose the host device. By default the
      ``hostPath`` value is used.

    - **permissions** *(list) --*

      The explicit permissions to provide to the container for the device. By default,
      the container has permissions for ``read`` , ``write`` , and ``mknod`` for the
      device.

      - *(string) --*
    """


_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertieslinuxParametersTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertieslinuxParametersTypeDef",
    {
        "devices": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertieslinuxParametersdevicesTypeDef
        ]
    },
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertieslinuxParametersTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertieslinuxParametersTypeDef
):
    """
    Type definition for `ClientDescribeJobDefinitionsResponsejobDefinitionscontainerProperties` `linuxParameters`

    Linux-specific modifications that are applied to the container, such as details for
    device mappings.

    - **devices** *(list) --*

      Any host devices to expose to the container. This parameter maps to ``Devices`` in
      the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--device`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__
      .

      - *(dict) --*

        An object representing a container instance host device.

        - **hostPath** *(string) --*

          The path for the device on the host container instance.

        - **containerPath** *(string) --*

          The path inside the container at which to expose the host device. By default the
          ``hostPath`` value is used.

        - **permissions** *(list) --*

          The explicit permissions to provide to the container for the device. By default,
          the container has permissions for ``read`` , ``write`` , and ``mknod`` for the
          device.

          - *(string) --*
    """


_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesmountPointsTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesmountPointsTypeDef",
    {"containerPath": str, "readOnly": bool, "sourceVolume": str},
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesmountPointsTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesmountPointsTypeDef
):
    """
    Type definition for `ClientDescribeJobDefinitionsResponsejobDefinitionscontainerProperties` `mountPoints`

    Details on a Docker volume mount point that is used in a job's container properties.
    This parameter maps to ``Volumes`` in the `Create a container
    <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
    section of the Docker Remote API and the ``--volume`` option to docker run.

    - **containerPath** *(string) --*

      The path on the container at which to mount the host volume.

    - **readOnly** *(boolean) --*

      If this value is ``true`` , the container has read-only access to the volume;
      otherwise, the container can write to the volume. The default value is ``false`` .

    - **sourceVolume** *(string) --*

      The name of the volume to mount.
    """


_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesresourceRequirementsTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesresourceRequirementsTypeDef",
    {"value": str, "type": str},
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesresourceRequirementsTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesresourceRequirementsTypeDef
):
    """
    Type definition for `ClientDescribeJobDefinitionsResponsejobDefinitionscontainerProperties` `resourceRequirements`

    The type and amount of a resource to assign to a container. Currently, the only
    supported resource type is ``GPU`` .

    - **value** *(string) --*

      The number of physical GPUs to reserve for the container. The number of GPUs
      reserved for all containers in a job should not exceed the number of available GPUs
      on the compute resource that the job is launched on.

    - **type** *(string) --*

      The type of resource to assign to a container. Currently, the only supported
      resource type is ``GPU`` .
    """


_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesulimitsTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesulimitsTypeDef",
    {"hardLimit": int, "name": str, "softLimit": int},
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesulimitsTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesulimitsTypeDef
):
    """
    Type definition for `ClientDescribeJobDefinitionsResponsejobDefinitionscontainerProperties` `ulimits`

    The ``ulimit`` settings to pass to the container.

    - **hardLimit** *(integer) --*

      The hard limit for the ``ulimit`` type.

    - **name** *(string) --*

      The ``type`` of the ``ulimit`` .

    - **softLimit** *(integer) --*

      The soft limit for the ``ulimit`` type.
    """


_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesvolumeshostTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesvolumeshostTypeDef",
    {"sourcePath": str},
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesvolumeshostTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesvolumeshostTypeDef
):
    """
    Type definition for `ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesvolumes` `host`

    The contents of the ``host`` parameter determine whether your data volume persists
    on the host container instance and where it is stored. If the host parameter is
    empty, then the Docker daemon assigns a host path for your data volume. However,
    the data is not guaranteed to persist after the containers associated with it stop
    running.

    - **sourcePath** *(string) --*

      The path on the host container instance that is presented to the container. If
      this parameter is empty, then the Docker daemon has assigned a host path for you.
      If this parameter contains a file location, then the data volume persists at the
      specified location on the host container instance until you delete it manually.
      If the source path location does not exist on the host container instance, the
      Docker daemon creates it. If the location does exist, the contents of the source
      path folder are exported.
    """


_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesvolumesTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesvolumesTypeDef",
    {
        "host": ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesvolumeshostTypeDef,
        "name": str,
    },
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesvolumesTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesvolumesTypeDef
):
    """
    Type definition for `ClientDescribeJobDefinitionsResponsejobDefinitionscontainerProperties` `volumes`

    A data volume used in a job's container properties.

    - **host** *(dict) --*

      The contents of the ``host`` parameter determine whether your data volume persists
      on the host container instance and where it is stored. If the host parameter is
      empty, then the Docker daemon assigns a host path for your data volume. However,
      the data is not guaranteed to persist after the containers associated with it stop
      running.

      - **sourcePath** *(string) --*

        The path on the host container instance that is presented to the container. If
        this parameter is empty, then the Docker daemon has assigned a host path for you.
        If this parameter contains a file location, then the data volume persists at the
        specified location on the host container instance until you delete it manually.
        If the source path location does not exist on the host container instance, the
        Docker daemon creates it. If the location does exist, the contents of the source
        path folder are exported.

    - **name** *(string) --*

      The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
      hyphens, and underscores are allowed. This name is referenced in the
      ``sourceVolume`` parameter of container definition ``mountPoints`` .
    """


_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesTypeDef",
    {
        "image": str,
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "jobRoleArn": str,
        "volumes": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesvolumesTypeDef
        ],
        "environment": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesenvironmentTypeDef
        ],
        "mountPoints": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesmountPointsTypeDef
        ],
        "readonlyRootFilesystem": bool,
        "privileged": bool,
        "ulimits": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesulimitsTypeDef
        ],
        "user": str,
        "instanceType": str,
        "resourceRequirements": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesresourceRequirementsTypeDef
        ],
        "linuxParameters": ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertieslinuxParametersTypeDef,
    },
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesTypeDef
):
    """
    Type definition for `ClientDescribeJobDefinitionsResponsejobDefinitions` `containerProperties`

    An object with various properties specific to container-based jobs.

    - **image** *(string) --*

      The image used to start a container. This string is passed directly to the Docker
      daemon. Images in the Docker Hub registry are available by default. Other repositories
      are specified with `` *repository-url* /*image* :*tag* `` . Up to 255 letters
      (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward
      slashes, and number signs are allowed. This parameter maps to ``Image`` in the `Create
      a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section
      of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``IMAGE`` parameter of `docker run <https://docs.docker.com/engine/reference/run/>`__ .

      * Images in Amazon ECR repositories use the full registry and repository URI (for
      example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ).

      * Images in official repositories on Docker Hub use a single name (for example,
      ``ubuntu`` or ``mongo`` ).

      * Images in other repositories on Docker Hub are qualified with an organization name
      (for example, ``amazon/amazon-ecs-agent`` ).

      * Images in other online repositories are qualified further by a domain name (for
      example, ``quay.io/assemblyline/ubuntu`` ).

    - **vcpus** *(integer) --*

      The number of vCPUs reserved for the container. This parameter maps to ``CpuShares`` in
      the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--cpu-shares`` option to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ . Each vCPU is equivalent to 1,024
      CPU shares. You must specify at least one vCPU.

    - **memory** *(integer) --*

      The hard limit (in MiB) of memory to present to the container. If your container
      attempts to exceed the memory specified here, the container is killed. This parameter
      maps to ``Memory`` in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--memory``
      option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . You must
      specify at least 4 MiB of memory for a job.

      .. note::

        If you are trying to maximize your resource utilization by providing your jobs as
        much memory as possible for a particular instance type, see `Memory Management
        <https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`__ in the
        *AWS Batch User Guide* .

    - **command** *(list) --*

      The command that is passed to the container. This parameter maps to ``Cmd`` in the
      `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
      section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and
      the ``COMMAND`` parameter to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ . For more information, see
      `https\\://docs.docker.com/engine/reference/builder/#cmd
      <https://docs.docker.com/engine/reference/builder/#cmd>`__ .

      - *(string) --*

    - **jobRoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS
      permissions.

    - **volumes** *(list) --*

      A list of data volumes used in a job.

      - *(dict) --*

        A data volume used in a job's container properties.

        - **host** *(dict) --*

          The contents of the ``host`` parameter determine whether your data volume persists
          on the host container instance and where it is stored. If the host parameter is
          empty, then the Docker daemon assigns a host path for your data volume. However,
          the data is not guaranteed to persist after the containers associated with it stop
          running.

          - **sourcePath** *(string) --*

            The path on the host container instance that is presented to the container. If
            this parameter is empty, then the Docker daemon has assigned a host path for you.
            If this parameter contains a file location, then the data volume persists at the
            specified location on the host container instance until you delete it manually.
            If the source path location does not exist on the host container instance, the
            Docker daemon creates it. If the location does exist, the contents of the source
            path folder are exported.

        - **name** *(string) --*

          The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
          hyphens, and underscores are allowed. This name is referenced in the
          ``sourceVolume`` parameter of container definition ``mountPoints`` .

    - **environment** *(list) --*

      The environment variables to pass to a container. This parameter maps to ``Env`` in the
      `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
      section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and
      the ``--env`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

      .. warning::

        We do not recommend using plaintext environment variables for sensitive information,
        such as credential data.

      .. note::

        Environment variables must not start with ``AWS_BATCH`` ; this naming convention is
        reserved for variables that are set by the AWS Batch service.

      - *(dict) --*

        A key-value pair object.

        - **name** *(string) --*

          The name of the key-value pair. For environment variables, this is the name of the
          environment variable.

        - **value** *(string) --*

          The value of the key-value pair. For environment variables, this is the value of
          the environment variable.

    - **mountPoints** *(list) --*

      The mount points for data volumes in your container. This parameter maps to ``Volumes``
      in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--volume``
      option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

      - *(dict) --*

        Details on a Docker volume mount point that is used in a job's container properties.
        This parameter maps to ``Volumes`` in the `Create a container
        <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
        section of the Docker Remote API and the ``--volume`` option to docker run.

        - **containerPath** *(string) --*

          The path on the container at which to mount the host volume.

        - **readOnly** *(boolean) --*

          If this value is ``true`` , the container has read-only access to the volume;
          otherwise, the container can write to the volume. The default value is ``false`` .

        - **sourceVolume** *(string) --*

          The name of the volume to mount.

    - **readonlyRootFilesystem** *(boolean) --*

      When this parameter is true, the container is given read-only access to its root file
      system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--read-only`` option to ``docker run`` .

    - **privileged** *(boolean) --*

      When this parameter is true, the container is given elevated privileges on the host
      container instance (similar to the ``root`` user). This parameter maps to
      ``Privileged`` in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--privileged`` option to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ .

    - **ulimits** *(list) --*

      A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits`` in
      the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--ulimit``
      option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

      - *(dict) --*

        The ``ulimit`` settings to pass to the container.

        - **hardLimit** *(integer) --*

          The hard limit for the ``ulimit`` type.

        - **name** *(string) --*

          The ``type`` of the ``ulimit`` .

        - **softLimit** *(integer) --*

          The soft limit for the ``ulimit`` type.

    - **user** *(string) --*

      The user name to use inside the container. This parameter maps to ``User`` in the
      `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
      section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and
      the ``--user`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__
      .

    - **instanceType** *(string) --*

      The instance type to use for a multi-node parallel job. Currently all node groups in a
      multi-node parallel job must use the same instance type. This parameter is not valid
      for single-node container jobs.

    - **resourceRequirements** *(list) --*

      The type and amount of a resource to assign to a container. Currently, the only
      supported resource is ``GPU`` .

      - *(dict) --*

        The type and amount of a resource to assign to a container. Currently, the only
        supported resource type is ``GPU`` .

        - **value** *(string) --*

          The number of physical GPUs to reserve for the container. The number of GPUs
          reserved for all containers in a job should not exceed the number of available GPUs
          on the compute resource that the job is launched on.

        - **type** *(string) --*

          The type of resource to assign to a container. Currently, the only supported
          resource type is ``GPU`` .

    - **linuxParameters** *(dict) --*

      Linux-specific modifications that are applied to the container, such as details for
      device mappings.

      - **devices** *(list) --*

        Any host devices to expose to the container. This parameter maps to ``Devices`` in
        the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--device`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__
        .

        - *(dict) --*

          An object representing a container instance host device.

          - **hostPath** *(string) --*

            The path for the device on the host container instance.

          - **containerPath** *(string) --*

            The path inside the container at which to expose the host device. By default the
            ``hostPath`` value is used.

          - **permissions** *(list) --*

            The explicit permissions to provide to the container for the device. By default,
            the container has permissions for ``read`` , ``write`` , and ``mknod`` for the
            device.

            - *(string) --*
    """


_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef
):
    """
    Type definition for `ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainer` `environment`

    A key-value pair object.

    - **name** *(string) --*

      The name of the key-value pair. For environment variables, this is the name
      of the environment variable.

    - **value** *(string) --*

      The value of the key-value pair. For environment variables, this is the value
      of the environment variable.
    """


_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef",
    {"hostPath": str, "containerPath": str, "permissions": List[str]},
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef
):
    """
    Type definition for `ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParameters` `devices`

    An object representing a container instance host device.

    - **hostPath** *(string) --*

      The path for the device on the host container instance.

    - **containerPath** *(string) --*

      The path inside the container at which to expose the host device. By
      default the ``hostPath`` value is used.

    - **permissions** *(list) --*

      The explicit permissions to provide to the container for the device. By
      default, the container has permissions for ``read`` , ``write`` , and
      ``mknod`` for the device.

      - *(string) --*
    """


_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef",
    {
        "devices": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef
        ]
    },
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef
):
    """
    Type definition for `ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainer` `linuxParameters`

    Linux-specific modifications that are applied to the container, such as details
    for device mappings.

    - **devices** *(list) --*

      Any host devices to expose to the container. This parameter maps to ``Devices``
      in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of
      the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--device`` option to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ .

      - *(dict) --*

        An object representing a container instance host device.

        - **hostPath** *(string) --*

          The path for the device on the host container instance.

        - **containerPath** *(string) --*

          The path inside the container at which to expose the host device. By
          default the ``hostPath`` value is used.

        - **permissions** *(list) --*

          The explicit permissions to provide to the container for the device. By
          default, the container has permissions for ``read`` , ``write`` , and
          ``mknod`` for the device.

          - *(string) --*
    """


_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef",
    {"containerPath": str, "readOnly": bool, "sourceVolume": str},
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef
):
    """
    Type definition for `ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainer` `mountPoints`

    Details on a Docker volume mount point that is used in a job's container
    properties. This parameter maps to ``Volumes`` in the `Create a container
    <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
    section of the Docker Remote API and the ``--volume`` option to docker run.

    - **containerPath** *(string) --*

      The path on the container at which to mount the host volume.

    - **readOnly** *(boolean) --*

      If this value is ``true`` , the container has read-only access to the volume;
      otherwise, the container can write to the volume. The default value is
      ``false`` .

    - **sourceVolume** *(string) --*

      The name of the volume to mount.
    """


_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef",
    {"value": str, "type": str},
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef
):
    """
    Type definition for `ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainer` `resourceRequirements`

    The type and amount of a resource to assign to a container. Currently, the only
    supported resource type is ``GPU`` .

    - **value** *(string) --*

      The number of physical GPUs to reserve for the container. The number of GPUs
      reserved for all containers in a job should not exceed the number of
      available GPUs on the compute resource that the job is launched on.

    - **type** *(string) --*

      The type of resource to assign to a container. Currently, the only supported
      resource type is ``GPU`` .
    """


_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef",
    {"hardLimit": int, "name": str, "softLimit": int},
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef
):
    """
    Type definition for `ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainer` `ulimits`

    The ``ulimit`` settings to pass to the container.

    - **hardLimit** *(integer) --*

      The hard limit for the ``ulimit`` type.

    - **name** *(string) --*

      The ``type`` of the ``ulimit`` .

    - **softLimit** *(integer) --*

      The soft limit for the ``ulimit`` type.
    """


_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef",
    {"sourcePath": str},
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef
):
    """
    Type definition for `ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumes` `host`

    The contents of the ``host`` parameter determine whether your data volume
    persists on the host container instance and where it is stored. If the host
    parameter is empty, then the Docker daemon assigns a host path for your data
    volume. However, the data is not guaranteed to persist after the containers
    associated with it stop running.

    - **sourcePath** *(string) --*

      The path on the host container instance that is presented to the container.
      If this parameter is empty, then the Docker daemon has assigned a host path
      for you. If this parameter contains a file location, then the data volume
      persists at the specified location on the host container instance until you
      delete it manually. If the source path location does not exist on the host
      container instance, the Docker daemon creates it. If the location does
      exist, the contents of the source path folder are exported.
    """


_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumesTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumesTypeDef",
    {
        "host": ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef,
        "name": str,
    },
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumesTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumesTypeDef
):
    """
    Type definition for `ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainer` `volumes`

    A data volume used in a job's container properties.

    - **host** *(dict) --*

      The contents of the ``host`` parameter determine whether your data volume
      persists on the host container instance and where it is stored. If the host
      parameter is empty, then the Docker daemon assigns a host path for your data
      volume. However, the data is not guaranteed to persist after the containers
      associated with it stop running.

      - **sourcePath** *(string) --*

        The path on the host container instance that is presented to the container.
        If this parameter is empty, then the Docker daemon has assigned a host path
        for you. If this parameter contains a file location, then the data volume
        persists at the specified location on the host container instance until you
        delete it manually. If the source path location does not exist on the host
        container instance, the Docker daemon creates it. If the location does
        exist, the contents of the source path folder are exported.

    - **name** *(string) --*

      The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
      hyphens, and underscores are allowed. This name is referenced in the
      ``sourceVolume`` parameter of container definition ``mountPoints`` .
    """


_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerTypeDef",
    {
        "image": str,
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "jobRoleArn": str,
        "volumes": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumesTypeDef
        ],
        "environment": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef
        ],
        "mountPoints": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef
        ],
        "readonlyRootFilesystem": bool,
        "privileged": bool,
        "ulimits": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef
        ],
        "user": str,
        "instanceType": str,
        "resourceRequirements": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef
        ],
        "linuxParameters": ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef,
    },
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerTypeDef
):
    """
    Type definition for `ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangeProperties` `container`

    The container details for the node range.

    - **image** *(string) --*

      The image used to start a container. This string is passed directly to the Docker
      daemon. Images in the Docker Hub registry are available by default. Other
      repositories are specified with `` *repository-url* /*image* :*tag* `` . Up to
      255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons,
      periods, forward slashes, and number signs are allowed. This parameter maps to
      ``Image`` in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``IMAGE`` parameter of `docker run
      <https://docs.docker.com/engine/reference/run/>`__ .

      * Images in Amazon ECR repositories use the full registry and repository URI (for
      example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ).

      * Images in official repositories on Docker Hub use a single name (for example,
      ``ubuntu`` or ``mongo`` ).

      * Images in other repositories on Docker Hub are qualified with an organization
      name (for example, ``amazon/amazon-ecs-agent`` ).

      * Images in other online repositories are qualified further by a domain name (for
      example, ``quay.io/assemblyline/ubuntu`` ).

    - **vcpus** *(integer) --*

      The number of vCPUs reserved for the container. This parameter maps to
      ``CpuShares`` in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--cpu-shares`` option to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ . Each vCPU is equivalent to
      1,024 CPU shares. You must specify at least one vCPU.

    - **memory** *(integer) --*

      The hard limit (in MiB) of memory to present to the container. If your container
      attempts to exceed the memory specified here, the container is killed. This
      parameter maps to ``Memory`` in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--memory`` option to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ . You must specify at least 4
      MiB of memory for a job.

      .. note::

        If you are trying to maximize your resource utilization by providing your jobs
        as much memory as possible for a particular instance type, see `Memory
        Management
        <https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`__
        in the *AWS Batch User Guide* .

    - **command** *(list) --*

      The command that is passed to the container. This parameter maps to ``Cmd`` in
      the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``COMMAND`` parameter to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ . For more information, see
      `https\\://docs.docker.com/engine/reference/builder/#cmd
      <https://docs.docker.com/engine/reference/builder/#cmd>`__ .

      - *(string) --*

    - **jobRoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that the container can assume for
      AWS permissions.

    - **volumes** *(list) --*

      A list of data volumes used in a job.

      - *(dict) --*

        A data volume used in a job's container properties.

        - **host** *(dict) --*

          The contents of the ``host`` parameter determine whether your data volume
          persists on the host container instance and where it is stored. If the host
          parameter is empty, then the Docker daemon assigns a host path for your data
          volume. However, the data is not guaranteed to persist after the containers
          associated with it stop running.

          - **sourcePath** *(string) --*

            The path on the host container instance that is presented to the container.
            If this parameter is empty, then the Docker daemon has assigned a host path
            for you. If this parameter contains a file location, then the data volume
            persists at the specified location on the host container instance until you
            delete it manually. If the source path location does not exist on the host
            container instance, the Docker daemon creates it. If the location does
            exist, the contents of the source path folder are exported.

        - **name** *(string) --*

          The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
          hyphens, and underscores are allowed. This name is referenced in the
          ``sourceVolume`` parameter of container definition ``mountPoints`` .

    - **environment** *(list) --*

      The environment variables to pass to a container. This parameter maps to ``Env``
      in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--env`` option to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ .

      .. warning::

        We do not recommend using plaintext environment variables for sensitive
        information, such as credential data.

      .. note::

        Environment variables must not start with ``AWS_BATCH`` ; this naming
        convention is reserved for variables that are set by the AWS Batch service.

      - *(dict) --*

        A key-value pair object.

        - **name** *(string) --*

          The name of the key-value pair. For environment variables, this is the name
          of the environment variable.

        - **value** *(string) --*

          The value of the key-value pair. For environment variables, this is the value
          of the environment variable.

    - **mountPoints** *(list) --*

      The mount points for data volumes in your container. This parameter maps to
      ``Volumes`` in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--volume`` option to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ .

      - *(dict) --*

        Details on a Docker volume mount point that is used in a job's container
        properties. This parameter maps to ``Volumes`` in the `Create a container
        <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
        section of the Docker Remote API and the ``--volume`` option to docker run.

        - **containerPath** *(string) --*

          The path on the container at which to mount the host volume.

        - **readOnly** *(boolean) --*

          If this value is ``true`` , the container has read-only access to the volume;
          otherwise, the container can write to the volume. The default value is
          ``false`` .

        - **sourceVolume** *(string) --*

          The name of the volume to mount.

    - **readonlyRootFilesystem** *(boolean) --*

      When this parameter is true, the container is given read-only access to its root
      file system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--read-only`` option to ``docker run`` .

    - **privileged** *(boolean) --*

      When this parameter is true, the container is given elevated privileges on the
      host container instance (similar to the ``root`` user). This parameter maps to
      ``Privileged`` in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--privileged`` option to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ .

    - **ulimits** *(list) --*

      A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits``
      in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--ulimit`` option to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ .

      - *(dict) --*

        The ``ulimit`` settings to pass to the container.

        - **hardLimit** *(integer) --*

          The hard limit for the ``ulimit`` type.

        - **name** *(string) --*

          The ``type`` of the ``ulimit`` .

        - **softLimit** *(integer) --*

          The soft limit for the ``ulimit`` type.

    - **user** *(string) --*

      The user name to use inside the container. This parameter maps to ``User`` in the
      `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--user`` option to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ .

    - **instanceType** *(string) --*

      The instance type to use for a multi-node parallel job. Currently all node groups
      in a multi-node parallel job must use the same instance type. This parameter is
      not valid for single-node container jobs.

    - **resourceRequirements** *(list) --*

      The type and amount of a resource to assign to a container. Currently, the only
      supported resource is ``GPU`` .

      - *(dict) --*

        The type and amount of a resource to assign to a container. Currently, the only
        supported resource type is ``GPU`` .

        - **value** *(string) --*

          The number of physical GPUs to reserve for the container. The number of GPUs
          reserved for all containers in a job should not exceed the number of
          available GPUs on the compute resource that the job is launched on.

        - **type** *(string) --*

          The type of resource to assign to a container. Currently, the only supported
          resource type is ``GPU`` .

    - **linuxParameters** *(dict) --*

      Linux-specific modifications that are applied to the container, such as details
      for device mappings.

      - **devices** *(list) --*

        Any host devices to expose to the container. This parameter maps to ``Devices``
        in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of
        the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--device`` option to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ .

        - *(dict) --*

          An object representing a container instance host device.

          - **hostPath** *(string) --*

            The path for the device on the host container instance.

          - **containerPath** *(string) --*

            The path inside the container at which to expose the host device. By
            default the ``hostPath`` value is used.

          - **permissions** *(list) --*

            The explicit permissions to provide to the container for the device. By
            default, the container has permissions for ``read`` , ``write`` , and
            ``mknod`` for the device.

            - *(string) --*
    """


_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiesTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiesTypeDef",
    {
        "targetNodes": str,
        "container": ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerTypeDef,
    },
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiesTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiesTypeDef
):
    """
    Type definition for `ClientDescribeJobDefinitionsResponsejobDefinitionsnodeProperties` `nodeRangeProperties`

    An object representing the properties of the node range for a multi-node parallel job.

    - **targetNodes** *(string) --*

      The range of nodes, using node index values. A range of ``0:3`` indicates nodes
      with index values of ``0`` through ``3`` . If the starting range value is omitted
      (``:n`` ), then ``0`` is used to start the range. If the ending range value is
      omitted (``n:`` ), then the highest possible node index is used to end the range.
      Your accumulative node ranges must account for all nodes (0:n). You may nest node
      ranges, for example 0:10 and 4:5, in which case the 4:5 range properties override
      the 0:10 properties.

    - **container** *(dict) --*

      The container details for the node range.

      - **image** *(string) --*

        The image used to start a container. This string is passed directly to the Docker
        daemon. Images in the Docker Hub registry are available by default. Other
        repositories are specified with `` *repository-url* /*image* :*tag* `` . Up to
        255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons,
        periods, forward slashes, and number signs are allowed. This parameter maps to
        ``Image`` in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``IMAGE`` parameter of `docker run
        <https://docs.docker.com/engine/reference/run/>`__ .

        * Images in Amazon ECR repositories use the full registry and repository URI (for
        example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ).

        * Images in official repositories on Docker Hub use a single name (for example,
        ``ubuntu`` or ``mongo`` ).

        * Images in other repositories on Docker Hub are qualified with an organization
        name (for example, ``amazon/amazon-ecs-agent`` ).

        * Images in other online repositories are qualified further by a domain name (for
        example, ``quay.io/assemblyline/ubuntu`` ).

      - **vcpus** *(integer) --*

        The number of vCPUs reserved for the container. This parameter maps to
        ``CpuShares`` in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--cpu-shares`` option to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ . Each vCPU is equivalent to
        1,024 CPU shares. You must specify at least one vCPU.

      - **memory** *(integer) --*

        The hard limit (in MiB) of memory to present to the container. If your container
        attempts to exceed the memory specified here, the container is killed. This
        parameter maps to ``Memory`` in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--memory`` option to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ . You must specify at least 4
        MiB of memory for a job.

        .. note::

          If you are trying to maximize your resource utilization by providing your jobs
          as much memory as possible for a particular instance type, see `Memory
          Management
          <https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`__
          in the *AWS Batch User Guide* .

      - **command** *(list) --*

        The command that is passed to the container. This parameter maps to ``Cmd`` in
        the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``COMMAND`` parameter to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ . For more information, see
        `https\\://docs.docker.com/engine/reference/builder/#cmd
        <https://docs.docker.com/engine/reference/builder/#cmd>`__ .

        - *(string) --*

      - **jobRoleArn** *(string) --*

        The Amazon Resource Name (ARN) of the IAM role that the container can assume for
        AWS permissions.

      - **volumes** *(list) --*

        A list of data volumes used in a job.

        - *(dict) --*

          A data volume used in a job's container properties.

          - **host** *(dict) --*

            The contents of the ``host`` parameter determine whether your data volume
            persists on the host container instance and where it is stored. If the host
            parameter is empty, then the Docker daemon assigns a host path for your data
            volume. However, the data is not guaranteed to persist after the containers
            associated with it stop running.

            - **sourcePath** *(string) --*

              The path on the host container instance that is presented to the container.
              If this parameter is empty, then the Docker daemon has assigned a host path
              for you. If this parameter contains a file location, then the data volume
              persists at the specified location on the host container instance until you
              delete it manually. If the source path location does not exist on the host
              container instance, the Docker daemon creates it. If the location does
              exist, the contents of the source path folder are exported.

          - **name** *(string) --*

            The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
            hyphens, and underscores are allowed. This name is referenced in the
            ``sourceVolume`` parameter of container definition ``mountPoints`` .

      - **environment** *(list) --*

        The environment variables to pass to a container. This parameter maps to ``Env``
        in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--env`` option to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ .

        .. warning::

          We do not recommend using plaintext environment variables for sensitive
          information, such as credential data.

        .. note::

          Environment variables must not start with ``AWS_BATCH`` ; this naming
          convention is reserved for variables that are set by the AWS Batch service.

        - *(dict) --*

          A key-value pair object.

          - **name** *(string) --*

            The name of the key-value pair. For environment variables, this is the name
            of the environment variable.

          - **value** *(string) --*

            The value of the key-value pair. For environment variables, this is the value
            of the environment variable.

      - **mountPoints** *(list) --*

        The mount points for data volumes in your container. This parameter maps to
        ``Volumes`` in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--volume`` option to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ .

        - *(dict) --*

          Details on a Docker volume mount point that is used in a job's container
          properties. This parameter maps to ``Volumes`` in the `Create a container
          <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
          section of the Docker Remote API and the ``--volume`` option to docker run.

          - **containerPath** *(string) --*

            The path on the container at which to mount the host volume.

          - **readOnly** *(boolean) --*

            If this value is ``true`` , the container has read-only access to the volume;
            otherwise, the container can write to the volume. The default value is
            ``false`` .

          - **sourceVolume** *(string) --*

            The name of the volume to mount.

      - **readonlyRootFilesystem** *(boolean) --*

        When this parameter is true, the container is given read-only access to its root
        file system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--read-only`` option to ``docker run`` .

      - **privileged** *(boolean) --*

        When this parameter is true, the container is given elevated privileges on the
        host container instance (similar to the ``root`` user). This parameter maps to
        ``Privileged`` in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--privileged`` option to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ .

      - **ulimits** *(list) --*

        A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits``
        in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--ulimit`` option to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ .

        - *(dict) --*

          The ``ulimit`` settings to pass to the container.

          - **hardLimit** *(integer) --*

            The hard limit for the ``ulimit`` type.

          - **name** *(string) --*

            The ``type`` of the ``ulimit`` .

          - **softLimit** *(integer) --*

            The soft limit for the ``ulimit`` type.

      - **user** *(string) --*

        The user name to use inside the container. This parameter maps to ``User`` in the
        `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--user`` option to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ .

      - **instanceType** *(string) --*

        The instance type to use for a multi-node parallel job. Currently all node groups
        in a multi-node parallel job must use the same instance type. This parameter is
        not valid for single-node container jobs.

      - **resourceRequirements** *(list) --*

        The type and amount of a resource to assign to a container. Currently, the only
        supported resource is ``GPU`` .

        - *(dict) --*

          The type and amount of a resource to assign to a container. Currently, the only
          supported resource type is ``GPU`` .

          - **value** *(string) --*

            The number of physical GPUs to reserve for the container. The number of GPUs
            reserved for all containers in a job should not exceed the number of
            available GPUs on the compute resource that the job is launched on.

          - **type** *(string) --*

            The type of resource to assign to a container. Currently, the only supported
            resource type is ``GPU`` .

      - **linuxParameters** *(dict) --*

        Linux-specific modifications that are applied to the container, such as details
        for device mappings.

        - **devices** *(list) --*

          Any host devices to expose to the container. This parameter maps to ``Devices``
          in the `Create a container
          <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of
          the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
          ``--device`` option to `docker run
          <https://docs.docker.com/engine/reference/run/>`__ .

          - *(dict) --*

            An object representing a container instance host device.

            - **hostPath** *(string) --*

              The path for the device on the host container instance.

            - **containerPath** *(string) --*

              The path inside the container at which to expose the host device. By
              default the ``hostPath`` value is used.

            - **permissions** *(list) --*

              The explicit permissions to provide to the container for the device. By
              default, the container has permissions for ``read`` , ``write`` , and
              ``mknod`` for the device.

              - *(string) --*
    """


_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesTypeDef",
    {
        "numNodes": int,
        "mainNode": int,
        "nodeRangeProperties": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesTypeDef
):
    """
    Type definition for `ClientDescribeJobDefinitionsResponsejobDefinitions` `nodeProperties`

    An object with various properties specific to multi-node parallel jobs.

    - **numNodes** *(integer) --*

      The number of nodes associated with a multi-node parallel job.

    - **mainNode** *(integer) --*

      Specifies the node index for the main node of a multi-node parallel job. This node
      index value must be fewer than the number of nodes.

    - **nodeRangeProperties** *(list) --*

      A list of node ranges and their properties associated with a multi-node parallel job.

      - *(dict) --*

        An object representing the properties of the node range for a multi-node parallel job.

        - **targetNodes** *(string) --*

          The range of nodes, using node index values. A range of ``0:3`` indicates nodes
          with index values of ``0`` through ``3`` . If the starting range value is omitted
          (``:n`` ), then ``0`` is used to start the range. If the ending range value is
          omitted (``n:`` ), then the highest possible node index is used to end the range.
          Your accumulative node ranges must account for all nodes (0:n). You may nest node
          ranges, for example 0:10 and 4:5, in which case the 4:5 range properties override
          the 0:10 properties.

        - **container** *(dict) --*

          The container details for the node range.

          - **image** *(string) --*

            The image used to start a container. This string is passed directly to the Docker
            daemon. Images in the Docker Hub registry are available by default. Other
            repositories are specified with `` *repository-url* /*image* :*tag* `` . Up to
            255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons,
            periods, forward slashes, and number signs are allowed. This parameter maps to
            ``Image`` in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``IMAGE`` parameter of `docker run
            <https://docs.docker.com/engine/reference/run/>`__ .

            * Images in Amazon ECR repositories use the full registry and repository URI (for
            example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ).

            * Images in official repositories on Docker Hub use a single name (for example,
            ``ubuntu`` or ``mongo`` ).

            * Images in other repositories on Docker Hub are qualified with an organization
            name (for example, ``amazon/amazon-ecs-agent`` ).

            * Images in other online repositories are qualified further by a domain name (for
            example, ``quay.io/assemblyline/ubuntu`` ).

          - **vcpus** *(integer) --*

            The number of vCPUs reserved for the container. This parameter maps to
            ``CpuShares`` in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``--cpu-shares`` option to `docker run
            <https://docs.docker.com/engine/reference/run/>`__ . Each vCPU is equivalent to
            1,024 CPU shares. You must specify at least one vCPU.

          - **memory** *(integer) --*

            The hard limit (in MiB) of memory to present to the container. If your container
            attempts to exceed the memory specified here, the container is killed. This
            parameter maps to ``Memory`` in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``--memory`` option to `docker run
            <https://docs.docker.com/engine/reference/run/>`__ . You must specify at least 4
            MiB of memory for a job.

            .. note::

              If you are trying to maximize your resource utilization by providing your jobs
              as much memory as possible for a particular instance type, see `Memory
              Management
              <https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`__
              in the *AWS Batch User Guide* .

          - **command** *(list) --*

            The command that is passed to the container. This parameter maps to ``Cmd`` in
            the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``COMMAND`` parameter to `docker run
            <https://docs.docker.com/engine/reference/run/>`__ . For more information, see
            `https\\://docs.docker.com/engine/reference/builder/#cmd
            <https://docs.docker.com/engine/reference/builder/#cmd>`__ .

            - *(string) --*

          - **jobRoleArn** *(string) --*

            The Amazon Resource Name (ARN) of the IAM role that the container can assume for
            AWS permissions.

          - **volumes** *(list) --*

            A list of data volumes used in a job.

            - *(dict) --*

              A data volume used in a job's container properties.

              - **host** *(dict) --*

                The contents of the ``host`` parameter determine whether your data volume
                persists on the host container instance and where it is stored. If the host
                parameter is empty, then the Docker daemon assigns a host path for your data
                volume. However, the data is not guaranteed to persist after the containers
                associated with it stop running.

                - **sourcePath** *(string) --*

                  The path on the host container instance that is presented to the container.
                  If this parameter is empty, then the Docker daemon has assigned a host path
                  for you. If this parameter contains a file location, then the data volume
                  persists at the specified location on the host container instance until you
                  delete it manually. If the source path location does not exist on the host
                  container instance, the Docker daemon creates it. If the location does
                  exist, the contents of the source path folder are exported.

              - **name** *(string) --*

                The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
                hyphens, and underscores are allowed. This name is referenced in the
                ``sourceVolume`` parameter of container definition ``mountPoints`` .

          - **environment** *(list) --*

            The environment variables to pass to a container. This parameter maps to ``Env``
            in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``--env`` option to `docker run
            <https://docs.docker.com/engine/reference/run/>`__ .

            .. warning::

              We do not recommend using plaintext environment variables for sensitive
              information, such as credential data.

            .. note::

              Environment variables must not start with ``AWS_BATCH`` ; this naming
              convention is reserved for variables that are set by the AWS Batch service.

            - *(dict) --*

              A key-value pair object.

              - **name** *(string) --*

                The name of the key-value pair. For environment variables, this is the name
                of the environment variable.

              - **value** *(string) --*

                The value of the key-value pair. For environment variables, this is the value
                of the environment variable.

          - **mountPoints** *(list) --*

            The mount points for data volumes in your container. This parameter maps to
            ``Volumes`` in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``--volume`` option to `docker run
            <https://docs.docker.com/engine/reference/run/>`__ .

            - *(dict) --*

              Details on a Docker volume mount point that is used in a job's container
              properties. This parameter maps to ``Volumes`` in the `Create a container
              <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
              section of the Docker Remote API and the ``--volume`` option to docker run.

              - **containerPath** *(string) --*

                The path on the container at which to mount the host volume.

              - **readOnly** *(boolean) --*

                If this value is ``true`` , the container has read-only access to the volume;
                otherwise, the container can write to the volume. The default value is
                ``false`` .

              - **sourceVolume** *(string) --*

                The name of the volume to mount.

          - **readonlyRootFilesystem** *(boolean) --*

            When this parameter is true, the container is given read-only access to its root
            file system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``--read-only`` option to ``docker run`` .

          - **privileged** *(boolean) --*

            When this parameter is true, the container is given elevated privileges on the
            host container instance (similar to the ``root`` user). This parameter maps to
            ``Privileged`` in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``--privileged`` option to `docker run
            <https://docs.docker.com/engine/reference/run/>`__ .

          - **ulimits** *(list) --*

            A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits``
            in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``--ulimit`` option to `docker run
            <https://docs.docker.com/engine/reference/run/>`__ .

            - *(dict) --*

              The ``ulimit`` settings to pass to the container.

              - **hardLimit** *(integer) --*

                The hard limit for the ``ulimit`` type.

              - **name** *(string) --*

                The ``type`` of the ``ulimit`` .

              - **softLimit** *(integer) --*

                The soft limit for the ``ulimit`` type.

          - **user** *(string) --*

            The user name to use inside the container. This parameter maps to ``User`` in the
            `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``--user`` option to `docker run
            <https://docs.docker.com/engine/reference/run/>`__ .

          - **instanceType** *(string) --*

            The instance type to use for a multi-node parallel job. Currently all node groups
            in a multi-node parallel job must use the same instance type. This parameter is
            not valid for single-node container jobs.

          - **resourceRequirements** *(list) --*

            The type and amount of a resource to assign to a container. Currently, the only
            supported resource is ``GPU`` .

            - *(dict) --*

              The type and amount of a resource to assign to a container. Currently, the only
              supported resource type is ``GPU`` .

              - **value** *(string) --*

                The number of physical GPUs to reserve for the container. The number of GPUs
                reserved for all containers in a job should not exceed the number of
                available GPUs on the compute resource that the job is launched on.

              - **type** *(string) --*

                The type of resource to assign to a container. Currently, the only supported
                resource type is ``GPU`` .

          - **linuxParameters** *(dict) --*

            Linux-specific modifications that are applied to the container, such as details
            for device mappings.

            - **devices** *(list) --*

              Any host devices to expose to the container. This parameter maps to ``Devices``
              in the `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of
              the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``--device`` option to `docker run
              <https://docs.docker.com/engine/reference/run/>`__ .

              - *(dict) --*

                An object representing a container instance host device.

                - **hostPath** *(string) --*

                  The path for the device on the host container instance.

                - **containerPath** *(string) --*

                  The path inside the container at which to expose the host device. By
                  default the ``hostPath`` value is used.

                - **permissions** *(list) --*

                  The explicit permissions to provide to the container for the device. By
                  default, the container has permissions for ``read`` , ``write`` , and
                  ``mknod`` for the device.

                  - *(string) --*
    """


_ClientDescribeJobDefinitionsResponsejobDefinitionsretryStrategyTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionsretryStrategyTypeDef",
    {"attempts": int},
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionsretryStrategyTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionsretryStrategyTypeDef
):
    """
    Type definition for `ClientDescribeJobDefinitionsResponsejobDefinitions` `retryStrategy`

    The retry strategy to use for failed jobs that are submitted with this job definition.

    - **attempts** *(integer) --*

      The number of times to move a job to the ``RUNNABLE`` status. You may specify between 1
      and 10 attempts. If the value of ``attempts`` is greater than one, the job is retried
      on failure the same number of attempts as the value.
    """


_ClientDescribeJobDefinitionsResponsejobDefinitionstimeoutTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionstimeoutTypeDef",
    {"attemptDurationSeconds": int},
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionstimeoutTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionstimeoutTypeDef
):
    """
    Type definition for `ClientDescribeJobDefinitionsResponsejobDefinitions` `timeout`

    The timeout configuration for jobs that are submitted with this job definition. You can
    specify a timeout duration after which AWS Batch terminates your jobs if they have not
    finished.

    - **attemptDurationSeconds** *(integer) --*

      The time duration in seconds (measured from the job attempt's ``startedAt`` timestamp)
      after which AWS Batch terminates your jobs if they have not finished.
    """


_ClientDescribeJobDefinitionsResponsejobDefinitionsTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionsTypeDef",
    {
        "jobDefinitionName": str,
        "jobDefinitionArn": str,
        "revision": int,
        "status": str,
        "type": str,
        "parameters": Dict[str, str],
        "retryStrategy": ClientDescribeJobDefinitionsResponsejobDefinitionsretryStrategyTypeDef,
        "containerProperties": ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesTypeDef,
        "timeout": ClientDescribeJobDefinitionsResponsejobDefinitionstimeoutTypeDef,
        "nodeProperties": ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesTypeDef,
    },
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionsTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionsTypeDef
):
    """
    Type definition for `ClientDescribeJobDefinitionsResponse` `jobDefinitions`

    An object representing an AWS Batch job definition.

    - **jobDefinitionName** *(string) --*

      The name of the job definition.

    - **jobDefinitionArn** *(string) --*

      The Amazon Resource Name (ARN) for the job definition.

    - **revision** *(integer) --*

      The revision of the job definition.

    - **status** *(string) --*

      The status of the job definition.

    - **type** *(string) --*

      The type of job definition.

    - **parameters** *(dict) --*

      Default parameters or parameter substitution placeholders that are set in the job
      definition. Parameters are specified as a key-value pair mapping. Parameters in a
      ``SubmitJob`` request override any corresponding parameter defaults from the job
      definition. For more information about specifying parameters, see `Job Definition
      Parameters
      <https://docs.aws.amazon.com/batch/latest/userguide/job_definition_parameters.html>`__ in
      the *AWS Batch User Guide* .

      - *(string) --*

        - *(string) --*

    - **retryStrategy** *(dict) --*

      The retry strategy to use for failed jobs that are submitted with this job definition.

      - **attempts** *(integer) --*

        The number of times to move a job to the ``RUNNABLE`` status. You may specify between 1
        and 10 attempts. If the value of ``attempts`` is greater than one, the job is retried
        on failure the same number of attempts as the value.

    - **containerProperties** *(dict) --*

      An object with various properties specific to container-based jobs.

      - **image** *(string) --*

        The image used to start a container. This string is passed directly to the Docker
        daemon. Images in the Docker Hub registry are available by default. Other repositories
        are specified with `` *repository-url* /*image* :*tag* `` . Up to 255 letters
        (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward
        slashes, and number signs are allowed. This parameter maps to ``Image`` in the `Create
        a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section
        of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``IMAGE`` parameter of `docker run <https://docs.docker.com/engine/reference/run/>`__ .

        * Images in Amazon ECR repositories use the full registry and repository URI (for
        example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ).

        * Images in official repositories on Docker Hub use a single name (for example,
        ``ubuntu`` or ``mongo`` ).

        * Images in other repositories on Docker Hub are qualified with an organization name
        (for example, ``amazon/amazon-ecs-agent`` ).

        * Images in other online repositories are qualified further by a domain name (for
        example, ``quay.io/assemblyline/ubuntu`` ).

      - **vcpus** *(integer) --*

        The number of vCPUs reserved for the container. This parameter maps to ``CpuShares`` in
        the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--cpu-shares`` option to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ . Each vCPU is equivalent to 1,024
        CPU shares. You must specify at least one vCPU.

      - **memory** *(integer) --*

        The hard limit (in MiB) of memory to present to the container. If your container
        attempts to exceed the memory specified here, the container is killed. This parameter
        maps to ``Memory`` in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--memory``
        option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . You must
        specify at least 4 MiB of memory for a job.

        .. note::

          If you are trying to maximize your resource utilization by providing your jobs as
          much memory as possible for a particular instance type, see `Memory Management
          <https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`__ in the
          *AWS Batch User Guide* .

      - **command** *(list) --*

        The command that is passed to the container. This parameter maps to ``Cmd`` in the
        `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
        section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and
        the ``COMMAND`` parameter to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ . For more information, see
        `https\\://docs.docker.com/engine/reference/builder/#cmd
        <https://docs.docker.com/engine/reference/builder/#cmd>`__ .

        - *(string) --*

      - **jobRoleArn** *(string) --*

        The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS
        permissions.

      - **volumes** *(list) --*

        A list of data volumes used in a job.

        - *(dict) --*

          A data volume used in a job's container properties.

          - **host** *(dict) --*

            The contents of the ``host`` parameter determine whether your data volume persists
            on the host container instance and where it is stored. If the host parameter is
            empty, then the Docker daemon assigns a host path for your data volume. However,
            the data is not guaranteed to persist after the containers associated with it stop
            running.

            - **sourcePath** *(string) --*

              The path on the host container instance that is presented to the container. If
              this parameter is empty, then the Docker daemon has assigned a host path for you.
              If this parameter contains a file location, then the data volume persists at the
              specified location on the host container instance until you delete it manually.
              If the source path location does not exist on the host container instance, the
              Docker daemon creates it. If the location does exist, the contents of the source
              path folder are exported.

          - **name** *(string) --*

            The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
            hyphens, and underscores are allowed. This name is referenced in the
            ``sourceVolume`` parameter of container definition ``mountPoints`` .

      - **environment** *(list) --*

        The environment variables to pass to a container. This parameter maps to ``Env`` in the
        `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
        section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and
        the ``--env`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

        .. warning::

          We do not recommend using plaintext environment variables for sensitive information,
          such as credential data.

        .. note::

          Environment variables must not start with ``AWS_BATCH`` ; this naming convention is
          reserved for variables that are set by the AWS Batch service.

        - *(dict) --*

          A key-value pair object.

          - **name** *(string) --*

            The name of the key-value pair. For environment variables, this is the name of the
            environment variable.

          - **value** *(string) --*

            The value of the key-value pair. For environment variables, this is the value of
            the environment variable.

      - **mountPoints** *(list) --*

        The mount points for data volumes in your container. This parameter maps to ``Volumes``
        in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--volume``
        option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

        - *(dict) --*

          Details on a Docker volume mount point that is used in a job's container properties.
          This parameter maps to ``Volumes`` in the `Create a container
          <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
          section of the Docker Remote API and the ``--volume`` option to docker run.

          - **containerPath** *(string) --*

            The path on the container at which to mount the host volume.

          - **readOnly** *(boolean) --*

            If this value is ``true`` , the container has read-only access to the volume;
            otherwise, the container can write to the volume. The default value is ``false`` .

          - **sourceVolume** *(string) --*

            The name of the volume to mount.

      - **readonlyRootFilesystem** *(boolean) --*

        When this parameter is true, the container is given read-only access to its root file
        system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--read-only`` option to ``docker run`` .

      - **privileged** *(boolean) --*

        When this parameter is true, the container is given elevated privileges on the host
        container instance (similar to the ``root`` user). This parameter maps to
        ``Privileged`` in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--privileged`` option to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ .

      - **ulimits** *(list) --*

        A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits`` in
        the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--ulimit``
        option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

        - *(dict) --*

          The ``ulimit`` settings to pass to the container.

          - **hardLimit** *(integer) --*

            The hard limit for the ``ulimit`` type.

          - **name** *(string) --*

            The ``type`` of the ``ulimit`` .

          - **softLimit** *(integer) --*

            The soft limit for the ``ulimit`` type.

      - **user** *(string) --*

        The user name to use inside the container. This parameter maps to ``User`` in the
        `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
        section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and
        the ``--user`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__
        .

      - **instanceType** *(string) --*

        The instance type to use for a multi-node parallel job. Currently all node groups in a
        multi-node parallel job must use the same instance type. This parameter is not valid
        for single-node container jobs.

      - **resourceRequirements** *(list) --*

        The type and amount of a resource to assign to a container. Currently, the only
        supported resource is ``GPU`` .

        - *(dict) --*

          The type and amount of a resource to assign to a container. Currently, the only
          supported resource type is ``GPU`` .

          - **value** *(string) --*

            The number of physical GPUs to reserve for the container. The number of GPUs
            reserved for all containers in a job should not exceed the number of available GPUs
            on the compute resource that the job is launched on.

          - **type** *(string) --*

            The type of resource to assign to a container. Currently, the only supported
            resource type is ``GPU`` .

      - **linuxParameters** *(dict) --*

        Linux-specific modifications that are applied to the container, such as details for
        device mappings.

        - **devices** *(list) --*

          Any host devices to expose to the container. This parameter maps to ``Devices`` in
          the `Create a container
          <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
          `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
          ``--device`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__
          .

          - *(dict) --*

            An object representing a container instance host device.

            - **hostPath** *(string) --*

              The path for the device on the host container instance.

            - **containerPath** *(string) --*

              The path inside the container at which to expose the host device. By default the
              ``hostPath`` value is used.

            - **permissions** *(list) --*

              The explicit permissions to provide to the container for the device. By default,
              the container has permissions for ``read`` , ``write`` , and ``mknod`` for the
              device.

              - *(string) --*

    - **timeout** *(dict) --*

      The timeout configuration for jobs that are submitted with this job definition. You can
      specify a timeout duration after which AWS Batch terminates your jobs if they have not
      finished.

      - **attemptDurationSeconds** *(integer) --*

        The time duration in seconds (measured from the job attempt's ``startedAt`` timestamp)
        after which AWS Batch terminates your jobs if they have not finished.

    - **nodeProperties** *(dict) --*

      An object with various properties specific to multi-node parallel jobs.

      - **numNodes** *(integer) --*

        The number of nodes associated with a multi-node parallel job.

      - **mainNode** *(integer) --*

        Specifies the node index for the main node of a multi-node parallel job. This node
        index value must be fewer than the number of nodes.

      - **nodeRangeProperties** *(list) --*

        A list of node ranges and their properties associated with a multi-node parallel job.

        - *(dict) --*

          An object representing the properties of the node range for a multi-node parallel job.

          - **targetNodes** *(string) --*

            The range of nodes, using node index values. A range of ``0:3`` indicates nodes
            with index values of ``0`` through ``3`` . If the starting range value is omitted
            (``:n`` ), then ``0`` is used to start the range. If the ending range value is
            omitted (``n:`` ), then the highest possible node index is used to end the range.
            Your accumulative node ranges must account for all nodes (0:n). You may nest node
            ranges, for example 0:10 and 4:5, in which case the 4:5 range properties override
            the 0:10 properties.

          - **container** *(dict) --*

            The container details for the node range.

            - **image** *(string) --*

              The image used to start a container. This string is passed directly to the Docker
              daemon. Images in the Docker Hub registry are available by default. Other
              repositories are specified with `` *repository-url* /*image* :*tag* `` . Up to
              255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons,
              periods, forward slashes, and number signs are allowed. This parameter maps to
              ``Image`` in the `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
              `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``IMAGE`` parameter of `docker run
              <https://docs.docker.com/engine/reference/run/>`__ .

              * Images in Amazon ECR repositories use the full registry and repository URI (for
              example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ).

              * Images in official repositories on Docker Hub use a single name (for example,
              ``ubuntu`` or ``mongo`` ).

              * Images in other repositories on Docker Hub are qualified with an organization
              name (for example, ``amazon/amazon-ecs-agent`` ).

              * Images in other online repositories are qualified further by a domain name (for
              example, ``quay.io/assemblyline/ubuntu`` ).

            - **vcpus** *(integer) --*

              The number of vCPUs reserved for the container. This parameter maps to
              ``CpuShares`` in the `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
              `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``--cpu-shares`` option to `docker run
              <https://docs.docker.com/engine/reference/run/>`__ . Each vCPU is equivalent to
              1,024 CPU shares. You must specify at least one vCPU.

            - **memory** *(integer) --*

              The hard limit (in MiB) of memory to present to the container. If your container
              attempts to exceed the memory specified here, the container is killed. This
              parameter maps to ``Memory`` in the `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
              `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``--memory`` option to `docker run
              <https://docs.docker.com/engine/reference/run/>`__ . You must specify at least 4
              MiB of memory for a job.

              .. note::

                If you are trying to maximize your resource utilization by providing your jobs
                as much memory as possible for a particular instance type, see `Memory
                Management
                <https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`__
                in the *AWS Batch User Guide* .

            - **command** *(list) --*

              The command that is passed to the container. This parameter maps to ``Cmd`` in
              the `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
              `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``COMMAND`` parameter to `docker run
              <https://docs.docker.com/engine/reference/run/>`__ . For more information, see
              `https\\://docs.docker.com/engine/reference/builder/#cmd
              <https://docs.docker.com/engine/reference/builder/#cmd>`__ .

              - *(string) --*

            - **jobRoleArn** *(string) --*

              The Amazon Resource Name (ARN) of the IAM role that the container can assume for
              AWS permissions.

            - **volumes** *(list) --*

              A list of data volumes used in a job.

              - *(dict) --*

                A data volume used in a job's container properties.

                - **host** *(dict) --*

                  The contents of the ``host`` parameter determine whether your data volume
                  persists on the host container instance and where it is stored. If the host
                  parameter is empty, then the Docker daemon assigns a host path for your data
                  volume. However, the data is not guaranteed to persist after the containers
                  associated with it stop running.

                  - **sourcePath** *(string) --*

                    The path on the host container instance that is presented to the container.
                    If this parameter is empty, then the Docker daemon has assigned a host path
                    for you. If this parameter contains a file location, then the data volume
                    persists at the specified location on the host container instance until you
                    delete it manually. If the source path location does not exist on the host
                    container instance, the Docker daemon creates it. If the location does
                    exist, the contents of the source path folder are exported.

                - **name** *(string) --*

                  The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
                  hyphens, and underscores are allowed. This name is referenced in the
                  ``sourceVolume`` parameter of container definition ``mountPoints`` .

            - **environment** *(list) --*

              The environment variables to pass to a container. This parameter maps to ``Env``
              in the `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
              `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``--env`` option to `docker run
              <https://docs.docker.com/engine/reference/run/>`__ .

              .. warning::

                We do not recommend using plaintext environment variables for sensitive
                information, such as credential data.

              .. note::

                Environment variables must not start with ``AWS_BATCH`` ; this naming
                convention is reserved for variables that are set by the AWS Batch service.

              - *(dict) --*

                A key-value pair object.

                - **name** *(string) --*

                  The name of the key-value pair. For environment variables, this is the name
                  of the environment variable.

                - **value** *(string) --*

                  The value of the key-value pair. For environment variables, this is the value
                  of the environment variable.

            - **mountPoints** *(list) --*

              The mount points for data volumes in your container. This parameter maps to
              ``Volumes`` in the `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
              `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``--volume`` option to `docker run
              <https://docs.docker.com/engine/reference/run/>`__ .

              - *(dict) --*

                Details on a Docker volume mount point that is used in a job's container
                properties. This parameter maps to ``Volumes`` in the `Create a container
                <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
                section of the Docker Remote API and the ``--volume`` option to docker run.

                - **containerPath** *(string) --*

                  The path on the container at which to mount the host volume.

                - **readOnly** *(boolean) --*

                  If this value is ``true`` , the container has read-only access to the volume;
                  otherwise, the container can write to the volume. The default value is
                  ``false`` .

                - **sourceVolume** *(string) --*

                  The name of the volume to mount.

            - **readonlyRootFilesystem** *(boolean) --*

              When this parameter is true, the container is given read-only access to its root
              file system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
              `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``--read-only`` option to ``docker run`` .

            - **privileged** *(boolean) --*

              When this parameter is true, the container is given elevated privileges on the
              host container instance (similar to the ``root`` user). This parameter maps to
              ``Privileged`` in the `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
              `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``--privileged`` option to `docker run
              <https://docs.docker.com/engine/reference/run/>`__ .

            - **ulimits** *(list) --*

              A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits``
              in the `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
              `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``--ulimit`` option to `docker run
              <https://docs.docker.com/engine/reference/run/>`__ .

              - *(dict) --*

                The ``ulimit`` settings to pass to the container.

                - **hardLimit** *(integer) --*

                  The hard limit for the ``ulimit`` type.

                - **name** *(string) --*

                  The ``type`` of the ``ulimit`` .

                - **softLimit** *(integer) --*

                  The soft limit for the ``ulimit`` type.

            - **user** *(string) --*

              The user name to use inside the container. This parameter maps to ``User`` in the
              `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
              `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``--user`` option to `docker run
              <https://docs.docker.com/engine/reference/run/>`__ .

            - **instanceType** *(string) --*

              The instance type to use for a multi-node parallel job. Currently all node groups
              in a multi-node parallel job must use the same instance type. This parameter is
              not valid for single-node container jobs.

            - **resourceRequirements** *(list) --*

              The type and amount of a resource to assign to a container. Currently, the only
              supported resource is ``GPU`` .

              - *(dict) --*

                The type and amount of a resource to assign to a container. Currently, the only
                supported resource type is ``GPU`` .

                - **value** *(string) --*

                  The number of physical GPUs to reserve for the container. The number of GPUs
                  reserved for all containers in a job should not exceed the number of
                  available GPUs on the compute resource that the job is launched on.

                - **type** *(string) --*

                  The type of resource to assign to a container. Currently, the only supported
                  resource type is ``GPU`` .

            - **linuxParameters** *(dict) --*

              Linux-specific modifications that are applied to the container, such as details
              for device mappings.

              - **devices** *(list) --*

                Any host devices to expose to the container. This parameter maps to ``Devices``
                in the `Create a container
                <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of
                the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                ``--device`` option to `docker run
                <https://docs.docker.com/engine/reference/run/>`__ .

                - *(dict) --*

                  An object representing a container instance host device.

                  - **hostPath** *(string) --*

                    The path for the device on the host container instance.

                  - **containerPath** *(string) --*

                    The path inside the container at which to expose the host device. By
                    default the ``hostPath`` value is used.

                  - **permissions** *(list) --*

                    The explicit permissions to provide to the container for the device. By
                    default, the container has permissions for ``read`` , ``write`` , and
                    ``mknod`` for the device.

                    - *(string) --*
    """


_ClientDescribeJobDefinitionsResponseTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponseTypeDef",
    {
        "jobDefinitions": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeJobDefinitionsResponseTypeDef(
    _ClientDescribeJobDefinitionsResponseTypeDef
):
    """
    Type definition for `ClientDescribeJobDefinitions` `Response`

    - **jobDefinitions** *(list) --*

      The list of job definitions.

      - *(dict) --*

        An object representing an AWS Batch job definition.

        - **jobDefinitionName** *(string) --*

          The name of the job definition.

        - **jobDefinitionArn** *(string) --*

          The Amazon Resource Name (ARN) for the job definition.

        - **revision** *(integer) --*

          The revision of the job definition.

        - **status** *(string) --*

          The status of the job definition.

        - **type** *(string) --*

          The type of job definition.

        - **parameters** *(dict) --*

          Default parameters or parameter substitution placeholders that are set in the job
          definition. Parameters are specified as a key-value pair mapping. Parameters in a
          ``SubmitJob`` request override any corresponding parameter defaults from the job
          definition. For more information about specifying parameters, see `Job Definition
          Parameters
          <https://docs.aws.amazon.com/batch/latest/userguide/job_definition_parameters.html>`__ in
          the *AWS Batch User Guide* .

          - *(string) --*

            - *(string) --*

        - **retryStrategy** *(dict) --*

          The retry strategy to use for failed jobs that are submitted with this job definition.

          - **attempts** *(integer) --*

            The number of times to move a job to the ``RUNNABLE`` status. You may specify between 1
            and 10 attempts. If the value of ``attempts`` is greater than one, the job is retried
            on failure the same number of attempts as the value.

        - **containerProperties** *(dict) --*

          An object with various properties specific to container-based jobs.

          - **image** *(string) --*

            The image used to start a container. This string is passed directly to the Docker
            daemon. Images in the Docker Hub registry are available by default. Other repositories
            are specified with `` *repository-url* /*image* :*tag* `` . Up to 255 letters
            (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward
            slashes, and number signs are allowed. This parameter maps to ``Image`` in the `Create
            a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section
            of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``IMAGE`` parameter of `docker run <https://docs.docker.com/engine/reference/run/>`__ .

            * Images in Amazon ECR repositories use the full registry and repository URI (for
            example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ).

            * Images in official repositories on Docker Hub use a single name (for example,
            ``ubuntu`` or ``mongo`` ).

            * Images in other repositories on Docker Hub are qualified with an organization name
            (for example, ``amazon/amazon-ecs-agent`` ).

            * Images in other online repositories are qualified further by a domain name (for
            example, ``quay.io/assemblyline/ubuntu`` ).

          - **vcpus** *(integer) --*

            The number of vCPUs reserved for the container. This parameter maps to ``CpuShares`` in
            the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``--cpu-shares`` option to `docker run
            <https://docs.docker.com/engine/reference/run/>`__ . Each vCPU is equivalent to 1,024
            CPU shares. You must specify at least one vCPU.

          - **memory** *(integer) --*

            The hard limit (in MiB) of memory to present to the container. If your container
            attempts to exceed the memory specified here, the container is killed. This parameter
            maps to ``Memory`` in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--memory``
            option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . You must
            specify at least 4 MiB of memory for a job.

            .. note::

              If you are trying to maximize your resource utilization by providing your jobs as
              much memory as possible for a particular instance type, see `Memory Management
              <https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`__ in the
              *AWS Batch User Guide* .

          - **command** *(list) --*

            The command that is passed to the container. This parameter maps to ``Cmd`` in the
            `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
            section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and
            the ``COMMAND`` parameter to `docker run
            <https://docs.docker.com/engine/reference/run/>`__ . For more information, see
            `https\\://docs.docker.com/engine/reference/builder/#cmd
            <https://docs.docker.com/engine/reference/builder/#cmd>`__ .

            - *(string) --*

          - **jobRoleArn** *(string) --*

            The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS
            permissions.

          - **volumes** *(list) --*

            A list of data volumes used in a job.

            - *(dict) --*

              A data volume used in a job's container properties.

              - **host** *(dict) --*

                The contents of the ``host`` parameter determine whether your data volume persists
                on the host container instance and where it is stored. If the host parameter is
                empty, then the Docker daemon assigns a host path for your data volume. However,
                the data is not guaranteed to persist after the containers associated with it stop
                running.

                - **sourcePath** *(string) --*

                  The path on the host container instance that is presented to the container. If
                  this parameter is empty, then the Docker daemon has assigned a host path for you.
                  If this parameter contains a file location, then the data volume persists at the
                  specified location on the host container instance until you delete it manually.
                  If the source path location does not exist on the host container instance, the
                  Docker daemon creates it. If the location does exist, the contents of the source
                  path folder are exported.

              - **name** *(string) --*

                The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
                hyphens, and underscores are allowed. This name is referenced in the
                ``sourceVolume`` parameter of container definition ``mountPoints`` .

          - **environment** *(list) --*

            The environment variables to pass to a container. This parameter maps to ``Env`` in the
            `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
            section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and
            the ``--env`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

            .. warning::

              We do not recommend using plaintext environment variables for sensitive information,
              such as credential data.

            .. note::

              Environment variables must not start with ``AWS_BATCH`` ; this naming convention is
              reserved for variables that are set by the AWS Batch service.

            - *(dict) --*

              A key-value pair object.

              - **name** *(string) --*

                The name of the key-value pair. For environment variables, this is the name of the
                environment variable.

              - **value** *(string) --*

                The value of the key-value pair. For environment variables, this is the value of
                the environment variable.

          - **mountPoints** *(list) --*

            The mount points for data volumes in your container. This parameter maps to ``Volumes``
            in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--volume``
            option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

            - *(dict) --*

              Details on a Docker volume mount point that is used in a job's container properties.
              This parameter maps to ``Volumes`` in the `Create a container
              <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
              section of the Docker Remote API and the ``--volume`` option to docker run.

              - **containerPath** *(string) --*

                The path on the container at which to mount the host volume.

              - **readOnly** *(boolean) --*

                If this value is ``true`` , the container has read-only access to the volume;
                otherwise, the container can write to the volume. The default value is ``false`` .

              - **sourceVolume** *(string) --*

                The name of the volume to mount.

          - **readonlyRootFilesystem** *(boolean) --*

            When this parameter is true, the container is given read-only access to its root file
            system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``--read-only`` option to ``docker run`` .

          - **privileged** *(boolean) --*

            When this parameter is true, the container is given elevated privileges on the host
            container instance (similar to the ``root`` user). This parameter maps to
            ``Privileged`` in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``--privileged`` option to `docker run
            <https://docs.docker.com/engine/reference/run/>`__ .

          - **ulimits** *(list) --*

            A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits`` in
            the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--ulimit``
            option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

            - *(dict) --*

              The ``ulimit`` settings to pass to the container.

              - **hardLimit** *(integer) --*

                The hard limit for the ``ulimit`` type.

              - **name** *(string) --*

                The ``type`` of the ``ulimit`` .

              - **softLimit** *(integer) --*

                The soft limit for the ``ulimit`` type.

          - **user** *(string) --*

            The user name to use inside the container. This parameter maps to ``User`` in the
            `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
            section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and
            the ``--user`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__
            .

          - **instanceType** *(string) --*

            The instance type to use for a multi-node parallel job. Currently all node groups in a
            multi-node parallel job must use the same instance type. This parameter is not valid
            for single-node container jobs.

          - **resourceRequirements** *(list) --*

            The type and amount of a resource to assign to a container. Currently, the only
            supported resource is ``GPU`` .

            - *(dict) --*

              The type and amount of a resource to assign to a container. Currently, the only
              supported resource type is ``GPU`` .

              - **value** *(string) --*

                The number of physical GPUs to reserve for the container. The number of GPUs
                reserved for all containers in a job should not exceed the number of available GPUs
                on the compute resource that the job is launched on.

              - **type** *(string) --*

                The type of resource to assign to a container. Currently, the only supported
                resource type is ``GPU`` .

          - **linuxParameters** *(dict) --*

            Linux-specific modifications that are applied to the container, such as details for
            device mappings.

            - **devices** *(list) --*

              Any host devices to expose to the container. This parameter maps to ``Devices`` in
              the `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
              `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``--device`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__
              .

              - *(dict) --*

                An object representing a container instance host device.

                - **hostPath** *(string) --*

                  The path for the device on the host container instance.

                - **containerPath** *(string) --*

                  The path inside the container at which to expose the host device. By default the
                  ``hostPath`` value is used.

                - **permissions** *(list) --*

                  The explicit permissions to provide to the container for the device. By default,
                  the container has permissions for ``read`` , ``write`` , and ``mknod`` for the
                  device.

                  - *(string) --*

        - **timeout** *(dict) --*

          The timeout configuration for jobs that are submitted with this job definition. You can
          specify a timeout duration after which AWS Batch terminates your jobs if they have not
          finished.

          - **attemptDurationSeconds** *(integer) --*

            The time duration in seconds (measured from the job attempt's ``startedAt`` timestamp)
            after which AWS Batch terminates your jobs if they have not finished.

        - **nodeProperties** *(dict) --*

          An object with various properties specific to multi-node parallel jobs.

          - **numNodes** *(integer) --*

            The number of nodes associated with a multi-node parallel job.

          - **mainNode** *(integer) --*

            Specifies the node index for the main node of a multi-node parallel job. This node
            index value must be fewer than the number of nodes.

          - **nodeRangeProperties** *(list) --*

            A list of node ranges and their properties associated with a multi-node parallel job.

            - *(dict) --*

              An object representing the properties of the node range for a multi-node parallel job.

              - **targetNodes** *(string) --*

                The range of nodes, using node index values. A range of ``0:3`` indicates nodes
                with index values of ``0`` through ``3`` . If the starting range value is omitted
                (``:n`` ), then ``0`` is used to start the range. If the ending range value is
                omitted (``n:`` ), then the highest possible node index is used to end the range.
                Your accumulative node ranges must account for all nodes (0:n). You may nest node
                ranges, for example 0:10 and 4:5, in which case the 4:5 range properties override
                the 0:10 properties.

              - **container** *(dict) --*

                The container details for the node range.

                - **image** *(string) --*

                  The image used to start a container. This string is passed directly to the Docker
                  daemon. Images in the Docker Hub registry are available by default. Other
                  repositories are specified with `` *repository-url* /*image* :*tag* `` . Up to
                  255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons,
                  periods, forward slashes, and number signs are allowed. This parameter maps to
                  ``Image`` in the `Create a container
                  <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
                  `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                  ``IMAGE`` parameter of `docker run
                  <https://docs.docker.com/engine/reference/run/>`__ .

                  * Images in Amazon ECR repositories use the full registry and repository URI (for
                  example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ).

                  * Images in official repositories on Docker Hub use a single name (for example,
                  ``ubuntu`` or ``mongo`` ).

                  * Images in other repositories on Docker Hub are qualified with an organization
                  name (for example, ``amazon/amazon-ecs-agent`` ).

                  * Images in other online repositories are qualified further by a domain name (for
                  example, ``quay.io/assemblyline/ubuntu`` ).

                - **vcpus** *(integer) --*

                  The number of vCPUs reserved for the container. This parameter maps to
                  ``CpuShares`` in the `Create a container
                  <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
                  `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                  ``--cpu-shares`` option to `docker run
                  <https://docs.docker.com/engine/reference/run/>`__ . Each vCPU is equivalent to
                  1,024 CPU shares. You must specify at least one vCPU.

                - **memory** *(integer) --*

                  The hard limit (in MiB) of memory to present to the container. If your container
                  attempts to exceed the memory specified here, the container is killed. This
                  parameter maps to ``Memory`` in the `Create a container
                  <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
                  `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                  ``--memory`` option to `docker run
                  <https://docs.docker.com/engine/reference/run/>`__ . You must specify at least 4
                  MiB of memory for a job.

                  .. note::

                    If you are trying to maximize your resource utilization by providing your jobs
                    as much memory as possible for a particular instance type, see `Memory
                    Management
                    <https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`__
                    in the *AWS Batch User Guide* .

                - **command** *(list) --*

                  The command that is passed to the container. This parameter maps to ``Cmd`` in
                  the `Create a container
                  <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
                  `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                  ``COMMAND`` parameter to `docker run
                  <https://docs.docker.com/engine/reference/run/>`__ . For more information, see
                  `https\\://docs.docker.com/engine/reference/builder/#cmd
                  <https://docs.docker.com/engine/reference/builder/#cmd>`__ .

                  - *(string) --*

                - **jobRoleArn** *(string) --*

                  The Amazon Resource Name (ARN) of the IAM role that the container can assume for
                  AWS permissions.

                - **volumes** *(list) --*

                  A list of data volumes used in a job.

                  - *(dict) --*

                    A data volume used in a job's container properties.

                    - **host** *(dict) --*

                      The contents of the ``host`` parameter determine whether your data volume
                      persists on the host container instance and where it is stored. If the host
                      parameter is empty, then the Docker daemon assigns a host path for your data
                      volume. However, the data is not guaranteed to persist after the containers
                      associated with it stop running.

                      - **sourcePath** *(string) --*

                        The path on the host container instance that is presented to the container.
                        If this parameter is empty, then the Docker daemon has assigned a host path
                        for you. If this parameter contains a file location, then the data volume
                        persists at the specified location on the host container instance until you
                        delete it manually. If the source path location does not exist on the host
                        container instance, the Docker daemon creates it. If the location does
                        exist, the contents of the source path folder are exported.

                    - **name** *(string) --*

                      The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
                      hyphens, and underscores are allowed. This name is referenced in the
                      ``sourceVolume`` parameter of container definition ``mountPoints`` .

                - **environment** *(list) --*

                  The environment variables to pass to a container. This parameter maps to ``Env``
                  in the `Create a container
                  <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
                  `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                  ``--env`` option to `docker run
                  <https://docs.docker.com/engine/reference/run/>`__ .

                  .. warning::

                    We do not recommend using plaintext environment variables for sensitive
                    information, such as credential data.

                  .. note::

                    Environment variables must not start with ``AWS_BATCH`` ; this naming
                    convention is reserved for variables that are set by the AWS Batch service.

                  - *(dict) --*

                    A key-value pair object.

                    - **name** *(string) --*

                      The name of the key-value pair. For environment variables, this is the name
                      of the environment variable.

                    - **value** *(string) --*

                      The value of the key-value pair. For environment variables, this is the value
                      of the environment variable.

                - **mountPoints** *(list) --*

                  The mount points for data volumes in your container. This parameter maps to
                  ``Volumes`` in the `Create a container
                  <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
                  `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                  ``--volume`` option to `docker run
                  <https://docs.docker.com/engine/reference/run/>`__ .

                  - *(dict) --*

                    Details on a Docker volume mount point that is used in a job's container
                    properties. This parameter maps to ``Volumes`` in the `Create a container
                    <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
                    section of the Docker Remote API and the ``--volume`` option to docker run.

                    - **containerPath** *(string) --*

                      The path on the container at which to mount the host volume.

                    - **readOnly** *(boolean) --*

                      If this value is ``true`` , the container has read-only access to the volume;
                      otherwise, the container can write to the volume. The default value is
                      ``false`` .

                    - **sourceVolume** *(string) --*

                      The name of the volume to mount.

                - **readonlyRootFilesystem** *(boolean) --*

                  When this parameter is true, the container is given read-only access to its root
                  file system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container
                  <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
                  `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                  ``--read-only`` option to ``docker run`` .

                - **privileged** *(boolean) --*

                  When this parameter is true, the container is given elevated privileges on the
                  host container instance (similar to the ``root`` user). This parameter maps to
                  ``Privileged`` in the `Create a container
                  <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
                  `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                  ``--privileged`` option to `docker run
                  <https://docs.docker.com/engine/reference/run/>`__ .

                - **ulimits** *(list) --*

                  A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits``
                  in the `Create a container
                  <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
                  `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                  ``--ulimit`` option to `docker run
                  <https://docs.docker.com/engine/reference/run/>`__ .

                  - *(dict) --*

                    The ``ulimit`` settings to pass to the container.

                    - **hardLimit** *(integer) --*

                      The hard limit for the ``ulimit`` type.

                    - **name** *(string) --*

                      The ``type`` of the ``ulimit`` .

                    - **softLimit** *(integer) --*

                      The soft limit for the ``ulimit`` type.

                - **user** *(string) --*

                  The user name to use inside the container. This parameter maps to ``User`` in the
                  `Create a container
                  <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
                  `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                  ``--user`` option to `docker run
                  <https://docs.docker.com/engine/reference/run/>`__ .

                - **instanceType** *(string) --*

                  The instance type to use for a multi-node parallel job. Currently all node groups
                  in a multi-node parallel job must use the same instance type. This parameter is
                  not valid for single-node container jobs.

                - **resourceRequirements** *(list) --*

                  The type and amount of a resource to assign to a container. Currently, the only
                  supported resource is ``GPU`` .

                  - *(dict) --*

                    The type and amount of a resource to assign to a container. Currently, the only
                    supported resource type is ``GPU`` .

                    - **value** *(string) --*

                      The number of physical GPUs to reserve for the container. The number of GPUs
                      reserved for all containers in a job should not exceed the number of
                      available GPUs on the compute resource that the job is launched on.

                    - **type** *(string) --*

                      The type of resource to assign to a container. Currently, the only supported
                      resource type is ``GPU`` .

                - **linuxParameters** *(dict) --*

                  Linux-specific modifications that are applied to the container, such as details
                  for device mappings.

                  - **devices** *(list) --*

                    Any host devices to expose to the container. This parameter maps to ``Devices``
                    in the `Create a container
                    <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of
                    the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                    ``--device`` option to `docker run
                    <https://docs.docker.com/engine/reference/run/>`__ .

                    - *(dict) --*

                      An object representing a container instance host device.

                      - **hostPath** *(string) --*

                        The path for the device on the host container instance.

                      - **containerPath** *(string) --*

                        The path inside the container at which to expose the host device. By
                        default the ``hostPath`` value is used.

                      - **permissions** *(list) --*

                        The explicit permissions to provide to the container for the device. By
                        default, the container has permissions for ``read`` , ``write`` , and
                        ``mknod`` for the device.

                        - *(string) --*

    - **nextToken** *(string) --*

      The ``nextToken`` value to include in a future ``DescribeJobDefinitions`` request. When the
      results of a ``DescribeJobDefinitions`` request exceed ``maxResults`` , this value can be
      used to retrieve the next page of results. This value is ``null`` when there are no more
      results to return.
    """


_ClientDescribeJobQueuesResponsejobQueuescomputeEnvironmentOrderTypeDef = TypedDict(
    "_ClientDescribeJobQueuesResponsejobQueuescomputeEnvironmentOrderTypeDef",
    {"order": int, "computeEnvironment": str},
    total=False,
)


class ClientDescribeJobQueuesResponsejobQueuescomputeEnvironmentOrderTypeDef(
    _ClientDescribeJobQueuesResponsejobQueuescomputeEnvironmentOrderTypeDef
):
    """
    Type definition for `ClientDescribeJobQueuesResponsejobQueues` `computeEnvironmentOrder`

    The order in which compute environments are tried for job placement within a queue.
    Compute environments are tried in ascending order. For example, if two compute
    environments are associated with a job queue, the compute environment with a lower
    order integer value is tried for job placement first.

    - **order** *(integer) --*

      The order of the compute environment.

    - **computeEnvironment** *(string) --*

      The Amazon Resource Name (ARN) of the compute environment.
    """


_ClientDescribeJobQueuesResponsejobQueuesTypeDef = TypedDict(
    "_ClientDescribeJobQueuesResponsejobQueuesTypeDef",
    {
        "jobQueueName": str,
        "jobQueueArn": str,
        "state": str,
        "status": str,
        "statusReason": str,
        "priority": int,
        "computeEnvironmentOrder": List[
            ClientDescribeJobQueuesResponsejobQueuescomputeEnvironmentOrderTypeDef
        ],
    },
    total=False,
)


class ClientDescribeJobQueuesResponsejobQueuesTypeDef(
    _ClientDescribeJobQueuesResponsejobQueuesTypeDef
):
    """
    Type definition for `ClientDescribeJobQueuesResponse` `jobQueues`

    An object representing the details of an AWS Batch job queue.

    - **jobQueueName** *(string) --*

      The name of the job queue.

    - **jobQueueArn** *(string) --*

      The Amazon Resource Name (ARN) of the job queue.

    - **state** *(string) --*

      Describes the ability of the queue to accept new jobs.

    - **status** *(string) --*

      The status of the job queue (for example, ``CREATING`` or ``VALID`` ).

    - **statusReason** *(string) --*

      A short, human-readable string to provide additional details about the current status of
      the job queue.

    - **priority** *(integer) --*

      The priority of the job queue.

    - **computeEnvironmentOrder** *(list) --*

      The compute environments that are attached to the job queue and the order in which job
      placement is preferred. Compute environments are selected for job placement in ascending
      order.

      - *(dict) --*

        The order in which compute environments are tried for job placement within a queue.
        Compute environments are tried in ascending order. For example, if two compute
        environments are associated with a job queue, the compute environment with a lower
        order integer value is tried for job placement first.

        - **order** *(integer) --*

          The order of the compute environment.

        - **computeEnvironment** *(string) --*

          The Amazon Resource Name (ARN) of the compute environment.
    """


_ClientDescribeJobQueuesResponseTypeDef = TypedDict(
    "_ClientDescribeJobQueuesResponseTypeDef",
    {
        "jobQueues": List[ClientDescribeJobQueuesResponsejobQueuesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeJobQueuesResponseTypeDef(_ClientDescribeJobQueuesResponseTypeDef):
    """
    Type definition for `ClientDescribeJobQueues` `Response`

    - **jobQueues** *(list) --*

      The list of job queues.

      - *(dict) --*

        An object representing the details of an AWS Batch job queue.

        - **jobQueueName** *(string) --*

          The name of the job queue.

        - **jobQueueArn** *(string) --*

          The Amazon Resource Name (ARN) of the job queue.

        - **state** *(string) --*

          Describes the ability of the queue to accept new jobs.

        - **status** *(string) --*

          The status of the job queue (for example, ``CREATING`` or ``VALID`` ).

        - **statusReason** *(string) --*

          A short, human-readable string to provide additional details about the current status of
          the job queue.

        - **priority** *(integer) --*

          The priority of the job queue.

        - **computeEnvironmentOrder** *(list) --*

          The compute environments that are attached to the job queue and the order in which job
          placement is preferred. Compute environments are selected for job placement in ascending
          order.

          - *(dict) --*

            The order in which compute environments are tried for job placement within a queue.
            Compute environments are tried in ascending order. For example, if two compute
            environments are associated with a job queue, the compute environment with a lower
            order integer value is tried for job placement first.

            - **order** *(integer) --*

              The order of the compute environment.

            - **computeEnvironment** *(string) --*

              The Amazon Resource Name (ARN) of the compute environment.

    - **nextToken** *(string) --*

      The ``nextToken`` value to include in a future ``DescribeJobQueues`` request. When the
      results of a ``DescribeJobQueues`` request exceed ``maxResults`` , this value can be used to
      retrieve the next page of results. This value is ``null`` when there are no more results to
      return.
    """


_ClientDescribeJobsResponsejobsarrayPropertiesTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsarrayPropertiesTypeDef",
    {"statusSummary": Dict[str, int], "size": int, "index": int},
    total=False,
)


class ClientDescribeJobsResponsejobsarrayPropertiesTypeDef(
    _ClientDescribeJobsResponsejobsarrayPropertiesTypeDef
):
    """
    Type definition for `ClientDescribeJobsResponsejobs` `arrayProperties`

    The array properties of the job, if it is an array job.

    - **statusSummary** *(dict) --*

      A summary of the number of array job children in each available job status. This
      parameter is returned for parent array jobs.

      - *(string) --*

        - *(integer) --*

    - **size** *(integer) --*

      The size of the array job. This parameter is returned for parent array jobs.

    - **index** *(integer) --*

      The job index within the array that is associated with this job. This parameter is
      returned for array job children.
    """


_ClientDescribeJobsResponsejobsattemptscontainernetworkInterfacesTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsattemptscontainernetworkInterfacesTypeDef",
    {"attachmentId": str, "ipv6Address": str, "privateIpv4Address": str},
    total=False,
)


class ClientDescribeJobsResponsejobsattemptscontainernetworkInterfacesTypeDef(
    _ClientDescribeJobsResponsejobsattemptscontainernetworkInterfacesTypeDef
):
    """
    Type definition for `ClientDescribeJobsResponsejobsattemptscontainer` `networkInterfaces`

    An object representing the elastic network interface for a multi-node parallel
    job node.

    - **attachmentId** *(string) --*

      The attachment ID for the network interface.

    - **ipv6Address** *(string) --*

      The private IPv6 address for the network interface.

    - **privateIpv4Address** *(string) --*

      The private IPv4 address for the network interface.
    """


_ClientDescribeJobsResponsejobsattemptscontainerTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsattemptscontainerTypeDef",
    {
        "containerInstanceArn": str,
        "taskArn": str,
        "exitCode": int,
        "reason": str,
        "logStreamName": str,
        "networkInterfaces": List[
            ClientDescribeJobsResponsejobsattemptscontainernetworkInterfacesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeJobsResponsejobsattemptscontainerTypeDef(
    _ClientDescribeJobsResponsejobsattemptscontainerTypeDef
):
    """
    Type definition for `ClientDescribeJobsResponsejobsattempts` `container`

    Details about the container in this job attempt.

    - **containerInstanceArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon ECS container instance that hosts the
      job attempt.

    - **taskArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon ECS task that is associated with the
      job attempt. Each container attempt receives a task ARN when they reach the
      ``STARTING`` status.

    - **exitCode** *(integer) --*

      The exit code for the job attempt. A non-zero exit code is considered a failure.

    - **reason** *(string) --*

      A short (255 max characters) human-readable string to provide additional details
      about a running or stopped container.

    - **logStreamName** *(string) --*

      The name of the CloudWatch Logs log stream associated with the container. The log
      group for AWS Batch jobs is ``/aws/batch/job`` . Each container attempt receives a
      log stream name when they reach the ``RUNNING`` status.

    - **networkInterfaces** *(list) --*

      The network interfaces associated with the job attempt.

      - *(dict) --*

        An object representing the elastic network interface for a multi-node parallel
        job node.

        - **attachmentId** *(string) --*

          The attachment ID for the network interface.

        - **ipv6Address** *(string) --*

          The private IPv6 address for the network interface.

        - **privateIpv4Address** *(string) --*

          The private IPv4 address for the network interface.
    """


_ClientDescribeJobsResponsejobsattemptsTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsattemptsTypeDef",
    {
        "container": ClientDescribeJobsResponsejobsattemptscontainerTypeDef,
        "startedAt": int,
        "stoppedAt": int,
        "statusReason": str,
    },
    total=False,
)


class ClientDescribeJobsResponsejobsattemptsTypeDef(
    _ClientDescribeJobsResponsejobsattemptsTypeDef
):
    """
    Type definition for `ClientDescribeJobsResponsejobs` `attempts`

    An object representing a job attempt.

    - **container** *(dict) --*

      Details about the container in this job attempt.

      - **containerInstanceArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon ECS container instance that hosts the
        job attempt.

      - **taskArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon ECS task that is associated with the
        job attempt. Each container attempt receives a task ARN when they reach the
        ``STARTING`` status.

      - **exitCode** *(integer) --*

        The exit code for the job attempt. A non-zero exit code is considered a failure.

      - **reason** *(string) --*

        A short (255 max characters) human-readable string to provide additional details
        about a running or stopped container.

      - **logStreamName** *(string) --*

        The name of the CloudWatch Logs log stream associated with the container. The log
        group for AWS Batch jobs is ``/aws/batch/job`` . Each container attempt receives a
        log stream name when they reach the ``RUNNING`` status.

      - **networkInterfaces** *(list) --*

        The network interfaces associated with the job attempt.

        - *(dict) --*

          An object representing the elastic network interface for a multi-node parallel
          job node.

          - **attachmentId** *(string) --*

            The attachment ID for the network interface.

          - **ipv6Address** *(string) --*

            The private IPv6 address for the network interface.

          - **privateIpv4Address** *(string) --*

            The private IPv4 address for the network interface.

    - **startedAt** *(integer) --*

      The Unix timestamp (in seconds and milliseconds) for when the attempt was started
      (when the attempt transitioned from the ``STARTING`` state to the ``RUNNING`` state).

    - **stoppedAt** *(integer) --*

      The Unix timestamp (in seconds and milliseconds) for when the attempt was stopped
      (when the attempt transitioned from the ``RUNNING`` state to a terminal state, such
      as ``SUCCEEDED`` or ``FAILED`` ).

    - **statusReason** *(string) --*

      A short, human-readable string to provide additional details about the current status
      of the job attempt.
    """


_ClientDescribeJobsResponsejobscontainerenvironmentTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobscontainerenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientDescribeJobsResponsejobscontainerenvironmentTypeDef(
    _ClientDescribeJobsResponsejobscontainerenvironmentTypeDef
):
    """
    Type definition for `ClientDescribeJobsResponsejobscontainer` `environment`

    A key-value pair object.

    - **name** *(string) --*

      The name of the key-value pair. For environment variables, this is the name of the
      environment variable.

    - **value** *(string) --*

      The value of the key-value pair. For environment variables, this is the value of
      the environment variable.
    """


_ClientDescribeJobsResponsejobscontainerlinuxParametersdevicesTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobscontainerlinuxParametersdevicesTypeDef",
    {"hostPath": str, "containerPath": str, "permissions": List[str]},
    total=False,
)


class ClientDescribeJobsResponsejobscontainerlinuxParametersdevicesTypeDef(
    _ClientDescribeJobsResponsejobscontainerlinuxParametersdevicesTypeDef
):
    """
    Type definition for `ClientDescribeJobsResponsejobscontainerlinuxParameters` `devices`

    An object representing a container instance host device.

    - **hostPath** *(string) --*

      The path for the device on the host container instance.

    - **containerPath** *(string) --*

      The path inside the container at which to expose the host device. By default the
      ``hostPath`` value is used.

    - **permissions** *(list) --*

      The explicit permissions to provide to the container for the device. By default,
      the container has permissions for ``read`` , ``write`` , and ``mknod`` for the
      device.

      - *(string) --*
    """


_ClientDescribeJobsResponsejobscontainerlinuxParametersTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobscontainerlinuxParametersTypeDef",
    {
        "devices": List[
            ClientDescribeJobsResponsejobscontainerlinuxParametersdevicesTypeDef
        ]
    },
    total=False,
)


class ClientDescribeJobsResponsejobscontainerlinuxParametersTypeDef(
    _ClientDescribeJobsResponsejobscontainerlinuxParametersTypeDef
):
    """
    Type definition for `ClientDescribeJobsResponsejobscontainer` `linuxParameters`

    Linux-specific modifications that are applied to the container, such as details for
    device mappings.

    - **devices** *(list) --*

      Any host devices to expose to the container. This parameter maps to ``Devices`` in
      the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--device`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__
      .

      - *(dict) --*

        An object representing a container instance host device.

        - **hostPath** *(string) --*

          The path for the device on the host container instance.

        - **containerPath** *(string) --*

          The path inside the container at which to expose the host device. By default the
          ``hostPath`` value is used.

        - **permissions** *(list) --*

          The explicit permissions to provide to the container for the device. By default,
          the container has permissions for ``read`` , ``write`` , and ``mknod`` for the
          device.

          - *(string) --*
    """


_ClientDescribeJobsResponsejobscontainermountPointsTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobscontainermountPointsTypeDef",
    {"containerPath": str, "readOnly": bool, "sourceVolume": str},
    total=False,
)


class ClientDescribeJobsResponsejobscontainermountPointsTypeDef(
    _ClientDescribeJobsResponsejobscontainermountPointsTypeDef
):
    """
    Type definition for `ClientDescribeJobsResponsejobscontainer` `mountPoints`

    Details on a Docker volume mount point that is used in a job's container properties.
    This parameter maps to ``Volumes`` in the `Create a container
    <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
    section of the Docker Remote API and the ``--volume`` option to docker run.

    - **containerPath** *(string) --*

      The path on the container at which to mount the host volume.

    - **readOnly** *(boolean) --*

      If this value is ``true`` , the container has read-only access to the volume;
      otherwise, the container can write to the volume. The default value is ``false`` .

    - **sourceVolume** *(string) --*

      The name of the volume to mount.
    """


_ClientDescribeJobsResponsejobscontainernetworkInterfacesTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobscontainernetworkInterfacesTypeDef",
    {"attachmentId": str, "ipv6Address": str, "privateIpv4Address": str},
    total=False,
)


class ClientDescribeJobsResponsejobscontainernetworkInterfacesTypeDef(
    _ClientDescribeJobsResponsejobscontainernetworkInterfacesTypeDef
):
    """
    Type definition for `ClientDescribeJobsResponsejobscontainer` `networkInterfaces`

    An object representing the elastic network interface for a multi-node parallel job
    node.

    - **attachmentId** *(string) --*

      The attachment ID for the network interface.

    - **ipv6Address** *(string) --*

      The private IPv6 address for the network interface.

    - **privateIpv4Address** *(string) --*

      The private IPv4 address for the network interface.
    """


_ClientDescribeJobsResponsejobscontainerresourceRequirementsTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobscontainerresourceRequirementsTypeDef",
    {"value": str, "type": str},
    total=False,
)


class ClientDescribeJobsResponsejobscontainerresourceRequirementsTypeDef(
    _ClientDescribeJobsResponsejobscontainerresourceRequirementsTypeDef
):
    """
    Type definition for `ClientDescribeJobsResponsejobscontainer` `resourceRequirements`

    The type and amount of a resource to assign to a container. Currently, the only
    supported resource type is ``GPU`` .

    - **value** *(string) --*

      The number of physical GPUs to reserve for the container. The number of GPUs
      reserved for all containers in a job should not exceed the number of available GPUs
      on the compute resource that the job is launched on.

    - **type** *(string) --*

      The type of resource to assign to a container. Currently, the only supported
      resource type is ``GPU`` .
    """


_ClientDescribeJobsResponsejobscontainerulimitsTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobscontainerulimitsTypeDef",
    {"hardLimit": int, "name": str, "softLimit": int},
    total=False,
)


class ClientDescribeJobsResponsejobscontainerulimitsTypeDef(
    _ClientDescribeJobsResponsejobscontainerulimitsTypeDef
):
    """
    Type definition for `ClientDescribeJobsResponsejobscontainer` `ulimits`

    The ``ulimit`` settings to pass to the container.

    - **hardLimit** *(integer) --*

      The hard limit for the ``ulimit`` type.

    - **name** *(string) --*

      The ``type`` of the ``ulimit`` .

    - **softLimit** *(integer) --*

      The soft limit for the ``ulimit`` type.
    """


_ClientDescribeJobsResponsejobscontainervolumeshostTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobscontainervolumeshostTypeDef",
    {"sourcePath": str},
    total=False,
)


class ClientDescribeJobsResponsejobscontainervolumeshostTypeDef(
    _ClientDescribeJobsResponsejobscontainervolumeshostTypeDef
):
    """
    Type definition for `ClientDescribeJobsResponsejobscontainervolumes` `host`

    The contents of the ``host`` parameter determine whether your data volume persists
    on the host container instance and where it is stored. If the host parameter is
    empty, then the Docker daemon assigns a host path for your data volume. However,
    the data is not guaranteed to persist after the containers associated with it stop
    running.

    - **sourcePath** *(string) --*

      The path on the host container instance that is presented to the container. If
      this parameter is empty, then the Docker daemon has assigned a host path for you.
      If this parameter contains a file location, then the data volume persists at the
      specified location on the host container instance until you delete it manually.
      If the source path location does not exist on the host container instance, the
      Docker daemon creates it. If the location does exist, the contents of the source
      path folder are exported.
    """


_ClientDescribeJobsResponsejobscontainervolumesTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobscontainervolumesTypeDef",
    {"host": ClientDescribeJobsResponsejobscontainervolumeshostTypeDef, "name": str},
    total=False,
)


class ClientDescribeJobsResponsejobscontainervolumesTypeDef(
    _ClientDescribeJobsResponsejobscontainervolumesTypeDef
):
    """
    Type definition for `ClientDescribeJobsResponsejobscontainer` `volumes`

    A data volume used in a job's container properties.

    - **host** *(dict) --*

      The contents of the ``host`` parameter determine whether your data volume persists
      on the host container instance and where it is stored. If the host parameter is
      empty, then the Docker daemon assigns a host path for your data volume. However,
      the data is not guaranteed to persist after the containers associated with it stop
      running.

      - **sourcePath** *(string) --*

        The path on the host container instance that is presented to the container. If
        this parameter is empty, then the Docker daemon has assigned a host path for you.
        If this parameter contains a file location, then the data volume persists at the
        specified location on the host container instance until you delete it manually.
        If the source path location does not exist on the host container instance, the
        Docker daemon creates it. If the location does exist, the contents of the source
        path folder are exported.

    - **name** *(string) --*

      The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
      hyphens, and underscores are allowed. This name is referenced in the
      ``sourceVolume`` parameter of container definition ``mountPoints`` .
    """


_ClientDescribeJobsResponsejobscontainerTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobscontainerTypeDef",
    {
        "image": str,
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "jobRoleArn": str,
        "volumes": List[ClientDescribeJobsResponsejobscontainervolumesTypeDef],
        "environment": List[ClientDescribeJobsResponsejobscontainerenvironmentTypeDef],
        "mountPoints": List[ClientDescribeJobsResponsejobscontainermountPointsTypeDef],
        "readonlyRootFilesystem": bool,
        "ulimits": List[ClientDescribeJobsResponsejobscontainerulimitsTypeDef],
        "privileged": bool,
        "user": str,
        "exitCode": int,
        "reason": str,
        "containerInstanceArn": str,
        "taskArn": str,
        "logStreamName": str,
        "instanceType": str,
        "networkInterfaces": List[
            ClientDescribeJobsResponsejobscontainernetworkInterfacesTypeDef
        ],
        "resourceRequirements": List[
            ClientDescribeJobsResponsejobscontainerresourceRequirementsTypeDef
        ],
        "linuxParameters": ClientDescribeJobsResponsejobscontainerlinuxParametersTypeDef,
    },
    total=False,
)


class ClientDescribeJobsResponsejobscontainerTypeDef(
    _ClientDescribeJobsResponsejobscontainerTypeDef
):
    """
    Type definition for `ClientDescribeJobsResponsejobs` `container`

    An object representing the details of the container that is associated with the job.

    - **image** *(string) --*

      The image used to start the container.

    - **vcpus** *(integer) --*

      The number of VCPUs allocated for the job.

    - **memory** *(integer) --*

      The number of MiB of memory reserved for the job.

    - **command** *(list) --*

      The command that is passed to the container.

      - *(string) --*

    - **jobRoleArn** *(string) --*

      The Amazon Resource Name (ARN) associated with the job upon execution.

    - **volumes** *(list) --*

      A list of volumes associated with the job.

      - *(dict) --*

        A data volume used in a job's container properties.

        - **host** *(dict) --*

          The contents of the ``host`` parameter determine whether your data volume persists
          on the host container instance and where it is stored. If the host parameter is
          empty, then the Docker daemon assigns a host path for your data volume. However,
          the data is not guaranteed to persist after the containers associated with it stop
          running.

          - **sourcePath** *(string) --*

            The path on the host container instance that is presented to the container. If
            this parameter is empty, then the Docker daemon has assigned a host path for you.
            If this parameter contains a file location, then the data volume persists at the
            specified location on the host container instance until you delete it manually.
            If the source path location does not exist on the host container instance, the
            Docker daemon creates it. If the location does exist, the contents of the source
            path folder are exported.

        - **name** *(string) --*

          The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
          hyphens, and underscores are allowed. This name is referenced in the
          ``sourceVolume`` parameter of container definition ``mountPoints`` .

    - **environment** *(list) --*

      The environment variables to pass to a container.

      .. note::

        Environment variables must not start with ``AWS_BATCH`` ; this naming convention is
        reserved for variables that are set by the AWS Batch service.

      - *(dict) --*

        A key-value pair object.

        - **name** *(string) --*

          The name of the key-value pair. For environment variables, this is the name of the
          environment variable.

        - **value** *(string) --*

          The value of the key-value pair. For environment variables, this is the value of
          the environment variable.

    - **mountPoints** *(list) --*

      The mount points for data volumes in your container.

      - *(dict) --*

        Details on a Docker volume mount point that is used in a job's container properties.
        This parameter maps to ``Volumes`` in the `Create a container
        <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
        section of the Docker Remote API and the ``--volume`` option to docker run.

        - **containerPath** *(string) --*

          The path on the container at which to mount the host volume.

        - **readOnly** *(boolean) --*

          If this value is ``true`` , the container has read-only access to the volume;
          otherwise, the container can write to the volume. The default value is ``false`` .

        - **sourceVolume** *(string) --*

          The name of the volume to mount.

    - **readonlyRootFilesystem** *(boolean) --*

      When this parameter is true, the container is given read-only access to its root file
      system.

    - **ulimits** *(list) --*

      A list of ``ulimit`` values to set in the container.

      - *(dict) --*

        The ``ulimit`` settings to pass to the container.

        - **hardLimit** *(integer) --*

          The hard limit for the ``ulimit`` type.

        - **name** *(string) --*

          The ``type`` of the ``ulimit`` .

        - **softLimit** *(integer) --*

          The soft limit for the ``ulimit`` type.

    - **privileged** *(boolean) --*

      When this parameter is true, the container is given elevated privileges on the host
      container instance (similar to the ``root`` user).

    - **user** *(string) --*

      The user name to use inside the container.

    - **exitCode** *(integer) --*

      The exit code to return upon completion.

    - **reason** *(string) --*

      A short (255 max characters) human-readable string to provide additional details about
      a running or stopped container.

    - **containerInstanceArn** *(string) --*

      The Amazon Resource Name (ARN) of the container instance on which the container is
      running.

    - **taskArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon ECS task that is associated with the
      container job. Each container attempt receives a task ARN when they reach the
      ``STARTING`` status.

    - **logStreamName** *(string) --*

      The name of the CloudWatch Logs log stream associated with the container. The log group
      for AWS Batch jobs is ``/aws/batch/job`` . Each container attempt receives a log stream
      name when they reach the ``RUNNING`` status.

    - **instanceType** *(string) --*

      The instance type of the underlying host infrastructure of a multi-node parallel job.

    - **networkInterfaces** *(list) --*

      The network interfaces associated with the job.

      - *(dict) --*

        An object representing the elastic network interface for a multi-node parallel job
        node.

        - **attachmentId** *(string) --*

          The attachment ID for the network interface.

        - **ipv6Address** *(string) --*

          The private IPv6 address for the network interface.

        - **privateIpv4Address** *(string) --*

          The private IPv4 address for the network interface.

    - **resourceRequirements** *(list) --*

      The type and amount of a resource to assign to a container. Currently, the only
      supported resource is ``GPU`` .

      - *(dict) --*

        The type and amount of a resource to assign to a container. Currently, the only
        supported resource type is ``GPU`` .

        - **value** *(string) --*

          The number of physical GPUs to reserve for the container. The number of GPUs
          reserved for all containers in a job should not exceed the number of available GPUs
          on the compute resource that the job is launched on.

        - **type** *(string) --*

          The type of resource to assign to a container. Currently, the only supported
          resource type is ``GPU`` .

    - **linuxParameters** *(dict) --*

      Linux-specific modifications that are applied to the container, such as details for
      device mappings.

      - **devices** *(list) --*

        Any host devices to expose to the container. This parameter maps to ``Devices`` in
        the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--device`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__
        .

        - *(dict) --*

          An object representing a container instance host device.

          - **hostPath** *(string) --*

            The path for the device on the host container instance.

          - **containerPath** *(string) --*

            The path inside the container at which to expose the host device. By default the
            ``hostPath`` value is used.

          - **permissions** *(list) --*

            The explicit permissions to provide to the container for the device. By default,
            the container has permissions for ``read`` , ``write`` , and ``mknod`` for the
            device.

            - *(string) --*
    """


_ClientDescribeJobsResponsejobsdependsOnTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsdependsOnTypeDef",
    {"jobId": str, "type": str},
    total=False,
)


class ClientDescribeJobsResponsejobsdependsOnTypeDef(
    _ClientDescribeJobsResponsejobsdependsOnTypeDef
):
    """
    Type definition for `ClientDescribeJobsResponsejobs` `dependsOn`

    An object representing an AWS Batch job dependency.

    - **jobId** *(string) --*

      The job ID of the AWS Batch job associated with this dependency.

    - **type** *(string) --*

      The type of the job dependency.
    """


_ClientDescribeJobsResponsejobsnodeDetailsTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsnodeDetailsTypeDef",
    {"nodeIndex": int, "isMainNode": bool},
    total=False,
)


class ClientDescribeJobsResponsejobsnodeDetailsTypeDef(
    _ClientDescribeJobsResponsejobsnodeDetailsTypeDef
):
    """
    Type definition for `ClientDescribeJobsResponsejobs` `nodeDetails`

    An object representing the details of a node that is associated with a multi-node
    parallel job.

    - **nodeIndex** *(integer) --*

      The node index for the node. Node index numbering begins at zero. This index is also
      available on the node with the ``AWS_BATCH_JOB_NODE_INDEX`` environment variable.

    - **isMainNode** *(boolean) --*

      Specifies whether the current node is the main node for a multi-node parallel job.
    """


_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef(
    _ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef
):
    """
    Type definition for `ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainer` `environment`

    A key-value pair object.

    - **name** *(string) --*

      The name of the key-value pair. For environment variables, this is the name
      of the environment variable.

    - **value** *(string) --*

      The value of the key-value pair. For environment variables, this is the value
      of the environment variable.
    """


_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef",
    {"hostPath": str, "containerPath": str, "permissions": List[str]},
    total=False,
)


class ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef(
    _ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef
):
    """
    Type definition for `ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerlinuxParameters` `devices`

    An object representing a container instance host device.

    - **hostPath** *(string) --*

      The path for the device on the host container instance.

    - **containerPath** *(string) --*

      The path inside the container at which to expose the host device. By
      default the ``hostPath`` value is used.

    - **permissions** *(list) --*

      The explicit permissions to provide to the container for the device. By
      default, the container has permissions for ``read`` , ``write`` , and
      ``mknod`` for the device.

      - *(string) --*
    """


_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef",
    {
        "devices": List[
            ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef
        ]
    },
    total=False,
)


class ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef(
    _ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef
):
    """
    Type definition for `ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainer` `linuxParameters`

    Linux-specific modifications that are applied to the container, such as details
    for device mappings.

    - **devices** *(list) --*

      Any host devices to expose to the container. This parameter maps to ``Devices``
      in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of
      the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--device`` option to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ .

      - *(dict) --*

        An object representing a container instance host device.

        - **hostPath** *(string) --*

          The path for the device on the host container instance.

        - **containerPath** *(string) --*

          The path inside the container at which to expose the host device. By
          default the ``hostPath`` value is used.

        - **permissions** *(list) --*

          The explicit permissions to provide to the container for the device. By
          default, the container has permissions for ``read`` , ``write`` , and
          ``mknod`` for the device.

          - *(string) --*
    """


_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef",
    {"containerPath": str, "readOnly": bool, "sourceVolume": str},
    total=False,
)


class ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef(
    _ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef
):
    """
    Type definition for `ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainer` `mountPoints`

    Details on a Docker volume mount point that is used in a job's container
    properties. This parameter maps to ``Volumes`` in the `Create a container
    <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
    section of the Docker Remote API and the ``--volume`` option to docker run.

    - **containerPath** *(string) --*

      The path on the container at which to mount the host volume.

    - **readOnly** *(boolean) --*

      If this value is ``true`` , the container has read-only access to the volume;
      otherwise, the container can write to the volume. The default value is
      ``false`` .

    - **sourceVolume** *(string) --*

      The name of the volume to mount.
    """


_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef",
    {"value": str, "type": str},
    total=False,
)


class ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef(
    _ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef
):
    """
    Type definition for `ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainer` `resourceRequirements`

    The type and amount of a resource to assign to a container. Currently, the only
    supported resource type is ``GPU`` .

    - **value** *(string) --*

      The number of physical GPUs to reserve for the container. The number of GPUs
      reserved for all containers in a job should not exceed the number of
      available GPUs on the compute resource that the job is launched on.

    - **type** *(string) --*

      The type of resource to assign to a container. Currently, the only supported
      resource type is ``GPU`` .
    """


_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef",
    {"hardLimit": int, "name": str, "softLimit": int},
    total=False,
)


class ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef(
    _ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef
):
    """
    Type definition for `ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainer` `ulimits`

    The ``ulimit`` settings to pass to the container.

    - **hardLimit** *(integer) --*

      The hard limit for the ``ulimit`` type.

    - **name** *(string) --*

      The ``type`` of the ``ulimit`` .

    - **softLimit** *(integer) --*

      The soft limit for the ``ulimit`` type.
    """


_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef",
    {"sourcePath": str},
    total=False,
)


class ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef(
    _ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef
):
    """
    Type definition for `ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainervolumes` `host`

    The contents of the ``host`` parameter determine whether your data volume
    persists on the host container instance and where it is stored. If the host
    parameter is empty, then the Docker daemon assigns a host path for your data
    volume. However, the data is not guaranteed to persist after the containers
    associated with it stop running.

    - **sourcePath** *(string) --*

      The path on the host container instance that is presented to the container.
      If this parameter is empty, then the Docker daemon has assigned a host path
      for you. If this parameter contains a file location, then the data volume
      persists at the specified location on the host container instance until you
      delete it manually. If the source path location does not exist on the host
      container instance, the Docker daemon creates it. If the location does
      exist, the contents of the source path folder are exported.
    """


_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainervolumesTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainervolumesTypeDef",
    {
        "host": ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef,
        "name": str,
    },
    total=False,
)


class ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainervolumesTypeDef(
    _ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainervolumesTypeDef
):
    """
    Type definition for `ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainer` `volumes`

    A data volume used in a job's container properties.

    - **host** *(dict) --*

      The contents of the ``host`` parameter determine whether your data volume
      persists on the host container instance and where it is stored. If the host
      parameter is empty, then the Docker daemon assigns a host path for your data
      volume. However, the data is not guaranteed to persist after the containers
      associated with it stop running.

      - **sourcePath** *(string) --*

        The path on the host container instance that is presented to the container.
        If this parameter is empty, then the Docker daemon has assigned a host path
        for you. If this parameter contains a file location, then the data volume
        persists at the specified location on the host container instance until you
        delete it manually. If the source path location does not exist on the host
        container instance, the Docker daemon creates it. If the location does
        exist, the contents of the source path folder are exported.

    - **name** *(string) --*

      The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
      hyphens, and underscores are allowed. This name is referenced in the
      ``sourceVolume`` parameter of container definition ``mountPoints`` .
    """


_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerTypeDef",
    {
        "image": str,
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "jobRoleArn": str,
        "volumes": List[
            ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainervolumesTypeDef
        ],
        "environment": List[
            ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef
        ],
        "mountPoints": List[
            ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef
        ],
        "readonlyRootFilesystem": bool,
        "privileged": bool,
        "ulimits": List[
            ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef
        ],
        "user": str,
        "instanceType": str,
        "resourceRequirements": List[
            ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef
        ],
        "linuxParameters": ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef,
    },
    total=False,
)


class ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerTypeDef(
    _ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerTypeDef
):
    """
    Type definition for `ClientDescribeJobsResponsejobsnodePropertiesnodeRangeProperties` `container`

    The container details for the node range.

    - **image** *(string) --*

      The image used to start a container. This string is passed directly to the Docker
      daemon. Images in the Docker Hub registry are available by default. Other
      repositories are specified with `` *repository-url* /*image* :*tag* `` . Up to
      255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons,
      periods, forward slashes, and number signs are allowed. This parameter maps to
      ``Image`` in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``IMAGE`` parameter of `docker run
      <https://docs.docker.com/engine/reference/run/>`__ .

      * Images in Amazon ECR repositories use the full registry and repository URI (for
      example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ).

      * Images in official repositories on Docker Hub use a single name (for example,
      ``ubuntu`` or ``mongo`` ).

      * Images in other repositories on Docker Hub are qualified with an organization
      name (for example, ``amazon/amazon-ecs-agent`` ).

      * Images in other online repositories are qualified further by a domain name (for
      example, ``quay.io/assemblyline/ubuntu`` ).

    - **vcpus** *(integer) --*

      The number of vCPUs reserved for the container. This parameter maps to
      ``CpuShares`` in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--cpu-shares`` option to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ . Each vCPU is equivalent to
      1,024 CPU shares. You must specify at least one vCPU.

    - **memory** *(integer) --*

      The hard limit (in MiB) of memory to present to the container. If your container
      attempts to exceed the memory specified here, the container is killed. This
      parameter maps to ``Memory`` in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--memory`` option to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ . You must specify at least 4
      MiB of memory for a job.

      .. note::

        If you are trying to maximize your resource utilization by providing your jobs
        as much memory as possible for a particular instance type, see `Memory
        Management
        <https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`__
        in the *AWS Batch User Guide* .

    - **command** *(list) --*

      The command that is passed to the container. This parameter maps to ``Cmd`` in
      the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``COMMAND`` parameter to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ . For more information, see
      `https\\://docs.docker.com/engine/reference/builder/#cmd
      <https://docs.docker.com/engine/reference/builder/#cmd>`__ .

      - *(string) --*

    - **jobRoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that the container can assume for
      AWS permissions.

    - **volumes** *(list) --*

      A list of data volumes used in a job.

      - *(dict) --*

        A data volume used in a job's container properties.

        - **host** *(dict) --*

          The contents of the ``host`` parameter determine whether your data volume
          persists on the host container instance and where it is stored. If the host
          parameter is empty, then the Docker daemon assigns a host path for your data
          volume. However, the data is not guaranteed to persist after the containers
          associated with it stop running.

          - **sourcePath** *(string) --*

            The path on the host container instance that is presented to the container.
            If this parameter is empty, then the Docker daemon has assigned a host path
            for you. If this parameter contains a file location, then the data volume
            persists at the specified location on the host container instance until you
            delete it manually. If the source path location does not exist on the host
            container instance, the Docker daemon creates it. If the location does
            exist, the contents of the source path folder are exported.

        - **name** *(string) --*

          The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
          hyphens, and underscores are allowed. This name is referenced in the
          ``sourceVolume`` parameter of container definition ``mountPoints`` .

    - **environment** *(list) --*

      The environment variables to pass to a container. This parameter maps to ``Env``
      in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--env`` option to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ .

      .. warning::

        We do not recommend using plaintext environment variables for sensitive
        information, such as credential data.

      .. note::

        Environment variables must not start with ``AWS_BATCH`` ; this naming
        convention is reserved for variables that are set by the AWS Batch service.

      - *(dict) --*

        A key-value pair object.

        - **name** *(string) --*

          The name of the key-value pair. For environment variables, this is the name
          of the environment variable.

        - **value** *(string) --*

          The value of the key-value pair. For environment variables, this is the value
          of the environment variable.

    - **mountPoints** *(list) --*

      The mount points for data volumes in your container. This parameter maps to
      ``Volumes`` in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--volume`` option to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ .

      - *(dict) --*

        Details on a Docker volume mount point that is used in a job's container
        properties. This parameter maps to ``Volumes`` in the `Create a container
        <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
        section of the Docker Remote API and the ``--volume`` option to docker run.

        - **containerPath** *(string) --*

          The path on the container at which to mount the host volume.

        - **readOnly** *(boolean) --*

          If this value is ``true`` , the container has read-only access to the volume;
          otherwise, the container can write to the volume. The default value is
          ``false`` .

        - **sourceVolume** *(string) --*

          The name of the volume to mount.

    - **readonlyRootFilesystem** *(boolean) --*

      When this parameter is true, the container is given read-only access to its root
      file system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--read-only`` option to ``docker run`` .

    - **privileged** *(boolean) --*

      When this parameter is true, the container is given elevated privileges on the
      host container instance (similar to the ``root`` user). This parameter maps to
      ``Privileged`` in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--privileged`` option to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ .

    - **ulimits** *(list) --*

      A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits``
      in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--ulimit`` option to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ .

      - *(dict) --*

        The ``ulimit`` settings to pass to the container.

        - **hardLimit** *(integer) --*

          The hard limit for the ``ulimit`` type.

        - **name** *(string) --*

          The ``type`` of the ``ulimit`` .

        - **softLimit** *(integer) --*

          The soft limit for the ``ulimit`` type.

    - **user** *(string) --*

      The user name to use inside the container. This parameter maps to ``User`` in the
      `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--user`` option to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ .

    - **instanceType** *(string) --*

      The instance type to use for a multi-node parallel job. Currently all node groups
      in a multi-node parallel job must use the same instance type. This parameter is
      not valid for single-node container jobs.

    - **resourceRequirements** *(list) --*

      The type and amount of a resource to assign to a container. Currently, the only
      supported resource is ``GPU`` .

      - *(dict) --*

        The type and amount of a resource to assign to a container. Currently, the only
        supported resource type is ``GPU`` .

        - **value** *(string) --*

          The number of physical GPUs to reserve for the container. The number of GPUs
          reserved for all containers in a job should not exceed the number of
          available GPUs on the compute resource that the job is launched on.

        - **type** *(string) --*

          The type of resource to assign to a container. Currently, the only supported
          resource type is ``GPU`` .

    - **linuxParameters** *(dict) --*

      Linux-specific modifications that are applied to the container, such as details
      for device mappings.

      - **devices** *(list) --*

        Any host devices to expose to the container. This parameter maps to ``Devices``
        in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of
        the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--device`` option to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ .

        - *(dict) --*

          An object representing a container instance host device.

          - **hostPath** *(string) --*

            The path for the device on the host container instance.

          - **containerPath** *(string) --*

            The path inside the container at which to expose the host device. By
            default the ``hostPath`` value is used.

          - **permissions** *(list) --*

            The explicit permissions to provide to the container for the device. By
            default, the container has permissions for ``read`` , ``write`` , and
            ``mknod`` for the device.

            - *(string) --*
    """


_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiesTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiesTypeDef",
    {
        "targetNodes": str,
        "container": ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerTypeDef,
    },
    total=False,
)


class ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiesTypeDef(
    _ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiesTypeDef
):
    """
    Type definition for `ClientDescribeJobsResponsejobsnodeProperties` `nodeRangeProperties`

    An object representing the properties of the node range for a multi-node parallel job.

    - **targetNodes** *(string) --*

      The range of nodes, using node index values. A range of ``0:3`` indicates nodes
      with index values of ``0`` through ``3`` . If the starting range value is omitted
      (``:n`` ), then ``0`` is used to start the range. If the ending range value is
      omitted (``n:`` ), then the highest possible node index is used to end the range.
      Your accumulative node ranges must account for all nodes (0:n). You may nest node
      ranges, for example 0:10 and 4:5, in which case the 4:5 range properties override
      the 0:10 properties.

    - **container** *(dict) --*

      The container details for the node range.

      - **image** *(string) --*

        The image used to start a container. This string is passed directly to the Docker
        daemon. Images in the Docker Hub registry are available by default. Other
        repositories are specified with `` *repository-url* /*image* :*tag* `` . Up to
        255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons,
        periods, forward slashes, and number signs are allowed. This parameter maps to
        ``Image`` in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``IMAGE`` parameter of `docker run
        <https://docs.docker.com/engine/reference/run/>`__ .

        * Images in Amazon ECR repositories use the full registry and repository URI (for
        example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ).

        * Images in official repositories on Docker Hub use a single name (for example,
        ``ubuntu`` or ``mongo`` ).

        * Images in other repositories on Docker Hub are qualified with an organization
        name (for example, ``amazon/amazon-ecs-agent`` ).

        * Images in other online repositories are qualified further by a domain name (for
        example, ``quay.io/assemblyline/ubuntu`` ).

      - **vcpus** *(integer) --*

        The number of vCPUs reserved for the container. This parameter maps to
        ``CpuShares`` in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--cpu-shares`` option to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ . Each vCPU is equivalent to
        1,024 CPU shares. You must specify at least one vCPU.

      - **memory** *(integer) --*

        The hard limit (in MiB) of memory to present to the container. If your container
        attempts to exceed the memory specified here, the container is killed. This
        parameter maps to ``Memory`` in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--memory`` option to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ . You must specify at least 4
        MiB of memory for a job.

        .. note::

          If you are trying to maximize your resource utilization by providing your jobs
          as much memory as possible for a particular instance type, see `Memory
          Management
          <https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`__
          in the *AWS Batch User Guide* .

      - **command** *(list) --*

        The command that is passed to the container. This parameter maps to ``Cmd`` in
        the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``COMMAND`` parameter to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ . For more information, see
        `https\\://docs.docker.com/engine/reference/builder/#cmd
        <https://docs.docker.com/engine/reference/builder/#cmd>`__ .

        - *(string) --*

      - **jobRoleArn** *(string) --*

        The Amazon Resource Name (ARN) of the IAM role that the container can assume for
        AWS permissions.

      - **volumes** *(list) --*

        A list of data volumes used in a job.

        - *(dict) --*

          A data volume used in a job's container properties.

          - **host** *(dict) --*

            The contents of the ``host`` parameter determine whether your data volume
            persists on the host container instance and where it is stored. If the host
            parameter is empty, then the Docker daemon assigns a host path for your data
            volume. However, the data is not guaranteed to persist after the containers
            associated with it stop running.

            - **sourcePath** *(string) --*

              The path on the host container instance that is presented to the container.
              If this parameter is empty, then the Docker daemon has assigned a host path
              for you. If this parameter contains a file location, then the data volume
              persists at the specified location on the host container instance until you
              delete it manually. If the source path location does not exist on the host
              container instance, the Docker daemon creates it. If the location does
              exist, the contents of the source path folder are exported.

          - **name** *(string) --*

            The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
            hyphens, and underscores are allowed. This name is referenced in the
            ``sourceVolume`` parameter of container definition ``mountPoints`` .

      - **environment** *(list) --*

        The environment variables to pass to a container. This parameter maps to ``Env``
        in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--env`` option to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ .

        .. warning::

          We do not recommend using plaintext environment variables for sensitive
          information, such as credential data.

        .. note::

          Environment variables must not start with ``AWS_BATCH`` ; this naming
          convention is reserved for variables that are set by the AWS Batch service.

        - *(dict) --*

          A key-value pair object.

          - **name** *(string) --*

            The name of the key-value pair. For environment variables, this is the name
            of the environment variable.

          - **value** *(string) --*

            The value of the key-value pair. For environment variables, this is the value
            of the environment variable.

      - **mountPoints** *(list) --*

        The mount points for data volumes in your container. This parameter maps to
        ``Volumes`` in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--volume`` option to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ .

        - *(dict) --*

          Details on a Docker volume mount point that is used in a job's container
          properties. This parameter maps to ``Volumes`` in the `Create a container
          <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
          section of the Docker Remote API and the ``--volume`` option to docker run.

          - **containerPath** *(string) --*

            The path on the container at which to mount the host volume.

          - **readOnly** *(boolean) --*

            If this value is ``true`` , the container has read-only access to the volume;
            otherwise, the container can write to the volume. The default value is
            ``false`` .

          - **sourceVolume** *(string) --*

            The name of the volume to mount.

      - **readonlyRootFilesystem** *(boolean) --*

        When this parameter is true, the container is given read-only access to its root
        file system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--read-only`` option to ``docker run`` .

      - **privileged** *(boolean) --*

        When this parameter is true, the container is given elevated privileges on the
        host container instance (similar to the ``root`` user). This parameter maps to
        ``Privileged`` in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--privileged`` option to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ .

      - **ulimits** *(list) --*

        A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits``
        in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--ulimit`` option to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ .

        - *(dict) --*

          The ``ulimit`` settings to pass to the container.

          - **hardLimit** *(integer) --*

            The hard limit for the ``ulimit`` type.

          - **name** *(string) --*

            The ``type`` of the ``ulimit`` .

          - **softLimit** *(integer) --*

            The soft limit for the ``ulimit`` type.

      - **user** *(string) --*

        The user name to use inside the container. This parameter maps to ``User`` in the
        `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--user`` option to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ .

      - **instanceType** *(string) --*

        The instance type to use for a multi-node parallel job. Currently all node groups
        in a multi-node parallel job must use the same instance type. This parameter is
        not valid for single-node container jobs.

      - **resourceRequirements** *(list) --*

        The type and amount of a resource to assign to a container. Currently, the only
        supported resource is ``GPU`` .

        - *(dict) --*

          The type and amount of a resource to assign to a container. Currently, the only
          supported resource type is ``GPU`` .

          - **value** *(string) --*

            The number of physical GPUs to reserve for the container. The number of GPUs
            reserved for all containers in a job should not exceed the number of
            available GPUs on the compute resource that the job is launched on.

          - **type** *(string) --*

            The type of resource to assign to a container. Currently, the only supported
            resource type is ``GPU`` .

      - **linuxParameters** *(dict) --*

        Linux-specific modifications that are applied to the container, such as details
        for device mappings.

        - **devices** *(list) --*

          Any host devices to expose to the container. This parameter maps to ``Devices``
          in the `Create a container
          <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of
          the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
          ``--device`` option to `docker run
          <https://docs.docker.com/engine/reference/run/>`__ .

          - *(dict) --*

            An object representing a container instance host device.

            - **hostPath** *(string) --*

              The path for the device on the host container instance.

            - **containerPath** *(string) --*

              The path inside the container at which to expose the host device. By
              default the ``hostPath`` value is used.

            - **permissions** *(list) --*

              The explicit permissions to provide to the container for the device. By
              default, the container has permissions for ``read`` , ``write`` , and
              ``mknod`` for the device.

              - *(string) --*
    """


_ClientDescribeJobsResponsejobsnodePropertiesTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsnodePropertiesTypeDef",
    {
        "numNodes": int,
        "mainNode": int,
        "nodeRangeProperties": List[
            ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeJobsResponsejobsnodePropertiesTypeDef(
    _ClientDescribeJobsResponsejobsnodePropertiesTypeDef
):
    """
    Type definition for `ClientDescribeJobsResponsejobs` `nodeProperties`

    An object representing the node properties of a multi-node parallel job.

    - **numNodes** *(integer) --*

      The number of nodes associated with a multi-node parallel job.

    - **mainNode** *(integer) --*

      Specifies the node index for the main node of a multi-node parallel job. This node
      index value must be fewer than the number of nodes.

    - **nodeRangeProperties** *(list) --*

      A list of node ranges and their properties associated with a multi-node parallel job.

      - *(dict) --*

        An object representing the properties of the node range for a multi-node parallel job.

        - **targetNodes** *(string) --*

          The range of nodes, using node index values. A range of ``0:3`` indicates nodes
          with index values of ``0`` through ``3`` . If the starting range value is omitted
          (``:n`` ), then ``0`` is used to start the range. If the ending range value is
          omitted (``n:`` ), then the highest possible node index is used to end the range.
          Your accumulative node ranges must account for all nodes (0:n). You may nest node
          ranges, for example 0:10 and 4:5, in which case the 4:5 range properties override
          the 0:10 properties.

        - **container** *(dict) --*

          The container details for the node range.

          - **image** *(string) --*

            The image used to start a container. This string is passed directly to the Docker
            daemon. Images in the Docker Hub registry are available by default. Other
            repositories are specified with `` *repository-url* /*image* :*tag* `` . Up to
            255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons,
            periods, forward slashes, and number signs are allowed. This parameter maps to
            ``Image`` in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``IMAGE`` parameter of `docker run
            <https://docs.docker.com/engine/reference/run/>`__ .

            * Images in Amazon ECR repositories use the full registry and repository URI (for
            example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ).

            * Images in official repositories on Docker Hub use a single name (for example,
            ``ubuntu`` or ``mongo`` ).

            * Images in other repositories on Docker Hub are qualified with an organization
            name (for example, ``amazon/amazon-ecs-agent`` ).

            * Images in other online repositories are qualified further by a domain name (for
            example, ``quay.io/assemblyline/ubuntu`` ).

          - **vcpus** *(integer) --*

            The number of vCPUs reserved for the container. This parameter maps to
            ``CpuShares`` in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``--cpu-shares`` option to `docker run
            <https://docs.docker.com/engine/reference/run/>`__ . Each vCPU is equivalent to
            1,024 CPU shares. You must specify at least one vCPU.

          - **memory** *(integer) --*

            The hard limit (in MiB) of memory to present to the container. If your container
            attempts to exceed the memory specified here, the container is killed. This
            parameter maps to ``Memory`` in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``--memory`` option to `docker run
            <https://docs.docker.com/engine/reference/run/>`__ . You must specify at least 4
            MiB of memory for a job.

            .. note::

              If you are trying to maximize your resource utilization by providing your jobs
              as much memory as possible for a particular instance type, see `Memory
              Management
              <https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`__
              in the *AWS Batch User Guide* .

          - **command** *(list) --*

            The command that is passed to the container. This parameter maps to ``Cmd`` in
            the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``COMMAND`` parameter to `docker run
            <https://docs.docker.com/engine/reference/run/>`__ . For more information, see
            `https\\://docs.docker.com/engine/reference/builder/#cmd
            <https://docs.docker.com/engine/reference/builder/#cmd>`__ .

            - *(string) --*

          - **jobRoleArn** *(string) --*

            The Amazon Resource Name (ARN) of the IAM role that the container can assume for
            AWS permissions.

          - **volumes** *(list) --*

            A list of data volumes used in a job.

            - *(dict) --*

              A data volume used in a job's container properties.

              - **host** *(dict) --*

                The contents of the ``host`` parameter determine whether your data volume
                persists on the host container instance and where it is stored. If the host
                parameter is empty, then the Docker daemon assigns a host path for your data
                volume. However, the data is not guaranteed to persist after the containers
                associated with it stop running.

                - **sourcePath** *(string) --*

                  The path on the host container instance that is presented to the container.
                  If this parameter is empty, then the Docker daemon has assigned a host path
                  for you. If this parameter contains a file location, then the data volume
                  persists at the specified location on the host container instance until you
                  delete it manually. If the source path location does not exist on the host
                  container instance, the Docker daemon creates it. If the location does
                  exist, the contents of the source path folder are exported.

              - **name** *(string) --*

                The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
                hyphens, and underscores are allowed. This name is referenced in the
                ``sourceVolume`` parameter of container definition ``mountPoints`` .

          - **environment** *(list) --*

            The environment variables to pass to a container. This parameter maps to ``Env``
            in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``--env`` option to `docker run
            <https://docs.docker.com/engine/reference/run/>`__ .

            .. warning::

              We do not recommend using plaintext environment variables for sensitive
              information, such as credential data.

            .. note::

              Environment variables must not start with ``AWS_BATCH`` ; this naming
              convention is reserved for variables that are set by the AWS Batch service.

            - *(dict) --*

              A key-value pair object.

              - **name** *(string) --*

                The name of the key-value pair. For environment variables, this is the name
                of the environment variable.

              - **value** *(string) --*

                The value of the key-value pair. For environment variables, this is the value
                of the environment variable.

          - **mountPoints** *(list) --*

            The mount points for data volumes in your container. This parameter maps to
            ``Volumes`` in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``--volume`` option to `docker run
            <https://docs.docker.com/engine/reference/run/>`__ .

            - *(dict) --*

              Details on a Docker volume mount point that is used in a job's container
              properties. This parameter maps to ``Volumes`` in the `Create a container
              <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
              section of the Docker Remote API and the ``--volume`` option to docker run.

              - **containerPath** *(string) --*

                The path on the container at which to mount the host volume.

              - **readOnly** *(boolean) --*

                If this value is ``true`` , the container has read-only access to the volume;
                otherwise, the container can write to the volume. The default value is
                ``false`` .

              - **sourceVolume** *(string) --*

                The name of the volume to mount.

          - **readonlyRootFilesystem** *(boolean) --*

            When this parameter is true, the container is given read-only access to its root
            file system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``--read-only`` option to ``docker run`` .

          - **privileged** *(boolean) --*

            When this parameter is true, the container is given elevated privileges on the
            host container instance (similar to the ``root`` user). This parameter maps to
            ``Privileged`` in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``--privileged`` option to `docker run
            <https://docs.docker.com/engine/reference/run/>`__ .

          - **ulimits** *(list) --*

            A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits``
            in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``--ulimit`` option to `docker run
            <https://docs.docker.com/engine/reference/run/>`__ .

            - *(dict) --*

              The ``ulimit`` settings to pass to the container.

              - **hardLimit** *(integer) --*

                The hard limit for the ``ulimit`` type.

              - **name** *(string) --*

                The ``type`` of the ``ulimit`` .

              - **softLimit** *(integer) --*

                The soft limit for the ``ulimit`` type.

          - **user** *(string) --*

            The user name to use inside the container. This parameter maps to ``User`` in the
            `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``--user`` option to `docker run
            <https://docs.docker.com/engine/reference/run/>`__ .

          - **instanceType** *(string) --*

            The instance type to use for a multi-node parallel job. Currently all node groups
            in a multi-node parallel job must use the same instance type. This parameter is
            not valid for single-node container jobs.

          - **resourceRequirements** *(list) --*

            The type and amount of a resource to assign to a container. Currently, the only
            supported resource is ``GPU`` .

            - *(dict) --*

              The type and amount of a resource to assign to a container. Currently, the only
              supported resource type is ``GPU`` .

              - **value** *(string) --*

                The number of physical GPUs to reserve for the container. The number of GPUs
                reserved for all containers in a job should not exceed the number of
                available GPUs on the compute resource that the job is launched on.

              - **type** *(string) --*

                The type of resource to assign to a container. Currently, the only supported
                resource type is ``GPU`` .

          - **linuxParameters** *(dict) --*

            Linux-specific modifications that are applied to the container, such as details
            for device mappings.

            - **devices** *(list) --*

              Any host devices to expose to the container. This parameter maps to ``Devices``
              in the `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of
              the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``--device`` option to `docker run
              <https://docs.docker.com/engine/reference/run/>`__ .

              - *(dict) --*

                An object representing a container instance host device.

                - **hostPath** *(string) --*

                  The path for the device on the host container instance.

                - **containerPath** *(string) --*

                  The path inside the container at which to expose the host device. By
                  default the ``hostPath`` value is used.

                - **permissions** *(list) --*

                  The explicit permissions to provide to the container for the device. By
                  default, the container has permissions for ``read`` , ``write`` , and
                  ``mknod`` for the device.

                  - *(string) --*
    """


_ClientDescribeJobsResponsejobsretryStrategyTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsretryStrategyTypeDef",
    {"attempts": int},
    total=False,
)


class ClientDescribeJobsResponsejobsretryStrategyTypeDef(
    _ClientDescribeJobsResponsejobsretryStrategyTypeDef
):
    """
    Type definition for `ClientDescribeJobsResponsejobs` `retryStrategy`

    The retry strategy to use for this job if an attempt fails.

    - **attempts** *(integer) --*

      The number of times to move a job to the ``RUNNABLE`` status. You may specify between 1
      and 10 attempts. If the value of ``attempts`` is greater than one, the job is retried
      on failure the same number of attempts as the value.
    """


_ClientDescribeJobsResponsejobstimeoutTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobstimeoutTypeDef",
    {"attemptDurationSeconds": int},
    total=False,
)


class ClientDescribeJobsResponsejobstimeoutTypeDef(
    _ClientDescribeJobsResponsejobstimeoutTypeDef
):
    """
    Type definition for `ClientDescribeJobsResponsejobs` `timeout`

    The timeout configuration for the job.

    - **attemptDurationSeconds** *(integer) --*

      The time duration in seconds (measured from the job attempt's ``startedAt`` timestamp)
      after which AWS Batch terminates your jobs if they have not finished.
    """


_ClientDescribeJobsResponsejobsTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsTypeDef",
    {
        "jobName": str,
        "jobId": str,
        "jobQueue": str,
        "status": str,
        "attempts": List[ClientDescribeJobsResponsejobsattemptsTypeDef],
        "statusReason": str,
        "createdAt": int,
        "retryStrategy": ClientDescribeJobsResponsejobsretryStrategyTypeDef,
        "startedAt": int,
        "stoppedAt": int,
        "dependsOn": List[ClientDescribeJobsResponsejobsdependsOnTypeDef],
        "jobDefinition": str,
        "parameters": Dict[str, str],
        "container": ClientDescribeJobsResponsejobscontainerTypeDef,
        "nodeDetails": ClientDescribeJobsResponsejobsnodeDetailsTypeDef,
        "nodeProperties": ClientDescribeJobsResponsejobsnodePropertiesTypeDef,
        "arrayProperties": ClientDescribeJobsResponsejobsarrayPropertiesTypeDef,
        "timeout": ClientDescribeJobsResponsejobstimeoutTypeDef,
    },
    total=False,
)


class ClientDescribeJobsResponsejobsTypeDef(_ClientDescribeJobsResponsejobsTypeDef):
    """
    Type definition for `ClientDescribeJobsResponse` `jobs`

    An object representing an AWS Batch job.

    - **jobName** *(string) --*

      The name of the job.

    - **jobId** *(string) --*

      The ID for the job.

    - **jobQueue** *(string) --*

      The Amazon Resource Name (ARN) of the job queue with which the job is associated.

    - **status** *(string) --*

      The current status for the job.

      .. note::

        If your jobs do not progress to ``STARTING`` , see `Jobs Stuck in RUNNABLE Status
        <https://docs.aws.amazon.com/batch/latest/userguide/troubleshooting.html#job_stuck_in_runnable>`__
        in the troubleshooting section of the *AWS Batch User Guide* .

    - **attempts** *(list) --*

      A list of job attempts associated with this job.

      - *(dict) --*

        An object representing a job attempt.

        - **container** *(dict) --*

          Details about the container in this job attempt.

          - **containerInstanceArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon ECS container instance that hosts the
            job attempt.

          - **taskArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon ECS task that is associated with the
            job attempt. Each container attempt receives a task ARN when they reach the
            ``STARTING`` status.

          - **exitCode** *(integer) --*

            The exit code for the job attempt. A non-zero exit code is considered a failure.

          - **reason** *(string) --*

            A short (255 max characters) human-readable string to provide additional details
            about a running or stopped container.

          - **logStreamName** *(string) --*

            The name of the CloudWatch Logs log stream associated with the container. The log
            group for AWS Batch jobs is ``/aws/batch/job`` . Each container attempt receives a
            log stream name when they reach the ``RUNNING`` status.

          - **networkInterfaces** *(list) --*

            The network interfaces associated with the job attempt.

            - *(dict) --*

              An object representing the elastic network interface for a multi-node parallel
              job node.

              - **attachmentId** *(string) --*

                The attachment ID for the network interface.

              - **ipv6Address** *(string) --*

                The private IPv6 address for the network interface.

              - **privateIpv4Address** *(string) --*

                The private IPv4 address for the network interface.

        - **startedAt** *(integer) --*

          The Unix timestamp (in seconds and milliseconds) for when the attempt was started
          (when the attempt transitioned from the ``STARTING`` state to the ``RUNNING`` state).

        - **stoppedAt** *(integer) --*

          The Unix timestamp (in seconds and milliseconds) for when the attempt was stopped
          (when the attempt transitioned from the ``RUNNING`` state to a terminal state, such
          as ``SUCCEEDED`` or ``FAILED`` ).

        - **statusReason** *(string) --*

          A short, human-readable string to provide additional details about the current status
          of the job attempt.

    - **statusReason** *(string) --*

      A short, human-readable string to provide additional details about the current status of
      the job.

    - **createdAt** *(integer) --*

      The Unix timestamp (in seconds and milliseconds) for when the job was created. For
      non-array jobs and parent array jobs, this is when the job entered the ``SUBMITTED``
      state (at the time  SubmitJob was called). For array child jobs, this is when the child
      job was spawned by its parent and entered the ``PENDING`` state.

    - **retryStrategy** *(dict) --*

      The retry strategy to use for this job if an attempt fails.

      - **attempts** *(integer) --*

        The number of times to move a job to the ``RUNNABLE`` status. You may specify between 1
        and 10 attempts. If the value of ``attempts`` is greater than one, the job is retried
        on failure the same number of attempts as the value.

    - **startedAt** *(integer) --*

      The Unix timestamp (in seconds and milliseconds) for when the job was started (when the
      job transitioned from the ``STARTING`` state to the ``RUNNING`` state).

    - **stoppedAt** *(integer) --*

      The Unix timestamp (in seconds and milliseconds) for when the job was stopped (when the
      job transitioned from the ``RUNNING`` state to a terminal state, such as ``SUCCEEDED`` or
      ``FAILED`` ).

    - **dependsOn** *(list) --*

      A list of job names or IDs on which this job depends.

      - *(dict) --*

        An object representing an AWS Batch job dependency.

        - **jobId** *(string) --*

          The job ID of the AWS Batch job associated with this dependency.

        - **type** *(string) --*

          The type of the job dependency.

    - **jobDefinition** *(string) --*

      The job definition that is used by this job.

    - **parameters** *(dict) --*

      Additional parameters passed to the job that replace parameter substitution placeholders
      or override any corresponding parameter defaults from the job definition.

      - *(string) --*

        - *(string) --*

    - **container** *(dict) --*

      An object representing the details of the container that is associated with the job.

      - **image** *(string) --*

        The image used to start the container.

      - **vcpus** *(integer) --*

        The number of VCPUs allocated for the job.

      - **memory** *(integer) --*

        The number of MiB of memory reserved for the job.

      - **command** *(list) --*

        The command that is passed to the container.

        - *(string) --*

      - **jobRoleArn** *(string) --*

        The Amazon Resource Name (ARN) associated with the job upon execution.

      - **volumes** *(list) --*

        A list of volumes associated with the job.

        - *(dict) --*

          A data volume used in a job's container properties.

          - **host** *(dict) --*

            The contents of the ``host`` parameter determine whether your data volume persists
            on the host container instance and where it is stored. If the host parameter is
            empty, then the Docker daemon assigns a host path for your data volume. However,
            the data is not guaranteed to persist after the containers associated with it stop
            running.

            - **sourcePath** *(string) --*

              The path on the host container instance that is presented to the container. If
              this parameter is empty, then the Docker daemon has assigned a host path for you.
              If this parameter contains a file location, then the data volume persists at the
              specified location on the host container instance until you delete it manually.
              If the source path location does not exist on the host container instance, the
              Docker daemon creates it. If the location does exist, the contents of the source
              path folder are exported.

          - **name** *(string) --*

            The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
            hyphens, and underscores are allowed. This name is referenced in the
            ``sourceVolume`` parameter of container definition ``mountPoints`` .

      - **environment** *(list) --*

        The environment variables to pass to a container.

        .. note::

          Environment variables must not start with ``AWS_BATCH`` ; this naming convention is
          reserved for variables that are set by the AWS Batch service.

        - *(dict) --*

          A key-value pair object.

          - **name** *(string) --*

            The name of the key-value pair. For environment variables, this is the name of the
            environment variable.

          - **value** *(string) --*

            The value of the key-value pair. For environment variables, this is the value of
            the environment variable.

      - **mountPoints** *(list) --*

        The mount points for data volumes in your container.

        - *(dict) --*

          Details on a Docker volume mount point that is used in a job's container properties.
          This parameter maps to ``Volumes`` in the `Create a container
          <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
          section of the Docker Remote API and the ``--volume`` option to docker run.

          - **containerPath** *(string) --*

            The path on the container at which to mount the host volume.

          - **readOnly** *(boolean) --*

            If this value is ``true`` , the container has read-only access to the volume;
            otherwise, the container can write to the volume. The default value is ``false`` .

          - **sourceVolume** *(string) --*

            The name of the volume to mount.

      - **readonlyRootFilesystem** *(boolean) --*

        When this parameter is true, the container is given read-only access to its root file
        system.

      - **ulimits** *(list) --*

        A list of ``ulimit`` values to set in the container.

        - *(dict) --*

          The ``ulimit`` settings to pass to the container.

          - **hardLimit** *(integer) --*

            The hard limit for the ``ulimit`` type.

          - **name** *(string) --*

            The ``type`` of the ``ulimit`` .

          - **softLimit** *(integer) --*

            The soft limit for the ``ulimit`` type.

      - **privileged** *(boolean) --*

        When this parameter is true, the container is given elevated privileges on the host
        container instance (similar to the ``root`` user).

      - **user** *(string) --*

        The user name to use inside the container.

      - **exitCode** *(integer) --*

        The exit code to return upon completion.

      - **reason** *(string) --*

        A short (255 max characters) human-readable string to provide additional details about
        a running or stopped container.

      - **containerInstanceArn** *(string) --*

        The Amazon Resource Name (ARN) of the container instance on which the container is
        running.

      - **taskArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon ECS task that is associated with the
        container job. Each container attempt receives a task ARN when they reach the
        ``STARTING`` status.

      - **logStreamName** *(string) --*

        The name of the CloudWatch Logs log stream associated with the container. The log group
        for AWS Batch jobs is ``/aws/batch/job`` . Each container attempt receives a log stream
        name when they reach the ``RUNNING`` status.

      - **instanceType** *(string) --*

        The instance type of the underlying host infrastructure of a multi-node parallel job.

      - **networkInterfaces** *(list) --*

        The network interfaces associated with the job.

        - *(dict) --*

          An object representing the elastic network interface for a multi-node parallel job
          node.

          - **attachmentId** *(string) --*

            The attachment ID for the network interface.

          - **ipv6Address** *(string) --*

            The private IPv6 address for the network interface.

          - **privateIpv4Address** *(string) --*

            The private IPv4 address for the network interface.

      - **resourceRequirements** *(list) --*

        The type and amount of a resource to assign to a container. Currently, the only
        supported resource is ``GPU`` .

        - *(dict) --*

          The type and amount of a resource to assign to a container. Currently, the only
          supported resource type is ``GPU`` .

          - **value** *(string) --*

            The number of physical GPUs to reserve for the container. The number of GPUs
            reserved for all containers in a job should not exceed the number of available GPUs
            on the compute resource that the job is launched on.

          - **type** *(string) --*

            The type of resource to assign to a container. Currently, the only supported
            resource type is ``GPU`` .

      - **linuxParameters** *(dict) --*

        Linux-specific modifications that are applied to the container, such as details for
        device mappings.

        - **devices** *(list) --*

          Any host devices to expose to the container. This parameter maps to ``Devices`` in
          the `Create a container
          <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
          `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
          ``--device`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__
          .

          - *(dict) --*

            An object representing a container instance host device.

            - **hostPath** *(string) --*

              The path for the device on the host container instance.

            - **containerPath** *(string) --*

              The path inside the container at which to expose the host device. By default the
              ``hostPath`` value is used.

            - **permissions** *(list) --*

              The explicit permissions to provide to the container for the device. By default,
              the container has permissions for ``read`` , ``write`` , and ``mknod`` for the
              device.

              - *(string) --*

    - **nodeDetails** *(dict) --*

      An object representing the details of a node that is associated with a multi-node
      parallel job.

      - **nodeIndex** *(integer) --*

        The node index for the node. Node index numbering begins at zero. This index is also
        available on the node with the ``AWS_BATCH_JOB_NODE_INDEX`` environment variable.

      - **isMainNode** *(boolean) --*

        Specifies whether the current node is the main node for a multi-node parallel job.

    - **nodeProperties** *(dict) --*

      An object representing the node properties of a multi-node parallel job.

      - **numNodes** *(integer) --*

        The number of nodes associated with a multi-node parallel job.

      - **mainNode** *(integer) --*

        Specifies the node index for the main node of a multi-node parallel job. This node
        index value must be fewer than the number of nodes.

      - **nodeRangeProperties** *(list) --*

        A list of node ranges and their properties associated with a multi-node parallel job.

        - *(dict) --*

          An object representing the properties of the node range for a multi-node parallel job.

          - **targetNodes** *(string) --*

            The range of nodes, using node index values. A range of ``0:3`` indicates nodes
            with index values of ``0`` through ``3`` . If the starting range value is omitted
            (``:n`` ), then ``0`` is used to start the range. If the ending range value is
            omitted (``n:`` ), then the highest possible node index is used to end the range.
            Your accumulative node ranges must account for all nodes (0:n). You may nest node
            ranges, for example 0:10 and 4:5, in which case the 4:5 range properties override
            the 0:10 properties.

          - **container** *(dict) --*

            The container details for the node range.

            - **image** *(string) --*

              The image used to start a container. This string is passed directly to the Docker
              daemon. Images in the Docker Hub registry are available by default. Other
              repositories are specified with `` *repository-url* /*image* :*tag* `` . Up to
              255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons,
              periods, forward slashes, and number signs are allowed. This parameter maps to
              ``Image`` in the `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
              `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``IMAGE`` parameter of `docker run
              <https://docs.docker.com/engine/reference/run/>`__ .

              * Images in Amazon ECR repositories use the full registry and repository URI (for
              example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ).

              * Images in official repositories on Docker Hub use a single name (for example,
              ``ubuntu`` or ``mongo`` ).

              * Images in other repositories on Docker Hub are qualified with an organization
              name (for example, ``amazon/amazon-ecs-agent`` ).

              * Images in other online repositories are qualified further by a domain name (for
              example, ``quay.io/assemblyline/ubuntu`` ).

            - **vcpus** *(integer) --*

              The number of vCPUs reserved for the container. This parameter maps to
              ``CpuShares`` in the `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
              `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``--cpu-shares`` option to `docker run
              <https://docs.docker.com/engine/reference/run/>`__ . Each vCPU is equivalent to
              1,024 CPU shares. You must specify at least one vCPU.

            - **memory** *(integer) --*

              The hard limit (in MiB) of memory to present to the container. If your container
              attempts to exceed the memory specified here, the container is killed. This
              parameter maps to ``Memory`` in the `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
              `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``--memory`` option to `docker run
              <https://docs.docker.com/engine/reference/run/>`__ . You must specify at least 4
              MiB of memory for a job.

              .. note::

                If you are trying to maximize your resource utilization by providing your jobs
                as much memory as possible for a particular instance type, see `Memory
                Management
                <https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`__
                in the *AWS Batch User Guide* .

            - **command** *(list) --*

              The command that is passed to the container. This parameter maps to ``Cmd`` in
              the `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
              `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``COMMAND`` parameter to `docker run
              <https://docs.docker.com/engine/reference/run/>`__ . For more information, see
              `https\\://docs.docker.com/engine/reference/builder/#cmd
              <https://docs.docker.com/engine/reference/builder/#cmd>`__ .

              - *(string) --*

            - **jobRoleArn** *(string) --*

              The Amazon Resource Name (ARN) of the IAM role that the container can assume for
              AWS permissions.

            - **volumes** *(list) --*

              A list of data volumes used in a job.

              - *(dict) --*

                A data volume used in a job's container properties.

                - **host** *(dict) --*

                  The contents of the ``host`` parameter determine whether your data volume
                  persists on the host container instance and where it is stored. If the host
                  parameter is empty, then the Docker daemon assigns a host path for your data
                  volume. However, the data is not guaranteed to persist after the containers
                  associated with it stop running.

                  - **sourcePath** *(string) --*

                    The path on the host container instance that is presented to the container.
                    If this parameter is empty, then the Docker daemon has assigned a host path
                    for you. If this parameter contains a file location, then the data volume
                    persists at the specified location on the host container instance until you
                    delete it manually. If the source path location does not exist on the host
                    container instance, the Docker daemon creates it. If the location does
                    exist, the contents of the source path folder are exported.

                - **name** *(string) --*

                  The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
                  hyphens, and underscores are allowed. This name is referenced in the
                  ``sourceVolume`` parameter of container definition ``mountPoints`` .

            - **environment** *(list) --*

              The environment variables to pass to a container. This parameter maps to ``Env``
              in the `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
              `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``--env`` option to `docker run
              <https://docs.docker.com/engine/reference/run/>`__ .

              .. warning::

                We do not recommend using plaintext environment variables for sensitive
                information, such as credential data.

              .. note::

                Environment variables must not start with ``AWS_BATCH`` ; this naming
                convention is reserved for variables that are set by the AWS Batch service.

              - *(dict) --*

                A key-value pair object.

                - **name** *(string) --*

                  The name of the key-value pair. For environment variables, this is the name
                  of the environment variable.

                - **value** *(string) --*

                  The value of the key-value pair. For environment variables, this is the value
                  of the environment variable.

            - **mountPoints** *(list) --*

              The mount points for data volumes in your container. This parameter maps to
              ``Volumes`` in the `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
              `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``--volume`` option to `docker run
              <https://docs.docker.com/engine/reference/run/>`__ .

              - *(dict) --*

                Details on a Docker volume mount point that is used in a job's container
                properties. This parameter maps to ``Volumes`` in the `Create a container
                <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
                section of the Docker Remote API and the ``--volume`` option to docker run.

                - **containerPath** *(string) --*

                  The path on the container at which to mount the host volume.

                - **readOnly** *(boolean) --*

                  If this value is ``true`` , the container has read-only access to the volume;
                  otherwise, the container can write to the volume. The default value is
                  ``false`` .

                - **sourceVolume** *(string) --*

                  The name of the volume to mount.

            - **readonlyRootFilesystem** *(boolean) --*

              When this parameter is true, the container is given read-only access to its root
              file system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
              `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``--read-only`` option to ``docker run`` .

            - **privileged** *(boolean) --*

              When this parameter is true, the container is given elevated privileges on the
              host container instance (similar to the ``root`` user). This parameter maps to
              ``Privileged`` in the `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
              `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``--privileged`` option to `docker run
              <https://docs.docker.com/engine/reference/run/>`__ .

            - **ulimits** *(list) --*

              A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits``
              in the `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
              `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``--ulimit`` option to `docker run
              <https://docs.docker.com/engine/reference/run/>`__ .

              - *(dict) --*

                The ``ulimit`` settings to pass to the container.

                - **hardLimit** *(integer) --*

                  The hard limit for the ``ulimit`` type.

                - **name** *(string) --*

                  The ``type`` of the ``ulimit`` .

                - **softLimit** *(integer) --*

                  The soft limit for the ``ulimit`` type.

            - **user** *(string) --*

              The user name to use inside the container. This parameter maps to ``User`` in the
              `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
              `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``--user`` option to `docker run
              <https://docs.docker.com/engine/reference/run/>`__ .

            - **instanceType** *(string) --*

              The instance type to use for a multi-node parallel job. Currently all node groups
              in a multi-node parallel job must use the same instance type. This parameter is
              not valid for single-node container jobs.

            - **resourceRequirements** *(list) --*

              The type and amount of a resource to assign to a container. Currently, the only
              supported resource is ``GPU`` .

              - *(dict) --*

                The type and amount of a resource to assign to a container. Currently, the only
                supported resource type is ``GPU`` .

                - **value** *(string) --*

                  The number of physical GPUs to reserve for the container. The number of GPUs
                  reserved for all containers in a job should not exceed the number of
                  available GPUs on the compute resource that the job is launched on.

                - **type** *(string) --*

                  The type of resource to assign to a container. Currently, the only supported
                  resource type is ``GPU`` .

            - **linuxParameters** *(dict) --*

              Linux-specific modifications that are applied to the container, such as details
              for device mappings.

              - **devices** *(list) --*

                Any host devices to expose to the container. This parameter maps to ``Devices``
                in the `Create a container
                <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of
                the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                ``--device`` option to `docker run
                <https://docs.docker.com/engine/reference/run/>`__ .

                - *(dict) --*

                  An object representing a container instance host device.

                  - **hostPath** *(string) --*

                    The path for the device on the host container instance.

                  - **containerPath** *(string) --*

                    The path inside the container at which to expose the host device. By
                    default the ``hostPath`` value is used.

                  - **permissions** *(list) --*

                    The explicit permissions to provide to the container for the device. By
                    default, the container has permissions for ``read`` , ``write`` , and
                    ``mknod`` for the device.

                    - *(string) --*

    - **arrayProperties** *(dict) --*

      The array properties of the job, if it is an array job.

      - **statusSummary** *(dict) --*

        A summary of the number of array job children in each available job status. This
        parameter is returned for parent array jobs.

        - *(string) --*

          - *(integer) --*

      - **size** *(integer) --*

        The size of the array job. This parameter is returned for parent array jobs.

      - **index** *(integer) --*

        The job index within the array that is associated with this job. This parameter is
        returned for array job children.

    - **timeout** *(dict) --*

      The timeout configuration for the job.

      - **attemptDurationSeconds** *(integer) --*

        The time duration in seconds (measured from the job attempt's ``startedAt`` timestamp)
        after which AWS Batch terminates your jobs if they have not finished.
    """


_ClientDescribeJobsResponseTypeDef = TypedDict(
    "_ClientDescribeJobsResponseTypeDef",
    {"jobs": List[ClientDescribeJobsResponsejobsTypeDef]},
    total=False,
)


class ClientDescribeJobsResponseTypeDef(_ClientDescribeJobsResponseTypeDef):
    """
    Type definition for `ClientDescribeJobs` `Response`

    - **jobs** *(list) --*

      The list of jobs.

      - *(dict) --*

        An object representing an AWS Batch job.

        - **jobName** *(string) --*

          The name of the job.

        - **jobId** *(string) --*

          The ID for the job.

        - **jobQueue** *(string) --*

          The Amazon Resource Name (ARN) of the job queue with which the job is associated.

        - **status** *(string) --*

          The current status for the job.

          .. note::

            If your jobs do not progress to ``STARTING`` , see `Jobs Stuck in RUNNABLE Status
            <https://docs.aws.amazon.com/batch/latest/userguide/troubleshooting.html#job_stuck_in_runnable>`__
            in the troubleshooting section of the *AWS Batch User Guide* .

        - **attempts** *(list) --*

          A list of job attempts associated with this job.

          - *(dict) --*

            An object representing a job attempt.

            - **container** *(dict) --*

              Details about the container in this job attempt.

              - **containerInstanceArn** *(string) --*

                The Amazon Resource Name (ARN) of the Amazon ECS container instance that hosts the
                job attempt.

              - **taskArn** *(string) --*

                The Amazon Resource Name (ARN) of the Amazon ECS task that is associated with the
                job attempt. Each container attempt receives a task ARN when they reach the
                ``STARTING`` status.

              - **exitCode** *(integer) --*

                The exit code for the job attempt. A non-zero exit code is considered a failure.

              - **reason** *(string) --*

                A short (255 max characters) human-readable string to provide additional details
                about a running or stopped container.

              - **logStreamName** *(string) --*

                The name of the CloudWatch Logs log stream associated with the container. The log
                group for AWS Batch jobs is ``/aws/batch/job`` . Each container attempt receives a
                log stream name when they reach the ``RUNNING`` status.

              - **networkInterfaces** *(list) --*

                The network interfaces associated with the job attempt.

                - *(dict) --*

                  An object representing the elastic network interface for a multi-node parallel
                  job node.

                  - **attachmentId** *(string) --*

                    The attachment ID for the network interface.

                  - **ipv6Address** *(string) --*

                    The private IPv6 address for the network interface.

                  - **privateIpv4Address** *(string) --*

                    The private IPv4 address for the network interface.

            - **startedAt** *(integer) --*

              The Unix timestamp (in seconds and milliseconds) for when the attempt was started
              (when the attempt transitioned from the ``STARTING`` state to the ``RUNNING`` state).

            - **stoppedAt** *(integer) --*

              The Unix timestamp (in seconds and milliseconds) for when the attempt was stopped
              (when the attempt transitioned from the ``RUNNING`` state to a terminal state, such
              as ``SUCCEEDED`` or ``FAILED`` ).

            - **statusReason** *(string) --*

              A short, human-readable string to provide additional details about the current status
              of the job attempt.

        - **statusReason** *(string) --*

          A short, human-readable string to provide additional details about the current status of
          the job.

        - **createdAt** *(integer) --*

          The Unix timestamp (in seconds and milliseconds) for when the job was created. For
          non-array jobs and parent array jobs, this is when the job entered the ``SUBMITTED``
          state (at the time  SubmitJob was called). For array child jobs, this is when the child
          job was spawned by its parent and entered the ``PENDING`` state.

        - **retryStrategy** *(dict) --*

          The retry strategy to use for this job if an attempt fails.

          - **attempts** *(integer) --*

            The number of times to move a job to the ``RUNNABLE`` status. You may specify between 1
            and 10 attempts. If the value of ``attempts`` is greater than one, the job is retried
            on failure the same number of attempts as the value.

        - **startedAt** *(integer) --*

          The Unix timestamp (in seconds and milliseconds) for when the job was started (when the
          job transitioned from the ``STARTING`` state to the ``RUNNING`` state).

        - **stoppedAt** *(integer) --*

          The Unix timestamp (in seconds and milliseconds) for when the job was stopped (when the
          job transitioned from the ``RUNNING`` state to a terminal state, such as ``SUCCEEDED`` or
          ``FAILED`` ).

        - **dependsOn** *(list) --*

          A list of job names or IDs on which this job depends.

          - *(dict) --*

            An object representing an AWS Batch job dependency.

            - **jobId** *(string) --*

              The job ID of the AWS Batch job associated with this dependency.

            - **type** *(string) --*

              The type of the job dependency.

        - **jobDefinition** *(string) --*

          The job definition that is used by this job.

        - **parameters** *(dict) --*

          Additional parameters passed to the job that replace parameter substitution placeholders
          or override any corresponding parameter defaults from the job definition.

          - *(string) --*

            - *(string) --*

        - **container** *(dict) --*

          An object representing the details of the container that is associated with the job.

          - **image** *(string) --*

            The image used to start the container.

          - **vcpus** *(integer) --*

            The number of VCPUs allocated for the job.

          - **memory** *(integer) --*

            The number of MiB of memory reserved for the job.

          - **command** *(list) --*

            The command that is passed to the container.

            - *(string) --*

          - **jobRoleArn** *(string) --*

            The Amazon Resource Name (ARN) associated with the job upon execution.

          - **volumes** *(list) --*

            A list of volumes associated with the job.

            - *(dict) --*

              A data volume used in a job's container properties.

              - **host** *(dict) --*

                The contents of the ``host`` parameter determine whether your data volume persists
                on the host container instance and where it is stored. If the host parameter is
                empty, then the Docker daemon assigns a host path for your data volume. However,
                the data is not guaranteed to persist after the containers associated with it stop
                running.

                - **sourcePath** *(string) --*

                  The path on the host container instance that is presented to the container. If
                  this parameter is empty, then the Docker daemon has assigned a host path for you.
                  If this parameter contains a file location, then the data volume persists at the
                  specified location on the host container instance until you delete it manually.
                  If the source path location does not exist on the host container instance, the
                  Docker daemon creates it. If the location does exist, the contents of the source
                  path folder are exported.

              - **name** *(string) --*

                The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
                hyphens, and underscores are allowed. This name is referenced in the
                ``sourceVolume`` parameter of container definition ``mountPoints`` .

          - **environment** *(list) --*

            The environment variables to pass to a container.

            .. note::

              Environment variables must not start with ``AWS_BATCH`` ; this naming convention is
              reserved for variables that are set by the AWS Batch service.

            - *(dict) --*

              A key-value pair object.

              - **name** *(string) --*

                The name of the key-value pair. For environment variables, this is the name of the
                environment variable.

              - **value** *(string) --*

                The value of the key-value pair. For environment variables, this is the value of
                the environment variable.

          - **mountPoints** *(list) --*

            The mount points for data volumes in your container.

            - *(dict) --*

              Details on a Docker volume mount point that is used in a job's container properties.
              This parameter maps to ``Volumes`` in the `Create a container
              <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
              section of the Docker Remote API and the ``--volume`` option to docker run.

              - **containerPath** *(string) --*

                The path on the container at which to mount the host volume.

              - **readOnly** *(boolean) --*

                If this value is ``true`` , the container has read-only access to the volume;
                otherwise, the container can write to the volume. The default value is ``false`` .

              - **sourceVolume** *(string) --*

                The name of the volume to mount.

          - **readonlyRootFilesystem** *(boolean) --*

            When this parameter is true, the container is given read-only access to its root file
            system.

          - **ulimits** *(list) --*

            A list of ``ulimit`` values to set in the container.

            - *(dict) --*

              The ``ulimit`` settings to pass to the container.

              - **hardLimit** *(integer) --*

                The hard limit for the ``ulimit`` type.

              - **name** *(string) --*

                The ``type`` of the ``ulimit`` .

              - **softLimit** *(integer) --*

                The soft limit for the ``ulimit`` type.

          - **privileged** *(boolean) --*

            When this parameter is true, the container is given elevated privileges on the host
            container instance (similar to the ``root`` user).

          - **user** *(string) --*

            The user name to use inside the container.

          - **exitCode** *(integer) --*

            The exit code to return upon completion.

          - **reason** *(string) --*

            A short (255 max characters) human-readable string to provide additional details about
            a running or stopped container.

          - **containerInstanceArn** *(string) --*

            The Amazon Resource Name (ARN) of the container instance on which the container is
            running.

          - **taskArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon ECS task that is associated with the
            container job. Each container attempt receives a task ARN when they reach the
            ``STARTING`` status.

          - **logStreamName** *(string) --*

            The name of the CloudWatch Logs log stream associated with the container. The log group
            for AWS Batch jobs is ``/aws/batch/job`` . Each container attempt receives a log stream
            name when they reach the ``RUNNING`` status.

          - **instanceType** *(string) --*

            The instance type of the underlying host infrastructure of a multi-node parallel job.

          - **networkInterfaces** *(list) --*

            The network interfaces associated with the job.

            - *(dict) --*

              An object representing the elastic network interface for a multi-node parallel job
              node.

              - **attachmentId** *(string) --*

                The attachment ID for the network interface.

              - **ipv6Address** *(string) --*

                The private IPv6 address for the network interface.

              - **privateIpv4Address** *(string) --*

                The private IPv4 address for the network interface.

          - **resourceRequirements** *(list) --*

            The type and amount of a resource to assign to a container. Currently, the only
            supported resource is ``GPU`` .

            - *(dict) --*

              The type and amount of a resource to assign to a container. Currently, the only
              supported resource type is ``GPU`` .

              - **value** *(string) --*

                The number of physical GPUs to reserve for the container. The number of GPUs
                reserved for all containers in a job should not exceed the number of available GPUs
                on the compute resource that the job is launched on.

              - **type** *(string) --*

                The type of resource to assign to a container. Currently, the only supported
                resource type is ``GPU`` .

          - **linuxParameters** *(dict) --*

            Linux-specific modifications that are applied to the container, such as details for
            device mappings.

            - **devices** *(list) --*

              Any host devices to expose to the container. This parameter maps to ``Devices`` in
              the `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
              `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``--device`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__
              .

              - *(dict) --*

                An object representing a container instance host device.

                - **hostPath** *(string) --*

                  The path for the device on the host container instance.

                - **containerPath** *(string) --*

                  The path inside the container at which to expose the host device. By default the
                  ``hostPath`` value is used.

                - **permissions** *(list) --*

                  The explicit permissions to provide to the container for the device. By default,
                  the container has permissions for ``read`` , ``write`` , and ``mknod`` for the
                  device.

                  - *(string) --*

        - **nodeDetails** *(dict) --*

          An object representing the details of a node that is associated with a multi-node
          parallel job.

          - **nodeIndex** *(integer) --*

            The node index for the node. Node index numbering begins at zero. This index is also
            available on the node with the ``AWS_BATCH_JOB_NODE_INDEX`` environment variable.

          - **isMainNode** *(boolean) --*

            Specifies whether the current node is the main node for a multi-node parallel job.

        - **nodeProperties** *(dict) --*

          An object representing the node properties of a multi-node parallel job.

          - **numNodes** *(integer) --*

            The number of nodes associated with a multi-node parallel job.

          - **mainNode** *(integer) --*

            Specifies the node index for the main node of a multi-node parallel job. This node
            index value must be fewer than the number of nodes.

          - **nodeRangeProperties** *(list) --*

            A list of node ranges and their properties associated with a multi-node parallel job.

            - *(dict) --*

              An object representing the properties of the node range for a multi-node parallel job.

              - **targetNodes** *(string) --*

                The range of nodes, using node index values. A range of ``0:3`` indicates nodes
                with index values of ``0`` through ``3`` . If the starting range value is omitted
                (``:n`` ), then ``0`` is used to start the range. If the ending range value is
                omitted (``n:`` ), then the highest possible node index is used to end the range.
                Your accumulative node ranges must account for all nodes (0:n). You may nest node
                ranges, for example 0:10 and 4:5, in which case the 4:5 range properties override
                the 0:10 properties.

              - **container** *(dict) --*

                The container details for the node range.

                - **image** *(string) --*

                  The image used to start a container. This string is passed directly to the Docker
                  daemon. Images in the Docker Hub registry are available by default. Other
                  repositories are specified with `` *repository-url* /*image* :*tag* `` . Up to
                  255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons,
                  periods, forward slashes, and number signs are allowed. This parameter maps to
                  ``Image`` in the `Create a container
                  <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
                  `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                  ``IMAGE`` parameter of `docker run
                  <https://docs.docker.com/engine/reference/run/>`__ .

                  * Images in Amazon ECR repositories use the full registry and repository URI (for
                  example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ).

                  * Images in official repositories on Docker Hub use a single name (for example,
                  ``ubuntu`` or ``mongo`` ).

                  * Images in other repositories on Docker Hub are qualified with an organization
                  name (for example, ``amazon/amazon-ecs-agent`` ).

                  * Images in other online repositories are qualified further by a domain name (for
                  example, ``quay.io/assemblyline/ubuntu`` ).

                - **vcpus** *(integer) --*

                  The number of vCPUs reserved for the container. This parameter maps to
                  ``CpuShares`` in the `Create a container
                  <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
                  `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                  ``--cpu-shares`` option to `docker run
                  <https://docs.docker.com/engine/reference/run/>`__ . Each vCPU is equivalent to
                  1,024 CPU shares. You must specify at least one vCPU.

                - **memory** *(integer) --*

                  The hard limit (in MiB) of memory to present to the container. If your container
                  attempts to exceed the memory specified here, the container is killed. This
                  parameter maps to ``Memory`` in the `Create a container
                  <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
                  `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                  ``--memory`` option to `docker run
                  <https://docs.docker.com/engine/reference/run/>`__ . You must specify at least 4
                  MiB of memory for a job.

                  .. note::

                    If you are trying to maximize your resource utilization by providing your jobs
                    as much memory as possible for a particular instance type, see `Memory
                    Management
                    <https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`__
                    in the *AWS Batch User Guide* .

                - **command** *(list) --*

                  The command that is passed to the container. This parameter maps to ``Cmd`` in
                  the `Create a container
                  <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
                  `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                  ``COMMAND`` parameter to `docker run
                  <https://docs.docker.com/engine/reference/run/>`__ . For more information, see
                  `https\\://docs.docker.com/engine/reference/builder/#cmd
                  <https://docs.docker.com/engine/reference/builder/#cmd>`__ .

                  - *(string) --*

                - **jobRoleArn** *(string) --*

                  The Amazon Resource Name (ARN) of the IAM role that the container can assume for
                  AWS permissions.

                - **volumes** *(list) --*

                  A list of data volumes used in a job.

                  - *(dict) --*

                    A data volume used in a job's container properties.

                    - **host** *(dict) --*

                      The contents of the ``host`` parameter determine whether your data volume
                      persists on the host container instance and where it is stored. If the host
                      parameter is empty, then the Docker daemon assigns a host path for your data
                      volume. However, the data is not guaranteed to persist after the containers
                      associated with it stop running.

                      - **sourcePath** *(string) --*

                        The path on the host container instance that is presented to the container.
                        If this parameter is empty, then the Docker daemon has assigned a host path
                        for you. If this parameter contains a file location, then the data volume
                        persists at the specified location on the host container instance until you
                        delete it manually. If the source path location does not exist on the host
                        container instance, the Docker daemon creates it. If the location does
                        exist, the contents of the source path folder are exported.

                    - **name** *(string) --*

                      The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
                      hyphens, and underscores are allowed. This name is referenced in the
                      ``sourceVolume`` parameter of container definition ``mountPoints`` .

                - **environment** *(list) --*

                  The environment variables to pass to a container. This parameter maps to ``Env``
                  in the `Create a container
                  <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
                  `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                  ``--env`` option to `docker run
                  <https://docs.docker.com/engine/reference/run/>`__ .

                  .. warning::

                    We do not recommend using plaintext environment variables for sensitive
                    information, such as credential data.

                  .. note::

                    Environment variables must not start with ``AWS_BATCH`` ; this naming
                    convention is reserved for variables that are set by the AWS Batch service.

                  - *(dict) --*

                    A key-value pair object.

                    - **name** *(string) --*

                      The name of the key-value pair. For environment variables, this is the name
                      of the environment variable.

                    - **value** *(string) --*

                      The value of the key-value pair. For environment variables, this is the value
                      of the environment variable.

                - **mountPoints** *(list) --*

                  The mount points for data volumes in your container. This parameter maps to
                  ``Volumes`` in the `Create a container
                  <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
                  `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                  ``--volume`` option to `docker run
                  <https://docs.docker.com/engine/reference/run/>`__ .

                  - *(dict) --*

                    Details on a Docker volume mount point that is used in a job's container
                    properties. This parameter maps to ``Volumes`` in the `Create a container
                    <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
                    section of the Docker Remote API and the ``--volume`` option to docker run.

                    - **containerPath** *(string) --*

                      The path on the container at which to mount the host volume.

                    - **readOnly** *(boolean) --*

                      If this value is ``true`` , the container has read-only access to the volume;
                      otherwise, the container can write to the volume. The default value is
                      ``false`` .

                    - **sourceVolume** *(string) --*

                      The name of the volume to mount.

                - **readonlyRootFilesystem** *(boolean) --*

                  When this parameter is true, the container is given read-only access to its root
                  file system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container
                  <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
                  `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                  ``--read-only`` option to ``docker run`` .

                - **privileged** *(boolean) --*

                  When this parameter is true, the container is given elevated privileges on the
                  host container instance (similar to the ``root`` user). This parameter maps to
                  ``Privileged`` in the `Create a container
                  <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
                  `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                  ``--privileged`` option to `docker run
                  <https://docs.docker.com/engine/reference/run/>`__ .

                - **ulimits** *(list) --*

                  A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits``
                  in the `Create a container
                  <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
                  `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                  ``--ulimit`` option to `docker run
                  <https://docs.docker.com/engine/reference/run/>`__ .

                  - *(dict) --*

                    The ``ulimit`` settings to pass to the container.

                    - **hardLimit** *(integer) --*

                      The hard limit for the ``ulimit`` type.

                    - **name** *(string) --*

                      The ``type`` of the ``ulimit`` .

                    - **softLimit** *(integer) --*

                      The soft limit for the ``ulimit`` type.

                - **user** *(string) --*

                  The user name to use inside the container. This parameter maps to ``User`` in the
                  `Create a container
                  <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
                  `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                  ``--user`` option to `docker run
                  <https://docs.docker.com/engine/reference/run/>`__ .

                - **instanceType** *(string) --*

                  The instance type to use for a multi-node parallel job. Currently all node groups
                  in a multi-node parallel job must use the same instance type. This parameter is
                  not valid for single-node container jobs.

                - **resourceRequirements** *(list) --*

                  The type and amount of a resource to assign to a container. Currently, the only
                  supported resource is ``GPU`` .

                  - *(dict) --*

                    The type and amount of a resource to assign to a container. Currently, the only
                    supported resource type is ``GPU`` .

                    - **value** *(string) --*

                      The number of physical GPUs to reserve for the container. The number of GPUs
                      reserved for all containers in a job should not exceed the number of
                      available GPUs on the compute resource that the job is launched on.

                    - **type** *(string) --*

                      The type of resource to assign to a container. Currently, the only supported
                      resource type is ``GPU`` .

                - **linuxParameters** *(dict) --*

                  Linux-specific modifications that are applied to the container, such as details
                  for device mappings.

                  - **devices** *(list) --*

                    Any host devices to expose to the container. This parameter maps to ``Devices``
                    in the `Create a container
                    <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of
                    the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                    ``--device`` option to `docker run
                    <https://docs.docker.com/engine/reference/run/>`__ .

                    - *(dict) --*

                      An object representing a container instance host device.

                      - **hostPath** *(string) --*

                        The path for the device on the host container instance.

                      - **containerPath** *(string) --*

                        The path inside the container at which to expose the host device. By
                        default the ``hostPath`` value is used.

                      - **permissions** *(list) --*

                        The explicit permissions to provide to the container for the device. By
                        default, the container has permissions for ``read`` , ``write`` , and
                        ``mknod`` for the device.

                        - *(string) --*

        - **arrayProperties** *(dict) --*

          The array properties of the job, if it is an array job.

          - **statusSummary** *(dict) --*

            A summary of the number of array job children in each available job status. This
            parameter is returned for parent array jobs.

            - *(string) --*

              - *(integer) --*

          - **size** *(integer) --*

            The size of the array job. This parameter is returned for parent array jobs.

          - **index** *(integer) --*

            The job index within the array that is associated with this job. This parameter is
            returned for array job children.

        - **timeout** *(dict) --*

          The timeout configuration for the job.

          - **attemptDurationSeconds** *(integer) --*

            The time duration in seconds (measured from the job attempt's ``startedAt`` timestamp)
            after which AWS Batch terminates your jobs if they have not finished.
    """


_ClientListJobsResponsejobSummaryListarrayPropertiesTypeDef = TypedDict(
    "_ClientListJobsResponsejobSummaryListarrayPropertiesTypeDef",
    {"size": int, "index": int},
    total=False,
)


class ClientListJobsResponsejobSummaryListarrayPropertiesTypeDef(
    _ClientListJobsResponsejobSummaryListarrayPropertiesTypeDef
):
    """
    Type definition for `ClientListJobsResponsejobSummaryList` `arrayProperties`

    The array properties of the job, if it is an array job.

    - **size** *(integer) --*

      The size of the array job. This parameter is returned for parent array jobs.

    - **index** *(integer) --*

      The job index within the array that is associated with this job. This parameter is
      returned for children of array jobs.
    """


_ClientListJobsResponsejobSummaryListcontainerTypeDef = TypedDict(
    "_ClientListJobsResponsejobSummaryListcontainerTypeDef",
    {"exitCode": int, "reason": str},
    total=False,
)


class ClientListJobsResponsejobSummaryListcontainerTypeDef(
    _ClientListJobsResponsejobSummaryListcontainerTypeDef
):
    """
    Type definition for `ClientListJobsResponsejobSummaryList` `container`

    An object representing the details of the container that is associated with the job.

    - **exitCode** *(integer) --*

      The exit code to return upon completion.

    - **reason** *(string) --*

      A short (255 max characters) human-readable string to provide additional details about
      a running or stopped container.
    """


_ClientListJobsResponsejobSummaryListnodePropertiesTypeDef = TypedDict(
    "_ClientListJobsResponsejobSummaryListnodePropertiesTypeDef",
    {"isMainNode": bool, "numNodes": int, "nodeIndex": int},
    total=False,
)


class ClientListJobsResponsejobSummaryListnodePropertiesTypeDef(
    _ClientListJobsResponsejobSummaryListnodePropertiesTypeDef
):
    """
    Type definition for `ClientListJobsResponsejobSummaryList` `nodeProperties`

    The node properties for a single node in a job summary list.

    - **isMainNode** *(boolean) --*

      Specifies whether the current node is the main node for a multi-node parallel job.

    - **numNodes** *(integer) --*

      The number of nodes associated with a multi-node parallel job.

    - **nodeIndex** *(integer) --*

      The node index for the node. Node index numbering begins at zero. This index is also
      available on the node with the ``AWS_BATCH_JOB_NODE_INDEX`` environment variable.
    """


_ClientListJobsResponsejobSummaryListTypeDef = TypedDict(
    "_ClientListJobsResponsejobSummaryListTypeDef",
    {
        "jobId": str,
        "jobName": str,
        "createdAt": int,
        "status": str,
        "statusReason": str,
        "startedAt": int,
        "stoppedAt": int,
        "container": ClientListJobsResponsejobSummaryListcontainerTypeDef,
        "arrayProperties": ClientListJobsResponsejobSummaryListarrayPropertiesTypeDef,
        "nodeProperties": ClientListJobsResponsejobSummaryListnodePropertiesTypeDef,
    },
    total=False,
)


class ClientListJobsResponsejobSummaryListTypeDef(
    _ClientListJobsResponsejobSummaryListTypeDef
):
    """
    Type definition for `ClientListJobsResponse` `jobSummaryList`

    An object representing summary details of a job.

    - **jobId** *(string) --*

      The ID of the job.

    - **jobName** *(string) --*

      The name of the job.

    - **createdAt** *(integer) --*

      The Unix timestamp for when the job was created. For non-array jobs and parent array
      jobs, this is when the job entered the ``SUBMITTED`` state (at the time  SubmitJob was
      called). For array child jobs, this is when the child job was spawned by its parent and
      entered the ``PENDING`` state.

    - **status** *(string) --*

      The current status for the job.

    - **statusReason** *(string) --*

      A short, human-readable string to provide additional details about the current status of
      the job.

    - **startedAt** *(integer) --*

      The Unix timestamp for when the job was started (when the job transitioned from the
      ``STARTING`` state to the ``RUNNING`` state).

    - **stoppedAt** *(integer) --*

      The Unix timestamp for when the job was stopped (when the job transitioned from the
      ``RUNNING`` state to a terminal state, such as ``SUCCEEDED`` or ``FAILED`` ).

    - **container** *(dict) --*

      An object representing the details of the container that is associated with the job.

      - **exitCode** *(integer) --*

        The exit code to return upon completion.

      - **reason** *(string) --*

        A short (255 max characters) human-readable string to provide additional details about
        a running or stopped container.

    - **arrayProperties** *(dict) --*

      The array properties of the job, if it is an array job.

      - **size** *(integer) --*

        The size of the array job. This parameter is returned for parent array jobs.

      - **index** *(integer) --*

        The job index within the array that is associated with this job. This parameter is
        returned for children of array jobs.

    - **nodeProperties** *(dict) --*

      The node properties for a single node in a job summary list.

      - **isMainNode** *(boolean) --*

        Specifies whether the current node is the main node for a multi-node parallel job.

      - **numNodes** *(integer) --*

        The number of nodes associated with a multi-node parallel job.

      - **nodeIndex** *(integer) --*

        The node index for the node. Node index numbering begins at zero. This index is also
        available on the node with the ``AWS_BATCH_JOB_NODE_INDEX`` environment variable.
    """


_ClientListJobsResponseTypeDef = TypedDict(
    "_ClientListJobsResponseTypeDef",
    {
        "jobSummaryList": List[ClientListJobsResponsejobSummaryListTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListJobsResponseTypeDef(_ClientListJobsResponseTypeDef):
    """
    Type definition for `ClientListJobs` `Response`

    - **jobSummaryList** *(list) --*

      A list of job summaries that match the request.

      - *(dict) --*

        An object representing summary details of a job.

        - **jobId** *(string) --*

          The ID of the job.

        - **jobName** *(string) --*

          The name of the job.

        - **createdAt** *(integer) --*

          The Unix timestamp for when the job was created. For non-array jobs and parent array
          jobs, this is when the job entered the ``SUBMITTED`` state (at the time  SubmitJob was
          called). For array child jobs, this is when the child job was spawned by its parent and
          entered the ``PENDING`` state.

        - **status** *(string) --*

          The current status for the job.

        - **statusReason** *(string) --*

          A short, human-readable string to provide additional details about the current status of
          the job.

        - **startedAt** *(integer) --*

          The Unix timestamp for when the job was started (when the job transitioned from the
          ``STARTING`` state to the ``RUNNING`` state).

        - **stoppedAt** *(integer) --*

          The Unix timestamp for when the job was stopped (when the job transitioned from the
          ``RUNNING`` state to a terminal state, such as ``SUCCEEDED`` or ``FAILED`` ).

        - **container** *(dict) --*

          An object representing the details of the container that is associated with the job.

          - **exitCode** *(integer) --*

            The exit code to return upon completion.

          - **reason** *(string) --*

            A short (255 max characters) human-readable string to provide additional details about
            a running or stopped container.

        - **arrayProperties** *(dict) --*

          The array properties of the job, if it is an array job.

          - **size** *(integer) --*

            The size of the array job. This parameter is returned for parent array jobs.

          - **index** *(integer) --*

            The job index within the array that is associated with this job. This parameter is
            returned for children of array jobs.

        - **nodeProperties** *(dict) --*

          The node properties for a single node in a job summary list.

          - **isMainNode** *(boolean) --*

            Specifies whether the current node is the main node for a multi-node parallel job.

          - **numNodes** *(integer) --*

            The number of nodes associated with a multi-node parallel job.

          - **nodeIndex** *(integer) --*

            The node index for the node. Node index numbering begins at zero. This index is also
            available on the node with the ``AWS_BATCH_JOB_NODE_INDEX`` environment variable.

    - **nextToken** *(string) --*

      The ``nextToken`` value to include in a future ``ListJobs`` request. When the results of a
      ``ListJobs`` request exceed ``maxResults`` , this value can be used to retrieve the next page
      of results. This value is ``null`` when there are no more results to return.
    """


_ClientRegisterJobDefinitionResponseTypeDef = TypedDict(
    "_ClientRegisterJobDefinitionResponseTypeDef",
    {"jobDefinitionName": str, "jobDefinitionArn": str, "revision": int},
    total=False,
)


class ClientRegisterJobDefinitionResponseTypeDef(
    _ClientRegisterJobDefinitionResponseTypeDef
):
    """
    Type definition for `ClientRegisterJobDefinition` `Response`

    - **jobDefinitionName** *(string) --*

      The name of the job definition.

    - **jobDefinitionArn** *(string) --*

      The Amazon Resource Name (ARN) of the job definition.

    - **revision** *(integer) --*

      The revision of the job definition.
    """


_ClientRegisterJobDefinitioncontainerPropertiesenvironmentTypeDef = TypedDict(
    "_ClientRegisterJobDefinitioncontainerPropertiesenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientRegisterJobDefinitioncontainerPropertiesenvironmentTypeDef(
    _ClientRegisterJobDefinitioncontainerPropertiesenvironmentTypeDef
):
    """
    Type definition for `ClientRegisterJobDefinitioncontainerProperties` `environment`

    A key-value pair object.

    - **name** *(string) --*

      The name of the key-value pair. For environment variables, this is the name of the
      environment variable.

    - **value** *(string) --*

      The value of the key-value pair. For environment variables, this is the value of the
      environment variable.
    """


_RequiredClientRegisterJobDefinitioncontainerPropertieslinuxParametersdevicesTypeDef = TypedDict(
    "_RequiredClientRegisterJobDefinitioncontainerPropertieslinuxParametersdevicesTypeDef",
    {"hostPath": str},
)
_OptionalClientRegisterJobDefinitioncontainerPropertieslinuxParametersdevicesTypeDef = TypedDict(
    "_OptionalClientRegisterJobDefinitioncontainerPropertieslinuxParametersdevicesTypeDef",
    {"containerPath": str, "permissions": List[str]},
    total=False,
)


class ClientRegisterJobDefinitioncontainerPropertieslinuxParametersdevicesTypeDef(
    _RequiredClientRegisterJobDefinitioncontainerPropertieslinuxParametersdevicesTypeDef,
    _OptionalClientRegisterJobDefinitioncontainerPropertieslinuxParametersdevicesTypeDef,
):
    """
    Type definition for `ClientRegisterJobDefinitioncontainerPropertieslinuxParameters` `devices`

    An object representing a container instance host device.

    - **hostPath** *(string) --* **[REQUIRED]**

      The path for the device on the host container instance.

    - **containerPath** *(string) --*

      The path inside the container at which to expose the host device. By default the
      ``hostPath`` value is used.

    - **permissions** *(list) --*

      The explicit permissions to provide to the container for the device. By default, the
      container has permissions for ``read`` , ``write`` , and ``mknod`` for the device.

      - *(string) --*
    """


_ClientRegisterJobDefinitioncontainerPropertieslinuxParametersTypeDef = TypedDict(
    "_ClientRegisterJobDefinitioncontainerPropertieslinuxParametersTypeDef",
    {
        "devices": List[
            ClientRegisterJobDefinitioncontainerPropertieslinuxParametersdevicesTypeDef
        ]
    },
    total=False,
)


class ClientRegisterJobDefinitioncontainerPropertieslinuxParametersTypeDef(
    _ClientRegisterJobDefinitioncontainerPropertieslinuxParametersTypeDef
):
    """
    Type definition for `ClientRegisterJobDefinitioncontainerProperties` `linuxParameters`

    Linux-specific modifications that are applied to the container, such as details for device
    mappings.

    - **devices** *(list) --*

      Any host devices to expose to the container. This parameter maps to ``Devices`` in the
      `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section
      of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--device``
      option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

      - *(dict) --*

        An object representing a container instance host device.

        - **hostPath** *(string) --* **[REQUIRED]**

          The path for the device on the host container instance.

        - **containerPath** *(string) --*

          The path inside the container at which to expose the host device. By default the
          ``hostPath`` value is used.

        - **permissions** *(list) --*

          The explicit permissions to provide to the container for the device. By default, the
          container has permissions for ``read`` , ``write`` , and ``mknod`` for the device.

          - *(string) --*
    """


_ClientRegisterJobDefinitioncontainerPropertiesmountPointsTypeDef = TypedDict(
    "_ClientRegisterJobDefinitioncontainerPropertiesmountPointsTypeDef",
    {"containerPath": str, "readOnly": bool, "sourceVolume": str},
    total=False,
)


class ClientRegisterJobDefinitioncontainerPropertiesmountPointsTypeDef(
    _ClientRegisterJobDefinitioncontainerPropertiesmountPointsTypeDef
):
    """
    Type definition for `ClientRegisterJobDefinitioncontainerProperties` `mountPoints`

    Details on a Docker volume mount point that is used in a job's container properties. This
    parameter maps to ``Volumes`` in the `Create a container
    <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
    section of the Docker Remote API and the ``--volume`` option to docker run.

    - **containerPath** *(string) --*

      The path on the container at which to mount the host volume.

    - **readOnly** *(boolean) --*

      If this value is ``true`` , the container has read-only access to the volume; otherwise,
      the container can write to the volume. The default value is ``false`` .

    - **sourceVolume** *(string) --*

      The name of the volume to mount.
    """


_ClientRegisterJobDefinitioncontainerPropertiesresourceRequirementsTypeDef = TypedDict(
    "_ClientRegisterJobDefinitioncontainerPropertiesresourceRequirementsTypeDef",
    {"value": str, "type": str},
)


class ClientRegisterJobDefinitioncontainerPropertiesresourceRequirementsTypeDef(
    _ClientRegisterJobDefinitioncontainerPropertiesresourceRequirementsTypeDef
):
    """
    Type definition for `ClientRegisterJobDefinitioncontainerProperties` `resourceRequirements`

    The type and amount of a resource to assign to a container. Currently, the only supported
    resource type is ``GPU`` .

    - **value** *(string) --* **[REQUIRED]**

      The number of physical GPUs to reserve for the container. The number of GPUs reserved for
      all containers in a job should not exceed the number of available GPUs on the compute
      resource that the job is launched on.

    - **type** *(string) --* **[REQUIRED]**

      The type of resource to assign to a container. Currently, the only supported resource type
      is ``GPU`` .
    """


_ClientRegisterJobDefinitioncontainerPropertiesulimitsTypeDef = TypedDict(
    "_ClientRegisterJobDefinitioncontainerPropertiesulimitsTypeDef",
    {"hardLimit": int, "name": str, "softLimit": int},
)


class ClientRegisterJobDefinitioncontainerPropertiesulimitsTypeDef(
    _ClientRegisterJobDefinitioncontainerPropertiesulimitsTypeDef
):
    """
    Type definition for `ClientRegisterJobDefinitioncontainerProperties` `ulimits`

    The ``ulimit`` settings to pass to the container.

    - **hardLimit** *(integer) --* **[REQUIRED]**

      The hard limit for the ``ulimit`` type.

    - **name** *(string) --* **[REQUIRED]**

      The ``type`` of the ``ulimit`` .

    - **softLimit** *(integer) --* **[REQUIRED]**

      The soft limit for the ``ulimit`` type.
    """


_ClientRegisterJobDefinitioncontainerPropertiesvolumeshostTypeDef = TypedDict(
    "_ClientRegisterJobDefinitioncontainerPropertiesvolumeshostTypeDef",
    {"sourcePath": str},
    total=False,
)


class ClientRegisterJobDefinitioncontainerPropertiesvolumeshostTypeDef(
    _ClientRegisterJobDefinitioncontainerPropertiesvolumeshostTypeDef
):
    """
    Type definition for `ClientRegisterJobDefinitioncontainerPropertiesvolumes` `host`

    The contents of the ``host`` parameter determine whether your data volume persists on the
    host container instance and where it is stored. If the host parameter is empty, then the
    Docker daemon assigns a host path for your data volume. However, the data is not guaranteed
    to persist after the containers associated with it stop running.

    - **sourcePath** *(string) --*

      The path on the host container instance that is presented to the container. If this
      parameter is empty, then the Docker daemon has assigned a host path for you. If this
      parameter contains a file location, then the data volume persists at the specified
      location on the host container instance until you delete it manually. If the source path
      location does not exist on the host container instance, the Docker daemon creates it. If
      the location does exist, the contents of the source path folder are exported.
    """


_ClientRegisterJobDefinitioncontainerPropertiesvolumesTypeDef = TypedDict(
    "_ClientRegisterJobDefinitioncontainerPropertiesvolumesTypeDef",
    {
        "host": ClientRegisterJobDefinitioncontainerPropertiesvolumeshostTypeDef,
        "name": str,
    },
    total=False,
)


class ClientRegisterJobDefinitioncontainerPropertiesvolumesTypeDef(
    _ClientRegisterJobDefinitioncontainerPropertiesvolumesTypeDef
):
    """
    Type definition for `ClientRegisterJobDefinitioncontainerProperties` `volumes`

    A data volume used in a job's container properties.

    - **host** *(dict) --*

      The contents of the ``host`` parameter determine whether your data volume persists on the
      host container instance and where it is stored. If the host parameter is empty, then the
      Docker daemon assigns a host path for your data volume. However, the data is not guaranteed
      to persist after the containers associated with it stop running.

      - **sourcePath** *(string) --*

        The path on the host container instance that is presented to the container. If this
        parameter is empty, then the Docker daemon has assigned a host path for you. If this
        parameter contains a file location, then the data volume persists at the specified
        location on the host container instance until you delete it manually. If the source path
        location does not exist on the host container instance, the Docker daemon creates it. If
        the location does exist, the contents of the source path folder are exported.

    - **name** *(string) --*

      The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and
      underscores are allowed. This name is referenced in the ``sourceVolume`` parameter of
      container definition ``mountPoints`` .
    """


_ClientRegisterJobDefinitioncontainerPropertiesTypeDef = TypedDict(
    "_ClientRegisterJobDefinitioncontainerPropertiesTypeDef",
    {
        "image": str,
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "jobRoleArn": str,
        "volumes": List[ClientRegisterJobDefinitioncontainerPropertiesvolumesTypeDef],
        "environment": List[
            ClientRegisterJobDefinitioncontainerPropertiesenvironmentTypeDef
        ],
        "mountPoints": List[
            ClientRegisterJobDefinitioncontainerPropertiesmountPointsTypeDef
        ],
        "readonlyRootFilesystem": bool,
        "privileged": bool,
        "ulimits": List[ClientRegisterJobDefinitioncontainerPropertiesulimitsTypeDef],
        "user": str,
        "instanceType": str,
        "resourceRequirements": List[
            ClientRegisterJobDefinitioncontainerPropertiesresourceRequirementsTypeDef
        ],
        "linuxParameters": ClientRegisterJobDefinitioncontainerPropertieslinuxParametersTypeDef,
    },
    total=False,
)


class ClientRegisterJobDefinitioncontainerPropertiesTypeDef(
    _ClientRegisterJobDefinitioncontainerPropertiesTypeDef
):
    """
    Type definition for `ClientRegisterJobDefinition` `containerProperties`

    An object with various properties specific to single-node container-based jobs. If the job
    definition's ``type`` parameter is ``container`` , then you must specify either
    ``containerProperties`` or ``nodeProperties`` .

    - **image** *(string) --*

      The image used to start a container. This string is passed directly to the Docker daemon.
      Images in the Docker Hub registry are available by default. Other repositories are specified
      with `` *repository-url* /*image* :*tag* `` . Up to 255 letters (uppercase and lowercase),
      numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed.
      This parameter maps to ``Image`` in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker Remote
      API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``IMAGE`` parameter of `docker run
      <https://docs.docker.com/engine/reference/run/>`__ .

      * Images in Amazon ECR repositories use the full registry and repository URI (for example,
      ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ).

      * Images in official repositories on Docker Hub use a single name (for example, ``ubuntu`` or
      ``mongo`` ).

      * Images in other repositories on Docker Hub are qualified with an organization name (for
      example, ``amazon/amazon-ecs-agent`` ).

      * Images in other online repositories are qualified further by a domain name (for example,
      ``quay.io/assemblyline/ubuntu`` ).

    - **vcpus** *(integer) --*

      The number of vCPUs reserved for the container. This parameter maps to ``CpuShares`` in the
      `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section
      of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--cpu-shares`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
      Each vCPU is equivalent to 1,024 CPU shares. You must specify at least one vCPU.

    - **memory** *(integer) --*

      The hard limit (in MiB) of memory to present to the container. If your container attempts to
      exceed the memory specified here, the container is killed. This parameter maps to ``Memory`` in
      the `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
      section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--memory`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . You
      must specify at least 4 MiB of memory for a job.

      .. note::

        If you are trying to maximize your resource utilization by providing your jobs as much memory
        as possible for a particular instance type, see `Memory Management
        <https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`__ in the *AWS
        Batch User Guide* .

    - **command** *(list) --*

      The command that is passed to the container. This parameter maps to ``Cmd`` in the `Create a
      container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``COMMAND`` parameter
      to `docker run <https://docs.docker.com/engine/reference/run/>`__ . For more information, see
      `https\\://docs.docker.com/engine/reference/builder/#cmd
      <https://docs.docker.com/engine/reference/builder/#cmd>`__ .

      - *(string) --*

    - **jobRoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS
      permissions.

    - **volumes** *(list) --*

      A list of data volumes used in a job.

      - *(dict) --*

        A data volume used in a job's container properties.

        - **host** *(dict) --*

          The contents of the ``host`` parameter determine whether your data volume persists on the
          host container instance and where it is stored. If the host parameter is empty, then the
          Docker daemon assigns a host path for your data volume. However, the data is not guaranteed
          to persist after the containers associated with it stop running.

          - **sourcePath** *(string) --*

            The path on the host container instance that is presented to the container. If this
            parameter is empty, then the Docker daemon has assigned a host path for you. If this
            parameter contains a file location, then the data volume persists at the specified
            location on the host container instance until you delete it manually. If the source path
            location does not exist on the host container instance, the Docker daemon creates it. If
            the location does exist, the contents of the source path folder are exported.

        - **name** *(string) --*

          The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and
          underscores are allowed. This name is referenced in the ``sourceVolume`` parameter of
          container definition ``mountPoints`` .

    - **environment** *(list) --*

      The environment variables to pass to a container. This parameter maps to ``Env`` in the `Create
      a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--env`` option to
      `docker run <https://docs.docker.com/engine/reference/run/>`__ .

      .. warning::

        We do not recommend using plaintext environment variables for sensitive information, such as
        credential data.

      .. note::

        Environment variables must not start with ``AWS_BATCH`` ; this naming convention is reserved
        for variables that are set by the AWS Batch service.

      - *(dict) --*

        A key-value pair object.

        - **name** *(string) --*

          The name of the key-value pair. For environment variables, this is the name of the
          environment variable.

        - **value** *(string) --*

          The value of the key-value pair. For environment variables, this is the value of the
          environment variable.

    - **mountPoints** *(list) --*

      The mount points for data volumes in your container. This parameter maps to ``Volumes`` in the
      `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section
      of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--volume``
      option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

      - *(dict) --*

        Details on a Docker volume mount point that is used in a job's container properties. This
        parameter maps to ``Volumes`` in the `Create a container
        <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
        section of the Docker Remote API and the ``--volume`` option to docker run.

        - **containerPath** *(string) --*

          The path on the container at which to mount the host volume.

        - **readOnly** *(boolean) --*

          If this value is ``true`` , the container has read-only access to the volume; otherwise,
          the container can write to the volume. The default value is ``false`` .

        - **sourceVolume** *(string) --*

          The name of the volume to mount.

    - **readonlyRootFilesystem** *(boolean) --*

      When this parameter is true, the container is given read-only access to its root file system.
      This parameter maps to ``ReadonlyRootfs`` in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker Remote
      API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--read-only`` option to ``docker
      run`` .

    - **privileged** *(boolean) --*

      When this parameter is true, the container is given elevated privileges on the host container
      instance (similar to the ``root`` user). This parameter maps to ``Privileged`` in the `Create a
      container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--privileged``
      option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

    - **ulimits** *(list) --*

      A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits`` in the
      `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section
      of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--ulimit``
      option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

      - *(dict) --*

        The ``ulimit`` settings to pass to the container.

        - **hardLimit** *(integer) --* **[REQUIRED]**

          The hard limit for the ``ulimit`` type.

        - **name** *(string) --* **[REQUIRED]**

          The ``type`` of the ``ulimit`` .

        - **softLimit** *(integer) --* **[REQUIRED]**

          The soft limit for the ``ulimit`` type.

    - **user** *(string) --*

      The user name to use inside the container. This parameter maps to ``User`` in the `Create a
      container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--user`` option to
      `docker run <https://docs.docker.com/engine/reference/run/>`__ .

    - **instanceType** *(string) --*

      The instance type to use for a multi-node parallel job. Currently all node groups in a
      multi-node parallel job must use the same instance type. This parameter is not valid for
      single-node container jobs.

    - **resourceRequirements** *(list) --*

      The type and amount of a resource to assign to a container. Currently, the only supported
      resource is ``GPU`` .

      - *(dict) --*

        The type and amount of a resource to assign to a container. Currently, the only supported
        resource type is ``GPU`` .

        - **value** *(string) --* **[REQUIRED]**

          The number of physical GPUs to reserve for the container. The number of GPUs reserved for
          all containers in a job should not exceed the number of available GPUs on the compute
          resource that the job is launched on.

        - **type** *(string) --* **[REQUIRED]**

          The type of resource to assign to a container. Currently, the only supported resource type
          is ``GPU`` .

    - **linuxParameters** *(dict) --*

      Linux-specific modifications that are applied to the container, such as details for device
      mappings.

      - **devices** *(list) --*

        Any host devices to expose to the container. This parameter maps to ``Devices`` in the
        `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section
        of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--device``
        option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

        - *(dict) --*

          An object representing a container instance host device.

          - **hostPath** *(string) --* **[REQUIRED]**

            The path for the device on the host container instance.

          - **containerPath** *(string) --*

            The path inside the container at which to expose the host device. By default the
            ``hostPath`` value is used.

          - **permissions** *(list) --*

            The explicit permissions to provide to the container for the device. By default, the
            container has permissions for ``read`` , ``write`` , and ``mknod`` for the device.

            - *(string) --*
    """


_ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef = TypedDict(
    "_ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef(
    _ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef
):
    """
    Type definition for `ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainer` `environment`

    A key-value pair object.

    - **name** *(string) --*

      The name of the key-value pair. For environment variables, this is the name of the
      environment variable.

    - **value** *(string) --*

      The value of the key-value pair. For environment variables, this is the value of the
      environment variable.
    """


_RequiredClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef = TypedDict(
    "_RequiredClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef",
    {"hostPath": str},
)
_OptionalClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef = TypedDict(
    "_OptionalClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef",
    {"containerPath": str, "permissions": List[str]},
    total=False,
)


class ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef(
    _RequiredClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef,
    _OptionalClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef,
):
    """
    Type definition for `ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerlinuxParameters` `devices`

    An object representing a container instance host device.

    - **hostPath** *(string) --* **[REQUIRED]**

      The path for the device on the host container instance.

    - **containerPath** *(string) --*

      The path inside the container at which to expose the host device. By default the
      ``hostPath`` value is used.

    - **permissions** *(list) --*

      The explicit permissions to provide to the container for the device. By default,
      the container has permissions for ``read`` , ``write`` , and ``mknod`` for the
      device.

      - *(string) --*
    """


_ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef = TypedDict(
    "_ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef",
    {
        "devices": List[
            ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef
        ]
    },
    total=False,
)


class ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef(
    _ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef
):
    """
    Type definition for `ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainer` `linuxParameters`

    Linux-specific modifications that are applied to the container, such as details for
    device mappings.

    - **devices** *(list) --*

      Any host devices to expose to the container. This parameter maps to ``Devices`` in the
      `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
      section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and
      the ``--device`` option to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ .

      - *(dict) --*

        An object representing a container instance host device.

        - **hostPath** *(string) --* **[REQUIRED]**

          The path for the device on the host container instance.

        - **containerPath** *(string) --*

          The path inside the container at which to expose the host device. By default the
          ``hostPath`` value is used.

        - **permissions** *(list) --*

          The explicit permissions to provide to the container for the device. By default,
          the container has permissions for ``read`` , ``write`` , and ``mknod`` for the
          device.

          - *(string) --*
    """


_ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainermountPointsTypeDef = TypedDict(
    "_ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainermountPointsTypeDef",
    {"containerPath": str, "readOnly": bool, "sourceVolume": str},
    total=False,
)


class ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainermountPointsTypeDef(
    _ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainermountPointsTypeDef
):
    """
    Type definition for `ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainer` `mountPoints`

    Details on a Docker volume mount point that is used in a job's container properties.
    This parameter maps to ``Volumes`` in the `Create a container
    <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
    section of the Docker Remote API and the ``--volume`` option to docker run.

    - **containerPath** *(string) --*

      The path on the container at which to mount the host volume.

    - **readOnly** *(boolean) --*

      If this value is ``true`` , the container has read-only access to the volume;
      otherwise, the container can write to the volume. The default value is ``false`` .

    - **sourceVolume** *(string) --*

      The name of the volume to mount.
    """


_ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef = TypedDict(
    "_ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef",
    {"value": str, "type": str},
)


class ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef(
    _ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef
):
    """
    Type definition for `ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainer` `resourceRequirements`

    The type and amount of a resource to assign to a container. Currently, the only
    supported resource type is ``GPU`` .

    - **value** *(string) --* **[REQUIRED]**

      The number of physical GPUs to reserve for the container. The number of GPUs reserved
      for all containers in a job should not exceed the number of available GPUs on the
      compute resource that the job is launched on.

    - **type** *(string) --* **[REQUIRED]**

      The type of resource to assign to a container. Currently, the only supported resource
      type is ``GPU`` .
    """


_ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerulimitsTypeDef = TypedDict(
    "_ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerulimitsTypeDef",
    {"hardLimit": int, "name": str, "softLimit": int},
)


class ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerulimitsTypeDef(
    _ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerulimitsTypeDef
):
    """
    Type definition for `ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainer` `ulimits`

    The ``ulimit`` settings to pass to the container.

    - **hardLimit** *(integer) --* **[REQUIRED]**

      The hard limit for the ``ulimit`` type.

    - **name** *(string) --* **[REQUIRED]**

      The ``type`` of the ``ulimit`` .

    - **softLimit** *(integer) --* **[REQUIRED]**

      The soft limit for the ``ulimit`` type.
    """


_ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef = TypedDict(
    "_ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef",
    {"sourcePath": str},
    total=False,
)


class ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef(
    _ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef
):
    """
    Type definition for `ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainervolumes` `host`

    The contents of the ``host`` parameter determine whether your data volume persists on
    the host container instance and where it is stored. If the host parameter is empty,
    then the Docker daemon assigns a host path for your data volume. However, the data is
    not guaranteed to persist after the containers associated with it stop running.

    - **sourcePath** *(string) --*

      The path on the host container instance that is presented to the container. If this
      parameter is empty, then the Docker daemon has assigned a host path for you. If
      this parameter contains a file location, then the data volume persists at the
      specified location on the host container instance until you delete it manually. If
      the source path location does not exist on the host container instance, the Docker
      daemon creates it. If the location does exist, the contents of the source path
      folder are exported.
    """


_ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainervolumesTypeDef = TypedDict(
    "_ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainervolumesTypeDef",
    {
        "host": ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef,
        "name": str,
    },
    total=False,
)


class ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainervolumesTypeDef(
    _ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainervolumesTypeDef
):
    """
    Type definition for `ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainer` `volumes`

    A data volume used in a job's container properties.

    - **host** *(dict) --*

      The contents of the ``host`` parameter determine whether your data volume persists on
      the host container instance and where it is stored. If the host parameter is empty,
      then the Docker daemon assigns a host path for your data volume. However, the data is
      not guaranteed to persist after the containers associated with it stop running.

      - **sourcePath** *(string) --*

        The path on the host container instance that is presented to the container. If this
        parameter is empty, then the Docker daemon has assigned a host path for you. If
        this parameter contains a file location, then the data volume persists at the
        specified location on the host container instance until you delete it manually. If
        the source path location does not exist on the host container instance, the Docker
        daemon creates it. If the location does exist, the contents of the source path
        folder are exported.

    - **name** *(string) --*

      The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
      hyphens, and underscores are allowed. This name is referenced in the ``sourceVolume``
      parameter of container definition ``mountPoints`` .
    """


_ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerTypeDef = TypedDict(
    "_ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerTypeDef",
    {
        "image": str,
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "jobRoleArn": str,
        "volumes": List[
            ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainervolumesTypeDef
        ],
        "environment": List[
            ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef
        ],
        "mountPoints": List[
            ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainermountPointsTypeDef
        ],
        "readonlyRootFilesystem": bool,
        "privileged": bool,
        "ulimits": List[
            ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerulimitsTypeDef
        ],
        "user": str,
        "instanceType": str,
        "resourceRequirements": List[
            ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef
        ],
        "linuxParameters": ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef,
    },
    total=False,
)


class ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerTypeDef(
    _ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerTypeDef
):
    """
    Type definition for `ClientRegisterJobDefinitionnodePropertiesnodeRangeProperties` `container`

    The container details for the node range.

    - **image** *(string) --*

      The image used to start a container. This string is passed directly to the Docker daemon.
      Images in the Docker Hub registry are available by default. Other repositories are
      specified with `` *repository-url* /*image* :*tag* `` . Up to 255 letters (uppercase and
      lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number
      signs are allowed. This parameter maps to ``Image`` in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker
      Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``IMAGE`` parameter of
      `docker run <https://docs.docker.com/engine/reference/run/>`__ .

      * Images in Amazon ECR repositories use the full registry and repository URI (for
      example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ).

      * Images in official repositories on Docker Hub use a single name (for example,
      ``ubuntu`` or ``mongo`` ).

      * Images in other repositories on Docker Hub are qualified with an organization name (for
      example, ``amazon/amazon-ecs-agent`` ).

      * Images in other online repositories are qualified further by a domain name (for
      example, ``quay.io/assemblyline/ubuntu`` ).

    - **vcpus** *(integer) --*

      The number of vCPUs reserved for the container. This parameter maps to ``CpuShares`` in
      the `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
      section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--cpu-shares`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__
      . Each vCPU is equivalent to 1,024 CPU shares. You must specify at least one vCPU.

    - **memory** *(integer) --*

      The hard limit (in MiB) of memory to present to the container. If your container attempts
      to exceed the memory specified here, the container is killed. This parameter maps to
      ``Memory`` in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker
      Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--memory`` option to
      `docker run <https://docs.docker.com/engine/reference/run/>`__ . You must specify at
      least 4 MiB of memory for a job.

      .. note::

        If you are trying to maximize your resource utilization by providing your jobs as much
        memory as possible for a particular instance type, see `Memory Management
        <https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`__ in the
        *AWS Batch User Guide* .

    - **command** *(list) --*

      The command that is passed to the container. This parameter maps to ``Cmd`` in the
      `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
      section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``COMMAND`` parameter to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
      For more information, see `https\\://docs.docker.com/engine/reference/builder/#cmd
      <https://docs.docker.com/engine/reference/builder/#cmd>`__ .

      - *(string) --*

    - **jobRoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS
      permissions.

    - **volumes** *(list) --*

      A list of data volumes used in a job.

      - *(dict) --*

        A data volume used in a job's container properties.

        - **host** *(dict) --*

          The contents of the ``host`` parameter determine whether your data volume persists on
          the host container instance and where it is stored. If the host parameter is empty,
          then the Docker daemon assigns a host path for your data volume. However, the data is
          not guaranteed to persist after the containers associated with it stop running.

          - **sourcePath** *(string) --*

            The path on the host container instance that is presented to the container. If this
            parameter is empty, then the Docker daemon has assigned a host path for you. If
            this parameter contains a file location, then the data volume persists at the
            specified location on the host container instance until you delete it manually. If
            the source path location does not exist on the host container instance, the Docker
            daemon creates it. If the location does exist, the contents of the source path
            folder are exported.

        - **name** *(string) --*

          The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
          hyphens, and underscores are allowed. This name is referenced in the ``sourceVolume``
          parameter of container definition ``mountPoints`` .

    - **environment** *(list) --*

      The environment variables to pass to a container. This parameter maps to ``Env`` in the
      `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
      section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--env`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

      .. warning::

        We do not recommend using plaintext environment variables for sensitive information,
        such as credential data.

      .. note::

        Environment variables must not start with ``AWS_BATCH`` ; this naming convention is
        reserved for variables that are set by the AWS Batch service.

      - *(dict) --*

        A key-value pair object.

        - **name** *(string) --*

          The name of the key-value pair. For environment variables, this is the name of the
          environment variable.

        - **value** *(string) --*

          The value of the key-value pair. For environment variables, this is the value of the
          environment variable.

    - **mountPoints** *(list) --*

      The mount points for data volumes in your container. This parameter maps to ``Volumes``
      in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker
      Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--volume`` option to
      `docker run <https://docs.docker.com/engine/reference/run/>`__ .

      - *(dict) --*

        Details on a Docker volume mount point that is used in a job's container properties.
        This parameter maps to ``Volumes`` in the `Create a container
        <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
        section of the Docker Remote API and the ``--volume`` option to docker run.

        - **containerPath** *(string) --*

          The path on the container at which to mount the host volume.

        - **readOnly** *(boolean) --*

          If this value is ``true`` , the container has read-only access to the volume;
          otherwise, the container can write to the volume. The default value is ``false`` .

        - **sourceVolume** *(string) --*

          The name of the volume to mount.

    - **readonlyRootFilesystem** *(boolean) --*

      When this parameter is true, the container is given read-only access to its root file
      system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker
      Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--read-only`` option
      to ``docker run`` .

    - **privileged** *(boolean) --*

      When this parameter is true, the container is given elevated privileges on the host
      container instance (similar to the ``root`` user). This parameter maps to ``Privileged``
      in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker
      Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--privileged`` option
      to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

    - **ulimits** *(list) --*

      A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits`` in the
      `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
      section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--ulimit`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

      - *(dict) --*

        The ``ulimit`` settings to pass to the container.

        - **hardLimit** *(integer) --* **[REQUIRED]**

          The hard limit for the ``ulimit`` type.

        - **name** *(string) --* **[REQUIRED]**

          The ``type`` of the ``ulimit`` .

        - **softLimit** *(integer) --* **[REQUIRED]**

          The soft limit for the ``ulimit`` type.

    - **user** *(string) --*

      The user name to use inside the container. This parameter maps to ``User`` in the `Create
      a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of
      the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--user``
      option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

    - **instanceType** *(string) --*

      The instance type to use for a multi-node parallel job. Currently all node groups in a
      multi-node parallel job must use the same instance type. This parameter is not valid for
      single-node container jobs.

    - **resourceRequirements** *(list) --*

      The type and amount of a resource to assign to a container. Currently, the only supported
      resource is ``GPU`` .

      - *(dict) --*

        The type and amount of a resource to assign to a container. Currently, the only
        supported resource type is ``GPU`` .

        - **value** *(string) --* **[REQUIRED]**

          The number of physical GPUs to reserve for the container. The number of GPUs reserved
          for all containers in a job should not exceed the number of available GPUs on the
          compute resource that the job is launched on.

        - **type** *(string) --* **[REQUIRED]**

          The type of resource to assign to a container. Currently, the only supported resource
          type is ``GPU`` .

    - **linuxParameters** *(dict) --*

      Linux-specific modifications that are applied to the container, such as details for
      device mappings.

      - **devices** *(list) --*

        Any host devices to expose to the container. This parameter maps to ``Devices`` in the
        `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
        section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and
        the ``--device`` option to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ .

        - *(dict) --*

          An object representing a container instance host device.

          - **hostPath** *(string) --* **[REQUIRED]**

            The path for the device on the host container instance.

          - **containerPath** *(string) --*

            The path inside the container at which to expose the host device. By default the
            ``hostPath`` value is used.

          - **permissions** *(list) --*

            The explicit permissions to provide to the container for the device. By default,
            the container has permissions for ``read`` , ``write`` , and ``mknod`` for the
            device.

            - *(string) --*
    """


_RequiredClientRegisterJobDefinitionnodePropertiesnodeRangePropertiesTypeDef = TypedDict(
    "_RequiredClientRegisterJobDefinitionnodePropertiesnodeRangePropertiesTypeDef",
    {"targetNodes": str},
)
_OptionalClientRegisterJobDefinitionnodePropertiesnodeRangePropertiesTypeDef = TypedDict(
    "_OptionalClientRegisterJobDefinitionnodePropertiesnodeRangePropertiesTypeDef",
    {
        "container": ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiescontainerTypeDef
    },
    total=False,
)


class ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiesTypeDef(
    _RequiredClientRegisterJobDefinitionnodePropertiesnodeRangePropertiesTypeDef,
    _OptionalClientRegisterJobDefinitionnodePropertiesnodeRangePropertiesTypeDef,
):
    """
    Type definition for `ClientRegisterJobDefinitionnodeProperties` `nodeRangeProperties`

    An object representing the properties of the node range for a multi-node parallel job.

    - **targetNodes** *(string) --* **[REQUIRED]**

      The range of nodes, using node index values. A range of ``0:3`` indicates nodes with index
      values of ``0`` through ``3`` . If the starting range value is omitted (``:n`` ), then
      ``0`` is used to start the range. If the ending range value is omitted (``n:`` ), then the
      highest possible node index is used to end the range. Your accumulative node ranges must
      account for all nodes (0:n). You may nest node ranges, for example 0:10 and 4:5, in which
      case the 4:5 range properties override the 0:10 properties.

    - **container** *(dict) --*

      The container details for the node range.

      - **image** *(string) --*

        The image used to start a container. This string is passed directly to the Docker daemon.
        Images in the Docker Hub registry are available by default. Other repositories are
        specified with `` *repository-url* /*image* :*tag* `` . Up to 255 letters (uppercase and
        lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number
        signs are allowed. This parameter maps to ``Image`` in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker
        Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``IMAGE`` parameter of
        `docker run <https://docs.docker.com/engine/reference/run/>`__ .

        * Images in Amazon ECR repositories use the full registry and repository URI (for
        example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ).

        * Images in official repositories on Docker Hub use a single name (for example,
        ``ubuntu`` or ``mongo`` ).

        * Images in other repositories on Docker Hub are qualified with an organization name (for
        example, ``amazon/amazon-ecs-agent`` ).

        * Images in other online repositories are qualified further by a domain name (for
        example, ``quay.io/assemblyline/ubuntu`` ).

      - **vcpus** *(integer) --*

        The number of vCPUs reserved for the container. This parameter maps to ``CpuShares`` in
        the `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
        section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--cpu-shares`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__
        . Each vCPU is equivalent to 1,024 CPU shares. You must specify at least one vCPU.

      - **memory** *(integer) --*

        The hard limit (in MiB) of memory to present to the container. If your container attempts
        to exceed the memory specified here, the container is killed. This parameter maps to
        ``Memory`` in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker
        Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--memory`` option to
        `docker run <https://docs.docker.com/engine/reference/run/>`__ . You must specify at
        least 4 MiB of memory for a job.

        .. note::

          If you are trying to maximize your resource utilization by providing your jobs as much
          memory as possible for a particular instance type, see `Memory Management
          <https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`__ in the
          *AWS Batch User Guide* .

      - **command** *(list) --*

        The command that is passed to the container. This parameter maps to ``Cmd`` in the
        `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
        section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``COMMAND`` parameter to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
        For more information, see `https\\://docs.docker.com/engine/reference/builder/#cmd
        <https://docs.docker.com/engine/reference/builder/#cmd>`__ .

        - *(string) --*

      - **jobRoleArn** *(string) --*

        The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS
        permissions.

      - **volumes** *(list) --*

        A list of data volumes used in a job.

        - *(dict) --*

          A data volume used in a job's container properties.

          - **host** *(dict) --*

            The contents of the ``host`` parameter determine whether your data volume persists on
            the host container instance and where it is stored. If the host parameter is empty,
            then the Docker daemon assigns a host path for your data volume. However, the data is
            not guaranteed to persist after the containers associated with it stop running.

            - **sourcePath** *(string) --*

              The path on the host container instance that is presented to the container. If this
              parameter is empty, then the Docker daemon has assigned a host path for you. If
              this parameter contains a file location, then the data volume persists at the
              specified location on the host container instance until you delete it manually. If
              the source path location does not exist on the host container instance, the Docker
              daemon creates it. If the location does exist, the contents of the source path
              folder are exported.

          - **name** *(string) --*

            The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
            hyphens, and underscores are allowed. This name is referenced in the ``sourceVolume``
            parameter of container definition ``mountPoints`` .

      - **environment** *(list) --*

        The environment variables to pass to a container. This parameter maps to ``Env`` in the
        `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
        section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--env`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

        .. warning::

          We do not recommend using plaintext environment variables for sensitive information,
          such as credential data.

        .. note::

          Environment variables must not start with ``AWS_BATCH`` ; this naming convention is
          reserved for variables that are set by the AWS Batch service.

        - *(dict) --*

          A key-value pair object.

          - **name** *(string) --*

            The name of the key-value pair. For environment variables, this is the name of the
            environment variable.

          - **value** *(string) --*

            The value of the key-value pair. For environment variables, this is the value of the
            environment variable.

      - **mountPoints** *(list) --*

        The mount points for data volumes in your container. This parameter maps to ``Volumes``
        in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker
        Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--volume`` option to
        `docker run <https://docs.docker.com/engine/reference/run/>`__ .

        - *(dict) --*

          Details on a Docker volume mount point that is used in a job's container properties.
          This parameter maps to ``Volumes`` in the `Create a container
          <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
          section of the Docker Remote API and the ``--volume`` option to docker run.

          - **containerPath** *(string) --*

            The path on the container at which to mount the host volume.

          - **readOnly** *(boolean) --*

            If this value is ``true`` , the container has read-only access to the volume;
            otherwise, the container can write to the volume. The default value is ``false`` .

          - **sourceVolume** *(string) --*

            The name of the volume to mount.

      - **readonlyRootFilesystem** *(boolean) --*

        When this parameter is true, the container is given read-only access to its root file
        system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker
        Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--read-only`` option
        to ``docker run`` .

      - **privileged** *(boolean) --*

        When this parameter is true, the container is given elevated privileges on the host
        container instance (similar to the ``root`` user). This parameter maps to ``Privileged``
        in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker
        Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--privileged`` option
        to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

      - **ulimits** *(list) --*

        A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits`` in the
        `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
        section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--ulimit`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

        - *(dict) --*

          The ``ulimit`` settings to pass to the container.

          - **hardLimit** *(integer) --* **[REQUIRED]**

            The hard limit for the ``ulimit`` type.

          - **name** *(string) --* **[REQUIRED]**

            The ``type`` of the ``ulimit`` .

          - **softLimit** *(integer) --* **[REQUIRED]**

            The soft limit for the ``ulimit`` type.

      - **user** *(string) --*

        The user name to use inside the container. This parameter maps to ``User`` in the `Create
        a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of
        the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--user``
        option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

      - **instanceType** *(string) --*

        The instance type to use for a multi-node parallel job. Currently all node groups in a
        multi-node parallel job must use the same instance type. This parameter is not valid for
        single-node container jobs.

      - **resourceRequirements** *(list) --*

        The type and amount of a resource to assign to a container. Currently, the only supported
        resource is ``GPU`` .

        - *(dict) --*

          The type and amount of a resource to assign to a container. Currently, the only
          supported resource type is ``GPU`` .

          - **value** *(string) --* **[REQUIRED]**

            The number of physical GPUs to reserve for the container. The number of GPUs reserved
            for all containers in a job should not exceed the number of available GPUs on the
            compute resource that the job is launched on.

          - **type** *(string) --* **[REQUIRED]**

            The type of resource to assign to a container. Currently, the only supported resource
            type is ``GPU`` .

      - **linuxParameters** *(dict) --*

        Linux-specific modifications that are applied to the container, such as details for
        device mappings.

        - **devices** *(list) --*

          Any host devices to expose to the container. This parameter maps to ``Devices`` in the
          `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
          section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and
          the ``--device`` option to `docker run
          <https://docs.docker.com/engine/reference/run/>`__ .

          - *(dict) --*

            An object representing a container instance host device.

            - **hostPath** *(string) --* **[REQUIRED]**

              The path for the device on the host container instance.

            - **containerPath** *(string) --*

              The path inside the container at which to expose the host device. By default the
              ``hostPath`` value is used.

            - **permissions** *(list) --*

              The explicit permissions to provide to the container for the device. By default,
              the container has permissions for ``read`` , ``write`` , and ``mknod`` for the
              device.

              - *(string) --*
    """


_ClientRegisterJobDefinitionnodePropertiesTypeDef = TypedDict(
    "_ClientRegisterJobDefinitionnodePropertiesTypeDef",
    {
        "numNodes": int,
        "mainNode": int,
        "nodeRangeProperties": List[
            ClientRegisterJobDefinitionnodePropertiesnodeRangePropertiesTypeDef
        ],
    },
)


class ClientRegisterJobDefinitionnodePropertiesTypeDef(
    _ClientRegisterJobDefinitionnodePropertiesTypeDef
):
    """
    Type definition for `ClientRegisterJobDefinition` `nodeProperties`

    An object with various properties specific to multi-node parallel jobs. If you specify node
    properties for a job, it becomes a multi-node parallel job. For more information, see `Multi-node
    Parallel Jobs
    <https://docs.aws.amazon.com/batch/latest/userguide/multi-node-parallel-jobs.html>`__ in the *AWS
    Batch User Guide* . If the job definition's ``type`` parameter is ``container`` , then you must
    specify either ``containerProperties`` or ``nodeProperties`` .

    - **numNodes** *(integer) --* **[REQUIRED]**

      The number of nodes associated with a multi-node parallel job.

    - **mainNode** *(integer) --* **[REQUIRED]**

      Specifies the node index for the main node of a multi-node parallel job. This node index value
      must be fewer than the number of nodes.

    - **nodeRangeProperties** *(list) --* **[REQUIRED]**

      A list of node ranges and their properties associated with a multi-node parallel job.

      - *(dict) --*

        An object representing the properties of the node range for a multi-node parallel job.

        - **targetNodes** *(string) --* **[REQUIRED]**

          The range of nodes, using node index values. A range of ``0:3`` indicates nodes with index
          values of ``0`` through ``3`` . If the starting range value is omitted (``:n`` ), then
          ``0`` is used to start the range. If the ending range value is omitted (``n:`` ), then the
          highest possible node index is used to end the range. Your accumulative node ranges must
          account for all nodes (0:n). You may nest node ranges, for example 0:10 and 4:5, in which
          case the 4:5 range properties override the 0:10 properties.

        - **container** *(dict) --*

          The container details for the node range.

          - **image** *(string) --*

            The image used to start a container. This string is passed directly to the Docker daemon.
            Images in the Docker Hub registry are available by default. Other repositories are
            specified with `` *repository-url* /*image* :*tag* `` . Up to 255 letters (uppercase and
            lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number
            signs are allowed. This parameter maps to ``Image`` in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker
            Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``IMAGE`` parameter of
            `docker run <https://docs.docker.com/engine/reference/run/>`__ .

            * Images in Amazon ECR repositories use the full registry and repository URI (for
            example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ).

            * Images in official repositories on Docker Hub use a single name (for example,
            ``ubuntu`` or ``mongo`` ).

            * Images in other repositories on Docker Hub are qualified with an organization name (for
            example, ``amazon/amazon-ecs-agent`` ).

            * Images in other online repositories are qualified further by a domain name (for
            example, ``quay.io/assemblyline/ubuntu`` ).

          - **vcpus** *(integer) --*

            The number of vCPUs reserved for the container. This parameter maps to ``CpuShares`` in
            the `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
            section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``--cpu-shares`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__
            . Each vCPU is equivalent to 1,024 CPU shares. You must specify at least one vCPU.

          - **memory** *(integer) --*

            The hard limit (in MiB) of memory to present to the container. If your container attempts
            to exceed the memory specified here, the container is killed. This parameter maps to
            ``Memory`` in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker
            Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--memory`` option to
            `docker run <https://docs.docker.com/engine/reference/run/>`__ . You must specify at
            least 4 MiB of memory for a job.

            .. note::

              If you are trying to maximize your resource utilization by providing your jobs as much
              memory as possible for a particular instance type, see `Memory Management
              <https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`__ in the
              *AWS Batch User Guide* .

          - **command** *(list) --*

            The command that is passed to the container. This parameter maps to ``Cmd`` in the
            `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
            section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``COMMAND`` parameter to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
            For more information, see `https\\://docs.docker.com/engine/reference/builder/#cmd
            <https://docs.docker.com/engine/reference/builder/#cmd>`__ .

            - *(string) --*

          - **jobRoleArn** *(string) --*

            The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS
            permissions.

          - **volumes** *(list) --*

            A list of data volumes used in a job.

            - *(dict) --*

              A data volume used in a job's container properties.

              - **host** *(dict) --*

                The contents of the ``host`` parameter determine whether your data volume persists on
                the host container instance and where it is stored. If the host parameter is empty,
                then the Docker daemon assigns a host path for your data volume. However, the data is
                not guaranteed to persist after the containers associated with it stop running.

                - **sourcePath** *(string) --*

                  The path on the host container instance that is presented to the container. If this
                  parameter is empty, then the Docker daemon has assigned a host path for you. If
                  this parameter contains a file location, then the data volume persists at the
                  specified location on the host container instance until you delete it manually. If
                  the source path location does not exist on the host container instance, the Docker
                  daemon creates it. If the location does exist, the contents of the source path
                  folder are exported.

              - **name** *(string) --*

                The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
                hyphens, and underscores are allowed. This name is referenced in the ``sourceVolume``
                parameter of container definition ``mountPoints`` .

          - **environment** *(list) --*

            The environment variables to pass to a container. This parameter maps to ``Env`` in the
            `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
            section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``--env`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

            .. warning::

              We do not recommend using plaintext environment variables for sensitive information,
              such as credential data.

            .. note::

              Environment variables must not start with ``AWS_BATCH`` ; this naming convention is
              reserved for variables that are set by the AWS Batch service.

            - *(dict) --*

              A key-value pair object.

              - **name** *(string) --*

                The name of the key-value pair. For environment variables, this is the name of the
                environment variable.

              - **value** *(string) --*

                The value of the key-value pair. For environment variables, this is the value of the
                environment variable.

          - **mountPoints** *(list) --*

            The mount points for data volumes in your container. This parameter maps to ``Volumes``
            in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker
            Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--volume`` option to
            `docker run <https://docs.docker.com/engine/reference/run/>`__ .

            - *(dict) --*

              Details on a Docker volume mount point that is used in a job's container properties.
              This parameter maps to ``Volumes`` in the `Create a container
              <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
              section of the Docker Remote API and the ``--volume`` option to docker run.

              - **containerPath** *(string) --*

                The path on the container at which to mount the host volume.

              - **readOnly** *(boolean) --*

                If this value is ``true`` , the container has read-only access to the volume;
                otherwise, the container can write to the volume. The default value is ``false`` .

              - **sourceVolume** *(string) --*

                The name of the volume to mount.

          - **readonlyRootFilesystem** *(boolean) --*

            When this parameter is true, the container is given read-only access to its root file
            system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker
            Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--read-only`` option
            to ``docker run`` .

          - **privileged** *(boolean) --*

            When this parameter is true, the container is given elevated privileges on the host
            container instance (similar to the ``root`` user). This parameter maps to ``Privileged``
            in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker
            Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--privileged`` option
            to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

          - **ulimits** *(list) --*

            A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits`` in the
            `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
            section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``--ulimit`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

            - *(dict) --*

              The ``ulimit`` settings to pass to the container.

              - **hardLimit** *(integer) --* **[REQUIRED]**

                The hard limit for the ``ulimit`` type.

              - **name** *(string) --* **[REQUIRED]**

                The ``type`` of the ``ulimit`` .

              - **softLimit** *(integer) --* **[REQUIRED]**

                The soft limit for the ``ulimit`` type.

          - **user** *(string) --*

            The user name to use inside the container. This parameter maps to ``User`` in the `Create
            a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of
            the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--user``
            option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

          - **instanceType** *(string) --*

            The instance type to use for a multi-node parallel job. Currently all node groups in a
            multi-node parallel job must use the same instance type. This parameter is not valid for
            single-node container jobs.

          - **resourceRequirements** *(list) --*

            The type and amount of a resource to assign to a container. Currently, the only supported
            resource is ``GPU`` .

            - *(dict) --*

              The type and amount of a resource to assign to a container. Currently, the only
              supported resource type is ``GPU`` .

              - **value** *(string) --* **[REQUIRED]**

                The number of physical GPUs to reserve for the container. The number of GPUs reserved
                for all containers in a job should not exceed the number of available GPUs on the
                compute resource that the job is launched on.

              - **type** *(string) --* **[REQUIRED]**

                The type of resource to assign to a container. Currently, the only supported resource
                type is ``GPU`` .

          - **linuxParameters** *(dict) --*

            Linux-specific modifications that are applied to the container, such as details for
            device mappings.

            - **devices** *(list) --*

              Any host devices to expose to the container. This parameter maps to ``Devices`` in the
              `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
              section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and
              the ``--device`` option to `docker run
              <https://docs.docker.com/engine/reference/run/>`__ .

              - *(dict) --*

                An object representing a container instance host device.

                - **hostPath** *(string) --* **[REQUIRED]**

                  The path for the device on the host container instance.

                - **containerPath** *(string) --*

                  The path inside the container at which to expose the host device. By default the
                  ``hostPath`` value is used.

                - **permissions** *(list) --*

                  The explicit permissions to provide to the container for the device. By default,
                  the container has permissions for ``read`` , ``write`` , and ``mknod`` for the
                  device.

                  - *(string) --*
    """


_ClientRegisterJobDefinitionretryStrategyTypeDef = TypedDict(
    "_ClientRegisterJobDefinitionretryStrategyTypeDef", {"attempts": int}, total=False
)


class ClientRegisterJobDefinitionretryStrategyTypeDef(
    _ClientRegisterJobDefinitionretryStrategyTypeDef
):
    """
    Type definition for `ClientRegisterJobDefinition` `retryStrategy`

    The retry strategy to use for failed jobs that are submitted with this job definition. Any retry
    strategy that is specified during a  SubmitJob operation overrides the retry strategy defined
    here. If a job is terminated due to a timeout, it is not retried.

    - **attempts** *(integer) --*

      The number of times to move a job to the ``RUNNABLE`` status. You may specify between 1 and 10
      attempts. If the value of ``attempts`` is greater than one, the job is retried on failure the
      same number of attempts as the value.
    """


_ClientRegisterJobDefinitiontimeoutTypeDef = TypedDict(
    "_ClientRegisterJobDefinitiontimeoutTypeDef",
    {"attemptDurationSeconds": int},
    total=False,
)


class ClientRegisterJobDefinitiontimeoutTypeDef(
    _ClientRegisterJobDefinitiontimeoutTypeDef
):
    """
    Type definition for `ClientRegisterJobDefinition` `timeout`

    The timeout configuration for jobs that are submitted with this job definition, after which AWS
    Batch terminates your jobs if they have not finished. If a job is terminated due to a timeout, it
    is not retried. The minimum value for the timeout is 60 seconds. Any timeout configuration that
    is specified during a  SubmitJob operation overrides the timeout configuration defined here. For
    more information, see `Job Timeouts
    <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/job_timeouts.html>`__ in the *Amazon
    Elastic Container Service Developer Guide* .

    - **attemptDurationSeconds** *(integer) --*

      The time duration in seconds (measured from the job attempt's ``startedAt`` timestamp) after
      which AWS Batch terminates your jobs if they have not finished.
    """


_ClientSubmitJobResponseTypeDef = TypedDict(
    "_ClientSubmitJobResponseTypeDef", {"jobName": str, "jobId": str}, total=False
)


class ClientSubmitJobResponseTypeDef(_ClientSubmitJobResponseTypeDef):
    """
    Type definition for `ClientSubmitJob` `Response`

    - **jobName** *(string) --*

      The name of the job.

    - **jobId** *(string) --*

      The unique identifier for the job.
    """


_ClientSubmitJobarrayPropertiesTypeDef = TypedDict(
    "_ClientSubmitJobarrayPropertiesTypeDef", {"size": int}, total=False
)


class ClientSubmitJobarrayPropertiesTypeDef(_ClientSubmitJobarrayPropertiesTypeDef):
    """
    Type definition for `ClientSubmitJob` `arrayProperties`

    The array properties for the submitted job, such as the size of the array. The array size can be
    between 2 and 10,000. If you specify array properties for a job, it becomes an array job. For
    more information, see `Array Jobs
    <https://docs.aws.amazon.com/batch/latest/userguide/array_jobs.html>`__ in the *AWS Batch User
    Guide* .

    - **size** *(integer) --*

      The size of the array job.
    """


_ClientSubmitJobcontainerOverridesenvironmentTypeDef = TypedDict(
    "_ClientSubmitJobcontainerOverridesenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientSubmitJobcontainerOverridesenvironmentTypeDef(
    _ClientSubmitJobcontainerOverridesenvironmentTypeDef
):
    """
    Type definition for `ClientSubmitJobcontainerOverrides` `environment`

    A key-value pair object.

    - **name** *(string) --*

      The name of the key-value pair. For environment variables, this is the name of the
      environment variable.

    - **value** *(string) --*

      The value of the key-value pair. For environment variables, this is the value of the
      environment variable.
    """


_ClientSubmitJobcontainerOverridesresourceRequirementsTypeDef = TypedDict(
    "_ClientSubmitJobcontainerOverridesresourceRequirementsTypeDef",
    {"value": str, "type": str},
)


class ClientSubmitJobcontainerOverridesresourceRequirementsTypeDef(
    _ClientSubmitJobcontainerOverridesresourceRequirementsTypeDef
):
    """
    Type definition for `ClientSubmitJobcontainerOverrides` `resourceRequirements`

    The type and amount of a resource to assign to a container. Currently, the only supported
    resource type is ``GPU`` .

    - **value** *(string) --* **[REQUIRED]**

      The number of physical GPUs to reserve for the container. The number of GPUs reserved for
      all containers in a job should not exceed the number of available GPUs on the compute
      resource that the job is launched on.

    - **type** *(string) --* **[REQUIRED]**

      The type of resource to assign to a container. Currently, the only supported resource type
      is ``GPU`` .
    """


_ClientSubmitJobcontainerOverridesTypeDef = TypedDict(
    "_ClientSubmitJobcontainerOverridesTypeDef",
    {
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "instanceType": str,
        "environment": List[ClientSubmitJobcontainerOverridesenvironmentTypeDef],
        "resourceRequirements": List[
            ClientSubmitJobcontainerOverridesresourceRequirementsTypeDef
        ],
    },
    total=False,
)


class ClientSubmitJobcontainerOverridesTypeDef(
    _ClientSubmitJobcontainerOverridesTypeDef
):
    """
    Type definition for `ClientSubmitJob` `containerOverrides`

    A list of container overrides in JSON format that specify the name of a container in the
    specified job definition and the overrides it should receive. You can override the default
    command for a container (that is specified in the job definition or the Docker image) with a
    ``command`` override. You can also override existing environment variables (that are specified in
    the job definition or Docker image) on a container or add new environment variables to it with an
    ``environment`` override.

    - **vcpus** *(integer) --*

      The number of vCPUs to reserve for the container. This value overrides the value set in the job
      definition.

    - **memory** *(integer) --*

      The number of MiB of memory reserved for the job. This value overrides the value set in the job
      definition.

    - **command** *(list) --*

      The command to send to the container that overrides the default command from the Docker image
      or the job definition.

      - *(string) --*

    - **instanceType** *(string) --*

      The instance type to use for a multi-node parallel job. This parameter is not valid for
      single-node container jobs.

    - **environment** *(list) --*

      The environment variables to send to the container. You can add new environment variables,
      which are added to the container at launch, or you can override the existing environment
      variables from the Docker image or the job definition.

      .. note::

        Environment variables must not start with ``AWS_BATCH`` ; this naming convention is reserved
        for variables that are set by the AWS Batch service.

      - *(dict) --*

        A key-value pair object.

        - **name** *(string) --*

          The name of the key-value pair. For environment variables, this is the name of the
          environment variable.

        - **value** *(string) --*

          The value of the key-value pair. For environment variables, this is the value of the
          environment variable.

    - **resourceRequirements** *(list) --*

      The type and amount of a resource to assign to a container. This value overrides the value set
      in the job definition. Currently, the only supported resource is ``GPU`` .

      - *(dict) --*

        The type and amount of a resource to assign to a container. Currently, the only supported
        resource type is ``GPU`` .

        - **value** *(string) --* **[REQUIRED]**

          The number of physical GPUs to reserve for the container. The number of GPUs reserved for
          all containers in a job should not exceed the number of available GPUs on the compute
          resource that the job is launched on.

        - **type** *(string) --* **[REQUIRED]**

          The type of resource to assign to a container. Currently, the only supported resource type
          is ``GPU`` .
    """


_ClientSubmitJobdependsOnTypeDef = TypedDict(
    "_ClientSubmitJobdependsOnTypeDef", {"jobId": str, "type": str}, total=False
)


class ClientSubmitJobdependsOnTypeDef(_ClientSubmitJobdependsOnTypeDef):
    """
    Type definition for `ClientSubmitJob` `dependsOn`

    An object representing an AWS Batch job dependency.

    - **jobId** *(string) --*

      The job ID of the AWS Batch job associated with this dependency.

    - **type** *(string) --*

      The type of the job dependency.
    """


_ClientSubmitJobnodeOverridesnodePropertyOverridescontainerOverridesenvironmentTypeDef = TypedDict(
    "_ClientSubmitJobnodeOverridesnodePropertyOverridescontainerOverridesenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientSubmitJobnodeOverridesnodePropertyOverridescontainerOverridesenvironmentTypeDef(
    _ClientSubmitJobnodeOverridesnodePropertyOverridescontainerOverridesenvironmentTypeDef
):
    """
    Type definition for `ClientSubmitJobnodeOverridesnodePropertyOverridescontainerOverrides` `environment`

    A key-value pair object.

    - **name** *(string) --*

      The name of the key-value pair. For environment variables, this is the name of the
      environment variable.

    - **value** *(string) --*

      The value of the key-value pair. For environment variables, this is the value of the
      environment variable.
    """


_ClientSubmitJobnodeOverridesnodePropertyOverridescontainerOverridesresourceRequirementsTypeDef = TypedDict(
    "_ClientSubmitJobnodeOverridesnodePropertyOverridescontainerOverridesresourceRequirementsTypeDef",
    {"value": str, "type": str},
)


class ClientSubmitJobnodeOverridesnodePropertyOverridescontainerOverridesresourceRequirementsTypeDef(
    _ClientSubmitJobnodeOverridesnodePropertyOverridescontainerOverridesresourceRequirementsTypeDef
):
    """
    Type definition for `ClientSubmitJobnodeOverridesnodePropertyOverridescontainerOverrides` `resourceRequirements`

    The type and amount of a resource to assign to a container. Currently, the only
    supported resource type is ``GPU`` .

    - **value** *(string) --* **[REQUIRED]**

      The number of physical GPUs to reserve for the container. The number of GPUs reserved
      for all containers in a job should not exceed the number of available GPUs on the
      compute resource that the job is launched on.

    - **type** *(string) --* **[REQUIRED]**

      The type of resource to assign to a container. Currently, the only supported resource
      type is ``GPU`` .
    """


_ClientSubmitJobnodeOverridesnodePropertyOverridescontainerOverridesTypeDef = TypedDict(
    "_ClientSubmitJobnodeOverridesnodePropertyOverridescontainerOverridesTypeDef",
    {
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "instanceType": str,
        "environment": List[
            ClientSubmitJobnodeOverridesnodePropertyOverridescontainerOverridesenvironmentTypeDef
        ],
        "resourceRequirements": List[
            ClientSubmitJobnodeOverridesnodePropertyOverridescontainerOverridesresourceRequirementsTypeDef
        ],
    },
    total=False,
)


class ClientSubmitJobnodeOverridesnodePropertyOverridescontainerOverridesTypeDef(
    _ClientSubmitJobnodeOverridesnodePropertyOverridescontainerOverridesTypeDef
):
    """
    Type definition for `ClientSubmitJobnodeOverridesnodePropertyOverrides` `containerOverrides`

    The overrides that should be sent to a node range.

    - **vcpus** *(integer) --*

      The number of vCPUs to reserve for the container. This value overrides the value set in
      the job definition.

    - **memory** *(integer) --*

      The number of MiB of memory reserved for the job. This value overrides the value set in
      the job definition.

    - **command** *(list) --*

      The command to send to the container that overrides the default command from the Docker
      image or the job definition.

      - *(string) --*

    - **instanceType** *(string) --*

      The instance type to use for a multi-node parallel job. This parameter is not valid for
      single-node container jobs.

    - **environment** *(list) --*

      The environment variables to send to the container. You can add new environment
      variables, which are added to the container at launch, or you can override the existing
      environment variables from the Docker image or the job definition.

      .. note::

        Environment variables must not start with ``AWS_BATCH`` ; this naming convention is
        reserved for variables that are set by the AWS Batch service.

      - *(dict) --*

        A key-value pair object.

        - **name** *(string) --*

          The name of the key-value pair. For environment variables, this is the name of the
          environment variable.

        - **value** *(string) --*

          The value of the key-value pair. For environment variables, this is the value of the
          environment variable.

    - **resourceRequirements** *(list) --*

      The type and amount of a resource to assign to a container. This value overrides the
      value set in the job definition. Currently, the only supported resource is ``GPU`` .

      - *(dict) --*

        The type and amount of a resource to assign to a container. Currently, the only
        supported resource type is ``GPU`` .

        - **value** *(string) --* **[REQUIRED]**

          The number of physical GPUs to reserve for the container. The number of GPUs reserved
          for all containers in a job should not exceed the number of available GPUs on the
          compute resource that the job is launched on.

        - **type** *(string) --* **[REQUIRED]**

          The type of resource to assign to a container. Currently, the only supported resource
          type is ``GPU`` .
    """


_RequiredClientSubmitJobnodeOverridesnodePropertyOverridesTypeDef = TypedDict(
    "_RequiredClientSubmitJobnodeOverridesnodePropertyOverridesTypeDef",
    {"targetNodes": str},
)
_OptionalClientSubmitJobnodeOverridesnodePropertyOverridesTypeDef = TypedDict(
    "_OptionalClientSubmitJobnodeOverridesnodePropertyOverridesTypeDef",
    {
        "containerOverrides": ClientSubmitJobnodeOverridesnodePropertyOverridescontainerOverridesTypeDef
    },
    total=False,
)


class ClientSubmitJobnodeOverridesnodePropertyOverridesTypeDef(
    _RequiredClientSubmitJobnodeOverridesnodePropertyOverridesTypeDef,
    _OptionalClientSubmitJobnodeOverridesnodePropertyOverridesTypeDef,
):
    """
    Type definition for `ClientSubmitJobnodeOverrides` `nodePropertyOverrides`

    Object representing any node overrides to a job definition that is used in a  SubmitJob API
    operation.

    - **targetNodes** *(string) --* **[REQUIRED]**

      The range of nodes, using node index values, with which to override. A range of ``0:3``
      indicates nodes with index values of ``0`` through ``3`` . If the starting range value is
      omitted (``:n`` ), then ``0`` is used to start the range. If the ending range value is
      omitted (``n:`` ), then the highest possible node index is used to end the range.

    - **containerOverrides** *(dict) --*

      The overrides that should be sent to a node range.

      - **vcpus** *(integer) --*

        The number of vCPUs to reserve for the container. This value overrides the value set in
        the job definition.

      - **memory** *(integer) --*

        The number of MiB of memory reserved for the job. This value overrides the value set in
        the job definition.

      - **command** *(list) --*

        The command to send to the container that overrides the default command from the Docker
        image or the job definition.

        - *(string) --*

      - **instanceType** *(string) --*

        The instance type to use for a multi-node parallel job. This parameter is not valid for
        single-node container jobs.

      - **environment** *(list) --*

        The environment variables to send to the container. You can add new environment
        variables, which are added to the container at launch, or you can override the existing
        environment variables from the Docker image or the job definition.

        .. note::

          Environment variables must not start with ``AWS_BATCH`` ; this naming convention is
          reserved for variables that are set by the AWS Batch service.

        - *(dict) --*

          A key-value pair object.

          - **name** *(string) --*

            The name of the key-value pair. For environment variables, this is the name of the
            environment variable.

          - **value** *(string) --*

            The value of the key-value pair. For environment variables, this is the value of the
            environment variable.

      - **resourceRequirements** *(list) --*

        The type and amount of a resource to assign to a container. This value overrides the
        value set in the job definition. Currently, the only supported resource is ``GPU`` .

        - *(dict) --*

          The type and amount of a resource to assign to a container. Currently, the only
          supported resource type is ``GPU`` .

          - **value** *(string) --* **[REQUIRED]**

            The number of physical GPUs to reserve for the container. The number of GPUs reserved
            for all containers in a job should not exceed the number of available GPUs on the
            compute resource that the job is launched on.

          - **type** *(string) --* **[REQUIRED]**

            The type of resource to assign to a container. Currently, the only supported resource
            type is ``GPU`` .
    """


_ClientSubmitJobnodeOverridesTypeDef = TypedDict(
    "_ClientSubmitJobnodeOverridesTypeDef",
    {
        "numNodes": int,
        "nodePropertyOverrides": List[
            ClientSubmitJobnodeOverridesnodePropertyOverridesTypeDef
        ],
    },
    total=False,
)


class ClientSubmitJobnodeOverridesTypeDef(_ClientSubmitJobnodeOverridesTypeDef):
    """
    Type definition for `ClientSubmitJob` `nodeOverrides`

    A list of node overrides in JSON format that specify the node range to target and the container
    overrides for that node range.

    - **numNodes** *(integer) --*

      The number of nodes to use with a multi-node parallel job. This value overrides the number of
      nodes that are specified in the job definition. To use this override:

      * There must be at least one node range in your job definition that has an open upper boundary
      (such as ``:`` or ``n:`` ).

      * The lower boundary of the node range specified in the job definition must be fewer than the
      number of nodes specified in the override.

      * The main node index specified in the job definition must be fewer than the number of nodes
      specified in the override.

    - **nodePropertyOverrides** *(list) --*

      The node property overrides for the job.

      - *(dict) --*

        Object representing any node overrides to a job definition that is used in a  SubmitJob API
        operation.

        - **targetNodes** *(string) --* **[REQUIRED]**

          The range of nodes, using node index values, with which to override. A range of ``0:3``
          indicates nodes with index values of ``0`` through ``3`` . If the starting range value is
          omitted (``:n`` ), then ``0`` is used to start the range. If the ending range value is
          omitted (``n:`` ), then the highest possible node index is used to end the range.

        - **containerOverrides** *(dict) --*

          The overrides that should be sent to a node range.

          - **vcpus** *(integer) --*

            The number of vCPUs to reserve for the container. This value overrides the value set in
            the job definition.

          - **memory** *(integer) --*

            The number of MiB of memory reserved for the job. This value overrides the value set in
            the job definition.

          - **command** *(list) --*

            The command to send to the container that overrides the default command from the Docker
            image or the job definition.

            - *(string) --*

          - **instanceType** *(string) --*

            The instance type to use for a multi-node parallel job. This parameter is not valid for
            single-node container jobs.

          - **environment** *(list) --*

            The environment variables to send to the container. You can add new environment
            variables, which are added to the container at launch, or you can override the existing
            environment variables from the Docker image or the job definition.

            .. note::

              Environment variables must not start with ``AWS_BATCH`` ; this naming convention is
              reserved for variables that are set by the AWS Batch service.

            - *(dict) --*

              A key-value pair object.

              - **name** *(string) --*

                The name of the key-value pair. For environment variables, this is the name of the
                environment variable.

              - **value** *(string) --*

                The value of the key-value pair. For environment variables, this is the value of the
                environment variable.

          - **resourceRequirements** *(list) --*

            The type and amount of a resource to assign to a container. This value overrides the
            value set in the job definition. Currently, the only supported resource is ``GPU`` .

            - *(dict) --*

              The type and amount of a resource to assign to a container. Currently, the only
              supported resource type is ``GPU`` .

              - **value** *(string) --* **[REQUIRED]**

                The number of physical GPUs to reserve for the container. The number of GPUs reserved
                for all containers in a job should not exceed the number of available GPUs on the
                compute resource that the job is launched on.

              - **type** *(string) --* **[REQUIRED]**

                The type of resource to assign to a container. Currently, the only supported resource
                type is ``GPU`` .
    """


_ClientSubmitJobretryStrategyTypeDef = TypedDict(
    "_ClientSubmitJobretryStrategyTypeDef", {"attempts": int}, total=False
)


class ClientSubmitJobretryStrategyTypeDef(_ClientSubmitJobretryStrategyTypeDef):
    """
    Type definition for `ClientSubmitJob` `retryStrategy`

    The retry strategy to use for failed jobs from this  SubmitJob operation. When a retry strategy
    is specified here, it overrides the retry strategy defined in the job definition.

    - **attempts** *(integer) --*

      The number of times to move a job to the ``RUNNABLE`` status. You may specify between 1 and 10
      attempts. If the value of ``attempts`` is greater than one, the job is retried on failure the
      same number of attempts as the value.
    """


_ClientSubmitJobtimeoutTypeDef = TypedDict(
    "_ClientSubmitJobtimeoutTypeDef", {"attemptDurationSeconds": int}, total=False
)


class ClientSubmitJobtimeoutTypeDef(_ClientSubmitJobtimeoutTypeDef):
    """
    Type definition for `ClientSubmitJob` `timeout`

    The timeout configuration for this  SubmitJob operation. You can specify a timeout duration after
    which AWS Batch terminates your jobs if they have not finished. If a job is terminated due to a
    timeout, it is not retried. The minimum value for the timeout is 60 seconds. This configuration
    overrides any timeout configuration specified in the job definition. For array jobs, child jobs
    have the same timeout configuration as the parent job. For more information, see `Job Timeouts
    <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/job_timeouts.html>`__ in the *Amazon
    Elastic Container Service Developer Guide* .

    - **attemptDurationSeconds** *(integer) --*

      The time duration in seconds (measured from the job attempt's ``startedAt`` timestamp) after
      which AWS Batch terminates your jobs if they have not finished.
    """


_ClientUpdateComputeEnvironmentResponseTypeDef = TypedDict(
    "_ClientUpdateComputeEnvironmentResponseTypeDef",
    {"computeEnvironmentName": str, "computeEnvironmentArn": str},
    total=False,
)


class ClientUpdateComputeEnvironmentResponseTypeDef(
    _ClientUpdateComputeEnvironmentResponseTypeDef
):
    """
    Type definition for `ClientUpdateComputeEnvironment` `Response`

    - **computeEnvironmentName** *(string) --*

      The name of the compute environment.

    - **computeEnvironmentArn** *(string) --*

      The Amazon Resource Name (ARN) of the compute environment.
    """


_ClientUpdateComputeEnvironmentcomputeResourcesTypeDef = TypedDict(
    "_ClientUpdateComputeEnvironmentcomputeResourcesTypeDef",
    {"minvCpus": int, "maxvCpus": int, "desiredvCpus": int},
    total=False,
)


class ClientUpdateComputeEnvironmentcomputeResourcesTypeDef(
    _ClientUpdateComputeEnvironmentcomputeResourcesTypeDef
):
    """
    Type definition for `ClientUpdateComputeEnvironment` `computeResources`

    Details of the compute resources managed by the compute environment. Required for a managed
    compute environment.

    - **minvCpus** *(integer) --*

      The minimum number of Amazon EC2 vCPUs that an environment should maintain.

    - **maxvCpus** *(integer) --*

      The maximum number of Amazon EC2 vCPUs that an environment can reach.

    - **desiredvCpus** *(integer) --*

      The desired number of Amazon EC2 vCPUS in the compute environment.
    """


_ClientUpdateJobQueueResponseTypeDef = TypedDict(
    "_ClientUpdateJobQueueResponseTypeDef",
    {"jobQueueName": str, "jobQueueArn": str},
    total=False,
)


class ClientUpdateJobQueueResponseTypeDef(_ClientUpdateJobQueueResponseTypeDef):
    """
    Type definition for `ClientUpdateJobQueue` `Response`

    - **jobQueueName** *(string) --*

      The name of the job queue.

    - **jobQueueArn** *(string) --*

      The Amazon Resource Name (ARN) of the job queue.
    """


_ClientUpdateJobQueuecomputeEnvironmentOrderTypeDef = TypedDict(
    "_ClientUpdateJobQueuecomputeEnvironmentOrderTypeDef",
    {"order": int, "computeEnvironment": str},
)


class ClientUpdateJobQueuecomputeEnvironmentOrderTypeDef(
    _ClientUpdateJobQueuecomputeEnvironmentOrderTypeDef
):
    """
    Type definition for `ClientUpdateJobQueue` `computeEnvironmentOrder`

    The order in which compute environments are tried for job placement within a queue. Compute
    environments are tried in ascending order. For example, if two compute environments are
    associated with a job queue, the compute environment with a lower order integer value is tried
    for job placement first.

    - **order** *(integer) --* **[REQUIRED]**

      The order of the compute environment.

    - **computeEnvironment** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the compute environment.
    """


_DescribeComputeEnvironmentsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeComputeEnvironmentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeComputeEnvironmentsPaginatePaginationConfigTypeDef(
    _DescribeComputeEnvironmentsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeComputeEnvironmentsPaginate` `PaginationConfig`

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


_DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentscomputeResourceslaunchTemplateTypeDef = TypedDict(
    "_DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentscomputeResourceslaunchTemplateTypeDef",
    {"launchTemplateId": str, "launchTemplateName": str, "version": str},
    total=False,
)


class DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentscomputeResourceslaunchTemplateTypeDef(
    _DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentscomputeResourceslaunchTemplateTypeDef
):
    """
    Type definition for `DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentscomputeResources` `launchTemplate`

    The launch template to use for your compute resources. Any other compute resource
    parameters that you specify in a  CreateComputeEnvironment API operation override the
    same parameters in the launch template. You must specify either the launch template ID
    or launch template name in the request, but not both. For more information, see `Launch
    Template Support
    <https://docs.aws.amazon.com/batch/latest/userguide/launch-templates.html>`__ in the
    *AWS Batch User Guide* .

    - **launchTemplateId** *(string) --*

      The ID of the launch template.

    - **launchTemplateName** *(string) --*

      The name of the launch template.

    - **version** *(string) --*

      The version number of the launch template.

      Default: The default version of the launch template.
    """


_DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentscomputeResourcesTypeDef = TypedDict(
    "_DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentscomputeResourcesTypeDef",
    {
        "type": str,
        "allocationStrategy": str,
        "minvCpus": int,
        "maxvCpus": int,
        "desiredvCpus": int,
        "instanceTypes": List[str],
        "imageId": str,
        "subnets": List[str],
        "securityGroupIds": List[str],
        "ec2KeyPair": str,
        "instanceRole": str,
        "tags": Dict[str, str],
        "placementGroup": str,
        "bidPercentage": int,
        "spotIamFleetRole": str,
        "launchTemplate": DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentscomputeResourceslaunchTemplateTypeDef,
    },
    total=False,
)


class DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentscomputeResourcesTypeDef(
    _DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentscomputeResourcesTypeDef
):
    """
    Type definition for `DescribeComputeEnvironmentsPaginateResponsecomputeEnvironments` `computeResources`

    The compute resources defined for the compute environment.

    - **type** *(string) --*

      The type of compute environment: ``EC2`` or ``SPOT`` .

    - **allocationStrategy** *(string) --*

      The allocation strategy to use for the compute resource in case not enough instances of
      the best fitting instance type can be allocated. This could be due to availability of
      the instance type in the region or `Amazon EC2 service limits
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html>`__ . If
      this is not specified, the default is ``BEST_FIT`` , which will use only the best
      fitting instance type, waiting for additional capacity if it's not available. This
      allocation strategy keeps costs lower but can limit scaling. ``BEST_FIT_PROGRESSIVE``
      will select an additional instance type that is large enough to meet the requirements
      of the jobs in the queue, with a preference for an instance type with a lower cost.
      ``SPOT_CAPACITY_OPTIMIZED`` is only available for Spot Instance compute resources and
      will select an additional instance type that is large enough to meet the requirements
      of the jobs in the queue, with a preference for an instance type that is less likely to
      be interrupted.

    - **minvCpus** *(integer) --*

      The minimum number of Amazon EC2 vCPUs that an environment should maintain (even if the
      compute environment is ``DISABLED`` ).

    - **maxvCpus** *(integer) --*

      The maximum number of Amazon EC2 vCPUs that an environment can reach.

    - **desiredvCpus** *(integer) --*

      The desired number of Amazon EC2 vCPUS in the compute environment.

    - **instanceTypes** *(list) --*

      The instances types that may be launched. You can specify instance families to launch
      any instance type within those families (for example, ``c5`` or ``p3`` ), or you can
      specify specific sizes within a family (such as ``c5.8xlarge`` ). You can also choose
      ``optimal`` to pick instance types (from the C, M, and R instance families) on the fly
      that match the demand of your job queues.

      - *(string) --*

    - **imageId** *(string) --*

      The Amazon Machine Image (AMI) ID used for instances launched in the compute
      environment.

    - **subnets** *(list) --*

      The VPC subnets into which the compute resources are launched. For more information,
      see `VPCs and Subnets
      <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ in the *Amazon
      VPC User Guide* .

      - *(string) --*

    - **securityGroupIds** *(list) --*

      The Amazon EC2 security groups associated with instances launched in the compute
      environment. One or more security groups must be specified, either in
      ``securityGroupIds`` or using a launch template referenced in ``launchTemplate`` . If
      security groups are specified using both ``securityGroupIds`` and ``launchTemplate`` ,
      the values in ``securityGroupIds`` will be used.

      - *(string) --*

    - **ec2KeyPair** *(string) --*

      The Amazon EC2 key pair that is used for instances launched in the compute environment.

    - **instanceRole** *(string) --*

      The Amazon ECS instance profile applied to Amazon EC2 instances in a compute
      environment. You can specify the short name or full Amazon Resource Name (ARN) of an
      instance profile. For example, `` *ecsInstanceRole* `` or
      ``arn:aws:iam::*<aws_account_id>* :instance-profile/*ecsInstanceRole* `` . For more
      information, see `Amazon ECS Instance Role
      <https://docs.aws.amazon.com/batch/latest/userguide/instance_IAM_role.html>`__ in the
      *AWS Batch User Guide* .

    - **tags** *(dict) --*

      Key-value pair tags to be applied to resources that are launched in the compute
      environment. For AWS Batch, these take the form of "String1": "String2", where String1
      is the tag key and String2 is the tag value—for example, { "Name": "AWS Batch Instance
      - C4OnDemand" }.

      - *(string) --*

        - *(string) --*

    - **placementGroup** *(string) --*

      The Amazon EC2 placement group to associate with your compute resources. If you intend
      to submit multi-node parallel jobs to your compute environment, you should consider
      creating a cluster placement group and associate it with your compute resources. This
      keeps your multi-node parallel job on a logical grouping of instances within a single
      Availability Zone with high network flow potential. For more information, see
      `Placement Groups
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html>`__ in the
      *Amazon EC2 User Guide for Linux Instances* .

    - **bidPercentage** *(integer) --*

      The maximum percentage that a Spot Instance price can be when compared with the
      On-Demand price for that instance type before instances are launched. For example, if
      your maximum percentage is 20%, then the Spot price must be below 20% of the current
      On-Demand price for that Amazon EC2 instance. You always pay the lowest (market) price
      and never more than your maximum percentage. If you leave this field empty, the default
      value is 100% of the On-Demand price.

    - **spotIamFleetRole** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a
      ``SPOT`` compute environment. For more information, see `Amazon EC2 Spot Fleet Role
      <https://docs.aws.amazon.com/batch/latest/userguide/spot_fleet_IAM_role.html>`__ in the
      *AWS Batch User Guide* .

    - **launchTemplate** *(dict) --*

      The launch template to use for your compute resources. Any other compute resource
      parameters that you specify in a  CreateComputeEnvironment API operation override the
      same parameters in the launch template. You must specify either the launch template ID
      or launch template name in the request, but not both. For more information, see `Launch
      Template Support
      <https://docs.aws.amazon.com/batch/latest/userguide/launch-templates.html>`__ in the
      *AWS Batch User Guide* .

      - **launchTemplateId** *(string) --*

        The ID of the launch template.

      - **launchTemplateName** *(string) --*

        The name of the launch template.

      - **version** *(string) --*

        The version number of the launch template.

        Default: The default version of the launch template.
    """


_DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentsTypeDef = TypedDict(
    "_DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentsTypeDef",
    {
        "computeEnvironmentName": str,
        "computeEnvironmentArn": str,
        "ecsClusterArn": str,
        "type": str,
        "state": str,
        "status": str,
        "statusReason": str,
        "computeResources": DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentscomputeResourcesTypeDef,
        "serviceRole": str,
    },
    total=False,
)


class DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentsTypeDef(
    _DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentsTypeDef
):
    """
    Type definition for `DescribeComputeEnvironmentsPaginateResponse` `computeEnvironments`

    An object representing an AWS Batch compute environment.

    - **computeEnvironmentName** *(string) --*

      The name of the compute environment.

    - **computeEnvironmentArn** *(string) --*

      The Amazon Resource Name (ARN) of the compute environment.

    - **ecsClusterArn** *(string) --*

      The Amazon Resource Name (ARN) of the underlying Amazon ECS cluster used by the compute
      environment.

    - **type** *(string) --*

      The type of the compute environment.

    - **state** *(string) --*

      The state of the compute environment. The valid values are ``ENABLED`` or ``DISABLED`` .

      If the state is ``ENABLED`` , then the AWS Batch scheduler can attempt to place jobs from
      an associated job queue on the compute resources within the environment. If the compute
      environment is managed, then it can scale its instances out or in automatically, based on
      the job queue demand.

      If the state is ``DISABLED`` , then the AWS Batch scheduler does not attempt to place
      jobs within the environment. Jobs in a ``STARTING`` or ``RUNNING`` state continue to
      progress normally. Managed compute environments in the ``DISABLED`` state do not scale
      out. However, they scale in to ``minvCpus`` value after instances become idle.

    - **status** *(string) --*

      The current status of the compute environment (for example, ``CREATING`` or ``VALID`` ).

    - **statusReason** *(string) --*

      A short, human-readable string to provide additional details about the current status of
      the compute environment.

    - **computeResources** *(dict) --*

      The compute resources defined for the compute environment.

      - **type** *(string) --*

        The type of compute environment: ``EC2`` or ``SPOT`` .

      - **allocationStrategy** *(string) --*

        The allocation strategy to use for the compute resource in case not enough instances of
        the best fitting instance type can be allocated. This could be due to availability of
        the instance type in the region or `Amazon EC2 service limits
        <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html>`__ . If
        this is not specified, the default is ``BEST_FIT`` , which will use only the best
        fitting instance type, waiting for additional capacity if it's not available. This
        allocation strategy keeps costs lower but can limit scaling. ``BEST_FIT_PROGRESSIVE``
        will select an additional instance type that is large enough to meet the requirements
        of the jobs in the queue, with a preference for an instance type with a lower cost.
        ``SPOT_CAPACITY_OPTIMIZED`` is only available for Spot Instance compute resources and
        will select an additional instance type that is large enough to meet the requirements
        of the jobs in the queue, with a preference for an instance type that is less likely to
        be interrupted.

      - **minvCpus** *(integer) --*

        The minimum number of Amazon EC2 vCPUs that an environment should maintain (even if the
        compute environment is ``DISABLED`` ).

      - **maxvCpus** *(integer) --*

        The maximum number of Amazon EC2 vCPUs that an environment can reach.

      - **desiredvCpus** *(integer) --*

        The desired number of Amazon EC2 vCPUS in the compute environment.

      - **instanceTypes** *(list) --*

        The instances types that may be launched. You can specify instance families to launch
        any instance type within those families (for example, ``c5`` or ``p3`` ), or you can
        specify specific sizes within a family (such as ``c5.8xlarge`` ). You can also choose
        ``optimal`` to pick instance types (from the C, M, and R instance families) on the fly
        that match the demand of your job queues.

        - *(string) --*

      - **imageId** *(string) --*

        The Amazon Machine Image (AMI) ID used for instances launched in the compute
        environment.

      - **subnets** *(list) --*

        The VPC subnets into which the compute resources are launched. For more information,
        see `VPCs and Subnets
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ in the *Amazon
        VPC User Guide* .

        - *(string) --*

      - **securityGroupIds** *(list) --*

        The Amazon EC2 security groups associated with instances launched in the compute
        environment. One or more security groups must be specified, either in
        ``securityGroupIds`` or using a launch template referenced in ``launchTemplate`` . If
        security groups are specified using both ``securityGroupIds`` and ``launchTemplate`` ,
        the values in ``securityGroupIds`` will be used.

        - *(string) --*

      - **ec2KeyPair** *(string) --*

        The Amazon EC2 key pair that is used for instances launched in the compute environment.

      - **instanceRole** *(string) --*

        The Amazon ECS instance profile applied to Amazon EC2 instances in a compute
        environment. You can specify the short name or full Amazon Resource Name (ARN) of an
        instance profile. For example, `` *ecsInstanceRole* `` or
        ``arn:aws:iam::*<aws_account_id>* :instance-profile/*ecsInstanceRole* `` . For more
        information, see `Amazon ECS Instance Role
        <https://docs.aws.amazon.com/batch/latest/userguide/instance_IAM_role.html>`__ in the
        *AWS Batch User Guide* .

      - **tags** *(dict) --*

        Key-value pair tags to be applied to resources that are launched in the compute
        environment. For AWS Batch, these take the form of "String1": "String2", where String1
        is the tag key and String2 is the tag value—for example, { "Name": "AWS Batch Instance
        - C4OnDemand" }.

        - *(string) --*

          - *(string) --*

      - **placementGroup** *(string) --*

        The Amazon EC2 placement group to associate with your compute resources. If you intend
        to submit multi-node parallel jobs to your compute environment, you should consider
        creating a cluster placement group and associate it with your compute resources. This
        keeps your multi-node parallel job on a logical grouping of instances within a single
        Availability Zone with high network flow potential. For more information, see
        `Placement Groups
        <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html>`__ in the
        *Amazon EC2 User Guide for Linux Instances* .

      - **bidPercentage** *(integer) --*

        The maximum percentage that a Spot Instance price can be when compared with the
        On-Demand price for that instance type before instances are launched. For example, if
        your maximum percentage is 20%, then the Spot price must be below 20% of the current
        On-Demand price for that Amazon EC2 instance. You always pay the lowest (market) price
        and never more than your maximum percentage. If you leave this field empty, the default
        value is 100% of the On-Demand price.

      - **spotIamFleetRole** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a
        ``SPOT`` compute environment. For more information, see `Amazon EC2 Spot Fleet Role
        <https://docs.aws.amazon.com/batch/latest/userguide/spot_fleet_IAM_role.html>`__ in the
        *AWS Batch User Guide* .

      - **launchTemplate** *(dict) --*

        The launch template to use for your compute resources. Any other compute resource
        parameters that you specify in a  CreateComputeEnvironment API operation override the
        same parameters in the launch template. You must specify either the launch template ID
        or launch template name in the request, but not both. For more information, see `Launch
        Template Support
        <https://docs.aws.amazon.com/batch/latest/userguide/launch-templates.html>`__ in the
        *AWS Batch User Guide* .

        - **launchTemplateId** *(string) --*

          The ID of the launch template.

        - **launchTemplateName** *(string) --*

          The name of the launch template.

        - **version** *(string) --*

          The version number of the launch template.

          Default: The default version of the launch template.

    - **serviceRole** *(string) --*

      The service role associated with the compute environment that allows AWS Batch to make
      calls to AWS API operations on your behalf.
    """


_DescribeComputeEnvironmentsPaginateResponseTypeDef = TypedDict(
    "_DescribeComputeEnvironmentsPaginateResponseTypeDef",
    {
        "computeEnvironments": List[
            DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeComputeEnvironmentsPaginateResponseTypeDef(
    _DescribeComputeEnvironmentsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeComputeEnvironmentsPaginate` `Response`

    - **computeEnvironments** *(list) --*

      The list of compute environments.

      - *(dict) --*

        An object representing an AWS Batch compute environment.

        - **computeEnvironmentName** *(string) --*

          The name of the compute environment.

        - **computeEnvironmentArn** *(string) --*

          The Amazon Resource Name (ARN) of the compute environment.

        - **ecsClusterArn** *(string) --*

          The Amazon Resource Name (ARN) of the underlying Amazon ECS cluster used by the compute
          environment.

        - **type** *(string) --*

          The type of the compute environment.

        - **state** *(string) --*

          The state of the compute environment. The valid values are ``ENABLED`` or ``DISABLED`` .

          If the state is ``ENABLED`` , then the AWS Batch scheduler can attempt to place jobs from
          an associated job queue on the compute resources within the environment. If the compute
          environment is managed, then it can scale its instances out or in automatically, based on
          the job queue demand.

          If the state is ``DISABLED`` , then the AWS Batch scheduler does not attempt to place
          jobs within the environment. Jobs in a ``STARTING`` or ``RUNNING`` state continue to
          progress normally. Managed compute environments in the ``DISABLED`` state do not scale
          out. However, they scale in to ``minvCpus`` value after instances become idle.

        - **status** *(string) --*

          The current status of the compute environment (for example, ``CREATING`` or ``VALID`` ).

        - **statusReason** *(string) --*

          A short, human-readable string to provide additional details about the current status of
          the compute environment.

        - **computeResources** *(dict) --*

          The compute resources defined for the compute environment.

          - **type** *(string) --*

            The type of compute environment: ``EC2`` or ``SPOT`` .

          - **allocationStrategy** *(string) --*

            The allocation strategy to use for the compute resource in case not enough instances of
            the best fitting instance type can be allocated. This could be due to availability of
            the instance type in the region or `Amazon EC2 service limits
            <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html>`__ . If
            this is not specified, the default is ``BEST_FIT`` , which will use only the best
            fitting instance type, waiting for additional capacity if it's not available. This
            allocation strategy keeps costs lower but can limit scaling. ``BEST_FIT_PROGRESSIVE``
            will select an additional instance type that is large enough to meet the requirements
            of the jobs in the queue, with a preference for an instance type with a lower cost.
            ``SPOT_CAPACITY_OPTIMIZED`` is only available for Spot Instance compute resources and
            will select an additional instance type that is large enough to meet the requirements
            of the jobs in the queue, with a preference for an instance type that is less likely to
            be interrupted.

          - **minvCpus** *(integer) --*

            The minimum number of Amazon EC2 vCPUs that an environment should maintain (even if the
            compute environment is ``DISABLED`` ).

          - **maxvCpus** *(integer) --*

            The maximum number of Amazon EC2 vCPUs that an environment can reach.

          - **desiredvCpus** *(integer) --*

            The desired number of Amazon EC2 vCPUS in the compute environment.

          - **instanceTypes** *(list) --*

            The instances types that may be launched. You can specify instance families to launch
            any instance type within those families (for example, ``c5`` or ``p3`` ), or you can
            specify specific sizes within a family (such as ``c5.8xlarge`` ). You can also choose
            ``optimal`` to pick instance types (from the C, M, and R instance families) on the fly
            that match the demand of your job queues.

            - *(string) --*

          - **imageId** *(string) --*

            The Amazon Machine Image (AMI) ID used for instances launched in the compute
            environment.

          - **subnets** *(list) --*

            The VPC subnets into which the compute resources are launched. For more information,
            see `VPCs and Subnets
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ in the *Amazon
            VPC User Guide* .

            - *(string) --*

          - **securityGroupIds** *(list) --*

            The Amazon EC2 security groups associated with instances launched in the compute
            environment. One or more security groups must be specified, either in
            ``securityGroupIds`` or using a launch template referenced in ``launchTemplate`` . If
            security groups are specified using both ``securityGroupIds`` and ``launchTemplate`` ,
            the values in ``securityGroupIds`` will be used.

            - *(string) --*

          - **ec2KeyPair** *(string) --*

            The Amazon EC2 key pair that is used for instances launched in the compute environment.

          - **instanceRole** *(string) --*

            The Amazon ECS instance profile applied to Amazon EC2 instances in a compute
            environment. You can specify the short name or full Amazon Resource Name (ARN) of an
            instance profile. For example, `` *ecsInstanceRole* `` or
            ``arn:aws:iam::*<aws_account_id>* :instance-profile/*ecsInstanceRole* `` . For more
            information, see `Amazon ECS Instance Role
            <https://docs.aws.amazon.com/batch/latest/userguide/instance_IAM_role.html>`__ in the
            *AWS Batch User Guide* .

          - **tags** *(dict) --*

            Key-value pair tags to be applied to resources that are launched in the compute
            environment. For AWS Batch, these take the form of "String1": "String2", where String1
            is the tag key and String2 is the tag value—for example, { "Name": "AWS Batch Instance
            - C4OnDemand" }.

            - *(string) --*

              - *(string) --*

          - **placementGroup** *(string) --*

            The Amazon EC2 placement group to associate with your compute resources. If you intend
            to submit multi-node parallel jobs to your compute environment, you should consider
            creating a cluster placement group and associate it with your compute resources. This
            keeps your multi-node parallel job on a logical grouping of instances within a single
            Availability Zone with high network flow potential. For more information, see
            `Placement Groups
            <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html>`__ in the
            *Amazon EC2 User Guide for Linux Instances* .

          - **bidPercentage** *(integer) --*

            The maximum percentage that a Spot Instance price can be when compared with the
            On-Demand price for that instance type before instances are launched. For example, if
            your maximum percentage is 20%, then the Spot price must be below 20% of the current
            On-Demand price for that Amazon EC2 instance. You always pay the lowest (market) price
            and never more than your maximum percentage. If you leave this field empty, the default
            value is 100% of the On-Demand price.

          - **spotIamFleetRole** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a
            ``SPOT`` compute environment. For more information, see `Amazon EC2 Spot Fleet Role
            <https://docs.aws.amazon.com/batch/latest/userguide/spot_fleet_IAM_role.html>`__ in the
            *AWS Batch User Guide* .

          - **launchTemplate** *(dict) --*

            The launch template to use for your compute resources. Any other compute resource
            parameters that you specify in a  CreateComputeEnvironment API operation override the
            same parameters in the launch template. You must specify either the launch template ID
            or launch template name in the request, but not both. For more information, see `Launch
            Template Support
            <https://docs.aws.amazon.com/batch/latest/userguide/launch-templates.html>`__ in the
            *AWS Batch User Guide* .

            - **launchTemplateId** *(string) --*

              The ID of the launch template.

            - **launchTemplateName** *(string) --*

              The name of the launch template.

            - **version** *(string) --*

              The version number of the launch template.

              Default: The default version of the launch template.

        - **serviceRole** *(string) --*

          The service role associated with the compute environment that allows AWS Batch to make
          calls to AWS API operations on your behalf.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeJobDefinitionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeJobDefinitionsPaginatePaginationConfigTypeDef(
    _DescribeJobDefinitionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeJobDefinitionsPaginate` `PaginationConfig`

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


_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesenvironmentTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesenvironmentTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesenvironmentTypeDef
):
    """
    Type definition for `DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerProperties` `environment`

    A key-value pair object.

    - **name** *(string) --*

      The name of the key-value pair. For environment variables, this is the name of the
      environment variable.

    - **value** *(string) --*

      The value of the key-value pair. For environment variables, this is the value of
      the environment variable.
    """


_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertieslinuxParametersdevicesTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertieslinuxParametersdevicesTypeDef",
    {"hostPath": str, "containerPath": str, "permissions": List[str]},
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertieslinuxParametersdevicesTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertieslinuxParametersdevicesTypeDef
):
    """
    Type definition for `DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertieslinuxParameters` `devices`

    An object representing a container instance host device.

    - **hostPath** *(string) --*

      The path for the device on the host container instance.

    - **containerPath** *(string) --*

      The path inside the container at which to expose the host device. By default the
      ``hostPath`` value is used.

    - **permissions** *(list) --*

      The explicit permissions to provide to the container for the device. By default,
      the container has permissions for ``read`` , ``write`` , and ``mknod`` for the
      device.

      - *(string) --*
    """


_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertieslinuxParametersTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertieslinuxParametersTypeDef",
    {
        "devices": List[
            DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertieslinuxParametersdevicesTypeDef
        ]
    },
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertieslinuxParametersTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertieslinuxParametersTypeDef
):
    """
    Type definition for `DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerProperties` `linuxParameters`

    Linux-specific modifications that are applied to the container, such as details for
    device mappings.

    - **devices** *(list) --*

      Any host devices to expose to the container. This parameter maps to ``Devices`` in
      the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--device`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__
      .

      - *(dict) --*

        An object representing a container instance host device.

        - **hostPath** *(string) --*

          The path for the device on the host container instance.

        - **containerPath** *(string) --*

          The path inside the container at which to expose the host device. By default the
          ``hostPath`` value is used.

        - **permissions** *(list) --*

          The explicit permissions to provide to the container for the device. By default,
          the container has permissions for ``read`` , ``write`` , and ``mknod`` for the
          device.

          - *(string) --*
    """


_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesmountPointsTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesmountPointsTypeDef",
    {"containerPath": str, "readOnly": bool, "sourceVolume": str},
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesmountPointsTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesmountPointsTypeDef
):
    """
    Type definition for `DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerProperties` `mountPoints`

    Details on a Docker volume mount point that is used in a job's container properties.
    This parameter maps to ``Volumes`` in the `Create a container
    <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
    section of the Docker Remote API and the ``--volume`` option to docker run.

    - **containerPath** *(string) --*

      The path on the container at which to mount the host volume.

    - **readOnly** *(boolean) --*

      If this value is ``true`` , the container has read-only access to the volume;
      otherwise, the container can write to the volume. The default value is ``false`` .

    - **sourceVolume** *(string) --*

      The name of the volume to mount.
    """


_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesresourceRequirementsTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesresourceRequirementsTypeDef",
    {"value": str, "type": str},
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesresourceRequirementsTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesresourceRequirementsTypeDef
):
    """
    Type definition for `DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerProperties` `resourceRequirements`

    The type and amount of a resource to assign to a container. Currently, the only
    supported resource type is ``GPU`` .

    - **value** *(string) --*

      The number of physical GPUs to reserve for the container. The number of GPUs
      reserved for all containers in a job should not exceed the number of available GPUs
      on the compute resource that the job is launched on.

    - **type** *(string) --*

      The type of resource to assign to a container. Currently, the only supported
      resource type is ``GPU`` .
    """


_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesulimitsTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesulimitsTypeDef",
    {"hardLimit": int, "name": str, "softLimit": int},
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesulimitsTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesulimitsTypeDef
):
    """
    Type definition for `DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerProperties` `ulimits`

    The ``ulimit`` settings to pass to the container.

    - **hardLimit** *(integer) --*

      The hard limit for the ``ulimit`` type.

    - **name** *(string) --*

      The ``type`` of the ``ulimit`` .

    - **softLimit** *(integer) --*

      The soft limit for the ``ulimit`` type.
    """


_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesvolumeshostTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesvolumeshostTypeDef",
    {"sourcePath": str},
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesvolumeshostTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesvolumeshostTypeDef
):
    """
    Type definition for `DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesvolumes` `host`

    The contents of the ``host`` parameter determine whether your data volume persists
    on the host container instance and where it is stored. If the host parameter is
    empty, then the Docker daemon assigns a host path for your data volume. However,
    the data is not guaranteed to persist after the containers associated with it stop
    running.

    - **sourcePath** *(string) --*

      The path on the host container instance that is presented to the container. If
      this parameter is empty, then the Docker daemon has assigned a host path for you.
      If this parameter contains a file location, then the data volume persists at the
      specified location on the host container instance until you delete it manually.
      If the source path location does not exist on the host container instance, the
      Docker daemon creates it. If the location does exist, the contents of the source
      path folder are exported.
    """


_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesvolumesTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesvolumesTypeDef",
    {
        "host": DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesvolumeshostTypeDef,
        "name": str,
    },
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesvolumesTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesvolumesTypeDef
):
    """
    Type definition for `DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerProperties` `volumes`

    A data volume used in a job's container properties.

    - **host** *(dict) --*

      The contents of the ``host`` parameter determine whether your data volume persists
      on the host container instance and where it is stored. If the host parameter is
      empty, then the Docker daemon assigns a host path for your data volume. However,
      the data is not guaranteed to persist after the containers associated with it stop
      running.

      - **sourcePath** *(string) --*

        The path on the host container instance that is presented to the container. If
        this parameter is empty, then the Docker daemon has assigned a host path for you.
        If this parameter contains a file location, then the data volume persists at the
        specified location on the host container instance until you delete it manually.
        If the source path location does not exist on the host container instance, the
        Docker daemon creates it. If the location does exist, the contents of the source
        path folder are exported.

    - **name** *(string) --*

      The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
      hyphens, and underscores are allowed. This name is referenced in the
      ``sourceVolume`` parameter of container definition ``mountPoints`` .
    """


_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesTypeDef",
    {
        "image": str,
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "jobRoleArn": str,
        "volumes": List[
            DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesvolumesTypeDef
        ],
        "environment": List[
            DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesenvironmentTypeDef
        ],
        "mountPoints": List[
            DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesmountPointsTypeDef
        ],
        "readonlyRootFilesystem": bool,
        "privileged": bool,
        "ulimits": List[
            DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesulimitsTypeDef
        ],
        "user": str,
        "instanceType": str,
        "resourceRequirements": List[
            DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesresourceRequirementsTypeDef
        ],
        "linuxParameters": DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertieslinuxParametersTypeDef,
    },
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesTypeDef
):
    """
    Type definition for `DescribeJobDefinitionsPaginateResponsejobDefinitions` `containerProperties`

    An object with various properties specific to container-based jobs.

    - **image** *(string) --*

      The image used to start a container. This string is passed directly to the Docker
      daemon. Images in the Docker Hub registry are available by default. Other repositories
      are specified with `` *repository-url* /*image* :*tag* `` . Up to 255 letters
      (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward
      slashes, and number signs are allowed. This parameter maps to ``Image`` in the `Create
      a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section
      of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``IMAGE`` parameter of `docker run <https://docs.docker.com/engine/reference/run/>`__ .

      * Images in Amazon ECR repositories use the full registry and repository URI (for
      example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ).

      * Images in official repositories on Docker Hub use a single name (for example,
      ``ubuntu`` or ``mongo`` ).

      * Images in other repositories on Docker Hub are qualified with an organization name
      (for example, ``amazon/amazon-ecs-agent`` ).

      * Images in other online repositories are qualified further by a domain name (for
      example, ``quay.io/assemblyline/ubuntu`` ).

    - **vcpus** *(integer) --*

      The number of vCPUs reserved for the container. This parameter maps to ``CpuShares`` in
      the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--cpu-shares`` option to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ . Each vCPU is equivalent to 1,024
      CPU shares. You must specify at least one vCPU.

    - **memory** *(integer) --*

      The hard limit (in MiB) of memory to present to the container. If your container
      attempts to exceed the memory specified here, the container is killed. This parameter
      maps to ``Memory`` in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--memory``
      option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . You must
      specify at least 4 MiB of memory for a job.

      .. note::

        If you are trying to maximize your resource utilization by providing your jobs as
        much memory as possible for a particular instance type, see `Memory Management
        <https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`__ in the
        *AWS Batch User Guide* .

    - **command** *(list) --*

      The command that is passed to the container. This parameter maps to ``Cmd`` in the
      `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
      section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and
      the ``COMMAND`` parameter to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ . For more information, see
      `https\\://docs.docker.com/engine/reference/builder/#cmd
      <https://docs.docker.com/engine/reference/builder/#cmd>`__ .

      - *(string) --*

    - **jobRoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS
      permissions.

    - **volumes** *(list) --*

      A list of data volumes used in a job.

      - *(dict) --*

        A data volume used in a job's container properties.

        - **host** *(dict) --*

          The contents of the ``host`` parameter determine whether your data volume persists
          on the host container instance and where it is stored. If the host parameter is
          empty, then the Docker daemon assigns a host path for your data volume. However,
          the data is not guaranteed to persist after the containers associated with it stop
          running.

          - **sourcePath** *(string) --*

            The path on the host container instance that is presented to the container. If
            this parameter is empty, then the Docker daemon has assigned a host path for you.
            If this parameter contains a file location, then the data volume persists at the
            specified location on the host container instance until you delete it manually.
            If the source path location does not exist on the host container instance, the
            Docker daemon creates it. If the location does exist, the contents of the source
            path folder are exported.

        - **name** *(string) --*

          The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
          hyphens, and underscores are allowed. This name is referenced in the
          ``sourceVolume`` parameter of container definition ``mountPoints`` .

    - **environment** *(list) --*

      The environment variables to pass to a container. This parameter maps to ``Env`` in the
      `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
      section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and
      the ``--env`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

      .. warning::

        We do not recommend using plaintext environment variables for sensitive information,
        such as credential data.

      .. note::

        Environment variables must not start with ``AWS_BATCH`` ; this naming convention is
        reserved for variables that are set by the AWS Batch service.

      - *(dict) --*

        A key-value pair object.

        - **name** *(string) --*

          The name of the key-value pair. For environment variables, this is the name of the
          environment variable.

        - **value** *(string) --*

          The value of the key-value pair. For environment variables, this is the value of
          the environment variable.

    - **mountPoints** *(list) --*

      The mount points for data volumes in your container. This parameter maps to ``Volumes``
      in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--volume``
      option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

      - *(dict) --*

        Details on a Docker volume mount point that is used in a job's container properties.
        This parameter maps to ``Volumes`` in the `Create a container
        <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
        section of the Docker Remote API and the ``--volume`` option to docker run.

        - **containerPath** *(string) --*

          The path on the container at which to mount the host volume.

        - **readOnly** *(boolean) --*

          If this value is ``true`` , the container has read-only access to the volume;
          otherwise, the container can write to the volume. The default value is ``false`` .

        - **sourceVolume** *(string) --*

          The name of the volume to mount.

    - **readonlyRootFilesystem** *(boolean) --*

      When this parameter is true, the container is given read-only access to its root file
      system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--read-only`` option to ``docker run`` .

    - **privileged** *(boolean) --*

      When this parameter is true, the container is given elevated privileges on the host
      container instance (similar to the ``root`` user). This parameter maps to
      ``Privileged`` in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--privileged`` option to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ .

    - **ulimits** *(list) --*

      A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits`` in
      the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--ulimit``
      option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

      - *(dict) --*

        The ``ulimit`` settings to pass to the container.

        - **hardLimit** *(integer) --*

          The hard limit for the ``ulimit`` type.

        - **name** *(string) --*

          The ``type`` of the ``ulimit`` .

        - **softLimit** *(integer) --*

          The soft limit for the ``ulimit`` type.

    - **user** *(string) --*

      The user name to use inside the container. This parameter maps to ``User`` in the
      `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
      section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and
      the ``--user`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__
      .

    - **instanceType** *(string) --*

      The instance type to use for a multi-node parallel job. Currently all node groups in a
      multi-node parallel job must use the same instance type. This parameter is not valid
      for single-node container jobs.

    - **resourceRequirements** *(list) --*

      The type and amount of a resource to assign to a container. Currently, the only
      supported resource is ``GPU`` .

      - *(dict) --*

        The type and amount of a resource to assign to a container. Currently, the only
        supported resource type is ``GPU`` .

        - **value** *(string) --*

          The number of physical GPUs to reserve for the container. The number of GPUs
          reserved for all containers in a job should not exceed the number of available GPUs
          on the compute resource that the job is launched on.

        - **type** *(string) --*

          The type of resource to assign to a container. Currently, the only supported
          resource type is ``GPU`` .

    - **linuxParameters** *(dict) --*

      Linux-specific modifications that are applied to the container, such as details for
      device mappings.

      - **devices** *(list) --*

        Any host devices to expose to the container. This parameter maps to ``Devices`` in
        the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--device`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__
        .

        - *(dict) --*

          An object representing a container instance host device.

          - **hostPath** *(string) --*

            The path for the device on the host container instance.

          - **containerPath** *(string) --*

            The path inside the container at which to expose the host device. By default the
            ``hostPath`` value is used.

          - **permissions** *(list) --*

            The explicit permissions to provide to the container for the device. By default,
            the container has permissions for ``read`` , ``write`` , and ``mknod`` for the
            device.

            - *(string) --*
    """


_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef
):
    """
    Type definition for `DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainer` `environment`

    A key-value pair object.

    - **name** *(string) --*

      The name of the key-value pair. For environment variables, this is the name
      of the environment variable.

    - **value** *(string) --*

      The value of the key-value pair. For environment variables, this is the value
      of the environment variable.
    """


_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef",
    {"hostPath": str, "containerPath": str, "permissions": List[str]},
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef
):
    """
    Type definition for `DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParameters` `devices`

    An object representing a container instance host device.

    - **hostPath** *(string) --*

      The path for the device on the host container instance.

    - **containerPath** *(string) --*

      The path inside the container at which to expose the host device. By
      default the ``hostPath`` value is used.

    - **permissions** *(list) --*

      The explicit permissions to provide to the container for the device. By
      default, the container has permissions for ``read`` , ``write`` , and
      ``mknod`` for the device.

      - *(string) --*
    """


_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef",
    {
        "devices": List[
            DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef
        ]
    },
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef
):
    """
    Type definition for `DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainer` `linuxParameters`

    Linux-specific modifications that are applied to the container, such as details
    for device mappings.

    - **devices** *(list) --*

      Any host devices to expose to the container. This parameter maps to ``Devices``
      in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of
      the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--device`` option to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ .

      - *(dict) --*

        An object representing a container instance host device.

        - **hostPath** *(string) --*

          The path for the device on the host container instance.

        - **containerPath** *(string) --*

          The path inside the container at which to expose the host device. By
          default the ``hostPath`` value is used.

        - **permissions** *(list) --*

          The explicit permissions to provide to the container for the device. By
          default, the container has permissions for ``read`` , ``write`` , and
          ``mknod`` for the device.

          - *(string) --*
    """


_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef",
    {"containerPath": str, "readOnly": bool, "sourceVolume": str},
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef
):
    """
    Type definition for `DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainer` `mountPoints`

    Details on a Docker volume mount point that is used in a job's container
    properties. This parameter maps to ``Volumes`` in the `Create a container
    <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
    section of the Docker Remote API and the ``--volume`` option to docker run.

    - **containerPath** *(string) --*

      The path on the container at which to mount the host volume.

    - **readOnly** *(boolean) --*

      If this value is ``true`` , the container has read-only access to the volume;
      otherwise, the container can write to the volume. The default value is
      ``false`` .

    - **sourceVolume** *(string) --*

      The name of the volume to mount.
    """


_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef",
    {"value": str, "type": str},
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef
):
    """
    Type definition for `DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainer` `resourceRequirements`

    The type and amount of a resource to assign to a container. Currently, the only
    supported resource type is ``GPU`` .

    - **value** *(string) --*

      The number of physical GPUs to reserve for the container. The number of GPUs
      reserved for all containers in a job should not exceed the number of
      available GPUs on the compute resource that the job is launched on.

    - **type** *(string) --*

      The type of resource to assign to a container. Currently, the only supported
      resource type is ``GPU`` .
    """


_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef",
    {"hardLimit": int, "name": str, "softLimit": int},
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef
):
    """
    Type definition for `DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainer` `ulimits`

    The ``ulimit`` settings to pass to the container.

    - **hardLimit** *(integer) --*

      The hard limit for the ``ulimit`` type.

    - **name** *(string) --*

      The ``type`` of the ``ulimit`` .

    - **softLimit** *(integer) --*

      The soft limit for the ``ulimit`` type.
    """


_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef",
    {"sourcePath": str},
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef
):
    """
    Type definition for `DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumes` `host`

    The contents of the ``host`` parameter determine whether your data volume
    persists on the host container instance and where it is stored. If the host
    parameter is empty, then the Docker daemon assigns a host path for your data
    volume. However, the data is not guaranteed to persist after the containers
    associated with it stop running.

    - **sourcePath** *(string) --*

      The path on the host container instance that is presented to the container.
      If this parameter is empty, then the Docker daemon has assigned a host path
      for you. If this parameter contains a file location, then the data volume
      persists at the specified location on the host container instance until you
      delete it manually. If the source path location does not exist on the host
      container instance, the Docker daemon creates it. If the location does
      exist, the contents of the source path folder are exported.
    """


_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumesTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumesTypeDef",
    {
        "host": DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef,
        "name": str,
    },
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumesTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumesTypeDef
):
    """
    Type definition for `DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainer` `volumes`

    A data volume used in a job's container properties.

    - **host** *(dict) --*

      The contents of the ``host`` parameter determine whether your data volume
      persists on the host container instance and where it is stored. If the host
      parameter is empty, then the Docker daemon assigns a host path for your data
      volume. However, the data is not guaranteed to persist after the containers
      associated with it stop running.

      - **sourcePath** *(string) --*

        The path on the host container instance that is presented to the container.
        If this parameter is empty, then the Docker daemon has assigned a host path
        for you. If this parameter contains a file location, then the data volume
        persists at the specified location on the host container instance until you
        delete it manually. If the source path location does not exist on the host
        container instance, the Docker daemon creates it. If the location does
        exist, the contents of the source path folder are exported.

    - **name** *(string) --*

      The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
      hyphens, and underscores are allowed. This name is referenced in the
      ``sourceVolume`` parameter of container definition ``mountPoints`` .
    """


_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerTypeDef",
    {
        "image": str,
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "jobRoleArn": str,
        "volumes": List[
            DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumesTypeDef
        ],
        "environment": List[
            DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef
        ],
        "mountPoints": List[
            DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef
        ],
        "readonlyRootFilesystem": bool,
        "privileged": bool,
        "ulimits": List[
            DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef
        ],
        "user": str,
        "instanceType": str,
        "resourceRequirements": List[
            DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef
        ],
        "linuxParameters": DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef,
    },
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerTypeDef
):
    """
    Type definition for `DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangeProperties` `container`

    The container details for the node range.

    - **image** *(string) --*

      The image used to start a container. This string is passed directly to the Docker
      daemon. Images in the Docker Hub registry are available by default. Other
      repositories are specified with `` *repository-url* /*image* :*tag* `` . Up to
      255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons,
      periods, forward slashes, and number signs are allowed. This parameter maps to
      ``Image`` in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``IMAGE`` parameter of `docker run
      <https://docs.docker.com/engine/reference/run/>`__ .

      * Images in Amazon ECR repositories use the full registry and repository URI (for
      example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ).

      * Images in official repositories on Docker Hub use a single name (for example,
      ``ubuntu`` or ``mongo`` ).

      * Images in other repositories on Docker Hub are qualified with an organization
      name (for example, ``amazon/amazon-ecs-agent`` ).

      * Images in other online repositories are qualified further by a domain name (for
      example, ``quay.io/assemblyline/ubuntu`` ).

    - **vcpus** *(integer) --*

      The number of vCPUs reserved for the container. This parameter maps to
      ``CpuShares`` in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--cpu-shares`` option to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ . Each vCPU is equivalent to
      1,024 CPU shares. You must specify at least one vCPU.

    - **memory** *(integer) --*

      The hard limit (in MiB) of memory to present to the container. If your container
      attempts to exceed the memory specified here, the container is killed. This
      parameter maps to ``Memory`` in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--memory`` option to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ . You must specify at least 4
      MiB of memory for a job.

      .. note::

        If you are trying to maximize your resource utilization by providing your jobs
        as much memory as possible for a particular instance type, see `Memory
        Management
        <https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`__
        in the *AWS Batch User Guide* .

    - **command** *(list) --*

      The command that is passed to the container. This parameter maps to ``Cmd`` in
      the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``COMMAND`` parameter to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ . For more information, see
      `https\\://docs.docker.com/engine/reference/builder/#cmd
      <https://docs.docker.com/engine/reference/builder/#cmd>`__ .

      - *(string) --*

    - **jobRoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that the container can assume for
      AWS permissions.

    - **volumes** *(list) --*

      A list of data volumes used in a job.

      - *(dict) --*

        A data volume used in a job's container properties.

        - **host** *(dict) --*

          The contents of the ``host`` parameter determine whether your data volume
          persists on the host container instance and where it is stored. If the host
          parameter is empty, then the Docker daemon assigns a host path for your data
          volume. However, the data is not guaranteed to persist after the containers
          associated with it stop running.

          - **sourcePath** *(string) --*

            The path on the host container instance that is presented to the container.
            If this parameter is empty, then the Docker daemon has assigned a host path
            for you. If this parameter contains a file location, then the data volume
            persists at the specified location on the host container instance until you
            delete it manually. If the source path location does not exist on the host
            container instance, the Docker daemon creates it. If the location does
            exist, the contents of the source path folder are exported.

        - **name** *(string) --*

          The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
          hyphens, and underscores are allowed. This name is referenced in the
          ``sourceVolume`` parameter of container definition ``mountPoints`` .

    - **environment** *(list) --*

      The environment variables to pass to a container. This parameter maps to ``Env``
      in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--env`` option to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ .

      .. warning::

        We do not recommend using plaintext environment variables for sensitive
        information, such as credential data.

      .. note::

        Environment variables must not start with ``AWS_BATCH`` ; this naming
        convention is reserved for variables that are set by the AWS Batch service.

      - *(dict) --*

        A key-value pair object.

        - **name** *(string) --*

          The name of the key-value pair. For environment variables, this is the name
          of the environment variable.

        - **value** *(string) --*

          The value of the key-value pair. For environment variables, this is the value
          of the environment variable.

    - **mountPoints** *(list) --*

      The mount points for data volumes in your container. This parameter maps to
      ``Volumes`` in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--volume`` option to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ .

      - *(dict) --*

        Details on a Docker volume mount point that is used in a job's container
        properties. This parameter maps to ``Volumes`` in the `Create a container
        <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
        section of the Docker Remote API and the ``--volume`` option to docker run.

        - **containerPath** *(string) --*

          The path on the container at which to mount the host volume.

        - **readOnly** *(boolean) --*

          If this value is ``true`` , the container has read-only access to the volume;
          otherwise, the container can write to the volume. The default value is
          ``false`` .

        - **sourceVolume** *(string) --*

          The name of the volume to mount.

    - **readonlyRootFilesystem** *(boolean) --*

      When this parameter is true, the container is given read-only access to its root
      file system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--read-only`` option to ``docker run`` .

    - **privileged** *(boolean) --*

      When this parameter is true, the container is given elevated privileges on the
      host container instance (similar to the ``root`` user). This parameter maps to
      ``Privileged`` in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--privileged`` option to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ .

    - **ulimits** *(list) --*

      A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits``
      in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--ulimit`` option to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ .

      - *(dict) --*

        The ``ulimit`` settings to pass to the container.

        - **hardLimit** *(integer) --*

          The hard limit for the ``ulimit`` type.

        - **name** *(string) --*

          The ``type`` of the ``ulimit`` .

        - **softLimit** *(integer) --*

          The soft limit for the ``ulimit`` type.

    - **user** *(string) --*

      The user name to use inside the container. This parameter maps to ``User`` in the
      `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
      `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
      ``--user`` option to `docker run
      <https://docs.docker.com/engine/reference/run/>`__ .

    - **instanceType** *(string) --*

      The instance type to use for a multi-node parallel job. Currently all node groups
      in a multi-node parallel job must use the same instance type. This parameter is
      not valid for single-node container jobs.

    - **resourceRequirements** *(list) --*

      The type and amount of a resource to assign to a container. Currently, the only
      supported resource is ``GPU`` .

      - *(dict) --*

        The type and amount of a resource to assign to a container. Currently, the only
        supported resource type is ``GPU`` .

        - **value** *(string) --*

          The number of physical GPUs to reserve for the container. The number of GPUs
          reserved for all containers in a job should not exceed the number of
          available GPUs on the compute resource that the job is launched on.

        - **type** *(string) --*

          The type of resource to assign to a container. Currently, the only supported
          resource type is ``GPU`` .

    - **linuxParameters** *(dict) --*

      Linux-specific modifications that are applied to the container, such as details
      for device mappings.

      - **devices** *(list) --*

        Any host devices to expose to the container. This parameter maps to ``Devices``
        in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of
        the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--device`` option to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ .

        - *(dict) --*

          An object representing a container instance host device.

          - **hostPath** *(string) --*

            The path for the device on the host container instance.

          - **containerPath** *(string) --*

            The path inside the container at which to expose the host device. By
            default the ``hostPath`` value is used.

          - **permissions** *(list) --*

            The explicit permissions to provide to the container for the device. By
            default, the container has permissions for ``read`` , ``write`` , and
            ``mknod`` for the device.

            - *(string) --*
    """


_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiesTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiesTypeDef",
    {
        "targetNodes": str,
        "container": DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerTypeDef,
    },
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiesTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiesTypeDef
):
    """
    Type definition for `DescribeJobDefinitionsPaginateResponsejobDefinitionsnodeProperties` `nodeRangeProperties`

    An object representing the properties of the node range for a multi-node parallel job.

    - **targetNodes** *(string) --*

      The range of nodes, using node index values. A range of ``0:3`` indicates nodes
      with index values of ``0`` through ``3`` . If the starting range value is omitted
      (``:n`` ), then ``0`` is used to start the range. If the ending range value is
      omitted (``n:`` ), then the highest possible node index is used to end the range.
      Your accumulative node ranges must account for all nodes (0:n). You may nest node
      ranges, for example 0:10 and 4:5, in which case the 4:5 range properties override
      the 0:10 properties.

    - **container** *(dict) --*

      The container details for the node range.

      - **image** *(string) --*

        The image used to start a container. This string is passed directly to the Docker
        daemon. Images in the Docker Hub registry are available by default. Other
        repositories are specified with `` *repository-url* /*image* :*tag* `` . Up to
        255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons,
        periods, forward slashes, and number signs are allowed. This parameter maps to
        ``Image`` in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``IMAGE`` parameter of `docker run
        <https://docs.docker.com/engine/reference/run/>`__ .

        * Images in Amazon ECR repositories use the full registry and repository URI (for
        example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ).

        * Images in official repositories on Docker Hub use a single name (for example,
        ``ubuntu`` or ``mongo`` ).

        * Images in other repositories on Docker Hub are qualified with an organization
        name (for example, ``amazon/amazon-ecs-agent`` ).

        * Images in other online repositories are qualified further by a domain name (for
        example, ``quay.io/assemblyline/ubuntu`` ).

      - **vcpus** *(integer) --*

        The number of vCPUs reserved for the container. This parameter maps to
        ``CpuShares`` in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--cpu-shares`` option to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ . Each vCPU is equivalent to
        1,024 CPU shares. You must specify at least one vCPU.

      - **memory** *(integer) --*

        The hard limit (in MiB) of memory to present to the container. If your container
        attempts to exceed the memory specified here, the container is killed. This
        parameter maps to ``Memory`` in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--memory`` option to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ . You must specify at least 4
        MiB of memory for a job.

        .. note::

          If you are trying to maximize your resource utilization by providing your jobs
          as much memory as possible for a particular instance type, see `Memory
          Management
          <https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`__
          in the *AWS Batch User Guide* .

      - **command** *(list) --*

        The command that is passed to the container. This parameter maps to ``Cmd`` in
        the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``COMMAND`` parameter to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ . For more information, see
        `https\\://docs.docker.com/engine/reference/builder/#cmd
        <https://docs.docker.com/engine/reference/builder/#cmd>`__ .

        - *(string) --*

      - **jobRoleArn** *(string) --*

        The Amazon Resource Name (ARN) of the IAM role that the container can assume for
        AWS permissions.

      - **volumes** *(list) --*

        A list of data volumes used in a job.

        - *(dict) --*

          A data volume used in a job's container properties.

          - **host** *(dict) --*

            The contents of the ``host`` parameter determine whether your data volume
            persists on the host container instance and where it is stored. If the host
            parameter is empty, then the Docker daemon assigns a host path for your data
            volume. However, the data is not guaranteed to persist after the containers
            associated with it stop running.

            - **sourcePath** *(string) --*

              The path on the host container instance that is presented to the container.
              If this parameter is empty, then the Docker daemon has assigned a host path
              for you. If this parameter contains a file location, then the data volume
              persists at the specified location on the host container instance until you
              delete it manually. If the source path location does not exist on the host
              container instance, the Docker daemon creates it. If the location does
              exist, the contents of the source path folder are exported.

          - **name** *(string) --*

            The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
            hyphens, and underscores are allowed. This name is referenced in the
            ``sourceVolume`` parameter of container definition ``mountPoints`` .

      - **environment** *(list) --*

        The environment variables to pass to a container. This parameter maps to ``Env``
        in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--env`` option to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ .

        .. warning::

          We do not recommend using plaintext environment variables for sensitive
          information, such as credential data.

        .. note::

          Environment variables must not start with ``AWS_BATCH`` ; this naming
          convention is reserved for variables that are set by the AWS Batch service.

        - *(dict) --*

          A key-value pair object.

          - **name** *(string) --*

            The name of the key-value pair. For environment variables, this is the name
            of the environment variable.

          - **value** *(string) --*

            The value of the key-value pair. For environment variables, this is the value
            of the environment variable.

      - **mountPoints** *(list) --*

        The mount points for data volumes in your container. This parameter maps to
        ``Volumes`` in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--volume`` option to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ .

        - *(dict) --*

          Details on a Docker volume mount point that is used in a job's container
          properties. This parameter maps to ``Volumes`` in the `Create a container
          <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
          section of the Docker Remote API and the ``--volume`` option to docker run.

          - **containerPath** *(string) --*

            The path on the container at which to mount the host volume.

          - **readOnly** *(boolean) --*

            If this value is ``true`` , the container has read-only access to the volume;
            otherwise, the container can write to the volume. The default value is
            ``false`` .

          - **sourceVolume** *(string) --*

            The name of the volume to mount.

      - **readonlyRootFilesystem** *(boolean) --*

        When this parameter is true, the container is given read-only access to its root
        file system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--read-only`` option to ``docker run`` .

      - **privileged** *(boolean) --*

        When this parameter is true, the container is given elevated privileges on the
        host container instance (similar to the ``root`` user). This parameter maps to
        ``Privileged`` in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--privileged`` option to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ .

      - **ulimits** *(list) --*

        A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits``
        in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--ulimit`` option to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ .

        - *(dict) --*

          The ``ulimit`` settings to pass to the container.

          - **hardLimit** *(integer) --*

            The hard limit for the ``ulimit`` type.

          - **name** *(string) --*

            The ``type`` of the ``ulimit`` .

          - **softLimit** *(integer) --*

            The soft limit for the ``ulimit`` type.

      - **user** *(string) --*

        The user name to use inside the container. This parameter maps to ``User`` in the
        `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--user`` option to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ .

      - **instanceType** *(string) --*

        The instance type to use for a multi-node parallel job. Currently all node groups
        in a multi-node parallel job must use the same instance type. This parameter is
        not valid for single-node container jobs.

      - **resourceRequirements** *(list) --*

        The type and amount of a resource to assign to a container. Currently, the only
        supported resource is ``GPU`` .

        - *(dict) --*

          The type and amount of a resource to assign to a container. Currently, the only
          supported resource type is ``GPU`` .

          - **value** *(string) --*

            The number of physical GPUs to reserve for the container. The number of GPUs
            reserved for all containers in a job should not exceed the number of
            available GPUs on the compute resource that the job is launched on.

          - **type** *(string) --*

            The type of resource to assign to a container. Currently, the only supported
            resource type is ``GPU`` .

      - **linuxParameters** *(dict) --*

        Linux-specific modifications that are applied to the container, such as details
        for device mappings.

        - **devices** *(list) --*

          Any host devices to expose to the container. This parameter maps to ``Devices``
          in the `Create a container
          <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of
          the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
          ``--device`` option to `docker run
          <https://docs.docker.com/engine/reference/run/>`__ .

          - *(dict) --*

            An object representing a container instance host device.

            - **hostPath** *(string) --*

              The path for the device on the host container instance.

            - **containerPath** *(string) --*

              The path inside the container at which to expose the host device. By
              default the ``hostPath`` value is used.

            - **permissions** *(list) --*

              The explicit permissions to provide to the container for the device. By
              default, the container has permissions for ``read`` , ``write`` , and
              ``mknod`` for the device.

              - *(string) --*
    """


_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesTypeDef",
    {
        "numNodes": int,
        "mainNode": int,
        "nodeRangeProperties": List[
            DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiesTypeDef
        ],
    },
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesTypeDef
):
    """
    Type definition for `DescribeJobDefinitionsPaginateResponsejobDefinitions` `nodeProperties`

    An object with various properties specific to multi-node parallel jobs.

    - **numNodes** *(integer) --*

      The number of nodes associated with a multi-node parallel job.

    - **mainNode** *(integer) --*

      Specifies the node index for the main node of a multi-node parallel job. This node
      index value must be fewer than the number of nodes.

    - **nodeRangeProperties** *(list) --*

      A list of node ranges and their properties associated with a multi-node parallel job.

      - *(dict) --*

        An object representing the properties of the node range for a multi-node parallel job.

        - **targetNodes** *(string) --*

          The range of nodes, using node index values. A range of ``0:3`` indicates nodes
          with index values of ``0`` through ``3`` . If the starting range value is omitted
          (``:n`` ), then ``0`` is used to start the range. If the ending range value is
          omitted (``n:`` ), then the highest possible node index is used to end the range.
          Your accumulative node ranges must account for all nodes (0:n). You may nest node
          ranges, for example 0:10 and 4:5, in which case the 4:5 range properties override
          the 0:10 properties.

        - **container** *(dict) --*

          The container details for the node range.

          - **image** *(string) --*

            The image used to start a container. This string is passed directly to the Docker
            daemon. Images in the Docker Hub registry are available by default. Other
            repositories are specified with `` *repository-url* /*image* :*tag* `` . Up to
            255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons,
            periods, forward slashes, and number signs are allowed. This parameter maps to
            ``Image`` in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``IMAGE`` parameter of `docker run
            <https://docs.docker.com/engine/reference/run/>`__ .

            * Images in Amazon ECR repositories use the full registry and repository URI (for
            example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ).

            * Images in official repositories on Docker Hub use a single name (for example,
            ``ubuntu`` or ``mongo`` ).

            * Images in other repositories on Docker Hub are qualified with an organization
            name (for example, ``amazon/amazon-ecs-agent`` ).

            * Images in other online repositories are qualified further by a domain name (for
            example, ``quay.io/assemblyline/ubuntu`` ).

          - **vcpus** *(integer) --*

            The number of vCPUs reserved for the container. This parameter maps to
            ``CpuShares`` in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``--cpu-shares`` option to `docker run
            <https://docs.docker.com/engine/reference/run/>`__ . Each vCPU is equivalent to
            1,024 CPU shares. You must specify at least one vCPU.

          - **memory** *(integer) --*

            The hard limit (in MiB) of memory to present to the container. If your container
            attempts to exceed the memory specified here, the container is killed. This
            parameter maps to ``Memory`` in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``--memory`` option to `docker run
            <https://docs.docker.com/engine/reference/run/>`__ . You must specify at least 4
            MiB of memory for a job.

            .. note::

              If you are trying to maximize your resource utilization by providing your jobs
              as much memory as possible for a particular instance type, see `Memory
              Management
              <https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`__
              in the *AWS Batch User Guide* .

          - **command** *(list) --*

            The command that is passed to the container. This parameter maps to ``Cmd`` in
            the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``COMMAND`` parameter to `docker run
            <https://docs.docker.com/engine/reference/run/>`__ . For more information, see
            `https\\://docs.docker.com/engine/reference/builder/#cmd
            <https://docs.docker.com/engine/reference/builder/#cmd>`__ .

            - *(string) --*

          - **jobRoleArn** *(string) --*

            The Amazon Resource Name (ARN) of the IAM role that the container can assume for
            AWS permissions.

          - **volumes** *(list) --*

            A list of data volumes used in a job.

            - *(dict) --*

              A data volume used in a job's container properties.

              - **host** *(dict) --*

                The contents of the ``host`` parameter determine whether your data volume
                persists on the host container instance and where it is stored. If the host
                parameter is empty, then the Docker daemon assigns a host path for your data
                volume. However, the data is not guaranteed to persist after the containers
                associated with it stop running.

                - **sourcePath** *(string) --*

                  The path on the host container instance that is presented to the container.
                  If this parameter is empty, then the Docker daemon has assigned a host path
                  for you. If this parameter contains a file location, then the data volume
                  persists at the specified location on the host container instance until you
                  delete it manually. If the source path location does not exist on the host
                  container instance, the Docker daemon creates it. If the location does
                  exist, the contents of the source path folder are exported.

              - **name** *(string) --*

                The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
                hyphens, and underscores are allowed. This name is referenced in the
                ``sourceVolume`` parameter of container definition ``mountPoints`` .

          - **environment** *(list) --*

            The environment variables to pass to a container. This parameter maps to ``Env``
            in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``--env`` option to `docker run
            <https://docs.docker.com/engine/reference/run/>`__ .

            .. warning::

              We do not recommend using plaintext environment variables for sensitive
              information, such as credential data.

            .. note::

              Environment variables must not start with ``AWS_BATCH`` ; this naming
              convention is reserved for variables that are set by the AWS Batch service.

            - *(dict) --*

              A key-value pair object.

              - **name** *(string) --*

                The name of the key-value pair. For environment variables, this is the name
                of the environment variable.

              - **value** *(string) --*

                The value of the key-value pair. For environment variables, this is the value
                of the environment variable.

          - **mountPoints** *(list) --*

            The mount points for data volumes in your container. This parameter maps to
            ``Volumes`` in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``--volume`` option to `docker run
            <https://docs.docker.com/engine/reference/run/>`__ .

            - *(dict) --*

              Details on a Docker volume mount point that is used in a job's container
              properties. This parameter maps to ``Volumes`` in the `Create a container
              <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
              section of the Docker Remote API and the ``--volume`` option to docker run.

              - **containerPath** *(string) --*

                The path on the container at which to mount the host volume.

              - **readOnly** *(boolean) --*

                If this value is ``true`` , the container has read-only access to the volume;
                otherwise, the container can write to the volume. The default value is
                ``false`` .

              - **sourceVolume** *(string) --*

                The name of the volume to mount.

          - **readonlyRootFilesystem** *(boolean) --*

            When this parameter is true, the container is given read-only access to its root
            file system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``--read-only`` option to ``docker run`` .

          - **privileged** *(boolean) --*

            When this parameter is true, the container is given elevated privileges on the
            host container instance (similar to the ``root`` user). This parameter maps to
            ``Privileged`` in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``--privileged`` option to `docker run
            <https://docs.docker.com/engine/reference/run/>`__ .

          - **ulimits** *(list) --*

            A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits``
            in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``--ulimit`` option to `docker run
            <https://docs.docker.com/engine/reference/run/>`__ .

            - *(dict) --*

              The ``ulimit`` settings to pass to the container.

              - **hardLimit** *(integer) --*

                The hard limit for the ``ulimit`` type.

              - **name** *(string) --*

                The ``type`` of the ``ulimit`` .

              - **softLimit** *(integer) --*

                The soft limit for the ``ulimit`` type.

          - **user** *(string) --*

            The user name to use inside the container. This parameter maps to ``User`` in the
            `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``--user`` option to `docker run
            <https://docs.docker.com/engine/reference/run/>`__ .

          - **instanceType** *(string) --*

            The instance type to use for a multi-node parallel job. Currently all node groups
            in a multi-node parallel job must use the same instance type. This parameter is
            not valid for single-node container jobs.

          - **resourceRequirements** *(list) --*

            The type and amount of a resource to assign to a container. Currently, the only
            supported resource is ``GPU`` .

            - *(dict) --*

              The type and amount of a resource to assign to a container. Currently, the only
              supported resource type is ``GPU`` .

              - **value** *(string) --*

                The number of physical GPUs to reserve for the container. The number of GPUs
                reserved for all containers in a job should not exceed the number of
                available GPUs on the compute resource that the job is launched on.

              - **type** *(string) --*

                The type of resource to assign to a container. Currently, the only supported
                resource type is ``GPU`` .

          - **linuxParameters** *(dict) --*

            Linux-specific modifications that are applied to the container, such as details
            for device mappings.

            - **devices** *(list) --*

              Any host devices to expose to the container. This parameter maps to ``Devices``
              in the `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of
              the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``--device`` option to `docker run
              <https://docs.docker.com/engine/reference/run/>`__ .

              - *(dict) --*

                An object representing a container instance host device.

                - **hostPath** *(string) --*

                  The path for the device on the host container instance.

                - **containerPath** *(string) --*

                  The path inside the container at which to expose the host device. By
                  default the ``hostPath`` value is used.

                - **permissions** *(list) --*

                  The explicit permissions to provide to the container for the device. By
                  default, the container has permissions for ``read`` , ``write`` , and
                  ``mknod`` for the device.

                  - *(string) --*
    """


_DescribeJobDefinitionsPaginateResponsejobDefinitionsretryStrategyTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionsretryStrategyTypeDef",
    {"attempts": int},
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionsretryStrategyTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionsretryStrategyTypeDef
):
    """
    Type definition for `DescribeJobDefinitionsPaginateResponsejobDefinitions` `retryStrategy`

    The retry strategy to use for failed jobs that are submitted with this job definition.

    - **attempts** *(integer) --*

      The number of times to move a job to the ``RUNNABLE`` status. You may specify between 1
      and 10 attempts. If the value of ``attempts`` is greater than one, the job is retried
      on failure the same number of attempts as the value.
    """


_DescribeJobDefinitionsPaginateResponsejobDefinitionstimeoutTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionstimeoutTypeDef",
    {"attemptDurationSeconds": int},
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionstimeoutTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionstimeoutTypeDef
):
    """
    Type definition for `DescribeJobDefinitionsPaginateResponsejobDefinitions` `timeout`

    The timeout configuration for jobs that are submitted with this job definition. You can
    specify a timeout duration after which AWS Batch terminates your jobs if they have not
    finished.

    - **attemptDurationSeconds** *(integer) --*

      The time duration in seconds (measured from the job attempt's ``startedAt`` timestamp)
      after which AWS Batch terminates your jobs if they have not finished.
    """


_DescribeJobDefinitionsPaginateResponsejobDefinitionsTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionsTypeDef",
    {
        "jobDefinitionName": str,
        "jobDefinitionArn": str,
        "revision": int,
        "status": str,
        "type": str,
        "parameters": Dict[str, str],
        "retryStrategy": DescribeJobDefinitionsPaginateResponsejobDefinitionsretryStrategyTypeDef,
        "containerProperties": DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesTypeDef,
        "timeout": DescribeJobDefinitionsPaginateResponsejobDefinitionstimeoutTypeDef,
        "nodeProperties": DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesTypeDef,
    },
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionsTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionsTypeDef
):
    """
    Type definition for `DescribeJobDefinitionsPaginateResponse` `jobDefinitions`

    An object representing an AWS Batch job definition.

    - **jobDefinitionName** *(string) --*

      The name of the job definition.

    - **jobDefinitionArn** *(string) --*

      The Amazon Resource Name (ARN) for the job definition.

    - **revision** *(integer) --*

      The revision of the job definition.

    - **status** *(string) --*

      The status of the job definition.

    - **type** *(string) --*

      The type of job definition.

    - **parameters** *(dict) --*

      Default parameters or parameter substitution placeholders that are set in the job
      definition. Parameters are specified as a key-value pair mapping. Parameters in a
      ``SubmitJob`` request override any corresponding parameter defaults from the job
      definition. For more information about specifying parameters, see `Job Definition
      Parameters
      <https://docs.aws.amazon.com/batch/latest/userguide/job_definition_parameters.html>`__ in
      the *AWS Batch User Guide* .

      - *(string) --*

        - *(string) --*

    - **retryStrategy** *(dict) --*

      The retry strategy to use for failed jobs that are submitted with this job definition.

      - **attempts** *(integer) --*

        The number of times to move a job to the ``RUNNABLE`` status. You may specify between 1
        and 10 attempts. If the value of ``attempts`` is greater than one, the job is retried
        on failure the same number of attempts as the value.

    - **containerProperties** *(dict) --*

      An object with various properties specific to container-based jobs.

      - **image** *(string) --*

        The image used to start a container. This string is passed directly to the Docker
        daemon. Images in the Docker Hub registry are available by default. Other repositories
        are specified with `` *repository-url* /*image* :*tag* `` . Up to 255 letters
        (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward
        slashes, and number signs are allowed. This parameter maps to ``Image`` in the `Create
        a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section
        of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``IMAGE`` parameter of `docker run <https://docs.docker.com/engine/reference/run/>`__ .

        * Images in Amazon ECR repositories use the full registry and repository URI (for
        example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ).

        * Images in official repositories on Docker Hub use a single name (for example,
        ``ubuntu`` or ``mongo`` ).

        * Images in other repositories on Docker Hub are qualified with an organization name
        (for example, ``amazon/amazon-ecs-agent`` ).

        * Images in other online repositories are qualified further by a domain name (for
        example, ``quay.io/assemblyline/ubuntu`` ).

      - **vcpus** *(integer) --*

        The number of vCPUs reserved for the container. This parameter maps to ``CpuShares`` in
        the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--cpu-shares`` option to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ . Each vCPU is equivalent to 1,024
        CPU shares. You must specify at least one vCPU.

      - **memory** *(integer) --*

        The hard limit (in MiB) of memory to present to the container. If your container
        attempts to exceed the memory specified here, the container is killed. This parameter
        maps to ``Memory`` in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--memory``
        option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . You must
        specify at least 4 MiB of memory for a job.

        .. note::

          If you are trying to maximize your resource utilization by providing your jobs as
          much memory as possible for a particular instance type, see `Memory Management
          <https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`__ in the
          *AWS Batch User Guide* .

      - **command** *(list) --*

        The command that is passed to the container. This parameter maps to ``Cmd`` in the
        `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
        section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and
        the ``COMMAND`` parameter to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ . For more information, see
        `https\\://docs.docker.com/engine/reference/builder/#cmd
        <https://docs.docker.com/engine/reference/builder/#cmd>`__ .

        - *(string) --*

      - **jobRoleArn** *(string) --*

        The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS
        permissions.

      - **volumes** *(list) --*

        A list of data volumes used in a job.

        - *(dict) --*

          A data volume used in a job's container properties.

          - **host** *(dict) --*

            The contents of the ``host`` parameter determine whether your data volume persists
            on the host container instance and where it is stored. If the host parameter is
            empty, then the Docker daemon assigns a host path for your data volume. However,
            the data is not guaranteed to persist after the containers associated with it stop
            running.

            - **sourcePath** *(string) --*

              The path on the host container instance that is presented to the container. If
              this parameter is empty, then the Docker daemon has assigned a host path for you.
              If this parameter contains a file location, then the data volume persists at the
              specified location on the host container instance until you delete it manually.
              If the source path location does not exist on the host container instance, the
              Docker daemon creates it. If the location does exist, the contents of the source
              path folder are exported.

          - **name** *(string) --*

            The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
            hyphens, and underscores are allowed. This name is referenced in the
            ``sourceVolume`` parameter of container definition ``mountPoints`` .

      - **environment** *(list) --*

        The environment variables to pass to a container. This parameter maps to ``Env`` in the
        `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
        section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and
        the ``--env`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

        .. warning::

          We do not recommend using plaintext environment variables for sensitive information,
          such as credential data.

        .. note::

          Environment variables must not start with ``AWS_BATCH`` ; this naming convention is
          reserved for variables that are set by the AWS Batch service.

        - *(dict) --*

          A key-value pair object.

          - **name** *(string) --*

            The name of the key-value pair. For environment variables, this is the name of the
            environment variable.

          - **value** *(string) --*

            The value of the key-value pair. For environment variables, this is the value of
            the environment variable.

      - **mountPoints** *(list) --*

        The mount points for data volumes in your container. This parameter maps to ``Volumes``
        in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--volume``
        option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

        - *(dict) --*

          Details on a Docker volume mount point that is used in a job's container properties.
          This parameter maps to ``Volumes`` in the `Create a container
          <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
          section of the Docker Remote API and the ``--volume`` option to docker run.

          - **containerPath** *(string) --*

            The path on the container at which to mount the host volume.

          - **readOnly** *(boolean) --*

            If this value is ``true`` , the container has read-only access to the volume;
            otherwise, the container can write to the volume. The default value is ``false`` .

          - **sourceVolume** *(string) --*

            The name of the volume to mount.

      - **readonlyRootFilesystem** *(boolean) --*

        When this parameter is true, the container is given read-only access to its root file
        system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--read-only`` option to ``docker run`` .

      - **privileged** *(boolean) --*

        When this parameter is true, the container is given elevated privileges on the host
        container instance (similar to the ``root`` user). This parameter maps to
        ``Privileged`` in the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
        ``--privileged`` option to `docker run
        <https://docs.docker.com/engine/reference/run/>`__ .

      - **ulimits** *(list) --*

        A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits`` in
        the `Create a container
        <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--ulimit``
        option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

        - *(dict) --*

          The ``ulimit`` settings to pass to the container.

          - **hardLimit** *(integer) --*

            The hard limit for the ``ulimit`` type.

          - **name** *(string) --*

            The ``type`` of the ``ulimit`` .

          - **softLimit** *(integer) --*

            The soft limit for the ``ulimit`` type.

      - **user** *(string) --*

        The user name to use inside the container. This parameter maps to ``User`` in the
        `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
        section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and
        the ``--user`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__
        .

      - **instanceType** *(string) --*

        The instance type to use for a multi-node parallel job. Currently all node groups in a
        multi-node parallel job must use the same instance type. This parameter is not valid
        for single-node container jobs.

      - **resourceRequirements** *(list) --*

        The type and amount of a resource to assign to a container. Currently, the only
        supported resource is ``GPU`` .

        - *(dict) --*

          The type and amount of a resource to assign to a container. Currently, the only
          supported resource type is ``GPU`` .

          - **value** *(string) --*

            The number of physical GPUs to reserve for the container. The number of GPUs
            reserved for all containers in a job should not exceed the number of available GPUs
            on the compute resource that the job is launched on.

          - **type** *(string) --*

            The type of resource to assign to a container. Currently, the only supported
            resource type is ``GPU`` .

      - **linuxParameters** *(dict) --*

        Linux-specific modifications that are applied to the container, such as details for
        device mappings.

        - **devices** *(list) --*

          Any host devices to expose to the container. This parameter maps to ``Devices`` in
          the `Create a container
          <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
          `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
          ``--device`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__
          .

          - *(dict) --*

            An object representing a container instance host device.

            - **hostPath** *(string) --*

              The path for the device on the host container instance.

            - **containerPath** *(string) --*

              The path inside the container at which to expose the host device. By default the
              ``hostPath`` value is used.

            - **permissions** *(list) --*

              The explicit permissions to provide to the container for the device. By default,
              the container has permissions for ``read`` , ``write`` , and ``mknod`` for the
              device.

              - *(string) --*

    - **timeout** *(dict) --*

      The timeout configuration for jobs that are submitted with this job definition. You can
      specify a timeout duration after which AWS Batch terminates your jobs if they have not
      finished.

      - **attemptDurationSeconds** *(integer) --*

        The time duration in seconds (measured from the job attempt's ``startedAt`` timestamp)
        after which AWS Batch terminates your jobs if they have not finished.

    - **nodeProperties** *(dict) --*

      An object with various properties specific to multi-node parallel jobs.

      - **numNodes** *(integer) --*

        The number of nodes associated with a multi-node parallel job.

      - **mainNode** *(integer) --*

        Specifies the node index for the main node of a multi-node parallel job. This node
        index value must be fewer than the number of nodes.

      - **nodeRangeProperties** *(list) --*

        A list of node ranges and their properties associated with a multi-node parallel job.

        - *(dict) --*

          An object representing the properties of the node range for a multi-node parallel job.

          - **targetNodes** *(string) --*

            The range of nodes, using node index values. A range of ``0:3`` indicates nodes
            with index values of ``0`` through ``3`` . If the starting range value is omitted
            (``:n`` ), then ``0`` is used to start the range. If the ending range value is
            omitted (``n:`` ), then the highest possible node index is used to end the range.
            Your accumulative node ranges must account for all nodes (0:n). You may nest node
            ranges, for example 0:10 and 4:5, in which case the 4:5 range properties override
            the 0:10 properties.

          - **container** *(dict) --*

            The container details for the node range.

            - **image** *(string) --*

              The image used to start a container. This string is passed directly to the Docker
              daemon. Images in the Docker Hub registry are available by default. Other
              repositories are specified with `` *repository-url* /*image* :*tag* `` . Up to
              255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons,
              periods, forward slashes, and number signs are allowed. This parameter maps to
              ``Image`` in the `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
              `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``IMAGE`` parameter of `docker run
              <https://docs.docker.com/engine/reference/run/>`__ .

              * Images in Amazon ECR repositories use the full registry and repository URI (for
              example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ).

              * Images in official repositories on Docker Hub use a single name (for example,
              ``ubuntu`` or ``mongo`` ).

              * Images in other repositories on Docker Hub are qualified with an organization
              name (for example, ``amazon/amazon-ecs-agent`` ).

              * Images in other online repositories are qualified further by a domain name (for
              example, ``quay.io/assemblyline/ubuntu`` ).

            - **vcpus** *(integer) --*

              The number of vCPUs reserved for the container. This parameter maps to
              ``CpuShares`` in the `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
              `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``--cpu-shares`` option to `docker run
              <https://docs.docker.com/engine/reference/run/>`__ . Each vCPU is equivalent to
              1,024 CPU shares. You must specify at least one vCPU.

            - **memory** *(integer) --*

              The hard limit (in MiB) of memory to present to the container. If your container
              attempts to exceed the memory specified here, the container is killed. This
              parameter maps to ``Memory`` in the `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
              `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``--memory`` option to `docker run
              <https://docs.docker.com/engine/reference/run/>`__ . You must specify at least 4
              MiB of memory for a job.

              .. note::

                If you are trying to maximize your resource utilization by providing your jobs
                as much memory as possible for a particular instance type, see `Memory
                Management
                <https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`__
                in the *AWS Batch User Guide* .

            - **command** *(list) --*

              The command that is passed to the container. This parameter maps to ``Cmd`` in
              the `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
              `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``COMMAND`` parameter to `docker run
              <https://docs.docker.com/engine/reference/run/>`__ . For more information, see
              `https\\://docs.docker.com/engine/reference/builder/#cmd
              <https://docs.docker.com/engine/reference/builder/#cmd>`__ .

              - *(string) --*

            - **jobRoleArn** *(string) --*

              The Amazon Resource Name (ARN) of the IAM role that the container can assume for
              AWS permissions.

            - **volumes** *(list) --*

              A list of data volumes used in a job.

              - *(dict) --*

                A data volume used in a job's container properties.

                - **host** *(dict) --*

                  The contents of the ``host`` parameter determine whether your data volume
                  persists on the host container instance and where it is stored. If the host
                  parameter is empty, then the Docker daemon assigns a host path for your data
                  volume. However, the data is not guaranteed to persist after the containers
                  associated with it stop running.

                  - **sourcePath** *(string) --*

                    The path on the host container instance that is presented to the container.
                    If this parameter is empty, then the Docker daemon has assigned a host path
                    for you. If this parameter contains a file location, then the data volume
                    persists at the specified location on the host container instance until you
                    delete it manually. If the source path location does not exist on the host
                    container instance, the Docker daemon creates it. If the location does
                    exist, the contents of the source path folder are exported.

                - **name** *(string) --*

                  The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
                  hyphens, and underscores are allowed. This name is referenced in the
                  ``sourceVolume`` parameter of container definition ``mountPoints`` .

            - **environment** *(list) --*

              The environment variables to pass to a container. This parameter maps to ``Env``
              in the `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
              `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``--env`` option to `docker run
              <https://docs.docker.com/engine/reference/run/>`__ .

              .. warning::

                We do not recommend using plaintext environment variables for sensitive
                information, such as credential data.

              .. note::

                Environment variables must not start with ``AWS_BATCH`` ; this naming
                convention is reserved for variables that are set by the AWS Batch service.

              - *(dict) --*

                A key-value pair object.

                - **name** *(string) --*

                  The name of the key-value pair. For environment variables, this is the name
                  of the environment variable.

                - **value** *(string) --*

                  The value of the key-value pair. For environment variables, this is the value
                  of the environment variable.

            - **mountPoints** *(list) --*

              The mount points for data volumes in your container. This parameter maps to
              ``Volumes`` in the `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
              `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``--volume`` option to `docker run
              <https://docs.docker.com/engine/reference/run/>`__ .

              - *(dict) --*

                Details on a Docker volume mount point that is used in a job's container
                properties. This parameter maps to ``Volumes`` in the `Create a container
                <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
                section of the Docker Remote API and the ``--volume`` option to docker run.

                - **containerPath** *(string) --*

                  The path on the container at which to mount the host volume.

                - **readOnly** *(boolean) --*

                  If this value is ``true`` , the container has read-only access to the volume;
                  otherwise, the container can write to the volume. The default value is
                  ``false`` .

                - **sourceVolume** *(string) --*

                  The name of the volume to mount.

            - **readonlyRootFilesystem** *(boolean) --*

              When this parameter is true, the container is given read-only access to its root
              file system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
              `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``--read-only`` option to ``docker run`` .

            - **privileged** *(boolean) --*

              When this parameter is true, the container is given elevated privileges on the
              host container instance (similar to the ``root`` user). This parameter maps to
              ``Privileged`` in the `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
              `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``--privileged`` option to `docker run
              <https://docs.docker.com/engine/reference/run/>`__ .

            - **ulimits** *(list) --*

              A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits``
              in the `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
              `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``--ulimit`` option to `docker run
              <https://docs.docker.com/engine/reference/run/>`__ .

              - *(dict) --*

                The ``ulimit`` settings to pass to the container.

                - **hardLimit** *(integer) --*

                  The hard limit for the ``ulimit`` type.

                - **name** *(string) --*

                  The ``type`` of the ``ulimit`` .

                - **softLimit** *(integer) --*

                  The soft limit for the ``ulimit`` type.

            - **user** *(string) --*

              The user name to use inside the container. This parameter maps to ``User`` in the
              `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
              `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``--user`` option to `docker run
              <https://docs.docker.com/engine/reference/run/>`__ .

            - **instanceType** *(string) --*

              The instance type to use for a multi-node parallel job. Currently all node groups
              in a multi-node parallel job must use the same instance type. This parameter is
              not valid for single-node container jobs.

            - **resourceRequirements** *(list) --*

              The type and amount of a resource to assign to a container. Currently, the only
              supported resource is ``GPU`` .

              - *(dict) --*

                The type and amount of a resource to assign to a container. Currently, the only
                supported resource type is ``GPU`` .

                - **value** *(string) --*

                  The number of physical GPUs to reserve for the container. The number of GPUs
                  reserved for all containers in a job should not exceed the number of
                  available GPUs on the compute resource that the job is launched on.

                - **type** *(string) --*

                  The type of resource to assign to a container. Currently, the only supported
                  resource type is ``GPU`` .

            - **linuxParameters** *(dict) --*

              Linux-specific modifications that are applied to the container, such as details
              for device mappings.

              - **devices** *(list) --*

                Any host devices to expose to the container. This parameter maps to ``Devices``
                in the `Create a container
                <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of
                the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                ``--device`` option to `docker run
                <https://docs.docker.com/engine/reference/run/>`__ .

                - *(dict) --*

                  An object representing a container instance host device.

                  - **hostPath** *(string) --*

                    The path for the device on the host container instance.

                  - **containerPath** *(string) --*

                    The path inside the container at which to expose the host device. By
                    default the ``hostPath`` value is used.

                  - **permissions** *(list) --*

                    The explicit permissions to provide to the container for the device. By
                    default, the container has permissions for ``read`` , ``write`` , and
                    ``mknod`` for the device.

                    - *(string) --*
    """


_DescribeJobDefinitionsPaginateResponseTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponseTypeDef",
    {
        "jobDefinitions": List[
            DescribeJobDefinitionsPaginateResponsejobDefinitionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeJobDefinitionsPaginateResponseTypeDef(
    _DescribeJobDefinitionsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeJobDefinitionsPaginate` `Response`

    - **jobDefinitions** *(list) --*

      The list of job definitions.

      - *(dict) --*

        An object representing an AWS Batch job definition.

        - **jobDefinitionName** *(string) --*

          The name of the job definition.

        - **jobDefinitionArn** *(string) --*

          The Amazon Resource Name (ARN) for the job definition.

        - **revision** *(integer) --*

          The revision of the job definition.

        - **status** *(string) --*

          The status of the job definition.

        - **type** *(string) --*

          The type of job definition.

        - **parameters** *(dict) --*

          Default parameters or parameter substitution placeholders that are set in the job
          definition. Parameters are specified as a key-value pair mapping. Parameters in a
          ``SubmitJob`` request override any corresponding parameter defaults from the job
          definition. For more information about specifying parameters, see `Job Definition
          Parameters
          <https://docs.aws.amazon.com/batch/latest/userguide/job_definition_parameters.html>`__ in
          the *AWS Batch User Guide* .

          - *(string) --*

            - *(string) --*

        - **retryStrategy** *(dict) --*

          The retry strategy to use for failed jobs that are submitted with this job definition.

          - **attempts** *(integer) --*

            The number of times to move a job to the ``RUNNABLE`` status. You may specify between 1
            and 10 attempts. If the value of ``attempts`` is greater than one, the job is retried
            on failure the same number of attempts as the value.

        - **containerProperties** *(dict) --*

          An object with various properties specific to container-based jobs.

          - **image** *(string) --*

            The image used to start a container. This string is passed directly to the Docker
            daemon. Images in the Docker Hub registry are available by default. Other repositories
            are specified with `` *repository-url* /*image* :*tag* `` . Up to 255 letters
            (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward
            slashes, and number signs are allowed. This parameter maps to ``Image`` in the `Create
            a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section
            of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``IMAGE`` parameter of `docker run <https://docs.docker.com/engine/reference/run/>`__ .

            * Images in Amazon ECR repositories use the full registry and repository URI (for
            example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ).

            * Images in official repositories on Docker Hub use a single name (for example,
            ``ubuntu`` or ``mongo`` ).

            * Images in other repositories on Docker Hub are qualified with an organization name
            (for example, ``amazon/amazon-ecs-agent`` ).

            * Images in other online repositories are qualified further by a domain name (for
            example, ``quay.io/assemblyline/ubuntu`` ).

          - **vcpus** *(integer) --*

            The number of vCPUs reserved for the container. This parameter maps to ``CpuShares`` in
            the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``--cpu-shares`` option to `docker run
            <https://docs.docker.com/engine/reference/run/>`__ . Each vCPU is equivalent to 1,024
            CPU shares. You must specify at least one vCPU.

          - **memory** *(integer) --*

            The hard limit (in MiB) of memory to present to the container. If your container
            attempts to exceed the memory specified here, the container is killed. This parameter
            maps to ``Memory`` in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--memory``
            option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . You must
            specify at least 4 MiB of memory for a job.

            .. note::

              If you are trying to maximize your resource utilization by providing your jobs as
              much memory as possible for a particular instance type, see `Memory Management
              <https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`__ in the
              *AWS Batch User Guide* .

          - **command** *(list) --*

            The command that is passed to the container. This parameter maps to ``Cmd`` in the
            `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
            section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and
            the ``COMMAND`` parameter to `docker run
            <https://docs.docker.com/engine/reference/run/>`__ . For more information, see
            `https\\://docs.docker.com/engine/reference/builder/#cmd
            <https://docs.docker.com/engine/reference/builder/#cmd>`__ .

            - *(string) --*

          - **jobRoleArn** *(string) --*

            The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS
            permissions.

          - **volumes** *(list) --*

            A list of data volumes used in a job.

            - *(dict) --*

              A data volume used in a job's container properties.

              - **host** *(dict) --*

                The contents of the ``host`` parameter determine whether your data volume persists
                on the host container instance and where it is stored. If the host parameter is
                empty, then the Docker daemon assigns a host path for your data volume. However,
                the data is not guaranteed to persist after the containers associated with it stop
                running.

                - **sourcePath** *(string) --*

                  The path on the host container instance that is presented to the container. If
                  this parameter is empty, then the Docker daemon has assigned a host path for you.
                  If this parameter contains a file location, then the data volume persists at the
                  specified location on the host container instance until you delete it manually.
                  If the source path location does not exist on the host container instance, the
                  Docker daemon creates it. If the location does exist, the contents of the source
                  path folder are exported.

              - **name** *(string) --*

                The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
                hyphens, and underscores are allowed. This name is referenced in the
                ``sourceVolume`` parameter of container definition ``mountPoints`` .

          - **environment** *(list) --*

            The environment variables to pass to a container. This parameter maps to ``Env`` in the
            `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
            section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and
            the ``--env`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

            .. warning::

              We do not recommend using plaintext environment variables for sensitive information,
              such as credential data.

            .. note::

              Environment variables must not start with ``AWS_BATCH`` ; this naming convention is
              reserved for variables that are set by the AWS Batch service.

            - *(dict) --*

              A key-value pair object.

              - **name** *(string) --*

                The name of the key-value pair. For environment variables, this is the name of the
                environment variable.

              - **value** *(string) --*

                The value of the key-value pair. For environment variables, this is the value of
                the environment variable.

          - **mountPoints** *(list) --*

            The mount points for data volumes in your container. This parameter maps to ``Volumes``
            in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--volume``
            option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

            - *(dict) --*

              Details on a Docker volume mount point that is used in a job's container properties.
              This parameter maps to ``Volumes`` in the `Create a container
              <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
              section of the Docker Remote API and the ``--volume`` option to docker run.

              - **containerPath** *(string) --*

                The path on the container at which to mount the host volume.

              - **readOnly** *(boolean) --*

                If this value is ``true`` , the container has read-only access to the volume;
                otherwise, the container can write to the volume. The default value is ``false`` .

              - **sourceVolume** *(string) --*

                The name of the volume to mount.

          - **readonlyRootFilesystem** *(boolean) --*

            When this parameter is true, the container is given read-only access to its root file
            system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``--read-only`` option to ``docker run`` .

          - **privileged** *(boolean) --*

            When this parameter is true, the container is given elevated privileges on the host
            container instance (similar to the ``root`` user). This parameter maps to
            ``Privileged`` in the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
            ``--privileged`` option to `docker run
            <https://docs.docker.com/engine/reference/run/>`__ .

          - **ulimits** *(list) --*

            A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits`` in
            the `Create a container
            <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
            `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--ulimit``
            option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .

            - *(dict) --*

              The ``ulimit`` settings to pass to the container.

              - **hardLimit** *(integer) --*

                The hard limit for the ``ulimit`` type.

              - **name** *(string) --*

                The ``type`` of the ``ulimit`` .

              - **softLimit** *(integer) --*

                The soft limit for the ``ulimit`` type.

          - **user** *(string) --*

            The user name to use inside the container. This parameter maps to ``User`` in the
            `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__
            section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and
            the ``--user`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__
            .

          - **instanceType** *(string) --*

            The instance type to use for a multi-node parallel job. Currently all node groups in a
            multi-node parallel job must use the same instance type. This parameter is not valid
            for single-node container jobs.

          - **resourceRequirements** *(list) --*

            The type and amount of a resource to assign to a container. Currently, the only
            supported resource is ``GPU`` .

            - *(dict) --*

              The type and amount of a resource to assign to a container. Currently, the only
              supported resource type is ``GPU`` .

              - **value** *(string) --*

                The number of physical GPUs to reserve for the container. The number of GPUs
                reserved for all containers in a job should not exceed the number of available GPUs
                on the compute resource that the job is launched on.

              - **type** *(string) --*

                The type of resource to assign to a container. Currently, the only supported
                resource type is ``GPU`` .

          - **linuxParameters** *(dict) --*

            Linux-specific modifications that are applied to the container, such as details for
            device mappings.

            - **devices** *(list) --*

              Any host devices to expose to the container. This parameter maps to ``Devices`` in
              the `Create a container
              <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
              `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
              ``--device`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__
              .

              - *(dict) --*

                An object representing a container instance host device.

                - **hostPath** *(string) --*

                  The path for the device on the host container instance.

                - **containerPath** *(string) --*

                  The path inside the container at which to expose the host device. By default the
                  ``hostPath`` value is used.

                - **permissions** *(list) --*

                  The explicit permissions to provide to the container for the device. By default,
                  the container has permissions for ``read`` , ``write`` , and ``mknod`` for the
                  device.

                  - *(string) --*

        - **timeout** *(dict) --*

          The timeout configuration for jobs that are submitted with this job definition. You can
          specify a timeout duration after which AWS Batch terminates your jobs if they have not
          finished.

          - **attemptDurationSeconds** *(integer) --*

            The time duration in seconds (measured from the job attempt's ``startedAt`` timestamp)
            after which AWS Batch terminates your jobs if they have not finished.

        - **nodeProperties** *(dict) --*

          An object with various properties specific to multi-node parallel jobs.

          - **numNodes** *(integer) --*

            The number of nodes associated with a multi-node parallel job.

          - **mainNode** *(integer) --*

            Specifies the node index for the main node of a multi-node parallel job. This node
            index value must be fewer than the number of nodes.

          - **nodeRangeProperties** *(list) --*

            A list of node ranges and their properties associated with a multi-node parallel job.

            - *(dict) --*

              An object representing the properties of the node range for a multi-node parallel job.

              - **targetNodes** *(string) --*

                The range of nodes, using node index values. A range of ``0:3`` indicates nodes
                with index values of ``0`` through ``3`` . If the starting range value is omitted
                (``:n`` ), then ``0`` is used to start the range. If the ending range value is
                omitted (``n:`` ), then the highest possible node index is used to end the range.
                Your accumulative node ranges must account for all nodes (0:n). You may nest node
                ranges, for example 0:10 and 4:5, in which case the 4:5 range properties override
                the 0:10 properties.

              - **container** *(dict) --*

                The container details for the node range.

                - **image** *(string) --*

                  The image used to start a container. This string is passed directly to the Docker
                  daemon. Images in the Docker Hub registry are available by default. Other
                  repositories are specified with `` *repository-url* /*image* :*tag* `` . Up to
                  255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons,
                  periods, forward slashes, and number signs are allowed. This parameter maps to
                  ``Image`` in the `Create a container
                  <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
                  `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                  ``IMAGE`` parameter of `docker run
                  <https://docs.docker.com/engine/reference/run/>`__ .

                  * Images in Amazon ECR repositories use the full registry and repository URI (for
                  example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ).

                  * Images in official repositories on Docker Hub use a single name (for example,
                  ``ubuntu`` or ``mongo`` ).

                  * Images in other repositories on Docker Hub are qualified with an organization
                  name (for example, ``amazon/amazon-ecs-agent`` ).

                  * Images in other online repositories are qualified further by a domain name (for
                  example, ``quay.io/assemblyline/ubuntu`` ).

                - **vcpus** *(integer) --*

                  The number of vCPUs reserved for the container. This parameter maps to
                  ``CpuShares`` in the `Create a container
                  <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
                  `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                  ``--cpu-shares`` option to `docker run
                  <https://docs.docker.com/engine/reference/run/>`__ . Each vCPU is equivalent to
                  1,024 CPU shares. You must specify at least one vCPU.

                - **memory** *(integer) --*

                  The hard limit (in MiB) of memory to present to the container. If your container
                  attempts to exceed the memory specified here, the container is killed. This
                  parameter maps to ``Memory`` in the `Create a container
                  <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
                  `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                  ``--memory`` option to `docker run
                  <https://docs.docker.com/engine/reference/run/>`__ . You must specify at least 4
                  MiB of memory for a job.

                  .. note::

                    If you are trying to maximize your resource utilization by providing your jobs
                    as much memory as possible for a particular instance type, see `Memory
                    Management
                    <https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`__
                    in the *AWS Batch User Guide* .

                - **command** *(list) --*

                  The command that is passed to the container. This parameter maps to ``Cmd`` in
                  the `Create a container
                  <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
                  `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                  ``COMMAND`` parameter to `docker run
                  <https://docs.docker.com/engine/reference/run/>`__ . For more information, see
                  `https\\://docs.docker.com/engine/reference/builder/#cmd
                  <https://docs.docker.com/engine/reference/builder/#cmd>`__ .

                  - *(string) --*

                - **jobRoleArn** *(string) --*

                  The Amazon Resource Name (ARN) of the IAM role that the container can assume for
                  AWS permissions.

                - **volumes** *(list) --*

                  A list of data volumes used in a job.

                  - *(dict) --*

                    A data volume used in a job's container properties.

                    - **host** *(dict) --*

                      The contents of the ``host`` parameter determine whether your data volume
                      persists on the host container instance and where it is stored. If the host
                      parameter is empty, then the Docker daemon assigns a host path for your data
                      volume. However, the data is not guaranteed to persist after the containers
                      associated with it stop running.

                      - **sourcePath** *(string) --*

                        The path on the host container instance that is presented to the container.
                        If this parameter is empty, then the Docker daemon has assigned a host path
                        for you. If this parameter contains a file location, then the data volume
                        persists at the specified location on the host container instance until you
                        delete it manually. If the source path location does not exist on the host
                        container instance, the Docker daemon creates it. If the location does
                        exist, the contents of the source path folder are exported.

                    - **name** *(string) --*

                      The name of the volume. Up to 255 letters (uppercase and lowercase), numbers,
                      hyphens, and underscores are allowed. This name is referenced in the
                      ``sourceVolume`` parameter of container definition ``mountPoints`` .

                - **environment** *(list) --*

                  The environment variables to pass to a container. This parameter maps to ``Env``
                  in the `Create a container
                  <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
                  `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                  ``--env`` option to `docker run
                  <https://docs.docker.com/engine/reference/run/>`__ .

                  .. warning::

                    We do not recommend using plaintext environment variables for sensitive
                    information, such as credential data.

                  .. note::

                    Environment variables must not start with ``AWS_BATCH`` ; this naming
                    convention is reserved for variables that are set by the AWS Batch service.

                  - *(dict) --*

                    A key-value pair object.

                    - **name** *(string) --*

                      The name of the key-value pair. For environment variables, this is the name
                      of the environment variable.

                    - **value** *(string) --*

                      The value of the key-value pair. For environment variables, this is the value
                      of the environment variable.

                - **mountPoints** *(list) --*

                  The mount points for data volumes in your container. This parameter maps to
                  ``Volumes`` in the `Create a container
                  <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
                  `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                  ``--volume`` option to `docker run
                  <https://docs.docker.com/engine/reference/run/>`__ .

                  - *(dict) --*

                    Details on a Docker volume mount point that is used in a job's container
                    properties. This parameter maps to ``Volumes`` in the `Create a container
                    <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__
                    section of the Docker Remote API and the ``--volume`` option to docker run.

                    - **containerPath** *(string) --*

                      The path on the container at which to mount the host volume.

                    - **readOnly** *(boolean) --*

                      If this value is ``true`` , the container has read-only access to the volume;
                      otherwise, the container can write to the volume. The default value is
                      ``false`` .

                    - **sourceVolume** *(string) --*

                      The name of the volume to mount.

                - **readonlyRootFilesystem** *(boolean) --*

                  When this parameter is true, the container is given read-only access to its root
                  file system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container
                  <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
                  `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                  ``--read-only`` option to ``docker run`` .

                - **privileged** *(boolean) --*

                  When this parameter is true, the container is given elevated privileges on the
                  host container instance (similar to the ``root`` user). This parameter maps to
                  ``Privileged`` in the `Create a container
                  <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
                  `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                  ``--privileged`` option to `docker run
                  <https://docs.docker.com/engine/reference/run/>`__ .

                - **ulimits** *(list) --*

                  A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits``
                  in the `Create a container
                  <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
                  `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                  ``--ulimit`` option to `docker run
                  <https://docs.docker.com/engine/reference/run/>`__ .

                  - *(dict) --*

                    The ``ulimit`` settings to pass to the container.

                    - **hardLimit** *(integer) --*

                      The hard limit for the ``ulimit`` type.

                    - **name** *(string) --*

                      The ``type`` of the ``ulimit`` .

                    - **softLimit** *(integer) --*

                      The soft limit for the ``ulimit`` type.

                - **user** *(string) --*

                  The user name to use inside the container. This parameter maps to ``User`` in the
                  `Create a container
                  <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the
                  `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                  ``--user`` option to `docker run
                  <https://docs.docker.com/engine/reference/run/>`__ .

                - **instanceType** *(string) --*

                  The instance type to use for a multi-node parallel job. Currently all node groups
                  in a multi-node parallel job must use the same instance type. This parameter is
                  not valid for single-node container jobs.

                - **resourceRequirements** *(list) --*

                  The type and amount of a resource to assign to a container. Currently, the only
                  supported resource is ``GPU`` .

                  - *(dict) --*

                    The type and amount of a resource to assign to a container. Currently, the only
                    supported resource type is ``GPU`` .

                    - **value** *(string) --*

                      The number of physical GPUs to reserve for the container. The number of GPUs
                      reserved for all containers in a job should not exceed the number of
                      available GPUs on the compute resource that the job is launched on.

                    - **type** *(string) --*

                      The type of resource to assign to a container. Currently, the only supported
                      resource type is ``GPU`` .

                - **linuxParameters** *(dict) --*

                  Linux-specific modifications that are applied to the container, such as details
                  for device mappings.

                  - **devices** *(list) --*

                    Any host devices to expose to the container. This parameter maps to ``Devices``
                    in the `Create a container
                    <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of
                    the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the
                    ``--device`` option to `docker run
                    <https://docs.docker.com/engine/reference/run/>`__ .

                    - *(dict) --*

                      An object representing a container instance host device.

                      - **hostPath** *(string) --*

                        The path for the device on the host container instance.

                      - **containerPath** *(string) --*

                        The path inside the container at which to expose the host device. By
                        default the ``hostPath`` value is used.

                      - **permissions** *(list) --*

                        The explicit permissions to provide to the container for the device. By
                        default, the container has permissions for ``read`` , ``write`` , and
                        ``mknod`` for the device.

                        - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeJobQueuesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeJobQueuesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeJobQueuesPaginatePaginationConfigTypeDef(
    _DescribeJobQueuesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeJobQueuesPaginate` `PaginationConfig`

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


_DescribeJobQueuesPaginateResponsejobQueuescomputeEnvironmentOrderTypeDef = TypedDict(
    "_DescribeJobQueuesPaginateResponsejobQueuescomputeEnvironmentOrderTypeDef",
    {"order": int, "computeEnvironment": str},
    total=False,
)


class DescribeJobQueuesPaginateResponsejobQueuescomputeEnvironmentOrderTypeDef(
    _DescribeJobQueuesPaginateResponsejobQueuescomputeEnvironmentOrderTypeDef
):
    """
    Type definition for `DescribeJobQueuesPaginateResponsejobQueues` `computeEnvironmentOrder`

    The order in which compute environments are tried for job placement within a queue.
    Compute environments are tried in ascending order. For example, if two compute
    environments are associated with a job queue, the compute environment with a lower
    order integer value is tried for job placement first.

    - **order** *(integer) --*

      The order of the compute environment.

    - **computeEnvironment** *(string) --*

      The Amazon Resource Name (ARN) of the compute environment.
    """


_DescribeJobQueuesPaginateResponsejobQueuesTypeDef = TypedDict(
    "_DescribeJobQueuesPaginateResponsejobQueuesTypeDef",
    {
        "jobQueueName": str,
        "jobQueueArn": str,
        "state": str,
        "status": str,
        "statusReason": str,
        "priority": int,
        "computeEnvironmentOrder": List[
            DescribeJobQueuesPaginateResponsejobQueuescomputeEnvironmentOrderTypeDef
        ],
    },
    total=False,
)


class DescribeJobQueuesPaginateResponsejobQueuesTypeDef(
    _DescribeJobQueuesPaginateResponsejobQueuesTypeDef
):
    """
    Type definition for `DescribeJobQueuesPaginateResponse` `jobQueues`

    An object representing the details of an AWS Batch job queue.

    - **jobQueueName** *(string) --*

      The name of the job queue.

    - **jobQueueArn** *(string) --*

      The Amazon Resource Name (ARN) of the job queue.

    - **state** *(string) --*

      Describes the ability of the queue to accept new jobs.

    - **status** *(string) --*

      The status of the job queue (for example, ``CREATING`` or ``VALID`` ).

    - **statusReason** *(string) --*

      A short, human-readable string to provide additional details about the current status of
      the job queue.

    - **priority** *(integer) --*

      The priority of the job queue.

    - **computeEnvironmentOrder** *(list) --*

      The compute environments that are attached to the job queue and the order in which job
      placement is preferred. Compute environments are selected for job placement in ascending
      order.

      - *(dict) --*

        The order in which compute environments are tried for job placement within a queue.
        Compute environments are tried in ascending order. For example, if two compute
        environments are associated with a job queue, the compute environment with a lower
        order integer value is tried for job placement first.

        - **order** *(integer) --*

          The order of the compute environment.

        - **computeEnvironment** *(string) --*

          The Amazon Resource Name (ARN) of the compute environment.
    """


_DescribeJobQueuesPaginateResponseTypeDef = TypedDict(
    "_DescribeJobQueuesPaginateResponseTypeDef",
    {
        "jobQueues": List[DescribeJobQueuesPaginateResponsejobQueuesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeJobQueuesPaginateResponseTypeDef(
    _DescribeJobQueuesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeJobQueuesPaginate` `Response`

    - **jobQueues** *(list) --*

      The list of job queues.

      - *(dict) --*

        An object representing the details of an AWS Batch job queue.

        - **jobQueueName** *(string) --*

          The name of the job queue.

        - **jobQueueArn** *(string) --*

          The Amazon Resource Name (ARN) of the job queue.

        - **state** *(string) --*

          Describes the ability of the queue to accept new jobs.

        - **status** *(string) --*

          The status of the job queue (for example, ``CREATING`` or ``VALID`` ).

        - **statusReason** *(string) --*

          A short, human-readable string to provide additional details about the current status of
          the job queue.

        - **priority** *(integer) --*

          The priority of the job queue.

        - **computeEnvironmentOrder** *(list) --*

          The compute environments that are attached to the job queue and the order in which job
          placement is preferred. Compute environments are selected for job placement in ascending
          order.

          - *(dict) --*

            The order in which compute environments are tried for job placement within a queue.
            Compute environments are tried in ascending order. For example, if two compute
            environments are associated with a job queue, the compute environment with a lower
            order integer value is tried for job placement first.

            - **order** *(integer) --*

              The order of the compute environment.

            - **computeEnvironment** *(string) --*

              The Amazon Resource Name (ARN) of the compute environment.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListJobsPaginatePaginationConfigTypeDef(_ListJobsPaginatePaginationConfigTypeDef):
    """
    Type definition for `ListJobsPaginate` `PaginationConfig`

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


_ListJobsPaginateResponsejobSummaryListarrayPropertiesTypeDef = TypedDict(
    "_ListJobsPaginateResponsejobSummaryListarrayPropertiesTypeDef",
    {"size": int, "index": int},
    total=False,
)


class ListJobsPaginateResponsejobSummaryListarrayPropertiesTypeDef(
    _ListJobsPaginateResponsejobSummaryListarrayPropertiesTypeDef
):
    """
    Type definition for `ListJobsPaginateResponsejobSummaryList` `arrayProperties`

    The array properties of the job, if it is an array job.

    - **size** *(integer) --*

      The size of the array job. This parameter is returned for parent array jobs.

    - **index** *(integer) --*

      The job index within the array that is associated with this job. This parameter is
      returned for children of array jobs.
    """


_ListJobsPaginateResponsejobSummaryListcontainerTypeDef = TypedDict(
    "_ListJobsPaginateResponsejobSummaryListcontainerTypeDef",
    {"exitCode": int, "reason": str},
    total=False,
)


class ListJobsPaginateResponsejobSummaryListcontainerTypeDef(
    _ListJobsPaginateResponsejobSummaryListcontainerTypeDef
):
    """
    Type definition for `ListJobsPaginateResponsejobSummaryList` `container`

    An object representing the details of the container that is associated with the job.

    - **exitCode** *(integer) --*

      The exit code to return upon completion.

    - **reason** *(string) --*

      A short (255 max characters) human-readable string to provide additional details about
      a running or stopped container.
    """


_ListJobsPaginateResponsejobSummaryListnodePropertiesTypeDef = TypedDict(
    "_ListJobsPaginateResponsejobSummaryListnodePropertiesTypeDef",
    {"isMainNode": bool, "numNodes": int, "nodeIndex": int},
    total=False,
)


class ListJobsPaginateResponsejobSummaryListnodePropertiesTypeDef(
    _ListJobsPaginateResponsejobSummaryListnodePropertiesTypeDef
):
    """
    Type definition for `ListJobsPaginateResponsejobSummaryList` `nodeProperties`

    The node properties for a single node in a job summary list.

    - **isMainNode** *(boolean) --*

      Specifies whether the current node is the main node for a multi-node parallel job.

    - **numNodes** *(integer) --*

      The number of nodes associated with a multi-node parallel job.

    - **nodeIndex** *(integer) --*

      The node index for the node. Node index numbering begins at zero. This index is also
      available on the node with the ``AWS_BATCH_JOB_NODE_INDEX`` environment variable.
    """


_ListJobsPaginateResponsejobSummaryListTypeDef = TypedDict(
    "_ListJobsPaginateResponsejobSummaryListTypeDef",
    {
        "jobId": str,
        "jobName": str,
        "createdAt": int,
        "status": str,
        "statusReason": str,
        "startedAt": int,
        "stoppedAt": int,
        "container": ListJobsPaginateResponsejobSummaryListcontainerTypeDef,
        "arrayProperties": ListJobsPaginateResponsejobSummaryListarrayPropertiesTypeDef,
        "nodeProperties": ListJobsPaginateResponsejobSummaryListnodePropertiesTypeDef,
    },
    total=False,
)


class ListJobsPaginateResponsejobSummaryListTypeDef(
    _ListJobsPaginateResponsejobSummaryListTypeDef
):
    """
    Type definition for `ListJobsPaginateResponse` `jobSummaryList`

    An object representing summary details of a job.

    - **jobId** *(string) --*

      The ID of the job.

    - **jobName** *(string) --*

      The name of the job.

    - **createdAt** *(integer) --*

      The Unix timestamp for when the job was created. For non-array jobs and parent array
      jobs, this is when the job entered the ``SUBMITTED`` state (at the time  SubmitJob was
      called). For array child jobs, this is when the child job was spawned by its parent and
      entered the ``PENDING`` state.

    - **status** *(string) --*

      The current status for the job.

    - **statusReason** *(string) --*

      A short, human-readable string to provide additional details about the current status of
      the job.

    - **startedAt** *(integer) --*

      The Unix timestamp for when the job was started (when the job transitioned from the
      ``STARTING`` state to the ``RUNNING`` state).

    - **stoppedAt** *(integer) --*

      The Unix timestamp for when the job was stopped (when the job transitioned from the
      ``RUNNING`` state to a terminal state, such as ``SUCCEEDED`` or ``FAILED`` ).

    - **container** *(dict) --*

      An object representing the details of the container that is associated with the job.

      - **exitCode** *(integer) --*

        The exit code to return upon completion.

      - **reason** *(string) --*

        A short (255 max characters) human-readable string to provide additional details about
        a running or stopped container.

    - **arrayProperties** *(dict) --*

      The array properties of the job, if it is an array job.

      - **size** *(integer) --*

        The size of the array job. This parameter is returned for parent array jobs.

      - **index** *(integer) --*

        The job index within the array that is associated with this job. This parameter is
        returned for children of array jobs.

    - **nodeProperties** *(dict) --*

      The node properties for a single node in a job summary list.

      - **isMainNode** *(boolean) --*

        Specifies whether the current node is the main node for a multi-node parallel job.

      - **numNodes** *(integer) --*

        The number of nodes associated with a multi-node parallel job.

      - **nodeIndex** *(integer) --*

        The node index for the node. Node index numbering begins at zero. This index is also
        available on the node with the ``AWS_BATCH_JOB_NODE_INDEX`` environment variable.
    """


_ListJobsPaginateResponseTypeDef = TypedDict(
    "_ListJobsPaginateResponseTypeDef",
    {
        "jobSummaryList": List[ListJobsPaginateResponsejobSummaryListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListJobsPaginateResponseTypeDef(_ListJobsPaginateResponseTypeDef):
    """
    Type definition for `ListJobsPaginate` `Response`

    - **jobSummaryList** *(list) --*

      A list of job summaries that match the request.

      - *(dict) --*

        An object representing summary details of a job.

        - **jobId** *(string) --*

          The ID of the job.

        - **jobName** *(string) --*

          The name of the job.

        - **createdAt** *(integer) --*

          The Unix timestamp for when the job was created. For non-array jobs and parent array
          jobs, this is when the job entered the ``SUBMITTED`` state (at the time  SubmitJob was
          called). For array child jobs, this is when the child job was spawned by its parent and
          entered the ``PENDING`` state.

        - **status** *(string) --*

          The current status for the job.

        - **statusReason** *(string) --*

          A short, human-readable string to provide additional details about the current status of
          the job.

        - **startedAt** *(integer) --*

          The Unix timestamp for when the job was started (when the job transitioned from the
          ``STARTING`` state to the ``RUNNING`` state).

        - **stoppedAt** *(integer) --*

          The Unix timestamp for when the job was stopped (when the job transitioned from the
          ``RUNNING`` state to a terminal state, such as ``SUCCEEDED`` or ``FAILED`` ).

        - **container** *(dict) --*

          An object representing the details of the container that is associated with the job.

          - **exitCode** *(integer) --*

            The exit code to return upon completion.

          - **reason** *(string) --*

            A short (255 max characters) human-readable string to provide additional details about
            a running or stopped container.

        - **arrayProperties** *(dict) --*

          The array properties of the job, if it is an array job.

          - **size** *(integer) --*

            The size of the array job. This parameter is returned for parent array jobs.

          - **index** *(integer) --*

            The job index within the array that is associated with this job. This parameter is
            returned for children of array jobs.

        - **nodeProperties** *(dict) --*

          The node properties for a single node in a job summary list.

          - **isMainNode** *(boolean) --*

            Specifies whether the current node is the main node for a multi-node parallel job.

          - **numNodes** *(integer) --*

            The number of nodes associated with a multi-node parallel job.

          - **nodeIndex** *(integer) --*

            The node index for the node. Node index numbering begins at zero. This index is also
            available on the node with the ``AWS_BATCH_JOB_NODE_INDEX`` environment variable.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """
