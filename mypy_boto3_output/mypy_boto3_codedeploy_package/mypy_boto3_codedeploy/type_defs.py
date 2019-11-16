"Main interface for codedeploy type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientAddTagsToOnPremisesInstancestagsTypeDef",
    "ClientBatchGetApplicationRevisionsResponserevisionsgenericRevisionInfoTypeDef",
    "ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationappSpecContentTypeDef",
    "ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationgitHubLocationTypeDef",
    "ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocations3LocationTypeDef",
    "ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationstringTypeDef",
    "ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationTypeDef",
    "ClientBatchGetApplicationRevisionsResponserevisionsTypeDef",
    "ClientBatchGetApplicationRevisionsResponseTypeDef",
    "ClientBatchGetApplicationRevisionsrevisionsappSpecContentTypeDef",
    "ClientBatchGetApplicationRevisionsrevisionsgitHubLocationTypeDef",
    "ClientBatchGetApplicationRevisionsrevisionss3LocationTypeDef",
    "ClientBatchGetApplicationRevisionsrevisionsstringTypeDef",
    "ClientBatchGetApplicationRevisionsrevisionsTypeDef",
    "ClientBatchGetApplicationsResponseapplicationsInfoTypeDef",
    "ClientBatchGetApplicationsResponseTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoalarmConfigurationalarmsTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoalarmConfigurationTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoautoRollbackConfigurationTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoautoScalingGroupsTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfodeploymentStyleTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagFiltersTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagSetec2TagSetListTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagSetTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoecsServicesTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfolastAttemptedDeploymentTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfolastSuccessfulDeploymentTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfoelbInfoListTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupInfoListTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfoTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesInstanceTagFiltersTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesTagSetonPremisesTagSetListTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesTagSetTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionappSpecContentTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisiongitHubLocationTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisions3LocationTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionstringTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotriggerConfigurationsTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoTypeDef",
    "ClientBatchGetDeploymentGroupsResponseTypeDef",
    "ClientBatchGetDeploymentInstancesResponseinstancesSummarylifecycleEventsdiagnosticsTypeDef",
    "ClientBatchGetDeploymentInstancesResponseinstancesSummarylifecycleEventsTypeDef",
    "ClientBatchGetDeploymentInstancesResponseinstancesSummaryTypeDef",
    "ClientBatchGetDeploymentInstancesResponseTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetlifecycleEventsdiagnosticsTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetlifecycleEventsTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargettaskSetsInfotargetGroupTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargettaskSetsInfoTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetlifecycleEventsdiagnosticsTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetlifecycleEventsTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlambdaFunctionInfoTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlifecycleEventsdiagnosticsTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlifecycleEventsTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsTypeDef",
    "ClientBatchGetDeploymentTargetsResponseTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoautoRollbackConfigurationTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfodeploymentOverviewTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfodeploymentStyleTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoerrorInformationTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfoelbInfoListTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupInfoListTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfoTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionappSpecContentTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisiongitHubLocationTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisions3LocationTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionstringTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInforevisionappSpecContentTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInforevisiongitHubLocationTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInforevisions3LocationTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInforevisionstringTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInforevisionTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInforollbackInfoTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesec2TagSetec2TagSetListTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesec2TagSetTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancestagFiltersTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoTypeDef",
    "ClientBatchGetDeploymentsResponseTypeDef",
    "ClientBatchGetOnPremisesInstancesResponseinstanceInfostagsTypeDef",
    "ClientBatchGetOnPremisesInstancesResponseinstanceInfosTypeDef",
    "ClientBatchGetOnPremisesInstancesResponseTypeDef",
    "ClientCreateApplicationResponseTypeDef",
    "ClientCreateApplicationtagsTypeDef",
    "ClientCreateDeploymentConfigResponseTypeDef",
    "ClientCreateDeploymentConfigminimumHealthyHostsTypeDef",
    "ClientCreateDeploymentConfigtrafficRoutingConfigtimeBasedCanaryTypeDef",
    "ClientCreateDeploymentConfigtrafficRoutingConfigtimeBasedLinearTypeDef",
    "ClientCreateDeploymentConfigtrafficRoutingConfigTypeDef",
    "ClientCreateDeploymentGroupResponseTypeDef",
    "ClientCreateDeploymentGroupalarmConfigurationalarmsTypeDef",
    "ClientCreateDeploymentGroupalarmConfigurationTypeDef",
    "ClientCreateDeploymentGroupautoRollbackConfigurationTypeDef",
    "ClientCreateDeploymentGroupblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    "ClientCreateDeploymentGroupblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    "ClientCreateDeploymentGroupblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    "ClientCreateDeploymentGroupblueGreenDeploymentConfigurationTypeDef",
    "ClientCreateDeploymentGroupdeploymentStyleTypeDef",
    "ClientCreateDeploymentGroupec2TagFiltersTypeDef",
    "ClientCreateDeploymentGroupec2TagSetec2TagSetListTypeDef",
    "ClientCreateDeploymentGroupec2TagSetTypeDef",
    "ClientCreateDeploymentGroupecsServicesTypeDef",
    "ClientCreateDeploymentGrouploadBalancerInfoelbInfoListTypeDef",
    "ClientCreateDeploymentGrouploadBalancerInfotargetGroupInfoListTypeDef",
    "ClientCreateDeploymentGrouploadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    "ClientCreateDeploymentGrouploadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    "ClientCreateDeploymentGrouploadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    "ClientCreateDeploymentGrouploadBalancerInfotargetGroupPairInfoListTypeDef",
    "ClientCreateDeploymentGrouploadBalancerInfoTypeDef",
    "ClientCreateDeploymentGrouponPremisesInstanceTagFiltersTypeDef",
    "ClientCreateDeploymentGrouponPremisesTagSetonPremisesTagSetListTypeDef",
    "ClientCreateDeploymentGrouponPremisesTagSetTypeDef",
    "ClientCreateDeploymentGrouptagsTypeDef",
    "ClientCreateDeploymentGrouptriggerConfigurationsTypeDef",
    "ClientCreateDeploymentResponseTypeDef",
    "ClientCreateDeploymentautoRollbackConfigurationTypeDef",
    "ClientCreateDeploymentrevisionappSpecContentTypeDef",
    "ClientCreateDeploymentrevisiongitHubLocationTypeDef",
    "ClientCreateDeploymentrevisions3LocationTypeDef",
    "ClientCreateDeploymentrevisionstringTypeDef",
    "ClientCreateDeploymentrevisionTypeDef",
    "ClientCreateDeploymenttargetInstancesec2TagSetec2TagSetListTypeDef",
    "ClientCreateDeploymenttargetInstancesec2TagSetTypeDef",
    "ClientCreateDeploymenttargetInstancestagFiltersTypeDef",
    "ClientCreateDeploymenttargetInstancesTypeDef",
    "ClientDeleteDeploymentGroupResponsehooksNotCleanedUpTypeDef",
    "ClientDeleteDeploymentGroupResponseTypeDef",
    "ClientDeleteGitHubAccountTokenResponseTypeDef",
    "ClientGetApplicationResponseapplicationTypeDef",
    "ClientGetApplicationResponseTypeDef",
    "ClientGetApplicationRevisionResponserevisionInfoTypeDef",
    "ClientGetApplicationRevisionResponserevisionappSpecContentTypeDef",
    "ClientGetApplicationRevisionResponserevisiongitHubLocationTypeDef",
    "ClientGetApplicationRevisionResponserevisions3LocationTypeDef",
    "ClientGetApplicationRevisionResponserevisionstringTypeDef",
    "ClientGetApplicationRevisionResponserevisionTypeDef",
    "ClientGetApplicationRevisionResponseTypeDef",
    "ClientGetApplicationRevisionrevisionappSpecContentTypeDef",
    "ClientGetApplicationRevisionrevisiongitHubLocationTypeDef",
    "ClientGetApplicationRevisionrevisions3LocationTypeDef",
    "ClientGetApplicationRevisionrevisionstringTypeDef",
    "ClientGetApplicationRevisionrevisionTypeDef",
    "ClientGetDeploymentConfigResponsedeploymentConfigInfominimumHealthyHostsTypeDef",
    "ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigtimeBasedCanaryTypeDef",
    "ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigtimeBasedLinearTypeDef",
    "ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigTypeDef",
    "ClientGetDeploymentConfigResponsedeploymentConfigInfoTypeDef",
    "ClientGetDeploymentConfigResponseTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoalarmConfigurationalarmsTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoalarmConfigurationTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoautoRollbackConfigurationTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoautoScalingGroupsTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfodeploymentStyleTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagFiltersTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagSetec2TagSetListTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagSetTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoecsServicesTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfolastAttemptedDeploymentTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfolastSuccessfulDeploymentTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfoelbInfoListTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupInfoListTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfoTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesInstanceTagFiltersTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesTagSetonPremisesTagSetListTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesTagSetTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionappSpecContentTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisiongitHubLocationTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisions3LocationTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionstringTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfotriggerConfigurationsTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoTypeDef",
    "ClientGetDeploymentGroupResponseTypeDef",
    "ClientGetDeploymentInstanceResponseinstanceSummarylifecycleEventsdiagnosticsTypeDef",
    "ClientGetDeploymentInstanceResponseinstanceSummarylifecycleEventsTypeDef",
    "ClientGetDeploymentInstanceResponseinstanceSummaryTypeDef",
    "ClientGetDeploymentInstanceResponseTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoautoRollbackConfigurationTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationTypeDef",
    "ClientGetDeploymentResponsedeploymentInfodeploymentOverviewTypeDef",
    "ClientGetDeploymentResponsedeploymentInfodeploymentStyleTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoerrorInformationTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoloadBalancerInfoelbInfoListTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupInfoListTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoloadBalancerInfoTypeDef",
    "ClientGetDeploymentResponsedeploymentInfopreviousRevisionappSpecContentTypeDef",
    "ClientGetDeploymentResponsedeploymentInfopreviousRevisiongitHubLocationTypeDef",
    "ClientGetDeploymentResponsedeploymentInfopreviousRevisions3LocationTypeDef",
    "ClientGetDeploymentResponsedeploymentInfopreviousRevisionstringTypeDef",
    "ClientGetDeploymentResponsedeploymentInfopreviousRevisionTypeDef",
    "ClientGetDeploymentResponsedeploymentInforevisionappSpecContentTypeDef",
    "ClientGetDeploymentResponsedeploymentInforevisiongitHubLocationTypeDef",
    "ClientGetDeploymentResponsedeploymentInforevisions3LocationTypeDef",
    "ClientGetDeploymentResponsedeploymentInforevisionstringTypeDef",
    "ClientGetDeploymentResponsedeploymentInforevisionTypeDef",
    "ClientGetDeploymentResponsedeploymentInforollbackInfoTypeDef",
    "ClientGetDeploymentResponsedeploymentInfotargetInstancesec2TagSetec2TagSetListTypeDef",
    "ClientGetDeploymentResponsedeploymentInfotargetInstancesec2TagSetTypeDef",
    "ClientGetDeploymentResponsedeploymentInfotargetInstancestagFiltersTypeDef",
    "ClientGetDeploymentResponsedeploymentInfotargetInstancesTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoTypeDef",
    "ClientGetDeploymentResponseTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetecsTargetlifecycleEventsdiagnosticsTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetecsTargetlifecycleEventsTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetecsTargettaskSetsInfotargetGroupTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetecsTargettaskSetsInfoTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetecsTargetTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetlifecycleEventsdiagnosticsTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetlifecycleEventsTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlambdaFunctionInfoTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlifecycleEventsdiagnosticsTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlifecycleEventsTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetTypeDef",
    "ClientGetDeploymentTargetResponseTypeDef",
    "ClientGetOnPremisesInstanceResponseinstanceInfotagsTypeDef",
    "ClientGetOnPremisesInstanceResponseinstanceInfoTypeDef",
    "ClientGetOnPremisesInstanceResponseTypeDef",
    "ClientListApplicationRevisionsResponserevisionsappSpecContentTypeDef",
    "ClientListApplicationRevisionsResponserevisionsgitHubLocationTypeDef",
    "ClientListApplicationRevisionsResponserevisionss3LocationTypeDef",
    "ClientListApplicationRevisionsResponserevisionsstringTypeDef",
    "ClientListApplicationRevisionsResponserevisionsTypeDef",
    "ClientListApplicationRevisionsResponseTypeDef",
    "ClientListApplicationsResponseTypeDef",
    "ClientListDeploymentConfigsResponseTypeDef",
    "ClientListDeploymentGroupsResponseTypeDef",
    "ClientListDeploymentInstancesResponseTypeDef",
    "ClientListDeploymentTargetsResponseTypeDef",
    "ClientListDeploymentsResponseTypeDef",
    "ClientListDeploymentscreateTimeRangeTypeDef",
    "ClientListGitHubAccountTokenNamesResponseTypeDef",
    "ClientListOnPremisesInstancesResponseTypeDef",
    "ClientListOnPremisesInstancestagFiltersTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutLifecycleEventHookExecutionStatusResponseTypeDef",
    "ClientRegisterApplicationRevisionrevisionappSpecContentTypeDef",
    "ClientRegisterApplicationRevisionrevisiongitHubLocationTypeDef",
    "ClientRegisterApplicationRevisionrevisions3LocationTypeDef",
    "ClientRegisterApplicationRevisionrevisionstringTypeDef",
    "ClientRegisterApplicationRevisionrevisionTypeDef",
    "ClientRemoveTagsFromOnPremisesInstancestagsTypeDef",
    "ClientStopDeploymentResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateDeploymentGroupResponsehooksNotCleanedUpTypeDef",
    "ClientUpdateDeploymentGroupResponseTypeDef",
    "ClientUpdateDeploymentGroupalarmConfigurationalarmsTypeDef",
    "ClientUpdateDeploymentGroupalarmConfigurationTypeDef",
    "ClientUpdateDeploymentGroupautoRollbackConfigurationTypeDef",
    "ClientUpdateDeploymentGroupblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    "ClientUpdateDeploymentGroupblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    "ClientUpdateDeploymentGroupblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    "ClientUpdateDeploymentGroupblueGreenDeploymentConfigurationTypeDef",
    "ClientUpdateDeploymentGroupdeploymentStyleTypeDef",
    "ClientUpdateDeploymentGroupec2TagFiltersTypeDef",
    "ClientUpdateDeploymentGroupec2TagSetec2TagSetListTypeDef",
    "ClientUpdateDeploymentGroupec2TagSetTypeDef",
    "ClientUpdateDeploymentGroupecsServicesTypeDef",
    "ClientUpdateDeploymentGrouploadBalancerInfoelbInfoListTypeDef",
    "ClientUpdateDeploymentGrouploadBalancerInfotargetGroupInfoListTypeDef",
    "ClientUpdateDeploymentGrouploadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    "ClientUpdateDeploymentGrouploadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    "ClientUpdateDeploymentGrouploadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    "ClientUpdateDeploymentGrouploadBalancerInfotargetGroupPairInfoListTypeDef",
    "ClientUpdateDeploymentGrouploadBalancerInfoTypeDef",
    "ClientUpdateDeploymentGrouponPremisesInstanceTagFiltersTypeDef",
    "ClientUpdateDeploymentGrouponPremisesTagSetonPremisesTagSetListTypeDef",
    "ClientUpdateDeploymentGrouponPremisesTagSetTypeDef",
    "ClientUpdateDeploymentGrouptriggerConfigurationsTypeDef",
    "DeploymentSuccessfulWaitWaiterConfigTypeDef",
    "ListApplicationRevisionsPaginatePaginationConfigTypeDef",
    "ListApplicationRevisionsPaginateResponserevisionsappSpecContentTypeDef",
    "ListApplicationRevisionsPaginateResponserevisionsgitHubLocationTypeDef",
    "ListApplicationRevisionsPaginateResponserevisionss3LocationTypeDef",
    "ListApplicationRevisionsPaginateResponserevisionsstringTypeDef",
    "ListApplicationRevisionsPaginateResponserevisionsTypeDef",
    "ListApplicationRevisionsPaginateResponseTypeDef",
    "ListApplicationsPaginatePaginationConfigTypeDef",
    "ListApplicationsPaginateResponseTypeDef",
    "ListDeploymentConfigsPaginatePaginationConfigTypeDef",
    "ListDeploymentConfigsPaginateResponseTypeDef",
    "ListDeploymentGroupsPaginatePaginationConfigTypeDef",
    "ListDeploymentGroupsPaginateResponseTypeDef",
    "ListDeploymentInstancesPaginatePaginationConfigTypeDef",
    "ListDeploymentInstancesPaginateResponseTypeDef",
    "ListDeploymentTargetsPaginatePaginationConfigTypeDef",
    "ListDeploymentTargetsPaginateResponseTypeDef",
    "ListDeploymentsPaginatePaginationConfigTypeDef",
    "ListDeploymentsPaginateResponseTypeDef",
    "ListDeploymentsPaginatecreateTimeRangeTypeDef",
    "ListGitHubAccountTokenNamesPaginatePaginationConfigTypeDef",
    "ListGitHubAccountTokenNamesPaginateResponseTypeDef",
    "ListOnPremisesInstancesPaginatePaginationConfigTypeDef",
    "ListOnPremisesInstancesPaginateResponseTypeDef",
    "ListOnPremisesInstancesPaginatetagFiltersTypeDef",
)


_ClientAddTagsToOnPremisesInstancestagsTypeDef = TypedDict(
    "_ClientAddTagsToOnPremisesInstancestagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientAddTagsToOnPremisesInstancestagsTypeDef(
    _ClientAddTagsToOnPremisesInstancestagsTypeDef
):
    """
    Type definition for `ClientAddTagsToOnPremisesInstances` `tags`

    Information about a tag.

    - **Key** *(string) --*

      The tag's key.

    - **Value** *(string) --*

      The tag's value.
    """


_ClientBatchGetApplicationRevisionsResponserevisionsgenericRevisionInfoTypeDef = TypedDict(
    "_ClientBatchGetApplicationRevisionsResponserevisionsgenericRevisionInfoTypeDef",
    {
        "description": str,
        "deploymentGroups": List[str],
        "firstUsedTime": datetime,
        "lastUsedTime": datetime,
        "registerTime": datetime,
    },
    total=False,
)


class ClientBatchGetApplicationRevisionsResponserevisionsgenericRevisionInfoTypeDef(
    _ClientBatchGetApplicationRevisionsResponserevisionsgenericRevisionInfoTypeDef
):
    """
    Type definition for `ClientBatchGetApplicationRevisionsResponserevisions` `genericRevisionInfo`

    Information about an application revision, including usage details and associated
    deployment groups.

    - **description** *(string) --*

      A comment about the revision.

    - **deploymentGroups** *(list) --*

      The deployment groups for which this is the current target revision.

      - *(string) --*

    - **firstUsedTime** *(datetime) --*

      When the revision was first used by AWS CodeDeploy.

    - **lastUsedTime** *(datetime) --*

      When the revision was last used by AWS CodeDeploy.

    - **registerTime** *(datetime) --*

      When the revision was registered with AWS CodeDeploy.
    """


_ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationappSpecContentTypeDef = TypedDict(
    "_ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationappSpecContentTypeDef(
    _ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationappSpecContentTypeDef
):
    """
    Type definition for `ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocation` `appSpecContent`

    The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content
    is formatted as JSON or YAML and stored as a RawString.

    - **content** *(string) --*

      The YAML-formatted or JSON-formatted revision string.

      For an AWS Lambda deployment, the content includes a Lambda function name, the alias
      for its original version, and the alias for its replacement version. The deployment
      shifts traffic from the original version of the Lambda function to the replacement
      version.

      For an Amazon ECS deployment, the content includes the task name, information about
      the load balancer that serves traffic to the container, and more.

      For both types of deployments, the content can specify Lambda functions that run at
      specified hooks, such as ``BeforeInstall`` , during a deployment.

    - **sha256** *(string) --*

      The SHA256 hash value of the revision content.
    """


_ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationgitHubLocationTypeDef = TypedDict(
    "_ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationgitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)


class ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationgitHubLocationTypeDef(
    _ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationgitHubLocationTypeDef
):
    """
    Type definition for `ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocation` `gitHubLocation`

    Information about the location of application artifacts stored in GitHub.

    - **repository** *(string) --*

      The GitHub account and repository pair that stores a reference to the commit that
      represents the bundled artifacts for the application revision.

      Specified as account/repository.

    - **commitId** *(string) --*

      The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
      application revision.
    """


_ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocations3LocationTypeDef = TypedDict(
    "_ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocations3LocationTypeDef",
    {"bucket": str, "key": str, "bundleType": str, "version": str, "eTag": str},
    total=False,
)


class ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocations3LocationTypeDef(
    _ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocations3LocationTypeDef
):
    """
    Type definition for `ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocation` `s3Location`

    Information about the location of a revision stored in Amazon S3.

    - **bucket** *(string) --*

      The name of the Amazon S3 bucket where the application revision is stored.

    - **key** *(string) --*

      The name of the Amazon S3 object that represents the bundled artifacts for the
      application revision.

    - **bundleType** *(string) --*

      The file type of the application revision. Must be one of the following:

      * tar: A tar archive file.

      * tgz: A compressed tar archive file.

      * zip: A zip archive file.

    - **version** *(string) --*

      A specific version of the Amazon S3 object that represents the bundled artifacts for
      the application revision.

      If the version is not specified, the system uses the most recent version by default.

    - **eTag** *(string) --*

      The ETag of the Amazon S3 object that represents the bundled artifacts for the
      application revision.

      If the ETag is not specified as an input parameter, ETag validation of the object is
      skipped.
    """


_ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationstringTypeDef = TypedDict(
    "_ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationstringTypeDef(
    _ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationstringTypeDef
):
    """
    Type definition for `ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocation` `string`

    Information about the location of an AWS Lambda deployment revision stored as a
    RawString.

    - **content** *(string) --*

      The YAML-formatted or JSON-formatted revision string. It includes information about
      which Lambda function to update and optional Lambda functions that validate
      deployment lifecycle events.

    - **sha256** *(string) --*

      The SHA256 hash value of the revision content.
    """


_ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationTypeDef = TypedDict(
    "_ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationTypeDef",
    {
        "revisionType": str,
        "s3Location": ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocations3LocationTypeDef,
        "gitHubLocation": ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationgitHubLocationTypeDef,
        "string": ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationstringTypeDef,
        "appSpecContent": ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationappSpecContentTypeDef,
    },
    total=False,
)


class ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationTypeDef(
    _ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationTypeDef
):
    """
    Type definition for `ClientBatchGetApplicationRevisionsResponserevisions` `revisionLocation`

    Information about the location and type of an application revision.

    - **revisionType** *(string) --*

      The type of application revision:

      * S3: An application revision stored in Amazon S3.

      * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

      * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

    - **s3Location** *(dict) --*

      Information about the location of a revision stored in Amazon S3.

      - **bucket** *(string) --*

        The name of the Amazon S3 bucket where the application revision is stored.

      - **key** *(string) --*

        The name of the Amazon S3 object that represents the bundled artifacts for the
        application revision.

      - **bundleType** *(string) --*

        The file type of the application revision. Must be one of the following:

        * tar: A tar archive file.

        * tgz: A compressed tar archive file.

        * zip: A zip archive file.

      - **version** *(string) --*

        A specific version of the Amazon S3 object that represents the bundled artifacts for
        the application revision.

        If the version is not specified, the system uses the most recent version by default.

      - **eTag** *(string) --*

        The ETag of the Amazon S3 object that represents the bundled artifacts for the
        application revision.

        If the ETag is not specified as an input parameter, ETag validation of the object is
        skipped.

    - **gitHubLocation** *(dict) --*

      Information about the location of application artifacts stored in GitHub.

      - **repository** *(string) --*

        The GitHub account and repository pair that stores a reference to the commit that
        represents the bundled artifacts for the application revision.

        Specified as account/repository.

      - **commitId** *(string) --*

        The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
        application revision.

    - **string** *(dict) --*

      Information about the location of an AWS Lambda deployment revision stored as a
      RawString.

      - **content** *(string) --*

        The YAML-formatted or JSON-formatted revision string. It includes information about
        which Lambda function to update and optional Lambda functions that validate
        deployment lifecycle events.

      - **sha256** *(string) --*

        The SHA256 hash value of the revision content.

    - **appSpecContent** *(dict) --*

      The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content
      is formatted as JSON or YAML and stored as a RawString.

      - **content** *(string) --*

        The YAML-formatted or JSON-formatted revision string.

        For an AWS Lambda deployment, the content includes a Lambda function name, the alias
        for its original version, and the alias for its replacement version. The deployment
        shifts traffic from the original version of the Lambda function to the replacement
        version.

        For an Amazon ECS deployment, the content includes the task name, information about
        the load balancer that serves traffic to the container, and more.

        For both types of deployments, the content can specify Lambda functions that run at
        specified hooks, such as ``BeforeInstall`` , during a deployment.

      - **sha256** *(string) --*

        The SHA256 hash value of the revision content.
    """


_ClientBatchGetApplicationRevisionsResponserevisionsTypeDef = TypedDict(
    "_ClientBatchGetApplicationRevisionsResponserevisionsTypeDef",
    {
        "revisionLocation": ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationTypeDef,
        "genericRevisionInfo": ClientBatchGetApplicationRevisionsResponserevisionsgenericRevisionInfoTypeDef,
    },
    total=False,
)


class ClientBatchGetApplicationRevisionsResponserevisionsTypeDef(
    _ClientBatchGetApplicationRevisionsResponserevisionsTypeDef
):
    """
    Type definition for `ClientBatchGetApplicationRevisionsResponse` `revisions`

    Information about an application revision.

    - **revisionLocation** *(dict) --*

      Information about the location and type of an application revision.

      - **revisionType** *(string) --*

        The type of application revision:

        * S3: An application revision stored in Amazon S3.

        * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

        * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

      - **s3Location** *(dict) --*

        Information about the location of a revision stored in Amazon S3.

        - **bucket** *(string) --*

          The name of the Amazon S3 bucket where the application revision is stored.

        - **key** *(string) --*

          The name of the Amazon S3 object that represents the bundled artifacts for the
          application revision.

        - **bundleType** *(string) --*

          The file type of the application revision. Must be one of the following:

          * tar: A tar archive file.

          * tgz: A compressed tar archive file.

          * zip: A zip archive file.

        - **version** *(string) --*

          A specific version of the Amazon S3 object that represents the bundled artifacts for
          the application revision.

          If the version is not specified, the system uses the most recent version by default.

        - **eTag** *(string) --*

          The ETag of the Amazon S3 object that represents the bundled artifacts for the
          application revision.

          If the ETag is not specified as an input parameter, ETag validation of the object is
          skipped.

      - **gitHubLocation** *(dict) --*

        Information about the location of application artifacts stored in GitHub.

        - **repository** *(string) --*

          The GitHub account and repository pair that stores a reference to the commit that
          represents the bundled artifacts for the application revision.

          Specified as account/repository.

        - **commitId** *(string) --*

          The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
          application revision.

      - **string** *(dict) --*

        Information about the location of an AWS Lambda deployment revision stored as a
        RawString.

        - **content** *(string) --*

          The YAML-formatted or JSON-formatted revision string. It includes information about
          which Lambda function to update and optional Lambda functions that validate
          deployment lifecycle events.

        - **sha256** *(string) --*

          The SHA256 hash value of the revision content.

      - **appSpecContent** *(dict) --*

        The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content
        is formatted as JSON or YAML and stored as a RawString.

        - **content** *(string) --*

          The YAML-formatted or JSON-formatted revision string.

          For an AWS Lambda deployment, the content includes a Lambda function name, the alias
          for its original version, and the alias for its replacement version. The deployment
          shifts traffic from the original version of the Lambda function to the replacement
          version.

          For an Amazon ECS deployment, the content includes the task name, information about
          the load balancer that serves traffic to the container, and more.

          For both types of deployments, the content can specify Lambda functions that run at
          specified hooks, such as ``BeforeInstall`` , during a deployment.

        - **sha256** *(string) --*

          The SHA256 hash value of the revision content.

    - **genericRevisionInfo** *(dict) --*

      Information about an application revision, including usage details and associated
      deployment groups.

      - **description** *(string) --*

        A comment about the revision.

      - **deploymentGroups** *(list) --*

        The deployment groups for which this is the current target revision.

        - *(string) --*

      - **firstUsedTime** *(datetime) --*

        When the revision was first used by AWS CodeDeploy.

      - **lastUsedTime** *(datetime) --*

        When the revision was last used by AWS CodeDeploy.

      - **registerTime** *(datetime) --*

        When the revision was registered with AWS CodeDeploy.
    """


_ClientBatchGetApplicationRevisionsResponseTypeDef = TypedDict(
    "_ClientBatchGetApplicationRevisionsResponseTypeDef",
    {
        "applicationName": str,
        "errorMessage": str,
        "revisions": List[ClientBatchGetApplicationRevisionsResponserevisionsTypeDef],
    },
    total=False,
)


class ClientBatchGetApplicationRevisionsResponseTypeDef(
    _ClientBatchGetApplicationRevisionsResponseTypeDef
):
    """
    Type definition for `ClientBatchGetApplicationRevisions` `Response`

    Represents the output of a BatchGetApplicationRevisions operation.

    - **applicationName** *(string) --*

      The name of the application that corresponds to the revisions.

    - **errorMessage** *(string) --*

      Information about errors that might have occurred during the API call.

    - **revisions** *(list) --*

      Additional information about the revisions, including the type and location.

      - *(dict) --*

        Information about an application revision.

        - **revisionLocation** *(dict) --*

          Information about the location and type of an application revision.

          - **revisionType** *(string) --*

            The type of application revision:

            * S3: An application revision stored in Amazon S3.

            * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

            * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

          - **s3Location** *(dict) --*

            Information about the location of a revision stored in Amazon S3.

            - **bucket** *(string) --*

              The name of the Amazon S3 bucket where the application revision is stored.

            - **key** *(string) --*

              The name of the Amazon S3 object that represents the bundled artifacts for the
              application revision.

            - **bundleType** *(string) --*

              The file type of the application revision. Must be one of the following:

              * tar: A tar archive file.

              * tgz: A compressed tar archive file.

              * zip: A zip archive file.

            - **version** *(string) --*

              A specific version of the Amazon S3 object that represents the bundled artifacts for
              the application revision.

              If the version is not specified, the system uses the most recent version by default.

            - **eTag** *(string) --*

              The ETag of the Amazon S3 object that represents the bundled artifacts for the
              application revision.

              If the ETag is not specified as an input parameter, ETag validation of the object is
              skipped.

          - **gitHubLocation** *(dict) --*

            Information about the location of application artifacts stored in GitHub.

            - **repository** *(string) --*

              The GitHub account and repository pair that stores a reference to the commit that
              represents the bundled artifacts for the application revision.

              Specified as account/repository.

            - **commitId** *(string) --*

              The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
              application revision.

          - **string** *(dict) --*

            Information about the location of an AWS Lambda deployment revision stored as a
            RawString.

            - **content** *(string) --*

              The YAML-formatted or JSON-formatted revision string. It includes information about
              which Lambda function to update and optional Lambda functions that validate
              deployment lifecycle events.

            - **sha256** *(string) --*

              The SHA256 hash value of the revision content.

          - **appSpecContent** *(dict) --*

            The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content
            is formatted as JSON or YAML and stored as a RawString.

            - **content** *(string) --*

              The YAML-formatted or JSON-formatted revision string.

              For an AWS Lambda deployment, the content includes a Lambda function name, the alias
              for its original version, and the alias for its replacement version. The deployment
              shifts traffic from the original version of the Lambda function to the replacement
              version.

              For an Amazon ECS deployment, the content includes the task name, information about
              the load balancer that serves traffic to the container, and more.

              For both types of deployments, the content can specify Lambda functions that run at
              specified hooks, such as ``BeforeInstall`` , during a deployment.

            - **sha256** *(string) --*

              The SHA256 hash value of the revision content.

        - **genericRevisionInfo** *(dict) --*

          Information about an application revision, including usage details and associated
          deployment groups.

          - **description** *(string) --*

            A comment about the revision.

          - **deploymentGroups** *(list) --*

            The deployment groups for which this is the current target revision.

            - *(string) --*

          - **firstUsedTime** *(datetime) --*

            When the revision was first used by AWS CodeDeploy.

          - **lastUsedTime** *(datetime) --*

            When the revision was last used by AWS CodeDeploy.

          - **registerTime** *(datetime) --*

            When the revision was registered with AWS CodeDeploy.
    """


_ClientBatchGetApplicationRevisionsrevisionsappSpecContentTypeDef = TypedDict(
    "_ClientBatchGetApplicationRevisionsrevisionsappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientBatchGetApplicationRevisionsrevisionsappSpecContentTypeDef(
    _ClientBatchGetApplicationRevisionsrevisionsappSpecContentTypeDef
):
    """
    Type definition for `ClientBatchGetApplicationRevisionsrevisions` `appSpecContent`

    The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is
    formatted as JSON or YAML and stored as a RawString.

    - **content** *(string) --*

      The YAML-formatted or JSON-formatted revision string.

      For an AWS Lambda deployment, the content includes a Lambda function name, the alias for
      its original version, and the alias for its replacement version. The deployment shifts
      traffic from the original version of the Lambda function to the replacement version.

      For an Amazon ECS deployment, the content includes the task name, information about the
      load balancer that serves traffic to the container, and more.

      For both types of deployments, the content can specify Lambda functions that run at
      specified hooks, such as ``BeforeInstall`` , during a deployment.

    - **sha256** *(string) --*

      The SHA256 hash value of the revision content.
    """


_ClientBatchGetApplicationRevisionsrevisionsgitHubLocationTypeDef = TypedDict(
    "_ClientBatchGetApplicationRevisionsrevisionsgitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)


class ClientBatchGetApplicationRevisionsrevisionsgitHubLocationTypeDef(
    _ClientBatchGetApplicationRevisionsrevisionsgitHubLocationTypeDef
):
    """
    Type definition for `ClientBatchGetApplicationRevisionsrevisions` `gitHubLocation`

    Information about the location of application artifacts stored in GitHub.

    - **repository** *(string) --*

      The GitHub account and repository pair that stores a reference to the commit that
      represents the bundled artifacts for the application revision.

      Specified as account/repository.

    - **commitId** *(string) --*

      The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
      application revision.
    """


_ClientBatchGetApplicationRevisionsrevisionss3LocationTypeDef = TypedDict(
    "_ClientBatchGetApplicationRevisionsrevisionss3LocationTypeDef",
    {"bucket": str, "key": str, "bundleType": str, "version": str, "eTag": str},
    total=False,
)


class ClientBatchGetApplicationRevisionsrevisionss3LocationTypeDef(
    _ClientBatchGetApplicationRevisionsrevisionss3LocationTypeDef
):
    """
    Type definition for `ClientBatchGetApplicationRevisionsrevisions` `s3Location`

    Information about the location of a revision stored in Amazon S3.

    - **bucket** *(string) --*

      The name of the Amazon S3 bucket where the application revision is stored.

    - **key** *(string) --*

      The name of the Amazon S3 object that represents the bundled artifacts for the application
      revision.

    - **bundleType** *(string) --*

      The file type of the application revision. Must be one of the following:

      * tar: A tar archive file.

      * tgz: A compressed tar archive file.

      * zip: A zip archive file.

    - **version** *(string) --*

      A specific version of the Amazon S3 object that represents the bundled artifacts for the
      application revision.

      If the version is not specified, the system uses the most recent version by default.

    - **eTag** *(string) --*

      The ETag of the Amazon S3 object that represents the bundled artifacts for the application
      revision.

      If the ETag is not specified as an input parameter, ETag validation of the object is
      skipped.
    """


_ClientBatchGetApplicationRevisionsrevisionsstringTypeDef = TypedDict(
    "_ClientBatchGetApplicationRevisionsrevisionsstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientBatchGetApplicationRevisionsrevisionsstringTypeDef(
    _ClientBatchGetApplicationRevisionsrevisionsstringTypeDef
):
    """
    Type definition for `ClientBatchGetApplicationRevisionsrevisions` `string`

    Information about the location of an AWS Lambda deployment revision stored as a RawString.

    - **content** *(string) --*

      The YAML-formatted or JSON-formatted revision string. It includes information about which
      Lambda function to update and optional Lambda functions that validate deployment lifecycle
      events.

    - **sha256** *(string) --*

      The SHA256 hash value of the revision content.
    """


_ClientBatchGetApplicationRevisionsrevisionsTypeDef = TypedDict(
    "_ClientBatchGetApplicationRevisionsrevisionsTypeDef",
    {
        "revisionType": str,
        "s3Location": ClientBatchGetApplicationRevisionsrevisionss3LocationTypeDef,
        "gitHubLocation": ClientBatchGetApplicationRevisionsrevisionsgitHubLocationTypeDef,
        "string": ClientBatchGetApplicationRevisionsrevisionsstringTypeDef,
        "appSpecContent": ClientBatchGetApplicationRevisionsrevisionsappSpecContentTypeDef,
    },
    total=False,
)


class ClientBatchGetApplicationRevisionsrevisionsTypeDef(
    _ClientBatchGetApplicationRevisionsrevisionsTypeDef
):
    """
    Type definition for `ClientBatchGetApplicationRevisions` `revisions`

    Information about the location of an application revision.

    - **revisionType** *(string) --*

      The type of application revision:

      * S3: An application revision stored in Amazon S3.

      * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

      * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

    - **s3Location** *(dict) --*

      Information about the location of a revision stored in Amazon S3.

      - **bucket** *(string) --*

        The name of the Amazon S3 bucket where the application revision is stored.

      - **key** *(string) --*

        The name of the Amazon S3 object that represents the bundled artifacts for the application
        revision.

      - **bundleType** *(string) --*

        The file type of the application revision. Must be one of the following:

        * tar: A tar archive file.

        * tgz: A compressed tar archive file.

        * zip: A zip archive file.

      - **version** *(string) --*

        A specific version of the Amazon S3 object that represents the bundled artifacts for the
        application revision.

        If the version is not specified, the system uses the most recent version by default.

      - **eTag** *(string) --*

        The ETag of the Amazon S3 object that represents the bundled artifacts for the application
        revision.

        If the ETag is not specified as an input parameter, ETag validation of the object is
        skipped.

    - **gitHubLocation** *(dict) --*

      Information about the location of application artifacts stored in GitHub.

      - **repository** *(string) --*

        The GitHub account and repository pair that stores a reference to the commit that
        represents the bundled artifacts for the application revision.

        Specified as account/repository.

      - **commitId** *(string) --*

        The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
        application revision.

    - **string** *(dict) --*

      Information about the location of an AWS Lambda deployment revision stored as a RawString.

      - **content** *(string) --*

        The YAML-formatted or JSON-formatted revision string. It includes information about which
        Lambda function to update and optional Lambda functions that validate deployment lifecycle
        events.

      - **sha256** *(string) --*

        The SHA256 hash value of the revision content.

    - **appSpecContent** *(dict) --*

      The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is
      formatted as JSON or YAML and stored as a RawString.

      - **content** *(string) --*

        The YAML-formatted or JSON-formatted revision string.

        For an AWS Lambda deployment, the content includes a Lambda function name, the alias for
        its original version, and the alias for its replacement version. The deployment shifts
        traffic from the original version of the Lambda function to the replacement version.

        For an Amazon ECS deployment, the content includes the task name, information about the
        load balancer that serves traffic to the container, and more.

        For both types of deployments, the content can specify Lambda functions that run at
        specified hooks, such as ``BeforeInstall`` , during a deployment.

      - **sha256** *(string) --*

        The SHA256 hash value of the revision content.
    """


_ClientBatchGetApplicationsResponseapplicationsInfoTypeDef = TypedDict(
    "_ClientBatchGetApplicationsResponseapplicationsInfoTypeDef",
    {
        "applicationId": str,
        "applicationName": str,
        "createTime": datetime,
        "linkedToGitHub": bool,
        "gitHubAccountName": str,
        "computePlatform": str,
    },
    total=False,
)


class ClientBatchGetApplicationsResponseapplicationsInfoTypeDef(
    _ClientBatchGetApplicationsResponseapplicationsInfoTypeDef
):
    """
    Type definition for `ClientBatchGetApplicationsResponse` `applicationsInfo`

    Information about an application.

    - **applicationId** *(string) --*

      The application ID.

    - **applicationName** *(string) --*

      The application name.

    - **createTime** *(datetime) --*

      The time at which the application was created.

    - **linkedToGitHub** *(boolean) --*

      True if the user has authenticated with GitHub for the specified application. Otherwise,
      false.

    - **gitHubAccountName** *(string) --*

      The name for a connection to a GitHub account.

    - **computePlatform** *(string) --*

      The destination platform type for deployment of the application (``Lambda`` or ``Server``
      ).
    """


_ClientBatchGetApplicationsResponseTypeDef = TypedDict(
    "_ClientBatchGetApplicationsResponseTypeDef",
    {
        "applicationsInfo": List[
            ClientBatchGetApplicationsResponseapplicationsInfoTypeDef
        ]
    },
    total=False,
)


class ClientBatchGetApplicationsResponseTypeDef(
    _ClientBatchGetApplicationsResponseTypeDef
):
    """
    Type definition for `ClientBatchGetApplications` `Response`

    Represents the output of a BatchGetApplications operation.

    - **applicationsInfo** *(list) --*

      Information about the applications.

      - *(dict) --*

        Information about an application.

        - **applicationId** *(string) --*

          The application ID.

        - **applicationName** *(string) --*

          The application name.

        - **createTime** *(datetime) --*

          The time at which the application was created.

        - **linkedToGitHub** *(boolean) --*

          True if the user has authenticated with GitHub for the specified application. Otherwise,
          false.

        - **gitHubAccountName** *(string) --*

          The name for a connection to a GitHub account.

        - **computePlatform** *(string) --*

          The destination platform type for deployment of the application (``Lambda`` or ``Server``
          ).
    """


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoalarmConfigurationalarmsTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoalarmConfigurationalarmsTypeDef",
    {"name": str},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoalarmConfigurationalarmsTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoalarmConfigurationalarmsTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoalarmConfiguration` `alarms`

    Information about an alarm.

    - **name** *(string) --*

      The name of the alarm. Maximum length is 255 characters. Each alarm name can be
      used only once in a list of alarms.
    """


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoalarmConfigurationTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoalarmConfigurationTypeDef",
    {
        "enabled": bool,
        "ignorePollAlarmFailure": bool,
        "alarms": List[
            ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoalarmConfigurationalarmsTypeDef
        ],
    },
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoalarmConfigurationTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoalarmConfigurationTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfo` `alarmConfiguration`

    A list of alarms associated with the deployment group.

    - **enabled** *(boolean) --*

      Indicates whether the alarm configuration is enabled.

    - **ignorePollAlarmFailure** *(boolean) --*

      Indicates whether a deployment should continue if information about the current state
      of alarms cannot be retrieved from Amazon CloudWatch. The default value is false.

      * true: The deployment proceeds even if alarm status information can't be retrieved
      from Amazon CloudWatch.

      * false: The deployment stops if alarm status information can't be retrieved from
      Amazon CloudWatch.

    - **alarms** *(list) --*

      A list of alarms configured for the deployment group. A maximum of 10 alarms can be
      added to a deployment group.

      - *(dict) --*

        Information about an alarm.

        - **name** *(string) --*

          The name of the alarm. Maximum length is 255 characters. Each alarm name can be
          used only once in a list of alarms.
    """


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoautoRollbackConfigurationTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoautoRollbackConfigurationTypeDef",
    {"enabled": bool, "events": List[str]},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoautoRollbackConfigurationTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoautoRollbackConfigurationTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfo` `autoRollbackConfiguration`

    Information about the automatic rollback configuration associated with the deployment
    group.

    - **enabled** *(boolean) --*

      Indicates whether a defined automatic rollback configuration is currently enabled.

    - **events** *(list) --*

      The event type or types that trigger a rollback.

      - *(string) --*
    """


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoautoScalingGroupsTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoautoScalingGroupsTypeDef",
    {"name": str, "hook": str},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoautoScalingGroupsTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoautoScalingGroupsTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfo` `autoScalingGroups`

    Information about an Auto Scaling group.

    - **name** *(string) --*

      The Auto Scaling group name.

    - **hook** *(string) --*

      An Auto Scaling lifecycle event hook name.
    """


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    {"actionOnTimeout": str, "waitTimeInMinutes": int},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfiguration` `deploymentReadyOption`

    Information about the action to take when newly provisioned instances are ready to
    receive traffic in a blue/green deployment.

    - **actionOnTimeout** *(string) --*

      Information about when to reroute traffic from an original environment to a
      replacement environment in a blue/green deployment.

      * CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately
      after the new application revision is installed on the instances in the replacement
      environment.

      * STOP_DEPLOYMENT: Do not register new instances with a load balancer unless traffic
      rerouting is started using  ContinueDeployment . If traffic rerouting is not started
      before the end of the specified wait period, the deployment status is changed to
      Stopped.

    - **waitTimeInMinutes** *(integer) --*

      The number of minutes to wait before the status of a blue/green deployment is changed
      to Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT
      option for actionOnTimeout
    """


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    {"action": str},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfiguration` `greenFleetProvisioningOption`

    Information about how instances are provisioned for a replacement environment in a
    blue/green deployment.

    - **action** *(string) --*

      The method used to add instances to a replacement environment.

      * DISCOVER_EXISTING: Use instances that already exist or will be created manually.

      * COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to define
      and create instances in a new Auto Scaling group.
    """


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    {"action": str, "terminationWaitTimeInMinutes": int},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfiguration` `terminateBlueInstancesOnDeploymentSuccess`

    Information about whether to terminate instances in the original fleet during a
    blue/green deployment.

    - **action** *(string) --*

      The action to take on instances in the original environment after a successful
      blue/green deployment.

      * TERMINATE: Instances are terminated after a specified wait time.

      * KEEP_ALIVE: Instances are left running after they are deregistered from the load
      balancer and removed from the deployment group.

    - **terminationWaitTimeInMinutes** *(integer) --*

      For an Amazon EC2 deployment, the number of minutes to wait after a successful
      blue/green deployment before terminating instances from the original environment.

      For an Amazon ECS deployment, the number of minutes before deleting the original
      (blue) task set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the
      original (blue) task set to a replacement (green) task set.

      The maximum setting is 2880 minutes (2 days).
    """


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationTypeDef",
    {
        "terminateBlueInstancesOnDeploymentSuccess": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef,
        "deploymentReadyOption": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef,
        "greenFleetProvisioningOption": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef,
    },
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfo` `blueGreenDeploymentConfiguration`

    Information about blue/green deployment options for a deployment group.

    - **terminateBlueInstancesOnDeploymentSuccess** *(dict) --*

      Information about whether to terminate instances in the original fleet during a
      blue/green deployment.

      - **action** *(string) --*

        The action to take on instances in the original environment after a successful
        blue/green deployment.

        * TERMINATE: Instances are terminated after a specified wait time.

        * KEEP_ALIVE: Instances are left running after they are deregistered from the load
        balancer and removed from the deployment group.

      - **terminationWaitTimeInMinutes** *(integer) --*

        For an Amazon EC2 deployment, the number of minutes to wait after a successful
        blue/green deployment before terminating instances from the original environment.

        For an Amazon ECS deployment, the number of minutes before deleting the original
        (blue) task set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the
        original (blue) task set to a replacement (green) task set.

        The maximum setting is 2880 minutes (2 days).

    - **deploymentReadyOption** *(dict) --*

      Information about the action to take when newly provisioned instances are ready to
      receive traffic in a blue/green deployment.

      - **actionOnTimeout** *(string) --*

        Information about when to reroute traffic from an original environment to a
        replacement environment in a blue/green deployment.

        * CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately
        after the new application revision is installed on the instances in the replacement
        environment.

        * STOP_DEPLOYMENT: Do not register new instances with a load balancer unless traffic
        rerouting is started using  ContinueDeployment . If traffic rerouting is not started
        before the end of the specified wait period, the deployment status is changed to
        Stopped.

      - **waitTimeInMinutes** *(integer) --*

        The number of minutes to wait before the status of a blue/green deployment is changed
        to Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT
        option for actionOnTimeout

    - **greenFleetProvisioningOption** *(dict) --*

      Information about how instances are provisioned for a replacement environment in a
      blue/green deployment.

      - **action** *(string) --*

        The method used to add instances to a replacement environment.

        * DISCOVER_EXISTING: Use instances that already exist or will be created manually.

        * COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to define
        and create instances in a new Auto Scaling group.
    """


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfodeploymentStyleTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfodeploymentStyleTypeDef",
    {"deploymentType": str, "deploymentOption": str},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfodeploymentStyleTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfodeploymentStyleTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfo` `deploymentStyle`

    Information about the type of deployment, either in-place or blue/green, you want to run
    and whether to route deployment traffic behind a load balancer.

    - **deploymentType** *(string) --*

      Indicates whether to run an in-place deployment or a blue/green deployment.

    - **deploymentOption** *(string) --*

      Indicates whether to route deployment traffic behind a load balancer.
    """


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagFiltersTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": str},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagFiltersTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagFiltersTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfo` `ec2TagFilters`

    Information about an EC2 tag filter.

    - **Key** *(string) --*

      The tag filter key.

    - **Value** *(string) --*

      The tag filter value.

    - **Type** *(string) --*

      The tag filter type:

      * KEY_ONLY: Key only.

      * VALUE_ONLY: Value only.

      * KEY_AND_VALUE: Key and value.
    """


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagSetec2TagSetListTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagSetec2TagSetListTypeDef",
    {"Key": str, "Value": str, "Type": str},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagSetec2TagSetListTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagSetec2TagSetListTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagSet` `ec2TagSetList`

    Information about an EC2 tag filter.

    - **Key** *(string) --*

      The tag filter key.

    - **Value** *(string) --*

      The tag filter value.

    - **Type** *(string) --*

      The tag filter type:

      * KEY_ONLY: Key only.

      * VALUE_ONLY: Value only.

      * KEY_AND_VALUE: Key and value.
    """


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagSetTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagSetTypeDef",
    {
        "ec2TagSetList": List[
            List[
                ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagSetec2TagSetListTypeDef
            ]
        ]
    },
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagSetTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagSetTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfo` `ec2TagSet`

    Information about groups of tags applied to an EC2 instance. The deployment group
    includes only EC2 instances identified by all of the tag groups. Cannot be used in the
    same call as ec2TagFilters.

    - **ec2TagSetList** *(list) --*

      A list that contains other lists of EC2 instance tag groups. For an instance to be
      included in the deployment group, it must be identified by all of the tag groups in the
      list.

      - *(list) --*

        - *(dict) --*

          Information about an EC2 tag filter.

          - **Key** *(string) --*

            The tag filter key.

          - **Value** *(string) --*

            The tag filter value.

          - **Type** *(string) --*

            The tag filter type:

            * KEY_ONLY: Key only.

            * VALUE_ONLY: Value only.

            * KEY_AND_VALUE: Key and value.
    """


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoecsServicesTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoecsServicesTypeDef",
    {"serviceName": str, "clusterName": str},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoecsServicesTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoecsServicesTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfo` `ecsServices`

    Contains the service and cluster names used to identify an Amazon ECS deployment's
    target.

    - **serviceName** *(string) --*

      The name of the target Amazon ECS service.

    - **clusterName** *(string) --*

      The name of the cluster that the Amazon ECS service is associated with.
    """


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfolastAttemptedDeploymentTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfolastAttemptedDeploymentTypeDef",
    {"deploymentId": str, "status": str, "endTime": datetime, "createTime": datetime},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfolastAttemptedDeploymentTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfolastAttemptedDeploymentTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfo` `lastAttemptedDeployment`

    Information about the most recent attempted deployment to the deployment group.

    - **deploymentId** *(string) --*

      The unique ID of a deployment.

    - **status** *(string) --*

      The status of the most recent deployment.

    - **endTime** *(datetime) --*

      A timestamp that indicates when the most recent deployment to the deployment group was
      complete.

    - **createTime** *(datetime) --*

      A timestamp that indicates when the most recent deployment to the deployment group
      started.
    """


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfolastSuccessfulDeploymentTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfolastSuccessfulDeploymentTypeDef",
    {"deploymentId": str, "status": str, "endTime": datetime, "createTime": datetime},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfolastSuccessfulDeploymentTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfolastSuccessfulDeploymentTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfo` `lastSuccessfulDeployment`

    Information about the most recent successful deployment to the deployment group.

    - **deploymentId** *(string) --*

      The unique ID of a deployment.

    - **status** *(string) --*

      The status of the most recent deployment.

    - **endTime** *(datetime) --*

      A timestamp that indicates when the most recent deployment to the deployment group was
      complete.

    - **createTime** *(datetime) --*

      A timestamp that indicates when the most recent deployment to the deployment group
      started.
    """


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfoelbInfoListTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfoelbInfoListTypeDef",
    {"name": str},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfoelbInfoListTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfoelbInfoListTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfo` `elbInfoList`

    Information about a load balancer in Elastic Load Balancing to use in a deployment.
    Instances are registered directly with a load balancer, and traffic is routed to the
    load balancer.

    - **name** *(string) --*

      For blue/green deployments, the name of the load balancer that is used to route
      traffic from original instances to replacement instances in a blue/green
      deployment. For in-place deployments, the name of the load balancer that instances
      are deregistered from so they are not serving traffic during a deployment, and then
      re-registered with after the deployment is complete.
    """


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupInfoListTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupInfoListTypeDef",
    {"name": str},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupInfoListTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupInfoListTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfo` `targetGroupInfoList`

    Information about a target group in Elastic Load Balancing to use in a deployment.
    Instances are registered as targets in a target group, and traffic is routed to the
    target group.

    - **name** *(string) --*

      For blue/green deployments, the name of the target group that instances in the
      original environment are deregistered from, and instances in the replacement
      environment are registered with. For in-place deployments, the name of the target
      group that instances are deregistered from, so they are not serving traffic during
      a deployment, and then re-registered with after the deployment is complete.
    """


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoList` `prodTrafficRoute`

    The path used by a load balancer to route production traffic when an Amazon ECS
    deployment is complete.

    - **listenerArns** *(list) --*

      The ARN of one listener. The listener identifies the route between a target group
      and a load balancer. This is an array of strings with a maximum size of one.

      - *(string) --*
    """


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    {"name": str},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoList` `targetGroups`

    Information about a target group in Elastic Load Balancing to use in a
    deployment. Instances are registered as targets in a target group, and traffic is
    routed to the target group.

    - **name** *(string) --*

      For blue/green deployments, the name of the target group that instances in the
      original environment are deregistered from, and instances in the replacement
      environment are registered with. For in-place deployments, the name of the
      target group that instances are deregistered from, so they are not serving
      traffic during a deployment, and then re-registered with after the deployment
      is complete.
    """


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoList` `testTrafficRoute`

    An optional path used by a load balancer to route test traffic after an Amazon ECS
    deployment. Validation can occur while test traffic is served during a deployment.

    - **listenerArns** *(list) --*

      The ARN of one listener. The listener identifies the route between a target group
      and a load balancer. This is an array of strings with a maximum size of one.

      - *(string) --*
    """


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListTypeDef",
    {
        "targetGroups": List[
            ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef
        ],
        "prodTrafficRoute": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef,
        "testTrafficRoute": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef,
    },
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfo` `targetGroupPairInfoList`

    Information about two target groups and how traffic is routed during an Amazon ECS
    deployment. An optional test traffic route can be specified.

    - **targetGroups** *(list) --*

      One pair of target groups. One is associated with the original task set. The second
      is associated with the task set that serves traffic after the deployment is
      complete.

      - *(dict) --*

        Information about a target group in Elastic Load Balancing to use in a
        deployment. Instances are registered as targets in a target group, and traffic is
        routed to the target group.

        - **name** *(string) --*

          For blue/green deployments, the name of the target group that instances in the
          original environment are deregistered from, and instances in the replacement
          environment are registered with. For in-place deployments, the name of the
          target group that instances are deregistered from, so they are not serving
          traffic during a deployment, and then re-registered with after the deployment
          is complete.

    - **prodTrafficRoute** *(dict) --*

      The path used by a load balancer to route production traffic when an Amazon ECS
      deployment is complete.

      - **listenerArns** *(list) --*

        The ARN of one listener. The listener identifies the route between a target group
        and a load balancer. This is an array of strings with a maximum size of one.

        - *(string) --*

    - **testTrafficRoute** *(dict) --*

      An optional path used by a load balancer to route test traffic after an Amazon ECS
      deployment. Validation can occur while test traffic is served during a deployment.

      - **listenerArns** *(list) --*

        The ARN of one listener. The listener identifies the route between a target group
        and a load balancer. This is an array of strings with a maximum size of one.

        - *(string) --*
    """


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfoTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfoTypeDef",
    {
        "elbInfoList": List[
            ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfoelbInfoListTypeDef
        ],
        "targetGroupInfoList": List[
            ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupInfoListTypeDef
        ],
        "targetGroupPairInfoList": List[
            ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListTypeDef
        ],
    },
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfoTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfoTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfo` `loadBalancerInfo`

    Information about the load balancer to use in a deployment.

    - **elbInfoList** *(list) --*

      An array that contains information about the load balancer to use for load balancing in
      a deployment. In Elastic Load Balancing, load balancers are used with Classic Load
      Balancers.

      .. note::

        Adding more than one load balancer to the array is not supported.

      - *(dict) --*

        Information about a load balancer in Elastic Load Balancing to use in a deployment.
        Instances are registered directly with a load balancer, and traffic is routed to the
        load balancer.

        - **name** *(string) --*

          For blue/green deployments, the name of the load balancer that is used to route
          traffic from original instances to replacement instances in a blue/green
          deployment. For in-place deployments, the name of the load balancer that instances
          are deregistered from so they are not serving traffic during a deployment, and then
          re-registered with after the deployment is complete.

    - **targetGroupInfoList** *(list) --*

      An array that contains information about the target group to use for load balancing in
      a deployment. In Elastic Load Balancing, target groups are used with Application Load
      Balancers.

      .. note::

        Adding more than one target group to the array is not supported.

      - *(dict) --*

        Information about a target group in Elastic Load Balancing to use in a deployment.
        Instances are registered as targets in a target group, and traffic is routed to the
        target group.

        - **name** *(string) --*

          For blue/green deployments, the name of the target group that instances in the
          original environment are deregistered from, and instances in the replacement
          environment are registered with. For in-place deployments, the name of the target
          group that instances are deregistered from, so they are not serving traffic during
          a deployment, and then re-registered with after the deployment is complete.

    - **targetGroupPairInfoList** *(list) --*

      The target group pair information. This is an array of ``TargeGroupPairInfo`` objects
      with a maximum size of one.

      - *(dict) --*

        Information about two target groups and how traffic is routed during an Amazon ECS
        deployment. An optional test traffic route can be specified.

        - **targetGroups** *(list) --*

          One pair of target groups. One is associated with the original task set. The second
          is associated with the task set that serves traffic after the deployment is
          complete.

          - *(dict) --*

            Information about a target group in Elastic Load Balancing to use in a
            deployment. Instances are registered as targets in a target group, and traffic is
            routed to the target group.

            - **name** *(string) --*

              For blue/green deployments, the name of the target group that instances in the
              original environment are deregistered from, and instances in the replacement
              environment are registered with. For in-place deployments, the name of the
              target group that instances are deregistered from, so they are not serving
              traffic during a deployment, and then re-registered with after the deployment
              is complete.

        - **prodTrafficRoute** *(dict) --*

          The path used by a load balancer to route production traffic when an Amazon ECS
          deployment is complete.

          - **listenerArns** *(list) --*

            The ARN of one listener. The listener identifies the route between a target group
            and a load balancer. This is an array of strings with a maximum size of one.

            - *(string) --*

        - **testTrafficRoute** *(dict) --*

          An optional path used by a load balancer to route test traffic after an Amazon ECS
          deployment. Validation can occur while test traffic is served during a deployment.

          - **listenerArns** *(list) --*

            The ARN of one listener. The listener identifies the route between a target group
            and a load balancer. This is an array of strings with a maximum size of one.

            - *(string) --*
    """


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesInstanceTagFiltersTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesInstanceTagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": str},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesInstanceTagFiltersTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesInstanceTagFiltersTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfo` `onPremisesInstanceTagFilters`

    Information about an on-premises instance tag filter.

    - **Key** *(string) --*

      The on-premises instance tag filter key.

    - **Value** *(string) --*

      The on-premises instance tag filter value.

    - **Type** *(string) --*

      The on-premises instance tag filter type:

      * KEY_ONLY: Key only.

      * VALUE_ONLY: Value only.

      * KEY_AND_VALUE: Key and value.
    """


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesTagSetonPremisesTagSetListTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesTagSetonPremisesTagSetListTypeDef",
    {"Key": str, "Value": str, "Type": str},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesTagSetonPremisesTagSetListTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesTagSetonPremisesTagSetListTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesTagSet` `onPremisesTagSetList`

    Information about an on-premises instance tag filter.

    - **Key** *(string) --*

      The on-premises instance tag filter key.

    - **Value** *(string) --*

      The on-premises instance tag filter value.

    - **Type** *(string) --*

      The on-premises instance tag filter type:

      * KEY_ONLY: Key only.

      * VALUE_ONLY: Value only.

      * KEY_AND_VALUE: Key and value.
    """


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesTagSetTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesTagSetTypeDef",
    {
        "onPremisesTagSetList": List[
            List[
                ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesTagSetonPremisesTagSetListTypeDef
            ]
        ]
    },
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesTagSetTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesTagSetTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfo` `onPremisesTagSet`

    Information about groups of tags applied to an on-premises instance. The deployment group
    includes only on-premises instances identified by all the tag groups. Cannot be used in
    the same call as onPremisesInstanceTagFilters.

    - **onPremisesTagSetList** *(list) --*

      A list that contains other lists of on-premises instance tag groups. For an instance to
      be included in the deployment group, it must be identified by all of the tag groups in
      the list.

      - *(list) --*

        - *(dict) --*

          Information about an on-premises instance tag filter.

          - **Key** *(string) --*

            The on-premises instance tag filter key.

          - **Value** *(string) --*

            The on-premises instance tag filter value.

          - **Type** *(string) --*

            The on-premises instance tag filter type:

            * KEY_ONLY: Key only.

            * VALUE_ONLY: Value only.

            * KEY_AND_VALUE: Key and value.
    """


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionappSpecContentTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionappSpecContentTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionappSpecContentTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevision` `appSpecContent`

    The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content
    is formatted as JSON or YAML and stored as a RawString.

    - **content** *(string) --*

      The YAML-formatted or JSON-formatted revision string.

      For an AWS Lambda deployment, the content includes a Lambda function name, the alias
      for its original version, and the alias for its replacement version. The deployment
      shifts traffic from the original version of the Lambda function to the replacement
      version.

      For an Amazon ECS deployment, the content includes the task name, information about
      the load balancer that serves traffic to the container, and more.

      For both types of deployments, the content can specify Lambda functions that run at
      specified hooks, such as ``BeforeInstall`` , during a deployment.

    - **sha256** *(string) --*

      The SHA256 hash value of the revision content.
    """


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisiongitHubLocationTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisiongitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisiongitHubLocationTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisiongitHubLocationTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevision` `gitHubLocation`

    Information about the location of application artifacts stored in GitHub.

    - **repository** *(string) --*

      The GitHub account and repository pair that stores a reference to the commit that
      represents the bundled artifacts for the application revision.

      Specified as account/repository.

    - **commitId** *(string) --*

      The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
      application revision.
    """


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisions3LocationTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisions3LocationTypeDef",
    {"bucket": str, "key": str, "bundleType": str, "version": str, "eTag": str},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisions3LocationTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisions3LocationTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevision` `s3Location`

    Information about the location of a revision stored in Amazon S3.

    - **bucket** *(string) --*

      The name of the Amazon S3 bucket where the application revision is stored.

    - **key** *(string) --*

      The name of the Amazon S3 object that represents the bundled artifacts for the
      application revision.

    - **bundleType** *(string) --*

      The file type of the application revision. Must be one of the following:

      * tar: A tar archive file.

      * tgz: A compressed tar archive file.

      * zip: A zip archive file.

    - **version** *(string) --*

      A specific version of the Amazon S3 object that represents the bundled artifacts for
      the application revision.

      If the version is not specified, the system uses the most recent version by default.

    - **eTag** *(string) --*

      The ETag of the Amazon S3 object that represents the bundled artifacts for the
      application revision.

      If the ETag is not specified as an input parameter, ETag validation of the object is
      skipped.
    """


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionstringTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionstringTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionstringTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevision` `string`

    Information about the location of an AWS Lambda deployment revision stored as a
    RawString.

    - **content** *(string) --*

      The YAML-formatted or JSON-formatted revision string. It includes information about
      which Lambda function to update and optional Lambda functions that validate
      deployment lifecycle events.

    - **sha256** *(string) --*

      The SHA256 hash value of the revision content.
    """


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionTypeDef",
    {
        "revisionType": str,
        "s3Location": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisions3LocationTypeDef,
        "gitHubLocation": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisiongitHubLocationTypeDef,
        "string": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionstringTypeDef,
        "appSpecContent": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionappSpecContentTypeDef,
    },
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfo` `targetRevision`

    Information about the deployment group's target revision, including type and location.

    - **revisionType** *(string) --*

      The type of application revision:

      * S3: An application revision stored in Amazon S3.

      * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

      * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

    - **s3Location** *(dict) --*

      Information about the location of a revision stored in Amazon S3.

      - **bucket** *(string) --*

        The name of the Amazon S3 bucket where the application revision is stored.

      - **key** *(string) --*

        The name of the Amazon S3 object that represents the bundled artifacts for the
        application revision.

      - **bundleType** *(string) --*

        The file type of the application revision. Must be one of the following:

        * tar: A tar archive file.

        * tgz: A compressed tar archive file.

        * zip: A zip archive file.

      - **version** *(string) --*

        A specific version of the Amazon S3 object that represents the bundled artifacts for
        the application revision.

        If the version is not specified, the system uses the most recent version by default.

      - **eTag** *(string) --*

        The ETag of the Amazon S3 object that represents the bundled artifacts for the
        application revision.

        If the ETag is not specified as an input parameter, ETag validation of the object is
        skipped.

    - **gitHubLocation** *(dict) --*

      Information about the location of application artifacts stored in GitHub.

      - **repository** *(string) --*

        The GitHub account and repository pair that stores a reference to the commit that
        represents the bundled artifacts for the application revision.

        Specified as account/repository.

      - **commitId** *(string) --*

        The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
        application revision.

    - **string** *(dict) --*

      Information about the location of an AWS Lambda deployment revision stored as a
      RawString.

      - **content** *(string) --*

        The YAML-formatted or JSON-formatted revision string. It includes information about
        which Lambda function to update and optional Lambda functions that validate
        deployment lifecycle events.

      - **sha256** *(string) --*

        The SHA256 hash value of the revision content.

    - **appSpecContent** *(dict) --*

      The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content
      is formatted as JSON or YAML and stored as a RawString.

      - **content** *(string) --*

        The YAML-formatted or JSON-formatted revision string.

        For an AWS Lambda deployment, the content includes a Lambda function name, the alias
        for its original version, and the alias for its replacement version. The deployment
        shifts traffic from the original version of the Lambda function to the replacement
        version.

        For an Amazon ECS deployment, the content includes the task name, information about
        the load balancer that serves traffic to the container, and more.

        For both types of deployments, the content can specify Lambda functions that run at
        specified hooks, such as ``BeforeInstall`` , during a deployment.

      - **sha256** *(string) --*

        The SHA256 hash value of the revision content.
    """


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotriggerConfigurationsTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotriggerConfigurationsTypeDef",
    {"triggerName": str, "triggerTargetArn": str, "triggerEvents": List[str]},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotriggerConfigurationsTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotriggerConfigurationsTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfo` `triggerConfigurations`

    Information about notification triggers for the deployment group.

    - **triggerName** *(string) --*

      The name of the notification trigger.

    - **triggerTargetArn** *(string) --*

      The ARN of the Amazon Simple Notification Service topic through which notifications
      about deployment or instance events are sent.

    - **triggerEvents** *(list) --*

      The event type or types for which notifications are triggered.

      - *(string) --*
    """


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoTypeDef",
    {
        "applicationName": str,
        "deploymentGroupId": str,
        "deploymentGroupName": str,
        "deploymentConfigName": str,
        "ec2TagFilters": List[
            ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagFiltersTypeDef
        ],
        "onPremisesInstanceTagFilters": List[
            ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesInstanceTagFiltersTypeDef
        ],
        "autoScalingGroups": List[
            ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoautoScalingGroupsTypeDef
        ],
        "serviceRoleArn": str,
        "targetRevision": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionTypeDef,
        "triggerConfigurations": List[
            ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotriggerConfigurationsTypeDef
        ],
        "alarmConfiguration": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoalarmConfigurationTypeDef,
        "autoRollbackConfiguration": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoautoRollbackConfigurationTypeDef,
        "deploymentStyle": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfodeploymentStyleTypeDef,
        "blueGreenDeploymentConfiguration": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationTypeDef,
        "loadBalancerInfo": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfoTypeDef,
        "lastSuccessfulDeployment": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfolastSuccessfulDeploymentTypeDef,
        "lastAttemptedDeployment": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfolastAttemptedDeploymentTypeDef,
        "ec2TagSet": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagSetTypeDef,
        "onPremisesTagSet": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesTagSetTypeDef,
        "computePlatform": str,
        "ecsServices": List[
            ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoecsServicesTypeDef
        ],
    },
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentGroupsResponse` `deploymentGroupsInfo`

    Information about a deployment group.

    - **applicationName** *(string) --*

      The application name.

    - **deploymentGroupId** *(string) --*

      The deployment group ID.

    - **deploymentGroupName** *(string) --*

      The deployment group name.

    - **deploymentConfigName** *(string) --*

      The deployment configuration name.

    - **ec2TagFilters** *(list) --*

      The Amazon EC2 tags on which to filter. The deployment group includes EC2 instances with
      any of the specified tags.

      - *(dict) --*

        Information about an EC2 tag filter.

        - **Key** *(string) --*

          The tag filter key.

        - **Value** *(string) --*

          The tag filter value.

        - **Type** *(string) --*

          The tag filter type:

          * KEY_ONLY: Key only.

          * VALUE_ONLY: Value only.

          * KEY_AND_VALUE: Key and value.

    - **onPremisesInstanceTagFilters** *(list) --*

      The on-premises instance tags on which to filter. The deployment group includes
      on-premises instances with any of the specified tags.

      - *(dict) --*

        Information about an on-premises instance tag filter.

        - **Key** *(string) --*

          The on-premises instance tag filter key.

        - **Value** *(string) --*

          The on-premises instance tag filter value.

        - **Type** *(string) --*

          The on-premises instance tag filter type:

          * KEY_ONLY: Key only.

          * VALUE_ONLY: Value only.

          * KEY_AND_VALUE: Key and value.

    - **autoScalingGroups** *(list) --*

      A list of associated Auto Scaling groups.

      - *(dict) --*

        Information about an Auto Scaling group.

        - **name** *(string) --*

          The Auto Scaling group name.

        - **hook** *(string) --*

          An Auto Scaling lifecycle event hook name.

    - **serviceRoleArn** *(string) --*

      A service role Amazon Resource Name (ARN) that grants CodeDeploy permission to make calls
      to AWS services on your behalf. For more information, see `Create a Service Role for AWS
      CodeDeploy
      <https://docs.aws.amazon.com/codedeploy/latest/userguide/getting-started-create-service-role.html>`__
      in the *AWS CodeDeploy User Guide* .

    - **targetRevision** *(dict) --*

      Information about the deployment group's target revision, including type and location.

      - **revisionType** *(string) --*

        The type of application revision:

        * S3: An application revision stored in Amazon S3.

        * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

        * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

      - **s3Location** *(dict) --*

        Information about the location of a revision stored in Amazon S3.

        - **bucket** *(string) --*

          The name of the Amazon S3 bucket where the application revision is stored.

        - **key** *(string) --*

          The name of the Amazon S3 object that represents the bundled artifacts for the
          application revision.

        - **bundleType** *(string) --*

          The file type of the application revision. Must be one of the following:

          * tar: A tar archive file.

          * tgz: A compressed tar archive file.

          * zip: A zip archive file.

        - **version** *(string) --*

          A specific version of the Amazon S3 object that represents the bundled artifacts for
          the application revision.

          If the version is not specified, the system uses the most recent version by default.

        - **eTag** *(string) --*

          The ETag of the Amazon S3 object that represents the bundled artifacts for the
          application revision.

          If the ETag is not specified as an input parameter, ETag validation of the object is
          skipped.

      - **gitHubLocation** *(dict) --*

        Information about the location of application artifacts stored in GitHub.

        - **repository** *(string) --*

          The GitHub account and repository pair that stores a reference to the commit that
          represents the bundled artifacts for the application revision.

          Specified as account/repository.

        - **commitId** *(string) --*

          The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
          application revision.

      - **string** *(dict) --*

        Information about the location of an AWS Lambda deployment revision stored as a
        RawString.

        - **content** *(string) --*

          The YAML-formatted or JSON-formatted revision string. It includes information about
          which Lambda function to update and optional Lambda functions that validate
          deployment lifecycle events.

        - **sha256** *(string) --*

          The SHA256 hash value of the revision content.

      - **appSpecContent** *(dict) --*

        The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content
        is formatted as JSON or YAML and stored as a RawString.

        - **content** *(string) --*

          The YAML-formatted or JSON-formatted revision string.

          For an AWS Lambda deployment, the content includes a Lambda function name, the alias
          for its original version, and the alias for its replacement version. The deployment
          shifts traffic from the original version of the Lambda function to the replacement
          version.

          For an Amazon ECS deployment, the content includes the task name, information about
          the load balancer that serves traffic to the container, and more.

          For both types of deployments, the content can specify Lambda functions that run at
          specified hooks, such as ``BeforeInstall`` , during a deployment.

        - **sha256** *(string) --*

          The SHA256 hash value of the revision content.

    - **triggerConfigurations** *(list) --*

      Information about triggers associated with the deployment group.

      - *(dict) --*

        Information about notification triggers for the deployment group.

        - **triggerName** *(string) --*

          The name of the notification trigger.

        - **triggerTargetArn** *(string) --*

          The ARN of the Amazon Simple Notification Service topic through which notifications
          about deployment or instance events are sent.

        - **triggerEvents** *(list) --*

          The event type or types for which notifications are triggered.

          - *(string) --*

    - **alarmConfiguration** *(dict) --*

      A list of alarms associated with the deployment group.

      - **enabled** *(boolean) --*

        Indicates whether the alarm configuration is enabled.

      - **ignorePollAlarmFailure** *(boolean) --*

        Indicates whether a deployment should continue if information about the current state
        of alarms cannot be retrieved from Amazon CloudWatch. The default value is false.

        * true: The deployment proceeds even if alarm status information can't be retrieved
        from Amazon CloudWatch.

        * false: The deployment stops if alarm status information can't be retrieved from
        Amazon CloudWatch.

      - **alarms** *(list) --*

        A list of alarms configured for the deployment group. A maximum of 10 alarms can be
        added to a deployment group.

        - *(dict) --*

          Information about an alarm.

          - **name** *(string) --*

            The name of the alarm. Maximum length is 255 characters. Each alarm name can be
            used only once in a list of alarms.

    - **autoRollbackConfiguration** *(dict) --*

      Information about the automatic rollback configuration associated with the deployment
      group.

      - **enabled** *(boolean) --*

        Indicates whether a defined automatic rollback configuration is currently enabled.

      - **events** *(list) --*

        The event type or types that trigger a rollback.

        - *(string) --*

    - **deploymentStyle** *(dict) --*

      Information about the type of deployment, either in-place or blue/green, you want to run
      and whether to route deployment traffic behind a load balancer.

      - **deploymentType** *(string) --*

        Indicates whether to run an in-place deployment or a blue/green deployment.

      - **deploymentOption** *(string) --*

        Indicates whether to route deployment traffic behind a load balancer.

    - **blueGreenDeploymentConfiguration** *(dict) --*

      Information about blue/green deployment options for a deployment group.

      - **terminateBlueInstancesOnDeploymentSuccess** *(dict) --*

        Information about whether to terminate instances in the original fleet during a
        blue/green deployment.

        - **action** *(string) --*

          The action to take on instances in the original environment after a successful
          blue/green deployment.

          * TERMINATE: Instances are terminated after a specified wait time.

          * KEEP_ALIVE: Instances are left running after they are deregistered from the load
          balancer and removed from the deployment group.

        - **terminationWaitTimeInMinutes** *(integer) --*

          For an Amazon EC2 deployment, the number of minutes to wait after a successful
          blue/green deployment before terminating instances from the original environment.

          For an Amazon ECS deployment, the number of minutes before deleting the original
          (blue) task set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the
          original (blue) task set to a replacement (green) task set.

          The maximum setting is 2880 minutes (2 days).

      - **deploymentReadyOption** *(dict) --*

        Information about the action to take when newly provisioned instances are ready to
        receive traffic in a blue/green deployment.

        - **actionOnTimeout** *(string) --*

          Information about when to reroute traffic from an original environment to a
          replacement environment in a blue/green deployment.

          * CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately
          after the new application revision is installed on the instances in the replacement
          environment.

          * STOP_DEPLOYMENT: Do not register new instances with a load balancer unless traffic
          rerouting is started using  ContinueDeployment . If traffic rerouting is not started
          before the end of the specified wait period, the deployment status is changed to
          Stopped.

        - **waitTimeInMinutes** *(integer) --*

          The number of minutes to wait before the status of a blue/green deployment is changed
          to Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT
          option for actionOnTimeout

      - **greenFleetProvisioningOption** *(dict) --*

        Information about how instances are provisioned for a replacement environment in a
        blue/green deployment.

        - **action** *(string) --*

          The method used to add instances to a replacement environment.

          * DISCOVER_EXISTING: Use instances that already exist or will be created manually.

          * COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to define
          and create instances in a new Auto Scaling group.

    - **loadBalancerInfo** *(dict) --*

      Information about the load balancer to use in a deployment.

      - **elbInfoList** *(list) --*

        An array that contains information about the load balancer to use for load balancing in
        a deployment. In Elastic Load Balancing, load balancers are used with Classic Load
        Balancers.

        .. note::

          Adding more than one load balancer to the array is not supported.

        - *(dict) --*

          Information about a load balancer in Elastic Load Balancing to use in a deployment.
          Instances are registered directly with a load balancer, and traffic is routed to the
          load balancer.

          - **name** *(string) --*

            For blue/green deployments, the name of the load balancer that is used to route
            traffic from original instances to replacement instances in a blue/green
            deployment. For in-place deployments, the name of the load balancer that instances
            are deregistered from so they are not serving traffic during a deployment, and then
            re-registered with after the deployment is complete.

      - **targetGroupInfoList** *(list) --*

        An array that contains information about the target group to use for load balancing in
        a deployment. In Elastic Load Balancing, target groups are used with Application Load
        Balancers.

        .. note::

          Adding more than one target group to the array is not supported.

        - *(dict) --*

          Information about a target group in Elastic Load Balancing to use in a deployment.
          Instances are registered as targets in a target group, and traffic is routed to the
          target group.

          - **name** *(string) --*

            For blue/green deployments, the name of the target group that instances in the
            original environment are deregistered from, and instances in the replacement
            environment are registered with. For in-place deployments, the name of the target
            group that instances are deregistered from, so they are not serving traffic during
            a deployment, and then re-registered with after the deployment is complete.

      - **targetGroupPairInfoList** *(list) --*

        The target group pair information. This is an array of ``TargeGroupPairInfo`` objects
        with a maximum size of one.

        - *(dict) --*

          Information about two target groups and how traffic is routed during an Amazon ECS
          deployment. An optional test traffic route can be specified.

          - **targetGroups** *(list) --*

            One pair of target groups. One is associated with the original task set. The second
            is associated with the task set that serves traffic after the deployment is
            complete.

            - *(dict) --*

              Information about a target group in Elastic Load Balancing to use in a
              deployment. Instances are registered as targets in a target group, and traffic is
              routed to the target group.

              - **name** *(string) --*

                For blue/green deployments, the name of the target group that instances in the
                original environment are deregistered from, and instances in the replacement
                environment are registered with. For in-place deployments, the name of the
                target group that instances are deregistered from, so they are not serving
                traffic during a deployment, and then re-registered with after the deployment
                is complete.

          - **prodTrafficRoute** *(dict) --*

            The path used by a load balancer to route production traffic when an Amazon ECS
            deployment is complete.

            - **listenerArns** *(list) --*

              The ARN of one listener. The listener identifies the route between a target group
              and a load balancer. This is an array of strings with a maximum size of one.

              - *(string) --*

          - **testTrafficRoute** *(dict) --*

            An optional path used by a load balancer to route test traffic after an Amazon ECS
            deployment. Validation can occur while test traffic is served during a deployment.

            - **listenerArns** *(list) --*

              The ARN of one listener. The listener identifies the route between a target group
              and a load balancer. This is an array of strings with a maximum size of one.

              - *(string) --*

    - **lastSuccessfulDeployment** *(dict) --*

      Information about the most recent successful deployment to the deployment group.

      - **deploymentId** *(string) --*

        The unique ID of a deployment.

      - **status** *(string) --*

        The status of the most recent deployment.

      - **endTime** *(datetime) --*

        A timestamp that indicates when the most recent deployment to the deployment group was
        complete.

      - **createTime** *(datetime) --*

        A timestamp that indicates when the most recent deployment to the deployment group
        started.

    - **lastAttemptedDeployment** *(dict) --*

      Information about the most recent attempted deployment to the deployment group.

      - **deploymentId** *(string) --*

        The unique ID of a deployment.

      - **status** *(string) --*

        The status of the most recent deployment.

      - **endTime** *(datetime) --*

        A timestamp that indicates when the most recent deployment to the deployment group was
        complete.

      - **createTime** *(datetime) --*

        A timestamp that indicates when the most recent deployment to the deployment group
        started.

    - **ec2TagSet** *(dict) --*

      Information about groups of tags applied to an EC2 instance. The deployment group
      includes only EC2 instances identified by all of the tag groups. Cannot be used in the
      same call as ec2TagFilters.

      - **ec2TagSetList** *(list) --*

        A list that contains other lists of EC2 instance tag groups. For an instance to be
        included in the deployment group, it must be identified by all of the tag groups in the
        list.

        - *(list) --*

          - *(dict) --*

            Information about an EC2 tag filter.

            - **Key** *(string) --*

              The tag filter key.

            - **Value** *(string) --*

              The tag filter value.

            - **Type** *(string) --*

              The tag filter type:

              * KEY_ONLY: Key only.

              * VALUE_ONLY: Value only.

              * KEY_AND_VALUE: Key and value.

    - **onPremisesTagSet** *(dict) --*

      Information about groups of tags applied to an on-premises instance. The deployment group
      includes only on-premises instances identified by all the tag groups. Cannot be used in
      the same call as onPremisesInstanceTagFilters.

      - **onPremisesTagSetList** *(list) --*

        A list that contains other lists of on-premises instance tag groups. For an instance to
        be included in the deployment group, it must be identified by all of the tag groups in
        the list.

        - *(list) --*

          - *(dict) --*

            Information about an on-premises instance tag filter.

            - **Key** *(string) --*

              The on-premises instance tag filter key.

            - **Value** *(string) --*

              The on-premises instance tag filter value.

            - **Type** *(string) --*

              The on-premises instance tag filter type:

              * KEY_ONLY: Key only.

              * VALUE_ONLY: Value only.

              * KEY_AND_VALUE: Key and value.

    - **computePlatform** *(string) --*

      The destination platform type for the deployment (``Lambda`` , ``Server`` , or ``ECS`` ).

    - **ecsServices** *(list) --*

      The target Amazon ECS services in the deployment group. This applies only to deployment
      groups that use the Amazon ECS compute platform. A target Amazon ECS service is specified
      as an Amazon ECS cluster and service name pair using the format
      ``<clustername>:<servicename>`` .

      - *(dict) --*

        Contains the service and cluster names used to identify an Amazon ECS deployment's
        target.

        - **serviceName** *(string) --*

          The name of the target Amazon ECS service.

        - **clusterName** *(string) --*

          The name of the cluster that the Amazon ECS service is associated with.
    """


_ClientBatchGetDeploymentGroupsResponseTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponseTypeDef",
    {
        "deploymentGroupsInfo": List[
            ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoTypeDef
        ],
        "errorMessage": str,
    },
    total=False,
)


class ClientBatchGetDeploymentGroupsResponseTypeDef(
    _ClientBatchGetDeploymentGroupsResponseTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentGroups` `Response`

    Represents the output of a BatchGetDeploymentGroups operation.

    - **deploymentGroupsInfo** *(list) --*

      Information about the deployment groups.

      - *(dict) --*

        Information about a deployment group.

        - **applicationName** *(string) --*

          The application name.

        - **deploymentGroupId** *(string) --*

          The deployment group ID.

        - **deploymentGroupName** *(string) --*

          The deployment group name.

        - **deploymentConfigName** *(string) --*

          The deployment configuration name.

        - **ec2TagFilters** *(list) --*

          The Amazon EC2 tags on which to filter. The deployment group includes EC2 instances with
          any of the specified tags.

          - *(dict) --*

            Information about an EC2 tag filter.

            - **Key** *(string) --*

              The tag filter key.

            - **Value** *(string) --*

              The tag filter value.

            - **Type** *(string) --*

              The tag filter type:

              * KEY_ONLY: Key only.

              * VALUE_ONLY: Value only.

              * KEY_AND_VALUE: Key and value.

        - **onPremisesInstanceTagFilters** *(list) --*

          The on-premises instance tags on which to filter. The deployment group includes
          on-premises instances with any of the specified tags.

          - *(dict) --*

            Information about an on-premises instance tag filter.

            - **Key** *(string) --*

              The on-premises instance tag filter key.

            - **Value** *(string) --*

              The on-premises instance tag filter value.

            - **Type** *(string) --*

              The on-premises instance tag filter type:

              * KEY_ONLY: Key only.

              * VALUE_ONLY: Value only.

              * KEY_AND_VALUE: Key and value.

        - **autoScalingGroups** *(list) --*

          A list of associated Auto Scaling groups.

          - *(dict) --*

            Information about an Auto Scaling group.

            - **name** *(string) --*

              The Auto Scaling group name.

            - **hook** *(string) --*

              An Auto Scaling lifecycle event hook name.

        - **serviceRoleArn** *(string) --*

          A service role Amazon Resource Name (ARN) that grants CodeDeploy permission to make calls
          to AWS services on your behalf. For more information, see `Create a Service Role for AWS
          CodeDeploy
          <https://docs.aws.amazon.com/codedeploy/latest/userguide/getting-started-create-service-role.html>`__
          in the *AWS CodeDeploy User Guide* .

        - **targetRevision** *(dict) --*

          Information about the deployment group's target revision, including type and location.

          - **revisionType** *(string) --*

            The type of application revision:

            * S3: An application revision stored in Amazon S3.

            * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

            * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

          - **s3Location** *(dict) --*

            Information about the location of a revision stored in Amazon S3.

            - **bucket** *(string) --*

              The name of the Amazon S3 bucket where the application revision is stored.

            - **key** *(string) --*

              The name of the Amazon S3 object that represents the bundled artifacts for the
              application revision.

            - **bundleType** *(string) --*

              The file type of the application revision. Must be one of the following:

              * tar: A tar archive file.

              * tgz: A compressed tar archive file.

              * zip: A zip archive file.

            - **version** *(string) --*

              A specific version of the Amazon S3 object that represents the bundled artifacts for
              the application revision.

              If the version is not specified, the system uses the most recent version by default.

            - **eTag** *(string) --*

              The ETag of the Amazon S3 object that represents the bundled artifacts for the
              application revision.

              If the ETag is not specified as an input parameter, ETag validation of the object is
              skipped.

          - **gitHubLocation** *(dict) --*

            Information about the location of application artifacts stored in GitHub.

            - **repository** *(string) --*

              The GitHub account and repository pair that stores a reference to the commit that
              represents the bundled artifacts for the application revision.

              Specified as account/repository.

            - **commitId** *(string) --*

              The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
              application revision.

          - **string** *(dict) --*

            Information about the location of an AWS Lambda deployment revision stored as a
            RawString.

            - **content** *(string) --*

              The YAML-formatted or JSON-formatted revision string. It includes information about
              which Lambda function to update and optional Lambda functions that validate
              deployment lifecycle events.

            - **sha256** *(string) --*

              The SHA256 hash value of the revision content.

          - **appSpecContent** *(dict) --*

            The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content
            is formatted as JSON or YAML and stored as a RawString.

            - **content** *(string) --*

              The YAML-formatted or JSON-formatted revision string.

              For an AWS Lambda deployment, the content includes a Lambda function name, the alias
              for its original version, and the alias for its replacement version. The deployment
              shifts traffic from the original version of the Lambda function to the replacement
              version.

              For an Amazon ECS deployment, the content includes the task name, information about
              the load balancer that serves traffic to the container, and more.

              For both types of deployments, the content can specify Lambda functions that run at
              specified hooks, such as ``BeforeInstall`` , during a deployment.

            - **sha256** *(string) --*

              The SHA256 hash value of the revision content.

        - **triggerConfigurations** *(list) --*

          Information about triggers associated with the deployment group.

          - *(dict) --*

            Information about notification triggers for the deployment group.

            - **triggerName** *(string) --*

              The name of the notification trigger.

            - **triggerTargetArn** *(string) --*

              The ARN of the Amazon Simple Notification Service topic through which notifications
              about deployment or instance events are sent.

            - **triggerEvents** *(list) --*

              The event type or types for which notifications are triggered.

              - *(string) --*

        - **alarmConfiguration** *(dict) --*

          A list of alarms associated with the deployment group.

          - **enabled** *(boolean) --*

            Indicates whether the alarm configuration is enabled.

          - **ignorePollAlarmFailure** *(boolean) --*

            Indicates whether a deployment should continue if information about the current state
            of alarms cannot be retrieved from Amazon CloudWatch. The default value is false.

            * true: The deployment proceeds even if alarm status information can't be retrieved
            from Amazon CloudWatch.

            * false: The deployment stops if alarm status information can't be retrieved from
            Amazon CloudWatch.

          - **alarms** *(list) --*

            A list of alarms configured for the deployment group. A maximum of 10 alarms can be
            added to a deployment group.

            - *(dict) --*

              Information about an alarm.

              - **name** *(string) --*

                The name of the alarm. Maximum length is 255 characters. Each alarm name can be
                used only once in a list of alarms.

        - **autoRollbackConfiguration** *(dict) --*

          Information about the automatic rollback configuration associated with the deployment
          group.

          - **enabled** *(boolean) --*

            Indicates whether a defined automatic rollback configuration is currently enabled.

          - **events** *(list) --*

            The event type or types that trigger a rollback.

            - *(string) --*

        - **deploymentStyle** *(dict) --*

          Information about the type of deployment, either in-place or blue/green, you want to run
          and whether to route deployment traffic behind a load balancer.

          - **deploymentType** *(string) --*

            Indicates whether to run an in-place deployment or a blue/green deployment.

          - **deploymentOption** *(string) --*

            Indicates whether to route deployment traffic behind a load balancer.

        - **blueGreenDeploymentConfiguration** *(dict) --*

          Information about blue/green deployment options for a deployment group.

          - **terminateBlueInstancesOnDeploymentSuccess** *(dict) --*

            Information about whether to terminate instances in the original fleet during a
            blue/green deployment.

            - **action** *(string) --*

              The action to take on instances in the original environment after a successful
              blue/green deployment.

              * TERMINATE: Instances are terminated after a specified wait time.

              * KEEP_ALIVE: Instances are left running after they are deregistered from the load
              balancer and removed from the deployment group.

            - **terminationWaitTimeInMinutes** *(integer) --*

              For an Amazon EC2 deployment, the number of minutes to wait after a successful
              blue/green deployment before terminating instances from the original environment.

              For an Amazon ECS deployment, the number of minutes before deleting the original
              (blue) task set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the
              original (blue) task set to a replacement (green) task set.

              The maximum setting is 2880 minutes (2 days).

          - **deploymentReadyOption** *(dict) --*

            Information about the action to take when newly provisioned instances are ready to
            receive traffic in a blue/green deployment.

            - **actionOnTimeout** *(string) --*

              Information about when to reroute traffic from an original environment to a
              replacement environment in a blue/green deployment.

              * CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately
              after the new application revision is installed on the instances in the replacement
              environment.

              * STOP_DEPLOYMENT: Do not register new instances with a load balancer unless traffic
              rerouting is started using  ContinueDeployment . If traffic rerouting is not started
              before the end of the specified wait period, the deployment status is changed to
              Stopped.

            - **waitTimeInMinutes** *(integer) --*

              The number of minutes to wait before the status of a blue/green deployment is changed
              to Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT
              option for actionOnTimeout

          - **greenFleetProvisioningOption** *(dict) --*

            Information about how instances are provisioned for a replacement environment in a
            blue/green deployment.

            - **action** *(string) --*

              The method used to add instances to a replacement environment.

              * DISCOVER_EXISTING: Use instances that already exist or will be created manually.

              * COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to define
              and create instances in a new Auto Scaling group.

        - **loadBalancerInfo** *(dict) --*

          Information about the load balancer to use in a deployment.

          - **elbInfoList** *(list) --*

            An array that contains information about the load balancer to use for load balancing in
            a deployment. In Elastic Load Balancing, load balancers are used with Classic Load
            Balancers.

            .. note::

              Adding more than one load balancer to the array is not supported.

            - *(dict) --*

              Information about a load balancer in Elastic Load Balancing to use in a deployment.
              Instances are registered directly with a load balancer, and traffic is routed to the
              load balancer.

              - **name** *(string) --*

                For blue/green deployments, the name of the load balancer that is used to route
                traffic from original instances to replacement instances in a blue/green
                deployment. For in-place deployments, the name of the load balancer that instances
                are deregistered from so they are not serving traffic during a deployment, and then
                re-registered with after the deployment is complete.

          - **targetGroupInfoList** *(list) --*

            An array that contains information about the target group to use for load balancing in
            a deployment. In Elastic Load Balancing, target groups are used with Application Load
            Balancers.

            .. note::

              Adding more than one target group to the array is not supported.

            - *(dict) --*

              Information about a target group in Elastic Load Balancing to use in a deployment.
              Instances are registered as targets in a target group, and traffic is routed to the
              target group.

              - **name** *(string) --*

                For blue/green deployments, the name of the target group that instances in the
                original environment are deregistered from, and instances in the replacement
                environment are registered with. For in-place deployments, the name of the target
                group that instances are deregistered from, so they are not serving traffic during
                a deployment, and then re-registered with after the deployment is complete.

          - **targetGroupPairInfoList** *(list) --*

            The target group pair information. This is an array of ``TargeGroupPairInfo`` objects
            with a maximum size of one.

            - *(dict) --*

              Information about two target groups and how traffic is routed during an Amazon ECS
              deployment. An optional test traffic route can be specified.

              - **targetGroups** *(list) --*

                One pair of target groups. One is associated with the original task set. The second
                is associated with the task set that serves traffic after the deployment is
                complete.

                - *(dict) --*

                  Information about a target group in Elastic Load Balancing to use in a
                  deployment. Instances are registered as targets in a target group, and traffic is
                  routed to the target group.

                  - **name** *(string) --*

                    For blue/green deployments, the name of the target group that instances in the
                    original environment are deregistered from, and instances in the replacement
                    environment are registered with. For in-place deployments, the name of the
                    target group that instances are deregistered from, so they are not serving
                    traffic during a deployment, and then re-registered with after the deployment
                    is complete.

              - **prodTrafficRoute** *(dict) --*

                The path used by a load balancer to route production traffic when an Amazon ECS
                deployment is complete.

                - **listenerArns** *(list) --*

                  The ARN of one listener. The listener identifies the route between a target group
                  and a load balancer. This is an array of strings with a maximum size of one.

                  - *(string) --*

              - **testTrafficRoute** *(dict) --*

                An optional path used by a load balancer to route test traffic after an Amazon ECS
                deployment. Validation can occur while test traffic is served during a deployment.

                - **listenerArns** *(list) --*

                  The ARN of one listener. The listener identifies the route between a target group
                  and a load balancer. This is an array of strings with a maximum size of one.

                  - *(string) --*

        - **lastSuccessfulDeployment** *(dict) --*

          Information about the most recent successful deployment to the deployment group.

          - **deploymentId** *(string) --*

            The unique ID of a deployment.

          - **status** *(string) --*

            The status of the most recent deployment.

          - **endTime** *(datetime) --*

            A timestamp that indicates when the most recent deployment to the deployment group was
            complete.

          - **createTime** *(datetime) --*

            A timestamp that indicates when the most recent deployment to the deployment group
            started.

        - **lastAttemptedDeployment** *(dict) --*

          Information about the most recent attempted deployment to the deployment group.

          - **deploymentId** *(string) --*

            The unique ID of a deployment.

          - **status** *(string) --*

            The status of the most recent deployment.

          - **endTime** *(datetime) --*

            A timestamp that indicates when the most recent deployment to the deployment group was
            complete.

          - **createTime** *(datetime) --*

            A timestamp that indicates when the most recent deployment to the deployment group
            started.

        - **ec2TagSet** *(dict) --*

          Information about groups of tags applied to an EC2 instance. The deployment group
          includes only EC2 instances identified by all of the tag groups. Cannot be used in the
          same call as ec2TagFilters.

          - **ec2TagSetList** *(list) --*

            A list that contains other lists of EC2 instance tag groups. For an instance to be
            included in the deployment group, it must be identified by all of the tag groups in the
            list.

            - *(list) --*

              - *(dict) --*

                Information about an EC2 tag filter.

                - **Key** *(string) --*

                  The tag filter key.

                - **Value** *(string) --*

                  The tag filter value.

                - **Type** *(string) --*

                  The tag filter type:

                  * KEY_ONLY: Key only.

                  * VALUE_ONLY: Value only.

                  * KEY_AND_VALUE: Key and value.

        - **onPremisesTagSet** *(dict) --*

          Information about groups of tags applied to an on-premises instance. The deployment group
          includes only on-premises instances identified by all the tag groups. Cannot be used in
          the same call as onPremisesInstanceTagFilters.

          - **onPremisesTagSetList** *(list) --*

            A list that contains other lists of on-premises instance tag groups. For an instance to
            be included in the deployment group, it must be identified by all of the tag groups in
            the list.

            - *(list) --*

              - *(dict) --*

                Information about an on-premises instance tag filter.

                - **Key** *(string) --*

                  The on-premises instance tag filter key.

                - **Value** *(string) --*

                  The on-premises instance tag filter value.

                - **Type** *(string) --*

                  The on-premises instance tag filter type:

                  * KEY_ONLY: Key only.

                  * VALUE_ONLY: Value only.

                  * KEY_AND_VALUE: Key and value.

        - **computePlatform** *(string) --*

          The destination platform type for the deployment (``Lambda`` , ``Server`` , or ``ECS`` ).

        - **ecsServices** *(list) --*

          The target Amazon ECS services in the deployment group. This applies only to deployment
          groups that use the Amazon ECS compute platform. A target Amazon ECS service is specified
          as an Amazon ECS cluster and service name pair using the format
          ``<clustername>:<servicename>`` .

          - *(dict) --*

            Contains the service and cluster names used to identify an Amazon ECS deployment's
            target.

            - **serviceName** *(string) --*

              The name of the target Amazon ECS service.

            - **clusterName** *(string) --*

              The name of the cluster that the Amazon ECS service is associated with.

    - **errorMessage** *(string) --*

      Information about errors that might have occurred during the API call.
    """


_ClientBatchGetDeploymentInstancesResponseinstancesSummarylifecycleEventsdiagnosticsTypeDef = TypedDict(
    "_ClientBatchGetDeploymentInstancesResponseinstancesSummarylifecycleEventsdiagnosticsTypeDef",
    {"errorCode": str, "scriptName": str, "message": str, "logTail": str},
    total=False,
)


class ClientBatchGetDeploymentInstancesResponseinstancesSummarylifecycleEventsdiagnosticsTypeDef(
    _ClientBatchGetDeploymentInstancesResponseinstancesSummarylifecycleEventsdiagnosticsTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentInstancesResponseinstancesSummarylifecycleEvents` `diagnostics`

    Diagnostic information about the deployment lifecycle event.

    - **errorCode** *(string) --*

      The associated error code:

      * Success: The specified script ran.

      * ScriptMissing: The specified script was not found in the specified location.

      * ScriptNotExecutable: The specified script is not a recognized executable file
      type.

      * ScriptTimedOut: The specified script did not finish running in the specified time
      period.

      * ScriptFailed: The specified script failed to run as expected.

      * UnknownError: The specified script did not run for an unknown reason.

    - **scriptName** *(string) --*

      The name of the script.

    - **message** *(string) --*

      The message associated with the error.

    - **logTail** *(string) --*

      The last portion of the diagnostic log.

      If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.
    """


_ClientBatchGetDeploymentInstancesResponseinstancesSummarylifecycleEventsTypeDef = TypedDict(
    "_ClientBatchGetDeploymentInstancesResponseinstancesSummarylifecycleEventsTypeDef",
    {
        "lifecycleEventName": str,
        "diagnostics": ClientBatchGetDeploymentInstancesResponseinstancesSummarylifecycleEventsdiagnosticsTypeDef,
        "startTime": datetime,
        "endTime": datetime,
        "status": str,
    },
    total=False,
)


class ClientBatchGetDeploymentInstancesResponseinstancesSummarylifecycleEventsTypeDef(
    _ClientBatchGetDeploymentInstancesResponseinstancesSummarylifecycleEventsTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentInstancesResponseinstancesSummary` `lifecycleEvents`

    Information about a deployment lifecycle event.

    - **lifecycleEventName** *(string) --*

      The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
      AfterInstall, ApplicationStart, or ValidateService.

    - **diagnostics** *(dict) --*

      Diagnostic information about the deployment lifecycle event.

      - **errorCode** *(string) --*

        The associated error code:

        * Success: The specified script ran.

        * ScriptMissing: The specified script was not found in the specified location.

        * ScriptNotExecutable: The specified script is not a recognized executable file
        type.

        * ScriptTimedOut: The specified script did not finish running in the specified time
        period.

        * ScriptFailed: The specified script failed to run as expected.

        * UnknownError: The specified script did not run for an unknown reason.

      - **scriptName** *(string) --*

        The name of the script.

      - **message** *(string) --*

        The message associated with the error.

      - **logTail** *(string) --*

        The last portion of the diagnostic log.

        If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.

    - **startTime** *(datetime) --*

      A timestamp that indicates when the deployment lifecycle event started.

    - **endTime** *(datetime) --*

      A timestamp that indicates when the deployment lifecycle event ended.

    - **status** *(string) --*

      The deployment lifecycle event status:

      * Pending: The deployment lifecycle event is pending.

      * InProgress: The deployment lifecycle event is in progress.

      * Succeeded: The deployment lifecycle event ran successfully.

      * Failed: The deployment lifecycle event has failed.

      * Skipped: The deployment lifecycle event has been skipped.

      * Unknown: The deployment lifecycle event is unknown.
    """


_ClientBatchGetDeploymentInstancesResponseinstancesSummaryTypeDef = TypedDict(
    "_ClientBatchGetDeploymentInstancesResponseinstancesSummaryTypeDef",
    {
        "deploymentId": str,
        "instanceId": str,
        "status": str,
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List[
            ClientBatchGetDeploymentInstancesResponseinstancesSummarylifecycleEventsTypeDef
        ],
        "instanceType": str,
    },
    total=False,
)


class ClientBatchGetDeploymentInstancesResponseinstancesSummaryTypeDef(
    _ClientBatchGetDeploymentInstancesResponseinstancesSummaryTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentInstancesResponse` `instancesSummary`

    Information about an instance in a deployment.

    - **deploymentId** *(string) --*

      The unique ID of a deployment.

    - **instanceId** *(string) --*

      The instance ID.

    - **status** *(string) --*

      The deployment status for this instance:

      * Pending: The deployment is pending for this instance.

      * In Progress: The deployment is in progress for this instance.

      * Succeeded: The deployment has succeeded for this instance.

      * Failed: The deployment has failed for this instance.

      * Skipped: The deployment has been skipped for this instance.

      * Unknown: The deployment status is unknown for this instance.

    - **lastUpdatedAt** *(datetime) --*

      A timestamp that indicaties when the instance information was last updated.

    - **lifecycleEvents** *(list) --*

      A list of lifecycle events for this instance.

      - *(dict) --*

        Information about a deployment lifecycle event.

        - **lifecycleEventName** *(string) --*

          The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
          AfterInstall, ApplicationStart, or ValidateService.

        - **diagnostics** *(dict) --*

          Diagnostic information about the deployment lifecycle event.

          - **errorCode** *(string) --*

            The associated error code:

            * Success: The specified script ran.

            * ScriptMissing: The specified script was not found in the specified location.

            * ScriptNotExecutable: The specified script is not a recognized executable file
            type.

            * ScriptTimedOut: The specified script did not finish running in the specified time
            period.

            * ScriptFailed: The specified script failed to run as expected.

            * UnknownError: The specified script did not run for an unknown reason.

          - **scriptName** *(string) --*

            The name of the script.

          - **message** *(string) --*

            The message associated with the error.

          - **logTail** *(string) --*

            The last portion of the diagnostic log.

            If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.

        - **startTime** *(datetime) --*

          A timestamp that indicates when the deployment lifecycle event started.

        - **endTime** *(datetime) --*

          A timestamp that indicates when the deployment lifecycle event ended.

        - **status** *(string) --*

          The deployment lifecycle event status:

          * Pending: The deployment lifecycle event is pending.

          * InProgress: The deployment lifecycle event is in progress.

          * Succeeded: The deployment lifecycle event ran successfully.

          * Failed: The deployment lifecycle event has failed.

          * Skipped: The deployment lifecycle event has been skipped.

          * Unknown: The deployment lifecycle event is unknown.

    - **instanceType** *(string) --*

      Information about which environment an instance belongs to in a blue/green deployment.

      * BLUE: The instance is part of the original environment.

      * GREEN: The instance is part of the replacement environment.
    """


_ClientBatchGetDeploymentInstancesResponseTypeDef = TypedDict(
    "_ClientBatchGetDeploymentInstancesResponseTypeDef",
    {
        "instancesSummary": List[
            ClientBatchGetDeploymentInstancesResponseinstancesSummaryTypeDef
        ],
        "errorMessage": str,
    },
    total=False,
)


class ClientBatchGetDeploymentInstancesResponseTypeDef(
    _ClientBatchGetDeploymentInstancesResponseTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentInstances` `Response`

    Represents the output of a BatchGetDeploymentInstances operation.

    - **instancesSummary** *(list) --*

      Information about the instance.

      - *(dict) --*

        Information about an instance in a deployment.

        - **deploymentId** *(string) --*

          The unique ID of a deployment.

        - **instanceId** *(string) --*

          The instance ID.

        - **status** *(string) --*

          The deployment status for this instance:

          * Pending: The deployment is pending for this instance.

          * In Progress: The deployment is in progress for this instance.

          * Succeeded: The deployment has succeeded for this instance.

          * Failed: The deployment has failed for this instance.

          * Skipped: The deployment has been skipped for this instance.

          * Unknown: The deployment status is unknown for this instance.

        - **lastUpdatedAt** *(datetime) --*

          A timestamp that indicaties when the instance information was last updated.

        - **lifecycleEvents** *(list) --*

          A list of lifecycle events for this instance.

          - *(dict) --*

            Information about a deployment lifecycle event.

            - **lifecycleEventName** *(string) --*

              The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
              AfterInstall, ApplicationStart, or ValidateService.

            - **diagnostics** *(dict) --*

              Diagnostic information about the deployment lifecycle event.

              - **errorCode** *(string) --*

                The associated error code:

                * Success: The specified script ran.

                * ScriptMissing: The specified script was not found in the specified location.

                * ScriptNotExecutable: The specified script is not a recognized executable file
                type.

                * ScriptTimedOut: The specified script did not finish running in the specified time
                period.

                * ScriptFailed: The specified script failed to run as expected.

                * UnknownError: The specified script did not run for an unknown reason.

              - **scriptName** *(string) --*

                The name of the script.

              - **message** *(string) --*

                The message associated with the error.

              - **logTail** *(string) --*

                The last portion of the diagnostic log.

                If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.

            - **startTime** *(datetime) --*

              A timestamp that indicates when the deployment lifecycle event started.

            - **endTime** *(datetime) --*

              A timestamp that indicates when the deployment lifecycle event ended.

            - **status** *(string) --*

              The deployment lifecycle event status:

              * Pending: The deployment lifecycle event is pending.

              * InProgress: The deployment lifecycle event is in progress.

              * Succeeded: The deployment lifecycle event ran successfully.

              * Failed: The deployment lifecycle event has failed.

              * Skipped: The deployment lifecycle event has been skipped.

              * Unknown: The deployment lifecycle event is unknown.

        - **instanceType** *(string) --*

          Information about which environment an instance belongs to in a blue/green deployment.

          * BLUE: The instance is part of the original environment.

          * GREEN: The instance is part of the replacement environment.

    - **errorMessage** *(string) --*

      Information about errors that might have occurred during the API call.
    """


_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetlifecycleEventsdiagnosticsTypeDef = TypedDict(
    "_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetlifecycleEventsdiagnosticsTypeDef",
    {"errorCode": str, "scriptName": str, "message": str, "logTail": str},
    total=False,
)


class ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetlifecycleEventsdiagnosticsTypeDef(
    _ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetlifecycleEventsdiagnosticsTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetlifecycleEvents` `diagnostics`

    Diagnostic information about the deployment lifecycle event.

    - **errorCode** *(string) --*

      The associated error code:

      * Success: The specified script ran.

      * ScriptMissing: The specified script was not found in the specified location.

      * ScriptNotExecutable: The specified script is not a recognized executable file
      type.

      * ScriptTimedOut: The specified script did not finish running in the specified
      time period.

      * ScriptFailed: The specified script failed to run as expected.

      * UnknownError: The specified script did not run for an unknown reason.

    - **scriptName** *(string) --*

      The name of the script.

    - **message** *(string) --*

      The message associated with the error.

    - **logTail** *(string) --*

      The last portion of the diagnostic log.

      If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.
    """


_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetlifecycleEventsTypeDef = TypedDict(
    "_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetlifecycleEventsTypeDef",
    {
        "lifecycleEventName": str,
        "diagnostics": ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetlifecycleEventsdiagnosticsTypeDef,
        "startTime": datetime,
        "endTime": datetime,
        "status": str,
    },
    total=False,
)


class ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetlifecycleEventsTypeDef(
    _ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetlifecycleEventsTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTarget` `lifecycleEvents`

    Information about a deployment lifecycle event.

    - **lifecycleEventName** *(string) --*

      The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
      AfterInstall, ApplicationStart, or ValidateService.

    - **diagnostics** *(dict) --*

      Diagnostic information about the deployment lifecycle event.

      - **errorCode** *(string) --*

        The associated error code:

        * Success: The specified script ran.

        * ScriptMissing: The specified script was not found in the specified location.

        * ScriptNotExecutable: The specified script is not a recognized executable file
        type.

        * ScriptTimedOut: The specified script did not finish running in the specified
        time period.

        * ScriptFailed: The specified script failed to run as expected.

        * UnknownError: The specified script did not run for an unknown reason.

      - **scriptName** *(string) --*

        The name of the script.

      - **message** *(string) --*

        The message associated with the error.

      - **logTail** *(string) --*

        The last portion of the diagnostic log.

        If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.

    - **startTime** *(datetime) --*

      A timestamp that indicates when the deployment lifecycle event started.

    - **endTime** *(datetime) --*

      A timestamp that indicates when the deployment lifecycle event ended.

    - **status** *(string) --*

      The deployment lifecycle event status:

      * Pending: The deployment lifecycle event is pending.

      * InProgress: The deployment lifecycle event is in progress.

      * Succeeded: The deployment lifecycle event ran successfully.

      * Failed: The deployment lifecycle event has failed.

      * Skipped: The deployment lifecycle event has been skipped.

      * Unknown: The deployment lifecycle event is unknown.
    """


_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargettaskSetsInfotargetGroupTypeDef = TypedDict(
    "_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargettaskSetsInfotargetGroupTypeDef",
    {"name": str},
    total=False,
)


class ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargettaskSetsInfotargetGroupTypeDef(
    _ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargettaskSetsInfotargetGroupTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargettaskSetsInfo` `targetGroup`

    The target group associated with the task set. The target group is used by AWS
    CodeDeploy to manage traffic to a task set.

    - **name** *(string) --*

      For blue/green deployments, the name of the target group that instances in the
      original environment are deregistered from, and instances in the replacement
      environment are registered with. For in-place deployments, the name of the target
      group that instances are deregistered from, so they are not serving traffic
      during a deployment, and then re-registered with after the deployment is complete.
    """


_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargettaskSetsInfoTypeDef = TypedDict(
    "_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargettaskSetsInfoTypeDef",
    {
        "identifer": str,
        "desiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "status": str,
        "trafficWeight": float,
        "targetGroup": ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargettaskSetsInfotargetGroupTypeDef,
        "taskSetLabel": str,
    },
    total=False,
)


class ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargettaskSetsInfoTypeDef(
    _ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargettaskSetsInfoTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTarget` `taskSetsInfo`

    Information about a set of Amazon ECS tasks in an AWS CodeDeploy deployment. An
    Amazon ECS task set includes details such as the desired number of tasks, how many
    tasks are running, and whether the task set serves production traffic. An AWS
    CodeDeploy application that uses the Amazon ECS compute platform deploys a
    containerized application in an Amazon ECS service as a task set.

    - **identifer** *(string) --*

      A unique ID of an ``ECSTaskSet`` .

    - **desiredCount** *(integer) --*

      The number of tasks in a task set. During a deployment that uses the Amazon ECS
      compute type, CodeDeploy instructs Amazon ECS to create a new task set and uses
      this value to determine how many tasks to create. After the updated task set is
      created, CodeDeploy shifts traffic to the new task set.

    - **pendingCount** *(integer) --*

      The number of tasks in the task set that are in the ``PENDING`` status during an
      Amazon ECS deployment. A task in the ``PENDING`` state is preparing to enter the
      ``RUNNING`` state. A task set enters the ``PENDING`` status when it launches for
      the first time, or when it is restarted after being in the ``STOPPED`` state.

    - **runningCount** *(integer) --*

      The number of tasks in the task set that are in the ``RUNNING`` status during an
      Amazon ECS deployment. A task in the ``RUNNING`` state is running and ready for use.

    - **status** *(string) --*

      The status of the task set. There are three valid task set statuses:

      * ``PRIMARY`` : Indicates the task set is serving production traffic.

      * ``ACTIVE`` : Indicates the task set is not serving production traffic.

      * ``DRAINING`` : Indicates the tasks in the task set are being stopped and their
      corresponding targets are being deregistered from their target group.

    - **trafficWeight** *(float) --*

      The percentage of traffic served by this task set.

    - **targetGroup** *(dict) --*

      The target group associated with the task set. The target group is used by AWS
      CodeDeploy to manage traffic to a task set.

      - **name** *(string) --*

        For blue/green deployments, the name of the target group that instances in the
        original environment are deregistered from, and instances in the replacement
        environment are registered with. For in-place deployments, the name of the target
        group that instances are deregistered from, so they are not serving traffic
        during a deployment, and then re-registered with after the deployment is complete.

    - **taskSetLabel** *(string) --*

      A label that identifies whether the ECS task set is an original target (``BLUE`` )
      or a replacement target (``GREEN`` ).
    """


_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetTypeDef = TypedDict(
    "_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
        "targetArn": str,
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List[
            ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetlifecycleEventsTypeDef
        ],
        "status": str,
        "taskSetsInfo": List[
            ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargettaskSetsInfoTypeDef
        ],
    },
    total=False,
)


class ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetTypeDef(
    _ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentTargetsResponsedeploymentTargets` `ecsTarget`

    Information about the target for a deployment that uses the Amazon ECS compute platform.

    - **deploymentId** *(string) --*

      The unique ID of a deployment.

    - **targetId** *(string) --*

      The unique ID of a deployment target that has a type of ``ecsTarget`` .

    - **targetArn** *(string) --*

      The ARN of the target.

    - **lastUpdatedAt** *(datetime) --*

      The date and time when the target Amazon ECS application was updated by a deployment.

    - **lifecycleEvents** *(list) --*

      The lifecycle events of the deployment to this target Amazon ECS application.

      - *(dict) --*

        Information about a deployment lifecycle event.

        - **lifecycleEventName** *(string) --*

          The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
          AfterInstall, ApplicationStart, or ValidateService.

        - **diagnostics** *(dict) --*

          Diagnostic information about the deployment lifecycle event.

          - **errorCode** *(string) --*

            The associated error code:

            * Success: The specified script ran.

            * ScriptMissing: The specified script was not found in the specified location.

            * ScriptNotExecutable: The specified script is not a recognized executable file
            type.

            * ScriptTimedOut: The specified script did not finish running in the specified
            time period.

            * ScriptFailed: The specified script failed to run as expected.

            * UnknownError: The specified script did not run for an unknown reason.

          - **scriptName** *(string) --*

            The name of the script.

          - **message** *(string) --*

            The message associated with the error.

          - **logTail** *(string) --*

            The last portion of the diagnostic log.

            If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.

        - **startTime** *(datetime) --*

          A timestamp that indicates when the deployment lifecycle event started.

        - **endTime** *(datetime) --*

          A timestamp that indicates when the deployment lifecycle event ended.

        - **status** *(string) --*

          The deployment lifecycle event status:

          * Pending: The deployment lifecycle event is pending.

          * InProgress: The deployment lifecycle event is in progress.

          * Succeeded: The deployment lifecycle event ran successfully.

          * Failed: The deployment lifecycle event has failed.

          * Skipped: The deployment lifecycle event has been skipped.

          * Unknown: The deployment lifecycle event is unknown.

    - **status** *(string) --*

      The status an Amazon ECS deployment's target ECS application.

    - **taskSetsInfo** *(list) --*

      The ``ECSTaskSet`` objects associated with the ECS target.

      - *(dict) --*

        Information about a set of Amazon ECS tasks in an AWS CodeDeploy deployment. An
        Amazon ECS task set includes details such as the desired number of tasks, how many
        tasks are running, and whether the task set serves production traffic. An AWS
        CodeDeploy application that uses the Amazon ECS compute platform deploys a
        containerized application in an Amazon ECS service as a task set.

        - **identifer** *(string) --*

          A unique ID of an ``ECSTaskSet`` .

        - **desiredCount** *(integer) --*

          The number of tasks in a task set. During a deployment that uses the Amazon ECS
          compute type, CodeDeploy instructs Amazon ECS to create a new task set and uses
          this value to determine how many tasks to create. After the updated task set is
          created, CodeDeploy shifts traffic to the new task set.

        - **pendingCount** *(integer) --*

          The number of tasks in the task set that are in the ``PENDING`` status during an
          Amazon ECS deployment. A task in the ``PENDING`` state is preparing to enter the
          ``RUNNING`` state. A task set enters the ``PENDING`` status when it launches for
          the first time, or when it is restarted after being in the ``STOPPED`` state.

        - **runningCount** *(integer) --*

          The number of tasks in the task set that are in the ``RUNNING`` status during an
          Amazon ECS deployment. A task in the ``RUNNING`` state is running and ready for use.

        - **status** *(string) --*

          The status of the task set. There are three valid task set statuses:

          * ``PRIMARY`` : Indicates the task set is serving production traffic.

          * ``ACTIVE`` : Indicates the task set is not serving production traffic.

          * ``DRAINING`` : Indicates the tasks in the task set are being stopped and their
          corresponding targets are being deregistered from their target group.

        - **trafficWeight** *(float) --*

          The percentage of traffic served by this task set.

        - **targetGroup** *(dict) --*

          The target group associated with the task set. The target group is used by AWS
          CodeDeploy to manage traffic to a task set.

          - **name** *(string) --*

            For blue/green deployments, the name of the target group that instances in the
            original environment are deregistered from, and instances in the replacement
            environment are registered with. For in-place deployments, the name of the target
            group that instances are deregistered from, so they are not serving traffic
            during a deployment, and then re-registered with after the deployment is complete.

        - **taskSetLabel** *(string) --*

          A label that identifies whether the ECS task set is an original target (``BLUE`` )
          or a replacement target (``GREEN`` ).
    """


_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetlifecycleEventsdiagnosticsTypeDef = TypedDict(
    "_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetlifecycleEventsdiagnosticsTypeDef",
    {"errorCode": str, "scriptName": str, "message": str, "logTail": str},
    total=False,
)


class ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetlifecycleEventsdiagnosticsTypeDef(
    _ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetlifecycleEventsdiagnosticsTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetlifecycleEvents` `diagnostics`

    Diagnostic information about the deployment lifecycle event.

    - **errorCode** *(string) --*

      The associated error code:

      * Success: The specified script ran.

      * ScriptMissing: The specified script was not found in the specified location.

      * ScriptNotExecutable: The specified script is not a recognized executable file
      type.

      * ScriptTimedOut: The specified script did not finish running in the specified
      time period.

      * ScriptFailed: The specified script failed to run as expected.

      * UnknownError: The specified script did not run for an unknown reason.

    - **scriptName** *(string) --*

      The name of the script.

    - **message** *(string) --*

      The message associated with the error.

    - **logTail** *(string) --*

      The last portion of the diagnostic log.

      If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.
    """


_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetlifecycleEventsTypeDef = TypedDict(
    "_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetlifecycleEventsTypeDef",
    {
        "lifecycleEventName": str,
        "diagnostics": ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetlifecycleEventsdiagnosticsTypeDef,
        "startTime": datetime,
        "endTime": datetime,
        "status": str,
    },
    total=False,
)


class ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetlifecycleEventsTypeDef(
    _ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetlifecycleEventsTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTarget` `lifecycleEvents`

    Information about a deployment lifecycle event.

    - **lifecycleEventName** *(string) --*

      The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
      AfterInstall, ApplicationStart, or ValidateService.

    - **diagnostics** *(dict) --*

      Diagnostic information about the deployment lifecycle event.

      - **errorCode** *(string) --*

        The associated error code:

        * Success: The specified script ran.

        * ScriptMissing: The specified script was not found in the specified location.

        * ScriptNotExecutable: The specified script is not a recognized executable file
        type.

        * ScriptTimedOut: The specified script did not finish running in the specified
        time period.

        * ScriptFailed: The specified script failed to run as expected.

        * UnknownError: The specified script did not run for an unknown reason.

      - **scriptName** *(string) --*

        The name of the script.

      - **message** *(string) --*

        The message associated with the error.

      - **logTail** *(string) --*

        The last portion of the diagnostic log.

        If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.

    - **startTime** *(datetime) --*

      A timestamp that indicates when the deployment lifecycle event started.

    - **endTime** *(datetime) --*

      A timestamp that indicates when the deployment lifecycle event ended.

    - **status** *(string) --*

      The deployment lifecycle event status:

      * Pending: The deployment lifecycle event is pending.

      * InProgress: The deployment lifecycle event is in progress.

      * Succeeded: The deployment lifecycle event ran successfully.

      * Failed: The deployment lifecycle event has failed.

      * Skipped: The deployment lifecycle event has been skipped.

      * Unknown: The deployment lifecycle event is unknown.
    """


_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetTypeDef = TypedDict(
    "_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
        "targetArn": str,
        "status": str,
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List[
            ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetlifecycleEventsTypeDef
        ],
        "instanceLabel": str,
    },
    total=False,
)


class ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetTypeDef(
    _ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentTargetsResponsedeploymentTargets` `instanceTarget`

    Information about the target for a deployment that uses the EC2/On-premises compute
    platform.

    - **deploymentId** *(string) --*

      The unique ID of a deployment.

    - **targetId** *(string) --*

      The unique ID of a deployment target that has a type of ``instanceTarget`` .

    - **targetArn** *(string) --*

      The ARN of the target.

    - **status** *(string) --*

      The status an EC2/On-premises deployment's target instance.

    - **lastUpdatedAt** *(datetime) --*

      The date and time when the target instance was updated by a deployment.

    - **lifecycleEvents** *(list) --*

      The lifecycle events of the deployment to this target instance.

      - *(dict) --*

        Information about a deployment lifecycle event.

        - **lifecycleEventName** *(string) --*

          The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
          AfterInstall, ApplicationStart, or ValidateService.

        - **diagnostics** *(dict) --*

          Diagnostic information about the deployment lifecycle event.

          - **errorCode** *(string) --*

            The associated error code:

            * Success: The specified script ran.

            * ScriptMissing: The specified script was not found in the specified location.

            * ScriptNotExecutable: The specified script is not a recognized executable file
            type.

            * ScriptTimedOut: The specified script did not finish running in the specified
            time period.

            * ScriptFailed: The specified script failed to run as expected.

            * UnknownError: The specified script did not run for an unknown reason.

          - **scriptName** *(string) --*

            The name of the script.

          - **message** *(string) --*

            The message associated with the error.

          - **logTail** *(string) --*

            The last portion of the diagnostic log.

            If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.

        - **startTime** *(datetime) --*

          A timestamp that indicates when the deployment lifecycle event started.

        - **endTime** *(datetime) --*

          A timestamp that indicates when the deployment lifecycle event ended.

        - **status** *(string) --*

          The deployment lifecycle event status:

          * Pending: The deployment lifecycle event is pending.

          * InProgress: The deployment lifecycle event is in progress.

          * Succeeded: The deployment lifecycle event ran successfully.

          * Failed: The deployment lifecycle event has failed.

          * Skipped: The deployment lifecycle event has been skipped.

          * Unknown: The deployment lifecycle event is unknown.

    - **instanceLabel** *(string) --*

      A label that identifies whether the instance is an original target (``BLUE`` ) or a
      replacement target (``GREEN`` ).
    """


_ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlambdaFunctionInfoTypeDef = TypedDict(
    "_ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlambdaFunctionInfoTypeDef",
    {
        "functionName": str,
        "functionAlias": str,
        "currentVersion": str,
        "targetVersion": str,
        "targetVersionWeight": float,
    },
    total=False,
)


class ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlambdaFunctionInfoTypeDef(
    _ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlambdaFunctionInfoTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTarget` `lambdaFunctionInfo`

    A ``LambdaFunctionInfo`` object that describes a target Lambda function.

    - **functionName** *(string) --*

      The name of a Lambda function.

    - **functionAlias** *(string) --*

      The alias of a Lambda function. For more information, see `Introduction to AWS Lambda
      Aliases <https://docs.aws.amazon.com/lambda/latest/dg/aliases-intro.html>`__ .

    - **currentVersion** *(string) --*

      The version of a Lambda function that production traffic points to.

    - **targetVersion** *(string) --*

      The version of a Lambda function that production traffic points to after the Lambda
      function is deployed.

    - **targetVersionWeight** *(float) --*

      The percentage of production traffic that the target version of a Lambda function
      receives.
    """


_ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlifecycleEventsdiagnosticsTypeDef = TypedDict(
    "_ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlifecycleEventsdiagnosticsTypeDef",
    {"errorCode": str, "scriptName": str, "message": str, "logTail": str},
    total=False,
)


class ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlifecycleEventsdiagnosticsTypeDef(
    _ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlifecycleEventsdiagnosticsTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlifecycleEvents` `diagnostics`

    Diagnostic information about the deployment lifecycle event.

    - **errorCode** *(string) --*

      The associated error code:

      * Success: The specified script ran.

      * ScriptMissing: The specified script was not found in the specified location.

      * ScriptNotExecutable: The specified script is not a recognized executable file
      type.

      * ScriptTimedOut: The specified script did not finish running in the specified
      time period.

      * ScriptFailed: The specified script failed to run as expected.

      * UnknownError: The specified script did not run for an unknown reason.

    - **scriptName** *(string) --*

      The name of the script.

    - **message** *(string) --*

      The message associated with the error.

    - **logTail** *(string) --*

      The last portion of the diagnostic log.

      If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.
    """


_ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlifecycleEventsTypeDef = TypedDict(
    "_ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlifecycleEventsTypeDef",
    {
        "lifecycleEventName": str,
        "diagnostics": ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlifecycleEventsdiagnosticsTypeDef,
        "startTime": datetime,
        "endTime": datetime,
        "status": str,
    },
    total=False,
)


class ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlifecycleEventsTypeDef(
    _ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlifecycleEventsTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTarget` `lifecycleEvents`

    Information about a deployment lifecycle event.

    - **lifecycleEventName** *(string) --*

      The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
      AfterInstall, ApplicationStart, or ValidateService.

    - **diagnostics** *(dict) --*

      Diagnostic information about the deployment lifecycle event.

      - **errorCode** *(string) --*

        The associated error code:

        * Success: The specified script ran.

        * ScriptMissing: The specified script was not found in the specified location.

        * ScriptNotExecutable: The specified script is not a recognized executable file
        type.

        * ScriptTimedOut: The specified script did not finish running in the specified
        time period.

        * ScriptFailed: The specified script failed to run as expected.

        * UnknownError: The specified script did not run for an unknown reason.

      - **scriptName** *(string) --*

        The name of the script.

      - **message** *(string) --*

        The message associated with the error.

      - **logTail** *(string) --*

        The last portion of the diagnostic log.

        If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.

    - **startTime** *(datetime) --*

      A timestamp that indicates when the deployment lifecycle event started.

    - **endTime** *(datetime) --*

      A timestamp that indicates when the deployment lifecycle event ended.

    - **status** *(string) --*

      The deployment lifecycle event status:

      * Pending: The deployment lifecycle event is pending.

      * InProgress: The deployment lifecycle event is in progress.

      * Succeeded: The deployment lifecycle event ran successfully.

      * Failed: The deployment lifecycle event has failed.

      * Skipped: The deployment lifecycle event has been skipped.

      * Unknown: The deployment lifecycle event is unknown.
    """


_ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetTypeDef = TypedDict(
    "_ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
        "targetArn": str,
        "status": str,
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List[
            ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlifecycleEventsTypeDef
        ],
        "lambdaFunctionInfo": ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlambdaFunctionInfoTypeDef,
    },
    total=False,
)


class ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetTypeDef(
    _ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentTargetsResponsedeploymentTargets` `lambdaTarget`

    Information about the target for a deployment that uses the AWS Lambda compute platform.

    - **deploymentId** *(string) --*

      The unique ID of a deployment.

    - **targetId** *(string) --*

      The unique ID of a deployment target that has a type of ``lambdaTarget`` .

    - **targetArn** *(string) --*

      The ARN of the target.

    - **status** *(string) --*

      The status an AWS Lambda deployment's target Lambda function.

    - **lastUpdatedAt** *(datetime) --*

      The date and time when the target Lambda function was updated by a deployment.

    - **lifecycleEvents** *(list) --*

      The lifecycle events of the deployment to this target Lambda function.

      - *(dict) --*

        Information about a deployment lifecycle event.

        - **lifecycleEventName** *(string) --*

          The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
          AfterInstall, ApplicationStart, or ValidateService.

        - **diagnostics** *(dict) --*

          Diagnostic information about the deployment lifecycle event.

          - **errorCode** *(string) --*

            The associated error code:

            * Success: The specified script ran.

            * ScriptMissing: The specified script was not found in the specified location.

            * ScriptNotExecutable: The specified script is not a recognized executable file
            type.

            * ScriptTimedOut: The specified script did not finish running in the specified
            time period.

            * ScriptFailed: The specified script failed to run as expected.

            * UnknownError: The specified script did not run for an unknown reason.

          - **scriptName** *(string) --*

            The name of the script.

          - **message** *(string) --*

            The message associated with the error.

          - **logTail** *(string) --*

            The last portion of the diagnostic log.

            If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.

        - **startTime** *(datetime) --*

          A timestamp that indicates when the deployment lifecycle event started.

        - **endTime** *(datetime) --*

          A timestamp that indicates when the deployment lifecycle event ended.

        - **status** *(string) --*

          The deployment lifecycle event status:

          * Pending: The deployment lifecycle event is pending.

          * InProgress: The deployment lifecycle event is in progress.

          * Succeeded: The deployment lifecycle event ran successfully.

          * Failed: The deployment lifecycle event has failed.

          * Skipped: The deployment lifecycle event has been skipped.

          * Unknown: The deployment lifecycle event is unknown.

    - **lambdaFunctionInfo** *(dict) --*

      A ``LambdaFunctionInfo`` object that describes a target Lambda function.

      - **functionName** *(string) --*

        The name of a Lambda function.

      - **functionAlias** *(string) --*

        The alias of a Lambda function. For more information, see `Introduction to AWS Lambda
        Aliases <https://docs.aws.amazon.com/lambda/latest/dg/aliases-intro.html>`__ .

      - **currentVersion** *(string) --*

        The version of a Lambda function that production traffic points to.

      - **targetVersion** *(string) --*

        The version of a Lambda function that production traffic points to after the Lambda
        function is deployed.

      - **targetVersionWeight** *(float) --*

        The percentage of production traffic that the target version of a Lambda function
        receives.
    """


_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsTypeDef = TypedDict(
    "_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsTypeDef",
    {
        "deploymentTargetType": str,
        "instanceTarget": ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetTypeDef,
        "lambdaTarget": ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetTypeDef,
        "ecsTarget": ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetTypeDef,
    },
    total=False,
)


class ClientBatchGetDeploymentTargetsResponsedeploymentTargetsTypeDef(
    _ClientBatchGetDeploymentTargetsResponsedeploymentTargetsTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentTargetsResponse` `deploymentTargets`

    Information about the deployment target.

    - **deploymentTargetType** *(string) --*

      The deployment type that is specific to the deployment's compute platform.

    - **instanceTarget** *(dict) --*

      Information about the target for a deployment that uses the EC2/On-premises compute
      platform.

      - **deploymentId** *(string) --*

        The unique ID of a deployment.

      - **targetId** *(string) --*

        The unique ID of a deployment target that has a type of ``instanceTarget`` .

      - **targetArn** *(string) --*

        The ARN of the target.

      - **status** *(string) --*

        The status an EC2/On-premises deployment's target instance.

      - **lastUpdatedAt** *(datetime) --*

        The date and time when the target instance was updated by a deployment.

      - **lifecycleEvents** *(list) --*

        The lifecycle events of the deployment to this target instance.

        - *(dict) --*

          Information about a deployment lifecycle event.

          - **lifecycleEventName** *(string) --*

            The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
            AfterInstall, ApplicationStart, or ValidateService.

          - **diagnostics** *(dict) --*

            Diagnostic information about the deployment lifecycle event.

            - **errorCode** *(string) --*

              The associated error code:

              * Success: The specified script ran.

              * ScriptMissing: The specified script was not found in the specified location.

              * ScriptNotExecutable: The specified script is not a recognized executable file
              type.

              * ScriptTimedOut: The specified script did not finish running in the specified
              time period.

              * ScriptFailed: The specified script failed to run as expected.

              * UnknownError: The specified script did not run for an unknown reason.

            - **scriptName** *(string) --*

              The name of the script.

            - **message** *(string) --*

              The message associated with the error.

            - **logTail** *(string) --*

              The last portion of the diagnostic log.

              If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.

          - **startTime** *(datetime) --*

            A timestamp that indicates when the deployment lifecycle event started.

          - **endTime** *(datetime) --*

            A timestamp that indicates when the deployment lifecycle event ended.

          - **status** *(string) --*

            The deployment lifecycle event status:

            * Pending: The deployment lifecycle event is pending.

            * InProgress: The deployment lifecycle event is in progress.

            * Succeeded: The deployment lifecycle event ran successfully.

            * Failed: The deployment lifecycle event has failed.

            * Skipped: The deployment lifecycle event has been skipped.

            * Unknown: The deployment lifecycle event is unknown.

      - **instanceLabel** *(string) --*

        A label that identifies whether the instance is an original target (``BLUE`` ) or a
        replacement target (``GREEN`` ).

    - **lambdaTarget** *(dict) --*

      Information about the target for a deployment that uses the AWS Lambda compute platform.

      - **deploymentId** *(string) --*

        The unique ID of a deployment.

      - **targetId** *(string) --*

        The unique ID of a deployment target that has a type of ``lambdaTarget`` .

      - **targetArn** *(string) --*

        The ARN of the target.

      - **status** *(string) --*

        The status an AWS Lambda deployment's target Lambda function.

      - **lastUpdatedAt** *(datetime) --*

        The date and time when the target Lambda function was updated by a deployment.

      - **lifecycleEvents** *(list) --*

        The lifecycle events of the deployment to this target Lambda function.

        - *(dict) --*

          Information about a deployment lifecycle event.

          - **lifecycleEventName** *(string) --*

            The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
            AfterInstall, ApplicationStart, or ValidateService.

          - **diagnostics** *(dict) --*

            Diagnostic information about the deployment lifecycle event.

            - **errorCode** *(string) --*

              The associated error code:

              * Success: The specified script ran.

              * ScriptMissing: The specified script was not found in the specified location.

              * ScriptNotExecutable: The specified script is not a recognized executable file
              type.

              * ScriptTimedOut: The specified script did not finish running in the specified
              time period.

              * ScriptFailed: The specified script failed to run as expected.

              * UnknownError: The specified script did not run for an unknown reason.

            - **scriptName** *(string) --*

              The name of the script.

            - **message** *(string) --*

              The message associated with the error.

            - **logTail** *(string) --*

              The last portion of the diagnostic log.

              If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.

          - **startTime** *(datetime) --*

            A timestamp that indicates when the deployment lifecycle event started.

          - **endTime** *(datetime) --*

            A timestamp that indicates when the deployment lifecycle event ended.

          - **status** *(string) --*

            The deployment lifecycle event status:

            * Pending: The deployment lifecycle event is pending.

            * InProgress: The deployment lifecycle event is in progress.

            * Succeeded: The deployment lifecycle event ran successfully.

            * Failed: The deployment lifecycle event has failed.

            * Skipped: The deployment lifecycle event has been skipped.

            * Unknown: The deployment lifecycle event is unknown.

      - **lambdaFunctionInfo** *(dict) --*

        A ``LambdaFunctionInfo`` object that describes a target Lambda function.

        - **functionName** *(string) --*

          The name of a Lambda function.

        - **functionAlias** *(string) --*

          The alias of a Lambda function. For more information, see `Introduction to AWS Lambda
          Aliases <https://docs.aws.amazon.com/lambda/latest/dg/aliases-intro.html>`__ .

        - **currentVersion** *(string) --*

          The version of a Lambda function that production traffic points to.

        - **targetVersion** *(string) --*

          The version of a Lambda function that production traffic points to after the Lambda
          function is deployed.

        - **targetVersionWeight** *(float) --*

          The percentage of production traffic that the target version of a Lambda function
          receives.

    - **ecsTarget** *(dict) --*

      Information about the target for a deployment that uses the Amazon ECS compute platform.

      - **deploymentId** *(string) --*

        The unique ID of a deployment.

      - **targetId** *(string) --*

        The unique ID of a deployment target that has a type of ``ecsTarget`` .

      - **targetArn** *(string) --*

        The ARN of the target.

      - **lastUpdatedAt** *(datetime) --*

        The date and time when the target Amazon ECS application was updated by a deployment.

      - **lifecycleEvents** *(list) --*

        The lifecycle events of the deployment to this target Amazon ECS application.

        - *(dict) --*

          Information about a deployment lifecycle event.

          - **lifecycleEventName** *(string) --*

            The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
            AfterInstall, ApplicationStart, or ValidateService.

          - **diagnostics** *(dict) --*

            Diagnostic information about the deployment lifecycle event.

            - **errorCode** *(string) --*

              The associated error code:

              * Success: The specified script ran.

              * ScriptMissing: The specified script was not found in the specified location.

              * ScriptNotExecutable: The specified script is not a recognized executable file
              type.

              * ScriptTimedOut: The specified script did not finish running in the specified
              time period.

              * ScriptFailed: The specified script failed to run as expected.

              * UnknownError: The specified script did not run for an unknown reason.

            - **scriptName** *(string) --*

              The name of the script.

            - **message** *(string) --*

              The message associated with the error.

            - **logTail** *(string) --*

              The last portion of the diagnostic log.

              If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.

          - **startTime** *(datetime) --*

            A timestamp that indicates when the deployment lifecycle event started.

          - **endTime** *(datetime) --*

            A timestamp that indicates when the deployment lifecycle event ended.

          - **status** *(string) --*

            The deployment lifecycle event status:

            * Pending: The deployment lifecycle event is pending.

            * InProgress: The deployment lifecycle event is in progress.

            * Succeeded: The deployment lifecycle event ran successfully.

            * Failed: The deployment lifecycle event has failed.

            * Skipped: The deployment lifecycle event has been skipped.

            * Unknown: The deployment lifecycle event is unknown.

      - **status** *(string) --*

        The status an Amazon ECS deployment's target ECS application.

      - **taskSetsInfo** *(list) --*

        The ``ECSTaskSet`` objects associated with the ECS target.

        - *(dict) --*

          Information about a set of Amazon ECS tasks in an AWS CodeDeploy deployment. An
          Amazon ECS task set includes details such as the desired number of tasks, how many
          tasks are running, and whether the task set serves production traffic. An AWS
          CodeDeploy application that uses the Amazon ECS compute platform deploys a
          containerized application in an Amazon ECS service as a task set.

          - **identifer** *(string) --*

            A unique ID of an ``ECSTaskSet`` .

          - **desiredCount** *(integer) --*

            The number of tasks in a task set. During a deployment that uses the Amazon ECS
            compute type, CodeDeploy instructs Amazon ECS to create a new task set and uses
            this value to determine how many tasks to create. After the updated task set is
            created, CodeDeploy shifts traffic to the new task set.

          - **pendingCount** *(integer) --*

            The number of tasks in the task set that are in the ``PENDING`` status during an
            Amazon ECS deployment. A task in the ``PENDING`` state is preparing to enter the
            ``RUNNING`` state. A task set enters the ``PENDING`` status when it launches for
            the first time, or when it is restarted after being in the ``STOPPED`` state.

          - **runningCount** *(integer) --*

            The number of tasks in the task set that are in the ``RUNNING`` status during an
            Amazon ECS deployment. A task in the ``RUNNING`` state is running and ready for use.

          - **status** *(string) --*

            The status of the task set. There are three valid task set statuses:

            * ``PRIMARY`` : Indicates the task set is serving production traffic.

            * ``ACTIVE`` : Indicates the task set is not serving production traffic.

            * ``DRAINING`` : Indicates the tasks in the task set are being stopped and their
            corresponding targets are being deregistered from their target group.

          - **trafficWeight** *(float) --*

            The percentage of traffic served by this task set.

          - **targetGroup** *(dict) --*

            The target group associated with the task set. The target group is used by AWS
            CodeDeploy to manage traffic to a task set.

            - **name** *(string) --*

              For blue/green deployments, the name of the target group that instances in the
              original environment are deregistered from, and instances in the replacement
              environment are registered with. For in-place deployments, the name of the target
              group that instances are deregistered from, so they are not serving traffic
              during a deployment, and then re-registered with after the deployment is complete.

          - **taskSetLabel** *(string) --*

            A label that identifies whether the ECS task set is an original target (``BLUE`` )
            or a replacement target (``GREEN`` ).
    """


_ClientBatchGetDeploymentTargetsResponseTypeDef = TypedDict(
    "_ClientBatchGetDeploymentTargetsResponseTypeDef",
    {
        "deploymentTargets": List[
            ClientBatchGetDeploymentTargetsResponsedeploymentTargetsTypeDef
        ]
    },
    total=False,
)


class ClientBatchGetDeploymentTargetsResponseTypeDef(
    _ClientBatchGetDeploymentTargetsResponseTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentTargets` `Response`

    - **deploymentTargets** *(list) --*

      A list of target objects for a deployment. Each target object contains details about the
      target, such as its status and lifecycle events. The type of the target objects depends on
      the deployment' compute platform.

      * **EC2/On-premises** : Each target object is an EC2 or on-premises instance.

      * **AWS Lambda** : The target object is a specific version of an AWS Lambda function.

      * **Amazon ECS** : The target object is an Amazon ECS service.

      - *(dict) --*

        Information about the deployment target.

        - **deploymentTargetType** *(string) --*

          The deployment type that is specific to the deployment's compute platform.

        - **instanceTarget** *(dict) --*

          Information about the target for a deployment that uses the EC2/On-premises compute
          platform.

          - **deploymentId** *(string) --*

            The unique ID of a deployment.

          - **targetId** *(string) --*

            The unique ID of a deployment target that has a type of ``instanceTarget`` .

          - **targetArn** *(string) --*

            The ARN of the target.

          - **status** *(string) --*

            The status an EC2/On-premises deployment's target instance.

          - **lastUpdatedAt** *(datetime) --*

            The date and time when the target instance was updated by a deployment.

          - **lifecycleEvents** *(list) --*

            The lifecycle events of the deployment to this target instance.

            - *(dict) --*

              Information about a deployment lifecycle event.

              - **lifecycleEventName** *(string) --*

                The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
                AfterInstall, ApplicationStart, or ValidateService.

              - **diagnostics** *(dict) --*

                Diagnostic information about the deployment lifecycle event.

                - **errorCode** *(string) --*

                  The associated error code:

                  * Success: The specified script ran.

                  * ScriptMissing: The specified script was not found in the specified location.

                  * ScriptNotExecutable: The specified script is not a recognized executable file
                  type.

                  * ScriptTimedOut: The specified script did not finish running in the specified
                  time period.

                  * ScriptFailed: The specified script failed to run as expected.

                  * UnknownError: The specified script did not run for an unknown reason.

                - **scriptName** *(string) --*

                  The name of the script.

                - **message** *(string) --*

                  The message associated with the error.

                - **logTail** *(string) --*

                  The last portion of the diagnostic log.

                  If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.

              - **startTime** *(datetime) --*

                A timestamp that indicates when the deployment lifecycle event started.

              - **endTime** *(datetime) --*

                A timestamp that indicates when the deployment lifecycle event ended.

              - **status** *(string) --*

                The deployment lifecycle event status:

                * Pending: The deployment lifecycle event is pending.

                * InProgress: The deployment lifecycle event is in progress.

                * Succeeded: The deployment lifecycle event ran successfully.

                * Failed: The deployment lifecycle event has failed.

                * Skipped: The deployment lifecycle event has been skipped.

                * Unknown: The deployment lifecycle event is unknown.

          - **instanceLabel** *(string) --*

            A label that identifies whether the instance is an original target (``BLUE`` ) or a
            replacement target (``GREEN`` ).

        - **lambdaTarget** *(dict) --*

          Information about the target for a deployment that uses the AWS Lambda compute platform.

          - **deploymentId** *(string) --*

            The unique ID of a deployment.

          - **targetId** *(string) --*

            The unique ID of a deployment target that has a type of ``lambdaTarget`` .

          - **targetArn** *(string) --*

            The ARN of the target.

          - **status** *(string) --*

            The status an AWS Lambda deployment's target Lambda function.

          - **lastUpdatedAt** *(datetime) --*

            The date and time when the target Lambda function was updated by a deployment.

          - **lifecycleEvents** *(list) --*

            The lifecycle events of the deployment to this target Lambda function.

            - *(dict) --*

              Information about a deployment lifecycle event.

              - **lifecycleEventName** *(string) --*

                The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
                AfterInstall, ApplicationStart, or ValidateService.

              - **diagnostics** *(dict) --*

                Diagnostic information about the deployment lifecycle event.

                - **errorCode** *(string) --*

                  The associated error code:

                  * Success: The specified script ran.

                  * ScriptMissing: The specified script was not found in the specified location.

                  * ScriptNotExecutable: The specified script is not a recognized executable file
                  type.

                  * ScriptTimedOut: The specified script did not finish running in the specified
                  time period.

                  * ScriptFailed: The specified script failed to run as expected.

                  * UnknownError: The specified script did not run for an unknown reason.

                - **scriptName** *(string) --*

                  The name of the script.

                - **message** *(string) --*

                  The message associated with the error.

                - **logTail** *(string) --*

                  The last portion of the diagnostic log.

                  If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.

              - **startTime** *(datetime) --*

                A timestamp that indicates when the deployment lifecycle event started.

              - **endTime** *(datetime) --*

                A timestamp that indicates when the deployment lifecycle event ended.

              - **status** *(string) --*

                The deployment lifecycle event status:

                * Pending: The deployment lifecycle event is pending.

                * InProgress: The deployment lifecycle event is in progress.

                * Succeeded: The deployment lifecycle event ran successfully.

                * Failed: The deployment lifecycle event has failed.

                * Skipped: The deployment lifecycle event has been skipped.

                * Unknown: The deployment lifecycle event is unknown.

          - **lambdaFunctionInfo** *(dict) --*

            A ``LambdaFunctionInfo`` object that describes a target Lambda function.

            - **functionName** *(string) --*

              The name of a Lambda function.

            - **functionAlias** *(string) --*

              The alias of a Lambda function. For more information, see `Introduction to AWS Lambda
              Aliases <https://docs.aws.amazon.com/lambda/latest/dg/aliases-intro.html>`__ .

            - **currentVersion** *(string) --*

              The version of a Lambda function that production traffic points to.

            - **targetVersion** *(string) --*

              The version of a Lambda function that production traffic points to after the Lambda
              function is deployed.

            - **targetVersionWeight** *(float) --*

              The percentage of production traffic that the target version of a Lambda function
              receives.

        - **ecsTarget** *(dict) --*

          Information about the target for a deployment that uses the Amazon ECS compute platform.

          - **deploymentId** *(string) --*

            The unique ID of a deployment.

          - **targetId** *(string) --*

            The unique ID of a deployment target that has a type of ``ecsTarget`` .

          - **targetArn** *(string) --*

            The ARN of the target.

          - **lastUpdatedAt** *(datetime) --*

            The date and time when the target Amazon ECS application was updated by a deployment.

          - **lifecycleEvents** *(list) --*

            The lifecycle events of the deployment to this target Amazon ECS application.

            - *(dict) --*

              Information about a deployment lifecycle event.

              - **lifecycleEventName** *(string) --*

                The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
                AfterInstall, ApplicationStart, or ValidateService.

              - **diagnostics** *(dict) --*

                Diagnostic information about the deployment lifecycle event.

                - **errorCode** *(string) --*

                  The associated error code:

                  * Success: The specified script ran.

                  * ScriptMissing: The specified script was not found in the specified location.

                  * ScriptNotExecutable: The specified script is not a recognized executable file
                  type.

                  * ScriptTimedOut: The specified script did not finish running in the specified
                  time period.

                  * ScriptFailed: The specified script failed to run as expected.

                  * UnknownError: The specified script did not run for an unknown reason.

                - **scriptName** *(string) --*

                  The name of the script.

                - **message** *(string) --*

                  The message associated with the error.

                - **logTail** *(string) --*

                  The last portion of the diagnostic log.

                  If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.

              - **startTime** *(datetime) --*

                A timestamp that indicates when the deployment lifecycle event started.

              - **endTime** *(datetime) --*

                A timestamp that indicates when the deployment lifecycle event ended.

              - **status** *(string) --*

                The deployment lifecycle event status:

                * Pending: The deployment lifecycle event is pending.

                * InProgress: The deployment lifecycle event is in progress.

                * Succeeded: The deployment lifecycle event ran successfully.

                * Failed: The deployment lifecycle event has failed.

                * Skipped: The deployment lifecycle event has been skipped.

                * Unknown: The deployment lifecycle event is unknown.

          - **status** *(string) --*

            The status an Amazon ECS deployment's target ECS application.

          - **taskSetsInfo** *(list) --*

            The ``ECSTaskSet`` objects associated with the ECS target.

            - *(dict) --*

              Information about a set of Amazon ECS tasks in an AWS CodeDeploy deployment. An
              Amazon ECS task set includes details such as the desired number of tasks, how many
              tasks are running, and whether the task set serves production traffic. An AWS
              CodeDeploy application that uses the Amazon ECS compute platform deploys a
              containerized application in an Amazon ECS service as a task set.

              - **identifer** *(string) --*

                A unique ID of an ``ECSTaskSet`` .

              - **desiredCount** *(integer) --*

                The number of tasks in a task set. During a deployment that uses the Amazon ECS
                compute type, CodeDeploy instructs Amazon ECS to create a new task set and uses
                this value to determine how many tasks to create. After the updated task set is
                created, CodeDeploy shifts traffic to the new task set.

              - **pendingCount** *(integer) --*

                The number of tasks in the task set that are in the ``PENDING`` status during an
                Amazon ECS deployment. A task in the ``PENDING`` state is preparing to enter the
                ``RUNNING`` state. A task set enters the ``PENDING`` status when it launches for
                the first time, or when it is restarted after being in the ``STOPPED`` state.

              - **runningCount** *(integer) --*

                The number of tasks in the task set that are in the ``RUNNING`` status during an
                Amazon ECS deployment. A task in the ``RUNNING`` state is running and ready for use.

              - **status** *(string) --*

                The status of the task set. There are three valid task set statuses:

                * ``PRIMARY`` : Indicates the task set is serving production traffic.

                * ``ACTIVE`` : Indicates the task set is not serving production traffic.

                * ``DRAINING`` : Indicates the tasks in the task set are being stopped and their
                corresponding targets are being deregistered from their target group.

              - **trafficWeight** *(float) --*

                The percentage of traffic served by this task set.

              - **targetGroup** *(dict) --*

                The target group associated with the task set. The target group is used by AWS
                CodeDeploy to manage traffic to a task set.

                - **name** *(string) --*

                  For blue/green deployments, the name of the target group that instances in the
                  original environment are deregistered from, and instances in the replacement
                  environment are registered with. For in-place deployments, the name of the target
                  group that instances are deregistered from, so they are not serving traffic
                  during a deployment, and then re-registered with after the deployment is complete.

              - **taskSetLabel** *(string) --*

                A label that identifies whether the ECS task set is an original target (``BLUE`` )
                or a replacement target (``GREEN`` ).
    """


_ClientBatchGetDeploymentsResponsedeploymentsInfoautoRollbackConfigurationTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfoautoRollbackConfigurationTypeDef",
    {"enabled": bool, "events": List[str]},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfoautoRollbackConfigurationTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfoautoRollbackConfigurationTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentsResponsedeploymentsInfo` `autoRollbackConfiguration`

    Information about the automatic rollback configuration associated with the deployment.

    - **enabled** *(boolean) --*

      Indicates whether a defined automatic rollback configuration is currently enabled.

    - **events** *(list) --*

      The event type or types that trigger a rollback.

      - *(string) --*
    """


_ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    {"actionOnTimeout": str, "waitTimeInMinutes": int},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfiguration` `deploymentReadyOption`

    Information about the action to take when newly provisioned instances are ready to
    receive traffic in a blue/green deployment.

    - **actionOnTimeout** *(string) --*

      Information about when to reroute traffic from an original environment to a
      replacement environment in a blue/green deployment.

      * CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately
      after the new application revision is installed on the instances in the replacement
      environment.

      * STOP_DEPLOYMENT: Do not register new instances with a load balancer unless traffic
      rerouting is started using  ContinueDeployment . If traffic rerouting is not started
      before the end of the specified wait period, the deployment status is changed to
      Stopped.

    - **waitTimeInMinutes** *(integer) --*

      The number of minutes to wait before the status of a blue/green deployment is changed
      to Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT
      option for actionOnTimeout
    """


_ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    {"action": str},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfiguration` `greenFleetProvisioningOption`

    Information about how instances are provisioned for a replacement environment in a
    blue/green deployment.

    - **action** *(string) --*

      The method used to add instances to a replacement environment.

      * DISCOVER_EXISTING: Use instances that already exist or will be created manually.

      * COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to define
      and create instances in a new Auto Scaling group.
    """


_ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    {"action": str, "terminationWaitTimeInMinutes": int},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfiguration` `terminateBlueInstancesOnDeploymentSuccess`

    Information about whether to terminate instances in the original fleet during a
    blue/green deployment.

    - **action** *(string) --*

      The action to take on instances in the original environment after a successful
      blue/green deployment.

      * TERMINATE: Instances are terminated after a specified wait time.

      * KEEP_ALIVE: Instances are left running after they are deregistered from the load
      balancer and removed from the deployment group.

    - **terminationWaitTimeInMinutes** *(integer) --*

      For an Amazon EC2 deployment, the number of minutes to wait after a successful
      blue/green deployment before terminating instances from the original environment.

      For an Amazon ECS deployment, the number of minutes before deleting the original
      (blue) task set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the
      original (blue) task set to a replacement (green) task set.

      The maximum setting is 2880 minutes (2 days).
    """


_ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationTypeDef",
    {
        "terminateBlueInstancesOnDeploymentSuccess": ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef,
        "deploymentReadyOption": ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef,
        "greenFleetProvisioningOption": ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef,
    },
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentsResponsedeploymentsInfo` `blueGreenDeploymentConfiguration`

    Information about blue/green deployment options for this deployment.

    - **terminateBlueInstancesOnDeploymentSuccess** *(dict) --*

      Information about whether to terminate instances in the original fleet during a
      blue/green deployment.

      - **action** *(string) --*

        The action to take on instances in the original environment after a successful
        blue/green deployment.

        * TERMINATE: Instances are terminated after a specified wait time.

        * KEEP_ALIVE: Instances are left running after they are deregistered from the load
        balancer and removed from the deployment group.

      - **terminationWaitTimeInMinutes** *(integer) --*

        For an Amazon EC2 deployment, the number of minutes to wait after a successful
        blue/green deployment before terminating instances from the original environment.

        For an Amazon ECS deployment, the number of minutes before deleting the original
        (blue) task set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the
        original (blue) task set to a replacement (green) task set.

        The maximum setting is 2880 minutes (2 days).

    - **deploymentReadyOption** *(dict) --*

      Information about the action to take when newly provisioned instances are ready to
      receive traffic in a blue/green deployment.

      - **actionOnTimeout** *(string) --*

        Information about when to reroute traffic from an original environment to a
        replacement environment in a blue/green deployment.

        * CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately
        after the new application revision is installed on the instances in the replacement
        environment.

        * STOP_DEPLOYMENT: Do not register new instances with a load balancer unless traffic
        rerouting is started using  ContinueDeployment . If traffic rerouting is not started
        before the end of the specified wait period, the deployment status is changed to
        Stopped.

      - **waitTimeInMinutes** *(integer) --*

        The number of minutes to wait before the status of a blue/green deployment is changed
        to Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT
        option for actionOnTimeout

    - **greenFleetProvisioningOption** *(dict) --*

      Information about how instances are provisioned for a replacement environment in a
      blue/green deployment.

      - **action** *(string) --*

        The method used to add instances to a replacement environment.

        * DISCOVER_EXISTING: Use instances that already exist or will be created manually.

        * COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to define
        and create instances in a new Auto Scaling group.
    """


_ClientBatchGetDeploymentsResponsedeploymentsInfodeploymentOverviewTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfodeploymentOverviewTypeDef",
    {
        "Pending": int,
        "InProgress": int,
        "Succeeded": int,
        "Failed": int,
        "Skipped": int,
        "Ready": int,
    },
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfodeploymentOverviewTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfodeploymentOverviewTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentsResponsedeploymentsInfo` `deploymentOverview`

    A summary of the deployment status of the instances in the deployment.

    - **Pending** *(integer) --*

      The number of instances in the deployment in a pending state.

    - **InProgress** *(integer) --*

      The number of instances in which the deployment is in progress.

    - **Succeeded** *(integer) --*

      The number of instances in the deployment to which revisions have been successfully
      deployed.

    - **Failed** *(integer) --*

      The number of instances in the deployment in a failed state.

    - **Skipped** *(integer) --*

      The number of instances in the deployment in a skipped state.

    - **Ready** *(integer) --*

      The number of instances in a replacement environment ready to receive traffic in a
      blue/green deployment.
    """


_ClientBatchGetDeploymentsResponsedeploymentsInfodeploymentStyleTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfodeploymentStyleTypeDef",
    {"deploymentType": str, "deploymentOption": str},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfodeploymentStyleTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfodeploymentStyleTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentsResponsedeploymentsInfo` `deploymentStyle`

    Information about the type of deployment, either in-place or blue/green, you want to run
    and whether to route deployment traffic behind a load balancer.

    - **deploymentType** *(string) --*

      Indicates whether to run an in-place deployment or a blue/green deployment.

    - **deploymentOption** *(string) --*

      Indicates whether to route deployment traffic behind a load balancer.
    """


_ClientBatchGetDeploymentsResponsedeploymentsInfoerrorInformationTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfoerrorInformationTypeDef",
    {"code": str, "message": str},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfoerrorInformationTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfoerrorInformationTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentsResponsedeploymentsInfo` `errorInformation`

    Information about any error associated with this deployment.

    - **code** *(string) --*

      For more information, see `Error Codes for AWS CodeDeploy
      <https://docs.aws.amazon.com/codedeploy/latest/userguide/error-codes.html>`__ in the
      `AWS CodeDeploy User Guide <https://docs.aws.amazon.com/codedeploy/latest/userguide>`__
      .

      The error code:

      * APPLICATION_MISSING: The application was missing. This error code is most likely
      raised if the application is deleted after the deployment is created, but before it is
      started.

      * DEPLOYMENT_GROUP_MISSING: The deployment group was missing. This error code is most
      likely raised if the deployment group is deleted after the deployment is created, but
      before it is started.

      * HEALTH_CONSTRAINTS: The deployment failed on too many instances to be successfully
      deployed within the instance health constraints specified.

      * HEALTH_CONSTRAINTS_INVALID: The revision cannot be successfully deployed within the
      instance health constraints specified.

      * IAM_ROLE_MISSING: The service role cannot be accessed.

      * IAM_ROLE_PERMISSIONS: The service role does not have the correct permissions.

      * INTERNAL_ERROR: There was an internal error.

      * NO_EC2_SUBSCRIPTION: The calling account is not subscribed to Amazon EC2.

      * NO_INSTANCES: No instances were specified, or no instances can be found.

      * OVER_MAX_INSTANCES: The maximum number of instances was exceeded.

      * THROTTLED: The operation was throttled because the calling account exceeded the
      throttling limits of one or more AWS services.

      * TIMEOUT: The deployment has timed out.

      * REVISION_MISSING: The revision ID was missing. This error code is most likely raised
      if the revision is deleted after the deployment is created, but before it is started.

    - **message** *(string) --*

      An accompanying error message.
    """


_ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfoelbInfoListTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfoelbInfoListTypeDef",
    {"name": str},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfoelbInfoListTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfoelbInfoListTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfo` `elbInfoList`

    Information about a load balancer in Elastic Load Balancing to use in a deployment.
    Instances are registered directly with a load balancer, and traffic is routed to the
    load balancer.

    - **name** *(string) --*

      For blue/green deployments, the name of the load balancer that is used to route
      traffic from original instances to replacement instances in a blue/green
      deployment. For in-place deployments, the name of the load balancer that instances
      are deregistered from so they are not serving traffic during a deployment, and then
      re-registered with after the deployment is complete.
    """


_ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupInfoListTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupInfoListTypeDef",
    {"name": str},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupInfoListTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupInfoListTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfo` `targetGroupInfoList`

    Information about a target group in Elastic Load Balancing to use in a deployment.
    Instances are registered as targets in a target group, and traffic is routed to the
    target group.

    - **name** *(string) --*

      For blue/green deployments, the name of the target group that instances in the
      original environment are deregistered from, and instances in the replacement
      environment are registered with. For in-place deployments, the name of the target
      group that instances are deregistered from, so they are not serving traffic during
      a deployment, and then re-registered with after the deployment is complete.
    """


_ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoList` `prodTrafficRoute`

    The path used by a load balancer to route production traffic when an Amazon ECS
    deployment is complete.

    - **listenerArns** *(list) --*

      The ARN of one listener. The listener identifies the route between a target group
      and a load balancer. This is an array of strings with a maximum size of one.

      - *(string) --*
    """


_ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    {"name": str},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoList` `targetGroups`

    Information about a target group in Elastic Load Balancing to use in a
    deployment. Instances are registered as targets in a target group, and traffic is
    routed to the target group.

    - **name** *(string) --*

      For blue/green deployments, the name of the target group that instances in the
      original environment are deregistered from, and instances in the replacement
      environment are registered with. For in-place deployments, the name of the
      target group that instances are deregistered from, so they are not serving
      traffic during a deployment, and then re-registered with after the deployment
      is complete.
    """


_ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoList` `testTrafficRoute`

    An optional path used by a load balancer to route test traffic after an Amazon ECS
    deployment. Validation can occur while test traffic is served during a deployment.

    - **listenerArns** *(list) --*

      The ARN of one listener. The listener identifies the route between a target group
      and a load balancer. This is an array of strings with a maximum size of one.

      - *(string) --*
    """


_ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListTypeDef",
    {
        "targetGroups": List[
            ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef
        ],
        "prodTrafficRoute": ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef,
        "testTrafficRoute": ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef,
    },
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfo` `targetGroupPairInfoList`

    Information about two target groups and how traffic is routed during an Amazon ECS
    deployment. An optional test traffic route can be specified.

    - **targetGroups** *(list) --*

      One pair of target groups. One is associated with the original task set. The second
      is associated with the task set that serves traffic after the deployment is
      complete.

      - *(dict) --*

        Information about a target group in Elastic Load Balancing to use in a
        deployment. Instances are registered as targets in a target group, and traffic is
        routed to the target group.

        - **name** *(string) --*

          For blue/green deployments, the name of the target group that instances in the
          original environment are deregistered from, and instances in the replacement
          environment are registered with. For in-place deployments, the name of the
          target group that instances are deregistered from, so they are not serving
          traffic during a deployment, and then re-registered with after the deployment
          is complete.

    - **prodTrafficRoute** *(dict) --*

      The path used by a load balancer to route production traffic when an Amazon ECS
      deployment is complete.

      - **listenerArns** *(list) --*

        The ARN of one listener. The listener identifies the route between a target group
        and a load balancer. This is an array of strings with a maximum size of one.

        - *(string) --*

    - **testTrafficRoute** *(dict) --*

      An optional path used by a load balancer to route test traffic after an Amazon ECS
      deployment. Validation can occur while test traffic is served during a deployment.

      - **listenerArns** *(list) --*

        The ARN of one listener. The listener identifies the route between a target group
        and a load balancer. This is an array of strings with a maximum size of one.

        - *(string) --*
    """


_ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfoTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfoTypeDef",
    {
        "elbInfoList": List[
            ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfoelbInfoListTypeDef
        ],
        "targetGroupInfoList": List[
            ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupInfoListTypeDef
        ],
        "targetGroupPairInfoList": List[
            ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListTypeDef
        ],
    },
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfoTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfoTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentsResponsedeploymentsInfo` `loadBalancerInfo`

    Information about the load balancer used in the deployment.

    - **elbInfoList** *(list) --*

      An array that contains information about the load balancer to use for load balancing in
      a deployment. In Elastic Load Balancing, load balancers are used with Classic Load
      Balancers.

      .. note::

        Adding more than one load balancer to the array is not supported.

      - *(dict) --*

        Information about a load balancer in Elastic Load Balancing to use in a deployment.
        Instances are registered directly with a load balancer, and traffic is routed to the
        load balancer.

        - **name** *(string) --*

          For blue/green deployments, the name of the load balancer that is used to route
          traffic from original instances to replacement instances in a blue/green
          deployment. For in-place deployments, the name of the load balancer that instances
          are deregistered from so they are not serving traffic during a deployment, and then
          re-registered with after the deployment is complete.

    - **targetGroupInfoList** *(list) --*

      An array that contains information about the target group to use for load balancing in
      a deployment. In Elastic Load Balancing, target groups are used with Application Load
      Balancers.

      .. note::

        Adding more than one target group to the array is not supported.

      - *(dict) --*

        Information about a target group in Elastic Load Balancing to use in a deployment.
        Instances are registered as targets in a target group, and traffic is routed to the
        target group.

        - **name** *(string) --*

          For blue/green deployments, the name of the target group that instances in the
          original environment are deregistered from, and instances in the replacement
          environment are registered with. For in-place deployments, the name of the target
          group that instances are deregistered from, so they are not serving traffic during
          a deployment, and then re-registered with after the deployment is complete.

    - **targetGroupPairInfoList** *(list) --*

      The target group pair information. This is an array of ``TargeGroupPairInfo`` objects
      with a maximum size of one.

      - *(dict) --*

        Information about two target groups and how traffic is routed during an Amazon ECS
        deployment. An optional test traffic route can be specified.

        - **targetGroups** *(list) --*

          One pair of target groups. One is associated with the original task set. The second
          is associated with the task set that serves traffic after the deployment is
          complete.

          - *(dict) --*

            Information about a target group in Elastic Load Balancing to use in a
            deployment. Instances are registered as targets in a target group, and traffic is
            routed to the target group.

            - **name** *(string) --*

              For blue/green deployments, the name of the target group that instances in the
              original environment are deregistered from, and instances in the replacement
              environment are registered with. For in-place deployments, the name of the
              target group that instances are deregistered from, so they are not serving
              traffic during a deployment, and then re-registered with after the deployment
              is complete.

        - **prodTrafficRoute** *(dict) --*

          The path used by a load balancer to route production traffic when an Amazon ECS
          deployment is complete.

          - **listenerArns** *(list) --*

            The ARN of one listener. The listener identifies the route between a target group
            and a load balancer. This is an array of strings with a maximum size of one.

            - *(string) --*

        - **testTrafficRoute** *(dict) --*

          An optional path used by a load balancer to route test traffic after an Amazon ECS
          deployment. Validation can occur while test traffic is served during a deployment.

          - **listenerArns** *(list) --*

            The ARN of one listener. The listener identifies the route between a target group
            and a load balancer. This is an array of strings with a maximum size of one.

            - *(string) --*
    """


_ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionappSpecContentTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionappSpecContentTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionappSpecContentTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevision` `appSpecContent`

    The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content
    is formatted as JSON or YAML and stored as a RawString.

    - **content** *(string) --*

      The YAML-formatted or JSON-formatted revision string.

      For an AWS Lambda deployment, the content includes a Lambda function name, the alias
      for its original version, and the alias for its replacement version. The deployment
      shifts traffic from the original version of the Lambda function to the replacement
      version.

      For an Amazon ECS deployment, the content includes the task name, information about
      the load balancer that serves traffic to the container, and more.

      For both types of deployments, the content can specify Lambda functions that run at
      specified hooks, such as ``BeforeInstall`` , during a deployment.

    - **sha256** *(string) --*

      The SHA256 hash value of the revision content.
    """


_ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisiongitHubLocationTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisiongitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisiongitHubLocationTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisiongitHubLocationTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevision` `gitHubLocation`

    Information about the location of application artifacts stored in GitHub.

    - **repository** *(string) --*

      The GitHub account and repository pair that stores a reference to the commit that
      represents the bundled artifacts for the application revision.

      Specified as account/repository.

    - **commitId** *(string) --*

      The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
      application revision.
    """


_ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisions3LocationTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisions3LocationTypeDef",
    {"bucket": str, "key": str, "bundleType": str, "version": str, "eTag": str},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisions3LocationTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisions3LocationTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevision` `s3Location`

    Information about the location of a revision stored in Amazon S3.

    - **bucket** *(string) --*

      The name of the Amazon S3 bucket where the application revision is stored.

    - **key** *(string) --*

      The name of the Amazon S3 object that represents the bundled artifacts for the
      application revision.

    - **bundleType** *(string) --*

      The file type of the application revision. Must be one of the following:

      * tar: A tar archive file.

      * tgz: A compressed tar archive file.

      * zip: A zip archive file.

    - **version** *(string) --*

      A specific version of the Amazon S3 object that represents the bundled artifacts for
      the application revision.

      If the version is not specified, the system uses the most recent version by default.

    - **eTag** *(string) --*

      The ETag of the Amazon S3 object that represents the bundled artifacts for the
      application revision.

      If the ETag is not specified as an input parameter, ETag validation of the object is
      skipped.
    """


_ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionstringTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionstringTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionstringTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevision` `string`

    Information about the location of an AWS Lambda deployment revision stored as a
    RawString.

    - **content** *(string) --*

      The YAML-formatted or JSON-formatted revision string. It includes information about
      which Lambda function to update and optional Lambda functions that validate
      deployment lifecycle events.

    - **sha256** *(string) --*

      The SHA256 hash value of the revision content.
    """


_ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionTypeDef",
    {
        "revisionType": str,
        "s3Location": ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisions3LocationTypeDef,
        "gitHubLocation": ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisiongitHubLocationTypeDef,
        "string": ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionstringTypeDef,
        "appSpecContent": ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionappSpecContentTypeDef,
    },
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentsResponsedeploymentsInfo` `previousRevision`

    Information about the application revision that was deployed to the deployment group
    before the most recent successful deployment.

    - **revisionType** *(string) --*

      The type of application revision:

      * S3: An application revision stored in Amazon S3.

      * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

      * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

    - **s3Location** *(dict) --*

      Information about the location of a revision stored in Amazon S3.

      - **bucket** *(string) --*

        The name of the Amazon S3 bucket where the application revision is stored.

      - **key** *(string) --*

        The name of the Amazon S3 object that represents the bundled artifacts for the
        application revision.

      - **bundleType** *(string) --*

        The file type of the application revision. Must be one of the following:

        * tar: A tar archive file.

        * tgz: A compressed tar archive file.

        * zip: A zip archive file.

      - **version** *(string) --*

        A specific version of the Amazon S3 object that represents the bundled artifacts for
        the application revision.

        If the version is not specified, the system uses the most recent version by default.

      - **eTag** *(string) --*

        The ETag of the Amazon S3 object that represents the bundled artifacts for the
        application revision.

        If the ETag is not specified as an input parameter, ETag validation of the object is
        skipped.

    - **gitHubLocation** *(dict) --*

      Information about the location of application artifacts stored in GitHub.

      - **repository** *(string) --*

        The GitHub account and repository pair that stores a reference to the commit that
        represents the bundled artifacts for the application revision.

        Specified as account/repository.

      - **commitId** *(string) --*

        The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
        application revision.

    - **string** *(dict) --*

      Information about the location of an AWS Lambda deployment revision stored as a
      RawString.

      - **content** *(string) --*

        The YAML-formatted or JSON-formatted revision string. It includes information about
        which Lambda function to update and optional Lambda functions that validate
        deployment lifecycle events.

      - **sha256** *(string) --*

        The SHA256 hash value of the revision content.

    - **appSpecContent** *(dict) --*

      The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content
      is formatted as JSON or YAML and stored as a RawString.

      - **content** *(string) --*

        The YAML-formatted or JSON-formatted revision string.

        For an AWS Lambda deployment, the content includes a Lambda function name, the alias
        for its original version, and the alias for its replacement version. The deployment
        shifts traffic from the original version of the Lambda function to the replacement
        version.

        For an Amazon ECS deployment, the content includes the task name, information about
        the load balancer that serves traffic to the container, and more.

        For both types of deployments, the content can specify Lambda functions that run at
        specified hooks, such as ``BeforeInstall`` , during a deployment.

      - **sha256** *(string) --*

        The SHA256 hash value of the revision content.
    """


_ClientBatchGetDeploymentsResponsedeploymentsInforevisionappSpecContentTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInforevisionappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInforevisionappSpecContentTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInforevisionappSpecContentTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentsResponsedeploymentsInforevision` `appSpecContent`

    The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content
    is formatted as JSON or YAML and stored as a RawString.

    - **content** *(string) --*

      The YAML-formatted or JSON-formatted revision string.

      For an AWS Lambda deployment, the content includes a Lambda function name, the alias
      for its original version, and the alias for its replacement version. The deployment
      shifts traffic from the original version of the Lambda function to the replacement
      version.

      For an Amazon ECS deployment, the content includes the task name, information about
      the load balancer that serves traffic to the container, and more.

      For both types of deployments, the content can specify Lambda functions that run at
      specified hooks, such as ``BeforeInstall`` , during a deployment.

    - **sha256** *(string) --*

      The SHA256 hash value of the revision content.
    """


_ClientBatchGetDeploymentsResponsedeploymentsInforevisiongitHubLocationTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInforevisiongitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInforevisiongitHubLocationTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInforevisiongitHubLocationTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentsResponsedeploymentsInforevision` `gitHubLocation`

    Information about the location of application artifacts stored in GitHub.

    - **repository** *(string) --*

      The GitHub account and repository pair that stores a reference to the commit that
      represents the bundled artifacts for the application revision.

      Specified as account/repository.

    - **commitId** *(string) --*

      The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
      application revision.
    """


_ClientBatchGetDeploymentsResponsedeploymentsInforevisions3LocationTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInforevisions3LocationTypeDef",
    {"bucket": str, "key": str, "bundleType": str, "version": str, "eTag": str},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInforevisions3LocationTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInforevisions3LocationTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentsResponsedeploymentsInforevision` `s3Location`

    Information about the location of a revision stored in Amazon S3.

    - **bucket** *(string) --*

      The name of the Amazon S3 bucket where the application revision is stored.

    - **key** *(string) --*

      The name of the Amazon S3 object that represents the bundled artifacts for the
      application revision.

    - **bundleType** *(string) --*

      The file type of the application revision. Must be one of the following:

      * tar: A tar archive file.

      * tgz: A compressed tar archive file.

      * zip: A zip archive file.

    - **version** *(string) --*

      A specific version of the Amazon S3 object that represents the bundled artifacts for
      the application revision.

      If the version is not specified, the system uses the most recent version by default.

    - **eTag** *(string) --*

      The ETag of the Amazon S3 object that represents the bundled artifacts for the
      application revision.

      If the ETag is not specified as an input parameter, ETag validation of the object is
      skipped.
    """


_ClientBatchGetDeploymentsResponsedeploymentsInforevisionstringTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInforevisionstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInforevisionstringTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInforevisionstringTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentsResponsedeploymentsInforevision` `string`

    Information about the location of an AWS Lambda deployment revision stored as a
    RawString.

    - **content** *(string) --*

      The YAML-formatted or JSON-formatted revision string. It includes information about
      which Lambda function to update and optional Lambda functions that validate
      deployment lifecycle events.

    - **sha256** *(string) --*

      The SHA256 hash value of the revision content.
    """


_ClientBatchGetDeploymentsResponsedeploymentsInforevisionTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInforevisionTypeDef",
    {
        "revisionType": str,
        "s3Location": ClientBatchGetDeploymentsResponsedeploymentsInforevisions3LocationTypeDef,
        "gitHubLocation": ClientBatchGetDeploymentsResponsedeploymentsInforevisiongitHubLocationTypeDef,
        "string": ClientBatchGetDeploymentsResponsedeploymentsInforevisionstringTypeDef,
        "appSpecContent": ClientBatchGetDeploymentsResponsedeploymentsInforevisionappSpecContentTypeDef,
    },
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInforevisionTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInforevisionTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentsResponsedeploymentsInfo` `revision`

    Information about the location of stored application artifacts and the service from which
    to retrieve them.

    - **revisionType** *(string) --*

      The type of application revision:

      * S3: An application revision stored in Amazon S3.

      * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

      * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

    - **s3Location** *(dict) --*

      Information about the location of a revision stored in Amazon S3.

      - **bucket** *(string) --*

        The name of the Amazon S3 bucket where the application revision is stored.

      - **key** *(string) --*

        The name of the Amazon S3 object that represents the bundled artifacts for the
        application revision.

      - **bundleType** *(string) --*

        The file type of the application revision. Must be one of the following:

        * tar: A tar archive file.

        * tgz: A compressed tar archive file.

        * zip: A zip archive file.

      - **version** *(string) --*

        A specific version of the Amazon S3 object that represents the bundled artifacts for
        the application revision.

        If the version is not specified, the system uses the most recent version by default.

      - **eTag** *(string) --*

        The ETag of the Amazon S3 object that represents the bundled artifacts for the
        application revision.

        If the ETag is not specified as an input parameter, ETag validation of the object is
        skipped.

    - **gitHubLocation** *(dict) --*

      Information about the location of application artifacts stored in GitHub.

      - **repository** *(string) --*

        The GitHub account and repository pair that stores a reference to the commit that
        represents the bundled artifacts for the application revision.

        Specified as account/repository.

      - **commitId** *(string) --*

        The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
        application revision.

    - **string** *(dict) --*

      Information about the location of an AWS Lambda deployment revision stored as a
      RawString.

      - **content** *(string) --*

        The YAML-formatted or JSON-formatted revision string. It includes information about
        which Lambda function to update and optional Lambda functions that validate
        deployment lifecycle events.

      - **sha256** *(string) --*

        The SHA256 hash value of the revision content.

    - **appSpecContent** *(dict) --*

      The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content
      is formatted as JSON or YAML and stored as a RawString.

      - **content** *(string) --*

        The YAML-formatted or JSON-formatted revision string.

        For an AWS Lambda deployment, the content includes a Lambda function name, the alias
        for its original version, and the alias for its replacement version. The deployment
        shifts traffic from the original version of the Lambda function to the replacement
        version.

        For an Amazon ECS deployment, the content includes the task name, information about
        the load balancer that serves traffic to the container, and more.

        For both types of deployments, the content can specify Lambda functions that run at
        specified hooks, such as ``BeforeInstall`` , during a deployment.

      - **sha256** *(string) --*

        The SHA256 hash value of the revision content.
    """


_ClientBatchGetDeploymentsResponsedeploymentsInforollbackInfoTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInforollbackInfoTypeDef",
    {
        "rollbackDeploymentId": str,
        "rollbackTriggeringDeploymentId": str,
        "rollbackMessage": str,
    },
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInforollbackInfoTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInforollbackInfoTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentsResponsedeploymentsInfo` `rollbackInfo`

    Information about a deployment rollback.

    - **rollbackDeploymentId** *(string) --*

      The ID of the deployment rollback.

    - **rollbackTriggeringDeploymentId** *(string) --*

      The deployment ID of the deployment that was underway and triggered a rollback
      deployment because it failed or was stopped.

    - **rollbackMessage** *(string) --*

      Information that describes the status of a deployment rollback (for example, whether
      the deployment can't be rolled back, is in progress, failed, or succeeded).
    """


_ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesec2TagSetec2TagSetListTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesec2TagSetec2TagSetListTypeDef",
    {"Key": str, "Value": str, "Type": str},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesec2TagSetec2TagSetListTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesec2TagSetec2TagSetListTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesec2TagSet` `ec2TagSetList`

    Information about an EC2 tag filter.

    - **Key** *(string) --*

      The tag filter key.

    - **Value** *(string) --*

      The tag filter value.

    - **Type** *(string) --*

      The tag filter type:

      * KEY_ONLY: Key only.

      * VALUE_ONLY: Value only.

      * KEY_AND_VALUE: Key and value.
    """


_ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesec2TagSetTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesec2TagSetTypeDef",
    {
        "ec2TagSetList": List[
            List[
                ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesec2TagSetec2TagSetListTypeDef
            ]
        ]
    },
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesec2TagSetTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesec2TagSetTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstances` `ec2TagSet`

    Information about the groups of EC2 instance tags that an instance must be identified
    by in order for it to be included in the replacement environment for a blue/green
    deployment. Cannot be used in the same call as tagFilters.

    - **ec2TagSetList** *(list) --*

      A list that contains other lists of EC2 instance tag groups. For an instance to be
      included in the deployment group, it must be identified by all of the tag groups in
      the list.

      - *(list) --*

        - *(dict) --*

          Information about an EC2 tag filter.

          - **Key** *(string) --*

            The tag filter key.

          - **Value** *(string) --*

            The tag filter value.

          - **Type** *(string) --*

            The tag filter type:

            * KEY_ONLY: Key only.

            * VALUE_ONLY: Value only.

            * KEY_AND_VALUE: Key and value.
    """


_ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancestagFiltersTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancestagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": str},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancestagFiltersTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancestagFiltersTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstances` `tagFilters`

    Information about an EC2 tag filter.

    - **Key** *(string) --*

      The tag filter key.

    - **Value** *(string) --*

      The tag filter value.

    - **Type** *(string) --*

      The tag filter type:

      * KEY_ONLY: Key only.

      * VALUE_ONLY: Value only.

      * KEY_AND_VALUE: Key and value.
    """


_ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesTypeDef",
    {
        "tagFilters": List[
            ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancestagFiltersTypeDef
        ],
        "autoScalingGroups": List[str],
        "ec2TagSet": ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesec2TagSetTypeDef,
    },
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentsResponsedeploymentsInfo` `targetInstances`

    Information about the instances that belong to the replacement environment in a
    blue/green deployment.

    - **tagFilters** *(list) --*

      The tag filter key, type, and value used to identify Amazon EC2 instances in a
      replacement environment for a blue/green deployment. Cannot be used in the same call as
      ec2TagSet.

      - *(dict) --*

        Information about an EC2 tag filter.

        - **Key** *(string) --*

          The tag filter key.

        - **Value** *(string) --*

          The tag filter value.

        - **Type** *(string) --*

          The tag filter type:

          * KEY_ONLY: Key only.

          * VALUE_ONLY: Value only.

          * KEY_AND_VALUE: Key and value.

    - **autoScalingGroups** *(list) --*

      The names of one or more Auto Scaling groups to identify a replacement environment for
      a blue/green deployment.

      - *(string) --*

    - **ec2TagSet** *(dict) --*

      Information about the groups of EC2 instance tags that an instance must be identified
      by in order for it to be included in the replacement environment for a blue/green
      deployment. Cannot be used in the same call as tagFilters.

      - **ec2TagSetList** *(list) --*

        A list that contains other lists of EC2 instance tag groups. For an instance to be
        included in the deployment group, it must be identified by all of the tag groups in
        the list.

        - *(list) --*

          - *(dict) --*

            Information about an EC2 tag filter.

            - **Key** *(string) --*

              The tag filter key.

            - **Value** *(string) --*

              The tag filter value.

            - **Type** *(string) --*

              The tag filter type:

              * KEY_ONLY: Key only.

              * VALUE_ONLY: Value only.

              * KEY_AND_VALUE: Key and value.
    """


_ClientBatchGetDeploymentsResponsedeploymentsInfoTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfoTypeDef",
    {
        "applicationName": str,
        "deploymentGroupName": str,
        "deploymentConfigName": str,
        "deploymentId": str,
        "previousRevision": ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionTypeDef,
        "revision": ClientBatchGetDeploymentsResponsedeploymentsInforevisionTypeDef,
        "status": str,
        "errorInformation": ClientBatchGetDeploymentsResponsedeploymentsInfoerrorInformationTypeDef,
        "createTime": datetime,
        "startTime": datetime,
        "completeTime": datetime,
        "deploymentOverview": ClientBatchGetDeploymentsResponsedeploymentsInfodeploymentOverviewTypeDef,
        "description": str,
        "creator": str,
        "ignoreApplicationStopFailures": bool,
        "autoRollbackConfiguration": ClientBatchGetDeploymentsResponsedeploymentsInfoautoRollbackConfigurationTypeDef,
        "updateOutdatedInstancesOnly": bool,
        "rollbackInfo": ClientBatchGetDeploymentsResponsedeploymentsInforollbackInfoTypeDef,
        "deploymentStyle": ClientBatchGetDeploymentsResponsedeploymentsInfodeploymentStyleTypeDef,
        "targetInstances": ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesTypeDef,
        "instanceTerminationWaitTimeStarted": bool,
        "blueGreenDeploymentConfiguration": ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationTypeDef,
        "loadBalancerInfo": ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfoTypeDef,
        "additionalDeploymentStatusInfo": str,
        "fileExistsBehavior": str,
        "deploymentStatusMessages": List[str],
        "computePlatform": str,
    },
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfoTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfoTypeDef
):
    """
    Type definition for `ClientBatchGetDeploymentsResponse` `deploymentsInfo`

    Information about a deployment.

    - **applicationName** *(string) --*

      The application name.

    - **deploymentGroupName** *(string) --*

      The deployment group name.

    - **deploymentConfigName** *(string) --*

      The deployment configuration name.

    - **deploymentId** *(string) --*

      The unique ID of a deployment.

    - **previousRevision** *(dict) --*

      Information about the application revision that was deployed to the deployment group
      before the most recent successful deployment.

      - **revisionType** *(string) --*

        The type of application revision:

        * S3: An application revision stored in Amazon S3.

        * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

        * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

      - **s3Location** *(dict) --*

        Information about the location of a revision stored in Amazon S3.

        - **bucket** *(string) --*

          The name of the Amazon S3 bucket where the application revision is stored.

        - **key** *(string) --*

          The name of the Amazon S3 object that represents the bundled artifacts for the
          application revision.

        - **bundleType** *(string) --*

          The file type of the application revision. Must be one of the following:

          * tar: A tar archive file.

          * tgz: A compressed tar archive file.

          * zip: A zip archive file.

        - **version** *(string) --*

          A specific version of the Amazon S3 object that represents the bundled artifacts for
          the application revision.

          If the version is not specified, the system uses the most recent version by default.

        - **eTag** *(string) --*

          The ETag of the Amazon S3 object that represents the bundled artifacts for the
          application revision.

          If the ETag is not specified as an input parameter, ETag validation of the object is
          skipped.

      - **gitHubLocation** *(dict) --*

        Information about the location of application artifacts stored in GitHub.

        - **repository** *(string) --*

          The GitHub account and repository pair that stores a reference to the commit that
          represents the bundled artifacts for the application revision.

          Specified as account/repository.

        - **commitId** *(string) --*

          The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
          application revision.

      - **string** *(dict) --*

        Information about the location of an AWS Lambda deployment revision stored as a
        RawString.

        - **content** *(string) --*

          The YAML-formatted or JSON-formatted revision string. It includes information about
          which Lambda function to update and optional Lambda functions that validate
          deployment lifecycle events.

        - **sha256** *(string) --*

          The SHA256 hash value of the revision content.

      - **appSpecContent** *(dict) --*

        The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content
        is formatted as JSON or YAML and stored as a RawString.

        - **content** *(string) --*

          The YAML-formatted or JSON-formatted revision string.

          For an AWS Lambda deployment, the content includes a Lambda function name, the alias
          for its original version, and the alias for its replacement version. The deployment
          shifts traffic from the original version of the Lambda function to the replacement
          version.

          For an Amazon ECS deployment, the content includes the task name, information about
          the load balancer that serves traffic to the container, and more.

          For both types of deployments, the content can specify Lambda functions that run at
          specified hooks, such as ``BeforeInstall`` , during a deployment.

        - **sha256** *(string) --*

          The SHA256 hash value of the revision content.

    - **revision** *(dict) --*

      Information about the location of stored application artifacts and the service from which
      to retrieve them.

      - **revisionType** *(string) --*

        The type of application revision:

        * S3: An application revision stored in Amazon S3.

        * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

        * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

      - **s3Location** *(dict) --*

        Information about the location of a revision stored in Amazon S3.

        - **bucket** *(string) --*

          The name of the Amazon S3 bucket where the application revision is stored.

        - **key** *(string) --*

          The name of the Amazon S3 object that represents the bundled artifacts for the
          application revision.

        - **bundleType** *(string) --*

          The file type of the application revision. Must be one of the following:

          * tar: A tar archive file.

          * tgz: A compressed tar archive file.

          * zip: A zip archive file.

        - **version** *(string) --*

          A specific version of the Amazon S3 object that represents the bundled artifacts for
          the application revision.

          If the version is not specified, the system uses the most recent version by default.

        - **eTag** *(string) --*

          The ETag of the Amazon S3 object that represents the bundled artifacts for the
          application revision.

          If the ETag is not specified as an input parameter, ETag validation of the object is
          skipped.

      - **gitHubLocation** *(dict) --*

        Information about the location of application artifacts stored in GitHub.

        - **repository** *(string) --*

          The GitHub account and repository pair that stores a reference to the commit that
          represents the bundled artifacts for the application revision.

          Specified as account/repository.

        - **commitId** *(string) --*

          The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
          application revision.

      - **string** *(dict) --*

        Information about the location of an AWS Lambda deployment revision stored as a
        RawString.

        - **content** *(string) --*

          The YAML-formatted or JSON-formatted revision string. It includes information about
          which Lambda function to update and optional Lambda functions that validate
          deployment lifecycle events.

        - **sha256** *(string) --*

          The SHA256 hash value of the revision content.

      - **appSpecContent** *(dict) --*

        The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content
        is formatted as JSON or YAML and stored as a RawString.

        - **content** *(string) --*

          The YAML-formatted or JSON-formatted revision string.

          For an AWS Lambda deployment, the content includes a Lambda function name, the alias
          for its original version, and the alias for its replacement version. The deployment
          shifts traffic from the original version of the Lambda function to the replacement
          version.

          For an Amazon ECS deployment, the content includes the task name, information about
          the load balancer that serves traffic to the container, and more.

          For both types of deployments, the content can specify Lambda functions that run at
          specified hooks, such as ``BeforeInstall`` , during a deployment.

        - **sha256** *(string) --*

          The SHA256 hash value of the revision content.

    - **status** *(string) --*

      The current state of the deployment as a whole.

    - **errorInformation** *(dict) --*

      Information about any error associated with this deployment.

      - **code** *(string) --*

        For more information, see `Error Codes for AWS CodeDeploy
        <https://docs.aws.amazon.com/codedeploy/latest/userguide/error-codes.html>`__ in the
        `AWS CodeDeploy User Guide <https://docs.aws.amazon.com/codedeploy/latest/userguide>`__
        .

        The error code:

        * APPLICATION_MISSING: The application was missing. This error code is most likely
        raised if the application is deleted after the deployment is created, but before it is
        started.

        * DEPLOYMENT_GROUP_MISSING: The deployment group was missing. This error code is most
        likely raised if the deployment group is deleted after the deployment is created, but
        before it is started.

        * HEALTH_CONSTRAINTS: The deployment failed on too many instances to be successfully
        deployed within the instance health constraints specified.

        * HEALTH_CONSTRAINTS_INVALID: The revision cannot be successfully deployed within the
        instance health constraints specified.

        * IAM_ROLE_MISSING: The service role cannot be accessed.

        * IAM_ROLE_PERMISSIONS: The service role does not have the correct permissions.

        * INTERNAL_ERROR: There was an internal error.

        * NO_EC2_SUBSCRIPTION: The calling account is not subscribed to Amazon EC2.

        * NO_INSTANCES: No instances were specified, or no instances can be found.

        * OVER_MAX_INSTANCES: The maximum number of instances was exceeded.

        * THROTTLED: The operation was throttled because the calling account exceeded the
        throttling limits of one or more AWS services.

        * TIMEOUT: The deployment has timed out.

        * REVISION_MISSING: The revision ID was missing. This error code is most likely raised
        if the revision is deleted after the deployment is created, but before it is started.

      - **message** *(string) --*

        An accompanying error message.

    - **createTime** *(datetime) --*

      A timestamp that indicates when the deployment was created.

    - **startTime** *(datetime) --*

      A timestamp that indicates when the deployment was deployed to the deployment group.

      In some cases, the reported value of the start time might be later than the complete
      time. This is due to differences in the clock settings of backend servers that
      participate in the deployment process.

    - **completeTime** *(datetime) --*

      A timestamp that indicates when the deployment was complete.

    - **deploymentOverview** *(dict) --*

      A summary of the deployment status of the instances in the deployment.

      - **Pending** *(integer) --*

        The number of instances in the deployment in a pending state.

      - **InProgress** *(integer) --*

        The number of instances in which the deployment is in progress.

      - **Succeeded** *(integer) --*

        The number of instances in the deployment to which revisions have been successfully
        deployed.

      - **Failed** *(integer) --*

        The number of instances in the deployment in a failed state.

      - **Skipped** *(integer) --*

        The number of instances in the deployment in a skipped state.

      - **Ready** *(integer) --*

        The number of instances in a replacement environment ready to receive traffic in a
        blue/green deployment.

    - **description** *(string) --*

      A comment about the deployment.

    - **creator** *(string) --*

      The means by which the deployment was created:

      * user: A user created the deployment.

      * autoscaling: Amazon EC2 Auto Scaling created the deployment.

      * codeDeployRollback: A rollback process created the deployment.

    - **ignoreApplicationStopFailures** *(boolean) --*

      If true, then if an ``ApplicationStop`` , ``BeforeBlockTraffic`` , or
      ``AfterBlockTraffic`` deployment lifecycle event to an instance fails, then the
      deployment continues to the next deployment lifecycle event. For example, if
      ``ApplicationStop`` fails, the deployment continues with DownloadBundle. If
      ``BeforeBlockTraffic`` fails, the deployment continues with ``BlockTraffic`` . If
      ``AfterBlockTraffic`` fails, the deployment continues with ``ApplicationStop`` .

      If false or not specified, then if a lifecycle event fails during a deployment to an
      instance, that deployment fails. If deployment to that instance is part of an overall
      deployment and the number of healthy hosts is not less than the minimum number of healthy
      hosts, then a deployment to the next instance is attempted.

      During a deployment, the AWS CodeDeploy agent runs the scripts specified for
      ``ApplicationStop`` , ``BeforeBlockTraffic`` , and ``AfterBlockTraffic`` in the AppSpec
      file from the previous successful deployment. (All other scripts are run from the AppSpec
      file in the current deployment.) If one of these scripts contains an error and does not
      run successfully, the deployment can fail.

      If the cause of the failure is a script from the last successful deployment that will
      never run successfully, create a new deployment and use ``ignoreApplicationStopFailures``
      to specify that the ``ApplicationStop`` , ``BeforeBlockTraffic`` , and
      ``AfterBlockTraffic`` failures should be ignored.

    - **autoRollbackConfiguration** *(dict) --*

      Information about the automatic rollback configuration associated with the deployment.

      - **enabled** *(boolean) --*

        Indicates whether a defined automatic rollback configuration is currently enabled.

      - **events** *(list) --*

        The event type or types that trigger a rollback.

        - *(string) --*

    - **updateOutdatedInstancesOnly** *(boolean) --*

      Indicates whether only instances that are not running the latest application revision are
      to be deployed to.

    - **rollbackInfo** *(dict) --*

      Information about a deployment rollback.

      - **rollbackDeploymentId** *(string) --*

        The ID of the deployment rollback.

      - **rollbackTriggeringDeploymentId** *(string) --*

        The deployment ID of the deployment that was underway and triggered a rollback
        deployment because it failed or was stopped.

      - **rollbackMessage** *(string) --*

        Information that describes the status of a deployment rollback (for example, whether
        the deployment can't be rolled back, is in progress, failed, or succeeded).

    - **deploymentStyle** *(dict) --*

      Information about the type of deployment, either in-place or blue/green, you want to run
      and whether to route deployment traffic behind a load balancer.

      - **deploymentType** *(string) --*

        Indicates whether to run an in-place deployment or a blue/green deployment.

      - **deploymentOption** *(string) --*

        Indicates whether to route deployment traffic behind a load balancer.

    - **targetInstances** *(dict) --*

      Information about the instances that belong to the replacement environment in a
      blue/green deployment.

      - **tagFilters** *(list) --*

        The tag filter key, type, and value used to identify Amazon EC2 instances in a
        replacement environment for a blue/green deployment. Cannot be used in the same call as
        ec2TagSet.

        - *(dict) --*

          Information about an EC2 tag filter.

          - **Key** *(string) --*

            The tag filter key.

          - **Value** *(string) --*

            The tag filter value.

          - **Type** *(string) --*

            The tag filter type:

            * KEY_ONLY: Key only.

            * VALUE_ONLY: Value only.

            * KEY_AND_VALUE: Key and value.

      - **autoScalingGroups** *(list) --*

        The names of one or more Auto Scaling groups to identify a replacement environment for
        a blue/green deployment.

        - *(string) --*

      - **ec2TagSet** *(dict) --*

        Information about the groups of EC2 instance tags that an instance must be identified
        by in order for it to be included in the replacement environment for a blue/green
        deployment. Cannot be used in the same call as tagFilters.

        - **ec2TagSetList** *(list) --*

          A list that contains other lists of EC2 instance tag groups. For an instance to be
          included in the deployment group, it must be identified by all of the tag groups in
          the list.

          - *(list) --*

            - *(dict) --*

              Information about an EC2 tag filter.

              - **Key** *(string) --*

                The tag filter key.

              - **Value** *(string) --*

                The tag filter value.

              - **Type** *(string) --*

                The tag filter type:

                * KEY_ONLY: Key only.

                * VALUE_ONLY: Value only.

                * KEY_AND_VALUE: Key and value.

    - **instanceTerminationWaitTimeStarted** *(boolean) --*

      Indicates whether the wait period set for the termination of instances in the original
      environment has started. Status is 'false' if the KEEP_ALIVE option is specified.
      Otherwise, 'true' as soon as the termination wait period starts.

    - **blueGreenDeploymentConfiguration** *(dict) --*

      Information about blue/green deployment options for this deployment.

      - **terminateBlueInstancesOnDeploymentSuccess** *(dict) --*

        Information about whether to terminate instances in the original fleet during a
        blue/green deployment.

        - **action** *(string) --*

          The action to take on instances in the original environment after a successful
          blue/green deployment.

          * TERMINATE: Instances are terminated after a specified wait time.

          * KEEP_ALIVE: Instances are left running after they are deregistered from the load
          balancer and removed from the deployment group.

        - **terminationWaitTimeInMinutes** *(integer) --*

          For an Amazon EC2 deployment, the number of minutes to wait after a successful
          blue/green deployment before terminating instances from the original environment.

          For an Amazon ECS deployment, the number of minutes before deleting the original
          (blue) task set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the
          original (blue) task set to a replacement (green) task set.

          The maximum setting is 2880 minutes (2 days).

      - **deploymentReadyOption** *(dict) --*

        Information about the action to take when newly provisioned instances are ready to
        receive traffic in a blue/green deployment.

        - **actionOnTimeout** *(string) --*

          Information about when to reroute traffic from an original environment to a
          replacement environment in a blue/green deployment.

          * CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately
          after the new application revision is installed on the instances in the replacement
          environment.

          * STOP_DEPLOYMENT: Do not register new instances with a load balancer unless traffic
          rerouting is started using  ContinueDeployment . If traffic rerouting is not started
          before the end of the specified wait period, the deployment status is changed to
          Stopped.

        - **waitTimeInMinutes** *(integer) --*

          The number of minutes to wait before the status of a blue/green deployment is changed
          to Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT
          option for actionOnTimeout

      - **greenFleetProvisioningOption** *(dict) --*

        Information about how instances are provisioned for a replacement environment in a
        blue/green deployment.

        - **action** *(string) --*

          The method used to add instances to a replacement environment.

          * DISCOVER_EXISTING: Use instances that already exist or will be created manually.

          * COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to define
          and create instances in a new Auto Scaling group.

    - **loadBalancerInfo** *(dict) --*

      Information about the load balancer used in the deployment.

      - **elbInfoList** *(list) --*

        An array that contains information about the load balancer to use for load balancing in
        a deployment. In Elastic Load Balancing, load balancers are used with Classic Load
        Balancers.

        .. note::

          Adding more than one load balancer to the array is not supported.

        - *(dict) --*

          Information about a load balancer in Elastic Load Balancing to use in a deployment.
          Instances are registered directly with a load balancer, and traffic is routed to the
          load balancer.

          - **name** *(string) --*

            For blue/green deployments, the name of the load balancer that is used to route
            traffic from original instances to replacement instances in a blue/green
            deployment. For in-place deployments, the name of the load balancer that instances
            are deregistered from so they are not serving traffic during a deployment, and then
            re-registered with after the deployment is complete.

      - **targetGroupInfoList** *(list) --*

        An array that contains information about the target group to use for load balancing in
        a deployment. In Elastic Load Balancing, target groups are used with Application Load
        Balancers.

        .. note::

          Adding more than one target group to the array is not supported.

        - *(dict) --*

          Information about a target group in Elastic Load Balancing to use in a deployment.
          Instances are registered as targets in a target group, and traffic is routed to the
          target group.

          - **name** *(string) --*

            For blue/green deployments, the name of the target group that instances in the
            original environment are deregistered from, and instances in the replacement
            environment are registered with. For in-place deployments, the name of the target
            group that instances are deregistered from, so they are not serving traffic during
            a deployment, and then re-registered with after the deployment is complete.

      - **targetGroupPairInfoList** *(list) --*

        The target group pair information. This is an array of ``TargeGroupPairInfo`` objects
        with a maximum size of one.

        - *(dict) --*

          Information about two target groups and how traffic is routed during an Amazon ECS
          deployment. An optional test traffic route can be specified.

          - **targetGroups** *(list) --*

            One pair of target groups. One is associated with the original task set. The second
            is associated with the task set that serves traffic after the deployment is
            complete.

            - *(dict) --*

              Information about a target group in Elastic Load Balancing to use in a
              deployment. Instances are registered as targets in a target group, and traffic is
              routed to the target group.

              - **name** *(string) --*

                For blue/green deployments, the name of the target group that instances in the
                original environment are deregistered from, and instances in the replacement
                environment are registered with. For in-place deployments, the name of the
                target group that instances are deregistered from, so they are not serving
                traffic during a deployment, and then re-registered with after the deployment
                is complete.

          - **prodTrafficRoute** *(dict) --*

            The path used by a load balancer to route production traffic when an Amazon ECS
            deployment is complete.

            - **listenerArns** *(list) --*

              The ARN of one listener. The listener identifies the route between a target group
              and a load balancer. This is an array of strings with a maximum size of one.

              - *(string) --*

          - **testTrafficRoute** *(dict) --*

            An optional path used by a load balancer to route test traffic after an Amazon ECS
            deployment. Validation can occur while test traffic is served during a deployment.

            - **listenerArns** *(list) --*

              The ARN of one listener. The listener identifies the route between a target group
              and a load balancer. This is an array of strings with a maximum size of one.

              - *(string) --*

    - **additionalDeploymentStatusInfo** *(string) --*

      Provides information about the results of a deployment, such as whether instances in the
      original environment in a blue/green deployment were not terminated.

    - **fileExistsBehavior** *(string) --*

      Information about how AWS CodeDeploy handles files that already exist in a deployment
      target location but weren't part of the previous successful deployment.

      * DISALLOW: The deployment fails. This is also the default behavior if no option is
      specified.

      * OVERWRITE: The version of the file from the application revision currently being
      deployed replaces the version already on the instance.

      * RETAIN: The version of the file already on the instance is kept and used as part of the
      new deployment.

    - **deploymentStatusMessages** *(list) --*

      Messages that contain information about the status of a deployment.

      - *(string) --*

    - **computePlatform** *(string) --*

      The destination platform type for the deployment (``Lambda`` , ``Server`` , or ``ECS`` ).
    """


_ClientBatchGetDeploymentsResponseTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponseTypeDef",
    {"deploymentsInfo": List[ClientBatchGetDeploymentsResponsedeploymentsInfoTypeDef]},
    total=False,
)


class ClientBatchGetDeploymentsResponseTypeDef(
    _ClientBatchGetDeploymentsResponseTypeDef
):
    """
    Type definition for `ClientBatchGetDeployments` `Response`

    Represents the output of a BatchGetDeployments operation.

    - **deploymentsInfo** *(list) --*

      Information about the deployments.

      - *(dict) --*

        Information about a deployment.

        - **applicationName** *(string) --*

          The application name.

        - **deploymentGroupName** *(string) --*

          The deployment group name.

        - **deploymentConfigName** *(string) --*

          The deployment configuration name.

        - **deploymentId** *(string) --*

          The unique ID of a deployment.

        - **previousRevision** *(dict) --*

          Information about the application revision that was deployed to the deployment group
          before the most recent successful deployment.

          - **revisionType** *(string) --*

            The type of application revision:

            * S3: An application revision stored in Amazon S3.

            * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

            * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

          - **s3Location** *(dict) --*

            Information about the location of a revision stored in Amazon S3.

            - **bucket** *(string) --*

              The name of the Amazon S3 bucket where the application revision is stored.

            - **key** *(string) --*

              The name of the Amazon S3 object that represents the bundled artifacts for the
              application revision.

            - **bundleType** *(string) --*

              The file type of the application revision. Must be one of the following:

              * tar: A tar archive file.

              * tgz: A compressed tar archive file.

              * zip: A zip archive file.

            - **version** *(string) --*

              A specific version of the Amazon S3 object that represents the bundled artifacts for
              the application revision.

              If the version is not specified, the system uses the most recent version by default.

            - **eTag** *(string) --*

              The ETag of the Amazon S3 object that represents the bundled artifacts for the
              application revision.

              If the ETag is not specified as an input parameter, ETag validation of the object is
              skipped.

          - **gitHubLocation** *(dict) --*

            Information about the location of application artifacts stored in GitHub.

            - **repository** *(string) --*

              The GitHub account and repository pair that stores a reference to the commit that
              represents the bundled artifacts for the application revision.

              Specified as account/repository.

            - **commitId** *(string) --*

              The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
              application revision.

          - **string** *(dict) --*

            Information about the location of an AWS Lambda deployment revision stored as a
            RawString.

            - **content** *(string) --*

              The YAML-formatted or JSON-formatted revision string. It includes information about
              which Lambda function to update and optional Lambda functions that validate
              deployment lifecycle events.

            - **sha256** *(string) --*

              The SHA256 hash value of the revision content.

          - **appSpecContent** *(dict) --*

            The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content
            is formatted as JSON or YAML and stored as a RawString.

            - **content** *(string) --*

              The YAML-formatted or JSON-formatted revision string.

              For an AWS Lambda deployment, the content includes a Lambda function name, the alias
              for its original version, and the alias for its replacement version. The deployment
              shifts traffic from the original version of the Lambda function to the replacement
              version.

              For an Amazon ECS deployment, the content includes the task name, information about
              the load balancer that serves traffic to the container, and more.

              For both types of deployments, the content can specify Lambda functions that run at
              specified hooks, such as ``BeforeInstall`` , during a deployment.

            - **sha256** *(string) --*

              The SHA256 hash value of the revision content.

        - **revision** *(dict) --*

          Information about the location of stored application artifacts and the service from which
          to retrieve them.

          - **revisionType** *(string) --*

            The type of application revision:

            * S3: An application revision stored in Amazon S3.

            * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

            * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

          - **s3Location** *(dict) --*

            Information about the location of a revision stored in Amazon S3.

            - **bucket** *(string) --*

              The name of the Amazon S3 bucket where the application revision is stored.

            - **key** *(string) --*

              The name of the Amazon S3 object that represents the bundled artifacts for the
              application revision.

            - **bundleType** *(string) --*

              The file type of the application revision. Must be one of the following:

              * tar: A tar archive file.

              * tgz: A compressed tar archive file.

              * zip: A zip archive file.

            - **version** *(string) --*

              A specific version of the Amazon S3 object that represents the bundled artifacts for
              the application revision.

              If the version is not specified, the system uses the most recent version by default.

            - **eTag** *(string) --*

              The ETag of the Amazon S3 object that represents the bundled artifacts for the
              application revision.

              If the ETag is not specified as an input parameter, ETag validation of the object is
              skipped.

          - **gitHubLocation** *(dict) --*

            Information about the location of application artifacts stored in GitHub.

            - **repository** *(string) --*

              The GitHub account and repository pair that stores a reference to the commit that
              represents the bundled artifacts for the application revision.

              Specified as account/repository.

            - **commitId** *(string) --*

              The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
              application revision.

          - **string** *(dict) --*

            Information about the location of an AWS Lambda deployment revision stored as a
            RawString.

            - **content** *(string) --*

              The YAML-formatted or JSON-formatted revision string. It includes information about
              which Lambda function to update and optional Lambda functions that validate
              deployment lifecycle events.

            - **sha256** *(string) --*

              The SHA256 hash value of the revision content.

          - **appSpecContent** *(dict) --*

            The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content
            is formatted as JSON or YAML and stored as a RawString.

            - **content** *(string) --*

              The YAML-formatted or JSON-formatted revision string.

              For an AWS Lambda deployment, the content includes a Lambda function name, the alias
              for its original version, and the alias for its replacement version. The deployment
              shifts traffic from the original version of the Lambda function to the replacement
              version.

              For an Amazon ECS deployment, the content includes the task name, information about
              the load balancer that serves traffic to the container, and more.

              For both types of deployments, the content can specify Lambda functions that run at
              specified hooks, such as ``BeforeInstall`` , during a deployment.

            - **sha256** *(string) --*

              The SHA256 hash value of the revision content.

        - **status** *(string) --*

          The current state of the deployment as a whole.

        - **errorInformation** *(dict) --*

          Information about any error associated with this deployment.

          - **code** *(string) --*

            For more information, see `Error Codes for AWS CodeDeploy
            <https://docs.aws.amazon.com/codedeploy/latest/userguide/error-codes.html>`__ in the
            `AWS CodeDeploy User Guide <https://docs.aws.amazon.com/codedeploy/latest/userguide>`__
            .

            The error code:

            * APPLICATION_MISSING: The application was missing. This error code is most likely
            raised if the application is deleted after the deployment is created, but before it is
            started.

            * DEPLOYMENT_GROUP_MISSING: The deployment group was missing. This error code is most
            likely raised if the deployment group is deleted after the deployment is created, but
            before it is started.

            * HEALTH_CONSTRAINTS: The deployment failed on too many instances to be successfully
            deployed within the instance health constraints specified.

            * HEALTH_CONSTRAINTS_INVALID: The revision cannot be successfully deployed within the
            instance health constraints specified.

            * IAM_ROLE_MISSING: The service role cannot be accessed.

            * IAM_ROLE_PERMISSIONS: The service role does not have the correct permissions.

            * INTERNAL_ERROR: There was an internal error.

            * NO_EC2_SUBSCRIPTION: The calling account is not subscribed to Amazon EC2.

            * NO_INSTANCES: No instances were specified, or no instances can be found.

            * OVER_MAX_INSTANCES: The maximum number of instances was exceeded.

            * THROTTLED: The operation was throttled because the calling account exceeded the
            throttling limits of one or more AWS services.

            * TIMEOUT: The deployment has timed out.

            * REVISION_MISSING: The revision ID was missing. This error code is most likely raised
            if the revision is deleted after the deployment is created, but before it is started.

          - **message** *(string) --*

            An accompanying error message.

        - **createTime** *(datetime) --*

          A timestamp that indicates when the deployment was created.

        - **startTime** *(datetime) --*

          A timestamp that indicates when the deployment was deployed to the deployment group.

          In some cases, the reported value of the start time might be later than the complete
          time. This is due to differences in the clock settings of backend servers that
          participate in the deployment process.

        - **completeTime** *(datetime) --*

          A timestamp that indicates when the deployment was complete.

        - **deploymentOverview** *(dict) --*

          A summary of the deployment status of the instances in the deployment.

          - **Pending** *(integer) --*

            The number of instances in the deployment in a pending state.

          - **InProgress** *(integer) --*

            The number of instances in which the deployment is in progress.

          - **Succeeded** *(integer) --*

            The number of instances in the deployment to which revisions have been successfully
            deployed.

          - **Failed** *(integer) --*

            The number of instances in the deployment in a failed state.

          - **Skipped** *(integer) --*

            The number of instances in the deployment in a skipped state.

          - **Ready** *(integer) --*

            The number of instances in a replacement environment ready to receive traffic in a
            blue/green deployment.

        - **description** *(string) --*

          A comment about the deployment.

        - **creator** *(string) --*

          The means by which the deployment was created:

          * user: A user created the deployment.

          * autoscaling: Amazon EC2 Auto Scaling created the deployment.

          * codeDeployRollback: A rollback process created the deployment.

        - **ignoreApplicationStopFailures** *(boolean) --*

          If true, then if an ``ApplicationStop`` , ``BeforeBlockTraffic`` , or
          ``AfterBlockTraffic`` deployment lifecycle event to an instance fails, then the
          deployment continues to the next deployment lifecycle event. For example, if
          ``ApplicationStop`` fails, the deployment continues with DownloadBundle. If
          ``BeforeBlockTraffic`` fails, the deployment continues with ``BlockTraffic`` . If
          ``AfterBlockTraffic`` fails, the deployment continues with ``ApplicationStop`` .

          If false or not specified, then if a lifecycle event fails during a deployment to an
          instance, that deployment fails. If deployment to that instance is part of an overall
          deployment and the number of healthy hosts is not less than the minimum number of healthy
          hosts, then a deployment to the next instance is attempted.

          During a deployment, the AWS CodeDeploy agent runs the scripts specified for
          ``ApplicationStop`` , ``BeforeBlockTraffic`` , and ``AfterBlockTraffic`` in the AppSpec
          file from the previous successful deployment. (All other scripts are run from the AppSpec
          file in the current deployment.) If one of these scripts contains an error and does not
          run successfully, the deployment can fail.

          If the cause of the failure is a script from the last successful deployment that will
          never run successfully, create a new deployment and use ``ignoreApplicationStopFailures``
          to specify that the ``ApplicationStop`` , ``BeforeBlockTraffic`` , and
          ``AfterBlockTraffic`` failures should be ignored.

        - **autoRollbackConfiguration** *(dict) --*

          Information about the automatic rollback configuration associated with the deployment.

          - **enabled** *(boolean) --*

            Indicates whether a defined automatic rollback configuration is currently enabled.

          - **events** *(list) --*

            The event type or types that trigger a rollback.

            - *(string) --*

        - **updateOutdatedInstancesOnly** *(boolean) --*

          Indicates whether only instances that are not running the latest application revision are
          to be deployed to.

        - **rollbackInfo** *(dict) --*

          Information about a deployment rollback.

          - **rollbackDeploymentId** *(string) --*

            The ID of the deployment rollback.

          - **rollbackTriggeringDeploymentId** *(string) --*

            The deployment ID of the deployment that was underway and triggered a rollback
            deployment because it failed or was stopped.

          - **rollbackMessage** *(string) --*

            Information that describes the status of a deployment rollback (for example, whether
            the deployment can't be rolled back, is in progress, failed, or succeeded).

        - **deploymentStyle** *(dict) --*

          Information about the type of deployment, either in-place or blue/green, you want to run
          and whether to route deployment traffic behind a load balancer.

          - **deploymentType** *(string) --*

            Indicates whether to run an in-place deployment or a blue/green deployment.

          - **deploymentOption** *(string) --*

            Indicates whether to route deployment traffic behind a load balancer.

        - **targetInstances** *(dict) --*

          Information about the instances that belong to the replacement environment in a
          blue/green deployment.

          - **tagFilters** *(list) --*

            The tag filter key, type, and value used to identify Amazon EC2 instances in a
            replacement environment for a blue/green deployment. Cannot be used in the same call as
            ec2TagSet.

            - *(dict) --*

              Information about an EC2 tag filter.

              - **Key** *(string) --*

                The tag filter key.

              - **Value** *(string) --*

                The tag filter value.

              - **Type** *(string) --*

                The tag filter type:

                * KEY_ONLY: Key only.

                * VALUE_ONLY: Value only.

                * KEY_AND_VALUE: Key and value.

          - **autoScalingGroups** *(list) --*

            The names of one or more Auto Scaling groups to identify a replacement environment for
            a blue/green deployment.

            - *(string) --*

          - **ec2TagSet** *(dict) --*

            Information about the groups of EC2 instance tags that an instance must be identified
            by in order for it to be included in the replacement environment for a blue/green
            deployment. Cannot be used in the same call as tagFilters.

            - **ec2TagSetList** *(list) --*

              A list that contains other lists of EC2 instance tag groups. For an instance to be
              included in the deployment group, it must be identified by all of the tag groups in
              the list.

              - *(list) --*

                - *(dict) --*

                  Information about an EC2 tag filter.

                  - **Key** *(string) --*

                    The tag filter key.

                  - **Value** *(string) --*

                    The tag filter value.

                  - **Type** *(string) --*

                    The tag filter type:

                    * KEY_ONLY: Key only.

                    * VALUE_ONLY: Value only.

                    * KEY_AND_VALUE: Key and value.

        - **instanceTerminationWaitTimeStarted** *(boolean) --*

          Indicates whether the wait period set for the termination of instances in the original
          environment has started. Status is 'false' if the KEEP_ALIVE option is specified.
          Otherwise, 'true' as soon as the termination wait period starts.

        - **blueGreenDeploymentConfiguration** *(dict) --*

          Information about blue/green deployment options for this deployment.

          - **terminateBlueInstancesOnDeploymentSuccess** *(dict) --*

            Information about whether to terminate instances in the original fleet during a
            blue/green deployment.

            - **action** *(string) --*

              The action to take on instances in the original environment after a successful
              blue/green deployment.

              * TERMINATE: Instances are terminated after a specified wait time.

              * KEEP_ALIVE: Instances are left running after they are deregistered from the load
              balancer and removed from the deployment group.

            - **terminationWaitTimeInMinutes** *(integer) --*

              For an Amazon EC2 deployment, the number of minutes to wait after a successful
              blue/green deployment before terminating instances from the original environment.

              For an Amazon ECS deployment, the number of minutes before deleting the original
              (blue) task set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the
              original (blue) task set to a replacement (green) task set.

              The maximum setting is 2880 minutes (2 days).

          - **deploymentReadyOption** *(dict) --*

            Information about the action to take when newly provisioned instances are ready to
            receive traffic in a blue/green deployment.

            - **actionOnTimeout** *(string) --*

              Information about when to reroute traffic from an original environment to a
              replacement environment in a blue/green deployment.

              * CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately
              after the new application revision is installed on the instances in the replacement
              environment.

              * STOP_DEPLOYMENT: Do not register new instances with a load balancer unless traffic
              rerouting is started using  ContinueDeployment . If traffic rerouting is not started
              before the end of the specified wait period, the deployment status is changed to
              Stopped.

            - **waitTimeInMinutes** *(integer) --*

              The number of minutes to wait before the status of a blue/green deployment is changed
              to Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT
              option for actionOnTimeout

          - **greenFleetProvisioningOption** *(dict) --*

            Information about how instances are provisioned for a replacement environment in a
            blue/green deployment.

            - **action** *(string) --*

              The method used to add instances to a replacement environment.

              * DISCOVER_EXISTING: Use instances that already exist or will be created manually.

              * COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to define
              and create instances in a new Auto Scaling group.

        - **loadBalancerInfo** *(dict) --*

          Information about the load balancer used in the deployment.

          - **elbInfoList** *(list) --*

            An array that contains information about the load balancer to use for load balancing in
            a deployment. In Elastic Load Balancing, load balancers are used with Classic Load
            Balancers.

            .. note::

              Adding more than one load balancer to the array is not supported.

            - *(dict) --*

              Information about a load balancer in Elastic Load Balancing to use in a deployment.
              Instances are registered directly with a load balancer, and traffic is routed to the
              load balancer.

              - **name** *(string) --*

                For blue/green deployments, the name of the load balancer that is used to route
                traffic from original instances to replacement instances in a blue/green
                deployment. For in-place deployments, the name of the load balancer that instances
                are deregistered from so they are not serving traffic during a deployment, and then
                re-registered with after the deployment is complete.

          - **targetGroupInfoList** *(list) --*

            An array that contains information about the target group to use for load balancing in
            a deployment. In Elastic Load Balancing, target groups are used with Application Load
            Balancers.

            .. note::

              Adding more than one target group to the array is not supported.

            - *(dict) --*

              Information about a target group in Elastic Load Balancing to use in a deployment.
              Instances are registered as targets in a target group, and traffic is routed to the
              target group.

              - **name** *(string) --*

                For blue/green deployments, the name of the target group that instances in the
                original environment are deregistered from, and instances in the replacement
                environment are registered with. For in-place deployments, the name of the target
                group that instances are deregistered from, so they are not serving traffic during
                a deployment, and then re-registered with after the deployment is complete.

          - **targetGroupPairInfoList** *(list) --*

            The target group pair information. This is an array of ``TargeGroupPairInfo`` objects
            with a maximum size of one.

            - *(dict) --*

              Information about two target groups and how traffic is routed during an Amazon ECS
              deployment. An optional test traffic route can be specified.

              - **targetGroups** *(list) --*

                One pair of target groups. One is associated with the original task set. The second
                is associated with the task set that serves traffic after the deployment is
                complete.

                - *(dict) --*

                  Information about a target group in Elastic Load Balancing to use in a
                  deployment. Instances are registered as targets in a target group, and traffic is
                  routed to the target group.

                  - **name** *(string) --*

                    For blue/green deployments, the name of the target group that instances in the
                    original environment are deregistered from, and instances in the replacement
                    environment are registered with. For in-place deployments, the name of the
                    target group that instances are deregistered from, so they are not serving
                    traffic during a deployment, and then re-registered with after the deployment
                    is complete.

              - **prodTrafficRoute** *(dict) --*

                The path used by a load balancer to route production traffic when an Amazon ECS
                deployment is complete.

                - **listenerArns** *(list) --*

                  The ARN of one listener. The listener identifies the route between a target group
                  and a load balancer. This is an array of strings with a maximum size of one.

                  - *(string) --*

              - **testTrafficRoute** *(dict) --*

                An optional path used by a load balancer to route test traffic after an Amazon ECS
                deployment. Validation can occur while test traffic is served during a deployment.

                - **listenerArns** *(list) --*

                  The ARN of one listener. The listener identifies the route between a target group
                  and a load balancer. This is an array of strings with a maximum size of one.

                  - *(string) --*

        - **additionalDeploymentStatusInfo** *(string) --*

          Provides information about the results of a deployment, such as whether instances in the
          original environment in a blue/green deployment were not terminated.

        - **fileExistsBehavior** *(string) --*

          Information about how AWS CodeDeploy handles files that already exist in a deployment
          target location but weren't part of the previous successful deployment.

          * DISALLOW: The deployment fails. This is also the default behavior if no option is
          specified.

          * OVERWRITE: The version of the file from the application revision currently being
          deployed replaces the version already on the instance.

          * RETAIN: The version of the file already on the instance is kept and used as part of the
          new deployment.

        - **deploymentStatusMessages** *(list) --*

          Messages that contain information about the status of a deployment.

          - *(string) --*

        - **computePlatform** *(string) --*

          The destination platform type for the deployment (``Lambda`` , ``Server`` , or ``ECS`` ).
    """


_ClientBatchGetOnPremisesInstancesResponseinstanceInfostagsTypeDef = TypedDict(
    "_ClientBatchGetOnPremisesInstancesResponseinstanceInfostagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientBatchGetOnPremisesInstancesResponseinstanceInfostagsTypeDef(
    _ClientBatchGetOnPremisesInstancesResponseinstanceInfostagsTypeDef
):
    """
    Type definition for `ClientBatchGetOnPremisesInstancesResponseinstanceInfos` `tags`

    Information about a tag.

    - **Key** *(string) --*

      The tag's key.

    - **Value** *(string) --*

      The tag's value.
    """


_ClientBatchGetOnPremisesInstancesResponseinstanceInfosTypeDef = TypedDict(
    "_ClientBatchGetOnPremisesInstancesResponseinstanceInfosTypeDef",
    {
        "instanceName": str,
        "iamSessionArn": str,
        "iamUserArn": str,
        "instanceArn": str,
        "registerTime": datetime,
        "deregisterTime": datetime,
        "tags": List[ClientBatchGetOnPremisesInstancesResponseinstanceInfostagsTypeDef],
    },
    total=False,
)


class ClientBatchGetOnPremisesInstancesResponseinstanceInfosTypeDef(
    _ClientBatchGetOnPremisesInstancesResponseinstanceInfosTypeDef
):
    """
    Type definition for `ClientBatchGetOnPremisesInstancesResponse` `instanceInfos`

    Information about an on-premises instance.

    - **instanceName** *(string) --*

      The name of the on-premises instance.

    - **iamSessionArn** *(string) --*

      The ARN of the IAM session associated with the on-premises instance.

    - **iamUserArn** *(string) --*

      The IAM user ARN associated with the on-premises instance.

    - **instanceArn** *(string) --*

      The ARN of the on-premises instance.

    - **registerTime** *(datetime) --*

      The time at which the on-premises instance was registered.

    - **deregisterTime** *(datetime) --*

      If the on-premises instance was deregistered, the time at which the on-premises instance
      was deregistered.

    - **tags** *(list) --*

      The tags currently associated with the on-premises instance.

      - *(dict) --*

        Information about a tag.

        - **Key** *(string) --*

          The tag's key.

        - **Value** *(string) --*

          The tag's value.
    """


_ClientBatchGetOnPremisesInstancesResponseTypeDef = TypedDict(
    "_ClientBatchGetOnPremisesInstancesResponseTypeDef",
    {
        "instanceInfos": List[
            ClientBatchGetOnPremisesInstancesResponseinstanceInfosTypeDef
        ]
    },
    total=False,
)


class ClientBatchGetOnPremisesInstancesResponseTypeDef(
    _ClientBatchGetOnPremisesInstancesResponseTypeDef
):
    """
    Type definition for `ClientBatchGetOnPremisesInstances` `Response`

    Represents the output of a BatchGetOnPremisesInstances operation.

    - **instanceInfos** *(list) --*

      Information about the on-premises instances.

      - *(dict) --*

        Information about an on-premises instance.

        - **instanceName** *(string) --*

          The name of the on-premises instance.

        - **iamSessionArn** *(string) --*

          The ARN of the IAM session associated with the on-premises instance.

        - **iamUserArn** *(string) --*

          The IAM user ARN associated with the on-premises instance.

        - **instanceArn** *(string) --*

          The ARN of the on-premises instance.

        - **registerTime** *(datetime) --*

          The time at which the on-premises instance was registered.

        - **deregisterTime** *(datetime) --*

          If the on-premises instance was deregistered, the time at which the on-premises instance
          was deregistered.

        - **tags** *(list) --*

          The tags currently associated with the on-premises instance.

          - *(dict) --*

            Information about a tag.

            - **Key** *(string) --*

              The tag's key.

            - **Value** *(string) --*

              The tag's value.
    """


_ClientCreateApplicationResponseTypeDef = TypedDict(
    "_ClientCreateApplicationResponseTypeDef", {"applicationId": str}, total=False
)


class ClientCreateApplicationResponseTypeDef(_ClientCreateApplicationResponseTypeDef):
    """
    Type definition for `ClientCreateApplication` `Response`

    Represents the output of a CreateApplication operation.

    - **applicationId** *(string) --*

      A unique application ID.
    """


_ClientCreateApplicationtagsTypeDef = TypedDict(
    "_ClientCreateApplicationtagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateApplicationtagsTypeDef(_ClientCreateApplicationtagsTypeDef):
    """
    Type definition for `ClientCreateApplication` `tags`

    Information about a tag.

    - **Key** *(string) --*

      The tag's key.

    - **Value** *(string) --*

      The tag's value.
    """


_ClientCreateDeploymentConfigResponseTypeDef = TypedDict(
    "_ClientCreateDeploymentConfigResponseTypeDef",
    {"deploymentConfigId": str},
    total=False,
)


class ClientCreateDeploymentConfigResponseTypeDef(
    _ClientCreateDeploymentConfigResponseTypeDef
):
    """
    Type definition for `ClientCreateDeploymentConfig` `Response`

    Represents the output of a CreateDeploymentConfig operation.

    - **deploymentConfigId** *(string) --*

      A unique deployment configuration ID.
    """


_ClientCreateDeploymentConfigminimumHealthyHostsTypeDef = TypedDict(
    "_ClientCreateDeploymentConfigminimumHealthyHostsTypeDef",
    {"value": int, "type": str},
    total=False,
)


class ClientCreateDeploymentConfigminimumHealthyHostsTypeDef(
    _ClientCreateDeploymentConfigminimumHealthyHostsTypeDef
):
    """
    Type definition for `ClientCreateDeploymentConfig` `minimumHealthyHosts`

    The minimum number of healthy instances that should be available at any time during the
    deployment. There are two parameters expected in the input: type and value.

    The type parameter takes either of the following values:

    * HOST_COUNT: The value parameter represents the minimum number of healthy instances as an
    absolute value.

    * FLEET_PERCENT: The value parameter represents the minimum number of healthy instances as a
    percentage of the total number of instances in the deployment. If you specify FLEET_PERCENT, at
    the start of the deployment, AWS CodeDeploy converts the percentage to the equivalent number of
    instance and rounds up fractional instances.

    The value parameter takes an integer.

    For example, to set a minimum of 95% healthy instance, specify a type of FLEET_PERCENT and a
    value of 95.

    - **value** *(integer) --*

      The minimum healthy instance value.

    - **type** *(string) --*

      The minimum healthy instance type:

      * HOST_COUNT: The minimum number of healthy instance as an absolute value.

      * FLEET_PERCENT: The minimum number of healthy instance as a percentage of the total number of
      instance in the deployment.

      In an example of nine instance, if a HOST_COUNT of six is specified, deploy to up to three
      instances at a time. The deployment is successful if six or more instances are deployed to
      successfully. Otherwise, the deployment fails. If a FLEET_PERCENT of 40 is specified, deploy to
      up to five instance at a time. The deployment is successful if four or more instance are
      deployed to successfully. Otherwise, the deployment fails.

      .. note::

        In a call to the ``GetDeploymentConfig`` , CodeDeployDefault.OneAtATime returns a minimum
        healthy instance type of MOST_CONCURRENCY and a value of 1. This means a deployment to only
        one instance at a time. (You cannot set the type to MOST_CONCURRENCY, only to HOST_COUNT or
        FLEET_PERCENT.) In addition, with CodeDeployDefault.OneAtATime, AWS CodeDeploy attempts to
        ensure that all instances but one are kept in a healthy state during the deployment. Although
        this allows one instance at a time to be taken offline for a new deployment, it also means
        that if the deployment to the last instance fails, the overall deployment is still successful.

      For more information, see `AWS CodeDeploy Instance Health
      <https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-health.html>`__ in the *AWS
      CodeDeploy User Guide* .
    """


_ClientCreateDeploymentConfigtrafficRoutingConfigtimeBasedCanaryTypeDef = TypedDict(
    "_ClientCreateDeploymentConfigtrafficRoutingConfigtimeBasedCanaryTypeDef",
    {"canaryPercentage": int, "canaryInterval": int},
    total=False,
)


class ClientCreateDeploymentConfigtrafficRoutingConfigtimeBasedCanaryTypeDef(
    _ClientCreateDeploymentConfigtrafficRoutingConfigtimeBasedCanaryTypeDef
):
    """
    Type definition for `ClientCreateDeploymentConfigtrafficRoutingConfig` `timeBasedCanary`

    A configuration that shifts traffic from one version of a Lambda function to another in two
    increments. The original and target Lambda function versions are specified in the deployment's
    AppSpec file.

    - **canaryPercentage** *(integer) --*

      The percentage of traffic to shift in the first increment of a ``TimeBasedCanary`` deployment.

    - **canaryInterval** *(integer) --*

      The number of minutes between the first and second traffic shifts of a ``TimeBasedCanary``
      deployment.
    """


_ClientCreateDeploymentConfigtrafficRoutingConfigtimeBasedLinearTypeDef = TypedDict(
    "_ClientCreateDeploymentConfigtrafficRoutingConfigtimeBasedLinearTypeDef",
    {"linearPercentage": int, "linearInterval": int},
    total=False,
)


class ClientCreateDeploymentConfigtrafficRoutingConfigtimeBasedLinearTypeDef(
    _ClientCreateDeploymentConfigtrafficRoutingConfigtimeBasedLinearTypeDef
):
    """
    Type definition for `ClientCreateDeploymentConfigtrafficRoutingConfig` `timeBasedLinear`

    A configuration that shifts traffic from one version of a Lambda function to another in equal
    increments, with an equal number of minutes between each increment. The original and target
    Lambda function versions are specified in the deployment's AppSpec file.

    - **linearPercentage** *(integer) --*

      The percentage of traffic that is shifted at the start of each increment of a
      ``TimeBasedLinear`` deployment.

    - **linearInterval** *(integer) --*

      The number of minutes between each incremental traffic shift of a ``TimeBasedLinear``
      deployment.
    """


_ClientCreateDeploymentConfigtrafficRoutingConfigTypeDef = TypedDict(
    "_ClientCreateDeploymentConfigtrafficRoutingConfigTypeDef",
    {
        "type": str,
        "timeBasedCanary": ClientCreateDeploymentConfigtrafficRoutingConfigtimeBasedCanaryTypeDef,
        "timeBasedLinear": ClientCreateDeploymentConfigtrafficRoutingConfigtimeBasedLinearTypeDef,
    },
    total=False,
)


class ClientCreateDeploymentConfigtrafficRoutingConfigTypeDef(
    _ClientCreateDeploymentConfigtrafficRoutingConfigTypeDef
):
    """
    Type definition for `ClientCreateDeploymentConfig` `trafficRoutingConfig`

    The configuration that specifies how the deployment traffic is routed.

    - **type** *(string) --*

      The type of traffic shifting (``TimeBasedCanary`` or ``TimeBasedLinear`` ) used by a deployment
      configuration .

    - **timeBasedCanary** *(dict) --*

      A configuration that shifts traffic from one version of a Lambda function to another in two
      increments. The original and target Lambda function versions are specified in the deployment's
      AppSpec file.

      - **canaryPercentage** *(integer) --*

        The percentage of traffic to shift in the first increment of a ``TimeBasedCanary`` deployment.

      - **canaryInterval** *(integer) --*

        The number of minutes between the first and second traffic shifts of a ``TimeBasedCanary``
        deployment.

    - **timeBasedLinear** *(dict) --*

      A configuration that shifts traffic from one version of a Lambda function to another in equal
      increments, with an equal number of minutes between each increment. The original and target
      Lambda function versions are specified in the deployment's AppSpec file.

      - **linearPercentage** *(integer) --*

        The percentage of traffic that is shifted at the start of each increment of a
        ``TimeBasedLinear`` deployment.

      - **linearInterval** *(integer) --*

        The number of minutes between each incremental traffic shift of a ``TimeBasedLinear``
        deployment.
    """


_ClientCreateDeploymentGroupResponseTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupResponseTypeDef",
    {"deploymentGroupId": str},
    total=False,
)


class ClientCreateDeploymentGroupResponseTypeDef(
    _ClientCreateDeploymentGroupResponseTypeDef
):
    """
    Type definition for `ClientCreateDeploymentGroup` `Response`

    Represents the output of a CreateDeploymentGroup operation.

    - **deploymentGroupId** *(string) --*

      A unique deployment group ID.
    """


_ClientCreateDeploymentGroupalarmConfigurationalarmsTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupalarmConfigurationalarmsTypeDef",
    {"name": str},
    total=False,
)


class ClientCreateDeploymentGroupalarmConfigurationalarmsTypeDef(
    _ClientCreateDeploymentGroupalarmConfigurationalarmsTypeDef
):
    """
    Type definition for `ClientCreateDeploymentGroupalarmConfiguration` `alarms`

    Information about an alarm.

    - **name** *(string) --*

      The name of the alarm. Maximum length is 255 characters. Each alarm name can be used only
      once in a list of alarms.
    """


_ClientCreateDeploymentGroupalarmConfigurationTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupalarmConfigurationTypeDef",
    {
        "enabled": bool,
        "ignorePollAlarmFailure": bool,
        "alarms": List[ClientCreateDeploymentGroupalarmConfigurationalarmsTypeDef],
    },
    total=False,
)


class ClientCreateDeploymentGroupalarmConfigurationTypeDef(
    _ClientCreateDeploymentGroupalarmConfigurationTypeDef
):
    """
    Type definition for `ClientCreateDeploymentGroup` `alarmConfiguration`

    Information to add about Amazon CloudWatch alarms when the deployment group is created.

    - **enabled** *(boolean) --*

      Indicates whether the alarm configuration is enabled.

    - **ignorePollAlarmFailure** *(boolean) --*

      Indicates whether a deployment should continue if information about the current state of alarms
      cannot be retrieved from Amazon CloudWatch. The default value is false.

      * true: The deployment proceeds even if alarm status information can't be retrieved from Amazon
      CloudWatch.

      * false: The deployment stops if alarm status information can't be retrieved from Amazon
      CloudWatch.

    - **alarms** *(list) --*

      A list of alarms configured for the deployment group. A maximum of 10 alarms can be added to a
      deployment group.

      - *(dict) --*

        Information about an alarm.

        - **name** *(string) --*

          The name of the alarm. Maximum length is 255 characters. Each alarm name can be used only
          once in a list of alarms.
    """


_ClientCreateDeploymentGroupautoRollbackConfigurationTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupautoRollbackConfigurationTypeDef",
    {"enabled": bool, "events": List[str]},
    total=False,
)


class ClientCreateDeploymentGroupautoRollbackConfigurationTypeDef(
    _ClientCreateDeploymentGroupautoRollbackConfigurationTypeDef
):
    """
    Type definition for `ClientCreateDeploymentGroup` `autoRollbackConfiguration`

    Configuration information for an automatic rollback that is added when a deployment group is
    created.

    - **enabled** *(boolean) --*

      Indicates whether a defined automatic rollback configuration is currently enabled.

    - **events** *(list) --*

      The event type or types that trigger a rollback.

      - *(string) --*
    """


_ClientCreateDeploymentGroupblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    {"actionOnTimeout": str, "waitTimeInMinutes": int},
    total=False,
)


class ClientCreateDeploymentGroupblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef(
    _ClientCreateDeploymentGroupblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef
):
    """
    Type definition for `ClientCreateDeploymentGroupblueGreenDeploymentConfiguration` `deploymentReadyOption`

    Information about the action to take when newly provisioned instances are ready to receive
    traffic in a blue/green deployment.

    - **actionOnTimeout** *(string) --*

      Information about when to reroute traffic from an original environment to a replacement
      environment in a blue/green deployment.

      * CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately after the
      new application revision is installed on the instances in the replacement environment.

      * STOP_DEPLOYMENT: Do not register new instances with a load balancer unless traffic
      rerouting is started using  ContinueDeployment . If traffic rerouting is not started before
      the end of the specified wait period, the deployment status is changed to Stopped.

    - **waitTimeInMinutes** *(integer) --*

      The number of minutes to wait before the status of a blue/green deployment is changed to
      Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT option for
      actionOnTimeout
    """


_ClientCreateDeploymentGroupblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    {"action": str},
    total=False,
)


class ClientCreateDeploymentGroupblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef(
    _ClientCreateDeploymentGroupblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef
):
    """
    Type definition for `ClientCreateDeploymentGroupblueGreenDeploymentConfiguration` `greenFleetProvisioningOption`

    Information about how instances are provisioned for a replacement environment in a blue/green
    deployment.

    - **action** *(string) --*

      The method used to add instances to a replacement environment.

      * DISCOVER_EXISTING: Use instances that already exist or will be created manually.

      * COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to define and
      create instances in a new Auto Scaling group.
    """


_ClientCreateDeploymentGroupblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    {"action": str, "terminationWaitTimeInMinutes": int},
    total=False,
)


class ClientCreateDeploymentGroupblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef(
    _ClientCreateDeploymentGroupblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef
):
    """
    Type definition for `ClientCreateDeploymentGroupblueGreenDeploymentConfiguration` `terminateBlueInstancesOnDeploymentSuccess`

    Information about whether to terminate instances in the original fleet during a blue/green
    deployment.

    - **action** *(string) --*

      The action to take on instances in the original environment after a successful blue/green
      deployment.

      * TERMINATE: Instances are terminated after a specified wait time.

      * KEEP_ALIVE: Instances are left running after they are deregistered from the load balancer
      and removed from the deployment group.

    - **terminationWaitTimeInMinutes** *(integer) --*

      For an Amazon EC2 deployment, the number of minutes to wait after a successful blue/green
      deployment before terminating instances from the original environment.

      For an Amazon ECS deployment, the number of minutes before deleting the original (blue) task
      set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the original (blue) task
      set to a replacement (green) task set.

      The maximum setting is 2880 minutes (2 days).
    """


_ClientCreateDeploymentGroupblueGreenDeploymentConfigurationTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupblueGreenDeploymentConfigurationTypeDef",
    {
        "terminateBlueInstancesOnDeploymentSuccess": ClientCreateDeploymentGroupblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef,
        "deploymentReadyOption": ClientCreateDeploymentGroupblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef,
        "greenFleetProvisioningOption": ClientCreateDeploymentGroupblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef,
    },
    total=False,
)


class ClientCreateDeploymentGroupblueGreenDeploymentConfigurationTypeDef(
    _ClientCreateDeploymentGroupblueGreenDeploymentConfigurationTypeDef
):
    """
    Type definition for `ClientCreateDeploymentGroup` `blueGreenDeploymentConfiguration`

    Information about blue/green deployment options for a deployment group.

    - **terminateBlueInstancesOnDeploymentSuccess** *(dict) --*

      Information about whether to terminate instances in the original fleet during a blue/green
      deployment.

      - **action** *(string) --*

        The action to take on instances in the original environment after a successful blue/green
        deployment.

        * TERMINATE: Instances are terminated after a specified wait time.

        * KEEP_ALIVE: Instances are left running after they are deregistered from the load balancer
        and removed from the deployment group.

      - **terminationWaitTimeInMinutes** *(integer) --*

        For an Amazon EC2 deployment, the number of minutes to wait after a successful blue/green
        deployment before terminating instances from the original environment.

        For an Amazon ECS deployment, the number of minutes before deleting the original (blue) task
        set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the original (blue) task
        set to a replacement (green) task set.

        The maximum setting is 2880 minutes (2 days).

    - **deploymentReadyOption** *(dict) --*

      Information about the action to take when newly provisioned instances are ready to receive
      traffic in a blue/green deployment.

      - **actionOnTimeout** *(string) --*

        Information about when to reroute traffic from an original environment to a replacement
        environment in a blue/green deployment.

        * CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately after the
        new application revision is installed on the instances in the replacement environment.

        * STOP_DEPLOYMENT: Do not register new instances with a load balancer unless traffic
        rerouting is started using  ContinueDeployment . If traffic rerouting is not started before
        the end of the specified wait period, the deployment status is changed to Stopped.

      - **waitTimeInMinutes** *(integer) --*

        The number of minutes to wait before the status of a blue/green deployment is changed to
        Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT option for
        actionOnTimeout

    - **greenFleetProvisioningOption** *(dict) --*

      Information about how instances are provisioned for a replacement environment in a blue/green
      deployment.

      - **action** *(string) --*

        The method used to add instances to a replacement environment.

        * DISCOVER_EXISTING: Use instances that already exist or will be created manually.

        * COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to define and
        create instances in a new Auto Scaling group.
    """


_ClientCreateDeploymentGroupdeploymentStyleTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupdeploymentStyleTypeDef",
    {"deploymentType": str, "deploymentOption": str},
    total=False,
)


class ClientCreateDeploymentGroupdeploymentStyleTypeDef(
    _ClientCreateDeploymentGroupdeploymentStyleTypeDef
):
    """
    Type definition for `ClientCreateDeploymentGroup` `deploymentStyle`

    Information about the type of deployment, in-place or blue/green, that you want to run and
    whether to route deployment traffic behind a load balancer.

    - **deploymentType** *(string) --*

      Indicates whether to run an in-place deployment or a blue/green deployment.

    - **deploymentOption** *(string) --*

      Indicates whether to route deployment traffic behind a load balancer.
    """


_ClientCreateDeploymentGroupec2TagFiltersTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupec2TagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": str},
    total=False,
)


class ClientCreateDeploymentGroupec2TagFiltersTypeDef(
    _ClientCreateDeploymentGroupec2TagFiltersTypeDef
):
    """
    Type definition for `ClientCreateDeploymentGroup` `ec2TagFilters`

    Information about an EC2 tag filter.

    - **Key** *(string) --*

      The tag filter key.

    - **Value** *(string) --*

      The tag filter value.

    - **Type** *(string) --*

      The tag filter type:

      * KEY_ONLY: Key only.

      * VALUE_ONLY: Value only.

      * KEY_AND_VALUE: Key and value.
    """


_ClientCreateDeploymentGroupec2TagSetec2TagSetListTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupec2TagSetec2TagSetListTypeDef",
    {"Key": str, "Value": str, "Type": str},
    total=False,
)


class ClientCreateDeploymentGroupec2TagSetec2TagSetListTypeDef(
    _ClientCreateDeploymentGroupec2TagSetec2TagSetListTypeDef
):
    """
    Type definition for `ClientCreateDeploymentGroupec2TagSet` `ec2TagSetList`

    Information about an EC2 tag filter.

    - **Key** *(string) --*

      The tag filter key.

    - **Value** *(string) --*

      The tag filter value.

    - **Type** *(string) --*

      The tag filter type:

      * KEY_ONLY: Key only.

      * VALUE_ONLY: Value only.

      * KEY_AND_VALUE: Key and value.
    """


_ClientCreateDeploymentGroupec2TagSetTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupec2TagSetTypeDef",
    {
        "ec2TagSetList": List[
            List[ClientCreateDeploymentGroupec2TagSetec2TagSetListTypeDef]
        ]
    },
    total=False,
)


class ClientCreateDeploymentGroupec2TagSetTypeDef(
    _ClientCreateDeploymentGroupec2TagSetTypeDef
):
    """
    Type definition for `ClientCreateDeploymentGroup` `ec2TagSet`

    Information about groups of tags applied to EC2 instances. The deployment group includes only EC2
    instances identified by all the tag groups. Cannot be used in the same call as ec2TagFilters.

    - **ec2TagSetList** *(list) --*

      A list that contains other lists of EC2 instance tag groups. For an instance to be included in
      the deployment group, it must be identified by all of the tag groups in the list.

      - *(list) --*

        - *(dict) --*

          Information about an EC2 tag filter.

          - **Key** *(string) --*

            The tag filter key.

          - **Value** *(string) --*

            The tag filter value.

          - **Type** *(string) --*

            The tag filter type:

            * KEY_ONLY: Key only.

            * VALUE_ONLY: Value only.

            * KEY_AND_VALUE: Key and value.
    """


_ClientCreateDeploymentGroupecsServicesTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupecsServicesTypeDef",
    {"serviceName": str, "clusterName": str},
    total=False,
)


class ClientCreateDeploymentGroupecsServicesTypeDef(
    _ClientCreateDeploymentGroupecsServicesTypeDef
):
    """
    Type definition for `ClientCreateDeploymentGroup` `ecsServices`

    Contains the service and cluster names used to identify an Amazon ECS deployment's target.

    - **serviceName** *(string) --*

      The name of the target Amazon ECS service.

    - **clusterName** *(string) --*

      The name of the cluster that the Amazon ECS service is associated with.
    """


_ClientCreateDeploymentGrouploadBalancerInfoelbInfoListTypeDef = TypedDict(
    "_ClientCreateDeploymentGrouploadBalancerInfoelbInfoListTypeDef",
    {"name": str},
    total=False,
)


class ClientCreateDeploymentGrouploadBalancerInfoelbInfoListTypeDef(
    _ClientCreateDeploymentGrouploadBalancerInfoelbInfoListTypeDef
):
    """
    Type definition for `ClientCreateDeploymentGrouploadBalancerInfo` `elbInfoList`

    Information about a load balancer in Elastic Load Balancing to use in a deployment. Instances
    are registered directly with a load balancer, and traffic is routed to the load balancer.

    - **name** *(string) --*

      For blue/green deployments, the name of the load balancer that is used to route traffic
      from original instances to replacement instances in a blue/green deployment. For in-place
      deployments, the name of the load balancer that instances are deregistered from so they are
      not serving traffic during a deployment, and then re-registered with after the deployment
      is complete.
    """


_ClientCreateDeploymentGrouploadBalancerInfotargetGroupInfoListTypeDef = TypedDict(
    "_ClientCreateDeploymentGrouploadBalancerInfotargetGroupInfoListTypeDef",
    {"name": str},
    total=False,
)


class ClientCreateDeploymentGrouploadBalancerInfotargetGroupInfoListTypeDef(
    _ClientCreateDeploymentGrouploadBalancerInfotargetGroupInfoListTypeDef
):
    """
    Type definition for `ClientCreateDeploymentGrouploadBalancerInfo` `targetGroupInfoList`

    Information about a target group in Elastic Load Balancing to use in a deployment. Instances
    are registered as targets in a target group, and traffic is routed to the target group.

    - **name** *(string) --*

      For blue/green deployments, the name of the target group that instances in the original
      environment are deregistered from, and instances in the replacement environment are
      registered with. For in-place deployments, the name of the target group that instances are
      deregistered from, so they are not serving traffic during a deployment, and then
      re-registered with after the deployment is complete.
    """


_ClientCreateDeploymentGrouploadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef = TypedDict(
    "_ClientCreateDeploymentGrouploadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)


class ClientCreateDeploymentGrouploadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef(
    _ClientCreateDeploymentGrouploadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef
):
    """
    Type definition for `ClientCreateDeploymentGrouploadBalancerInfotargetGroupPairInfoList` `prodTrafficRoute`

    The path used by a load balancer to route production traffic when an Amazon ECS deployment
    is complete.

    - **listenerArns** *(list) --*

      The ARN of one listener. The listener identifies the route between a target group and a
      load balancer. This is an array of strings with a maximum size of one.

      - *(string) --*
    """


_ClientCreateDeploymentGrouploadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef = TypedDict(
    "_ClientCreateDeploymentGrouploadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    {"name": str},
    total=False,
)


class ClientCreateDeploymentGrouploadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef(
    _ClientCreateDeploymentGrouploadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef
):
    """
    Type definition for `ClientCreateDeploymentGrouploadBalancerInfotargetGroupPairInfoList` `targetGroups`

    Information about a target group in Elastic Load Balancing to use in a deployment.
    Instances are registered as targets in a target group, and traffic is routed to the
    target group.

    - **name** *(string) --*

      For blue/green deployments, the name of the target group that instances in the original
      environment are deregistered from, and instances in the replacement environment are
      registered with. For in-place deployments, the name of the target group that instances
      are deregistered from, so they are not serving traffic during a deployment, and then
      re-registered with after the deployment is complete.
    """


_ClientCreateDeploymentGrouploadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef = TypedDict(
    "_ClientCreateDeploymentGrouploadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)


class ClientCreateDeploymentGrouploadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef(
    _ClientCreateDeploymentGrouploadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef
):
    """
    Type definition for `ClientCreateDeploymentGrouploadBalancerInfotargetGroupPairInfoList` `testTrafficRoute`

    An optional path used by a load balancer to route test traffic after an Amazon ECS
    deployment. Validation can occur while test traffic is served during a deployment.

    - **listenerArns** *(list) --*

      The ARN of one listener. The listener identifies the route between a target group and a
      load balancer. This is an array of strings with a maximum size of one.

      - *(string) --*
    """


_ClientCreateDeploymentGrouploadBalancerInfotargetGroupPairInfoListTypeDef = TypedDict(
    "_ClientCreateDeploymentGrouploadBalancerInfotargetGroupPairInfoListTypeDef",
    {
        "targetGroups": List[
            ClientCreateDeploymentGrouploadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef
        ],
        "prodTrafficRoute": ClientCreateDeploymentGrouploadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef,
        "testTrafficRoute": ClientCreateDeploymentGrouploadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef,
    },
    total=False,
)


class ClientCreateDeploymentGrouploadBalancerInfotargetGroupPairInfoListTypeDef(
    _ClientCreateDeploymentGrouploadBalancerInfotargetGroupPairInfoListTypeDef
):
    """
    Type definition for `ClientCreateDeploymentGrouploadBalancerInfo` `targetGroupPairInfoList`

    Information about two target groups and how traffic is routed during an Amazon ECS
    deployment. An optional test traffic route can be specified.

    - **targetGroups** *(list) --*

      One pair of target groups. One is associated with the original task set. The second is
      associated with the task set that serves traffic after the deployment is complete.

      - *(dict) --*

        Information about a target group in Elastic Load Balancing to use in a deployment.
        Instances are registered as targets in a target group, and traffic is routed to the
        target group.

        - **name** *(string) --*

          For blue/green deployments, the name of the target group that instances in the original
          environment are deregistered from, and instances in the replacement environment are
          registered with. For in-place deployments, the name of the target group that instances
          are deregistered from, so they are not serving traffic during a deployment, and then
          re-registered with after the deployment is complete.

    - **prodTrafficRoute** *(dict) --*

      The path used by a load balancer to route production traffic when an Amazon ECS deployment
      is complete.

      - **listenerArns** *(list) --*

        The ARN of one listener. The listener identifies the route between a target group and a
        load balancer. This is an array of strings with a maximum size of one.

        - *(string) --*

    - **testTrafficRoute** *(dict) --*

      An optional path used by a load balancer to route test traffic after an Amazon ECS
      deployment. Validation can occur while test traffic is served during a deployment.

      - **listenerArns** *(list) --*

        The ARN of one listener. The listener identifies the route between a target group and a
        load balancer. This is an array of strings with a maximum size of one.

        - *(string) --*
    """


_ClientCreateDeploymentGrouploadBalancerInfoTypeDef = TypedDict(
    "_ClientCreateDeploymentGrouploadBalancerInfoTypeDef",
    {
        "elbInfoList": List[
            ClientCreateDeploymentGrouploadBalancerInfoelbInfoListTypeDef
        ],
        "targetGroupInfoList": List[
            ClientCreateDeploymentGrouploadBalancerInfotargetGroupInfoListTypeDef
        ],
        "targetGroupPairInfoList": List[
            ClientCreateDeploymentGrouploadBalancerInfotargetGroupPairInfoListTypeDef
        ],
    },
    total=False,
)


class ClientCreateDeploymentGrouploadBalancerInfoTypeDef(
    _ClientCreateDeploymentGrouploadBalancerInfoTypeDef
):
    """
    Type definition for `ClientCreateDeploymentGroup` `loadBalancerInfo`

    Information about the load balancer used in a deployment.

    - **elbInfoList** *(list) --*

      An array that contains information about the load balancer to use for load balancing in a
      deployment. In Elastic Load Balancing, load balancers are used with Classic Load Balancers.

      .. note::

        Adding more than one load balancer to the array is not supported.

      - *(dict) --*

        Information about a load balancer in Elastic Load Balancing to use in a deployment. Instances
        are registered directly with a load balancer, and traffic is routed to the load balancer.

        - **name** *(string) --*

          For blue/green deployments, the name of the load balancer that is used to route traffic
          from original instances to replacement instances in a blue/green deployment. For in-place
          deployments, the name of the load balancer that instances are deregistered from so they are
          not serving traffic during a deployment, and then re-registered with after the deployment
          is complete.

    - **targetGroupInfoList** *(list) --*

      An array that contains information about the target group to use for load balancing in a
      deployment. In Elastic Load Balancing, target groups are used with Application Load Balancers.

      .. note::

        Adding more than one target group to the array is not supported.

      - *(dict) --*

        Information about a target group in Elastic Load Balancing to use in a deployment. Instances
        are registered as targets in a target group, and traffic is routed to the target group.

        - **name** *(string) --*

          For blue/green deployments, the name of the target group that instances in the original
          environment are deregistered from, and instances in the replacement environment are
          registered with. For in-place deployments, the name of the target group that instances are
          deregistered from, so they are not serving traffic during a deployment, and then
          re-registered with after the deployment is complete.

    - **targetGroupPairInfoList** *(list) --*

      The target group pair information. This is an array of ``TargeGroupPairInfo`` objects with a
      maximum size of one.

      - *(dict) --*

        Information about two target groups and how traffic is routed during an Amazon ECS
        deployment. An optional test traffic route can be specified.

        - **targetGroups** *(list) --*

          One pair of target groups. One is associated with the original task set. The second is
          associated with the task set that serves traffic after the deployment is complete.

          - *(dict) --*

            Information about a target group in Elastic Load Balancing to use in a deployment.
            Instances are registered as targets in a target group, and traffic is routed to the
            target group.

            - **name** *(string) --*

              For blue/green deployments, the name of the target group that instances in the original
              environment are deregistered from, and instances in the replacement environment are
              registered with. For in-place deployments, the name of the target group that instances
              are deregistered from, so they are not serving traffic during a deployment, and then
              re-registered with after the deployment is complete.

        - **prodTrafficRoute** *(dict) --*

          The path used by a load balancer to route production traffic when an Amazon ECS deployment
          is complete.

          - **listenerArns** *(list) --*

            The ARN of one listener. The listener identifies the route between a target group and a
            load balancer. This is an array of strings with a maximum size of one.

            - *(string) --*

        - **testTrafficRoute** *(dict) --*

          An optional path used by a load balancer to route test traffic after an Amazon ECS
          deployment. Validation can occur while test traffic is served during a deployment.

          - **listenerArns** *(list) --*

            The ARN of one listener. The listener identifies the route between a target group and a
            load balancer. This is an array of strings with a maximum size of one.

            - *(string) --*
    """


_ClientCreateDeploymentGrouponPremisesInstanceTagFiltersTypeDef = TypedDict(
    "_ClientCreateDeploymentGrouponPremisesInstanceTagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": str},
    total=False,
)


class ClientCreateDeploymentGrouponPremisesInstanceTagFiltersTypeDef(
    _ClientCreateDeploymentGrouponPremisesInstanceTagFiltersTypeDef
):
    """
    Type definition for `ClientCreateDeploymentGroup` `onPremisesInstanceTagFilters`

    Information about an on-premises instance tag filter.

    - **Key** *(string) --*

      The on-premises instance tag filter key.

    - **Value** *(string) --*

      The on-premises instance tag filter value.

    - **Type** *(string) --*

      The on-premises instance tag filter type:

      * KEY_ONLY: Key only.

      * VALUE_ONLY: Value only.

      * KEY_AND_VALUE: Key and value.
    """


_ClientCreateDeploymentGrouponPremisesTagSetonPremisesTagSetListTypeDef = TypedDict(
    "_ClientCreateDeploymentGrouponPremisesTagSetonPremisesTagSetListTypeDef",
    {"Key": str, "Value": str, "Type": str},
    total=False,
)


class ClientCreateDeploymentGrouponPremisesTagSetonPremisesTagSetListTypeDef(
    _ClientCreateDeploymentGrouponPremisesTagSetonPremisesTagSetListTypeDef
):
    """
    Type definition for `ClientCreateDeploymentGrouponPremisesTagSet` `onPremisesTagSetList`

    Information about an on-premises instance tag filter.

    - **Key** *(string) --*

      The on-premises instance tag filter key.

    - **Value** *(string) --*

      The on-premises instance tag filter value.

    - **Type** *(string) --*

      The on-premises instance tag filter type:

      * KEY_ONLY: Key only.

      * VALUE_ONLY: Value only.

      * KEY_AND_VALUE: Key and value.
    """


_ClientCreateDeploymentGrouponPremisesTagSetTypeDef = TypedDict(
    "_ClientCreateDeploymentGrouponPremisesTagSetTypeDef",
    {
        "onPremisesTagSetList": List[
            List[ClientCreateDeploymentGrouponPremisesTagSetonPremisesTagSetListTypeDef]
        ]
    },
    total=False,
)


class ClientCreateDeploymentGrouponPremisesTagSetTypeDef(
    _ClientCreateDeploymentGrouponPremisesTagSetTypeDef
):
    """
    Type definition for `ClientCreateDeploymentGroup` `onPremisesTagSet`

    Information about groups of tags applied to on-premises instances. The deployment group includes
    only on-premises instances identified by all of the tag groups. Cannot be used in the same call
    as onPremisesInstanceTagFilters.

    - **onPremisesTagSetList** *(list) --*

      A list that contains other lists of on-premises instance tag groups. For an instance to be
      included in the deployment group, it must be identified by all of the tag groups in the list.

      - *(list) --*

        - *(dict) --*

          Information about an on-premises instance tag filter.

          - **Key** *(string) --*

            The on-premises instance tag filter key.

          - **Value** *(string) --*

            The on-premises instance tag filter value.

          - **Type** *(string) --*

            The on-premises instance tag filter type:

            * KEY_ONLY: Key only.

            * VALUE_ONLY: Value only.

            * KEY_AND_VALUE: Key and value.
    """


_ClientCreateDeploymentGrouptagsTypeDef = TypedDict(
    "_ClientCreateDeploymentGrouptagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateDeploymentGrouptagsTypeDef(_ClientCreateDeploymentGrouptagsTypeDef):
    """
    Type definition for `ClientCreateDeploymentGroup` `tags`

    Information about a tag.

    - **Key** *(string) --*

      The tag's key.

    - **Value** *(string) --*

      The tag's value.
    """


_ClientCreateDeploymentGrouptriggerConfigurationsTypeDef = TypedDict(
    "_ClientCreateDeploymentGrouptriggerConfigurationsTypeDef",
    {"triggerName": str, "triggerTargetArn": str, "triggerEvents": List[str]},
    total=False,
)


class ClientCreateDeploymentGrouptriggerConfigurationsTypeDef(
    _ClientCreateDeploymentGrouptriggerConfigurationsTypeDef
):
    """
    Type definition for `ClientCreateDeploymentGroup` `triggerConfigurations`

    Information about notification triggers for the deployment group.

    - **triggerName** *(string) --*

      The name of the notification trigger.

    - **triggerTargetArn** *(string) --*

      The ARN of the Amazon Simple Notification Service topic through which notifications about
      deployment or instance events are sent.

    - **triggerEvents** *(list) --*

      The event type or types for which notifications are triggered.

      - *(string) --*
    """


_ClientCreateDeploymentResponseTypeDef = TypedDict(
    "_ClientCreateDeploymentResponseTypeDef", {"deploymentId": str}, total=False
)


class ClientCreateDeploymentResponseTypeDef(_ClientCreateDeploymentResponseTypeDef):
    """
    Type definition for `ClientCreateDeployment` `Response`

    Represents the output of a CreateDeployment operation.

    - **deploymentId** *(string) --*

      The unique ID of a deployment.
    """


_ClientCreateDeploymentautoRollbackConfigurationTypeDef = TypedDict(
    "_ClientCreateDeploymentautoRollbackConfigurationTypeDef",
    {"enabled": bool, "events": List[str]},
    total=False,
)


class ClientCreateDeploymentautoRollbackConfigurationTypeDef(
    _ClientCreateDeploymentautoRollbackConfigurationTypeDef
):
    """
    Type definition for `ClientCreateDeployment` `autoRollbackConfiguration`

    Configuration information for an automatic rollback that is added when a deployment is created.

    - **enabled** *(boolean) --*

      Indicates whether a defined automatic rollback configuration is currently enabled.

    - **events** *(list) --*

      The event type or types that trigger a rollback.

      - *(string) --*
    """


_ClientCreateDeploymentrevisionappSpecContentTypeDef = TypedDict(
    "_ClientCreateDeploymentrevisionappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientCreateDeploymentrevisionappSpecContentTypeDef(
    _ClientCreateDeploymentrevisionappSpecContentTypeDef
):
    """
    Type definition for `ClientCreateDeploymentrevision` `appSpecContent`

    The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is
    formatted as JSON or YAML and stored as a RawString.

    - **content** *(string) --*

      The YAML-formatted or JSON-formatted revision string.

      For an AWS Lambda deployment, the content includes a Lambda function name, the alias for its
      original version, and the alias for its replacement version. The deployment shifts traffic
      from the original version of the Lambda function to the replacement version.

      For an Amazon ECS deployment, the content includes the task name, information about the load
      balancer that serves traffic to the container, and more.

      For both types of deployments, the content can specify Lambda functions that run at specified
      hooks, such as ``BeforeInstall`` , during a deployment.

    - **sha256** *(string) --*

      The SHA256 hash value of the revision content.
    """


_ClientCreateDeploymentrevisiongitHubLocationTypeDef = TypedDict(
    "_ClientCreateDeploymentrevisiongitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)


class ClientCreateDeploymentrevisiongitHubLocationTypeDef(
    _ClientCreateDeploymentrevisiongitHubLocationTypeDef
):
    """
    Type definition for `ClientCreateDeploymentrevision` `gitHubLocation`

    Information about the location of application artifacts stored in GitHub.

    - **repository** *(string) --*

      The GitHub account and repository pair that stores a reference to the commit that represents
      the bundled artifacts for the application revision.

      Specified as account/repository.

    - **commitId** *(string) --*

      The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
      application revision.
    """


_ClientCreateDeploymentrevisions3LocationTypeDef = TypedDict(
    "_ClientCreateDeploymentrevisions3LocationTypeDef",
    {"bucket": str, "key": str, "bundleType": str, "version": str, "eTag": str},
    total=False,
)


class ClientCreateDeploymentrevisions3LocationTypeDef(
    _ClientCreateDeploymentrevisions3LocationTypeDef
):
    """
    Type definition for `ClientCreateDeploymentrevision` `s3Location`

    Information about the location of a revision stored in Amazon S3.

    - **bucket** *(string) --*

      The name of the Amazon S3 bucket where the application revision is stored.

    - **key** *(string) --*

      The name of the Amazon S3 object that represents the bundled artifacts for the application
      revision.

    - **bundleType** *(string) --*

      The file type of the application revision. Must be one of the following:

      * tar: A tar archive file.

      * tgz: A compressed tar archive file.

      * zip: A zip archive file.

    - **version** *(string) --*

      A specific version of the Amazon S3 object that represents the bundled artifacts for the
      application revision.

      If the version is not specified, the system uses the most recent version by default.

    - **eTag** *(string) --*

      The ETag of the Amazon S3 object that represents the bundled artifacts for the application
      revision.

      If the ETag is not specified as an input parameter, ETag validation of the object is skipped.
    """


_ClientCreateDeploymentrevisionstringTypeDef = TypedDict(
    "_ClientCreateDeploymentrevisionstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientCreateDeploymentrevisionstringTypeDef(
    _ClientCreateDeploymentrevisionstringTypeDef
):
    """
    Type definition for `ClientCreateDeploymentrevision` `string`

    Information about the location of an AWS Lambda deployment revision stored as a RawString.

    - **content** *(string) --*

      The YAML-formatted or JSON-formatted revision string. It includes information about which
      Lambda function to update and optional Lambda functions that validate deployment lifecycle
      events.

    - **sha256** *(string) --*

      The SHA256 hash value of the revision content.
    """


_ClientCreateDeploymentrevisionTypeDef = TypedDict(
    "_ClientCreateDeploymentrevisionTypeDef",
    {
        "revisionType": str,
        "s3Location": ClientCreateDeploymentrevisions3LocationTypeDef,
        "gitHubLocation": ClientCreateDeploymentrevisiongitHubLocationTypeDef,
        "string": ClientCreateDeploymentrevisionstringTypeDef,
        "appSpecContent": ClientCreateDeploymentrevisionappSpecContentTypeDef,
    },
    total=False,
)


class ClientCreateDeploymentrevisionTypeDef(_ClientCreateDeploymentrevisionTypeDef):
    """
    Type definition for `ClientCreateDeployment` `revision`

    The type and location of the revision to deploy.

    - **revisionType** *(string) --*

      The type of application revision:

      * S3: An application revision stored in Amazon S3.

      * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

      * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

    - **s3Location** *(dict) --*

      Information about the location of a revision stored in Amazon S3.

      - **bucket** *(string) --*

        The name of the Amazon S3 bucket where the application revision is stored.

      - **key** *(string) --*

        The name of the Amazon S3 object that represents the bundled artifacts for the application
        revision.

      - **bundleType** *(string) --*

        The file type of the application revision. Must be one of the following:

        * tar: A tar archive file.

        * tgz: A compressed tar archive file.

        * zip: A zip archive file.

      - **version** *(string) --*

        A specific version of the Amazon S3 object that represents the bundled artifacts for the
        application revision.

        If the version is not specified, the system uses the most recent version by default.

      - **eTag** *(string) --*

        The ETag of the Amazon S3 object that represents the bundled artifacts for the application
        revision.

        If the ETag is not specified as an input parameter, ETag validation of the object is skipped.

    - **gitHubLocation** *(dict) --*

      Information about the location of application artifacts stored in GitHub.

      - **repository** *(string) --*

        The GitHub account and repository pair that stores a reference to the commit that represents
        the bundled artifacts for the application revision.

        Specified as account/repository.

      - **commitId** *(string) --*

        The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
        application revision.

    - **string** *(dict) --*

      Information about the location of an AWS Lambda deployment revision stored as a RawString.

      - **content** *(string) --*

        The YAML-formatted or JSON-formatted revision string. It includes information about which
        Lambda function to update and optional Lambda functions that validate deployment lifecycle
        events.

      - **sha256** *(string) --*

        The SHA256 hash value of the revision content.

    - **appSpecContent** *(dict) --*

      The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is
      formatted as JSON or YAML and stored as a RawString.

      - **content** *(string) --*

        The YAML-formatted or JSON-formatted revision string.

        For an AWS Lambda deployment, the content includes a Lambda function name, the alias for its
        original version, and the alias for its replacement version. The deployment shifts traffic
        from the original version of the Lambda function to the replacement version.

        For an Amazon ECS deployment, the content includes the task name, information about the load
        balancer that serves traffic to the container, and more.

        For both types of deployments, the content can specify Lambda functions that run at specified
        hooks, such as ``BeforeInstall`` , during a deployment.

      - **sha256** *(string) --*

        The SHA256 hash value of the revision content.
    """


_ClientCreateDeploymenttargetInstancesec2TagSetec2TagSetListTypeDef = TypedDict(
    "_ClientCreateDeploymenttargetInstancesec2TagSetec2TagSetListTypeDef",
    {"Key": str, "Value": str, "Type": str},
    total=False,
)


class ClientCreateDeploymenttargetInstancesec2TagSetec2TagSetListTypeDef(
    _ClientCreateDeploymenttargetInstancesec2TagSetec2TagSetListTypeDef
):
    """
    Type definition for `ClientCreateDeploymenttargetInstancesec2TagSet` `ec2TagSetList`

    Information about an EC2 tag filter.

    - **Key** *(string) --*

      The tag filter key.

    - **Value** *(string) --*

      The tag filter value.

    - **Type** *(string) --*

      The tag filter type:

      * KEY_ONLY: Key only.

      * VALUE_ONLY: Value only.

      * KEY_AND_VALUE: Key and value.
    """


_ClientCreateDeploymenttargetInstancesec2TagSetTypeDef = TypedDict(
    "_ClientCreateDeploymenttargetInstancesec2TagSetTypeDef",
    {
        "ec2TagSetList": List[
            List[ClientCreateDeploymenttargetInstancesec2TagSetec2TagSetListTypeDef]
        ]
    },
    total=False,
)


class ClientCreateDeploymenttargetInstancesec2TagSetTypeDef(
    _ClientCreateDeploymenttargetInstancesec2TagSetTypeDef
):
    """
    Type definition for `ClientCreateDeploymenttargetInstances` `ec2TagSet`

    Information about the groups of EC2 instance tags that an instance must be identified by in
    order for it to be included in the replacement environment for a blue/green deployment. Cannot
    be used in the same call as tagFilters.

    - **ec2TagSetList** *(list) --*

      A list that contains other lists of EC2 instance tag groups. For an instance to be included
      in the deployment group, it must be identified by all of the tag groups in the list.

      - *(list) --*

        - *(dict) --*

          Information about an EC2 tag filter.

          - **Key** *(string) --*

            The tag filter key.

          - **Value** *(string) --*

            The tag filter value.

          - **Type** *(string) --*

            The tag filter type:

            * KEY_ONLY: Key only.

            * VALUE_ONLY: Value only.

            * KEY_AND_VALUE: Key and value.
    """


_ClientCreateDeploymenttargetInstancestagFiltersTypeDef = TypedDict(
    "_ClientCreateDeploymenttargetInstancestagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": str},
    total=False,
)


class ClientCreateDeploymenttargetInstancestagFiltersTypeDef(
    _ClientCreateDeploymenttargetInstancestagFiltersTypeDef
):
    """
    Type definition for `ClientCreateDeploymenttargetInstances` `tagFilters`

    Information about an EC2 tag filter.

    - **Key** *(string) --*

      The tag filter key.

    - **Value** *(string) --*

      The tag filter value.

    - **Type** *(string) --*

      The tag filter type:

      * KEY_ONLY: Key only.

      * VALUE_ONLY: Value only.

      * KEY_AND_VALUE: Key and value.
    """


_ClientCreateDeploymenttargetInstancesTypeDef = TypedDict(
    "_ClientCreateDeploymenttargetInstancesTypeDef",
    {
        "tagFilters": List[ClientCreateDeploymenttargetInstancestagFiltersTypeDef],
        "autoScalingGroups": List[str],
        "ec2TagSet": ClientCreateDeploymenttargetInstancesec2TagSetTypeDef,
    },
    total=False,
)


class ClientCreateDeploymenttargetInstancesTypeDef(
    _ClientCreateDeploymenttargetInstancesTypeDef
):
    """
    Type definition for `ClientCreateDeployment` `targetInstances`

    Information about the instances that belong to the replacement environment in a blue/green
    deployment.

    - **tagFilters** *(list) --*

      The tag filter key, type, and value used to identify Amazon EC2 instances in a replacement
      environment for a blue/green deployment. Cannot be used in the same call as ec2TagSet.

      - *(dict) --*

        Information about an EC2 tag filter.

        - **Key** *(string) --*

          The tag filter key.

        - **Value** *(string) --*

          The tag filter value.

        - **Type** *(string) --*

          The tag filter type:

          * KEY_ONLY: Key only.

          * VALUE_ONLY: Value only.

          * KEY_AND_VALUE: Key and value.

    - **autoScalingGroups** *(list) --*

      The names of one or more Auto Scaling groups to identify a replacement environment for a
      blue/green deployment.

      - *(string) --*

    - **ec2TagSet** *(dict) --*

      Information about the groups of EC2 instance tags that an instance must be identified by in
      order for it to be included in the replacement environment for a blue/green deployment. Cannot
      be used in the same call as tagFilters.

      - **ec2TagSetList** *(list) --*

        A list that contains other lists of EC2 instance tag groups. For an instance to be included
        in the deployment group, it must be identified by all of the tag groups in the list.

        - *(list) --*

          - *(dict) --*

            Information about an EC2 tag filter.

            - **Key** *(string) --*

              The tag filter key.

            - **Value** *(string) --*

              The tag filter value.

            - **Type** *(string) --*

              The tag filter type:

              * KEY_ONLY: Key only.

              * VALUE_ONLY: Value only.

              * KEY_AND_VALUE: Key and value.
    """


_ClientDeleteDeploymentGroupResponsehooksNotCleanedUpTypeDef = TypedDict(
    "_ClientDeleteDeploymentGroupResponsehooksNotCleanedUpTypeDef",
    {"name": str, "hook": str},
    total=False,
)


class ClientDeleteDeploymentGroupResponsehooksNotCleanedUpTypeDef(
    _ClientDeleteDeploymentGroupResponsehooksNotCleanedUpTypeDef
):
    """
    Type definition for `ClientDeleteDeploymentGroupResponse` `hooksNotCleanedUp`

    Information about an Auto Scaling group.

    - **name** *(string) --*

      The Auto Scaling group name.

    - **hook** *(string) --*

      An Auto Scaling lifecycle event hook name.
    """


_ClientDeleteDeploymentGroupResponseTypeDef = TypedDict(
    "_ClientDeleteDeploymentGroupResponseTypeDef",
    {
        "hooksNotCleanedUp": List[
            ClientDeleteDeploymentGroupResponsehooksNotCleanedUpTypeDef
        ]
    },
    total=False,
)


class ClientDeleteDeploymentGroupResponseTypeDef(
    _ClientDeleteDeploymentGroupResponseTypeDef
):
    """
    Type definition for `ClientDeleteDeploymentGroup` `Response`

    Represents the output of a DeleteDeploymentGroup operation.

    - **hooksNotCleanedUp** *(list) --*

      If the output contains no data, and the corresponding deployment group contained at least one
      Auto Scaling group, AWS CodeDeploy successfully removed all corresponding Auto Scaling
      lifecycle event hooks from the Amazon EC2 instances in the Auto Scaling group. If the output
      contains data, AWS CodeDeploy could not remove some Auto Scaling lifecycle event hooks from
      the Amazon EC2 instances in the Auto Scaling group.

      - *(dict) --*

        Information about an Auto Scaling group.

        - **name** *(string) --*

          The Auto Scaling group name.

        - **hook** *(string) --*

          An Auto Scaling lifecycle event hook name.
    """


_ClientDeleteGitHubAccountTokenResponseTypeDef = TypedDict(
    "_ClientDeleteGitHubAccountTokenResponseTypeDef", {"tokenName": str}, total=False
)


class ClientDeleteGitHubAccountTokenResponseTypeDef(
    _ClientDeleteGitHubAccountTokenResponseTypeDef
):
    """
    Type definition for `ClientDeleteGitHubAccountToken` `Response`

    Represents the output of a DeleteGitHubAccountToken operation.

    - **tokenName** *(string) --*

      The name of the GitHub account connection that was deleted.
    """


_ClientGetApplicationResponseapplicationTypeDef = TypedDict(
    "_ClientGetApplicationResponseapplicationTypeDef",
    {
        "applicationId": str,
        "applicationName": str,
        "createTime": datetime,
        "linkedToGitHub": bool,
        "gitHubAccountName": str,
        "computePlatform": str,
    },
    total=False,
)


class ClientGetApplicationResponseapplicationTypeDef(
    _ClientGetApplicationResponseapplicationTypeDef
):
    """
    Type definition for `ClientGetApplicationResponse` `application`

    Information about the application.

    - **applicationId** *(string) --*

      The application ID.

    - **applicationName** *(string) --*

      The application name.

    - **createTime** *(datetime) --*

      The time at which the application was created.

    - **linkedToGitHub** *(boolean) --*

      True if the user has authenticated with GitHub for the specified application. Otherwise,
      false.

    - **gitHubAccountName** *(string) --*

      The name for a connection to a GitHub account.

    - **computePlatform** *(string) --*

      The destination platform type for deployment of the application (``Lambda`` or ``Server`` ).
    """


_ClientGetApplicationResponseTypeDef = TypedDict(
    "_ClientGetApplicationResponseTypeDef",
    {"application": ClientGetApplicationResponseapplicationTypeDef},
    total=False,
)


class ClientGetApplicationResponseTypeDef(_ClientGetApplicationResponseTypeDef):
    """
    Type definition for `ClientGetApplication` `Response`

    Represents the output of a GetApplication operation.

    - **application** *(dict) --*

      Information about the application.

      - **applicationId** *(string) --*

        The application ID.

      - **applicationName** *(string) --*

        The application name.

      - **createTime** *(datetime) --*

        The time at which the application was created.

      - **linkedToGitHub** *(boolean) --*

        True if the user has authenticated with GitHub for the specified application. Otherwise,
        false.

      - **gitHubAccountName** *(string) --*

        The name for a connection to a GitHub account.

      - **computePlatform** *(string) --*

        The destination platform type for deployment of the application (``Lambda`` or ``Server`` ).
    """


_ClientGetApplicationRevisionResponserevisionInfoTypeDef = TypedDict(
    "_ClientGetApplicationRevisionResponserevisionInfoTypeDef",
    {
        "description": str,
        "deploymentGroups": List[str],
        "firstUsedTime": datetime,
        "lastUsedTime": datetime,
        "registerTime": datetime,
    },
    total=False,
)


class ClientGetApplicationRevisionResponserevisionInfoTypeDef(
    _ClientGetApplicationRevisionResponserevisionInfoTypeDef
):
    """
    Type definition for `ClientGetApplicationRevisionResponse` `revisionInfo`

    General information about the revision.

    - **description** *(string) --*

      A comment about the revision.

    - **deploymentGroups** *(list) --*

      The deployment groups for which this is the current target revision.

      - *(string) --*

    - **firstUsedTime** *(datetime) --*

      When the revision was first used by AWS CodeDeploy.

    - **lastUsedTime** *(datetime) --*

      When the revision was last used by AWS CodeDeploy.

    - **registerTime** *(datetime) --*

      When the revision was registered with AWS CodeDeploy.
    """


_ClientGetApplicationRevisionResponserevisionappSpecContentTypeDef = TypedDict(
    "_ClientGetApplicationRevisionResponserevisionappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientGetApplicationRevisionResponserevisionappSpecContentTypeDef(
    _ClientGetApplicationRevisionResponserevisionappSpecContentTypeDef
):
    """
    Type definition for `ClientGetApplicationRevisionResponserevision` `appSpecContent`

    The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is
    formatted as JSON or YAML and stored as a RawString.

    - **content** *(string) --*

      The YAML-formatted or JSON-formatted revision string.

      For an AWS Lambda deployment, the content includes a Lambda function name, the alias for
      its original version, and the alias for its replacement version. The deployment shifts
      traffic from the original version of the Lambda function to the replacement version.

      For an Amazon ECS deployment, the content includes the task name, information about the
      load balancer that serves traffic to the container, and more.

      For both types of deployments, the content can specify Lambda functions that run at
      specified hooks, such as ``BeforeInstall`` , during a deployment.

    - **sha256** *(string) --*

      The SHA256 hash value of the revision content.
    """


_ClientGetApplicationRevisionResponserevisiongitHubLocationTypeDef = TypedDict(
    "_ClientGetApplicationRevisionResponserevisiongitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)


class ClientGetApplicationRevisionResponserevisiongitHubLocationTypeDef(
    _ClientGetApplicationRevisionResponserevisiongitHubLocationTypeDef
):
    """
    Type definition for `ClientGetApplicationRevisionResponserevision` `gitHubLocation`

    Information about the location of application artifacts stored in GitHub.

    - **repository** *(string) --*

      The GitHub account and repository pair that stores a reference to the commit that
      represents the bundled artifacts for the application revision.

      Specified as account/repository.

    - **commitId** *(string) --*

      The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
      application revision.
    """


_ClientGetApplicationRevisionResponserevisions3LocationTypeDef = TypedDict(
    "_ClientGetApplicationRevisionResponserevisions3LocationTypeDef",
    {"bucket": str, "key": str, "bundleType": str, "version": str, "eTag": str},
    total=False,
)


class ClientGetApplicationRevisionResponserevisions3LocationTypeDef(
    _ClientGetApplicationRevisionResponserevisions3LocationTypeDef
):
    """
    Type definition for `ClientGetApplicationRevisionResponserevision` `s3Location`

    Information about the location of a revision stored in Amazon S3.

    - **bucket** *(string) --*

      The name of the Amazon S3 bucket where the application revision is stored.

    - **key** *(string) --*

      The name of the Amazon S3 object that represents the bundled artifacts for the
      application revision.

    - **bundleType** *(string) --*

      The file type of the application revision. Must be one of the following:

      * tar: A tar archive file.

      * tgz: A compressed tar archive file.

      * zip: A zip archive file.

    - **version** *(string) --*

      A specific version of the Amazon S3 object that represents the bundled artifacts for the
      application revision.

      If the version is not specified, the system uses the most recent version by default.

    - **eTag** *(string) --*

      The ETag of the Amazon S3 object that represents the bundled artifacts for the
      application revision.

      If the ETag is not specified as an input parameter, ETag validation of the object is
      skipped.
    """


_ClientGetApplicationRevisionResponserevisionstringTypeDef = TypedDict(
    "_ClientGetApplicationRevisionResponserevisionstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientGetApplicationRevisionResponserevisionstringTypeDef(
    _ClientGetApplicationRevisionResponserevisionstringTypeDef
):
    """
    Type definition for `ClientGetApplicationRevisionResponserevision` `string`

    Information about the location of an AWS Lambda deployment revision stored as a RawString.

    - **content** *(string) --*

      The YAML-formatted or JSON-formatted revision string. It includes information about which
      Lambda function to update and optional Lambda functions that validate deployment
      lifecycle events.

    - **sha256** *(string) --*

      The SHA256 hash value of the revision content.
    """


_ClientGetApplicationRevisionResponserevisionTypeDef = TypedDict(
    "_ClientGetApplicationRevisionResponserevisionTypeDef",
    {
        "revisionType": str,
        "s3Location": ClientGetApplicationRevisionResponserevisions3LocationTypeDef,
        "gitHubLocation": ClientGetApplicationRevisionResponserevisiongitHubLocationTypeDef,
        "string": ClientGetApplicationRevisionResponserevisionstringTypeDef,
        "appSpecContent": ClientGetApplicationRevisionResponserevisionappSpecContentTypeDef,
    },
    total=False,
)


class ClientGetApplicationRevisionResponserevisionTypeDef(
    _ClientGetApplicationRevisionResponserevisionTypeDef
):
    """
    Type definition for `ClientGetApplicationRevisionResponse` `revision`

    Additional information about the revision, including type and location.

    - **revisionType** *(string) --*

      The type of application revision:

      * S3: An application revision stored in Amazon S3.

      * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

      * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

    - **s3Location** *(dict) --*

      Information about the location of a revision stored in Amazon S3.

      - **bucket** *(string) --*

        The name of the Amazon S3 bucket where the application revision is stored.

      - **key** *(string) --*

        The name of the Amazon S3 object that represents the bundled artifacts for the
        application revision.

      - **bundleType** *(string) --*

        The file type of the application revision. Must be one of the following:

        * tar: A tar archive file.

        * tgz: A compressed tar archive file.

        * zip: A zip archive file.

      - **version** *(string) --*

        A specific version of the Amazon S3 object that represents the bundled artifacts for the
        application revision.

        If the version is not specified, the system uses the most recent version by default.

      - **eTag** *(string) --*

        The ETag of the Amazon S3 object that represents the bundled artifacts for the
        application revision.

        If the ETag is not specified as an input parameter, ETag validation of the object is
        skipped.

    - **gitHubLocation** *(dict) --*

      Information about the location of application artifacts stored in GitHub.

      - **repository** *(string) --*

        The GitHub account and repository pair that stores a reference to the commit that
        represents the bundled artifacts for the application revision.

        Specified as account/repository.

      - **commitId** *(string) --*

        The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
        application revision.

    - **string** *(dict) --*

      Information about the location of an AWS Lambda deployment revision stored as a RawString.

      - **content** *(string) --*

        The YAML-formatted or JSON-formatted revision string. It includes information about which
        Lambda function to update and optional Lambda functions that validate deployment
        lifecycle events.

      - **sha256** *(string) --*

        The SHA256 hash value of the revision content.

    - **appSpecContent** *(dict) --*

      The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is
      formatted as JSON or YAML and stored as a RawString.

      - **content** *(string) --*

        The YAML-formatted or JSON-formatted revision string.

        For an AWS Lambda deployment, the content includes a Lambda function name, the alias for
        its original version, and the alias for its replacement version. The deployment shifts
        traffic from the original version of the Lambda function to the replacement version.

        For an Amazon ECS deployment, the content includes the task name, information about the
        load balancer that serves traffic to the container, and more.

        For both types of deployments, the content can specify Lambda functions that run at
        specified hooks, such as ``BeforeInstall`` , during a deployment.

      - **sha256** *(string) --*

        The SHA256 hash value of the revision content.
    """


_ClientGetApplicationRevisionResponseTypeDef = TypedDict(
    "_ClientGetApplicationRevisionResponseTypeDef",
    {
        "applicationName": str,
        "revision": ClientGetApplicationRevisionResponserevisionTypeDef,
        "revisionInfo": ClientGetApplicationRevisionResponserevisionInfoTypeDef,
    },
    total=False,
)


class ClientGetApplicationRevisionResponseTypeDef(
    _ClientGetApplicationRevisionResponseTypeDef
):
    """
    Type definition for `ClientGetApplicationRevision` `Response`

    Represents the output of a GetApplicationRevision operation.

    - **applicationName** *(string) --*

      The name of the application that corresponds to the revision.

    - **revision** *(dict) --*

      Additional information about the revision, including type and location.

      - **revisionType** *(string) --*

        The type of application revision:

        * S3: An application revision stored in Amazon S3.

        * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

        * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

      - **s3Location** *(dict) --*

        Information about the location of a revision stored in Amazon S3.

        - **bucket** *(string) --*

          The name of the Amazon S3 bucket where the application revision is stored.

        - **key** *(string) --*

          The name of the Amazon S3 object that represents the bundled artifacts for the
          application revision.

        - **bundleType** *(string) --*

          The file type of the application revision. Must be one of the following:

          * tar: A tar archive file.

          * tgz: A compressed tar archive file.

          * zip: A zip archive file.

        - **version** *(string) --*

          A specific version of the Amazon S3 object that represents the bundled artifacts for the
          application revision.

          If the version is not specified, the system uses the most recent version by default.

        - **eTag** *(string) --*

          The ETag of the Amazon S3 object that represents the bundled artifacts for the
          application revision.

          If the ETag is not specified as an input parameter, ETag validation of the object is
          skipped.

      - **gitHubLocation** *(dict) --*

        Information about the location of application artifacts stored in GitHub.

        - **repository** *(string) --*

          The GitHub account and repository pair that stores a reference to the commit that
          represents the bundled artifacts for the application revision.

          Specified as account/repository.

        - **commitId** *(string) --*

          The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
          application revision.

      - **string** *(dict) --*

        Information about the location of an AWS Lambda deployment revision stored as a RawString.

        - **content** *(string) --*

          The YAML-formatted or JSON-formatted revision string. It includes information about which
          Lambda function to update and optional Lambda functions that validate deployment
          lifecycle events.

        - **sha256** *(string) --*

          The SHA256 hash value of the revision content.

      - **appSpecContent** *(dict) --*

        The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is
        formatted as JSON or YAML and stored as a RawString.

        - **content** *(string) --*

          The YAML-formatted or JSON-formatted revision string.

          For an AWS Lambda deployment, the content includes a Lambda function name, the alias for
          its original version, and the alias for its replacement version. The deployment shifts
          traffic from the original version of the Lambda function to the replacement version.

          For an Amazon ECS deployment, the content includes the task name, information about the
          load balancer that serves traffic to the container, and more.

          For both types of deployments, the content can specify Lambda functions that run at
          specified hooks, such as ``BeforeInstall`` , during a deployment.

        - **sha256** *(string) --*

          The SHA256 hash value of the revision content.

    - **revisionInfo** *(dict) --*

      General information about the revision.

      - **description** *(string) --*

        A comment about the revision.

      - **deploymentGroups** *(list) --*

        The deployment groups for which this is the current target revision.

        - *(string) --*

      - **firstUsedTime** *(datetime) --*

        When the revision was first used by AWS CodeDeploy.

      - **lastUsedTime** *(datetime) --*

        When the revision was last used by AWS CodeDeploy.

      - **registerTime** *(datetime) --*

        When the revision was registered with AWS CodeDeploy.
    """


_ClientGetApplicationRevisionrevisionappSpecContentTypeDef = TypedDict(
    "_ClientGetApplicationRevisionrevisionappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientGetApplicationRevisionrevisionappSpecContentTypeDef(
    _ClientGetApplicationRevisionrevisionappSpecContentTypeDef
):
    """
    Type definition for `ClientGetApplicationRevisionrevision` `appSpecContent`

    The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is
    formatted as JSON or YAML and stored as a RawString.

    - **content** *(string) --*

      The YAML-formatted or JSON-formatted revision string.

      For an AWS Lambda deployment, the content includes a Lambda function name, the alias for its
      original version, and the alias for its replacement version. The deployment shifts traffic
      from the original version of the Lambda function to the replacement version.

      For an Amazon ECS deployment, the content includes the task name, information about the load
      balancer that serves traffic to the container, and more.

      For both types of deployments, the content can specify Lambda functions that run at specified
      hooks, such as ``BeforeInstall`` , during a deployment.

    - **sha256** *(string) --*

      The SHA256 hash value of the revision content.
    """


_ClientGetApplicationRevisionrevisiongitHubLocationTypeDef = TypedDict(
    "_ClientGetApplicationRevisionrevisiongitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)


class ClientGetApplicationRevisionrevisiongitHubLocationTypeDef(
    _ClientGetApplicationRevisionrevisiongitHubLocationTypeDef
):
    """
    Type definition for `ClientGetApplicationRevisionrevision` `gitHubLocation`

    Information about the location of application artifacts stored in GitHub.

    - **repository** *(string) --*

      The GitHub account and repository pair that stores a reference to the commit that represents
      the bundled artifacts for the application revision.

      Specified as account/repository.

    - **commitId** *(string) --*

      The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
      application revision.
    """


_ClientGetApplicationRevisionrevisions3LocationTypeDef = TypedDict(
    "_ClientGetApplicationRevisionrevisions3LocationTypeDef",
    {"bucket": str, "key": str, "bundleType": str, "version": str, "eTag": str},
    total=False,
)


class ClientGetApplicationRevisionrevisions3LocationTypeDef(
    _ClientGetApplicationRevisionrevisions3LocationTypeDef
):
    """
    Type definition for `ClientGetApplicationRevisionrevision` `s3Location`

    Information about the location of a revision stored in Amazon S3.

    - **bucket** *(string) --*

      The name of the Amazon S3 bucket where the application revision is stored.

    - **key** *(string) --*

      The name of the Amazon S3 object that represents the bundled artifacts for the application
      revision.

    - **bundleType** *(string) --*

      The file type of the application revision. Must be one of the following:

      * tar: A tar archive file.

      * tgz: A compressed tar archive file.

      * zip: A zip archive file.

    - **version** *(string) --*

      A specific version of the Amazon S3 object that represents the bundled artifacts for the
      application revision.

      If the version is not specified, the system uses the most recent version by default.

    - **eTag** *(string) --*

      The ETag of the Amazon S3 object that represents the bundled artifacts for the application
      revision.

      If the ETag is not specified as an input parameter, ETag validation of the object is skipped.
    """


_ClientGetApplicationRevisionrevisionstringTypeDef = TypedDict(
    "_ClientGetApplicationRevisionrevisionstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientGetApplicationRevisionrevisionstringTypeDef(
    _ClientGetApplicationRevisionrevisionstringTypeDef
):
    """
    Type definition for `ClientGetApplicationRevisionrevision` `string`

    Information about the location of an AWS Lambda deployment revision stored as a RawString.

    - **content** *(string) --*

      The YAML-formatted or JSON-formatted revision string. It includes information about which
      Lambda function to update and optional Lambda functions that validate deployment lifecycle
      events.

    - **sha256** *(string) --*

      The SHA256 hash value of the revision content.
    """


_ClientGetApplicationRevisionrevisionTypeDef = TypedDict(
    "_ClientGetApplicationRevisionrevisionTypeDef",
    {
        "revisionType": str,
        "s3Location": ClientGetApplicationRevisionrevisions3LocationTypeDef,
        "gitHubLocation": ClientGetApplicationRevisionrevisiongitHubLocationTypeDef,
        "string": ClientGetApplicationRevisionrevisionstringTypeDef,
        "appSpecContent": ClientGetApplicationRevisionrevisionappSpecContentTypeDef,
    },
    total=False,
)


class ClientGetApplicationRevisionrevisionTypeDef(
    _ClientGetApplicationRevisionrevisionTypeDef
):
    """
    Type definition for `ClientGetApplicationRevision` `revision`

    Information about the application revision to get, including type and location.

    - **revisionType** *(string) --*

      The type of application revision:

      * S3: An application revision stored in Amazon S3.

      * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

      * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

    - **s3Location** *(dict) --*

      Information about the location of a revision stored in Amazon S3.

      - **bucket** *(string) --*

        The name of the Amazon S3 bucket where the application revision is stored.

      - **key** *(string) --*

        The name of the Amazon S3 object that represents the bundled artifacts for the application
        revision.

      - **bundleType** *(string) --*

        The file type of the application revision. Must be one of the following:

        * tar: A tar archive file.

        * tgz: A compressed tar archive file.

        * zip: A zip archive file.

      - **version** *(string) --*

        A specific version of the Amazon S3 object that represents the bundled artifacts for the
        application revision.

        If the version is not specified, the system uses the most recent version by default.

      - **eTag** *(string) --*

        The ETag of the Amazon S3 object that represents the bundled artifacts for the application
        revision.

        If the ETag is not specified as an input parameter, ETag validation of the object is skipped.

    - **gitHubLocation** *(dict) --*

      Information about the location of application artifacts stored in GitHub.

      - **repository** *(string) --*

        The GitHub account and repository pair that stores a reference to the commit that represents
        the bundled artifacts for the application revision.

        Specified as account/repository.

      - **commitId** *(string) --*

        The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
        application revision.

    - **string** *(dict) --*

      Information about the location of an AWS Lambda deployment revision stored as a RawString.

      - **content** *(string) --*

        The YAML-formatted or JSON-formatted revision string. It includes information about which
        Lambda function to update and optional Lambda functions that validate deployment lifecycle
        events.

      - **sha256** *(string) --*

        The SHA256 hash value of the revision content.

    - **appSpecContent** *(dict) --*

      The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is
      formatted as JSON or YAML and stored as a RawString.

      - **content** *(string) --*

        The YAML-formatted or JSON-formatted revision string.

        For an AWS Lambda deployment, the content includes a Lambda function name, the alias for its
        original version, and the alias for its replacement version. The deployment shifts traffic
        from the original version of the Lambda function to the replacement version.

        For an Amazon ECS deployment, the content includes the task name, information about the load
        balancer that serves traffic to the container, and more.

        For both types of deployments, the content can specify Lambda functions that run at specified
        hooks, such as ``BeforeInstall`` , during a deployment.

      - **sha256** *(string) --*

        The SHA256 hash value of the revision content.
    """


_ClientGetDeploymentConfigResponsedeploymentConfigInfominimumHealthyHostsTypeDef = TypedDict(
    "_ClientGetDeploymentConfigResponsedeploymentConfigInfominimumHealthyHostsTypeDef",
    {"value": int, "type": str},
    total=False,
)


class ClientGetDeploymentConfigResponsedeploymentConfigInfominimumHealthyHostsTypeDef(
    _ClientGetDeploymentConfigResponsedeploymentConfigInfominimumHealthyHostsTypeDef
):
    """
    Type definition for `ClientGetDeploymentConfigResponsedeploymentConfigInfo` `minimumHealthyHosts`

    Information about the number or percentage of minimum healthy instance.

    - **value** *(integer) --*

      The minimum healthy instance value.

    - **type** *(string) --*

      The minimum healthy instance type:

      * HOST_COUNT: The minimum number of healthy instance as an absolute value.

      * FLEET_PERCENT: The minimum number of healthy instance as a percentage of the total
      number of instance in the deployment.

      In an example of nine instance, if a HOST_COUNT of six is specified, deploy to up to
      three instances at a time. The deployment is successful if six or more instances are
      deployed to successfully. Otherwise, the deployment fails. If a FLEET_PERCENT of 40 is
      specified, deploy to up to five instance at a time. The deployment is successful if four
      or more instance are deployed to successfully. Otherwise, the deployment fails.

      .. note::

        In a call to the ``GetDeploymentConfig`` , CodeDeployDefault.OneAtATime returns a
        minimum healthy instance type of MOST_CONCURRENCY and a value of 1. This means a
        deployment to only one instance at a time. (You cannot set the type to
        MOST_CONCURRENCY, only to HOST_COUNT or FLEET_PERCENT.) In addition, with
        CodeDeployDefault.OneAtATime, AWS CodeDeploy attempts to ensure that all instances but
        one are kept in a healthy state during the deployment. Although this allows one
        instance at a time to be taken offline for a new deployment, it also means that if the
        deployment to the last instance fails, the overall deployment is still successful.

      For more information, see `AWS CodeDeploy Instance Health
      <https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-health.html>`__ in the
      *AWS CodeDeploy User Guide* .
    """


_ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigtimeBasedCanaryTypeDef = TypedDict(
    "_ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigtimeBasedCanaryTypeDef",
    {"canaryPercentage": int, "canaryInterval": int},
    total=False,
)


class ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigtimeBasedCanaryTypeDef(
    _ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigtimeBasedCanaryTypeDef
):
    """
    Type definition for `ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfig` `timeBasedCanary`

    A configuration that shifts traffic from one version of a Lambda function to another in
    two increments. The original and target Lambda function versions are specified in the
    deployment's AppSpec file.

    - **canaryPercentage** *(integer) --*

      The percentage of traffic to shift in the first increment of a ``TimeBasedCanary``
      deployment.

    - **canaryInterval** *(integer) --*

      The number of minutes between the first and second traffic shifts of a
      ``TimeBasedCanary`` deployment.
    """


_ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigtimeBasedLinearTypeDef = TypedDict(
    "_ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigtimeBasedLinearTypeDef",
    {"linearPercentage": int, "linearInterval": int},
    total=False,
)


class ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigtimeBasedLinearTypeDef(
    _ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigtimeBasedLinearTypeDef
):
    """
    Type definition for `ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfig` `timeBasedLinear`

    A configuration that shifts traffic from one version of a Lambda function to another in
    equal increments, with an equal number of minutes between each increment. The original
    and target Lambda function versions are specified in the deployment's AppSpec file.

    - **linearPercentage** *(integer) --*

      The percentage of traffic that is shifted at the start of each increment of a
      ``TimeBasedLinear`` deployment.

    - **linearInterval** *(integer) --*

      The number of minutes between each incremental traffic shift of a ``TimeBasedLinear``
      deployment.
    """


_ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigTypeDef = TypedDict(
    "_ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigTypeDef",
    {
        "type": str,
        "timeBasedCanary": ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigtimeBasedCanaryTypeDef,
        "timeBasedLinear": ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigtimeBasedLinearTypeDef,
    },
    total=False,
)


class ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigTypeDef(
    _ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigTypeDef
):
    """
    Type definition for `ClientGetDeploymentConfigResponsedeploymentConfigInfo` `trafficRoutingConfig`

    The configuration that specifies how the deployment traffic is routed. Only deployments
    with a Lambda compute platform can specify this.

    - **type** *(string) --*

      The type of traffic shifting (``TimeBasedCanary`` or ``TimeBasedLinear`` ) used by a
      deployment configuration .

    - **timeBasedCanary** *(dict) --*

      A configuration that shifts traffic from one version of a Lambda function to another in
      two increments. The original and target Lambda function versions are specified in the
      deployment's AppSpec file.

      - **canaryPercentage** *(integer) --*

        The percentage of traffic to shift in the first increment of a ``TimeBasedCanary``
        deployment.

      - **canaryInterval** *(integer) --*

        The number of minutes between the first and second traffic shifts of a
        ``TimeBasedCanary`` deployment.

    - **timeBasedLinear** *(dict) --*

      A configuration that shifts traffic from one version of a Lambda function to another in
      equal increments, with an equal number of minutes between each increment. The original
      and target Lambda function versions are specified in the deployment's AppSpec file.

      - **linearPercentage** *(integer) --*

        The percentage of traffic that is shifted at the start of each increment of a
        ``TimeBasedLinear`` deployment.

      - **linearInterval** *(integer) --*

        The number of minutes between each incremental traffic shift of a ``TimeBasedLinear``
        deployment.
    """


_ClientGetDeploymentConfigResponsedeploymentConfigInfoTypeDef = TypedDict(
    "_ClientGetDeploymentConfigResponsedeploymentConfigInfoTypeDef",
    {
        "deploymentConfigId": str,
        "deploymentConfigName": str,
        "minimumHealthyHosts": ClientGetDeploymentConfigResponsedeploymentConfigInfominimumHealthyHostsTypeDef,
        "createTime": datetime,
        "computePlatform": str,
        "trafficRoutingConfig": ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigTypeDef,
    },
    total=False,
)


class ClientGetDeploymentConfigResponsedeploymentConfigInfoTypeDef(
    _ClientGetDeploymentConfigResponsedeploymentConfigInfoTypeDef
):
    """
    Type definition for `ClientGetDeploymentConfigResponse` `deploymentConfigInfo`

    Information about the deployment configuration.

    - **deploymentConfigId** *(string) --*

      The deployment configuration ID.

    - **deploymentConfigName** *(string) --*

      The deployment configuration name.

    - **minimumHealthyHosts** *(dict) --*

      Information about the number or percentage of minimum healthy instance.

      - **value** *(integer) --*

        The minimum healthy instance value.

      - **type** *(string) --*

        The minimum healthy instance type:

        * HOST_COUNT: The minimum number of healthy instance as an absolute value.

        * FLEET_PERCENT: The minimum number of healthy instance as a percentage of the total
        number of instance in the deployment.

        In an example of nine instance, if a HOST_COUNT of six is specified, deploy to up to
        three instances at a time. The deployment is successful if six or more instances are
        deployed to successfully. Otherwise, the deployment fails. If a FLEET_PERCENT of 40 is
        specified, deploy to up to five instance at a time. The deployment is successful if four
        or more instance are deployed to successfully. Otherwise, the deployment fails.

        .. note::

          In a call to the ``GetDeploymentConfig`` , CodeDeployDefault.OneAtATime returns a
          minimum healthy instance type of MOST_CONCURRENCY and a value of 1. This means a
          deployment to only one instance at a time. (You cannot set the type to
          MOST_CONCURRENCY, only to HOST_COUNT or FLEET_PERCENT.) In addition, with
          CodeDeployDefault.OneAtATime, AWS CodeDeploy attempts to ensure that all instances but
          one are kept in a healthy state during the deployment. Although this allows one
          instance at a time to be taken offline for a new deployment, it also means that if the
          deployment to the last instance fails, the overall deployment is still successful.

        For more information, see `AWS CodeDeploy Instance Health
        <https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-health.html>`__ in the
        *AWS CodeDeploy User Guide* .

    - **createTime** *(datetime) --*

      The time at which the deployment configuration was created.

    - **computePlatform** *(string) --*

      The destination platform type for the deployment (``Lambda`` , ``Server`` , or ``ECS`` ).

    - **trafficRoutingConfig** *(dict) --*

      The configuration that specifies how the deployment traffic is routed. Only deployments
      with a Lambda compute platform can specify this.

      - **type** *(string) --*

        The type of traffic shifting (``TimeBasedCanary`` or ``TimeBasedLinear`` ) used by a
        deployment configuration .

      - **timeBasedCanary** *(dict) --*

        A configuration that shifts traffic from one version of a Lambda function to another in
        two increments. The original and target Lambda function versions are specified in the
        deployment's AppSpec file.

        - **canaryPercentage** *(integer) --*

          The percentage of traffic to shift in the first increment of a ``TimeBasedCanary``
          deployment.

        - **canaryInterval** *(integer) --*

          The number of minutes between the first and second traffic shifts of a
          ``TimeBasedCanary`` deployment.

      - **timeBasedLinear** *(dict) --*

        A configuration that shifts traffic from one version of a Lambda function to another in
        equal increments, with an equal number of minutes between each increment. The original
        and target Lambda function versions are specified in the deployment's AppSpec file.

        - **linearPercentage** *(integer) --*

          The percentage of traffic that is shifted at the start of each increment of a
          ``TimeBasedLinear`` deployment.

        - **linearInterval** *(integer) --*

          The number of minutes between each incremental traffic shift of a ``TimeBasedLinear``
          deployment.
    """


_ClientGetDeploymentConfigResponseTypeDef = TypedDict(
    "_ClientGetDeploymentConfigResponseTypeDef",
    {
        "deploymentConfigInfo": ClientGetDeploymentConfigResponsedeploymentConfigInfoTypeDef
    },
    total=False,
)


class ClientGetDeploymentConfigResponseTypeDef(
    _ClientGetDeploymentConfigResponseTypeDef
):
    """
    Type definition for `ClientGetDeploymentConfig` `Response`

    Represents the output of a GetDeploymentConfig operation.

    - **deploymentConfigInfo** *(dict) --*

      Information about the deployment configuration.

      - **deploymentConfigId** *(string) --*

        The deployment configuration ID.

      - **deploymentConfigName** *(string) --*

        The deployment configuration name.

      - **minimumHealthyHosts** *(dict) --*

        Information about the number or percentage of minimum healthy instance.

        - **value** *(integer) --*

          The minimum healthy instance value.

        - **type** *(string) --*

          The minimum healthy instance type:

          * HOST_COUNT: The minimum number of healthy instance as an absolute value.

          * FLEET_PERCENT: The minimum number of healthy instance as a percentage of the total
          number of instance in the deployment.

          In an example of nine instance, if a HOST_COUNT of six is specified, deploy to up to
          three instances at a time. The deployment is successful if six or more instances are
          deployed to successfully. Otherwise, the deployment fails. If a FLEET_PERCENT of 40 is
          specified, deploy to up to five instance at a time. The deployment is successful if four
          or more instance are deployed to successfully. Otherwise, the deployment fails.

          .. note::

            In a call to the ``GetDeploymentConfig`` , CodeDeployDefault.OneAtATime returns a
            minimum healthy instance type of MOST_CONCURRENCY and a value of 1. This means a
            deployment to only one instance at a time. (You cannot set the type to
            MOST_CONCURRENCY, only to HOST_COUNT or FLEET_PERCENT.) In addition, with
            CodeDeployDefault.OneAtATime, AWS CodeDeploy attempts to ensure that all instances but
            one are kept in a healthy state during the deployment. Although this allows one
            instance at a time to be taken offline for a new deployment, it also means that if the
            deployment to the last instance fails, the overall deployment is still successful.

          For more information, see `AWS CodeDeploy Instance Health
          <https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-health.html>`__ in the
          *AWS CodeDeploy User Guide* .

      - **createTime** *(datetime) --*

        The time at which the deployment configuration was created.

      - **computePlatform** *(string) --*

        The destination platform type for the deployment (``Lambda`` , ``Server`` , or ``ECS`` ).

      - **trafficRoutingConfig** *(dict) --*

        The configuration that specifies how the deployment traffic is routed. Only deployments
        with a Lambda compute platform can specify this.

        - **type** *(string) --*

          The type of traffic shifting (``TimeBasedCanary`` or ``TimeBasedLinear`` ) used by a
          deployment configuration .

        - **timeBasedCanary** *(dict) --*

          A configuration that shifts traffic from one version of a Lambda function to another in
          two increments. The original and target Lambda function versions are specified in the
          deployment's AppSpec file.

          - **canaryPercentage** *(integer) --*

            The percentage of traffic to shift in the first increment of a ``TimeBasedCanary``
            deployment.

          - **canaryInterval** *(integer) --*

            The number of minutes between the first and second traffic shifts of a
            ``TimeBasedCanary`` deployment.

        - **timeBasedLinear** *(dict) --*

          A configuration that shifts traffic from one version of a Lambda function to another in
          equal increments, with an equal number of minutes between each increment. The original
          and target Lambda function versions are specified in the deployment's AppSpec file.

          - **linearPercentage** *(integer) --*

            The percentage of traffic that is shifted at the start of each increment of a
            ``TimeBasedLinear`` deployment.

          - **linearInterval** *(integer) --*

            The number of minutes between each incremental traffic shift of a ``TimeBasedLinear``
            deployment.
    """


_ClientGetDeploymentGroupResponsedeploymentGroupInfoalarmConfigurationalarmsTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoalarmConfigurationalarmsTypeDef",
    {"name": str},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoalarmConfigurationalarmsTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoalarmConfigurationalarmsTypeDef
):
    """
    Type definition for `ClientGetDeploymentGroupResponsedeploymentGroupInfoalarmConfiguration` `alarms`

    Information about an alarm.

    - **name** *(string) --*

      The name of the alarm. Maximum length is 255 characters. Each alarm name can be used
      only once in a list of alarms.
    """


_ClientGetDeploymentGroupResponsedeploymentGroupInfoalarmConfigurationTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoalarmConfigurationTypeDef",
    {
        "enabled": bool,
        "ignorePollAlarmFailure": bool,
        "alarms": List[
            ClientGetDeploymentGroupResponsedeploymentGroupInfoalarmConfigurationalarmsTypeDef
        ],
    },
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoalarmConfigurationTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoalarmConfigurationTypeDef
):
    """
    Type definition for `ClientGetDeploymentGroupResponsedeploymentGroupInfo` `alarmConfiguration`

    A list of alarms associated with the deployment group.

    - **enabled** *(boolean) --*

      Indicates whether the alarm configuration is enabled.

    - **ignorePollAlarmFailure** *(boolean) --*

      Indicates whether a deployment should continue if information about the current state of
      alarms cannot be retrieved from Amazon CloudWatch. The default value is false.

      * true: The deployment proceeds even if alarm status information can't be retrieved from
      Amazon CloudWatch.

      * false: The deployment stops if alarm status information can't be retrieved from Amazon
      CloudWatch.

    - **alarms** *(list) --*

      A list of alarms configured for the deployment group. A maximum of 10 alarms can be added
      to a deployment group.

      - *(dict) --*

        Information about an alarm.

        - **name** *(string) --*

          The name of the alarm. Maximum length is 255 characters. Each alarm name can be used
          only once in a list of alarms.
    """


_ClientGetDeploymentGroupResponsedeploymentGroupInfoautoRollbackConfigurationTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoautoRollbackConfigurationTypeDef",
    {"enabled": bool, "events": List[str]},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoautoRollbackConfigurationTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoautoRollbackConfigurationTypeDef
):
    """
    Type definition for `ClientGetDeploymentGroupResponsedeploymentGroupInfo` `autoRollbackConfiguration`

    Information about the automatic rollback configuration associated with the deployment group.

    - **enabled** *(boolean) --*

      Indicates whether a defined automatic rollback configuration is currently enabled.

    - **events** *(list) --*

      The event type or types that trigger a rollback.

      - *(string) --*
    """


_ClientGetDeploymentGroupResponsedeploymentGroupInfoautoScalingGroupsTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoautoScalingGroupsTypeDef",
    {"name": str, "hook": str},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoautoScalingGroupsTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoautoScalingGroupsTypeDef
):
    """
    Type definition for `ClientGetDeploymentGroupResponsedeploymentGroupInfo` `autoScalingGroups`

    Information about an Auto Scaling group.

    - **name** *(string) --*

      The Auto Scaling group name.

    - **hook** *(string) --*

      An Auto Scaling lifecycle event hook name.
    """


_ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    {"actionOnTimeout": str, "waitTimeInMinutes": int},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef
):
    """
    Type definition for `ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfiguration` `deploymentReadyOption`

    Information about the action to take when newly provisioned instances are ready to
    receive traffic in a blue/green deployment.

    - **actionOnTimeout** *(string) --*

      Information about when to reroute traffic from an original environment to a replacement
      environment in a blue/green deployment.

      * CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately after
      the new application revision is installed on the instances in the replacement
      environment.

      * STOP_DEPLOYMENT: Do not register new instances with a load balancer unless traffic
      rerouting is started using  ContinueDeployment . If traffic rerouting is not started
      before the end of the specified wait period, the deployment status is changed to
      Stopped.

    - **waitTimeInMinutes** *(integer) --*

      The number of minutes to wait before the status of a blue/green deployment is changed
      to Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT
      option for actionOnTimeout
    """


_ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    {"action": str},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef
):
    """
    Type definition for `ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfiguration` `greenFleetProvisioningOption`

    Information about how instances are provisioned for a replacement environment in a
    blue/green deployment.

    - **action** *(string) --*

      The method used to add instances to a replacement environment.

      * DISCOVER_EXISTING: Use instances that already exist or will be created manually.

      * COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to define
      and create instances in a new Auto Scaling group.
    """


_ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    {"action": str, "terminationWaitTimeInMinutes": int},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef
):
    """
    Type definition for `ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfiguration` `terminateBlueInstancesOnDeploymentSuccess`

    Information about whether to terminate instances in the original fleet during a
    blue/green deployment.

    - **action** *(string) --*

      The action to take on instances in the original environment after a successful
      blue/green deployment.

      * TERMINATE: Instances are terminated after a specified wait time.

      * KEEP_ALIVE: Instances are left running after they are deregistered from the load
      balancer and removed from the deployment group.

    - **terminationWaitTimeInMinutes** *(integer) --*

      For an Amazon EC2 deployment, the number of minutes to wait after a successful
      blue/green deployment before terminating instances from the original environment.

      For an Amazon ECS deployment, the number of minutes before deleting the original (blue)
      task set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the original
      (blue) task set to a replacement (green) task set.

      The maximum setting is 2880 minutes (2 days).
    """


_ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationTypeDef",
    {
        "terminateBlueInstancesOnDeploymentSuccess": ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef,
        "deploymentReadyOption": ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef,
        "greenFleetProvisioningOption": ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef,
    },
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationTypeDef
):
    """
    Type definition for `ClientGetDeploymentGroupResponsedeploymentGroupInfo` `blueGreenDeploymentConfiguration`

    Information about blue/green deployment options for a deployment group.

    - **terminateBlueInstancesOnDeploymentSuccess** *(dict) --*

      Information about whether to terminate instances in the original fleet during a
      blue/green deployment.

      - **action** *(string) --*

        The action to take on instances in the original environment after a successful
        blue/green deployment.

        * TERMINATE: Instances are terminated after a specified wait time.

        * KEEP_ALIVE: Instances are left running after they are deregistered from the load
        balancer and removed from the deployment group.

      - **terminationWaitTimeInMinutes** *(integer) --*

        For an Amazon EC2 deployment, the number of minutes to wait after a successful
        blue/green deployment before terminating instances from the original environment.

        For an Amazon ECS deployment, the number of minutes before deleting the original (blue)
        task set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the original
        (blue) task set to a replacement (green) task set.

        The maximum setting is 2880 minutes (2 days).

    - **deploymentReadyOption** *(dict) --*

      Information about the action to take when newly provisioned instances are ready to
      receive traffic in a blue/green deployment.

      - **actionOnTimeout** *(string) --*

        Information about when to reroute traffic from an original environment to a replacement
        environment in a blue/green deployment.

        * CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately after
        the new application revision is installed on the instances in the replacement
        environment.

        * STOP_DEPLOYMENT: Do not register new instances with a load balancer unless traffic
        rerouting is started using  ContinueDeployment . If traffic rerouting is not started
        before the end of the specified wait period, the deployment status is changed to
        Stopped.

      - **waitTimeInMinutes** *(integer) --*

        The number of minutes to wait before the status of a blue/green deployment is changed
        to Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT
        option for actionOnTimeout

    - **greenFleetProvisioningOption** *(dict) --*

      Information about how instances are provisioned for a replacement environment in a
      blue/green deployment.

      - **action** *(string) --*

        The method used to add instances to a replacement environment.

        * DISCOVER_EXISTING: Use instances that already exist or will be created manually.

        * COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to define
        and create instances in a new Auto Scaling group.
    """


_ClientGetDeploymentGroupResponsedeploymentGroupInfodeploymentStyleTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfodeploymentStyleTypeDef",
    {"deploymentType": str, "deploymentOption": str},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfodeploymentStyleTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfodeploymentStyleTypeDef
):
    """
    Type definition for `ClientGetDeploymentGroupResponsedeploymentGroupInfo` `deploymentStyle`

    Information about the type of deployment, either in-place or blue/green, you want to run
    and whether to route deployment traffic behind a load balancer.

    - **deploymentType** *(string) --*

      Indicates whether to run an in-place deployment or a blue/green deployment.

    - **deploymentOption** *(string) --*

      Indicates whether to route deployment traffic behind a load balancer.
    """


_ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagFiltersTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": str},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagFiltersTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagFiltersTypeDef
):
    """
    Type definition for `ClientGetDeploymentGroupResponsedeploymentGroupInfo` `ec2TagFilters`

    Information about an EC2 tag filter.

    - **Key** *(string) --*

      The tag filter key.

    - **Value** *(string) --*

      The tag filter value.

    - **Type** *(string) --*

      The tag filter type:

      * KEY_ONLY: Key only.

      * VALUE_ONLY: Value only.

      * KEY_AND_VALUE: Key and value.
    """


_ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagSetec2TagSetListTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagSetec2TagSetListTypeDef",
    {"Key": str, "Value": str, "Type": str},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagSetec2TagSetListTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagSetec2TagSetListTypeDef
):
    """
    Type definition for `ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagSet` `ec2TagSetList`

    Information about an EC2 tag filter.

    - **Key** *(string) --*

      The tag filter key.

    - **Value** *(string) --*

      The tag filter value.

    - **Type** *(string) --*

      The tag filter type:

      * KEY_ONLY: Key only.

      * VALUE_ONLY: Value only.

      * KEY_AND_VALUE: Key and value.
    """


_ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagSetTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagSetTypeDef",
    {
        "ec2TagSetList": List[
            List[
                ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagSetec2TagSetListTypeDef
            ]
        ]
    },
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagSetTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagSetTypeDef
):
    """
    Type definition for `ClientGetDeploymentGroupResponsedeploymentGroupInfo` `ec2TagSet`

    Information about groups of tags applied to an EC2 instance. The deployment group includes
    only EC2 instances identified by all of the tag groups. Cannot be used in the same call as
    ec2TagFilters.

    - **ec2TagSetList** *(list) --*

      A list that contains other lists of EC2 instance tag groups. For an instance to be
      included in the deployment group, it must be identified by all of the tag groups in the
      list.

      - *(list) --*

        - *(dict) --*

          Information about an EC2 tag filter.

          - **Key** *(string) --*

            The tag filter key.

          - **Value** *(string) --*

            The tag filter value.

          - **Type** *(string) --*

            The tag filter type:

            * KEY_ONLY: Key only.

            * VALUE_ONLY: Value only.

            * KEY_AND_VALUE: Key and value.
    """


_ClientGetDeploymentGroupResponsedeploymentGroupInfoecsServicesTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoecsServicesTypeDef",
    {"serviceName": str, "clusterName": str},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoecsServicesTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoecsServicesTypeDef
):
    """
    Type definition for `ClientGetDeploymentGroupResponsedeploymentGroupInfo` `ecsServices`

    Contains the service and cluster names used to identify an Amazon ECS deployment's target.

    - **serviceName** *(string) --*

      The name of the target Amazon ECS service.

    - **clusterName** *(string) --*

      The name of the cluster that the Amazon ECS service is associated with.
    """


_ClientGetDeploymentGroupResponsedeploymentGroupInfolastAttemptedDeploymentTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfolastAttemptedDeploymentTypeDef",
    {"deploymentId": str, "status": str, "endTime": datetime, "createTime": datetime},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfolastAttemptedDeploymentTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfolastAttemptedDeploymentTypeDef
):
    """
    Type definition for `ClientGetDeploymentGroupResponsedeploymentGroupInfo` `lastAttemptedDeployment`

    Information about the most recent attempted deployment to the deployment group.

    - **deploymentId** *(string) --*

      The unique ID of a deployment.

    - **status** *(string) --*

      The status of the most recent deployment.

    - **endTime** *(datetime) --*

      A timestamp that indicates when the most recent deployment to the deployment group was
      complete.

    - **createTime** *(datetime) --*

      A timestamp that indicates when the most recent deployment to the deployment group
      started.
    """


_ClientGetDeploymentGroupResponsedeploymentGroupInfolastSuccessfulDeploymentTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfolastSuccessfulDeploymentTypeDef",
    {"deploymentId": str, "status": str, "endTime": datetime, "createTime": datetime},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfolastSuccessfulDeploymentTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfolastSuccessfulDeploymentTypeDef
):
    """
    Type definition for `ClientGetDeploymentGroupResponsedeploymentGroupInfo` `lastSuccessfulDeployment`

    Information about the most recent successful deployment to the deployment group.

    - **deploymentId** *(string) --*

      The unique ID of a deployment.

    - **status** *(string) --*

      The status of the most recent deployment.

    - **endTime** *(datetime) --*

      A timestamp that indicates when the most recent deployment to the deployment group was
      complete.

    - **createTime** *(datetime) --*

      A timestamp that indicates when the most recent deployment to the deployment group
      started.
    """


_ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfoelbInfoListTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfoelbInfoListTypeDef",
    {"name": str},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfoelbInfoListTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfoelbInfoListTypeDef
):
    """
    Type definition for `ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfo` `elbInfoList`

    Information about a load balancer in Elastic Load Balancing to use in a deployment.
    Instances are registered directly with a load balancer, and traffic is routed to the
    load balancer.

    - **name** *(string) --*

      For blue/green deployments, the name of the load balancer that is used to route
      traffic from original instances to replacement instances in a blue/green deployment.
      For in-place deployments, the name of the load balancer that instances are
      deregistered from so they are not serving traffic during a deployment, and then
      re-registered with after the deployment is complete.
    """


_ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupInfoListTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupInfoListTypeDef",
    {"name": str},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupInfoListTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupInfoListTypeDef
):
    """
    Type definition for `ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfo` `targetGroupInfoList`

    Information about a target group in Elastic Load Balancing to use in a deployment.
    Instances are registered as targets in a target group, and traffic is routed to the
    target group.

    - **name** *(string) --*

      For blue/green deployments, the name of the target group that instances in the
      original environment are deregistered from, and instances in the replacement
      environment are registered with. For in-place deployments, the name of the target
      group that instances are deregistered from, so they are not serving traffic during a
      deployment, and then re-registered with after the deployment is complete.
    """


_ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef
):
    """
    Type definition for `ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoList` `prodTrafficRoute`

    The path used by a load balancer to route production traffic when an Amazon ECS
    deployment is complete.

    - **listenerArns** *(list) --*

      The ARN of one listener. The listener identifies the route between a target group
      and a load balancer. This is an array of strings with a maximum size of one.

      - *(string) --*
    """


_ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    {"name": str},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef
):
    """
    Type definition for `ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoList` `targetGroups`

    Information about a target group in Elastic Load Balancing to use in a deployment.
    Instances are registered as targets in a target group, and traffic is routed to the
    target group.

    - **name** *(string) --*

      For blue/green deployments, the name of the target group that instances in the
      original environment are deregistered from, and instances in the replacement
      environment are registered with. For in-place deployments, the name of the target
      group that instances are deregistered from, so they are not serving traffic
      during a deployment, and then re-registered with after the deployment is complete.
    """


_ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef
):
    """
    Type definition for `ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoList` `testTrafficRoute`

    An optional path used by a load balancer to route test traffic after an Amazon ECS
    deployment. Validation can occur while test traffic is served during a deployment.

    - **listenerArns** *(list) --*

      The ARN of one listener. The listener identifies the route between a target group
      and a load balancer. This is an array of strings with a maximum size of one.

      - *(string) --*
    """


_ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListTypeDef",
    {
        "targetGroups": List[
            ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef
        ],
        "prodTrafficRoute": ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef,
        "testTrafficRoute": ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef,
    },
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListTypeDef
):
    """
    Type definition for `ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfo` `targetGroupPairInfoList`

    Information about two target groups and how traffic is routed during an Amazon ECS
    deployment. An optional test traffic route can be specified.

    - **targetGroups** *(list) --*

      One pair of target groups. One is associated with the original task set. The second
      is associated with the task set that serves traffic after the deployment is complete.

      - *(dict) --*

        Information about a target group in Elastic Load Balancing to use in a deployment.
        Instances are registered as targets in a target group, and traffic is routed to the
        target group.

        - **name** *(string) --*

          For blue/green deployments, the name of the target group that instances in the
          original environment are deregistered from, and instances in the replacement
          environment are registered with. For in-place deployments, the name of the target
          group that instances are deregistered from, so they are not serving traffic
          during a deployment, and then re-registered with after the deployment is complete.

    - **prodTrafficRoute** *(dict) --*

      The path used by a load balancer to route production traffic when an Amazon ECS
      deployment is complete.

      - **listenerArns** *(list) --*

        The ARN of one listener. The listener identifies the route between a target group
        and a load balancer. This is an array of strings with a maximum size of one.

        - *(string) --*

    - **testTrafficRoute** *(dict) --*

      An optional path used by a load balancer to route test traffic after an Amazon ECS
      deployment. Validation can occur while test traffic is served during a deployment.

      - **listenerArns** *(list) --*

        The ARN of one listener. The listener identifies the route between a target group
        and a load balancer. This is an array of strings with a maximum size of one.

        - *(string) --*
    """


_ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfoTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfoTypeDef",
    {
        "elbInfoList": List[
            ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfoelbInfoListTypeDef
        ],
        "targetGroupInfoList": List[
            ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupInfoListTypeDef
        ],
        "targetGroupPairInfoList": List[
            ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListTypeDef
        ],
    },
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfoTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfoTypeDef
):
    """
    Type definition for `ClientGetDeploymentGroupResponsedeploymentGroupInfo` `loadBalancerInfo`

    Information about the load balancer to use in a deployment.

    - **elbInfoList** *(list) --*

      An array that contains information about the load balancer to use for load balancing in a
      deployment. In Elastic Load Balancing, load balancers are used with Classic Load
      Balancers.

      .. note::

        Adding more than one load balancer to the array is not supported.

      - *(dict) --*

        Information about a load balancer in Elastic Load Balancing to use in a deployment.
        Instances are registered directly with a load balancer, and traffic is routed to the
        load balancer.

        - **name** *(string) --*

          For blue/green deployments, the name of the load balancer that is used to route
          traffic from original instances to replacement instances in a blue/green deployment.
          For in-place deployments, the name of the load balancer that instances are
          deregistered from so they are not serving traffic during a deployment, and then
          re-registered with after the deployment is complete.

    - **targetGroupInfoList** *(list) --*

      An array that contains information about the target group to use for load balancing in a
      deployment. In Elastic Load Balancing, target groups are used with Application Load
      Balancers.

      .. note::

        Adding more than one target group to the array is not supported.

      - *(dict) --*

        Information about a target group in Elastic Load Balancing to use in a deployment.
        Instances are registered as targets in a target group, and traffic is routed to the
        target group.

        - **name** *(string) --*

          For blue/green deployments, the name of the target group that instances in the
          original environment are deregistered from, and instances in the replacement
          environment are registered with. For in-place deployments, the name of the target
          group that instances are deregistered from, so they are not serving traffic during a
          deployment, and then re-registered with after the deployment is complete.

    - **targetGroupPairInfoList** *(list) --*

      The target group pair information. This is an array of ``TargeGroupPairInfo`` objects
      with a maximum size of one.

      - *(dict) --*

        Information about two target groups and how traffic is routed during an Amazon ECS
        deployment. An optional test traffic route can be specified.

        - **targetGroups** *(list) --*

          One pair of target groups. One is associated with the original task set. The second
          is associated with the task set that serves traffic after the deployment is complete.

          - *(dict) --*

            Information about a target group in Elastic Load Balancing to use in a deployment.
            Instances are registered as targets in a target group, and traffic is routed to the
            target group.

            - **name** *(string) --*

              For blue/green deployments, the name of the target group that instances in the
              original environment are deregistered from, and instances in the replacement
              environment are registered with. For in-place deployments, the name of the target
              group that instances are deregistered from, so they are not serving traffic
              during a deployment, and then re-registered with after the deployment is complete.

        - **prodTrafficRoute** *(dict) --*

          The path used by a load balancer to route production traffic when an Amazon ECS
          deployment is complete.

          - **listenerArns** *(list) --*

            The ARN of one listener. The listener identifies the route between a target group
            and a load balancer. This is an array of strings with a maximum size of one.

            - *(string) --*

        - **testTrafficRoute** *(dict) --*

          An optional path used by a load balancer to route test traffic after an Amazon ECS
          deployment. Validation can occur while test traffic is served during a deployment.

          - **listenerArns** *(list) --*

            The ARN of one listener. The listener identifies the route between a target group
            and a load balancer. This is an array of strings with a maximum size of one.

            - *(string) --*
    """


_ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesInstanceTagFiltersTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesInstanceTagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": str},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesInstanceTagFiltersTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesInstanceTagFiltersTypeDef
):
    """
    Type definition for `ClientGetDeploymentGroupResponsedeploymentGroupInfo` `onPremisesInstanceTagFilters`

    Information about an on-premises instance tag filter.

    - **Key** *(string) --*

      The on-premises instance tag filter key.

    - **Value** *(string) --*

      The on-premises instance tag filter value.

    - **Type** *(string) --*

      The on-premises instance tag filter type:

      * KEY_ONLY: Key only.

      * VALUE_ONLY: Value only.

      * KEY_AND_VALUE: Key and value.
    """


_ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesTagSetonPremisesTagSetListTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesTagSetonPremisesTagSetListTypeDef",
    {"Key": str, "Value": str, "Type": str},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesTagSetonPremisesTagSetListTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesTagSetonPremisesTagSetListTypeDef
):
    """
    Type definition for `ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesTagSet` `onPremisesTagSetList`

    Information about an on-premises instance tag filter.

    - **Key** *(string) --*

      The on-premises instance tag filter key.

    - **Value** *(string) --*

      The on-premises instance tag filter value.

    - **Type** *(string) --*

      The on-premises instance tag filter type:

      * KEY_ONLY: Key only.

      * VALUE_ONLY: Value only.

      * KEY_AND_VALUE: Key and value.
    """


_ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesTagSetTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesTagSetTypeDef",
    {
        "onPremisesTagSetList": List[
            List[
                ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesTagSetonPremisesTagSetListTypeDef
            ]
        ]
    },
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesTagSetTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesTagSetTypeDef
):
    """
    Type definition for `ClientGetDeploymentGroupResponsedeploymentGroupInfo` `onPremisesTagSet`

    Information about groups of tags applied to an on-premises instance. The deployment group
    includes only on-premises instances identified by all the tag groups. Cannot be used in the
    same call as onPremisesInstanceTagFilters.

    - **onPremisesTagSetList** *(list) --*

      A list that contains other lists of on-premises instance tag groups. For an instance to
      be included in the deployment group, it must be identified by all of the tag groups in
      the list.

      - *(list) --*

        - *(dict) --*

          Information about an on-premises instance tag filter.

          - **Key** *(string) --*

            The on-premises instance tag filter key.

          - **Value** *(string) --*

            The on-premises instance tag filter value.

          - **Type** *(string) --*

            The on-premises instance tag filter type:

            * KEY_ONLY: Key only.

            * VALUE_ONLY: Value only.

            * KEY_AND_VALUE: Key and value.
    """


_ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionappSpecContentTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionappSpecContentTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionappSpecContentTypeDef
):
    """
    Type definition for `ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevision` `appSpecContent`

    The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is
    formatted as JSON or YAML and stored as a RawString.

    - **content** *(string) --*

      The YAML-formatted or JSON-formatted revision string.

      For an AWS Lambda deployment, the content includes a Lambda function name, the alias
      for its original version, and the alias for its replacement version. The deployment
      shifts traffic from the original version of the Lambda function to the replacement
      version.

      For an Amazon ECS deployment, the content includes the task name, information about the
      load balancer that serves traffic to the container, and more.

      For both types of deployments, the content can specify Lambda functions that run at
      specified hooks, such as ``BeforeInstall`` , during a deployment.

    - **sha256** *(string) --*

      The SHA256 hash value of the revision content.
    """


_ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisiongitHubLocationTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisiongitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisiongitHubLocationTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisiongitHubLocationTypeDef
):
    """
    Type definition for `ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevision` `gitHubLocation`

    Information about the location of application artifacts stored in GitHub.

    - **repository** *(string) --*

      The GitHub account and repository pair that stores a reference to the commit that
      represents the bundled artifacts for the application revision.

      Specified as account/repository.

    - **commitId** *(string) --*

      The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
      application revision.
    """


_ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisions3LocationTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisions3LocationTypeDef",
    {"bucket": str, "key": str, "bundleType": str, "version": str, "eTag": str},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisions3LocationTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisions3LocationTypeDef
):
    """
    Type definition for `ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevision` `s3Location`

    Information about the location of a revision stored in Amazon S3.

    - **bucket** *(string) --*

      The name of the Amazon S3 bucket where the application revision is stored.

    - **key** *(string) --*

      The name of the Amazon S3 object that represents the bundled artifacts for the
      application revision.

    - **bundleType** *(string) --*

      The file type of the application revision. Must be one of the following:

      * tar: A tar archive file.

      * tgz: A compressed tar archive file.

      * zip: A zip archive file.

    - **version** *(string) --*

      A specific version of the Amazon S3 object that represents the bundled artifacts for
      the application revision.

      If the version is not specified, the system uses the most recent version by default.

    - **eTag** *(string) --*

      The ETag of the Amazon S3 object that represents the bundled artifacts for the
      application revision.

      If the ETag is not specified as an input parameter, ETag validation of the object is
      skipped.
    """


_ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionstringTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionstringTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionstringTypeDef
):
    """
    Type definition for `ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevision` `string`

    Information about the location of an AWS Lambda deployment revision stored as a RawString.

    - **content** *(string) --*

      The YAML-formatted or JSON-formatted revision string. It includes information about
      which Lambda function to update and optional Lambda functions that validate deployment
      lifecycle events.

    - **sha256** *(string) --*

      The SHA256 hash value of the revision content.
    """


_ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionTypeDef",
    {
        "revisionType": str,
        "s3Location": ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisions3LocationTypeDef,
        "gitHubLocation": ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisiongitHubLocationTypeDef,
        "string": ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionstringTypeDef,
        "appSpecContent": ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionappSpecContentTypeDef,
    },
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionTypeDef
):
    """
    Type definition for `ClientGetDeploymentGroupResponsedeploymentGroupInfo` `targetRevision`

    Information about the deployment group's target revision, including type and location.

    - **revisionType** *(string) --*

      The type of application revision:

      * S3: An application revision stored in Amazon S3.

      * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

      * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

    - **s3Location** *(dict) --*

      Information about the location of a revision stored in Amazon S3.

      - **bucket** *(string) --*

        The name of the Amazon S3 bucket where the application revision is stored.

      - **key** *(string) --*

        The name of the Amazon S3 object that represents the bundled artifacts for the
        application revision.

      - **bundleType** *(string) --*

        The file type of the application revision. Must be one of the following:

        * tar: A tar archive file.

        * tgz: A compressed tar archive file.

        * zip: A zip archive file.

      - **version** *(string) --*

        A specific version of the Amazon S3 object that represents the bundled artifacts for
        the application revision.

        If the version is not specified, the system uses the most recent version by default.

      - **eTag** *(string) --*

        The ETag of the Amazon S3 object that represents the bundled artifacts for the
        application revision.

        If the ETag is not specified as an input parameter, ETag validation of the object is
        skipped.

    - **gitHubLocation** *(dict) --*

      Information about the location of application artifacts stored in GitHub.

      - **repository** *(string) --*

        The GitHub account and repository pair that stores a reference to the commit that
        represents the bundled artifacts for the application revision.

        Specified as account/repository.

      - **commitId** *(string) --*

        The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
        application revision.

    - **string** *(dict) --*

      Information about the location of an AWS Lambda deployment revision stored as a RawString.

      - **content** *(string) --*

        The YAML-formatted or JSON-formatted revision string. It includes information about
        which Lambda function to update and optional Lambda functions that validate deployment
        lifecycle events.

      - **sha256** *(string) --*

        The SHA256 hash value of the revision content.

    - **appSpecContent** *(dict) --*

      The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is
      formatted as JSON or YAML and stored as a RawString.

      - **content** *(string) --*

        The YAML-formatted or JSON-formatted revision string.

        For an AWS Lambda deployment, the content includes a Lambda function name, the alias
        for its original version, and the alias for its replacement version. The deployment
        shifts traffic from the original version of the Lambda function to the replacement
        version.

        For an Amazon ECS deployment, the content includes the task name, information about the
        load balancer that serves traffic to the container, and more.

        For both types of deployments, the content can specify Lambda functions that run at
        specified hooks, such as ``BeforeInstall`` , during a deployment.

      - **sha256** *(string) --*

        The SHA256 hash value of the revision content.
    """


_ClientGetDeploymentGroupResponsedeploymentGroupInfotriggerConfigurationsTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfotriggerConfigurationsTypeDef",
    {"triggerName": str, "triggerTargetArn": str, "triggerEvents": List[str]},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfotriggerConfigurationsTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfotriggerConfigurationsTypeDef
):
    """
    Type definition for `ClientGetDeploymentGroupResponsedeploymentGroupInfo` `triggerConfigurations`

    Information about notification triggers for the deployment group.

    - **triggerName** *(string) --*

      The name of the notification trigger.

    - **triggerTargetArn** *(string) --*

      The ARN of the Amazon Simple Notification Service topic through which notifications
      about deployment or instance events are sent.

    - **triggerEvents** *(list) --*

      The event type or types for which notifications are triggered.

      - *(string) --*
    """


_ClientGetDeploymentGroupResponsedeploymentGroupInfoTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoTypeDef",
    {
        "applicationName": str,
        "deploymentGroupId": str,
        "deploymentGroupName": str,
        "deploymentConfigName": str,
        "ec2TagFilters": List[
            ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagFiltersTypeDef
        ],
        "onPremisesInstanceTagFilters": List[
            ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesInstanceTagFiltersTypeDef
        ],
        "autoScalingGroups": List[
            ClientGetDeploymentGroupResponsedeploymentGroupInfoautoScalingGroupsTypeDef
        ],
        "serviceRoleArn": str,
        "targetRevision": ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionTypeDef,
        "triggerConfigurations": List[
            ClientGetDeploymentGroupResponsedeploymentGroupInfotriggerConfigurationsTypeDef
        ],
        "alarmConfiguration": ClientGetDeploymentGroupResponsedeploymentGroupInfoalarmConfigurationTypeDef,
        "autoRollbackConfiguration": ClientGetDeploymentGroupResponsedeploymentGroupInfoautoRollbackConfigurationTypeDef,
        "deploymentStyle": ClientGetDeploymentGroupResponsedeploymentGroupInfodeploymentStyleTypeDef,
        "blueGreenDeploymentConfiguration": ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationTypeDef,
        "loadBalancerInfo": ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfoTypeDef,
        "lastSuccessfulDeployment": ClientGetDeploymentGroupResponsedeploymentGroupInfolastSuccessfulDeploymentTypeDef,
        "lastAttemptedDeployment": ClientGetDeploymentGroupResponsedeploymentGroupInfolastAttemptedDeploymentTypeDef,
        "ec2TagSet": ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagSetTypeDef,
        "onPremisesTagSet": ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesTagSetTypeDef,
        "computePlatform": str,
        "ecsServices": List[
            ClientGetDeploymentGroupResponsedeploymentGroupInfoecsServicesTypeDef
        ],
    },
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoTypeDef
):
    """
    Type definition for `ClientGetDeploymentGroupResponse` `deploymentGroupInfo`

    Information about the deployment group.

    - **applicationName** *(string) --*

      The application name.

    - **deploymentGroupId** *(string) --*

      The deployment group ID.

    - **deploymentGroupName** *(string) --*

      The deployment group name.

    - **deploymentConfigName** *(string) --*

      The deployment configuration name.

    - **ec2TagFilters** *(list) --*

      The Amazon EC2 tags on which to filter. The deployment group includes EC2 instances with
      any of the specified tags.

      - *(dict) --*

        Information about an EC2 tag filter.

        - **Key** *(string) --*

          The tag filter key.

        - **Value** *(string) --*

          The tag filter value.

        - **Type** *(string) --*

          The tag filter type:

          * KEY_ONLY: Key only.

          * VALUE_ONLY: Value only.

          * KEY_AND_VALUE: Key and value.

    - **onPremisesInstanceTagFilters** *(list) --*

      The on-premises instance tags on which to filter. The deployment group includes on-premises
      instances with any of the specified tags.

      - *(dict) --*

        Information about an on-premises instance tag filter.

        - **Key** *(string) --*

          The on-premises instance tag filter key.

        - **Value** *(string) --*

          The on-premises instance tag filter value.

        - **Type** *(string) --*

          The on-premises instance tag filter type:

          * KEY_ONLY: Key only.

          * VALUE_ONLY: Value only.

          * KEY_AND_VALUE: Key and value.

    - **autoScalingGroups** *(list) --*

      A list of associated Auto Scaling groups.

      - *(dict) --*

        Information about an Auto Scaling group.

        - **name** *(string) --*

          The Auto Scaling group name.

        - **hook** *(string) --*

          An Auto Scaling lifecycle event hook name.

    - **serviceRoleArn** *(string) --*

      A service role Amazon Resource Name (ARN) that grants CodeDeploy permission to make calls
      to AWS services on your behalf. For more information, see `Create a Service Role for AWS
      CodeDeploy
      <https://docs.aws.amazon.com/codedeploy/latest/userguide/getting-started-create-service-role.html>`__
      in the *AWS CodeDeploy User Guide* .

    - **targetRevision** *(dict) --*

      Information about the deployment group's target revision, including type and location.

      - **revisionType** *(string) --*

        The type of application revision:

        * S3: An application revision stored in Amazon S3.

        * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

        * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

      - **s3Location** *(dict) --*

        Information about the location of a revision stored in Amazon S3.

        - **bucket** *(string) --*

          The name of the Amazon S3 bucket where the application revision is stored.

        - **key** *(string) --*

          The name of the Amazon S3 object that represents the bundled artifacts for the
          application revision.

        - **bundleType** *(string) --*

          The file type of the application revision. Must be one of the following:

          * tar: A tar archive file.

          * tgz: A compressed tar archive file.

          * zip: A zip archive file.

        - **version** *(string) --*

          A specific version of the Amazon S3 object that represents the bundled artifacts for
          the application revision.

          If the version is not specified, the system uses the most recent version by default.

        - **eTag** *(string) --*

          The ETag of the Amazon S3 object that represents the bundled artifacts for the
          application revision.

          If the ETag is not specified as an input parameter, ETag validation of the object is
          skipped.

      - **gitHubLocation** *(dict) --*

        Information about the location of application artifacts stored in GitHub.

        - **repository** *(string) --*

          The GitHub account and repository pair that stores a reference to the commit that
          represents the bundled artifacts for the application revision.

          Specified as account/repository.

        - **commitId** *(string) --*

          The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
          application revision.

      - **string** *(dict) --*

        Information about the location of an AWS Lambda deployment revision stored as a RawString.

        - **content** *(string) --*

          The YAML-formatted or JSON-formatted revision string. It includes information about
          which Lambda function to update and optional Lambda functions that validate deployment
          lifecycle events.

        - **sha256** *(string) --*

          The SHA256 hash value of the revision content.

      - **appSpecContent** *(dict) --*

        The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is
        formatted as JSON or YAML and stored as a RawString.

        - **content** *(string) --*

          The YAML-formatted or JSON-formatted revision string.

          For an AWS Lambda deployment, the content includes a Lambda function name, the alias
          for its original version, and the alias for its replacement version. The deployment
          shifts traffic from the original version of the Lambda function to the replacement
          version.

          For an Amazon ECS deployment, the content includes the task name, information about the
          load balancer that serves traffic to the container, and more.

          For both types of deployments, the content can specify Lambda functions that run at
          specified hooks, such as ``BeforeInstall`` , during a deployment.

        - **sha256** *(string) --*

          The SHA256 hash value of the revision content.

    - **triggerConfigurations** *(list) --*

      Information about triggers associated with the deployment group.

      - *(dict) --*

        Information about notification triggers for the deployment group.

        - **triggerName** *(string) --*

          The name of the notification trigger.

        - **triggerTargetArn** *(string) --*

          The ARN of the Amazon Simple Notification Service topic through which notifications
          about deployment or instance events are sent.

        - **triggerEvents** *(list) --*

          The event type or types for which notifications are triggered.

          - *(string) --*

    - **alarmConfiguration** *(dict) --*

      A list of alarms associated with the deployment group.

      - **enabled** *(boolean) --*

        Indicates whether the alarm configuration is enabled.

      - **ignorePollAlarmFailure** *(boolean) --*

        Indicates whether a deployment should continue if information about the current state of
        alarms cannot be retrieved from Amazon CloudWatch. The default value is false.

        * true: The deployment proceeds even if alarm status information can't be retrieved from
        Amazon CloudWatch.

        * false: The deployment stops if alarm status information can't be retrieved from Amazon
        CloudWatch.

      - **alarms** *(list) --*

        A list of alarms configured for the deployment group. A maximum of 10 alarms can be added
        to a deployment group.

        - *(dict) --*

          Information about an alarm.

          - **name** *(string) --*

            The name of the alarm. Maximum length is 255 characters. Each alarm name can be used
            only once in a list of alarms.

    - **autoRollbackConfiguration** *(dict) --*

      Information about the automatic rollback configuration associated with the deployment group.

      - **enabled** *(boolean) --*

        Indicates whether a defined automatic rollback configuration is currently enabled.

      - **events** *(list) --*

        The event type or types that trigger a rollback.

        - *(string) --*

    - **deploymentStyle** *(dict) --*

      Information about the type of deployment, either in-place or blue/green, you want to run
      and whether to route deployment traffic behind a load balancer.

      - **deploymentType** *(string) --*

        Indicates whether to run an in-place deployment or a blue/green deployment.

      - **deploymentOption** *(string) --*

        Indicates whether to route deployment traffic behind a load balancer.

    - **blueGreenDeploymentConfiguration** *(dict) --*

      Information about blue/green deployment options for a deployment group.

      - **terminateBlueInstancesOnDeploymentSuccess** *(dict) --*

        Information about whether to terminate instances in the original fleet during a
        blue/green deployment.

        - **action** *(string) --*

          The action to take on instances in the original environment after a successful
          blue/green deployment.

          * TERMINATE: Instances are terminated after a specified wait time.

          * KEEP_ALIVE: Instances are left running after they are deregistered from the load
          balancer and removed from the deployment group.

        - **terminationWaitTimeInMinutes** *(integer) --*

          For an Amazon EC2 deployment, the number of minutes to wait after a successful
          blue/green deployment before terminating instances from the original environment.

          For an Amazon ECS deployment, the number of minutes before deleting the original (blue)
          task set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the original
          (blue) task set to a replacement (green) task set.

          The maximum setting is 2880 minutes (2 days).

      - **deploymentReadyOption** *(dict) --*

        Information about the action to take when newly provisioned instances are ready to
        receive traffic in a blue/green deployment.

        - **actionOnTimeout** *(string) --*

          Information about when to reroute traffic from an original environment to a replacement
          environment in a blue/green deployment.

          * CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately after
          the new application revision is installed on the instances in the replacement
          environment.

          * STOP_DEPLOYMENT: Do not register new instances with a load balancer unless traffic
          rerouting is started using  ContinueDeployment . If traffic rerouting is not started
          before the end of the specified wait period, the deployment status is changed to
          Stopped.

        - **waitTimeInMinutes** *(integer) --*

          The number of minutes to wait before the status of a blue/green deployment is changed
          to Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT
          option for actionOnTimeout

      - **greenFleetProvisioningOption** *(dict) --*

        Information about how instances are provisioned for a replacement environment in a
        blue/green deployment.

        - **action** *(string) --*

          The method used to add instances to a replacement environment.

          * DISCOVER_EXISTING: Use instances that already exist or will be created manually.

          * COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to define
          and create instances in a new Auto Scaling group.

    - **loadBalancerInfo** *(dict) --*

      Information about the load balancer to use in a deployment.

      - **elbInfoList** *(list) --*

        An array that contains information about the load balancer to use for load balancing in a
        deployment. In Elastic Load Balancing, load balancers are used with Classic Load
        Balancers.

        .. note::

          Adding more than one load balancer to the array is not supported.

        - *(dict) --*

          Information about a load balancer in Elastic Load Balancing to use in a deployment.
          Instances are registered directly with a load balancer, and traffic is routed to the
          load balancer.

          - **name** *(string) --*

            For blue/green deployments, the name of the load balancer that is used to route
            traffic from original instances to replacement instances in a blue/green deployment.
            For in-place deployments, the name of the load balancer that instances are
            deregistered from so they are not serving traffic during a deployment, and then
            re-registered with after the deployment is complete.

      - **targetGroupInfoList** *(list) --*

        An array that contains information about the target group to use for load balancing in a
        deployment. In Elastic Load Balancing, target groups are used with Application Load
        Balancers.

        .. note::

          Adding more than one target group to the array is not supported.

        - *(dict) --*

          Information about a target group in Elastic Load Balancing to use in a deployment.
          Instances are registered as targets in a target group, and traffic is routed to the
          target group.

          - **name** *(string) --*

            For blue/green deployments, the name of the target group that instances in the
            original environment are deregistered from, and instances in the replacement
            environment are registered with. For in-place deployments, the name of the target
            group that instances are deregistered from, so they are not serving traffic during a
            deployment, and then re-registered with after the deployment is complete.

      - **targetGroupPairInfoList** *(list) --*

        The target group pair information. This is an array of ``TargeGroupPairInfo`` objects
        with a maximum size of one.

        - *(dict) --*

          Information about two target groups and how traffic is routed during an Amazon ECS
          deployment. An optional test traffic route can be specified.

          - **targetGroups** *(list) --*

            One pair of target groups. One is associated with the original task set. The second
            is associated with the task set that serves traffic after the deployment is complete.

            - *(dict) --*

              Information about a target group in Elastic Load Balancing to use in a deployment.
              Instances are registered as targets in a target group, and traffic is routed to the
              target group.

              - **name** *(string) --*

                For blue/green deployments, the name of the target group that instances in the
                original environment are deregistered from, and instances in the replacement
                environment are registered with. For in-place deployments, the name of the target
                group that instances are deregistered from, so they are not serving traffic
                during a deployment, and then re-registered with after the deployment is complete.

          - **prodTrafficRoute** *(dict) --*

            The path used by a load balancer to route production traffic when an Amazon ECS
            deployment is complete.

            - **listenerArns** *(list) --*

              The ARN of one listener. The listener identifies the route between a target group
              and a load balancer. This is an array of strings with a maximum size of one.

              - *(string) --*

          - **testTrafficRoute** *(dict) --*

            An optional path used by a load balancer to route test traffic after an Amazon ECS
            deployment. Validation can occur while test traffic is served during a deployment.

            - **listenerArns** *(list) --*

              The ARN of one listener. The listener identifies the route between a target group
              and a load balancer. This is an array of strings with a maximum size of one.

              - *(string) --*

    - **lastSuccessfulDeployment** *(dict) --*

      Information about the most recent successful deployment to the deployment group.

      - **deploymentId** *(string) --*

        The unique ID of a deployment.

      - **status** *(string) --*

        The status of the most recent deployment.

      - **endTime** *(datetime) --*

        A timestamp that indicates when the most recent deployment to the deployment group was
        complete.

      - **createTime** *(datetime) --*

        A timestamp that indicates when the most recent deployment to the deployment group
        started.

    - **lastAttemptedDeployment** *(dict) --*

      Information about the most recent attempted deployment to the deployment group.

      - **deploymentId** *(string) --*

        The unique ID of a deployment.

      - **status** *(string) --*

        The status of the most recent deployment.

      - **endTime** *(datetime) --*

        A timestamp that indicates when the most recent deployment to the deployment group was
        complete.

      - **createTime** *(datetime) --*

        A timestamp that indicates when the most recent deployment to the deployment group
        started.

    - **ec2TagSet** *(dict) --*

      Information about groups of tags applied to an EC2 instance. The deployment group includes
      only EC2 instances identified by all of the tag groups. Cannot be used in the same call as
      ec2TagFilters.

      - **ec2TagSetList** *(list) --*

        A list that contains other lists of EC2 instance tag groups. For an instance to be
        included in the deployment group, it must be identified by all of the tag groups in the
        list.

        - *(list) --*

          - *(dict) --*

            Information about an EC2 tag filter.

            - **Key** *(string) --*

              The tag filter key.

            - **Value** *(string) --*

              The tag filter value.

            - **Type** *(string) --*

              The tag filter type:

              * KEY_ONLY: Key only.

              * VALUE_ONLY: Value only.

              * KEY_AND_VALUE: Key and value.

    - **onPremisesTagSet** *(dict) --*

      Information about groups of tags applied to an on-premises instance. The deployment group
      includes only on-premises instances identified by all the tag groups. Cannot be used in the
      same call as onPremisesInstanceTagFilters.

      - **onPremisesTagSetList** *(list) --*

        A list that contains other lists of on-premises instance tag groups. For an instance to
        be included in the deployment group, it must be identified by all of the tag groups in
        the list.

        - *(list) --*

          - *(dict) --*

            Information about an on-premises instance tag filter.

            - **Key** *(string) --*

              The on-premises instance tag filter key.

            - **Value** *(string) --*

              The on-premises instance tag filter value.

            - **Type** *(string) --*

              The on-premises instance tag filter type:

              * KEY_ONLY: Key only.

              * VALUE_ONLY: Value only.

              * KEY_AND_VALUE: Key and value.

    - **computePlatform** *(string) --*

      The destination platform type for the deployment (``Lambda`` , ``Server`` , or ``ECS`` ).

    - **ecsServices** *(list) --*

      The target Amazon ECS services in the deployment group. This applies only to deployment
      groups that use the Amazon ECS compute platform. A target Amazon ECS service is specified
      as an Amazon ECS cluster and service name pair using the format
      ``<clustername>:<servicename>`` .

      - *(dict) --*

        Contains the service and cluster names used to identify an Amazon ECS deployment's target.

        - **serviceName** *(string) --*

          The name of the target Amazon ECS service.

        - **clusterName** *(string) --*

          The name of the cluster that the Amazon ECS service is associated with.
    """


_ClientGetDeploymentGroupResponseTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponseTypeDef",
    {"deploymentGroupInfo": ClientGetDeploymentGroupResponsedeploymentGroupInfoTypeDef},
    total=False,
)


class ClientGetDeploymentGroupResponseTypeDef(_ClientGetDeploymentGroupResponseTypeDef):
    """
    Type definition for `ClientGetDeploymentGroup` `Response`

    Represents the output of a GetDeploymentGroup operation.

    - **deploymentGroupInfo** *(dict) --*

      Information about the deployment group.

      - **applicationName** *(string) --*

        The application name.

      - **deploymentGroupId** *(string) --*

        The deployment group ID.

      - **deploymentGroupName** *(string) --*

        The deployment group name.

      - **deploymentConfigName** *(string) --*

        The deployment configuration name.

      - **ec2TagFilters** *(list) --*

        The Amazon EC2 tags on which to filter. The deployment group includes EC2 instances with
        any of the specified tags.

        - *(dict) --*

          Information about an EC2 tag filter.

          - **Key** *(string) --*

            The tag filter key.

          - **Value** *(string) --*

            The tag filter value.

          - **Type** *(string) --*

            The tag filter type:

            * KEY_ONLY: Key only.

            * VALUE_ONLY: Value only.

            * KEY_AND_VALUE: Key and value.

      - **onPremisesInstanceTagFilters** *(list) --*

        The on-premises instance tags on which to filter. The deployment group includes on-premises
        instances with any of the specified tags.

        - *(dict) --*

          Information about an on-premises instance tag filter.

          - **Key** *(string) --*

            The on-premises instance tag filter key.

          - **Value** *(string) --*

            The on-premises instance tag filter value.

          - **Type** *(string) --*

            The on-premises instance tag filter type:

            * KEY_ONLY: Key only.

            * VALUE_ONLY: Value only.

            * KEY_AND_VALUE: Key and value.

      - **autoScalingGroups** *(list) --*

        A list of associated Auto Scaling groups.

        - *(dict) --*

          Information about an Auto Scaling group.

          - **name** *(string) --*

            The Auto Scaling group name.

          - **hook** *(string) --*

            An Auto Scaling lifecycle event hook name.

      - **serviceRoleArn** *(string) --*

        A service role Amazon Resource Name (ARN) that grants CodeDeploy permission to make calls
        to AWS services on your behalf. For more information, see `Create a Service Role for AWS
        CodeDeploy
        <https://docs.aws.amazon.com/codedeploy/latest/userguide/getting-started-create-service-role.html>`__
        in the *AWS CodeDeploy User Guide* .

      - **targetRevision** *(dict) --*

        Information about the deployment group's target revision, including type and location.

        - **revisionType** *(string) --*

          The type of application revision:

          * S3: An application revision stored in Amazon S3.

          * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

          * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

        - **s3Location** *(dict) --*

          Information about the location of a revision stored in Amazon S3.

          - **bucket** *(string) --*

            The name of the Amazon S3 bucket where the application revision is stored.

          - **key** *(string) --*

            The name of the Amazon S3 object that represents the bundled artifacts for the
            application revision.

          - **bundleType** *(string) --*

            The file type of the application revision. Must be one of the following:

            * tar: A tar archive file.

            * tgz: A compressed tar archive file.

            * zip: A zip archive file.

          - **version** *(string) --*

            A specific version of the Amazon S3 object that represents the bundled artifacts for
            the application revision.

            If the version is not specified, the system uses the most recent version by default.

          - **eTag** *(string) --*

            The ETag of the Amazon S3 object that represents the bundled artifacts for the
            application revision.

            If the ETag is not specified as an input parameter, ETag validation of the object is
            skipped.

        - **gitHubLocation** *(dict) --*

          Information about the location of application artifacts stored in GitHub.

          - **repository** *(string) --*

            The GitHub account and repository pair that stores a reference to the commit that
            represents the bundled artifacts for the application revision.

            Specified as account/repository.

          - **commitId** *(string) --*

            The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
            application revision.

        - **string** *(dict) --*

          Information about the location of an AWS Lambda deployment revision stored as a RawString.

          - **content** *(string) --*

            The YAML-formatted or JSON-formatted revision string. It includes information about
            which Lambda function to update and optional Lambda functions that validate deployment
            lifecycle events.

          - **sha256** *(string) --*

            The SHA256 hash value of the revision content.

        - **appSpecContent** *(dict) --*

          The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is
          formatted as JSON or YAML and stored as a RawString.

          - **content** *(string) --*

            The YAML-formatted or JSON-formatted revision string.

            For an AWS Lambda deployment, the content includes a Lambda function name, the alias
            for its original version, and the alias for its replacement version. The deployment
            shifts traffic from the original version of the Lambda function to the replacement
            version.

            For an Amazon ECS deployment, the content includes the task name, information about the
            load balancer that serves traffic to the container, and more.

            For both types of deployments, the content can specify Lambda functions that run at
            specified hooks, such as ``BeforeInstall`` , during a deployment.

          - **sha256** *(string) --*

            The SHA256 hash value of the revision content.

      - **triggerConfigurations** *(list) --*

        Information about triggers associated with the deployment group.

        - *(dict) --*

          Information about notification triggers for the deployment group.

          - **triggerName** *(string) --*

            The name of the notification trigger.

          - **triggerTargetArn** *(string) --*

            The ARN of the Amazon Simple Notification Service topic through which notifications
            about deployment or instance events are sent.

          - **triggerEvents** *(list) --*

            The event type or types for which notifications are triggered.

            - *(string) --*

      - **alarmConfiguration** *(dict) --*

        A list of alarms associated with the deployment group.

        - **enabled** *(boolean) --*

          Indicates whether the alarm configuration is enabled.

        - **ignorePollAlarmFailure** *(boolean) --*

          Indicates whether a deployment should continue if information about the current state of
          alarms cannot be retrieved from Amazon CloudWatch. The default value is false.

          * true: The deployment proceeds even if alarm status information can't be retrieved from
          Amazon CloudWatch.

          * false: The deployment stops if alarm status information can't be retrieved from Amazon
          CloudWatch.

        - **alarms** *(list) --*

          A list of alarms configured for the deployment group. A maximum of 10 alarms can be added
          to a deployment group.

          - *(dict) --*

            Information about an alarm.

            - **name** *(string) --*

              The name of the alarm. Maximum length is 255 characters. Each alarm name can be used
              only once in a list of alarms.

      - **autoRollbackConfiguration** *(dict) --*

        Information about the automatic rollback configuration associated with the deployment group.

        - **enabled** *(boolean) --*

          Indicates whether a defined automatic rollback configuration is currently enabled.

        - **events** *(list) --*

          The event type or types that trigger a rollback.

          - *(string) --*

      - **deploymentStyle** *(dict) --*

        Information about the type of deployment, either in-place or blue/green, you want to run
        and whether to route deployment traffic behind a load balancer.

        - **deploymentType** *(string) --*

          Indicates whether to run an in-place deployment or a blue/green deployment.

        - **deploymentOption** *(string) --*

          Indicates whether to route deployment traffic behind a load balancer.

      - **blueGreenDeploymentConfiguration** *(dict) --*

        Information about blue/green deployment options for a deployment group.

        - **terminateBlueInstancesOnDeploymentSuccess** *(dict) --*

          Information about whether to terminate instances in the original fleet during a
          blue/green deployment.

          - **action** *(string) --*

            The action to take on instances in the original environment after a successful
            blue/green deployment.

            * TERMINATE: Instances are terminated after a specified wait time.

            * KEEP_ALIVE: Instances are left running after they are deregistered from the load
            balancer and removed from the deployment group.

          - **terminationWaitTimeInMinutes** *(integer) --*

            For an Amazon EC2 deployment, the number of minutes to wait after a successful
            blue/green deployment before terminating instances from the original environment.

            For an Amazon ECS deployment, the number of minutes before deleting the original (blue)
            task set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the original
            (blue) task set to a replacement (green) task set.

            The maximum setting is 2880 minutes (2 days).

        - **deploymentReadyOption** *(dict) --*

          Information about the action to take when newly provisioned instances are ready to
          receive traffic in a blue/green deployment.

          - **actionOnTimeout** *(string) --*

            Information about when to reroute traffic from an original environment to a replacement
            environment in a blue/green deployment.

            * CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately after
            the new application revision is installed on the instances in the replacement
            environment.

            * STOP_DEPLOYMENT: Do not register new instances with a load balancer unless traffic
            rerouting is started using  ContinueDeployment . If traffic rerouting is not started
            before the end of the specified wait period, the deployment status is changed to
            Stopped.

          - **waitTimeInMinutes** *(integer) --*

            The number of minutes to wait before the status of a blue/green deployment is changed
            to Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT
            option for actionOnTimeout

        - **greenFleetProvisioningOption** *(dict) --*

          Information about how instances are provisioned for a replacement environment in a
          blue/green deployment.

          - **action** *(string) --*

            The method used to add instances to a replacement environment.

            * DISCOVER_EXISTING: Use instances that already exist or will be created manually.

            * COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to define
            and create instances in a new Auto Scaling group.

      - **loadBalancerInfo** *(dict) --*

        Information about the load balancer to use in a deployment.

        - **elbInfoList** *(list) --*

          An array that contains information about the load balancer to use for load balancing in a
          deployment. In Elastic Load Balancing, load balancers are used with Classic Load
          Balancers.

          .. note::

            Adding more than one load balancer to the array is not supported.

          - *(dict) --*

            Information about a load balancer in Elastic Load Balancing to use in a deployment.
            Instances are registered directly with a load balancer, and traffic is routed to the
            load balancer.

            - **name** *(string) --*

              For blue/green deployments, the name of the load balancer that is used to route
              traffic from original instances to replacement instances in a blue/green deployment.
              For in-place deployments, the name of the load balancer that instances are
              deregistered from so they are not serving traffic during a deployment, and then
              re-registered with after the deployment is complete.

        - **targetGroupInfoList** *(list) --*

          An array that contains information about the target group to use for load balancing in a
          deployment. In Elastic Load Balancing, target groups are used with Application Load
          Balancers.

          .. note::

            Adding more than one target group to the array is not supported.

          - *(dict) --*

            Information about a target group in Elastic Load Balancing to use in a deployment.
            Instances are registered as targets in a target group, and traffic is routed to the
            target group.

            - **name** *(string) --*

              For blue/green deployments, the name of the target group that instances in the
              original environment are deregistered from, and instances in the replacement
              environment are registered with. For in-place deployments, the name of the target
              group that instances are deregistered from, so they are not serving traffic during a
              deployment, and then re-registered with after the deployment is complete.

        - **targetGroupPairInfoList** *(list) --*

          The target group pair information. This is an array of ``TargeGroupPairInfo`` objects
          with a maximum size of one.

          - *(dict) --*

            Information about two target groups and how traffic is routed during an Amazon ECS
            deployment. An optional test traffic route can be specified.

            - **targetGroups** *(list) --*

              One pair of target groups. One is associated with the original task set. The second
              is associated with the task set that serves traffic after the deployment is complete.

              - *(dict) --*

                Information about a target group in Elastic Load Balancing to use in a deployment.
                Instances are registered as targets in a target group, and traffic is routed to the
                target group.

                - **name** *(string) --*

                  For blue/green deployments, the name of the target group that instances in the
                  original environment are deregistered from, and instances in the replacement
                  environment are registered with. For in-place deployments, the name of the target
                  group that instances are deregistered from, so they are not serving traffic
                  during a deployment, and then re-registered with after the deployment is complete.

            - **prodTrafficRoute** *(dict) --*

              The path used by a load balancer to route production traffic when an Amazon ECS
              deployment is complete.

              - **listenerArns** *(list) --*

                The ARN of one listener. The listener identifies the route between a target group
                and a load balancer. This is an array of strings with a maximum size of one.

                - *(string) --*

            - **testTrafficRoute** *(dict) --*

              An optional path used by a load balancer to route test traffic after an Amazon ECS
              deployment. Validation can occur while test traffic is served during a deployment.

              - **listenerArns** *(list) --*

                The ARN of one listener. The listener identifies the route between a target group
                and a load balancer. This is an array of strings with a maximum size of one.

                - *(string) --*

      - **lastSuccessfulDeployment** *(dict) --*

        Information about the most recent successful deployment to the deployment group.

        - **deploymentId** *(string) --*

          The unique ID of a deployment.

        - **status** *(string) --*

          The status of the most recent deployment.

        - **endTime** *(datetime) --*

          A timestamp that indicates when the most recent deployment to the deployment group was
          complete.

        - **createTime** *(datetime) --*

          A timestamp that indicates when the most recent deployment to the deployment group
          started.

      - **lastAttemptedDeployment** *(dict) --*

        Information about the most recent attempted deployment to the deployment group.

        - **deploymentId** *(string) --*

          The unique ID of a deployment.

        - **status** *(string) --*

          The status of the most recent deployment.

        - **endTime** *(datetime) --*

          A timestamp that indicates when the most recent deployment to the deployment group was
          complete.

        - **createTime** *(datetime) --*

          A timestamp that indicates when the most recent deployment to the deployment group
          started.

      - **ec2TagSet** *(dict) --*

        Information about groups of tags applied to an EC2 instance. The deployment group includes
        only EC2 instances identified by all of the tag groups. Cannot be used in the same call as
        ec2TagFilters.

        - **ec2TagSetList** *(list) --*

          A list that contains other lists of EC2 instance tag groups. For an instance to be
          included in the deployment group, it must be identified by all of the tag groups in the
          list.

          - *(list) --*

            - *(dict) --*

              Information about an EC2 tag filter.

              - **Key** *(string) --*

                The tag filter key.

              - **Value** *(string) --*

                The tag filter value.

              - **Type** *(string) --*

                The tag filter type:

                * KEY_ONLY: Key only.

                * VALUE_ONLY: Value only.

                * KEY_AND_VALUE: Key and value.

      - **onPremisesTagSet** *(dict) --*

        Information about groups of tags applied to an on-premises instance. The deployment group
        includes only on-premises instances identified by all the tag groups. Cannot be used in the
        same call as onPremisesInstanceTagFilters.

        - **onPremisesTagSetList** *(list) --*

          A list that contains other lists of on-premises instance tag groups. For an instance to
          be included in the deployment group, it must be identified by all of the tag groups in
          the list.

          - *(list) --*

            - *(dict) --*

              Information about an on-premises instance tag filter.

              - **Key** *(string) --*

                The on-premises instance tag filter key.

              - **Value** *(string) --*

                The on-premises instance tag filter value.

              - **Type** *(string) --*

                The on-premises instance tag filter type:

                * KEY_ONLY: Key only.

                * VALUE_ONLY: Value only.

                * KEY_AND_VALUE: Key and value.

      - **computePlatform** *(string) --*

        The destination platform type for the deployment (``Lambda`` , ``Server`` , or ``ECS`` ).

      - **ecsServices** *(list) --*

        The target Amazon ECS services in the deployment group. This applies only to deployment
        groups that use the Amazon ECS compute platform. A target Amazon ECS service is specified
        as an Amazon ECS cluster and service name pair using the format
        ``<clustername>:<servicename>`` .

        - *(dict) --*

          Contains the service and cluster names used to identify an Amazon ECS deployment's target.

          - **serviceName** *(string) --*

            The name of the target Amazon ECS service.

          - **clusterName** *(string) --*

            The name of the cluster that the Amazon ECS service is associated with.
    """


_ClientGetDeploymentInstanceResponseinstanceSummarylifecycleEventsdiagnosticsTypeDef = TypedDict(
    "_ClientGetDeploymentInstanceResponseinstanceSummarylifecycleEventsdiagnosticsTypeDef",
    {"errorCode": str, "scriptName": str, "message": str, "logTail": str},
    total=False,
)


class ClientGetDeploymentInstanceResponseinstanceSummarylifecycleEventsdiagnosticsTypeDef(
    _ClientGetDeploymentInstanceResponseinstanceSummarylifecycleEventsdiagnosticsTypeDef
):
    """
    Type definition for `ClientGetDeploymentInstanceResponseinstanceSummarylifecycleEvents` `diagnostics`

    Diagnostic information about the deployment lifecycle event.

    - **errorCode** *(string) --*

      The associated error code:

      * Success: The specified script ran.

      * ScriptMissing: The specified script was not found in the specified location.

      * ScriptNotExecutable: The specified script is not a recognized executable file type.

      * ScriptTimedOut: The specified script did not finish running in the specified time
      period.

      * ScriptFailed: The specified script failed to run as expected.

      * UnknownError: The specified script did not run for an unknown reason.

    - **scriptName** *(string) --*

      The name of the script.

    - **message** *(string) --*

      The message associated with the error.

    - **logTail** *(string) --*

      The last portion of the diagnostic log.

      If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.
    """


_ClientGetDeploymentInstanceResponseinstanceSummarylifecycleEventsTypeDef = TypedDict(
    "_ClientGetDeploymentInstanceResponseinstanceSummarylifecycleEventsTypeDef",
    {
        "lifecycleEventName": str,
        "diagnostics": ClientGetDeploymentInstanceResponseinstanceSummarylifecycleEventsdiagnosticsTypeDef,
        "startTime": datetime,
        "endTime": datetime,
        "status": str,
    },
    total=False,
)


class ClientGetDeploymentInstanceResponseinstanceSummarylifecycleEventsTypeDef(
    _ClientGetDeploymentInstanceResponseinstanceSummarylifecycleEventsTypeDef
):
    """
    Type definition for `ClientGetDeploymentInstanceResponseinstanceSummary` `lifecycleEvents`

    Information about a deployment lifecycle event.

    - **lifecycleEventName** *(string) --*

      The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
      AfterInstall, ApplicationStart, or ValidateService.

    - **diagnostics** *(dict) --*

      Diagnostic information about the deployment lifecycle event.

      - **errorCode** *(string) --*

        The associated error code:

        * Success: The specified script ran.

        * ScriptMissing: The specified script was not found in the specified location.

        * ScriptNotExecutable: The specified script is not a recognized executable file type.

        * ScriptTimedOut: The specified script did not finish running in the specified time
        period.

        * ScriptFailed: The specified script failed to run as expected.

        * UnknownError: The specified script did not run for an unknown reason.

      - **scriptName** *(string) --*

        The name of the script.

      - **message** *(string) --*

        The message associated with the error.

      - **logTail** *(string) --*

        The last portion of the diagnostic log.

        If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.

    - **startTime** *(datetime) --*

      A timestamp that indicates when the deployment lifecycle event started.

    - **endTime** *(datetime) --*

      A timestamp that indicates when the deployment lifecycle event ended.

    - **status** *(string) --*

      The deployment lifecycle event status:

      * Pending: The deployment lifecycle event is pending.

      * InProgress: The deployment lifecycle event is in progress.

      * Succeeded: The deployment lifecycle event ran successfully.

      * Failed: The deployment lifecycle event has failed.

      * Skipped: The deployment lifecycle event has been skipped.

      * Unknown: The deployment lifecycle event is unknown.
    """


_ClientGetDeploymentInstanceResponseinstanceSummaryTypeDef = TypedDict(
    "_ClientGetDeploymentInstanceResponseinstanceSummaryTypeDef",
    {
        "deploymentId": str,
        "instanceId": str,
        "status": str,
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List[
            ClientGetDeploymentInstanceResponseinstanceSummarylifecycleEventsTypeDef
        ],
        "instanceType": str,
    },
    total=False,
)


class ClientGetDeploymentInstanceResponseinstanceSummaryTypeDef(
    _ClientGetDeploymentInstanceResponseinstanceSummaryTypeDef
):
    """
    Type definition for `ClientGetDeploymentInstanceResponse` `instanceSummary`

    Information about the instance.

    - **deploymentId** *(string) --*

      The unique ID of a deployment.

    - **instanceId** *(string) --*

      The instance ID.

    - **status** *(string) --*

      The deployment status for this instance:

      * Pending: The deployment is pending for this instance.

      * In Progress: The deployment is in progress for this instance.

      * Succeeded: The deployment has succeeded for this instance.

      * Failed: The deployment has failed for this instance.

      * Skipped: The deployment has been skipped for this instance.

      * Unknown: The deployment status is unknown for this instance.

    - **lastUpdatedAt** *(datetime) --*

      A timestamp that indicaties when the instance information was last updated.

    - **lifecycleEvents** *(list) --*

      A list of lifecycle events for this instance.

      - *(dict) --*

        Information about a deployment lifecycle event.

        - **lifecycleEventName** *(string) --*

          The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
          AfterInstall, ApplicationStart, or ValidateService.

        - **diagnostics** *(dict) --*

          Diagnostic information about the deployment lifecycle event.

          - **errorCode** *(string) --*

            The associated error code:

            * Success: The specified script ran.

            * ScriptMissing: The specified script was not found in the specified location.

            * ScriptNotExecutable: The specified script is not a recognized executable file type.

            * ScriptTimedOut: The specified script did not finish running in the specified time
            period.

            * ScriptFailed: The specified script failed to run as expected.

            * UnknownError: The specified script did not run for an unknown reason.

          - **scriptName** *(string) --*

            The name of the script.

          - **message** *(string) --*

            The message associated with the error.

          - **logTail** *(string) --*

            The last portion of the diagnostic log.

            If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.

        - **startTime** *(datetime) --*

          A timestamp that indicates when the deployment lifecycle event started.

        - **endTime** *(datetime) --*

          A timestamp that indicates when the deployment lifecycle event ended.

        - **status** *(string) --*

          The deployment lifecycle event status:

          * Pending: The deployment lifecycle event is pending.

          * InProgress: The deployment lifecycle event is in progress.

          * Succeeded: The deployment lifecycle event ran successfully.

          * Failed: The deployment lifecycle event has failed.

          * Skipped: The deployment lifecycle event has been skipped.

          * Unknown: The deployment lifecycle event is unknown.

    - **instanceType** *(string) --*

      Information about which environment an instance belongs to in a blue/green deployment.

      * BLUE: The instance is part of the original environment.

      * GREEN: The instance is part of the replacement environment.
    """


_ClientGetDeploymentInstanceResponseTypeDef = TypedDict(
    "_ClientGetDeploymentInstanceResponseTypeDef",
    {"instanceSummary": ClientGetDeploymentInstanceResponseinstanceSummaryTypeDef},
    total=False,
)


class ClientGetDeploymentInstanceResponseTypeDef(
    _ClientGetDeploymentInstanceResponseTypeDef
):
    """
    Type definition for `ClientGetDeploymentInstance` `Response`

    Represents the output of a GetDeploymentInstance operation.

    - **instanceSummary** *(dict) --*

      Information about the instance.

      - **deploymentId** *(string) --*

        The unique ID of a deployment.

      - **instanceId** *(string) --*

        The instance ID.

      - **status** *(string) --*

        The deployment status for this instance:

        * Pending: The deployment is pending for this instance.

        * In Progress: The deployment is in progress for this instance.

        * Succeeded: The deployment has succeeded for this instance.

        * Failed: The deployment has failed for this instance.

        * Skipped: The deployment has been skipped for this instance.

        * Unknown: The deployment status is unknown for this instance.

      - **lastUpdatedAt** *(datetime) --*

        A timestamp that indicaties when the instance information was last updated.

      - **lifecycleEvents** *(list) --*

        A list of lifecycle events for this instance.

        - *(dict) --*

          Information about a deployment lifecycle event.

          - **lifecycleEventName** *(string) --*

            The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
            AfterInstall, ApplicationStart, or ValidateService.

          - **diagnostics** *(dict) --*

            Diagnostic information about the deployment lifecycle event.

            - **errorCode** *(string) --*

              The associated error code:

              * Success: The specified script ran.

              * ScriptMissing: The specified script was not found in the specified location.

              * ScriptNotExecutable: The specified script is not a recognized executable file type.

              * ScriptTimedOut: The specified script did not finish running in the specified time
              period.

              * ScriptFailed: The specified script failed to run as expected.

              * UnknownError: The specified script did not run for an unknown reason.

            - **scriptName** *(string) --*

              The name of the script.

            - **message** *(string) --*

              The message associated with the error.

            - **logTail** *(string) --*

              The last portion of the diagnostic log.

              If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.

          - **startTime** *(datetime) --*

            A timestamp that indicates when the deployment lifecycle event started.

          - **endTime** *(datetime) --*

            A timestamp that indicates when the deployment lifecycle event ended.

          - **status** *(string) --*

            The deployment lifecycle event status:

            * Pending: The deployment lifecycle event is pending.

            * InProgress: The deployment lifecycle event is in progress.

            * Succeeded: The deployment lifecycle event ran successfully.

            * Failed: The deployment lifecycle event has failed.

            * Skipped: The deployment lifecycle event has been skipped.

            * Unknown: The deployment lifecycle event is unknown.

      - **instanceType** *(string) --*

        Information about which environment an instance belongs to in a blue/green deployment.

        * BLUE: The instance is part of the original environment.

        * GREEN: The instance is part of the replacement environment.
    """


_ClientGetDeploymentResponsedeploymentInfoautoRollbackConfigurationTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfoautoRollbackConfigurationTypeDef",
    {"enabled": bool, "events": List[str]},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfoautoRollbackConfigurationTypeDef(
    _ClientGetDeploymentResponsedeploymentInfoautoRollbackConfigurationTypeDef
):
    """
    Type definition for `ClientGetDeploymentResponsedeploymentInfo` `autoRollbackConfiguration`

    Information about the automatic rollback configuration associated with the deployment.

    - **enabled** *(boolean) --*

      Indicates whether a defined automatic rollback configuration is currently enabled.

    - **events** *(list) --*

      The event type or types that trigger a rollback.

      - *(string) --*
    """


_ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    {"actionOnTimeout": str, "waitTimeInMinutes": int},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef(
    _ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef
):
    """
    Type definition for `ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfiguration` `deploymentReadyOption`

    Information about the action to take when newly provisioned instances are ready to
    receive traffic in a blue/green deployment.

    - **actionOnTimeout** *(string) --*

      Information about when to reroute traffic from an original environment to a replacement
      environment in a blue/green deployment.

      * CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately after
      the new application revision is installed on the instances in the replacement
      environment.

      * STOP_DEPLOYMENT: Do not register new instances with a load balancer unless traffic
      rerouting is started using  ContinueDeployment . If traffic rerouting is not started
      before the end of the specified wait period, the deployment status is changed to
      Stopped.

    - **waitTimeInMinutes** *(integer) --*

      The number of minutes to wait before the status of a blue/green deployment is changed
      to Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT
      option for actionOnTimeout
    """


_ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    {"action": str},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef(
    _ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef
):
    """
    Type definition for `ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfiguration` `greenFleetProvisioningOption`

    Information about how instances are provisioned for a replacement environment in a
    blue/green deployment.

    - **action** *(string) --*

      The method used to add instances to a replacement environment.

      * DISCOVER_EXISTING: Use instances that already exist or will be created manually.

      * COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to define
      and create instances in a new Auto Scaling group.
    """


_ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    {"action": str, "terminationWaitTimeInMinutes": int},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef(
    _ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef
):
    """
    Type definition for `ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfiguration` `terminateBlueInstancesOnDeploymentSuccess`

    Information about whether to terminate instances in the original fleet during a
    blue/green deployment.

    - **action** *(string) --*

      The action to take on instances in the original environment after a successful
      blue/green deployment.

      * TERMINATE: Instances are terminated after a specified wait time.

      * KEEP_ALIVE: Instances are left running after they are deregistered from the load
      balancer and removed from the deployment group.

    - **terminationWaitTimeInMinutes** *(integer) --*

      For an Amazon EC2 deployment, the number of minutes to wait after a successful
      blue/green deployment before terminating instances from the original environment.

      For an Amazon ECS deployment, the number of minutes before deleting the original (blue)
      task set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the original
      (blue) task set to a replacement (green) task set.

      The maximum setting is 2880 minutes (2 days).
    """


_ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationTypeDef",
    {
        "terminateBlueInstancesOnDeploymentSuccess": ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef,
        "deploymentReadyOption": ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef,
        "greenFleetProvisioningOption": ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef,
    },
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationTypeDef(
    _ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationTypeDef
):
    """
    Type definition for `ClientGetDeploymentResponsedeploymentInfo` `blueGreenDeploymentConfiguration`

    Information about blue/green deployment options for this deployment.

    - **terminateBlueInstancesOnDeploymentSuccess** *(dict) --*

      Information about whether to terminate instances in the original fleet during a
      blue/green deployment.

      - **action** *(string) --*

        The action to take on instances in the original environment after a successful
        blue/green deployment.

        * TERMINATE: Instances are terminated after a specified wait time.

        * KEEP_ALIVE: Instances are left running after they are deregistered from the load
        balancer and removed from the deployment group.

      - **terminationWaitTimeInMinutes** *(integer) --*

        For an Amazon EC2 deployment, the number of minutes to wait after a successful
        blue/green deployment before terminating instances from the original environment.

        For an Amazon ECS deployment, the number of minutes before deleting the original (blue)
        task set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the original
        (blue) task set to a replacement (green) task set.

        The maximum setting is 2880 minutes (2 days).

    - **deploymentReadyOption** *(dict) --*

      Information about the action to take when newly provisioned instances are ready to
      receive traffic in a blue/green deployment.

      - **actionOnTimeout** *(string) --*

        Information about when to reroute traffic from an original environment to a replacement
        environment in a blue/green deployment.

        * CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately after
        the new application revision is installed on the instances in the replacement
        environment.

        * STOP_DEPLOYMENT: Do not register new instances with a load balancer unless traffic
        rerouting is started using  ContinueDeployment . If traffic rerouting is not started
        before the end of the specified wait period, the deployment status is changed to
        Stopped.

      - **waitTimeInMinutes** *(integer) --*

        The number of minutes to wait before the status of a blue/green deployment is changed
        to Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT
        option for actionOnTimeout

    - **greenFleetProvisioningOption** *(dict) --*

      Information about how instances are provisioned for a replacement environment in a
      blue/green deployment.

      - **action** *(string) --*

        The method used to add instances to a replacement environment.

        * DISCOVER_EXISTING: Use instances that already exist or will be created manually.

        * COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to define
        and create instances in a new Auto Scaling group.
    """


_ClientGetDeploymentResponsedeploymentInfodeploymentOverviewTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfodeploymentOverviewTypeDef",
    {
        "Pending": int,
        "InProgress": int,
        "Succeeded": int,
        "Failed": int,
        "Skipped": int,
        "Ready": int,
    },
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfodeploymentOverviewTypeDef(
    _ClientGetDeploymentResponsedeploymentInfodeploymentOverviewTypeDef
):
    """
    Type definition for `ClientGetDeploymentResponsedeploymentInfo` `deploymentOverview`

    A summary of the deployment status of the instances in the deployment.

    - **Pending** *(integer) --*

      The number of instances in the deployment in a pending state.

    - **InProgress** *(integer) --*

      The number of instances in which the deployment is in progress.

    - **Succeeded** *(integer) --*

      The number of instances in the deployment to which revisions have been successfully
      deployed.

    - **Failed** *(integer) --*

      The number of instances in the deployment in a failed state.

    - **Skipped** *(integer) --*

      The number of instances in the deployment in a skipped state.

    - **Ready** *(integer) --*

      The number of instances in a replacement environment ready to receive traffic in a
      blue/green deployment.
    """


_ClientGetDeploymentResponsedeploymentInfodeploymentStyleTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfodeploymentStyleTypeDef",
    {"deploymentType": str, "deploymentOption": str},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfodeploymentStyleTypeDef(
    _ClientGetDeploymentResponsedeploymentInfodeploymentStyleTypeDef
):
    """
    Type definition for `ClientGetDeploymentResponsedeploymentInfo` `deploymentStyle`

    Information about the type of deployment, either in-place or blue/green, you want to run
    and whether to route deployment traffic behind a load balancer.

    - **deploymentType** *(string) --*

      Indicates whether to run an in-place deployment or a blue/green deployment.

    - **deploymentOption** *(string) --*

      Indicates whether to route deployment traffic behind a load balancer.
    """


_ClientGetDeploymentResponsedeploymentInfoerrorInformationTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfoerrorInformationTypeDef",
    {"code": str, "message": str},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfoerrorInformationTypeDef(
    _ClientGetDeploymentResponsedeploymentInfoerrorInformationTypeDef
):
    """
    Type definition for `ClientGetDeploymentResponsedeploymentInfo` `errorInformation`

    Information about any error associated with this deployment.

    - **code** *(string) --*

      For more information, see `Error Codes for AWS CodeDeploy
      <https://docs.aws.amazon.com/codedeploy/latest/userguide/error-codes.html>`__ in the `AWS
      CodeDeploy User Guide <https://docs.aws.amazon.com/codedeploy/latest/userguide>`__ .

      The error code:

      * APPLICATION_MISSING: The application was missing. This error code is most likely raised
      if the application is deleted after the deployment is created, but before it is started.

      * DEPLOYMENT_GROUP_MISSING: The deployment group was missing. This error code is most
      likely raised if the deployment group is deleted after the deployment is created, but
      before it is started.

      * HEALTH_CONSTRAINTS: The deployment failed on too many instances to be successfully
      deployed within the instance health constraints specified.

      * HEALTH_CONSTRAINTS_INVALID: The revision cannot be successfully deployed within the
      instance health constraints specified.

      * IAM_ROLE_MISSING: The service role cannot be accessed.

      * IAM_ROLE_PERMISSIONS: The service role does not have the correct permissions.

      * INTERNAL_ERROR: There was an internal error.

      * NO_EC2_SUBSCRIPTION: The calling account is not subscribed to Amazon EC2.

      * NO_INSTANCES: No instances were specified, or no instances can be found.

      * OVER_MAX_INSTANCES: The maximum number of instances was exceeded.

      * THROTTLED: The operation was throttled because the calling account exceeded the
      throttling limits of one or more AWS services.

      * TIMEOUT: The deployment has timed out.

      * REVISION_MISSING: The revision ID was missing. This error code is most likely raised if
      the revision is deleted after the deployment is created, but before it is started.

    - **message** *(string) --*

      An accompanying error message.
    """


_ClientGetDeploymentResponsedeploymentInfoloadBalancerInfoelbInfoListTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfoloadBalancerInfoelbInfoListTypeDef",
    {"name": str},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfoloadBalancerInfoelbInfoListTypeDef(
    _ClientGetDeploymentResponsedeploymentInfoloadBalancerInfoelbInfoListTypeDef
):
    """
    Type definition for `ClientGetDeploymentResponsedeploymentInfoloadBalancerInfo` `elbInfoList`

    Information about a load balancer in Elastic Load Balancing to use in a deployment.
    Instances are registered directly with a load balancer, and traffic is routed to the
    load balancer.

    - **name** *(string) --*

      For blue/green deployments, the name of the load balancer that is used to route
      traffic from original instances to replacement instances in a blue/green deployment.
      For in-place deployments, the name of the load balancer that instances are
      deregistered from so they are not serving traffic during a deployment, and then
      re-registered with after the deployment is complete.
    """


_ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupInfoListTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupInfoListTypeDef",
    {"name": str},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupInfoListTypeDef(
    _ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupInfoListTypeDef
):
    """
    Type definition for `ClientGetDeploymentResponsedeploymentInfoloadBalancerInfo` `targetGroupInfoList`

    Information about a target group in Elastic Load Balancing to use in a deployment.
    Instances are registered as targets in a target group, and traffic is routed to the
    target group.

    - **name** *(string) --*

      For blue/green deployments, the name of the target group that instances in the
      original environment are deregistered from, and instances in the replacement
      environment are registered with. For in-place deployments, the name of the target
      group that instances are deregistered from, so they are not serving traffic during a
      deployment, and then re-registered with after the deployment is complete.
    """


_ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef(
    _ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef
):
    """
    Type definition for `ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoList` `prodTrafficRoute`

    The path used by a load balancer to route production traffic when an Amazon ECS
    deployment is complete.

    - **listenerArns** *(list) --*

      The ARN of one listener. The listener identifies the route between a target group
      and a load balancer. This is an array of strings with a maximum size of one.

      - *(string) --*
    """


_ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    {"name": str},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef(
    _ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef
):
    """
    Type definition for `ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoList` `targetGroups`

    Information about a target group in Elastic Load Balancing to use in a deployment.
    Instances are registered as targets in a target group, and traffic is routed to the
    target group.

    - **name** *(string) --*

      For blue/green deployments, the name of the target group that instances in the
      original environment are deregistered from, and instances in the replacement
      environment are registered with. For in-place deployments, the name of the target
      group that instances are deregistered from, so they are not serving traffic
      during a deployment, and then re-registered with after the deployment is complete.
    """


_ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef(
    _ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef
):
    """
    Type definition for `ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoList` `testTrafficRoute`

    An optional path used by a load balancer to route test traffic after an Amazon ECS
    deployment. Validation can occur while test traffic is served during a deployment.

    - **listenerArns** *(list) --*

      The ARN of one listener. The listener identifies the route between a target group
      and a load balancer. This is an array of strings with a maximum size of one.

      - *(string) --*
    """


_ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListTypeDef",
    {
        "targetGroups": List[
            ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef
        ],
        "prodTrafficRoute": ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef,
        "testTrafficRoute": ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef,
    },
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListTypeDef(
    _ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListTypeDef
):
    """
    Type definition for `ClientGetDeploymentResponsedeploymentInfoloadBalancerInfo` `targetGroupPairInfoList`

    Information about two target groups and how traffic is routed during an Amazon ECS
    deployment. An optional test traffic route can be specified.

    - **targetGroups** *(list) --*

      One pair of target groups. One is associated with the original task set. The second
      is associated with the task set that serves traffic after the deployment is complete.

      - *(dict) --*

        Information about a target group in Elastic Load Balancing to use in a deployment.
        Instances are registered as targets in a target group, and traffic is routed to the
        target group.

        - **name** *(string) --*

          For blue/green deployments, the name of the target group that instances in the
          original environment are deregistered from, and instances in the replacement
          environment are registered with. For in-place deployments, the name of the target
          group that instances are deregistered from, so they are not serving traffic
          during a deployment, and then re-registered with after the deployment is complete.

    - **prodTrafficRoute** *(dict) --*

      The path used by a load balancer to route production traffic when an Amazon ECS
      deployment is complete.

      - **listenerArns** *(list) --*

        The ARN of one listener. The listener identifies the route between a target group
        and a load balancer. This is an array of strings with a maximum size of one.

        - *(string) --*

    - **testTrafficRoute** *(dict) --*

      An optional path used by a load balancer to route test traffic after an Amazon ECS
      deployment. Validation can occur while test traffic is served during a deployment.

      - **listenerArns** *(list) --*

        The ARN of one listener. The listener identifies the route between a target group
        and a load balancer. This is an array of strings with a maximum size of one.

        - *(string) --*
    """


_ClientGetDeploymentResponsedeploymentInfoloadBalancerInfoTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfoloadBalancerInfoTypeDef",
    {
        "elbInfoList": List[
            ClientGetDeploymentResponsedeploymentInfoloadBalancerInfoelbInfoListTypeDef
        ],
        "targetGroupInfoList": List[
            ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupInfoListTypeDef
        ],
        "targetGroupPairInfoList": List[
            ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListTypeDef
        ],
    },
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfoloadBalancerInfoTypeDef(
    _ClientGetDeploymentResponsedeploymentInfoloadBalancerInfoTypeDef
):
    """
    Type definition for `ClientGetDeploymentResponsedeploymentInfo` `loadBalancerInfo`

    Information about the load balancer used in the deployment.

    - **elbInfoList** *(list) --*

      An array that contains information about the load balancer to use for load balancing in a
      deployment. In Elastic Load Balancing, load balancers are used with Classic Load
      Balancers.

      .. note::

        Adding more than one load balancer to the array is not supported.

      - *(dict) --*

        Information about a load balancer in Elastic Load Balancing to use in a deployment.
        Instances are registered directly with a load balancer, and traffic is routed to the
        load balancer.

        - **name** *(string) --*

          For blue/green deployments, the name of the load balancer that is used to route
          traffic from original instances to replacement instances in a blue/green deployment.
          For in-place deployments, the name of the load balancer that instances are
          deregistered from so they are not serving traffic during a deployment, and then
          re-registered with after the deployment is complete.

    - **targetGroupInfoList** *(list) --*

      An array that contains information about the target group to use for load balancing in a
      deployment. In Elastic Load Balancing, target groups are used with Application Load
      Balancers.

      .. note::

        Adding more than one target group to the array is not supported.

      - *(dict) --*

        Information about a target group in Elastic Load Balancing to use in a deployment.
        Instances are registered as targets in a target group, and traffic is routed to the
        target group.

        - **name** *(string) --*

          For blue/green deployments, the name of the target group that instances in the
          original environment are deregistered from, and instances in the replacement
          environment are registered with. For in-place deployments, the name of the target
          group that instances are deregistered from, so they are not serving traffic during a
          deployment, and then re-registered with after the deployment is complete.

    - **targetGroupPairInfoList** *(list) --*

      The target group pair information. This is an array of ``TargeGroupPairInfo`` objects
      with a maximum size of one.

      - *(dict) --*

        Information about two target groups and how traffic is routed during an Amazon ECS
        deployment. An optional test traffic route can be specified.

        - **targetGroups** *(list) --*

          One pair of target groups. One is associated with the original task set. The second
          is associated with the task set that serves traffic after the deployment is complete.

          - *(dict) --*

            Information about a target group in Elastic Load Balancing to use in a deployment.
            Instances are registered as targets in a target group, and traffic is routed to the
            target group.

            - **name** *(string) --*

              For blue/green deployments, the name of the target group that instances in the
              original environment are deregistered from, and instances in the replacement
              environment are registered with. For in-place deployments, the name of the target
              group that instances are deregistered from, so they are not serving traffic
              during a deployment, and then re-registered with after the deployment is complete.

        - **prodTrafficRoute** *(dict) --*

          The path used by a load balancer to route production traffic when an Amazon ECS
          deployment is complete.

          - **listenerArns** *(list) --*

            The ARN of one listener. The listener identifies the route between a target group
            and a load balancer. This is an array of strings with a maximum size of one.

            - *(string) --*

        - **testTrafficRoute** *(dict) --*

          An optional path used by a load balancer to route test traffic after an Amazon ECS
          deployment. Validation can occur while test traffic is served during a deployment.

          - **listenerArns** *(list) --*

            The ARN of one listener. The listener identifies the route between a target group
            and a load balancer. This is an array of strings with a maximum size of one.

            - *(string) --*
    """


_ClientGetDeploymentResponsedeploymentInfopreviousRevisionappSpecContentTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfopreviousRevisionappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfopreviousRevisionappSpecContentTypeDef(
    _ClientGetDeploymentResponsedeploymentInfopreviousRevisionappSpecContentTypeDef
):
    """
    Type definition for `ClientGetDeploymentResponsedeploymentInfopreviousRevision` `appSpecContent`

    The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is
    formatted as JSON or YAML and stored as a RawString.

    - **content** *(string) --*

      The YAML-formatted or JSON-formatted revision string.

      For an AWS Lambda deployment, the content includes a Lambda function name, the alias
      for its original version, and the alias for its replacement version. The deployment
      shifts traffic from the original version of the Lambda function to the replacement
      version.

      For an Amazon ECS deployment, the content includes the task name, information about the
      load balancer that serves traffic to the container, and more.

      For both types of deployments, the content can specify Lambda functions that run at
      specified hooks, such as ``BeforeInstall`` , during a deployment.

    - **sha256** *(string) --*

      The SHA256 hash value of the revision content.
    """


_ClientGetDeploymentResponsedeploymentInfopreviousRevisiongitHubLocationTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfopreviousRevisiongitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfopreviousRevisiongitHubLocationTypeDef(
    _ClientGetDeploymentResponsedeploymentInfopreviousRevisiongitHubLocationTypeDef
):
    """
    Type definition for `ClientGetDeploymentResponsedeploymentInfopreviousRevision` `gitHubLocation`

    Information about the location of application artifacts stored in GitHub.

    - **repository** *(string) --*

      The GitHub account and repository pair that stores a reference to the commit that
      represents the bundled artifacts for the application revision.

      Specified as account/repository.

    - **commitId** *(string) --*

      The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
      application revision.
    """


_ClientGetDeploymentResponsedeploymentInfopreviousRevisions3LocationTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfopreviousRevisions3LocationTypeDef",
    {"bucket": str, "key": str, "bundleType": str, "version": str, "eTag": str},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfopreviousRevisions3LocationTypeDef(
    _ClientGetDeploymentResponsedeploymentInfopreviousRevisions3LocationTypeDef
):
    """
    Type definition for `ClientGetDeploymentResponsedeploymentInfopreviousRevision` `s3Location`

    Information about the location of a revision stored in Amazon S3.

    - **bucket** *(string) --*

      The name of the Amazon S3 bucket where the application revision is stored.

    - **key** *(string) --*

      The name of the Amazon S3 object that represents the bundled artifacts for the
      application revision.

    - **bundleType** *(string) --*

      The file type of the application revision. Must be one of the following:

      * tar: A tar archive file.

      * tgz: A compressed tar archive file.

      * zip: A zip archive file.

    - **version** *(string) --*

      A specific version of the Amazon S3 object that represents the bundled artifacts for
      the application revision.

      If the version is not specified, the system uses the most recent version by default.

    - **eTag** *(string) --*

      The ETag of the Amazon S3 object that represents the bundled artifacts for the
      application revision.

      If the ETag is not specified as an input parameter, ETag validation of the object is
      skipped.
    """


_ClientGetDeploymentResponsedeploymentInfopreviousRevisionstringTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfopreviousRevisionstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfopreviousRevisionstringTypeDef(
    _ClientGetDeploymentResponsedeploymentInfopreviousRevisionstringTypeDef
):
    """
    Type definition for `ClientGetDeploymentResponsedeploymentInfopreviousRevision` `string`

    Information about the location of an AWS Lambda deployment revision stored as a RawString.

    - **content** *(string) --*

      The YAML-formatted or JSON-formatted revision string. It includes information about
      which Lambda function to update and optional Lambda functions that validate deployment
      lifecycle events.

    - **sha256** *(string) --*

      The SHA256 hash value of the revision content.
    """


_ClientGetDeploymentResponsedeploymentInfopreviousRevisionTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfopreviousRevisionTypeDef",
    {
        "revisionType": str,
        "s3Location": ClientGetDeploymentResponsedeploymentInfopreviousRevisions3LocationTypeDef,
        "gitHubLocation": ClientGetDeploymentResponsedeploymentInfopreviousRevisiongitHubLocationTypeDef,
        "string": ClientGetDeploymentResponsedeploymentInfopreviousRevisionstringTypeDef,
        "appSpecContent": ClientGetDeploymentResponsedeploymentInfopreviousRevisionappSpecContentTypeDef,
    },
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfopreviousRevisionTypeDef(
    _ClientGetDeploymentResponsedeploymentInfopreviousRevisionTypeDef
):
    """
    Type definition for `ClientGetDeploymentResponsedeploymentInfo` `previousRevision`

    Information about the application revision that was deployed to the deployment group before
    the most recent successful deployment.

    - **revisionType** *(string) --*

      The type of application revision:

      * S3: An application revision stored in Amazon S3.

      * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

      * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

    - **s3Location** *(dict) --*

      Information about the location of a revision stored in Amazon S3.

      - **bucket** *(string) --*

        The name of the Amazon S3 bucket where the application revision is stored.

      - **key** *(string) --*

        The name of the Amazon S3 object that represents the bundled artifacts for the
        application revision.

      - **bundleType** *(string) --*

        The file type of the application revision. Must be one of the following:

        * tar: A tar archive file.

        * tgz: A compressed tar archive file.

        * zip: A zip archive file.

      - **version** *(string) --*

        A specific version of the Amazon S3 object that represents the bundled artifacts for
        the application revision.

        If the version is not specified, the system uses the most recent version by default.

      - **eTag** *(string) --*

        The ETag of the Amazon S3 object that represents the bundled artifacts for the
        application revision.

        If the ETag is not specified as an input parameter, ETag validation of the object is
        skipped.

    - **gitHubLocation** *(dict) --*

      Information about the location of application artifacts stored in GitHub.

      - **repository** *(string) --*

        The GitHub account and repository pair that stores a reference to the commit that
        represents the bundled artifacts for the application revision.

        Specified as account/repository.

      - **commitId** *(string) --*

        The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
        application revision.

    - **string** *(dict) --*

      Information about the location of an AWS Lambda deployment revision stored as a RawString.

      - **content** *(string) --*

        The YAML-formatted or JSON-formatted revision string. It includes information about
        which Lambda function to update and optional Lambda functions that validate deployment
        lifecycle events.

      - **sha256** *(string) --*

        The SHA256 hash value of the revision content.

    - **appSpecContent** *(dict) --*

      The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is
      formatted as JSON or YAML and stored as a RawString.

      - **content** *(string) --*

        The YAML-formatted or JSON-formatted revision string.

        For an AWS Lambda deployment, the content includes a Lambda function name, the alias
        for its original version, and the alias for its replacement version. The deployment
        shifts traffic from the original version of the Lambda function to the replacement
        version.

        For an Amazon ECS deployment, the content includes the task name, information about the
        load balancer that serves traffic to the container, and more.

        For both types of deployments, the content can specify Lambda functions that run at
        specified hooks, such as ``BeforeInstall`` , during a deployment.

      - **sha256** *(string) --*

        The SHA256 hash value of the revision content.
    """


_ClientGetDeploymentResponsedeploymentInforevisionappSpecContentTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInforevisionappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInforevisionappSpecContentTypeDef(
    _ClientGetDeploymentResponsedeploymentInforevisionappSpecContentTypeDef
):
    """
    Type definition for `ClientGetDeploymentResponsedeploymentInforevision` `appSpecContent`

    The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is
    formatted as JSON or YAML and stored as a RawString.

    - **content** *(string) --*

      The YAML-formatted or JSON-formatted revision string.

      For an AWS Lambda deployment, the content includes a Lambda function name, the alias
      for its original version, and the alias for its replacement version. The deployment
      shifts traffic from the original version of the Lambda function to the replacement
      version.

      For an Amazon ECS deployment, the content includes the task name, information about the
      load balancer that serves traffic to the container, and more.

      For both types of deployments, the content can specify Lambda functions that run at
      specified hooks, such as ``BeforeInstall`` , during a deployment.

    - **sha256** *(string) --*

      The SHA256 hash value of the revision content.
    """


_ClientGetDeploymentResponsedeploymentInforevisiongitHubLocationTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInforevisiongitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInforevisiongitHubLocationTypeDef(
    _ClientGetDeploymentResponsedeploymentInforevisiongitHubLocationTypeDef
):
    """
    Type definition for `ClientGetDeploymentResponsedeploymentInforevision` `gitHubLocation`

    Information about the location of application artifacts stored in GitHub.

    - **repository** *(string) --*

      The GitHub account and repository pair that stores a reference to the commit that
      represents the bundled artifacts for the application revision.

      Specified as account/repository.

    - **commitId** *(string) --*

      The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
      application revision.
    """


_ClientGetDeploymentResponsedeploymentInforevisions3LocationTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInforevisions3LocationTypeDef",
    {"bucket": str, "key": str, "bundleType": str, "version": str, "eTag": str},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInforevisions3LocationTypeDef(
    _ClientGetDeploymentResponsedeploymentInforevisions3LocationTypeDef
):
    """
    Type definition for `ClientGetDeploymentResponsedeploymentInforevision` `s3Location`

    Information about the location of a revision stored in Amazon S3.

    - **bucket** *(string) --*

      The name of the Amazon S3 bucket where the application revision is stored.

    - **key** *(string) --*

      The name of the Amazon S3 object that represents the bundled artifacts for the
      application revision.

    - **bundleType** *(string) --*

      The file type of the application revision. Must be one of the following:

      * tar: A tar archive file.

      * tgz: A compressed tar archive file.

      * zip: A zip archive file.

    - **version** *(string) --*

      A specific version of the Amazon S3 object that represents the bundled artifacts for
      the application revision.

      If the version is not specified, the system uses the most recent version by default.

    - **eTag** *(string) --*

      The ETag of the Amazon S3 object that represents the bundled artifacts for the
      application revision.

      If the ETag is not specified as an input parameter, ETag validation of the object is
      skipped.
    """


_ClientGetDeploymentResponsedeploymentInforevisionstringTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInforevisionstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInforevisionstringTypeDef(
    _ClientGetDeploymentResponsedeploymentInforevisionstringTypeDef
):
    """
    Type definition for `ClientGetDeploymentResponsedeploymentInforevision` `string`

    Information about the location of an AWS Lambda deployment revision stored as a RawString.

    - **content** *(string) --*

      The YAML-formatted or JSON-formatted revision string. It includes information about
      which Lambda function to update and optional Lambda functions that validate deployment
      lifecycle events.

    - **sha256** *(string) --*

      The SHA256 hash value of the revision content.
    """


_ClientGetDeploymentResponsedeploymentInforevisionTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInforevisionTypeDef",
    {
        "revisionType": str,
        "s3Location": ClientGetDeploymentResponsedeploymentInforevisions3LocationTypeDef,
        "gitHubLocation": ClientGetDeploymentResponsedeploymentInforevisiongitHubLocationTypeDef,
        "string": ClientGetDeploymentResponsedeploymentInforevisionstringTypeDef,
        "appSpecContent": ClientGetDeploymentResponsedeploymentInforevisionappSpecContentTypeDef,
    },
    total=False,
)


class ClientGetDeploymentResponsedeploymentInforevisionTypeDef(
    _ClientGetDeploymentResponsedeploymentInforevisionTypeDef
):
    """
    Type definition for `ClientGetDeploymentResponsedeploymentInfo` `revision`

    Information about the location of stored application artifacts and the service from which
    to retrieve them.

    - **revisionType** *(string) --*

      The type of application revision:

      * S3: An application revision stored in Amazon S3.

      * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

      * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

    - **s3Location** *(dict) --*

      Information about the location of a revision stored in Amazon S3.

      - **bucket** *(string) --*

        The name of the Amazon S3 bucket where the application revision is stored.

      - **key** *(string) --*

        The name of the Amazon S3 object that represents the bundled artifacts for the
        application revision.

      - **bundleType** *(string) --*

        The file type of the application revision. Must be one of the following:

        * tar: A tar archive file.

        * tgz: A compressed tar archive file.

        * zip: A zip archive file.

      - **version** *(string) --*

        A specific version of the Amazon S3 object that represents the bundled artifacts for
        the application revision.

        If the version is not specified, the system uses the most recent version by default.

      - **eTag** *(string) --*

        The ETag of the Amazon S3 object that represents the bundled artifacts for the
        application revision.

        If the ETag is not specified as an input parameter, ETag validation of the object is
        skipped.

    - **gitHubLocation** *(dict) --*

      Information about the location of application artifacts stored in GitHub.

      - **repository** *(string) --*

        The GitHub account and repository pair that stores a reference to the commit that
        represents the bundled artifacts for the application revision.

        Specified as account/repository.

      - **commitId** *(string) --*

        The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
        application revision.

    - **string** *(dict) --*

      Information about the location of an AWS Lambda deployment revision stored as a RawString.

      - **content** *(string) --*

        The YAML-formatted or JSON-formatted revision string. It includes information about
        which Lambda function to update and optional Lambda functions that validate deployment
        lifecycle events.

      - **sha256** *(string) --*

        The SHA256 hash value of the revision content.

    - **appSpecContent** *(dict) --*

      The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is
      formatted as JSON or YAML and stored as a RawString.

      - **content** *(string) --*

        The YAML-formatted or JSON-formatted revision string.

        For an AWS Lambda deployment, the content includes a Lambda function name, the alias
        for its original version, and the alias for its replacement version. The deployment
        shifts traffic from the original version of the Lambda function to the replacement
        version.

        For an Amazon ECS deployment, the content includes the task name, information about the
        load balancer that serves traffic to the container, and more.

        For both types of deployments, the content can specify Lambda functions that run at
        specified hooks, such as ``BeforeInstall`` , during a deployment.

      - **sha256** *(string) --*

        The SHA256 hash value of the revision content.
    """


_ClientGetDeploymentResponsedeploymentInforollbackInfoTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInforollbackInfoTypeDef",
    {
        "rollbackDeploymentId": str,
        "rollbackTriggeringDeploymentId": str,
        "rollbackMessage": str,
    },
    total=False,
)


class ClientGetDeploymentResponsedeploymentInforollbackInfoTypeDef(
    _ClientGetDeploymentResponsedeploymentInforollbackInfoTypeDef
):
    """
    Type definition for `ClientGetDeploymentResponsedeploymentInfo` `rollbackInfo`

    Information about a deployment rollback.

    - **rollbackDeploymentId** *(string) --*

      The ID of the deployment rollback.

    - **rollbackTriggeringDeploymentId** *(string) --*

      The deployment ID of the deployment that was underway and triggered a rollback deployment
      because it failed or was stopped.

    - **rollbackMessage** *(string) --*

      Information that describes the status of a deployment rollback (for example, whether the
      deployment can't be rolled back, is in progress, failed, or succeeded).
    """


_ClientGetDeploymentResponsedeploymentInfotargetInstancesec2TagSetec2TagSetListTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfotargetInstancesec2TagSetec2TagSetListTypeDef",
    {"Key": str, "Value": str, "Type": str},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfotargetInstancesec2TagSetec2TagSetListTypeDef(
    _ClientGetDeploymentResponsedeploymentInfotargetInstancesec2TagSetec2TagSetListTypeDef
):
    """
    Type definition for `ClientGetDeploymentResponsedeploymentInfotargetInstancesec2TagSet` `ec2TagSetList`

    Information about an EC2 tag filter.

    - **Key** *(string) --*

      The tag filter key.

    - **Value** *(string) --*

      The tag filter value.

    - **Type** *(string) --*

      The tag filter type:

      * KEY_ONLY: Key only.

      * VALUE_ONLY: Value only.

      * KEY_AND_VALUE: Key and value.
    """


_ClientGetDeploymentResponsedeploymentInfotargetInstancesec2TagSetTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfotargetInstancesec2TagSetTypeDef",
    {
        "ec2TagSetList": List[
            List[
                ClientGetDeploymentResponsedeploymentInfotargetInstancesec2TagSetec2TagSetListTypeDef
            ]
        ]
    },
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfotargetInstancesec2TagSetTypeDef(
    _ClientGetDeploymentResponsedeploymentInfotargetInstancesec2TagSetTypeDef
):
    """
    Type definition for `ClientGetDeploymentResponsedeploymentInfotargetInstances` `ec2TagSet`

    Information about the groups of EC2 instance tags that an instance must be identified by
    in order for it to be included in the replacement environment for a blue/green
    deployment. Cannot be used in the same call as tagFilters.

    - **ec2TagSetList** *(list) --*

      A list that contains other lists of EC2 instance tag groups. For an instance to be
      included in the deployment group, it must be identified by all of the tag groups in the
      list.

      - *(list) --*

        - *(dict) --*

          Information about an EC2 tag filter.

          - **Key** *(string) --*

            The tag filter key.

          - **Value** *(string) --*

            The tag filter value.

          - **Type** *(string) --*

            The tag filter type:

            * KEY_ONLY: Key only.

            * VALUE_ONLY: Value only.

            * KEY_AND_VALUE: Key and value.
    """


_ClientGetDeploymentResponsedeploymentInfotargetInstancestagFiltersTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfotargetInstancestagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": str},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfotargetInstancestagFiltersTypeDef(
    _ClientGetDeploymentResponsedeploymentInfotargetInstancestagFiltersTypeDef
):
    """
    Type definition for `ClientGetDeploymentResponsedeploymentInfotargetInstances` `tagFilters`

    Information about an EC2 tag filter.

    - **Key** *(string) --*

      The tag filter key.

    - **Value** *(string) --*

      The tag filter value.

    - **Type** *(string) --*

      The tag filter type:

      * KEY_ONLY: Key only.

      * VALUE_ONLY: Value only.

      * KEY_AND_VALUE: Key and value.
    """


_ClientGetDeploymentResponsedeploymentInfotargetInstancesTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfotargetInstancesTypeDef",
    {
        "tagFilters": List[
            ClientGetDeploymentResponsedeploymentInfotargetInstancestagFiltersTypeDef
        ],
        "autoScalingGroups": List[str],
        "ec2TagSet": ClientGetDeploymentResponsedeploymentInfotargetInstancesec2TagSetTypeDef,
    },
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfotargetInstancesTypeDef(
    _ClientGetDeploymentResponsedeploymentInfotargetInstancesTypeDef
):
    """
    Type definition for `ClientGetDeploymentResponsedeploymentInfo` `targetInstances`

    Information about the instances that belong to the replacement environment in a blue/green
    deployment.

    - **tagFilters** *(list) --*

      The tag filter key, type, and value used to identify Amazon EC2 instances in a
      replacement environment for a blue/green deployment. Cannot be used in the same call as
      ec2TagSet.

      - *(dict) --*

        Information about an EC2 tag filter.

        - **Key** *(string) --*

          The tag filter key.

        - **Value** *(string) --*

          The tag filter value.

        - **Type** *(string) --*

          The tag filter type:

          * KEY_ONLY: Key only.

          * VALUE_ONLY: Value only.

          * KEY_AND_VALUE: Key and value.

    - **autoScalingGroups** *(list) --*

      The names of one or more Auto Scaling groups to identify a replacement environment for a
      blue/green deployment.

      - *(string) --*

    - **ec2TagSet** *(dict) --*

      Information about the groups of EC2 instance tags that an instance must be identified by
      in order for it to be included in the replacement environment for a blue/green
      deployment. Cannot be used in the same call as tagFilters.

      - **ec2TagSetList** *(list) --*

        A list that contains other lists of EC2 instance tag groups. For an instance to be
        included in the deployment group, it must be identified by all of the tag groups in the
        list.

        - *(list) --*

          - *(dict) --*

            Information about an EC2 tag filter.

            - **Key** *(string) --*

              The tag filter key.

            - **Value** *(string) --*

              The tag filter value.

            - **Type** *(string) --*

              The tag filter type:

              * KEY_ONLY: Key only.

              * VALUE_ONLY: Value only.

              * KEY_AND_VALUE: Key and value.
    """


_ClientGetDeploymentResponsedeploymentInfoTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfoTypeDef",
    {
        "applicationName": str,
        "deploymentGroupName": str,
        "deploymentConfigName": str,
        "deploymentId": str,
        "previousRevision": ClientGetDeploymentResponsedeploymentInfopreviousRevisionTypeDef,
        "revision": ClientGetDeploymentResponsedeploymentInforevisionTypeDef,
        "status": str,
        "errorInformation": ClientGetDeploymentResponsedeploymentInfoerrorInformationTypeDef,
        "createTime": datetime,
        "startTime": datetime,
        "completeTime": datetime,
        "deploymentOverview": ClientGetDeploymentResponsedeploymentInfodeploymentOverviewTypeDef,
        "description": str,
        "creator": str,
        "ignoreApplicationStopFailures": bool,
        "autoRollbackConfiguration": ClientGetDeploymentResponsedeploymentInfoautoRollbackConfigurationTypeDef,
        "updateOutdatedInstancesOnly": bool,
        "rollbackInfo": ClientGetDeploymentResponsedeploymentInforollbackInfoTypeDef,
        "deploymentStyle": ClientGetDeploymentResponsedeploymentInfodeploymentStyleTypeDef,
        "targetInstances": ClientGetDeploymentResponsedeploymentInfotargetInstancesTypeDef,
        "instanceTerminationWaitTimeStarted": bool,
        "blueGreenDeploymentConfiguration": ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationTypeDef,
        "loadBalancerInfo": ClientGetDeploymentResponsedeploymentInfoloadBalancerInfoTypeDef,
        "additionalDeploymentStatusInfo": str,
        "fileExistsBehavior": str,
        "deploymentStatusMessages": List[str],
        "computePlatform": str,
    },
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfoTypeDef(
    _ClientGetDeploymentResponsedeploymentInfoTypeDef
):
    """
    Type definition for `ClientGetDeploymentResponse` `deploymentInfo`

    Information about the deployment.

    - **applicationName** *(string) --*

      The application name.

    - **deploymentGroupName** *(string) --*

      The deployment group name.

    - **deploymentConfigName** *(string) --*

      The deployment configuration name.

    - **deploymentId** *(string) --*

      The unique ID of a deployment.

    - **previousRevision** *(dict) --*

      Information about the application revision that was deployed to the deployment group before
      the most recent successful deployment.

      - **revisionType** *(string) --*

        The type of application revision:

        * S3: An application revision stored in Amazon S3.

        * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

        * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

      - **s3Location** *(dict) --*

        Information about the location of a revision stored in Amazon S3.

        - **bucket** *(string) --*

          The name of the Amazon S3 bucket where the application revision is stored.

        - **key** *(string) --*

          The name of the Amazon S3 object that represents the bundled artifacts for the
          application revision.

        - **bundleType** *(string) --*

          The file type of the application revision. Must be one of the following:

          * tar: A tar archive file.

          * tgz: A compressed tar archive file.

          * zip: A zip archive file.

        - **version** *(string) --*

          A specific version of the Amazon S3 object that represents the bundled artifacts for
          the application revision.

          If the version is not specified, the system uses the most recent version by default.

        - **eTag** *(string) --*

          The ETag of the Amazon S3 object that represents the bundled artifacts for the
          application revision.

          If the ETag is not specified as an input parameter, ETag validation of the object is
          skipped.

      - **gitHubLocation** *(dict) --*

        Information about the location of application artifacts stored in GitHub.

        - **repository** *(string) --*

          The GitHub account and repository pair that stores a reference to the commit that
          represents the bundled artifacts for the application revision.

          Specified as account/repository.

        - **commitId** *(string) --*

          The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
          application revision.

      - **string** *(dict) --*

        Information about the location of an AWS Lambda deployment revision stored as a RawString.

        - **content** *(string) --*

          The YAML-formatted or JSON-formatted revision string. It includes information about
          which Lambda function to update and optional Lambda functions that validate deployment
          lifecycle events.

        - **sha256** *(string) --*

          The SHA256 hash value of the revision content.

      - **appSpecContent** *(dict) --*

        The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is
        formatted as JSON or YAML and stored as a RawString.

        - **content** *(string) --*

          The YAML-formatted or JSON-formatted revision string.

          For an AWS Lambda deployment, the content includes a Lambda function name, the alias
          for its original version, and the alias for its replacement version. The deployment
          shifts traffic from the original version of the Lambda function to the replacement
          version.

          For an Amazon ECS deployment, the content includes the task name, information about the
          load balancer that serves traffic to the container, and more.

          For both types of deployments, the content can specify Lambda functions that run at
          specified hooks, such as ``BeforeInstall`` , during a deployment.

        - **sha256** *(string) --*

          The SHA256 hash value of the revision content.

    - **revision** *(dict) --*

      Information about the location of stored application artifacts and the service from which
      to retrieve them.

      - **revisionType** *(string) --*

        The type of application revision:

        * S3: An application revision stored in Amazon S3.

        * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

        * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

      - **s3Location** *(dict) --*

        Information about the location of a revision stored in Amazon S3.

        - **bucket** *(string) --*

          The name of the Amazon S3 bucket where the application revision is stored.

        - **key** *(string) --*

          The name of the Amazon S3 object that represents the bundled artifacts for the
          application revision.

        - **bundleType** *(string) --*

          The file type of the application revision. Must be one of the following:

          * tar: A tar archive file.

          * tgz: A compressed tar archive file.

          * zip: A zip archive file.

        - **version** *(string) --*

          A specific version of the Amazon S3 object that represents the bundled artifacts for
          the application revision.

          If the version is not specified, the system uses the most recent version by default.

        - **eTag** *(string) --*

          The ETag of the Amazon S3 object that represents the bundled artifacts for the
          application revision.

          If the ETag is not specified as an input parameter, ETag validation of the object is
          skipped.

      - **gitHubLocation** *(dict) --*

        Information about the location of application artifacts stored in GitHub.

        - **repository** *(string) --*

          The GitHub account and repository pair that stores a reference to the commit that
          represents the bundled artifacts for the application revision.

          Specified as account/repository.

        - **commitId** *(string) --*

          The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
          application revision.

      - **string** *(dict) --*

        Information about the location of an AWS Lambda deployment revision stored as a RawString.

        - **content** *(string) --*

          The YAML-formatted or JSON-formatted revision string. It includes information about
          which Lambda function to update and optional Lambda functions that validate deployment
          lifecycle events.

        - **sha256** *(string) --*

          The SHA256 hash value of the revision content.

      - **appSpecContent** *(dict) --*

        The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is
        formatted as JSON or YAML and stored as a RawString.

        - **content** *(string) --*

          The YAML-formatted or JSON-formatted revision string.

          For an AWS Lambda deployment, the content includes a Lambda function name, the alias
          for its original version, and the alias for its replacement version. The deployment
          shifts traffic from the original version of the Lambda function to the replacement
          version.

          For an Amazon ECS deployment, the content includes the task name, information about the
          load balancer that serves traffic to the container, and more.

          For both types of deployments, the content can specify Lambda functions that run at
          specified hooks, such as ``BeforeInstall`` , during a deployment.

        - **sha256** *(string) --*

          The SHA256 hash value of the revision content.

    - **status** *(string) --*

      The current state of the deployment as a whole.

    - **errorInformation** *(dict) --*

      Information about any error associated with this deployment.

      - **code** *(string) --*

        For more information, see `Error Codes for AWS CodeDeploy
        <https://docs.aws.amazon.com/codedeploy/latest/userguide/error-codes.html>`__ in the `AWS
        CodeDeploy User Guide <https://docs.aws.amazon.com/codedeploy/latest/userguide>`__ .

        The error code:

        * APPLICATION_MISSING: The application was missing. This error code is most likely raised
        if the application is deleted after the deployment is created, but before it is started.

        * DEPLOYMENT_GROUP_MISSING: The deployment group was missing. This error code is most
        likely raised if the deployment group is deleted after the deployment is created, but
        before it is started.

        * HEALTH_CONSTRAINTS: The deployment failed on too many instances to be successfully
        deployed within the instance health constraints specified.

        * HEALTH_CONSTRAINTS_INVALID: The revision cannot be successfully deployed within the
        instance health constraints specified.

        * IAM_ROLE_MISSING: The service role cannot be accessed.

        * IAM_ROLE_PERMISSIONS: The service role does not have the correct permissions.

        * INTERNAL_ERROR: There was an internal error.

        * NO_EC2_SUBSCRIPTION: The calling account is not subscribed to Amazon EC2.

        * NO_INSTANCES: No instances were specified, or no instances can be found.

        * OVER_MAX_INSTANCES: The maximum number of instances was exceeded.

        * THROTTLED: The operation was throttled because the calling account exceeded the
        throttling limits of one or more AWS services.

        * TIMEOUT: The deployment has timed out.

        * REVISION_MISSING: The revision ID was missing. This error code is most likely raised if
        the revision is deleted after the deployment is created, but before it is started.

      - **message** *(string) --*

        An accompanying error message.

    - **createTime** *(datetime) --*

      A timestamp that indicates when the deployment was created.

    - **startTime** *(datetime) --*

      A timestamp that indicates when the deployment was deployed to the deployment group.

      In some cases, the reported value of the start time might be later than the complete time.
      This is due to differences in the clock settings of backend servers that participate in the
      deployment process.

    - **completeTime** *(datetime) --*

      A timestamp that indicates when the deployment was complete.

    - **deploymentOverview** *(dict) --*

      A summary of the deployment status of the instances in the deployment.

      - **Pending** *(integer) --*

        The number of instances in the deployment in a pending state.

      - **InProgress** *(integer) --*

        The number of instances in which the deployment is in progress.

      - **Succeeded** *(integer) --*

        The number of instances in the deployment to which revisions have been successfully
        deployed.

      - **Failed** *(integer) --*

        The number of instances in the deployment in a failed state.

      - **Skipped** *(integer) --*

        The number of instances in the deployment in a skipped state.

      - **Ready** *(integer) --*

        The number of instances in a replacement environment ready to receive traffic in a
        blue/green deployment.

    - **description** *(string) --*

      A comment about the deployment.

    - **creator** *(string) --*

      The means by which the deployment was created:

      * user: A user created the deployment.

      * autoscaling: Amazon EC2 Auto Scaling created the deployment.

      * codeDeployRollback: A rollback process created the deployment.

    - **ignoreApplicationStopFailures** *(boolean) --*

      If true, then if an ``ApplicationStop`` , ``BeforeBlockTraffic`` , or ``AfterBlockTraffic``
      deployment lifecycle event to an instance fails, then the deployment continues to the next
      deployment lifecycle event. For example, if ``ApplicationStop`` fails, the deployment
      continues with DownloadBundle. If ``BeforeBlockTraffic`` fails, the deployment continues
      with ``BlockTraffic`` . If ``AfterBlockTraffic`` fails, the deployment continues with
      ``ApplicationStop`` .

      If false or not specified, then if a lifecycle event fails during a deployment to an
      instance, that deployment fails. If deployment to that instance is part of an overall
      deployment and the number of healthy hosts is not less than the minimum number of healthy
      hosts, then a deployment to the next instance is attempted.

      During a deployment, the AWS CodeDeploy agent runs the scripts specified for
      ``ApplicationStop`` , ``BeforeBlockTraffic`` , and ``AfterBlockTraffic`` in the AppSpec
      file from the previous successful deployment. (All other scripts are run from the AppSpec
      file in the current deployment.) If one of these scripts contains an error and does not run
      successfully, the deployment can fail.

      If the cause of the failure is a script from the last successful deployment that will never
      run successfully, create a new deployment and use ``ignoreApplicationStopFailures`` to
      specify that the ``ApplicationStop`` , ``BeforeBlockTraffic`` , and ``AfterBlockTraffic``
      failures should be ignored.

    - **autoRollbackConfiguration** *(dict) --*

      Information about the automatic rollback configuration associated with the deployment.

      - **enabled** *(boolean) --*

        Indicates whether a defined automatic rollback configuration is currently enabled.

      - **events** *(list) --*

        The event type or types that trigger a rollback.

        - *(string) --*

    - **updateOutdatedInstancesOnly** *(boolean) --*

      Indicates whether only instances that are not running the latest application revision are
      to be deployed to.

    - **rollbackInfo** *(dict) --*

      Information about a deployment rollback.

      - **rollbackDeploymentId** *(string) --*

        The ID of the deployment rollback.

      - **rollbackTriggeringDeploymentId** *(string) --*

        The deployment ID of the deployment that was underway and triggered a rollback deployment
        because it failed or was stopped.

      - **rollbackMessage** *(string) --*

        Information that describes the status of a deployment rollback (for example, whether the
        deployment can't be rolled back, is in progress, failed, or succeeded).

    - **deploymentStyle** *(dict) --*

      Information about the type of deployment, either in-place or blue/green, you want to run
      and whether to route deployment traffic behind a load balancer.

      - **deploymentType** *(string) --*

        Indicates whether to run an in-place deployment or a blue/green deployment.

      - **deploymentOption** *(string) --*

        Indicates whether to route deployment traffic behind a load balancer.

    - **targetInstances** *(dict) --*

      Information about the instances that belong to the replacement environment in a blue/green
      deployment.

      - **tagFilters** *(list) --*

        The tag filter key, type, and value used to identify Amazon EC2 instances in a
        replacement environment for a blue/green deployment. Cannot be used in the same call as
        ec2TagSet.

        - *(dict) --*

          Information about an EC2 tag filter.

          - **Key** *(string) --*

            The tag filter key.

          - **Value** *(string) --*

            The tag filter value.

          - **Type** *(string) --*

            The tag filter type:

            * KEY_ONLY: Key only.

            * VALUE_ONLY: Value only.

            * KEY_AND_VALUE: Key and value.

      - **autoScalingGroups** *(list) --*

        The names of one or more Auto Scaling groups to identify a replacement environment for a
        blue/green deployment.

        - *(string) --*

      - **ec2TagSet** *(dict) --*

        Information about the groups of EC2 instance tags that an instance must be identified by
        in order for it to be included in the replacement environment for a blue/green
        deployment. Cannot be used in the same call as tagFilters.

        - **ec2TagSetList** *(list) --*

          A list that contains other lists of EC2 instance tag groups. For an instance to be
          included in the deployment group, it must be identified by all of the tag groups in the
          list.

          - *(list) --*

            - *(dict) --*

              Information about an EC2 tag filter.

              - **Key** *(string) --*

                The tag filter key.

              - **Value** *(string) --*

                The tag filter value.

              - **Type** *(string) --*

                The tag filter type:

                * KEY_ONLY: Key only.

                * VALUE_ONLY: Value only.

                * KEY_AND_VALUE: Key and value.

    - **instanceTerminationWaitTimeStarted** *(boolean) --*

      Indicates whether the wait period set for the termination of instances in the original
      environment has started. Status is 'false' if the KEEP_ALIVE option is specified.
      Otherwise, 'true' as soon as the termination wait period starts.

    - **blueGreenDeploymentConfiguration** *(dict) --*

      Information about blue/green deployment options for this deployment.

      - **terminateBlueInstancesOnDeploymentSuccess** *(dict) --*

        Information about whether to terminate instances in the original fleet during a
        blue/green deployment.

        - **action** *(string) --*

          The action to take on instances in the original environment after a successful
          blue/green deployment.

          * TERMINATE: Instances are terminated after a specified wait time.

          * KEEP_ALIVE: Instances are left running after they are deregistered from the load
          balancer and removed from the deployment group.

        - **terminationWaitTimeInMinutes** *(integer) --*

          For an Amazon EC2 deployment, the number of minutes to wait after a successful
          blue/green deployment before terminating instances from the original environment.

          For an Amazon ECS deployment, the number of minutes before deleting the original (blue)
          task set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the original
          (blue) task set to a replacement (green) task set.

          The maximum setting is 2880 minutes (2 days).

      - **deploymentReadyOption** *(dict) --*

        Information about the action to take when newly provisioned instances are ready to
        receive traffic in a blue/green deployment.

        - **actionOnTimeout** *(string) --*

          Information about when to reroute traffic from an original environment to a replacement
          environment in a blue/green deployment.

          * CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately after
          the new application revision is installed on the instances in the replacement
          environment.

          * STOP_DEPLOYMENT: Do not register new instances with a load balancer unless traffic
          rerouting is started using  ContinueDeployment . If traffic rerouting is not started
          before the end of the specified wait period, the deployment status is changed to
          Stopped.

        - **waitTimeInMinutes** *(integer) --*

          The number of minutes to wait before the status of a blue/green deployment is changed
          to Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT
          option for actionOnTimeout

      - **greenFleetProvisioningOption** *(dict) --*

        Information about how instances are provisioned for a replacement environment in a
        blue/green deployment.

        - **action** *(string) --*

          The method used to add instances to a replacement environment.

          * DISCOVER_EXISTING: Use instances that already exist or will be created manually.

          * COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to define
          and create instances in a new Auto Scaling group.

    - **loadBalancerInfo** *(dict) --*

      Information about the load balancer used in the deployment.

      - **elbInfoList** *(list) --*

        An array that contains information about the load balancer to use for load balancing in a
        deployment. In Elastic Load Balancing, load balancers are used with Classic Load
        Balancers.

        .. note::

          Adding more than one load balancer to the array is not supported.

        - *(dict) --*

          Information about a load balancer in Elastic Load Balancing to use in a deployment.
          Instances are registered directly with a load balancer, and traffic is routed to the
          load balancer.

          - **name** *(string) --*

            For blue/green deployments, the name of the load balancer that is used to route
            traffic from original instances to replacement instances in a blue/green deployment.
            For in-place deployments, the name of the load balancer that instances are
            deregistered from so they are not serving traffic during a deployment, and then
            re-registered with after the deployment is complete.

      - **targetGroupInfoList** *(list) --*

        An array that contains information about the target group to use for load balancing in a
        deployment. In Elastic Load Balancing, target groups are used with Application Load
        Balancers.

        .. note::

          Adding more than one target group to the array is not supported.

        - *(dict) --*

          Information about a target group in Elastic Load Balancing to use in a deployment.
          Instances are registered as targets in a target group, and traffic is routed to the
          target group.

          - **name** *(string) --*

            For blue/green deployments, the name of the target group that instances in the
            original environment are deregistered from, and instances in the replacement
            environment are registered with. For in-place deployments, the name of the target
            group that instances are deregistered from, so they are not serving traffic during a
            deployment, and then re-registered with after the deployment is complete.

      - **targetGroupPairInfoList** *(list) --*

        The target group pair information. This is an array of ``TargeGroupPairInfo`` objects
        with a maximum size of one.

        - *(dict) --*

          Information about two target groups and how traffic is routed during an Amazon ECS
          deployment. An optional test traffic route can be specified.

          - **targetGroups** *(list) --*

            One pair of target groups. One is associated with the original task set. The second
            is associated with the task set that serves traffic after the deployment is complete.

            - *(dict) --*

              Information about a target group in Elastic Load Balancing to use in a deployment.
              Instances are registered as targets in a target group, and traffic is routed to the
              target group.

              - **name** *(string) --*

                For blue/green deployments, the name of the target group that instances in the
                original environment are deregistered from, and instances in the replacement
                environment are registered with. For in-place deployments, the name of the target
                group that instances are deregistered from, so they are not serving traffic
                during a deployment, and then re-registered with after the deployment is complete.

          - **prodTrafficRoute** *(dict) --*

            The path used by a load balancer to route production traffic when an Amazon ECS
            deployment is complete.

            - **listenerArns** *(list) --*

              The ARN of one listener. The listener identifies the route between a target group
              and a load balancer. This is an array of strings with a maximum size of one.

              - *(string) --*

          - **testTrafficRoute** *(dict) --*

            An optional path used by a load balancer to route test traffic after an Amazon ECS
            deployment. Validation can occur while test traffic is served during a deployment.

            - **listenerArns** *(list) --*

              The ARN of one listener. The listener identifies the route between a target group
              and a load balancer. This is an array of strings with a maximum size of one.

              - *(string) --*

    - **additionalDeploymentStatusInfo** *(string) --*

      Provides information about the results of a deployment, such as whether instances in the
      original environment in a blue/green deployment were not terminated.

    - **fileExistsBehavior** *(string) --*

      Information about how AWS CodeDeploy handles files that already exist in a deployment
      target location but weren't part of the previous successful deployment.

      * DISALLOW: The deployment fails. This is also the default behavior if no option is
      specified.

      * OVERWRITE: The version of the file from the application revision currently being deployed
      replaces the version already on the instance.

      * RETAIN: The version of the file already on the instance is kept and used as part of the
      new deployment.

    - **deploymentStatusMessages** *(list) --*

      Messages that contain information about the status of a deployment.

      - *(string) --*

    - **computePlatform** *(string) --*

      The destination platform type for the deployment (``Lambda`` , ``Server`` , or ``ECS`` ).
    """


_ClientGetDeploymentResponseTypeDef = TypedDict(
    "_ClientGetDeploymentResponseTypeDef",
    {"deploymentInfo": ClientGetDeploymentResponsedeploymentInfoTypeDef},
    total=False,
)


class ClientGetDeploymentResponseTypeDef(_ClientGetDeploymentResponseTypeDef):
    """
    Type definition for `ClientGetDeployment` `Response`

    Represents the output of a GetDeployment operation.

    - **deploymentInfo** *(dict) --*

      Information about the deployment.

      - **applicationName** *(string) --*

        The application name.

      - **deploymentGroupName** *(string) --*

        The deployment group name.

      - **deploymentConfigName** *(string) --*

        The deployment configuration name.

      - **deploymentId** *(string) --*

        The unique ID of a deployment.

      - **previousRevision** *(dict) --*

        Information about the application revision that was deployed to the deployment group before
        the most recent successful deployment.

        - **revisionType** *(string) --*

          The type of application revision:

          * S3: An application revision stored in Amazon S3.

          * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

          * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

        - **s3Location** *(dict) --*

          Information about the location of a revision stored in Amazon S3.

          - **bucket** *(string) --*

            The name of the Amazon S3 bucket where the application revision is stored.

          - **key** *(string) --*

            The name of the Amazon S3 object that represents the bundled artifacts for the
            application revision.

          - **bundleType** *(string) --*

            The file type of the application revision. Must be one of the following:

            * tar: A tar archive file.

            * tgz: A compressed tar archive file.

            * zip: A zip archive file.

          - **version** *(string) --*

            A specific version of the Amazon S3 object that represents the bundled artifacts for
            the application revision.

            If the version is not specified, the system uses the most recent version by default.

          - **eTag** *(string) --*

            The ETag of the Amazon S3 object that represents the bundled artifacts for the
            application revision.

            If the ETag is not specified as an input parameter, ETag validation of the object is
            skipped.

        - **gitHubLocation** *(dict) --*

          Information about the location of application artifacts stored in GitHub.

          - **repository** *(string) --*

            The GitHub account and repository pair that stores a reference to the commit that
            represents the bundled artifacts for the application revision.

            Specified as account/repository.

          - **commitId** *(string) --*

            The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
            application revision.

        - **string** *(dict) --*

          Information about the location of an AWS Lambda deployment revision stored as a RawString.

          - **content** *(string) --*

            The YAML-formatted or JSON-formatted revision string. It includes information about
            which Lambda function to update and optional Lambda functions that validate deployment
            lifecycle events.

          - **sha256** *(string) --*

            The SHA256 hash value of the revision content.

        - **appSpecContent** *(dict) --*

          The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is
          formatted as JSON or YAML and stored as a RawString.

          - **content** *(string) --*

            The YAML-formatted or JSON-formatted revision string.

            For an AWS Lambda deployment, the content includes a Lambda function name, the alias
            for its original version, and the alias for its replacement version. The deployment
            shifts traffic from the original version of the Lambda function to the replacement
            version.

            For an Amazon ECS deployment, the content includes the task name, information about the
            load balancer that serves traffic to the container, and more.

            For both types of deployments, the content can specify Lambda functions that run at
            specified hooks, such as ``BeforeInstall`` , during a deployment.

          - **sha256** *(string) --*

            The SHA256 hash value of the revision content.

      - **revision** *(dict) --*

        Information about the location of stored application artifacts and the service from which
        to retrieve them.

        - **revisionType** *(string) --*

          The type of application revision:

          * S3: An application revision stored in Amazon S3.

          * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

          * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

        - **s3Location** *(dict) --*

          Information about the location of a revision stored in Amazon S3.

          - **bucket** *(string) --*

            The name of the Amazon S3 bucket where the application revision is stored.

          - **key** *(string) --*

            The name of the Amazon S3 object that represents the bundled artifacts for the
            application revision.

          - **bundleType** *(string) --*

            The file type of the application revision. Must be one of the following:

            * tar: A tar archive file.

            * tgz: A compressed tar archive file.

            * zip: A zip archive file.

          - **version** *(string) --*

            A specific version of the Amazon S3 object that represents the bundled artifacts for
            the application revision.

            If the version is not specified, the system uses the most recent version by default.

          - **eTag** *(string) --*

            The ETag of the Amazon S3 object that represents the bundled artifacts for the
            application revision.

            If the ETag is not specified as an input parameter, ETag validation of the object is
            skipped.

        - **gitHubLocation** *(dict) --*

          Information about the location of application artifacts stored in GitHub.

          - **repository** *(string) --*

            The GitHub account and repository pair that stores a reference to the commit that
            represents the bundled artifacts for the application revision.

            Specified as account/repository.

          - **commitId** *(string) --*

            The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
            application revision.

        - **string** *(dict) --*

          Information about the location of an AWS Lambda deployment revision stored as a RawString.

          - **content** *(string) --*

            The YAML-formatted or JSON-formatted revision string. It includes information about
            which Lambda function to update and optional Lambda functions that validate deployment
            lifecycle events.

          - **sha256** *(string) --*

            The SHA256 hash value of the revision content.

        - **appSpecContent** *(dict) --*

          The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is
          formatted as JSON or YAML and stored as a RawString.

          - **content** *(string) --*

            The YAML-formatted or JSON-formatted revision string.

            For an AWS Lambda deployment, the content includes a Lambda function name, the alias
            for its original version, and the alias for its replacement version. The deployment
            shifts traffic from the original version of the Lambda function to the replacement
            version.

            For an Amazon ECS deployment, the content includes the task name, information about the
            load balancer that serves traffic to the container, and more.

            For both types of deployments, the content can specify Lambda functions that run at
            specified hooks, such as ``BeforeInstall`` , during a deployment.

          - **sha256** *(string) --*

            The SHA256 hash value of the revision content.

      - **status** *(string) --*

        The current state of the deployment as a whole.

      - **errorInformation** *(dict) --*

        Information about any error associated with this deployment.

        - **code** *(string) --*

          For more information, see `Error Codes for AWS CodeDeploy
          <https://docs.aws.amazon.com/codedeploy/latest/userguide/error-codes.html>`__ in the `AWS
          CodeDeploy User Guide <https://docs.aws.amazon.com/codedeploy/latest/userguide>`__ .

          The error code:

          * APPLICATION_MISSING: The application was missing. This error code is most likely raised
          if the application is deleted after the deployment is created, but before it is started.

          * DEPLOYMENT_GROUP_MISSING: The deployment group was missing. This error code is most
          likely raised if the deployment group is deleted after the deployment is created, but
          before it is started.

          * HEALTH_CONSTRAINTS: The deployment failed on too many instances to be successfully
          deployed within the instance health constraints specified.

          * HEALTH_CONSTRAINTS_INVALID: The revision cannot be successfully deployed within the
          instance health constraints specified.

          * IAM_ROLE_MISSING: The service role cannot be accessed.

          * IAM_ROLE_PERMISSIONS: The service role does not have the correct permissions.

          * INTERNAL_ERROR: There was an internal error.

          * NO_EC2_SUBSCRIPTION: The calling account is not subscribed to Amazon EC2.

          * NO_INSTANCES: No instances were specified, or no instances can be found.

          * OVER_MAX_INSTANCES: The maximum number of instances was exceeded.

          * THROTTLED: The operation was throttled because the calling account exceeded the
          throttling limits of one or more AWS services.

          * TIMEOUT: The deployment has timed out.

          * REVISION_MISSING: The revision ID was missing. This error code is most likely raised if
          the revision is deleted after the deployment is created, but before it is started.

        - **message** *(string) --*

          An accompanying error message.

      - **createTime** *(datetime) --*

        A timestamp that indicates when the deployment was created.

      - **startTime** *(datetime) --*

        A timestamp that indicates when the deployment was deployed to the deployment group.

        In some cases, the reported value of the start time might be later than the complete time.
        This is due to differences in the clock settings of backend servers that participate in the
        deployment process.

      - **completeTime** *(datetime) --*

        A timestamp that indicates when the deployment was complete.

      - **deploymentOverview** *(dict) --*

        A summary of the deployment status of the instances in the deployment.

        - **Pending** *(integer) --*

          The number of instances in the deployment in a pending state.

        - **InProgress** *(integer) --*

          The number of instances in which the deployment is in progress.

        - **Succeeded** *(integer) --*

          The number of instances in the deployment to which revisions have been successfully
          deployed.

        - **Failed** *(integer) --*

          The number of instances in the deployment in a failed state.

        - **Skipped** *(integer) --*

          The number of instances in the deployment in a skipped state.

        - **Ready** *(integer) --*

          The number of instances in a replacement environment ready to receive traffic in a
          blue/green deployment.

      - **description** *(string) --*

        A comment about the deployment.

      - **creator** *(string) --*

        The means by which the deployment was created:

        * user: A user created the deployment.

        * autoscaling: Amazon EC2 Auto Scaling created the deployment.

        * codeDeployRollback: A rollback process created the deployment.

      - **ignoreApplicationStopFailures** *(boolean) --*

        If true, then if an ``ApplicationStop`` , ``BeforeBlockTraffic`` , or ``AfterBlockTraffic``
        deployment lifecycle event to an instance fails, then the deployment continues to the next
        deployment lifecycle event. For example, if ``ApplicationStop`` fails, the deployment
        continues with DownloadBundle. If ``BeforeBlockTraffic`` fails, the deployment continues
        with ``BlockTraffic`` . If ``AfterBlockTraffic`` fails, the deployment continues with
        ``ApplicationStop`` .

        If false or not specified, then if a lifecycle event fails during a deployment to an
        instance, that deployment fails. If deployment to that instance is part of an overall
        deployment and the number of healthy hosts is not less than the minimum number of healthy
        hosts, then a deployment to the next instance is attempted.

        During a deployment, the AWS CodeDeploy agent runs the scripts specified for
        ``ApplicationStop`` , ``BeforeBlockTraffic`` , and ``AfterBlockTraffic`` in the AppSpec
        file from the previous successful deployment. (All other scripts are run from the AppSpec
        file in the current deployment.) If one of these scripts contains an error and does not run
        successfully, the deployment can fail.

        If the cause of the failure is a script from the last successful deployment that will never
        run successfully, create a new deployment and use ``ignoreApplicationStopFailures`` to
        specify that the ``ApplicationStop`` , ``BeforeBlockTraffic`` , and ``AfterBlockTraffic``
        failures should be ignored.

      - **autoRollbackConfiguration** *(dict) --*

        Information about the automatic rollback configuration associated with the deployment.

        - **enabled** *(boolean) --*

          Indicates whether a defined automatic rollback configuration is currently enabled.

        - **events** *(list) --*

          The event type or types that trigger a rollback.

          - *(string) --*

      - **updateOutdatedInstancesOnly** *(boolean) --*

        Indicates whether only instances that are not running the latest application revision are
        to be deployed to.

      - **rollbackInfo** *(dict) --*

        Information about a deployment rollback.

        - **rollbackDeploymentId** *(string) --*

          The ID of the deployment rollback.

        - **rollbackTriggeringDeploymentId** *(string) --*

          The deployment ID of the deployment that was underway and triggered a rollback deployment
          because it failed or was stopped.

        - **rollbackMessage** *(string) --*

          Information that describes the status of a deployment rollback (for example, whether the
          deployment can't be rolled back, is in progress, failed, or succeeded).

      - **deploymentStyle** *(dict) --*

        Information about the type of deployment, either in-place or blue/green, you want to run
        and whether to route deployment traffic behind a load balancer.

        - **deploymentType** *(string) --*

          Indicates whether to run an in-place deployment or a blue/green deployment.

        - **deploymentOption** *(string) --*

          Indicates whether to route deployment traffic behind a load balancer.

      - **targetInstances** *(dict) --*

        Information about the instances that belong to the replacement environment in a blue/green
        deployment.

        - **tagFilters** *(list) --*

          The tag filter key, type, and value used to identify Amazon EC2 instances in a
          replacement environment for a blue/green deployment. Cannot be used in the same call as
          ec2TagSet.

          - *(dict) --*

            Information about an EC2 tag filter.

            - **Key** *(string) --*

              The tag filter key.

            - **Value** *(string) --*

              The tag filter value.

            - **Type** *(string) --*

              The tag filter type:

              * KEY_ONLY: Key only.

              * VALUE_ONLY: Value only.

              * KEY_AND_VALUE: Key and value.

        - **autoScalingGroups** *(list) --*

          The names of one or more Auto Scaling groups to identify a replacement environment for a
          blue/green deployment.

          - *(string) --*

        - **ec2TagSet** *(dict) --*

          Information about the groups of EC2 instance tags that an instance must be identified by
          in order for it to be included in the replacement environment for a blue/green
          deployment. Cannot be used in the same call as tagFilters.

          - **ec2TagSetList** *(list) --*

            A list that contains other lists of EC2 instance tag groups. For an instance to be
            included in the deployment group, it must be identified by all of the tag groups in the
            list.

            - *(list) --*

              - *(dict) --*

                Information about an EC2 tag filter.

                - **Key** *(string) --*

                  The tag filter key.

                - **Value** *(string) --*

                  The tag filter value.

                - **Type** *(string) --*

                  The tag filter type:

                  * KEY_ONLY: Key only.

                  * VALUE_ONLY: Value only.

                  * KEY_AND_VALUE: Key and value.

      - **instanceTerminationWaitTimeStarted** *(boolean) --*

        Indicates whether the wait period set for the termination of instances in the original
        environment has started. Status is 'false' if the KEEP_ALIVE option is specified.
        Otherwise, 'true' as soon as the termination wait period starts.

      - **blueGreenDeploymentConfiguration** *(dict) --*

        Information about blue/green deployment options for this deployment.

        - **terminateBlueInstancesOnDeploymentSuccess** *(dict) --*

          Information about whether to terminate instances in the original fleet during a
          blue/green deployment.

          - **action** *(string) --*

            The action to take on instances in the original environment after a successful
            blue/green deployment.

            * TERMINATE: Instances are terminated after a specified wait time.

            * KEEP_ALIVE: Instances are left running after they are deregistered from the load
            balancer and removed from the deployment group.

          - **terminationWaitTimeInMinutes** *(integer) --*

            For an Amazon EC2 deployment, the number of minutes to wait after a successful
            blue/green deployment before terminating instances from the original environment.

            For an Amazon ECS deployment, the number of minutes before deleting the original (blue)
            task set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the original
            (blue) task set to a replacement (green) task set.

            The maximum setting is 2880 minutes (2 days).

        - **deploymentReadyOption** *(dict) --*

          Information about the action to take when newly provisioned instances are ready to
          receive traffic in a blue/green deployment.

          - **actionOnTimeout** *(string) --*

            Information about when to reroute traffic from an original environment to a replacement
            environment in a blue/green deployment.

            * CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately after
            the new application revision is installed on the instances in the replacement
            environment.

            * STOP_DEPLOYMENT: Do not register new instances with a load balancer unless traffic
            rerouting is started using  ContinueDeployment . If traffic rerouting is not started
            before the end of the specified wait period, the deployment status is changed to
            Stopped.

          - **waitTimeInMinutes** *(integer) --*

            The number of minutes to wait before the status of a blue/green deployment is changed
            to Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT
            option for actionOnTimeout

        - **greenFleetProvisioningOption** *(dict) --*

          Information about how instances are provisioned for a replacement environment in a
          blue/green deployment.

          - **action** *(string) --*

            The method used to add instances to a replacement environment.

            * DISCOVER_EXISTING: Use instances that already exist or will be created manually.

            * COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to define
            and create instances in a new Auto Scaling group.

      - **loadBalancerInfo** *(dict) --*

        Information about the load balancer used in the deployment.

        - **elbInfoList** *(list) --*

          An array that contains information about the load balancer to use for load balancing in a
          deployment. In Elastic Load Balancing, load balancers are used with Classic Load
          Balancers.

          .. note::

            Adding more than one load balancer to the array is not supported.

          - *(dict) --*

            Information about a load balancer in Elastic Load Balancing to use in a deployment.
            Instances are registered directly with a load balancer, and traffic is routed to the
            load balancer.

            - **name** *(string) --*

              For blue/green deployments, the name of the load balancer that is used to route
              traffic from original instances to replacement instances in a blue/green deployment.
              For in-place deployments, the name of the load balancer that instances are
              deregistered from so they are not serving traffic during a deployment, and then
              re-registered with after the deployment is complete.

        - **targetGroupInfoList** *(list) --*

          An array that contains information about the target group to use for load balancing in a
          deployment. In Elastic Load Balancing, target groups are used with Application Load
          Balancers.

          .. note::

            Adding more than one target group to the array is not supported.

          - *(dict) --*

            Information about a target group in Elastic Load Balancing to use in a deployment.
            Instances are registered as targets in a target group, and traffic is routed to the
            target group.

            - **name** *(string) --*

              For blue/green deployments, the name of the target group that instances in the
              original environment are deregistered from, and instances in the replacement
              environment are registered with. For in-place deployments, the name of the target
              group that instances are deregistered from, so they are not serving traffic during a
              deployment, and then re-registered with after the deployment is complete.

        - **targetGroupPairInfoList** *(list) --*

          The target group pair information. This is an array of ``TargeGroupPairInfo`` objects
          with a maximum size of one.

          - *(dict) --*

            Information about two target groups and how traffic is routed during an Amazon ECS
            deployment. An optional test traffic route can be specified.

            - **targetGroups** *(list) --*

              One pair of target groups. One is associated with the original task set. The second
              is associated with the task set that serves traffic after the deployment is complete.

              - *(dict) --*

                Information about a target group in Elastic Load Balancing to use in a deployment.
                Instances are registered as targets in a target group, and traffic is routed to the
                target group.

                - **name** *(string) --*

                  For blue/green deployments, the name of the target group that instances in the
                  original environment are deregistered from, and instances in the replacement
                  environment are registered with. For in-place deployments, the name of the target
                  group that instances are deregistered from, so they are not serving traffic
                  during a deployment, and then re-registered with after the deployment is complete.

            - **prodTrafficRoute** *(dict) --*

              The path used by a load balancer to route production traffic when an Amazon ECS
              deployment is complete.

              - **listenerArns** *(list) --*

                The ARN of one listener. The listener identifies the route between a target group
                and a load balancer. This is an array of strings with a maximum size of one.

                - *(string) --*

            - **testTrafficRoute** *(dict) --*

              An optional path used by a load balancer to route test traffic after an Amazon ECS
              deployment. Validation can occur while test traffic is served during a deployment.

              - **listenerArns** *(list) --*

                The ARN of one listener. The listener identifies the route between a target group
                and a load balancer. This is an array of strings with a maximum size of one.

                - *(string) --*

      - **additionalDeploymentStatusInfo** *(string) --*

        Provides information about the results of a deployment, such as whether instances in the
        original environment in a blue/green deployment were not terminated.

      - **fileExistsBehavior** *(string) --*

        Information about how AWS CodeDeploy handles files that already exist in a deployment
        target location but weren't part of the previous successful deployment.

        * DISALLOW: The deployment fails. This is also the default behavior if no option is
        specified.

        * OVERWRITE: The version of the file from the application revision currently being deployed
        replaces the version already on the instance.

        * RETAIN: The version of the file already on the instance is kept and used as part of the
        new deployment.

      - **deploymentStatusMessages** *(list) --*

        Messages that contain information about the status of a deployment.

        - *(string) --*

      - **computePlatform** *(string) --*

        The destination platform type for the deployment (``Lambda`` , ``Server`` , or ``ECS`` ).
    """


_ClientGetDeploymentTargetResponsedeploymentTargetecsTargetlifecycleEventsdiagnosticsTypeDef = TypedDict(
    "_ClientGetDeploymentTargetResponsedeploymentTargetecsTargetlifecycleEventsdiagnosticsTypeDef",
    {"errorCode": str, "scriptName": str, "message": str, "logTail": str},
    total=False,
)


class ClientGetDeploymentTargetResponsedeploymentTargetecsTargetlifecycleEventsdiagnosticsTypeDef(
    _ClientGetDeploymentTargetResponsedeploymentTargetecsTargetlifecycleEventsdiagnosticsTypeDef
):
    """
    Type definition for `ClientGetDeploymentTargetResponsedeploymentTargetecsTargetlifecycleEvents` `diagnostics`

    Diagnostic information about the deployment lifecycle event.

    - **errorCode** *(string) --*

      The associated error code:

      * Success: The specified script ran.

      * ScriptMissing: The specified script was not found in the specified location.

      * ScriptNotExecutable: The specified script is not a recognized executable file
      type.

      * ScriptTimedOut: The specified script did not finish running in the specified time
      period.

      * ScriptFailed: The specified script failed to run as expected.

      * UnknownError: The specified script did not run for an unknown reason.

    - **scriptName** *(string) --*

      The name of the script.

    - **message** *(string) --*

      The message associated with the error.

    - **logTail** *(string) --*

      The last portion of the diagnostic log.

      If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.
    """


_ClientGetDeploymentTargetResponsedeploymentTargetecsTargetlifecycleEventsTypeDef = TypedDict(
    "_ClientGetDeploymentTargetResponsedeploymentTargetecsTargetlifecycleEventsTypeDef",
    {
        "lifecycleEventName": str,
        "diagnostics": ClientGetDeploymentTargetResponsedeploymentTargetecsTargetlifecycleEventsdiagnosticsTypeDef,
        "startTime": datetime,
        "endTime": datetime,
        "status": str,
    },
    total=False,
)


class ClientGetDeploymentTargetResponsedeploymentTargetecsTargetlifecycleEventsTypeDef(
    _ClientGetDeploymentTargetResponsedeploymentTargetecsTargetlifecycleEventsTypeDef
):
    """
    Type definition for `ClientGetDeploymentTargetResponsedeploymentTargetecsTarget` `lifecycleEvents`

    Information about a deployment lifecycle event.

    - **lifecycleEventName** *(string) --*

      The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
      AfterInstall, ApplicationStart, or ValidateService.

    - **diagnostics** *(dict) --*

      Diagnostic information about the deployment lifecycle event.

      - **errorCode** *(string) --*

        The associated error code:

        * Success: The specified script ran.

        * ScriptMissing: The specified script was not found in the specified location.

        * ScriptNotExecutable: The specified script is not a recognized executable file
        type.

        * ScriptTimedOut: The specified script did not finish running in the specified time
        period.

        * ScriptFailed: The specified script failed to run as expected.

        * UnknownError: The specified script did not run for an unknown reason.

      - **scriptName** *(string) --*

        The name of the script.

      - **message** *(string) --*

        The message associated with the error.

      - **logTail** *(string) --*

        The last portion of the diagnostic log.

        If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.

    - **startTime** *(datetime) --*

      A timestamp that indicates when the deployment lifecycle event started.

    - **endTime** *(datetime) --*

      A timestamp that indicates when the deployment lifecycle event ended.

    - **status** *(string) --*

      The deployment lifecycle event status:

      * Pending: The deployment lifecycle event is pending.

      * InProgress: The deployment lifecycle event is in progress.

      * Succeeded: The deployment lifecycle event ran successfully.

      * Failed: The deployment lifecycle event has failed.

      * Skipped: The deployment lifecycle event has been skipped.

      * Unknown: The deployment lifecycle event is unknown.
    """


_ClientGetDeploymentTargetResponsedeploymentTargetecsTargettaskSetsInfotargetGroupTypeDef = TypedDict(
    "_ClientGetDeploymentTargetResponsedeploymentTargetecsTargettaskSetsInfotargetGroupTypeDef",
    {"name": str},
    total=False,
)


class ClientGetDeploymentTargetResponsedeploymentTargetecsTargettaskSetsInfotargetGroupTypeDef(
    _ClientGetDeploymentTargetResponsedeploymentTargetecsTargettaskSetsInfotargetGroupTypeDef
):
    """
    Type definition for `ClientGetDeploymentTargetResponsedeploymentTargetecsTargettaskSetsInfo` `targetGroup`

    The target group associated with the task set. The target group is used by AWS
    CodeDeploy to manage traffic to a task set.

    - **name** *(string) --*

      For blue/green deployments, the name of the target group that instances in the
      original environment are deregistered from, and instances in the replacement
      environment are registered with. For in-place deployments, the name of the target
      group that instances are deregistered from, so they are not serving traffic during
      a deployment, and then re-registered with after the deployment is complete.
    """


_ClientGetDeploymentTargetResponsedeploymentTargetecsTargettaskSetsInfoTypeDef = TypedDict(
    "_ClientGetDeploymentTargetResponsedeploymentTargetecsTargettaskSetsInfoTypeDef",
    {
        "identifer": str,
        "desiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "status": str,
        "trafficWeight": float,
        "targetGroup": ClientGetDeploymentTargetResponsedeploymentTargetecsTargettaskSetsInfotargetGroupTypeDef,
        "taskSetLabel": str,
    },
    total=False,
)


class ClientGetDeploymentTargetResponsedeploymentTargetecsTargettaskSetsInfoTypeDef(
    _ClientGetDeploymentTargetResponsedeploymentTargetecsTargettaskSetsInfoTypeDef
):
    """
    Type definition for `ClientGetDeploymentTargetResponsedeploymentTargetecsTarget` `taskSetsInfo`

    Information about a set of Amazon ECS tasks in an AWS CodeDeploy deployment. An Amazon
    ECS task set includes details such as the desired number of tasks, how many tasks are
    running, and whether the task set serves production traffic. An AWS CodeDeploy
    application that uses the Amazon ECS compute platform deploys a containerized
    application in an Amazon ECS service as a task set.

    - **identifer** *(string) --*

      A unique ID of an ``ECSTaskSet`` .

    - **desiredCount** *(integer) --*

      The number of tasks in a task set. During a deployment that uses the Amazon ECS
      compute type, CodeDeploy instructs Amazon ECS to create a new task set and uses this
      value to determine how many tasks to create. After the updated task set is created,
      CodeDeploy shifts traffic to the new task set.

    - **pendingCount** *(integer) --*

      The number of tasks in the task set that are in the ``PENDING`` status during an
      Amazon ECS deployment. A task in the ``PENDING`` state is preparing to enter the
      ``RUNNING`` state. A task set enters the ``PENDING`` status when it launches for the
      first time, or when it is restarted after being in the ``STOPPED`` state.

    - **runningCount** *(integer) --*

      The number of tasks in the task set that are in the ``RUNNING`` status during an
      Amazon ECS deployment. A task in the ``RUNNING`` state is running and ready for use.

    - **status** *(string) --*

      The status of the task set. There are three valid task set statuses:

      * ``PRIMARY`` : Indicates the task set is serving production traffic.

      * ``ACTIVE`` : Indicates the task set is not serving production traffic.

      * ``DRAINING`` : Indicates the tasks in the task set are being stopped and their
      corresponding targets are being deregistered from their target group.

    - **trafficWeight** *(float) --*

      The percentage of traffic served by this task set.

    - **targetGroup** *(dict) --*

      The target group associated with the task set. The target group is used by AWS
      CodeDeploy to manage traffic to a task set.

      - **name** *(string) --*

        For blue/green deployments, the name of the target group that instances in the
        original environment are deregistered from, and instances in the replacement
        environment are registered with. For in-place deployments, the name of the target
        group that instances are deregistered from, so they are not serving traffic during
        a deployment, and then re-registered with after the deployment is complete.

    - **taskSetLabel** *(string) --*

      A label that identifies whether the ECS task set is an original target (``BLUE`` ) or
      a replacement target (``GREEN`` ).
    """


_ClientGetDeploymentTargetResponsedeploymentTargetecsTargetTypeDef = TypedDict(
    "_ClientGetDeploymentTargetResponsedeploymentTargetecsTargetTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
        "targetArn": str,
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List[
            ClientGetDeploymentTargetResponsedeploymentTargetecsTargetlifecycleEventsTypeDef
        ],
        "status": str,
        "taskSetsInfo": List[
            ClientGetDeploymentTargetResponsedeploymentTargetecsTargettaskSetsInfoTypeDef
        ],
    },
    total=False,
)


class ClientGetDeploymentTargetResponsedeploymentTargetecsTargetTypeDef(
    _ClientGetDeploymentTargetResponsedeploymentTargetecsTargetTypeDef
):
    """
    Type definition for `ClientGetDeploymentTargetResponsedeploymentTarget` `ecsTarget`

    Information about the target for a deployment that uses the Amazon ECS compute platform.

    - **deploymentId** *(string) --*

      The unique ID of a deployment.

    - **targetId** *(string) --*

      The unique ID of a deployment target that has a type of ``ecsTarget`` .

    - **targetArn** *(string) --*

      The ARN of the target.

    - **lastUpdatedAt** *(datetime) --*

      The date and time when the target Amazon ECS application was updated by a deployment.

    - **lifecycleEvents** *(list) --*

      The lifecycle events of the deployment to this target Amazon ECS application.

      - *(dict) --*

        Information about a deployment lifecycle event.

        - **lifecycleEventName** *(string) --*

          The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
          AfterInstall, ApplicationStart, or ValidateService.

        - **diagnostics** *(dict) --*

          Diagnostic information about the deployment lifecycle event.

          - **errorCode** *(string) --*

            The associated error code:

            * Success: The specified script ran.

            * ScriptMissing: The specified script was not found in the specified location.

            * ScriptNotExecutable: The specified script is not a recognized executable file
            type.

            * ScriptTimedOut: The specified script did not finish running in the specified time
            period.

            * ScriptFailed: The specified script failed to run as expected.

            * UnknownError: The specified script did not run for an unknown reason.

          - **scriptName** *(string) --*

            The name of the script.

          - **message** *(string) --*

            The message associated with the error.

          - **logTail** *(string) --*

            The last portion of the diagnostic log.

            If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.

        - **startTime** *(datetime) --*

          A timestamp that indicates when the deployment lifecycle event started.

        - **endTime** *(datetime) --*

          A timestamp that indicates when the deployment lifecycle event ended.

        - **status** *(string) --*

          The deployment lifecycle event status:

          * Pending: The deployment lifecycle event is pending.

          * InProgress: The deployment lifecycle event is in progress.

          * Succeeded: The deployment lifecycle event ran successfully.

          * Failed: The deployment lifecycle event has failed.

          * Skipped: The deployment lifecycle event has been skipped.

          * Unknown: The deployment lifecycle event is unknown.

    - **status** *(string) --*

      The status an Amazon ECS deployment's target ECS application.

    - **taskSetsInfo** *(list) --*

      The ``ECSTaskSet`` objects associated with the ECS target.

      - *(dict) --*

        Information about a set of Amazon ECS tasks in an AWS CodeDeploy deployment. An Amazon
        ECS task set includes details such as the desired number of tasks, how many tasks are
        running, and whether the task set serves production traffic. An AWS CodeDeploy
        application that uses the Amazon ECS compute platform deploys a containerized
        application in an Amazon ECS service as a task set.

        - **identifer** *(string) --*

          A unique ID of an ``ECSTaskSet`` .

        - **desiredCount** *(integer) --*

          The number of tasks in a task set. During a deployment that uses the Amazon ECS
          compute type, CodeDeploy instructs Amazon ECS to create a new task set and uses this
          value to determine how many tasks to create. After the updated task set is created,
          CodeDeploy shifts traffic to the new task set.

        - **pendingCount** *(integer) --*

          The number of tasks in the task set that are in the ``PENDING`` status during an
          Amazon ECS deployment. A task in the ``PENDING`` state is preparing to enter the
          ``RUNNING`` state. A task set enters the ``PENDING`` status when it launches for the
          first time, or when it is restarted after being in the ``STOPPED`` state.

        - **runningCount** *(integer) --*

          The number of tasks in the task set that are in the ``RUNNING`` status during an
          Amazon ECS deployment. A task in the ``RUNNING`` state is running and ready for use.

        - **status** *(string) --*

          The status of the task set. There are three valid task set statuses:

          * ``PRIMARY`` : Indicates the task set is serving production traffic.

          * ``ACTIVE`` : Indicates the task set is not serving production traffic.

          * ``DRAINING`` : Indicates the tasks in the task set are being stopped and their
          corresponding targets are being deregistered from their target group.

        - **trafficWeight** *(float) --*

          The percentage of traffic served by this task set.

        - **targetGroup** *(dict) --*

          The target group associated with the task set. The target group is used by AWS
          CodeDeploy to manage traffic to a task set.

          - **name** *(string) --*

            For blue/green deployments, the name of the target group that instances in the
            original environment are deregistered from, and instances in the replacement
            environment are registered with. For in-place deployments, the name of the target
            group that instances are deregistered from, so they are not serving traffic during
            a deployment, and then re-registered with after the deployment is complete.

        - **taskSetLabel** *(string) --*

          A label that identifies whether the ECS task set is an original target (``BLUE`` ) or
          a replacement target (``GREEN`` ).
    """


_ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetlifecycleEventsdiagnosticsTypeDef = TypedDict(
    "_ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetlifecycleEventsdiagnosticsTypeDef",
    {"errorCode": str, "scriptName": str, "message": str, "logTail": str},
    total=False,
)


class ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetlifecycleEventsdiagnosticsTypeDef(
    _ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetlifecycleEventsdiagnosticsTypeDef
):
    """
    Type definition for `ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetlifecycleEvents` `diagnostics`

    Diagnostic information about the deployment lifecycle event.

    - **errorCode** *(string) --*

      The associated error code:

      * Success: The specified script ran.

      * ScriptMissing: The specified script was not found in the specified location.

      * ScriptNotExecutable: The specified script is not a recognized executable file
      type.

      * ScriptTimedOut: The specified script did not finish running in the specified time
      period.

      * ScriptFailed: The specified script failed to run as expected.

      * UnknownError: The specified script did not run for an unknown reason.

    - **scriptName** *(string) --*

      The name of the script.

    - **message** *(string) --*

      The message associated with the error.

    - **logTail** *(string) --*

      The last portion of the diagnostic log.

      If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.
    """


_ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetlifecycleEventsTypeDef = TypedDict(
    "_ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetlifecycleEventsTypeDef",
    {
        "lifecycleEventName": str,
        "diagnostics": ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetlifecycleEventsdiagnosticsTypeDef,
        "startTime": datetime,
        "endTime": datetime,
        "status": str,
    },
    total=False,
)


class ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetlifecycleEventsTypeDef(
    _ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetlifecycleEventsTypeDef
):
    """
    Type definition for `ClientGetDeploymentTargetResponsedeploymentTargetinstanceTarget` `lifecycleEvents`

    Information about a deployment lifecycle event.

    - **lifecycleEventName** *(string) --*

      The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
      AfterInstall, ApplicationStart, or ValidateService.

    - **diagnostics** *(dict) --*

      Diagnostic information about the deployment lifecycle event.

      - **errorCode** *(string) --*

        The associated error code:

        * Success: The specified script ran.

        * ScriptMissing: The specified script was not found in the specified location.

        * ScriptNotExecutable: The specified script is not a recognized executable file
        type.

        * ScriptTimedOut: The specified script did not finish running in the specified time
        period.

        * ScriptFailed: The specified script failed to run as expected.

        * UnknownError: The specified script did not run for an unknown reason.

      - **scriptName** *(string) --*

        The name of the script.

      - **message** *(string) --*

        The message associated with the error.

      - **logTail** *(string) --*

        The last portion of the diagnostic log.

        If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.

    - **startTime** *(datetime) --*

      A timestamp that indicates when the deployment lifecycle event started.

    - **endTime** *(datetime) --*

      A timestamp that indicates when the deployment lifecycle event ended.

    - **status** *(string) --*

      The deployment lifecycle event status:

      * Pending: The deployment lifecycle event is pending.

      * InProgress: The deployment lifecycle event is in progress.

      * Succeeded: The deployment lifecycle event ran successfully.

      * Failed: The deployment lifecycle event has failed.

      * Skipped: The deployment lifecycle event has been skipped.

      * Unknown: The deployment lifecycle event is unknown.
    """


_ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetTypeDef = TypedDict(
    "_ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
        "targetArn": str,
        "status": str,
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List[
            ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetlifecycleEventsTypeDef
        ],
        "instanceLabel": str,
    },
    total=False,
)


class ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetTypeDef(
    _ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetTypeDef
):
    """
    Type definition for `ClientGetDeploymentTargetResponsedeploymentTarget` `instanceTarget`

    Information about the target for a deployment that uses the EC2/On-premises compute
    platform.

    - **deploymentId** *(string) --*

      The unique ID of a deployment.

    - **targetId** *(string) --*

      The unique ID of a deployment target that has a type of ``instanceTarget`` .

    - **targetArn** *(string) --*

      The ARN of the target.

    - **status** *(string) --*

      The status an EC2/On-premises deployment's target instance.

    - **lastUpdatedAt** *(datetime) --*

      The date and time when the target instance was updated by a deployment.

    - **lifecycleEvents** *(list) --*

      The lifecycle events of the deployment to this target instance.

      - *(dict) --*

        Information about a deployment lifecycle event.

        - **lifecycleEventName** *(string) --*

          The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
          AfterInstall, ApplicationStart, or ValidateService.

        - **diagnostics** *(dict) --*

          Diagnostic information about the deployment lifecycle event.

          - **errorCode** *(string) --*

            The associated error code:

            * Success: The specified script ran.

            * ScriptMissing: The specified script was not found in the specified location.

            * ScriptNotExecutable: The specified script is not a recognized executable file
            type.

            * ScriptTimedOut: The specified script did not finish running in the specified time
            period.

            * ScriptFailed: The specified script failed to run as expected.

            * UnknownError: The specified script did not run for an unknown reason.

          - **scriptName** *(string) --*

            The name of the script.

          - **message** *(string) --*

            The message associated with the error.

          - **logTail** *(string) --*

            The last portion of the diagnostic log.

            If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.

        - **startTime** *(datetime) --*

          A timestamp that indicates when the deployment lifecycle event started.

        - **endTime** *(datetime) --*

          A timestamp that indicates when the deployment lifecycle event ended.

        - **status** *(string) --*

          The deployment lifecycle event status:

          * Pending: The deployment lifecycle event is pending.

          * InProgress: The deployment lifecycle event is in progress.

          * Succeeded: The deployment lifecycle event ran successfully.

          * Failed: The deployment lifecycle event has failed.

          * Skipped: The deployment lifecycle event has been skipped.

          * Unknown: The deployment lifecycle event is unknown.

    - **instanceLabel** *(string) --*

      A label that identifies whether the instance is an original target (``BLUE`` ) or a
      replacement target (``GREEN`` ).
    """


_ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlambdaFunctionInfoTypeDef = TypedDict(
    "_ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlambdaFunctionInfoTypeDef",
    {
        "functionName": str,
        "functionAlias": str,
        "currentVersion": str,
        "targetVersion": str,
        "targetVersionWeight": float,
    },
    total=False,
)


class ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlambdaFunctionInfoTypeDef(
    _ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlambdaFunctionInfoTypeDef
):
    """
    Type definition for `ClientGetDeploymentTargetResponsedeploymentTargetlambdaTarget` `lambdaFunctionInfo`

    A ``LambdaFunctionInfo`` object that describes a target Lambda function.

    - **functionName** *(string) --*

      The name of a Lambda function.

    - **functionAlias** *(string) --*

      The alias of a Lambda function. For more information, see `Introduction to AWS Lambda
      Aliases <https://docs.aws.amazon.com/lambda/latest/dg/aliases-intro.html>`__ .

    - **currentVersion** *(string) --*

      The version of a Lambda function that production traffic points to.

    - **targetVersion** *(string) --*

      The version of a Lambda function that production traffic points to after the Lambda
      function is deployed.

    - **targetVersionWeight** *(float) --*

      The percentage of production traffic that the target version of a Lambda function
      receives.
    """


_ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlifecycleEventsdiagnosticsTypeDef = TypedDict(
    "_ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlifecycleEventsdiagnosticsTypeDef",
    {"errorCode": str, "scriptName": str, "message": str, "logTail": str},
    total=False,
)


class ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlifecycleEventsdiagnosticsTypeDef(
    _ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlifecycleEventsdiagnosticsTypeDef
):
    """
    Type definition for `ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlifecycleEvents` `diagnostics`

    Diagnostic information about the deployment lifecycle event.

    - **errorCode** *(string) --*

      The associated error code:

      * Success: The specified script ran.

      * ScriptMissing: The specified script was not found in the specified location.

      * ScriptNotExecutable: The specified script is not a recognized executable file
      type.

      * ScriptTimedOut: The specified script did not finish running in the specified time
      period.

      * ScriptFailed: The specified script failed to run as expected.

      * UnknownError: The specified script did not run for an unknown reason.

    - **scriptName** *(string) --*

      The name of the script.

    - **message** *(string) --*

      The message associated with the error.

    - **logTail** *(string) --*

      The last portion of the diagnostic log.

      If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.
    """


_ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlifecycleEventsTypeDef = TypedDict(
    "_ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlifecycleEventsTypeDef",
    {
        "lifecycleEventName": str,
        "diagnostics": ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlifecycleEventsdiagnosticsTypeDef,
        "startTime": datetime,
        "endTime": datetime,
        "status": str,
    },
    total=False,
)


class ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlifecycleEventsTypeDef(
    _ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlifecycleEventsTypeDef
):
    """
    Type definition for `ClientGetDeploymentTargetResponsedeploymentTargetlambdaTarget` `lifecycleEvents`

    Information about a deployment lifecycle event.

    - **lifecycleEventName** *(string) --*

      The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
      AfterInstall, ApplicationStart, or ValidateService.

    - **diagnostics** *(dict) --*

      Diagnostic information about the deployment lifecycle event.

      - **errorCode** *(string) --*

        The associated error code:

        * Success: The specified script ran.

        * ScriptMissing: The specified script was not found in the specified location.

        * ScriptNotExecutable: The specified script is not a recognized executable file
        type.

        * ScriptTimedOut: The specified script did not finish running in the specified time
        period.

        * ScriptFailed: The specified script failed to run as expected.

        * UnknownError: The specified script did not run for an unknown reason.

      - **scriptName** *(string) --*

        The name of the script.

      - **message** *(string) --*

        The message associated with the error.

      - **logTail** *(string) --*

        The last portion of the diagnostic log.

        If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.

    - **startTime** *(datetime) --*

      A timestamp that indicates when the deployment lifecycle event started.

    - **endTime** *(datetime) --*

      A timestamp that indicates when the deployment lifecycle event ended.

    - **status** *(string) --*

      The deployment lifecycle event status:

      * Pending: The deployment lifecycle event is pending.

      * InProgress: The deployment lifecycle event is in progress.

      * Succeeded: The deployment lifecycle event ran successfully.

      * Failed: The deployment lifecycle event has failed.

      * Skipped: The deployment lifecycle event has been skipped.

      * Unknown: The deployment lifecycle event is unknown.
    """


_ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetTypeDef = TypedDict(
    "_ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
        "targetArn": str,
        "status": str,
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List[
            ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlifecycleEventsTypeDef
        ],
        "lambdaFunctionInfo": ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlambdaFunctionInfoTypeDef,
    },
    total=False,
)


class ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetTypeDef(
    _ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetTypeDef
):
    """
    Type definition for `ClientGetDeploymentTargetResponsedeploymentTarget` `lambdaTarget`

    Information about the target for a deployment that uses the AWS Lambda compute platform.

    - **deploymentId** *(string) --*

      The unique ID of a deployment.

    - **targetId** *(string) --*

      The unique ID of a deployment target that has a type of ``lambdaTarget`` .

    - **targetArn** *(string) --*

      The ARN of the target.

    - **status** *(string) --*

      The status an AWS Lambda deployment's target Lambda function.

    - **lastUpdatedAt** *(datetime) --*

      The date and time when the target Lambda function was updated by a deployment.

    - **lifecycleEvents** *(list) --*

      The lifecycle events of the deployment to this target Lambda function.

      - *(dict) --*

        Information about a deployment lifecycle event.

        - **lifecycleEventName** *(string) --*

          The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
          AfterInstall, ApplicationStart, or ValidateService.

        - **diagnostics** *(dict) --*

          Diagnostic information about the deployment lifecycle event.

          - **errorCode** *(string) --*

            The associated error code:

            * Success: The specified script ran.

            * ScriptMissing: The specified script was not found in the specified location.

            * ScriptNotExecutable: The specified script is not a recognized executable file
            type.

            * ScriptTimedOut: The specified script did not finish running in the specified time
            period.

            * ScriptFailed: The specified script failed to run as expected.

            * UnknownError: The specified script did not run for an unknown reason.

          - **scriptName** *(string) --*

            The name of the script.

          - **message** *(string) --*

            The message associated with the error.

          - **logTail** *(string) --*

            The last portion of the diagnostic log.

            If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.

        - **startTime** *(datetime) --*

          A timestamp that indicates when the deployment lifecycle event started.

        - **endTime** *(datetime) --*

          A timestamp that indicates when the deployment lifecycle event ended.

        - **status** *(string) --*

          The deployment lifecycle event status:

          * Pending: The deployment lifecycle event is pending.

          * InProgress: The deployment lifecycle event is in progress.

          * Succeeded: The deployment lifecycle event ran successfully.

          * Failed: The deployment lifecycle event has failed.

          * Skipped: The deployment lifecycle event has been skipped.

          * Unknown: The deployment lifecycle event is unknown.

    - **lambdaFunctionInfo** *(dict) --*

      A ``LambdaFunctionInfo`` object that describes a target Lambda function.

      - **functionName** *(string) --*

        The name of a Lambda function.

      - **functionAlias** *(string) --*

        The alias of a Lambda function. For more information, see `Introduction to AWS Lambda
        Aliases <https://docs.aws.amazon.com/lambda/latest/dg/aliases-intro.html>`__ .

      - **currentVersion** *(string) --*

        The version of a Lambda function that production traffic points to.

      - **targetVersion** *(string) --*

        The version of a Lambda function that production traffic points to after the Lambda
        function is deployed.

      - **targetVersionWeight** *(float) --*

        The percentage of production traffic that the target version of a Lambda function
        receives.
    """


_ClientGetDeploymentTargetResponsedeploymentTargetTypeDef = TypedDict(
    "_ClientGetDeploymentTargetResponsedeploymentTargetTypeDef",
    {
        "deploymentTargetType": str,
        "instanceTarget": ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetTypeDef,
        "lambdaTarget": ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetTypeDef,
        "ecsTarget": ClientGetDeploymentTargetResponsedeploymentTargetecsTargetTypeDef,
    },
    total=False,
)


class ClientGetDeploymentTargetResponsedeploymentTargetTypeDef(
    _ClientGetDeploymentTargetResponsedeploymentTargetTypeDef
):
    """
    Type definition for `ClientGetDeploymentTargetResponse` `deploymentTarget`

    A deployment target that contains information about a deployment such as its status, lifecyle
    events, and when it was last updated. It also contains metadata about the deployment target.
    The deployment target metadata depends on the deployment target's type (``instanceTarget`` ,
    ``lambdaTarget`` , or ``ecsTarget`` ).

    - **deploymentTargetType** *(string) --*

      The deployment type that is specific to the deployment's compute platform.

    - **instanceTarget** *(dict) --*

      Information about the target for a deployment that uses the EC2/On-premises compute
      platform.

      - **deploymentId** *(string) --*

        The unique ID of a deployment.

      - **targetId** *(string) --*

        The unique ID of a deployment target that has a type of ``instanceTarget`` .

      - **targetArn** *(string) --*

        The ARN of the target.

      - **status** *(string) --*

        The status an EC2/On-premises deployment's target instance.

      - **lastUpdatedAt** *(datetime) --*

        The date and time when the target instance was updated by a deployment.

      - **lifecycleEvents** *(list) --*

        The lifecycle events of the deployment to this target instance.

        - *(dict) --*

          Information about a deployment lifecycle event.

          - **lifecycleEventName** *(string) --*

            The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
            AfterInstall, ApplicationStart, or ValidateService.

          - **diagnostics** *(dict) --*

            Diagnostic information about the deployment lifecycle event.

            - **errorCode** *(string) --*

              The associated error code:

              * Success: The specified script ran.

              * ScriptMissing: The specified script was not found in the specified location.

              * ScriptNotExecutable: The specified script is not a recognized executable file
              type.

              * ScriptTimedOut: The specified script did not finish running in the specified time
              period.

              * ScriptFailed: The specified script failed to run as expected.

              * UnknownError: The specified script did not run for an unknown reason.

            - **scriptName** *(string) --*

              The name of the script.

            - **message** *(string) --*

              The message associated with the error.

            - **logTail** *(string) --*

              The last portion of the diagnostic log.

              If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.

          - **startTime** *(datetime) --*

            A timestamp that indicates when the deployment lifecycle event started.

          - **endTime** *(datetime) --*

            A timestamp that indicates when the deployment lifecycle event ended.

          - **status** *(string) --*

            The deployment lifecycle event status:

            * Pending: The deployment lifecycle event is pending.

            * InProgress: The deployment lifecycle event is in progress.

            * Succeeded: The deployment lifecycle event ran successfully.

            * Failed: The deployment lifecycle event has failed.

            * Skipped: The deployment lifecycle event has been skipped.

            * Unknown: The deployment lifecycle event is unknown.

      - **instanceLabel** *(string) --*

        A label that identifies whether the instance is an original target (``BLUE`` ) or a
        replacement target (``GREEN`` ).

    - **lambdaTarget** *(dict) --*

      Information about the target for a deployment that uses the AWS Lambda compute platform.

      - **deploymentId** *(string) --*

        The unique ID of a deployment.

      - **targetId** *(string) --*

        The unique ID of a deployment target that has a type of ``lambdaTarget`` .

      - **targetArn** *(string) --*

        The ARN of the target.

      - **status** *(string) --*

        The status an AWS Lambda deployment's target Lambda function.

      - **lastUpdatedAt** *(datetime) --*

        The date and time when the target Lambda function was updated by a deployment.

      - **lifecycleEvents** *(list) --*

        The lifecycle events of the deployment to this target Lambda function.

        - *(dict) --*

          Information about a deployment lifecycle event.

          - **lifecycleEventName** *(string) --*

            The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
            AfterInstall, ApplicationStart, or ValidateService.

          - **diagnostics** *(dict) --*

            Diagnostic information about the deployment lifecycle event.

            - **errorCode** *(string) --*

              The associated error code:

              * Success: The specified script ran.

              * ScriptMissing: The specified script was not found in the specified location.

              * ScriptNotExecutable: The specified script is not a recognized executable file
              type.

              * ScriptTimedOut: The specified script did not finish running in the specified time
              period.

              * ScriptFailed: The specified script failed to run as expected.

              * UnknownError: The specified script did not run for an unknown reason.

            - **scriptName** *(string) --*

              The name of the script.

            - **message** *(string) --*

              The message associated with the error.

            - **logTail** *(string) --*

              The last portion of the diagnostic log.

              If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.

          - **startTime** *(datetime) --*

            A timestamp that indicates when the deployment lifecycle event started.

          - **endTime** *(datetime) --*

            A timestamp that indicates when the deployment lifecycle event ended.

          - **status** *(string) --*

            The deployment lifecycle event status:

            * Pending: The deployment lifecycle event is pending.

            * InProgress: The deployment lifecycle event is in progress.

            * Succeeded: The deployment lifecycle event ran successfully.

            * Failed: The deployment lifecycle event has failed.

            * Skipped: The deployment lifecycle event has been skipped.

            * Unknown: The deployment lifecycle event is unknown.

      - **lambdaFunctionInfo** *(dict) --*

        A ``LambdaFunctionInfo`` object that describes a target Lambda function.

        - **functionName** *(string) --*

          The name of a Lambda function.

        - **functionAlias** *(string) --*

          The alias of a Lambda function. For more information, see `Introduction to AWS Lambda
          Aliases <https://docs.aws.amazon.com/lambda/latest/dg/aliases-intro.html>`__ .

        - **currentVersion** *(string) --*

          The version of a Lambda function that production traffic points to.

        - **targetVersion** *(string) --*

          The version of a Lambda function that production traffic points to after the Lambda
          function is deployed.

        - **targetVersionWeight** *(float) --*

          The percentage of production traffic that the target version of a Lambda function
          receives.

    - **ecsTarget** *(dict) --*

      Information about the target for a deployment that uses the Amazon ECS compute platform.

      - **deploymentId** *(string) --*

        The unique ID of a deployment.

      - **targetId** *(string) --*

        The unique ID of a deployment target that has a type of ``ecsTarget`` .

      - **targetArn** *(string) --*

        The ARN of the target.

      - **lastUpdatedAt** *(datetime) --*

        The date and time when the target Amazon ECS application was updated by a deployment.

      - **lifecycleEvents** *(list) --*

        The lifecycle events of the deployment to this target Amazon ECS application.

        - *(dict) --*

          Information about a deployment lifecycle event.

          - **lifecycleEventName** *(string) --*

            The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
            AfterInstall, ApplicationStart, or ValidateService.

          - **diagnostics** *(dict) --*

            Diagnostic information about the deployment lifecycle event.

            - **errorCode** *(string) --*

              The associated error code:

              * Success: The specified script ran.

              * ScriptMissing: The specified script was not found in the specified location.

              * ScriptNotExecutable: The specified script is not a recognized executable file
              type.

              * ScriptTimedOut: The specified script did not finish running in the specified time
              period.

              * ScriptFailed: The specified script failed to run as expected.

              * UnknownError: The specified script did not run for an unknown reason.

            - **scriptName** *(string) --*

              The name of the script.

            - **message** *(string) --*

              The message associated with the error.

            - **logTail** *(string) --*

              The last portion of the diagnostic log.

              If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.

          - **startTime** *(datetime) --*

            A timestamp that indicates when the deployment lifecycle event started.

          - **endTime** *(datetime) --*

            A timestamp that indicates when the deployment lifecycle event ended.

          - **status** *(string) --*

            The deployment lifecycle event status:

            * Pending: The deployment lifecycle event is pending.

            * InProgress: The deployment lifecycle event is in progress.

            * Succeeded: The deployment lifecycle event ran successfully.

            * Failed: The deployment lifecycle event has failed.

            * Skipped: The deployment lifecycle event has been skipped.

            * Unknown: The deployment lifecycle event is unknown.

      - **status** *(string) --*

        The status an Amazon ECS deployment's target ECS application.

      - **taskSetsInfo** *(list) --*

        The ``ECSTaskSet`` objects associated with the ECS target.

        - *(dict) --*

          Information about a set of Amazon ECS tasks in an AWS CodeDeploy deployment. An Amazon
          ECS task set includes details such as the desired number of tasks, how many tasks are
          running, and whether the task set serves production traffic. An AWS CodeDeploy
          application that uses the Amazon ECS compute platform deploys a containerized
          application in an Amazon ECS service as a task set.

          - **identifer** *(string) --*

            A unique ID of an ``ECSTaskSet`` .

          - **desiredCount** *(integer) --*

            The number of tasks in a task set. During a deployment that uses the Amazon ECS
            compute type, CodeDeploy instructs Amazon ECS to create a new task set and uses this
            value to determine how many tasks to create. After the updated task set is created,
            CodeDeploy shifts traffic to the new task set.

          - **pendingCount** *(integer) --*

            The number of tasks in the task set that are in the ``PENDING`` status during an
            Amazon ECS deployment. A task in the ``PENDING`` state is preparing to enter the
            ``RUNNING`` state. A task set enters the ``PENDING`` status when it launches for the
            first time, or when it is restarted after being in the ``STOPPED`` state.

          - **runningCount** *(integer) --*

            The number of tasks in the task set that are in the ``RUNNING`` status during an
            Amazon ECS deployment. A task in the ``RUNNING`` state is running and ready for use.

          - **status** *(string) --*

            The status of the task set. There are three valid task set statuses:

            * ``PRIMARY`` : Indicates the task set is serving production traffic.

            * ``ACTIVE`` : Indicates the task set is not serving production traffic.

            * ``DRAINING`` : Indicates the tasks in the task set are being stopped and their
            corresponding targets are being deregistered from their target group.

          - **trafficWeight** *(float) --*

            The percentage of traffic served by this task set.

          - **targetGroup** *(dict) --*

            The target group associated with the task set. The target group is used by AWS
            CodeDeploy to manage traffic to a task set.

            - **name** *(string) --*

              For blue/green deployments, the name of the target group that instances in the
              original environment are deregistered from, and instances in the replacement
              environment are registered with. For in-place deployments, the name of the target
              group that instances are deregistered from, so they are not serving traffic during
              a deployment, and then re-registered with after the deployment is complete.

          - **taskSetLabel** *(string) --*

            A label that identifies whether the ECS task set is an original target (``BLUE`` ) or
            a replacement target (``GREEN`` ).
    """


_ClientGetDeploymentTargetResponseTypeDef = TypedDict(
    "_ClientGetDeploymentTargetResponseTypeDef",
    {"deploymentTarget": ClientGetDeploymentTargetResponsedeploymentTargetTypeDef},
    total=False,
)


class ClientGetDeploymentTargetResponseTypeDef(
    _ClientGetDeploymentTargetResponseTypeDef
):
    """
    Type definition for `ClientGetDeploymentTarget` `Response`

    - **deploymentTarget** *(dict) --*

      A deployment target that contains information about a deployment such as its status, lifecyle
      events, and when it was last updated. It also contains metadata about the deployment target.
      The deployment target metadata depends on the deployment target's type (``instanceTarget`` ,
      ``lambdaTarget`` , or ``ecsTarget`` ).

      - **deploymentTargetType** *(string) --*

        The deployment type that is specific to the deployment's compute platform.

      - **instanceTarget** *(dict) --*

        Information about the target for a deployment that uses the EC2/On-premises compute
        platform.

        - **deploymentId** *(string) --*

          The unique ID of a deployment.

        - **targetId** *(string) --*

          The unique ID of a deployment target that has a type of ``instanceTarget`` .

        - **targetArn** *(string) --*

          The ARN of the target.

        - **status** *(string) --*

          The status an EC2/On-premises deployment's target instance.

        - **lastUpdatedAt** *(datetime) --*

          The date and time when the target instance was updated by a deployment.

        - **lifecycleEvents** *(list) --*

          The lifecycle events of the deployment to this target instance.

          - *(dict) --*

            Information about a deployment lifecycle event.

            - **lifecycleEventName** *(string) --*

              The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
              AfterInstall, ApplicationStart, or ValidateService.

            - **diagnostics** *(dict) --*

              Diagnostic information about the deployment lifecycle event.

              - **errorCode** *(string) --*

                The associated error code:

                * Success: The specified script ran.

                * ScriptMissing: The specified script was not found in the specified location.

                * ScriptNotExecutable: The specified script is not a recognized executable file
                type.

                * ScriptTimedOut: The specified script did not finish running in the specified time
                period.

                * ScriptFailed: The specified script failed to run as expected.

                * UnknownError: The specified script did not run for an unknown reason.

              - **scriptName** *(string) --*

                The name of the script.

              - **message** *(string) --*

                The message associated with the error.

              - **logTail** *(string) --*

                The last portion of the diagnostic log.

                If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.

            - **startTime** *(datetime) --*

              A timestamp that indicates when the deployment lifecycle event started.

            - **endTime** *(datetime) --*

              A timestamp that indicates when the deployment lifecycle event ended.

            - **status** *(string) --*

              The deployment lifecycle event status:

              * Pending: The deployment lifecycle event is pending.

              * InProgress: The deployment lifecycle event is in progress.

              * Succeeded: The deployment lifecycle event ran successfully.

              * Failed: The deployment lifecycle event has failed.

              * Skipped: The deployment lifecycle event has been skipped.

              * Unknown: The deployment lifecycle event is unknown.

        - **instanceLabel** *(string) --*

          A label that identifies whether the instance is an original target (``BLUE`` ) or a
          replacement target (``GREEN`` ).

      - **lambdaTarget** *(dict) --*

        Information about the target for a deployment that uses the AWS Lambda compute platform.

        - **deploymentId** *(string) --*

          The unique ID of a deployment.

        - **targetId** *(string) --*

          The unique ID of a deployment target that has a type of ``lambdaTarget`` .

        - **targetArn** *(string) --*

          The ARN of the target.

        - **status** *(string) --*

          The status an AWS Lambda deployment's target Lambda function.

        - **lastUpdatedAt** *(datetime) --*

          The date and time when the target Lambda function was updated by a deployment.

        - **lifecycleEvents** *(list) --*

          The lifecycle events of the deployment to this target Lambda function.

          - *(dict) --*

            Information about a deployment lifecycle event.

            - **lifecycleEventName** *(string) --*

              The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
              AfterInstall, ApplicationStart, or ValidateService.

            - **diagnostics** *(dict) --*

              Diagnostic information about the deployment lifecycle event.

              - **errorCode** *(string) --*

                The associated error code:

                * Success: The specified script ran.

                * ScriptMissing: The specified script was not found in the specified location.

                * ScriptNotExecutable: The specified script is not a recognized executable file
                type.

                * ScriptTimedOut: The specified script did not finish running in the specified time
                period.

                * ScriptFailed: The specified script failed to run as expected.

                * UnknownError: The specified script did not run for an unknown reason.

              - **scriptName** *(string) --*

                The name of the script.

              - **message** *(string) --*

                The message associated with the error.

              - **logTail** *(string) --*

                The last portion of the diagnostic log.

                If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.

            - **startTime** *(datetime) --*

              A timestamp that indicates when the deployment lifecycle event started.

            - **endTime** *(datetime) --*

              A timestamp that indicates when the deployment lifecycle event ended.

            - **status** *(string) --*

              The deployment lifecycle event status:

              * Pending: The deployment lifecycle event is pending.

              * InProgress: The deployment lifecycle event is in progress.

              * Succeeded: The deployment lifecycle event ran successfully.

              * Failed: The deployment lifecycle event has failed.

              * Skipped: The deployment lifecycle event has been skipped.

              * Unknown: The deployment lifecycle event is unknown.

        - **lambdaFunctionInfo** *(dict) --*

          A ``LambdaFunctionInfo`` object that describes a target Lambda function.

          - **functionName** *(string) --*

            The name of a Lambda function.

          - **functionAlias** *(string) --*

            The alias of a Lambda function. For more information, see `Introduction to AWS Lambda
            Aliases <https://docs.aws.amazon.com/lambda/latest/dg/aliases-intro.html>`__ .

          - **currentVersion** *(string) --*

            The version of a Lambda function that production traffic points to.

          - **targetVersion** *(string) --*

            The version of a Lambda function that production traffic points to after the Lambda
            function is deployed.

          - **targetVersionWeight** *(float) --*

            The percentage of production traffic that the target version of a Lambda function
            receives.

      - **ecsTarget** *(dict) --*

        Information about the target for a deployment that uses the Amazon ECS compute platform.

        - **deploymentId** *(string) --*

          The unique ID of a deployment.

        - **targetId** *(string) --*

          The unique ID of a deployment target that has a type of ``ecsTarget`` .

        - **targetArn** *(string) --*

          The ARN of the target.

        - **lastUpdatedAt** *(datetime) --*

          The date and time when the target Amazon ECS application was updated by a deployment.

        - **lifecycleEvents** *(list) --*

          The lifecycle events of the deployment to this target Amazon ECS application.

          - *(dict) --*

            Information about a deployment lifecycle event.

            - **lifecycleEventName** *(string) --*

              The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
              AfterInstall, ApplicationStart, or ValidateService.

            - **diagnostics** *(dict) --*

              Diagnostic information about the deployment lifecycle event.

              - **errorCode** *(string) --*

                The associated error code:

                * Success: The specified script ran.

                * ScriptMissing: The specified script was not found in the specified location.

                * ScriptNotExecutable: The specified script is not a recognized executable file
                type.

                * ScriptTimedOut: The specified script did not finish running in the specified time
                period.

                * ScriptFailed: The specified script failed to run as expected.

                * UnknownError: The specified script did not run for an unknown reason.

              - **scriptName** *(string) --*

                The name of the script.

              - **message** *(string) --*

                The message associated with the error.

              - **logTail** *(string) --*

                The last portion of the diagnostic log.

                If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.

            - **startTime** *(datetime) --*

              A timestamp that indicates when the deployment lifecycle event started.

            - **endTime** *(datetime) --*

              A timestamp that indicates when the deployment lifecycle event ended.

            - **status** *(string) --*

              The deployment lifecycle event status:

              * Pending: The deployment lifecycle event is pending.

              * InProgress: The deployment lifecycle event is in progress.

              * Succeeded: The deployment lifecycle event ran successfully.

              * Failed: The deployment lifecycle event has failed.

              * Skipped: The deployment lifecycle event has been skipped.

              * Unknown: The deployment lifecycle event is unknown.

        - **status** *(string) --*

          The status an Amazon ECS deployment's target ECS application.

        - **taskSetsInfo** *(list) --*

          The ``ECSTaskSet`` objects associated with the ECS target.

          - *(dict) --*

            Information about a set of Amazon ECS tasks in an AWS CodeDeploy deployment. An Amazon
            ECS task set includes details such as the desired number of tasks, how many tasks are
            running, and whether the task set serves production traffic. An AWS CodeDeploy
            application that uses the Amazon ECS compute platform deploys a containerized
            application in an Amazon ECS service as a task set.

            - **identifer** *(string) --*

              A unique ID of an ``ECSTaskSet`` .

            - **desiredCount** *(integer) --*

              The number of tasks in a task set. During a deployment that uses the Amazon ECS
              compute type, CodeDeploy instructs Amazon ECS to create a new task set and uses this
              value to determine how many tasks to create. After the updated task set is created,
              CodeDeploy shifts traffic to the new task set.

            - **pendingCount** *(integer) --*

              The number of tasks in the task set that are in the ``PENDING`` status during an
              Amazon ECS deployment. A task in the ``PENDING`` state is preparing to enter the
              ``RUNNING`` state. A task set enters the ``PENDING`` status when it launches for the
              first time, or when it is restarted after being in the ``STOPPED`` state.

            - **runningCount** *(integer) --*

              The number of tasks in the task set that are in the ``RUNNING`` status during an
              Amazon ECS deployment. A task in the ``RUNNING`` state is running and ready for use.

            - **status** *(string) --*

              The status of the task set. There are three valid task set statuses:

              * ``PRIMARY`` : Indicates the task set is serving production traffic.

              * ``ACTIVE`` : Indicates the task set is not serving production traffic.

              * ``DRAINING`` : Indicates the tasks in the task set are being stopped and their
              corresponding targets are being deregistered from their target group.

            - **trafficWeight** *(float) --*

              The percentage of traffic served by this task set.

            - **targetGroup** *(dict) --*

              The target group associated with the task set. The target group is used by AWS
              CodeDeploy to manage traffic to a task set.

              - **name** *(string) --*

                For blue/green deployments, the name of the target group that instances in the
                original environment are deregistered from, and instances in the replacement
                environment are registered with. For in-place deployments, the name of the target
                group that instances are deregistered from, so they are not serving traffic during
                a deployment, and then re-registered with after the deployment is complete.

            - **taskSetLabel** *(string) --*

              A label that identifies whether the ECS task set is an original target (``BLUE`` ) or
              a replacement target (``GREEN`` ).
    """


_ClientGetOnPremisesInstanceResponseinstanceInfotagsTypeDef = TypedDict(
    "_ClientGetOnPremisesInstanceResponseinstanceInfotagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetOnPremisesInstanceResponseinstanceInfotagsTypeDef(
    _ClientGetOnPremisesInstanceResponseinstanceInfotagsTypeDef
):
    """
    Type definition for `ClientGetOnPremisesInstanceResponseinstanceInfo` `tags`

    Information about a tag.

    - **Key** *(string) --*

      The tag's key.

    - **Value** *(string) --*

      The tag's value.
    """


_ClientGetOnPremisesInstanceResponseinstanceInfoTypeDef = TypedDict(
    "_ClientGetOnPremisesInstanceResponseinstanceInfoTypeDef",
    {
        "instanceName": str,
        "iamSessionArn": str,
        "iamUserArn": str,
        "instanceArn": str,
        "registerTime": datetime,
        "deregisterTime": datetime,
        "tags": List[ClientGetOnPremisesInstanceResponseinstanceInfotagsTypeDef],
    },
    total=False,
)


class ClientGetOnPremisesInstanceResponseinstanceInfoTypeDef(
    _ClientGetOnPremisesInstanceResponseinstanceInfoTypeDef
):
    """
    Type definition for `ClientGetOnPremisesInstanceResponse` `instanceInfo`

    Information about the on-premises instance.

    - **instanceName** *(string) --*

      The name of the on-premises instance.

    - **iamSessionArn** *(string) --*

      The ARN of the IAM session associated with the on-premises instance.

    - **iamUserArn** *(string) --*

      The IAM user ARN associated with the on-premises instance.

    - **instanceArn** *(string) --*

      The ARN of the on-premises instance.

    - **registerTime** *(datetime) --*

      The time at which the on-premises instance was registered.

    - **deregisterTime** *(datetime) --*

      If the on-premises instance was deregistered, the time at which the on-premises instance
      was deregistered.

    - **tags** *(list) --*

      The tags currently associated with the on-premises instance.

      - *(dict) --*

        Information about a tag.

        - **Key** *(string) --*

          The tag's key.

        - **Value** *(string) --*

          The tag's value.
    """


_ClientGetOnPremisesInstanceResponseTypeDef = TypedDict(
    "_ClientGetOnPremisesInstanceResponseTypeDef",
    {"instanceInfo": ClientGetOnPremisesInstanceResponseinstanceInfoTypeDef},
    total=False,
)


class ClientGetOnPremisesInstanceResponseTypeDef(
    _ClientGetOnPremisesInstanceResponseTypeDef
):
    """
    Type definition for `ClientGetOnPremisesInstance` `Response`

    Represents the output of a GetOnPremisesInstance operation.

    - **instanceInfo** *(dict) --*

      Information about the on-premises instance.

      - **instanceName** *(string) --*

        The name of the on-premises instance.

      - **iamSessionArn** *(string) --*

        The ARN of the IAM session associated with the on-premises instance.

      - **iamUserArn** *(string) --*

        The IAM user ARN associated with the on-premises instance.

      - **instanceArn** *(string) --*

        The ARN of the on-premises instance.

      - **registerTime** *(datetime) --*

        The time at which the on-premises instance was registered.

      - **deregisterTime** *(datetime) --*

        If the on-premises instance was deregistered, the time at which the on-premises instance
        was deregistered.

      - **tags** *(list) --*

        The tags currently associated with the on-premises instance.

        - *(dict) --*

          Information about a tag.

          - **Key** *(string) --*

            The tag's key.

          - **Value** *(string) --*

            The tag's value.
    """


_ClientListApplicationRevisionsResponserevisionsappSpecContentTypeDef = TypedDict(
    "_ClientListApplicationRevisionsResponserevisionsappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientListApplicationRevisionsResponserevisionsappSpecContentTypeDef(
    _ClientListApplicationRevisionsResponserevisionsappSpecContentTypeDef
):
    """
    Type definition for `ClientListApplicationRevisionsResponserevisions` `appSpecContent`

    The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is
    formatted as JSON or YAML and stored as a RawString.

    - **content** *(string) --*

      The YAML-formatted or JSON-formatted revision string.

      For an AWS Lambda deployment, the content includes a Lambda function name, the alias
      for its original version, and the alias for its replacement version. The deployment
      shifts traffic from the original version of the Lambda function to the replacement
      version.

      For an Amazon ECS deployment, the content includes the task name, information about the
      load balancer that serves traffic to the container, and more.

      For both types of deployments, the content can specify Lambda functions that run at
      specified hooks, such as ``BeforeInstall`` , during a deployment.

    - **sha256** *(string) --*

      The SHA256 hash value of the revision content.
    """


_ClientListApplicationRevisionsResponserevisionsgitHubLocationTypeDef = TypedDict(
    "_ClientListApplicationRevisionsResponserevisionsgitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)


class ClientListApplicationRevisionsResponserevisionsgitHubLocationTypeDef(
    _ClientListApplicationRevisionsResponserevisionsgitHubLocationTypeDef
):
    """
    Type definition for `ClientListApplicationRevisionsResponserevisions` `gitHubLocation`

    Information about the location of application artifacts stored in GitHub.

    - **repository** *(string) --*

      The GitHub account and repository pair that stores a reference to the commit that
      represents the bundled artifacts for the application revision.

      Specified as account/repository.

    - **commitId** *(string) --*

      The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
      application revision.
    """


_ClientListApplicationRevisionsResponserevisionss3LocationTypeDef = TypedDict(
    "_ClientListApplicationRevisionsResponserevisionss3LocationTypeDef",
    {"bucket": str, "key": str, "bundleType": str, "version": str, "eTag": str},
    total=False,
)


class ClientListApplicationRevisionsResponserevisionss3LocationTypeDef(
    _ClientListApplicationRevisionsResponserevisionss3LocationTypeDef
):
    """
    Type definition for `ClientListApplicationRevisionsResponserevisions` `s3Location`

    Information about the location of a revision stored in Amazon S3.

    - **bucket** *(string) --*

      The name of the Amazon S3 bucket where the application revision is stored.

    - **key** *(string) --*

      The name of the Amazon S3 object that represents the bundled artifacts for the
      application revision.

    - **bundleType** *(string) --*

      The file type of the application revision. Must be one of the following:

      * tar: A tar archive file.

      * tgz: A compressed tar archive file.

      * zip: A zip archive file.

    - **version** *(string) --*

      A specific version of the Amazon S3 object that represents the bundled artifacts for
      the application revision.

      If the version is not specified, the system uses the most recent version by default.

    - **eTag** *(string) --*

      The ETag of the Amazon S3 object that represents the bundled artifacts for the
      application revision.

      If the ETag is not specified as an input parameter, ETag validation of the object is
      skipped.
    """


_ClientListApplicationRevisionsResponserevisionsstringTypeDef = TypedDict(
    "_ClientListApplicationRevisionsResponserevisionsstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientListApplicationRevisionsResponserevisionsstringTypeDef(
    _ClientListApplicationRevisionsResponserevisionsstringTypeDef
):
    """
    Type definition for `ClientListApplicationRevisionsResponserevisions` `string`

    Information about the location of an AWS Lambda deployment revision stored as a RawString.

    - **content** *(string) --*

      The YAML-formatted or JSON-formatted revision string. It includes information about
      which Lambda function to update and optional Lambda functions that validate deployment
      lifecycle events.

    - **sha256** *(string) --*

      The SHA256 hash value of the revision content.
    """


_ClientListApplicationRevisionsResponserevisionsTypeDef = TypedDict(
    "_ClientListApplicationRevisionsResponserevisionsTypeDef",
    {
        "revisionType": str,
        "s3Location": ClientListApplicationRevisionsResponserevisionss3LocationTypeDef,
        "gitHubLocation": ClientListApplicationRevisionsResponserevisionsgitHubLocationTypeDef,
        "string": ClientListApplicationRevisionsResponserevisionsstringTypeDef,
        "appSpecContent": ClientListApplicationRevisionsResponserevisionsappSpecContentTypeDef,
    },
    total=False,
)


class ClientListApplicationRevisionsResponserevisionsTypeDef(
    _ClientListApplicationRevisionsResponserevisionsTypeDef
):
    """
    Type definition for `ClientListApplicationRevisionsResponse` `revisions`

    Information about the location of an application revision.

    - **revisionType** *(string) --*

      The type of application revision:

      * S3: An application revision stored in Amazon S3.

      * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

      * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

    - **s3Location** *(dict) --*

      Information about the location of a revision stored in Amazon S3.

      - **bucket** *(string) --*

        The name of the Amazon S3 bucket where the application revision is stored.

      - **key** *(string) --*

        The name of the Amazon S3 object that represents the bundled artifacts for the
        application revision.

      - **bundleType** *(string) --*

        The file type of the application revision. Must be one of the following:

        * tar: A tar archive file.

        * tgz: A compressed tar archive file.

        * zip: A zip archive file.

      - **version** *(string) --*

        A specific version of the Amazon S3 object that represents the bundled artifacts for
        the application revision.

        If the version is not specified, the system uses the most recent version by default.

      - **eTag** *(string) --*

        The ETag of the Amazon S3 object that represents the bundled artifacts for the
        application revision.

        If the ETag is not specified as an input parameter, ETag validation of the object is
        skipped.

    - **gitHubLocation** *(dict) --*

      Information about the location of application artifacts stored in GitHub.

      - **repository** *(string) --*

        The GitHub account and repository pair that stores a reference to the commit that
        represents the bundled artifacts for the application revision.

        Specified as account/repository.

      - **commitId** *(string) --*

        The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
        application revision.

    - **string** *(dict) --*

      Information about the location of an AWS Lambda deployment revision stored as a RawString.

      - **content** *(string) --*

        The YAML-formatted or JSON-formatted revision string. It includes information about
        which Lambda function to update and optional Lambda functions that validate deployment
        lifecycle events.

      - **sha256** *(string) --*

        The SHA256 hash value of the revision content.

    - **appSpecContent** *(dict) --*

      The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is
      formatted as JSON or YAML and stored as a RawString.

      - **content** *(string) --*

        The YAML-formatted or JSON-formatted revision string.

        For an AWS Lambda deployment, the content includes a Lambda function name, the alias
        for its original version, and the alias for its replacement version. The deployment
        shifts traffic from the original version of the Lambda function to the replacement
        version.

        For an Amazon ECS deployment, the content includes the task name, information about the
        load balancer that serves traffic to the container, and more.

        For both types of deployments, the content can specify Lambda functions that run at
        specified hooks, such as ``BeforeInstall`` , during a deployment.

      - **sha256** *(string) --*

        The SHA256 hash value of the revision content.
    """


_ClientListApplicationRevisionsResponseTypeDef = TypedDict(
    "_ClientListApplicationRevisionsResponseTypeDef",
    {
        "revisions": List[ClientListApplicationRevisionsResponserevisionsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListApplicationRevisionsResponseTypeDef(
    _ClientListApplicationRevisionsResponseTypeDef
):
    """
    Type definition for `ClientListApplicationRevisions` `Response`

    Represents the output of a ListApplicationRevisions operation.

    - **revisions** *(list) --*

      A list of locations that contain the matching revisions.

      - *(dict) --*

        Information about the location of an application revision.

        - **revisionType** *(string) --*

          The type of application revision:

          * S3: An application revision stored in Amazon S3.

          * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

          * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

        - **s3Location** *(dict) --*

          Information about the location of a revision stored in Amazon S3.

          - **bucket** *(string) --*

            The name of the Amazon S3 bucket where the application revision is stored.

          - **key** *(string) --*

            The name of the Amazon S3 object that represents the bundled artifacts for the
            application revision.

          - **bundleType** *(string) --*

            The file type of the application revision. Must be one of the following:

            * tar: A tar archive file.

            * tgz: A compressed tar archive file.

            * zip: A zip archive file.

          - **version** *(string) --*

            A specific version of the Amazon S3 object that represents the bundled artifacts for
            the application revision.

            If the version is not specified, the system uses the most recent version by default.

          - **eTag** *(string) --*

            The ETag of the Amazon S3 object that represents the bundled artifacts for the
            application revision.

            If the ETag is not specified as an input parameter, ETag validation of the object is
            skipped.

        - **gitHubLocation** *(dict) --*

          Information about the location of application artifacts stored in GitHub.

          - **repository** *(string) --*

            The GitHub account and repository pair that stores a reference to the commit that
            represents the bundled artifacts for the application revision.

            Specified as account/repository.

          - **commitId** *(string) --*

            The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
            application revision.

        - **string** *(dict) --*

          Information about the location of an AWS Lambda deployment revision stored as a RawString.

          - **content** *(string) --*

            The YAML-formatted or JSON-formatted revision string. It includes information about
            which Lambda function to update and optional Lambda functions that validate deployment
            lifecycle events.

          - **sha256** *(string) --*

            The SHA256 hash value of the revision content.

        - **appSpecContent** *(dict) --*

          The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is
          formatted as JSON or YAML and stored as a RawString.

          - **content** *(string) --*

            The YAML-formatted or JSON-formatted revision string.

            For an AWS Lambda deployment, the content includes a Lambda function name, the alias
            for its original version, and the alias for its replacement version. The deployment
            shifts traffic from the original version of the Lambda function to the replacement
            version.

            For an Amazon ECS deployment, the content includes the task name, information about the
            load balancer that serves traffic to the container, and more.

            For both types of deployments, the content can specify Lambda functions that run at
            specified hooks, such as ``BeforeInstall`` , during a deployment.

          - **sha256** *(string) --*

            The SHA256 hash value of the revision content.

    - **nextToken** *(string) --*

      If a large amount of information is returned, an identifier is also returned. It can be used
      in a subsequent list application revisions call to return the next set of application
      revisions in the list.
    """


_ClientListApplicationsResponseTypeDef = TypedDict(
    "_ClientListApplicationsResponseTypeDef",
    {"applications": List[str], "nextToken": str},
    total=False,
)


class ClientListApplicationsResponseTypeDef(_ClientListApplicationsResponseTypeDef):
    """
    Type definition for `ClientListApplications` `Response`

    Represents the output of a ListApplications operation.

    - **applications** *(list) --*

      A list of application names.

      - *(string) --*

    - **nextToken** *(string) --*

      If a large amount of information is returned, an identifier is also returned. It can be used
      in a subsequent list applications call to return the next set of applications in the list.
    """


_ClientListDeploymentConfigsResponseTypeDef = TypedDict(
    "_ClientListDeploymentConfigsResponseTypeDef",
    {"deploymentConfigsList": List[str], "nextToken": str},
    total=False,
)


class ClientListDeploymentConfigsResponseTypeDef(
    _ClientListDeploymentConfigsResponseTypeDef
):
    """
    Type definition for `ClientListDeploymentConfigs` `Response`

    Represents the output of a ListDeploymentConfigs operation.

    - **deploymentConfigsList** *(list) --*

      A list of deployment configurations, including built-in configurations such as
      CodeDeployDefault.OneAtATime.

      - *(string) --*

    - **nextToken** *(string) --*

      If a large amount of information is returned, an identifier is also returned. It can be used
      in a subsequent list deployment configurations call to return the next set of deployment
      configurations in the list.
    """


_ClientListDeploymentGroupsResponseTypeDef = TypedDict(
    "_ClientListDeploymentGroupsResponseTypeDef",
    {"applicationName": str, "deploymentGroups": List[str], "nextToken": str},
    total=False,
)


class ClientListDeploymentGroupsResponseTypeDef(
    _ClientListDeploymentGroupsResponseTypeDef
):
    """
    Type definition for `ClientListDeploymentGroups` `Response`

    Represents the output of a ListDeploymentGroups operation.

    - **applicationName** *(string) --*

      The application name.

    - **deploymentGroups** *(list) --*

      A list of deployment group names.

      - *(string) --*

    - **nextToken** *(string) --*

      If a large amount of information is returned, an identifier is also returned. It can be used
      in a subsequent list deployment groups call to return the next set of deployment groups in
      the list.
    """


_ClientListDeploymentInstancesResponseTypeDef = TypedDict(
    "_ClientListDeploymentInstancesResponseTypeDef",
    {"instancesList": List[str], "nextToken": str},
    total=False,
)


class ClientListDeploymentInstancesResponseTypeDef(
    _ClientListDeploymentInstancesResponseTypeDef
):
    """
    Type definition for `ClientListDeploymentInstances` `Response`

    Represents the output of a ListDeploymentInstances operation.

    - **instancesList** *(list) --*

      A list of instance IDs.

      - *(string) --*

    - **nextToken** *(string) --*

      If a large amount of information is returned, an identifier is also returned. It can be used
      in a subsequent list deployment instances call to return the next set of deployment instances
      in the list.
    """


_ClientListDeploymentTargetsResponseTypeDef = TypedDict(
    "_ClientListDeploymentTargetsResponseTypeDef",
    {"targetIds": List[str], "nextToken": str},
    total=False,
)


class ClientListDeploymentTargetsResponseTypeDef(
    _ClientListDeploymentTargetsResponseTypeDef
):
    """
    Type definition for `ClientListDeploymentTargets` `Response`

    - **targetIds** *(list) --*

      The unique IDs of deployment targets.

      - *(string) --*

    - **nextToken** *(string) --*

      If a large amount of information is returned, a token identifier is also returned. It can be
      used in a subsequent ``ListDeploymentTargets`` call to return the next set of deployment
      targets in the list.
    """


_ClientListDeploymentsResponseTypeDef = TypedDict(
    "_ClientListDeploymentsResponseTypeDef",
    {"deployments": List[str], "nextToken": str},
    total=False,
)


class ClientListDeploymentsResponseTypeDef(_ClientListDeploymentsResponseTypeDef):
    """
    Type definition for `ClientListDeployments` `Response`

    Represents the output of a ListDeployments operation.

    - **deployments** *(list) --*

      A list of deployment IDs.

      - *(string) --*

    - **nextToken** *(string) --*

      If a large amount of information is returned, an identifier is also returned. It can be used
      in a subsequent list deployments call to return the next set of deployments in the list.
    """


_ClientListDeploymentscreateTimeRangeTypeDef = TypedDict(
    "_ClientListDeploymentscreateTimeRangeTypeDef",
    {"start": datetime, "end": datetime},
    total=False,
)


class ClientListDeploymentscreateTimeRangeTypeDef(
    _ClientListDeploymentscreateTimeRangeTypeDef
):
    """
    Type definition for `ClientListDeployments` `createTimeRange`

    A time range (start and end) for returning a subset of the list of deployments.

    - **start** *(datetime) --*

      The start time of the time range.

      .. note::

        Specify null to leave the start time open-ended.

    - **end** *(datetime) --*

      The end time of the time range.

      .. note::

        Specify null to leave the end time open-ended.
    """


_ClientListGitHubAccountTokenNamesResponseTypeDef = TypedDict(
    "_ClientListGitHubAccountTokenNamesResponseTypeDef",
    {"tokenNameList": List[str], "nextToken": str},
    total=False,
)


class ClientListGitHubAccountTokenNamesResponseTypeDef(
    _ClientListGitHubAccountTokenNamesResponseTypeDef
):
    """
    Type definition for `ClientListGitHubAccountTokenNames` `Response`

    Represents the output of a ListGitHubAccountTokenNames operation.

    - **tokenNameList** *(list) --*

      A list of names of connections to GitHub accounts.

      - *(string) --*

    - **nextToken** *(string) --*

      If a large amount of information is returned, an identifier is also returned. It can be used
      in a subsequent ListGitHubAccountTokenNames call to return the next set of names in the list.
    """


_ClientListOnPremisesInstancesResponseTypeDef = TypedDict(
    "_ClientListOnPremisesInstancesResponseTypeDef",
    {"instanceNames": List[str], "nextToken": str},
    total=False,
)


class ClientListOnPremisesInstancesResponseTypeDef(
    _ClientListOnPremisesInstancesResponseTypeDef
):
    """
    Type definition for `ClientListOnPremisesInstances` `Response`

    Represents the output of the list on-premises instances operation.

    - **instanceNames** *(list) --*

      The list of matching on-premises instance names.

      - *(string) --*

    - **nextToken** *(string) --*

      If a large amount of information is returned, an identifier is also returned. It can be used
      in a subsequent list on-premises instances call to return the next set of on-premises
      instances in the list.
    """


_ClientListOnPremisesInstancestagFiltersTypeDef = TypedDict(
    "_ClientListOnPremisesInstancestagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": str},
    total=False,
)


class ClientListOnPremisesInstancestagFiltersTypeDef(
    _ClientListOnPremisesInstancestagFiltersTypeDef
):
    """
    Type definition for `ClientListOnPremisesInstances` `tagFilters`

    Information about an on-premises instance tag filter.

    - **Key** *(string) --*

      The on-premises instance tag filter key.

    - **Value** *(string) --*

      The on-premises instance tag filter value.

    - **Type** *(string) --*

      The on-premises instance tag filter type:

      * KEY_ONLY: Key only.

      * VALUE_ONLY: Value only.

      * KEY_AND_VALUE: Key and value.
    """


_ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListTagsForResourceResponseTagsTypeDef(
    _ClientListTagsForResourceResponseTagsTypeDef
):
    """
    Type definition for `ClientListTagsForResourceResponse` `Tags`

    Information about a tag.

    - **Key** *(string) --*

      The tag's key.

    - **Value** *(string) --*

      The tag's value.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef], "NextToken": str},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **Tags** *(list) --*

      A list of tags returned by ``ListTagsForResource`` . The tags are associated with the
      resource identified by the input ``ResourceArn`` parameter.

      - *(dict) --*

        Information about a tag.

        - **Key** *(string) --*

          The tag's key.

        - **Value** *(string) --*

          The tag's value.

    - **NextToken** *(string) --*

      If a large amount of information is returned, an identifier is also returned. It can be used
      in a subsequent list application revisions call to return the next set of application
      revisions in the list.
    """


_ClientPutLifecycleEventHookExecutionStatusResponseTypeDef = TypedDict(
    "_ClientPutLifecycleEventHookExecutionStatusResponseTypeDef",
    {"lifecycleEventHookExecutionId": str},
    total=False,
)


class ClientPutLifecycleEventHookExecutionStatusResponseTypeDef(
    _ClientPutLifecycleEventHookExecutionStatusResponseTypeDef
):
    """
    Type definition for `ClientPutLifecycleEventHookExecutionStatus` `Response`

    - **lifecycleEventHookExecutionId** *(string) --*

      The execution ID of the lifecycle event hook. A hook is specified in the ``hooks`` section of
      the deployment's AppSpec file.
    """


_ClientRegisterApplicationRevisionrevisionappSpecContentTypeDef = TypedDict(
    "_ClientRegisterApplicationRevisionrevisionappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientRegisterApplicationRevisionrevisionappSpecContentTypeDef(
    _ClientRegisterApplicationRevisionrevisionappSpecContentTypeDef
):
    """
    Type definition for `ClientRegisterApplicationRevisionrevision` `appSpecContent`

    The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is
    formatted as JSON or YAML and stored as a RawString.

    - **content** *(string) --*

      The YAML-formatted or JSON-formatted revision string.

      For an AWS Lambda deployment, the content includes a Lambda function name, the alias for its
      original version, and the alias for its replacement version. The deployment shifts traffic
      from the original version of the Lambda function to the replacement version.

      For an Amazon ECS deployment, the content includes the task name, information about the load
      balancer that serves traffic to the container, and more.

      For both types of deployments, the content can specify Lambda functions that run at specified
      hooks, such as ``BeforeInstall`` , during a deployment.

    - **sha256** *(string) --*

      The SHA256 hash value of the revision content.
    """


_ClientRegisterApplicationRevisionrevisiongitHubLocationTypeDef = TypedDict(
    "_ClientRegisterApplicationRevisionrevisiongitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)


class ClientRegisterApplicationRevisionrevisiongitHubLocationTypeDef(
    _ClientRegisterApplicationRevisionrevisiongitHubLocationTypeDef
):
    """
    Type definition for `ClientRegisterApplicationRevisionrevision` `gitHubLocation`

    Information about the location of application artifacts stored in GitHub.

    - **repository** *(string) --*

      The GitHub account and repository pair that stores a reference to the commit that represents
      the bundled artifacts for the application revision.

      Specified as account/repository.

    - **commitId** *(string) --*

      The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
      application revision.
    """


_ClientRegisterApplicationRevisionrevisions3LocationTypeDef = TypedDict(
    "_ClientRegisterApplicationRevisionrevisions3LocationTypeDef",
    {"bucket": str, "key": str, "bundleType": str, "version": str, "eTag": str},
    total=False,
)


class ClientRegisterApplicationRevisionrevisions3LocationTypeDef(
    _ClientRegisterApplicationRevisionrevisions3LocationTypeDef
):
    """
    Type definition for `ClientRegisterApplicationRevisionrevision` `s3Location`

    Information about the location of a revision stored in Amazon S3.

    - **bucket** *(string) --*

      The name of the Amazon S3 bucket where the application revision is stored.

    - **key** *(string) --*

      The name of the Amazon S3 object that represents the bundled artifacts for the application
      revision.

    - **bundleType** *(string) --*

      The file type of the application revision. Must be one of the following:

      * tar: A tar archive file.

      * tgz: A compressed tar archive file.

      * zip: A zip archive file.

    - **version** *(string) --*

      A specific version of the Amazon S3 object that represents the bundled artifacts for the
      application revision.

      If the version is not specified, the system uses the most recent version by default.

    - **eTag** *(string) --*

      The ETag of the Amazon S3 object that represents the bundled artifacts for the application
      revision.

      If the ETag is not specified as an input parameter, ETag validation of the object is skipped.
    """


_ClientRegisterApplicationRevisionrevisionstringTypeDef = TypedDict(
    "_ClientRegisterApplicationRevisionrevisionstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientRegisterApplicationRevisionrevisionstringTypeDef(
    _ClientRegisterApplicationRevisionrevisionstringTypeDef
):
    """
    Type definition for `ClientRegisterApplicationRevisionrevision` `string`

    Information about the location of an AWS Lambda deployment revision stored as a RawString.

    - **content** *(string) --*

      The YAML-formatted or JSON-formatted revision string. It includes information about which
      Lambda function to update and optional Lambda functions that validate deployment lifecycle
      events.

    - **sha256** *(string) --*

      The SHA256 hash value of the revision content.
    """


_ClientRegisterApplicationRevisionrevisionTypeDef = TypedDict(
    "_ClientRegisterApplicationRevisionrevisionTypeDef",
    {
        "revisionType": str,
        "s3Location": ClientRegisterApplicationRevisionrevisions3LocationTypeDef,
        "gitHubLocation": ClientRegisterApplicationRevisionrevisiongitHubLocationTypeDef,
        "string": ClientRegisterApplicationRevisionrevisionstringTypeDef,
        "appSpecContent": ClientRegisterApplicationRevisionrevisionappSpecContentTypeDef,
    },
    total=False,
)


class ClientRegisterApplicationRevisionrevisionTypeDef(
    _ClientRegisterApplicationRevisionrevisionTypeDef
):
    """
    Type definition for `ClientRegisterApplicationRevision` `revision`

    Information about the application revision to register, including type and location.

    - **revisionType** *(string) --*

      The type of application revision:

      * S3: An application revision stored in Amazon S3.

      * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

      * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

    - **s3Location** *(dict) --*

      Information about the location of a revision stored in Amazon S3.

      - **bucket** *(string) --*

        The name of the Amazon S3 bucket where the application revision is stored.

      - **key** *(string) --*

        The name of the Amazon S3 object that represents the bundled artifacts for the application
        revision.

      - **bundleType** *(string) --*

        The file type of the application revision. Must be one of the following:

        * tar: A tar archive file.

        * tgz: A compressed tar archive file.

        * zip: A zip archive file.

      - **version** *(string) --*

        A specific version of the Amazon S3 object that represents the bundled artifacts for the
        application revision.

        If the version is not specified, the system uses the most recent version by default.

      - **eTag** *(string) --*

        The ETag of the Amazon S3 object that represents the bundled artifacts for the application
        revision.

        If the ETag is not specified as an input parameter, ETag validation of the object is skipped.

    - **gitHubLocation** *(dict) --*

      Information about the location of application artifacts stored in GitHub.

      - **repository** *(string) --*

        The GitHub account and repository pair that stores a reference to the commit that represents
        the bundled artifacts for the application revision.

        Specified as account/repository.

      - **commitId** *(string) --*

        The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
        application revision.

    - **string** *(dict) --*

      Information about the location of an AWS Lambda deployment revision stored as a RawString.

      - **content** *(string) --*

        The YAML-formatted or JSON-formatted revision string. It includes information about which
        Lambda function to update and optional Lambda functions that validate deployment lifecycle
        events.

      - **sha256** *(string) --*

        The SHA256 hash value of the revision content.

    - **appSpecContent** *(dict) --*

      The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is
      formatted as JSON or YAML and stored as a RawString.

      - **content** *(string) --*

        The YAML-formatted or JSON-formatted revision string.

        For an AWS Lambda deployment, the content includes a Lambda function name, the alias for its
        original version, and the alias for its replacement version. The deployment shifts traffic
        from the original version of the Lambda function to the replacement version.

        For an Amazon ECS deployment, the content includes the task name, information about the load
        balancer that serves traffic to the container, and more.

        For both types of deployments, the content can specify Lambda functions that run at specified
        hooks, such as ``BeforeInstall`` , during a deployment.

      - **sha256** *(string) --*

        The SHA256 hash value of the revision content.
    """


_ClientRemoveTagsFromOnPremisesInstancestagsTypeDef = TypedDict(
    "_ClientRemoveTagsFromOnPremisesInstancestagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientRemoveTagsFromOnPremisesInstancestagsTypeDef(
    _ClientRemoveTagsFromOnPremisesInstancestagsTypeDef
):
    """
    Type definition for `ClientRemoveTagsFromOnPremisesInstances` `tags`

    Information about a tag.

    - **Key** *(string) --*

      The tag's key.

    - **Value** *(string) --*

      The tag's value.
    """


_ClientStopDeploymentResponseTypeDef = TypedDict(
    "_ClientStopDeploymentResponseTypeDef",
    {"status": str, "statusMessage": str},
    total=False,
)


class ClientStopDeploymentResponseTypeDef(_ClientStopDeploymentResponseTypeDef):
    """
    Type definition for `ClientStopDeployment` `Response`

    Represents the output of a StopDeployment operation.

    - **status** *(string) --*

      The status of the stop deployment operation:

      * Pending: The stop operation is pending.

      * Succeeded: The stop operation was successful.

    - **statusMessage** *(string) --*

      An accompanying status message.
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    Type definition for `ClientTagResource` `Tags`

    Information about a tag.

    - **Key** *(string) --*

      The tag's key.

    - **Value** *(string) --*

      The tag's value.
    """


_ClientUpdateDeploymentGroupResponsehooksNotCleanedUpTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupResponsehooksNotCleanedUpTypeDef",
    {"name": str, "hook": str},
    total=False,
)


class ClientUpdateDeploymentGroupResponsehooksNotCleanedUpTypeDef(
    _ClientUpdateDeploymentGroupResponsehooksNotCleanedUpTypeDef
):
    """
    Type definition for `ClientUpdateDeploymentGroupResponse` `hooksNotCleanedUp`

    Information about an Auto Scaling group.

    - **name** *(string) --*

      The Auto Scaling group name.

    - **hook** *(string) --*

      An Auto Scaling lifecycle event hook name.
    """


_ClientUpdateDeploymentGroupResponseTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupResponseTypeDef",
    {
        "hooksNotCleanedUp": List[
            ClientUpdateDeploymentGroupResponsehooksNotCleanedUpTypeDef
        ]
    },
    total=False,
)


class ClientUpdateDeploymentGroupResponseTypeDef(
    _ClientUpdateDeploymentGroupResponseTypeDef
):
    """
    Type definition for `ClientUpdateDeploymentGroup` `Response`

    Represents the output of an UpdateDeploymentGroup operation.

    - **hooksNotCleanedUp** *(list) --*

      If the output contains no data, and the corresponding deployment group contained at least one
      Auto Scaling group, AWS CodeDeploy successfully removed all corresponding Auto Scaling
      lifecycle event hooks from the AWS account. If the output contains data, AWS CodeDeploy could
      not remove some Auto Scaling lifecycle event hooks from the AWS account.

      - *(dict) --*

        Information about an Auto Scaling group.

        - **name** *(string) --*

          The Auto Scaling group name.

        - **hook** *(string) --*

          An Auto Scaling lifecycle event hook name.
    """


_ClientUpdateDeploymentGroupalarmConfigurationalarmsTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupalarmConfigurationalarmsTypeDef",
    {"name": str},
    total=False,
)


class ClientUpdateDeploymentGroupalarmConfigurationalarmsTypeDef(
    _ClientUpdateDeploymentGroupalarmConfigurationalarmsTypeDef
):
    """
    Type definition for `ClientUpdateDeploymentGroupalarmConfiguration` `alarms`

    Information about an alarm.

    - **name** *(string) --*

      The name of the alarm. Maximum length is 255 characters. Each alarm name can be used only
      once in a list of alarms.
    """


_ClientUpdateDeploymentGroupalarmConfigurationTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupalarmConfigurationTypeDef",
    {
        "enabled": bool,
        "ignorePollAlarmFailure": bool,
        "alarms": List[ClientUpdateDeploymentGroupalarmConfigurationalarmsTypeDef],
    },
    total=False,
)


class ClientUpdateDeploymentGroupalarmConfigurationTypeDef(
    _ClientUpdateDeploymentGroupalarmConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateDeploymentGroup` `alarmConfiguration`

    Information to add or change about Amazon CloudWatch alarms when the deployment group is updated.

    - **enabled** *(boolean) --*

      Indicates whether the alarm configuration is enabled.

    - **ignorePollAlarmFailure** *(boolean) --*

      Indicates whether a deployment should continue if information about the current state of alarms
      cannot be retrieved from Amazon CloudWatch. The default value is false.

      * true: The deployment proceeds even if alarm status information can't be retrieved from Amazon
      CloudWatch.

      * false: The deployment stops if alarm status information can't be retrieved from Amazon
      CloudWatch.

    - **alarms** *(list) --*

      A list of alarms configured for the deployment group. A maximum of 10 alarms can be added to a
      deployment group.

      - *(dict) --*

        Information about an alarm.

        - **name** *(string) --*

          The name of the alarm. Maximum length is 255 characters. Each alarm name can be used only
          once in a list of alarms.
    """


_ClientUpdateDeploymentGroupautoRollbackConfigurationTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupautoRollbackConfigurationTypeDef",
    {"enabled": bool, "events": List[str]},
    total=False,
)


class ClientUpdateDeploymentGroupautoRollbackConfigurationTypeDef(
    _ClientUpdateDeploymentGroupautoRollbackConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateDeploymentGroup` `autoRollbackConfiguration`

    Information for an automatic rollback configuration that is added or changed when a deployment
    group is updated.

    - **enabled** *(boolean) --*

      Indicates whether a defined automatic rollback configuration is currently enabled.

    - **events** *(list) --*

      The event type or types that trigger a rollback.

      - *(string) --*
    """


_ClientUpdateDeploymentGroupblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    {"actionOnTimeout": str, "waitTimeInMinutes": int},
    total=False,
)


class ClientUpdateDeploymentGroupblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef(
    _ClientUpdateDeploymentGroupblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef
):
    """
    Type definition for `ClientUpdateDeploymentGroupblueGreenDeploymentConfiguration` `deploymentReadyOption`

    Information about the action to take when newly provisioned instances are ready to receive
    traffic in a blue/green deployment.

    - **actionOnTimeout** *(string) --*

      Information about when to reroute traffic from an original environment to a replacement
      environment in a blue/green deployment.

      * CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately after the
      new application revision is installed on the instances in the replacement environment.

      * STOP_DEPLOYMENT: Do not register new instances with a load balancer unless traffic
      rerouting is started using  ContinueDeployment . If traffic rerouting is not started before
      the end of the specified wait period, the deployment status is changed to Stopped.

    - **waitTimeInMinutes** *(integer) --*

      The number of minutes to wait before the status of a blue/green deployment is changed to
      Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT option for
      actionOnTimeout
    """


_ClientUpdateDeploymentGroupblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    {"action": str},
    total=False,
)


class ClientUpdateDeploymentGroupblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef(
    _ClientUpdateDeploymentGroupblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef
):
    """
    Type definition for `ClientUpdateDeploymentGroupblueGreenDeploymentConfiguration` `greenFleetProvisioningOption`

    Information about how instances are provisioned for a replacement environment in a blue/green
    deployment.

    - **action** *(string) --*

      The method used to add instances to a replacement environment.

      * DISCOVER_EXISTING: Use instances that already exist or will be created manually.

      * COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to define and
      create instances in a new Auto Scaling group.
    """


_ClientUpdateDeploymentGroupblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    {"action": str, "terminationWaitTimeInMinutes": int},
    total=False,
)


class ClientUpdateDeploymentGroupblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef(
    _ClientUpdateDeploymentGroupblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef
):
    """
    Type definition for `ClientUpdateDeploymentGroupblueGreenDeploymentConfiguration` `terminateBlueInstancesOnDeploymentSuccess`

    Information about whether to terminate instances in the original fleet during a blue/green
    deployment.

    - **action** *(string) --*

      The action to take on instances in the original environment after a successful blue/green
      deployment.

      * TERMINATE: Instances are terminated after a specified wait time.

      * KEEP_ALIVE: Instances are left running after they are deregistered from the load balancer
      and removed from the deployment group.

    - **terminationWaitTimeInMinutes** *(integer) --*

      For an Amazon EC2 deployment, the number of minutes to wait after a successful blue/green
      deployment before terminating instances from the original environment.

      For an Amazon ECS deployment, the number of minutes before deleting the original (blue) task
      set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the original (blue) task
      set to a replacement (green) task set.

      The maximum setting is 2880 minutes (2 days).
    """


_ClientUpdateDeploymentGroupblueGreenDeploymentConfigurationTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupblueGreenDeploymentConfigurationTypeDef",
    {
        "terminateBlueInstancesOnDeploymentSuccess": ClientUpdateDeploymentGroupblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef,
        "deploymentReadyOption": ClientUpdateDeploymentGroupblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef,
        "greenFleetProvisioningOption": ClientUpdateDeploymentGroupblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef,
    },
    total=False,
)


class ClientUpdateDeploymentGroupblueGreenDeploymentConfigurationTypeDef(
    _ClientUpdateDeploymentGroupblueGreenDeploymentConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateDeploymentGroup` `blueGreenDeploymentConfiguration`

    Information about blue/green deployment options for a deployment group.

    - **terminateBlueInstancesOnDeploymentSuccess** *(dict) --*

      Information about whether to terminate instances in the original fleet during a blue/green
      deployment.

      - **action** *(string) --*

        The action to take on instances in the original environment after a successful blue/green
        deployment.

        * TERMINATE: Instances are terminated after a specified wait time.

        * KEEP_ALIVE: Instances are left running after they are deregistered from the load balancer
        and removed from the deployment group.

      - **terminationWaitTimeInMinutes** *(integer) --*

        For an Amazon EC2 deployment, the number of minutes to wait after a successful blue/green
        deployment before terminating instances from the original environment.

        For an Amazon ECS deployment, the number of minutes before deleting the original (blue) task
        set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the original (blue) task
        set to a replacement (green) task set.

        The maximum setting is 2880 minutes (2 days).

    - **deploymentReadyOption** *(dict) --*

      Information about the action to take when newly provisioned instances are ready to receive
      traffic in a blue/green deployment.

      - **actionOnTimeout** *(string) --*

        Information about when to reroute traffic from an original environment to a replacement
        environment in a blue/green deployment.

        * CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately after the
        new application revision is installed on the instances in the replacement environment.

        * STOP_DEPLOYMENT: Do not register new instances with a load balancer unless traffic
        rerouting is started using  ContinueDeployment . If traffic rerouting is not started before
        the end of the specified wait period, the deployment status is changed to Stopped.

      - **waitTimeInMinutes** *(integer) --*

        The number of minutes to wait before the status of a blue/green deployment is changed to
        Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT option for
        actionOnTimeout

    - **greenFleetProvisioningOption** *(dict) --*

      Information about how instances are provisioned for a replacement environment in a blue/green
      deployment.

      - **action** *(string) --*

        The method used to add instances to a replacement environment.

        * DISCOVER_EXISTING: Use instances that already exist or will be created manually.

        * COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to define and
        create instances in a new Auto Scaling group.
    """


_ClientUpdateDeploymentGroupdeploymentStyleTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupdeploymentStyleTypeDef",
    {"deploymentType": str, "deploymentOption": str},
    total=False,
)


class ClientUpdateDeploymentGroupdeploymentStyleTypeDef(
    _ClientUpdateDeploymentGroupdeploymentStyleTypeDef
):
    """
    Type definition for `ClientUpdateDeploymentGroup` `deploymentStyle`

    Information about the type of deployment, either in-place or blue/green, you want to run and
    whether to route deployment traffic behind a load balancer.

    - **deploymentType** *(string) --*

      Indicates whether to run an in-place deployment or a blue/green deployment.

    - **deploymentOption** *(string) --*

      Indicates whether to route deployment traffic behind a load balancer.
    """


_ClientUpdateDeploymentGroupec2TagFiltersTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupec2TagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": str},
    total=False,
)


class ClientUpdateDeploymentGroupec2TagFiltersTypeDef(
    _ClientUpdateDeploymentGroupec2TagFiltersTypeDef
):
    """
    Type definition for `ClientUpdateDeploymentGroup` `ec2TagFilters`

    Information about an EC2 tag filter.

    - **Key** *(string) --*

      The tag filter key.

    - **Value** *(string) --*

      The tag filter value.

    - **Type** *(string) --*

      The tag filter type:

      * KEY_ONLY: Key only.

      * VALUE_ONLY: Value only.

      * KEY_AND_VALUE: Key and value.
    """


_ClientUpdateDeploymentGroupec2TagSetec2TagSetListTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupec2TagSetec2TagSetListTypeDef",
    {"Key": str, "Value": str, "Type": str},
    total=False,
)


class ClientUpdateDeploymentGroupec2TagSetec2TagSetListTypeDef(
    _ClientUpdateDeploymentGroupec2TagSetec2TagSetListTypeDef
):
    """
    Type definition for `ClientUpdateDeploymentGroupec2TagSet` `ec2TagSetList`

    Information about an EC2 tag filter.

    - **Key** *(string) --*

      The tag filter key.

    - **Value** *(string) --*

      The tag filter value.

    - **Type** *(string) --*

      The tag filter type:

      * KEY_ONLY: Key only.

      * VALUE_ONLY: Value only.

      * KEY_AND_VALUE: Key and value.
    """


_ClientUpdateDeploymentGroupec2TagSetTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupec2TagSetTypeDef",
    {
        "ec2TagSetList": List[
            List[ClientUpdateDeploymentGroupec2TagSetec2TagSetListTypeDef]
        ]
    },
    total=False,
)


class ClientUpdateDeploymentGroupec2TagSetTypeDef(
    _ClientUpdateDeploymentGroupec2TagSetTypeDef
):
    """
    Type definition for `ClientUpdateDeploymentGroup` `ec2TagSet`

    Information about groups of tags applied to on-premises instances. The deployment group includes
    only EC2 instances identified by all the tag groups.

    - **ec2TagSetList** *(list) --*

      A list that contains other lists of EC2 instance tag groups. For an instance to be included in
      the deployment group, it must be identified by all of the tag groups in the list.

      - *(list) --*

        - *(dict) --*

          Information about an EC2 tag filter.

          - **Key** *(string) --*

            The tag filter key.

          - **Value** *(string) --*

            The tag filter value.

          - **Type** *(string) --*

            The tag filter type:

            * KEY_ONLY: Key only.

            * VALUE_ONLY: Value only.

            * KEY_AND_VALUE: Key and value.
    """


_ClientUpdateDeploymentGroupecsServicesTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupecsServicesTypeDef",
    {"serviceName": str, "clusterName": str},
    total=False,
)


class ClientUpdateDeploymentGroupecsServicesTypeDef(
    _ClientUpdateDeploymentGroupecsServicesTypeDef
):
    """
    Type definition for `ClientUpdateDeploymentGroup` `ecsServices`

    Contains the service and cluster names used to identify an Amazon ECS deployment's target.

    - **serviceName** *(string) --*

      The name of the target Amazon ECS service.

    - **clusterName** *(string) --*

      The name of the cluster that the Amazon ECS service is associated with.
    """


_ClientUpdateDeploymentGrouploadBalancerInfoelbInfoListTypeDef = TypedDict(
    "_ClientUpdateDeploymentGrouploadBalancerInfoelbInfoListTypeDef",
    {"name": str},
    total=False,
)


class ClientUpdateDeploymentGrouploadBalancerInfoelbInfoListTypeDef(
    _ClientUpdateDeploymentGrouploadBalancerInfoelbInfoListTypeDef
):
    """
    Type definition for `ClientUpdateDeploymentGrouploadBalancerInfo` `elbInfoList`

    Information about a load balancer in Elastic Load Balancing to use in a deployment. Instances
    are registered directly with a load balancer, and traffic is routed to the load balancer.

    - **name** *(string) --*

      For blue/green deployments, the name of the load balancer that is used to route traffic
      from original instances to replacement instances in a blue/green deployment. For in-place
      deployments, the name of the load balancer that instances are deregistered from so they are
      not serving traffic during a deployment, and then re-registered with after the deployment
      is complete.
    """


_ClientUpdateDeploymentGrouploadBalancerInfotargetGroupInfoListTypeDef = TypedDict(
    "_ClientUpdateDeploymentGrouploadBalancerInfotargetGroupInfoListTypeDef",
    {"name": str},
    total=False,
)


class ClientUpdateDeploymentGrouploadBalancerInfotargetGroupInfoListTypeDef(
    _ClientUpdateDeploymentGrouploadBalancerInfotargetGroupInfoListTypeDef
):
    """
    Type definition for `ClientUpdateDeploymentGrouploadBalancerInfo` `targetGroupInfoList`

    Information about a target group in Elastic Load Balancing to use in a deployment. Instances
    are registered as targets in a target group, and traffic is routed to the target group.

    - **name** *(string) --*

      For blue/green deployments, the name of the target group that instances in the original
      environment are deregistered from, and instances in the replacement environment are
      registered with. For in-place deployments, the name of the target group that instances are
      deregistered from, so they are not serving traffic during a deployment, and then
      re-registered with after the deployment is complete.
    """


_ClientUpdateDeploymentGrouploadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef = TypedDict(
    "_ClientUpdateDeploymentGrouploadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)


class ClientUpdateDeploymentGrouploadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef(
    _ClientUpdateDeploymentGrouploadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef
):
    """
    Type definition for `ClientUpdateDeploymentGrouploadBalancerInfotargetGroupPairInfoList` `prodTrafficRoute`

    The path used by a load balancer to route production traffic when an Amazon ECS deployment
    is complete.

    - **listenerArns** *(list) --*

      The ARN of one listener. The listener identifies the route between a target group and a
      load balancer. This is an array of strings with a maximum size of one.

      - *(string) --*
    """


_ClientUpdateDeploymentGrouploadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef = TypedDict(
    "_ClientUpdateDeploymentGrouploadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    {"name": str},
    total=False,
)


class ClientUpdateDeploymentGrouploadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef(
    _ClientUpdateDeploymentGrouploadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef
):
    """
    Type definition for `ClientUpdateDeploymentGrouploadBalancerInfotargetGroupPairInfoList` `targetGroups`

    Information about a target group in Elastic Load Balancing to use in a deployment.
    Instances are registered as targets in a target group, and traffic is routed to the
    target group.

    - **name** *(string) --*

      For blue/green deployments, the name of the target group that instances in the original
      environment are deregistered from, and instances in the replacement environment are
      registered with. For in-place deployments, the name of the target group that instances
      are deregistered from, so they are not serving traffic during a deployment, and then
      re-registered with after the deployment is complete.
    """


_ClientUpdateDeploymentGrouploadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef = TypedDict(
    "_ClientUpdateDeploymentGrouploadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)


class ClientUpdateDeploymentGrouploadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef(
    _ClientUpdateDeploymentGrouploadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef
):
    """
    Type definition for `ClientUpdateDeploymentGrouploadBalancerInfotargetGroupPairInfoList` `testTrafficRoute`

    An optional path used by a load balancer to route test traffic after an Amazon ECS
    deployment. Validation can occur while test traffic is served during a deployment.

    - **listenerArns** *(list) --*

      The ARN of one listener. The listener identifies the route between a target group and a
      load balancer. This is an array of strings with a maximum size of one.

      - *(string) --*
    """


_ClientUpdateDeploymentGrouploadBalancerInfotargetGroupPairInfoListTypeDef = TypedDict(
    "_ClientUpdateDeploymentGrouploadBalancerInfotargetGroupPairInfoListTypeDef",
    {
        "targetGroups": List[
            ClientUpdateDeploymentGrouploadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef
        ],
        "prodTrafficRoute": ClientUpdateDeploymentGrouploadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef,
        "testTrafficRoute": ClientUpdateDeploymentGrouploadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef,
    },
    total=False,
)


class ClientUpdateDeploymentGrouploadBalancerInfotargetGroupPairInfoListTypeDef(
    _ClientUpdateDeploymentGrouploadBalancerInfotargetGroupPairInfoListTypeDef
):
    """
    Type definition for `ClientUpdateDeploymentGrouploadBalancerInfo` `targetGroupPairInfoList`

    Information about two target groups and how traffic is routed during an Amazon ECS
    deployment. An optional test traffic route can be specified.

    - **targetGroups** *(list) --*

      One pair of target groups. One is associated with the original task set. The second is
      associated with the task set that serves traffic after the deployment is complete.

      - *(dict) --*

        Information about a target group in Elastic Load Balancing to use in a deployment.
        Instances are registered as targets in a target group, and traffic is routed to the
        target group.

        - **name** *(string) --*

          For blue/green deployments, the name of the target group that instances in the original
          environment are deregistered from, and instances in the replacement environment are
          registered with. For in-place deployments, the name of the target group that instances
          are deregistered from, so they are not serving traffic during a deployment, and then
          re-registered with after the deployment is complete.

    - **prodTrafficRoute** *(dict) --*

      The path used by a load balancer to route production traffic when an Amazon ECS deployment
      is complete.

      - **listenerArns** *(list) --*

        The ARN of one listener. The listener identifies the route between a target group and a
        load balancer. This is an array of strings with a maximum size of one.

        - *(string) --*

    - **testTrafficRoute** *(dict) --*

      An optional path used by a load balancer to route test traffic after an Amazon ECS
      deployment. Validation can occur while test traffic is served during a deployment.

      - **listenerArns** *(list) --*

        The ARN of one listener. The listener identifies the route between a target group and a
        load balancer. This is an array of strings with a maximum size of one.

        - *(string) --*
    """


_ClientUpdateDeploymentGrouploadBalancerInfoTypeDef = TypedDict(
    "_ClientUpdateDeploymentGrouploadBalancerInfoTypeDef",
    {
        "elbInfoList": List[
            ClientUpdateDeploymentGrouploadBalancerInfoelbInfoListTypeDef
        ],
        "targetGroupInfoList": List[
            ClientUpdateDeploymentGrouploadBalancerInfotargetGroupInfoListTypeDef
        ],
        "targetGroupPairInfoList": List[
            ClientUpdateDeploymentGrouploadBalancerInfotargetGroupPairInfoListTypeDef
        ],
    },
    total=False,
)


class ClientUpdateDeploymentGrouploadBalancerInfoTypeDef(
    _ClientUpdateDeploymentGrouploadBalancerInfoTypeDef
):
    """
    Type definition for `ClientUpdateDeploymentGroup` `loadBalancerInfo`

    Information about the load balancer used in a deployment.

    - **elbInfoList** *(list) --*

      An array that contains information about the load balancer to use for load balancing in a
      deployment. In Elastic Load Balancing, load balancers are used with Classic Load Balancers.

      .. note::

        Adding more than one load balancer to the array is not supported.

      - *(dict) --*

        Information about a load balancer in Elastic Load Balancing to use in a deployment. Instances
        are registered directly with a load balancer, and traffic is routed to the load balancer.

        - **name** *(string) --*

          For blue/green deployments, the name of the load balancer that is used to route traffic
          from original instances to replacement instances in a blue/green deployment. For in-place
          deployments, the name of the load balancer that instances are deregistered from so they are
          not serving traffic during a deployment, and then re-registered with after the deployment
          is complete.

    - **targetGroupInfoList** *(list) --*

      An array that contains information about the target group to use for load balancing in a
      deployment. In Elastic Load Balancing, target groups are used with Application Load Balancers.

      .. note::

        Adding more than one target group to the array is not supported.

      - *(dict) --*

        Information about a target group in Elastic Load Balancing to use in a deployment. Instances
        are registered as targets in a target group, and traffic is routed to the target group.

        - **name** *(string) --*

          For blue/green deployments, the name of the target group that instances in the original
          environment are deregistered from, and instances in the replacement environment are
          registered with. For in-place deployments, the name of the target group that instances are
          deregistered from, so they are not serving traffic during a deployment, and then
          re-registered with after the deployment is complete.

    - **targetGroupPairInfoList** *(list) --*

      The target group pair information. This is an array of ``TargeGroupPairInfo`` objects with a
      maximum size of one.

      - *(dict) --*

        Information about two target groups and how traffic is routed during an Amazon ECS
        deployment. An optional test traffic route can be specified.

        - **targetGroups** *(list) --*

          One pair of target groups. One is associated with the original task set. The second is
          associated with the task set that serves traffic after the deployment is complete.

          - *(dict) --*

            Information about a target group in Elastic Load Balancing to use in a deployment.
            Instances are registered as targets in a target group, and traffic is routed to the
            target group.

            - **name** *(string) --*

              For blue/green deployments, the name of the target group that instances in the original
              environment are deregistered from, and instances in the replacement environment are
              registered with. For in-place deployments, the name of the target group that instances
              are deregistered from, so they are not serving traffic during a deployment, and then
              re-registered with after the deployment is complete.

        - **prodTrafficRoute** *(dict) --*

          The path used by a load balancer to route production traffic when an Amazon ECS deployment
          is complete.

          - **listenerArns** *(list) --*

            The ARN of one listener. The listener identifies the route between a target group and a
            load balancer. This is an array of strings with a maximum size of one.

            - *(string) --*

        - **testTrafficRoute** *(dict) --*

          An optional path used by a load balancer to route test traffic after an Amazon ECS
          deployment. Validation can occur while test traffic is served during a deployment.

          - **listenerArns** *(list) --*

            The ARN of one listener. The listener identifies the route between a target group and a
            load balancer. This is an array of strings with a maximum size of one.

            - *(string) --*
    """


_ClientUpdateDeploymentGrouponPremisesInstanceTagFiltersTypeDef = TypedDict(
    "_ClientUpdateDeploymentGrouponPremisesInstanceTagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": str},
    total=False,
)


class ClientUpdateDeploymentGrouponPremisesInstanceTagFiltersTypeDef(
    _ClientUpdateDeploymentGrouponPremisesInstanceTagFiltersTypeDef
):
    """
    Type definition for `ClientUpdateDeploymentGroup` `onPremisesInstanceTagFilters`

    Information about an on-premises instance tag filter.

    - **Key** *(string) --*

      The on-premises instance tag filter key.

    - **Value** *(string) --*

      The on-premises instance tag filter value.

    - **Type** *(string) --*

      The on-premises instance tag filter type:

      * KEY_ONLY: Key only.

      * VALUE_ONLY: Value only.

      * KEY_AND_VALUE: Key and value.
    """


_ClientUpdateDeploymentGrouponPremisesTagSetonPremisesTagSetListTypeDef = TypedDict(
    "_ClientUpdateDeploymentGrouponPremisesTagSetonPremisesTagSetListTypeDef",
    {"Key": str, "Value": str, "Type": str},
    total=False,
)


class ClientUpdateDeploymentGrouponPremisesTagSetonPremisesTagSetListTypeDef(
    _ClientUpdateDeploymentGrouponPremisesTagSetonPremisesTagSetListTypeDef
):
    """
    Type definition for `ClientUpdateDeploymentGrouponPremisesTagSet` `onPremisesTagSetList`

    Information about an on-premises instance tag filter.

    - **Key** *(string) --*

      The on-premises instance tag filter key.

    - **Value** *(string) --*

      The on-premises instance tag filter value.

    - **Type** *(string) --*

      The on-premises instance tag filter type:

      * KEY_ONLY: Key only.

      * VALUE_ONLY: Value only.

      * KEY_AND_VALUE: Key and value.
    """


_ClientUpdateDeploymentGrouponPremisesTagSetTypeDef = TypedDict(
    "_ClientUpdateDeploymentGrouponPremisesTagSetTypeDef",
    {
        "onPremisesTagSetList": List[
            List[ClientUpdateDeploymentGrouponPremisesTagSetonPremisesTagSetListTypeDef]
        ]
    },
    total=False,
)


class ClientUpdateDeploymentGrouponPremisesTagSetTypeDef(
    _ClientUpdateDeploymentGrouponPremisesTagSetTypeDef
):
    """
    Type definition for `ClientUpdateDeploymentGroup` `onPremisesTagSet`

    Information about an on-premises instance tag set. The deployment group includes only on-premises
    instances identified by all the tag groups.

    - **onPremisesTagSetList** *(list) --*

      A list that contains other lists of on-premises instance tag groups. For an instance to be
      included in the deployment group, it must be identified by all of the tag groups in the list.

      - *(list) --*

        - *(dict) --*

          Information about an on-premises instance tag filter.

          - **Key** *(string) --*

            The on-premises instance tag filter key.

          - **Value** *(string) --*

            The on-premises instance tag filter value.

          - **Type** *(string) --*

            The on-premises instance tag filter type:

            * KEY_ONLY: Key only.

            * VALUE_ONLY: Value only.

            * KEY_AND_VALUE: Key and value.
    """


_ClientUpdateDeploymentGrouptriggerConfigurationsTypeDef = TypedDict(
    "_ClientUpdateDeploymentGrouptriggerConfigurationsTypeDef",
    {"triggerName": str, "triggerTargetArn": str, "triggerEvents": List[str]},
    total=False,
)


class ClientUpdateDeploymentGrouptriggerConfigurationsTypeDef(
    _ClientUpdateDeploymentGrouptriggerConfigurationsTypeDef
):
    """
    Type definition for `ClientUpdateDeploymentGroup` `triggerConfigurations`

    Information about notification triggers for the deployment group.

    - **triggerName** *(string) --*

      The name of the notification trigger.

    - **triggerTargetArn** *(string) --*

      The ARN of the Amazon Simple Notification Service topic through which notifications about
      deployment or instance events are sent.

    - **triggerEvents** *(list) --*

      The event type or types for which notifications are triggered.

      - *(string) --*
    """


_DeploymentSuccessfulWaitWaiterConfigTypeDef = TypedDict(
    "_DeploymentSuccessfulWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class DeploymentSuccessfulWaitWaiterConfigTypeDef(
    _DeploymentSuccessfulWaitWaiterConfigTypeDef
):
    """
    Type definition for `DeploymentSuccessfulWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 120
    """


_ListApplicationRevisionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListApplicationRevisionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListApplicationRevisionsPaginatePaginationConfigTypeDef(
    _ListApplicationRevisionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListApplicationRevisionsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListApplicationRevisionsPaginateResponserevisionsappSpecContentTypeDef = TypedDict(
    "_ListApplicationRevisionsPaginateResponserevisionsappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ListApplicationRevisionsPaginateResponserevisionsappSpecContentTypeDef(
    _ListApplicationRevisionsPaginateResponserevisionsappSpecContentTypeDef
):
    """
    Type definition for `ListApplicationRevisionsPaginateResponserevisions` `appSpecContent`

    The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is
    formatted as JSON or YAML and stored as a RawString.

    - **content** *(string) --*

      The YAML-formatted or JSON-formatted revision string.

      For an AWS Lambda deployment, the content includes a Lambda function name, the alias
      for its original version, and the alias for its replacement version. The deployment
      shifts traffic from the original version of the Lambda function to the replacement
      version.

      For an Amazon ECS deployment, the content includes the task name, information about the
      load balancer that serves traffic to the container, and more.

      For both types of deployments, the content can specify Lambda functions that run at
      specified hooks, such as ``BeforeInstall`` , during a deployment.

    - **sha256** *(string) --*

      The SHA256 hash value of the revision content.
    """


_ListApplicationRevisionsPaginateResponserevisionsgitHubLocationTypeDef = TypedDict(
    "_ListApplicationRevisionsPaginateResponserevisionsgitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)


class ListApplicationRevisionsPaginateResponserevisionsgitHubLocationTypeDef(
    _ListApplicationRevisionsPaginateResponserevisionsgitHubLocationTypeDef
):
    """
    Type definition for `ListApplicationRevisionsPaginateResponserevisions` `gitHubLocation`

    Information about the location of application artifacts stored in GitHub.

    - **repository** *(string) --*

      The GitHub account and repository pair that stores a reference to the commit that
      represents the bundled artifacts for the application revision.

      Specified as account/repository.

    - **commitId** *(string) --*

      The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
      application revision.
    """


_ListApplicationRevisionsPaginateResponserevisionss3LocationTypeDef = TypedDict(
    "_ListApplicationRevisionsPaginateResponserevisionss3LocationTypeDef",
    {"bucket": str, "key": str, "bundleType": str, "version": str, "eTag": str},
    total=False,
)


class ListApplicationRevisionsPaginateResponserevisionss3LocationTypeDef(
    _ListApplicationRevisionsPaginateResponserevisionss3LocationTypeDef
):
    """
    Type definition for `ListApplicationRevisionsPaginateResponserevisions` `s3Location`

    Information about the location of a revision stored in Amazon S3.

    - **bucket** *(string) --*

      The name of the Amazon S3 bucket where the application revision is stored.

    - **key** *(string) --*

      The name of the Amazon S3 object that represents the bundled artifacts for the
      application revision.

    - **bundleType** *(string) --*

      The file type of the application revision. Must be one of the following:

      * tar: A tar archive file.

      * tgz: A compressed tar archive file.

      * zip: A zip archive file.

    - **version** *(string) --*

      A specific version of the Amazon S3 object that represents the bundled artifacts for
      the application revision.

      If the version is not specified, the system uses the most recent version by default.

    - **eTag** *(string) --*

      The ETag of the Amazon S3 object that represents the bundled artifacts for the
      application revision.

      If the ETag is not specified as an input parameter, ETag validation of the object is
      skipped.
    """


_ListApplicationRevisionsPaginateResponserevisionsstringTypeDef = TypedDict(
    "_ListApplicationRevisionsPaginateResponserevisionsstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ListApplicationRevisionsPaginateResponserevisionsstringTypeDef(
    _ListApplicationRevisionsPaginateResponserevisionsstringTypeDef
):
    """
    Type definition for `ListApplicationRevisionsPaginateResponserevisions` `string`

    Information about the location of an AWS Lambda deployment revision stored as a RawString.

    - **content** *(string) --*

      The YAML-formatted or JSON-formatted revision string. It includes information about
      which Lambda function to update and optional Lambda functions that validate deployment
      lifecycle events.

    - **sha256** *(string) --*

      The SHA256 hash value of the revision content.
    """


_ListApplicationRevisionsPaginateResponserevisionsTypeDef = TypedDict(
    "_ListApplicationRevisionsPaginateResponserevisionsTypeDef",
    {
        "revisionType": str,
        "s3Location": ListApplicationRevisionsPaginateResponserevisionss3LocationTypeDef,
        "gitHubLocation": ListApplicationRevisionsPaginateResponserevisionsgitHubLocationTypeDef,
        "string": ListApplicationRevisionsPaginateResponserevisionsstringTypeDef,
        "appSpecContent": ListApplicationRevisionsPaginateResponserevisionsappSpecContentTypeDef,
    },
    total=False,
)


class ListApplicationRevisionsPaginateResponserevisionsTypeDef(
    _ListApplicationRevisionsPaginateResponserevisionsTypeDef
):
    """
    Type definition for `ListApplicationRevisionsPaginateResponse` `revisions`

    Information about the location of an application revision.

    - **revisionType** *(string) --*

      The type of application revision:

      * S3: An application revision stored in Amazon S3.

      * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

      * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

    - **s3Location** *(dict) --*

      Information about the location of a revision stored in Amazon S3.

      - **bucket** *(string) --*

        The name of the Amazon S3 bucket where the application revision is stored.

      - **key** *(string) --*

        The name of the Amazon S3 object that represents the bundled artifacts for the
        application revision.

      - **bundleType** *(string) --*

        The file type of the application revision. Must be one of the following:

        * tar: A tar archive file.

        * tgz: A compressed tar archive file.

        * zip: A zip archive file.

      - **version** *(string) --*

        A specific version of the Amazon S3 object that represents the bundled artifacts for
        the application revision.

        If the version is not specified, the system uses the most recent version by default.

      - **eTag** *(string) --*

        The ETag of the Amazon S3 object that represents the bundled artifacts for the
        application revision.

        If the ETag is not specified as an input parameter, ETag validation of the object is
        skipped.

    - **gitHubLocation** *(dict) --*

      Information about the location of application artifacts stored in GitHub.

      - **repository** *(string) --*

        The GitHub account and repository pair that stores a reference to the commit that
        represents the bundled artifacts for the application revision.

        Specified as account/repository.

      - **commitId** *(string) --*

        The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
        application revision.

    - **string** *(dict) --*

      Information about the location of an AWS Lambda deployment revision stored as a RawString.

      - **content** *(string) --*

        The YAML-formatted or JSON-formatted revision string. It includes information about
        which Lambda function to update and optional Lambda functions that validate deployment
        lifecycle events.

      - **sha256** *(string) --*

        The SHA256 hash value of the revision content.

    - **appSpecContent** *(dict) --*

      The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is
      formatted as JSON or YAML and stored as a RawString.

      - **content** *(string) --*

        The YAML-formatted or JSON-formatted revision string.

        For an AWS Lambda deployment, the content includes a Lambda function name, the alias
        for its original version, and the alias for its replacement version. The deployment
        shifts traffic from the original version of the Lambda function to the replacement
        version.

        For an Amazon ECS deployment, the content includes the task name, information about the
        load balancer that serves traffic to the container, and more.

        For both types of deployments, the content can specify Lambda functions that run at
        specified hooks, such as ``BeforeInstall`` , during a deployment.

      - **sha256** *(string) --*

        The SHA256 hash value of the revision content.
    """


_ListApplicationRevisionsPaginateResponseTypeDef = TypedDict(
    "_ListApplicationRevisionsPaginateResponseTypeDef",
    {
        "revisions": List[ListApplicationRevisionsPaginateResponserevisionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListApplicationRevisionsPaginateResponseTypeDef(
    _ListApplicationRevisionsPaginateResponseTypeDef
):
    """
    Type definition for `ListApplicationRevisionsPaginate` `Response`

    Represents the output of a ListApplicationRevisions operation.

    - **revisions** *(list) --*

      A list of locations that contain the matching revisions.

      - *(dict) --*

        Information about the location of an application revision.

        - **revisionType** *(string) --*

          The type of application revision:

          * S3: An application revision stored in Amazon S3.

          * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

          * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

        - **s3Location** *(dict) --*

          Information about the location of a revision stored in Amazon S3.

          - **bucket** *(string) --*

            The name of the Amazon S3 bucket where the application revision is stored.

          - **key** *(string) --*

            The name of the Amazon S3 object that represents the bundled artifacts for the
            application revision.

          - **bundleType** *(string) --*

            The file type of the application revision. Must be one of the following:

            * tar: A tar archive file.

            * tgz: A compressed tar archive file.

            * zip: A zip archive file.

          - **version** *(string) --*

            A specific version of the Amazon S3 object that represents the bundled artifacts for
            the application revision.

            If the version is not specified, the system uses the most recent version by default.

          - **eTag** *(string) --*

            The ETag of the Amazon S3 object that represents the bundled artifacts for the
            application revision.

            If the ETag is not specified as an input parameter, ETag validation of the object is
            skipped.

        - **gitHubLocation** *(dict) --*

          Information about the location of application artifacts stored in GitHub.

          - **repository** *(string) --*

            The GitHub account and repository pair that stores a reference to the commit that
            represents the bundled artifacts for the application revision.

            Specified as account/repository.

          - **commitId** *(string) --*

            The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
            application revision.

        - **string** *(dict) --*

          Information about the location of an AWS Lambda deployment revision stored as a RawString.

          - **content** *(string) --*

            The YAML-formatted or JSON-formatted revision string. It includes information about
            which Lambda function to update and optional Lambda functions that validate deployment
            lifecycle events.

          - **sha256** *(string) --*

            The SHA256 hash value of the revision content.

        - **appSpecContent** *(dict) --*

          The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is
          formatted as JSON or YAML and stored as a RawString.

          - **content** *(string) --*

            The YAML-formatted or JSON-formatted revision string.

            For an AWS Lambda deployment, the content includes a Lambda function name, the alias
            for its original version, and the alias for its replacement version. The deployment
            shifts traffic from the original version of the Lambda function to the replacement
            version.

            For an Amazon ECS deployment, the content includes the task name, information about the
            load balancer that serves traffic to the container, and more.

            For both types of deployments, the content can specify Lambda functions that run at
            specified hooks, such as ``BeforeInstall`` , during a deployment.

          - **sha256** *(string) --*

            The SHA256 hash value of the revision content.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListApplicationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListApplicationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListApplicationsPaginatePaginationConfigTypeDef(
    _ListApplicationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListApplicationsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListApplicationsPaginateResponseTypeDef = TypedDict(
    "_ListApplicationsPaginateResponseTypeDef",
    {"applications": List[str], "NextToken": str},
    total=False,
)


class ListApplicationsPaginateResponseTypeDef(_ListApplicationsPaginateResponseTypeDef):
    """
    Type definition for `ListApplicationsPaginate` `Response`

    Represents the output of a ListApplications operation.

    - **applications** *(list) --*

      A list of application names.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListDeploymentConfigsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDeploymentConfigsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListDeploymentConfigsPaginatePaginationConfigTypeDef(
    _ListDeploymentConfigsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDeploymentConfigsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListDeploymentConfigsPaginateResponseTypeDef = TypedDict(
    "_ListDeploymentConfigsPaginateResponseTypeDef",
    {"deploymentConfigsList": List[str], "NextToken": str},
    total=False,
)


class ListDeploymentConfigsPaginateResponseTypeDef(
    _ListDeploymentConfigsPaginateResponseTypeDef
):
    """
    Type definition for `ListDeploymentConfigsPaginate` `Response`

    Represents the output of a ListDeploymentConfigs operation.

    - **deploymentConfigsList** *(list) --*

      A list of deployment configurations, including built-in configurations such as
      CodeDeployDefault.OneAtATime.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListDeploymentGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDeploymentGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListDeploymentGroupsPaginatePaginationConfigTypeDef(
    _ListDeploymentGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDeploymentGroupsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListDeploymentGroupsPaginateResponseTypeDef = TypedDict(
    "_ListDeploymentGroupsPaginateResponseTypeDef",
    {"applicationName": str, "deploymentGroups": List[str], "NextToken": str},
    total=False,
)


class ListDeploymentGroupsPaginateResponseTypeDef(
    _ListDeploymentGroupsPaginateResponseTypeDef
):
    """
    Type definition for `ListDeploymentGroupsPaginate` `Response`

    Represents the output of a ListDeploymentGroups operation.

    - **applicationName** *(string) --*

      The application name.

    - **deploymentGroups** *(list) --*

      A list of deployment group names.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListDeploymentInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDeploymentInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListDeploymentInstancesPaginatePaginationConfigTypeDef(
    _ListDeploymentInstancesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDeploymentInstancesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListDeploymentInstancesPaginateResponseTypeDef = TypedDict(
    "_ListDeploymentInstancesPaginateResponseTypeDef",
    {"instancesList": List[str], "NextToken": str},
    total=False,
)


class ListDeploymentInstancesPaginateResponseTypeDef(
    _ListDeploymentInstancesPaginateResponseTypeDef
):
    """
    Type definition for `ListDeploymentInstancesPaginate` `Response`

    Represents the output of a ListDeploymentInstances operation.

    - **instancesList** *(list) --*

      A list of instance IDs.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListDeploymentTargetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDeploymentTargetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListDeploymentTargetsPaginatePaginationConfigTypeDef(
    _ListDeploymentTargetsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDeploymentTargetsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListDeploymentTargetsPaginateResponseTypeDef = TypedDict(
    "_ListDeploymentTargetsPaginateResponseTypeDef",
    {"targetIds": List[str], "NextToken": str},
    total=False,
)


class ListDeploymentTargetsPaginateResponseTypeDef(
    _ListDeploymentTargetsPaginateResponseTypeDef
):
    """
    Type definition for `ListDeploymentTargetsPaginate` `Response`

    - **targetIds** *(list) --*

      The unique IDs of deployment targets.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListDeploymentsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDeploymentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListDeploymentsPaginatePaginationConfigTypeDef(
    _ListDeploymentsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDeploymentsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListDeploymentsPaginateResponseTypeDef = TypedDict(
    "_ListDeploymentsPaginateResponseTypeDef",
    {"deployments": List[str], "NextToken": str},
    total=False,
)


class ListDeploymentsPaginateResponseTypeDef(_ListDeploymentsPaginateResponseTypeDef):
    """
    Type definition for `ListDeploymentsPaginate` `Response`

    Represents the output of a ListDeployments operation.

    - **deployments** *(list) --*

      A list of deployment IDs.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListDeploymentsPaginatecreateTimeRangeTypeDef = TypedDict(
    "_ListDeploymentsPaginatecreateTimeRangeTypeDef",
    {"start": datetime, "end": datetime},
    total=False,
)


class ListDeploymentsPaginatecreateTimeRangeTypeDef(
    _ListDeploymentsPaginatecreateTimeRangeTypeDef
):
    """
    Type definition for `ListDeploymentsPaginate` `createTimeRange`

    A time range (start and end) for returning a subset of the list of deployments.

    - **start** *(datetime) --*

      The start time of the time range.

      .. note::

        Specify null to leave the start time open-ended.

    - **end** *(datetime) --*

      The end time of the time range.

      .. note::

        Specify null to leave the end time open-ended.
    """


_ListGitHubAccountTokenNamesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListGitHubAccountTokenNamesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListGitHubAccountTokenNamesPaginatePaginationConfigTypeDef(
    _ListGitHubAccountTokenNamesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListGitHubAccountTokenNamesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListGitHubAccountTokenNamesPaginateResponseTypeDef = TypedDict(
    "_ListGitHubAccountTokenNamesPaginateResponseTypeDef",
    {"tokenNameList": List[str], "NextToken": str},
    total=False,
)


class ListGitHubAccountTokenNamesPaginateResponseTypeDef(
    _ListGitHubAccountTokenNamesPaginateResponseTypeDef
):
    """
    Type definition for `ListGitHubAccountTokenNamesPaginate` `Response`

    Represents the output of a ListGitHubAccountTokenNames operation.

    - **tokenNameList** *(list) --*

      A list of names of connections to GitHub accounts.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListOnPremisesInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListOnPremisesInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListOnPremisesInstancesPaginatePaginationConfigTypeDef(
    _ListOnPremisesInstancesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListOnPremisesInstancesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListOnPremisesInstancesPaginateResponseTypeDef = TypedDict(
    "_ListOnPremisesInstancesPaginateResponseTypeDef",
    {"instanceNames": List[str], "NextToken": str},
    total=False,
)


class ListOnPremisesInstancesPaginateResponseTypeDef(
    _ListOnPremisesInstancesPaginateResponseTypeDef
):
    """
    Type definition for `ListOnPremisesInstancesPaginate` `Response`

    Represents the output of the list on-premises instances operation.

    - **instanceNames** *(list) --*

      The list of matching on-premises instance names.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListOnPremisesInstancesPaginatetagFiltersTypeDef = TypedDict(
    "_ListOnPremisesInstancesPaginatetagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": str},
    total=False,
)


class ListOnPremisesInstancesPaginatetagFiltersTypeDef(
    _ListOnPremisesInstancesPaginatetagFiltersTypeDef
):
    """
    Type definition for `ListOnPremisesInstancesPaginate` `tagFilters`

    Information about an on-premises instance tag filter.

    - **Key** *(string) --*

      The on-premises instance tag filter key.

    - **Value** *(string) --*

      The on-premises instance tag filter value.

    - **Type** *(string) --*

      The on-premises instance tag filter type:

      * KEY_ONLY: Key only.

      * VALUE_ONLY: Value only.

      * KEY_AND_VALUE: Key and value.
    """
