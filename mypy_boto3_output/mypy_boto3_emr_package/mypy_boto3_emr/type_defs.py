"Main interface for emr type defs"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsConfigurationsTypeDef",
    "ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef",
    "ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef",
    "ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationTypeDef",
    "ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsTypeDef",
    "ClientAddInstanceFleetInstanceFleetLaunchSpecificationsSpotSpecificationTypeDef",
    "ClientAddInstanceFleetInstanceFleetLaunchSpecificationsTypeDef",
    "ClientAddInstanceFleetInstanceFleetTypeDef",
    "ClientAddInstanceFleetResponseTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyConstraintsTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsConfigurationsTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsEbsConfigurationTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsTypeDef",
    "ClientAddInstanceGroupsResponseTypeDef",
    "ClientAddJobFlowStepsResponseTypeDef",
    "ClientAddJobFlowStepsStepsHadoopJarStepPropertiesTypeDef",
    "ClientAddJobFlowStepsStepsHadoopJarStepTypeDef",
    "ClientAddJobFlowStepsStepsTypeDef",
    "ClientAddTagsTagsTypeDef",
    "ClientCancelStepsResponseCancelStepsInfoListTypeDef",
    "ClientCancelStepsResponseTypeDef",
    "ClientCreateSecurityConfigurationResponseTypeDef",
    "ClientDescribeClusterResponseClusterApplicationsTypeDef",
    "ClientDescribeClusterResponseClusterConfigurationsTypeDef",
    "ClientDescribeClusterResponseClusterEc2InstanceAttributesTypeDef",
    "ClientDescribeClusterResponseClusterKerberosAttributesTypeDef",
    "ClientDescribeClusterResponseClusterStatusStateChangeReasonTypeDef",
    "ClientDescribeClusterResponseClusterStatusTimelineTypeDef",
    "ClientDescribeClusterResponseClusterStatusTypeDef",
    "ClientDescribeClusterResponseClusterTagsTypeDef",
    "ClientDescribeClusterResponseClusterTypeDef",
    "ClientDescribeClusterResponseTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsBootstrapActionConfigScriptBootstrapActionTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsBootstrapActionConfigTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsExecutionStatusDetailTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsInstancesInstanceGroupsTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsInstancesPlacementTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsInstancesTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsStepsExecutionStatusDetailTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigHadoopJarStepPropertiesTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigHadoopJarStepTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsStepsTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsTypeDef",
    "ClientDescribeJobFlowsResponseTypeDef",
    "ClientDescribeSecurityConfigurationResponseTypeDef",
    "ClientDescribeStepResponseStepConfigTypeDef",
    "ClientDescribeStepResponseStepStatusFailureDetailsTypeDef",
    "ClientDescribeStepResponseStepStatusStateChangeReasonTypeDef",
    "ClientDescribeStepResponseStepStatusTimelineTypeDef",
    "ClientDescribeStepResponseStepStatusTypeDef",
    "ClientDescribeStepResponseStepTypeDef",
    "ClientDescribeStepResponseTypeDef",
    "ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationMetadataTypeDef",
    "ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef",
    "ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationTypeDef",
    "ClientGetBlockPublicAccessConfigurationResponseTypeDef",
    "ClientListBootstrapActionsResponseBootstrapActionsTypeDef",
    "ClientListBootstrapActionsResponseTypeDef",
    "ClientListClustersResponseClustersStatusStateChangeReasonTypeDef",
    "ClientListClustersResponseClustersStatusTimelineTypeDef",
    "ClientListClustersResponseClustersStatusTypeDef",
    "ClientListClustersResponseClustersTypeDef",
    "ClientListClustersResponseTypeDef",
    "ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsConfigurationsTypeDef",
    "ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesVolumeSpecificationTypeDef",
    "ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesTypeDef",
    "ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsTypeDef",
    "ClientListInstanceFleetsResponseInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef",
    "ClientListInstanceFleetsResponseInstanceFleetsLaunchSpecificationsTypeDef",
    "ClientListInstanceFleetsResponseInstanceFleetsStatusStateChangeReasonTypeDef",
    "ClientListInstanceFleetsResponseInstanceFleetsStatusTimelineTypeDef",
    "ClientListInstanceFleetsResponseInstanceFleetsStatusTypeDef",
    "ClientListInstanceFleetsResponseInstanceFleetsTypeDef",
    "ClientListInstanceFleetsResponseTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyConstraintsTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesActionTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyStatusStateChangeReasonTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyStatusTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsConfigurationsTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsEbsBlockDevicesVolumeSpecificationTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsEbsBlockDevicesTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsLastSuccessfullyAppliedConfigurationsTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsShrinkPolicyTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsStatusStateChangeReasonTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsStatusTimelineTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsStatusTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsTypeDef",
    "ClientListInstanceGroupsResponseTypeDef",
    "ClientListInstancesResponseInstancesEbsVolumesTypeDef",
    "ClientListInstancesResponseInstancesStatusStateChangeReasonTypeDef",
    "ClientListInstancesResponseInstancesStatusTimelineTypeDef",
    "ClientListInstancesResponseInstancesStatusTypeDef",
    "ClientListInstancesResponseInstancesTypeDef",
    "ClientListInstancesResponseTypeDef",
    "ClientListSecurityConfigurationsResponseSecurityConfigurationsTypeDef",
    "ClientListSecurityConfigurationsResponseTypeDef",
    "ClientListStepsResponseStepsConfigTypeDef",
    "ClientListStepsResponseStepsStatusFailureDetailsTypeDef",
    "ClientListStepsResponseStepsStatusStateChangeReasonTypeDef",
    "ClientListStepsResponseStepsStatusTimelineTypeDef",
    "ClientListStepsResponseStepsStatusTypeDef",
    "ClientListStepsResponseStepsTypeDef",
    "ClientListStepsResponseTypeDef",
    "ClientModifyInstanceFleetInstanceFleetTypeDef",
    "ClientModifyInstanceGroupsInstanceGroupsConfigurationsTypeDef",
    "ClientModifyInstanceGroupsInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef",
    "ClientModifyInstanceGroupsInstanceGroupsShrinkPolicyTypeDef",
    "ClientModifyInstanceGroupsInstanceGroupsTypeDef",
    "ClientPutAutoScalingPolicyAutoScalingPolicyConstraintsTypeDef",
    "ClientPutAutoScalingPolicyAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    "ClientPutAutoScalingPolicyAutoScalingPolicyRulesActionTypeDef",
    "ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    "ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    "ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerTypeDef",
    "ClientPutAutoScalingPolicyAutoScalingPolicyRulesTypeDef",
    "ClientPutAutoScalingPolicyAutoScalingPolicyTypeDef",
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyConstraintsTypeDef",
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesActionTypeDef",
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerTypeDef",
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTypeDef",
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyStatusStateChangeReasonTypeDef",
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyStatusTypeDef",
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyTypeDef",
    "ClientPutAutoScalingPolicyResponseTypeDef",
    "ClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef",
    "ClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationTypeDef",
    "ClientRunJobFlowApplicationsTypeDef",
    "ClientRunJobFlowBootstrapActionsScriptBootstrapActionTypeDef",
    "ClientRunJobFlowBootstrapActionsTypeDef",
    "ClientRunJobFlowConfigurationsTypeDef",
    "ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsConfigurationsTypeDef",
    "ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef",
    "ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef",
    "ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationTypeDef",
    "ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsTypeDef",
    "ClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef",
    "ClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsTypeDef",
    "ClientRunJobFlowInstancesInstanceFleetsTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyConstraintsTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsConfigurationsTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsTypeDef",
    "ClientRunJobFlowInstancesPlacementTypeDef",
    "ClientRunJobFlowInstancesTypeDef",
    "ClientRunJobFlowKerberosAttributesTypeDef",
    "ClientRunJobFlowNewSupportedProductsTypeDef",
    "ClientRunJobFlowResponseTypeDef",
    "ClientRunJobFlowStepsHadoopJarStepPropertiesTypeDef",
    "ClientRunJobFlowStepsHadoopJarStepTypeDef",
    "ClientRunJobFlowStepsTypeDef",
    "ClientRunJobFlowTagsTypeDef",
    "ClusterRunningWaitWaiterConfigTypeDef",
    "ClusterTerminatedWaitWaiterConfigTypeDef",
    "ListBootstrapActionsPaginatePaginationConfigTypeDef",
    "ListBootstrapActionsPaginateResponseBootstrapActionsTypeDef",
    "ListBootstrapActionsPaginateResponseTypeDef",
    "ListClustersPaginatePaginationConfigTypeDef",
    "ListClustersPaginateResponseClustersStatusStateChangeReasonTypeDef",
    "ListClustersPaginateResponseClustersStatusTimelineTypeDef",
    "ListClustersPaginateResponseClustersStatusTypeDef",
    "ListClustersPaginateResponseClustersTypeDef",
    "ListClustersPaginateResponseTypeDef",
    "ListInstanceFleetsPaginatePaginationConfigTypeDef",
    "ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsConfigurationsTypeDef",
    "ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesVolumeSpecificationTypeDef",
    "ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesTypeDef",
    "ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsTypeDef",
    "ListInstanceFleetsPaginateResponseInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef",
    "ListInstanceFleetsPaginateResponseInstanceFleetsLaunchSpecificationsTypeDef",
    "ListInstanceFleetsPaginateResponseInstanceFleetsStatusStateChangeReasonTypeDef",
    "ListInstanceFleetsPaginateResponseInstanceFleetsStatusTimelineTypeDef",
    "ListInstanceFleetsPaginateResponseInstanceFleetsStatusTypeDef",
    "ListInstanceFleetsPaginateResponseInstanceFleetsTypeDef",
    "ListInstanceFleetsPaginateResponseTypeDef",
    "ListInstanceGroupsPaginatePaginationConfigTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyConstraintsTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesActionTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyStatusStateChangeReasonTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyStatusTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsConfigurationsTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsEbsBlockDevicesVolumeSpecificationTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsEbsBlockDevicesTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsLastSuccessfullyAppliedConfigurationsTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsShrinkPolicyTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsStatusStateChangeReasonTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsStatusTimelineTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsStatusTypeDef",
    "ListInstanceGroupsPaginateResponseInstanceGroupsTypeDef",
    "ListInstanceGroupsPaginateResponseTypeDef",
    "ListInstancesPaginatePaginationConfigTypeDef",
    "ListInstancesPaginateResponseInstancesEbsVolumesTypeDef",
    "ListInstancesPaginateResponseInstancesStatusStateChangeReasonTypeDef",
    "ListInstancesPaginateResponseInstancesStatusTimelineTypeDef",
    "ListInstancesPaginateResponseInstancesStatusTypeDef",
    "ListInstancesPaginateResponseInstancesTypeDef",
    "ListInstancesPaginateResponseTypeDef",
    "ListSecurityConfigurationsPaginatePaginationConfigTypeDef",
    "ListSecurityConfigurationsPaginateResponseSecurityConfigurationsTypeDef",
    "ListSecurityConfigurationsPaginateResponseTypeDef",
    "ListStepsPaginatePaginationConfigTypeDef",
    "ListStepsPaginateResponseStepsConfigTypeDef",
    "ListStepsPaginateResponseStepsStatusFailureDetailsTypeDef",
    "ListStepsPaginateResponseStepsStatusStateChangeReasonTypeDef",
    "ListStepsPaginateResponseStepsStatusTimelineTypeDef",
    "ListStepsPaginateResponseStepsStatusTypeDef",
    "ListStepsPaginateResponseStepsTypeDef",
    "ListStepsPaginateResponseTypeDef",
    "StepCompleteWaitWaiterConfigTypeDef",
)


_ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsConfigurationsTypeDef = TypedDict(
    "_ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsConfigurationsTypeDef",
    {"Classification": str, "Configurations": List[Any], "Properties": Dict[str, str]},
    total=False,
)


class ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsConfigurationsTypeDef(
    _ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsConfigurationsTypeDef
):
    """
    Type definition for `ClientAddInstanceFleetInstanceFleetInstanceTypeConfigs` `Configurations`

    .. note::

      Amazon EMR releases 4.x or later.

    An optional configuration specification to be used when provisioning cluster instances,
    which can include configurations for applications and software bundled with Amazon EMR. A
    configuration consists of a classification, properties, and optional nested
    configurations. A classification refers to an application-specific configuration file.
    Properties are the settings you want to change in that file. For more information, see
    `Configuring Applications
    <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

    - **Classification** *(string) --*

      The classification within a configuration.

    - **Configurations** *(list) --*

      A list of additional configurations to apply within a configuration object.

    - **Properties** *(dict) --*

      A set of properties specified within a configuration classification.

      - *(string) --*

        - *(string) --*
    """


_RequiredClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef = TypedDict(
    "_RequiredClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef",
    {"VolumeType": str, "SizeInGB": int},
)
_OptionalClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef = TypedDict(
    "_OptionalClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef",
    {"Iops": int},
    total=False,
)


class ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef(
    _RequiredClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef,
    _OptionalClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef,
):
    """
    Type definition for `ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigs` `VolumeSpecification`

    EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
    requested for the EBS volume attached to an EC2 instance in the cluster.

    - **VolumeType** *(string) --* **[REQUIRED]**

      The volume type. Volume types supported are gp2, io1, standard.

    - **Iops** *(integer) --*

      The number of I/O operations per second (IOPS) that the volume supports.

    - **SizeInGB** *(integer) --* **[REQUIRED]**

      The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
      volume type is EBS-optimized, the minimum value is 10.
    """


_RequiredClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef = TypedDict(
    "_RequiredClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef",
    {
        "VolumeSpecification": ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef
    },
)
_OptionalClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef = TypedDict(
    "_OptionalClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef",
    {"VolumesPerInstance": int},
    total=False,
)


class ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef(
    _RequiredClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef,
    _OptionalClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef,
):
    """
    Type definition for `ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfiguration` `EbsBlockDeviceConfigs`

    Configuration of requested EBS block device associated with the instance group with
    count of volumes that will be associated to every instance.

    - **VolumeSpecification** *(dict) --* **[REQUIRED]**

      EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
      requested for the EBS volume attached to an EC2 instance in the cluster.

      - **VolumeType** *(string) --* **[REQUIRED]**

        The volume type. Volume types supported are gp2, io1, standard.

      - **Iops** *(integer) --*

        The number of I/O operations per second (IOPS) that the volume supports.

      - **SizeInGB** *(integer) --* **[REQUIRED]**

        The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
        volume type is EBS-optimized, the minimum value is 10.

    - **VolumesPerInstance** *(integer) --*

      Number of EBS volumes with a specific volume configuration that will be associated
      with every instance in the instance group
    """


_ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationTypeDef = TypedDict(
    "_ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationTypeDef",
    {
        "EbsBlockDeviceConfigs": List[
            ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef
        ],
        "EbsOptimized": bool,
    },
    total=False,
)


class ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationTypeDef(
    _ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationTypeDef
):
    """
    Type definition for `ClientAddInstanceFleetInstanceFleetInstanceTypeConfigs` `EbsConfiguration`

    The configuration of Amazon Elastic Block Storage (EBS) attached to each instance as
    defined by ``InstanceType`` .

    - **EbsBlockDeviceConfigs** *(list) --*

      An array of Amazon EBS volume specifications attached to a cluster instance.

      - *(dict) --*

        Configuration of requested EBS block device associated with the instance group with
        count of volumes that will be associated to every instance.

        - **VolumeSpecification** *(dict) --* **[REQUIRED]**

          EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
          requested for the EBS volume attached to an EC2 instance in the cluster.

          - **VolumeType** *(string) --* **[REQUIRED]**

            The volume type. Volume types supported are gp2, io1, standard.

          - **Iops** *(integer) --*

            The number of I/O operations per second (IOPS) that the volume supports.

          - **SizeInGB** *(integer) --* **[REQUIRED]**

            The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
            volume type is EBS-optimized, the minimum value is 10.

        - **VolumesPerInstance** *(integer) --*

          Number of EBS volumes with a specific volume configuration that will be associated
          with every instance in the instance group

    - **EbsOptimized** *(boolean) --*

      Indicates whether an Amazon EBS volume is EBS-optimized.
    """


_RequiredClientAddInstanceFleetInstanceFleetInstanceTypeConfigsTypeDef = TypedDict(
    "_RequiredClientAddInstanceFleetInstanceFleetInstanceTypeConfigsTypeDef",
    {"InstanceType": str},
)
_OptionalClientAddInstanceFleetInstanceFleetInstanceTypeConfigsTypeDef = TypedDict(
    "_OptionalClientAddInstanceFleetInstanceFleetInstanceTypeConfigsTypeDef",
    {
        "WeightedCapacity": int,
        "BidPrice": str,
        "BidPriceAsPercentageOfOnDemandPrice": float,
        "EbsConfiguration": ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationTypeDef,
        "Configurations": List[
            ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsConfigurationsTypeDef
        ],
    },
    total=False,
)


class ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsTypeDef(
    _RequiredClientAddInstanceFleetInstanceFleetInstanceTypeConfigsTypeDef,
    _OptionalClientAddInstanceFleetInstanceFleetInstanceTypeConfigsTypeDef,
):
    """
    Type definition for `ClientAddInstanceFleetInstanceFleet` `InstanceTypeConfigs`

    An instance type configuration for each instance type in an instance fleet, which determines
    the EC2 instances Amazon EMR attempts to provision to fulfill On-Demand and Spot target
    capacities. There can be a maximum of 5 instance type configurations in a fleet.

    .. note::

      The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later,
      excluding 5.0.x versions.

    - **InstanceType** *(string) --* **[REQUIRED]**

      An EC2 instance type, such as ``m3.xlarge`` .

    - **WeightedCapacity** *(integer) --*

      The number of units that a provisioned instance of this type provides toward fulfilling the
      target capacities defined in  InstanceFleetConfig . This value is 1 for a master instance
      fleet, and must be 1 or greater for core and task instance fleets. Defaults to 1 if not
      specified.

    - **BidPrice** *(string) --*

      The bid price for each EC2 Spot instance type as defined by ``InstanceType`` . Expressed in
      USD. If neither ``BidPrice`` nor ``BidPriceAsPercentageOfOnDemandPrice`` is provided,
      ``BidPriceAsPercentageOfOnDemandPrice`` defaults to 100%.

    - **BidPriceAsPercentageOfOnDemandPrice** *(float) --*

      The bid price, as a percentage of On-Demand price, for each EC2 Spot instance as defined by
      ``InstanceType`` . Expressed as a number (for example, 20 specifies 20%). If neither
      ``BidPrice`` nor ``BidPriceAsPercentageOfOnDemandPrice`` is provided,
      ``BidPriceAsPercentageOfOnDemandPrice`` defaults to 100%.

    - **EbsConfiguration** *(dict) --*

      The configuration of Amazon Elastic Block Storage (EBS) attached to each instance as
      defined by ``InstanceType`` .

      - **EbsBlockDeviceConfigs** *(list) --*

        An array of Amazon EBS volume specifications attached to a cluster instance.

        - *(dict) --*

          Configuration of requested EBS block device associated with the instance group with
          count of volumes that will be associated to every instance.

          - **VolumeSpecification** *(dict) --* **[REQUIRED]**

            EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
            requested for the EBS volume attached to an EC2 instance in the cluster.

            - **VolumeType** *(string) --* **[REQUIRED]**

              The volume type. Volume types supported are gp2, io1, standard.

            - **Iops** *(integer) --*

              The number of I/O operations per second (IOPS) that the volume supports.

            - **SizeInGB** *(integer) --* **[REQUIRED]**

              The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
              volume type is EBS-optimized, the minimum value is 10.

          - **VolumesPerInstance** *(integer) --*

            Number of EBS volumes with a specific volume configuration that will be associated
            with every instance in the instance group

      - **EbsOptimized** *(boolean) --*

        Indicates whether an Amazon EBS volume is EBS-optimized.

    - **Configurations** *(list) --*

      A configuration classification that applies when provisioning cluster instances, which can
      include configurations for applications and software that run on the cluster.

      - *(dict) --*

        .. note::

          Amazon EMR releases 4.x or later.

        An optional configuration specification to be used when provisioning cluster instances,
        which can include configurations for applications and software bundled with Amazon EMR. A
        configuration consists of a classification, properties, and optional nested
        configurations. A classification refers to an application-specific configuration file.
        Properties are the settings you want to change in that file. For more information, see
        `Configuring Applications
        <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

        - **Classification** *(string) --*

          The classification within a configuration.

        - **Configurations** *(list) --*

          A list of additional configurations to apply within a configuration object.

        - **Properties** *(dict) --*

          A set of properties specified within a configuration classification.

          - *(string) --*

            - *(string) --*
    """


_RequiredClientAddInstanceFleetInstanceFleetLaunchSpecificationsSpotSpecificationTypeDef = TypedDict(
    "_RequiredClientAddInstanceFleetInstanceFleetLaunchSpecificationsSpotSpecificationTypeDef",
    {"TimeoutDurationMinutes": int, "TimeoutAction": str},
)
_OptionalClientAddInstanceFleetInstanceFleetLaunchSpecificationsSpotSpecificationTypeDef = TypedDict(
    "_OptionalClientAddInstanceFleetInstanceFleetLaunchSpecificationsSpotSpecificationTypeDef",
    {"BlockDurationMinutes": int},
    total=False,
)


class ClientAddInstanceFleetInstanceFleetLaunchSpecificationsSpotSpecificationTypeDef(
    _RequiredClientAddInstanceFleetInstanceFleetLaunchSpecificationsSpotSpecificationTypeDef,
    _OptionalClientAddInstanceFleetInstanceFleetLaunchSpecificationsSpotSpecificationTypeDef,
):
    """
    Type definition for `ClientAddInstanceFleetInstanceFleetLaunchSpecifications` `SpotSpecification`

    The launch specification for Spot instances in the fleet, which determines the defined
    duration and provisioning timeout behavior.

    - **TimeoutDurationMinutes** *(integer) --* **[REQUIRED]**

      The spot provisioning timeout period in minutes. If Spot instances are not provisioned
      within this time period, the ``TimeOutAction`` is taken. Minimum value is 5 and maximum
      value is 1440. The timeout applies only during initial provisioning, when the cluster is
      first created.

    - **TimeoutAction** *(string) --* **[REQUIRED]**

      The action to take when ``TargetSpotCapacity`` has not been fulfilled when the
      ``TimeoutDurationMinutes`` has expired; that is, when all Spot instances could not be
      provisioned within the Spot provisioning timeout. Valid values are ``TERMINATE_CLUSTER``
      and ``SWITCH_TO_ON_DEMAND`` . SWITCH_TO_ON_DEMAND specifies that if no Spot instances are
      available, On-Demand Instances should be provisioned to fulfill any remaining Spot capacity.

    - **BlockDurationMinutes** *(integer) --*

      The defined duration for Spot instances (also known as Spot blocks) in minutes. When
      specified, the Spot instance does not terminate before the defined duration expires, and
      defined duration pricing for Spot instances applies. Valid values are 60, 120, 180, 240,
      300, or 360. The duration period starts as soon as a Spot instance receives its instance
      ID. At the end of the duration, Amazon EC2 marks the Spot instance for termination and
      provides a Spot instance termination notice, which gives the instance a two-minute warning
      before it terminates.
    """


_ClientAddInstanceFleetInstanceFleetLaunchSpecificationsTypeDef = TypedDict(
    "_ClientAddInstanceFleetInstanceFleetLaunchSpecificationsTypeDef",
    {
        "SpotSpecification": ClientAddInstanceFleetInstanceFleetLaunchSpecificationsSpotSpecificationTypeDef
    },
)


class ClientAddInstanceFleetInstanceFleetLaunchSpecificationsTypeDef(
    _ClientAddInstanceFleetInstanceFleetLaunchSpecificationsTypeDef
):
    """
    Type definition for `ClientAddInstanceFleetInstanceFleet` `LaunchSpecifications`

    The launch specification for the instance fleet.

    - **SpotSpecification** *(dict) --* **[REQUIRED]**

      The launch specification for Spot instances in the fleet, which determines the defined
      duration and provisioning timeout behavior.

      - **TimeoutDurationMinutes** *(integer) --* **[REQUIRED]**

        The spot provisioning timeout period in minutes. If Spot instances are not provisioned
        within this time period, the ``TimeOutAction`` is taken. Minimum value is 5 and maximum
        value is 1440. The timeout applies only during initial provisioning, when the cluster is
        first created.

      - **TimeoutAction** *(string) --* **[REQUIRED]**

        The action to take when ``TargetSpotCapacity`` has not been fulfilled when the
        ``TimeoutDurationMinutes`` has expired; that is, when all Spot instances could not be
        provisioned within the Spot provisioning timeout. Valid values are ``TERMINATE_CLUSTER``
        and ``SWITCH_TO_ON_DEMAND`` . SWITCH_TO_ON_DEMAND specifies that if no Spot instances are
        available, On-Demand Instances should be provisioned to fulfill any remaining Spot capacity.

      - **BlockDurationMinutes** *(integer) --*

        The defined duration for Spot instances (also known as Spot blocks) in minutes. When
        specified, the Spot instance does not terminate before the defined duration expires, and
        defined duration pricing for Spot instances applies. Valid values are 60, 120, 180, 240,
        300, or 360. The duration period starts as soon as a Spot instance receives its instance
        ID. At the end of the duration, Amazon EC2 marks the Spot instance for termination and
        provides a Spot instance termination notice, which gives the instance a two-minute warning
        before it terminates.
    """


_RequiredClientAddInstanceFleetInstanceFleetTypeDef = TypedDict(
    "_RequiredClientAddInstanceFleetInstanceFleetTypeDef", {"InstanceFleetType": str}
)
_OptionalClientAddInstanceFleetInstanceFleetTypeDef = TypedDict(
    "_OptionalClientAddInstanceFleetInstanceFleetTypeDef",
    {
        "Name": str,
        "TargetOnDemandCapacity": int,
        "TargetSpotCapacity": int,
        "InstanceTypeConfigs": List[
            ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsTypeDef
        ],
        "LaunchSpecifications": ClientAddInstanceFleetInstanceFleetLaunchSpecificationsTypeDef,
    },
    total=False,
)


class ClientAddInstanceFleetInstanceFleetTypeDef(
    _RequiredClientAddInstanceFleetInstanceFleetTypeDef,
    _OptionalClientAddInstanceFleetInstanceFleetTypeDef,
):
    """
    Type definition for `ClientAddInstanceFleet` `InstanceFleet`

    Specifies the configuration of the instance fleet.

    - **Name** *(string) --*

      The friendly name of the instance fleet.

    - **InstanceFleetType** *(string) --* **[REQUIRED]**

      The node type that the instance fleet hosts. Valid values are MASTER,CORE,and TASK.

    - **TargetOnDemandCapacity** *(integer) --*

      The target capacity of On-Demand units for the instance fleet, which determines how many
      On-Demand instances to provision. When the instance fleet launches, Amazon EMR tries to
      provision On-Demand instances as specified by  InstanceTypeConfig . Each instance configuration
      has a specified ``WeightedCapacity`` . When an On-Demand instance is provisioned, the
      ``WeightedCapacity`` units count toward the target capacity. Amazon EMR provisions instances
      until the target capacity is totally fulfilled, even if this results in an overage. For
      example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision
      an instance with a ``WeightedCapacity`` of 5 units, the instance is provisioned, and the target
      capacity is exceeded by 3 units.

      .. note::

        If not specified or set to 0, only Spot instances are provisioned for the instance fleet
        using ``TargetSpotCapacity`` . At least one of ``TargetSpotCapacity`` and
        ``TargetOnDemandCapacity`` should be greater than 0. For a master instance fleet, only one of
        ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` can be specified, and its value must be
        1.

    - **TargetSpotCapacity** *(integer) --*

      The target capacity of Spot units for the instance fleet, which determines how many Spot
      instances to provision. When the instance fleet launches, Amazon EMR tries to provision Spot
      instances as specified by  InstanceTypeConfig . Each instance configuration has a specified
      ``WeightedCapacity`` . When a Spot instance is provisioned, the ``WeightedCapacity`` units
      count toward the target capacity. Amazon EMR provisions instances until the target capacity is
      totally fulfilled, even if this results in an overage. For example, if there are 2 units
      remaining to fulfill capacity, and Amazon EMR can only provision an instance with a
      ``WeightedCapacity`` of 5 units, the instance is provisioned, and the target capacity is
      exceeded by 3 units.

      .. note::

        If not specified or set to 0, only On-Demand instances are provisioned for the instance
        fleet. At least one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` should be
        greater than 0. For a master instance fleet, only one of ``TargetSpotCapacity`` and
        ``TargetOnDemandCapacity`` can be specified, and its value must be 1.

    - **InstanceTypeConfigs** *(list) --*

      The instance type configurations that define the EC2 instances in the instance fleet.

      - *(dict) --*

        An instance type configuration for each instance type in an instance fleet, which determines
        the EC2 instances Amazon EMR attempts to provision to fulfill On-Demand and Spot target
        capacities. There can be a maximum of 5 instance type configurations in a fleet.

        .. note::

          The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later,
          excluding 5.0.x versions.

        - **InstanceType** *(string) --* **[REQUIRED]**

          An EC2 instance type, such as ``m3.xlarge`` .

        - **WeightedCapacity** *(integer) --*

          The number of units that a provisioned instance of this type provides toward fulfilling the
          target capacities defined in  InstanceFleetConfig . This value is 1 for a master instance
          fleet, and must be 1 or greater for core and task instance fleets. Defaults to 1 if not
          specified.

        - **BidPrice** *(string) --*

          The bid price for each EC2 Spot instance type as defined by ``InstanceType`` . Expressed in
          USD. If neither ``BidPrice`` nor ``BidPriceAsPercentageOfOnDemandPrice`` is provided,
          ``BidPriceAsPercentageOfOnDemandPrice`` defaults to 100%.

        - **BidPriceAsPercentageOfOnDemandPrice** *(float) --*

          The bid price, as a percentage of On-Demand price, for each EC2 Spot instance as defined by
          ``InstanceType`` . Expressed as a number (for example, 20 specifies 20%). If neither
          ``BidPrice`` nor ``BidPriceAsPercentageOfOnDemandPrice`` is provided,
          ``BidPriceAsPercentageOfOnDemandPrice`` defaults to 100%.

        - **EbsConfiguration** *(dict) --*

          The configuration of Amazon Elastic Block Storage (EBS) attached to each instance as
          defined by ``InstanceType`` .

          - **EbsBlockDeviceConfigs** *(list) --*

            An array of Amazon EBS volume specifications attached to a cluster instance.

            - *(dict) --*

              Configuration of requested EBS block device associated with the instance group with
              count of volumes that will be associated to every instance.

              - **VolumeSpecification** *(dict) --* **[REQUIRED]**

                EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
                requested for the EBS volume attached to an EC2 instance in the cluster.

                - **VolumeType** *(string) --* **[REQUIRED]**

                  The volume type. Volume types supported are gp2, io1, standard.

                - **Iops** *(integer) --*

                  The number of I/O operations per second (IOPS) that the volume supports.

                - **SizeInGB** *(integer) --* **[REQUIRED]**

                  The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
                  volume type is EBS-optimized, the minimum value is 10.

              - **VolumesPerInstance** *(integer) --*

                Number of EBS volumes with a specific volume configuration that will be associated
                with every instance in the instance group

          - **EbsOptimized** *(boolean) --*

            Indicates whether an Amazon EBS volume is EBS-optimized.

        - **Configurations** *(list) --*

          A configuration classification that applies when provisioning cluster instances, which can
          include configurations for applications and software that run on the cluster.

          - *(dict) --*

            .. note::

              Amazon EMR releases 4.x or later.

            An optional configuration specification to be used when provisioning cluster instances,
            which can include configurations for applications and software bundled with Amazon EMR. A
            configuration consists of a classification, properties, and optional nested
            configurations. A classification refers to an application-specific configuration file.
            Properties are the settings you want to change in that file. For more information, see
            `Configuring Applications
            <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

            - **Classification** *(string) --*

              The classification within a configuration.

            - **Configurations** *(list) --*

              A list of additional configurations to apply within a configuration object.

            - **Properties** *(dict) --*

              A set of properties specified within a configuration classification.

              - *(string) --*

                - *(string) --*

    - **LaunchSpecifications** *(dict) --*

      The launch specification for the instance fleet.

      - **SpotSpecification** *(dict) --* **[REQUIRED]**

        The launch specification for Spot instances in the fleet, which determines the defined
        duration and provisioning timeout behavior.

        - **TimeoutDurationMinutes** *(integer) --* **[REQUIRED]**

          The spot provisioning timeout period in minutes. If Spot instances are not provisioned
          within this time period, the ``TimeOutAction`` is taken. Minimum value is 5 and maximum
          value is 1440. The timeout applies only during initial provisioning, when the cluster is
          first created.

        - **TimeoutAction** *(string) --* **[REQUIRED]**

          The action to take when ``TargetSpotCapacity`` has not been fulfilled when the
          ``TimeoutDurationMinutes`` has expired; that is, when all Spot instances could not be
          provisioned within the Spot provisioning timeout. Valid values are ``TERMINATE_CLUSTER``
          and ``SWITCH_TO_ON_DEMAND`` . SWITCH_TO_ON_DEMAND specifies that if no Spot instances are
          available, On-Demand Instances should be provisioned to fulfill any remaining Spot capacity.

        - **BlockDurationMinutes** *(integer) --*

          The defined duration for Spot instances (also known as Spot blocks) in minutes. When
          specified, the Spot instance does not terminate before the defined duration expires, and
          defined duration pricing for Spot instances applies. Valid values are 60, 120, 180, 240,
          300, or 360. The duration period starts as soon as a Spot instance receives its instance
          ID. At the end of the duration, Amazon EC2 marks the Spot instance for termination and
          provides a Spot instance termination notice, which gives the instance a two-minute warning
          before it terminates.
    """


_ClientAddInstanceFleetResponseTypeDef = TypedDict(
    "_ClientAddInstanceFleetResponseTypeDef",
    {"ClusterId": str, "InstanceFleetId": str, "ClusterArn": str},
    total=False,
)


class ClientAddInstanceFleetResponseTypeDef(_ClientAddInstanceFleetResponseTypeDef):
    """
    Type definition for `ClientAddInstanceFleet` `Response`

    - **ClusterId** *(string) --*

      The unique identifier of the cluster.

    - **InstanceFleetId** *(string) --*

      The unique identifier of the instance fleet.

    - **ClusterArn** *(string) --*

      The Amazon Resource Name of the cluster.
    """


_ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyConstraintsTypeDef = TypedDict(
    "_ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyConstraintsTypeDef",
    {"MinCapacity": int, "MaxCapacity": int},
)


class ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyConstraintsTypeDef(
    _ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyConstraintsTypeDef
):
    """
    Type definition for `ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicy` `Constraints`

    The upper and lower EC2 instance limits for an automatic scaling policy. Automatic scaling
    activity will not cause an instance group to grow above or below these limits.

    - **MinCapacity** *(integer) --* **[REQUIRED]**

      The lower boundary of EC2 instances in an instance group below which scaling activities
      are not allowed to shrink. Scale-in activities will not terminate instances below this
      boundary.

    - **MaxCapacity** *(integer) --* **[REQUIRED]**

      The upper boundary of EC2 instances in an instance group beyond which scaling activities
      are not allowed to grow. Scale-out activities will not add instances beyond this boundary.
    """


_RequiredClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef = TypedDict(
    "_RequiredClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    {"ScalingAdjustment": int},
)
_OptionalClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef = TypedDict(
    "_OptionalClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    {"AdjustmentType": str, "CoolDown": int},
    total=False,
)


class ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef(
    _RequiredClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef,
    _OptionalClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef,
):
    """
    Type definition for `ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesAction` `SimpleScalingPolicyConfiguration`

    The type of adjustment the automatic scaling activity makes when triggered, and the
    periodicity of the adjustment.

    - **AdjustmentType** *(string) --*

      The way in which EC2 instances are added (if ``ScalingAdjustment`` is a positive
      number) or terminated (if ``ScalingAdjustment`` is a negative number) each time the
      scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the default.
      ``CHANGE_IN_CAPACITY`` indicates that the EC2 instance count increments or
      decrements by ``ScalingAdjustment`` , which should be expressed as an integer.
      ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count increments or
      decrements by the percentage specified by ``ScalingAdjustment`` , which should be
      expressed as an integer. For example, 20 indicates an increase in 20% increments of
      cluster capacity. ``EXACT_CAPACITY`` indicates the scaling activity results in an
      instance group with the number of EC2 instances specified by ``ScalingAdjustment``
      , which should be expressed as a positive integer.

    - **ScalingAdjustment** *(integer) --* **[REQUIRED]**

      The amount by which to scale in or scale out, based on the specified
      ``AdjustmentType`` . A positive value adds to the instance group's EC2 instance
      count while a negative number removes instances. If ``AdjustmentType`` is set to
      ``EXACT_CAPACITY`` , the number should only be a positive integer. If
      ``AdjustmentType`` is set to ``PERCENT_CHANGE_IN_CAPACITY`` , the value should
      express the percentage as an integer. For example, -20 indicates a decrease in 20%
      increments of cluster capacity.

    - **CoolDown** *(integer) --*

      The amount of time, in seconds, after a scaling activity completes before any
      further trigger-related scaling activities can start. The default value is 0.
    """


_RequiredClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionTypeDef = TypedDict(
    "_RequiredClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionTypeDef",
    {
        "SimpleScalingPolicyConfiguration": ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef
    },
)
_OptionalClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionTypeDef = TypedDict(
    "_OptionalClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionTypeDef",
    {"Market": str},
    total=False,
)


class ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionTypeDef(
    _RequiredClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionTypeDef,
    _OptionalClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionTypeDef,
):
    """
    Type definition for `ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRules` `Action`

    The conditions that trigger an automatic scaling activity.

    - **Market** *(string) --*

      Not available for instance groups. Instance groups use the market type specified for
      the group.

    - **SimpleScalingPolicyConfiguration** *(dict) --* **[REQUIRED]**

      The type of adjustment the automatic scaling activity makes when triggered, and the
      periodicity of the adjustment.

      - **AdjustmentType** *(string) --*

        The way in which EC2 instances are added (if ``ScalingAdjustment`` is a positive
        number) or terminated (if ``ScalingAdjustment`` is a negative number) each time the
        scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the default.
        ``CHANGE_IN_CAPACITY`` indicates that the EC2 instance count increments or
        decrements by ``ScalingAdjustment`` , which should be expressed as an integer.
        ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count increments or
        decrements by the percentage specified by ``ScalingAdjustment`` , which should be
        expressed as an integer. For example, 20 indicates an increase in 20% increments of
        cluster capacity. ``EXACT_CAPACITY`` indicates the scaling activity results in an
        instance group with the number of EC2 instances specified by ``ScalingAdjustment``
        , which should be expressed as a positive integer.

      - **ScalingAdjustment** *(integer) --* **[REQUIRED]**

        The amount by which to scale in or scale out, based on the specified
        ``AdjustmentType`` . A positive value adds to the instance group's EC2 instance
        count while a negative number removes instances. If ``AdjustmentType`` is set to
        ``EXACT_CAPACITY`` , the number should only be a positive integer. If
        ``AdjustmentType`` is set to ``PERCENT_CHANGE_IN_CAPACITY`` , the value should
        express the percentage as an integer. For example, -20 indicates a decrease in 20%
        increments of cluster capacity.

      - **CoolDown** *(integer) --*

        The amount of time, in seconds, after a scaling activity completes before any
        further trigger-related scaling activities can start. The default value is 0.
    """


_ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef = TypedDict(
    "_ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef(
    _ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef
):
    """
    Type definition for `ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinition` `Dimensions`

    A CloudWatch dimension, which is specified using a ``Key`` (known as a ``Name``
    in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one dimension whose
    ``Key`` is ``JobFlowID`` and ``Value`` is a variable representing the cluster ID,
    which is ``${emr.clusterId}`` . This enables the rule to bootstrap when the
    cluster ID becomes available.

    - **Key** *(string) --*

      The dimension name.

    - **Value** *(string) --*

      The dimension value.
    """


_RequiredClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef = TypedDict(
    "_RequiredClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    {"ComparisonOperator": str, "MetricName": str, "Period": int, "Threshold": float},
)
_OptionalClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef = TypedDict(
    "_OptionalClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    {
        "EvaluationPeriods": int,
        "Namespace": str,
        "Statistic": str,
        "Unit": str,
        "Dimensions": List[
            ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef
        ],
    },
    total=False,
)


class ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef(
    _RequiredClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef,
    _OptionalClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef,
):
    """
    Type definition for `ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTrigger` `CloudWatchAlarmDefinition`

    The definition of a CloudWatch metric alarm. When the defined alarm conditions are
    met along with other trigger parameters, scaling activity begins.

    - **ComparisonOperator** *(string) --* **[REQUIRED]**

      Determines how the metric specified by ``MetricName`` is compared to the value
      specified by ``Threshold`` .

    - **EvaluationPeriods** *(integer) --*

      The number of periods, in five-minute increments, during which the alarm condition
      must exist before the alarm triggers automatic scaling activity. The default value
      is ``1`` .

    - **MetricName** *(string) --* **[REQUIRED]**

      The name of the CloudWatch metric that is watched to determine an alarm condition.

    - **Namespace** *(string) --*

      The namespace for the CloudWatch metric. The default is ``AWS/ElasticMapReduce`` .

    - **Period** *(integer) --* **[REQUIRED]**

      The period, in seconds, over which the statistic is applied. EMR CloudWatch metrics
      are emitted every five minutes (300 seconds), so if an EMR CloudWatch metric is
      specified, specify ``300`` .

    - **Statistic** *(string) --*

      The statistic to apply to the metric associated with the alarm. The default is
      ``AVERAGE`` .

    - **Threshold** *(float) --* **[REQUIRED]**

      The value against which the specified statistic is compared.

    - **Unit** *(string) --*

      The unit of measure associated with the CloudWatch metric being watched. The value
      specified for ``Unit`` must correspond to the units specified in the CloudWatch
      metric.

    - **Dimensions** *(list) --*

      A CloudWatch metric dimension.

      - *(dict) --*

        A CloudWatch dimension, which is specified using a ``Key`` (known as a ``Name``
        in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one dimension whose
        ``Key`` is ``JobFlowID`` and ``Value`` is a variable representing the cluster ID,
        which is ``${emr.clusterId}`` . This enables the rule to bootstrap when the
        cluster ID becomes available.

        - **Key** *(string) --*

          The dimension name.

        - **Value** *(string) --*

          The dimension value.
    """


_ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef = TypedDict(
    "_ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef",
    {
        "CloudWatchAlarmDefinition": ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef
    },
)


class ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef(
    _ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef
):
    """
    Type definition for `ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRules` `Trigger`

    The CloudWatch alarm definition that determines when automatic scaling activity is
    triggered.

    - **CloudWatchAlarmDefinition** *(dict) --* **[REQUIRED]**

      The definition of a CloudWatch metric alarm. When the defined alarm conditions are
      met along with other trigger parameters, scaling activity begins.

      - **ComparisonOperator** *(string) --* **[REQUIRED]**

        Determines how the metric specified by ``MetricName`` is compared to the value
        specified by ``Threshold`` .

      - **EvaluationPeriods** *(integer) --*

        The number of periods, in five-minute increments, during which the alarm condition
        must exist before the alarm triggers automatic scaling activity. The default value
        is ``1`` .

      - **MetricName** *(string) --* **[REQUIRED]**

        The name of the CloudWatch metric that is watched to determine an alarm condition.

      - **Namespace** *(string) --*

        The namespace for the CloudWatch metric. The default is ``AWS/ElasticMapReduce`` .

      - **Period** *(integer) --* **[REQUIRED]**

        The period, in seconds, over which the statistic is applied. EMR CloudWatch metrics
        are emitted every five minutes (300 seconds), so if an EMR CloudWatch metric is
        specified, specify ``300`` .

      - **Statistic** *(string) --*

        The statistic to apply to the metric associated with the alarm. The default is
        ``AVERAGE`` .

      - **Threshold** *(float) --* **[REQUIRED]**

        The value against which the specified statistic is compared.

      - **Unit** *(string) --*

        The unit of measure associated with the CloudWatch metric being watched. The value
        specified for ``Unit`` must correspond to the units specified in the CloudWatch
        metric.

      - **Dimensions** *(list) --*

        A CloudWatch metric dimension.

        - *(dict) --*

          A CloudWatch dimension, which is specified using a ``Key`` (known as a ``Name``
          in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one dimension whose
          ``Key`` is ``JobFlowID`` and ``Value`` is a variable representing the cluster ID,
          which is ``${emr.clusterId}`` . This enables the rule to bootstrap when the
          cluster ID becomes available.

          - **Key** *(string) --*

            The dimension name.

          - **Value** *(string) --*

            The dimension value.
    """


_RequiredClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTypeDef = TypedDict(
    "_RequiredClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTypeDef",
    {
        "Name": str,
        "Action": ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionTypeDef,
        "Trigger": ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef,
    },
)
_OptionalClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTypeDef = TypedDict(
    "_OptionalClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTypeDef",
    {"Description": str},
    total=False,
)


class ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTypeDef(
    _RequiredClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTypeDef,
    _OptionalClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTypeDef,
):
    """
    Type definition for `ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicy` `Rules`

    A scale-in or scale-out rule that defines scaling activity, including the CloudWatch
    metric alarm that triggers activity, how EC2 instances are added or removed, and the
    periodicity of adjustments. The automatic scaling policy for an instance group can
    comprise one or more automatic scaling rules.

    - **Name** *(string) --* **[REQUIRED]**

      The name used to identify an automatic scaling rule. Rule names must be unique within a
      scaling policy.

    - **Description** *(string) --*

      A friendly, more verbose description of the automatic scaling rule.

    - **Action** *(dict) --* **[REQUIRED]**

      The conditions that trigger an automatic scaling activity.

      - **Market** *(string) --*

        Not available for instance groups. Instance groups use the market type specified for
        the group.

      - **SimpleScalingPolicyConfiguration** *(dict) --* **[REQUIRED]**

        The type of adjustment the automatic scaling activity makes when triggered, and the
        periodicity of the adjustment.

        - **AdjustmentType** *(string) --*

          The way in which EC2 instances are added (if ``ScalingAdjustment`` is a positive
          number) or terminated (if ``ScalingAdjustment`` is a negative number) each time the
          scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the default.
          ``CHANGE_IN_CAPACITY`` indicates that the EC2 instance count increments or
          decrements by ``ScalingAdjustment`` , which should be expressed as an integer.
          ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count increments or
          decrements by the percentage specified by ``ScalingAdjustment`` , which should be
          expressed as an integer. For example, 20 indicates an increase in 20% increments of
          cluster capacity. ``EXACT_CAPACITY`` indicates the scaling activity results in an
          instance group with the number of EC2 instances specified by ``ScalingAdjustment``
          , which should be expressed as a positive integer.

        - **ScalingAdjustment** *(integer) --* **[REQUIRED]**

          The amount by which to scale in or scale out, based on the specified
          ``AdjustmentType`` . A positive value adds to the instance group's EC2 instance
          count while a negative number removes instances. If ``AdjustmentType`` is set to
          ``EXACT_CAPACITY`` , the number should only be a positive integer. If
          ``AdjustmentType`` is set to ``PERCENT_CHANGE_IN_CAPACITY`` , the value should
          express the percentage as an integer. For example, -20 indicates a decrease in 20%
          increments of cluster capacity.

        - **CoolDown** *(integer) --*

          The amount of time, in seconds, after a scaling activity completes before any
          further trigger-related scaling activities can start. The default value is 0.

    - **Trigger** *(dict) --* **[REQUIRED]**

      The CloudWatch alarm definition that determines when automatic scaling activity is
      triggered.

      - **CloudWatchAlarmDefinition** *(dict) --* **[REQUIRED]**

        The definition of a CloudWatch metric alarm. When the defined alarm conditions are
        met along with other trigger parameters, scaling activity begins.

        - **ComparisonOperator** *(string) --* **[REQUIRED]**

          Determines how the metric specified by ``MetricName`` is compared to the value
          specified by ``Threshold`` .

        - **EvaluationPeriods** *(integer) --*

          The number of periods, in five-minute increments, during which the alarm condition
          must exist before the alarm triggers automatic scaling activity. The default value
          is ``1`` .

        - **MetricName** *(string) --* **[REQUIRED]**

          The name of the CloudWatch metric that is watched to determine an alarm condition.

        - **Namespace** *(string) --*

          The namespace for the CloudWatch metric. The default is ``AWS/ElasticMapReduce`` .

        - **Period** *(integer) --* **[REQUIRED]**

          The period, in seconds, over which the statistic is applied. EMR CloudWatch metrics
          are emitted every five minutes (300 seconds), so if an EMR CloudWatch metric is
          specified, specify ``300`` .

        - **Statistic** *(string) --*

          The statistic to apply to the metric associated with the alarm. The default is
          ``AVERAGE`` .

        - **Threshold** *(float) --* **[REQUIRED]**

          The value against which the specified statistic is compared.

        - **Unit** *(string) --*

          The unit of measure associated with the CloudWatch metric being watched. The value
          specified for ``Unit`` must correspond to the units specified in the CloudWatch
          metric.

        - **Dimensions** *(list) --*

          A CloudWatch metric dimension.

          - *(dict) --*

            A CloudWatch dimension, which is specified using a ``Key`` (known as a ``Name``
            in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one dimension whose
            ``Key`` is ``JobFlowID`` and ``Value`` is a variable representing the cluster ID,
            which is ``${emr.clusterId}`` . This enables the rule to bootstrap when the
            cluster ID becomes available.

            - **Key** *(string) --*

              The dimension name.

            - **Value** *(string) --*

              The dimension value.
    """


_ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyTypeDef = TypedDict(
    "_ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyTypeDef",
    {
        "Constraints": ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyConstraintsTypeDef,
        "Rules": List[
            ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTypeDef
        ],
    },
)


class ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyTypeDef(
    _ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyTypeDef
):
    """
    Type definition for `ClientAddInstanceGroupsInstanceGroups` `AutoScalingPolicy`

    An automatic scaling policy for a core instance group or task instance group in an Amazon EMR
    cluster. The automatic scaling policy defines how an instance group dynamically adds and
    terminates EC2 instances in response to the value of a CloudWatch metric. See
    PutAutoScalingPolicy .

    - **Constraints** *(dict) --* **[REQUIRED]**

      The upper and lower EC2 instance limits for an automatic scaling policy. Automatic scaling
      activity will not cause an instance group to grow above or below these limits.

      - **MinCapacity** *(integer) --* **[REQUIRED]**

        The lower boundary of EC2 instances in an instance group below which scaling activities
        are not allowed to shrink. Scale-in activities will not terminate instances below this
        boundary.

      - **MaxCapacity** *(integer) --* **[REQUIRED]**

        The upper boundary of EC2 instances in an instance group beyond which scaling activities
        are not allowed to grow. Scale-out activities will not add instances beyond this boundary.

    - **Rules** *(list) --* **[REQUIRED]**

      The scale-in and scale-out rules that comprise the automatic scaling policy.

      - *(dict) --*

        A scale-in or scale-out rule that defines scaling activity, including the CloudWatch
        metric alarm that triggers activity, how EC2 instances are added or removed, and the
        periodicity of adjustments. The automatic scaling policy for an instance group can
        comprise one or more automatic scaling rules.

        - **Name** *(string) --* **[REQUIRED]**

          The name used to identify an automatic scaling rule. Rule names must be unique within a
          scaling policy.

        - **Description** *(string) --*

          A friendly, more verbose description of the automatic scaling rule.

        - **Action** *(dict) --* **[REQUIRED]**

          The conditions that trigger an automatic scaling activity.

          - **Market** *(string) --*

            Not available for instance groups. Instance groups use the market type specified for
            the group.

          - **SimpleScalingPolicyConfiguration** *(dict) --* **[REQUIRED]**

            The type of adjustment the automatic scaling activity makes when triggered, and the
            periodicity of the adjustment.

            - **AdjustmentType** *(string) --*

              The way in which EC2 instances are added (if ``ScalingAdjustment`` is a positive
              number) or terminated (if ``ScalingAdjustment`` is a negative number) each time the
              scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the default.
              ``CHANGE_IN_CAPACITY`` indicates that the EC2 instance count increments or
              decrements by ``ScalingAdjustment`` , which should be expressed as an integer.
              ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count increments or
              decrements by the percentage specified by ``ScalingAdjustment`` , which should be
              expressed as an integer. For example, 20 indicates an increase in 20% increments of
              cluster capacity. ``EXACT_CAPACITY`` indicates the scaling activity results in an
              instance group with the number of EC2 instances specified by ``ScalingAdjustment``
              , which should be expressed as a positive integer.

            - **ScalingAdjustment** *(integer) --* **[REQUIRED]**

              The amount by which to scale in or scale out, based on the specified
              ``AdjustmentType`` . A positive value adds to the instance group's EC2 instance
              count while a negative number removes instances. If ``AdjustmentType`` is set to
              ``EXACT_CAPACITY`` , the number should only be a positive integer. If
              ``AdjustmentType`` is set to ``PERCENT_CHANGE_IN_CAPACITY`` , the value should
              express the percentage as an integer. For example, -20 indicates a decrease in 20%
              increments of cluster capacity.

            - **CoolDown** *(integer) --*

              The amount of time, in seconds, after a scaling activity completes before any
              further trigger-related scaling activities can start. The default value is 0.

        - **Trigger** *(dict) --* **[REQUIRED]**

          The CloudWatch alarm definition that determines when automatic scaling activity is
          triggered.

          - **CloudWatchAlarmDefinition** *(dict) --* **[REQUIRED]**

            The definition of a CloudWatch metric alarm. When the defined alarm conditions are
            met along with other trigger parameters, scaling activity begins.

            - **ComparisonOperator** *(string) --* **[REQUIRED]**

              Determines how the metric specified by ``MetricName`` is compared to the value
              specified by ``Threshold`` .

            - **EvaluationPeriods** *(integer) --*

              The number of periods, in five-minute increments, during which the alarm condition
              must exist before the alarm triggers automatic scaling activity. The default value
              is ``1`` .

            - **MetricName** *(string) --* **[REQUIRED]**

              The name of the CloudWatch metric that is watched to determine an alarm condition.

            - **Namespace** *(string) --*

              The namespace for the CloudWatch metric. The default is ``AWS/ElasticMapReduce`` .

            - **Period** *(integer) --* **[REQUIRED]**

              The period, in seconds, over which the statistic is applied. EMR CloudWatch metrics
              are emitted every five minutes (300 seconds), so if an EMR CloudWatch metric is
              specified, specify ``300`` .

            - **Statistic** *(string) --*

              The statistic to apply to the metric associated with the alarm. The default is
              ``AVERAGE`` .

            - **Threshold** *(float) --* **[REQUIRED]**

              The value against which the specified statistic is compared.

            - **Unit** *(string) --*

              The unit of measure associated with the CloudWatch metric being watched. The value
              specified for ``Unit`` must correspond to the units specified in the CloudWatch
              metric.

            - **Dimensions** *(list) --*

              A CloudWatch metric dimension.

              - *(dict) --*

                A CloudWatch dimension, which is specified using a ``Key`` (known as a ``Name``
                in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one dimension whose
                ``Key`` is ``JobFlowID`` and ``Value`` is a variable representing the cluster ID,
                which is ``${emr.clusterId}`` . This enables the rule to bootstrap when the
                cluster ID becomes available.

                - **Key** *(string) --*

                  The dimension name.

                - **Value** *(string) --*

                  The dimension value.
    """


_ClientAddInstanceGroupsInstanceGroupsConfigurationsTypeDef = TypedDict(
    "_ClientAddInstanceGroupsInstanceGroupsConfigurationsTypeDef",
    {"Classification": str, "Configurations": List[Any], "Properties": Dict[str, str]},
    total=False,
)


class ClientAddInstanceGroupsInstanceGroupsConfigurationsTypeDef(
    _ClientAddInstanceGroupsInstanceGroupsConfigurationsTypeDef
):
    """
    Type definition for `ClientAddInstanceGroupsInstanceGroups` `Configurations`

    .. note::

      Amazon EMR releases 4.x or later.

    An optional configuration specification to be used when provisioning cluster instances,
    which can include configurations for applications and software bundled with Amazon EMR. A
    configuration consists of a classification, properties, and optional nested configurations.
    A classification refers to an application-specific configuration file. Properties are the
    settings you want to change in that file. For more information, see `Configuring
    Applications
    <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

    - **Classification** *(string) --*

      The classification within a configuration.

    - **Configurations** *(list) --*

      A list of additional configurations to apply within a configuration object.

    - **Properties** *(dict) --*

      A set of properties specified within a configuration classification.

      - *(string) --*

        - *(string) --*
    """


_RequiredClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef = TypedDict(
    "_RequiredClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef",
    {"VolumeType": str, "SizeInGB": int},
)
_OptionalClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef = TypedDict(
    "_OptionalClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef",
    {"Iops": int},
    total=False,
)


class ClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef(
    _RequiredClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef,
    _OptionalClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef,
):
    """
    Type definition for `ClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigs` `VolumeSpecification`

    EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
    requested for the EBS volume attached to an EC2 instance in the cluster.

    - **VolumeType** *(string) --* **[REQUIRED]**

      The volume type. Volume types supported are gp2, io1, standard.

    - **Iops** *(integer) --*

      The number of I/O operations per second (IOPS) that the volume supports.

    - **SizeInGB** *(integer) --* **[REQUIRED]**

      The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
      volume type is EBS-optimized, the minimum value is 10.
    """


_RequiredClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef = TypedDict(
    "_RequiredClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef",
    {
        "VolumeSpecification": ClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef
    },
)
_OptionalClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef = TypedDict(
    "_OptionalClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef",
    {"VolumesPerInstance": int},
    total=False,
)


class ClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef(
    _RequiredClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef,
    _OptionalClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef,
):
    """
    Type definition for `ClientAddInstanceGroupsInstanceGroupsEbsConfiguration` `EbsBlockDeviceConfigs`

    Configuration of requested EBS block device associated with the instance group with count
    of volumes that will be associated to every instance.

    - **VolumeSpecification** *(dict) --* **[REQUIRED]**

      EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
      requested for the EBS volume attached to an EC2 instance in the cluster.

      - **VolumeType** *(string) --* **[REQUIRED]**

        The volume type. Volume types supported are gp2, io1, standard.

      - **Iops** *(integer) --*

        The number of I/O operations per second (IOPS) that the volume supports.

      - **SizeInGB** *(integer) --* **[REQUIRED]**

        The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
        volume type is EBS-optimized, the minimum value is 10.

    - **VolumesPerInstance** *(integer) --*

      Number of EBS volumes with a specific volume configuration that will be associated with
      every instance in the instance group
    """


_ClientAddInstanceGroupsInstanceGroupsEbsConfigurationTypeDef = TypedDict(
    "_ClientAddInstanceGroupsInstanceGroupsEbsConfigurationTypeDef",
    {
        "EbsBlockDeviceConfigs": List[
            ClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef
        ],
        "EbsOptimized": bool,
    },
    total=False,
)


class ClientAddInstanceGroupsInstanceGroupsEbsConfigurationTypeDef(
    _ClientAddInstanceGroupsInstanceGroupsEbsConfigurationTypeDef
):
    """
    Type definition for `ClientAddInstanceGroupsInstanceGroups` `EbsConfiguration`

    EBS configurations that will be attached to each EC2 instance in the instance group.

    - **EbsBlockDeviceConfigs** *(list) --*

      An array of Amazon EBS volume specifications attached to a cluster instance.

      - *(dict) --*

        Configuration of requested EBS block device associated with the instance group with count
        of volumes that will be associated to every instance.

        - **VolumeSpecification** *(dict) --* **[REQUIRED]**

          EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
          requested for the EBS volume attached to an EC2 instance in the cluster.

          - **VolumeType** *(string) --* **[REQUIRED]**

            The volume type. Volume types supported are gp2, io1, standard.

          - **Iops** *(integer) --*

            The number of I/O operations per second (IOPS) that the volume supports.

          - **SizeInGB** *(integer) --* **[REQUIRED]**

            The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
            volume type is EBS-optimized, the minimum value is 10.

        - **VolumesPerInstance** *(integer) --*

          Number of EBS volumes with a specific volume configuration that will be associated with
          every instance in the instance group

    - **EbsOptimized** *(boolean) --*

      Indicates whether an Amazon EBS volume is EBS-optimized.
    """


_RequiredClientAddInstanceGroupsInstanceGroupsTypeDef = TypedDict(
    "_RequiredClientAddInstanceGroupsInstanceGroupsTypeDef",
    {"InstanceRole": str, "InstanceType": str, "InstanceCount": int},
)
_OptionalClientAddInstanceGroupsInstanceGroupsTypeDef = TypedDict(
    "_OptionalClientAddInstanceGroupsInstanceGroupsTypeDef",
    {
        "Name": str,
        "Market": str,
        "BidPrice": str,
        "Configurations": List[
            ClientAddInstanceGroupsInstanceGroupsConfigurationsTypeDef
        ],
        "EbsConfiguration": ClientAddInstanceGroupsInstanceGroupsEbsConfigurationTypeDef,
        "AutoScalingPolicy": ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyTypeDef,
    },
    total=False,
)


class ClientAddInstanceGroupsInstanceGroupsTypeDef(
    _RequiredClientAddInstanceGroupsInstanceGroupsTypeDef,
    _OptionalClientAddInstanceGroupsInstanceGroupsTypeDef,
):
    """
    Type definition for `ClientAddInstanceGroups` `InstanceGroups`

    Configuration defining a new instance group.

    - **Name** *(string) --*

      Friendly name given to the instance group.

    - **Market** *(string) --*

      Market type of the EC2 instances used to create a cluster node.

    - **InstanceRole** *(string) --* **[REQUIRED]**

      The role of the instance group in the cluster.

    - **BidPrice** *(string) --*

      The bid price for each EC2 Spot instance type as defined by ``InstanceType`` . Expressed in
      USD. If neither ``BidPrice`` nor ``BidPriceAsPercentageOfOnDemandPrice`` is provided,
      ``BidPriceAsPercentageOfOnDemandPrice`` defaults to 100%.

    - **InstanceType** *(string) --* **[REQUIRED]**

      The EC2 instance type for all instances in the instance group.

    - **InstanceCount** *(integer) --* **[REQUIRED]**

      Target number of instances for the instance group.

    - **Configurations** *(list) --*

      .. note::

        Amazon EMR releases 4.x or later.

      The list of configurations supplied for an EMR cluster instance group. You can specify a
      separate configuration for each instance group (master, core, and task).

      - *(dict) --*

        .. note::

          Amazon EMR releases 4.x or later.

        An optional configuration specification to be used when provisioning cluster instances,
        which can include configurations for applications and software bundled with Amazon EMR. A
        configuration consists of a classification, properties, and optional nested configurations.
        A classification refers to an application-specific configuration file. Properties are the
        settings you want to change in that file. For more information, see `Configuring
        Applications
        <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

        - **Classification** *(string) --*

          The classification within a configuration.

        - **Configurations** *(list) --*

          A list of additional configurations to apply within a configuration object.

        - **Properties** *(dict) --*

          A set of properties specified within a configuration classification.

          - *(string) --*

            - *(string) --*

    - **EbsConfiguration** *(dict) --*

      EBS configurations that will be attached to each EC2 instance in the instance group.

      - **EbsBlockDeviceConfigs** *(list) --*

        An array of Amazon EBS volume specifications attached to a cluster instance.

        - *(dict) --*

          Configuration of requested EBS block device associated with the instance group with count
          of volumes that will be associated to every instance.

          - **VolumeSpecification** *(dict) --* **[REQUIRED]**

            EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
            requested for the EBS volume attached to an EC2 instance in the cluster.

            - **VolumeType** *(string) --* **[REQUIRED]**

              The volume type. Volume types supported are gp2, io1, standard.

            - **Iops** *(integer) --*

              The number of I/O operations per second (IOPS) that the volume supports.

            - **SizeInGB** *(integer) --* **[REQUIRED]**

              The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
              volume type is EBS-optimized, the minimum value is 10.

          - **VolumesPerInstance** *(integer) --*

            Number of EBS volumes with a specific volume configuration that will be associated with
            every instance in the instance group

      - **EbsOptimized** *(boolean) --*

        Indicates whether an Amazon EBS volume is EBS-optimized.

    - **AutoScalingPolicy** *(dict) --*

      An automatic scaling policy for a core instance group or task instance group in an Amazon EMR
      cluster. The automatic scaling policy defines how an instance group dynamically adds and
      terminates EC2 instances in response to the value of a CloudWatch metric. See
      PutAutoScalingPolicy .

      - **Constraints** *(dict) --* **[REQUIRED]**

        The upper and lower EC2 instance limits for an automatic scaling policy. Automatic scaling
        activity will not cause an instance group to grow above or below these limits.

        - **MinCapacity** *(integer) --* **[REQUIRED]**

          The lower boundary of EC2 instances in an instance group below which scaling activities
          are not allowed to shrink. Scale-in activities will not terminate instances below this
          boundary.

        - **MaxCapacity** *(integer) --* **[REQUIRED]**

          The upper boundary of EC2 instances in an instance group beyond which scaling activities
          are not allowed to grow. Scale-out activities will not add instances beyond this boundary.

      - **Rules** *(list) --* **[REQUIRED]**

        The scale-in and scale-out rules that comprise the automatic scaling policy.

        - *(dict) --*

          A scale-in or scale-out rule that defines scaling activity, including the CloudWatch
          metric alarm that triggers activity, how EC2 instances are added or removed, and the
          periodicity of adjustments. The automatic scaling policy for an instance group can
          comprise one or more automatic scaling rules.

          - **Name** *(string) --* **[REQUIRED]**

            The name used to identify an automatic scaling rule. Rule names must be unique within a
            scaling policy.

          - **Description** *(string) --*

            A friendly, more verbose description of the automatic scaling rule.

          - **Action** *(dict) --* **[REQUIRED]**

            The conditions that trigger an automatic scaling activity.

            - **Market** *(string) --*

              Not available for instance groups. Instance groups use the market type specified for
              the group.

            - **SimpleScalingPolicyConfiguration** *(dict) --* **[REQUIRED]**

              The type of adjustment the automatic scaling activity makes when triggered, and the
              periodicity of the adjustment.

              - **AdjustmentType** *(string) --*

                The way in which EC2 instances are added (if ``ScalingAdjustment`` is a positive
                number) or terminated (if ``ScalingAdjustment`` is a negative number) each time the
                scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the default.
                ``CHANGE_IN_CAPACITY`` indicates that the EC2 instance count increments or
                decrements by ``ScalingAdjustment`` , which should be expressed as an integer.
                ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count increments or
                decrements by the percentage specified by ``ScalingAdjustment`` , which should be
                expressed as an integer. For example, 20 indicates an increase in 20% increments of
                cluster capacity. ``EXACT_CAPACITY`` indicates the scaling activity results in an
                instance group with the number of EC2 instances specified by ``ScalingAdjustment``
                , which should be expressed as a positive integer.

              - **ScalingAdjustment** *(integer) --* **[REQUIRED]**

                The amount by which to scale in or scale out, based on the specified
                ``AdjustmentType`` . A positive value adds to the instance group's EC2 instance
                count while a negative number removes instances. If ``AdjustmentType`` is set to
                ``EXACT_CAPACITY`` , the number should only be a positive integer. If
                ``AdjustmentType`` is set to ``PERCENT_CHANGE_IN_CAPACITY`` , the value should
                express the percentage as an integer. For example, -20 indicates a decrease in 20%
                increments of cluster capacity.

              - **CoolDown** *(integer) --*

                The amount of time, in seconds, after a scaling activity completes before any
                further trigger-related scaling activities can start. The default value is 0.

          - **Trigger** *(dict) --* **[REQUIRED]**

            The CloudWatch alarm definition that determines when automatic scaling activity is
            triggered.

            - **CloudWatchAlarmDefinition** *(dict) --* **[REQUIRED]**

              The definition of a CloudWatch metric alarm. When the defined alarm conditions are
              met along with other trigger parameters, scaling activity begins.

              - **ComparisonOperator** *(string) --* **[REQUIRED]**

                Determines how the metric specified by ``MetricName`` is compared to the value
                specified by ``Threshold`` .

              - **EvaluationPeriods** *(integer) --*

                The number of periods, in five-minute increments, during which the alarm condition
                must exist before the alarm triggers automatic scaling activity. The default value
                is ``1`` .

              - **MetricName** *(string) --* **[REQUIRED]**

                The name of the CloudWatch metric that is watched to determine an alarm condition.

              - **Namespace** *(string) --*

                The namespace for the CloudWatch metric. The default is ``AWS/ElasticMapReduce`` .

              - **Period** *(integer) --* **[REQUIRED]**

                The period, in seconds, over which the statistic is applied. EMR CloudWatch metrics
                are emitted every five minutes (300 seconds), so if an EMR CloudWatch metric is
                specified, specify ``300`` .

              - **Statistic** *(string) --*

                The statistic to apply to the metric associated with the alarm. The default is
                ``AVERAGE`` .

              - **Threshold** *(float) --* **[REQUIRED]**

                The value against which the specified statistic is compared.

              - **Unit** *(string) --*

                The unit of measure associated with the CloudWatch metric being watched. The value
                specified for ``Unit`` must correspond to the units specified in the CloudWatch
                metric.

              - **Dimensions** *(list) --*

                A CloudWatch metric dimension.

                - *(dict) --*

                  A CloudWatch dimension, which is specified using a ``Key`` (known as a ``Name``
                  in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one dimension whose
                  ``Key`` is ``JobFlowID`` and ``Value`` is a variable representing the cluster ID,
                  which is ``${emr.clusterId}`` . This enables the rule to bootstrap when the
                  cluster ID becomes available.

                  - **Key** *(string) --*

                    The dimension name.

                  - **Value** *(string) --*

                    The dimension value.
    """


_ClientAddInstanceGroupsResponseTypeDef = TypedDict(
    "_ClientAddInstanceGroupsResponseTypeDef",
    {"JobFlowId": str, "InstanceGroupIds": List[str], "ClusterArn": str},
    total=False,
)


class ClientAddInstanceGroupsResponseTypeDef(_ClientAddInstanceGroupsResponseTypeDef):
    """
    Type definition for `ClientAddInstanceGroups` `Response`

    Output from an AddInstanceGroups call.

    - **JobFlowId** *(string) --*

      The job flow ID in which the instance groups are added.

    - **InstanceGroupIds** *(list) --*

      Instance group IDs of the newly created instance groups.

      - *(string) --*

    - **ClusterArn** *(string) --*

      The Amazon Resource Name of the cluster.
    """


_ClientAddJobFlowStepsResponseTypeDef = TypedDict(
    "_ClientAddJobFlowStepsResponseTypeDef", {"StepIds": List[str]}, total=False
)


class ClientAddJobFlowStepsResponseTypeDef(_ClientAddJobFlowStepsResponseTypeDef):
    """
    Type definition for `ClientAddJobFlowSteps` `Response`

    The output for the  AddJobFlowSteps operation.

    - **StepIds** *(list) --*

      The identifiers of the list of steps added to the job flow.

      - *(string) --*
    """


_ClientAddJobFlowStepsStepsHadoopJarStepPropertiesTypeDef = TypedDict(
    "_ClientAddJobFlowStepsStepsHadoopJarStepPropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientAddJobFlowStepsStepsHadoopJarStepPropertiesTypeDef(
    _ClientAddJobFlowStepsStepsHadoopJarStepPropertiesTypeDef
):
    """
    Type definition for `ClientAddJobFlowStepsStepsHadoopJarStep` `Properties`

    A key value pair.

    - **Key** *(string) --*

      The unique identifier of a key value pair.

    - **Value** *(string) --*

      The value part of the identified key.
    """


_RequiredClientAddJobFlowStepsStepsHadoopJarStepTypeDef = TypedDict(
    "_RequiredClientAddJobFlowStepsStepsHadoopJarStepTypeDef", {"Jar": str}
)
_OptionalClientAddJobFlowStepsStepsHadoopJarStepTypeDef = TypedDict(
    "_OptionalClientAddJobFlowStepsStepsHadoopJarStepTypeDef",
    {
        "Properties": List[ClientAddJobFlowStepsStepsHadoopJarStepPropertiesTypeDef],
        "MainClass": str,
        "Args": List[str],
    },
    total=False,
)


class ClientAddJobFlowStepsStepsHadoopJarStepTypeDef(
    _RequiredClientAddJobFlowStepsStepsHadoopJarStepTypeDef,
    _OptionalClientAddJobFlowStepsStepsHadoopJarStepTypeDef,
):
    """
    Type definition for `ClientAddJobFlowStepsSteps` `HadoopJarStep`

    The JAR file used for the step.

    - **Properties** *(list) --*

      A list of Java properties that are set when the step runs. You can use these properties to
      pass key value pairs to your main function.

      - *(dict) --*

        A key value pair.

        - **Key** *(string) --*

          The unique identifier of a key value pair.

        - **Value** *(string) --*

          The value part of the identified key.

    - **Jar** *(string) --* **[REQUIRED]**

      A path to a JAR file run during the step.

    - **MainClass** *(string) --*

      The name of the main class in the specified Java file. If not specified, the JAR file
      should specify a Main-Class in its manifest file.

    - **Args** *(list) --*

      A list of command line arguments passed to the JAR file's main function when executed.

      - *(string) --*
    """


_RequiredClientAddJobFlowStepsStepsTypeDef = TypedDict(
    "_RequiredClientAddJobFlowStepsStepsTypeDef",
    {"Name": str, "HadoopJarStep": ClientAddJobFlowStepsStepsHadoopJarStepTypeDef},
)
_OptionalClientAddJobFlowStepsStepsTypeDef = TypedDict(
    "_OptionalClientAddJobFlowStepsStepsTypeDef", {"ActionOnFailure": str}, total=False
)


class ClientAddJobFlowStepsStepsTypeDef(
    _RequiredClientAddJobFlowStepsStepsTypeDef,
    _OptionalClientAddJobFlowStepsStepsTypeDef,
):
    """
    Type definition for `ClientAddJobFlowSteps` `Steps`

    Specification of a cluster (job flow) step.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the step.

    - **ActionOnFailure** *(string) --*

      The action to take when the cluster step fails. Possible values are TERMINATE_CLUSTER,
      CANCEL_AND_WAIT, and CONTINUE. TERMINATE_JOB_FLOW is provided for backward compatibility. We
      recommend using TERMINATE_CLUSTER instead.

    - **HadoopJarStep** *(dict) --* **[REQUIRED]**

      The JAR file used for the step.

      - **Properties** *(list) --*

        A list of Java properties that are set when the step runs. You can use these properties to
        pass key value pairs to your main function.

        - *(dict) --*

          A key value pair.

          - **Key** *(string) --*

            The unique identifier of a key value pair.

          - **Value** *(string) --*

            The value part of the identified key.

      - **Jar** *(string) --* **[REQUIRED]**

        A path to a JAR file run during the step.

      - **MainClass** *(string) --*

        The name of the main class in the specified Java file. If not specified, the JAR file
        should specify a Main-Class in its manifest file.

      - **Args** *(list) --*

        A list of command line arguments passed to the JAR file's main function when executed.

        - *(string) --*
    """


_ClientAddTagsTagsTypeDef = TypedDict(
    "_ClientAddTagsTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientAddTagsTagsTypeDef(_ClientAddTagsTagsTypeDef):
    """
    Type definition for `ClientAddTags` `Tags`

    A key/value pair containing user-defined metadata that you can associate with an Amazon EMR
    resource. Tags make it easier to associate clusters in various ways, such as grouping clusters
    to track your Amazon EMR resource allocation costs. For more information, see `Tag Clusters
    <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html>`__ .

    - **Key** *(string) --*

      A user-defined key, which is the minimum required information for a valid tag. For more
      information, see `Tag
      <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html>`__ .

    - **Value** *(string) --*

      A user-defined value, which is optional in a tag. For more information, see `Tag Clusters
      <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html>`__ .
    """


_ClientCancelStepsResponseCancelStepsInfoListTypeDef = TypedDict(
    "_ClientCancelStepsResponseCancelStepsInfoListTypeDef",
    {"StepId": str, "Status": str, "Reason": str},
    total=False,
)


class ClientCancelStepsResponseCancelStepsInfoListTypeDef(
    _ClientCancelStepsResponseCancelStepsInfoListTypeDef
):
    """
    Type definition for `ClientCancelStepsResponse` `CancelStepsInfoList`

    Specification of the status of a CancelSteps request. Available only in Amazon EMR version
    4.8.0 and later, excluding version 5.0.0.

    - **StepId** *(string) --*

      The encrypted StepId of a step.

    - **Status** *(string) --*

      The status of a CancelSteps Request. The value may be SUBMITTED or FAILED.

    - **Reason** *(string) --*

      The reason for the failure if the CancelSteps request fails.
    """


_ClientCancelStepsResponseTypeDef = TypedDict(
    "_ClientCancelStepsResponseTypeDef",
    {"CancelStepsInfoList": List[ClientCancelStepsResponseCancelStepsInfoListTypeDef]},
    total=False,
)


class ClientCancelStepsResponseTypeDef(_ClientCancelStepsResponseTypeDef):
    """
    Type definition for `ClientCancelSteps` `Response`

    The output for the  CancelSteps operation.

    - **CancelStepsInfoList** *(list) --*

      A list of  CancelStepsInfo , which shows the status of specified cancel requests for each
      ``StepID`` specified.

      - *(dict) --*

        Specification of the status of a CancelSteps request. Available only in Amazon EMR version
        4.8.0 and later, excluding version 5.0.0.

        - **StepId** *(string) --*

          The encrypted StepId of a step.

        - **Status** *(string) --*

          The status of a CancelSteps Request. The value may be SUBMITTED or FAILED.

        - **Reason** *(string) --*

          The reason for the failure if the CancelSteps request fails.
    """


_ClientCreateSecurityConfigurationResponseTypeDef = TypedDict(
    "_ClientCreateSecurityConfigurationResponseTypeDef",
    {"Name": str, "CreationDateTime": datetime},
    total=False,
)


class ClientCreateSecurityConfigurationResponseTypeDef(
    _ClientCreateSecurityConfigurationResponseTypeDef
):
    """
    Type definition for `ClientCreateSecurityConfiguration` `Response`

    - **Name** *(string) --*

      The name of the security configuration.

    - **CreationDateTime** *(datetime) --*

      The date and time the security configuration was created.
    """


_ClientDescribeClusterResponseClusterApplicationsTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterApplicationsTypeDef",
    {"Name": str, "Version": str, "Args": List[str], "AdditionalInfo": Dict[str, str]},
    total=False,
)


class ClientDescribeClusterResponseClusterApplicationsTypeDef(
    _ClientDescribeClusterResponseClusterApplicationsTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponseCluster` `Applications`

    With Amazon EMR release version 4.0 and later, the only accepted parameter is the
    application name. To pass arguments to applications, you use configuration
    classifications specified using configuration JSON objects. For more information, see
    `Configuring Applications
    <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

    With earlier Amazon EMR releases, the application is any Amazon or third-party software
    that you can add to the cluster. This structure contains a list of strings that indicates
    the software to use with the cluster and accepts a user argument list. Amazon EMR accepts
    and forwards the argument list to the corresponding installation script as bootstrap
    action argument.

    - **Name** *(string) --*

      The name of the application.

    - **Version** *(string) --*

      The version of the application.

    - **Args** *(list) --*

      Arguments for Amazon EMR to pass to the application.

      - *(string) --*

    - **AdditionalInfo** *(dict) --*

      This option is for advanced users only. This is meta information about third-party
      applications that third-party vendors use for testing purposes.

      - *(string) --*

        - *(string) --*
    """


_ClientDescribeClusterResponseClusterConfigurationsTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterConfigurationsTypeDef",
    {"Classification": str, "Configurations": List[Any], "Properties": Dict[str, str]},
    total=False,
)


class ClientDescribeClusterResponseClusterConfigurationsTypeDef(
    _ClientDescribeClusterResponseClusterConfigurationsTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponseCluster` `Configurations`

    .. note::

      Amazon EMR releases 4.x or later.

    An optional configuration specification to be used when provisioning cluster instances,
    which can include configurations for applications and software bundled with Amazon EMR. A
    configuration consists of a classification, properties, and optional nested
    configurations. A classification refers to an application-specific configuration file.
    Properties are the settings you want to change in that file. For more information, see
    `Configuring Applications
    <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

    - **Classification** *(string) --*

      The classification within a configuration.

    - **Configurations** *(list) --*

      A list of additional configurations to apply within a configuration object.

    - **Properties** *(dict) --*

      A set of properties specified within a configuration classification.

      - *(string) --*

        - *(string) --*
    """


_ClientDescribeClusterResponseClusterEc2InstanceAttributesTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterEc2InstanceAttributesTypeDef",
    {
        "Ec2KeyName": str,
        "Ec2SubnetId": str,
        "RequestedEc2SubnetIds": List[str],
        "Ec2AvailabilityZone": str,
        "RequestedEc2AvailabilityZones": List[str],
        "IamInstanceProfile": str,
        "EmrManagedMasterSecurityGroup": str,
        "EmrManagedSlaveSecurityGroup": str,
        "ServiceAccessSecurityGroup": str,
        "AdditionalMasterSecurityGroups": List[str],
        "AdditionalSlaveSecurityGroups": List[str],
    },
    total=False,
)


class ClientDescribeClusterResponseClusterEc2InstanceAttributesTypeDef(
    _ClientDescribeClusterResponseClusterEc2InstanceAttributesTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponseCluster` `Ec2InstanceAttributes`

    Provides information about the EC2 instances in a cluster grouped by category. For example,
    key name, subnet ID, IAM instance profile, and so on.

    - **Ec2KeyName** *(string) --*

      The name of the Amazon EC2 key pair to use when connecting with SSH into the master node
      as a user named "hadoop".

    - **Ec2SubnetId** *(string) --*

      Set this parameter to the identifier of the Amazon VPC subnet where you want the cluster
      to launch. If you do not specify this value, and your account supports EC2-Classic, the
      cluster launches in EC2-Classic.

    - **RequestedEc2SubnetIds** *(list) --*

      Applies to clusters configured with the instance fleets option. Specifies the unique
      identifier of one or more Amazon EC2 subnets in which to launch EC2 cluster instances.
      Subnets must exist within the same VPC. Amazon EMR chooses the EC2 subnet with the best
      fit from among the list of ``RequestedEc2SubnetIds`` , and then launches all cluster
      instances within that Subnet. If this value is not specified, and the account and Region
      support EC2-Classic networks, the cluster launches instances in the EC2-Classic network
      and uses ``RequestedEc2AvailabilityZones`` instead of this setting. If EC2-Classic is not
      supported, and no Subnet is specified, Amazon EMR chooses the subnet for you.
      ``RequestedEc2SubnetIDs`` and ``RequestedEc2AvailabilityZones`` cannot be specified
      together.

      - *(string) --*

    - **Ec2AvailabilityZone** *(string) --*

      The Availability Zone in which the cluster will run.

    - **RequestedEc2AvailabilityZones** *(list) --*

      Applies to clusters configured with the instance fleets option. Specifies one or more
      Availability Zones in which to launch EC2 cluster instances when the EC2-Classic network
      configuration is supported. Amazon EMR chooses the Availability Zone with the best fit
      from among the list of ``RequestedEc2AvailabilityZones`` , and then launches all cluster
      instances within that Availability Zone. If you do not specify this value, Amazon EMR
      chooses the Availability Zone for you. ``RequestedEc2SubnetIDs`` and
      ``RequestedEc2AvailabilityZones`` cannot be specified together.

      - *(string) --*

    - **IamInstanceProfile** *(string) --*

      The IAM role that was specified when the cluster was launched. The EC2 instances of the
      cluster assume this role.

    - **EmrManagedMasterSecurityGroup** *(string) --*

      The identifier of the Amazon EC2 security group for the master node.

    - **EmrManagedSlaveSecurityGroup** *(string) --*

      The identifier of the Amazon EC2 security group for the core and task nodes.

    - **ServiceAccessSecurityGroup** *(string) --*

      The identifier of the Amazon EC2 security group for the Amazon EMR service to access
      clusters in VPC private subnets.

    - **AdditionalMasterSecurityGroups** *(list) --*

      A list of additional Amazon EC2 security group IDs for the master node.

      - *(string) --*

    - **AdditionalSlaveSecurityGroups** *(list) --*

      A list of additional Amazon EC2 security group IDs for the core and task nodes.

      - *(string) --*
    """


_ClientDescribeClusterResponseClusterKerberosAttributesTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterKerberosAttributesTypeDef",
    {
        "Realm": str,
        "KdcAdminPassword": str,
        "CrossRealmTrustPrincipalPassword": str,
        "ADDomainJoinUser": str,
        "ADDomainJoinPassword": str,
    },
    total=False,
)


class ClientDescribeClusterResponseClusterKerberosAttributesTypeDef(
    _ClientDescribeClusterResponseClusterKerberosAttributesTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponseCluster` `KerberosAttributes`

    Attributes for Kerberos configuration when Kerberos authentication is enabled using a
    security configuration. For more information see `Use Kerberos Authentication
    <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-kerberos.html>`__ in the *EMR
    Management Guide* .

    - **Realm** *(string) --*

      The name of the Kerberos realm to which all nodes in a cluster belong. For example,
      ``EC2.INTERNAL`` .

    - **KdcAdminPassword** *(string) --*

      The password used within the cluster for the kadmin service on the cluster-dedicated KDC,
      which maintains Kerberos principals, password policies, and keytabs for the cluster.

    - **CrossRealmTrustPrincipalPassword** *(string) --*

      Required only when establishing a cross-realm trust with a KDC in a different realm. The
      cross-realm principal password, which must be identical across realms.

    - **ADDomainJoinUser** *(string) --*

      Required only when establishing a cross-realm trust with an Active Directory domain. A
      user with sufficient privileges to join resources to the domain.

    - **ADDomainJoinPassword** *(string) --*

      The Active Directory password for ``ADDomainJoinUser`` .
    """


_ClientDescribeClusterResponseClusterStatusStateChangeReasonTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterStatusStateChangeReasonTypeDef",
    {"Code": str, "Message": str},
    total=False,
)


class ClientDescribeClusterResponseClusterStatusStateChangeReasonTypeDef(
    _ClientDescribeClusterResponseClusterStatusStateChangeReasonTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponseClusterStatus` `StateChangeReason`

    The reason for the cluster status change.

    - **Code** *(string) --*

      The programmatic code for the state change reason.

    - **Message** *(string) --*

      The descriptive message for the state change reason.
    """


_ClientDescribeClusterResponseClusterStatusTimelineTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterStatusTimelineTypeDef",
    {"CreationDateTime": datetime, "ReadyDateTime": datetime, "EndDateTime": datetime},
    total=False,
)


class ClientDescribeClusterResponseClusterStatusTimelineTypeDef(
    _ClientDescribeClusterResponseClusterStatusTimelineTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponseClusterStatus` `Timeline`

    A timeline that represents the status of a cluster over the lifetime of the cluster.

    - **CreationDateTime** *(datetime) --*

      The creation date and time of the cluster.

    - **ReadyDateTime** *(datetime) --*

      The date and time when the cluster was ready to execute steps.

    - **EndDateTime** *(datetime) --*

      The date and time when the cluster was terminated.
    """


_ClientDescribeClusterResponseClusterStatusTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterStatusTypeDef",
    {
        "State": str,
        "StateChangeReason": ClientDescribeClusterResponseClusterStatusStateChangeReasonTypeDef,
        "Timeline": ClientDescribeClusterResponseClusterStatusTimelineTypeDef,
    },
    total=False,
)


class ClientDescribeClusterResponseClusterStatusTypeDef(
    _ClientDescribeClusterResponseClusterStatusTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponseCluster` `Status`

    The current status details about the cluster.

    - **State** *(string) --*

      The current state of the cluster.

    - **StateChangeReason** *(dict) --*

      The reason for the cluster status change.

      - **Code** *(string) --*

        The programmatic code for the state change reason.

      - **Message** *(string) --*

        The descriptive message for the state change reason.

    - **Timeline** *(dict) --*

      A timeline that represents the status of a cluster over the lifetime of the cluster.

      - **CreationDateTime** *(datetime) --*

        The creation date and time of the cluster.

      - **ReadyDateTime** *(datetime) --*

        The date and time when the cluster was ready to execute steps.

      - **EndDateTime** *(datetime) --*

        The date and time when the cluster was terminated.
    """


_ClientDescribeClusterResponseClusterTagsTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeClusterResponseClusterTagsTypeDef(
    _ClientDescribeClusterResponseClusterTagsTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponseCluster` `Tags`

    A key/value pair containing user-defined metadata that you can associate with an Amazon
    EMR resource. Tags make it easier to associate clusters in various ways, such as grouping
    clusters to track your Amazon EMR resource allocation costs. For more information, see
    `Tag Clusters
    <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html>`__ .

    - **Key** *(string) --*

      A user-defined key, which is the minimum required information for a valid tag. For more
      information, see `Tag
      <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html>`__ .

    - **Value** *(string) --*

      A user-defined value, which is optional in a tag. For more information, see `Tag
      Clusters <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html>`__
      .
    """


_ClientDescribeClusterResponseClusterTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": ClientDescribeClusterResponseClusterStatusTypeDef,
        "Ec2InstanceAttributes": ClientDescribeClusterResponseClusterEc2InstanceAttributesTypeDef,
        "InstanceCollectionType": str,
        "LogUri": str,
        "RequestedAmiVersion": str,
        "RunningAmiVersion": str,
        "ReleaseLabel": str,
        "AutoTerminate": bool,
        "TerminationProtected": bool,
        "VisibleToAllUsers": bool,
        "Applications": List[ClientDescribeClusterResponseClusterApplicationsTypeDef],
        "Tags": List[ClientDescribeClusterResponseClusterTagsTypeDef],
        "ServiceRole": str,
        "NormalizedInstanceHours": int,
        "MasterPublicDnsName": str,
        "Configurations": List[
            ClientDescribeClusterResponseClusterConfigurationsTypeDef
        ],
        "SecurityConfiguration": str,
        "AutoScalingRole": str,
        "ScaleDownBehavior": str,
        "CustomAmiId": str,
        "EbsRootVolumeSize": int,
        "RepoUpgradeOnBoot": str,
        "KerberosAttributes": ClientDescribeClusterResponseClusterKerberosAttributesTypeDef,
        "ClusterArn": str,
    },
    total=False,
)


class ClientDescribeClusterResponseClusterTypeDef(
    _ClientDescribeClusterResponseClusterTypeDef
):
    """
    Type definition for `ClientDescribeClusterResponse` `Cluster`

    This output contains the details for the requested cluster.

    - **Id** *(string) --*

      The unique identifier for the cluster.

    - **Name** *(string) --*

      The name of the cluster.

    - **Status** *(dict) --*

      The current status details about the cluster.

      - **State** *(string) --*

        The current state of the cluster.

      - **StateChangeReason** *(dict) --*

        The reason for the cluster status change.

        - **Code** *(string) --*

          The programmatic code for the state change reason.

        - **Message** *(string) --*

          The descriptive message for the state change reason.

      - **Timeline** *(dict) --*

        A timeline that represents the status of a cluster over the lifetime of the cluster.

        - **CreationDateTime** *(datetime) --*

          The creation date and time of the cluster.

        - **ReadyDateTime** *(datetime) --*

          The date and time when the cluster was ready to execute steps.

        - **EndDateTime** *(datetime) --*

          The date and time when the cluster was terminated.

    - **Ec2InstanceAttributes** *(dict) --*

      Provides information about the EC2 instances in a cluster grouped by category. For example,
      key name, subnet ID, IAM instance profile, and so on.

      - **Ec2KeyName** *(string) --*

        The name of the Amazon EC2 key pair to use when connecting with SSH into the master node
        as a user named "hadoop".

      - **Ec2SubnetId** *(string) --*

        Set this parameter to the identifier of the Amazon VPC subnet where you want the cluster
        to launch. If you do not specify this value, and your account supports EC2-Classic, the
        cluster launches in EC2-Classic.

      - **RequestedEc2SubnetIds** *(list) --*

        Applies to clusters configured with the instance fleets option. Specifies the unique
        identifier of one or more Amazon EC2 subnets in which to launch EC2 cluster instances.
        Subnets must exist within the same VPC. Amazon EMR chooses the EC2 subnet with the best
        fit from among the list of ``RequestedEc2SubnetIds`` , and then launches all cluster
        instances within that Subnet. If this value is not specified, and the account and Region
        support EC2-Classic networks, the cluster launches instances in the EC2-Classic network
        and uses ``RequestedEc2AvailabilityZones`` instead of this setting. If EC2-Classic is not
        supported, and no Subnet is specified, Amazon EMR chooses the subnet for you.
        ``RequestedEc2SubnetIDs`` and ``RequestedEc2AvailabilityZones`` cannot be specified
        together.

        - *(string) --*

      - **Ec2AvailabilityZone** *(string) --*

        The Availability Zone in which the cluster will run.

      - **RequestedEc2AvailabilityZones** *(list) --*

        Applies to clusters configured with the instance fleets option. Specifies one or more
        Availability Zones in which to launch EC2 cluster instances when the EC2-Classic network
        configuration is supported. Amazon EMR chooses the Availability Zone with the best fit
        from among the list of ``RequestedEc2AvailabilityZones`` , and then launches all cluster
        instances within that Availability Zone. If you do not specify this value, Amazon EMR
        chooses the Availability Zone for you. ``RequestedEc2SubnetIDs`` and
        ``RequestedEc2AvailabilityZones`` cannot be specified together.

        - *(string) --*

      - **IamInstanceProfile** *(string) --*

        The IAM role that was specified when the cluster was launched. The EC2 instances of the
        cluster assume this role.

      - **EmrManagedMasterSecurityGroup** *(string) --*

        The identifier of the Amazon EC2 security group for the master node.

      - **EmrManagedSlaveSecurityGroup** *(string) --*

        The identifier of the Amazon EC2 security group for the core and task nodes.

      - **ServiceAccessSecurityGroup** *(string) --*

        The identifier of the Amazon EC2 security group for the Amazon EMR service to access
        clusters in VPC private subnets.

      - **AdditionalMasterSecurityGroups** *(list) --*

        A list of additional Amazon EC2 security group IDs for the master node.

        - *(string) --*

      - **AdditionalSlaveSecurityGroups** *(list) --*

        A list of additional Amazon EC2 security group IDs for the core and task nodes.

        - *(string) --*

    - **InstanceCollectionType** *(string) --*

      .. note::

        The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and
        later, excluding 5.0.x versions.

      The instance group configuration of the cluster. A value of ``INSTANCE_GROUP`` indicates a
      uniform instance group configuration. A value of ``INSTANCE_FLEET`` indicates an instance
      fleets configuration.

    - **LogUri** *(string) --*

      The path to the Amazon S3 location where logs for this cluster are stored.

    - **RequestedAmiVersion** *(string) --*

      The AMI version requested for this cluster.

    - **RunningAmiVersion** *(string) --*

      The AMI version running on this cluster.

    - **ReleaseLabel** *(string) --*

      The Amazon EMR release label, which determines the version of open-source application
      packages installed on the cluster. Release labels are in the form ``emr-x.x.x`` , where
      x.x.x is an Amazon EMR release version such as ``emr-5.14.0`` . For more information about
      Amazon EMR release versions and included application versions and features, see
      `https\\://docs.aws.amazon.com/emr/latest/ReleaseGuide/
      <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/>`__ . The release label applies only
      to Amazon EMR releases version 4.0 and later. Earlier versions use ``AmiVersion`` .

    - **AutoTerminate** *(boolean) --*

      Specifies whether the cluster should terminate after completing all steps.

    - **TerminationProtected** *(boolean) --*

      Indicates whether Amazon EMR will lock the cluster to prevent the EC2 instances from being
      terminated by an API call or user intervention, or in the event of a cluster error.

    - **VisibleToAllUsers** *(boolean) --*

      Indicates whether the cluster is visible to all IAM users of the AWS account associated
      with the cluster. The default value, ``true`` , indicates that all IAM users in the AWS
      account can perform cluster actions if they have the proper IAM policy permissions. If this
      value is ``false`` , only the IAM user that created the cluster can perform actions. This
      value can be changed on a running cluster by using the  SetVisibleToAllUsers action. You
      can override the default value of ``true`` when you create a cluster by using the
      ``VisibleToAllUsers`` parameter of the ``RunJobFlow`` action.

    - **Applications** *(list) --*

      The applications installed on this cluster.

      - *(dict) --*

        With Amazon EMR release version 4.0 and later, the only accepted parameter is the
        application name. To pass arguments to applications, you use configuration
        classifications specified using configuration JSON objects. For more information, see
        `Configuring Applications
        <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

        With earlier Amazon EMR releases, the application is any Amazon or third-party software
        that you can add to the cluster. This structure contains a list of strings that indicates
        the software to use with the cluster and accepts a user argument list. Amazon EMR accepts
        and forwards the argument list to the corresponding installation script as bootstrap
        action argument.

        - **Name** *(string) --*

          The name of the application.

        - **Version** *(string) --*

          The version of the application.

        - **Args** *(list) --*

          Arguments for Amazon EMR to pass to the application.

          - *(string) --*

        - **AdditionalInfo** *(dict) --*

          This option is for advanced users only. This is meta information about third-party
          applications that third-party vendors use for testing purposes.

          - *(string) --*

            - *(string) --*

    - **Tags** *(list) --*

      A list of tags associated with a cluster.

      - *(dict) --*

        A key/value pair containing user-defined metadata that you can associate with an Amazon
        EMR resource. Tags make it easier to associate clusters in various ways, such as grouping
        clusters to track your Amazon EMR resource allocation costs. For more information, see
        `Tag Clusters
        <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html>`__ .

        - **Key** *(string) --*

          A user-defined key, which is the minimum required information for a valid tag. For more
          information, see `Tag
          <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html>`__ .

        - **Value** *(string) --*

          A user-defined value, which is optional in a tag. For more information, see `Tag
          Clusters <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html>`__
          .

    - **ServiceRole** *(string) --*

      The IAM role that will be assumed by the Amazon EMR service to access AWS resources on your
      behalf.

    - **NormalizedInstanceHours** *(integer) --*

      An approximation of the cost of the cluster, represented in m1.small/hours. This value is
      incremented one time for every hour an m1.small instance runs. Larger instances are
      weighted more, so an EC2 instance that is roughly four times more expensive would result in
      the normalized instance hours being incremented by four. This result is only an
      approximation and does not reflect the actual billing rate.

    - **MasterPublicDnsName** *(string) --*

      The DNS name of the master node. If the cluster is on a private subnet, this is the private
      DNS name. On a public subnet, this is the public DNS name.

    - **Configurations** *(list) --*

      Applies only to Amazon EMR releases 4.x and later. The list of Configurations supplied to
      the EMR cluster.

      - *(dict) --*

        .. note::

          Amazon EMR releases 4.x or later.

        An optional configuration specification to be used when provisioning cluster instances,
        which can include configurations for applications and software bundled with Amazon EMR. A
        configuration consists of a classification, properties, and optional nested
        configurations. A classification refers to an application-specific configuration file.
        Properties are the settings you want to change in that file. For more information, see
        `Configuring Applications
        <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

        - **Classification** *(string) --*

          The classification within a configuration.

        - **Configurations** *(list) --*

          A list of additional configurations to apply within a configuration object.

        - **Properties** *(dict) --*

          A set of properties specified within a configuration classification.

          - *(string) --*

            - *(string) --*

    - **SecurityConfiguration** *(string) --*

      The name of the security configuration applied to the cluster.

    - **AutoScalingRole** *(string) --*

      An IAM role for automatic scaling policies. The default role is
      ``EMR_AutoScaling_DefaultRole`` . The IAM role provides permissions that the automatic
      scaling feature requires to launch and terminate EC2 instances in an instance group.

    - **ScaleDownBehavior** *(string) --*

      The way that individual Amazon EC2 instances terminate when an automatic scale-in activity
      occurs or an instance group is resized. ``TERMINATE_AT_INSTANCE_HOUR`` indicates that
      Amazon EMR terminates nodes at the instance-hour boundary, regardless of when the request
      to terminate the instance was submitted. This option is only available with Amazon EMR
      5.1.0 and later and is the default for clusters created using that version.
      ``TERMINATE_AT_TASK_COMPLETION`` indicates that Amazon EMR blacklists and drains tasks from
      nodes before terminating the Amazon EC2 instances, regardless of the instance-hour
      boundary. With either behavior, Amazon EMR removes the least active nodes first and blocks
      instance termination if it could lead to HDFS corruption. ``TERMINATE_AT_TASK_COMPLETION``
      is available only in Amazon EMR version 4.1.0 and later, and is the default for versions of
      Amazon EMR earlier than 5.1.0.

    - **CustomAmiId** *(string) --*

      Available only in Amazon EMR version 5.7.0 and later. The ID of a custom Amazon EBS-backed
      Linux AMI if the cluster uses a custom AMI.

    - **EbsRootVolumeSize** *(integer) --*

      The size, in GiB, of the EBS root device volume of the Linux AMI that is used for each EC2
      instance. Available in Amazon EMR version 4.x and later.

    - **RepoUpgradeOnBoot** *(string) --*

      Applies only when ``CustomAmiID`` is used. Specifies the type of updates that are applied
      from the Amazon Linux AMI package repositories when an instance boots using the AMI.

    - **KerberosAttributes** *(dict) --*

      Attributes for Kerberos configuration when Kerberos authentication is enabled using a
      security configuration. For more information see `Use Kerberos Authentication
      <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-kerberos.html>`__ in the *EMR
      Management Guide* .

      - **Realm** *(string) --*

        The name of the Kerberos realm to which all nodes in a cluster belong. For example,
        ``EC2.INTERNAL`` .

      - **KdcAdminPassword** *(string) --*

        The password used within the cluster for the kadmin service on the cluster-dedicated KDC,
        which maintains Kerberos principals, password policies, and keytabs for the cluster.

      - **CrossRealmTrustPrincipalPassword** *(string) --*

        Required only when establishing a cross-realm trust with a KDC in a different realm. The
        cross-realm principal password, which must be identical across realms.

      - **ADDomainJoinUser** *(string) --*

        Required only when establishing a cross-realm trust with an Active Directory domain. A
        user with sufficient privileges to join resources to the domain.

      - **ADDomainJoinPassword** *(string) --*

        The Active Directory password for ``ADDomainJoinUser`` .

    - **ClusterArn** *(string) --*

      The Amazon Resource Name of the cluster.
    """


_ClientDescribeClusterResponseTypeDef = TypedDict(
    "_ClientDescribeClusterResponseTypeDef",
    {"Cluster": ClientDescribeClusterResponseClusterTypeDef},
    total=False,
)


class ClientDescribeClusterResponseTypeDef(_ClientDescribeClusterResponseTypeDef):
    """
    Type definition for `ClientDescribeCluster` `Response`

    This output contains the description of the cluster.

    - **Cluster** *(dict) --*

      This output contains the details for the requested cluster.

      - **Id** *(string) --*

        The unique identifier for the cluster.

      - **Name** *(string) --*

        The name of the cluster.

      - **Status** *(dict) --*

        The current status details about the cluster.

        - **State** *(string) --*

          The current state of the cluster.

        - **StateChangeReason** *(dict) --*

          The reason for the cluster status change.

          - **Code** *(string) --*

            The programmatic code for the state change reason.

          - **Message** *(string) --*

            The descriptive message for the state change reason.

        - **Timeline** *(dict) --*

          A timeline that represents the status of a cluster over the lifetime of the cluster.

          - **CreationDateTime** *(datetime) --*

            The creation date and time of the cluster.

          - **ReadyDateTime** *(datetime) --*

            The date and time when the cluster was ready to execute steps.

          - **EndDateTime** *(datetime) --*

            The date and time when the cluster was terminated.

      - **Ec2InstanceAttributes** *(dict) --*

        Provides information about the EC2 instances in a cluster grouped by category. For example,
        key name, subnet ID, IAM instance profile, and so on.

        - **Ec2KeyName** *(string) --*

          The name of the Amazon EC2 key pair to use when connecting with SSH into the master node
          as a user named "hadoop".

        - **Ec2SubnetId** *(string) --*

          Set this parameter to the identifier of the Amazon VPC subnet where you want the cluster
          to launch. If you do not specify this value, and your account supports EC2-Classic, the
          cluster launches in EC2-Classic.

        - **RequestedEc2SubnetIds** *(list) --*

          Applies to clusters configured with the instance fleets option. Specifies the unique
          identifier of one or more Amazon EC2 subnets in which to launch EC2 cluster instances.
          Subnets must exist within the same VPC. Amazon EMR chooses the EC2 subnet with the best
          fit from among the list of ``RequestedEc2SubnetIds`` , and then launches all cluster
          instances within that Subnet. If this value is not specified, and the account and Region
          support EC2-Classic networks, the cluster launches instances in the EC2-Classic network
          and uses ``RequestedEc2AvailabilityZones`` instead of this setting. If EC2-Classic is not
          supported, and no Subnet is specified, Amazon EMR chooses the subnet for you.
          ``RequestedEc2SubnetIDs`` and ``RequestedEc2AvailabilityZones`` cannot be specified
          together.

          - *(string) --*

        - **Ec2AvailabilityZone** *(string) --*

          The Availability Zone in which the cluster will run.

        - **RequestedEc2AvailabilityZones** *(list) --*

          Applies to clusters configured with the instance fleets option. Specifies one or more
          Availability Zones in which to launch EC2 cluster instances when the EC2-Classic network
          configuration is supported. Amazon EMR chooses the Availability Zone with the best fit
          from among the list of ``RequestedEc2AvailabilityZones`` , and then launches all cluster
          instances within that Availability Zone. If you do not specify this value, Amazon EMR
          chooses the Availability Zone for you. ``RequestedEc2SubnetIDs`` and
          ``RequestedEc2AvailabilityZones`` cannot be specified together.

          - *(string) --*

        - **IamInstanceProfile** *(string) --*

          The IAM role that was specified when the cluster was launched. The EC2 instances of the
          cluster assume this role.

        - **EmrManagedMasterSecurityGroup** *(string) --*

          The identifier of the Amazon EC2 security group for the master node.

        - **EmrManagedSlaveSecurityGroup** *(string) --*

          The identifier of the Amazon EC2 security group for the core and task nodes.

        - **ServiceAccessSecurityGroup** *(string) --*

          The identifier of the Amazon EC2 security group for the Amazon EMR service to access
          clusters in VPC private subnets.

        - **AdditionalMasterSecurityGroups** *(list) --*

          A list of additional Amazon EC2 security group IDs for the master node.

          - *(string) --*

        - **AdditionalSlaveSecurityGroups** *(list) --*

          A list of additional Amazon EC2 security group IDs for the core and task nodes.

          - *(string) --*

      - **InstanceCollectionType** *(string) --*

        .. note::

          The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and
          later, excluding 5.0.x versions.

        The instance group configuration of the cluster. A value of ``INSTANCE_GROUP`` indicates a
        uniform instance group configuration. A value of ``INSTANCE_FLEET`` indicates an instance
        fleets configuration.

      - **LogUri** *(string) --*

        The path to the Amazon S3 location where logs for this cluster are stored.

      - **RequestedAmiVersion** *(string) --*

        The AMI version requested for this cluster.

      - **RunningAmiVersion** *(string) --*

        The AMI version running on this cluster.

      - **ReleaseLabel** *(string) --*

        The Amazon EMR release label, which determines the version of open-source application
        packages installed on the cluster. Release labels are in the form ``emr-x.x.x`` , where
        x.x.x is an Amazon EMR release version such as ``emr-5.14.0`` . For more information about
        Amazon EMR release versions and included application versions and features, see
        `https\\://docs.aws.amazon.com/emr/latest/ReleaseGuide/
        <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/>`__ . The release label applies only
        to Amazon EMR releases version 4.0 and later. Earlier versions use ``AmiVersion`` .

      - **AutoTerminate** *(boolean) --*

        Specifies whether the cluster should terminate after completing all steps.

      - **TerminationProtected** *(boolean) --*

        Indicates whether Amazon EMR will lock the cluster to prevent the EC2 instances from being
        terminated by an API call or user intervention, or in the event of a cluster error.

      - **VisibleToAllUsers** *(boolean) --*

        Indicates whether the cluster is visible to all IAM users of the AWS account associated
        with the cluster. The default value, ``true`` , indicates that all IAM users in the AWS
        account can perform cluster actions if they have the proper IAM policy permissions. If this
        value is ``false`` , only the IAM user that created the cluster can perform actions. This
        value can be changed on a running cluster by using the  SetVisibleToAllUsers action. You
        can override the default value of ``true`` when you create a cluster by using the
        ``VisibleToAllUsers`` parameter of the ``RunJobFlow`` action.

      - **Applications** *(list) --*

        The applications installed on this cluster.

        - *(dict) --*

          With Amazon EMR release version 4.0 and later, the only accepted parameter is the
          application name. To pass arguments to applications, you use configuration
          classifications specified using configuration JSON objects. For more information, see
          `Configuring Applications
          <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

          With earlier Amazon EMR releases, the application is any Amazon or third-party software
          that you can add to the cluster. This structure contains a list of strings that indicates
          the software to use with the cluster and accepts a user argument list. Amazon EMR accepts
          and forwards the argument list to the corresponding installation script as bootstrap
          action argument.

          - **Name** *(string) --*

            The name of the application.

          - **Version** *(string) --*

            The version of the application.

          - **Args** *(list) --*

            Arguments for Amazon EMR to pass to the application.

            - *(string) --*

          - **AdditionalInfo** *(dict) --*

            This option is for advanced users only. This is meta information about third-party
            applications that third-party vendors use for testing purposes.

            - *(string) --*

              - *(string) --*

      - **Tags** *(list) --*

        A list of tags associated with a cluster.

        - *(dict) --*

          A key/value pair containing user-defined metadata that you can associate with an Amazon
          EMR resource. Tags make it easier to associate clusters in various ways, such as grouping
          clusters to track your Amazon EMR resource allocation costs. For more information, see
          `Tag Clusters
          <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html>`__ .

          - **Key** *(string) --*

            A user-defined key, which is the minimum required information for a valid tag. For more
            information, see `Tag
            <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html>`__ .

          - **Value** *(string) --*

            A user-defined value, which is optional in a tag. For more information, see `Tag
            Clusters <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html>`__
            .

      - **ServiceRole** *(string) --*

        The IAM role that will be assumed by the Amazon EMR service to access AWS resources on your
        behalf.

      - **NormalizedInstanceHours** *(integer) --*

        An approximation of the cost of the cluster, represented in m1.small/hours. This value is
        incremented one time for every hour an m1.small instance runs. Larger instances are
        weighted more, so an EC2 instance that is roughly four times more expensive would result in
        the normalized instance hours being incremented by four. This result is only an
        approximation and does not reflect the actual billing rate.

      - **MasterPublicDnsName** *(string) --*

        The DNS name of the master node. If the cluster is on a private subnet, this is the private
        DNS name. On a public subnet, this is the public DNS name.

      - **Configurations** *(list) --*

        Applies only to Amazon EMR releases 4.x and later. The list of Configurations supplied to
        the EMR cluster.

        - *(dict) --*

          .. note::

            Amazon EMR releases 4.x or later.

          An optional configuration specification to be used when provisioning cluster instances,
          which can include configurations for applications and software bundled with Amazon EMR. A
          configuration consists of a classification, properties, and optional nested
          configurations. A classification refers to an application-specific configuration file.
          Properties are the settings you want to change in that file. For more information, see
          `Configuring Applications
          <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

          - **Classification** *(string) --*

            The classification within a configuration.

          - **Configurations** *(list) --*

            A list of additional configurations to apply within a configuration object.

          - **Properties** *(dict) --*

            A set of properties specified within a configuration classification.

            - *(string) --*

              - *(string) --*

      - **SecurityConfiguration** *(string) --*

        The name of the security configuration applied to the cluster.

      - **AutoScalingRole** *(string) --*

        An IAM role for automatic scaling policies. The default role is
        ``EMR_AutoScaling_DefaultRole`` . The IAM role provides permissions that the automatic
        scaling feature requires to launch and terminate EC2 instances in an instance group.

      - **ScaleDownBehavior** *(string) --*

        The way that individual Amazon EC2 instances terminate when an automatic scale-in activity
        occurs or an instance group is resized. ``TERMINATE_AT_INSTANCE_HOUR`` indicates that
        Amazon EMR terminates nodes at the instance-hour boundary, regardless of when the request
        to terminate the instance was submitted. This option is only available with Amazon EMR
        5.1.0 and later and is the default for clusters created using that version.
        ``TERMINATE_AT_TASK_COMPLETION`` indicates that Amazon EMR blacklists and drains tasks from
        nodes before terminating the Amazon EC2 instances, regardless of the instance-hour
        boundary. With either behavior, Amazon EMR removes the least active nodes first and blocks
        instance termination if it could lead to HDFS corruption. ``TERMINATE_AT_TASK_COMPLETION``
        is available only in Amazon EMR version 4.1.0 and later, and is the default for versions of
        Amazon EMR earlier than 5.1.0.

      - **CustomAmiId** *(string) --*

        Available only in Amazon EMR version 5.7.0 and later. The ID of a custom Amazon EBS-backed
        Linux AMI if the cluster uses a custom AMI.

      - **EbsRootVolumeSize** *(integer) --*

        The size, in GiB, of the EBS root device volume of the Linux AMI that is used for each EC2
        instance. Available in Amazon EMR version 4.x and later.

      - **RepoUpgradeOnBoot** *(string) --*

        Applies only when ``CustomAmiID`` is used. Specifies the type of updates that are applied
        from the Amazon Linux AMI package repositories when an instance boots using the AMI.

      - **KerberosAttributes** *(dict) --*

        Attributes for Kerberos configuration when Kerberos authentication is enabled using a
        security configuration. For more information see `Use Kerberos Authentication
        <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-kerberos.html>`__ in the *EMR
        Management Guide* .

        - **Realm** *(string) --*

          The name of the Kerberos realm to which all nodes in a cluster belong. For example,
          ``EC2.INTERNAL`` .

        - **KdcAdminPassword** *(string) --*

          The password used within the cluster for the kadmin service on the cluster-dedicated KDC,
          which maintains Kerberos principals, password policies, and keytabs for the cluster.

        - **CrossRealmTrustPrincipalPassword** *(string) --*

          Required only when establishing a cross-realm trust with a KDC in a different realm. The
          cross-realm principal password, which must be identical across realms.

        - **ADDomainJoinUser** *(string) --*

          Required only when establishing a cross-realm trust with an Active Directory domain. A
          user with sufficient privileges to join resources to the domain.

        - **ADDomainJoinPassword** *(string) --*

          The Active Directory password for ``ADDomainJoinUser`` .

      - **ClusterArn** *(string) --*

        The Amazon Resource Name of the cluster.
    """


_ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsBootstrapActionConfigScriptBootstrapActionTypeDef = TypedDict(
    "_ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsBootstrapActionConfigScriptBootstrapActionTypeDef",
    {"Path": str, "Args": List[str]},
    total=False,
)


class ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsBootstrapActionConfigScriptBootstrapActionTypeDef(
    _ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsBootstrapActionConfigScriptBootstrapActionTypeDef
):
    """
    Type definition for `ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsBootstrapActionConfig` `ScriptBootstrapAction`

    The script run by the bootstrap action.

    - **Path** *(string) --*

      Location of the script to run during a bootstrap action. Can be either a location
      in Amazon S3 or on a local file system.

    - **Args** *(list) --*

      A list of command line arguments to pass to the bootstrap action script.

      - *(string) --*
    """


_ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsBootstrapActionConfigTypeDef = TypedDict(
    "_ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsBootstrapActionConfigTypeDef",
    {
        "Name": str,
        "ScriptBootstrapAction": ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsBootstrapActionConfigScriptBootstrapActionTypeDef,
    },
    total=False,
)


class ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsBootstrapActionConfigTypeDef(
    _ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsBootstrapActionConfigTypeDef
):
    """
    Type definition for `ClientDescribeJobFlowsResponseJobFlowsBootstrapActions` `BootstrapActionConfig`

    A description of the bootstrap action.

    - **Name** *(string) --*

      The name of the bootstrap action.

    - **ScriptBootstrapAction** *(dict) --*

      The script run by the bootstrap action.

      - **Path** *(string) --*

        Location of the script to run during a bootstrap action. Can be either a location
        in Amazon S3 or on a local file system.

      - **Args** *(list) --*

        A list of command line arguments to pass to the bootstrap action script.

        - *(string) --*
    """


_ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsTypeDef = TypedDict(
    "_ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsTypeDef",
    {
        "BootstrapActionConfig": ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsBootstrapActionConfigTypeDef
    },
    total=False,
)


class ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsTypeDef(
    _ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsTypeDef
):
    """
    Type definition for `ClientDescribeJobFlowsResponseJobFlows` `BootstrapActions`

    Reports the configuration of a bootstrap action in a cluster (job flow).

    - **BootstrapActionConfig** *(dict) --*

      A description of the bootstrap action.

      - **Name** *(string) --*

        The name of the bootstrap action.

      - **ScriptBootstrapAction** *(dict) --*

        The script run by the bootstrap action.

        - **Path** *(string) --*

          Location of the script to run during a bootstrap action. Can be either a location
          in Amazon S3 or on a local file system.

        - **Args** *(list) --*

          A list of command line arguments to pass to the bootstrap action script.

          - *(string) --*
    """


_ClientDescribeJobFlowsResponseJobFlowsExecutionStatusDetailTypeDef = TypedDict(
    "_ClientDescribeJobFlowsResponseJobFlowsExecutionStatusDetailTypeDef",
    {
        "State": str,
        "CreationDateTime": datetime,
        "StartDateTime": datetime,
        "ReadyDateTime": datetime,
        "EndDateTime": datetime,
        "LastStateChangeReason": str,
    },
    total=False,
)


class ClientDescribeJobFlowsResponseJobFlowsExecutionStatusDetailTypeDef(
    _ClientDescribeJobFlowsResponseJobFlowsExecutionStatusDetailTypeDef
):
    """
    Type definition for `ClientDescribeJobFlowsResponseJobFlows` `ExecutionStatusDetail`

    Describes the execution status of the job flow.

    - **State** *(string) --*

      The state of the job flow.

    - **CreationDateTime** *(datetime) --*

      The creation date and time of the job flow.

    - **StartDateTime** *(datetime) --*

      The start date and time of the job flow.

    - **ReadyDateTime** *(datetime) --*

      The date and time when the job flow was ready to start running bootstrap actions.

    - **EndDateTime** *(datetime) --*

      The completion date and time of the job flow.

    - **LastStateChangeReason** *(string) --*

      Description of the job flow last changed state.
    """


_ClientDescribeJobFlowsResponseJobFlowsInstancesInstanceGroupsTypeDef = TypedDict(
    "_ClientDescribeJobFlowsResponseJobFlowsInstancesInstanceGroupsTypeDef",
    {
        "InstanceGroupId": str,
        "Name": str,
        "Market": str,
        "InstanceRole": str,
        "BidPrice": str,
        "InstanceType": str,
        "InstanceRequestCount": int,
        "InstanceRunningCount": int,
        "State": str,
        "LastStateChangeReason": str,
        "CreationDateTime": datetime,
        "StartDateTime": datetime,
        "ReadyDateTime": datetime,
        "EndDateTime": datetime,
    },
    total=False,
)


class ClientDescribeJobFlowsResponseJobFlowsInstancesInstanceGroupsTypeDef(
    _ClientDescribeJobFlowsResponseJobFlowsInstancesInstanceGroupsTypeDef
):
    """
    Type definition for `ClientDescribeJobFlowsResponseJobFlowsInstances` `InstanceGroups`

    Detailed information about an instance group.

    - **InstanceGroupId** *(string) --*

      Unique identifier for the instance group.

    - **Name** *(string) --*

      Friendly name for the instance group.

    - **Market** *(string) --*

      Market type of the EC2 instances used to create a cluster node.

    - **InstanceRole** *(string) --*

      Instance group role in the cluster

    - **BidPrice** *(string) --*

      The bid price for each EC2 Spot instance type as defined by ``InstanceType`` .
      Expressed in USD. If neither ``BidPrice`` nor
      ``BidPriceAsPercentageOfOnDemandPrice`` is provided,
      ``BidPriceAsPercentageOfOnDemandPrice`` defaults to 100%.

    - **InstanceType** *(string) --*

      EC2 instance type.

    - **InstanceRequestCount** *(integer) --*

      Target number of instances to run in the instance group.

    - **InstanceRunningCount** *(integer) --*

      Actual count of running instances.

    - **State** *(string) --*

      State of instance group. The following values are deprecated: STARTING, TERMINATED,
      and FAILED.

    - **LastStateChangeReason** *(string) --*

      Details regarding the state of the instance group.

    - **CreationDateTime** *(datetime) --*

      The date/time the instance group was created.

    - **StartDateTime** *(datetime) --*

      The date/time the instance group was started.

    - **ReadyDateTime** *(datetime) --*

      The date/time the instance group was available to the cluster.

    - **EndDateTime** *(datetime) --*

      The date/time the instance group was terminated.
    """


_ClientDescribeJobFlowsResponseJobFlowsInstancesPlacementTypeDef = TypedDict(
    "_ClientDescribeJobFlowsResponseJobFlowsInstancesPlacementTypeDef",
    {"AvailabilityZone": str, "AvailabilityZones": List[str]},
    total=False,
)


class ClientDescribeJobFlowsResponseJobFlowsInstancesPlacementTypeDef(
    _ClientDescribeJobFlowsResponseJobFlowsInstancesPlacementTypeDef
):
    """
    Type definition for `ClientDescribeJobFlowsResponseJobFlowsInstances` `Placement`

    The Amazon EC2 Availability Zone for the cluster.

    - **AvailabilityZone** *(string) --*

      The Amazon EC2 Availability Zone for the cluster. ``AvailabilityZone`` is used for
      uniform instance groups, while ``AvailabilityZones`` (plural) is used for instance
      fleets.

    - **AvailabilityZones** *(list) --*

      When multiple Availability Zones are specified, Amazon EMR evaluates them and
      launches instances in the optimal Availability Zone. ``AvailabilityZones`` is used
      for instance fleets, while ``AvailabilityZone`` (singular) is used for uniform
      instance groups.

      .. note::

        The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and
        later, excluding 5.0.x versions.

      - *(string) --*
    """


_ClientDescribeJobFlowsResponseJobFlowsInstancesTypeDef = TypedDict(
    "_ClientDescribeJobFlowsResponseJobFlowsInstancesTypeDef",
    {
        "MasterInstanceType": str,
        "MasterPublicDnsName": str,
        "MasterInstanceId": str,
        "SlaveInstanceType": str,
        "InstanceCount": int,
        "InstanceGroups": List[
            ClientDescribeJobFlowsResponseJobFlowsInstancesInstanceGroupsTypeDef
        ],
        "NormalizedInstanceHours": int,
        "Ec2KeyName": str,
        "Ec2SubnetId": str,
        "Placement": ClientDescribeJobFlowsResponseJobFlowsInstancesPlacementTypeDef,
        "KeepJobFlowAliveWhenNoSteps": bool,
        "TerminationProtected": bool,
        "HadoopVersion": str,
    },
    total=False,
)


class ClientDescribeJobFlowsResponseJobFlowsInstancesTypeDef(
    _ClientDescribeJobFlowsResponseJobFlowsInstancesTypeDef
):
    """
    Type definition for `ClientDescribeJobFlowsResponseJobFlows` `Instances`

    Describes the Amazon EC2 instances of the job flow.

    - **MasterInstanceType** *(string) --*

      The Amazon EC2 master node instance type.

    - **MasterPublicDnsName** *(string) --*

      The DNS name of the master node. If the cluster is on a private subnet, this is the
      private DNS name. On a public subnet, this is the public DNS name.

    - **MasterInstanceId** *(string) --*

      The Amazon EC2 instance identifier of the master node.

    - **SlaveInstanceType** *(string) --*

      The Amazon EC2 core and task node instance type.

    - **InstanceCount** *(integer) --*

      The number of Amazon EC2 instances in the cluster. If the value is 1, the same instance
      serves as both the master and core and task node. If the value is greater than 1, one
      instance is the master node and all others are core and task nodes.

    - **InstanceGroups** *(list) --*

      Details about the instance groups in a cluster.

      - *(dict) --*

        Detailed information about an instance group.

        - **InstanceGroupId** *(string) --*

          Unique identifier for the instance group.

        - **Name** *(string) --*

          Friendly name for the instance group.

        - **Market** *(string) --*

          Market type of the EC2 instances used to create a cluster node.

        - **InstanceRole** *(string) --*

          Instance group role in the cluster

        - **BidPrice** *(string) --*

          The bid price for each EC2 Spot instance type as defined by ``InstanceType`` .
          Expressed in USD. If neither ``BidPrice`` nor
          ``BidPriceAsPercentageOfOnDemandPrice`` is provided,
          ``BidPriceAsPercentageOfOnDemandPrice`` defaults to 100%.

        - **InstanceType** *(string) --*

          EC2 instance type.

        - **InstanceRequestCount** *(integer) --*

          Target number of instances to run in the instance group.

        - **InstanceRunningCount** *(integer) --*

          Actual count of running instances.

        - **State** *(string) --*

          State of instance group. The following values are deprecated: STARTING, TERMINATED,
          and FAILED.

        - **LastStateChangeReason** *(string) --*

          Details regarding the state of the instance group.

        - **CreationDateTime** *(datetime) --*

          The date/time the instance group was created.

        - **StartDateTime** *(datetime) --*

          The date/time the instance group was started.

        - **ReadyDateTime** *(datetime) --*

          The date/time the instance group was available to the cluster.

        - **EndDateTime** *(datetime) --*

          The date/time the instance group was terminated.

    - **NormalizedInstanceHours** *(integer) --*

      An approximation of the cost of the cluster, represented in m1.small/hours. This value
      is incremented one time for every hour that an m1.small runs. Larger instances are
      weighted more, so an Amazon EC2 instance that is roughly four times more expensive
      would result in the normalized instance hours being incremented by four. This result is
      only an approximation and does not reflect the actual billing rate.

    - **Ec2KeyName** *(string) --*

      The name of an Amazon EC2 key pair that can be used to ssh to the master node.

    - **Ec2SubnetId** *(string) --*

      For clusters launched within Amazon Virtual Private Cloud, this is the identifier of
      the subnet where the cluster was launched.

    - **Placement** *(dict) --*

      The Amazon EC2 Availability Zone for the cluster.

      - **AvailabilityZone** *(string) --*

        The Amazon EC2 Availability Zone for the cluster. ``AvailabilityZone`` is used for
        uniform instance groups, while ``AvailabilityZones`` (plural) is used for instance
        fleets.

      - **AvailabilityZones** *(list) --*

        When multiple Availability Zones are specified, Amazon EMR evaluates them and
        launches instances in the optimal Availability Zone. ``AvailabilityZones`` is used
        for instance fleets, while ``AvailabilityZone`` (singular) is used for uniform
        instance groups.

        .. note::

          The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and
          later, excluding 5.0.x versions.

        - *(string) --*

    - **KeepJobFlowAliveWhenNoSteps** *(boolean) --*

      Specifies whether the cluster should remain available after completing all steps.

    - **TerminationProtected** *(boolean) --*

      Specifies whether the Amazon EC2 instances in the cluster are protected from
      termination by API calls, user intervention, or in the event of a job-flow error.

    - **HadoopVersion** *(string) --*

      The Hadoop version for the cluster.
    """


_ClientDescribeJobFlowsResponseJobFlowsStepsExecutionStatusDetailTypeDef = TypedDict(
    "_ClientDescribeJobFlowsResponseJobFlowsStepsExecutionStatusDetailTypeDef",
    {
        "State": str,
        "CreationDateTime": datetime,
        "StartDateTime": datetime,
        "EndDateTime": datetime,
        "LastStateChangeReason": str,
    },
    total=False,
)


class ClientDescribeJobFlowsResponseJobFlowsStepsExecutionStatusDetailTypeDef(
    _ClientDescribeJobFlowsResponseJobFlowsStepsExecutionStatusDetailTypeDef
):
    """
    Type definition for `ClientDescribeJobFlowsResponseJobFlowsSteps` `ExecutionStatusDetail`

    The description of the step status.

    - **State** *(string) --*

      The state of the step.

    - **CreationDateTime** *(datetime) --*

      The creation date and time of the step.

    - **StartDateTime** *(datetime) --*

      The start date and time of the step.

    - **EndDateTime** *(datetime) --*

      The completion date and time of the step.

    - **LastStateChangeReason** *(string) --*

      A description of the step's current state.
    """


_ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigHadoopJarStepPropertiesTypeDef = TypedDict(
    "_ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigHadoopJarStepPropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigHadoopJarStepPropertiesTypeDef(
    _ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigHadoopJarStepPropertiesTypeDef
):
    """
    Type definition for `ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigHadoopJarStep` `Properties`

    A key value pair.

    - **Key** *(string) --*

      The unique identifier of a key value pair.

    - **Value** *(string) --*

      The value part of the identified key.
    """


_ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigHadoopJarStepTypeDef = TypedDict(
    "_ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigHadoopJarStepTypeDef",
    {
        "Properties": List[
            ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigHadoopJarStepPropertiesTypeDef
        ],
        "Jar": str,
        "MainClass": str,
        "Args": List[str],
    },
    total=False,
)


class ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigHadoopJarStepTypeDef(
    _ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigHadoopJarStepTypeDef
):
    """
    Type definition for `ClientDescribeJobFlowsResponseJobFlowsStepsStepConfig` `HadoopJarStep`

    The JAR file used for the step.

    - **Properties** *(list) --*

      A list of Java properties that are set when the step runs. You can use these
      properties to pass key value pairs to your main function.

      - *(dict) --*

        A key value pair.

        - **Key** *(string) --*

          The unique identifier of a key value pair.

        - **Value** *(string) --*

          The value part of the identified key.

    - **Jar** *(string) --*

      A path to a JAR file run during the step.

    - **MainClass** *(string) --*

      The name of the main class in the specified Java file. If not specified, the JAR
      file should specify a Main-Class in its manifest file.

    - **Args** *(list) --*

      A list of command line arguments passed to the JAR file's main function when
      executed.

      - *(string) --*
    """


_ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigTypeDef = TypedDict(
    "_ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigTypeDef",
    {
        "Name": str,
        "ActionOnFailure": str,
        "HadoopJarStep": ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigHadoopJarStepTypeDef,
    },
    total=False,
)


class ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigTypeDef(
    _ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigTypeDef
):
    """
    Type definition for `ClientDescribeJobFlowsResponseJobFlowsSteps` `StepConfig`

    The step configuration.

    - **Name** *(string) --*

      The name of the step.

    - **ActionOnFailure** *(string) --*

      The action to take when the cluster step fails. Possible values are
      TERMINATE_CLUSTER, CANCEL_AND_WAIT, and CONTINUE. TERMINATE_JOB_FLOW is provided
      for backward compatibility. We recommend using TERMINATE_CLUSTER instead.

    - **HadoopJarStep** *(dict) --*

      The JAR file used for the step.

      - **Properties** *(list) --*

        A list of Java properties that are set when the step runs. You can use these
        properties to pass key value pairs to your main function.

        - *(dict) --*

          A key value pair.

          - **Key** *(string) --*

            The unique identifier of a key value pair.

          - **Value** *(string) --*

            The value part of the identified key.

      - **Jar** *(string) --*

        A path to a JAR file run during the step.

      - **MainClass** *(string) --*

        The name of the main class in the specified Java file. If not specified, the JAR
        file should specify a Main-Class in its manifest file.

      - **Args** *(list) --*

        A list of command line arguments passed to the JAR file's main function when
        executed.

        - *(string) --*
    """


_ClientDescribeJobFlowsResponseJobFlowsStepsTypeDef = TypedDict(
    "_ClientDescribeJobFlowsResponseJobFlowsStepsTypeDef",
    {
        "StepConfig": ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigTypeDef,
        "ExecutionStatusDetail": ClientDescribeJobFlowsResponseJobFlowsStepsExecutionStatusDetailTypeDef,
    },
    total=False,
)


class ClientDescribeJobFlowsResponseJobFlowsStepsTypeDef(
    _ClientDescribeJobFlowsResponseJobFlowsStepsTypeDef
):
    """
    Type definition for `ClientDescribeJobFlowsResponseJobFlows` `Steps`

    Combines the execution state and configuration of a step.

    - **StepConfig** *(dict) --*

      The step configuration.

      - **Name** *(string) --*

        The name of the step.

      - **ActionOnFailure** *(string) --*

        The action to take when the cluster step fails. Possible values are
        TERMINATE_CLUSTER, CANCEL_AND_WAIT, and CONTINUE. TERMINATE_JOB_FLOW is provided
        for backward compatibility. We recommend using TERMINATE_CLUSTER instead.

      - **HadoopJarStep** *(dict) --*

        The JAR file used for the step.

        - **Properties** *(list) --*

          A list of Java properties that are set when the step runs. You can use these
          properties to pass key value pairs to your main function.

          - *(dict) --*

            A key value pair.

            - **Key** *(string) --*

              The unique identifier of a key value pair.

            - **Value** *(string) --*

              The value part of the identified key.

        - **Jar** *(string) --*

          A path to a JAR file run during the step.

        - **MainClass** *(string) --*

          The name of the main class in the specified Java file. If not specified, the JAR
          file should specify a Main-Class in its manifest file.

        - **Args** *(list) --*

          A list of command line arguments passed to the JAR file's main function when
          executed.

          - *(string) --*

    - **ExecutionStatusDetail** *(dict) --*

      The description of the step status.

      - **State** *(string) --*

        The state of the step.

      - **CreationDateTime** *(datetime) --*

        The creation date and time of the step.

      - **StartDateTime** *(datetime) --*

        The start date and time of the step.

      - **EndDateTime** *(datetime) --*

        The completion date and time of the step.

      - **LastStateChangeReason** *(string) --*

        A description of the step's current state.
    """


_ClientDescribeJobFlowsResponseJobFlowsTypeDef = TypedDict(
    "_ClientDescribeJobFlowsResponseJobFlowsTypeDef",
    {
        "JobFlowId": str,
        "Name": str,
        "LogUri": str,
        "AmiVersion": str,
        "ExecutionStatusDetail": ClientDescribeJobFlowsResponseJobFlowsExecutionStatusDetailTypeDef,
        "Instances": ClientDescribeJobFlowsResponseJobFlowsInstancesTypeDef,
        "Steps": List[ClientDescribeJobFlowsResponseJobFlowsStepsTypeDef],
        "BootstrapActions": List[
            ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsTypeDef
        ],
        "SupportedProducts": List[str],
        "VisibleToAllUsers": bool,
        "JobFlowRole": str,
        "ServiceRole": str,
        "AutoScalingRole": str,
        "ScaleDownBehavior": str,
    },
    total=False,
)


class ClientDescribeJobFlowsResponseJobFlowsTypeDef(
    _ClientDescribeJobFlowsResponseJobFlowsTypeDef
):
    """
    Type definition for `ClientDescribeJobFlowsResponse` `JobFlows`

    A description of a cluster (job flow).

    - **JobFlowId** *(string) --*

      The job flow identifier.

    - **Name** *(string) --*

      The name of the job flow.

    - **LogUri** *(string) --*

      The location in Amazon S3 where log files for the job are stored.

    - **AmiVersion** *(string) --*

      Applies only to Amazon EMR AMI versions 3.x and 2.x. For Amazon EMR releases 4.0 and
      later, ``ReleaseLabel`` is used. To specify a custom AMI, use ``CustomAmiID`` .

    - **ExecutionStatusDetail** *(dict) --*

      Describes the execution status of the job flow.

      - **State** *(string) --*

        The state of the job flow.

      - **CreationDateTime** *(datetime) --*

        The creation date and time of the job flow.

      - **StartDateTime** *(datetime) --*

        The start date and time of the job flow.

      - **ReadyDateTime** *(datetime) --*

        The date and time when the job flow was ready to start running bootstrap actions.

      - **EndDateTime** *(datetime) --*

        The completion date and time of the job flow.

      - **LastStateChangeReason** *(string) --*

        Description of the job flow last changed state.

    - **Instances** *(dict) --*

      Describes the Amazon EC2 instances of the job flow.

      - **MasterInstanceType** *(string) --*

        The Amazon EC2 master node instance type.

      - **MasterPublicDnsName** *(string) --*

        The DNS name of the master node. If the cluster is on a private subnet, this is the
        private DNS name. On a public subnet, this is the public DNS name.

      - **MasterInstanceId** *(string) --*

        The Amazon EC2 instance identifier of the master node.

      - **SlaveInstanceType** *(string) --*

        The Amazon EC2 core and task node instance type.

      - **InstanceCount** *(integer) --*

        The number of Amazon EC2 instances in the cluster. If the value is 1, the same instance
        serves as both the master and core and task node. If the value is greater than 1, one
        instance is the master node and all others are core and task nodes.

      - **InstanceGroups** *(list) --*

        Details about the instance groups in a cluster.

        - *(dict) --*

          Detailed information about an instance group.

          - **InstanceGroupId** *(string) --*

            Unique identifier for the instance group.

          - **Name** *(string) --*

            Friendly name for the instance group.

          - **Market** *(string) --*

            Market type of the EC2 instances used to create a cluster node.

          - **InstanceRole** *(string) --*

            Instance group role in the cluster

          - **BidPrice** *(string) --*

            The bid price for each EC2 Spot instance type as defined by ``InstanceType`` .
            Expressed in USD. If neither ``BidPrice`` nor
            ``BidPriceAsPercentageOfOnDemandPrice`` is provided,
            ``BidPriceAsPercentageOfOnDemandPrice`` defaults to 100%.

          - **InstanceType** *(string) --*

            EC2 instance type.

          - **InstanceRequestCount** *(integer) --*

            Target number of instances to run in the instance group.

          - **InstanceRunningCount** *(integer) --*

            Actual count of running instances.

          - **State** *(string) --*

            State of instance group. The following values are deprecated: STARTING, TERMINATED,
            and FAILED.

          - **LastStateChangeReason** *(string) --*

            Details regarding the state of the instance group.

          - **CreationDateTime** *(datetime) --*

            The date/time the instance group was created.

          - **StartDateTime** *(datetime) --*

            The date/time the instance group was started.

          - **ReadyDateTime** *(datetime) --*

            The date/time the instance group was available to the cluster.

          - **EndDateTime** *(datetime) --*

            The date/time the instance group was terminated.

      - **NormalizedInstanceHours** *(integer) --*

        An approximation of the cost of the cluster, represented in m1.small/hours. This value
        is incremented one time for every hour that an m1.small runs. Larger instances are
        weighted more, so an Amazon EC2 instance that is roughly four times more expensive
        would result in the normalized instance hours being incremented by four. This result is
        only an approximation and does not reflect the actual billing rate.

      - **Ec2KeyName** *(string) --*

        The name of an Amazon EC2 key pair that can be used to ssh to the master node.

      - **Ec2SubnetId** *(string) --*

        For clusters launched within Amazon Virtual Private Cloud, this is the identifier of
        the subnet where the cluster was launched.

      - **Placement** *(dict) --*

        The Amazon EC2 Availability Zone for the cluster.

        - **AvailabilityZone** *(string) --*

          The Amazon EC2 Availability Zone for the cluster. ``AvailabilityZone`` is used for
          uniform instance groups, while ``AvailabilityZones`` (plural) is used for instance
          fleets.

        - **AvailabilityZones** *(list) --*

          When multiple Availability Zones are specified, Amazon EMR evaluates them and
          launches instances in the optimal Availability Zone. ``AvailabilityZones`` is used
          for instance fleets, while ``AvailabilityZone`` (singular) is used for uniform
          instance groups.

          .. note::

            The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and
            later, excluding 5.0.x versions.

          - *(string) --*

      - **KeepJobFlowAliveWhenNoSteps** *(boolean) --*

        Specifies whether the cluster should remain available after completing all steps.

      - **TerminationProtected** *(boolean) --*

        Specifies whether the Amazon EC2 instances in the cluster are protected from
        termination by API calls, user intervention, or in the event of a job-flow error.

      - **HadoopVersion** *(string) --*

        The Hadoop version for the cluster.

    - **Steps** *(list) --*

      A list of steps run by the job flow.

      - *(dict) --*

        Combines the execution state and configuration of a step.

        - **StepConfig** *(dict) --*

          The step configuration.

          - **Name** *(string) --*

            The name of the step.

          - **ActionOnFailure** *(string) --*

            The action to take when the cluster step fails. Possible values are
            TERMINATE_CLUSTER, CANCEL_AND_WAIT, and CONTINUE. TERMINATE_JOB_FLOW is provided
            for backward compatibility. We recommend using TERMINATE_CLUSTER instead.

          - **HadoopJarStep** *(dict) --*

            The JAR file used for the step.

            - **Properties** *(list) --*

              A list of Java properties that are set when the step runs. You can use these
              properties to pass key value pairs to your main function.

              - *(dict) --*

                A key value pair.

                - **Key** *(string) --*

                  The unique identifier of a key value pair.

                - **Value** *(string) --*

                  The value part of the identified key.

            - **Jar** *(string) --*

              A path to a JAR file run during the step.

            - **MainClass** *(string) --*

              The name of the main class in the specified Java file. If not specified, the JAR
              file should specify a Main-Class in its manifest file.

            - **Args** *(list) --*

              A list of command line arguments passed to the JAR file's main function when
              executed.

              - *(string) --*

        - **ExecutionStatusDetail** *(dict) --*

          The description of the step status.

          - **State** *(string) --*

            The state of the step.

          - **CreationDateTime** *(datetime) --*

            The creation date and time of the step.

          - **StartDateTime** *(datetime) --*

            The start date and time of the step.

          - **EndDateTime** *(datetime) --*

            The completion date and time of the step.

          - **LastStateChangeReason** *(string) --*

            A description of the step's current state.

    - **BootstrapActions** *(list) --*

      A list of the bootstrap actions run by the job flow.

      - *(dict) --*

        Reports the configuration of a bootstrap action in a cluster (job flow).

        - **BootstrapActionConfig** *(dict) --*

          A description of the bootstrap action.

          - **Name** *(string) --*

            The name of the bootstrap action.

          - **ScriptBootstrapAction** *(dict) --*

            The script run by the bootstrap action.

            - **Path** *(string) --*

              Location of the script to run during a bootstrap action. Can be either a location
              in Amazon S3 or on a local file system.

            - **Args** *(list) --*

              A list of command line arguments to pass to the bootstrap action script.

              - *(string) --*

    - **SupportedProducts** *(list) --*

      A list of strings set by third party software when the job flow is launched. If you are
      not using third party software to manage the job flow this value is empty.

      - *(string) --*

    - **VisibleToAllUsers** *(boolean) --*

      Indicates whether the cluster is visible to all IAM users of the AWS account associated
      with the cluster. The default value, ``true`` , indicates that all IAM users in the AWS
      account can perform cluster actions if they have the proper IAM policy permissions. If
      this value is ``false`` , only the IAM user that created the cluster can perform actions.
      This value can be changed on a running cluster by using the  SetVisibleToAllUsers action.
      You can override the default value of ``true`` when you create a cluster by using the
      ``VisibleToAllUsers`` parameter of the ``RunJobFlow`` action.

    - **JobFlowRole** *(string) --*

      The IAM role that was specified when the job flow was launched. The EC2 instances of the
      job flow assume this role.

    - **ServiceRole** *(string) --*

      The IAM role that will be assumed by the Amazon EMR service to access AWS resources on
      your behalf.

    - **AutoScalingRole** *(string) --*

      An IAM role for automatic scaling policies. The default role is
      ``EMR_AutoScaling_DefaultRole`` . The IAM role provides a way for the automatic scaling
      feature to get the required permissions it needs to launch and terminate EC2 instances in
      an instance group.

    - **ScaleDownBehavior** *(string) --*

      The way that individual Amazon EC2 instances terminate when an automatic scale-in
      activity occurs or an instance group is resized. ``TERMINATE_AT_INSTANCE_HOUR`` indicates
      that Amazon EMR terminates nodes at the instance-hour boundary, regardless of when the
      request to terminate the instance was submitted. This option is only available with
      Amazon EMR 5.1.0 and later and is the default for clusters created using that version.
      ``TERMINATE_AT_TASK_COMPLETION`` indicates that Amazon EMR blacklists and drains tasks
      from nodes before terminating the Amazon EC2 instances, regardless of the instance-hour
      boundary. With either behavior, Amazon EMR removes the least active nodes first and
      blocks instance termination if it could lead to HDFS corruption.
      ``TERMINATE_AT_TASK_COMPLETION`` available only in Amazon EMR version 4.1.0 and later,
      and is the default for versions of Amazon EMR earlier than 5.1.0.
    """


_ClientDescribeJobFlowsResponseTypeDef = TypedDict(
    "_ClientDescribeJobFlowsResponseTypeDef",
    {"JobFlows": List[ClientDescribeJobFlowsResponseJobFlowsTypeDef]},
    total=False,
)


class ClientDescribeJobFlowsResponseTypeDef(_ClientDescribeJobFlowsResponseTypeDef):
    """
    Type definition for `ClientDescribeJobFlows` `Response`

    The output for the  DescribeJobFlows operation.

    - **JobFlows** *(list) --*

      A list of job flows matching the parameters supplied.

      - *(dict) --*

        A description of a cluster (job flow).

        - **JobFlowId** *(string) --*

          The job flow identifier.

        - **Name** *(string) --*

          The name of the job flow.

        - **LogUri** *(string) --*

          The location in Amazon S3 where log files for the job are stored.

        - **AmiVersion** *(string) --*

          Applies only to Amazon EMR AMI versions 3.x and 2.x. For Amazon EMR releases 4.0 and
          later, ``ReleaseLabel`` is used. To specify a custom AMI, use ``CustomAmiID`` .

        - **ExecutionStatusDetail** *(dict) --*

          Describes the execution status of the job flow.

          - **State** *(string) --*

            The state of the job flow.

          - **CreationDateTime** *(datetime) --*

            The creation date and time of the job flow.

          - **StartDateTime** *(datetime) --*

            The start date and time of the job flow.

          - **ReadyDateTime** *(datetime) --*

            The date and time when the job flow was ready to start running bootstrap actions.

          - **EndDateTime** *(datetime) --*

            The completion date and time of the job flow.

          - **LastStateChangeReason** *(string) --*

            Description of the job flow last changed state.

        - **Instances** *(dict) --*

          Describes the Amazon EC2 instances of the job flow.

          - **MasterInstanceType** *(string) --*

            The Amazon EC2 master node instance type.

          - **MasterPublicDnsName** *(string) --*

            The DNS name of the master node. If the cluster is on a private subnet, this is the
            private DNS name. On a public subnet, this is the public DNS name.

          - **MasterInstanceId** *(string) --*

            The Amazon EC2 instance identifier of the master node.

          - **SlaveInstanceType** *(string) --*

            The Amazon EC2 core and task node instance type.

          - **InstanceCount** *(integer) --*

            The number of Amazon EC2 instances in the cluster. If the value is 1, the same instance
            serves as both the master and core and task node. If the value is greater than 1, one
            instance is the master node and all others are core and task nodes.

          - **InstanceGroups** *(list) --*

            Details about the instance groups in a cluster.

            - *(dict) --*

              Detailed information about an instance group.

              - **InstanceGroupId** *(string) --*

                Unique identifier for the instance group.

              - **Name** *(string) --*

                Friendly name for the instance group.

              - **Market** *(string) --*

                Market type of the EC2 instances used to create a cluster node.

              - **InstanceRole** *(string) --*

                Instance group role in the cluster

              - **BidPrice** *(string) --*

                The bid price for each EC2 Spot instance type as defined by ``InstanceType`` .
                Expressed in USD. If neither ``BidPrice`` nor
                ``BidPriceAsPercentageOfOnDemandPrice`` is provided,
                ``BidPriceAsPercentageOfOnDemandPrice`` defaults to 100%.

              - **InstanceType** *(string) --*

                EC2 instance type.

              - **InstanceRequestCount** *(integer) --*

                Target number of instances to run in the instance group.

              - **InstanceRunningCount** *(integer) --*

                Actual count of running instances.

              - **State** *(string) --*

                State of instance group. The following values are deprecated: STARTING, TERMINATED,
                and FAILED.

              - **LastStateChangeReason** *(string) --*

                Details regarding the state of the instance group.

              - **CreationDateTime** *(datetime) --*

                The date/time the instance group was created.

              - **StartDateTime** *(datetime) --*

                The date/time the instance group was started.

              - **ReadyDateTime** *(datetime) --*

                The date/time the instance group was available to the cluster.

              - **EndDateTime** *(datetime) --*

                The date/time the instance group was terminated.

          - **NormalizedInstanceHours** *(integer) --*

            An approximation of the cost of the cluster, represented in m1.small/hours. This value
            is incremented one time for every hour that an m1.small runs. Larger instances are
            weighted more, so an Amazon EC2 instance that is roughly four times more expensive
            would result in the normalized instance hours being incremented by four. This result is
            only an approximation and does not reflect the actual billing rate.

          - **Ec2KeyName** *(string) --*

            The name of an Amazon EC2 key pair that can be used to ssh to the master node.

          - **Ec2SubnetId** *(string) --*

            For clusters launched within Amazon Virtual Private Cloud, this is the identifier of
            the subnet where the cluster was launched.

          - **Placement** *(dict) --*

            The Amazon EC2 Availability Zone for the cluster.

            - **AvailabilityZone** *(string) --*

              The Amazon EC2 Availability Zone for the cluster. ``AvailabilityZone`` is used for
              uniform instance groups, while ``AvailabilityZones`` (plural) is used for instance
              fleets.

            - **AvailabilityZones** *(list) --*

              When multiple Availability Zones are specified, Amazon EMR evaluates them and
              launches instances in the optimal Availability Zone. ``AvailabilityZones`` is used
              for instance fleets, while ``AvailabilityZone`` (singular) is used for uniform
              instance groups.

              .. note::

                The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and
                later, excluding 5.0.x versions.

              - *(string) --*

          - **KeepJobFlowAliveWhenNoSteps** *(boolean) --*

            Specifies whether the cluster should remain available after completing all steps.

          - **TerminationProtected** *(boolean) --*

            Specifies whether the Amazon EC2 instances in the cluster are protected from
            termination by API calls, user intervention, or in the event of a job-flow error.

          - **HadoopVersion** *(string) --*

            The Hadoop version for the cluster.

        - **Steps** *(list) --*

          A list of steps run by the job flow.

          - *(dict) --*

            Combines the execution state and configuration of a step.

            - **StepConfig** *(dict) --*

              The step configuration.

              - **Name** *(string) --*

                The name of the step.

              - **ActionOnFailure** *(string) --*

                The action to take when the cluster step fails. Possible values are
                TERMINATE_CLUSTER, CANCEL_AND_WAIT, and CONTINUE. TERMINATE_JOB_FLOW is provided
                for backward compatibility. We recommend using TERMINATE_CLUSTER instead.

              - **HadoopJarStep** *(dict) --*

                The JAR file used for the step.

                - **Properties** *(list) --*

                  A list of Java properties that are set when the step runs. You can use these
                  properties to pass key value pairs to your main function.

                  - *(dict) --*

                    A key value pair.

                    - **Key** *(string) --*

                      The unique identifier of a key value pair.

                    - **Value** *(string) --*

                      The value part of the identified key.

                - **Jar** *(string) --*

                  A path to a JAR file run during the step.

                - **MainClass** *(string) --*

                  The name of the main class in the specified Java file. If not specified, the JAR
                  file should specify a Main-Class in its manifest file.

                - **Args** *(list) --*

                  A list of command line arguments passed to the JAR file's main function when
                  executed.

                  - *(string) --*

            - **ExecutionStatusDetail** *(dict) --*

              The description of the step status.

              - **State** *(string) --*

                The state of the step.

              - **CreationDateTime** *(datetime) --*

                The creation date and time of the step.

              - **StartDateTime** *(datetime) --*

                The start date and time of the step.

              - **EndDateTime** *(datetime) --*

                The completion date and time of the step.

              - **LastStateChangeReason** *(string) --*

                A description of the step's current state.

        - **BootstrapActions** *(list) --*

          A list of the bootstrap actions run by the job flow.

          - *(dict) --*

            Reports the configuration of a bootstrap action in a cluster (job flow).

            - **BootstrapActionConfig** *(dict) --*

              A description of the bootstrap action.

              - **Name** *(string) --*

                The name of the bootstrap action.

              - **ScriptBootstrapAction** *(dict) --*

                The script run by the bootstrap action.

                - **Path** *(string) --*

                  Location of the script to run during a bootstrap action. Can be either a location
                  in Amazon S3 or on a local file system.

                - **Args** *(list) --*

                  A list of command line arguments to pass to the bootstrap action script.

                  - *(string) --*

        - **SupportedProducts** *(list) --*

          A list of strings set by third party software when the job flow is launched. If you are
          not using third party software to manage the job flow this value is empty.

          - *(string) --*

        - **VisibleToAllUsers** *(boolean) --*

          Indicates whether the cluster is visible to all IAM users of the AWS account associated
          with the cluster. The default value, ``true`` , indicates that all IAM users in the AWS
          account can perform cluster actions if they have the proper IAM policy permissions. If
          this value is ``false`` , only the IAM user that created the cluster can perform actions.
          This value can be changed on a running cluster by using the  SetVisibleToAllUsers action.
          You can override the default value of ``true`` when you create a cluster by using the
          ``VisibleToAllUsers`` parameter of the ``RunJobFlow`` action.

        - **JobFlowRole** *(string) --*

          The IAM role that was specified when the job flow was launched. The EC2 instances of the
          job flow assume this role.

        - **ServiceRole** *(string) --*

          The IAM role that will be assumed by the Amazon EMR service to access AWS resources on
          your behalf.

        - **AutoScalingRole** *(string) --*

          An IAM role for automatic scaling policies. The default role is
          ``EMR_AutoScaling_DefaultRole`` . The IAM role provides a way for the automatic scaling
          feature to get the required permissions it needs to launch and terminate EC2 instances in
          an instance group.

        - **ScaleDownBehavior** *(string) --*

          The way that individual Amazon EC2 instances terminate when an automatic scale-in
          activity occurs or an instance group is resized. ``TERMINATE_AT_INSTANCE_HOUR`` indicates
          that Amazon EMR terminates nodes at the instance-hour boundary, regardless of when the
          request to terminate the instance was submitted. This option is only available with
          Amazon EMR 5.1.0 and later and is the default for clusters created using that version.
          ``TERMINATE_AT_TASK_COMPLETION`` indicates that Amazon EMR blacklists and drains tasks
          from nodes before terminating the Amazon EC2 instances, regardless of the instance-hour
          boundary. With either behavior, Amazon EMR removes the least active nodes first and
          blocks instance termination if it could lead to HDFS corruption.
          ``TERMINATE_AT_TASK_COMPLETION`` available only in Amazon EMR version 4.1.0 and later,
          and is the default for versions of Amazon EMR earlier than 5.1.0.
    """


_ClientDescribeSecurityConfigurationResponseTypeDef = TypedDict(
    "_ClientDescribeSecurityConfigurationResponseTypeDef",
    {"Name": str, "SecurityConfiguration": str, "CreationDateTime": datetime},
    total=False,
)


class ClientDescribeSecurityConfigurationResponseTypeDef(
    _ClientDescribeSecurityConfigurationResponseTypeDef
):
    """
    Type definition for `ClientDescribeSecurityConfiguration` `Response`

    - **Name** *(string) --*

      The name of the security configuration.

    - **SecurityConfiguration** *(string) --*

      The security configuration details in JSON format.

    - **CreationDateTime** *(datetime) --*

      The date and time the security configuration was created
    """


_ClientDescribeStepResponseStepConfigTypeDef = TypedDict(
    "_ClientDescribeStepResponseStepConfigTypeDef",
    {"Jar": str, "Properties": Dict[str, str], "MainClass": str, "Args": List[str]},
    total=False,
)


class ClientDescribeStepResponseStepConfigTypeDef(
    _ClientDescribeStepResponseStepConfigTypeDef
):
    """
    Type definition for `ClientDescribeStepResponseStep` `Config`

    The Hadoop job configuration of the cluster step.

    - **Jar** *(string) --*

      The path to the JAR file that runs during the step.

    - **Properties** *(dict) --*

      The list of Java properties that are set when the step runs. You can use these properties
      to pass key value pairs to your main function.

      - *(string) --*

        - *(string) --*

    - **MainClass** *(string) --*

      The name of the main class in the specified Java file. If not specified, the JAR file
      should specify a main class in its manifest file.

    - **Args** *(list) --*

      The list of command line arguments to pass to the JAR file's main function for execution.

      - *(string) --*
    """


_ClientDescribeStepResponseStepStatusFailureDetailsTypeDef = TypedDict(
    "_ClientDescribeStepResponseStepStatusFailureDetailsTypeDef",
    {"Reason": str, "Message": str, "LogFile": str},
    total=False,
)


class ClientDescribeStepResponseStepStatusFailureDetailsTypeDef(
    _ClientDescribeStepResponseStepStatusFailureDetailsTypeDef
):
    """
    Type definition for `ClientDescribeStepResponseStepStatus` `FailureDetails`

    The details for the step failure including reason, message, and log file path where the
    root cause was identified.

    - **Reason** *(string) --*

      The reason for the step failure. In the case where the service cannot successfully
      determine the root cause of the failure, it returns "Unknown Error" as a reason.

    - **Message** *(string) --*

      The descriptive message including the error the EMR service has identified as the cause
      of step failure. This is text from an error log that describes the root cause of the
      failure.

    - **LogFile** *(string) --*

      The path to the log file where the step failure root cause was originally recorded.
    """


_ClientDescribeStepResponseStepStatusStateChangeReasonTypeDef = TypedDict(
    "_ClientDescribeStepResponseStepStatusStateChangeReasonTypeDef",
    {"Code": str, "Message": str},
    total=False,
)


class ClientDescribeStepResponseStepStatusStateChangeReasonTypeDef(
    _ClientDescribeStepResponseStepStatusStateChangeReasonTypeDef
):
    """
    Type definition for `ClientDescribeStepResponseStepStatus` `StateChangeReason`

    The reason for the step execution status change.

    - **Code** *(string) --*

      The programmable code for the state change reason. Note: Currently, the service
      provides no code for the state change.

    - **Message** *(string) --*

      The descriptive message for the state change reason.
    """


_ClientDescribeStepResponseStepStatusTimelineTypeDef = TypedDict(
    "_ClientDescribeStepResponseStepStatusTimelineTypeDef",
    {"CreationDateTime": datetime, "StartDateTime": datetime, "EndDateTime": datetime},
    total=False,
)


class ClientDescribeStepResponseStepStatusTimelineTypeDef(
    _ClientDescribeStepResponseStepStatusTimelineTypeDef
):
    """
    Type definition for `ClientDescribeStepResponseStepStatus` `Timeline`

    The timeline of the cluster step status over time.

    - **CreationDateTime** *(datetime) --*

      The date and time when the cluster step was created.

    - **StartDateTime** *(datetime) --*

      The date and time when the cluster step execution started.

    - **EndDateTime** *(datetime) --*

      The date and time when the cluster step execution completed or failed.
    """


_ClientDescribeStepResponseStepStatusTypeDef = TypedDict(
    "_ClientDescribeStepResponseStepStatusTypeDef",
    {
        "State": str,
        "StateChangeReason": ClientDescribeStepResponseStepStatusStateChangeReasonTypeDef,
        "FailureDetails": ClientDescribeStepResponseStepStatusFailureDetailsTypeDef,
        "Timeline": ClientDescribeStepResponseStepStatusTimelineTypeDef,
    },
    total=False,
)


class ClientDescribeStepResponseStepStatusTypeDef(
    _ClientDescribeStepResponseStepStatusTypeDef
):
    """
    Type definition for `ClientDescribeStepResponseStep` `Status`

    The current execution status details of the cluster step.

    - **State** *(string) --*

      The execution state of the cluster step.

    - **StateChangeReason** *(dict) --*

      The reason for the step execution status change.

      - **Code** *(string) --*

        The programmable code for the state change reason. Note: Currently, the service
        provides no code for the state change.

      - **Message** *(string) --*

        The descriptive message for the state change reason.

    - **FailureDetails** *(dict) --*

      The details for the step failure including reason, message, and log file path where the
      root cause was identified.

      - **Reason** *(string) --*

        The reason for the step failure. In the case where the service cannot successfully
        determine the root cause of the failure, it returns "Unknown Error" as a reason.

      - **Message** *(string) --*

        The descriptive message including the error the EMR service has identified as the cause
        of step failure. This is text from an error log that describes the root cause of the
        failure.

      - **LogFile** *(string) --*

        The path to the log file where the step failure root cause was originally recorded.

    - **Timeline** *(dict) --*

      The timeline of the cluster step status over time.

      - **CreationDateTime** *(datetime) --*

        The date and time when the cluster step was created.

      - **StartDateTime** *(datetime) --*

        The date and time when the cluster step execution started.

      - **EndDateTime** *(datetime) --*

        The date and time when the cluster step execution completed or failed.
    """


_ClientDescribeStepResponseStepTypeDef = TypedDict(
    "_ClientDescribeStepResponseStepTypeDef",
    {
        "Id": str,
        "Name": str,
        "Config": ClientDescribeStepResponseStepConfigTypeDef,
        "ActionOnFailure": str,
        "Status": ClientDescribeStepResponseStepStatusTypeDef,
    },
    total=False,
)


class ClientDescribeStepResponseStepTypeDef(_ClientDescribeStepResponseStepTypeDef):
    """
    Type definition for `ClientDescribeStepResponse` `Step`

    The step details for the requested step identifier.

    - **Id** *(string) --*

      The identifier of the cluster step.

    - **Name** *(string) --*

      The name of the cluster step.

    - **Config** *(dict) --*

      The Hadoop job configuration of the cluster step.

      - **Jar** *(string) --*

        The path to the JAR file that runs during the step.

      - **Properties** *(dict) --*

        The list of Java properties that are set when the step runs. You can use these properties
        to pass key value pairs to your main function.

        - *(string) --*

          - *(string) --*

      - **MainClass** *(string) --*

        The name of the main class in the specified Java file. If not specified, the JAR file
        should specify a main class in its manifest file.

      - **Args** *(list) --*

        The list of command line arguments to pass to the JAR file's main function for execution.

        - *(string) --*

    - **ActionOnFailure** *(string) --*

      The action to take when the cluster step fails. Possible values are TERMINATE_CLUSTER,
      CANCEL_AND_WAIT, and CONTINUE. TERMINATE_JOB_FLOW is provided for backward compatibility.
      We recommend using TERMINATE_CLUSTER instead.

    - **Status** *(dict) --*

      The current execution status details of the cluster step.

      - **State** *(string) --*

        The execution state of the cluster step.

      - **StateChangeReason** *(dict) --*

        The reason for the step execution status change.

        - **Code** *(string) --*

          The programmable code for the state change reason. Note: Currently, the service
          provides no code for the state change.

        - **Message** *(string) --*

          The descriptive message for the state change reason.

      - **FailureDetails** *(dict) --*

        The details for the step failure including reason, message, and log file path where the
        root cause was identified.

        - **Reason** *(string) --*

          The reason for the step failure. In the case where the service cannot successfully
          determine the root cause of the failure, it returns "Unknown Error" as a reason.

        - **Message** *(string) --*

          The descriptive message including the error the EMR service has identified as the cause
          of step failure. This is text from an error log that describes the root cause of the
          failure.

        - **LogFile** *(string) --*

          The path to the log file where the step failure root cause was originally recorded.

      - **Timeline** *(dict) --*

        The timeline of the cluster step status over time.

        - **CreationDateTime** *(datetime) --*

          The date and time when the cluster step was created.

        - **StartDateTime** *(datetime) --*

          The date and time when the cluster step execution started.

        - **EndDateTime** *(datetime) --*

          The date and time when the cluster step execution completed or failed.
    """


_ClientDescribeStepResponseTypeDef = TypedDict(
    "_ClientDescribeStepResponseTypeDef",
    {"Step": ClientDescribeStepResponseStepTypeDef},
    total=False,
)


class ClientDescribeStepResponseTypeDef(_ClientDescribeStepResponseTypeDef):
    """
    Type definition for `ClientDescribeStep` `Response`

    This output contains the description of the cluster step.

    - **Step** *(dict) --*

      The step details for the requested step identifier.

      - **Id** *(string) --*

        The identifier of the cluster step.

      - **Name** *(string) --*

        The name of the cluster step.

      - **Config** *(dict) --*

        The Hadoop job configuration of the cluster step.

        - **Jar** *(string) --*

          The path to the JAR file that runs during the step.

        - **Properties** *(dict) --*

          The list of Java properties that are set when the step runs. You can use these properties
          to pass key value pairs to your main function.

          - *(string) --*

            - *(string) --*

        - **MainClass** *(string) --*

          The name of the main class in the specified Java file. If not specified, the JAR file
          should specify a main class in its manifest file.

        - **Args** *(list) --*

          The list of command line arguments to pass to the JAR file's main function for execution.

          - *(string) --*

      - **ActionOnFailure** *(string) --*

        The action to take when the cluster step fails. Possible values are TERMINATE_CLUSTER,
        CANCEL_AND_WAIT, and CONTINUE. TERMINATE_JOB_FLOW is provided for backward compatibility.
        We recommend using TERMINATE_CLUSTER instead.

      - **Status** *(dict) --*

        The current execution status details of the cluster step.

        - **State** *(string) --*

          The execution state of the cluster step.

        - **StateChangeReason** *(dict) --*

          The reason for the step execution status change.

          - **Code** *(string) --*

            The programmable code for the state change reason. Note: Currently, the service
            provides no code for the state change.

          - **Message** *(string) --*

            The descriptive message for the state change reason.

        - **FailureDetails** *(dict) --*

          The details for the step failure including reason, message, and log file path where the
          root cause was identified.

          - **Reason** *(string) --*

            The reason for the step failure. In the case where the service cannot successfully
            determine the root cause of the failure, it returns "Unknown Error" as a reason.

          - **Message** *(string) --*

            The descriptive message including the error the EMR service has identified as the cause
            of step failure. This is text from an error log that describes the root cause of the
            failure.

          - **LogFile** *(string) --*

            The path to the log file where the step failure root cause was originally recorded.

        - **Timeline** *(dict) --*

          The timeline of the cluster step status over time.

          - **CreationDateTime** *(datetime) --*

            The date and time when the cluster step was created.

          - **StartDateTime** *(datetime) --*

            The date and time when the cluster step execution started.

          - **EndDateTime** *(datetime) --*

            The date and time when the cluster step execution completed or failed.
    """


_ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationMetadataTypeDef = TypedDict(
    "_ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationMetadataTypeDef",
    {"CreationDateTime": datetime, "CreatedByArn": str},
    total=False,
)


class ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationMetadataTypeDef(
    _ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationMetadataTypeDef
):
    """
    Type definition for `ClientGetBlockPublicAccessConfigurationResponse` `BlockPublicAccessConfigurationMetadata`

    Properties that describe the AWS principal that created the
    ``BlockPublicAccessConfiguration`` using the ``PutBlockPublicAccessConfiguration`` action as
    well as the date and time that the configuration was created. Each time a configuration for
    block public access is updated, Amazon EMR updates this metadata.

    - **CreationDateTime** *(datetime) --*

      The date and time that the configuration was created.

    - **CreatedByArn** *(string) --*

      The Amazon Resource Name that created or last modified the configuration.
    """


_ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef = TypedDict(
    "_ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef",
    {"MinRange": int, "MaxRange": int},
    total=False,
)


class ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef(
    _ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef
):
    """
    Type definition for `ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfiguration` `PermittedPublicSecurityGroupRuleRanges`

    A list of port ranges that are permitted to allow inbound traffic from all public IP
    addresses. To specify a single port, use the same value for ``MinRange`` and ``MaxRange``
    .

    - **MinRange** *(integer) --*

      The smallest port number in a specified range of port numbers.

    - **MaxRange** *(integer) --*

      The smallest port number in a specified range of port numbers.
    """


_ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationTypeDef = TypedDict(
    "_ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationTypeDef",
    {
        "BlockPublicSecurityGroupRules": bool,
        "PermittedPublicSecurityGroupRuleRanges": List[
            ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef
        ],
    },
    total=False,
)


class ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationTypeDef(
    _ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationTypeDef
):
    """
    Type definition for `ClientGetBlockPublicAccessConfigurationResponse` `BlockPublicAccessConfiguration`

    A configuration for Amazon EMR block public access. The configuration applies to all clusters
    created in your account for the current Region. The configuration specifies whether block
    public access is enabled. If block public access is enabled, security groups associated with
    the cluster cannot have rules that allow inbound traffic from 0.0.0.0/0 or ::/0 on a port,
    unless the port is specified as an exception using ``PermittedPublicSecurityGroupRuleRanges``
    in the ``BlockPublicAccessConfiguration`` . By default, Port 22 (SSH) is an exception, and
    public access is allowed on this port. You can change this by updating the block public
    access configuration to remove the exception.

    - **BlockPublicSecurityGroupRules** *(boolean) --*

      Indicates whether EMR block public access is enabled (``true`` ) or disabled (``false`` ).
      By default, the value is ``false`` for accounts that have created EMR clusters before July
      2019. For accounts created after this, the default is ``true`` .

    - **PermittedPublicSecurityGroupRuleRanges** *(list) --*

      Specifies ports and port ranges that are permitted to have security group rules that allow
      inbound traffic from all public sources. For example, if Port 23 (Telnet) is specified for
      ``PermittedPublicSecurityGroupRuleRanges`` , Amazon EMR allows cluster creation if a
      security group associated with the cluster has a rule that allows inbound traffic on Port
      23 from IPv4 0.0.0.0/0 or IPv6 port ::/0 as the source.

      By default, Port 22, which is used for SSH access to the cluster EC2 instances, is in the
      list of ``PermittedPublicSecurityGroupRuleRanges`` .

      - *(dict) --*

        A list of port ranges that are permitted to allow inbound traffic from all public IP
        addresses. To specify a single port, use the same value for ``MinRange`` and ``MaxRange``
        .

        - **MinRange** *(integer) --*

          The smallest port number in a specified range of port numbers.

        - **MaxRange** *(integer) --*

          The smallest port number in a specified range of port numbers.
    """


_ClientGetBlockPublicAccessConfigurationResponseTypeDef = TypedDict(
    "_ClientGetBlockPublicAccessConfigurationResponseTypeDef",
    {
        "BlockPublicAccessConfiguration": ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationTypeDef,
        "BlockPublicAccessConfigurationMetadata": ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationMetadataTypeDef,
    },
    total=False,
)


class ClientGetBlockPublicAccessConfigurationResponseTypeDef(
    _ClientGetBlockPublicAccessConfigurationResponseTypeDef
):
    """
    Type definition for `ClientGetBlockPublicAccessConfiguration` `Response`

    - **BlockPublicAccessConfiguration** *(dict) --*

      A configuration for Amazon EMR block public access. The configuration applies to all clusters
      created in your account for the current Region. The configuration specifies whether block
      public access is enabled. If block public access is enabled, security groups associated with
      the cluster cannot have rules that allow inbound traffic from 0.0.0.0/0 or ::/0 on a port,
      unless the port is specified as an exception using ``PermittedPublicSecurityGroupRuleRanges``
      in the ``BlockPublicAccessConfiguration`` . By default, Port 22 (SSH) is an exception, and
      public access is allowed on this port. You can change this by updating the block public
      access configuration to remove the exception.

      - **BlockPublicSecurityGroupRules** *(boolean) --*

        Indicates whether EMR block public access is enabled (``true`` ) or disabled (``false`` ).
        By default, the value is ``false`` for accounts that have created EMR clusters before July
        2019. For accounts created after this, the default is ``true`` .

      - **PermittedPublicSecurityGroupRuleRanges** *(list) --*

        Specifies ports and port ranges that are permitted to have security group rules that allow
        inbound traffic from all public sources. For example, if Port 23 (Telnet) is specified for
        ``PermittedPublicSecurityGroupRuleRanges`` , Amazon EMR allows cluster creation if a
        security group associated with the cluster has a rule that allows inbound traffic on Port
        23 from IPv4 0.0.0.0/0 or IPv6 port ::/0 as the source.

        By default, Port 22, which is used for SSH access to the cluster EC2 instances, is in the
        list of ``PermittedPublicSecurityGroupRuleRanges`` .

        - *(dict) --*

          A list of port ranges that are permitted to allow inbound traffic from all public IP
          addresses. To specify a single port, use the same value for ``MinRange`` and ``MaxRange``
          .

          - **MinRange** *(integer) --*

            The smallest port number in a specified range of port numbers.

          - **MaxRange** *(integer) --*

            The smallest port number in a specified range of port numbers.

    - **BlockPublicAccessConfigurationMetadata** *(dict) --*

      Properties that describe the AWS principal that created the
      ``BlockPublicAccessConfiguration`` using the ``PutBlockPublicAccessConfiguration`` action as
      well as the date and time that the configuration was created. Each time a configuration for
      block public access is updated, Amazon EMR updates this metadata.

      - **CreationDateTime** *(datetime) --*

        The date and time that the configuration was created.

      - **CreatedByArn** *(string) --*

        The Amazon Resource Name that created or last modified the configuration.
    """


_ClientListBootstrapActionsResponseBootstrapActionsTypeDef = TypedDict(
    "_ClientListBootstrapActionsResponseBootstrapActionsTypeDef",
    {"Name": str, "ScriptPath": str, "Args": List[str]},
    total=False,
)


class ClientListBootstrapActionsResponseBootstrapActionsTypeDef(
    _ClientListBootstrapActionsResponseBootstrapActionsTypeDef
):
    """
    Type definition for `ClientListBootstrapActionsResponse` `BootstrapActions`

    An entity describing an executable that runs on a cluster.

    - **Name** *(string) --*

      The name of the command.

    - **ScriptPath** *(string) --*

      The Amazon S3 location of the command script.

    - **Args** *(list) --*

      Arguments for Amazon EMR to pass to the command for execution.

      - *(string) --*
    """


_ClientListBootstrapActionsResponseTypeDef = TypedDict(
    "_ClientListBootstrapActionsResponseTypeDef",
    {
        "BootstrapActions": List[
            ClientListBootstrapActionsResponseBootstrapActionsTypeDef
        ],
        "Marker": str,
    },
    total=False,
)


class ClientListBootstrapActionsResponseTypeDef(
    _ClientListBootstrapActionsResponseTypeDef
):
    """
    Type definition for `ClientListBootstrapActions` `Response`

    This output contains the bootstrap actions detail.

    - **BootstrapActions** *(list) --*

      The bootstrap actions associated with the cluster.

      - *(dict) --*

        An entity describing an executable that runs on a cluster.

        - **Name** *(string) --*

          The name of the command.

        - **ScriptPath** *(string) --*

          The Amazon S3 location of the command script.

        - **Args** *(list) --*

          Arguments for Amazon EMR to pass to the command for execution.

          - *(string) --*

    - **Marker** *(string) --*

      The pagination token that indicates the next set of results to retrieve.
    """


_ClientListClustersResponseClustersStatusStateChangeReasonTypeDef = TypedDict(
    "_ClientListClustersResponseClustersStatusStateChangeReasonTypeDef",
    {"Code": str, "Message": str},
    total=False,
)


class ClientListClustersResponseClustersStatusStateChangeReasonTypeDef(
    _ClientListClustersResponseClustersStatusStateChangeReasonTypeDef
):
    """
    Type definition for `ClientListClustersResponseClustersStatus` `StateChangeReason`

    The reason for the cluster status change.

    - **Code** *(string) --*

      The programmatic code for the state change reason.

    - **Message** *(string) --*

      The descriptive message for the state change reason.
    """


_ClientListClustersResponseClustersStatusTimelineTypeDef = TypedDict(
    "_ClientListClustersResponseClustersStatusTimelineTypeDef",
    {"CreationDateTime": datetime, "ReadyDateTime": datetime, "EndDateTime": datetime},
    total=False,
)


class ClientListClustersResponseClustersStatusTimelineTypeDef(
    _ClientListClustersResponseClustersStatusTimelineTypeDef
):
    """
    Type definition for `ClientListClustersResponseClustersStatus` `Timeline`

    A timeline that represents the status of a cluster over the lifetime of the cluster.

    - **CreationDateTime** *(datetime) --*

      The creation date and time of the cluster.

    - **ReadyDateTime** *(datetime) --*

      The date and time when the cluster was ready to execute steps.

    - **EndDateTime** *(datetime) --*

      The date and time when the cluster was terminated.
    """


_ClientListClustersResponseClustersStatusTypeDef = TypedDict(
    "_ClientListClustersResponseClustersStatusTypeDef",
    {
        "State": str,
        "StateChangeReason": ClientListClustersResponseClustersStatusStateChangeReasonTypeDef,
        "Timeline": ClientListClustersResponseClustersStatusTimelineTypeDef,
    },
    total=False,
)


class ClientListClustersResponseClustersStatusTypeDef(
    _ClientListClustersResponseClustersStatusTypeDef
):
    """
    Type definition for `ClientListClustersResponseClusters` `Status`

    The details about the current status of the cluster.

    - **State** *(string) --*

      The current state of the cluster.

    - **StateChangeReason** *(dict) --*

      The reason for the cluster status change.

      - **Code** *(string) --*

        The programmatic code for the state change reason.

      - **Message** *(string) --*

        The descriptive message for the state change reason.

    - **Timeline** *(dict) --*

      A timeline that represents the status of a cluster over the lifetime of the cluster.

      - **CreationDateTime** *(datetime) --*

        The creation date and time of the cluster.

      - **ReadyDateTime** *(datetime) --*

        The date and time when the cluster was ready to execute steps.

      - **EndDateTime** *(datetime) --*

        The date and time when the cluster was terminated.
    """


_ClientListClustersResponseClustersTypeDef = TypedDict(
    "_ClientListClustersResponseClustersTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": ClientListClustersResponseClustersStatusTypeDef,
        "NormalizedInstanceHours": int,
        "ClusterArn": str,
    },
    total=False,
)


class ClientListClustersResponseClustersTypeDef(
    _ClientListClustersResponseClustersTypeDef
):
    """
    Type definition for `ClientListClustersResponse` `Clusters`

    The summary description of the cluster.

    - **Id** *(string) --*

      The unique identifier for the cluster.

    - **Name** *(string) --*

      The name of the cluster.

    - **Status** *(dict) --*

      The details about the current status of the cluster.

      - **State** *(string) --*

        The current state of the cluster.

      - **StateChangeReason** *(dict) --*

        The reason for the cluster status change.

        - **Code** *(string) --*

          The programmatic code for the state change reason.

        - **Message** *(string) --*

          The descriptive message for the state change reason.

      - **Timeline** *(dict) --*

        A timeline that represents the status of a cluster over the lifetime of the cluster.

        - **CreationDateTime** *(datetime) --*

          The creation date and time of the cluster.

        - **ReadyDateTime** *(datetime) --*

          The date and time when the cluster was ready to execute steps.

        - **EndDateTime** *(datetime) --*

          The date and time when the cluster was terminated.

    - **NormalizedInstanceHours** *(integer) --*

      An approximation of the cost of the cluster, represented in m1.small/hours. This value is
      incremented one time for every hour an m1.small instance runs. Larger instances are
      weighted more, so an EC2 instance that is roughly four times more expensive would result
      in the normalized instance hours being incremented by four. This result is only an
      approximation and does not reflect the actual billing rate.

    - **ClusterArn** *(string) --*

      The Amazon Resource Name of the cluster.
    """


_ClientListClustersResponseTypeDef = TypedDict(
    "_ClientListClustersResponseTypeDef",
    {"Clusters": List[ClientListClustersResponseClustersTypeDef], "Marker": str},
    total=False,
)


class ClientListClustersResponseTypeDef(_ClientListClustersResponseTypeDef):
    """
    Type definition for `ClientListClusters` `Response`

    This contains a ClusterSummaryList with the cluster details; for example, the cluster IDs,
    names, and status.

    - **Clusters** *(list) --*

      The list of clusters for the account based on the given filters.

      - *(dict) --*

        The summary description of the cluster.

        - **Id** *(string) --*

          The unique identifier for the cluster.

        - **Name** *(string) --*

          The name of the cluster.

        - **Status** *(dict) --*

          The details about the current status of the cluster.

          - **State** *(string) --*

            The current state of the cluster.

          - **StateChangeReason** *(dict) --*

            The reason for the cluster status change.

            - **Code** *(string) --*

              The programmatic code for the state change reason.

            - **Message** *(string) --*

              The descriptive message for the state change reason.

          - **Timeline** *(dict) --*

            A timeline that represents the status of a cluster over the lifetime of the cluster.

            - **CreationDateTime** *(datetime) --*

              The creation date and time of the cluster.

            - **ReadyDateTime** *(datetime) --*

              The date and time when the cluster was ready to execute steps.

            - **EndDateTime** *(datetime) --*

              The date and time when the cluster was terminated.

        - **NormalizedInstanceHours** *(integer) --*

          An approximation of the cost of the cluster, represented in m1.small/hours. This value is
          incremented one time for every hour an m1.small instance runs. Larger instances are
          weighted more, so an EC2 instance that is roughly four times more expensive would result
          in the normalized instance hours being incremented by four. This result is only an
          approximation and does not reflect the actual billing rate.

        - **ClusterArn** *(string) --*

          The Amazon Resource Name of the cluster.

    - **Marker** *(string) --*

      The pagination token that indicates the next set of results to retrieve.
    """


_ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsConfigurationsTypeDef = TypedDict(
    "_ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsConfigurationsTypeDef",
    {"Classification": str, "Configurations": List[Any], "Properties": Dict[str, str]},
    total=False,
)


class ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsConfigurationsTypeDef(
    _ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsConfigurationsTypeDef
):
    """
    Type definition for `ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecifications` `Configurations`

    .. note::

      Amazon EMR releases 4.x or later.

    An optional configuration specification to be used when provisioning cluster
    instances, which can include configurations for applications and software bundled
    with Amazon EMR. A configuration consists of a classification, properties, and
    optional nested configurations. A classification refers to an application-specific
    configuration file. Properties are the settings you want to change in that file.
    For more information, see `Configuring Applications
    <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

    - **Classification** *(string) --*

      The classification within a configuration.

    - **Configurations** *(list) --*

      A list of additional configurations to apply within a configuration object.

    - **Properties** *(dict) --*

      A set of properties specified within a configuration classification.

      - *(string) --*

        - *(string) --*
    """


_ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesVolumeSpecificationTypeDef = TypedDict(
    "_ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesVolumeSpecificationTypeDef",
    {"VolumeType": str, "Iops": int, "SizeInGB": int},
    total=False,
)


class ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesVolumeSpecificationTypeDef(
    _ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesVolumeSpecificationTypeDef
):
    """
    Type definition for `ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevices` `VolumeSpecification`

    EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
    requested for the EBS volume attached to an EC2 instance in the cluster.

    - **VolumeType** *(string) --*

      The volume type. Volume types supported are gp2, io1, standard.

    - **Iops** *(integer) --*

      The number of I/O operations per second (IOPS) that the volume supports.

    - **SizeInGB** *(integer) --*

      The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
      volume type is EBS-optimized, the minimum value is 10.
    """


_ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesTypeDef = TypedDict(
    "_ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesTypeDef",
    {
        "VolumeSpecification": ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesVolumeSpecificationTypeDef,
        "Device": str,
    },
    total=False,
)


class ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesTypeDef(
    _ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesTypeDef
):
    """
    Type definition for `ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecifications` `EbsBlockDevices`

    Configuration of requested EBS block device associated with the instance group.

    - **VolumeSpecification** *(dict) --*

      EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
      requested for the EBS volume attached to an EC2 instance in the cluster.

      - **VolumeType** *(string) --*

        The volume type. Volume types supported are gp2, io1, standard.

      - **Iops** *(integer) --*

        The number of I/O operations per second (IOPS) that the volume supports.

      - **SizeInGB** *(integer) --*

        The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
        volume type is EBS-optimized, the minimum value is 10.

    - **Device** *(string) --*

      The device name that is exposed to the instance, such as /dev/sdh.
    """


_ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsTypeDef = TypedDict(
    "_ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsTypeDef",
    {
        "InstanceType": str,
        "WeightedCapacity": int,
        "BidPrice": str,
        "BidPriceAsPercentageOfOnDemandPrice": float,
        "Configurations": List[
            ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsConfigurationsTypeDef
        ],
        "EbsBlockDevices": List[
            ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesTypeDef
        ],
        "EbsOptimized": bool,
    },
    total=False,
)


class ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsTypeDef(
    _ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsTypeDef
):
    """
    Type definition for `ClientListInstanceFleetsResponseInstanceFleets` `InstanceTypeSpecifications`

    The configuration specification for each instance type in an instance fleet.

    .. note::

      The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and
      later, excluding 5.0.x versions.

    - **InstanceType** *(string) --*

      The EC2 instance type, for example ``m3.xlarge`` .

    - **WeightedCapacity** *(integer) --*

      The number of units that a provisioned instance of this type provides toward
      fulfilling the target capacities defined in  InstanceFleetConfig . Capacity values
      represent performance characteristics such as vCPUs, memory, or I/O. If not
      specified, the default value is 1.

    - **BidPrice** *(string) --*

      The bid price for each EC2 Spot instance type as defined by ``InstanceType`` .
      Expressed in USD.

    - **BidPriceAsPercentageOfOnDemandPrice** *(float) --*

      The bid price, as a percentage of On-Demand price, for each EC2 Spot instance as
      defined by ``InstanceType`` . Expressed as a number (for example, 20 specifies 20%).

    - **Configurations** *(list) --*

      A configuration classification that applies when provisioning cluster instances,
      which can include configurations for applications and software bundled with Amazon
      EMR.

      - *(dict) --*

        .. note::

          Amazon EMR releases 4.x or later.

        An optional configuration specification to be used when provisioning cluster
        instances, which can include configurations for applications and software bundled
        with Amazon EMR. A configuration consists of a classification, properties, and
        optional nested configurations. A classification refers to an application-specific
        configuration file. Properties are the settings you want to change in that file.
        For more information, see `Configuring Applications
        <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

        - **Classification** *(string) --*

          The classification within a configuration.

        - **Configurations** *(list) --*

          A list of additional configurations to apply within a configuration object.

        - **Properties** *(dict) --*

          A set of properties specified within a configuration classification.

          - *(string) --*

            - *(string) --*

    - **EbsBlockDevices** *(list) --*

      The configuration of Amazon Elastic Block Storage (EBS) attached to each instance as
      defined by ``InstanceType`` .

      - *(dict) --*

        Configuration of requested EBS block device associated with the instance group.

        - **VolumeSpecification** *(dict) --*

          EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
          requested for the EBS volume attached to an EC2 instance in the cluster.

          - **VolumeType** *(string) --*

            The volume type. Volume types supported are gp2, io1, standard.

          - **Iops** *(integer) --*

            The number of I/O operations per second (IOPS) that the volume supports.

          - **SizeInGB** *(integer) --*

            The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
            volume type is EBS-optimized, the minimum value is 10.

        - **Device** *(string) --*

          The device name that is exposed to the instance, such as /dev/sdh.

    - **EbsOptimized** *(boolean) --*

      Evaluates to ``TRUE`` when the specified ``InstanceType`` is EBS-optimized.
    """


_ClientListInstanceFleetsResponseInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef = TypedDict(
    "_ClientListInstanceFleetsResponseInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef",
    {"TimeoutDurationMinutes": int, "TimeoutAction": str, "BlockDurationMinutes": int},
    total=False,
)


class ClientListInstanceFleetsResponseInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef(
    _ClientListInstanceFleetsResponseInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef
):
    """
    Type definition for `ClientListInstanceFleetsResponseInstanceFleetsLaunchSpecifications` `SpotSpecification`

    The launch specification for Spot instances in the fleet, which determines the defined
    duration and provisioning timeout behavior.

    - **TimeoutDurationMinutes** *(integer) --*

      The spot provisioning timeout period in minutes. If Spot instances are not
      provisioned within this time period, the ``TimeOutAction`` is taken. Minimum value is
      5 and maximum value is 1440. The timeout applies only during initial provisioning,
      when the cluster is first created.

    - **TimeoutAction** *(string) --*

      The action to take when ``TargetSpotCapacity`` has not been fulfilled when the
      ``TimeoutDurationMinutes`` has expired; that is, when all Spot instances could not be
      provisioned within the Spot provisioning timeout. Valid values are
      ``TERMINATE_CLUSTER`` and ``SWITCH_TO_ON_DEMAND`` . SWITCH_TO_ON_DEMAND specifies
      that if no Spot instances are available, On-Demand Instances should be provisioned to
      fulfill any remaining Spot capacity.

    - **BlockDurationMinutes** *(integer) --*

      The defined duration for Spot instances (also known as Spot blocks) in minutes. When
      specified, the Spot instance does not terminate before the defined duration expires,
      and defined duration pricing for Spot instances applies. Valid values are 60, 120,
      180, 240, 300, or 360. The duration period starts as soon as a Spot instance receives
      its instance ID. At the end of the duration, Amazon EC2 marks the Spot instance for
      termination and provides a Spot instance termination notice, which gives the instance
      a two-minute warning before it terminates.
    """


_ClientListInstanceFleetsResponseInstanceFleetsLaunchSpecificationsTypeDef = TypedDict(
    "_ClientListInstanceFleetsResponseInstanceFleetsLaunchSpecificationsTypeDef",
    {
        "SpotSpecification": ClientListInstanceFleetsResponseInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef
    },
    total=False,
)


class ClientListInstanceFleetsResponseInstanceFleetsLaunchSpecificationsTypeDef(
    _ClientListInstanceFleetsResponseInstanceFleetsLaunchSpecificationsTypeDef
):
    """
    Type definition for `ClientListInstanceFleetsResponseInstanceFleets` `LaunchSpecifications`

    Describes the launch specification for an instance fleet.

    - **SpotSpecification** *(dict) --*

      The launch specification for Spot instances in the fleet, which determines the defined
      duration and provisioning timeout behavior.

      - **TimeoutDurationMinutes** *(integer) --*

        The spot provisioning timeout period in minutes. If Spot instances are not
        provisioned within this time period, the ``TimeOutAction`` is taken. Minimum value is
        5 and maximum value is 1440. The timeout applies only during initial provisioning,
        when the cluster is first created.

      - **TimeoutAction** *(string) --*

        The action to take when ``TargetSpotCapacity`` has not been fulfilled when the
        ``TimeoutDurationMinutes`` has expired; that is, when all Spot instances could not be
        provisioned within the Spot provisioning timeout. Valid values are
        ``TERMINATE_CLUSTER`` and ``SWITCH_TO_ON_DEMAND`` . SWITCH_TO_ON_DEMAND specifies
        that if no Spot instances are available, On-Demand Instances should be provisioned to
        fulfill any remaining Spot capacity.

      - **BlockDurationMinutes** *(integer) --*

        The defined duration for Spot instances (also known as Spot blocks) in minutes. When
        specified, the Spot instance does not terminate before the defined duration expires,
        and defined duration pricing for Spot instances applies. Valid values are 60, 120,
        180, 240, 300, or 360. The duration period starts as soon as a Spot instance receives
        its instance ID. At the end of the duration, Amazon EC2 marks the Spot instance for
        termination and provides a Spot instance termination notice, which gives the instance
        a two-minute warning before it terminates.
    """


_ClientListInstanceFleetsResponseInstanceFleetsStatusStateChangeReasonTypeDef = TypedDict(
    "_ClientListInstanceFleetsResponseInstanceFleetsStatusStateChangeReasonTypeDef",
    {"Code": str, "Message": str},
    total=False,
)


class ClientListInstanceFleetsResponseInstanceFleetsStatusStateChangeReasonTypeDef(
    _ClientListInstanceFleetsResponseInstanceFleetsStatusStateChangeReasonTypeDef
):
    """
    Type definition for `ClientListInstanceFleetsResponseInstanceFleetsStatus` `StateChangeReason`

    Provides status change reason details for the instance fleet.

    - **Code** *(string) --*

      A code corresponding to the reason the state change occurred.

    - **Message** *(string) --*

      An explanatory message.
    """


_ClientListInstanceFleetsResponseInstanceFleetsStatusTimelineTypeDef = TypedDict(
    "_ClientListInstanceFleetsResponseInstanceFleetsStatusTimelineTypeDef",
    {"CreationDateTime": datetime, "ReadyDateTime": datetime, "EndDateTime": datetime},
    total=False,
)


class ClientListInstanceFleetsResponseInstanceFleetsStatusTimelineTypeDef(
    _ClientListInstanceFleetsResponseInstanceFleetsStatusTimelineTypeDef
):
    """
    Type definition for `ClientListInstanceFleetsResponseInstanceFleetsStatus` `Timeline`

    Provides historical timestamps for the instance fleet, including the time of creation,
    the time it became ready to run jobs, and the time of termination.

    - **CreationDateTime** *(datetime) --*

      The time and date the instance fleet was created.

    - **ReadyDateTime** *(datetime) --*

      The time and date the instance fleet was ready to run jobs.

    - **EndDateTime** *(datetime) --*

      The time and date the instance fleet terminated.
    """


_ClientListInstanceFleetsResponseInstanceFleetsStatusTypeDef = TypedDict(
    "_ClientListInstanceFleetsResponseInstanceFleetsStatusTypeDef",
    {
        "State": str,
        "StateChangeReason": ClientListInstanceFleetsResponseInstanceFleetsStatusStateChangeReasonTypeDef,
        "Timeline": ClientListInstanceFleetsResponseInstanceFleetsStatusTimelineTypeDef,
    },
    total=False,
)


class ClientListInstanceFleetsResponseInstanceFleetsStatusTypeDef(
    _ClientListInstanceFleetsResponseInstanceFleetsStatusTypeDef
):
    """
    Type definition for `ClientListInstanceFleetsResponseInstanceFleets` `Status`

    The current status of the instance fleet.

    - **State** *(string) --*

      A code representing the instance fleet status.

      * ``PROVISIONING`` —The instance fleet is provisioning EC2 resources and is not yet
      ready to run jobs.

      * ``BOOTSTRAPPING`` —EC2 instances and other resources have been provisioned and the
      bootstrap actions specified for the instances are underway.

      * ``RUNNING`` —EC2 instances and other resources are running. They are either executing
      jobs or waiting to execute jobs.

      * ``RESIZING`` —A resize operation is underway. EC2 instances are either being added or
      removed.

      * ``SUSPENDED`` —A resize operation could not complete. Existing EC2 instances are
      running, but instances can't be added or removed.

      * ``TERMINATING`` —The instance fleet is terminating EC2 instances.

      * ``TERMINATED`` —The instance fleet is no longer active, and all EC2 instances have
      been terminated.

    - **StateChangeReason** *(dict) --*

      Provides status change reason details for the instance fleet.

      - **Code** *(string) --*

        A code corresponding to the reason the state change occurred.

      - **Message** *(string) --*

        An explanatory message.

    - **Timeline** *(dict) --*

      Provides historical timestamps for the instance fleet, including the time of creation,
      the time it became ready to run jobs, and the time of termination.

      - **CreationDateTime** *(datetime) --*

        The time and date the instance fleet was created.

      - **ReadyDateTime** *(datetime) --*

        The time and date the instance fleet was ready to run jobs.

      - **EndDateTime** *(datetime) --*

        The time and date the instance fleet terminated.
    """


_ClientListInstanceFleetsResponseInstanceFleetsTypeDef = TypedDict(
    "_ClientListInstanceFleetsResponseInstanceFleetsTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": ClientListInstanceFleetsResponseInstanceFleetsStatusTypeDef,
        "InstanceFleetType": str,
        "TargetOnDemandCapacity": int,
        "TargetSpotCapacity": int,
        "ProvisionedOnDemandCapacity": int,
        "ProvisionedSpotCapacity": int,
        "InstanceTypeSpecifications": List[
            ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsTypeDef
        ],
        "LaunchSpecifications": ClientListInstanceFleetsResponseInstanceFleetsLaunchSpecificationsTypeDef,
    },
    total=False,
)


class ClientListInstanceFleetsResponseInstanceFleetsTypeDef(
    _ClientListInstanceFleetsResponseInstanceFleetsTypeDef
):
    """
    Type definition for `ClientListInstanceFleetsResponse` `InstanceFleets`

    Describes an instance fleet, which is a group of EC2 instances that host a particular node
    type (master, core, or task) in an Amazon EMR cluster. Instance fleets can consist of a mix
    of instance types and On-Demand and Spot instances, which are provisioned to meet a defined
    target capacity.

    .. note::

      The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and
      later, excluding 5.0.x versions.

    - **Id** *(string) --*

      The unique identifier of the instance fleet.

    - **Name** *(string) --*

      A friendly name for the instance fleet.

    - **Status** *(dict) --*

      The current status of the instance fleet.

      - **State** *(string) --*

        A code representing the instance fleet status.

        * ``PROVISIONING`` —The instance fleet is provisioning EC2 resources and is not yet
        ready to run jobs.

        * ``BOOTSTRAPPING`` —EC2 instances and other resources have been provisioned and the
        bootstrap actions specified for the instances are underway.

        * ``RUNNING`` —EC2 instances and other resources are running. They are either executing
        jobs or waiting to execute jobs.

        * ``RESIZING`` —A resize operation is underway. EC2 instances are either being added or
        removed.

        * ``SUSPENDED`` —A resize operation could not complete. Existing EC2 instances are
        running, but instances can't be added or removed.

        * ``TERMINATING`` —The instance fleet is terminating EC2 instances.

        * ``TERMINATED`` —The instance fleet is no longer active, and all EC2 instances have
        been terminated.

      - **StateChangeReason** *(dict) --*

        Provides status change reason details for the instance fleet.

        - **Code** *(string) --*

          A code corresponding to the reason the state change occurred.

        - **Message** *(string) --*

          An explanatory message.

      - **Timeline** *(dict) --*

        Provides historical timestamps for the instance fleet, including the time of creation,
        the time it became ready to run jobs, and the time of termination.

        - **CreationDateTime** *(datetime) --*

          The time and date the instance fleet was created.

        - **ReadyDateTime** *(datetime) --*

          The time and date the instance fleet was ready to run jobs.

        - **EndDateTime** *(datetime) --*

          The time and date the instance fleet terminated.

    - **InstanceFleetType** *(string) --*

      The node type that the instance fleet hosts. Valid values are MASTER, CORE, or TASK.

    - **TargetOnDemandCapacity** *(integer) --*

      The target capacity of On-Demand units for the instance fleet, which determines how many
      On-Demand instances to provision. When the instance fleet launches, Amazon EMR tries to
      provision On-Demand instances as specified by  InstanceTypeConfig . Each instance
      configuration has a specified ``WeightedCapacity`` . When an On-Demand instance is
      provisioned, the ``WeightedCapacity`` units count toward the target capacity. Amazon EMR
      provisions instances until the target capacity is totally fulfilled, even if this results
      in an overage. For example, if there are 2 units remaining to fulfill capacity, and
      Amazon EMR can only provision an instance with a ``WeightedCapacity`` of 5 units, the
      instance is provisioned, and the target capacity is exceeded by 3 units. You can use
      InstanceFleet$ProvisionedOnDemandCapacity to determine the Spot capacity units that have
      been provisioned for the instance fleet.

      .. note::

        If not specified or set to 0, only Spot instances are provisioned for the instance
        fleet using ``TargetSpotCapacity`` . At least one of ``TargetSpotCapacity`` and
        ``TargetOnDemandCapacity`` should be greater than 0. For a master instance fleet, only
        one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` can be specified, and its
        value must be 1.

    - **TargetSpotCapacity** *(integer) --*

      The target capacity of Spot units for the instance fleet, which determines how many Spot
      instances to provision. When the instance fleet launches, Amazon EMR tries to provision
      Spot instances as specified by  InstanceTypeConfig . Each instance configuration has a
      specified ``WeightedCapacity`` . When a Spot instance is provisioned, the
      ``WeightedCapacity`` units count toward the target capacity. Amazon EMR provisions
      instances until the target capacity is totally fulfilled, even if this results in an
      overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR
      can only provision an instance with a ``WeightedCapacity`` of 5 units, the instance is
      provisioned, and the target capacity is exceeded by 3 units. You can use
      InstanceFleet$ProvisionedSpotCapacity to determine the Spot capacity units that have been
      provisioned for the instance fleet.

      .. note::

        If not specified or set to 0, only On-Demand instances are provisioned for the instance
        fleet. At least one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` should be
        greater than 0. For a master instance fleet, only one of ``TargetSpotCapacity`` and
        ``TargetOnDemandCapacity`` can be specified, and its value must be 1.

    - **ProvisionedOnDemandCapacity** *(integer) --*

      The number of On-Demand units that have been provisioned for the instance fleet to
      fulfill ``TargetOnDemandCapacity`` . This provisioned capacity might be less than or
      greater than ``TargetOnDemandCapacity`` .

    - **ProvisionedSpotCapacity** *(integer) --*

      The number of Spot units that have been provisioned for this instance fleet to fulfill
      ``TargetSpotCapacity`` . This provisioned capacity might be less than or greater than
      ``TargetSpotCapacity`` .

    - **InstanceTypeSpecifications** *(list) --*

      The specification for the instance types that comprise an instance fleet. Up to five
      unique instance specifications may be defined for each instance fleet.

      - *(dict) --*

        The configuration specification for each instance type in an instance fleet.

        .. note::

          The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and
          later, excluding 5.0.x versions.

        - **InstanceType** *(string) --*

          The EC2 instance type, for example ``m3.xlarge`` .

        - **WeightedCapacity** *(integer) --*

          The number of units that a provisioned instance of this type provides toward
          fulfilling the target capacities defined in  InstanceFleetConfig . Capacity values
          represent performance characteristics such as vCPUs, memory, or I/O. If not
          specified, the default value is 1.

        - **BidPrice** *(string) --*

          The bid price for each EC2 Spot instance type as defined by ``InstanceType`` .
          Expressed in USD.

        - **BidPriceAsPercentageOfOnDemandPrice** *(float) --*

          The bid price, as a percentage of On-Demand price, for each EC2 Spot instance as
          defined by ``InstanceType`` . Expressed as a number (for example, 20 specifies 20%).

        - **Configurations** *(list) --*

          A configuration classification that applies when provisioning cluster instances,
          which can include configurations for applications and software bundled with Amazon
          EMR.

          - *(dict) --*

            .. note::

              Amazon EMR releases 4.x or later.

            An optional configuration specification to be used when provisioning cluster
            instances, which can include configurations for applications and software bundled
            with Amazon EMR. A configuration consists of a classification, properties, and
            optional nested configurations. A classification refers to an application-specific
            configuration file. Properties are the settings you want to change in that file.
            For more information, see `Configuring Applications
            <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

            - **Classification** *(string) --*

              The classification within a configuration.

            - **Configurations** *(list) --*

              A list of additional configurations to apply within a configuration object.

            - **Properties** *(dict) --*

              A set of properties specified within a configuration classification.

              - *(string) --*

                - *(string) --*

        - **EbsBlockDevices** *(list) --*

          The configuration of Amazon Elastic Block Storage (EBS) attached to each instance as
          defined by ``InstanceType`` .

          - *(dict) --*

            Configuration of requested EBS block device associated with the instance group.

            - **VolumeSpecification** *(dict) --*

              EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
              requested for the EBS volume attached to an EC2 instance in the cluster.

              - **VolumeType** *(string) --*

                The volume type. Volume types supported are gp2, io1, standard.

              - **Iops** *(integer) --*

                The number of I/O operations per second (IOPS) that the volume supports.

              - **SizeInGB** *(integer) --*

                The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
                volume type is EBS-optimized, the minimum value is 10.

            - **Device** *(string) --*

              The device name that is exposed to the instance, such as /dev/sdh.

        - **EbsOptimized** *(boolean) --*

          Evaluates to ``TRUE`` when the specified ``InstanceType`` is EBS-optimized.

    - **LaunchSpecifications** *(dict) --*

      Describes the launch specification for an instance fleet.

      - **SpotSpecification** *(dict) --*

        The launch specification for Spot instances in the fleet, which determines the defined
        duration and provisioning timeout behavior.

        - **TimeoutDurationMinutes** *(integer) --*

          The spot provisioning timeout period in minutes. If Spot instances are not
          provisioned within this time period, the ``TimeOutAction`` is taken. Minimum value is
          5 and maximum value is 1440. The timeout applies only during initial provisioning,
          when the cluster is first created.

        - **TimeoutAction** *(string) --*

          The action to take when ``TargetSpotCapacity`` has not been fulfilled when the
          ``TimeoutDurationMinutes`` has expired; that is, when all Spot instances could not be
          provisioned within the Spot provisioning timeout. Valid values are
          ``TERMINATE_CLUSTER`` and ``SWITCH_TO_ON_DEMAND`` . SWITCH_TO_ON_DEMAND specifies
          that if no Spot instances are available, On-Demand Instances should be provisioned to
          fulfill any remaining Spot capacity.

        - **BlockDurationMinutes** *(integer) --*

          The defined duration for Spot instances (also known as Spot blocks) in minutes. When
          specified, the Spot instance does not terminate before the defined duration expires,
          and defined duration pricing for Spot instances applies. Valid values are 60, 120,
          180, 240, 300, or 360. The duration period starts as soon as a Spot instance receives
          its instance ID. At the end of the duration, Amazon EC2 marks the Spot instance for
          termination and provides a Spot instance termination notice, which gives the instance
          a two-minute warning before it terminates.
    """


_ClientListInstanceFleetsResponseTypeDef = TypedDict(
    "_ClientListInstanceFleetsResponseTypeDef",
    {
        "InstanceFleets": List[ClientListInstanceFleetsResponseInstanceFleetsTypeDef],
        "Marker": str,
    },
    total=False,
)


class ClientListInstanceFleetsResponseTypeDef(_ClientListInstanceFleetsResponseTypeDef):
    """
    Type definition for `ClientListInstanceFleets` `Response`

    - **InstanceFleets** *(list) --*

      The list of instance fleets for the cluster and given filters.

      - *(dict) --*

        Describes an instance fleet, which is a group of EC2 instances that host a particular node
        type (master, core, or task) in an Amazon EMR cluster. Instance fleets can consist of a mix
        of instance types and On-Demand and Spot instances, which are provisioned to meet a defined
        target capacity.

        .. note::

          The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and
          later, excluding 5.0.x versions.

        - **Id** *(string) --*

          The unique identifier of the instance fleet.

        - **Name** *(string) --*

          A friendly name for the instance fleet.

        - **Status** *(dict) --*

          The current status of the instance fleet.

          - **State** *(string) --*

            A code representing the instance fleet status.

            * ``PROVISIONING`` —The instance fleet is provisioning EC2 resources and is not yet
            ready to run jobs.

            * ``BOOTSTRAPPING`` —EC2 instances and other resources have been provisioned and the
            bootstrap actions specified for the instances are underway.

            * ``RUNNING`` —EC2 instances and other resources are running. They are either executing
            jobs or waiting to execute jobs.

            * ``RESIZING`` —A resize operation is underway. EC2 instances are either being added or
            removed.

            * ``SUSPENDED`` —A resize operation could not complete. Existing EC2 instances are
            running, but instances can't be added or removed.

            * ``TERMINATING`` —The instance fleet is terminating EC2 instances.

            * ``TERMINATED`` —The instance fleet is no longer active, and all EC2 instances have
            been terminated.

          - **StateChangeReason** *(dict) --*

            Provides status change reason details for the instance fleet.

            - **Code** *(string) --*

              A code corresponding to the reason the state change occurred.

            - **Message** *(string) --*

              An explanatory message.

          - **Timeline** *(dict) --*

            Provides historical timestamps for the instance fleet, including the time of creation,
            the time it became ready to run jobs, and the time of termination.

            - **CreationDateTime** *(datetime) --*

              The time and date the instance fleet was created.

            - **ReadyDateTime** *(datetime) --*

              The time and date the instance fleet was ready to run jobs.

            - **EndDateTime** *(datetime) --*

              The time and date the instance fleet terminated.

        - **InstanceFleetType** *(string) --*

          The node type that the instance fleet hosts. Valid values are MASTER, CORE, or TASK.

        - **TargetOnDemandCapacity** *(integer) --*

          The target capacity of On-Demand units for the instance fleet, which determines how many
          On-Demand instances to provision. When the instance fleet launches, Amazon EMR tries to
          provision On-Demand instances as specified by  InstanceTypeConfig . Each instance
          configuration has a specified ``WeightedCapacity`` . When an On-Demand instance is
          provisioned, the ``WeightedCapacity`` units count toward the target capacity. Amazon EMR
          provisions instances until the target capacity is totally fulfilled, even if this results
          in an overage. For example, if there are 2 units remaining to fulfill capacity, and
          Amazon EMR can only provision an instance with a ``WeightedCapacity`` of 5 units, the
          instance is provisioned, and the target capacity is exceeded by 3 units. You can use
          InstanceFleet$ProvisionedOnDemandCapacity to determine the Spot capacity units that have
          been provisioned for the instance fleet.

          .. note::

            If not specified or set to 0, only Spot instances are provisioned for the instance
            fleet using ``TargetSpotCapacity`` . At least one of ``TargetSpotCapacity`` and
            ``TargetOnDemandCapacity`` should be greater than 0. For a master instance fleet, only
            one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` can be specified, and its
            value must be 1.

        - **TargetSpotCapacity** *(integer) --*

          The target capacity of Spot units for the instance fleet, which determines how many Spot
          instances to provision. When the instance fleet launches, Amazon EMR tries to provision
          Spot instances as specified by  InstanceTypeConfig . Each instance configuration has a
          specified ``WeightedCapacity`` . When a Spot instance is provisioned, the
          ``WeightedCapacity`` units count toward the target capacity. Amazon EMR provisions
          instances until the target capacity is totally fulfilled, even if this results in an
          overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR
          can only provision an instance with a ``WeightedCapacity`` of 5 units, the instance is
          provisioned, and the target capacity is exceeded by 3 units. You can use
          InstanceFleet$ProvisionedSpotCapacity to determine the Spot capacity units that have been
          provisioned for the instance fleet.

          .. note::

            If not specified or set to 0, only On-Demand instances are provisioned for the instance
            fleet. At least one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` should be
            greater than 0. For a master instance fleet, only one of ``TargetSpotCapacity`` and
            ``TargetOnDemandCapacity`` can be specified, and its value must be 1.

        - **ProvisionedOnDemandCapacity** *(integer) --*

          The number of On-Demand units that have been provisioned for the instance fleet to
          fulfill ``TargetOnDemandCapacity`` . This provisioned capacity might be less than or
          greater than ``TargetOnDemandCapacity`` .

        - **ProvisionedSpotCapacity** *(integer) --*

          The number of Spot units that have been provisioned for this instance fleet to fulfill
          ``TargetSpotCapacity`` . This provisioned capacity might be less than or greater than
          ``TargetSpotCapacity`` .

        - **InstanceTypeSpecifications** *(list) --*

          The specification for the instance types that comprise an instance fleet. Up to five
          unique instance specifications may be defined for each instance fleet.

          - *(dict) --*

            The configuration specification for each instance type in an instance fleet.

            .. note::

              The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and
              later, excluding 5.0.x versions.

            - **InstanceType** *(string) --*

              The EC2 instance type, for example ``m3.xlarge`` .

            - **WeightedCapacity** *(integer) --*

              The number of units that a provisioned instance of this type provides toward
              fulfilling the target capacities defined in  InstanceFleetConfig . Capacity values
              represent performance characteristics such as vCPUs, memory, or I/O. If not
              specified, the default value is 1.

            - **BidPrice** *(string) --*

              The bid price for each EC2 Spot instance type as defined by ``InstanceType`` .
              Expressed in USD.

            - **BidPriceAsPercentageOfOnDemandPrice** *(float) --*

              The bid price, as a percentage of On-Demand price, for each EC2 Spot instance as
              defined by ``InstanceType`` . Expressed as a number (for example, 20 specifies 20%).

            - **Configurations** *(list) --*

              A configuration classification that applies when provisioning cluster instances,
              which can include configurations for applications and software bundled with Amazon
              EMR.

              - *(dict) --*

                .. note::

                  Amazon EMR releases 4.x or later.

                An optional configuration specification to be used when provisioning cluster
                instances, which can include configurations for applications and software bundled
                with Amazon EMR. A configuration consists of a classification, properties, and
                optional nested configurations. A classification refers to an application-specific
                configuration file. Properties are the settings you want to change in that file.
                For more information, see `Configuring Applications
                <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

                - **Classification** *(string) --*

                  The classification within a configuration.

                - **Configurations** *(list) --*

                  A list of additional configurations to apply within a configuration object.

                - **Properties** *(dict) --*

                  A set of properties specified within a configuration classification.

                  - *(string) --*

                    - *(string) --*

            - **EbsBlockDevices** *(list) --*

              The configuration of Amazon Elastic Block Storage (EBS) attached to each instance as
              defined by ``InstanceType`` .

              - *(dict) --*

                Configuration of requested EBS block device associated with the instance group.

                - **VolumeSpecification** *(dict) --*

                  EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
                  requested for the EBS volume attached to an EC2 instance in the cluster.

                  - **VolumeType** *(string) --*

                    The volume type. Volume types supported are gp2, io1, standard.

                  - **Iops** *(integer) --*

                    The number of I/O operations per second (IOPS) that the volume supports.

                  - **SizeInGB** *(integer) --*

                    The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
                    volume type is EBS-optimized, the minimum value is 10.

                - **Device** *(string) --*

                  The device name that is exposed to the instance, such as /dev/sdh.

            - **EbsOptimized** *(boolean) --*

              Evaluates to ``TRUE`` when the specified ``InstanceType`` is EBS-optimized.

        - **LaunchSpecifications** *(dict) --*

          Describes the launch specification for an instance fleet.

          - **SpotSpecification** *(dict) --*

            The launch specification for Spot instances in the fleet, which determines the defined
            duration and provisioning timeout behavior.

            - **TimeoutDurationMinutes** *(integer) --*

              The spot provisioning timeout period in minutes. If Spot instances are not
              provisioned within this time period, the ``TimeOutAction`` is taken. Minimum value is
              5 and maximum value is 1440. The timeout applies only during initial provisioning,
              when the cluster is first created.

            - **TimeoutAction** *(string) --*

              The action to take when ``TargetSpotCapacity`` has not been fulfilled when the
              ``TimeoutDurationMinutes`` has expired; that is, when all Spot instances could not be
              provisioned within the Spot provisioning timeout. Valid values are
              ``TERMINATE_CLUSTER`` and ``SWITCH_TO_ON_DEMAND`` . SWITCH_TO_ON_DEMAND specifies
              that if no Spot instances are available, On-Demand Instances should be provisioned to
              fulfill any remaining Spot capacity.

            - **BlockDurationMinutes** *(integer) --*

              The defined duration for Spot instances (also known as Spot blocks) in minutes. When
              specified, the Spot instance does not terminate before the defined duration expires,
              and defined duration pricing for Spot instances applies. Valid values are 60, 120,
              180, 240, 300, or 360. The duration period starts as soon as a Spot instance receives
              its instance ID. At the end of the duration, Amazon EC2 marks the Spot instance for
              termination and provides a Spot instance termination notice, which gives the instance
              a two-minute warning before it terminates.

    - **Marker** *(string) --*

      The pagination token that indicates the next set of results to retrieve.
    """


_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyConstraintsTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyConstraintsTypeDef",
    {"MinCapacity": int, "MaxCapacity": int},
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyConstraintsTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyConstraintsTypeDef
):
    """
    Type definition for `ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicy` `Constraints`

    The upper and lower EC2 instance limits for an automatic scaling policy. Automatic
    scaling activity will not cause an instance group to grow above or below these limits.

    - **MinCapacity** *(integer) --*

      The lower boundary of EC2 instances in an instance group below which scaling
      activities are not allowed to shrink. Scale-in activities will not terminate
      instances below this boundary.

    - **MaxCapacity** *(integer) --*

      The upper boundary of EC2 instances in an instance group beyond which scaling
      activities are not allowed to grow. Scale-out activities will not add instances
      beyond this boundary.
    """


_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    {"AdjustmentType": str, "ScalingAdjustment": int, "CoolDown": int},
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef
):
    """
    Type definition for `ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesAction` `SimpleScalingPolicyConfiguration`

    The type of adjustment the automatic scaling activity makes when triggered, and
    the periodicity of the adjustment.

    - **AdjustmentType** *(string) --*

      The way in which EC2 instances are added (if ``ScalingAdjustment`` is a
      positive number) or terminated (if ``ScalingAdjustment`` is a negative number)
      each time the scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the
      default. ``CHANGE_IN_CAPACITY`` indicates that the EC2 instance count
      increments or decrements by ``ScalingAdjustment`` , which should be expressed
      as an integer. ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count
      increments or decrements by the percentage specified by ``ScalingAdjustment`` ,
      which should be expressed as an integer. For example, 20 indicates an increase
      in 20% increments of cluster capacity. ``EXACT_CAPACITY`` indicates the scaling
      activity results in an instance group with the number of EC2 instances
      specified by ``ScalingAdjustment`` , which should be expressed as a positive
      integer.

    - **ScalingAdjustment** *(integer) --*

      The amount by which to scale in or scale out, based on the specified
      ``AdjustmentType`` . A positive value adds to the instance group's EC2 instance
      count while a negative number removes instances. If ``AdjustmentType`` is set
      to ``EXACT_CAPACITY`` , the number should only be a positive integer. If
      ``AdjustmentType`` is set to ``PERCENT_CHANGE_IN_CAPACITY`` , the value should
      express the percentage as an integer. For example, -20 indicates a decrease in
      20% increments of cluster capacity.

    - **CoolDown** *(integer) --*

      The amount of time, in seconds, after a scaling activity completes before any
      further trigger-related scaling activities can start. The default value is 0.
    """


_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesActionTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesActionTypeDef",
    {
        "Market": str,
        "SimpleScalingPolicyConfiguration": ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef,
    },
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesActionTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesActionTypeDef
):
    """
    Type definition for `ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRules` `Action`

    The conditions that trigger an automatic scaling activity.

    - **Market** *(string) --*

      Not available for instance groups. Instance groups use the market type specified
      for the group.

    - **SimpleScalingPolicyConfiguration** *(dict) --*

      The type of adjustment the automatic scaling activity makes when triggered, and
      the periodicity of the adjustment.

      - **AdjustmentType** *(string) --*

        The way in which EC2 instances are added (if ``ScalingAdjustment`` is a
        positive number) or terminated (if ``ScalingAdjustment`` is a negative number)
        each time the scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the
        default. ``CHANGE_IN_CAPACITY`` indicates that the EC2 instance count
        increments or decrements by ``ScalingAdjustment`` , which should be expressed
        as an integer. ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count
        increments or decrements by the percentage specified by ``ScalingAdjustment`` ,
        which should be expressed as an integer. For example, 20 indicates an increase
        in 20% increments of cluster capacity. ``EXACT_CAPACITY`` indicates the scaling
        activity results in an instance group with the number of EC2 instances
        specified by ``ScalingAdjustment`` , which should be expressed as a positive
        integer.

      - **ScalingAdjustment** *(integer) --*

        The amount by which to scale in or scale out, based on the specified
        ``AdjustmentType`` . A positive value adds to the instance group's EC2 instance
        count while a negative number removes instances. If ``AdjustmentType`` is set
        to ``EXACT_CAPACITY`` , the number should only be a positive integer. If
        ``AdjustmentType`` is set to ``PERCENT_CHANGE_IN_CAPACITY`` , the value should
        express the percentage as an integer. For example, -20 indicates a decrease in
        20% increments of cluster capacity.

      - **CoolDown** *(integer) --*

        The amount of time, in seconds, after a scaling activity completes before any
        further trigger-related scaling activities can start. The default value is 0.
    """


_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef
):
    """
    Type definition for `ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinition` `Dimensions`

    A CloudWatch dimension, which is specified using a ``Key`` (known as a
    ``Name`` in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one
    dimension whose ``Key`` is ``JobFlowID`` and ``Value`` is a variable
    representing the cluster ID, which is ``${emr.clusterId}`` . This enables the
    rule to bootstrap when the cluster ID becomes available.

    - **Key** *(string) --*

      The dimension name.

    - **Value** *(string) --*

      The dimension value.
    """


_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    {
        "ComparisonOperator": str,
        "EvaluationPeriods": int,
        "MetricName": str,
        "Namespace": str,
        "Period": int,
        "Statistic": str,
        "Threshold": float,
        "Unit": str,
        "Dimensions": List[
            ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef
        ],
    },
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef
):
    """
    Type definition for `ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTrigger` `CloudWatchAlarmDefinition`

    The definition of a CloudWatch metric alarm. When the defined alarm conditions
    are met along with other trigger parameters, scaling activity begins.

    - **ComparisonOperator** *(string) --*

      Determines how the metric specified by ``MetricName`` is compared to the value
      specified by ``Threshold`` .

    - **EvaluationPeriods** *(integer) --*

      The number of periods, in five-minute increments, during which the alarm
      condition must exist before the alarm triggers automatic scaling activity. The
      default value is ``1`` .

    - **MetricName** *(string) --*

      The name of the CloudWatch metric that is watched to determine an alarm
      condition.

    - **Namespace** *(string) --*

      The namespace for the CloudWatch metric. The default is
      ``AWS/ElasticMapReduce`` .

    - **Period** *(integer) --*

      The period, in seconds, over which the statistic is applied. EMR CloudWatch
      metrics are emitted every five minutes (300 seconds), so if an EMR CloudWatch
      metric is specified, specify ``300`` .

    - **Statistic** *(string) --*

      The statistic to apply to the metric associated with the alarm. The default is
      ``AVERAGE`` .

    - **Threshold** *(float) --*

      The value against which the specified statistic is compared.

    - **Unit** *(string) --*

      The unit of measure associated with the CloudWatch metric being watched. The
      value specified for ``Unit`` must correspond to the units specified in the
      CloudWatch metric.

    - **Dimensions** *(list) --*

      A CloudWatch metric dimension.

      - *(dict) --*

        A CloudWatch dimension, which is specified using a ``Key`` (known as a
        ``Name`` in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one
        dimension whose ``Key`` is ``JobFlowID`` and ``Value`` is a variable
        representing the cluster ID, which is ``${emr.clusterId}`` . This enables the
        rule to bootstrap when the cluster ID becomes available.

        - **Key** *(string) --*

          The dimension name.

        - **Value** *(string) --*

          The dimension value.
    """


_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef",
    {
        "CloudWatchAlarmDefinition": ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef
    },
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef
):
    """
    Type definition for `ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRules` `Trigger`

    The CloudWatch alarm definition that determines when automatic scaling activity is
    triggered.

    - **CloudWatchAlarmDefinition** *(dict) --*

      The definition of a CloudWatch metric alarm. When the defined alarm conditions
      are met along with other trigger parameters, scaling activity begins.

      - **ComparisonOperator** *(string) --*

        Determines how the metric specified by ``MetricName`` is compared to the value
        specified by ``Threshold`` .

      - **EvaluationPeriods** *(integer) --*

        The number of periods, in five-minute increments, during which the alarm
        condition must exist before the alarm triggers automatic scaling activity. The
        default value is ``1`` .

      - **MetricName** *(string) --*

        The name of the CloudWatch metric that is watched to determine an alarm
        condition.

      - **Namespace** *(string) --*

        The namespace for the CloudWatch metric. The default is
        ``AWS/ElasticMapReduce`` .

      - **Period** *(integer) --*

        The period, in seconds, over which the statistic is applied. EMR CloudWatch
        metrics are emitted every five minutes (300 seconds), so if an EMR CloudWatch
        metric is specified, specify ``300`` .

      - **Statistic** *(string) --*

        The statistic to apply to the metric associated with the alarm. The default is
        ``AVERAGE`` .

      - **Threshold** *(float) --*

        The value against which the specified statistic is compared.

      - **Unit** *(string) --*

        The unit of measure associated with the CloudWatch metric being watched. The
        value specified for ``Unit`` must correspond to the units specified in the
        CloudWatch metric.

      - **Dimensions** *(list) --*

        A CloudWatch metric dimension.

        - *(dict) --*

          A CloudWatch dimension, which is specified using a ``Key`` (known as a
          ``Name`` in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one
          dimension whose ``Key`` is ``JobFlowID`` and ``Value`` is a variable
          representing the cluster ID, which is ``${emr.clusterId}`` . This enables the
          rule to bootstrap when the cluster ID becomes available.

          - **Key** *(string) --*

            The dimension name.

          - **Value** *(string) --*

            The dimension value.
    """


_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTypeDef",
    {
        "Name": str,
        "Description": str,
        "Action": ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesActionTypeDef,
        "Trigger": ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef,
    },
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTypeDef
):
    """
    Type definition for `ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicy` `Rules`

    A scale-in or scale-out rule that defines scaling activity, including the CloudWatch
    metric alarm that triggers activity, how EC2 instances are added or removed, and the
    periodicity of adjustments. The automatic scaling policy for an instance group can
    comprise one or more automatic scaling rules.

    - **Name** *(string) --*

      The name used to identify an automatic scaling rule. Rule names must be unique
      within a scaling policy.

    - **Description** *(string) --*

      A friendly, more verbose description of the automatic scaling rule.

    - **Action** *(dict) --*

      The conditions that trigger an automatic scaling activity.

      - **Market** *(string) --*

        Not available for instance groups. Instance groups use the market type specified
        for the group.

      - **SimpleScalingPolicyConfiguration** *(dict) --*

        The type of adjustment the automatic scaling activity makes when triggered, and
        the periodicity of the adjustment.

        - **AdjustmentType** *(string) --*

          The way in which EC2 instances are added (if ``ScalingAdjustment`` is a
          positive number) or terminated (if ``ScalingAdjustment`` is a negative number)
          each time the scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the
          default. ``CHANGE_IN_CAPACITY`` indicates that the EC2 instance count
          increments or decrements by ``ScalingAdjustment`` , which should be expressed
          as an integer. ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count
          increments or decrements by the percentage specified by ``ScalingAdjustment`` ,
          which should be expressed as an integer. For example, 20 indicates an increase
          in 20% increments of cluster capacity. ``EXACT_CAPACITY`` indicates the scaling
          activity results in an instance group with the number of EC2 instances
          specified by ``ScalingAdjustment`` , which should be expressed as a positive
          integer.

        - **ScalingAdjustment** *(integer) --*

          The amount by which to scale in or scale out, based on the specified
          ``AdjustmentType`` . A positive value adds to the instance group's EC2 instance
          count while a negative number removes instances. If ``AdjustmentType`` is set
          to ``EXACT_CAPACITY`` , the number should only be a positive integer. If
          ``AdjustmentType`` is set to ``PERCENT_CHANGE_IN_CAPACITY`` , the value should
          express the percentage as an integer. For example, -20 indicates a decrease in
          20% increments of cluster capacity.

        - **CoolDown** *(integer) --*

          The amount of time, in seconds, after a scaling activity completes before any
          further trigger-related scaling activities can start. The default value is 0.

    - **Trigger** *(dict) --*

      The CloudWatch alarm definition that determines when automatic scaling activity is
      triggered.

      - **CloudWatchAlarmDefinition** *(dict) --*

        The definition of a CloudWatch metric alarm. When the defined alarm conditions
        are met along with other trigger parameters, scaling activity begins.

        - **ComparisonOperator** *(string) --*

          Determines how the metric specified by ``MetricName`` is compared to the value
          specified by ``Threshold`` .

        - **EvaluationPeriods** *(integer) --*

          The number of periods, in five-minute increments, during which the alarm
          condition must exist before the alarm triggers automatic scaling activity. The
          default value is ``1`` .

        - **MetricName** *(string) --*

          The name of the CloudWatch metric that is watched to determine an alarm
          condition.

        - **Namespace** *(string) --*

          The namespace for the CloudWatch metric. The default is
          ``AWS/ElasticMapReduce`` .

        - **Period** *(integer) --*

          The period, in seconds, over which the statistic is applied. EMR CloudWatch
          metrics are emitted every five minutes (300 seconds), so if an EMR CloudWatch
          metric is specified, specify ``300`` .

        - **Statistic** *(string) --*

          The statistic to apply to the metric associated with the alarm. The default is
          ``AVERAGE`` .

        - **Threshold** *(float) --*

          The value against which the specified statistic is compared.

        - **Unit** *(string) --*

          The unit of measure associated with the CloudWatch metric being watched. The
          value specified for ``Unit`` must correspond to the units specified in the
          CloudWatch metric.

        - **Dimensions** *(list) --*

          A CloudWatch metric dimension.

          - *(dict) --*

            A CloudWatch dimension, which is specified using a ``Key`` (known as a
            ``Name`` in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one
            dimension whose ``Key`` is ``JobFlowID`` and ``Value`` is a variable
            representing the cluster ID, which is ``${emr.clusterId}`` . This enables the
            rule to bootstrap when the cluster ID becomes available.

            - **Key** *(string) --*

              The dimension name.

            - **Value** *(string) --*

              The dimension value.
    """


_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyStatusStateChangeReasonTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyStatusStateChangeReasonTypeDef",
    {"Code": str, "Message": str},
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyStatusStateChangeReasonTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyStatusStateChangeReasonTypeDef
):
    """
    Type definition for `ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyStatus` `StateChangeReason`

    The reason for a change in status.

    - **Code** *(string) --*

      The code indicating the reason for the change in status.``USER_REQUEST`` indicates
      that the scaling policy status was changed by a user. ``PROVISION_FAILURE``
      indicates that the status change was because the policy failed to provision.
      ``CLEANUP_FAILURE`` indicates an error.

    - **Message** *(string) --*

      A friendly, more verbose message that accompanies an automatic scaling policy state
      change.
    """


_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyStatusTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyStatusTypeDef",
    {
        "State": str,
        "StateChangeReason": ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyStatusStateChangeReasonTypeDef,
    },
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyStatusTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyStatusTypeDef
):
    """
    Type definition for `ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicy` `Status`

    The status of an automatic scaling policy.

    - **State** *(string) --*

      Indicates the status of the automatic scaling policy.

    - **StateChangeReason** *(dict) --*

      The reason for a change in status.

      - **Code** *(string) --*

        The code indicating the reason for the change in status.``USER_REQUEST`` indicates
        that the scaling policy status was changed by a user. ``PROVISION_FAILURE``
        indicates that the status change was because the policy failed to provision.
        ``CLEANUP_FAILURE`` indicates an error.

      - **Message** *(string) --*

        A friendly, more verbose message that accompanies an automatic scaling policy state
        change.
    """


_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyTypeDef",
    {
        "Status": ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyStatusTypeDef,
        "Constraints": ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyConstraintsTypeDef,
        "Rules": List[
            ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTypeDef
        ],
    },
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyTypeDef
):
    """
    Type definition for `ClientListInstanceGroupsResponseInstanceGroups` `AutoScalingPolicy`

    An automatic scaling policy for a core instance group or task instance group in an Amazon
    EMR cluster. The automatic scaling policy defines how an instance group dynamically adds
    and terminates EC2 instances in response to the value of a CloudWatch metric. See
    PutAutoScalingPolicy.

    - **Status** *(dict) --*

      The status of an automatic scaling policy.

      - **State** *(string) --*

        Indicates the status of the automatic scaling policy.

      - **StateChangeReason** *(dict) --*

        The reason for a change in status.

        - **Code** *(string) --*

          The code indicating the reason for the change in status.``USER_REQUEST`` indicates
          that the scaling policy status was changed by a user. ``PROVISION_FAILURE``
          indicates that the status change was because the policy failed to provision.
          ``CLEANUP_FAILURE`` indicates an error.

        - **Message** *(string) --*

          A friendly, more verbose message that accompanies an automatic scaling policy state
          change.

    - **Constraints** *(dict) --*

      The upper and lower EC2 instance limits for an automatic scaling policy. Automatic
      scaling activity will not cause an instance group to grow above or below these limits.

      - **MinCapacity** *(integer) --*

        The lower boundary of EC2 instances in an instance group below which scaling
        activities are not allowed to shrink. Scale-in activities will not terminate
        instances below this boundary.

      - **MaxCapacity** *(integer) --*

        The upper boundary of EC2 instances in an instance group beyond which scaling
        activities are not allowed to grow. Scale-out activities will not add instances
        beyond this boundary.

    - **Rules** *(list) --*

      The scale-in and scale-out rules that comprise the automatic scaling policy.

      - *(dict) --*

        A scale-in or scale-out rule that defines scaling activity, including the CloudWatch
        metric alarm that triggers activity, how EC2 instances are added or removed, and the
        periodicity of adjustments. The automatic scaling policy for an instance group can
        comprise one or more automatic scaling rules.

        - **Name** *(string) --*

          The name used to identify an automatic scaling rule. Rule names must be unique
          within a scaling policy.

        - **Description** *(string) --*

          A friendly, more verbose description of the automatic scaling rule.

        - **Action** *(dict) --*

          The conditions that trigger an automatic scaling activity.

          - **Market** *(string) --*

            Not available for instance groups. Instance groups use the market type specified
            for the group.

          - **SimpleScalingPolicyConfiguration** *(dict) --*

            The type of adjustment the automatic scaling activity makes when triggered, and
            the periodicity of the adjustment.

            - **AdjustmentType** *(string) --*

              The way in which EC2 instances are added (if ``ScalingAdjustment`` is a
              positive number) or terminated (if ``ScalingAdjustment`` is a negative number)
              each time the scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the
              default. ``CHANGE_IN_CAPACITY`` indicates that the EC2 instance count
              increments or decrements by ``ScalingAdjustment`` , which should be expressed
              as an integer. ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count
              increments or decrements by the percentage specified by ``ScalingAdjustment`` ,
              which should be expressed as an integer. For example, 20 indicates an increase
              in 20% increments of cluster capacity. ``EXACT_CAPACITY`` indicates the scaling
              activity results in an instance group with the number of EC2 instances
              specified by ``ScalingAdjustment`` , which should be expressed as a positive
              integer.

            - **ScalingAdjustment** *(integer) --*

              The amount by which to scale in or scale out, based on the specified
              ``AdjustmentType`` . A positive value adds to the instance group's EC2 instance
              count while a negative number removes instances. If ``AdjustmentType`` is set
              to ``EXACT_CAPACITY`` , the number should only be a positive integer. If
              ``AdjustmentType`` is set to ``PERCENT_CHANGE_IN_CAPACITY`` , the value should
              express the percentage as an integer. For example, -20 indicates a decrease in
              20% increments of cluster capacity.

            - **CoolDown** *(integer) --*

              The amount of time, in seconds, after a scaling activity completes before any
              further trigger-related scaling activities can start. The default value is 0.

        - **Trigger** *(dict) --*

          The CloudWatch alarm definition that determines when automatic scaling activity is
          triggered.

          - **CloudWatchAlarmDefinition** *(dict) --*

            The definition of a CloudWatch metric alarm. When the defined alarm conditions
            are met along with other trigger parameters, scaling activity begins.

            - **ComparisonOperator** *(string) --*

              Determines how the metric specified by ``MetricName`` is compared to the value
              specified by ``Threshold`` .

            - **EvaluationPeriods** *(integer) --*

              The number of periods, in five-minute increments, during which the alarm
              condition must exist before the alarm triggers automatic scaling activity. The
              default value is ``1`` .

            - **MetricName** *(string) --*

              The name of the CloudWatch metric that is watched to determine an alarm
              condition.

            - **Namespace** *(string) --*

              The namespace for the CloudWatch metric. The default is
              ``AWS/ElasticMapReduce`` .

            - **Period** *(integer) --*

              The period, in seconds, over which the statistic is applied. EMR CloudWatch
              metrics are emitted every five minutes (300 seconds), so if an EMR CloudWatch
              metric is specified, specify ``300`` .

            - **Statistic** *(string) --*

              The statistic to apply to the metric associated with the alarm. The default is
              ``AVERAGE`` .

            - **Threshold** *(float) --*

              The value against which the specified statistic is compared.

            - **Unit** *(string) --*

              The unit of measure associated with the CloudWatch metric being watched. The
              value specified for ``Unit`` must correspond to the units specified in the
              CloudWatch metric.

            - **Dimensions** *(list) --*

              A CloudWatch metric dimension.

              - *(dict) --*

                A CloudWatch dimension, which is specified using a ``Key`` (known as a
                ``Name`` in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one
                dimension whose ``Key`` is ``JobFlowID`` and ``Value`` is a variable
                representing the cluster ID, which is ``${emr.clusterId}`` . This enables the
                rule to bootstrap when the cluster ID becomes available.

                - **Key** *(string) --*

                  The dimension name.

                - **Value** *(string) --*

                  The dimension value.
    """


_ClientListInstanceGroupsResponseInstanceGroupsConfigurationsTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsConfigurationsTypeDef",
    {"Classification": str, "Configurations": List[Any], "Properties": Dict[str, str]},
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsConfigurationsTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsConfigurationsTypeDef
):
    """
    Type definition for `ClientListInstanceGroupsResponseInstanceGroups` `Configurations`

    .. note::

      Amazon EMR releases 4.x or later.

    An optional configuration specification to be used when provisioning cluster instances,
    which can include configurations for applications and software bundled with Amazon EMR.
    A configuration consists of a classification, properties, and optional nested
    configurations. A classification refers to an application-specific configuration file.
    Properties are the settings you want to change in that file. For more information, see
    `Configuring Applications
    <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

    - **Classification** *(string) --*

      The classification within a configuration.

    - **Configurations** *(list) --*

      A list of additional configurations to apply within a configuration object.

    - **Properties** *(dict) --*

      A set of properties specified within a configuration classification.

      - *(string) --*

        - *(string) --*
    """


_ClientListInstanceGroupsResponseInstanceGroupsEbsBlockDevicesVolumeSpecificationTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsEbsBlockDevicesVolumeSpecificationTypeDef",
    {"VolumeType": str, "Iops": int, "SizeInGB": int},
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsEbsBlockDevicesVolumeSpecificationTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsEbsBlockDevicesVolumeSpecificationTypeDef
):
    """
    Type definition for `ClientListInstanceGroupsResponseInstanceGroupsEbsBlockDevices` `VolumeSpecification`

    EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
    requested for the EBS volume attached to an EC2 instance in the cluster.

    - **VolumeType** *(string) --*

      The volume type. Volume types supported are gp2, io1, standard.

    - **Iops** *(integer) --*

      The number of I/O operations per second (IOPS) that the volume supports.

    - **SizeInGB** *(integer) --*

      The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
      volume type is EBS-optimized, the minimum value is 10.
    """


_ClientListInstanceGroupsResponseInstanceGroupsEbsBlockDevicesTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsEbsBlockDevicesTypeDef",
    {
        "VolumeSpecification": ClientListInstanceGroupsResponseInstanceGroupsEbsBlockDevicesVolumeSpecificationTypeDef,
        "Device": str,
    },
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsEbsBlockDevicesTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsEbsBlockDevicesTypeDef
):
    """
    Type definition for `ClientListInstanceGroupsResponseInstanceGroups` `EbsBlockDevices`

    Configuration of requested EBS block device associated with the instance group.

    - **VolumeSpecification** *(dict) --*

      EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
      requested for the EBS volume attached to an EC2 instance in the cluster.

      - **VolumeType** *(string) --*

        The volume type. Volume types supported are gp2, io1, standard.

      - **Iops** *(integer) --*

        The number of I/O operations per second (IOPS) that the volume supports.

      - **SizeInGB** *(integer) --*

        The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
        volume type is EBS-optimized, the minimum value is 10.

    - **Device** *(string) --*

      The device name that is exposed to the instance, such as /dev/sdh.
    """


_ClientListInstanceGroupsResponseInstanceGroupsLastSuccessfullyAppliedConfigurationsTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsLastSuccessfullyAppliedConfigurationsTypeDef",
    {"Classification": str, "Configurations": List[Any], "Properties": Dict[str, str]},
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsLastSuccessfullyAppliedConfigurationsTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsLastSuccessfullyAppliedConfigurationsTypeDef
):
    """
    Type definition for `ClientListInstanceGroupsResponseInstanceGroups` `LastSuccessfullyAppliedConfigurations`

    .. note::

      Amazon EMR releases 4.x or later.

    An optional configuration specification to be used when provisioning cluster instances,
    which can include configurations for applications and software bundled with Amazon EMR.
    A configuration consists of a classification, properties, and optional nested
    configurations. A classification refers to an application-specific configuration file.
    Properties are the settings you want to change in that file. For more information, see
    `Configuring Applications
    <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

    - **Classification** *(string) --*

      The classification within a configuration.

    - **Configurations** *(list) --*

      A list of additional configurations to apply within a configuration object.

    - **Properties** *(dict) --*

      A set of properties specified within a configuration classification.

      - *(string) --*

        - *(string) --*
    """


_ClientListInstanceGroupsResponseInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef",
    {
        "InstancesToTerminate": List[str],
        "InstancesToProtect": List[str],
        "InstanceTerminationTimeout": int,
    },
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef
):
    """
    Type definition for `ClientListInstanceGroupsResponseInstanceGroupsShrinkPolicy` `InstanceResizePolicy`

    Custom policy for requesting termination protection or termination of specific
    instances when shrinking an instance group.

    - **InstancesToTerminate** *(list) --*

      Specific list of instances to be terminated when shrinking an instance group.

      - *(string) --*

    - **InstancesToProtect** *(list) --*

      Specific list of instances to be protected when shrinking an instance group.

      - *(string) --*

    - **InstanceTerminationTimeout** *(integer) --*

      Decommissioning timeout override for the specific list of instances to be terminated.
    """


_ClientListInstanceGroupsResponseInstanceGroupsShrinkPolicyTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsShrinkPolicyTypeDef",
    {
        "DecommissionTimeout": int,
        "InstanceResizePolicy": ClientListInstanceGroupsResponseInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef,
    },
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsShrinkPolicyTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsShrinkPolicyTypeDef
):
    """
    Type definition for `ClientListInstanceGroupsResponseInstanceGroups` `ShrinkPolicy`

    Policy for customizing shrink operations.

    - **DecommissionTimeout** *(integer) --*

      The desired timeout for decommissioning an instance. Overrides the default YARN
      decommissioning timeout.

    - **InstanceResizePolicy** *(dict) --*

      Custom policy for requesting termination protection or termination of specific
      instances when shrinking an instance group.

      - **InstancesToTerminate** *(list) --*

        Specific list of instances to be terminated when shrinking an instance group.

        - *(string) --*

      - **InstancesToProtect** *(list) --*

        Specific list of instances to be protected when shrinking an instance group.

        - *(string) --*

      - **InstanceTerminationTimeout** *(integer) --*

        Decommissioning timeout override for the specific list of instances to be terminated.
    """


_ClientListInstanceGroupsResponseInstanceGroupsStatusStateChangeReasonTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsStatusStateChangeReasonTypeDef",
    {"Code": str, "Message": str},
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsStatusStateChangeReasonTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsStatusStateChangeReasonTypeDef
):
    """
    Type definition for `ClientListInstanceGroupsResponseInstanceGroupsStatus` `StateChangeReason`

    The status change reason details for the instance group.

    - **Code** *(string) --*

      The programmable code for the state change reason.

    - **Message** *(string) --*

      The status change reason description.
    """


_ClientListInstanceGroupsResponseInstanceGroupsStatusTimelineTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsStatusTimelineTypeDef",
    {"CreationDateTime": datetime, "ReadyDateTime": datetime, "EndDateTime": datetime},
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsStatusTimelineTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsStatusTimelineTypeDef
):
    """
    Type definition for `ClientListInstanceGroupsResponseInstanceGroupsStatus` `Timeline`

    The timeline of the instance group status over time.

    - **CreationDateTime** *(datetime) --*

      The creation date and time of the instance group.

    - **ReadyDateTime** *(datetime) --*

      The date and time when the instance group became ready to perform tasks.

    - **EndDateTime** *(datetime) --*

      The date and time when the instance group terminated.
    """


_ClientListInstanceGroupsResponseInstanceGroupsStatusTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsStatusTypeDef",
    {
        "State": str,
        "StateChangeReason": ClientListInstanceGroupsResponseInstanceGroupsStatusStateChangeReasonTypeDef,
        "Timeline": ClientListInstanceGroupsResponseInstanceGroupsStatusTimelineTypeDef,
    },
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsStatusTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsStatusTypeDef
):
    """
    Type definition for `ClientListInstanceGroupsResponseInstanceGroups` `Status`

    The current status of the instance group.

    - **State** *(string) --*

      The current state of the instance group.

    - **StateChangeReason** *(dict) --*

      The status change reason details for the instance group.

      - **Code** *(string) --*

        The programmable code for the state change reason.

      - **Message** *(string) --*

        The status change reason description.

    - **Timeline** *(dict) --*

      The timeline of the instance group status over time.

      - **CreationDateTime** *(datetime) --*

        The creation date and time of the instance group.

      - **ReadyDateTime** *(datetime) --*

        The date and time when the instance group became ready to perform tasks.

      - **EndDateTime** *(datetime) --*

        The date and time when the instance group terminated.
    """


_ClientListInstanceGroupsResponseInstanceGroupsTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseInstanceGroupsTypeDef",
    {
        "Id": str,
        "Name": str,
        "Market": str,
        "InstanceGroupType": str,
        "BidPrice": str,
        "InstanceType": str,
        "RequestedInstanceCount": int,
        "RunningInstanceCount": int,
        "Status": ClientListInstanceGroupsResponseInstanceGroupsStatusTypeDef,
        "Configurations": List[
            ClientListInstanceGroupsResponseInstanceGroupsConfigurationsTypeDef
        ],
        "ConfigurationsVersion": int,
        "LastSuccessfullyAppliedConfigurations": List[
            ClientListInstanceGroupsResponseInstanceGroupsLastSuccessfullyAppliedConfigurationsTypeDef
        ],
        "LastSuccessfullyAppliedConfigurationsVersion": int,
        "EbsBlockDevices": List[
            ClientListInstanceGroupsResponseInstanceGroupsEbsBlockDevicesTypeDef
        ],
        "EbsOptimized": bool,
        "ShrinkPolicy": ClientListInstanceGroupsResponseInstanceGroupsShrinkPolicyTypeDef,
        "AutoScalingPolicy": ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyTypeDef,
    },
    total=False,
)


class ClientListInstanceGroupsResponseInstanceGroupsTypeDef(
    _ClientListInstanceGroupsResponseInstanceGroupsTypeDef
):
    """
    Type definition for `ClientListInstanceGroupsResponse` `InstanceGroups`

    This entity represents an instance group, which is a group of instances that have common
    purpose. For example, CORE instance group is used for HDFS.

    - **Id** *(string) --*

      The identifier of the instance group.

    - **Name** *(string) --*

      The name of the instance group.

    - **Market** *(string) --*

      The marketplace to provision instances for this group. Valid values are ON_DEMAND or SPOT.

    - **InstanceGroupType** *(string) --*

      The type of the instance group. Valid values are MASTER, CORE or TASK.

    - **BidPrice** *(string) --*

      The bid price for each EC2 Spot instance type as defined by ``InstanceType`` . Expressed
      in USD. If neither ``BidPrice`` nor ``BidPriceAsPercentageOfOnDemandPrice`` is provided,
      ``BidPriceAsPercentageOfOnDemandPrice`` defaults to 100%.

    - **InstanceType** *(string) --*

      The EC2 instance type for all instances in the instance group.

    - **RequestedInstanceCount** *(integer) --*

      The target number of instances for the instance group.

    - **RunningInstanceCount** *(integer) --*

      The number of instances currently running in this instance group.

    - **Status** *(dict) --*

      The current status of the instance group.

      - **State** *(string) --*

        The current state of the instance group.

      - **StateChangeReason** *(dict) --*

        The status change reason details for the instance group.

        - **Code** *(string) --*

          The programmable code for the state change reason.

        - **Message** *(string) --*

          The status change reason description.

      - **Timeline** *(dict) --*

        The timeline of the instance group status over time.

        - **CreationDateTime** *(datetime) --*

          The creation date and time of the instance group.

        - **ReadyDateTime** *(datetime) --*

          The date and time when the instance group became ready to perform tasks.

        - **EndDateTime** *(datetime) --*

          The date and time when the instance group terminated.

    - **Configurations** *(list) --*

      .. note::

        Amazon EMR releases 4.x or later.

      The list of configurations supplied for an EMR cluster instance group. You can specify a
      separate configuration for each instance group (master, core, and task).

      - *(dict) --*

        .. note::

          Amazon EMR releases 4.x or later.

        An optional configuration specification to be used when provisioning cluster instances,
        which can include configurations for applications and software bundled with Amazon EMR.
        A configuration consists of a classification, properties, and optional nested
        configurations. A classification refers to an application-specific configuration file.
        Properties are the settings you want to change in that file. For more information, see
        `Configuring Applications
        <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

        - **Classification** *(string) --*

          The classification within a configuration.

        - **Configurations** *(list) --*

          A list of additional configurations to apply within a configuration object.

        - **Properties** *(dict) --*

          A set of properties specified within a configuration classification.

          - *(string) --*

            - *(string) --*

    - **ConfigurationsVersion** *(integer) --*

      The version number of the requested configuration specification for this instance group.

    - **LastSuccessfullyAppliedConfigurations** *(list) --*

      A list of configurations that were successfully applied for an instance group last time.

      - *(dict) --*

        .. note::

          Amazon EMR releases 4.x or later.

        An optional configuration specification to be used when provisioning cluster instances,
        which can include configurations for applications and software bundled with Amazon EMR.
        A configuration consists of a classification, properties, and optional nested
        configurations. A classification refers to an application-specific configuration file.
        Properties are the settings you want to change in that file. For more information, see
        `Configuring Applications
        <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

        - **Classification** *(string) --*

          The classification within a configuration.

        - **Configurations** *(list) --*

          A list of additional configurations to apply within a configuration object.

        - **Properties** *(dict) --*

          A set of properties specified within a configuration classification.

          - *(string) --*

            - *(string) --*

    - **LastSuccessfullyAppliedConfigurationsVersion** *(integer) --*

      The version number of a configuration specification that was successfully applied for an
      instance group last time.

    - **EbsBlockDevices** *(list) --*

      The EBS block devices that are mapped to this instance group.

      - *(dict) --*

        Configuration of requested EBS block device associated with the instance group.

        - **VolumeSpecification** *(dict) --*

          EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
          requested for the EBS volume attached to an EC2 instance in the cluster.

          - **VolumeType** *(string) --*

            The volume type. Volume types supported are gp2, io1, standard.

          - **Iops** *(integer) --*

            The number of I/O operations per second (IOPS) that the volume supports.

          - **SizeInGB** *(integer) --*

            The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
            volume type is EBS-optimized, the minimum value is 10.

        - **Device** *(string) --*

          The device name that is exposed to the instance, such as /dev/sdh.

    - **EbsOptimized** *(boolean) --*

      If the instance group is EBS-optimized. An Amazon EBS-optimized instance uses an
      optimized configuration stack and provides additional, dedicated capacity for Amazon EBS
      I/O.

    - **ShrinkPolicy** *(dict) --*

      Policy for customizing shrink operations.

      - **DecommissionTimeout** *(integer) --*

        The desired timeout for decommissioning an instance. Overrides the default YARN
        decommissioning timeout.

      - **InstanceResizePolicy** *(dict) --*

        Custom policy for requesting termination protection or termination of specific
        instances when shrinking an instance group.

        - **InstancesToTerminate** *(list) --*

          Specific list of instances to be terminated when shrinking an instance group.

          - *(string) --*

        - **InstancesToProtect** *(list) --*

          Specific list of instances to be protected when shrinking an instance group.

          - *(string) --*

        - **InstanceTerminationTimeout** *(integer) --*

          Decommissioning timeout override for the specific list of instances to be terminated.

    - **AutoScalingPolicy** *(dict) --*

      An automatic scaling policy for a core instance group or task instance group in an Amazon
      EMR cluster. The automatic scaling policy defines how an instance group dynamically adds
      and terminates EC2 instances in response to the value of a CloudWatch metric. See
      PutAutoScalingPolicy.

      - **Status** *(dict) --*

        The status of an automatic scaling policy.

        - **State** *(string) --*

          Indicates the status of the automatic scaling policy.

        - **StateChangeReason** *(dict) --*

          The reason for a change in status.

          - **Code** *(string) --*

            The code indicating the reason for the change in status.``USER_REQUEST`` indicates
            that the scaling policy status was changed by a user. ``PROVISION_FAILURE``
            indicates that the status change was because the policy failed to provision.
            ``CLEANUP_FAILURE`` indicates an error.

          - **Message** *(string) --*

            A friendly, more verbose message that accompanies an automatic scaling policy state
            change.

      - **Constraints** *(dict) --*

        The upper and lower EC2 instance limits for an automatic scaling policy. Automatic
        scaling activity will not cause an instance group to grow above or below these limits.

        - **MinCapacity** *(integer) --*

          The lower boundary of EC2 instances in an instance group below which scaling
          activities are not allowed to shrink. Scale-in activities will not terminate
          instances below this boundary.

        - **MaxCapacity** *(integer) --*

          The upper boundary of EC2 instances in an instance group beyond which scaling
          activities are not allowed to grow. Scale-out activities will not add instances
          beyond this boundary.

      - **Rules** *(list) --*

        The scale-in and scale-out rules that comprise the automatic scaling policy.

        - *(dict) --*

          A scale-in or scale-out rule that defines scaling activity, including the CloudWatch
          metric alarm that triggers activity, how EC2 instances are added or removed, and the
          periodicity of adjustments. The automatic scaling policy for an instance group can
          comprise one or more automatic scaling rules.

          - **Name** *(string) --*

            The name used to identify an automatic scaling rule. Rule names must be unique
            within a scaling policy.

          - **Description** *(string) --*

            A friendly, more verbose description of the automatic scaling rule.

          - **Action** *(dict) --*

            The conditions that trigger an automatic scaling activity.

            - **Market** *(string) --*

              Not available for instance groups. Instance groups use the market type specified
              for the group.

            - **SimpleScalingPolicyConfiguration** *(dict) --*

              The type of adjustment the automatic scaling activity makes when triggered, and
              the periodicity of the adjustment.

              - **AdjustmentType** *(string) --*

                The way in which EC2 instances are added (if ``ScalingAdjustment`` is a
                positive number) or terminated (if ``ScalingAdjustment`` is a negative number)
                each time the scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the
                default. ``CHANGE_IN_CAPACITY`` indicates that the EC2 instance count
                increments or decrements by ``ScalingAdjustment`` , which should be expressed
                as an integer. ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count
                increments or decrements by the percentage specified by ``ScalingAdjustment`` ,
                which should be expressed as an integer. For example, 20 indicates an increase
                in 20% increments of cluster capacity. ``EXACT_CAPACITY`` indicates the scaling
                activity results in an instance group with the number of EC2 instances
                specified by ``ScalingAdjustment`` , which should be expressed as a positive
                integer.

              - **ScalingAdjustment** *(integer) --*

                The amount by which to scale in or scale out, based on the specified
                ``AdjustmentType`` . A positive value adds to the instance group's EC2 instance
                count while a negative number removes instances. If ``AdjustmentType`` is set
                to ``EXACT_CAPACITY`` , the number should only be a positive integer. If
                ``AdjustmentType`` is set to ``PERCENT_CHANGE_IN_CAPACITY`` , the value should
                express the percentage as an integer. For example, -20 indicates a decrease in
                20% increments of cluster capacity.

              - **CoolDown** *(integer) --*

                The amount of time, in seconds, after a scaling activity completes before any
                further trigger-related scaling activities can start. The default value is 0.

          - **Trigger** *(dict) --*

            The CloudWatch alarm definition that determines when automatic scaling activity is
            triggered.

            - **CloudWatchAlarmDefinition** *(dict) --*

              The definition of a CloudWatch metric alarm. When the defined alarm conditions
              are met along with other trigger parameters, scaling activity begins.

              - **ComparisonOperator** *(string) --*

                Determines how the metric specified by ``MetricName`` is compared to the value
                specified by ``Threshold`` .

              - **EvaluationPeriods** *(integer) --*

                The number of periods, in five-minute increments, during which the alarm
                condition must exist before the alarm triggers automatic scaling activity. The
                default value is ``1`` .

              - **MetricName** *(string) --*

                The name of the CloudWatch metric that is watched to determine an alarm
                condition.

              - **Namespace** *(string) --*

                The namespace for the CloudWatch metric. The default is
                ``AWS/ElasticMapReduce`` .

              - **Period** *(integer) --*

                The period, in seconds, over which the statistic is applied. EMR CloudWatch
                metrics are emitted every five minutes (300 seconds), so if an EMR CloudWatch
                metric is specified, specify ``300`` .

              - **Statistic** *(string) --*

                The statistic to apply to the metric associated with the alarm. The default is
                ``AVERAGE`` .

              - **Threshold** *(float) --*

                The value against which the specified statistic is compared.

              - **Unit** *(string) --*

                The unit of measure associated with the CloudWatch metric being watched. The
                value specified for ``Unit`` must correspond to the units specified in the
                CloudWatch metric.

              - **Dimensions** *(list) --*

                A CloudWatch metric dimension.

                - *(dict) --*

                  A CloudWatch dimension, which is specified using a ``Key`` (known as a
                  ``Name`` in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one
                  dimension whose ``Key`` is ``JobFlowID`` and ``Value`` is a variable
                  representing the cluster ID, which is ``${emr.clusterId}`` . This enables the
                  rule to bootstrap when the cluster ID becomes available.

                  - **Key** *(string) --*

                    The dimension name.

                  - **Value** *(string) --*

                    The dimension value.
    """


_ClientListInstanceGroupsResponseTypeDef = TypedDict(
    "_ClientListInstanceGroupsResponseTypeDef",
    {
        "InstanceGroups": List[ClientListInstanceGroupsResponseInstanceGroupsTypeDef],
        "Marker": str,
    },
    total=False,
)


class ClientListInstanceGroupsResponseTypeDef(_ClientListInstanceGroupsResponseTypeDef):
    """
    Type definition for `ClientListInstanceGroups` `Response`

    This input determines which instance groups to retrieve.

    - **InstanceGroups** *(list) --*

      The list of instance groups for the cluster and given filters.

      - *(dict) --*

        This entity represents an instance group, which is a group of instances that have common
        purpose. For example, CORE instance group is used for HDFS.

        - **Id** *(string) --*

          The identifier of the instance group.

        - **Name** *(string) --*

          The name of the instance group.

        - **Market** *(string) --*

          The marketplace to provision instances for this group. Valid values are ON_DEMAND or SPOT.

        - **InstanceGroupType** *(string) --*

          The type of the instance group. Valid values are MASTER, CORE or TASK.

        - **BidPrice** *(string) --*

          The bid price for each EC2 Spot instance type as defined by ``InstanceType`` . Expressed
          in USD. If neither ``BidPrice`` nor ``BidPriceAsPercentageOfOnDemandPrice`` is provided,
          ``BidPriceAsPercentageOfOnDemandPrice`` defaults to 100%.

        - **InstanceType** *(string) --*

          The EC2 instance type for all instances in the instance group.

        - **RequestedInstanceCount** *(integer) --*

          The target number of instances for the instance group.

        - **RunningInstanceCount** *(integer) --*

          The number of instances currently running in this instance group.

        - **Status** *(dict) --*

          The current status of the instance group.

          - **State** *(string) --*

            The current state of the instance group.

          - **StateChangeReason** *(dict) --*

            The status change reason details for the instance group.

            - **Code** *(string) --*

              The programmable code for the state change reason.

            - **Message** *(string) --*

              The status change reason description.

          - **Timeline** *(dict) --*

            The timeline of the instance group status over time.

            - **CreationDateTime** *(datetime) --*

              The creation date and time of the instance group.

            - **ReadyDateTime** *(datetime) --*

              The date and time when the instance group became ready to perform tasks.

            - **EndDateTime** *(datetime) --*

              The date and time when the instance group terminated.

        - **Configurations** *(list) --*

          .. note::

            Amazon EMR releases 4.x or later.

          The list of configurations supplied for an EMR cluster instance group. You can specify a
          separate configuration for each instance group (master, core, and task).

          - *(dict) --*

            .. note::

              Amazon EMR releases 4.x or later.

            An optional configuration specification to be used when provisioning cluster instances,
            which can include configurations for applications and software bundled with Amazon EMR.
            A configuration consists of a classification, properties, and optional nested
            configurations. A classification refers to an application-specific configuration file.
            Properties are the settings you want to change in that file. For more information, see
            `Configuring Applications
            <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

            - **Classification** *(string) --*

              The classification within a configuration.

            - **Configurations** *(list) --*

              A list of additional configurations to apply within a configuration object.

            - **Properties** *(dict) --*

              A set of properties specified within a configuration classification.

              - *(string) --*

                - *(string) --*

        - **ConfigurationsVersion** *(integer) --*

          The version number of the requested configuration specification for this instance group.

        - **LastSuccessfullyAppliedConfigurations** *(list) --*

          A list of configurations that were successfully applied for an instance group last time.

          - *(dict) --*

            .. note::

              Amazon EMR releases 4.x or later.

            An optional configuration specification to be used when provisioning cluster instances,
            which can include configurations for applications and software bundled with Amazon EMR.
            A configuration consists of a classification, properties, and optional nested
            configurations. A classification refers to an application-specific configuration file.
            Properties are the settings you want to change in that file. For more information, see
            `Configuring Applications
            <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

            - **Classification** *(string) --*

              The classification within a configuration.

            - **Configurations** *(list) --*

              A list of additional configurations to apply within a configuration object.

            - **Properties** *(dict) --*

              A set of properties specified within a configuration classification.

              - *(string) --*

                - *(string) --*

        - **LastSuccessfullyAppliedConfigurationsVersion** *(integer) --*

          The version number of a configuration specification that was successfully applied for an
          instance group last time.

        - **EbsBlockDevices** *(list) --*

          The EBS block devices that are mapped to this instance group.

          - *(dict) --*

            Configuration of requested EBS block device associated with the instance group.

            - **VolumeSpecification** *(dict) --*

              EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
              requested for the EBS volume attached to an EC2 instance in the cluster.

              - **VolumeType** *(string) --*

                The volume type. Volume types supported are gp2, io1, standard.

              - **Iops** *(integer) --*

                The number of I/O operations per second (IOPS) that the volume supports.

              - **SizeInGB** *(integer) --*

                The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
                volume type is EBS-optimized, the minimum value is 10.

            - **Device** *(string) --*

              The device name that is exposed to the instance, such as /dev/sdh.

        - **EbsOptimized** *(boolean) --*

          If the instance group is EBS-optimized. An Amazon EBS-optimized instance uses an
          optimized configuration stack and provides additional, dedicated capacity for Amazon EBS
          I/O.

        - **ShrinkPolicy** *(dict) --*

          Policy for customizing shrink operations.

          - **DecommissionTimeout** *(integer) --*

            The desired timeout for decommissioning an instance. Overrides the default YARN
            decommissioning timeout.

          - **InstanceResizePolicy** *(dict) --*

            Custom policy for requesting termination protection or termination of specific
            instances when shrinking an instance group.

            - **InstancesToTerminate** *(list) --*

              Specific list of instances to be terminated when shrinking an instance group.

              - *(string) --*

            - **InstancesToProtect** *(list) --*

              Specific list of instances to be protected when shrinking an instance group.

              - *(string) --*

            - **InstanceTerminationTimeout** *(integer) --*

              Decommissioning timeout override for the specific list of instances to be terminated.

        - **AutoScalingPolicy** *(dict) --*

          An automatic scaling policy for a core instance group or task instance group in an Amazon
          EMR cluster. The automatic scaling policy defines how an instance group dynamically adds
          and terminates EC2 instances in response to the value of a CloudWatch metric. See
          PutAutoScalingPolicy.

          - **Status** *(dict) --*

            The status of an automatic scaling policy.

            - **State** *(string) --*

              Indicates the status of the automatic scaling policy.

            - **StateChangeReason** *(dict) --*

              The reason for a change in status.

              - **Code** *(string) --*

                The code indicating the reason for the change in status.``USER_REQUEST`` indicates
                that the scaling policy status was changed by a user. ``PROVISION_FAILURE``
                indicates that the status change was because the policy failed to provision.
                ``CLEANUP_FAILURE`` indicates an error.

              - **Message** *(string) --*

                A friendly, more verbose message that accompanies an automatic scaling policy state
                change.

          - **Constraints** *(dict) --*

            The upper and lower EC2 instance limits for an automatic scaling policy. Automatic
            scaling activity will not cause an instance group to grow above or below these limits.

            - **MinCapacity** *(integer) --*

              The lower boundary of EC2 instances in an instance group below which scaling
              activities are not allowed to shrink. Scale-in activities will not terminate
              instances below this boundary.

            - **MaxCapacity** *(integer) --*

              The upper boundary of EC2 instances in an instance group beyond which scaling
              activities are not allowed to grow. Scale-out activities will not add instances
              beyond this boundary.

          - **Rules** *(list) --*

            The scale-in and scale-out rules that comprise the automatic scaling policy.

            - *(dict) --*

              A scale-in or scale-out rule that defines scaling activity, including the CloudWatch
              metric alarm that triggers activity, how EC2 instances are added or removed, and the
              periodicity of adjustments. The automatic scaling policy for an instance group can
              comprise one or more automatic scaling rules.

              - **Name** *(string) --*

                The name used to identify an automatic scaling rule. Rule names must be unique
                within a scaling policy.

              - **Description** *(string) --*

                A friendly, more verbose description of the automatic scaling rule.

              - **Action** *(dict) --*

                The conditions that trigger an automatic scaling activity.

                - **Market** *(string) --*

                  Not available for instance groups. Instance groups use the market type specified
                  for the group.

                - **SimpleScalingPolicyConfiguration** *(dict) --*

                  The type of adjustment the automatic scaling activity makes when triggered, and
                  the periodicity of the adjustment.

                  - **AdjustmentType** *(string) --*

                    The way in which EC2 instances are added (if ``ScalingAdjustment`` is a
                    positive number) or terminated (if ``ScalingAdjustment`` is a negative number)
                    each time the scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the
                    default. ``CHANGE_IN_CAPACITY`` indicates that the EC2 instance count
                    increments or decrements by ``ScalingAdjustment`` , which should be expressed
                    as an integer. ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count
                    increments or decrements by the percentage specified by ``ScalingAdjustment`` ,
                    which should be expressed as an integer. For example, 20 indicates an increase
                    in 20% increments of cluster capacity. ``EXACT_CAPACITY`` indicates the scaling
                    activity results in an instance group with the number of EC2 instances
                    specified by ``ScalingAdjustment`` , which should be expressed as a positive
                    integer.

                  - **ScalingAdjustment** *(integer) --*

                    The amount by which to scale in or scale out, based on the specified
                    ``AdjustmentType`` . A positive value adds to the instance group's EC2 instance
                    count while a negative number removes instances. If ``AdjustmentType`` is set
                    to ``EXACT_CAPACITY`` , the number should only be a positive integer. If
                    ``AdjustmentType`` is set to ``PERCENT_CHANGE_IN_CAPACITY`` , the value should
                    express the percentage as an integer. For example, -20 indicates a decrease in
                    20% increments of cluster capacity.

                  - **CoolDown** *(integer) --*

                    The amount of time, in seconds, after a scaling activity completes before any
                    further trigger-related scaling activities can start. The default value is 0.

              - **Trigger** *(dict) --*

                The CloudWatch alarm definition that determines when automatic scaling activity is
                triggered.

                - **CloudWatchAlarmDefinition** *(dict) --*

                  The definition of a CloudWatch metric alarm. When the defined alarm conditions
                  are met along with other trigger parameters, scaling activity begins.

                  - **ComparisonOperator** *(string) --*

                    Determines how the metric specified by ``MetricName`` is compared to the value
                    specified by ``Threshold`` .

                  - **EvaluationPeriods** *(integer) --*

                    The number of periods, in five-minute increments, during which the alarm
                    condition must exist before the alarm triggers automatic scaling activity. The
                    default value is ``1`` .

                  - **MetricName** *(string) --*

                    The name of the CloudWatch metric that is watched to determine an alarm
                    condition.

                  - **Namespace** *(string) --*

                    The namespace for the CloudWatch metric. The default is
                    ``AWS/ElasticMapReduce`` .

                  - **Period** *(integer) --*

                    The period, in seconds, over which the statistic is applied. EMR CloudWatch
                    metrics are emitted every five minutes (300 seconds), so if an EMR CloudWatch
                    metric is specified, specify ``300`` .

                  - **Statistic** *(string) --*

                    The statistic to apply to the metric associated with the alarm. The default is
                    ``AVERAGE`` .

                  - **Threshold** *(float) --*

                    The value against which the specified statistic is compared.

                  - **Unit** *(string) --*

                    The unit of measure associated with the CloudWatch metric being watched. The
                    value specified for ``Unit`` must correspond to the units specified in the
                    CloudWatch metric.

                  - **Dimensions** *(list) --*

                    A CloudWatch metric dimension.

                    - *(dict) --*

                      A CloudWatch dimension, which is specified using a ``Key`` (known as a
                      ``Name`` in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one
                      dimension whose ``Key`` is ``JobFlowID`` and ``Value`` is a variable
                      representing the cluster ID, which is ``${emr.clusterId}`` . This enables the
                      rule to bootstrap when the cluster ID becomes available.

                      - **Key** *(string) --*

                        The dimension name.

                      - **Value** *(string) --*

                        The dimension value.

    - **Marker** *(string) --*

      The pagination token that indicates the next set of results to retrieve.
    """


_ClientListInstancesResponseInstancesEbsVolumesTypeDef = TypedDict(
    "_ClientListInstancesResponseInstancesEbsVolumesTypeDef",
    {"Device": str, "VolumeId": str},
    total=False,
)


class ClientListInstancesResponseInstancesEbsVolumesTypeDef(
    _ClientListInstancesResponseInstancesEbsVolumesTypeDef
):
    """
    Type definition for `ClientListInstancesResponseInstances` `EbsVolumes`

    EBS block device that's attached to an EC2 instance.

    - **Device** *(string) --*

      The device name that is exposed to the instance, such as /dev/sdh.

    - **VolumeId** *(string) --*

      The volume identifier of the EBS volume.
    """


_ClientListInstancesResponseInstancesStatusStateChangeReasonTypeDef = TypedDict(
    "_ClientListInstancesResponseInstancesStatusStateChangeReasonTypeDef",
    {"Code": str, "Message": str},
    total=False,
)


class ClientListInstancesResponseInstancesStatusStateChangeReasonTypeDef(
    _ClientListInstancesResponseInstancesStatusStateChangeReasonTypeDef
):
    """
    Type definition for `ClientListInstancesResponseInstancesStatus` `StateChangeReason`

    The details of the status change reason for the instance.

    - **Code** *(string) --*

      The programmable code for the state change reason.

    - **Message** *(string) --*

      The status change reason description.
    """


_ClientListInstancesResponseInstancesStatusTimelineTypeDef = TypedDict(
    "_ClientListInstancesResponseInstancesStatusTimelineTypeDef",
    {"CreationDateTime": datetime, "ReadyDateTime": datetime, "EndDateTime": datetime},
    total=False,
)


class ClientListInstancesResponseInstancesStatusTimelineTypeDef(
    _ClientListInstancesResponseInstancesStatusTimelineTypeDef
):
    """
    Type definition for `ClientListInstancesResponseInstancesStatus` `Timeline`

    The timeline of the instance status over time.

    - **CreationDateTime** *(datetime) --*

      The creation date and time of the instance.

    - **ReadyDateTime** *(datetime) --*

      The date and time when the instance was ready to perform tasks.

    - **EndDateTime** *(datetime) --*

      The date and time when the instance was terminated.
    """


_ClientListInstancesResponseInstancesStatusTypeDef = TypedDict(
    "_ClientListInstancesResponseInstancesStatusTypeDef",
    {
        "State": str,
        "StateChangeReason": ClientListInstancesResponseInstancesStatusStateChangeReasonTypeDef,
        "Timeline": ClientListInstancesResponseInstancesStatusTimelineTypeDef,
    },
    total=False,
)


class ClientListInstancesResponseInstancesStatusTypeDef(
    _ClientListInstancesResponseInstancesStatusTypeDef
):
    """
    Type definition for `ClientListInstancesResponseInstances` `Status`

    The current status of the instance.

    - **State** *(string) --*

      The current state of the instance.

    - **StateChangeReason** *(dict) --*

      The details of the status change reason for the instance.

      - **Code** *(string) --*

        The programmable code for the state change reason.

      - **Message** *(string) --*

        The status change reason description.

    - **Timeline** *(dict) --*

      The timeline of the instance status over time.

      - **CreationDateTime** *(datetime) --*

        The creation date and time of the instance.

      - **ReadyDateTime** *(datetime) --*

        The date and time when the instance was ready to perform tasks.

      - **EndDateTime** *(datetime) --*

        The date and time when the instance was terminated.
    """


_ClientListInstancesResponseInstancesTypeDef = TypedDict(
    "_ClientListInstancesResponseInstancesTypeDef",
    {
        "Id": str,
        "Ec2InstanceId": str,
        "PublicDnsName": str,
        "PublicIpAddress": str,
        "PrivateDnsName": str,
        "PrivateIpAddress": str,
        "Status": ClientListInstancesResponseInstancesStatusTypeDef,
        "InstanceGroupId": str,
        "InstanceFleetId": str,
        "Market": str,
        "InstanceType": str,
        "EbsVolumes": List[ClientListInstancesResponseInstancesEbsVolumesTypeDef],
    },
    total=False,
)


class ClientListInstancesResponseInstancesTypeDef(
    _ClientListInstancesResponseInstancesTypeDef
):
    """
    Type definition for `ClientListInstancesResponse` `Instances`

    Represents an EC2 instance provisioned as part of cluster.

    - **Id** *(string) --*

      The unique identifier for the instance in Amazon EMR.

    - **Ec2InstanceId** *(string) --*

      The unique identifier of the instance in Amazon EC2.

    - **PublicDnsName** *(string) --*

      The public DNS name of the instance.

    - **PublicIpAddress** *(string) --*

      The public IP address of the instance.

    - **PrivateDnsName** *(string) --*

      The private DNS name of the instance.

    - **PrivateIpAddress** *(string) --*

      The private IP address of the instance.

    - **Status** *(dict) --*

      The current status of the instance.

      - **State** *(string) --*

        The current state of the instance.

      - **StateChangeReason** *(dict) --*

        The details of the status change reason for the instance.

        - **Code** *(string) --*

          The programmable code for the state change reason.

        - **Message** *(string) --*

          The status change reason description.

      - **Timeline** *(dict) --*

        The timeline of the instance status over time.

        - **CreationDateTime** *(datetime) --*

          The creation date and time of the instance.

        - **ReadyDateTime** *(datetime) --*

          The date and time when the instance was ready to perform tasks.

        - **EndDateTime** *(datetime) --*

          The date and time when the instance was terminated.

    - **InstanceGroupId** *(string) --*

      The identifier of the instance group to which this instance belongs.

    - **InstanceFleetId** *(string) --*

      The unique identifier of the instance fleet to which an EC2 instance belongs.

    - **Market** *(string) --*

      The instance purchasing option. Valid values are ``ON_DEMAND`` or ``SPOT`` .

    - **InstanceType** *(string) --*

      The EC2 instance type, for example ``m3.xlarge`` .

    - **EbsVolumes** *(list) --*

      The list of EBS volumes that are attached to this instance.

      - *(dict) --*

        EBS block device that's attached to an EC2 instance.

        - **Device** *(string) --*

          The device name that is exposed to the instance, such as /dev/sdh.

        - **VolumeId** *(string) --*

          The volume identifier of the EBS volume.
    """


_ClientListInstancesResponseTypeDef = TypedDict(
    "_ClientListInstancesResponseTypeDef",
    {"Instances": List[ClientListInstancesResponseInstancesTypeDef], "Marker": str},
    total=False,
)


class ClientListInstancesResponseTypeDef(_ClientListInstancesResponseTypeDef):
    """
    Type definition for `ClientListInstances` `Response`

    This output contains the list of instances.

    - **Instances** *(list) --*

      The list of instances for the cluster and given filters.

      - *(dict) --*

        Represents an EC2 instance provisioned as part of cluster.

        - **Id** *(string) --*

          The unique identifier for the instance in Amazon EMR.

        - **Ec2InstanceId** *(string) --*

          The unique identifier of the instance in Amazon EC2.

        - **PublicDnsName** *(string) --*

          The public DNS name of the instance.

        - **PublicIpAddress** *(string) --*

          The public IP address of the instance.

        - **PrivateDnsName** *(string) --*

          The private DNS name of the instance.

        - **PrivateIpAddress** *(string) --*

          The private IP address of the instance.

        - **Status** *(dict) --*

          The current status of the instance.

          - **State** *(string) --*

            The current state of the instance.

          - **StateChangeReason** *(dict) --*

            The details of the status change reason for the instance.

            - **Code** *(string) --*

              The programmable code for the state change reason.

            - **Message** *(string) --*

              The status change reason description.

          - **Timeline** *(dict) --*

            The timeline of the instance status over time.

            - **CreationDateTime** *(datetime) --*

              The creation date and time of the instance.

            - **ReadyDateTime** *(datetime) --*

              The date and time when the instance was ready to perform tasks.

            - **EndDateTime** *(datetime) --*

              The date and time when the instance was terminated.

        - **InstanceGroupId** *(string) --*

          The identifier of the instance group to which this instance belongs.

        - **InstanceFleetId** *(string) --*

          The unique identifier of the instance fleet to which an EC2 instance belongs.

        - **Market** *(string) --*

          The instance purchasing option. Valid values are ``ON_DEMAND`` or ``SPOT`` .

        - **InstanceType** *(string) --*

          The EC2 instance type, for example ``m3.xlarge`` .

        - **EbsVolumes** *(list) --*

          The list of EBS volumes that are attached to this instance.

          - *(dict) --*

            EBS block device that's attached to an EC2 instance.

            - **Device** *(string) --*

              The device name that is exposed to the instance, such as /dev/sdh.

            - **VolumeId** *(string) --*

              The volume identifier of the EBS volume.

    - **Marker** *(string) --*

      The pagination token that indicates the next set of results to retrieve.
    """


_ClientListSecurityConfigurationsResponseSecurityConfigurationsTypeDef = TypedDict(
    "_ClientListSecurityConfigurationsResponseSecurityConfigurationsTypeDef",
    {"Name": str, "CreationDateTime": datetime},
    total=False,
)


class ClientListSecurityConfigurationsResponseSecurityConfigurationsTypeDef(
    _ClientListSecurityConfigurationsResponseSecurityConfigurationsTypeDef
):
    """
    Type definition for `ClientListSecurityConfigurationsResponse` `SecurityConfigurations`

    The creation date and time, and name, of a security configuration.

    - **Name** *(string) --*

      The name of the security configuration.

    - **CreationDateTime** *(datetime) --*

      The date and time the security configuration was created.
    """


_ClientListSecurityConfigurationsResponseTypeDef = TypedDict(
    "_ClientListSecurityConfigurationsResponseTypeDef",
    {
        "SecurityConfigurations": List[
            ClientListSecurityConfigurationsResponseSecurityConfigurationsTypeDef
        ],
        "Marker": str,
    },
    total=False,
)


class ClientListSecurityConfigurationsResponseTypeDef(
    _ClientListSecurityConfigurationsResponseTypeDef
):
    """
    Type definition for `ClientListSecurityConfigurations` `Response`

    - **SecurityConfigurations** *(list) --*

      The creation date and time, and name, of each security configuration.

      - *(dict) --*

        The creation date and time, and name, of a security configuration.

        - **Name** *(string) --*

          The name of the security configuration.

        - **CreationDateTime** *(datetime) --*

          The date and time the security configuration was created.

    - **Marker** *(string) --*

      A pagination token that indicates the next set of results to retrieve. Include the marker in
      the next ListSecurityConfiguration call to retrieve the next page of results, if required.
    """


_ClientListStepsResponseStepsConfigTypeDef = TypedDict(
    "_ClientListStepsResponseStepsConfigTypeDef",
    {"Jar": str, "Properties": Dict[str, str], "MainClass": str, "Args": List[str]},
    total=False,
)


class ClientListStepsResponseStepsConfigTypeDef(
    _ClientListStepsResponseStepsConfigTypeDef
):
    """
    Type definition for `ClientListStepsResponseSteps` `Config`

    The Hadoop job configuration of the cluster step.

    - **Jar** *(string) --*

      The path to the JAR file that runs during the step.

    - **Properties** *(dict) --*

      The list of Java properties that are set when the step runs. You can use these
      properties to pass key value pairs to your main function.

      - *(string) --*

        - *(string) --*

    - **MainClass** *(string) --*

      The name of the main class in the specified Java file. If not specified, the JAR file
      should specify a main class in its manifest file.

    - **Args** *(list) --*

      The list of command line arguments to pass to the JAR file's main function for
      execution.

      - *(string) --*
    """


_ClientListStepsResponseStepsStatusFailureDetailsTypeDef = TypedDict(
    "_ClientListStepsResponseStepsStatusFailureDetailsTypeDef",
    {"Reason": str, "Message": str, "LogFile": str},
    total=False,
)


class ClientListStepsResponseStepsStatusFailureDetailsTypeDef(
    _ClientListStepsResponseStepsStatusFailureDetailsTypeDef
):
    """
    Type definition for `ClientListStepsResponseStepsStatus` `FailureDetails`

    The details for the step failure including reason, message, and log file path where the
    root cause was identified.

    - **Reason** *(string) --*

      The reason for the step failure. In the case where the service cannot successfully
      determine the root cause of the failure, it returns "Unknown Error" as a reason.

    - **Message** *(string) --*

      The descriptive message including the error the EMR service has identified as the
      cause of step failure. This is text from an error log that describes the root cause
      of the failure.

    - **LogFile** *(string) --*

      The path to the log file where the step failure root cause was originally recorded.
    """


_ClientListStepsResponseStepsStatusStateChangeReasonTypeDef = TypedDict(
    "_ClientListStepsResponseStepsStatusStateChangeReasonTypeDef",
    {"Code": str, "Message": str},
    total=False,
)


class ClientListStepsResponseStepsStatusStateChangeReasonTypeDef(
    _ClientListStepsResponseStepsStatusStateChangeReasonTypeDef
):
    """
    Type definition for `ClientListStepsResponseStepsStatus` `StateChangeReason`

    The reason for the step execution status change.

    - **Code** *(string) --*

      The programmable code for the state change reason. Note: Currently, the service
      provides no code for the state change.

    - **Message** *(string) --*

      The descriptive message for the state change reason.
    """


_ClientListStepsResponseStepsStatusTimelineTypeDef = TypedDict(
    "_ClientListStepsResponseStepsStatusTimelineTypeDef",
    {"CreationDateTime": datetime, "StartDateTime": datetime, "EndDateTime": datetime},
    total=False,
)


class ClientListStepsResponseStepsStatusTimelineTypeDef(
    _ClientListStepsResponseStepsStatusTimelineTypeDef
):
    """
    Type definition for `ClientListStepsResponseStepsStatus` `Timeline`

    The timeline of the cluster step status over time.

    - **CreationDateTime** *(datetime) --*

      The date and time when the cluster step was created.

    - **StartDateTime** *(datetime) --*

      The date and time when the cluster step execution started.

    - **EndDateTime** *(datetime) --*

      The date and time when the cluster step execution completed or failed.
    """


_ClientListStepsResponseStepsStatusTypeDef = TypedDict(
    "_ClientListStepsResponseStepsStatusTypeDef",
    {
        "State": str,
        "StateChangeReason": ClientListStepsResponseStepsStatusStateChangeReasonTypeDef,
        "FailureDetails": ClientListStepsResponseStepsStatusFailureDetailsTypeDef,
        "Timeline": ClientListStepsResponseStepsStatusTimelineTypeDef,
    },
    total=False,
)


class ClientListStepsResponseStepsStatusTypeDef(
    _ClientListStepsResponseStepsStatusTypeDef
):
    """
    Type definition for `ClientListStepsResponseSteps` `Status`

    The current execution status details of the cluster step.

    - **State** *(string) --*

      The execution state of the cluster step.

    - **StateChangeReason** *(dict) --*

      The reason for the step execution status change.

      - **Code** *(string) --*

        The programmable code for the state change reason. Note: Currently, the service
        provides no code for the state change.

      - **Message** *(string) --*

        The descriptive message for the state change reason.

    - **FailureDetails** *(dict) --*

      The details for the step failure including reason, message, and log file path where the
      root cause was identified.

      - **Reason** *(string) --*

        The reason for the step failure. In the case where the service cannot successfully
        determine the root cause of the failure, it returns "Unknown Error" as a reason.

      - **Message** *(string) --*

        The descriptive message including the error the EMR service has identified as the
        cause of step failure. This is text from an error log that describes the root cause
        of the failure.

      - **LogFile** *(string) --*

        The path to the log file where the step failure root cause was originally recorded.

    - **Timeline** *(dict) --*

      The timeline of the cluster step status over time.

      - **CreationDateTime** *(datetime) --*

        The date and time when the cluster step was created.

      - **StartDateTime** *(datetime) --*

        The date and time when the cluster step execution started.

      - **EndDateTime** *(datetime) --*

        The date and time when the cluster step execution completed or failed.
    """


_ClientListStepsResponseStepsTypeDef = TypedDict(
    "_ClientListStepsResponseStepsTypeDef",
    {
        "Id": str,
        "Name": str,
        "Config": ClientListStepsResponseStepsConfigTypeDef,
        "ActionOnFailure": str,
        "Status": ClientListStepsResponseStepsStatusTypeDef,
    },
    total=False,
)


class ClientListStepsResponseStepsTypeDef(_ClientListStepsResponseStepsTypeDef):
    """
    Type definition for `ClientListStepsResponse` `Steps`

    The summary of the cluster step.

    - **Id** *(string) --*

      The identifier of the cluster step.

    - **Name** *(string) --*

      The name of the cluster step.

    - **Config** *(dict) --*

      The Hadoop job configuration of the cluster step.

      - **Jar** *(string) --*

        The path to the JAR file that runs during the step.

      - **Properties** *(dict) --*

        The list of Java properties that are set when the step runs. You can use these
        properties to pass key value pairs to your main function.

        - *(string) --*

          - *(string) --*

      - **MainClass** *(string) --*

        The name of the main class in the specified Java file. If not specified, the JAR file
        should specify a main class in its manifest file.

      - **Args** *(list) --*

        The list of command line arguments to pass to the JAR file's main function for
        execution.

        - *(string) --*

    - **ActionOnFailure** *(string) --*

      The action to take when the cluster step fails. Possible values are TERMINATE_CLUSTER,
      CANCEL_AND_WAIT, and CONTINUE. TERMINATE_JOB_FLOW is available for backward
      compatibility. We recommend using TERMINATE_CLUSTER instead.

    - **Status** *(dict) --*

      The current execution status details of the cluster step.

      - **State** *(string) --*

        The execution state of the cluster step.

      - **StateChangeReason** *(dict) --*

        The reason for the step execution status change.

        - **Code** *(string) --*

          The programmable code for the state change reason. Note: Currently, the service
          provides no code for the state change.

        - **Message** *(string) --*

          The descriptive message for the state change reason.

      - **FailureDetails** *(dict) --*

        The details for the step failure including reason, message, and log file path where the
        root cause was identified.

        - **Reason** *(string) --*

          The reason for the step failure. In the case where the service cannot successfully
          determine the root cause of the failure, it returns "Unknown Error" as a reason.

        - **Message** *(string) --*

          The descriptive message including the error the EMR service has identified as the
          cause of step failure. This is text from an error log that describes the root cause
          of the failure.

        - **LogFile** *(string) --*

          The path to the log file where the step failure root cause was originally recorded.

      - **Timeline** *(dict) --*

        The timeline of the cluster step status over time.

        - **CreationDateTime** *(datetime) --*

          The date and time when the cluster step was created.

        - **StartDateTime** *(datetime) --*

          The date and time when the cluster step execution started.

        - **EndDateTime** *(datetime) --*

          The date and time when the cluster step execution completed or failed.
    """


_ClientListStepsResponseTypeDef = TypedDict(
    "_ClientListStepsResponseTypeDef",
    {"Steps": List[ClientListStepsResponseStepsTypeDef], "Marker": str},
    total=False,
)


class ClientListStepsResponseTypeDef(_ClientListStepsResponseTypeDef):
    """
    Type definition for `ClientListSteps` `Response`

    This output contains the list of steps returned in reverse order. This means that the last step
    is the first element in the list.

    - **Steps** *(list) --*

      The filtered list of steps for the cluster.

      - *(dict) --*

        The summary of the cluster step.

        - **Id** *(string) --*

          The identifier of the cluster step.

        - **Name** *(string) --*

          The name of the cluster step.

        - **Config** *(dict) --*

          The Hadoop job configuration of the cluster step.

          - **Jar** *(string) --*

            The path to the JAR file that runs during the step.

          - **Properties** *(dict) --*

            The list of Java properties that are set when the step runs. You can use these
            properties to pass key value pairs to your main function.

            - *(string) --*

              - *(string) --*

          - **MainClass** *(string) --*

            The name of the main class in the specified Java file. If not specified, the JAR file
            should specify a main class in its manifest file.

          - **Args** *(list) --*

            The list of command line arguments to pass to the JAR file's main function for
            execution.

            - *(string) --*

        - **ActionOnFailure** *(string) --*

          The action to take when the cluster step fails. Possible values are TERMINATE_CLUSTER,
          CANCEL_AND_WAIT, and CONTINUE. TERMINATE_JOB_FLOW is available for backward
          compatibility. We recommend using TERMINATE_CLUSTER instead.

        - **Status** *(dict) --*

          The current execution status details of the cluster step.

          - **State** *(string) --*

            The execution state of the cluster step.

          - **StateChangeReason** *(dict) --*

            The reason for the step execution status change.

            - **Code** *(string) --*

              The programmable code for the state change reason. Note: Currently, the service
              provides no code for the state change.

            - **Message** *(string) --*

              The descriptive message for the state change reason.

          - **FailureDetails** *(dict) --*

            The details for the step failure including reason, message, and log file path where the
            root cause was identified.

            - **Reason** *(string) --*

              The reason for the step failure. In the case where the service cannot successfully
              determine the root cause of the failure, it returns "Unknown Error" as a reason.

            - **Message** *(string) --*

              The descriptive message including the error the EMR service has identified as the
              cause of step failure. This is text from an error log that describes the root cause
              of the failure.

            - **LogFile** *(string) --*

              The path to the log file where the step failure root cause was originally recorded.

          - **Timeline** *(dict) --*

            The timeline of the cluster step status over time.

            - **CreationDateTime** *(datetime) --*

              The date and time when the cluster step was created.

            - **StartDateTime** *(datetime) --*

              The date and time when the cluster step execution started.

            - **EndDateTime** *(datetime) --*

              The date and time when the cluster step execution completed or failed.

    - **Marker** *(string) --*

      The pagination token that indicates the next set of results to retrieve.
    """


_RequiredClientModifyInstanceFleetInstanceFleetTypeDef = TypedDict(
    "_RequiredClientModifyInstanceFleetInstanceFleetTypeDef", {"InstanceFleetId": str}
)
_OptionalClientModifyInstanceFleetInstanceFleetTypeDef = TypedDict(
    "_OptionalClientModifyInstanceFleetInstanceFleetTypeDef",
    {"TargetOnDemandCapacity": int, "TargetSpotCapacity": int},
    total=False,
)


class ClientModifyInstanceFleetInstanceFleetTypeDef(
    _RequiredClientModifyInstanceFleetInstanceFleetTypeDef,
    _OptionalClientModifyInstanceFleetInstanceFleetTypeDef,
):
    """
    Type definition for `ClientModifyInstanceFleet` `InstanceFleet`

    The unique identifier of the instance fleet.

    - **InstanceFleetId** *(string) --* **[REQUIRED]**

      A unique identifier for the instance fleet.

    - **TargetOnDemandCapacity** *(integer) --*

      The target capacity of On-Demand units for the instance fleet. For more information see
      InstanceFleetConfig$TargetOnDemandCapacity .

    - **TargetSpotCapacity** *(integer) --*

      The target capacity of Spot units for the instance fleet. For more information, see
      InstanceFleetConfig$TargetSpotCapacity .
    """


_ClientModifyInstanceGroupsInstanceGroupsConfigurationsTypeDef = TypedDict(
    "_ClientModifyInstanceGroupsInstanceGroupsConfigurationsTypeDef",
    {"Classification": str, "Configurations": List[Any], "Properties": Dict[str, str]},
    total=False,
)


class ClientModifyInstanceGroupsInstanceGroupsConfigurationsTypeDef(
    _ClientModifyInstanceGroupsInstanceGroupsConfigurationsTypeDef
):
    """
    Type definition for `ClientModifyInstanceGroupsInstanceGroups` `Configurations`

    .. note::

      Amazon EMR releases 4.x or later.

    An optional configuration specification to be used when provisioning cluster instances,
    which can include configurations for applications and software bundled with Amazon EMR. A
    configuration consists of a classification, properties, and optional nested configurations.
    A classification refers to an application-specific configuration file. Properties are the
    settings you want to change in that file. For more information, see `Configuring
    Applications
    <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

    - **Classification** *(string) --*

      The classification within a configuration.

    - **Configurations** *(list) --*

      A list of additional configurations to apply within a configuration object.

    - **Properties** *(dict) --*

      A set of properties specified within a configuration classification.

      - *(string) --*

        - *(string) --*
    """


_ClientModifyInstanceGroupsInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef = TypedDict(
    "_ClientModifyInstanceGroupsInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef",
    {
        "InstancesToTerminate": List[str],
        "InstancesToProtect": List[str],
        "InstanceTerminationTimeout": int,
    },
    total=False,
)


class ClientModifyInstanceGroupsInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef(
    _ClientModifyInstanceGroupsInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef
):
    """
    Type definition for `ClientModifyInstanceGroupsInstanceGroupsShrinkPolicy` `InstanceResizePolicy`

    Custom policy for requesting termination protection or termination of specific instances
    when shrinking an instance group.

    - **InstancesToTerminate** *(list) --*

      Specific list of instances to be terminated when shrinking an instance group.

      - *(string) --*

    - **InstancesToProtect** *(list) --*

      Specific list of instances to be protected when shrinking an instance group.

      - *(string) --*

    - **InstanceTerminationTimeout** *(integer) --*

      Decommissioning timeout override for the specific list of instances to be terminated.
    """


_ClientModifyInstanceGroupsInstanceGroupsShrinkPolicyTypeDef = TypedDict(
    "_ClientModifyInstanceGroupsInstanceGroupsShrinkPolicyTypeDef",
    {
        "DecommissionTimeout": int,
        "InstanceResizePolicy": ClientModifyInstanceGroupsInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef,
    },
    total=False,
)


class ClientModifyInstanceGroupsInstanceGroupsShrinkPolicyTypeDef(
    _ClientModifyInstanceGroupsInstanceGroupsShrinkPolicyTypeDef
):
    """
    Type definition for `ClientModifyInstanceGroupsInstanceGroups` `ShrinkPolicy`

    Policy for customizing shrink operations.

    - **DecommissionTimeout** *(integer) --*

      The desired timeout for decommissioning an instance. Overrides the default YARN
      decommissioning timeout.

    - **InstanceResizePolicy** *(dict) --*

      Custom policy for requesting termination protection or termination of specific instances
      when shrinking an instance group.

      - **InstancesToTerminate** *(list) --*

        Specific list of instances to be terminated when shrinking an instance group.

        - *(string) --*

      - **InstancesToProtect** *(list) --*

        Specific list of instances to be protected when shrinking an instance group.

        - *(string) --*

      - **InstanceTerminationTimeout** *(integer) --*

        Decommissioning timeout override for the specific list of instances to be terminated.
    """


_RequiredClientModifyInstanceGroupsInstanceGroupsTypeDef = TypedDict(
    "_RequiredClientModifyInstanceGroupsInstanceGroupsTypeDef", {"InstanceGroupId": str}
)
_OptionalClientModifyInstanceGroupsInstanceGroupsTypeDef = TypedDict(
    "_OptionalClientModifyInstanceGroupsInstanceGroupsTypeDef",
    {
        "InstanceCount": int,
        "EC2InstanceIdsToTerminate": List[str],
        "ShrinkPolicy": ClientModifyInstanceGroupsInstanceGroupsShrinkPolicyTypeDef,
        "Configurations": List[
            ClientModifyInstanceGroupsInstanceGroupsConfigurationsTypeDef
        ],
    },
    total=False,
)


class ClientModifyInstanceGroupsInstanceGroupsTypeDef(
    _RequiredClientModifyInstanceGroupsInstanceGroupsTypeDef,
    _OptionalClientModifyInstanceGroupsInstanceGroupsTypeDef,
):
    """
    Type definition for `ClientModifyInstanceGroups` `InstanceGroups`

    Modify the size or configurations of an instance group.

    - **InstanceGroupId** *(string) --* **[REQUIRED]**

      Unique ID of the instance group to expand or shrink.

    - **InstanceCount** *(integer) --*

      Target size for the instance group.

    - **EC2InstanceIdsToTerminate** *(list) --*

      The EC2 InstanceIds to terminate. After you terminate the instances, the instance group will
      not return to its original requested size.

      - *(string) --*

    - **ShrinkPolicy** *(dict) --*

      Policy for customizing shrink operations.

      - **DecommissionTimeout** *(integer) --*

        The desired timeout for decommissioning an instance. Overrides the default YARN
        decommissioning timeout.

      - **InstanceResizePolicy** *(dict) --*

        Custom policy for requesting termination protection or termination of specific instances
        when shrinking an instance group.

        - **InstancesToTerminate** *(list) --*

          Specific list of instances to be terminated when shrinking an instance group.

          - *(string) --*

        - **InstancesToProtect** *(list) --*

          Specific list of instances to be protected when shrinking an instance group.

          - *(string) --*

        - **InstanceTerminationTimeout** *(integer) --*

          Decommissioning timeout override for the specific list of instances to be terminated.

    - **Configurations** *(list) --*

      A list of new or modified configurations to apply for an instance group.

      - *(dict) --*

        .. note::

          Amazon EMR releases 4.x or later.

        An optional configuration specification to be used when provisioning cluster instances,
        which can include configurations for applications and software bundled with Amazon EMR. A
        configuration consists of a classification, properties, and optional nested configurations.
        A classification refers to an application-specific configuration file. Properties are the
        settings you want to change in that file. For more information, see `Configuring
        Applications
        <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

        - **Classification** *(string) --*

          The classification within a configuration.

        - **Configurations** *(list) --*

          A list of additional configurations to apply within a configuration object.

        - **Properties** *(dict) --*

          A set of properties specified within a configuration classification.

          - *(string) --*

            - *(string) --*
    """


_ClientPutAutoScalingPolicyAutoScalingPolicyConstraintsTypeDef = TypedDict(
    "_ClientPutAutoScalingPolicyAutoScalingPolicyConstraintsTypeDef",
    {"MinCapacity": int, "MaxCapacity": int},
)


class ClientPutAutoScalingPolicyAutoScalingPolicyConstraintsTypeDef(
    _ClientPutAutoScalingPolicyAutoScalingPolicyConstraintsTypeDef
):
    """
    Type definition for `ClientPutAutoScalingPolicyAutoScalingPolicy` `Constraints`

    The upper and lower EC2 instance limits for an automatic scaling policy. Automatic scaling
    activity will not cause an instance group to grow above or below these limits.

    - **MinCapacity** *(integer) --* **[REQUIRED]**

      The lower boundary of EC2 instances in an instance group below which scaling activities are
      not allowed to shrink. Scale-in activities will not terminate instances below this boundary.

    - **MaxCapacity** *(integer) --* **[REQUIRED]**

      The upper boundary of EC2 instances in an instance group beyond which scaling activities are
      not allowed to grow. Scale-out activities will not add instances beyond this boundary.
    """


_RequiredClientPutAutoScalingPolicyAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef = TypedDict(
    "_RequiredClientPutAutoScalingPolicyAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    {"ScalingAdjustment": int},
)
_OptionalClientPutAutoScalingPolicyAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef = TypedDict(
    "_OptionalClientPutAutoScalingPolicyAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    {"AdjustmentType": str, "CoolDown": int},
    total=False,
)


class ClientPutAutoScalingPolicyAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef(
    _RequiredClientPutAutoScalingPolicyAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef,
    _OptionalClientPutAutoScalingPolicyAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef,
):
    """
    Type definition for `ClientPutAutoScalingPolicyAutoScalingPolicyRulesAction` `SimpleScalingPolicyConfiguration`

    The type of adjustment the automatic scaling activity makes when triggered, and the
    periodicity of the adjustment.

    - **AdjustmentType** *(string) --*

      The way in which EC2 instances are added (if ``ScalingAdjustment`` is a positive
      number) or terminated (if ``ScalingAdjustment`` is a negative number) each time the
      scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the default.
      ``CHANGE_IN_CAPACITY`` indicates that the EC2 instance count increments or decrements
      by ``ScalingAdjustment`` , which should be expressed as an integer.
      ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count increments or decrements by
      the percentage specified by ``ScalingAdjustment`` , which should be expressed as an
      integer. For example, 20 indicates an increase in 20% increments of cluster capacity.
      ``EXACT_CAPACITY`` indicates the scaling activity results in an instance group with the
      number of EC2 instances specified by ``ScalingAdjustment`` , which should be expressed
      as a positive integer.

    - **ScalingAdjustment** *(integer) --* **[REQUIRED]**

      The amount by which to scale in or scale out, based on the specified ``AdjustmentType``
      . A positive value adds to the instance group's EC2 instance count while a negative
      number removes instances. If ``AdjustmentType`` is set to ``EXACT_CAPACITY`` , the
      number should only be a positive integer. If ``AdjustmentType`` is set to
      ``PERCENT_CHANGE_IN_CAPACITY`` , the value should express the percentage as an integer.
      For example, -20 indicates a decrease in 20% increments of cluster capacity.

    - **CoolDown** *(integer) --*

      The amount of time, in seconds, after a scaling activity completes before any further
      trigger-related scaling activities can start. The default value is 0.
    """


_RequiredClientPutAutoScalingPolicyAutoScalingPolicyRulesActionTypeDef = TypedDict(
    "_RequiredClientPutAutoScalingPolicyAutoScalingPolicyRulesActionTypeDef",
    {
        "SimpleScalingPolicyConfiguration": ClientPutAutoScalingPolicyAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef
    },
)
_OptionalClientPutAutoScalingPolicyAutoScalingPolicyRulesActionTypeDef = TypedDict(
    "_OptionalClientPutAutoScalingPolicyAutoScalingPolicyRulesActionTypeDef",
    {"Market": str},
    total=False,
)


class ClientPutAutoScalingPolicyAutoScalingPolicyRulesActionTypeDef(
    _RequiredClientPutAutoScalingPolicyAutoScalingPolicyRulesActionTypeDef,
    _OptionalClientPutAutoScalingPolicyAutoScalingPolicyRulesActionTypeDef,
):
    """
    Type definition for `ClientPutAutoScalingPolicyAutoScalingPolicyRules` `Action`

    The conditions that trigger an automatic scaling activity.

    - **Market** *(string) --*

      Not available for instance groups. Instance groups use the market type specified for the
      group.

    - **SimpleScalingPolicyConfiguration** *(dict) --* **[REQUIRED]**

      The type of adjustment the automatic scaling activity makes when triggered, and the
      periodicity of the adjustment.

      - **AdjustmentType** *(string) --*

        The way in which EC2 instances are added (if ``ScalingAdjustment`` is a positive
        number) or terminated (if ``ScalingAdjustment`` is a negative number) each time the
        scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the default.
        ``CHANGE_IN_CAPACITY`` indicates that the EC2 instance count increments or decrements
        by ``ScalingAdjustment`` , which should be expressed as an integer.
        ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count increments or decrements by
        the percentage specified by ``ScalingAdjustment`` , which should be expressed as an
        integer. For example, 20 indicates an increase in 20% increments of cluster capacity.
        ``EXACT_CAPACITY`` indicates the scaling activity results in an instance group with the
        number of EC2 instances specified by ``ScalingAdjustment`` , which should be expressed
        as a positive integer.

      - **ScalingAdjustment** *(integer) --* **[REQUIRED]**

        The amount by which to scale in or scale out, based on the specified ``AdjustmentType``
        . A positive value adds to the instance group's EC2 instance count while a negative
        number removes instances. If ``AdjustmentType`` is set to ``EXACT_CAPACITY`` , the
        number should only be a positive integer. If ``AdjustmentType`` is set to
        ``PERCENT_CHANGE_IN_CAPACITY`` , the value should express the percentage as an integer.
        For example, -20 indicates a decrease in 20% increments of cluster capacity.

      - **CoolDown** *(integer) --*

        The amount of time, in seconds, after a scaling activity completes before any further
        trigger-related scaling activities can start. The default value is 0.
    """


_ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef = TypedDict(
    "_ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef(
    _ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef
):
    """
    Type definition for `ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinition` `Dimensions`

    A CloudWatch dimension, which is specified using a ``Key`` (known as a ``Name`` in
    CloudWatch), ``Value`` pair. By default, Amazon EMR uses one dimension whose ``Key``
    is ``JobFlowID`` and ``Value`` is a variable representing the cluster ID, which is
    ``${emr.clusterId}`` . This enables the rule to bootstrap when the cluster ID becomes
    available.

    - **Key** *(string) --*

      The dimension name.

    - **Value** *(string) --*

      The dimension value.
    """


_RequiredClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef = TypedDict(
    "_RequiredClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    {"ComparisonOperator": str, "MetricName": str, "Period": int, "Threshold": float},
)
_OptionalClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef = TypedDict(
    "_OptionalClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    {
        "EvaluationPeriods": int,
        "Namespace": str,
        "Statistic": str,
        "Unit": str,
        "Dimensions": List[
            ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef
        ],
    },
    total=False,
)


class ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef(
    _RequiredClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef,
    _OptionalClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef,
):
    """
    Type definition for `ClientPutAutoScalingPolicyAutoScalingPolicyRulesTrigger` `CloudWatchAlarmDefinition`

    The definition of a CloudWatch metric alarm. When the defined alarm conditions are met
    along with other trigger parameters, scaling activity begins.

    - **ComparisonOperator** *(string) --* **[REQUIRED]**

      Determines how the metric specified by ``MetricName`` is compared to the value
      specified by ``Threshold`` .

    - **EvaluationPeriods** *(integer) --*

      The number of periods, in five-minute increments, during which the alarm condition must
      exist before the alarm triggers automatic scaling activity. The default value is ``1`` .

    - **MetricName** *(string) --* **[REQUIRED]**

      The name of the CloudWatch metric that is watched to determine an alarm condition.

    - **Namespace** *(string) --*

      The namespace for the CloudWatch metric. The default is ``AWS/ElasticMapReduce`` .

    - **Period** *(integer) --* **[REQUIRED]**

      The period, in seconds, over which the statistic is applied. EMR CloudWatch metrics are
      emitted every five minutes (300 seconds), so if an EMR CloudWatch metric is specified,
      specify ``300`` .

    - **Statistic** *(string) --*

      The statistic to apply to the metric associated with the alarm. The default is
      ``AVERAGE`` .

    - **Threshold** *(float) --* **[REQUIRED]**

      The value against which the specified statistic is compared.

    - **Unit** *(string) --*

      The unit of measure associated with the CloudWatch metric being watched. The value
      specified for ``Unit`` must correspond to the units specified in the CloudWatch metric.

    - **Dimensions** *(list) --*

      A CloudWatch metric dimension.

      - *(dict) --*

        A CloudWatch dimension, which is specified using a ``Key`` (known as a ``Name`` in
        CloudWatch), ``Value`` pair. By default, Amazon EMR uses one dimension whose ``Key``
        is ``JobFlowID`` and ``Value`` is a variable representing the cluster ID, which is
        ``${emr.clusterId}`` . This enables the rule to bootstrap when the cluster ID becomes
        available.

        - **Key** *(string) --*

          The dimension name.

        - **Value** *(string) --*

          The dimension value.
    """


_ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerTypeDef = TypedDict(
    "_ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerTypeDef",
    {
        "CloudWatchAlarmDefinition": ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef
    },
)


class ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerTypeDef(
    _ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerTypeDef
):
    """
    Type definition for `ClientPutAutoScalingPolicyAutoScalingPolicyRules` `Trigger`

    The CloudWatch alarm definition that determines when automatic scaling activity is
    triggered.

    - **CloudWatchAlarmDefinition** *(dict) --* **[REQUIRED]**

      The definition of a CloudWatch metric alarm. When the defined alarm conditions are met
      along with other trigger parameters, scaling activity begins.

      - **ComparisonOperator** *(string) --* **[REQUIRED]**

        Determines how the metric specified by ``MetricName`` is compared to the value
        specified by ``Threshold`` .

      - **EvaluationPeriods** *(integer) --*

        The number of periods, in five-minute increments, during which the alarm condition must
        exist before the alarm triggers automatic scaling activity. The default value is ``1`` .

      - **MetricName** *(string) --* **[REQUIRED]**

        The name of the CloudWatch metric that is watched to determine an alarm condition.

      - **Namespace** *(string) --*

        The namespace for the CloudWatch metric. The default is ``AWS/ElasticMapReduce`` .

      - **Period** *(integer) --* **[REQUIRED]**

        The period, in seconds, over which the statistic is applied. EMR CloudWatch metrics are
        emitted every five minutes (300 seconds), so if an EMR CloudWatch metric is specified,
        specify ``300`` .

      - **Statistic** *(string) --*

        The statistic to apply to the metric associated with the alarm. The default is
        ``AVERAGE`` .

      - **Threshold** *(float) --* **[REQUIRED]**

        The value against which the specified statistic is compared.

      - **Unit** *(string) --*

        The unit of measure associated with the CloudWatch metric being watched. The value
        specified for ``Unit`` must correspond to the units specified in the CloudWatch metric.

      - **Dimensions** *(list) --*

        A CloudWatch metric dimension.

        - *(dict) --*

          A CloudWatch dimension, which is specified using a ``Key`` (known as a ``Name`` in
          CloudWatch), ``Value`` pair. By default, Amazon EMR uses one dimension whose ``Key``
          is ``JobFlowID`` and ``Value`` is a variable representing the cluster ID, which is
          ``${emr.clusterId}`` . This enables the rule to bootstrap when the cluster ID becomes
          available.

          - **Key** *(string) --*

            The dimension name.

          - **Value** *(string) --*

            The dimension value.
    """


_RequiredClientPutAutoScalingPolicyAutoScalingPolicyRulesTypeDef = TypedDict(
    "_RequiredClientPutAutoScalingPolicyAutoScalingPolicyRulesTypeDef",
    {
        "Name": str,
        "Action": ClientPutAutoScalingPolicyAutoScalingPolicyRulesActionTypeDef,
        "Trigger": ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerTypeDef,
    },
)
_OptionalClientPutAutoScalingPolicyAutoScalingPolicyRulesTypeDef = TypedDict(
    "_OptionalClientPutAutoScalingPolicyAutoScalingPolicyRulesTypeDef",
    {"Description": str},
    total=False,
)


class ClientPutAutoScalingPolicyAutoScalingPolicyRulesTypeDef(
    _RequiredClientPutAutoScalingPolicyAutoScalingPolicyRulesTypeDef,
    _OptionalClientPutAutoScalingPolicyAutoScalingPolicyRulesTypeDef,
):
    """
    Type definition for `ClientPutAutoScalingPolicyAutoScalingPolicy` `Rules`

    A scale-in or scale-out rule that defines scaling activity, including the CloudWatch metric
    alarm that triggers activity, how EC2 instances are added or removed, and the periodicity of
    adjustments. The automatic scaling policy for an instance group can comprise one or more
    automatic scaling rules.

    - **Name** *(string) --* **[REQUIRED]**

      The name used to identify an automatic scaling rule. Rule names must be unique within a
      scaling policy.

    - **Description** *(string) --*

      A friendly, more verbose description of the automatic scaling rule.

    - **Action** *(dict) --* **[REQUIRED]**

      The conditions that trigger an automatic scaling activity.

      - **Market** *(string) --*

        Not available for instance groups. Instance groups use the market type specified for the
        group.

      - **SimpleScalingPolicyConfiguration** *(dict) --* **[REQUIRED]**

        The type of adjustment the automatic scaling activity makes when triggered, and the
        periodicity of the adjustment.

        - **AdjustmentType** *(string) --*

          The way in which EC2 instances are added (if ``ScalingAdjustment`` is a positive
          number) or terminated (if ``ScalingAdjustment`` is a negative number) each time the
          scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the default.
          ``CHANGE_IN_CAPACITY`` indicates that the EC2 instance count increments or decrements
          by ``ScalingAdjustment`` , which should be expressed as an integer.
          ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count increments or decrements by
          the percentage specified by ``ScalingAdjustment`` , which should be expressed as an
          integer. For example, 20 indicates an increase in 20% increments of cluster capacity.
          ``EXACT_CAPACITY`` indicates the scaling activity results in an instance group with the
          number of EC2 instances specified by ``ScalingAdjustment`` , which should be expressed
          as a positive integer.

        - **ScalingAdjustment** *(integer) --* **[REQUIRED]**

          The amount by which to scale in or scale out, based on the specified ``AdjustmentType``
          . A positive value adds to the instance group's EC2 instance count while a negative
          number removes instances. If ``AdjustmentType`` is set to ``EXACT_CAPACITY`` , the
          number should only be a positive integer. If ``AdjustmentType`` is set to
          ``PERCENT_CHANGE_IN_CAPACITY`` , the value should express the percentage as an integer.
          For example, -20 indicates a decrease in 20% increments of cluster capacity.

        - **CoolDown** *(integer) --*

          The amount of time, in seconds, after a scaling activity completes before any further
          trigger-related scaling activities can start. The default value is 0.

    - **Trigger** *(dict) --* **[REQUIRED]**

      The CloudWatch alarm definition that determines when automatic scaling activity is
      triggered.

      - **CloudWatchAlarmDefinition** *(dict) --* **[REQUIRED]**

        The definition of a CloudWatch metric alarm. When the defined alarm conditions are met
        along with other trigger parameters, scaling activity begins.

        - **ComparisonOperator** *(string) --* **[REQUIRED]**

          Determines how the metric specified by ``MetricName`` is compared to the value
          specified by ``Threshold`` .

        - **EvaluationPeriods** *(integer) --*

          The number of periods, in five-minute increments, during which the alarm condition must
          exist before the alarm triggers automatic scaling activity. The default value is ``1`` .

        - **MetricName** *(string) --* **[REQUIRED]**

          The name of the CloudWatch metric that is watched to determine an alarm condition.

        - **Namespace** *(string) --*

          The namespace for the CloudWatch metric. The default is ``AWS/ElasticMapReduce`` .

        - **Period** *(integer) --* **[REQUIRED]**

          The period, in seconds, over which the statistic is applied. EMR CloudWatch metrics are
          emitted every five minutes (300 seconds), so if an EMR CloudWatch metric is specified,
          specify ``300`` .

        - **Statistic** *(string) --*

          The statistic to apply to the metric associated with the alarm. The default is
          ``AVERAGE`` .

        - **Threshold** *(float) --* **[REQUIRED]**

          The value against which the specified statistic is compared.

        - **Unit** *(string) --*

          The unit of measure associated with the CloudWatch metric being watched. The value
          specified for ``Unit`` must correspond to the units specified in the CloudWatch metric.

        - **Dimensions** *(list) --*

          A CloudWatch metric dimension.

          - *(dict) --*

            A CloudWatch dimension, which is specified using a ``Key`` (known as a ``Name`` in
            CloudWatch), ``Value`` pair. By default, Amazon EMR uses one dimension whose ``Key``
            is ``JobFlowID`` and ``Value`` is a variable representing the cluster ID, which is
            ``${emr.clusterId}`` . This enables the rule to bootstrap when the cluster ID becomes
            available.

            - **Key** *(string) --*

              The dimension name.

            - **Value** *(string) --*

              The dimension value.
    """


_ClientPutAutoScalingPolicyAutoScalingPolicyTypeDef = TypedDict(
    "_ClientPutAutoScalingPolicyAutoScalingPolicyTypeDef",
    {
        "Constraints": ClientPutAutoScalingPolicyAutoScalingPolicyConstraintsTypeDef,
        "Rules": List[ClientPutAutoScalingPolicyAutoScalingPolicyRulesTypeDef],
    },
)


class ClientPutAutoScalingPolicyAutoScalingPolicyTypeDef(
    _ClientPutAutoScalingPolicyAutoScalingPolicyTypeDef
):
    """
    Type definition for `ClientPutAutoScalingPolicy` `AutoScalingPolicy`

    Specifies the definition of the automatic scaling policy.

    - **Constraints** *(dict) --* **[REQUIRED]**

      The upper and lower EC2 instance limits for an automatic scaling policy. Automatic scaling
      activity will not cause an instance group to grow above or below these limits.

      - **MinCapacity** *(integer) --* **[REQUIRED]**

        The lower boundary of EC2 instances in an instance group below which scaling activities are
        not allowed to shrink. Scale-in activities will not terminate instances below this boundary.

      - **MaxCapacity** *(integer) --* **[REQUIRED]**

        The upper boundary of EC2 instances in an instance group beyond which scaling activities are
        not allowed to grow. Scale-out activities will not add instances beyond this boundary.

    - **Rules** *(list) --* **[REQUIRED]**

      The scale-in and scale-out rules that comprise the automatic scaling policy.

      - *(dict) --*

        A scale-in or scale-out rule that defines scaling activity, including the CloudWatch metric
        alarm that triggers activity, how EC2 instances are added or removed, and the periodicity of
        adjustments. The automatic scaling policy for an instance group can comprise one or more
        automatic scaling rules.

        - **Name** *(string) --* **[REQUIRED]**

          The name used to identify an automatic scaling rule. Rule names must be unique within a
          scaling policy.

        - **Description** *(string) --*

          A friendly, more verbose description of the automatic scaling rule.

        - **Action** *(dict) --* **[REQUIRED]**

          The conditions that trigger an automatic scaling activity.

          - **Market** *(string) --*

            Not available for instance groups. Instance groups use the market type specified for the
            group.

          - **SimpleScalingPolicyConfiguration** *(dict) --* **[REQUIRED]**

            The type of adjustment the automatic scaling activity makes when triggered, and the
            periodicity of the adjustment.

            - **AdjustmentType** *(string) --*

              The way in which EC2 instances are added (if ``ScalingAdjustment`` is a positive
              number) or terminated (if ``ScalingAdjustment`` is a negative number) each time the
              scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the default.
              ``CHANGE_IN_CAPACITY`` indicates that the EC2 instance count increments or decrements
              by ``ScalingAdjustment`` , which should be expressed as an integer.
              ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count increments or decrements by
              the percentage specified by ``ScalingAdjustment`` , which should be expressed as an
              integer. For example, 20 indicates an increase in 20% increments of cluster capacity.
              ``EXACT_CAPACITY`` indicates the scaling activity results in an instance group with the
              number of EC2 instances specified by ``ScalingAdjustment`` , which should be expressed
              as a positive integer.

            - **ScalingAdjustment** *(integer) --* **[REQUIRED]**

              The amount by which to scale in or scale out, based on the specified ``AdjustmentType``
              . A positive value adds to the instance group's EC2 instance count while a negative
              number removes instances. If ``AdjustmentType`` is set to ``EXACT_CAPACITY`` , the
              number should only be a positive integer. If ``AdjustmentType`` is set to
              ``PERCENT_CHANGE_IN_CAPACITY`` , the value should express the percentage as an integer.
              For example, -20 indicates a decrease in 20% increments of cluster capacity.

            - **CoolDown** *(integer) --*

              The amount of time, in seconds, after a scaling activity completes before any further
              trigger-related scaling activities can start. The default value is 0.

        - **Trigger** *(dict) --* **[REQUIRED]**

          The CloudWatch alarm definition that determines when automatic scaling activity is
          triggered.

          - **CloudWatchAlarmDefinition** *(dict) --* **[REQUIRED]**

            The definition of a CloudWatch metric alarm. When the defined alarm conditions are met
            along with other trigger parameters, scaling activity begins.

            - **ComparisonOperator** *(string) --* **[REQUIRED]**

              Determines how the metric specified by ``MetricName`` is compared to the value
              specified by ``Threshold`` .

            - **EvaluationPeriods** *(integer) --*

              The number of periods, in five-minute increments, during which the alarm condition must
              exist before the alarm triggers automatic scaling activity. The default value is ``1`` .

            - **MetricName** *(string) --* **[REQUIRED]**

              The name of the CloudWatch metric that is watched to determine an alarm condition.

            - **Namespace** *(string) --*

              The namespace for the CloudWatch metric. The default is ``AWS/ElasticMapReduce`` .

            - **Period** *(integer) --* **[REQUIRED]**

              The period, in seconds, over which the statistic is applied. EMR CloudWatch metrics are
              emitted every five minutes (300 seconds), so if an EMR CloudWatch metric is specified,
              specify ``300`` .

            - **Statistic** *(string) --*

              The statistic to apply to the metric associated with the alarm. The default is
              ``AVERAGE`` .

            - **Threshold** *(float) --* **[REQUIRED]**

              The value against which the specified statistic is compared.

            - **Unit** *(string) --*

              The unit of measure associated with the CloudWatch metric being watched. The value
              specified for ``Unit`` must correspond to the units specified in the CloudWatch metric.

            - **Dimensions** *(list) --*

              A CloudWatch metric dimension.

              - *(dict) --*

                A CloudWatch dimension, which is specified using a ``Key`` (known as a ``Name`` in
                CloudWatch), ``Value`` pair. By default, Amazon EMR uses one dimension whose ``Key``
                is ``JobFlowID`` and ``Value`` is a variable representing the cluster ID, which is
                ``${emr.clusterId}`` . This enables the rule to bootstrap when the cluster ID becomes
                available.

                - **Key** *(string) --*

                  The dimension name.

                - **Value** *(string) --*

                  The dimension value.
    """


_ClientPutAutoScalingPolicyResponseAutoScalingPolicyConstraintsTypeDef = TypedDict(
    "_ClientPutAutoScalingPolicyResponseAutoScalingPolicyConstraintsTypeDef",
    {"MinCapacity": int, "MaxCapacity": int},
    total=False,
)


class ClientPutAutoScalingPolicyResponseAutoScalingPolicyConstraintsTypeDef(
    _ClientPutAutoScalingPolicyResponseAutoScalingPolicyConstraintsTypeDef
):
    """
    Type definition for `ClientPutAutoScalingPolicyResponseAutoScalingPolicy` `Constraints`

    The upper and lower EC2 instance limits for an automatic scaling policy. Automatic scaling
    activity will not cause an instance group to grow above or below these limits.

    - **MinCapacity** *(integer) --*

      The lower boundary of EC2 instances in an instance group below which scaling activities
      are not allowed to shrink. Scale-in activities will not terminate instances below this
      boundary.

    - **MaxCapacity** *(integer) --*

      The upper boundary of EC2 instances in an instance group beyond which scaling activities
      are not allowed to grow. Scale-out activities will not add instances beyond this boundary.
    """


_ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef = TypedDict(
    "_ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    {"AdjustmentType": str, "ScalingAdjustment": int, "CoolDown": int},
    total=False,
)


class ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef(
    _ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef
):
    """
    Type definition for `ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesAction` `SimpleScalingPolicyConfiguration`

    The type of adjustment the automatic scaling activity makes when triggered, and the
    periodicity of the adjustment.

    - **AdjustmentType** *(string) --*

      The way in which EC2 instances are added (if ``ScalingAdjustment`` is a positive
      number) or terminated (if ``ScalingAdjustment`` is a negative number) each time the
      scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the default.
      ``CHANGE_IN_CAPACITY`` indicates that the EC2 instance count increments or
      decrements by ``ScalingAdjustment`` , which should be expressed as an integer.
      ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count increments or
      decrements by the percentage specified by ``ScalingAdjustment`` , which should be
      expressed as an integer. For example, 20 indicates an increase in 20% increments of
      cluster capacity. ``EXACT_CAPACITY`` indicates the scaling activity results in an
      instance group with the number of EC2 instances specified by ``ScalingAdjustment``
      , which should be expressed as a positive integer.

    - **ScalingAdjustment** *(integer) --*

      The amount by which to scale in or scale out, based on the specified
      ``AdjustmentType`` . A positive value adds to the instance group's EC2 instance
      count while a negative number removes instances. If ``AdjustmentType`` is set to
      ``EXACT_CAPACITY`` , the number should only be a positive integer. If
      ``AdjustmentType`` is set to ``PERCENT_CHANGE_IN_CAPACITY`` , the value should
      express the percentage as an integer. For example, -20 indicates a decrease in 20%
      increments of cluster capacity.

    - **CoolDown** *(integer) --*

      The amount of time, in seconds, after a scaling activity completes before any
      further trigger-related scaling activities can start. The default value is 0.
    """


_ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesActionTypeDef = TypedDict(
    "_ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesActionTypeDef",
    {
        "Market": str,
        "SimpleScalingPolicyConfiguration": ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef,
    },
    total=False,
)


class ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesActionTypeDef(
    _ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesActionTypeDef
):
    """
    Type definition for `ClientPutAutoScalingPolicyResponseAutoScalingPolicyRules` `Action`

    The conditions that trigger an automatic scaling activity.

    - **Market** *(string) --*

      Not available for instance groups. Instance groups use the market type specified for
      the group.

    - **SimpleScalingPolicyConfiguration** *(dict) --*

      The type of adjustment the automatic scaling activity makes when triggered, and the
      periodicity of the adjustment.

      - **AdjustmentType** *(string) --*

        The way in which EC2 instances are added (if ``ScalingAdjustment`` is a positive
        number) or terminated (if ``ScalingAdjustment`` is a negative number) each time the
        scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the default.
        ``CHANGE_IN_CAPACITY`` indicates that the EC2 instance count increments or
        decrements by ``ScalingAdjustment`` , which should be expressed as an integer.
        ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count increments or
        decrements by the percentage specified by ``ScalingAdjustment`` , which should be
        expressed as an integer. For example, 20 indicates an increase in 20% increments of
        cluster capacity. ``EXACT_CAPACITY`` indicates the scaling activity results in an
        instance group with the number of EC2 instances specified by ``ScalingAdjustment``
        , which should be expressed as a positive integer.

      - **ScalingAdjustment** *(integer) --*

        The amount by which to scale in or scale out, based on the specified
        ``AdjustmentType`` . A positive value adds to the instance group's EC2 instance
        count while a negative number removes instances. If ``AdjustmentType`` is set to
        ``EXACT_CAPACITY`` , the number should only be a positive integer. If
        ``AdjustmentType`` is set to ``PERCENT_CHANGE_IN_CAPACITY`` , the value should
        express the percentage as an integer. For example, -20 indicates a decrease in 20%
        increments of cluster capacity.

      - **CoolDown** *(integer) --*

        The amount of time, in seconds, after a scaling activity completes before any
        further trigger-related scaling activities can start. The default value is 0.
    """


_ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef = TypedDict(
    "_ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef(
    _ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef
):
    """
    Type definition for `ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinition` `Dimensions`

    A CloudWatch dimension, which is specified using a ``Key`` (known as a ``Name``
    in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one dimension whose
    ``Key`` is ``JobFlowID`` and ``Value`` is a variable representing the cluster ID,
    which is ``${emr.clusterId}`` . This enables the rule to bootstrap when the
    cluster ID becomes available.

    - **Key** *(string) --*

      The dimension name.

    - **Value** *(string) --*

      The dimension value.
    """


_ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef = TypedDict(
    "_ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    {
        "ComparisonOperator": str,
        "EvaluationPeriods": int,
        "MetricName": str,
        "Namespace": str,
        "Period": int,
        "Statistic": str,
        "Threshold": float,
        "Unit": str,
        "Dimensions": List[
            ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef
        ],
    },
    total=False,
)


class ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef(
    _ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef
):
    """
    Type definition for `ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTrigger` `CloudWatchAlarmDefinition`

    The definition of a CloudWatch metric alarm. When the defined alarm conditions are
    met along with other trigger parameters, scaling activity begins.

    - **ComparisonOperator** *(string) --*

      Determines how the metric specified by ``MetricName`` is compared to the value
      specified by ``Threshold`` .

    - **EvaluationPeriods** *(integer) --*

      The number of periods, in five-minute increments, during which the alarm condition
      must exist before the alarm triggers automatic scaling activity. The default value
      is ``1`` .

    - **MetricName** *(string) --*

      The name of the CloudWatch metric that is watched to determine an alarm condition.

    - **Namespace** *(string) --*

      The namespace for the CloudWatch metric. The default is ``AWS/ElasticMapReduce`` .

    - **Period** *(integer) --*

      The period, in seconds, over which the statistic is applied. EMR CloudWatch metrics
      are emitted every five minutes (300 seconds), so if an EMR CloudWatch metric is
      specified, specify ``300`` .

    - **Statistic** *(string) --*

      The statistic to apply to the metric associated with the alarm. The default is
      ``AVERAGE`` .

    - **Threshold** *(float) --*

      The value against which the specified statistic is compared.

    - **Unit** *(string) --*

      The unit of measure associated with the CloudWatch metric being watched. The value
      specified for ``Unit`` must correspond to the units specified in the CloudWatch
      metric.

    - **Dimensions** *(list) --*

      A CloudWatch metric dimension.

      - *(dict) --*

        A CloudWatch dimension, which is specified using a ``Key`` (known as a ``Name``
        in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one dimension whose
        ``Key`` is ``JobFlowID`` and ``Value`` is a variable representing the cluster ID,
        which is ``${emr.clusterId}`` . This enables the rule to bootstrap when the
        cluster ID becomes available.

        - **Key** *(string) --*

          The dimension name.

        - **Value** *(string) --*

          The dimension value.
    """


_ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerTypeDef = TypedDict(
    "_ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerTypeDef",
    {
        "CloudWatchAlarmDefinition": ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef
    },
    total=False,
)


class ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerTypeDef(
    _ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerTypeDef
):
    """
    Type definition for `ClientPutAutoScalingPolicyResponseAutoScalingPolicyRules` `Trigger`

    The CloudWatch alarm definition that determines when automatic scaling activity is
    triggered.

    - **CloudWatchAlarmDefinition** *(dict) --*

      The definition of a CloudWatch metric alarm. When the defined alarm conditions are
      met along with other trigger parameters, scaling activity begins.

      - **ComparisonOperator** *(string) --*

        Determines how the metric specified by ``MetricName`` is compared to the value
        specified by ``Threshold`` .

      - **EvaluationPeriods** *(integer) --*

        The number of periods, in five-minute increments, during which the alarm condition
        must exist before the alarm triggers automatic scaling activity. The default value
        is ``1`` .

      - **MetricName** *(string) --*

        The name of the CloudWatch metric that is watched to determine an alarm condition.

      - **Namespace** *(string) --*

        The namespace for the CloudWatch metric. The default is ``AWS/ElasticMapReduce`` .

      - **Period** *(integer) --*

        The period, in seconds, over which the statistic is applied. EMR CloudWatch metrics
        are emitted every five minutes (300 seconds), so if an EMR CloudWatch metric is
        specified, specify ``300`` .

      - **Statistic** *(string) --*

        The statistic to apply to the metric associated with the alarm. The default is
        ``AVERAGE`` .

      - **Threshold** *(float) --*

        The value against which the specified statistic is compared.

      - **Unit** *(string) --*

        The unit of measure associated with the CloudWatch metric being watched. The value
        specified for ``Unit`` must correspond to the units specified in the CloudWatch
        metric.

      - **Dimensions** *(list) --*

        A CloudWatch metric dimension.

        - *(dict) --*

          A CloudWatch dimension, which is specified using a ``Key`` (known as a ``Name``
          in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one dimension whose
          ``Key`` is ``JobFlowID`` and ``Value`` is a variable representing the cluster ID,
          which is ``${emr.clusterId}`` . This enables the rule to bootstrap when the
          cluster ID becomes available.

          - **Key** *(string) --*

            The dimension name.

          - **Value** *(string) --*

            The dimension value.
    """


_ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTypeDef = TypedDict(
    "_ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTypeDef",
    {
        "Name": str,
        "Description": str,
        "Action": ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesActionTypeDef,
        "Trigger": ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerTypeDef,
    },
    total=False,
)


class ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTypeDef(
    _ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTypeDef
):
    """
    Type definition for `ClientPutAutoScalingPolicyResponseAutoScalingPolicy` `Rules`

    A scale-in or scale-out rule that defines scaling activity, including the CloudWatch
    metric alarm that triggers activity, how EC2 instances are added or removed, and the
    periodicity of adjustments. The automatic scaling policy for an instance group can
    comprise one or more automatic scaling rules.

    - **Name** *(string) --*

      The name used to identify an automatic scaling rule. Rule names must be unique within a
      scaling policy.

    - **Description** *(string) --*

      A friendly, more verbose description of the automatic scaling rule.

    - **Action** *(dict) --*

      The conditions that trigger an automatic scaling activity.

      - **Market** *(string) --*

        Not available for instance groups. Instance groups use the market type specified for
        the group.

      - **SimpleScalingPolicyConfiguration** *(dict) --*

        The type of adjustment the automatic scaling activity makes when triggered, and the
        periodicity of the adjustment.

        - **AdjustmentType** *(string) --*

          The way in which EC2 instances are added (if ``ScalingAdjustment`` is a positive
          number) or terminated (if ``ScalingAdjustment`` is a negative number) each time the
          scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the default.
          ``CHANGE_IN_CAPACITY`` indicates that the EC2 instance count increments or
          decrements by ``ScalingAdjustment`` , which should be expressed as an integer.
          ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count increments or
          decrements by the percentage specified by ``ScalingAdjustment`` , which should be
          expressed as an integer. For example, 20 indicates an increase in 20% increments of
          cluster capacity. ``EXACT_CAPACITY`` indicates the scaling activity results in an
          instance group with the number of EC2 instances specified by ``ScalingAdjustment``
          , which should be expressed as a positive integer.

        - **ScalingAdjustment** *(integer) --*

          The amount by which to scale in or scale out, based on the specified
          ``AdjustmentType`` . A positive value adds to the instance group's EC2 instance
          count while a negative number removes instances. If ``AdjustmentType`` is set to
          ``EXACT_CAPACITY`` , the number should only be a positive integer. If
          ``AdjustmentType`` is set to ``PERCENT_CHANGE_IN_CAPACITY`` , the value should
          express the percentage as an integer. For example, -20 indicates a decrease in 20%
          increments of cluster capacity.

        - **CoolDown** *(integer) --*

          The amount of time, in seconds, after a scaling activity completes before any
          further trigger-related scaling activities can start. The default value is 0.

    - **Trigger** *(dict) --*

      The CloudWatch alarm definition that determines when automatic scaling activity is
      triggered.

      - **CloudWatchAlarmDefinition** *(dict) --*

        The definition of a CloudWatch metric alarm. When the defined alarm conditions are
        met along with other trigger parameters, scaling activity begins.

        - **ComparisonOperator** *(string) --*

          Determines how the metric specified by ``MetricName`` is compared to the value
          specified by ``Threshold`` .

        - **EvaluationPeriods** *(integer) --*

          The number of periods, in five-minute increments, during which the alarm condition
          must exist before the alarm triggers automatic scaling activity. The default value
          is ``1`` .

        - **MetricName** *(string) --*

          The name of the CloudWatch metric that is watched to determine an alarm condition.

        - **Namespace** *(string) --*

          The namespace for the CloudWatch metric. The default is ``AWS/ElasticMapReduce`` .

        - **Period** *(integer) --*

          The period, in seconds, over which the statistic is applied. EMR CloudWatch metrics
          are emitted every five minutes (300 seconds), so if an EMR CloudWatch metric is
          specified, specify ``300`` .

        - **Statistic** *(string) --*

          The statistic to apply to the metric associated with the alarm. The default is
          ``AVERAGE`` .

        - **Threshold** *(float) --*

          The value against which the specified statistic is compared.

        - **Unit** *(string) --*

          The unit of measure associated with the CloudWatch metric being watched. The value
          specified for ``Unit`` must correspond to the units specified in the CloudWatch
          metric.

        - **Dimensions** *(list) --*

          A CloudWatch metric dimension.

          - *(dict) --*

            A CloudWatch dimension, which is specified using a ``Key`` (known as a ``Name``
            in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one dimension whose
            ``Key`` is ``JobFlowID`` and ``Value`` is a variable representing the cluster ID,
            which is ``${emr.clusterId}`` . This enables the rule to bootstrap when the
            cluster ID becomes available.

            - **Key** *(string) --*

              The dimension name.

            - **Value** *(string) --*

              The dimension value.
    """


_ClientPutAutoScalingPolicyResponseAutoScalingPolicyStatusStateChangeReasonTypeDef = TypedDict(
    "_ClientPutAutoScalingPolicyResponseAutoScalingPolicyStatusStateChangeReasonTypeDef",
    {"Code": str, "Message": str},
    total=False,
)


class ClientPutAutoScalingPolicyResponseAutoScalingPolicyStatusStateChangeReasonTypeDef(
    _ClientPutAutoScalingPolicyResponseAutoScalingPolicyStatusStateChangeReasonTypeDef
):
    """
    Type definition for `ClientPutAutoScalingPolicyResponseAutoScalingPolicyStatus` `StateChangeReason`

    The reason for a change in status.

    - **Code** *(string) --*

      The code indicating the reason for the change in status.``USER_REQUEST`` indicates that
      the scaling policy status was changed by a user. ``PROVISION_FAILURE`` indicates that
      the status change was because the policy failed to provision. ``CLEANUP_FAILURE``
      indicates an error.

    - **Message** *(string) --*

      A friendly, more verbose message that accompanies an automatic scaling policy state
      change.
    """


_ClientPutAutoScalingPolicyResponseAutoScalingPolicyStatusTypeDef = TypedDict(
    "_ClientPutAutoScalingPolicyResponseAutoScalingPolicyStatusTypeDef",
    {
        "State": str,
        "StateChangeReason": ClientPutAutoScalingPolicyResponseAutoScalingPolicyStatusStateChangeReasonTypeDef,
    },
    total=False,
)


class ClientPutAutoScalingPolicyResponseAutoScalingPolicyStatusTypeDef(
    _ClientPutAutoScalingPolicyResponseAutoScalingPolicyStatusTypeDef
):
    """
    Type definition for `ClientPutAutoScalingPolicyResponseAutoScalingPolicy` `Status`

    The status of an automatic scaling policy.

    - **State** *(string) --*

      Indicates the status of the automatic scaling policy.

    - **StateChangeReason** *(dict) --*

      The reason for a change in status.

      - **Code** *(string) --*

        The code indicating the reason for the change in status.``USER_REQUEST`` indicates that
        the scaling policy status was changed by a user. ``PROVISION_FAILURE`` indicates that
        the status change was because the policy failed to provision. ``CLEANUP_FAILURE``
        indicates an error.

      - **Message** *(string) --*

        A friendly, more verbose message that accompanies an automatic scaling policy state
        change.
    """


_ClientPutAutoScalingPolicyResponseAutoScalingPolicyTypeDef = TypedDict(
    "_ClientPutAutoScalingPolicyResponseAutoScalingPolicyTypeDef",
    {
        "Status": ClientPutAutoScalingPolicyResponseAutoScalingPolicyStatusTypeDef,
        "Constraints": ClientPutAutoScalingPolicyResponseAutoScalingPolicyConstraintsTypeDef,
        "Rules": List[ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTypeDef],
    },
    total=False,
)


class ClientPutAutoScalingPolicyResponseAutoScalingPolicyTypeDef(
    _ClientPutAutoScalingPolicyResponseAutoScalingPolicyTypeDef
):
    """
    Type definition for `ClientPutAutoScalingPolicyResponse` `AutoScalingPolicy`

    The automatic scaling policy definition.

    - **Status** *(dict) --*

      The status of an automatic scaling policy.

      - **State** *(string) --*

        Indicates the status of the automatic scaling policy.

      - **StateChangeReason** *(dict) --*

        The reason for a change in status.

        - **Code** *(string) --*

          The code indicating the reason for the change in status.``USER_REQUEST`` indicates that
          the scaling policy status was changed by a user. ``PROVISION_FAILURE`` indicates that
          the status change was because the policy failed to provision. ``CLEANUP_FAILURE``
          indicates an error.

        - **Message** *(string) --*

          A friendly, more verbose message that accompanies an automatic scaling policy state
          change.

    - **Constraints** *(dict) --*

      The upper and lower EC2 instance limits for an automatic scaling policy. Automatic scaling
      activity will not cause an instance group to grow above or below these limits.

      - **MinCapacity** *(integer) --*

        The lower boundary of EC2 instances in an instance group below which scaling activities
        are not allowed to shrink. Scale-in activities will not terminate instances below this
        boundary.

      - **MaxCapacity** *(integer) --*

        The upper boundary of EC2 instances in an instance group beyond which scaling activities
        are not allowed to grow. Scale-out activities will not add instances beyond this boundary.

    - **Rules** *(list) --*

      The scale-in and scale-out rules that comprise the automatic scaling policy.

      - *(dict) --*

        A scale-in or scale-out rule that defines scaling activity, including the CloudWatch
        metric alarm that triggers activity, how EC2 instances are added or removed, and the
        periodicity of adjustments. The automatic scaling policy for an instance group can
        comprise one or more automatic scaling rules.

        - **Name** *(string) --*

          The name used to identify an automatic scaling rule. Rule names must be unique within a
          scaling policy.

        - **Description** *(string) --*

          A friendly, more verbose description of the automatic scaling rule.

        - **Action** *(dict) --*

          The conditions that trigger an automatic scaling activity.

          - **Market** *(string) --*

            Not available for instance groups. Instance groups use the market type specified for
            the group.

          - **SimpleScalingPolicyConfiguration** *(dict) --*

            The type of adjustment the automatic scaling activity makes when triggered, and the
            periodicity of the adjustment.

            - **AdjustmentType** *(string) --*

              The way in which EC2 instances are added (if ``ScalingAdjustment`` is a positive
              number) or terminated (if ``ScalingAdjustment`` is a negative number) each time the
              scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the default.
              ``CHANGE_IN_CAPACITY`` indicates that the EC2 instance count increments or
              decrements by ``ScalingAdjustment`` , which should be expressed as an integer.
              ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count increments or
              decrements by the percentage specified by ``ScalingAdjustment`` , which should be
              expressed as an integer. For example, 20 indicates an increase in 20% increments of
              cluster capacity. ``EXACT_CAPACITY`` indicates the scaling activity results in an
              instance group with the number of EC2 instances specified by ``ScalingAdjustment``
              , which should be expressed as a positive integer.

            - **ScalingAdjustment** *(integer) --*

              The amount by which to scale in or scale out, based on the specified
              ``AdjustmentType`` . A positive value adds to the instance group's EC2 instance
              count while a negative number removes instances. If ``AdjustmentType`` is set to
              ``EXACT_CAPACITY`` , the number should only be a positive integer. If
              ``AdjustmentType`` is set to ``PERCENT_CHANGE_IN_CAPACITY`` , the value should
              express the percentage as an integer. For example, -20 indicates a decrease in 20%
              increments of cluster capacity.

            - **CoolDown** *(integer) --*

              The amount of time, in seconds, after a scaling activity completes before any
              further trigger-related scaling activities can start. The default value is 0.

        - **Trigger** *(dict) --*

          The CloudWatch alarm definition that determines when automatic scaling activity is
          triggered.

          - **CloudWatchAlarmDefinition** *(dict) --*

            The definition of a CloudWatch metric alarm. When the defined alarm conditions are
            met along with other trigger parameters, scaling activity begins.

            - **ComparisonOperator** *(string) --*

              Determines how the metric specified by ``MetricName`` is compared to the value
              specified by ``Threshold`` .

            - **EvaluationPeriods** *(integer) --*

              The number of periods, in five-minute increments, during which the alarm condition
              must exist before the alarm triggers automatic scaling activity. The default value
              is ``1`` .

            - **MetricName** *(string) --*

              The name of the CloudWatch metric that is watched to determine an alarm condition.

            - **Namespace** *(string) --*

              The namespace for the CloudWatch metric. The default is ``AWS/ElasticMapReduce`` .

            - **Period** *(integer) --*

              The period, in seconds, over which the statistic is applied. EMR CloudWatch metrics
              are emitted every five minutes (300 seconds), so if an EMR CloudWatch metric is
              specified, specify ``300`` .

            - **Statistic** *(string) --*

              The statistic to apply to the metric associated with the alarm. The default is
              ``AVERAGE`` .

            - **Threshold** *(float) --*

              The value against which the specified statistic is compared.

            - **Unit** *(string) --*

              The unit of measure associated with the CloudWatch metric being watched. The value
              specified for ``Unit`` must correspond to the units specified in the CloudWatch
              metric.

            - **Dimensions** *(list) --*

              A CloudWatch metric dimension.

              - *(dict) --*

                A CloudWatch dimension, which is specified using a ``Key`` (known as a ``Name``
                in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one dimension whose
                ``Key`` is ``JobFlowID`` and ``Value`` is a variable representing the cluster ID,
                which is ``${emr.clusterId}`` . This enables the rule to bootstrap when the
                cluster ID becomes available.

                - **Key** *(string) --*

                  The dimension name.

                - **Value** *(string) --*

                  The dimension value.
    """


_ClientPutAutoScalingPolicyResponseTypeDef = TypedDict(
    "_ClientPutAutoScalingPolicyResponseTypeDef",
    {
        "ClusterId": str,
        "InstanceGroupId": str,
        "AutoScalingPolicy": ClientPutAutoScalingPolicyResponseAutoScalingPolicyTypeDef,
        "ClusterArn": str,
    },
    total=False,
)


class ClientPutAutoScalingPolicyResponseTypeDef(
    _ClientPutAutoScalingPolicyResponseTypeDef
):
    """
    Type definition for `ClientPutAutoScalingPolicy` `Response`

    - **ClusterId** *(string) --*

      Specifies the ID of a cluster. The instance group to which the automatic scaling policy is
      applied is within this cluster.

    - **InstanceGroupId** *(string) --*

      Specifies the ID of the instance group to which the scaling policy is applied.

    - **AutoScalingPolicy** *(dict) --*

      The automatic scaling policy definition.

      - **Status** *(dict) --*

        The status of an automatic scaling policy.

        - **State** *(string) --*

          Indicates the status of the automatic scaling policy.

        - **StateChangeReason** *(dict) --*

          The reason for a change in status.

          - **Code** *(string) --*

            The code indicating the reason for the change in status.``USER_REQUEST`` indicates that
            the scaling policy status was changed by a user. ``PROVISION_FAILURE`` indicates that
            the status change was because the policy failed to provision. ``CLEANUP_FAILURE``
            indicates an error.

          - **Message** *(string) --*

            A friendly, more verbose message that accompanies an automatic scaling policy state
            change.

      - **Constraints** *(dict) --*

        The upper and lower EC2 instance limits for an automatic scaling policy. Automatic scaling
        activity will not cause an instance group to grow above or below these limits.

        - **MinCapacity** *(integer) --*

          The lower boundary of EC2 instances in an instance group below which scaling activities
          are not allowed to shrink. Scale-in activities will not terminate instances below this
          boundary.

        - **MaxCapacity** *(integer) --*

          The upper boundary of EC2 instances in an instance group beyond which scaling activities
          are not allowed to grow. Scale-out activities will not add instances beyond this boundary.

      - **Rules** *(list) --*

        The scale-in and scale-out rules that comprise the automatic scaling policy.

        - *(dict) --*

          A scale-in or scale-out rule that defines scaling activity, including the CloudWatch
          metric alarm that triggers activity, how EC2 instances are added or removed, and the
          periodicity of adjustments. The automatic scaling policy for an instance group can
          comprise one or more automatic scaling rules.

          - **Name** *(string) --*

            The name used to identify an automatic scaling rule. Rule names must be unique within a
            scaling policy.

          - **Description** *(string) --*

            A friendly, more verbose description of the automatic scaling rule.

          - **Action** *(dict) --*

            The conditions that trigger an automatic scaling activity.

            - **Market** *(string) --*

              Not available for instance groups. Instance groups use the market type specified for
              the group.

            - **SimpleScalingPolicyConfiguration** *(dict) --*

              The type of adjustment the automatic scaling activity makes when triggered, and the
              periodicity of the adjustment.

              - **AdjustmentType** *(string) --*

                The way in which EC2 instances are added (if ``ScalingAdjustment`` is a positive
                number) or terminated (if ``ScalingAdjustment`` is a negative number) each time the
                scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the default.
                ``CHANGE_IN_CAPACITY`` indicates that the EC2 instance count increments or
                decrements by ``ScalingAdjustment`` , which should be expressed as an integer.
                ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count increments or
                decrements by the percentage specified by ``ScalingAdjustment`` , which should be
                expressed as an integer. For example, 20 indicates an increase in 20% increments of
                cluster capacity. ``EXACT_CAPACITY`` indicates the scaling activity results in an
                instance group with the number of EC2 instances specified by ``ScalingAdjustment``
                , which should be expressed as a positive integer.

              - **ScalingAdjustment** *(integer) --*

                The amount by which to scale in or scale out, based on the specified
                ``AdjustmentType`` . A positive value adds to the instance group's EC2 instance
                count while a negative number removes instances. If ``AdjustmentType`` is set to
                ``EXACT_CAPACITY`` , the number should only be a positive integer. If
                ``AdjustmentType`` is set to ``PERCENT_CHANGE_IN_CAPACITY`` , the value should
                express the percentage as an integer. For example, -20 indicates a decrease in 20%
                increments of cluster capacity.

              - **CoolDown** *(integer) --*

                The amount of time, in seconds, after a scaling activity completes before any
                further trigger-related scaling activities can start. The default value is 0.

          - **Trigger** *(dict) --*

            The CloudWatch alarm definition that determines when automatic scaling activity is
            triggered.

            - **CloudWatchAlarmDefinition** *(dict) --*

              The definition of a CloudWatch metric alarm. When the defined alarm conditions are
              met along with other trigger parameters, scaling activity begins.

              - **ComparisonOperator** *(string) --*

                Determines how the metric specified by ``MetricName`` is compared to the value
                specified by ``Threshold`` .

              - **EvaluationPeriods** *(integer) --*

                The number of periods, in five-minute increments, during which the alarm condition
                must exist before the alarm triggers automatic scaling activity. The default value
                is ``1`` .

              - **MetricName** *(string) --*

                The name of the CloudWatch metric that is watched to determine an alarm condition.

              - **Namespace** *(string) --*

                The namespace for the CloudWatch metric. The default is ``AWS/ElasticMapReduce`` .

              - **Period** *(integer) --*

                The period, in seconds, over which the statistic is applied. EMR CloudWatch metrics
                are emitted every five minutes (300 seconds), so if an EMR CloudWatch metric is
                specified, specify ``300`` .

              - **Statistic** *(string) --*

                The statistic to apply to the metric associated with the alarm. The default is
                ``AVERAGE`` .

              - **Threshold** *(float) --*

                The value against which the specified statistic is compared.

              - **Unit** *(string) --*

                The unit of measure associated with the CloudWatch metric being watched. The value
                specified for ``Unit`` must correspond to the units specified in the CloudWatch
                metric.

              - **Dimensions** *(list) --*

                A CloudWatch metric dimension.

                - *(dict) --*

                  A CloudWatch dimension, which is specified using a ``Key`` (known as a ``Name``
                  in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one dimension whose
                  ``Key`` is ``JobFlowID`` and ``Value`` is a variable representing the cluster ID,
                  which is ``${emr.clusterId}`` . This enables the rule to bootstrap when the
                  cluster ID becomes available.

                  - **Key** *(string) --*

                    The dimension name.

                  - **Value** *(string) --*

                    The dimension value.

    - **ClusterArn** *(string) --*

      The Amazon Resource Name of the cluster.
    """


_RequiredClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef = TypedDict(
    "_RequiredClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef",
    {"MinRange": int},
)
_OptionalClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef = TypedDict(
    "_OptionalClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef",
    {"MaxRange": int},
    total=False,
)


class ClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef(
    _RequiredClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef,
    _OptionalClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef,
):
    """
    Type definition for `ClientPutBlockPublicAccessConfigurationBlockPublicAccessConfiguration` `PermittedPublicSecurityGroupRuleRanges`

    A list of port ranges that are permitted to allow inbound traffic from all public IP
    addresses. To specify a single port, use the same value for ``MinRange`` and ``MaxRange`` .

    - **MinRange** *(integer) --* **[REQUIRED]**

      The smallest port number in a specified range of port numbers.

    - **MaxRange** *(integer) --*

      The smallest port number in a specified range of port numbers.
    """


_RequiredClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationTypeDef = TypedDict(
    "_RequiredClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationTypeDef",
    {"BlockPublicSecurityGroupRules": bool},
)
_OptionalClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationTypeDef = TypedDict(
    "_OptionalClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationTypeDef",
    {
        "PermittedPublicSecurityGroupRuleRanges": List[
            ClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef
        ]
    },
    total=False,
)


class ClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationTypeDef(
    _RequiredClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationTypeDef,
    _OptionalClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationTypeDef,
):
    """
    Type definition for `ClientPutBlockPublicAccessConfiguration` `BlockPublicAccessConfiguration`

    A configuration for Amazon EMR block public access. The configuration applies to all clusters
    created in your account for the current Region. The configuration specifies whether block public
    access is enabled. If block public access is enabled, security groups associated with the cluster
    cannot have rules that allow inbound traffic from 0.0.0.0/0 or ::/0 on a port, unless the port is
    specified as an exception using ``PermittedPublicSecurityGroupRuleRanges`` in the
    ``BlockPublicAccessConfiguration`` . By default, Port 22 (SSH) is an exception, and public access
    is allowed on this port. You can change this by updating ``BlockPublicSecurityGroupRules`` to
    remove the exception.

    - **BlockPublicSecurityGroupRules** *(boolean) --* **[REQUIRED]**

      Indicates whether EMR block public access is enabled (``true`` ) or disabled (``false`` ). By
      default, the value is ``false`` for accounts that have created EMR clusters before July 2019.
      For accounts created after this, the default is ``true`` .

    - **PermittedPublicSecurityGroupRuleRanges** *(list) --*

      Specifies ports and port ranges that are permitted to have security group rules that allow
      inbound traffic from all public sources. For example, if Port 23 (Telnet) is specified for
      ``PermittedPublicSecurityGroupRuleRanges`` , Amazon EMR allows cluster creation if a security
      group associated with the cluster has a rule that allows inbound traffic on Port 23 from IPv4
      0.0.0.0/0 or IPv6 port ::/0 as the source.

      By default, Port 22, which is used for SSH access to the cluster EC2 instances, is in the list
      of ``PermittedPublicSecurityGroupRuleRanges`` .

      - *(dict) --*

        A list of port ranges that are permitted to allow inbound traffic from all public IP
        addresses. To specify a single port, use the same value for ``MinRange`` and ``MaxRange`` .

        - **MinRange** *(integer) --* **[REQUIRED]**

          The smallest port number in a specified range of port numbers.

        - **MaxRange** *(integer) --*

          The smallest port number in a specified range of port numbers.
    """


_ClientRunJobFlowApplicationsTypeDef = TypedDict(
    "_ClientRunJobFlowApplicationsTypeDef",
    {"Name": str, "Version": str, "Args": List[str], "AdditionalInfo": Dict[str, str]},
    total=False,
)


class ClientRunJobFlowApplicationsTypeDef(_ClientRunJobFlowApplicationsTypeDef):
    """
    Type definition for `ClientRunJobFlow` `Applications`

    With Amazon EMR release version 4.0 and later, the only accepted parameter is the application
    name. To pass arguments to applications, you use configuration classifications specified using
    configuration JSON objects. For more information, see `Configuring Applications
    <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

    With earlier Amazon EMR releases, the application is any Amazon or third-party software that
    you can add to the cluster. This structure contains a list of strings that indicates the
    software to use with the cluster and accepts a user argument list. Amazon EMR accepts and
    forwards the argument list to the corresponding installation script as bootstrap action
    argument.

    - **Name** *(string) --*

      The name of the application.

    - **Version** *(string) --*

      The version of the application.

    - **Args** *(list) --*

      Arguments for Amazon EMR to pass to the application.

      - *(string) --*

    - **AdditionalInfo** *(dict) --*

      This option is for advanced users only. This is meta information about third-party
      applications that third-party vendors use for testing purposes.

      - *(string) --*

        - *(string) --*
    """


_RequiredClientRunJobFlowBootstrapActionsScriptBootstrapActionTypeDef = TypedDict(
    "_RequiredClientRunJobFlowBootstrapActionsScriptBootstrapActionTypeDef",
    {"Path": str},
)
_OptionalClientRunJobFlowBootstrapActionsScriptBootstrapActionTypeDef = TypedDict(
    "_OptionalClientRunJobFlowBootstrapActionsScriptBootstrapActionTypeDef",
    {"Args": List[str]},
    total=False,
)


class ClientRunJobFlowBootstrapActionsScriptBootstrapActionTypeDef(
    _RequiredClientRunJobFlowBootstrapActionsScriptBootstrapActionTypeDef,
    _OptionalClientRunJobFlowBootstrapActionsScriptBootstrapActionTypeDef,
):
    """
    Type definition for `ClientRunJobFlowBootstrapActions` `ScriptBootstrapAction`

    The script run by the bootstrap action.

    - **Path** *(string) --* **[REQUIRED]**

      Location of the script to run during a bootstrap action. Can be either a location in Amazon
      S3 or on a local file system.

    - **Args** *(list) --*

      A list of command line arguments to pass to the bootstrap action script.

      - *(string) --*
    """


_ClientRunJobFlowBootstrapActionsTypeDef = TypedDict(
    "_ClientRunJobFlowBootstrapActionsTypeDef",
    {
        "Name": str,
        "ScriptBootstrapAction": ClientRunJobFlowBootstrapActionsScriptBootstrapActionTypeDef,
    },
)


class ClientRunJobFlowBootstrapActionsTypeDef(_ClientRunJobFlowBootstrapActionsTypeDef):
    """
    Type definition for `ClientRunJobFlow` `BootstrapActions`

    Configuration of a bootstrap action.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the bootstrap action.

    - **ScriptBootstrapAction** *(dict) --* **[REQUIRED]**

      The script run by the bootstrap action.

      - **Path** *(string) --* **[REQUIRED]**

        Location of the script to run during a bootstrap action. Can be either a location in Amazon
        S3 or on a local file system.

      - **Args** *(list) --*

        A list of command line arguments to pass to the bootstrap action script.

        - *(string) --*
    """


_ClientRunJobFlowConfigurationsTypeDef = TypedDict(
    "_ClientRunJobFlowConfigurationsTypeDef",
    {"Classification": str, "Configurations": List[Any], "Properties": Dict[str, str]},
    total=False,
)


class ClientRunJobFlowConfigurationsTypeDef(_ClientRunJobFlowConfigurationsTypeDef):
    """
    Type definition for `ClientRunJobFlow` `Configurations`

    .. note::

      Amazon EMR releases 4.x or later.

    An optional configuration specification to be used when provisioning cluster instances, which
    can include configurations for applications and software bundled with Amazon EMR. A
    configuration consists of a classification, properties, and optional nested configurations. A
    classification refers to an application-specific configuration file. Properties are the
    settings you want to change in that file. For more information, see `Configuring Applications
    <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

    - **Classification** *(string) --*

      The classification within a configuration.

    - **Configurations** *(list) --*

      A list of additional configurations to apply within a configuration object.

    - **Properties** *(dict) --*

      A set of properties specified within a configuration classification.

      - *(string) --*

        - *(string) --*
    """


_ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsConfigurationsTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsConfigurationsTypeDef",
    {"Classification": str, "Configurations": List[Any], "Properties": Dict[str, str]},
    total=False,
)


class ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsConfigurationsTypeDef(
    _ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsConfigurationsTypeDef
):
    """
    Type definition for `ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigs` `Configurations`

    .. note::

      Amazon EMR releases 4.x or later.

    An optional configuration specification to be used when provisioning cluster
    instances, which can include configurations for applications and software bundled
    with Amazon EMR. A configuration consists of a classification, properties, and
    optional nested configurations. A classification refers to an application-specific
    configuration file. Properties are the settings you want to change in that file. For
    more information, see `Configuring Applications
    <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

    - **Classification** *(string) --*

      The classification within a configuration.

    - **Configurations** *(list) --*

      A list of additional configurations to apply within a configuration object.

    - **Properties** *(dict) --*

      A set of properties specified within a configuration classification.

      - *(string) --*

        - *(string) --*
    """


_RequiredClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef = TypedDict(
    "_RequiredClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef",
    {"VolumeType": str, "SizeInGB": int},
)
_OptionalClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef = TypedDict(
    "_OptionalClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef",
    {"Iops": int},
    total=False,
)


class ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef(
    _RequiredClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef,
    _OptionalClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef,
):
    """
    Type definition for `ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigs` `VolumeSpecification`

    EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
    requested for the EBS volume attached to an EC2 instance in the cluster.

    - **VolumeType** *(string) --* **[REQUIRED]**

      The volume type. Volume types supported are gp2, io1, standard.

    - **Iops** *(integer) --*

      The number of I/O operations per second (IOPS) that the volume supports.

    - **SizeInGB** *(integer) --* **[REQUIRED]**

      The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
      volume type is EBS-optimized, the minimum value is 10.
    """


_RequiredClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef = TypedDict(
    "_RequiredClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef",
    {
        "VolumeSpecification": ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef
    },
)
_OptionalClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef = TypedDict(
    "_OptionalClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef",
    {"VolumesPerInstance": int},
    total=False,
)


class ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef(
    _RequiredClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef,
    _OptionalClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef,
):
    """
    Type definition for `ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfiguration` `EbsBlockDeviceConfigs`

    Configuration of requested EBS block device associated with the instance group with
    count of volumes that will be associated to every instance.

    - **VolumeSpecification** *(dict) --* **[REQUIRED]**

      EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
      requested for the EBS volume attached to an EC2 instance in the cluster.

      - **VolumeType** *(string) --* **[REQUIRED]**

        The volume type. Volume types supported are gp2, io1, standard.

      - **Iops** *(integer) --*

        The number of I/O operations per second (IOPS) that the volume supports.

      - **SizeInGB** *(integer) --* **[REQUIRED]**

        The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
        volume type is EBS-optimized, the minimum value is 10.

    - **VolumesPerInstance** *(integer) --*

      Number of EBS volumes with a specific volume configuration that will be
      associated with every instance in the instance group
    """


_ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationTypeDef",
    {
        "EbsBlockDeviceConfigs": List[
            ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef
        ],
        "EbsOptimized": bool,
    },
    total=False,
)


class ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationTypeDef(
    _ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationTypeDef
):
    """
    Type definition for `ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigs` `EbsConfiguration`

    The configuration of Amazon Elastic Block Storage (EBS) attached to each instance as
    defined by ``InstanceType`` .

    - **EbsBlockDeviceConfigs** *(list) --*

      An array of Amazon EBS volume specifications attached to a cluster instance.

      - *(dict) --*

        Configuration of requested EBS block device associated with the instance group with
        count of volumes that will be associated to every instance.

        - **VolumeSpecification** *(dict) --* **[REQUIRED]**

          EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
          requested for the EBS volume attached to an EC2 instance in the cluster.

          - **VolumeType** *(string) --* **[REQUIRED]**

            The volume type. Volume types supported are gp2, io1, standard.

          - **Iops** *(integer) --*

            The number of I/O operations per second (IOPS) that the volume supports.

          - **SizeInGB** *(integer) --* **[REQUIRED]**

            The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
            volume type is EBS-optimized, the minimum value is 10.

        - **VolumesPerInstance** *(integer) --*

          Number of EBS volumes with a specific volume configuration that will be
          associated with every instance in the instance group

    - **EbsOptimized** *(boolean) --*

      Indicates whether an Amazon EBS volume is EBS-optimized.
    """


_RequiredClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsTypeDef = TypedDict(
    "_RequiredClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsTypeDef",
    {"InstanceType": str},
)
_OptionalClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsTypeDef = TypedDict(
    "_OptionalClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsTypeDef",
    {
        "WeightedCapacity": int,
        "BidPrice": str,
        "BidPriceAsPercentageOfOnDemandPrice": float,
        "EbsConfiguration": ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationTypeDef,
        "Configurations": List[
            ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsConfigurationsTypeDef
        ],
    },
    total=False,
)


class ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsTypeDef(
    _RequiredClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsTypeDef,
    _OptionalClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsTypeDef,
):
    """
    Type definition for `ClientRunJobFlowInstancesInstanceFleets` `InstanceTypeConfigs`

    An instance type configuration for each instance type in an instance fleet, which
    determines the EC2 instances Amazon EMR attempts to provision to fulfill On-Demand and
    Spot target capacities. There can be a maximum of 5 instance type configurations in a
    fleet.

    .. note::

      The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and
      later, excluding 5.0.x versions.

    - **InstanceType** *(string) --* **[REQUIRED]**

      An EC2 instance type, such as ``m3.xlarge`` .

    - **WeightedCapacity** *(integer) --*

      The number of units that a provisioned instance of this type provides toward fulfilling
      the target capacities defined in  InstanceFleetConfig . This value is 1 for a master
      instance fleet, and must be 1 or greater for core and task instance fleets. Defaults to
      1 if not specified.

    - **BidPrice** *(string) --*

      The bid price for each EC2 Spot instance type as defined by ``InstanceType`` .
      Expressed in USD. If neither ``BidPrice`` nor ``BidPriceAsPercentageOfOnDemandPrice``
      is provided, ``BidPriceAsPercentageOfOnDemandPrice`` defaults to 100%.

    - **BidPriceAsPercentageOfOnDemandPrice** *(float) --*

      The bid price, as a percentage of On-Demand price, for each EC2 Spot instance as
      defined by ``InstanceType`` . Expressed as a number (for example, 20 specifies 20%). If
      neither ``BidPrice`` nor ``BidPriceAsPercentageOfOnDemandPrice`` is provided,
      ``BidPriceAsPercentageOfOnDemandPrice`` defaults to 100%.

    - **EbsConfiguration** *(dict) --*

      The configuration of Amazon Elastic Block Storage (EBS) attached to each instance as
      defined by ``InstanceType`` .

      - **EbsBlockDeviceConfigs** *(list) --*

        An array of Amazon EBS volume specifications attached to a cluster instance.

        - *(dict) --*

          Configuration of requested EBS block device associated with the instance group with
          count of volumes that will be associated to every instance.

          - **VolumeSpecification** *(dict) --* **[REQUIRED]**

            EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
            requested for the EBS volume attached to an EC2 instance in the cluster.

            - **VolumeType** *(string) --* **[REQUIRED]**

              The volume type. Volume types supported are gp2, io1, standard.

            - **Iops** *(integer) --*

              The number of I/O operations per second (IOPS) that the volume supports.

            - **SizeInGB** *(integer) --* **[REQUIRED]**

              The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
              volume type is EBS-optimized, the minimum value is 10.

          - **VolumesPerInstance** *(integer) --*

            Number of EBS volumes with a specific volume configuration that will be
            associated with every instance in the instance group

      - **EbsOptimized** *(boolean) --*

        Indicates whether an Amazon EBS volume is EBS-optimized.

    - **Configurations** *(list) --*

      A configuration classification that applies when provisioning cluster instances, which
      can include configurations for applications and software that run on the cluster.

      - *(dict) --*

        .. note::

          Amazon EMR releases 4.x or later.

        An optional configuration specification to be used when provisioning cluster
        instances, which can include configurations for applications and software bundled
        with Amazon EMR. A configuration consists of a classification, properties, and
        optional nested configurations. A classification refers to an application-specific
        configuration file. Properties are the settings you want to change in that file. For
        more information, see `Configuring Applications
        <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

        - **Classification** *(string) --*

          The classification within a configuration.

        - **Configurations** *(list) --*

          A list of additional configurations to apply within a configuration object.

        - **Properties** *(dict) --*

          A set of properties specified within a configuration classification.

          - *(string) --*

            - *(string) --*
    """


_RequiredClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef = TypedDict(
    "_RequiredClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef",
    {"TimeoutDurationMinutes": int, "TimeoutAction": str},
)
_OptionalClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef = TypedDict(
    "_OptionalClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef",
    {"BlockDurationMinutes": int},
    total=False,
)


class ClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef(
    _RequiredClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef,
    _OptionalClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef,
):
    """
    Type definition for `ClientRunJobFlowInstancesInstanceFleetsLaunchSpecifications` `SpotSpecification`

    The launch specification for Spot instances in the fleet, which determines the defined
    duration and provisioning timeout behavior.

    - **TimeoutDurationMinutes** *(integer) --* **[REQUIRED]**

      The spot provisioning timeout period in minutes. If Spot instances are not provisioned
      within this time period, the ``TimeOutAction`` is taken. Minimum value is 5 and maximum
      value is 1440. The timeout applies only during initial provisioning, when the cluster
      is first created.

    - **TimeoutAction** *(string) --* **[REQUIRED]**

      The action to take when ``TargetSpotCapacity`` has not been fulfilled when the
      ``TimeoutDurationMinutes`` has expired; that is, when all Spot instances could not be
      provisioned within the Spot provisioning timeout. Valid values are
      ``TERMINATE_CLUSTER`` and ``SWITCH_TO_ON_DEMAND`` . SWITCH_TO_ON_DEMAND specifies that
      if no Spot instances are available, On-Demand Instances should be provisioned to
      fulfill any remaining Spot capacity.

    - **BlockDurationMinutes** *(integer) --*

      The defined duration for Spot instances (also known as Spot blocks) in minutes. When
      specified, the Spot instance does not terminate before the defined duration expires,
      and defined duration pricing for Spot instances applies. Valid values are 60, 120, 180,
      240, 300, or 360. The duration period starts as soon as a Spot instance receives its
      instance ID. At the end of the duration, Amazon EC2 marks the Spot instance for
      termination and provides a Spot instance termination notice, which gives the instance a
      two-minute warning before it terminates.
    """


_ClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsTypeDef",
    {
        "SpotSpecification": ClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef
    },
)


class ClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsTypeDef(
    _ClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsTypeDef
):
    """
    Type definition for `ClientRunJobFlowInstancesInstanceFleets` `LaunchSpecifications`

    The launch specification for the instance fleet.

    - **SpotSpecification** *(dict) --* **[REQUIRED]**

      The launch specification for Spot instances in the fleet, which determines the defined
      duration and provisioning timeout behavior.

      - **TimeoutDurationMinutes** *(integer) --* **[REQUIRED]**

        The spot provisioning timeout period in minutes. If Spot instances are not provisioned
        within this time period, the ``TimeOutAction`` is taken. Minimum value is 5 and maximum
        value is 1440. The timeout applies only during initial provisioning, when the cluster
        is first created.

      - **TimeoutAction** *(string) --* **[REQUIRED]**

        The action to take when ``TargetSpotCapacity`` has not been fulfilled when the
        ``TimeoutDurationMinutes`` has expired; that is, when all Spot instances could not be
        provisioned within the Spot provisioning timeout. Valid values are
        ``TERMINATE_CLUSTER`` and ``SWITCH_TO_ON_DEMAND`` . SWITCH_TO_ON_DEMAND specifies that
        if no Spot instances are available, On-Demand Instances should be provisioned to
        fulfill any remaining Spot capacity.

      - **BlockDurationMinutes** *(integer) --*

        The defined duration for Spot instances (also known as Spot blocks) in minutes. When
        specified, the Spot instance does not terminate before the defined duration expires,
        and defined duration pricing for Spot instances applies. Valid values are 60, 120, 180,
        240, 300, or 360. The duration period starts as soon as a Spot instance receives its
        instance ID. At the end of the duration, Amazon EC2 marks the Spot instance for
        termination and provides a Spot instance termination notice, which gives the instance a
        two-minute warning before it terminates.
    """


_RequiredClientRunJobFlowInstancesInstanceFleetsTypeDef = TypedDict(
    "_RequiredClientRunJobFlowInstancesInstanceFleetsTypeDef",
    {"InstanceFleetType": str},
)
_OptionalClientRunJobFlowInstancesInstanceFleetsTypeDef = TypedDict(
    "_OptionalClientRunJobFlowInstancesInstanceFleetsTypeDef",
    {
        "Name": str,
        "TargetOnDemandCapacity": int,
        "TargetSpotCapacity": int,
        "InstanceTypeConfigs": List[
            ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsTypeDef
        ],
        "LaunchSpecifications": ClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsTypeDef,
    },
    total=False,
)


class ClientRunJobFlowInstancesInstanceFleetsTypeDef(
    _RequiredClientRunJobFlowInstancesInstanceFleetsTypeDef,
    _OptionalClientRunJobFlowInstancesInstanceFleetsTypeDef,
):
    """
    Type definition for `ClientRunJobFlowInstances` `InstanceFleets`

    The configuration that defines an instance fleet.

    .. note::

      The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later,
      excluding 5.0.x versions.

    - **Name** *(string) --*

      The friendly name of the instance fleet.

    - **InstanceFleetType** *(string) --* **[REQUIRED]**

      The node type that the instance fleet hosts. Valid values are MASTER,CORE,and TASK.

    - **TargetOnDemandCapacity** *(integer) --*

      The target capacity of On-Demand units for the instance fleet, which determines how many
      On-Demand instances to provision. When the instance fleet launches, Amazon EMR tries to
      provision On-Demand instances as specified by  InstanceTypeConfig . Each instance
      configuration has a specified ``WeightedCapacity`` . When an On-Demand instance is
      provisioned, the ``WeightedCapacity`` units count toward the target capacity. Amazon EMR
      provisions instances until the target capacity is totally fulfilled, even if this results
      in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon
      EMR can only provision an instance with a ``WeightedCapacity`` of 5 units, the instance is
      provisioned, and the target capacity is exceeded by 3 units.

      .. note::

        If not specified or set to 0, only Spot instances are provisioned for the instance fleet
        using ``TargetSpotCapacity`` . At least one of ``TargetSpotCapacity`` and
        ``TargetOnDemandCapacity`` should be greater than 0. For a master instance fleet, only
        one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` can be specified, and its
        value must be 1.

    - **TargetSpotCapacity** *(integer) --*

      The target capacity of Spot units for the instance fleet, which determines how many Spot
      instances to provision. When the instance fleet launches, Amazon EMR tries to provision
      Spot instances as specified by  InstanceTypeConfig . Each instance configuration has a
      specified ``WeightedCapacity`` . When a Spot instance is provisioned, the
      ``WeightedCapacity`` units count toward the target capacity. Amazon EMR provisions
      instances until the target capacity is totally fulfilled, even if this results in an
      overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR
      can only provision an instance with a ``WeightedCapacity`` of 5 units, the instance is
      provisioned, and the target capacity is exceeded by 3 units.

      .. note::

        If not specified or set to 0, only On-Demand instances are provisioned for the instance
        fleet. At least one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` should be
        greater than 0. For a master instance fleet, only one of ``TargetSpotCapacity`` and
        ``TargetOnDemandCapacity`` can be specified, and its value must be 1.

    - **InstanceTypeConfigs** *(list) --*

      The instance type configurations that define the EC2 instances in the instance fleet.

      - *(dict) --*

        An instance type configuration for each instance type in an instance fleet, which
        determines the EC2 instances Amazon EMR attempts to provision to fulfill On-Demand and
        Spot target capacities. There can be a maximum of 5 instance type configurations in a
        fleet.

        .. note::

          The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and
          later, excluding 5.0.x versions.

        - **InstanceType** *(string) --* **[REQUIRED]**

          An EC2 instance type, such as ``m3.xlarge`` .

        - **WeightedCapacity** *(integer) --*

          The number of units that a provisioned instance of this type provides toward fulfilling
          the target capacities defined in  InstanceFleetConfig . This value is 1 for a master
          instance fleet, and must be 1 or greater for core and task instance fleets. Defaults to
          1 if not specified.

        - **BidPrice** *(string) --*

          The bid price for each EC2 Spot instance type as defined by ``InstanceType`` .
          Expressed in USD. If neither ``BidPrice`` nor ``BidPriceAsPercentageOfOnDemandPrice``
          is provided, ``BidPriceAsPercentageOfOnDemandPrice`` defaults to 100%.

        - **BidPriceAsPercentageOfOnDemandPrice** *(float) --*

          The bid price, as a percentage of On-Demand price, for each EC2 Spot instance as
          defined by ``InstanceType`` . Expressed as a number (for example, 20 specifies 20%). If
          neither ``BidPrice`` nor ``BidPriceAsPercentageOfOnDemandPrice`` is provided,
          ``BidPriceAsPercentageOfOnDemandPrice`` defaults to 100%.

        - **EbsConfiguration** *(dict) --*

          The configuration of Amazon Elastic Block Storage (EBS) attached to each instance as
          defined by ``InstanceType`` .

          - **EbsBlockDeviceConfigs** *(list) --*

            An array of Amazon EBS volume specifications attached to a cluster instance.

            - *(dict) --*

              Configuration of requested EBS block device associated with the instance group with
              count of volumes that will be associated to every instance.

              - **VolumeSpecification** *(dict) --* **[REQUIRED]**

                EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
                requested for the EBS volume attached to an EC2 instance in the cluster.

                - **VolumeType** *(string) --* **[REQUIRED]**

                  The volume type. Volume types supported are gp2, io1, standard.

                - **Iops** *(integer) --*

                  The number of I/O operations per second (IOPS) that the volume supports.

                - **SizeInGB** *(integer) --* **[REQUIRED]**

                  The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
                  volume type is EBS-optimized, the minimum value is 10.

              - **VolumesPerInstance** *(integer) --*

                Number of EBS volumes with a specific volume configuration that will be
                associated with every instance in the instance group

          - **EbsOptimized** *(boolean) --*

            Indicates whether an Amazon EBS volume is EBS-optimized.

        - **Configurations** *(list) --*

          A configuration classification that applies when provisioning cluster instances, which
          can include configurations for applications and software that run on the cluster.

          - *(dict) --*

            .. note::

              Amazon EMR releases 4.x or later.

            An optional configuration specification to be used when provisioning cluster
            instances, which can include configurations for applications and software bundled
            with Amazon EMR. A configuration consists of a classification, properties, and
            optional nested configurations. A classification refers to an application-specific
            configuration file. Properties are the settings you want to change in that file. For
            more information, see `Configuring Applications
            <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

            - **Classification** *(string) --*

              The classification within a configuration.

            - **Configurations** *(list) --*

              A list of additional configurations to apply within a configuration object.

            - **Properties** *(dict) --*

              A set of properties specified within a configuration classification.

              - *(string) --*

                - *(string) --*

    - **LaunchSpecifications** *(dict) --*

      The launch specification for the instance fleet.

      - **SpotSpecification** *(dict) --* **[REQUIRED]**

        The launch specification for Spot instances in the fleet, which determines the defined
        duration and provisioning timeout behavior.

        - **TimeoutDurationMinutes** *(integer) --* **[REQUIRED]**

          The spot provisioning timeout period in minutes. If Spot instances are not provisioned
          within this time period, the ``TimeOutAction`` is taken. Minimum value is 5 and maximum
          value is 1440. The timeout applies only during initial provisioning, when the cluster
          is first created.

        - **TimeoutAction** *(string) --* **[REQUIRED]**

          The action to take when ``TargetSpotCapacity`` has not been fulfilled when the
          ``TimeoutDurationMinutes`` has expired; that is, when all Spot instances could not be
          provisioned within the Spot provisioning timeout. Valid values are
          ``TERMINATE_CLUSTER`` and ``SWITCH_TO_ON_DEMAND`` . SWITCH_TO_ON_DEMAND specifies that
          if no Spot instances are available, On-Demand Instances should be provisioned to
          fulfill any remaining Spot capacity.

        - **BlockDurationMinutes** *(integer) --*

          The defined duration for Spot instances (also known as Spot blocks) in minutes. When
          specified, the Spot instance does not terminate before the defined duration expires,
          and defined duration pricing for Spot instances applies. Valid values are 60, 120, 180,
          240, 300, or 360. The duration period starts as soon as a Spot instance receives its
          instance ID. At the end of the duration, Amazon EC2 marks the Spot instance for
          termination and provides a Spot instance termination notice, which gives the instance a
          two-minute warning before it terminates.
    """


_ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyConstraintsTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyConstraintsTypeDef",
    {"MinCapacity": int, "MaxCapacity": int},
)


class ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyConstraintsTypeDef(
    _ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyConstraintsTypeDef
):
    """
    Type definition for `ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicy` `Constraints`

    The upper and lower EC2 instance limits for an automatic scaling policy. Automatic
    scaling activity will not cause an instance group to grow above or below these limits.

    - **MinCapacity** *(integer) --* **[REQUIRED]**

      The lower boundary of EC2 instances in an instance group below which scaling activities
      are not allowed to shrink. Scale-in activities will not terminate instances below this
      boundary.

    - **MaxCapacity** *(integer) --* **[REQUIRED]**

      The upper boundary of EC2 instances in an instance group beyond which scaling
      activities are not allowed to grow. Scale-out activities will not add instances beyond
      this boundary.
    """


_RequiredClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef = TypedDict(
    "_RequiredClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    {"ScalingAdjustment": int},
)
_OptionalClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef = TypedDict(
    "_OptionalClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    {"AdjustmentType": str, "CoolDown": int},
    total=False,
)


class ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef(
    _RequiredClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef,
    _OptionalClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef,
):
    """
    Type definition for `ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesAction` `SimpleScalingPolicyConfiguration`

    The type of adjustment the automatic scaling activity makes when triggered, and the
    periodicity of the adjustment.

    - **AdjustmentType** *(string) --*

      The way in which EC2 instances are added (if ``ScalingAdjustment`` is a positive
      number) or terminated (if ``ScalingAdjustment`` is a negative number) each time
      the scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the default.
      ``CHANGE_IN_CAPACITY`` indicates that the EC2 instance count increments or
      decrements by ``ScalingAdjustment`` , which should be expressed as an integer.
      ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count increments or
      decrements by the percentage specified by ``ScalingAdjustment`` , which should be
      expressed as an integer. For example, 20 indicates an increase in 20% increments
      of cluster capacity. ``EXACT_CAPACITY`` indicates the scaling activity results in
      an instance group with the number of EC2 instances specified by
      ``ScalingAdjustment`` , which should be expressed as a positive integer.

    - **ScalingAdjustment** *(integer) --* **[REQUIRED]**

      The amount by which to scale in or scale out, based on the specified
      ``AdjustmentType`` . A positive value adds to the instance group's EC2 instance
      count while a negative number removes instances. If ``AdjustmentType`` is set to
      ``EXACT_CAPACITY`` , the number should only be a positive integer. If
      ``AdjustmentType`` is set to ``PERCENT_CHANGE_IN_CAPACITY`` , the value should
      express the percentage as an integer. For example, -20 indicates a decrease in
      20% increments of cluster capacity.

    - **CoolDown** *(integer) --*

      The amount of time, in seconds, after a scaling activity completes before any
      further trigger-related scaling activities can start. The default value is 0.
    """


_RequiredClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionTypeDef = TypedDict(
    "_RequiredClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionTypeDef",
    {
        "SimpleScalingPolicyConfiguration": ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef
    },
)
_OptionalClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionTypeDef = TypedDict(
    "_OptionalClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionTypeDef",
    {"Market": str},
    total=False,
)


class ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionTypeDef(
    _RequiredClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionTypeDef,
    _OptionalClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionTypeDef,
):
    """
    Type definition for `ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRules` `Action`

    The conditions that trigger an automatic scaling activity.

    - **Market** *(string) --*

      Not available for instance groups. Instance groups use the market type specified
      for the group.

    - **SimpleScalingPolicyConfiguration** *(dict) --* **[REQUIRED]**

      The type of adjustment the automatic scaling activity makes when triggered, and the
      periodicity of the adjustment.

      - **AdjustmentType** *(string) --*

        The way in which EC2 instances are added (if ``ScalingAdjustment`` is a positive
        number) or terminated (if ``ScalingAdjustment`` is a negative number) each time
        the scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the default.
        ``CHANGE_IN_CAPACITY`` indicates that the EC2 instance count increments or
        decrements by ``ScalingAdjustment`` , which should be expressed as an integer.
        ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count increments or
        decrements by the percentage specified by ``ScalingAdjustment`` , which should be
        expressed as an integer. For example, 20 indicates an increase in 20% increments
        of cluster capacity. ``EXACT_CAPACITY`` indicates the scaling activity results in
        an instance group with the number of EC2 instances specified by
        ``ScalingAdjustment`` , which should be expressed as a positive integer.

      - **ScalingAdjustment** *(integer) --* **[REQUIRED]**

        The amount by which to scale in or scale out, based on the specified
        ``AdjustmentType`` . A positive value adds to the instance group's EC2 instance
        count while a negative number removes instances. If ``AdjustmentType`` is set to
        ``EXACT_CAPACITY`` , the number should only be a positive integer. If
        ``AdjustmentType`` is set to ``PERCENT_CHANGE_IN_CAPACITY`` , the value should
        express the percentage as an integer. For example, -20 indicates a decrease in
        20% increments of cluster capacity.

      - **CoolDown** *(integer) --*

        The amount of time, in seconds, after a scaling activity completes before any
        further trigger-related scaling activities can start. The default value is 0.
    """


_ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef(
    _ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef
):
    """
    Type definition for `ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinition` `Dimensions`

    A CloudWatch dimension, which is specified using a ``Key`` (known as a ``Name``
    in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one dimension whose
    ``Key`` is ``JobFlowID`` and ``Value`` is a variable representing the cluster
    ID, which is ``${emr.clusterId}`` . This enables the rule to bootstrap when the
    cluster ID becomes available.

    - **Key** *(string) --*

      The dimension name.

    - **Value** *(string) --*

      The dimension value.
    """


_RequiredClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef = TypedDict(
    "_RequiredClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    {"ComparisonOperator": str, "MetricName": str, "Period": int, "Threshold": float},
)
_OptionalClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef = TypedDict(
    "_OptionalClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    {
        "EvaluationPeriods": int,
        "Namespace": str,
        "Statistic": str,
        "Unit": str,
        "Dimensions": List[
            ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef
        ],
    },
    total=False,
)


class ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef(
    _RequiredClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef,
    _OptionalClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef,
):
    """
    Type definition for `ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTrigger` `CloudWatchAlarmDefinition`

    The definition of a CloudWatch metric alarm. When the defined alarm conditions are
    met along with other trigger parameters, scaling activity begins.

    - **ComparisonOperator** *(string) --* **[REQUIRED]**

      Determines how the metric specified by ``MetricName`` is compared to the value
      specified by ``Threshold`` .

    - **EvaluationPeriods** *(integer) --*

      The number of periods, in five-minute increments, during which the alarm
      condition must exist before the alarm triggers automatic scaling activity. The
      default value is ``1`` .

    - **MetricName** *(string) --* **[REQUIRED]**

      The name of the CloudWatch metric that is watched to determine an alarm condition.

    - **Namespace** *(string) --*

      The namespace for the CloudWatch metric. The default is ``AWS/ElasticMapReduce`` .

    - **Period** *(integer) --* **[REQUIRED]**

      The period, in seconds, over which the statistic is applied. EMR CloudWatch
      metrics are emitted every five minutes (300 seconds), so if an EMR CloudWatch
      metric is specified, specify ``300`` .

    - **Statistic** *(string) --*

      The statistic to apply to the metric associated with the alarm. The default is
      ``AVERAGE`` .

    - **Threshold** *(float) --* **[REQUIRED]**

      The value against which the specified statistic is compared.

    - **Unit** *(string) --*

      The unit of measure associated with the CloudWatch metric being watched. The
      value specified for ``Unit`` must correspond to the units specified in the
      CloudWatch metric.

    - **Dimensions** *(list) --*

      A CloudWatch metric dimension.

      - *(dict) --*

        A CloudWatch dimension, which is specified using a ``Key`` (known as a ``Name``
        in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one dimension whose
        ``Key`` is ``JobFlowID`` and ``Value`` is a variable representing the cluster
        ID, which is ``${emr.clusterId}`` . This enables the rule to bootstrap when the
        cluster ID becomes available.

        - **Key** *(string) --*

          The dimension name.

        - **Value** *(string) --*

          The dimension value.
    """


_ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef",
    {
        "CloudWatchAlarmDefinition": ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef
    },
)


class ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef(
    _ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef
):
    """
    Type definition for `ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRules` `Trigger`

    The CloudWatch alarm definition that determines when automatic scaling activity is
    triggered.

    - **CloudWatchAlarmDefinition** *(dict) --* **[REQUIRED]**

      The definition of a CloudWatch metric alarm. When the defined alarm conditions are
      met along with other trigger parameters, scaling activity begins.

      - **ComparisonOperator** *(string) --* **[REQUIRED]**

        Determines how the metric specified by ``MetricName`` is compared to the value
        specified by ``Threshold`` .

      - **EvaluationPeriods** *(integer) --*

        The number of periods, in five-minute increments, during which the alarm
        condition must exist before the alarm triggers automatic scaling activity. The
        default value is ``1`` .

      - **MetricName** *(string) --* **[REQUIRED]**

        The name of the CloudWatch metric that is watched to determine an alarm condition.

      - **Namespace** *(string) --*

        The namespace for the CloudWatch metric. The default is ``AWS/ElasticMapReduce`` .

      - **Period** *(integer) --* **[REQUIRED]**

        The period, in seconds, over which the statistic is applied. EMR CloudWatch
        metrics are emitted every five minutes (300 seconds), so if an EMR CloudWatch
        metric is specified, specify ``300`` .

      - **Statistic** *(string) --*

        The statistic to apply to the metric associated with the alarm. The default is
        ``AVERAGE`` .

      - **Threshold** *(float) --* **[REQUIRED]**

        The value against which the specified statistic is compared.

      - **Unit** *(string) --*

        The unit of measure associated with the CloudWatch metric being watched. The
        value specified for ``Unit`` must correspond to the units specified in the
        CloudWatch metric.

      - **Dimensions** *(list) --*

        A CloudWatch metric dimension.

        - *(dict) --*

          A CloudWatch dimension, which is specified using a ``Key`` (known as a ``Name``
          in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one dimension whose
          ``Key`` is ``JobFlowID`` and ``Value`` is a variable representing the cluster
          ID, which is ``${emr.clusterId}`` . This enables the rule to bootstrap when the
          cluster ID becomes available.

          - **Key** *(string) --*

            The dimension name.

          - **Value** *(string) --*

            The dimension value.
    """


_RequiredClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTypeDef = TypedDict(
    "_RequiredClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTypeDef",
    {
        "Name": str,
        "Action": ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionTypeDef,
        "Trigger": ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef,
    },
)
_OptionalClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTypeDef = TypedDict(
    "_OptionalClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTypeDef",
    {"Description": str},
    total=False,
)


class ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTypeDef(
    _RequiredClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTypeDef,
    _OptionalClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTypeDef,
):
    """
    Type definition for `ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicy` `Rules`

    A scale-in or scale-out rule that defines scaling activity, including the CloudWatch
    metric alarm that triggers activity, how EC2 instances are added or removed, and the
    periodicity of adjustments. The automatic scaling policy for an instance group can
    comprise one or more automatic scaling rules.

    - **Name** *(string) --* **[REQUIRED]**

      The name used to identify an automatic scaling rule. Rule names must be unique within
      a scaling policy.

    - **Description** *(string) --*

      A friendly, more verbose description of the automatic scaling rule.

    - **Action** *(dict) --* **[REQUIRED]**

      The conditions that trigger an automatic scaling activity.

      - **Market** *(string) --*

        Not available for instance groups. Instance groups use the market type specified
        for the group.

      - **SimpleScalingPolicyConfiguration** *(dict) --* **[REQUIRED]**

        The type of adjustment the automatic scaling activity makes when triggered, and the
        periodicity of the adjustment.

        - **AdjustmentType** *(string) --*

          The way in which EC2 instances are added (if ``ScalingAdjustment`` is a positive
          number) or terminated (if ``ScalingAdjustment`` is a negative number) each time
          the scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the default.
          ``CHANGE_IN_CAPACITY`` indicates that the EC2 instance count increments or
          decrements by ``ScalingAdjustment`` , which should be expressed as an integer.
          ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count increments or
          decrements by the percentage specified by ``ScalingAdjustment`` , which should be
          expressed as an integer. For example, 20 indicates an increase in 20% increments
          of cluster capacity. ``EXACT_CAPACITY`` indicates the scaling activity results in
          an instance group with the number of EC2 instances specified by
          ``ScalingAdjustment`` , which should be expressed as a positive integer.

        - **ScalingAdjustment** *(integer) --* **[REQUIRED]**

          The amount by which to scale in or scale out, based on the specified
          ``AdjustmentType`` . A positive value adds to the instance group's EC2 instance
          count while a negative number removes instances. If ``AdjustmentType`` is set to
          ``EXACT_CAPACITY`` , the number should only be a positive integer. If
          ``AdjustmentType`` is set to ``PERCENT_CHANGE_IN_CAPACITY`` , the value should
          express the percentage as an integer. For example, -20 indicates a decrease in
          20% increments of cluster capacity.

        - **CoolDown** *(integer) --*

          The amount of time, in seconds, after a scaling activity completes before any
          further trigger-related scaling activities can start. The default value is 0.

    - **Trigger** *(dict) --* **[REQUIRED]**

      The CloudWatch alarm definition that determines when automatic scaling activity is
      triggered.

      - **CloudWatchAlarmDefinition** *(dict) --* **[REQUIRED]**

        The definition of a CloudWatch metric alarm. When the defined alarm conditions are
        met along with other trigger parameters, scaling activity begins.

        - **ComparisonOperator** *(string) --* **[REQUIRED]**

          Determines how the metric specified by ``MetricName`` is compared to the value
          specified by ``Threshold`` .

        - **EvaluationPeriods** *(integer) --*

          The number of periods, in five-minute increments, during which the alarm
          condition must exist before the alarm triggers automatic scaling activity. The
          default value is ``1`` .

        - **MetricName** *(string) --* **[REQUIRED]**

          The name of the CloudWatch metric that is watched to determine an alarm condition.

        - **Namespace** *(string) --*

          The namespace for the CloudWatch metric. The default is ``AWS/ElasticMapReduce`` .

        - **Period** *(integer) --* **[REQUIRED]**

          The period, in seconds, over which the statistic is applied. EMR CloudWatch
          metrics are emitted every five minutes (300 seconds), so if an EMR CloudWatch
          metric is specified, specify ``300`` .

        - **Statistic** *(string) --*

          The statistic to apply to the metric associated with the alarm. The default is
          ``AVERAGE`` .

        - **Threshold** *(float) --* **[REQUIRED]**

          The value against which the specified statistic is compared.

        - **Unit** *(string) --*

          The unit of measure associated with the CloudWatch metric being watched. The
          value specified for ``Unit`` must correspond to the units specified in the
          CloudWatch metric.

        - **Dimensions** *(list) --*

          A CloudWatch metric dimension.

          - *(dict) --*

            A CloudWatch dimension, which is specified using a ``Key`` (known as a ``Name``
            in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one dimension whose
            ``Key`` is ``JobFlowID`` and ``Value`` is a variable representing the cluster
            ID, which is ``${emr.clusterId}`` . This enables the rule to bootstrap when the
            cluster ID becomes available.

            - **Key** *(string) --*

              The dimension name.

            - **Value** *(string) --*

              The dimension value.
    """


_ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyTypeDef",
    {
        "Constraints": ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyConstraintsTypeDef,
        "Rules": List[
            ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTypeDef
        ],
    },
)


class ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyTypeDef(
    _ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyTypeDef
):
    """
    Type definition for `ClientRunJobFlowInstancesInstanceGroups` `AutoScalingPolicy`

    An automatic scaling policy for a core instance group or task instance group in an Amazon
    EMR cluster. The automatic scaling policy defines how an instance group dynamically adds
    and terminates EC2 instances in response to the value of a CloudWatch metric. See
    PutAutoScalingPolicy .

    - **Constraints** *(dict) --* **[REQUIRED]**

      The upper and lower EC2 instance limits for an automatic scaling policy. Automatic
      scaling activity will not cause an instance group to grow above or below these limits.

      - **MinCapacity** *(integer) --* **[REQUIRED]**

        The lower boundary of EC2 instances in an instance group below which scaling activities
        are not allowed to shrink. Scale-in activities will not terminate instances below this
        boundary.

      - **MaxCapacity** *(integer) --* **[REQUIRED]**

        The upper boundary of EC2 instances in an instance group beyond which scaling
        activities are not allowed to grow. Scale-out activities will not add instances beyond
        this boundary.

    - **Rules** *(list) --* **[REQUIRED]**

      The scale-in and scale-out rules that comprise the automatic scaling policy.

      - *(dict) --*

        A scale-in or scale-out rule that defines scaling activity, including the CloudWatch
        metric alarm that triggers activity, how EC2 instances are added or removed, and the
        periodicity of adjustments. The automatic scaling policy for an instance group can
        comprise one or more automatic scaling rules.

        - **Name** *(string) --* **[REQUIRED]**

          The name used to identify an automatic scaling rule. Rule names must be unique within
          a scaling policy.

        - **Description** *(string) --*

          A friendly, more verbose description of the automatic scaling rule.

        - **Action** *(dict) --* **[REQUIRED]**

          The conditions that trigger an automatic scaling activity.

          - **Market** *(string) --*

            Not available for instance groups. Instance groups use the market type specified
            for the group.

          - **SimpleScalingPolicyConfiguration** *(dict) --* **[REQUIRED]**

            The type of adjustment the automatic scaling activity makes when triggered, and the
            periodicity of the adjustment.

            - **AdjustmentType** *(string) --*

              The way in which EC2 instances are added (if ``ScalingAdjustment`` is a positive
              number) or terminated (if ``ScalingAdjustment`` is a negative number) each time
              the scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the default.
              ``CHANGE_IN_CAPACITY`` indicates that the EC2 instance count increments or
              decrements by ``ScalingAdjustment`` , which should be expressed as an integer.
              ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count increments or
              decrements by the percentage specified by ``ScalingAdjustment`` , which should be
              expressed as an integer. For example, 20 indicates an increase in 20% increments
              of cluster capacity. ``EXACT_CAPACITY`` indicates the scaling activity results in
              an instance group with the number of EC2 instances specified by
              ``ScalingAdjustment`` , which should be expressed as a positive integer.

            - **ScalingAdjustment** *(integer) --* **[REQUIRED]**

              The amount by which to scale in or scale out, based on the specified
              ``AdjustmentType`` . A positive value adds to the instance group's EC2 instance
              count while a negative number removes instances. If ``AdjustmentType`` is set to
              ``EXACT_CAPACITY`` , the number should only be a positive integer. If
              ``AdjustmentType`` is set to ``PERCENT_CHANGE_IN_CAPACITY`` , the value should
              express the percentage as an integer. For example, -20 indicates a decrease in
              20% increments of cluster capacity.

            - **CoolDown** *(integer) --*

              The amount of time, in seconds, after a scaling activity completes before any
              further trigger-related scaling activities can start. The default value is 0.

        - **Trigger** *(dict) --* **[REQUIRED]**

          The CloudWatch alarm definition that determines when automatic scaling activity is
          triggered.

          - **CloudWatchAlarmDefinition** *(dict) --* **[REQUIRED]**

            The definition of a CloudWatch metric alarm. When the defined alarm conditions are
            met along with other trigger parameters, scaling activity begins.

            - **ComparisonOperator** *(string) --* **[REQUIRED]**

              Determines how the metric specified by ``MetricName`` is compared to the value
              specified by ``Threshold`` .

            - **EvaluationPeriods** *(integer) --*

              The number of periods, in five-minute increments, during which the alarm
              condition must exist before the alarm triggers automatic scaling activity. The
              default value is ``1`` .

            - **MetricName** *(string) --* **[REQUIRED]**

              The name of the CloudWatch metric that is watched to determine an alarm condition.

            - **Namespace** *(string) --*

              The namespace for the CloudWatch metric. The default is ``AWS/ElasticMapReduce`` .

            - **Period** *(integer) --* **[REQUIRED]**

              The period, in seconds, over which the statistic is applied. EMR CloudWatch
              metrics are emitted every five minutes (300 seconds), so if an EMR CloudWatch
              metric is specified, specify ``300`` .

            - **Statistic** *(string) --*

              The statistic to apply to the metric associated with the alarm. The default is
              ``AVERAGE`` .

            - **Threshold** *(float) --* **[REQUIRED]**

              The value against which the specified statistic is compared.

            - **Unit** *(string) --*

              The unit of measure associated with the CloudWatch metric being watched. The
              value specified for ``Unit`` must correspond to the units specified in the
              CloudWatch metric.

            - **Dimensions** *(list) --*

              A CloudWatch metric dimension.

              - *(dict) --*

                A CloudWatch dimension, which is specified using a ``Key`` (known as a ``Name``
                in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one dimension whose
                ``Key`` is ``JobFlowID`` and ``Value`` is a variable representing the cluster
                ID, which is ``${emr.clusterId}`` . This enables the rule to bootstrap when the
                cluster ID becomes available.

                - **Key** *(string) --*

                  The dimension name.

                - **Value** *(string) --*

                  The dimension value.
    """


_ClientRunJobFlowInstancesInstanceGroupsConfigurationsTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesInstanceGroupsConfigurationsTypeDef",
    {"Classification": str, "Configurations": List[Any], "Properties": Dict[str, str]},
    total=False,
)


class ClientRunJobFlowInstancesInstanceGroupsConfigurationsTypeDef(
    _ClientRunJobFlowInstancesInstanceGroupsConfigurationsTypeDef
):
    """
    Type definition for `ClientRunJobFlowInstancesInstanceGroups` `Configurations`

    .. note::

      Amazon EMR releases 4.x or later.

    An optional configuration specification to be used when provisioning cluster instances,
    which can include configurations for applications and software bundled with Amazon EMR. A
    configuration consists of a classification, properties, and optional nested
    configurations. A classification refers to an application-specific configuration file.
    Properties are the settings you want to change in that file. For more information, see
    `Configuring Applications
    <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

    - **Classification** *(string) --*

      The classification within a configuration.

    - **Configurations** *(list) --*

      A list of additional configurations to apply within a configuration object.

    - **Properties** *(dict) --*

      A set of properties specified within a configuration classification.

      - *(string) --*

        - *(string) --*
    """


_RequiredClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef = TypedDict(
    "_RequiredClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef",
    {"VolumeType": str, "SizeInGB": int},
)
_OptionalClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef = TypedDict(
    "_OptionalClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef",
    {"Iops": int},
    total=False,
)


class ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef(
    _RequiredClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef,
    _OptionalClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef,
):
    """
    Type definition for `ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigs` `VolumeSpecification`

    EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
    requested for the EBS volume attached to an EC2 instance in the cluster.

    - **VolumeType** *(string) --* **[REQUIRED]**

      The volume type. Volume types supported are gp2, io1, standard.

    - **Iops** *(integer) --*

      The number of I/O operations per second (IOPS) that the volume supports.

    - **SizeInGB** *(integer) --* **[REQUIRED]**

      The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
      volume type is EBS-optimized, the minimum value is 10.
    """


_RequiredClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef = TypedDict(
    "_RequiredClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef",
    {
        "VolumeSpecification": ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef
    },
)
_OptionalClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef = TypedDict(
    "_OptionalClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef",
    {"VolumesPerInstance": int},
    total=False,
)


class ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef(
    _RequiredClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef,
    _OptionalClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef,
):
    """
    Type definition for `ClientRunJobFlowInstancesInstanceGroupsEbsConfiguration` `EbsBlockDeviceConfigs`

    Configuration of requested EBS block device associated with the instance group with
    count of volumes that will be associated to every instance.

    - **VolumeSpecification** *(dict) --* **[REQUIRED]**

      EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
      requested for the EBS volume attached to an EC2 instance in the cluster.

      - **VolumeType** *(string) --* **[REQUIRED]**

        The volume type. Volume types supported are gp2, io1, standard.

      - **Iops** *(integer) --*

        The number of I/O operations per second (IOPS) that the volume supports.

      - **SizeInGB** *(integer) --* **[REQUIRED]**

        The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
        volume type is EBS-optimized, the minimum value is 10.

    - **VolumesPerInstance** *(integer) --*

      Number of EBS volumes with a specific volume configuration that will be associated
      with every instance in the instance group
    """


_ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationTypeDef",
    {
        "EbsBlockDeviceConfigs": List[
            ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef
        ],
        "EbsOptimized": bool,
    },
    total=False,
)


class ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationTypeDef(
    _ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationTypeDef
):
    """
    Type definition for `ClientRunJobFlowInstancesInstanceGroups` `EbsConfiguration`

    EBS configurations that will be attached to each EC2 instance in the instance group.

    - **EbsBlockDeviceConfigs** *(list) --*

      An array of Amazon EBS volume specifications attached to a cluster instance.

      - *(dict) --*

        Configuration of requested EBS block device associated with the instance group with
        count of volumes that will be associated to every instance.

        - **VolumeSpecification** *(dict) --* **[REQUIRED]**

          EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
          requested for the EBS volume attached to an EC2 instance in the cluster.

          - **VolumeType** *(string) --* **[REQUIRED]**

            The volume type. Volume types supported are gp2, io1, standard.

          - **Iops** *(integer) --*

            The number of I/O operations per second (IOPS) that the volume supports.

          - **SizeInGB** *(integer) --* **[REQUIRED]**

            The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
            volume type is EBS-optimized, the minimum value is 10.

        - **VolumesPerInstance** *(integer) --*

          Number of EBS volumes with a specific volume configuration that will be associated
          with every instance in the instance group

    - **EbsOptimized** *(boolean) --*

      Indicates whether an Amazon EBS volume is EBS-optimized.
    """


_RequiredClientRunJobFlowInstancesInstanceGroupsTypeDef = TypedDict(
    "_RequiredClientRunJobFlowInstancesInstanceGroupsTypeDef",
    {"InstanceRole": str, "InstanceType": str, "InstanceCount": int},
)
_OptionalClientRunJobFlowInstancesInstanceGroupsTypeDef = TypedDict(
    "_OptionalClientRunJobFlowInstancesInstanceGroupsTypeDef",
    {
        "Name": str,
        "Market": str,
        "BidPrice": str,
        "Configurations": List[
            ClientRunJobFlowInstancesInstanceGroupsConfigurationsTypeDef
        ],
        "EbsConfiguration": ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationTypeDef,
        "AutoScalingPolicy": ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyTypeDef,
    },
    total=False,
)


class ClientRunJobFlowInstancesInstanceGroupsTypeDef(
    _RequiredClientRunJobFlowInstancesInstanceGroupsTypeDef,
    _OptionalClientRunJobFlowInstancesInstanceGroupsTypeDef,
):
    """
    Type definition for `ClientRunJobFlowInstances` `InstanceGroups`

    Configuration defining a new instance group.

    - **Name** *(string) --*

      Friendly name given to the instance group.

    - **Market** *(string) --*

      Market type of the EC2 instances used to create a cluster node.

    - **InstanceRole** *(string) --* **[REQUIRED]**

      The role of the instance group in the cluster.

    - **BidPrice** *(string) --*

      The bid price for each EC2 Spot instance type as defined by ``InstanceType`` . Expressed in
      USD. If neither ``BidPrice`` nor ``BidPriceAsPercentageOfOnDemandPrice`` is provided,
      ``BidPriceAsPercentageOfOnDemandPrice`` defaults to 100%.

    - **InstanceType** *(string) --* **[REQUIRED]**

      The EC2 instance type for all instances in the instance group.

    - **InstanceCount** *(integer) --* **[REQUIRED]**

      Target number of instances for the instance group.

    - **Configurations** *(list) --*

      .. note::

        Amazon EMR releases 4.x or later.

      The list of configurations supplied for an EMR cluster instance group. You can specify a
      separate configuration for each instance group (master, core, and task).

      - *(dict) --*

        .. note::

          Amazon EMR releases 4.x or later.

        An optional configuration specification to be used when provisioning cluster instances,
        which can include configurations for applications and software bundled with Amazon EMR. A
        configuration consists of a classification, properties, and optional nested
        configurations. A classification refers to an application-specific configuration file.
        Properties are the settings you want to change in that file. For more information, see
        `Configuring Applications
        <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

        - **Classification** *(string) --*

          The classification within a configuration.

        - **Configurations** *(list) --*

          A list of additional configurations to apply within a configuration object.

        - **Properties** *(dict) --*

          A set of properties specified within a configuration classification.

          - *(string) --*

            - *(string) --*

    - **EbsConfiguration** *(dict) --*

      EBS configurations that will be attached to each EC2 instance in the instance group.

      - **EbsBlockDeviceConfigs** *(list) --*

        An array of Amazon EBS volume specifications attached to a cluster instance.

        - *(dict) --*

          Configuration of requested EBS block device associated with the instance group with
          count of volumes that will be associated to every instance.

          - **VolumeSpecification** *(dict) --* **[REQUIRED]**

            EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
            requested for the EBS volume attached to an EC2 instance in the cluster.

            - **VolumeType** *(string) --* **[REQUIRED]**

              The volume type. Volume types supported are gp2, io1, standard.

            - **Iops** *(integer) --*

              The number of I/O operations per second (IOPS) that the volume supports.

            - **SizeInGB** *(integer) --* **[REQUIRED]**

              The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
              volume type is EBS-optimized, the minimum value is 10.

          - **VolumesPerInstance** *(integer) --*

            Number of EBS volumes with a specific volume configuration that will be associated
            with every instance in the instance group

      - **EbsOptimized** *(boolean) --*

        Indicates whether an Amazon EBS volume is EBS-optimized.

    - **AutoScalingPolicy** *(dict) --*

      An automatic scaling policy for a core instance group or task instance group in an Amazon
      EMR cluster. The automatic scaling policy defines how an instance group dynamically adds
      and terminates EC2 instances in response to the value of a CloudWatch metric. See
      PutAutoScalingPolicy .

      - **Constraints** *(dict) --* **[REQUIRED]**

        The upper and lower EC2 instance limits for an automatic scaling policy. Automatic
        scaling activity will not cause an instance group to grow above or below these limits.

        - **MinCapacity** *(integer) --* **[REQUIRED]**

          The lower boundary of EC2 instances in an instance group below which scaling activities
          are not allowed to shrink. Scale-in activities will not terminate instances below this
          boundary.

        - **MaxCapacity** *(integer) --* **[REQUIRED]**

          The upper boundary of EC2 instances in an instance group beyond which scaling
          activities are not allowed to grow. Scale-out activities will not add instances beyond
          this boundary.

      - **Rules** *(list) --* **[REQUIRED]**

        The scale-in and scale-out rules that comprise the automatic scaling policy.

        - *(dict) --*

          A scale-in or scale-out rule that defines scaling activity, including the CloudWatch
          metric alarm that triggers activity, how EC2 instances are added or removed, and the
          periodicity of adjustments. The automatic scaling policy for an instance group can
          comprise one or more automatic scaling rules.

          - **Name** *(string) --* **[REQUIRED]**

            The name used to identify an automatic scaling rule. Rule names must be unique within
            a scaling policy.

          - **Description** *(string) --*

            A friendly, more verbose description of the automatic scaling rule.

          - **Action** *(dict) --* **[REQUIRED]**

            The conditions that trigger an automatic scaling activity.

            - **Market** *(string) --*

              Not available for instance groups. Instance groups use the market type specified
              for the group.

            - **SimpleScalingPolicyConfiguration** *(dict) --* **[REQUIRED]**

              The type of adjustment the automatic scaling activity makes when triggered, and the
              periodicity of the adjustment.

              - **AdjustmentType** *(string) --*

                The way in which EC2 instances are added (if ``ScalingAdjustment`` is a positive
                number) or terminated (if ``ScalingAdjustment`` is a negative number) each time
                the scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the default.
                ``CHANGE_IN_CAPACITY`` indicates that the EC2 instance count increments or
                decrements by ``ScalingAdjustment`` , which should be expressed as an integer.
                ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count increments or
                decrements by the percentage specified by ``ScalingAdjustment`` , which should be
                expressed as an integer. For example, 20 indicates an increase in 20% increments
                of cluster capacity. ``EXACT_CAPACITY`` indicates the scaling activity results in
                an instance group with the number of EC2 instances specified by
                ``ScalingAdjustment`` , which should be expressed as a positive integer.

              - **ScalingAdjustment** *(integer) --* **[REQUIRED]**

                The amount by which to scale in or scale out, based on the specified
                ``AdjustmentType`` . A positive value adds to the instance group's EC2 instance
                count while a negative number removes instances. If ``AdjustmentType`` is set to
                ``EXACT_CAPACITY`` , the number should only be a positive integer. If
                ``AdjustmentType`` is set to ``PERCENT_CHANGE_IN_CAPACITY`` , the value should
                express the percentage as an integer. For example, -20 indicates a decrease in
                20% increments of cluster capacity.

              - **CoolDown** *(integer) --*

                The amount of time, in seconds, after a scaling activity completes before any
                further trigger-related scaling activities can start. The default value is 0.

          - **Trigger** *(dict) --* **[REQUIRED]**

            The CloudWatch alarm definition that determines when automatic scaling activity is
            triggered.

            - **CloudWatchAlarmDefinition** *(dict) --* **[REQUIRED]**

              The definition of a CloudWatch metric alarm. When the defined alarm conditions are
              met along with other trigger parameters, scaling activity begins.

              - **ComparisonOperator** *(string) --* **[REQUIRED]**

                Determines how the metric specified by ``MetricName`` is compared to the value
                specified by ``Threshold`` .

              - **EvaluationPeriods** *(integer) --*

                The number of periods, in five-minute increments, during which the alarm
                condition must exist before the alarm triggers automatic scaling activity. The
                default value is ``1`` .

              - **MetricName** *(string) --* **[REQUIRED]**

                The name of the CloudWatch metric that is watched to determine an alarm condition.

              - **Namespace** *(string) --*

                The namespace for the CloudWatch metric. The default is ``AWS/ElasticMapReduce`` .

              - **Period** *(integer) --* **[REQUIRED]**

                The period, in seconds, over which the statistic is applied. EMR CloudWatch
                metrics are emitted every five minutes (300 seconds), so if an EMR CloudWatch
                metric is specified, specify ``300`` .

              - **Statistic** *(string) --*

                The statistic to apply to the metric associated with the alarm. The default is
                ``AVERAGE`` .

              - **Threshold** *(float) --* **[REQUIRED]**

                The value against which the specified statistic is compared.

              - **Unit** *(string) --*

                The unit of measure associated with the CloudWatch metric being watched. The
                value specified for ``Unit`` must correspond to the units specified in the
                CloudWatch metric.

              - **Dimensions** *(list) --*

                A CloudWatch metric dimension.

                - *(dict) --*

                  A CloudWatch dimension, which is specified using a ``Key`` (known as a ``Name``
                  in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one dimension whose
                  ``Key`` is ``JobFlowID`` and ``Value`` is a variable representing the cluster
                  ID, which is ``${emr.clusterId}`` . This enables the rule to bootstrap when the
                  cluster ID becomes available.

                  - **Key** *(string) --*

                    The dimension name.

                  - **Value** *(string) --*

                    The dimension value.
    """


_ClientRunJobFlowInstancesPlacementTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesPlacementTypeDef",
    {"AvailabilityZone": str, "AvailabilityZones": List[str]},
    total=False,
)


class ClientRunJobFlowInstancesPlacementTypeDef(
    _ClientRunJobFlowInstancesPlacementTypeDef
):
    """
    Type definition for `ClientRunJobFlowInstances` `Placement`

    The Availability Zone in which the cluster runs.

    - **AvailabilityZone** *(string) --*

      The Amazon EC2 Availability Zone for the cluster. ``AvailabilityZone`` is used for uniform
      instance groups, while ``AvailabilityZones`` (plural) is used for instance fleets.

    - **AvailabilityZones** *(list) --*

      When multiple Availability Zones are specified, Amazon EMR evaluates them and launches
      instances in the optimal Availability Zone. ``AvailabilityZones`` is used for instance
      fleets, while ``AvailabilityZone`` (singular) is used for uniform instance groups.

      .. note::

        The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later,
        excluding 5.0.x versions.

      - *(string) --*
    """


_ClientRunJobFlowInstancesTypeDef = TypedDict(
    "_ClientRunJobFlowInstancesTypeDef",
    {
        "MasterInstanceType": str,
        "SlaveInstanceType": str,
        "InstanceCount": int,
        "InstanceGroups": List[ClientRunJobFlowInstancesInstanceGroupsTypeDef],
        "InstanceFleets": List[ClientRunJobFlowInstancesInstanceFleetsTypeDef],
        "Ec2KeyName": str,
        "Placement": ClientRunJobFlowInstancesPlacementTypeDef,
        "KeepJobFlowAliveWhenNoSteps": bool,
        "TerminationProtected": bool,
        "HadoopVersion": str,
        "Ec2SubnetId": str,
        "Ec2SubnetIds": List[str],
        "EmrManagedMasterSecurityGroup": str,
        "EmrManagedSlaveSecurityGroup": str,
        "ServiceAccessSecurityGroup": str,
        "AdditionalMasterSecurityGroups": List[str],
        "AdditionalSlaveSecurityGroups": List[str],
    },
    total=False,
)


class ClientRunJobFlowInstancesTypeDef(_ClientRunJobFlowInstancesTypeDef):
    """
    Type definition for `ClientRunJobFlow` `Instances`

    A specification of the number and type of Amazon EC2 instances.

    - **MasterInstanceType** *(string) --*

      The EC2 instance type of the master node.

    - **SlaveInstanceType** *(string) --*

      The EC2 instance type of the core and task nodes.

    - **InstanceCount** *(integer) --*

      The number of EC2 instances in the cluster.

    - **InstanceGroups** *(list) --*

      Configuration for the instance groups in a cluster.

      - *(dict) --*

        Configuration defining a new instance group.

        - **Name** *(string) --*

          Friendly name given to the instance group.

        - **Market** *(string) --*

          Market type of the EC2 instances used to create a cluster node.

        - **InstanceRole** *(string) --* **[REQUIRED]**

          The role of the instance group in the cluster.

        - **BidPrice** *(string) --*

          The bid price for each EC2 Spot instance type as defined by ``InstanceType`` . Expressed in
          USD. If neither ``BidPrice`` nor ``BidPriceAsPercentageOfOnDemandPrice`` is provided,
          ``BidPriceAsPercentageOfOnDemandPrice`` defaults to 100%.

        - **InstanceType** *(string) --* **[REQUIRED]**

          The EC2 instance type for all instances in the instance group.

        - **InstanceCount** *(integer) --* **[REQUIRED]**

          Target number of instances for the instance group.

        - **Configurations** *(list) --*

          .. note::

            Amazon EMR releases 4.x or later.

          The list of configurations supplied for an EMR cluster instance group. You can specify a
          separate configuration for each instance group (master, core, and task).

          - *(dict) --*

            .. note::

              Amazon EMR releases 4.x or later.

            An optional configuration specification to be used when provisioning cluster instances,
            which can include configurations for applications and software bundled with Amazon EMR. A
            configuration consists of a classification, properties, and optional nested
            configurations. A classification refers to an application-specific configuration file.
            Properties are the settings you want to change in that file. For more information, see
            `Configuring Applications
            <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

            - **Classification** *(string) --*

              The classification within a configuration.

            - **Configurations** *(list) --*

              A list of additional configurations to apply within a configuration object.

            - **Properties** *(dict) --*

              A set of properties specified within a configuration classification.

              - *(string) --*

                - *(string) --*

        - **EbsConfiguration** *(dict) --*

          EBS configurations that will be attached to each EC2 instance in the instance group.

          - **EbsBlockDeviceConfigs** *(list) --*

            An array of Amazon EBS volume specifications attached to a cluster instance.

            - *(dict) --*

              Configuration of requested EBS block device associated with the instance group with
              count of volumes that will be associated to every instance.

              - **VolumeSpecification** *(dict) --* **[REQUIRED]**

                EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
                requested for the EBS volume attached to an EC2 instance in the cluster.

                - **VolumeType** *(string) --* **[REQUIRED]**

                  The volume type. Volume types supported are gp2, io1, standard.

                - **Iops** *(integer) --*

                  The number of I/O operations per second (IOPS) that the volume supports.

                - **SizeInGB** *(integer) --* **[REQUIRED]**

                  The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
                  volume type is EBS-optimized, the minimum value is 10.

              - **VolumesPerInstance** *(integer) --*

                Number of EBS volumes with a specific volume configuration that will be associated
                with every instance in the instance group

          - **EbsOptimized** *(boolean) --*

            Indicates whether an Amazon EBS volume is EBS-optimized.

        - **AutoScalingPolicy** *(dict) --*

          An automatic scaling policy for a core instance group or task instance group in an Amazon
          EMR cluster. The automatic scaling policy defines how an instance group dynamically adds
          and terminates EC2 instances in response to the value of a CloudWatch metric. See
          PutAutoScalingPolicy .

          - **Constraints** *(dict) --* **[REQUIRED]**

            The upper and lower EC2 instance limits for an automatic scaling policy. Automatic
            scaling activity will not cause an instance group to grow above or below these limits.

            - **MinCapacity** *(integer) --* **[REQUIRED]**

              The lower boundary of EC2 instances in an instance group below which scaling activities
              are not allowed to shrink. Scale-in activities will not terminate instances below this
              boundary.

            - **MaxCapacity** *(integer) --* **[REQUIRED]**

              The upper boundary of EC2 instances in an instance group beyond which scaling
              activities are not allowed to grow. Scale-out activities will not add instances beyond
              this boundary.

          - **Rules** *(list) --* **[REQUIRED]**

            The scale-in and scale-out rules that comprise the automatic scaling policy.

            - *(dict) --*

              A scale-in or scale-out rule that defines scaling activity, including the CloudWatch
              metric alarm that triggers activity, how EC2 instances are added or removed, and the
              periodicity of adjustments. The automatic scaling policy for an instance group can
              comprise one or more automatic scaling rules.

              - **Name** *(string) --* **[REQUIRED]**

                The name used to identify an automatic scaling rule. Rule names must be unique within
                a scaling policy.

              - **Description** *(string) --*

                A friendly, more verbose description of the automatic scaling rule.

              - **Action** *(dict) --* **[REQUIRED]**

                The conditions that trigger an automatic scaling activity.

                - **Market** *(string) --*

                  Not available for instance groups. Instance groups use the market type specified
                  for the group.

                - **SimpleScalingPolicyConfiguration** *(dict) --* **[REQUIRED]**

                  The type of adjustment the automatic scaling activity makes when triggered, and the
                  periodicity of the adjustment.

                  - **AdjustmentType** *(string) --*

                    The way in which EC2 instances are added (if ``ScalingAdjustment`` is a positive
                    number) or terminated (if ``ScalingAdjustment`` is a negative number) each time
                    the scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the default.
                    ``CHANGE_IN_CAPACITY`` indicates that the EC2 instance count increments or
                    decrements by ``ScalingAdjustment`` , which should be expressed as an integer.
                    ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count increments or
                    decrements by the percentage specified by ``ScalingAdjustment`` , which should be
                    expressed as an integer. For example, 20 indicates an increase in 20% increments
                    of cluster capacity. ``EXACT_CAPACITY`` indicates the scaling activity results in
                    an instance group with the number of EC2 instances specified by
                    ``ScalingAdjustment`` , which should be expressed as a positive integer.

                  - **ScalingAdjustment** *(integer) --* **[REQUIRED]**

                    The amount by which to scale in or scale out, based on the specified
                    ``AdjustmentType`` . A positive value adds to the instance group's EC2 instance
                    count while a negative number removes instances. If ``AdjustmentType`` is set to
                    ``EXACT_CAPACITY`` , the number should only be a positive integer. If
                    ``AdjustmentType`` is set to ``PERCENT_CHANGE_IN_CAPACITY`` , the value should
                    express the percentage as an integer. For example, -20 indicates a decrease in
                    20% increments of cluster capacity.

                  - **CoolDown** *(integer) --*

                    The amount of time, in seconds, after a scaling activity completes before any
                    further trigger-related scaling activities can start. The default value is 0.

              - **Trigger** *(dict) --* **[REQUIRED]**

                The CloudWatch alarm definition that determines when automatic scaling activity is
                triggered.

                - **CloudWatchAlarmDefinition** *(dict) --* **[REQUIRED]**

                  The definition of a CloudWatch metric alarm. When the defined alarm conditions are
                  met along with other trigger parameters, scaling activity begins.

                  - **ComparisonOperator** *(string) --* **[REQUIRED]**

                    Determines how the metric specified by ``MetricName`` is compared to the value
                    specified by ``Threshold`` .

                  - **EvaluationPeriods** *(integer) --*

                    The number of periods, in five-minute increments, during which the alarm
                    condition must exist before the alarm triggers automatic scaling activity. The
                    default value is ``1`` .

                  - **MetricName** *(string) --* **[REQUIRED]**

                    The name of the CloudWatch metric that is watched to determine an alarm condition.

                  - **Namespace** *(string) --*

                    The namespace for the CloudWatch metric. The default is ``AWS/ElasticMapReduce`` .

                  - **Period** *(integer) --* **[REQUIRED]**

                    The period, in seconds, over which the statistic is applied. EMR CloudWatch
                    metrics are emitted every five minutes (300 seconds), so if an EMR CloudWatch
                    metric is specified, specify ``300`` .

                  - **Statistic** *(string) --*

                    The statistic to apply to the metric associated with the alarm. The default is
                    ``AVERAGE`` .

                  - **Threshold** *(float) --* **[REQUIRED]**

                    The value against which the specified statistic is compared.

                  - **Unit** *(string) --*

                    The unit of measure associated with the CloudWatch metric being watched. The
                    value specified for ``Unit`` must correspond to the units specified in the
                    CloudWatch metric.

                  - **Dimensions** *(list) --*

                    A CloudWatch metric dimension.

                    - *(dict) --*

                      A CloudWatch dimension, which is specified using a ``Key`` (known as a ``Name``
                      in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one dimension whose
                      ``Key`` is ``JobFlowID`` and ``Value`` is a variable representing the cluster
                      ID, which is ``${emr.clusterId}`` . This enables the rule to bootstrap when the
                      cluster ID becomes available.

                      - **Key** *(string) --*

                        The dimension name.

                      - **Value** *(string) --*

                        The dimension value.

    - **InstanceFleets** *(list) --*

      .. note::

        The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later,
        excluding 5.0.x versions.

      Describes the EC2 instances and instance configurations for clusters that use the instance
      fleet configuration.

      - *(dict) --*

        The configuration that defines an instance fleet.

        .. note::

          The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later,
          excluding 5.0.x versions.

        - **Name** *(string) --*

          The friendly name of the instance fleet.

        - **InstanceFleetType** *(string) --* **[REQUIRED]**

          The node type that the instance fleet hosts. Valid values are MASTER,CORE,and TASK.

        - **TargetOnDemandCapacity** *(integer) --*

          The target capacity of On-Demand units for the instance fleet, which determines how many
          On-Demand instances to provision. When the instance fleet launches, Amazon EMR tries to
          provision On-Demand instances as specified by  InstanceTypeConfig . Each instance
          configuration has a specified ``WeightedCapacity`` . When an On-Demand instance is
          provisioned, the ``WeightedCapacity`` units count toward the target capacity. Amazon EMR
          provisions instances until the target capacity is totally fulfilled, even if this results
          in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon
          EMR can only provision an instance with a ``WeightedCapacity`` of 5 units, the instance is
          provisioned, and the target capacity is exceeded by 3 units.

          .. note::

            If not specified or set to 0, only Spot instances are provisioned for the instance fleet
            using ``TargetSpotCapacity`` . At least one of ``TargetSpotCapacity`` and
            ``TargetOnDemandCapacity`` should be greater than 0. For a master instance fleet, only
            one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` can be specified, and its
            value must be 1.

        - **TargetSpotCapacity** *(integer) --*

          The target capacity of Spot units for the instance fleet, which determines how many Spot
          instances to provision. When the instance fleet launches, Amazon EMR tries to provision
          Spot instances as specified by  InstanceTypeConfig . Each instance configuration has a
          specified ``WeightedCapacity`` . When a Spot instance is provisioned, the
          ``WeightedCapacity`` units count toward the target capacity. Amazon EMR provisions
          instances until the target capacity is totally fulfilled, even if this results in an
          overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR
          can only provision an instance with a ``WeightedCapacity`` of 5 units, the instance is
          provisioned, and the target capacity is exceeded by 3 units.

          .. note::

            If not specified or set to 0, only On-Demand instances are provisioned for the instance
            fleet. At least one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` should be
            greater than 0. For a master instance fleet, only one of ``TargetSpotCapacity`` and
            ``TargetOnDemandCapacity`` can be specified, and its value must be 1.

        - **InstanceTypeConfigs** *(list) --*

          The instance type configurations that define the EC2 instances in the instance fleet.

          - *(dict) --*

            An instance type configuration for each instance type in an instance fleet, which
            determines the EC2 instances Amazon EMR attempts to provision to fulfill On-Demand and
            Spot target capacities. There can be a maximum of 5 instance type configurations in a
            fleet.

            .. note::

              The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and
              later, excluding 5.0.x versions.

            - **InstanceType** *(string) --* **[REQUIRED]**

              An EC2 instance type, such as ``m3.xlarge`` .

            - **WeightedCapacity** *(integer) --*

              The number of units that a provisioned instance of this type provides toward fulfilling
              the target capacities defined in  InstanceFleetConfig . This value is 1 for a master
              instance fleet, and must be 1 or greater for core and task instance fleets. Defaults to
              1 if not specified.

            - **BidPrice** *(string) --*

              The bid price for each EC2 Spot instance type as defined by ``InstanceType`` .
              Expressed in USD. If neither ``BidPrice`` nor ``BidPriceAsPercentageOfOnDemandPrice``
              is provided, ``BidPriceAsPercentageOfOnDemandPrice`` defaults to 100%.

            - **BidPriceAsPercentageOfOnDemandPrice** *(float) --*

              The bid price, as a percentage of On-Demand price, for each EC2 Spot instance as
              defined by ``InstanceType`` . Expressed as a number (for example, 20 specifies 20%). If
              neither ``BidPrice`` nor ``BidPriceAsPercentageOfOnDemandPrice`` is provided,
              ``BidPriceAsPercentageOfOnDemandPrice`` defaults to 100%.

            - **EbsConfiguration** *(dict) --*

              The configuration of Amazon Elastic Block Storage (EBS) attached to each instance as
              defined by ``InstanceType`` .

              - **EbsBlockDeviceConfigs** *(list) --*

                An array of Amazon EBS volume specifications attached to a cluster instance.

                - *(dict) --*

                  Configuration of requested EBS block device associated with the instance group with
                  count of volumes that will be associated to every instance.

                  - **VolumeSpecification** *(dict) --* **[REQUIRED]**

                    EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
                    requested for the EBS volume attached to an EC2 instance in the cluster.

                    - **VolumeType** *(string) --* **[REQUIRED]**

                      The volume type. Volume types supported are gp2, io1, standard.

                    - **Iops** *(integer) --*

                      The number of I/O operations per second (IOPS) that the volume supports.

                    - **SizeInGB** *(integer) --* **[REQUIRED]**

                      The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
                      volume type is EBS-optimized, the minimum value is 10.

                  - **VolumesPerInstance** *(integer) --*

                    Number of EBS volumes with a specific volume configuration that will be
                    associated with every instance in the instance group

              - **EbsOptimized** *(boolean) --*

                Indicates whether an Amazon EBS volume is EBS-optimized.

            - **Configurations** *(list) --*

              A configuration classification that applies when provisioning cluster instances, which
              can include configurations for applications and software that run on the cluster.

              - *(dict) --*

                .. note::

                  Amazon EMR releases 4.x or later.

                An optional configuration specification to be used when provisioning cluster
                instances, which can include configurations for applications and software bundled
                with Amazon EMR. A configuration consists of a classification, properties, and
                optional nested configurations. A classification refers to an application-specific
                configuration file. Properties are the settings you want to change in that file. For
                more information, see `Configuring Applications
                <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

                - **Classification** *(string) --*

                  The classification within a configuration.

                - **Configurations** *(list) --*

                  A list of additional configurations to apply within a configuration object.

                - **Properties** *(dict) --*

                  A set of properties specified within a configuration classification.

                  - *(string) --*

                    - *(string) --*

        - **LaunchSpecifications** *(dict) --*

          The launch specification for the instance fleet.

          - **SpotSpecification** *(dict) --* **[REQUIRED]**

            The launch specification for Spot instances in the fleet, which determines the defined
            duration and provisioning timeout behavior.

            - **TimeoutDurationMinutes** *(integer) --* **[REQUIRED]**

              The spot provisioning timeout period in minutes. If Spot instances are not provisioned
              within this time period, the ``TimeOutAction`` is taken. Minimum value is 5 and maximum
              value is 1440. The timeout applies only during initial provisioning, when the cluster
              is first created.

            - **TimeoutAction** *(string) --* **[REQUIRED]**

              The action to take when ``TargetSpotCapacity`` has not been fulfilled when the
              ``TimeoutDurationMinutes`` has expired; that is, when all Spot instances could not be
              provisioned within the Spot provisioning timeout. Valid values are
              ``TERMINATE_CLUSTER`` and ``SWITCH_TO_ON_DEMAND`` . SWITCH_TO_ON_DEMAND specifies that
              if no Spot instances are available, On-Demand Instances should be provisioned to
              fulfill any remaining Spot capacity.

            - **BlockDurationMinutes** *(integer) --*

              The defined duration for Spot instances (also known as Spot blocks) in minutes. When
              specified, the Spot instance does not terminate before the defined duration expires,
              and defined duration pricing for Spot instances applies. Valid values are 60, 120, 180,
              240, 300, or 360. The duration period starts as soon as a Spot instance receives its
              instance ID. At the end of the duration, Amazon EC2 marks the Spot instance for
              termination and provides a Spot instance termination notice, which gives the instance a
              two-minute warning before it terminates.

    - **Ec2KeyName** *(string) --*

      The name of the EC2 key pair that can be used to ssh to the master node as the user called
      "hadoop."

    - **Placement** *(dict) --*

      The Availability Zone in which the cluster runs.

      - **AvailabilityZone** *(string) --*

        The Amazon EC2 Availability Zone for the cluster. ``AvailabilityZone`` is used for uniform
        instance groups, while ``AvailabilityZones`` (plural) is used for instance fleets.

      - **AvailabilityZones** *(list) --*

        When multiple Availability Zones are specified, Amazon EMR evaluates them and launches
        instances in the optimal Availability Zone. ``AvailabilityZones`` is used for instance
        fleets, while ``AvailabilityZone`` (singular) is used for uniform instance groups.

        .. note::

          The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later,
          excluding 5.0.x versions.

        - *(string) --*

    - **KeepJobFlowAliveWhenNoSteps** *(boolean) --*

      Specifies whether the cluster should remain available after completing all steps.

    - **TerminationProtected** *(boolean) --*

      Specifies whether to lock the cluster to prevent the Amazon EC2 instances from being terminated
      by API call, user intervention, or in the event of a job-flow error.

    - **HadoopVersion** *(string) --*

      Applies only to Amazon EMR release versions earlier than 4.0. The Hadoop version for the
      cluster. Valid inputs are "0.18" (deprecated), "0.20" (deprecated), "0.20.205" (deprecated),
      "1.0.3", "2.2.0", or "2.4.0". If you do not set this value, the default of 0.18 is used, unless
      the ``AmiVersion`` parameter is set in the RunJobFlow call, in which case the default version
      of Hadoop for that AMI version is used.

    - **Ec2SubnetId** *(string) --*

      Applies to clusters that use the uniform instance group configuration. To launch the cluster in
      Amazon Virtual Private Cloud (Amazon VPC), set this parameter to the identifier of the Amazon
      VPC subnet where you want the cluster to launch. If you do not specify this value and your
      account supports EC2-Classic, the cluster launches in EC2-Classic.

    - **Ec2SubnetIds** *(list) --*

      Applies to clusters that use the instance fleet configuration. When multiple EC2 subnet IDs are
      specified, Amazon EMR evaluates them and launches instances in the optimal subnet.

      .. note::

        The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later,
        excluding 5.0.x versions.

      - *(string) --*

    - **EmrManagedMasterSecurityGroup** *(string) --*

      The identifier of the Amazon EC2 security group for the master node.

    - **EmrManagedSlaveSecurityGroup** *(string) --*

      The identifier of the Amazon EC2 security group for the core and task nodes.

    - **ServiceAccessSecurityGroup** *(string) --*

      The identifier of the Amazon EC2 security group for the Amazon EMR service to access clusters
      in VPC private subnets.

    - **AdditionalMasterSecurityGroups** *(list) --*

      A list of additional Amazon EC2 security group IDs for the master node.

      - *(string) --*

    - **AdditionalSlaveSecurityGroups** *(list) --*

      A list of additional Amazon EC2 security group IDs for the core and task nodes.

      - *(string) --*
    """


_RequiredClientRunJobFlowKerberosAttributesTypeDef = TypedDict(
    "_RequiredClientRunJobFlowKerberosAttributesTypeDef",
    {"Realm": str, "KdcAdminPassword": str},
)
_OptionalClientRunJobFlowKerberosAttributesTypeDef = TypedDict(
    "_OptionalClientRunJobFlowKerberosAttributesTypeDef",
    {
        "CrossRealmTrustPrincipalPassword": str,
        "ADDomainJoinUser": str,
        "ADDomainJoinPassword": str,
    },
    total=False,
)


class ClientRunJobFlowKerberosAttributesTypeDef(
    _RequiredClientRunJobFlowKerberosAttributesTypeDef,
    _OptionalClientRunJobFlowKerberosAttributesTypeDef,
):
    """
    Type definition for `ClientRunJobFlow` `KerberosAttributes`

    Attributes for Kerberos configuration when Kerberos authentication is enabled using a security
    configuration. For more information see `Use Kerberos Authentication
    <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-kerberos.html>`__ in the *EMR
    Management Guide* .

    - **Realm** *(string) --* **[REQUIRED]**

      The name of the Kerberos realm to which all nodes in a cluster belong. For example,
      ``EC2.INTERNAL`` .

    - **KdcAdminPassword** *(string) --* **[REQUIRED]**

      The password used within the cluster for the kadmin service on the cluster-dedicated KDC, which
      maintains Kerberos principals, password policies, and keytabs for the cluster.

    - **CrossRealmTrustPrincipalPassword** *(string) --*

      Required only when establishing a cross-realm trust with a KDC in a different realm. The
      cross-realm principal password, which must be identical across realms.

    - **ADDomainJoinUser** *(string) --*

      Required only when establishing a cross-realm trust with an Active Directory domain. A user
      with sufficient privileges to join resources to the domain.

    - **ADDomainJoinPassword** *(string) --*

      The Active Directory password for ``ADDomainJoinUser`` .
    """


_ClientRunJobFlowNewSupportedProductsTypeDef = TypedDict(
    "_ClientRunJobFlowNewSupportedProductsTypeDef",
    {"Name": str, "Args": List[str]},
    total=False,
)


class ClientRunJobFlowNewSupportedProductsTypeDef(
    _ClientRunJobFlowNewSupportedProductsTypeDef
):
    """
    Type definition for `ClientRunJobFlow` `NewSupportedProducts`

    The list of supported product configurations which allow user-supplied arguments. EMR accepts
    these arguments and forwards them to the corresponding installation script as bootstrap action
    arguments.

    - **Name** *(string) --*

      The name of the product configuration.

    - **Args** *(list) --*

      The list of user-supplied arguments.

      - *(string) --*
    """


_ClientRunJobFlowResponseTypeDef = TypedDict(
    "_ClientRunJobFlowResponseTypeDef",
    {"JobFlowId": str, "ClusterArn": str},
    total=False,
)


class ClientRunJobFlowResponseTypeDef(_ClientRunJobFlowResponseTypeDef):
    """
    Type definition for `ClientRunJobFlow` `Response`

    The result of the  RunJobFlow operation.

    - **JobFlowId** *(string) --*

      An unique identifier for the job flow.

    - **ClusterArn** *(string) --*

      The Amazon Resource Name of the cluster.
    """


_ClientRunJobFlowStepsHadoopJarStepPropertiesTypeDef = TypedDict(
    "_ClientRunJobFlowStepsHadoopJarStepPropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientRunJobFlowStepsHadoopJarStepPropertiesTypeDef(
    _ClientRunJobFlowStepsHadoopJarStepPropertiesTypeDef
):
    """
    Type definition for `ClientRunJobFlowStepsHadoopJarStep` `Properties`

    A key value pair.

    - **Key** *(string) --*

      The unique identifier of a key value pair.

    - **Value** *(string) --*

      The value part of the identified key.
    """


_RequiredClientRunJobFlowStepsHadoopJarStepTypeDef = TypedDict(
    "_RequiredClientRunJobFlowStepsHadoopJarStepTypeDef", {"Jar": str}
)
_OptionalClientRunJobFlowStepsHadoopJarStepTypeDef = TypedDict(
    "_OptionalClientRunJobFlowStepsHadoopJarStepTypeDef",
    {
        "Properties": List[ClientRunJobFlowStepsHadoopJarStepPropertiesTypeDef],
        "MainClass": str,
        "Args": List[str],
    },
    total=False,
)


class ClientRunJobFlowStepsHadoopJarStepTypeDef(
    _RequiredClientRunJobFlowStepsHadoopJarStepTypeDef,
    _OptionalClientRunJobFlowStepsHadoopJarStepTypeDef,
):
    """
    Type definition for `ClientRunJobFlowSteps` `HadoopJarStep`

    The JAR file used for the step.

    - **Properties** *(list) --*

      A list of Java properties that are set when the step runs. You can use these properties to
      pass key value pairs to your main function.

      - *(dict) --*

        A key value pair.

        - **Key** *(string) --*

          The unique identifier of a key value pair.

        - **Value** *(string) --*

          The value part of the identified key.

    - **Jar** *(string) --* **[REQUIRED]**

      A path to a JAR file run during the step.

    - **MainClass** *(string) --*

      The name of the main class in the specified Java file. If not specified, the JAR file
      should specify a Main-Class in its manifest file.

    - **Args** *(list) --*

      A list of command line arguments passed to the JAR file's main function when executed.

      - *(string) --*
    """


_RequiredClientRunJobFlowStepsTypeDef = TypedDict(
    "_RequiredClientRunJobFlowStepsTypeDef",
    {"Name": str, "HadoopJarStep": ClientRunJobFlowStepsHadoopJarStepTypeDef},
)
_OptionalClientRunJobFlowStepsTypeDef = TypedDict(
    "_OptionalClientRunJobFlowStepsTypeDef", {"ActionOnFailure": str}, total=False
)


class ClientRunJobFlowStepsTypeDef(
    _RequiredClientRunJobFlowStepsTypeDef, _OptionalClientRunJobFlowStepsTypeDef
):
    """
    Type definition for `ClientRunJobFlow` `Steps`

    Specification of a cluster (job flow) step.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the step.

    - **ActionOnFailure** *(string) --*

      The action to take when the cluster step fails. Possible values are TERMINATE_CLUSTER,
      CANCEL_AND_WAIT, and CONTINUE. TERMINATE_JOB_FLOW is provided for backward compatibility. We
      recommend using TERMINATE_CLUSTER instead.

    - **HadoopJarStep** *(dict) --* **[REQUIRED]**

      The JAR file used for the step.

      - **Properties** *(list) --*

        A list of Java properties that are set when the step runs. You can use these properties to
        pass key value pairs to your main function.

        - *(dict) --*

          A key value pair.

          - **Key** *(string) --*

            The unique identifier of a key value pair.

          - **Value** *(string) --*

            The value part of the identified key.

      - **Jar** *(string) --* **[REQUIRED]**

        A path to a JAR file run during the step.

      - **MainClass** *(string) --*

        The name of the main class in the specified Java file. If not specified, the JAR file
        should specify a Main-Class in its manifest file.

      - **Args** *(list) --*

        A list of command line arguments passed to the JAR file's main function when executed.

        - *(string) --*
    """


_ClientRunJobFlowTagsTypeDef = TypedDict(
    "_ClientRunJobFlowTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientRunJobFlowTagsTypeDef(_ClientRunJobFlowTagsTypeDef):
    """
    Type definition for `ClientRunJobFlow` `Tags`

    A key/value pair containing user-defined metadata that you can associate with an Amazon EMR
    resource. Tags make it easier to associate clusters in various ways, such as grouping clusters
    to track your Amazon EMR resource allocation costs. For more information, see `Tag Clusters
    <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html>`__ .

    - **Key** *(string) --*

      A user-defined key, which is the minimum required information for a valid tag. For more
      information, see `Tag
      <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html>`__ .

    - **Value** *(string) --*

      A user-defined value, which is optional in a tag. For more information, see `Tag Clusters
      <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html>`__ .
    """


_ClusterRunningWaitWaiterConfigTypeDef = TypedDict(
    "_ClusterRunningWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class ClusterRunningWaitWaiterConfigTypeDef(_ClusterRunningWaitWaiterConfigTypeDef):
    """
    Type definition for `ClusterRunningWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 60
    """


_ClusterTerminatedWaitWaiterConfigTypeDef = TypedDict(
    "_ClusterTerminatedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class ClusterTerminatedWaitWaiterConfigTypeDef(
    _ClusterTerminatedWaitWaiterConfigTypeDef
):
    """
    Type definition for `ClusterTerminatedWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 60
    """


_ListBootstrapActionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListBootstrapActionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListBootstrapActionsPaginatePaginationConfigTypeDef(
    _ListBootstrapActionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListBootstrapActionsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListBootstrapActionsPaginateResponseBootstrapActionsTypeDef = TypedDict(
    "_ListBootstrapActionsPaginateResponseBootstrapActionsTypeDef",
    {"Name": str, "ScriptPath": str, "Args": List[str]},
    total=False,
)


class ListBootstrapActionsPaginateResponseBootstrapActionsTypeDef(
    _ListBootstrapActionsPaginateResponseBootstrapActionsTypeDef
):
    """
    Type definition for `ListBootstrapActionsPaginateResponse` `BootstrapActions`

    An entity describing an executable that runs on a cluster.

    - **Name** *(string) --*

      The name of the command.

    - **ScriptPath** *(string) --*

      The Amazon S3 location of the command script.

    - **Args** *(list) --*

      Arguments for Amazon EMR to pass to the command for execution.

      - *(string) --*
    """


_ListBootstrapActionsPaginateResponseTypeDef = TypedDict(
    "_ListBootstrapActionsPaginateResponseTypeDef",
    {
        "BootstrapActions": List[
            ListBootstrapActionsPaginateResponseBootstrapActionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListBootstrapActionsPaginateResponseTypeDef(
    _ListBootstrapActionsPaginateResponseTypeDef
):
    """
    Type definition for `ListBootstrapActionsPaginate` `Response`

    This output contains the bootstrap actions detail.

    - **BootstrapActions** *(list) --*

      The bootstrap actions associated with the cluster.

      - *(dict) --*

        An entity describing an executable that runs on a cluster.

        - **Name** *(string) --*

          The name of the command.

        - **ScriptPath** *(string) --*

          The Amazon S3 location of the command script.

        - **Args** *(list) --*

          Arguments for Amazon EMR to pass to the command for execution.

          - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListClustersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListClustersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListClustersPaginatePaginationConfigTypeDef(
    _ListClustersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListClustersPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListClustersPaginateResponseClustersStatusStateChangeReasonTypeDef = TypedDict(
    "_ListClustersPaginateResponseClustersStatusStateChangeReasonTypeDef",
    {"Code": str, "Message": str},
    total=False,
)


class ListClustersPaginateResponseClustersStatusStateChangeReasonTypeDef(
    _ListClustersPaginateResponseClustersStatusStateChangeReasonTypeDef
):
    """
    Type definition for `ListClustersPaginateResponseClustersStatus` `StateChangeReason`

    The reason for the cluster status change.

    - **Code** *(string) --*

      The programmatic code for the state change reason.

    - **Message** *(string) --*

      The descriptive message for the state change reason.
    """


_ListClustersPaginateResponseClustersStatusTimelineTypeDef = TypedDict(
    "_ListClustersPaginateResponseClustersStatusTimelineTypeDef",
    {"CreationDateTime": datetime, "ReadyDateTime": datetime, "EndDateTime": datetime},
    total=False,
)


class ListClustersPaginateResponseClustersStatusTimelineTypeDef(
    _ListClustersPaginateResponseClustersStatusTimelineTypeDef
):
    """
    Type definition for `ListClustersPaginateResponseClustersStatus` `Timeline`

    A timeline that represents the status of a cluster over the lifetime of the cluster.

    - **CreationDateTime** *(datetime) --*

      The creation date and time of the cluster.

    - **ReadyDateTime** *(datetime) --*

      The date and time when the cluster was ready to execute steps.

    - **EndDateTime** *(datetime) --*

      The date and time when the cluster was terminated.
    """


_ListClustersPaginateResponseClustersStatusTypeDef = TypedDict(
    "_ListClustersPaginateResponseClustersStatusTypeDef",
    {
        "State": str,
        "StateChangeReason": ListClustersPaginateResponseClustersStatusStateChangeReasonTypeDef,
        "Timeline": ListClustersPaginateResponseClustersStatusTimelineTypeDef,
    },
    total=False,
)


class ListClustersPaginateResponseClustersStatusTypeDef(
    _ListClustersPaginateResponseClustersStatusTypeDef
):
    """
    Type definition for `ListClustersPaginateResponseClusters` `Status`

    The details about the current status of the cluster.

    - **State** *(string) --*

      The current state of the cluster.

    - **StateChangeReason** *(dict) --*

      The reason for the cluster status change.

      - **Code** *(string) --*

        The programmatic code for the state change reason.

      - **Message** *(string) --*

        The descriptive message for the state change reason.

    - **Timeline** *(dict) --*

      A timeline that represents the status of a cluster over the lifetime of the cluster.

      - **CreationDateTime** *(datetime) --*

        The creation date and time of the cluster.

      - **ReadyDateTime** *(datetime) --*

        The date and time when the cluster was ready to execute steps.

      - **EndDateTime** *(datetime) --*

        The date and time when the cluster was terminated.
    """


_ListClustersPaginateResponseClustersTypeDef = TypedDict(
    "_ListClustersPaginateResponseClustersTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": ListClustersPaginateResponseClustersStatusTypeDef,
        "NormalizedInstanceHours": int,
        "ClusterArn": str,
    },
    total=False,
)


class ListClustersPaginateResponseClustersTypeDef(
    _ListClustersPaginateResponseClustersTypeDef
):
    """
    Type definition for `ListClustersPaginateResponse` `Clusters`

    The summary description of the cluster.

    - **Id** *(string) --*

      The unique identifier for the cluster.

    - **Name** *(string) --*

      The name of the cluster.

    - **Status** *(dict) --*

      The details about the current status of the cluster.

      - **State** *(string) --*

        The current state of the cluster.

      - **StateChangeReason** *(dict) --*

        The reason for the cluster status change.

        - **Code** *(string) --*

          The programmatic code for the state change reason.

        - **Message** *(string) --*

          The descriptive message for the state change reason.

      - **Timeline** *(dict) --*

        A timeline that represents the status of a cluster over the lifetime of the cluster.

        - **CreationDateTime** *(datetime) --*

          The creation date and time of the cluster.

        - **ReadyDateTime** *(datetime) --*

          The date and time when the cluster was ready to execute steps.

        - **EndDateTime** *(datetime) --*

          The date and time when the cluster was terminated.

    - **NormalizedInstanceHours** *(integer) --*

      An approximation of the cost of the cluster, represented in m1.small/hours. This value is
      incremented one time for every hour an m1.small instance runs. Larger instances are
      weighted more, so an EC2 instance that is roughly four times more expensive would result
      in the normalized instance hours being incremented by four. This result is only an
      approximation and does not reflect the actual billing rate.

    - **ClusterArn** *(string) --*

      The Amazon Resource Name of the cluster.
    """


_ListClustersPaginateResponseTypeDef = TypedDict(
    "_ListClustersPaginateResponseTypeDef",
    {"Clusters": List[ListClustersPaginateResponseClustersTypeDef], "NextToken": str},
    total=False,
)


class ListClustersPaginateResponseTypeDef(_ListClustersPaginateResponseTypeDef):
    """
    Type definition for `ListClustersPaginate` `Response`

    This contains a ClusterSummaryList with the cluster details; for example, the cluster IDs,
    names, and status.

    - **Clusters** *(list) --*

      The list of clusters for the account based on the given filters.

      - *(dict) --*

        The summary description of the cluster.

        - **Id** *(string) --*

          The unique identifier for the cluster.

        - **Name** *(string) --*

          The name of the cluster.

        - **Status** *(dict) --*

          The details about the current status of the cluster.

          - **State** *(string) --*

            The current state of the cluster.

          - **StateChangeReason** *(dict) --*

            The reason for the cluster status change.

            - **Code** *(string) --*

              The programmatic code for the state change reason.

            - **Message** *(string) --*

              The descriptive message for the state change reason.

          - **Timeline** *(dict) --*

            A timeline that represents the status of a cluster over the lifetime of the cluster.

            - **CreationDateTime** *(datetime) --*

              The creation date and time of the cluster.

            - **ReadyDateTime** *(datetime) --*

              The date and time when the cluster was ready to execute steps.

            - **EndDateTime** *(datetime) --*

              The date and time when the cluster was terminated.

        - **NormalizedInstanceHours** *(integer) --*

          An approximation of the cost of the cluster, represented in m1.small/hours. This value is
          incremented one time for every hour an m1.small instance runs. Larger instances are
          weighted more, so an EC2 instance that is roughly four times more expensive would result
          in the normalized instance hours being incremented by four. This result is only an
          approximation and does not reflect the actual billing rate.

        - **ClusterArn** *(string) --*

          The Amazon Resource Name of the cluster.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListInstanceFleetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListInstanceFleetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListInstanceFleetsPaginatePaginationConfigTypeDef(
    _ListInstanceFleetsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListInstanceFleetsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsConfigurationsTypeDef = TypedDict(
    "_ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsConfigurationsTypeDef",
    {"Classification": str, "Configurations": List[Any], "Properties": Dict[str, str]},
    total=False,
)


class ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsConfigurationsTypeDef(
    _ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsConfigurationsTypeDef
):
    """
    Type definition for `ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecifications` `Configurations`

    .. note::

      Amazon EMR releases 4.x or later.

    An optional configuration specification to be used when provisioning cluster
    instances, which can include configurations for applications and software bundled
    with Amazon EMR. A configuration consists of a classification, properties, and
    optional nested configurations. A classification refers to an application-specific
    configuration file. Properties are the settings you want to change in that file.
    For more information, see `Configuring Applications
    <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

    - **Classification** *(string) --*

      The classification within a configuration.

    - **Configurations** *(list) --*

      A list of additional configurations to apply within a configuration object.

    - **Properties** *(dict) --*

      A set of properties specified within a configuration classification.

      - *(string) --*

        - *(string) --*
    """


_ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesVolumeSpecificationTypeDef = TypedDict(
    "_ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesVolumeSpecificationTypeDef",
    {"VolumeType": str, "Iops": int, "SizeInGB": int},
    total=False,
)


class ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesVolumeSpecificationTypeDef(
    _ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesVolumeSpecificationTypeDef
):
    """
    Type definition for `ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevices` `VolumeSpecification`

    EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
    requested for the EBS volume attached to an EC2 instance in the cluster.

    - **VolumeType** *(string) --*

      The volume type. Volume types supported are gp2, io1, standard.

    - **Iops** *(integer) --*

      The number of I/O operations per second (IOPS) that the volume supports.

    - **SizeInGB** *(integer) --*

      The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
      volume type is EBS-optimized, the minimum value is 10.
    """


_ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesTypeDef = TypedDict(
    "_ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesTypeDef",
    {
        "VolumeSpecification": ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesVolumeSpecificationTypeDef,
        "Device": str,
    },
    total=False,
)


class ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesTypeDef(
    _ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesTypeDef
):
    """
    Type definition for `ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecifications` `EbsBlockDevices`

    Configuration of requested EBS block device associated with the instance group.

    - **VolumeSpecification** *(dict) --*

      EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
      requested for the EBS volume attached to an EC2 instance in the cluster.

      - **VolumeType** *(string) --*

        The volume type. Volume types supported are gp2, io1, standard.

      - **Iops** *(integer) --*

        The number of I/O operations per second (IOPS) that the volume supports.

      - **SizeInGB** *(integer) --*

        The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
        volume type is EBS-optimized, the minimum value is 10.

    - **Device** *(string) --*

      The device name that is exposed to the instance, such as /dev/sdh.
    """


_ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsTypeDef = TypedDict(
    "_ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsTypeDef",
    {
        "InstanceType": str,
        "WeightedCapacity": int,
        "BidPrice": str,
        "BidPriceAsPercentageOfOnDemandPrice": float,
        "Configurations": List[
            ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsConfigurationsTypeDef
        ],
        "EbsBlockDevices": List[
            ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesTypeDef
        ],
        "EbsOptimized": bool,
    },
    total=False,
)


class ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsTypeDef(
    _ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsTypeDef
):
    """
    Type definition for `ListInstanceFleetsPaginateResponseInstanceFleets` `InstanceTypeSpecifications`

    The configuration specification for each instance type in an instance fleet.

    .. note::

      The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and
      later, excluding 5.0.x versions.

    - **InstanceType** *(string) --*

      The EC2 instance type, for example ``m3.xlarge`` .

    - **WeightedCapacity** *(integer) --*

      The number of units that a provisioned instance of this type provides toward
      fulfilling the target capacities defined in  InstanceFleetConfig . Capacity values
      represent performance characteristics such as vCPUs, memory, or I/O. If not
      specified, the default value is 1.

    - **BidPrice** *(string) --*

      The bid price for each EC2 Spot instance type as defined by ``InstanceType`` .
      Expressed in USD.

    - **BidPriceAsPercentageOfOnDemandPrice** *(float) --*

      The bid price, as a percentage of On-Demand price, for each EC2 Spot instance as
      defined by ``InstanceType`` . Expressed as a number (for example, 20 specifies 20%).

    - **Configurations** *(list) --*

      A configuration classification that applies when provisioning cluster instances,
      which can include configurations for applications and software bundled with Amazon
      EMR.

      - *(dict) --*

        .. note::

          Amazon EMR releases 4.x or later.

        An optional configuration specification to be used when provisioning cluster
        instances, which can include configurations for applications and software bundled
        with Amazon EMR. A configuration consists of a classification, properties, and
        optional nested configurations. A classification refers to an application-specific
        configuration file. Properties are the settings you want to change in that file.
        For more information, see `Configuring Applications
        <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

        - **Classification** *(string) --*

          The classification within a configuration.

        - **Configurations** *(list) --*

          A list of additional configurations to apply within a configuration object.

        - **Properties** *(dict) --*

          A set of properties specified within a configuration classification.

          - *(string) --*

            - *(string) --*

    - **EbsBlockDevices** *(list) --*

      The configuration of Amazon Elastic Block Storage (EBS) attached to each instance as
      defined by ``InstanceType`` .

      - *(dict) --*

        Configuration of requested EBS block device associated with the instance group.

        - **VolumeSpecification** *(dict) --*

          EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
          requested for the EBS volume attached to an EC2 instance in the cluster.

          - **VolumeType** *(string) --*

            The volume type. Volume types supported are gp2, io1, standard.

          - **Iops** *(integer) --*

            The number of I/O operations per second (IOPS) that the volume supports.

          - **SizeInGB** *(integer) --*

            The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
            volume type is EBS-optimized, the minimum value is 10.

        - **Device** *(string) --*

          The device name that is exposed to the instance, such as /dev/sdh.

    - **EbsOptimized** *(boolean) --*

      Evaluates to ``TRUE`` when the specified ``InstanceType`` is EBS-optimized.
    """


_ListInstanceFleetsPaginateResponseInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef = TypedDict(
    "_ListInstanceFleetsPaginateResponseInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef",
    {"TimeoutDurationMinutes": int, "TimeoutAction": str, "BlockDurationMinutes": int},
    total=False,
)


class ListInstanceFleetsPaginateResponseInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef(
    _ListInstanceFleetsPaginateResponseInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef
):
    """
    Type definition for `ListInstanceFleetsPaginateResponseInstanceFleetsLaunchSpecifications` `SpotSpecification`

    The launch specification for Spot instances in the fleet, which determines the defined
    duration and provisioning timeout behavior.

    - **TimeoutDurationMinutes** *(integer) --*

      The spot provisioning timeout period in minutes. If Spot instances are not
      provisioned within this time period, the ``TimeOutAction`` is taken. Minimum value is
      5 and maximum value is 1440. The timeout applies only during initial provisioning,
      when the cluster is first created.

    - **TimeoutAction** *(string) --*

      The action to take when ``TargetSpotCapacity`` has not been fulfilled when the
      ``TimeoutDurationMinutes`` has expired; that is, when all Spot instances could not be
      provisioned within the Spot provisioning timeout. Valid values are
      ``TERMINATE_CLUSTER`` and ``SWITCH_TO_ON_DEMAND`` . SWITCH_TO_ON_DEMAND specifies
      that if no Spot instances are available, On-Demand Instances should be provisioned to
      fulfill any remaining Spot capacity.

    - **BlockDurationMinutes** *(integer) --*

      The defined duration for Spot instances (also known as Spot blocks) in minutes. When
      specified, the Spot instance does not terminate before the defined duration expires,
      and defined duration pricing for Spot instances applies. Valid values are 60, 120,
      180, 240, 300, or 360. The duration period starts as soon as a Spot instance receives
      its instance ID. At the end of the duration, Amazon EC2 marks the Spot instance for
      termination and provides a Spot instance termination notice, which gives the instance
      a two-minute warning before it terminates.
    """


_ListInstanceFleetsPaginateResponseInstanceFleetsLaunchSpecificationsTypeDef = TypedDict(
    "_ListInstanceFleetsPaginateResponseInstanceFleetsLaunchSpecificationsTypeDef",
    {
        "SpotSpecification": ListInstanceFleetsPaginateResponseInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef
    },
    total=False,
)


class ListInstanceFleetsPaginateResponseInstanceFleetsLaunchSpecificationsTypeDef(
    _ListInstanceFleetsPaginateResponseInstanceFleetsLaunchSpecificationsTypeDef
):
    """
    Type definition for `ListInstanceFleetsPaginateResponseInstanceFleets` `LaunchSpecifications`

    Describes the launch specification for an instance fleet.

    - **SpotSpecification** *(dict) --*

      The launch specification for Spot instances in the fleet, which determines the defined
      duration and provisioning timeout behavior.

      - **TimeoutDurationMinutes** *(integer) --*

        The spot provisioning timeout period in minutes. If Spot instances are not
        provisioned within this time period, the ``TimeOutAction`` is taken. Minimum value is
        5 and maximum value is 1440. The timeout applies only during initial provisioning,
        when the cluster is first created.

      - **TimeoutAction** *(string) --*

        The action to take when ``TargetSpotCapacity`` has not been fulfilled when the
        ``TimeoutDurationMinutes`` has expired; that is, when all Spot instances could not be
        provisioned within the Spot provisioning timeout. Valid values are
        ``TERMINATE_CLUSTER`` and ``SWITCH_TO_ON_DEMAND`` . SWITCH_TO_ON_DEMAND specifies
        that if no Spot instances are available, On-Demand Instances should be provisioned to
        fulfill any remaining Spot capacity.

      - **BlockDurationMinutes** *(integer) --*

        The defined duration for Spot instances (also known as Spot blocks) in minutes. When
        specified, the Spot instance does not terminate before the defined duration expires,
        and defined duration pricing for Spot instances applies. Valid values are 60, 120,
        180, 240, 300, or 360. The duration period starts as soon as a Spot instance receives
        its instance ID. At the end of the duration, Amazon EC2 marks the Spot instance for
        termination and provides a Spot instance termination notice, which gives the instance
        a two-minute warning before it terminates.
    """


_ListInstanceFleetsPaginateResponseInstanceFleetsStatusStateChangeReasonTypeDef = TypedDict(
    "_ListInstanceFleetsPaginateResponseInstanceFleetsStatusStateChangeReasonTypeDef",
    {"Code": str, "Message": str},
    total=False,
)


class ListInstanceFleetsPaginateResponseInstanceFleetsStatusStateChangeReasonTypeDef(
    _ListInstanceFleetsPaginateResponseInstanceFleetsStatusStateChangeReasonTypeDef
):
    """
    Type definition for `ListInstanceFleetsPaginateResponseInstanceFleetsStatus` `StateChangeReason`

    Provides status change reason details for the instance fleet.

    - **Code** *(string) --*

      A code corresponding to the reason the state change occurred.

    - **Message** *(string) --*

      An explanatory message.
    """


_ListInstanceFleetsPaginateResponseInstanceFleetsStatusTimelineTypeDef = TypedDict(
    "_ListInstanceFleetsPaginateResponseInstanceFleetsStatusTimelineTypeDef",
    {"CreationDateTime": datetime, "ReadyDateTime": datetime, "EndDateTime": datetime},
    total=False,
)


class ListInstanceFleetsPaginateResponseInstanceFleetsStatusTimelineTypeDef(
    _ListInstanceFleetsPaginateResponseInstanceFleetsStatusTimelineTypeDef
):
    """
    Type definition for `ListInstanceFleetsPaginateResponseInstanceFleetsStatus` `Timeline`

    Provides historical timestamps for the instance fleet, including the time of creation,
    the time it became ready to run jobs, and the time of termination.

    - **CreationDateTime** *(datetime) --*

      The time and date the instance fleet was created.

    - **ReadyDateTime** *(datetime) --*

      The time and date the instance fleet was ready to run jobs.

    - **EndDateTime** *(datetime) --*

      The time and date the instance fleet terminated.
    """


_ListInstanceFleetsPaginateResponseInstanceFleetsStatusTypeDef = TypedDict(
    "_ListInstanceFleetsPaginateResponseInstanceFleetsStatusTypeDef",
    {
        "State": str,
        "StateChangeReason": ListInstanceFleetsPaginateResponseInstanceFleetsStatusStateChangeReasonTypeDef,
        "Timeline": ListInstanceFleetsPaginateResponseInstanceFleetsStatusTimelineTypeDef,
    },
    total=False,
)


class ListInstanceFleetsPaginateResponseInstanceFleetsStatusTypeDef(
    _ListInstanceFleetsPaginateResponseInstanceFleetsStatusTypeDef
):
    """
    Type definition for `ListInstanceFleetsPaginateResponseInstanceFleets` `Status`

    The current status of the instance fleet.

    - **State** *(string) --*

      A code representing the instance fleet status.

      * ``PROVISIONING`` —The instance fleet is provisioning EC2 resources and is not yet
      ready to run jobs.

      * ``BOOTSTRAPPING`` —EC2 instances and other resources have been provisioned and the
      bootstrap actions specified for the instances are underway.

      * ``RUNNING`` —EC2 instances and other resources are running. They are either executing
      jobs or waiting to execute jobs.

      * ``RESIZING`` —A resize operation is underway. EC2 instances are either being added or
      removed.

      * ``SUSPENDED`` —A resize operation could not complete. Existing EC2 instances are
      running, but instances can't be added or removed.

      * ``TERMINATING`` —The instance fleet is terminating EC2 instances.

      * ``TERMINATED`` —The instance fleet is no longer active, and all EC2 instances have
      been terminated.

    - **StateChangeReason** *(dict) --*

      Provides status change reason details for the instance fleet.

      - **Code** *(string) --*

        A code corresponding to the reason the state change occurred.

      - **Message** *(string) --*

        An explanatory message.

    - **Timeline** *(dict) --*

      Provides historical timestamps for the instance fleet, including the time of creation,
      the time it became ready to run jobs, and the time of termination.

      - **CreationDateTime** *(datetime) --*

        The time and date the instance fleet was created.

      - **ReadyDateTime** *(datetime) --*

        The time and date the instance fleet was ready to run jobs.

      - **EndDateTime** *(datetime) --*

        The time and date the instance fleet terminated.
    """


_ListInstanceFleetsPaginateResponseInstanceFleetsTypeDef = TypedDict(
    "_ListInstanceFleetsPaginateResponseInstanceFleetsTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": ListInstanceFleetsPaginateResponseInstanceFleetsStatusTypeDef,
        "InstanceFleetType": str,
        "TargetOnDemandCapacity": int,
        "TargetSpotCapacity": int,
        "ProvisionedOnDemandCapacity": int,
        "ProvisionedSpotCapacity": int,
        "InstanceTypeSpecifications": List[
            ListInstanceFleetsPaginateResponseInstanceFleetsInstanceTypeSpecificationsTypeDef
        ],
        "LaunchSpecifications": ListInstanceFleetsPaginateResponseInstanceFleetsLaunchSpecificationsTypeDef,
    },
    total=False,
)


class ListInstanceFleetsPaginateResponseInstanceFleetsTypeDef(
    _ListInstanceFleetsPaginateResponseInstanceFleetsTypeDef
):
    """
    Type definition for `ListInstanceFleetsPaginateResponse` `InstanceFleets`

    Describes an instance fleet, which is a group of EC2 instances that host a particular node
    type (master, core, or task) in an Amazon EMR cluster. Instance fleets can consist of a mix
    of instance types and On-Demand and Spot instances, which are provisioned to meet a defined
    target capacity.

    .. note::

      The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and
      later, excluding 5.0.x versions.

    - **Id** *(string) --*

      The unique identifier of the instance fleet.

    - **Name** *(string) --*

      A friendly name for the instance fleet.

    - **Status** *(dict) --*

      The current status of the instance fleet.

      - **State** *(string) --*

        A code representing the instance fleet status.

        * ``PROVISIONING`` —The instance fleet is provisioning EC2 resources and is not yet
        ready to run jobs.

        * ``BOOTSTRAPPING`` —EC2 instances and other resources have been provisioned and the
        bootstrap actions specified for the instances are underway.

        * ``RUNNING`` —EC2 instances and other resources are running. They are either executing
        jobs or waiting to execute jobs.

        * ``RESIZING`` —A resize operation is underway. EC2 instances are either being added or
        removed.

        * ``SUSPENDED`` —A resize operation could not complete. Existing EC2 instances are
        running, but instances can't be added or removed.

        * ``TERMINATING`` —The instance fleet is terminating EC2 instances.

        * ``TERMINATED`` —The instance fleet is no longer active, and all EC2 instances have
        been terminated.

      - **StateChangeReason** *(dict) --*

        Provides status change reason details for the instance fleet.

        - **Code** *(string) --*

          A code corresponding to the reason the state change occurred.

        - **Message** *(string) --*

          An explanatory message.

      - **Timeline** *(dict) --*

        Provides historical timestamps for the instance fleet, including the time of creation,
        the time it became ready to run jobs, and the time of termination.

        - **CreationDateTime** *(datetime) --*

          The time and date the instance fleet was created.

        - **ReadyDateTime** *(datetime) --*

          The time and date the instance fleet was ready to run jobs.

        - **EndDateTime** *(datetime) --*

          The time and date the instance fleet terminated.

    - **InstanceFleetType** *(string) --*

      The node type that the instance fleet hosts. Valid values are MASTER, CORE, or TASK.

    - **TargetOnDemandCapacity** *(integer) --*

      The target capacity of On-Demand units for the instance fleet, which determines how many
      On-Demand instances to provision. When the instance fleet launches, Amazon EMR tries to
      provision On-Demand instances as specified by  InstanceTypeConfig . Each instance
      configuration has a specified ``WeightedCapacity`` . When an On-Demand instance is
      provisioned, the ``WeightedCapacity`` units count toward the target capacity. Amazon EMR
      provisions instances until the target capacity is totally fulfilled, even if this results
      in an overage. For example, if there are 2 units remaining to fulfill capacity, and
      Amazon EMR can only provision an instance with a ``WeightedCapacity`` of 5 units, the
      instance is provisioned, and the target capacity is exceeded by 3 units. You can use
      InstanceFleet$ProvisionedOnDemandCapacity to determine the Spot capacity units that have
      been provisioned for the instance fleet.

      .. note::

        If not specified or set to 0, only Spot instances are provisioned for the instance
        fleet using ``TargetSpotCapacity`` . At least one of ``TargetSpotCapacity`` and
        ``TargetOnDemandCapacity`` should be greater than 0. For a master instance fleet, only
        one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` can be specified, and its
        value must be 1.

    - **TargetSpotCapacity** *(integer) --*

      The target capacity of Spot units for the instance fleet, which determines how many Spot
      instances to provision. When the instance fleet launches, Amazon EMR tries to provision
      Spot instances as specified by  InstanceTypeConfig . Each instance configuration has a
      specified ``WeightedCapacity`` . When a Spot instance is provisioned, the
      ``WeightedCapacity`` units count toward the target capacity. Amazon EMR provisions
      instances until the target capacity is totally fulfilled, even if this results in an
      overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR
      can only provision an instance with a ``WeightedCapacity`` of 5 units, the instance is
      provisioned, and the target capacity is exceeded by 3 units. You can use
      InstanceFleet$ProvisionedSpotCapacity to determine the Spot capacity units that have been
      provisioned for the instance fleet.

      .. note::

        If not specified or set to 0, only On-Demand instances are provisioned for the instance
        fleet. At least one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` should be
        greater than 0. For a master instance fleet, only one of ``TargetSpotCapacity`` and
        ``TargetOnDemandCapacity`` can be specified, and its value must be 1.

    - **ProvisionedOnDemandCapacity** *(integer) --*

      The number of On-Demand units that have been provisioned for the instance fleet to
      fulfill ``TargetOnDemandCapacity`` . This provisioned capacity might be less than or
      greater than ``TargetOnDemandCapacity`` .

    - **ProvisionedSpotCapacity** *(integer) --*

      The number of Spot units that have been provisioned for this instance fleet to fulfill
      ``TargetSpotCapacity`` . This provisioned capacity might be less than or greater than
      ``TargetSpotCapacity`` .

    - **InstanceTypeSpecifications** *(list) --*

      The specification for the instance types that comprise an instance fleet. Up to five
      unique instance specifications may be defined for each instance fleet.

      - *(dict) --*

        The configuration specification for each instance type in an instance fleet.

        .. note::

          The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and
          later, excluding 5.0.x versions.

        - **InstanceType** *(string) --*

          The EC2 instance type, for example ``m3.xlarge`` .

        - **WeightedCapacity** *(integer) --*

          The number of units that a provisioned instance of this type provides toward
          fulfilling the target capacities defined in  InstanceFleetConfig . Capacity values
          represent performance characteristics such as vCPUs, memory, or I/O. If not
          specified, the default value is 1.

        - **BidPrice** *(string) --*

          The bid price for each EC2 Spot instance type as defined by ``InstanceType`` .
          Expressed in USD.

        - **BidPriceAsPercentageOfOnDemandPrice** *(float) --*

          The bid price, as a percentage of On-Demand price, for each EC2 Spot instance as
          defined by ``InstanceType`` . Expressed as a number (for example, 20 specifies 20%).

        - **Configurations** *(list) --*

          A configuration classification that applies when provisioning cluster instances,
          which can include configurations for applications and software bundled with Amazon
          EMR.

          - *(dict) --*

            .. note::

              Amazon EMR releases 4.x or later.

            An optional configuration specification to be used when provisioning cluster
            instances, which can include configurations for applications and software bundled
            with Amazon EMR. A configuration consists of a classification, properties, and
            optional nested configurations. A classification refers to an application-specific
            configuration file. Properties are the settings you want to change in that file.
            For more information, see `Configuring Applications
            <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

            - **Classification** *(string) --*

              The classification within a configuration.

            - **Configurations** *(list) --*

              A list of additional configurations to apply within a configuration object.

            - **Properties** *(dict) --*

              A set of properties specified within a configuration classification.

              - *(string) --*

                - *(string) --*

        - **EbsBlockDevices** *(list) --*

          The configuration of Amazon Elastic Block Storage (EBS) attached to each instance as
          defined by ``InstanceType`` .

          - *(dict) --*

            Configuration of requested EBS block device associated with the instance group.

            - **VolumeSpecification** *(dict) --*

              EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
              requested for the EBS volume attached to an EC2 instance in the cluster.

              - **VolumeType** *(string) --*

                The volume type. Volume types supported are gp2, io1, standard.

              - **Iops** *(integer) --*

                The number of I/O operations per second (IOPS) that the volume supports.

              - **SizeInGB** *(integer) --*

                The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
                volume type is EBS-optimized, the minimum value is 10.

            - **Device** *(string) --*

              The device name that is exposed to the instance, such as /dev/sdh.

        - **EbsOptimized** *(boolean) --*

          Evaluates to ``TRUE`` when the specified ``InstanceType`` is EBS-optimized.

    - **LaunchSpecifications** *(dict) --*

      Describes the launch specification for an instance fleet.

      - **SpotSpecification** *(dict) --*

        The launch specification for Spot instances in the fleet, which determines the defined
        duration and provisioning timeout behavior.

        - **TimeoutDurationMinutes** *(integer) --*

          The spot provisioning timeout period in minutes. If Spot instances are not
          provisioned within this time period, the ``TimeOutAction`` is taken. Minimum value is
          5 and maximum value is 1440. The timeout applies only during initial provisioning,
          when the cluster is first created.

        - **TimeoutAction** *(string) --*

          The action to take when ``TargetSpotCapacity`` has not been fulfilled when the
          ``TimeoutDurationMinutes`` has expired; that is, when all Spot instances could not be
          provisioned within the Spot provisioning timeout. Valid values are
          ``TERMINATE_CLUSTER`` and ``SWITCH_TO_ON_DEMAND`` . SWITCH_TO_ON_DEMAND specifies
          that if no Spot instances are available, On-Demand Instances should be provisioned to
          fulfill any remaining Spot capacity.

        - **BlockDurationMinutes** *(integer) --*

          The defined duration for Spot instances (also known as Spot blocks) in minutes. When
          specified, the Spot instance does not terminate before the defined duration expires,
          and defined duration pricing for Spot instances applies. Valid values are 60, 120,
          180, 240, 300, or 360. The duration period starts as soon as a Spot instance receives
          its instance ID. At the end of the duration, Amazon EC2 marks the Spot instance for
          termination and provides a Spot instance termination notice, which gives the instance
          a two-minute warning before it terminates.
    """


_ListInstanceFleetsPaginateResponseTypeDef = TypedDict(
    "_ListInstanceFleetsPaginateResponseTypeDef",
    {
        "InstanceFleets": List[ListInstanceFleetsPaginateResponseInstanceFleetsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListInstanceFleetsPaginateResponseTypeDef(
    _ListInstanceFleetsPaginateResponseTypeDef
):
    """
    Type definition for `ListInstanceFleetsPaginate` `Response`

    - **InstanceFleets** *(list) --*

      The list of instance fleets for the cluster and given filters.

      - *(dict) --*

        Describes an instance fleet, which is a group of EC2 instances that host a particular node
        type (master, core, or task) in an Amazon EMR cluster. Instance fleets can consist of a mix
        of instance types and On-Demand and Spot instances, which are provisioned to meet a defined
        target capacity.

        .. note::

          The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and
          later, excluding 5.0.x versions.

        - **Id** *(string) --*

          The unique identifier of the instance fleet.

        - **Name** *(string) --*

          A friendly name for the instance fleet.

        - **Status** *(dict) --*

          The current status of the instance fleet.

          - **State** *(string) --*

            A code representing the instance fleet status.

            * ``PROVISIONING`` —The instance fleet is provisioning EC2 resources and is not yet
            ready to run jobs.

            * ``BOOTSTRAPPING`` —EC2 instances and other resources have been provisioned and the
            bootstrap actions specified for the instances are underway.

            * ``RUNNING`` —EC2 instances and other resources are running. They are either executing
            jobs or waiting to execute jobs.

            * ``RESIZING`` —A resize operation is underway. EC2 instances are either being added or
            removed.

            * ``SUSPENDED`` —A resize operation could not complete. Existing EC2 instances are
            running, but instances can't be added or removed.

            * ``TERMINATING`` —The instance fleet is terminating EC2 instances.

            * ``TERMINATED`` —The instance fleet is no longer active, and all EC2 instances have
            been terminated.

          - **StateChangeReason** *(dict) --*

            Provides status change reason details for the instance fleet.

            - **Code** *(string) --*

              A code corresponding to the reason the state change occurred.

            - **Message** *(string) --*

              An explanatory message.

          - **Timeline** *(dict) --*

            Provides historical timestamps for the instance fleet, including the time of creation,
            the time it became ready to run jobs, and the time of termination.

            - **CreationDateTime** *(datetime) --*

              The time and date the instance fleet was created.

            - **ReadyDateTime** *(datetime) --*

              The time and date the instance fleet was ready to run jobs.

            - **EndDateTime** *(datetime) --*

              The time and date the instance fleet terminated.

        - **InstanceFleetType** *(string) --*

          The node type that the instance fleet hosts. Valid values are MASTER, CORE, or TASK.

        - **TargetOnDemandCapacity** *(integer) --*

          The target capacity of On-Demand units for the instance fleet, which determines how many
          On-Demand instances to provision. When the instance fleet launches, Amazon EMR tries to
          provision On-Demand instances as specified by  InstanceTypeConfig . Each instance
          configuration has a specified ``WeightedCapacity`` . When an On-Demand instance is
          provisioned, the ``WeightedCapacity`` units count toward the target capacity. Amazon EMR
          provisions instances until the target capacity is totally fulfilled, even if this results
          in an overage. For example, if there are 2 units remaining to fulfill capacity, and
          Amazon EMR can only provision an instance with a ``WeightedCapacity`` of 5 units, the
          instance is provisioned, and the target capacity is exceeded by 3 units. You can use
          InstanceFleet$ProvisionedOnDemandCapacity to determine the Spot capacity units that have
          been provisioned for the instance fleet.

          .. note::

            If not specified or set to 0, only Spot instances are provisioned for the instance
            fleet using ``TargetSpotCapacity`` . At least one of ``TargetSpotCapacity`` and
            ``TargetOnDemandCapacity`` should be greater than 0. For a master instance fleet, only
            one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` can be specified, and its
            value must be 1.

        - **TargetSpotCapacity** *(integer) --*

          The target capacity of Spot units for the instance fleet, which determines how many Spot
          instances to provision. When the instance fleet launches, Amazon EMR tries to provision
          Spot instances as specified by  InstanceTypeConfig . Each instance configuration has a
          specified ``WeightedCapacity`` . When a Spot instance is provisioned, the
          ``WeightedCapacity`` units count toward the target capacity. Amazon EMR provisions
          instances until the target capacity is totally fulfilled, even if this results in an
          overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR
          can only provision an instance with a ``WeightedCapacity`` of 5 units, the instance is
          provisioned, and the target capacity is exceeded by 3 units. You can use
          InstanceFleet$ProvisionedSpotCapacity to determine the Spot capacity units that have been
          provisioned for the instance fleet.

          .. note::

            If not specified or set to 0, only On-Demand instances are provisioned for the instance
            fleet. At least one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` should be
            greater than 0. For a master instance fleet, only one of ``TargetSpotCapacity`` and
            ``TargetOnDemandCapacity`` can be specified, and its value must be 1.

        - **ProvisionedOnDemandCapacity** *(integer) --*

          The number of On-Demand units that have been provisioned for the instance fleet to
          fulfill ``TargetOnDemandCapacity`` . This provisioned capacity might be less than or
          greater than ``TargetOnDemandCapacity`` .

        - **ProvisionedSpotCapacity** *(integer) --*

          The number of Spot units that have been provisioned for this instance fleet to fulfill
          ``TargetSpotCapacity`` . This provisioned capacity might be less than or greater than
          ``TargetSpotCapacity`` .

        - **InstanceTypeSpecifications** *(list) --*

          The specification for the instance types that comprise an instance fleet. Up to five
          unique instance specifications may be defined for each instance fleet.

          - *(dict) --*

            The configuration specification for each instance type in an instance fleet.

            .. note::

              The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and
              later, excluding 5.0.x versions.

            - **InstanceType** *(string) --*

              The EC2 instance type, for example ``m3.xlarge`` .

            - **WeightedCapacity** *(integer) --*

              The number of units that a provisioned instance of this type provides toward
              fulfilling the target capacities defined in  InstanceFleetConfig . Capacity values
              represent performance characteristics such as vCPUs, memory, or I/O. If not
              specified, the default value is 1.

            - **BidPrice** *(string) --*

              The bid price for each EC2 Spot instance type as defined by ``InstanceType`` .
              Expressed in USD.

            - **BidPriceAsPercentageOfOnDemandPrice** *(float) --*

              The bid price, as a percentage of On-Demand price, for each EC2 Spot instance as
              defined by ``InstanceType`` . Expressed as a number (for example, 20 specifies 20%).

            - **Configurations** *(list) --*

              A configuration classification that applies when provisioning cluster instances,
              which can include configurations for applications and software bundled with Amazon
              EMR.

              - *(dict) --*

                .. note::

                  Amazon EMR releases 4.x or later.

                An optional configuration specification to be used when provisioning cluster
                instances, which can include configurations for applications and software bundled
                with Amazon EMR. A configuration consists of a classification, properties, and
                optional nested configurations. A classification refers to an application-specific
                configuration file. Properties are the settings you want to change in that file.
                For more information, see `Configuring Applications
                <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

                - **Classification** *(string) --*

                  The classification within a configuration.

                - **Configurations** *(list) --*

                  A list of additional configurations to apply within a configuration object.

                - **Properties** *(dict) --*

                  A set of properties specified within a configuration classification.

                  - *(string) --*

                    - *(string) --*

            - **EbsBlockDevices** *(list) --*

              The configuration of Amazon Elastic Block Storage (EBS) attached to each instance as
              defined by ``InstanceType`` .

              - *(dict) --*

                Configuration of requested EBS block device associated with the instance group.

                - **VolumeSpecification** *(dict) --*

                  EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
                  requested for the EBS volume attached to an EC2 instance in the cluster.

                  - **VolumeType** *(string) --*

                    The volume type. Volume types supported are gp2, io1, standard.

                  - **Iops** *(integer) --*

                    The number of I/O operations per second (IOPS) that the volume supports.

                  - **SizeInGB** *(integer) --*

                    The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
                    volume type is EBS-optimized, the minimum value is 10.

                - **Device** *(string) --*

                  The device name that is exposed to the instance, such as /dev/sdh.

            - **EbsOptimized** *(boolean) --*

              Evaluates to ``TRUE`` when the specified ``InstanceType`` is EBS-optimized.

        - **LaunchSpecifications** *(dict) --*

          Describes the launch specification for an instance fleet.

          - **SpotSpecification** *(dict) --*

            The launch specification for Spot instances in the fleet, which determines the defined
            duration and provisioning timeout behavior.

            - **TimeoutDurationMinutes** *(integer) --*

              The spot provisioning timeout period in minutes. If Spot instances are not
              provisioned within this time period, the ``TimeOutAction`` is taken. Minimum value is
              5 and maximum value is 1440. The timeout applies only during initial provisioning,
              when the cluster is first created.

            - **TimeoutAction** *(string) --*

              The action to take when ``TargetSpotCapacity`` has not been fulfilled when the
              ``TimeoutDurationMinutes`` has expired; that is, when all Spot instances could not be
              provisioned within the Spot provisioning timeout. Valid values are
              ``TERMINATE_CLUSTER`` and ``SWITCH_TO_ON_DEMAND`` . SWITCH_TO_ON_DEMAND specifies
              that if no Spot instances are available, On-Demand Instances should be provisioned to
              fulfill any remaining Spot capacity.

            - **BlockDurationMinutes** *(integer) --*

              The defined duration for Spot instances (also known as Spot blocks) in minutes. When
              specified, the Spot instance does not terminate before the defined duration expires,
              and defined duration pricing for Spot instances applies. Valid values are 60, 120,
              180, 240, 300, or 360. The duration period starts as soon as a Spot instance receives
              its instance ID. At the end of the duration, Amazon EC2 marks the Spot instance for
              termination and provides a Spot instance termination notice, which gives the instance
              a two-minute warning before it terminates.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListInstanceGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListInstanceGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListInstanceGroupsPaginatePaginationConfigTypeDef(
    _ListInstanceGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListInstanceGroupsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyConstraintsTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyConstraintsTypeDef",
    {"MinCapacity": int, "MaxCapacity": int},
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyConstraintsTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyConstraintsTypeDef
):
    """
    Type definition for `ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicy` `Constraints`

    The upper and lower EC2 instance limits for an automatic scaling policy. Automatic
    scaling activity will not cause an instance group to grow above or below these limits.

    - **MinCapacity** *(integer) --*

      The lower boundary of EC2 instances in an instance group below which scaling
      activities are not allowed to shrink. Scale-in activities will not terminate
      instances below this boundary.

    - **MaxCapacity** *(integer) --*

      The upper boundary of EC2 instances in an instance group beyond which scaling
      activities are not allowed to grow. Scale-out activities will not add instances
      beyond this boundary.
    """


_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    {"AdjustmentType": str, "ScalingAdjustment": int, "CoolDown": int},
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef
):
    """
    Type definition for `ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesAction` `SimpleScalingPolicyConfiguration`

    The type of adjustment the automatic scaling activity makes when triggered, and
    the periodicity of the adjustment.

    - **AdjustmentType** *(string) --*

      The way in which EC2 instances are added (if ``ScalingAdjustment`` is a
      positive number) or terminated (if ``ScalingAdjustment`` is a negative number)
      each time the scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the
      default. ``CHANGE_IN_CAPACITY`` indicates that the EC2 instance count
      increments or decrements by ``ScalingAdjustment`` , which should be expressed
      as an integer. ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count
      increments or decrements by the percentage specified by ``ScalingAdjustment`` ,
      which should be expressed as an integer. For example, 20 indicates an increase
      in 20% increments of cluster capacity. ``EXACT_CAPACITY`` indicates the scaling
      activity results in an instance group with the number of EC2 instances
      specified by ``ScalingAdjustment`` , which should be expressed as a positive
      integer.

    - **ScalingAdjustment** *(integer) --*

      The amount by which to scale in or scale out, based on the specified
      ``AdjustmentType`` . A positive value adds to the instance group's EC2 instance
      count while a negative number removes instances. If ``AdjustmentType`` is set
      to ``EXACT_CAPACITY`` , the number should only be a positive integer. If
      ``AdjustmentType`` is set to ``PERCENT_CHANGE_IN_CAPACITY`` , the value should
      express the percentage as an integer. For example, -20 indicates a decrease in
      20% increments of cluster capacity.

    - **CoolDown** *(integer) --*

      The amount of time, in seconds, after a scaling activity completes before any
      further trigger-related scaling activities can start. The default value is 0.
    """


_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesActionTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesActionTypeDef",
    {
        "Market": str,
        "SimpleScalingPolicyConfiguration": ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef,
    },
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesActionTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesActionTypeDef
):
    """
    Type definition for `ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRules` `Action`

    The conditions that trigger an automatic scaling activity.

    - **Market** *(string) --*

      Not available for instance groups. Instance groups use the market type specified
      for the group.

    - **SimpleScalingPolicyConfiguration** *(dict) --*

      The type of adjustment the automatic scaling activity makes when triggered, and
      the periodicity of the adjustment.

      - **AdjustmentType** *(string) --*

        The way in which EC2 instances are added (if ``ScalingAdjustment`` is a
        positive number) or terminated (if ``ScalingAdjustment`` is a negative number)
        each time the scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the
        default. ``CHANGE_IN_CAPACITY`` indicates that the EC2 instance count
        increments or decrements by ``ScalingAdjustment`` , which should be expressed
        as an integer. ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count
        increments or decrements by the percentage specified by ``ScalingAdjustment`` ,
        which should be expressed as an integer. For example, 20 indicates an increase
        in 20% increments of cluster capacity. ``EXACT_CAPACITY`` indicates the scaling
        activity results in an instance group with the number of EC2 instances
        specified by ``ScalingAdjustment`` , which should be expressed as a positive
        integer.

      - **ScalingAdjustment** *(integer) --*

        The amount by which to scale in or scale out, based on the specified
        ``AdjustmentType`` . A positive value adds to the instance group's EC2 instance
        count while a negative number removes instances. If ``AdjustmentType`` is set
        to ``EXACT_CAPACITY`` , the number should only be a positive integer. If
        ``AdjustmentType`` is set to ``PERCENT_CHANGE_IN_CAPACITY`` , the value should
        express the percentage as an integer. For example, -20 indicates a decrease in
        20% increments of cluster capacity.

      - **CoolDown** *(integer) --*

        The amount of time, in seconds, after a scaling activity completes before any
        further trigger-related scaling activities can start. The default value is 0.
    """


_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef
):
    """
    Type definition for `ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinition` `Dimensions`

    A CloudWatch dimension, which is specified using a ``Key`` (known as a
    ``Name`` in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one
    dimension whose ``Key`` is ``JobFlowID`` and ``Value`` is a variable
    representing the cluster ID, which is ``${emr.clusterId}`` . This enables the
    rule to bootstrap when the cluster ID becomes available.

    - **Key** *(string) --*

      The dimension name.

    - **Value** *(string) --*

      The dimension value.
    """


_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    {
        "ComparisonOperator": str,
        "EvaluationPeriods": int,
        "MetricName": str,
        "Namespace": str,
        "Period": int,
        "Statistic": str,
        "Threshold": float,
        "Unit": str,
        "Dimensions": List[
            ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef
        ],
    },
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef
):
    """
    Type definition for `ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTrigger` `CloudWatchAlarmDefinition`

    The definition of a CloudWatch metric alarm. When the defined alarm conditions
    are met along with other trigger parameters, scaling activity begins.

    - **ComparisonOperator** *(string) --*

      Determines how the metric specified by ``MetricName`` is compared to the value
      specified by ``Threshold`` .

    - **EvaluationPeriods** *(integer) --*

      The number of periods, in five-minute increments, during which the alarm
      condition must exist before the alarm triggers automatic scaling activity. The
      default value is ``1`` .

    - **MetricName** *(string) --*

      The name of the CloudWatch metric that is watched to determine an alarm
      condition.

    - **Namespace** *(string) --*

      The namespace for the CloudWatch metric. The default is
      ``AWS/ElasticMapReduce`` .

    - **Period** *(integer) --*

      The period, in seconds, over which the statistic is applied. EMR CloudWatch
      metrics are emitted every five minutes (300 seconds), so if an EMR CloudWatch
      metric is specified, specify ``300`` .

    - **Statistic** *(string) --*

      The statistic to apply to the metric associated with the alarm. The default is
      ``AVERAGE`` .

    - **Threshold** *(float) --*

      The value against which the specified statistic is compared.

    - **Unit** *(string) --*

      The unit of measure associated with the CloudWatch metric being watched. The
      value specified for ``Unit`` must correspond to the units specified in the
      CloudWatch metric.

    - **Dimensions** *(list) --*

      A CloudWatch metric dimension.

      - *(dict) --*

        A CloudWatch dimension, which is specified using a ``Key`` (known as a
        ``Name`` in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one
        dimension whose ``Key`` is ``JobFlowID`` and ``Value`` is a variable
        representing the cluster ID, which is ``${emr.clusterId}`` . This enables the
        rule to bootstrap when the cluster ID becomes available.

        - **Key** *(string) --*

          The dimension name.

        - **Value** *(string) --*

          The dimension value.
    """


_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef",
    {
        "CloudWatchAlarmDefinition": ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef
    },
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef
):
    """
    Type definition for `ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRules` `Trigger`

    The CloudWatch alarm definition that determines when automatic scaling activity is
    triggered.

    - **CloudWatchAlarmDefinition** *(dict) --*

      The definition of a CloudWatch metric alarm. When the defined alarm conditions
      are met along with other trigger parameters, scaling activity begins.

      - **ComparisonOperator** *(string) --*

        Determines how the metric specified by ``MetricName`` is compared to the value
        specified by ``Threshold`` .

      - **EvaluationPeriods** *(integer) --*

        The number of periods, in five-minute increments, during which the alarm
        condition must exist before the alarm triggers automatic scaling activity. The
        default value is ``1`` .

      - **MetricName** *(string) --*

        The name of the CloudWatch metric that is watched to determine an alarm
        condition.

      - **Namespace** *(string) --*

        The namespace for the CloudWatch metric. The default is
        ``AWS/ElasticMapReduce`` .

      - **Period** *(integer) --*

        The period, in seconds, over which the statistic is applied. EMR CloudWatch
        metrics are emitted every five minutes (300 seconds), so if an EMR CloudWatch
        metric is specified, specify ``300`` .

      - **Statistic** *(string) --*

        The statistic to apply to the metric associated with the alarm. The default is
        ``AVERAGE`` .

      - **Threshold** *(float) --*

        The value against which the specified statistic is compared.

      - **Unit** *(string) --*

        The unit of measure associated with the CloudWatch metric being watched. The
        value specified for ``Unit`` must correspond to the units specified in the
        CloudWatch metric.

      - **Dimensions** *(list) --*

        A CloudWatch metric dimension.

        - *(dict) --*

          A CloudWatch dimension, which is specified using a ``Key`` (known as a
          ``Name`` in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one
          dimension whose ``Key`` is ``JobFlowID`` and ``Value`` is a variable
          representing the cluster ID, which is ``${emr.clusterId}`` . This enables the
          rule to bootstrap when the cluster ID becomes available.

          - **Key** *(string) --*

            The dimension name.

          - **Value** *(string) --*

            The dimension value.
    """


_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTypeDef",
    {
        "Name": str,
        "Description": str,
        "Action": ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesActionTypeDef,
        "Trigger": ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef,
    },
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTypeDef
):
    """
    Type definition for `ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicy` `Rules`

    A scale-in or scale-out rule that defines scaling activity, including the CloudWatch
    metric alarm that triggers activity, how EC2 instances are added or removed, and the
    periodicity of adjustments. The automatic scaling policy for an instance group can
    comprise one or more automatic scaling rules.

    - **Name** *(string) --*

      The name used to identify an automatic scaling rule. Rule names must be unique
      within a scaling policy.

    - **Description** *(string) --*

      A friendly, more verbose description of the automatic scaling rule.

    - **Action** *(dict) --*

      The conditions that trigger an automatic scaling activity.

      - **Market** *(string) --*

        Not available for instance groups. Instance groups use the market type specified
        for the group.

      - **SimpleScalingPolicyConfiguration** *(dict) --*

        The type of adjustment the automatic scaling activity makes when triggered, and
        the periodicity of the adjustment.

        - **AdjustmentType** *(string) --*

          The way in which EC2 instances are added (if ``ScalingAdjustment`` is a
          positive number) or terminated (if ``ScalingAdjustment`` is a negative number)
          each time the scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the
          default. ``CHANGE_IN_CAPACITY`` indicates that the EC2 instance count
          increments or decrements by ``ScalingAdjustment`` , which should be expressed
          as an integer. ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count
          increments or decrements by the percentage specified by ``ScalingAdjustment`` ,
          which should be expressed as an integer. For example, 20 indicates an increase
          in 20% increments of cluster capacity. ``EXACT_CAPACITY`` indicates the scaling
          activity results in an instance group with the number of EC2 instances
          specified by ``ScalingAdjustment`` , which should be expressed as a positive
          integer.

        - **ScalingAdjustment** *(integer) --*

          The amount by which to scale in or scale out, based on the specified
          ``AdjustmentType`` . A positive value adds to the instance group's EC2 instance
          count while a negative number removes instances. If ``AdjustmentType`` is set
          to ``EXACT_CAPACITY`` , the number should only be a positive integer. If
          ``AdjustmentType`` is set to ``PERCENT_CHANGE_IN_CAPACITY`` , the value should
          express the percentage as an integer. For example, -20 indicates a decrease in
          20% increments of cluster capacity.

        - **CoolDown** *(integer) --*

          The amount of time, in seconds, after a scaling activity completes before any
          further trigger-related scaling activities can start. The default value is 0.

    - **Trigger** *(dict) --*

      The CloudWatch alarm definition that determines when automatic scaling activity is
      triggered.

      - **CloudWatchAlarmDefinition** *(dict) --*

        The definition of a CloudWatch metric alarm. When the defined alarm conditions
        are met along with other trigger parameters, scaling activity begins.

        - **ComparisonOperator** *(string) --*

          Determines how the metric specified by ``MetricName`` is compared to the value
          specified by ``Threshold`` .

        - **EvaluationPeriods** *(integer) --*

          The number of periods, in five-minute increments, during which the alarm
          condition must exist before the alarm triggers automatic scaling activity. The
          default value is ``1`` .

        - **MetricName** *(string) --*

          The name of the CloudWatch metric that is watched to determine an alarm
          condition.

        - **Namespace** *(string) --*

          The namespace for the CloudWatch metric. The default is
          ``AWS/ElasticMapReduce`` .

        - **Period** *(integer) --*

          The period, in seconds, over which the statistic is applied. EMR CloudWatch
          metrics are emitted every five minutes (300 seconds), so if an EMR CloudWatch
          metric is specified, specify ``300`` .

        - **Statistic** *(string) --*

          The statistic to apply to the metric associated with the alarm. The default is
          ``AVERAGE`` .

        - **Threshold** *(float) --*

          The value against which the specified statistic is compared.

        - **Unit** *(string) --*

          The unit of measure associated with the CloudWatch metric being watched. The
          value specified for ``Unit`` must correspond to the units specified in the
          CloudWatch metric.

        - **Dimensions** *(list) --*

          A CloudWatch metric dimension.

          - *(dict) --*

            A CloudWatch dimension, which is specified using a ``Key`` (known as a
            ``Name`` in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one
            dimension whose ``Key`` is ``JobFlowID`` and ``Value`` is a variable
            representing the cluster ID, which is ``${emr.clusterId}`` . This enables the
            rule to bootstrap when the cluster ID becomes available.

            - **Key** *(string) --*

              The dimension name.

            - **Value** *(string) --*

              The dimension value.
    """


_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyStatusStateChangeReasonTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyStatusStateChangeReasonTypeDef",
    {"Code": str, "Message": str},
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyStatusStateChangeReasonTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyStatusStateChangeReasonTypeDef
):
    """
    Type definition for `ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyStatus` `StateChangeReason`

    The reason for a change in status.

    - **Code** *(string) --*

      The code indicating the reason for the change in status.``USER_REQUEST`` indicates
      that the scaling policy status was changed by a user. ``PROVISION_FAILURE``
      indicates that the status change was because the policy failed to provision.
      ``CLEANUP_FAILURE`` indicates an error.

    - **Message** *(string) --*

      A friendly, more verbose message that accompanies an automatic scaling policy state
      change.
    """


_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyStatusTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyStatusTypeDef",
    {
        "State": str,
        "StateChangeReason": ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyStatusStateChangeReasonTypeDef,
    },
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyStatusTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyStatusTypeDef
):
    """
    Type definition for `ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicy` `Status`

    The status of an automatic scaling policy.

    - **State** *(string) --*

      Indicates the status of the automatic scaling policy.

    - **StateChangeReason** *(dict) --*

      The reason for a change in status.

      - **Code** *(string) --*

        The code indicating the reason for the change in status.``USER_REQUEST`` indicates
        that the scaling policy status was changed by a user. ``PROVISION_FAILURE``
        indicates that the status change was because the policy failed to provision.
        ``CLEANUP_FAILURE`` indicates an error.

      - **Message** *(string) --*

        A friendly, more verbose message that accompanies an automatic scaling policy state
        change.
    """


_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyTypeDef",
    {
        "Status": ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyStatusTypeDef,
        "Constraints": ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyConstraintsTypeDef,
        "Rules": List[
            ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyRulesTypeDef
        ],
    },
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyTypeDef
):
    """
    Type definition for `ListInstanceGroupsPaginateResponseInstanceGroups` `AutoScalingPolicy`

    An automatic scaling policy for a core instance group or task instance group in an Amazon
    EMR cluster. The automatic scaling policy defines how an instance group dynamically adds
    and terminates EC2 instances in response to the value of a CloudWatch metric. See
    PutAutoScalingPolicy.

    - **Status** *(dict) --*

      The status of an automatic scaling policy.

      - **State** *(string) --*

        Indicates the status of the automatic scaling policy.

      - **StateChangeReason** *(dict) --*

        The reason for a change in status.

        - **Code** *(string) --*

          The code indicating the reason for the change in status.``USER_REQUEST`` indicates
          that the scaling policy status was changed by a user. ``PROVISION_FAILURE``
          indicates that the status change was because the policy failed to provision.
          ``CLEANUP_FAILURE`` indicates an error.

        - **Message** *(string) --*

          A friendly, more verbose message that accompanies an automatic scaling policy state
          change.

    - **Constraints** *(dict) --*

      The upper and lower EC2 instance limits for an automatic scaling policy. Automatic
      scaling activity will not cause an instance group to grow above or below these limits.

      - **MinCapacity** *(integer) --*

        The lower boundary of EC2 instances in an instance group below which scaling
        activities are not allowed to shrink. Scale-in activities will not terminate
        instances below this boundary.

      - **MaxCapacity** *(integer) --*

        The upper boundary of EC2 instances in an instance group beyond which scaling
        activities are not allowed to grow. Scale-out activities will not add instances
        beyond this boundary.

    - **Rules** *(list) --*

      The scale-in and scale-out rules that comprise the automatic scaling policy.

      - *(dict) --*

        A scale-in or scale-out rule that defines scaling activity, including the CloudWatch
        metric alarm that triggers activity, how EC2 instances are added or removed, and the
        periodicity of adjustments. The automatic scaling policy for an instance group can
        comprise one or more automatic scaling rules.

        - **Name** *(string) --*

          The name used to identify an automatic scaling rule. Rule names must be unique
          within a scaling policy.

        - **Description** *(string) --*

          A friendly, more verbose description of the automatic scaling rule.

        - **Action** *(dict) --*

          The conditions that trigger an automatic scaling activity.

          - **Market** *(string) --*

            Not available for instance groups. Instance groups use the market type specified
            for the group.

          - **SimpleScalingPolicyConfiguration** *(dict) --*

            The type of adjustment the automatic scaling activity makes when triggered, and
            the periodicity of the adjustment.

            - **AdjustmentType** *(string) --*

              The way in which EC2 instances are added (if ``ScalingAdjustment`` is a
              positive number) or terminated (if ``ScalingAdjustment`` is a negative number)
              each time the scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the
              default. ``CHANGE_IN_CAPACITY`` indicates that the EC2 instance count
              increments or decrements by ``ScalingAdjustment`` , which should be expressed
              as an integer. ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count
              increments or decrements by the percentage specified by ``ScalingAdjustment`` ,
              which should be expressed as an integer. For example, 20 indicates an increase
              in 20% increments of cluster capacity. ``EXACT_CAPACITY`` indicates the scaling
              activity results in an instance group with the number of EC2 instances
              specified by ``ScalingAdjustment`` , which should be expressed as a positive
              integer.

            - **ScalingAdjustment** *(integer) --*

              The amount by which to scale in or scale out, based on the specified
              ``AdjustmentType`` . A positive value adds to the instance group's EC2 instance
              count while a negative number removes instances. If ``AdjustmentType`` is set
              to ``EXACT_CAPACITY`` , the number should only be a positive integer. If
              ``AdjustmentType`` is set to ``PERCENT_CHANGE_IN_CAPACITY`` , the value should
              express the percentage as an integer. For example, -20 indicates a decrease in
              20% increments of cluster capacity.

            - **CoolDown** *(integer) --*

              The amount of time, in seconds, after a scaling activity completes before any
              further trigger-related scaling activities can start. The default value is 0.

        - **Trigger** *(dict) --*

          The CloudWatch alarm definition that determines when automatic scaling activity is
          triggered.

          - **CloudWatchAlarmDefinition** *(dict) --*

            The definition of a CloudWatch metric alarm. When the defined alarm conditions
            are met along with other trigger parameters, scaling activity begins.

            - **ComparisonOperator** *(string) --*

              Determines how the metric specified by ``MetricName`` is compared to the value
              specified by ``Threshold`` .

            - **EvaluationPeriods** *(integer) --*

              The number of periods, in five-minute increments, during which the alarm
              condition must exist before the alarm triggers automatic scaling activity. The
              default value is ``1`` .

            - **MetricName** *(string) --*

              The name of the CloudWatch metric that is watched to determine an alarm
              condition.

            - **Namespace** *(string) --*

              The namespace for the CloudWatch metric. The default is
              ``AWS/ElasticMapReduce`` .

            - **Period** *(integer) --*

              The period, in seconds, over which the statistic is applied. EMR CloudWatch
              metrics are emitted every five minutes (300 seconds), so if an EMR CloudWatch
              metric is specified, specify ``300`` .

            - **Statistic** *(string) --*

              The statistic to apply to the metric associated with the alarm. The default is
              ``AVERAGE`` .

            - **Threshold** *(float) --*

              The value against which the specified statistic is compared.

            - **Unit** *(string) --*

              The unit of measure associated with the CloudWatch metric being watched. The
              value specified for ``Unit`` must correspond to the units specified in the
              CloudWatch metric.

            - **Dimensions** *(list) --*

              A CloudWatch metric dimension.

              - *(dict) --*

                A CloudWatch dimension, which is specified using a ``Key`` (known as a
                ``Name`` in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one
                dimension whose ``Key`` is ``JobFlowID`` and ``Value`` is a variable
                representing the cluster ID, which is ``${emr.clusterId}`` . This enables the
                rule to bootstrap when the cluster ID becomes available.

                - **Key** *(string) --*

                  The dimension name.

                - **Value** *(string) --*

                  The dimension value.
    """


_ListInstanceGroupsPaginateResponseInstanceGroupsConfigurationsTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsConfigurationsTypeDef",
    {"Classification": str, "Configurations": List[Any], "Properties": Dict[str, str]},
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsConfigurationsTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsConfigurationsTypeDef
):
    """
    Type definition for `ListInstanceGroupsPaginateResponseInstanceGroups` `Configurations`

    .. note::

      Amazon EMR releases 4.x or later.

    An optional configuration specification to be used when provisioning cluster instances,
    which can include configurations for applications and software bundled with Amazon EMR.
    A configuration consists of a classification, properties, and optional nested
    configurations. A classification refers to an application-specific configuration file.
    Properties are the settings you want to change in that file. For more information, see
    `Configuring Applications
    <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

    - **Classification** *(string) --*

      The classification within a configuration.

    - **Configurations** *(list) --*

      A list of additional configurations to apply within a configuration object.

    - **Properties** *(dict) --*

      A set of properties specified within a configuration classification.

      - *(string) --*

        - *(string) --*
    """


_ListInstanceGroupsPaginateResponseInstanceGroupsEbsBlockDevicesVolumeSpecificationTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsEbsBlockDevicesVolumeSpecificationTypeDef",
    {"VolumeType": str, "Iops": int, "SizeInGB": int},
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsEbsBlockDevicesVolumeSpecificationTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsEbsBlockDevicesVolumeSpecificationTypeDef
):
    """
    Type definition for `ListInstanceGroupsPaginateResponseInstanceGroupsEbsBlockDevices` `VolumeSpecification`

    EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
    requested for the EBS volume attached to an EC2 instance in the cluster.

    - **VolumeType** *(string) --*

      The volume type. Volume types supported are gp2, io1, standard.

    - **Iops** *(integer) --*

      The number of I/O operations per second (IOPS) that the volume supports.

    - **SizeInGB** *(integer) --*

      The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
      volume type is EBS-optimized, the minimum value is 10.
    """


_ListInstanceGroupsPaginateResponseInstanceGroupsEbsBlockDevicesTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsEbsBlockDevicesTypeDef",
    {
        "VolumeSpecification": ListInstanceGroupsPaginateResponseInstanceGroupsEbsBlockDevicesVolumeSpecificationTypeDef,
        "Device": str,
    },
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsEbsBlockDevicesTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsEbsBlockDevicesTypeDef
):
    """
    Type definition for `ListInstanceGroupsPaginateResponseInstanceGroups` `EbsBlockDevices`

    Configuration of requested EBS block device associated with the instance group.

    - **VolumeSpecification** *(dict) --*

      EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
      requested for the EBS volume attached to an EC2 instance in the cluster.

      - **VolumeType** *(string) --*

        The volume type. Volume types supported are gp2, io1, standard.

      - **Iops** *(integer) --*

        The number of I/O operations per second (IOPS) that the volume supports.

      - **SizeInGB** *(integer) --*

        The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
        volume type is EBS-optimized, the minimum value is 10.

    - **Device** *(string) --*

      The device name that is exposed to the instance, such as /dev/sdh.
    """


_ListInstanceGroupsPaginateResponseInstanceGroupsLastSuccessfullyAppliedConfigurationsTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsLastSuccessfullyAppliedConfigurationsTypeDef",
    {"Classification": str, "Configurations": List[Any], "Properties": Dict[str, str]},
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsLastSuccessfullyAppliedConfigurationsTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsLastSuccessfullyAppliedConfigurationsTypeDef
):
    """
    Type definition for `ListInstanceGroupsPaginateResponseInstanceGroups` `LastSuccessfullyAppliedConfigurations`

    .. note::

      Amazon EMR releases 4.x or later.

    An optional configuration specification to be used when provisioning cluster instances,
    which can include configurations for applications and software bundled with Amazon EMR.
    A configuration consists of a classification, properties, and optional nested
    configurations. A classification refers to an application-specific configuration file.
    Properties are the settings you want to change in that file. For more information, see
    `Configuring Applications
    <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

    - **Classification** *(string) --*

      The classification within a configuration.

    - **Configurations** *(list) --*

      A list of additional configurations to apply within a configuration object.

    - **Properties** *(dict) --*

      A set of properties specified within a configuration classification.

      - *(string) --*

        - *(string) --*
    """


_ListInstanceGroupsPaginateResponseInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef",
    {
        "InstancesToTerminate": List[str],
        "InstancesToProtect": List[str],
        "InstanceTerminationTimeout": int,
    },
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef
):
    """
    Type definition for `ListInstanceGroupsPaginateResponseInstanceGroupsShrinkPolicy` `InstanceResizePolicy`

    Custom policy for requesting termination protection or termination of specific
    instances when shrinking an instance group.

    - **InstancesToTerminate** *(list) --*

      Specific list of instances to be terminated when shrinking an instance group.

      - *(string) --*

    - **InstancesToProtect** *(list) --*

      Specific list of instances to be protected when shrinking an instance group.

      - *(string) --*

    - **InstanceTerminationTimeout** *(integer) --*

      Decommissioning timeout override for the specific list of instances to be terminated.
    """


_ListInstanceGroupsPaginateResponseInstanceGroupsShrinkPolicyTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsShrinkPolicyTypeDef",
    {
        "DecommissionTimeout": int,
        "InstanceResizePolicy": ListInstanceGroupsPaginateResponseInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef,
    },
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsShrinkPolicyTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsShrinkPolicyTypeDef
):
    """
    Type definition for `ListInstanceGroupsPaginateResponseInstanceGroups` `ShrinkPolicy`

    Policy for customizing shrink operations.

    - **DecommissionTimeout** *(integer) --*

      The desired timeout for decommissioning an instance. Overrides the default YARN
      decommissioning timeout.

    - **InstanceResizePolicy** *(dict) --*

      Custom policy for requesting termination protection or termination of specific
      instances when shrinking an instance group.

      - **InstancesToTerminate** *(list) --*

        Specific list of instances to be terminated when shrinking an instance group.

        - *(string) --*

      - **InstancesToProtect** *(list) --*

        Specific list of instances to be protected when shrinking an instance group.

        - *(string) --*

      - **InstanceTerminationTimeout** *(integer) --*

        Decommissioning timeout override for the specific list of instances to be terminated.
    """


_ListInstanceGroupsPaginateResponseInstanceGroupsStatusStateChangeReasonTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsStatusStateChangeReasonTypeDef",
    {"Code": str, "Message": str},
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsStatusStateChangeReasonTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsStatusStateChangeReasonTypeDef
):
    """
    Type definition for `ListInstanceGroupsPaginateResponseInstanceGroupsStatus` `StateChangeReason`

    The status change reason details for the instance group.

    - **Code** *(string) --*

      The programmable code for the state change reason.

    - **Message** *(string) --*

      The status change reason description.
    """


_ListInstanceGroupsPaginateResponseInstanceGroupsStatusTimelineTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsStatusTimelineTypeDef",
    {"CreationDateTime": datetime, "ReadyDateTime": datetime, "EndDateTime": datetime},
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsStatusTimelineTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsStatusTimelineTypeDef
):
    """
    Type definition for `ListInstanceGroupsPaginateResponseInstanceGroupsStatus` `Timeline`

    The timeline of the instance group status over time.

    - **CreationDateTime** *(datetime) --*

      The creation date and time of the instance group.

    - **ReadyDateTime** *(datetime) --*

      The date and time when the instance group became ready to perform tasks.

    - **EndDateTime** *(datetime) --*

      The date and time when the instance group terminated.
    """


_ListInstanceGroupsPaginateResponseInstanceGroupsStatusTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsStatusTypeDef",
    {
        "State": str,
        "StateChangeReason": ListInstanceGroupsPaginateResponseInstanceGroupsStatusStateChangeReasonTypeDef,
        "Timeline": ListInstanceGroupsPaginateResponseInstanceGroupsStatusTimelineTypeDef,
    },
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsStatusTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsStatusTypeDef
):
    """
    Type definition for `ListInstanceGroupsPaginateResponseInstanceGroups` `Status`

    The current status of the instance group.

    - **State** *(string) --*

      The current state of the instance group.

    - **StateChangeReason** *(dict) --*

      The status change reason details for the instance group.

      - **Code** *(string) --*

        The programmable code for the state change reason.

      - **Message** *(string) --*

        The status change reason description.

    - **Timeline** *(dict) --*

      The timeline of the instance group status over time.

      - **CreationDateTime** *(datetime) --*

        The creation date and time of the instance group.

      - **ReadyDateTime** *(datetime) --*

        The date and time when the instance group became ready to perform tasks.

      - **EndDateTime** *(datetime) --*

        The date and time when the instance group terminated.
    """


_ListInstanceGroupsPaginateResponseInstanceGroupsTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseInstanceGroupsTypeDef",
    {
        "Id": str,
        "Name": str,
        "Market": str,
        "InstanceGroupType": str,
        "BidPrice": str,
        "InstanceType": str,
        "RequestedInstanceCount": int,
        "RunningInstanceCount": int,
        "Status": ListInstanceGroupsPaginateResponseInstanceGroupsStatusTypeDef,
        "Configurations": List[
            ListInstanceGroupsPaginateResponseInstanceGroupsConfigurationsTypeDef
        ],
        "ConfigurationsVersion": int,
        "LastSuccessfullyAppliedConfigurations": List[
            ListInstanceGroupsPaginateResponseInstanceGroupsLastSuccessfullyAppliedConfigurationsTypeDef
        ],
        "LastSuccessfullyAppliedConfigurationsVersion": int,
        "EbsBlockDevices": List[
            ListInstanceGroupsPaginateResponseInstanceGroupsEbsBlockDevicesTypeDef
        ],
        "EbsOptimized": bool,
        "ShrinkPolicy": ListInstanceGroupsPaginateResponseInstanceGroupsShrinkPolicyTypeDef,
        "AutoScalingPolicy": ListInstanceGroupsPaginateResponseInstanceGroupsAutoScalingPolicyTypeDef,
    },
    total=False,
)


class ListInstanceGroupsPaginateResponseInstanceGroupsTypeDef(
    _ListInstanceGroupsPaginateResponseInstanceGroupsTypeDef
):
    """
    Type definition for `ListInstanceGroupsPaginateResponse` `InstanceGroups`

    This entity represents an instance group, which is a group of instances that have common
    purpose. For example, CORE instance group is used for HDFS.

    - **Id** *(string) --*

      The identifier of the instance group.

    - **Name** *(string) --*

      The name of the instance group.

    - **Market** *(string) --*

      The marketplace to provision instances for this group. Valid values are ON_DEMAND or SPOT.

    - **InstanceGroupType** *(string) --*

      The type of the instance group. Valid values are MASTER, CORE or TASK.

    - **BidPrice** *(string) --*

      The bid price for each EC2 Spot instance type as defined by ``InstanceType`` . Expressed
      in USD. If neither ``BidPrice`` nor ``BidPriceAsPercentageOfOnDemandPrice`` is provided,
      ``BidPriceAsPercentageOfOnDemandPrice`` defaults to 100%.

    - **InstanceType** *(string) --*

      The EC2 instance type for all instances in the instance group.

    - **RequestedInstanceCount** *(integer) --*

      The target number of instances for the instance group.

    - **RunningInstanceCount** *(integer) --*

      The number of instances currently running in this instance group.

    - **Status** *(dict) --*

      The current status of the instance group.

      - **State** *(string) --*

        The current state of the instance group.

      - **StateChangeReason** *(dict) --*

        The status change reason details for the instance group.

        - **Code** *(string) --*

          The programmable code for the state change reason.

        - **Message** *(string) --*

          The status change reason description.

      - **Timeline** *(dict) --*

        The timeline of the instance group status over time.

        - **CreationDateTime** *(datetime) --*

          The creation date and time of the instance group.

        - **ReadyDateTime** *(datetime) --*

          The date and time when the instance group became ready to perform tasks.

        - **EndDateTime** *(datetime) --*

          The date and time when the instance group terminated.

    - **Configurations** *(list) --*

      .. note::

        Amazon EMR releases 4.x or later.

      The list of configurations supplied for an EMR cluster instance group. You can specify a
      separate configuration for each instance group (master, core, and task).

      - *(dict) --*

        .. note::

          Amazon EMR releases 4.x or later.

        An optional configuration specification to be used when provisioning cluster instances,
        which can include configurations for applications and software bundled with Amazon EMR.
        A configuration consists of a classification, properties, and optional nested
        configurations. A classification refers to an application-specific configuration file.
        Properties are the settings you want to change in that file. For more information, see
        `Configuring Applications
        <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

        - **Classification** *(string) --*

          The classification within a configuration.

        - **Configurations** *(list) --*

          A list of additional configurations to apply within a configuration object.

        - **Properties** *(dict) --*

          A set of properties specified within a configuration classification.

          - *(string) --*

            - *(string) --*

    - **ConfigurationsVersion** *(integer) --*

      The version number of the requested configuration specification for this instance group.

    - **LastSuccessfullyAppliedConfigurations** *(list) --*

      A list of configurations that were successfully applied for an instance group last time.

      - *(dict) --*

        .. note::

          Amazon EMR releases 4.x or later.

        An optional configuration specification to be used when provisioning cluster instances,
        which can include configurations for applications and software bundled with Amazon EMR.
        A configuration consists of a classification, properties, and optional nested
        configurations. A classification refers to an application-specific configuration file.
        Properties are the settings you want to change in that file. For more information, see
        `Configuring Applications
        <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

        - **Classification** *(string) --*

          The classification within a configuration.

        - **Configurations** *(list) --*

          A list of additional configurations to apply within a configuration object.

        - **Properties** *(dict) --*

          A set of properties specified within a configuration classification.

          - *(string) --*

            - *(string) --*

    - **LastSuccessfullyAppliedConfigurationsVersion** *(integer) --*

      The version number of a configuration specification that was successfully applied for an
      instance group last time.

    - **EbsBlockDevices** *(list) --*

      The EBS block devices that are mapped to this instance group.

      - *(dict) --*

        Configuration of requested EBS block device associated with the instance group.

        - **VolumeSpecification** *(dict) --*

          EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
          requested for the EBS volume attached to an EC2 instance in the cluster.

          - **VolumeType** *(string) --*

            The volume type. Volume types supported are gp2, io1, standard.

          - **Iops** *(integer) --*

            The number of I/O operations per second (IOPS) that the volume supports.

          - **SizeInGB** *(integer) --*

            The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
            volume type is EBS-optimized, the minimum value is 10.

        - **Device** *(string) --*

          The device name that is exposed to the instance, such as /dev/sdh.

    - **EbsOptimized** *(boolean) --*

      If the instance group is EBS-optimized. An Amazon EBS-optimized instance uses an
      optimized configuration stack and provides additional, dedicated capacity for Amazon EBS
      I/O.

    - **ShrinkPolicy** *(dict) --*

      Policy for customizing shrink operations.

      - **DecommissionTimeout** *(integer) --*

        The desired timeout for decommissioning an instance. Overrides the default YARN
        decommissioning timeout.

      - **InstanceResizePolicy** *(dict) --*

        Custom policy for requesting termination protection or termination of specific
        instances when shrinking an instance group.

        - **InstancesToTerminate** *(list) --*

          Specific list of instances to be terminated when shrinking an instance group.

          - *(string) --*

        - **InstancesToProtect** *(list) --*

          Specific list of instances to be protected when shrinking an instance group.

          - *(string) --*

        - **InstanceTerminationTimeout** *(integer) --*

          Decommissioning timeout override for the specific list of instances to be terminated.

    - **AutoScalingPolicy** *(dict) --*

      An automatic scaling policy for a core instance group or task instance group in an Amazon
      EMR cluster. The automatic scaling policy defines how an instance group dynamically adds
      and terminates EC2 instances in response to the value of a CloudWatch metric. See
      PutAutoScalingPolicy.

      - **Status** *(dict) --*

        The status of an automatic scaling policy.

        - **State** *(string) --*

          Indicates the status of the automatic scaling policy.

        - **StateChangeReason** *(dict) --*

          The reason for a change in status.

          - **Code** *(string) --*

            The code indicating the reason for the change in status.``USER_REQUEST`` indicates
            that the scaling policy status was changed by a user. ``PROVISION_FAILURE``
            indicates that the status change was because the policy failed to provision.
            ``CLEANUP_FAILURE`` indicates an error.

          - **Message** *(string) --*

            A friendly, more verbose message that accompanies an automatic scaling policy state
            change.

      - **Constraints** *(dict) --*

        The upper and lower EC2 instance limits for an automatic scaling policy. Automatic
        scaling activity will not cause an instance group to grow above or below these limits.

        - **MinCapacity** *(integer) --*

          The lower boundary of EC2 instances in an instance group below which scaling
          activities are not allowed to shrink. Scale-in activities will not terminate
          instances below this boundary.

        - **MaxCapacity** *(integer) --*

          The upper boundary of EC2 instances in an instance group beyond which scaling
          activities are not allowed to grow. Scale-out activities will not add instances
          beyond this boundary.

      - **Rules** *(list) --*

        The scale-in and scale-out rules that comprise the automatic scaling policy.

        - *(dict) --*

          A scale-in or scale-out rule that defines scaling activity, including the CloudWatch
          metric alarm that triggers activity, how EC2 instances are added or removed, and the
          periodicity of adjustments. The automatic scaling policy for an instance group can
          comprise one or more automatic scaling rules.

          - **Name** *(string) --*

            The name used to identify an automatic scaling rule. Rule names must be unique
            within a scaling policy.

          - **Description** *(string) --*

            A friendly, more verbose description of the automatic scaling rule.

          - **Action** *(dict) --*

            The conditions that trigger an automatic scaling activity.

            - **Market** *(string) --*

              Not available for instance groups. Instance groups use the market type specified
              for the group.

            - **SimpleScalingPolicyConfiguration** *(dict) --*

              The type of adjustment the automatic scaling activity makes when triggered, and
              the periodicity of the adjustment.

              - **AdjustmentType** *(string) --*

                The way in which EC2 instances are added (if ``ScalingAdjustment`` is a
                positive number) or terminated (if ``ScalingAdjustment`` is a negative number)
                each time the scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the
                default. ``CHANGE_IN_CAPACITY`` indicates that the EC2 instance count
                increments or decrements by ``ScalingAdjustment`` , which should be expressed
                as an integer. ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count
                increments or decrements by the percentage specified by ``ScalingAdjustment`` ,
                which should be expressed as an integer. For example, 20 indicates an increase
                in 20% increments of cluster capacity. ``EXACT_CAPACITY`` indicates the scaling
                activity results in an instance group with the number of EC2 instances
                specified by ``ScalingAdjustment`` , which should be expressed as a positive
                integer.

              - **ScalingAdjustment** *(integer) --*

                The amount by which to scale in or scale out, based on the specified
                ``AdjustmentType`` . A positive value adds to the instance group's EC2 instance
                count while a negative number removes instances. If ``AdjustmentType`` is set
                to ``EXACT_CAPACITY`` , the number should only be a positive integer. If
                ``AdjustmentType`` is set to ``PERCENT_CHANGE_IN_CAPACITY`` , the value should
                express the percentage as an integer. For example, -20 indicates a decrease in
                20% increments of cluster capacity.

              - **CoolDown** *(integer) --*

                The amount of time, in seconds, after a scaling activity completes before any
                further trigger-related scaling activities can start. The default value is 0.

          - **Trigger** *(dict) --*

            The CloudWatch alarm definition that determines when automatic scaling activity is
            triggered.

            - **CloudWatchAlarmDefinition** *(dict) --*

              The definition of a CloudWatch metric alarm. When the defined alarm conditions
              are met along with other trigger parameters, scaling activity begins.

              - **ComparisonOperator** *(string) --*

                Determines how the metric specified by ``MetricName`` is compared to the value
                specified by ``Threshold`` .

              - **EvaluationPeriods** *(integer) --*

                The number of periods, in five-minute increments, during which the alarm
                condition must exist before the alarm triggers automatic scaling activity. The
                default value is ``1`` .

              - **MetricName** *(string) --*

                The name of the CloudWatch metric that is watched to determine an alarm
                condition.

              - **Namespace** *(string) --*

                The namespace for the CloudWatch metric. The default is
                ``AWS/ElasticMapReduce`` .

              - **Period** *(integer) --*

                The period, in seconds, over which the statistic is applied. EMR CloudWatch
                metrics are emitted every five minutes (300 seconds), so if an EMR CloudWatch
                metric is specified, specify ``300`` .

              - **Statistic** *(string) --*

                The statistic to apply to the metric associated with the alarm. The default is
                ``AVERAGE`` .

              - **Threshold** *(float) --*

                The value against which the specified statistic is compared.

              - **Unit** *(string) --*

                The unit of measure associated with the CloudWatch metric being watched. The
                value specified for ``Unit`` must correspond to the units specified in the
                CloudWatch metric.

              - **Dimensions** *(list) --*

                A CloudWatch metric dimension.

                - *(dict) --*

                  A CloudWatch dimension, which is specified using a ``Key`` (known as a
                  ``Name`` in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one
                  dimension whose ``Key`` is ``JobFlowID`` and ``Value`` is a variable
                  representing the cluster ID, which is ``${emr.clusterId}`` . This enables the
                  rule to bootstrap when the cluster ID becomes available.

                  - **Key** *(string) --*

                    The dimension name.

                  - **Value** *(string) --*

                    The dimension value.
    """


_ListInstanceGroupsPaginateResponseTypeDef = TypedDict(
    "_ListInstanceGroupsPaginateResponseTypeDef",
    {
        "InstanceGroups": List[ListInstanceGroupsPaginateResponseInstanceGroupsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListInstanceGroupsPaginateResponseTypeDef(
    _ListInstanceGroupsPaginateResponseTypeDef
):
    """
    Type definition for `ListInstanceGroupsPaginate` `Response`

    This input determines which instance groups to retrieve.

    - **InstanceGroups** *(list) --*

      The list of instance groups for the cluster and given filters.

      - *(dict) --*

        This entity represents an instance group, which is a group of instances that have common
        purpose. For example, CORE instance group is used for HDFS.

        - **Id** *(string) --*

          The identifier of the instance group.

        - **Name** *(string) --*

          The name of the instance group.

        - **Market** *(string) --*

          The marketplace to provision instances for this group. Valid values are ON_DEMAND or SPOT.

        - **InstanceGroupType** *(string) --*

          The type of the instance group. Valid values are MASTER, CORE or TASK.

        - **BidPrice** *(string) --*

          The bid price for each EC2 Spot instance type as defined by ``InstanceType`` . Expressed
          in USD. If neither ``BidPrice`` nor ``BidPriceAsPercentageOfOnDemandPrice`` is provided,
          ``BidPriceAsPercentageOfOnDemandPrice`` defaults to 100%.

        - **InstanceType** *(string) --*

          The EC2 instance type for all instances in the instance group.

        - **RequestedInstanceCount** *(integer) --*

          The target number of instances for the instance group.

        - **RunningInstanceCount** *(integer) --*

          The number of instances currently running in this instance group.

        - **Status** *(dict) --*

          The current status of the instance group.

          - **State** *(string) --*

            The current state of the instance group.

          - **StateChangeReason** *(dict) --*

            The status change reason details for the instance group.

            - **Code** *(string) --*

              The programmable code for the state change reason.

            - **Message** *(string) --*

              The status change reason description.

          - **Timeline** *(dict) --*

            The timeline of the instance group status over time.

            - **CreationDateTime** *(datetime) --*

              The creation date and time of the instance group.

            - **ReadyDateTime** *(datetime) --*

              The date and time when the instance group became ready to perform tasks.

            - **EndDateTime** *(datetime) --*

              The date and time when the instance group terminated.

        - **Configurations** *(list) --*

          .. note::

            Amazon EMR releases 4.x or later.

          The list of configurations supplied for an EMR cluster instance group. You can specify a
          separate configuration for each instance group (master, core, and task).

          - *(dict) --*

            .. note::

              Amazon EMR releases 4.x or later.

            An optional configuration specification to be used when provisioning cluster instances,
            which can include configurations for applications and software bundled with Amazon EMR.
            A configuration consists of a classification, properties, and optional nested
            configurations. A classification refers to an application-specific configuration file.
            Properties are the settings you want to change in that file. For more information, see
            `Configuring Applications
            <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

            - **Classification** *(string) --*

              The classification within a configuration.

            - **Configurations** *(list) --*

              A list of additional configurations to apply within a configuration object.

            - **Properties** *(dict) --*

              A set of properties specified within a configuration classification.

              - *(string) --*

                - *(string) --*

        - **ConfigurationsVersion** *(integer) --*

          The version number of the requested configuration specification for this instance group.

        - **LastSuccessfullyAppliedConfigurations** *(list) --*

          A list of configurations that were successfully applied for an instance group last time.

          - *(dict) --*

            .. note::

              Amazon EMR releases 4.x or later.

            An optional configuration specification to be used when provisioning cluster instances,
            which can include configurations for applications and software bundled with Amazon EMR.
            A configuration consists of a classification, properties, and optional nested
            configurations. A classification refers to an application-specific configuration file.
            Properties are the settings you want to change in that file. For more information, see
            `Configuring Applications
            <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .

            - **Classification** *(string) --*

              The classification within a configuration.

            - **Configurations** *(list) --*

              A list of additional configurations to apply within a configuration object.

            - **Properties** *(dict) --*

              A set of properties specified within a configuration classification.

              - *(string) --*

                - *(string) --*

        - **LastSuccessfullyAppliedConfigurationsVersion** *(integer) --*

          The version number of a configuration specification that was successfully applied for an
          instance group last time.

        - **EbsBlockDevices** *(list) --*

          The EBS block devices that are mapped to this instance group.

          - *(dict) --*

            Configuration of requested EBS block device associated with the instance group.

            - **VolumeSpecification** *(dict) --*

              EBS volume specifications such as volume type, IOPS, and size (GiB) that will be
              requested for the EBS volume attached to an EC2 instance in the cluster.

              - **VolumeType** *(string) --*

                The volume type. Volume types supported are gp2, io1, standard.

              - **Iops** *(integer) --*

                The number of I/O operations per second (IOPS) that the volume supports.

              - **SizeInGB** *(integer) --*

                The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the
                volume type is EBS-optimized, the minimum value is 10.

            - **Device** *(string) --*

              The device name that is exposed to the instance, such as /dev/sdh.

        - **EbsOptimized** *(boolean) --*

          If the instance group is EBS-optimized. An Amazon EBS-optimized instance uses an
          optimized configuration stack and provides additional, dedicated capacity for Amazon EBS
          I/O.

        - **ShrinkPolicy** *(dict) --*

          Policy for customizing shrink operations.

          - **DecommissionTimeout** *(integer) --*

            The desired timeout for decommissioning an instance. Overrides the default YARN
            decommissioning timeout.

          - **InstanceResizePolicy** *(dict) --*

            Custom policy for requesting termination protection or termination of specific
            instances when shrinking an instance group.

            - **InstancesToTerminate** *(list) --*

              Specific list of instances to be terminated when shrinking an instance group.

              - *(string) --*

            - **InstancesToProtect** *(list) --*

              Specific list of instances to be protected when shrinking an instance group.

              - *(string) --*

            - **InstanceTerminationTimeout** *(integer) --*

              Decommissioning timeout override for the specific list of instances to be terminated.

        - **AutoScalingPolicy** *(dict) --*

          An automatic scaling policy for a core instance group or task instance group in an Amazon
          EMR cluster. The automatic scaling policy defines how an instance group dynamically adds
          and terminates EC2 instances in response to the value of a CloudWatch metric. See
          PutAutoScalingPolicy.

          - **Status** *(dict) --*

            The status of an automatic scaling policy.

            - **State** *(string) --*

              Indicates the status of the automatic scaling policy.

            - **StateChangeReason** *(dict) --*

              The reason for a change in status.

              - **Code** *(string) --*

                The code indicating the reason for the change in status.``USER_REQUEST`` indicates
                that the scaling policy status was changed by a user. ``PROVISION_FAILURE``
                indicates that the status change was because the policy failed to provision.
                ``CLEANUP_FAILURE`` indicates an error.

              - **Message** *(string) --*

                A friendly, more verbose message that accompanies an automatic scaling policy state
                change.

          - **Constraints** *(dict) --*

            The upper and lower EC2 instance limits for an automatic scaling policy. Automatic
            scaling activity will not cause an instance group to grow above or below these limits.

            - **MinCapacity** *(integer) --*

              The lower boundary of EC2 instances in an instance group below which scaling
              activities are not allowed to shrink. Scale-in activities will not terminate
              instances below this boundary.

            - **MaxCapacity** *(integer) --*

              The upper boundary of EC2 instances in an instance group beyond which scaling
              activities are not allowed to grow. Scale-out activities will not add instances
              beyond this boundary.

          - **Rules** *(list) --*

            The scale-in and scale-out rules that comprise the automatic scaling policy.

            - *(dict) --*

              A scale-in or scale-out rule that defines scaling activity, including the CloudWatch
              metric alarm that triggers activity, how EC2 instances are added or removed, and the
              periodicity of adjustments. The automatic scaling policy for an instance group can
              comprise one or more automatic scaling rules.

              - **Name** *(string) --*

                The name used to identify an automatic scaling rule. Rule names must be unique
                within a scaling policy.

              - **Description** *(string) --*

                A friendly, more verbose description of the automatic scaling rule.

              - **Action** *(dict) --*

                The conditions that trigger an automatic scaling activity.

                - **Market** *(string) --*

                  Not available for instance groups. Instance groups use the market type specified
                  for the group.

                - **SimpleScalingPolicyConfiguration** *(dict) --*

                  The type of adjustment the automatic scaling activity makes when triggered, and
                  the periodicity of the adjustment.

                  - **AdjustmentType** *(string) --*

                    The way in which EC2 instances are added (if ``ScalingAdjustment`` is a
                    positive number) or terminated (if ``ScalingAdjustment`` is a negative number)
                    each time the scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the
                    default. ``CHANGE_IN_CAPACITY`` indicates that the EC2 instance count
                    increments or decrements by ``ScalingAdjustment`` , which should be expressed
                    as an integer. ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count
                    increments or decrements by the percentage specified by ``ScalingAdjustment`` ,
                    which should be expressed as an integer. For example, 20 indicates an increase
                    in 20% increments of cluster capacity. ``EXACT_CAPACITY`` indicates the scaling
                    activity results in an instance group with the number of EC2 instances
                    specified by ``ScalingAdjustment`` , which should be expressed as a positive
                    integer.

                  - **ScalingAdjustment** *(integer) --*

                    The amount by which to scale in or scale out, based on the specified
                    ``AdjustmentType`` . A positive value adds to the instance group's EC2 instance
                    count while a negative number removes instances. If ``AdjustmentType`` is set
                    to ``EXACT_CAPACITY`` , the number should only be a positive integer. If
                    ``AdjustmentType`` is set to ``PERCENT_CHANGE_IN_CAPACITY`` , the value should
                    express the percentage as an integer. For example, -20 indicates a decrease in
                    20% increments of cluster capacity.

                  - **CoolDown** *(integer) --*

                    The amount of time, in seconds, after a scaling activity completes before any
                    further trigger-related scaling activities can start. The default value is 0.

              - **Trigger** *(dict) --*

                The CloudWatch alarm definition that determines when automatic scaling activity is
                triggered.

                - **CloudWatchAlarmDefinition** *(dict) --*

                  The definition of a CloudWatch metric alarm. When the defined alarm conditions
                  are met along with other trigger parameters, scaling activity begins.

                  - **ComparisonOperator** *(string) --*

                    Determines how the metric specified by ``MetricName`` is compared to the value
                    specified by ``Threshold`` .

                  - **EvaluationPeriods** *(integer) --*

                    The number of periods, in five-minute increments, during which the alarm
                    condition must exist before the alarm triggers automatic scaling activity. The
                    default value is ``1`` .

                  - **MetricName** *(string) --*

                    The name of the CloudWatch metric that is watched to determine an alarm
                    condition.

                  - **Namespace** *(string) --*

                    The namespace for the CloudWatch metric. The default is
                    ``AWS/ElasticMapReduce`` .

                  - **Period** *(integer) --*

                    The period, in seconds, over which the statistic is applied. EMR CloudWatch
                    metrics are emitted every five minutes (300 seconds), so if an EMR CloudWatch
                    metric is specified, specify ``300`` .

                  - **Statistic** *(string) --*

                    The statistic to apply to the metric associated with the alarm. The default is
                    ``AVERAGE`` .

                  - **Threshold** *(float) --*

                    The value against which the specified statistic is compared.

                  - **Unit** *(string) --*

                    The unit of measure associated with the CloudWatch metric being watched. The
                    value specified for ``Unit`` must correspond to the units specified in the
                    CloudWatch metric.

                  - **Dimensions** *(list) --*

                    A CloudWatch metric dimension.

                    - *(dict) --*

                      A CloudWatch dimension, which is specified using a ``Key`` (known as a
                      ``Name`` in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one
                      dimension whose ``Key`` is ``JobFlowID`` and ``Value`` is a variable
                      representing the cluster ID, which is ``${emr.clusterId}`` . This enables the
                      rule to bootstrap when the cluster ID becomes available.

                      - **Key** *(string) --*

                        The dimension name.

                      - **Value** *(string) --*

                        The dimension value.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListInstancesPaginatePaginationConfigTypeDef(
    _ListInstancesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListInstancesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListInstancesPaginateResponseInstancesEbsVolumesTypeDef = TypedDict(
    "_ListInstancesPaginateResponseInstancesEbsVolumesTypeDef",
    {"Device": str, "VolumeId": str},
    total=False,
)


class ListInstancesPaginateResponseInstancesEbsVolumesTypeDef(
    _ListInstancesPaginateResponseInstancesEbsVolumesTypeDef
):
    """
    Type definition for `ListInstancesPaginateResponseInstances` `EbsVolumes`

    EBS block device that's attached to an EC2 instance.

    - **Device** *(string) --*

      The device name that is exposed to the instance, such as /dev/sdh.

    - **VolumeId** *(string) --*

      The volume identifier of the EBS volume.
    """


_ListInstancesPaginateResponseInstancesStatusStateChangeReasonTypeDef = TypedDict(
    "_ListInstancesPaginateResponseInstancesStatusStateChangeReasonTypeDef",
    {"Code": str, "Message": str},
    total=False,
)


class ListInstancesPaginateResponseInstancesStatusStateChangeReasonTypeDef(
    _ListInstancesPaginateResponseInstancesStatusStateChangeReasonTypeDef
):
    """
    Type definition for `ListInstancesPaginateResponseInstancesStatus` `StateChangeReason`

    The details of the status change reason for the instance.

    - **Code** *(string) --*

      The programmable code for the state change reason.

    - **Message** *(string) --*

      The status change reason description.
    """


_ListInstancesPaginateResponseInstancesStatusTimelineTypeDef = TypedDict(
    "_ListInstancesPaginateResponseInstancesStatusTimelineTypeDef",
    {"CreationDateTime": datetime, "ReadyDateTime": datetime, "EndDateTime": datetime},
    total=False,
)


class ListInstancesPaginateResponseInstancesStatusTimelineTypeDef(
    _ListInstancesPaginateResponseInstancesStatusTimelineTypeDef
):
    """
    Type definition for `ListInstancesPaginateResponseInstancesStatus` `Timeline`

    The timeline of the instance status over time.

    - **CreationDateTime** *(datetime) --*

      The creation date and time of the instance.

    - **ReadyDateTime** *(datetime) --*

      The date and time when the instance was ready to perform tasks.

    - **EndDateTime** *(datetime) --*

      The date and time when the instance was terminated.
    """


_ListInstancesPaginateResponseInstancesStatusTypeDef = TypedDict(
    "_ListInstancesPaginateResponseInstancesStatusTypeDef",
    {
        "State": str,
        "StateChangeReason": ListInstancesPaginateResponseInstancesStatusStateChangeReasonTypeDef,
        "Timeline": ListInstancesPaginateResponseInstancesStatusTimelineTypeDef,
    },
    total=False,
)


class ListInstancesPaginateResponseInstancesStatusTypeDef(
    _ListInstancesPaginateResponseInstancesStatusTypeDef
):
    """
    Type definition for `ListInstancesPaginateResponseInstances` `Status`

    The current status of the instance.

    - **State** *(string) --*

      The current state of the instance.

    - **StateChangeReason** *(dict) --*

      The details of the status change reason for the instance.

      - **Code** *(string) --*

        The programmable code for the state change reason.

      - **Message** *(string) --*

        The status change reason description.

    - **Timeline** *(dict) --*

      The timeline of the instance status over time.

      - **CreationDateTime** *(datetime) --*

        The creation date and time of the instance.

      - **ReadyDateTime** *(datetime) --*

        The date and time when the instance was ready to perform tasks.

      - **EndDateTime** *(datetime) --*

        The date and time when the instance was terminated.
    """


_ListInstancesPaginateResponseInstancesTypeDef = TypedDict(
    "_ListInstancesPaginateResponseInstancesTypeDef",
    {
        "Id": str,
        "Ec2InstanceId": str,
        "PublicDnsName": str,
        "PublicIpAddress": str,
        "PrivateDnsName": str,
        "PrivateIpAddress": str,
        "Status": ListInstancesPaginateResponseInstancesStatusTypeDef,
        "InstanceGroupId": str,
        "InstanceFleetId": str,
        "Market": str,
        "InstanceType": str,
        "EbsVolumes": List[ListInstancesPaginateResponseInstancesEbsVolumesTypeDef],
    },
    total=False,
)


class ListInstancesPaginateResponseInstancesTypeDef(
    _ListInstancesPaginateResponseInstancesTypeDef
):
    """
    Type definition for `ListInstancesPaginateResponse` `Instances`

    Represents an EC2 instance provisioned as part of cluster.

    - **Id** *(string) --*

      The unique identifier for the instance in Amazon EMR.

    - **Ec2InstanceId** *(string) --*

      The unique identifier of the instance in Amazon EC2.

    - **PublicDnsName** *(string) --*

      The public DNS name of the instance.

    - **PublicIpAddress** *(string) --*

      The public IP address of the instance.

    - **PrivateDnsName** *(string) --*

      The private DNS name of the instance.

    - **PrivateIpAddress** *(string) --*

      The private IP address of the instance.

    - **Status** *(dict) --*

      The current status of the instance.

      - **State** *(string) --*

        The current state of the instance.

      - **StateChangeReason** *(dict) --*

        The details of the status change reason for the instance.

        - **Code** *(string) --*

          The programmable code for the state change reason.

        - **Message** *(string) --*

          The status change reason description.

      - **Timeline** *(dict) --*

        The timeline of the instance status over time.

        - **CreationDateTime** *(datetime) --*

          The creation date and time of the instance.

        - **ReadyDateTime** *(datetime) --*

          The date and time when the instance was ready to perform tasks.

        - **EndDateTime** *(datetime) --*

          The date and time when the instance was terminated.

    - **InstanceGroupId** *(string) --*

      The identifier of the instance group to which this instance belongs.

    - **InstanceFleetId** *(string) --*

      The unique identifier of the instance fleet to which an EC2 instance belongs.

    - **Market** *(string) --*

      The instance purchasing option. Valid values are ``ON_DEMAND`` or ``SPOT`` .

    - **InstanceType** *(string) --*

      The EC2 instance type, for example ``m3.xlarge`` .

    - **EbsVolumes** *(list) --*

      The list of EBS volumes that are attached to this instance.

      - *(dict) --*

        EBS block device that's attached to an EC2 instance.

        - **Device** *(string) --*

          The device name that is exposed to the instance, such as /dev/sdh.

        - **VolumeId** *(string) --*

          The volume identifier of the EBS volume.
    """


_ListInstancesPaginateResponseTypeDef = TypedDict(
    "_ListInstancesPaginateResponseTypeDef",
    {
        "Instances": List[ListInstancesPaginateResponseInstancesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListInstancesPaginateResponseTypeDef(_ListInstancesPaginateResponseTypeDef):
    """
    Type definition for `ListInstancesPaginate` `Response`

    This output contains the list of instances.

    - **Instances** *(list) --*

      The list of instances for the cluster and given filters.

      - *(dict) --*

        Represents an EC2 instance provisioned as part of cluster.

        - **Id** *(string) --*

          The unique identifier for the instance in Amazon EMR.

        - **Ec2InstanceId** *(string) --*

          The unique identifier of the instance in Amazon EC2.

        - **PublicDnsName** *(string) --*

          The public DNS name of the instance.

        - **PublicIpAddress** *(string) --*

          The public IP address of the instance.

        - **PrivateDnsName** *(string) --*

          The private DNS name of the instance.

        - **PrivateIpAddress** *(string) --*

          The private IP address of the instance.

        - **Status** *(dict) --*

          The current status of the instance.

          - **State** *(string) --*

            The current state of the instance.

          - **StateChangeReason** *(dict) --*

            The details of the status change reason for the instance.

            - **Code** *(string) --*

              The programmable code for the state change reason.

            - **Message** *(string) --*

              The status change reason description.

          - **Timeline** *(dict) --*

            The timeline of the instance status over time.

            - **CreationDateTime** *(datetime) --*

              The creation date and time of the instance.

            - **ReadyDateTime** *(datetime) --*

              The date and time when the instance was ready to perform tasks.

            - **EndDateTime** *(datetime) --*

              The date and time when the instance was terminated.

        - **InstanceGroupId** *(string) --*

          The identifier of the instance group to which this instance belongs.

        - **InstanceFleetId** *(string) --*

          The unique identifier of the instance fleet to which an EC2 instance belongs.

        - **Market** *(string) --*

          The instance purchasing option. Valid values are ``ON_DEMAND`` or ``SPOT`` .

        - **InstanceType** *(string) --*

          The EC2 instance type, for example ``m3.xlarge`` .

        - **EbsVolumes** *(list) --*

          The list of EBS volumes that are attached to this instance.

          - *(dict) --*

            EBS block device that's attached to an EC2 instance.

            - **Device** *(string) --*

              The device name that is exposed to the instance, such as /dev/sdh.

            - **VolumeId** *(string) --*

              The volume identifier of the EBS volume.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListSecurityConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSecurityConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListSecurityConfigurationsPaginatePaginationConfigTypeDef(
    _ListSecurityConfigurationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListSecurityConfigurationsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListSecurityConfigurationsPaginateResponseSecurityConfigurationsTypeDef = TypedDict(
    "_ListSecurityConfigurationsPaginateResponseSecurityConfigurationsTypeDef",
    {"Name": str, "CreationDateTime": datetime},
    total=False,
)


class ListSecurityConfigurationsPaginateResponseSecurityConfigurationsTypeDef(
    _ListSecurityConfigurationsPaginateResponseSecurityConfigurationsTypeDef
):
    """
    Type definition for `ListSecurityConfigurationsPaginateResponse` `SecurityConfigurations`

    The creation date and time, and name, of a security configuration.

    - **Name** *(string) --*

      The name of the security configuration.

    - **CreationDateTime** *(datetime) --*

      The date and time the security configuration was created.
    """


_ListSecurityConfigurationsPaginateResponseTypeDef = TypedDict(
    "_ListSecurityConfigurationsPaginateResponseTypeDef",
    {
        "SecurityConfigurations": List[
            ListSecurityConfigurationsPaginateResponseSecurityConfigurationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListSecurityConfigurationsPaginateResponseTypeDef(
    _ListSecurityConfigurationsPaginateResponseTypeDef
):
    """
    Type definition for `ListSecurityConfigurationsPaginate` `Response`

    - **SecurityConfigurations** *(list) --*

      The creation date and time, and name, of each security configuration.

      - *(dict) --*

        The creation date and time, and name, of a security configuration.

        - **Name** *(string) --*

          The name of the security configuration.

        - **CreationDateTime** *(datetime) --*

          The date and time the security configuration was created.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListStepsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListStepsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListStepsPaginatePaginationConfigTypeDef(
    _ListStepsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListStepsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListStepsPaginateResponseStepsConfigTypeDef = TypedDict(
    "_ListStepsPaginateResponseStepsConfigTypeDef",
    {"Jar": str, "Properties": Dict[str, str], "MainClass": str, "Args": List[str]},
    total=False,
)


class ListStepsPaginateResponseStepsConfigTypeDef(
    _ListStepsPaginateResponseStepsConfigTypeDef
):
    """
    Type definition for `ListStepsPaginateResponseSteps` `Config`

    The Hadoop job configuration of the cluster step.

    - **Jar** *(string) --*

      The path to the JAR file that runs during the step.

    - **Properties** *(dict) --*

      The list of Java properties that are set when the step runs. You can use these
      properties to pass key value pairs to your main function.

      - *(string) --*

        - *(string) --*

    - **MainClass** *(string) --*

      The name of the main class in the specified Java file. If not specified, the JAR file
      should specify a main class in its manifest file.

    - **Args** *(list) --*

      The list of command line arguments to pass to the JAR file's main function for
      execution.

      - *(string) --*
    """


_ListStepsPaginateResponseStepsStatusFailureDetailsTypeDef = TypedDict(
    "_ListStepsPaginateResponseStepsStatusFailureDetailsTypeDef",
    {"Reason": str, "Message": str, "LogFile": str},
    total=False,
)


class ListStepsPaginateResponseStepsStatusFailureDetailsTypeDef(
    _ListStepsPaginateResponseStepsStatusFailureDetailsTypeDef
):
    """
    Type definition for `ListStepsPaginateResponseStepsStatus` `FailureDetails`

    The details for the step failure including reason, message, and log file path where the
    root cause was identified.

    - **Reason** *(string) --*

      The reason for the step failure. In the case where the service cannot successfully
      determine the root cause of the failure, it returns "Unknown Error" as a reason.

    - **Message** *(string) --*

      The descriptive message including the error the EMR service has identified as the
      cause of step failure. This is text from an error log that describes the root cause
      of the failure.

    - **LogFile** *(string) --*

      The path to the log file where the step failure root cause was originally recorded.
    """


_ListStepsPaginateResponseStepsStatusStateChangeReasonTypeDef = TypedDict(
    "_ListStepsPaginateResponseStepsStatusStateChangeReasonTypeDef",
    {"Code": str, "Message": str},
    total=False,
)


class ListStepsPaginateResponseStepsStatusStateChangeReasonTypeDef(
    _ListStepsPaginateResponseStepsStatusStateChangeReasonTypeDef
):
    """
    Type definition for `ListStepsPaginateResponseStepsStatus` `StateChangeReason`

    The reason for the step execution status change.

    - **Code** *(string) --*

      The programmable code for the state change reason. Note: Currently, the service
      provides no code for the state change.

    - **Message** *(string) --*

      The descriptive message for the state change reason.
    """


_ListStepsPaginateResponseStepsStatusTimelineTypeDef = TypedDict(
    "_ListStepsPaginateResponseStepsStatusTimelineTypeDef",
    {"CreationDateTime": datetime, "StartDateTime": datetime, "EndDateTime": datetime},
    total=False,
)


class ListStepsPaginateResponseStepsStatusTimelineTypeDef(
    _ListStepsPaginateResponseStepsStatusTimelineTypeDef
):
    """
    Type definition for `ListStepsPaginateResponseStepsStatus` `Timeline`

    The timeline of the cluster step status over time.

    - **CreationDateTime** *(datetime) --*

      The date and time when the cluster step was created.

    - **StartDateTime** *(datetime) --*

      The date and time when the cluster step execution started.

    - **EndDateTime** *(datetime) --*

      The date and time when the cluster step execution completed or failed.
    """


_ListStepsPaginateResponseStepsStatusTypeDef = TypedDict(
    "_ListStepsPaginateResponseStepsStatusTypeDef",
    {
        "State": str,
        "StateChangeReason": ListStepsPaginateResponseStepsStatusStateChangeReasonTypeDef,
        "FailureDetails": ListStepsPaginateResponseStepsStatusFailureDetailsTypeDef,
        "Timeline": ListStepsPaginateResponseStepsStatusTimelineTypeDef,
    },
    total=False,
)


class ListStepsPaginateResponseStepsStatusTypeDef(
    _ListStepsPaginateResponseStepsStatusTypeDef
):
    """
    Type definition for `ListStepsPaginateResponseSteps` `Status`

    The current execution status details of the cluster step.

    - **State** *(string) --*

      The execution state of the cluster step.

    - **StateChangeReason** *(dict) --*

      The reason for the step execution status change.

      - **Code** *(string) --*

        The programmable code for the state change reason. Note: Currently, the service
        provides no code for the state change.

      - **Message** *(string) --*

        The descriptive message for the state change reason.

    - **FailureDetails** *(dict) --*

      The details for the step failure including reason, message, and log file path where the
      root cause was identified.

      - **Reason** *(string) --*

        The reason for the step failure. In the case where the service cannot successfully
        determine the root cause of the failure, it returns "Unknown Error" as a reason.

      - **Message** *(string) --*

        The descriptive message including the error the EMR service has identified as the
        cause of step failure. This is text from an error log that describes the root cause
        of the failure.

      - **LogFile** *(string) --*

        The path to the log file where the step failure root cause was originally recorded.

    - **Timeline** *(dict) --*

      The timeline of the cluster step status over time.

      - **CreationDateTime** *(datetime) --*

        The date and time when the cluster step was created.

      - **StartDateTime** *(datetime) --*

        The date and time when the cluster step execution started.

      - **EndDateTime** *(datetime) --*

        The date and time when the cluster step execution completed or failed.
    """


_ListStepsPaginateResponseStepsTypeDef = TypedDict(
    "_ListStepsPaginateResponseStepsTypeDef",
    {
        "Id": str,
        "Name": str,
        "Config": ListStepsPaginateResponseStepsConfigTypeDef,
        "ActionOnFailure": str,
        "Status": ListStepsPaginateResponseStepsStatusTypeDef,
    },
    total=False,
)


class ListStepsPaginateResponseStepsTypeDef(_ListStepsPaginateResponseStepsTypeDef):
    """
    Type definition for `ListStepsPaginateResponse` `Steps`

    The summary of the cluster step.

    - **Id** *(string) --*

      The identifier of the cluster step.

    - **Name** *(string) --*

      The name of the cluster step.

    - **Config** *(dict) --*

      The Hadoop job configuration of the cluster step.

      - **Jar** *(string) --*

        The path to the JAR file that runs during the step.

      - **Properties** *(dict) --*

        The list of Java properties that are set when the step runs. You can use these
        properties to pass key value pairs to your main function.

        - *(string) --*

          - *(string) --*

      - **MainClass** *(string) --*

        The name of the main class in the specified Java file. If not specified, the JAR file
        should specify a main class in its manifest file.

      - **Args** *(list) --*

        The list of command line arguments to pass to the JAR file's main function for
        execution.

        - *(string) --*

    - **ActionOnFailure** *(string) --*

      The action to take when the cluster step fails. Possible values are TERMINATE_CLUSTER,
      CANCEL_AND_WAIT, and CONTINUE. TERMINATE_JOB_FLOW is available for backward
      compatibility. We recommend using TERMINATE_CLUSTER instead.

    - **Status** *(dict) --*

      The current execution status details of the cluster step.

      - **State** *(string) --*

        The execution state of the cluster step.

      - **StateChangeReason** *(dict) --*

        The reason for the step execution status change.

        - **Code** *(string) --*

          The programmable code for the state change reason. Note: Currently, the service
          provides no code for the state change.

        - **Message** *(string) --*

          The descriptive message for the state change reason.

      - **FailureDetails** *(dict) --*

        The details for the step failure including reason, message, and log file path where the
        root cause was identified.

        - **Reason** *(string) --*

          The reason for the step failure. In the case where the service cannot successfully
          determine the root cause of the failure, it returns "Unknown Error" as a reason.

        - **Message** *(string) --*

          The descriptive message including the error the EMR service has identified as the
          cause of step failure. This is text from an error log that describes the root cause
          of the failure.

        - **LogFile** *(string) --*

          The path to the log file where the step failure root cause was originally recorded.

      - **Timeline** *(dict) --*

        The timeline of the cluster step status over time.

        - **CreationDateTime** *(datetime) --*

          The date and time when the cluster step was created.

        - **StartDateTime** *(datetime) --*

          The date and time when the cluster step execution started.

        - **EndDateTime** *(datetime) --*

          The date and time when the cluster step execution completed or failed.
    """


_ListStepsPaginateResponseTypeDef = TypedDict(
    "_ListStepsPaginateResponseTypeDef",
    {"Steps": List[ListStepsPaginateResponseStepsTypeDef], "NextToken": str},
    total=False,
)


class ListStepsPaginateResponseTypeDef(_ListStepsPaginateResponseTypeDef):
    """
    Type definition for `ListStepsPaginate` `Response`

    This output contains the list of steps returned in reverse order. This means that the last step
    is the first element in the list.

    - **Steps** *(list) --*

      The filtered list of steps for the cluster.

      - *(dict) --*

        The summary of the cluster step.

        - **Id** *(string) --*

          The identifier of the cluster step.

        - **Name** *(string) --*

          The name of the cluster step.

        - **Config** *(dict) --*

          The Hadoop job configuration of the cluster step.

          - **Jar** *(string) --*

            The path to the JAR file that runs during the step.

          - **Properties** *(dict) --*

            The list of Java properties that are set when the step runs. You can use these
            properties to pass key value pairs to your main function.

            - *(string) --*

              - *(string) --*

          - **MainClass** *(string) --*

            The name of the main class in the specified Java file. If not specified, the JAR file
            should specify a main class in its manifest file.

          - **Args** *(list) --*

            The list of command line arguments to pass to the JAR file's main function for
            execution.

            - *(string) --*

        - **ActionOnFailure** *(string) --*

          The action to take when the cluster step fails. Possible values are TERMINATE_CLUSTER,
          CANCEL_AND_WAIT, and CONTINUE. TERMINATE_JOB_FLOW is available for backward
          compatibility. We recommend using TERMINATE_CLUSTER instead.

        - **Status** *(dict) --*

          The current execution status details of the cluster step.

          - **State** *(string) --*

            The execution state of the cluster step.

          - **StateChangeReason** *(dict) --*

            The reason for the step execution status change.

            - **Code** *(string) --*

              The programmable code for the state change reason. Note: Currently, the service
              provides no code for the state change.

            - **Message** *(string) --*

              The descriptive message for the state change reason.

          - **FailureDetails** *(dict) --*

            The details for the step failure including reason, message, and log file path where the
            root cause was identified.

            - **Reason** *(string) --*

              The reason for the step failure. In the case where the service cannot successfully
              determine the root cause of the failure, it returns "Unknown Error" as a reason.

            - **Message** *(string) --*

              The descriptive message including the error the EMR service has identified as the
              cause of step failure. This is text from an error log that describes the root cause
              of the failure.

            - **LogFile** *(string) --*

              The path to the log file where the step failure root cause was originally recorded.

          - **Timeline** *(dict) --*

            The timeline of the cluster step status over time.

            - **CreationDateTime** *(datetime) --*

              The date and time when the cluster step was created.

            - **StartDateTime** *(datetime) --*

              The date and time when the cluster step execution started.

            - **EndDateTime** *(datetime) --*

              The date and time when the cluster step execution completed or failed.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_StepCompleteWaitWaiterConfigTypeDef = TypedDict(
    "_StepCompleteWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class StepCompleteWaitWaiterConfigTypeDef(_StepCompleteWaitWaiterConfigTypeDef):
    """
    Type definition for `StepCompleteWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 60
    """
