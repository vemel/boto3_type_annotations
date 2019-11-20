"Main interface for config type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientBatchGetAggregateResourceConfigResourceIdentifiersTypeDef",
    "ClientBatchGetAggregateResourceConfigResponseBaseConfigurationItemsTypeDef",
    "ClientBatchGetAggregateResourceConfigResponseUnprocessedResourceIdentifiersTypeDef",
    "ClientBatchGetAggregateResourceConfigResponseTypeDef",
    "ClientBatchGetResourceConfigResponsebaseConfigurationItemsTypeDef",
    "ClientBatchGetResourceConfigResponseunprocessedResourceKeysTypeDef",
    "ClientBatchGetResourceConfigResponseTypeDef",
    "ClientBatchGetResourceConfigresourceKeysTypeDef",
    "ClientDeleteRemediationExceptionsResourceKeysTypeDef",
    "ClientDeleteRemediationExceptionsResponseFailedBatchesFailedItemsTypeDef",
    "ClientDeleteRemediationExceptionsResponseFailedBatchesTypeDef",
    "ClientDeleteRemediationExceptionsResponseTypeDef",
    "ClientDeliverConfigSnapshotResponseTypeDef",
    "ClientDescribeAggregateComplianceByConfigRulesFiltersTypeDef",
    "ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesComplianceComplianceContributorCountTypeDef",
    "ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesComplianceTypeDef",
    "ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesTypeDef",
    "ClientDescribeAggregateComplianceByConfigRulesResponseTypeDef",
    "ClientDescribeAggregationAuthorizationsResponseAggregationAuthorizationsTypeDef",
    "ClientDescribeAggregationAuthorizationsResponseTypeDef",
    "ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesComplianceComplianceContributorCountTypeDef",
    "ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesComplianceTypeDef",
    "ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesTypeDef",
    "ClientDescribeComplianceByConfigRuleResponseTypeDef",
    "ClientDescribeComplianceByResourceResponseComplianceByResourcesComplianceComplianceContributorCountTypeDef",
    "ClientDescribeComplianceByResourceResponseComplianceByResourcesComplianceTypeDef",
    "ClientDescribeComplianceByResourceResponseComplianceByResourcesTypeDef",
    "ClientDescribeComplianceByResourceResponseTypeDef",
    "ClientDescribeConfigRuleEvaluationStatusResponseConfigRulesEvaluationStatusTypeDef",
    "ClientDescribeConfigRuleEvaluationStatusResponseTypeDef",
    "ClientDescribeConfigRulesResponseConfigRulesScopeTypeDef",
    "ClientDescribeConfigRulesResponseConfigRulesSourceSourceDetailsTypeDef",
    "ClientDescribeConfigRulesResponseConfigRulesSourceTypeDef",
    "ClientDescribeConfigRulesResponseConfigRulesTypeDef",
    "ClientDescribeConfigRulesResponseTypeDef",
    "ClientDescribeConfigurationAggregatorSourcesStatusResponseAggregatedSourceStatusListTypeDef",
    "ClientDescribeConfigurationAggregatorSourcesStatusResponseTypeDef",
    "ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsAccountAggregationSourcesTypeDef",
    "ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsOrganizationAggregationSourceTypeDef",
    "ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsTypeDef",
    "ClientDescribeConfigurationAggregatorsResponseTypeDef",
    "ClientDescribeConfigurationRecorderStatusResponseConfigurationRecordersStatusTypeDef",
    "ClientDescribeConfigurationRecorderStatusResponseTypeDef",
    "ClientDescribeConfigurationRecordersResponseConfigurationRecordersrecordingGroupTypeDef",
    "ClientDescribeConfigurationRecordersResponseConfigurationRecordersTypeDef",
    "ClientDescribeConfigurationRecordersResponseTypeDef",
    "ClientDescribeConformancePackComplianceFiltersTypeDef",
    "ClientDescribeConformancePackComplianceResponseConformancePackRuleComplianceListTypeDef",
    "ClientDescribeConformancePackComplianceResponseTypeDef",
    "ClientDescribeConformancePackStatusResponseConformancePackStatusDetailsTypeDef",
    "ClientDescribeConformancePackStatusResponseTypeDef",
    "ClientDescribeConformancePacksResponseConformancePackDetailsConformancePackInputParametersTypeDef",
    "ClientDescribeConformancePacksResponseConformancePackDetailsTypeDef",
    "ClientDescribeConformancePacksResponseTypeDef",
    "ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigHistoryDeliveryInfoTypeDef",
    "ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigSnapshotDeliveryInfoTypeDef",
    "ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigStreamDeliveryInfoTypeDef",
    "ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusTypeDef",
    "ClientDescribeDeliveryChannelStatusResponseTypeDef",
    "ClientDescribeDeliveryChannelsResponseDeliveryChannelsconfigSnapshotDeliveryPropertiesTypeDef",
    "ClientDescribeDeliveryChannelsResponseDeliveryChannelsTypeDef",
    "ClientDescribeDeliveryChannelsResponseTypeDef",
    "ClientDescribeOrganizationConfigRuleStatusesResponseOrganizationConfigRuleStatusesTypeDef",
    "ClientDescribeOrganizationConfigRuleStatusesResponseTypeDef",
    "ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesOrganizationCustomRuleMetadataTypeDef",
    "ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesOrganizationManagedRuleMetadataTypeDef",
    "ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesTypeDef",
    "ClientDescribeOrganizationConfigRulesResponseTypeDef",
    "ClientDescribeOrganizationConformancePackStatusesResponseOrganizationConformancePackStatusesTypeDef",
    "ClientDescribeOrganizationConformancePackStatusesResponseTypeDef",
    "ClientDescribeOrganizationConformancePacksResponseOrganizationConformancePacksConformancePackInputParametersTypeDef",
    "ClientDescribeOrganizationConformancePacksResponseOrganizationConformancePacksTypeDef",
    "ClientDescribeOrganizationConformancePacksResponseTypeDef",
    "ClientDescribePendingAggregationRequestsResponsePendingAggregationRequestsTypeDef",
    "ClientDescribePendingAggregationRequestsResponseTypeDef",
    "ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsExecutionControlsSsmControlsTypeDef",
    "ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsExecutionControlsTypeDef",
    "ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersResourceValueTypeDef",
    "ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersStaticValueTypeDef",
    "ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersTypeDef",
    "ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsTypeDef",
    "ClientDescribeRemediationConfigurationsResponseTypeDef",
    "ClientDescribeRemediationExceptionsResourceKeysTypeDef",
    "ClientDescribeRemediationExceptionsResponseRemediationExceptionsTypeDef",
    "ClientDescribeRemediationExceptionsResponseTypeDef",
    "ClientDescribeRemediationExecutionStatusResourceKeysTypeDef",
    "ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesResourceKeyTypeDef",
    "ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesStepDetailsTypeDef",
    "ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesTypeDef",
    "ClientDescribeRemediationExecutionStatusResponseTypeDef",
    "ClientDescribeRetentionConfigurationsResponseRetentionConfigurationsTypeDef",
    "ClientDescribeRetentionConfigurationsResponseTypeDef",
    "ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    "ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsEvaluationResultIdentifierTypeDef",
    "ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsTypeDef",
    "ClientGetAggregateComplianceDetailsByConfigRuleResponseTypeDef",
    "ClientGetAggregateConfigRuleComplianceSummaryFiltersTypeDef",
    "ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryCompliantResourceCountTypeDef",
    "ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryNonCompliantResourceCountTypeDef",
    "ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryTypeDef",
    "ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsTypeDef",
    "ClientGetAggregateConfigRuleComplianceSummaryResponseTypeDef",
    "ClientGetAggregateDiscoveredResourceCountsFiltersTypeDef",
    "ClientGetAggregateDiscoveredResourceCountsResponseGroupedResourceCountsTypeDef",
    "ClientGetAggregateDiscoveredResourceCountsResponseTypeDef",
    "ClientGetAggregateResourceConfigResourceIdentifierTypeDef",
    "ClientGetAggregateResourceConfigResponseConfigurationItemrelationshipsTypeDef",
    "ClientGetAggregateResourceConfigResponseConfigurationItemTypeDef",
    "ClientGetAggregateResourceConfigResponseTypeDef",
    "ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    "ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsEvaluationResultIdentifierTypeDef",
    "ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsTypeDef",
    "ClientGetComplianceDetailsByConfigRuleResponseTypeDef",
    "ClientGetComplianceDetailsByResourceResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    "ClientGetComplianceDetailsByResourceResponseEvaluationResultsEvaluationResultIdentifierTypeDef",
    "ClientGetComplianceDetailsByResourceResponseEvaluationResultsTypeDef",
    "ClientGetComplianceDetailsByResourceResponseTypeDef",
    "ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryCompliantResourceCountTypeDef",
    "ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryNonCompliantResourceCountTypeDef",
    "ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryTypeDef",
    "ClientGetComplianceSummaryByConfigRuleResponseTypeDef",
    "ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryCompliantResourceCountTypeDef",
    "ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryNonCompliantResourceCountTypeDef",
    "ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryTypeDef",
    "ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeTypeDef",
    "ClientGetComplianceSummaryByResourceTypeResponseTypeDef",
    "ClientGetConformancePackComplianceDetailsFiltersTypeDef",
    "ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    "ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsEvaluationResultIdentifierTypeDef",
    "ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsTypeDef",
    "ClientGetConformancePackComplianceDetailsResponseTypeDef",
    "ClientGetConformancePackComplianceSummaryResponseConformancePackComplianceSummaryListTypeDef",
    "ClientGetConformancePackComplianceSummaryResponseTypeDef",
    "ClientGetDiscoveredResourceCountsResponseresourceCountsTypeDef",
    "ClientGetDiscoveredResourceCountsResponseTypeDef",
    "ClientGetOrganizationConfigRuleDetailedStatusFiltersTypeDef",
    "ClientGetOrganizationConfigRuleDetailedStatusResponseOrganizationConfigRuleDetailedStatusTypeDef",
    "ClientGetOrganizationConfigRuleDetailedStatusResponseTypeDef",
    "ClientGetOrganizationConformancePackDetailedStatusFiltersTypeDef",
    "ClientGetOrganizationConformancePackDetailedStatusResponseOrganizationConformancePackDetailedStatusesTypeDef",
    "ClientGetOrganizationConformancePackDetailedStatusResponseTypeDef",
    "ClientGetResourceConfigHistoryResponseconfigurationItemsrelationshipsTypeDef",
    "ClientGetResourceConfigHistoryResponseconfigurationItemsTypeDef",
    "ClientGetResourceConfigHistoryResponseTypeDef",
    "ClientListAggregateDiscoveredResourcesFiltersTypeDef",
    "ClientListAggregateDiscoveredResourcesResponseResourceIdentifiersTypeDef",
    "ClientListAggregateDiscoveredResourcesResponseTypeDef",
    "ClientListDiscoveredResourcesResponseresourceIdentifiersTypeDef",
    "ClientListDiscoveredResourcesResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutAggregationAuthorizationResponseAggregationAuthorizationTypeDef",
    "ClientPutAggregationAuthorizationResponseTypeDef",
    "ClientPutAggregationAuthorizationTagsTypeDef",
    "ClientPutConfigRuleConfigRuleScopeTypeDef",
    "ClientPutConfigRuleConfigRuleSourceSourceDetailsTypeDef",
    "ClientPutConfigRuleConfigRuleSourceTypeDef",
    "ClientPutConfigRuleConfigRuleTypeDef",
    "ClientPutConfigRuleTagsTypeDef",
    "ClientPutConfigurationAggregatorAccountAggregationSourcesTypeDef",
    "ClientPutConfigurationAggregatorOrganizationAggregationSourceTypeDef",
    "ClientPutConfigurationAggregatorResponseConfigurationAggregatorAccountAggregationSourcesTypeDef",
    "ClientPutConfigurationAggregatorResponseConfigurationAggregatorOrganizationAggregationSourceTypeDef",
    "ClientPutConfigurationAggregatorResponseConfigurationAggregatorTypeDef",
    "ClientPutConfigurationAggregatorResponseTypeDef",
    "ClientPutConfigurationAggregatorTagsTypeDef",
    "ClientPutConfigurationRecorderConfigurationRecorderrecordingGroupTypeDef",
    "ClientPutConfigurationRecorderConfigurationRecorderTypeDef",
    "ClientPutConformancePackConformancePackInputParametersTypeDef",
    "ClientPutConformancePackResponseTypeDef",
    "ClientPutDeliveryChannelDeliveryChannelconfigSnapshotDeliveryPropertiesTypeDef",
    "ClientPutDeliveryChannelDeliveryChannelTypeDef",
    "ClientPutEvaluationsEvaluationsTypeDef",
    "ClientPutEvaluationsResponseFailedEvaluationsTypeDef",
    "ClientPutEvaluationsResponseTypeDef",
    "ClientPutOrganizationConfigRuleOrganizationCustomRuleMetadataTypeDef",
    "ClientPutOrganizationConfigRuleOrganizationManagedRuleMetadataTypeDef",
    "ClientPutOrganizationConfigRuleResponseTypeDef",
    "ClientPutOrganizationConformancePackConformancePackInputParametersTypeDef",
    "ClientPutOrganizationConformancePackResponseTypeDef",
    "ClientPutRemediationConfigurationsRemediationConfigurationsExecutionControlsSsmControlsTypeDef",
    "ClientPutRemediationConfigurationsRemediationConfigurationsExecutionControlsTypeDef",
    "ClientPutRemediationConfigurationsRemediationConfigurationsParametersResourceValueTypeDef",
    "ClientPutRemediationConfigurationsRemediationConfigurationsParametersStaticValueTypeDef",
    "ClientPutRemediationConfigurationsRemediationConfigurationsParametersTypeDef",
    "ClientPutRemediationConfigurationsRemediationConfigurationsTypeDef",
    "ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsExecutionControlsSsmControlsTypeDef",
    "ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsExecutionControlsTypeDef",
    "ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersResourceValueTypeDef",
    "ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersStaticValueTypeDef",
    "ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersTypeDef",
    "ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsTypeDef",
    "ClientPutRemediationConfigurationsResponseFailedBatchesTypeDef",
    "ClientPutRemediationConfigurationsResponseTypeDef",
    "ClientPutRemediationExceptionsResourceKeysTypeDef",
    "ClientPutRemediationExceptionsResponseFailedBatchesFailedItemsTypeDef",
    "ClientPutRemediationExceptionsResponseFailedBatchesTypeDef",
    "ClientPutRemediationExceptionsResponseTypeDef",
    "ClientPutRetentionConfigurationResponseRetentionConfigurationTypeDef",
    "ClientPutRetentionConfigurationResponseTypeDef",
    "ClientSelectResourceConfigResponseQueryInfoSelectFieldsTypeDef",
    "ClientSelectResourceConfigResponseQueryInfoTypeDef",
    "ClientSelectResourceConfigResponseTypeDef",
    "ClientStartRemediationExecutionResourceKeysTypeDef",
    "ClientStartRemediationExecutionResponseFailedItemsTypeDef",
    "ClientStartRemediationExecutionResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "DescribeAggregateComplianceByConfigRulesPaginateFiltersTypeDef",
    "DescribeAggregateComplianceByConfigRulesPaginatePaginationConfigTypeDef",
    "DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesComplianceComplianceContributorCountTypeDef",
    "DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesComplianceTypeDef",
    "DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesTypeDef",
    "DescribeAggregateComplianceByConfigRulesPaginateResponseTypeDef",
    "DescribeAggregationAuthorizationsPaginatePaginationConfigTypeDef",
    "DescribeAggregationAuthorizationsPaginateResponseAggregationAuthorizationsTypeDef",
    "DescribeAggregationAuthorizationsPaginateResponseTypeDef",
    "DescribeComplianceByConfigRulePaginatePaginationConfigTypeDef",
    "DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesComplianceComplianceContributorCountTypeDef",
    "DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesComplianceTypeDef",
    "DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesTypeDef",
    "DescribeComplianceByConfigRulePaginateResponseTypeDef",
    "DescribeComplianceByResourcePaginatePaginationConfigTypeDef",
    "DescribeComplianceByResourcePaginateResponseComplianceByResourcesComplianceComplianceContributorCountTypeDef",
    "DescribeComplianceByResourcePaginateResponseComplianceByResourcesComplianceTypeDef",
    "DescribeComplianceByResourcePaginateResponseComplianceByResourcesTypeDef",
    "DescribeComplianceByResourcePaginateResponseTypeDef",
    "DescribeConfigRuleEvaluationStatusPaginatePaginationConfigTypeDef",
    "DescribeConfigRuleEvaluationStatusPaginateResponseConfigRulesEvaluationStatusTypeDef",
    "DescribeConfigRuleEvaluationStatusPaginateResponseTypeDef",
    "DescribeConfigRulesPaginatePaginationConfigTypeDef",
    "DescribeConfigRulesPaginateResponseConfigRulesScopeTypeDef",
    "DescribeConfigRulesPaginateResponseConfigRulesSourceSourceDetailsTypeDef",
    "DescribeConfigRulesPaginateResponseConfigRulesSourceTypeDef",
    "DescribeConfigRulesPaginateResponseConfigRulesTypeDef",
    "DescribeConfigRulesPaginateResponseTypeDef",
    "DescribeConfigurationAggregatorSourcesStatusPaginatePaginationConfigTypeDef",
    "DescribeConfigurationAggregatorSourcesStatusPaginateResponseAggregatedSourceStatusListTypeDef",
    "DescribeConfigurationAggregatorSourcesStatusPaginateResponseTypeDef",
    "DescribeConfigurationAggregatorsPaginatePaginationConfigTypeDef",
    "DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsAccountAggregationSourcesTypeDef",
    "DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsOrganizationAggregationSourceTypeDef",
    "DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsTypeDef",
    "DescribeConfigurationAggregatorsPaginateResponseTypeDef",
    "DescribePendingAggregationRequestsPaginatePaginationConfigTypeDef",
    "DescribePendingAggregationRequestsPaginateResponsePendingAggregationRequestsTypeDef",
    "DescribePendingAggregationRequestsPaginateResponseTypeDef",
    "DescribeRemediationExecutionStatusPaginatePaginationConfigTypeDef",
    "DescribeRemediationExecutionStatusPaginateResourceKeysTypeDef",
    "DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesResourceKeyTypeDef",
    "DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesStepDetailsTypeDef",
    "DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesTypeDef",
    "DescribeRemediationExecutionStatusPaginateResponseTypeDef",
    "DescribeRetentionConfigurationsPaginatePaginationConfigTypeDef",
    "DescribeRetentionConfigurationsPaginateResponseRetentionConfigurationsTypeDef",
    "DescribeRetentionConfigurationsPaginateResponseTypeDef",
    "GetAggregateComplianceDetailsByConfigRulePaginatePaginationConfigTypeDef",
    "GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    "GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsEvaluationResultIdentifierTypeDef",
    "GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsTypeDef",
    "GetAggregateComplianceDetailsByConfigRulePaginateResponseTypeDef",
    "GetComplianceDetailsByConfigRulePaginatePaginationConfigTypeDef",
    "GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    "GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsEvaluationResultIdentifierTypeDef",
    "GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsTypeDef",
    "GetComplianceDetailsByConfigRulePaginateResponseTypeDef",
    "GetComplianceDetailsByResourcePaginatePaginationConfigTypeDef",
    "GetComplianceDetailsByResourcePaginateResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    "GetComplianceDetailsByResourcePaginateResponseEvaluationResultsEvaluationResultIdentifierTypeDef",
    "GetComplianceDetailsByResourcePaginateResponseEvaluationResultsTypeDef",
    "GetComplianceDetailsByResourcePaginateResponseTypeDef",
    "GetResourceConfigHistoryPaginatePaginationConfigTypeDef",
    "GetResourceConfigHistoryPaginateResponseconfigurationItemsrelationshipsTypeDef",
    "GetResourceConfigHistoryPaginateResponseconfigurationItemsTypeDef",
    "GetResourceConfigHistoryPaginateResponseTypeDef",
    "ListAggregateDiscoveredResourcesPaginateFiltersTypeDef",
    "ListAggregateDiscoveredResourcesPaginatePaginationConfigTypeDef",
    "ListAggregateDiscoveredResourcesPaginateResponseResourceIdentifiersTypeDef",
    "ListAggregateDiscoveredResourcesPaginateResponseTypeDef",
    "ListDiscoveredResourcesPaginatePaginationConfigTypeDef",
    "ListDiscoveredResourcesPaginateResponseresourceIdentifiersTypeDef",
    "ListDiscoveredResourcesPaginateResponseTypeDef",
)


_RequiredClientBatchGetAggregateResourceConfigResourceIdentifiersTypeDef = TypedDict(
    "_RequiredClientBatchGetAggregateResourceConfigResourceIdentifiersTypeDef",
    {
        "SourceAccountId": str,
        "SourceRegion": str,
        "ResourceId": str,
        "ResourceType": str,
    },
)
_OptionalClientBatchGetAggregateResourceConfigResourceIdentifiersTypeDef = TypedDict(
    "_OptionalClientBatchGetAggregateResourceConfigResourceIdentifiersTypeDef",
    {"ResourceName": str},
    total=False,
)


class ClientBatchGetAggregateResourceConfigResourceIdentifiersTypeDef(
    _RequiredClientBatchGetAggregateResourceConfigResourceIdentifiersTypeDef,
    _OptionalClientBatchGetAggregateResourceConfigResourceIdentifiersTypeDef,
):
    """
    Type definition for `ClientBatchGetAggregateResourceConfig` `ResourceIdentifiers`

    The details that identify a resource that is collected by AWS Config aggregator, including the
    resource type, ID, (if available) the custom resource name, the source account, and source
    region.

    - **SourceAccountId** *(string) --* **[REQUIRED]**

      The 12-digit account ID of the source account.

    - **SourceRegion** *(string) --* **[REQUIRED]**

      The source region where data is aggregated.

    - **ResourceId** *(string) --* **[REQUIRED]**

      The ID of the AWS resource.

    - **ResourceType** *(string) --* **[REQUIRED]**

      The type of the AWS resource.

    - **ResourceName** *(string) --*

      The name of the AWS resource.
    """


_ClientBatchGetAggregateResourceConfigResponseBaseConfigurationItemsTypeDef = TypedDict(
    "_ClientBatchGetAggregateResourceConfigResponseBaseConfigurationItemsTypeDef",
    {
        "version": str,
        "accountId": str,
        "configurationItemCaptureTime": datetime,
        "configurationItemStatus": str,
        "configurationStateId": str,
        "arn": str,
        "resourceType": str,
        "resourceId": str,
        "resourceName": str,
        "awsRegion": str,
        "availabilityZone": str,
        "resourceCreationTime": datetime,
        "configuration": str,
        "supplementaryConfiguration": Dict[str, str],
    },
    total=False,
)


class ClientBatchGetAggregateResourceConfigResponseBaseConfigurationItemsTypeDef(
    _ClientBatchGetAggregateResourceConfigResponseBaseConfigurationItemsTypeDef
):
    """
    Type definition for `ClientBatchGetAggregateResourceConfigResponse` `BaseConfigurationItems`

    The detailed configuration of a specified resource.

    - **version** *(string) --*

      The version number of the resource configuration.

    - **accountId** *(string) --*

      The 12-digit AWS account ID associated with the resource.

    - **configurationItemCaptureTime** *(datetime) --*

      The time when the configuration recording was initiated.

    - **configurationItemStatus** *(string) --*

      The configuration item status.

    - **configurationStateId** *(string) --*

      An identifier that indicates the ordering of the configuration items of a resource.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the resource.

    - **resourceType** *(string) --*

      The type of AWS resource.

    - **resourceId** *(string) --*

      The ID of the resource (for example., sg-xxxxxx).

    - **resourceName** *(string) --*

      The custom name of the resource, if available.

    - **awsRegion** *(string) --*

      The region where the resource resides.

    - **availabilityZone** *(string) --*

      The Availability Zone associated with the resource.

    - **resourceCreationTime** *(datetime) --*

      The time stamp when the resource was created.

    - **configuration** *(string) --*

      The description of the resource configuration.

    - **supplementaryConfiguration** *(dict) --*

      Configuration attributes that AWS Config returns for certain resource types to supplement
      the information returned for the configuration parameter.

      - *(string) --*

        - *(string) --*
    """


_ClientBatchGetAggregateResourceConfigResponseUnprocessedResourceIdentifiersTypeDef = TypedDict(
    "_ClientBatchGetAggregateResourceConfigResponseUnprocessedResourceIdentifiersTypeDef",
    {
        "SourceAccountId": str,
        "SourceRegion": str,
        "ResourceId": str,
        "ResourceType": str,
        "ResourceName": str,
    },
    total=False,
)


class ClientBatchGetAggregateResourceConfigResponseUnprocessedResourceIdentifiersTypeDef(
    _ClientBatchGetAggregateResourceConfigResponseUnprocessedResourceIdentifiersTypeDef
):
    """
    Type definition for `ClientBatchGetAggregateResourceConfigResponse` `UnprocessedResourceIdentifiers`

    The details that identify a resource that is collected by AWS Config aggregator, including
    the resource type, ID, (if available) the custom resource name, the source account, and
    source region.

    - **SourceAccountId** *(string) --*

      The 12-digit account ID of the source account.

    - **SourceRegion** *(string) --*

      The source region where data is aggregated.

    - **ResourceId** *(string) --*

      The ID of the AWS resource.

    - **ResourceType** *(string) --*

      The type of the AWS resource.

    - **ResourceName** *(string) --*

      The name of the AWS resource.
    """


_ClientBatchGetAggregateResourceConfigResponseTypeDef = TypedDict(
    "_ClientBatchGetAggregateResourceConfigResponseTypeDef",
    {
        "BaseConfigurationItems": List[
            ClientBatchGetAggregateResourceConfigResponseBaseConfigurationItemsTypeDef
        ],
        "UnprocessedResourceIdentifiers": List[
            ClientBatchGetAggregateResourceConfigResponseUnprocessedResourceIdentifiersTypeDef
        ],
    },
    total=False,
)


class ClientBatchGetAggregateResourceConfigResponseTypeDef(
    _ClientBatchGetAggregateResourceConfigResponseTypeDef
):
    """
    Type definition for `ClientBatchGetAggregateResourceConfig` `Response`

    - **BaseConfigurationItems** *(list) --*

      A list that contains the current configuration of one or more resources.

      - *(dict) --*

        The detailed configuration of a specified resource.

        - **version** *(string) --*

          The version number of the resource configuration.

        - **accountId** *(string) --*

          The 12-digit AWS account ID associated with the resource.

        - **configurationItemCaptureTime** *(datetime) --*

          The time when the configuration recording was initiated.

        - **configurationItemStatus** *(string) --*

          The configuration item status.

        - **configurationStateId** *(string) --*

          An identifier that indicates the ordering of the configuration items of a resource.

        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the resource.

        - **resourceType** *(string) --*

          The type of AWS resource.

        - **resourceId** *(string) --*

          The ID of the resource (for example., sg-xxxxxx).

        - **resourceName** *(string) --*

          The custom name of the resource, if available.

        - **awsRegion** *(string) --*

          The region where the resource resides.

        - **availabilityZone** *(string) --*

          The Availability Zone associated with the resource.

        - **resourceCreationTime** *(datetime) --*

          The time stamp when the resource was created.

        - **configuration** *(string) --*

          The description of the resource configuration.

        - **supplementaryConfiguration** *(dict) --*

          Configuration attributes that AWS Config returns for certain resource types to supplement
          the information returned for the configuration parameter.

          - *(string) --*

            - *(string) --*

    - **UnprocessedResourceIdentifiers** *(list) --*

      A list of resource identifiers that were not processed with current scope. The list is empty
      if all the resources are processed.

      - *(dict) --*

        The details that identify a resource that is collected by AWS Config aggregator, including
        the resource type, ID, (if available) the custom resource name, the source account, and
        source region.

        - **SourceAccountId** *(string) --*

          The 12-digit account ID of the source account.

        - **SourceRegion** *(string) --*

          The source region where data is aggregated.

        - **ResourceId** *(string) --*

          The ID of the AWS resource.

        - **ResourceType** *(string) --*

          The type of the AWS resource.

        - **ResourceName** *(string) --*

          The name of the AWS resource.
    """


_ClientBatchGetResourceConfigResponsebaseConfigurationItemsTypeDef = TypedDict(
    "_ClientBatchGetResourceConfigResponsebaseConfigurationItemsTypeDef",
    {
        "version": str,
        "accountId": str,
        "configurationItemCaptureTime": datetime,
        "configurationItemStatus": str,
        "configurationStateId": str,
        "arn": str,
        "resourceType": str,
        "resourceId": str,
        "resourceName": str,
        "awsRegion": str,
        "availabilityZone": str,
        "resourceCreationTime": datetime,
        "configuration": str,
        "supplementaryConfiguration": Dict[str, str],
    },
    total=False,
)


class ClientBatchGetResourceConfigResponsebaseConfigurationItemsTypeDef(
    _ClientBatchGetResourceConfigResponsebaseConfigurationItemsTypeDef
):
    """
    Type definition for `ClientBatchGetResourceConfigResponse` `baseConfigurationItems`

    The detailed configuration of a specified resource.

    - **version** *(string) --*

      The version number of the resource configuration.

    - **accountId** *(string) --*

      The 12-digit AWS account ID associated with the resource.

    - **configurationItemCaptureTime** *(datetime) --*

      The time when the configuration recording was initiated.

    - **configurationItemStatus** *(string) --*

      The configuration item status.

    - **configurationStateId** *(string) --*

      An identifier that indicates the ordering of the configuration items of a resource.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the resource.

    - **resourceType** *(string) --*

      The type of AWS resource.

    - **resourceId** *(string) --*

      The ID of the resource (for example., sg-xxxxxx).

    - **resourceName** *(string) --*

      The custom name of the resource, if available.

    - **awsRegion** *(string) --*

      The region where the resource resides.

    - **availabilityZone** *(string) --*

      The Availability Zone associated with the resource.

    - **resourceCreationTime** *(datetime) --*

      The time stamp when the resource was created.

    - **configuration** *(string) --*

      The description of the resource configuration.

    - **supplementaryConfiguration** *(dict) --*

      Configuration attributes that AWS Config returns for certain resource types to supplement
      the information returned for the configuration parameter.

      - *(string) --*

        - *(string) --*
    """


_ClientBatchGetResourceConfigResponseunprocessedResourceKeysTypeDef = TypedDict(
    "_ClientBatchGetResourceConfigResponseunprocessedResourceKeysTypeDef",
    {"resourceType": str, "resourceId": str},
    total=False,
)


class ClientBatchGetResourceConfigResponseunprocessedResourceKeysTypeDef(
    _ClientBatchGetResourceConfigResponseunprocessedResourceKeysTypeDef
):
    """
    Type definition for `ClientBatchGetResourceConfigResponse` `unprocessedResourceKeys`

    The details that identify a resource within AWS Config, including the resource type and
    resource ID.

    - **resourceType** *(string) --*

      The resource type.

    - **resourceId** *(string) --*

      The ID of the resource (for example., sg-xxxxxx).
    """


_ClientBatchGetResourceConfigResponseTypeDef = TypedDict(
    "_ClientBatchGetResourceConfigResponseTypeDef",
    {
        "baseConfigurationItems": List[
            ClientBatchGetResourceConfigResponsebaseConfigurationItemsTypeDef
        ],
        "unprocessedResourceKeys": List[
            ClientBatchGetResourceConfigResponseunprocessedResourceKeysTypeDef
        ],
    },
    total=False,
)


class ClientBatchGetResourceConfigResponseTypeDef(
    _ClientBatchGetResourceConfigResponseTypeDef
):
    """
    Type definition for `ClientBatchGetResourceConfig` `Response`

    - **baseConfigurationItems** *(list) --*

      A list that contains the current configuration of one or more resources.

      - *(dict) --*

        The detailed configuration of a specified resource.

        - **version** *(string) --*

          The version number of the resource configuration.

        - **accountId** *(string) --*

          The 12-digit AWS account ID associated with the resource.

        - **configurationItemCaptureTime** *(datetime) --*

          The time when the configuration recording was initiated.

        - **configurationItemStatus** *(string) --*

          The configuration item status.

        - **configurationStateId** *(string) --*

          An identifier that indicates the ordering of the configuration items of a resource.

        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the resource.

        - **resourceType** *(string) --*

          The type of AWS resource.

        - **resourceId** *(string) --*

          The ID of the resource (for example., sg-xxxxxx).

        - **resourceName** *(string) --*

          The custom name of the resource, if available.

        - **awsRegion** *(string) --*

          The region where the resource resides.

        - **availabilityZone** *(string) --*

          The Availability Zone associated with the resource.

        - **resourceCreationTime** *(datetime) --*

          The time stamp when the resource was created.

        - **configuration** *(string) --*

          The description of the resource configuration.

        - **supplementaryConfiguration** *(dict) --*

          Configuration attributes that AWS Config returns for certain resource types to supplement
          the information returned for the configuration parameter.

          - *(string) --*

            - *(string) --*

    - **unprocessedResourceKeys** *(list) --*

      A list of resource keys that were not processed with the current response. The
      unprocessesResourceKeys value is in the same form as ResourceKeys, so the value can be
      directly provided to a subsequent BatchGetResourceConfig operation. If there are no
      unprocessed resource keys, the response contains an empty unprocessedResourceKeys list.

      - *(dict) --*

        The details that identify a resource within AWS Config, including the resource type and
        resource ID.

        - **resourceType** *(string) --*

          The resource type.

        - **resourceId** *(string) --*

          The ID of the resource (for example., sg-xxxxxx).
    """


_ClientBatchGetResourceConfigresourceKeysTypeDef = TypedDict(
    "_ClientBatchGetResourceConfigresourceKeysTypeDef",
    {"resourceType": str, "resourceId": str},
)


class ClientBatchGetResourceConfigresourceKeysTypeDef(
    _ClientBatchGetResourceConfigresourceKeysTypeDef
):
    """
    Type definition for `ClientBatchGetResourceConfig` `resourceKeys`

    The details that identify a resource within AWS Config, including the resource type and
    resource ID.

    - **resourceType** *(string) --* **[REQUIRED]**

      The resource type.

    - **resourceId** *(string) --* **[REQUIRED]**

      The ID of the resource (for example., sg-xxxxxx).
    """


_ClientDeleteRemediationExceptionsResourceKeysTypeDef = TypedDict(
    "_ClientDeleteRemediationExceptionsResourceKeysTypeDef",
    {"ResourceType": str, "ResourceId": str},
    total=False,
)


class ClientDeleteRemediationExceptionsResourceKeysTypeDef(
    _ClientDeleteRemediationExceptionsResourceKeysTypeDef
):
    """
    Type definition for `ClientDeleteRemediationExceptions` `ResourceKeys`

    The details that identify a resource within AWS Config, including the resource type and
    resource ID.

    - **ResourceType** *(string) --*

      The type of a resource.

    - **ResourceId** *(string) --*

      The ID of the resource (for example., sg-xxxxxx).
    """


_ClientDeleteRemediationExceptionsResponseFailedBatchesFailedItemsTypeDef = TypedDict(
    "_ClientDeleteRemediationExceptionsResponseFailedBatchesFailedItemsTypeDef",
    {"ResourceType": str, "ResourceId": str},
    total=False,
)


class ClientDeleteRemediationExceptionsResponseFailedBatchesFailedItemsTypeDef(
    _ClientDeleteRemediationExceptionsResponseFailedBatchesFailedItemsTypeDef
):
    """
    Type definition for `ClientDeleteRemediationExceptionsResponseFailedBatches` `FailedItems`

    The details that identify a resource within AWS Config, including the resource type and
    resource ID.

    - **ResourceType** *(string) --*

      The type of a resource.

    - **ResourceId** *(string) --*

      The ID of the resource (for example., sg-xxxxxx).
    """


_ClientDeleteRemediationExceptionsResponseFailedBatchesTypeDef = TypedDict(
    "_ClientDeleteRemediationExceptionsResponseFailedBatchesTypeDef",
    {
        "FailureMessage": str,
        "FailedItems": List[
            ClientDeleteRemediationExceptionsResponseFailedBatchesFailedItemsTypeDef
        ],
    },
    total=False,
)


class ClientDeleteRemediationExceptionsResponseFailedBatchesTypeDef(
    _ClientDeleteRemediationExceptionsResponseFailedBatchesTypeDef
):
    """
    Type definition for `ClientDeleteRemediationExceptionsResponse` `FailedBatches`

    List of each of the failed delete remediation exceptions with specific reasons.

    - **FailureMessage** *(string) --*

      Returns a failure message for delete remediation exception. For example, AWS Config
      creates an exception due to an internal error.

    - **FailedItems** *(list) --*

      Returns remediation exception resource key object of the failed items.

      - *(dict) --*

        The details that identify a resource within AWS Config, including the resource type and
        resource ID.

        - **ResourceType** *(string) --*

          The type of a resource.

        - **ResourceId** *(string) --*

          The ID of the resource (for example., sg-xxxxxx).
    """


_ClientDeleteRemediationExceptionsResponseTypeDef = TypedDict(
    "_ClientDeleteRemediationExceptionsResponseTypeDef",
    {
        "FailedBatches": List[
            ClientDeleteRemediationExceptionsResponseFailedBatchesTypeDef
        ]
    },
    total=False,
)


class ClientDeleteRemediationExceptionsResponseTypeDef(
    _ClientDeleteRemediationExceptionsResponseTypeDef
):
    """
    Type definition for `ClientDeleteRemediationExceptions` `Response`

    - **FailedBatches** *(list) --*

      Returns a list of failed delete remediation exceptions batch objects. Each object in the
      batch consists of a list of failed items and failure messages.

      - *(dict) --*

        List of each of the failed delete remediation exceptions with specific reasons.

        - **FailureMessage** *(string) --*

          Returns a failure message for delete remediation exception. For example, AWS Config
          creates an exception due to an internal error.

        - **FailedItems** *(list) --*

          Returns remediation exception resource key object of the failed items.

          - *(dict) --*

            The details that identify a resource within AWS Config, including the resource type and
            resource ID.

            - **ResourceType** *(string) --*

              The type of a resource.

            - **ResourceId** *(string) --*

              The ID of the resource (for example., sg-xxxxxx).
    """


_ClientDeliverConfigSnapshotResponseTypeDef = TypedDict(
    "_ClientDeliverConfigSnapshotResponseTypeDef",
    {"configSnapshotId": str},
    total=False,
)


class ClientDeliverConfigSnapshotResponseTypeDef(
    _ClientDeliverConfigSnapshotResponseTypeDef
):
    """
    Type definition for `ClientDeliverConfigSnapshot` `Response`

    The output for the  DeliverConfigSnapshot action, in JSON format.

    - **configSnapshotId** *(string) --*

      The ID of the snapshot that is being created.
    """


_ClientDescribeAggregateComplianceByConfigRulesFiltersTypeDef = TypedDict(
    "_ClientDescribeAggregateComplianceByConfigRulesFiltersTypeDef",
    {"ConfigRuleName": str, "ComplianceType": str, "AccountId": str, "AwsRegion": str},
    total=False,
)


class ClientDescribeAggregateComplianceByConfigRulesFiltersTypeDef(
    _ClientDescribeAggregateComplianceByConfigRulesFiltersTypeDef
):
    """
    Type definition for `ClientDescribeAggregateComplianceByConfigRules` `Filters`

    Filters the results by ConfigRuleComplianceFilters object.

    - **ConfigRuleName** *(string) --*

      The name of the AWS Config rule.

    - **ComplianceType** *(string) --*

      The rule compliance status.

      For the ``ConfigRuleComplianceFilters`` data type, AWS Config supports only ``COMPLIANT`` and
      ``NON_COMPLIANT`` . AWS Config does not support the ``NOT_APPLICABLE`` and the
      ``INSUFFICIENT_DATA`` values.

    - **AccountId** *(string) --*

      The 12-digit account ID of the source account.

    - **AwsRegion** *(string) --*

      The source region where the data is aggregated.
    """


_ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesComplianceComplianceContributorCountTypeDef = TypedDict(
    "_ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesComplianceComplianceContributorCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)


class ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesComplianceComplianceContributorCountTypeDef(
    _ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesComplianceComplianceContributorCountTypeDef
):
    """
    Type definition for `ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesCompliance` `ComplianceContributorCount`

    The number of AWS resources or AWS Config rules that cause a result of
    ``NON_COMPLIANT`` , up to a maximum number.

    - **CappedCount** *(integer) --*

      The number of AWS resources or AWS Config rules responsible for the current
      compliance of the item.

    - **CapExceeded** *(boolean) --*

      Indicates whether the maximum count is reached.
    """


_ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesComplianceTypeDef = TypedDict(
    "_ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesComplianceTypeDef",
    {
        "ComplianceType": str,
        "ComplianceContributorCount": ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesComplianceComplianceContributorCountTypeDef,
    },
    total=False,
)


class ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesComplianceTypeDef(
    _ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesComplianceTypeDef
):
    """
    Type definition for `ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRules` `Compliance`

    Indicates whether an AWS resource or AWS Config rule is compliant and provides the number
    of contributors that affect the compliance.

    - **ComplianceType** *(string) --*

      Indicates whether an AWS resource or AWS Config rule is compliant.

      A resource is compliant if it complies with all of the AWS Config rules that evaluate
      it. A resource is noncompliant if it does not comply with one or more of these rules.

      A rule is compliant if all of the resources that the rule evaluates comply with it. A
      rule is noncompliant if any of these resources do not comply.

      AWS Config returns the ``INSUFFICIENT_DATA`` value when no evaluation results are
      available for the AWS resource or AWS Config rule.

      For the ``Compliance`` data type, AWS Config supports only ``COMPLIANT`` ,
      ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` values. AWS Config does not support the
      ``NOT_APPLICABLE`` value for the ``Compliance`` data type.

    - **ComplianceContributorCount** *(dict) --*

      The number of AWS resources or AWS Config rules that cause a result of
      ``NON_COMPLIANT`` , up to a maximum number.

      - **CappedCount** *(integer) --*

        The number of AWS resources or AWS Config rules responsible for the current
        compliance of the item.

      - **CapExceeded** *(boolean) --*

        Indicates whether the maximum count is reached.
    """


_ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesTypeDef = TypedDict(
    "_ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesTypeDef",
    {
        "ConfigRuleName": str,
        "Compliance": ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesComplianceTypeDef,
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)


class ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesTypeDef(
    _ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesTypeDef
):
    """
    Type definition for `ClientDescribeAggregateComplianceByConfigRulesResponse` `AggregateComplianceByConfigRules`

    Indicates whether an AWS Config rule is compliant based on account ID, region, compliance,
    and rule name.

    A rule is compliant if all of the resources that the rule evaluated comply with it. It is
    noncompliant if any of these resources do not comply.

    - **ConfigRuleName** *(string) --*

      The name of the AWS Config rule.

    - **Compliance** *(dict) --*

      Indicates whether an AWS resource or AWS Config rule is compliant and provides the number
      of contributors that affect the compliance.

      - **ComplianceType** *(string) --*

        Indicates whether an AWS resource or AWS Config rule is compliant.

        A resource is compliant if it complies with all of the AWS Config rules that evaluate
        it. A resource is noncompliant if it does not comply with one or more of these rules.

        A rule is compliant if all of the resources that the rule evaluates comply with it. A
        rule is noncompliant if any of these resources do not comply.

        AWS Config returns the ``INSUFFICIENT_DATA`` value when no evaluation results are
        available for the AWS resource or AWS Config rule.

        For the ``Compliance`` data type, AWS Config supports only ``COMPLIANT`` ,
        ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` values. AWS Config does not support the
        ``NOT_APPLICABLE`` value for the ``Compliance`` data type.

      - **ComplianceContributorCount** *(dict) --*

        The number of AWS resources or AWS Config rules that cause a result of
        ``NON_COMPLIANT`` , up to a maximum number.

        - **CappedCount** *(integer) --*

          The number of AWS resources or AWS Config rules responsible for the current
          compliance of the item.

        - **CapExceeded** *(boolean) --*

          Indicates whether the maximum count is reached.

    - **AccountId** *(string) --*

      The 12-digit account ID of the source account.

    - **AwsRegion** *(string) --*

      The source region from where the data is aggregated.
    """


_ClientDescribeAggregateComplianceByConfigRulesResponseTypeDef = TypedDict(
    "_ClientDescribeAggregateComplianceByConfigRulesResponseTypeDef",
    {
        "AggregateComplianceByConfigRules": List[
            ClientDescribeAggregateComplianceByConfigRulesResponseAggregateComplianceByConfigRulesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeAggregateComplianceByConfigRulesResponseTypeDef(
    _ClientDescribeAggregateComplianceByConfigRulesResponseTypeDef
):
    """
    Type definition for `ClientDescribeAggregateComplianceByConfigRules` `Response`

    - **AggregateComplianceByConfigRules** *(list) --*

      Returns a list of AggregateComplianceByConfigRule object.

      - *(dict) --*

        Indicates whether an AWS Config rule is compliant based on account ID, region, compliance,
        and rule name.

        A rule is compliant if all of the resources that the rule evaluated comply with it. It is
        noncompliant if any of these resources do not comply.

        - **ConfigRuleName** *(string) --*

          The name of the AWS Config rule.

        - **Compliance** *(dict) --*

          Indicates whether an AWS resource or AWS Config rule is compliant and provides the number
          of contributors that affect the compliance.

          - **ComplianceType** *(string) --*

            Indicates whether an AWS resource or AWS Config rule is compliant.

            A resource is compliant if it complies with all of the AWS Config rules that evaluate
            it. A resource is noncompliant if it does not comply with one or more of these rules.

            A rule is compliant if all of the resources that the rule evaluates comply with it. A
            rule is noncompliant if any of these resources do not comply.

            AWS Config returns the ``INSUFFICIENT_DATA`` value when no evaluation results are
            available for the AWS resource or AWS Config rule.

            For the ``Compliance`` data type, AWS Config supports only ``COMPLIANT`` ,
            ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` values. AWS Config does not support the
            ``NOT_APPLICABLE`` value for the ``Compliance`` data type.

          - **ComplianceContributorCount** *(dict) --*

            The number of AWS resources or AWS Config rules that cause a result of
            ``NON_COMPLIANT`` , up to a maximum number.

            - **CappedCount** *(integer) --*

              The number of AWS resources or AWS Config rules responsible for the current
              compliance of the item.

            - **CapExceeded** *(boolean) --*

              Indicates whether the maximum count is reached.

        - **AccountId** *(string) --*

          The 12-digit account ID of the source account.

        - **AwsRegion** *(string) --*

          The source region from where the data is aggregated.

    - **NextToken** *(string) --*

      The ``nextToken`` string returned on a previous page that you use to get the next page of
      results in a paginated response.
    """


_ClientDescribeAggregationAuthorizationsResponseAggregationAuthorizationsTypeDef = TypedDict(
    "_ClientDescribeAggregationAuthorizationsResponseAggregationAuthorizationsTypeDef",
    {
        "AggregationAuthorizationArn": str,
        "AuthorizedAccountId": str,
        "AuthorizedAwsRegion": str,
        "CreationTime": datetime,
    },
    total=False,
)


class ClientDescribeAggregationAuthorizationsResponseAggregationAuthorizationsTypeDef(
    _ClientDescribeAggregationAuthorizationsResponseAggregationAuthorizationsTypeDef
):
    """
    Type definition for `ClientDescribeAggregationAuthorizationsResponse` `AggregationAuthorizations`

    An object that represents the authorizations granted to aggregator accounts and regions.

    - **AggregationAuthorizationArn** *(string) --*

      The Amazon Resource Name (ARN) of the aggregation object.

    - **AuthorizedAccountId** *(string) --*

      The 12-digit account ID of the account authorized to aggregate data.

    - **AuthorizedAwsRegion** *(string) --*

      The region authorized to collect aggregated data.

    - **CreationTime** *(datetime) --*

      The time stamp when the aggregation authorization was created.
    """


_ClientDescribeAggregationAuthorizationsResponseTypeDef = TypedDict(
    "_ClientDescribeAggregationAuthorizationsResponseTypeDef",
    {
        "AggregationAuthorizations": List[
            ClientDescribeAggregationAuthorizationsResponseAggregationAuthorizationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeAggregationAuthorizationsResponseTypeDef(
    _ClientDescribeAggregationAuthorizationsResponseTypeDef
):
    """
    Type definition for `ClientDescribeAggregationAuthorizations` `Response`

    - **AggregationAuthorizations** *(list) --*

      Returns a list of authorizations granted to various aggregator accounts and regions.

      - *(dict) --*

        An object that represents the authorizations granted to aggregator accounts and regions.

        - **AggregationAuthorizationArn** *(string) --*

          The Amazon Resource Name (ARN) of the aggregation object.

        - **AuthorizedAccountId** *(string) --*

          The 12-digit account ID of the account authorized to aggregate data.

        - **AuthorizedAwsRegion** *(string) --*

          The region authorized to collect aggregated data.

        - **CreationTime** *(datetime) --*

          The time stamp when the aggregation authorization was created.

    - **NextToken** *(string) --*

      The ``nextToken`` string returned on a previous page that you use to get the next page of
      results in a paginated response.
    """


_ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesComplianceComplianceContributorCountTypeDef = TypedDict(
    "_ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesComplianceComplianceContributorCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)


class ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesComplianceComplianceContributorCountTypeDef(
    _ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesComplianceComplianceContributorCountTypeDef
):
    """
    Type definition for `ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesCompliance` `ComplianceContributorCount`

    The number of AWS resources or AWS Config rules that cause a result of
    ``NON_COMPLIANT`` , up to a maximum number.

    - **CappedCount** *(integer) --*

      The number of AWS resources or AWS Config rules responsible for the current
      compliance of the item.

    - **CapExceeded** *(boolean) --*

      Indicates whether the maximum count is reached.
    """


_ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesComplianceTypeDef = TypedDict(
    "_ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesComplianceTypeDef",
    {
        "ComplianceType": str,
        "ComplianceContributorCount": ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesComplianceComplianceContributorCountTypeDef,
    },
    total=False,
)


class ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesComplianceTypeDef(
    _ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesComplianceTypeDef
):
    """
    Type definition for `ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRules` `Compliance`

    Indicates whether the AWS Config rule is compliant.

    - **ComplianceType** *(string) --*

      Indicates whether an AWS resource or AWS Config rule is compliant.

      A resource is compliant if it complies with all of the AWS Config rules that evaluate
      it. A resource is noncompliant if it does not comply with one or more of these rules.

      A rule is compliant if all of the resources that the rule evaluates comply with it. A
      rule is noncompliant if any of these resources do not comply.

      AWS Config returns the ``INSUFFICIENT_DATA`` value when no evaluation results are
      available for the AWS resource or AWS Config rule.

      For the ``Compliance`` data type, AWS Config supports only ``COMPLIANT`` ,
      ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` values. AWS Config does not support the
      ``NOT_APPLICABLE`` value for the ``Compliance`` data type.

    - **ComplianceContributorCount** *(dict) --*

      The number of AWS resources or AWS Config rules that cause a result of
      ``NON_COMPLIANT`` , up to a maximum number.

      - **CappedCount** *(integer) --*

        The number of AWS resources or AWS Config rules responsible for the current
        compliance of the item.

      - **CapExceeded** *(boolean) --*

        Indicates whether the maximum count is reached.
    """


_ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesTypeDef = TypedDict(
    "_ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesTypeDef",
    {
        "ConfigRuleName": str,
        "Compliance": ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesComplianceTypeDef,
    },
    total=False,
)


class ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesTypeDef(
    _ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesTypeDef
):
    """
    Type definition for `ClientDescribeComplianceByConfigRuleResponse` `ComplianceByConfigRules`

    Indicates whether an AWS Config rule is compliant. A rule is compliant if all of the
    resources that the rule evaluated comply with it. A rule is noncompliant if any of these
    resources do not comply.

    - **ConfigRuleName** *(string) --*

      The name of the AWS Config rule.

    - **Compliance** *(dict) --*

      Indicates whether the AWS Config rule is compliant.

      - **ComplianceType** *(string) --*

        Indicates whether an AWS resource or AWS Config rule is compliant.

        A resource is compliant if it complies with all of the AWS Config rules that evaluate
        it. A resource is noncompliant if it does not comply with one or more of these rules.

        A rule is compliant if all of the resources that the rule evaluates comply with it. A
        rule is noncompliant if any of these resources do not comply.

        AWS Config returns the ``INSUFFICIENT_DATA`` value when no evaluation results are
        available for the AWS resource or AWS Config rule.

        For the ``Compliance`` data type, AWS Config supports only ``COMPLIANT`` ,
        ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` values. AWS Config does not support the
        ``NOT_APPLICABLE`` value for the ``Compliance`` data type.

      - **ComplianceContributorCount** *(dict) --*

        The number of AWS resources or AWS Config rules that cause a result of
        ``NON_COMPLIANT`` , up to a maximum number.

        - **CappedCount** *(integer) --*

          The number of AWS resources or AWS Config rules responsible for the current
          compliance of the item.

        - **CapExceeded** *(boolean) --*

          Indicates whether the maximum count is reached.
    """


_ClientDescribeComplianceByConfigRuleResponseTypeDef = TypedDict(
    "_ClientDescribeComplianceByConfigRuleResponseTypeDef",
    {
        "ComplianceByConfigRules": List[
            ClientDescribeComplianceByConfigRuleResponseComplianceByConfigRulesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeComplianceByConfigRuleResponseTypeDef(
    _ClientDescribeComplianceByConfigRuleResponseTypeDef
):
    """
    Type definition for `ClientDescribeComplianceByConfigRule` `Response`

    - **ComplianceByConfigRules** *(list) --*

      Indicates whether each of the specified AWS Config rules is compliant.

      - *(dict) --*

        Indicates whether an AWS Config rule is compliant. A rule is compliant if all of the
        resources that the rule evaluated comply with it. A rule is noncompliant if any of these
        resources do not comply.

        - **ConfigRuleName** *(string) --*

          The name of the AWS Config rule.

        - **Compliance** *(dict) --*

          Indicates whether the AWS Config rule is compliant.

          - **ComplianceType** *(string) --*

            Indicates whether an AWS resource or AWS Config rule is compliant.

            A resource is compliant if it complies with all of the AWS Config rules that evaluate
            it. A resource is noncompliant if it does not comply with one or more of these rules.

            A rule is compliant if all of the resources that the rule evaluates comply with it. A
            rule is noncompliant if any of these resources do not comply.

            AWS Config returns the ``INSUFFICIENT_DATA`` value when no evaluation results are
            available for the AWS resource or AWS Config rule.

            For the ``Compliance`` data type, AWS Config supports only ``COMPLIANT`` ,
            ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` values. AWS Config does not support the
            ``NOT_APPLICABLE`` value for the ``Compliance`` data type.

          - **ComplianceContributorCount** *(dict) --*

            The number of AWS resources or AWS Config rules that cause a result of
            ``NON_COMPLIANT`` , up to a maximum number.

            - **CappedCount** *(integer) --*

              The number of AWS resources or AWS Config rules responsible for the current
              compliance of the item.

            - **CapExceeded** *(boolean) --*

              Indicates whether the maximum count is reached.

    - **NextToken** *(string) --*

      The string that you use in a subsequent request to get the next page of results in a
      paginated response.
    """


_ClientDescribeComplianceByResourceResponseComplianceByResourcesComplianceComplianceContributorCountTypeDef = TypedDict(
    "_ClientDescribeComplianceByResourceResponseComplianceByResourcesComplianceComplianceContributorCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)


class ClientDescribeComplianceByResourceResponseComplianceByResourcesComplianceComplianceContributorCountTypeDef(
    _ClientDescribeComplianceByResourceResponseComplianceByResourcesComplianceComplianceContributorCountTypeDef
):
    """
    Type definition for `ClientDescribeComplianceByResourceResponseComplianceByResourcesCompliance` `ComplianceContributorCount`

    The number of AWS resources or AWS Config rules that cause a result of
    ``NON_COMPLIANT`` , up to a maximum number.

    - **CappedCount** *(integer) --*

      The number of AWS resources or AWS Config rules responsible for the current
      compliance of the item.

    - **CapExceeded** *(boolean) --*

      Indicates whether the maximum count is reached.
    """


_ClientDescribeComplianceByResourceResponseComplianceByResourcesComplianceTypeDef = TypedDict(
    "_ClientDescribeComplianceByResourceResponseComplianceByResourcesComplianceTypeDef",
    {
        "ComplianceType": str,
        "ComplianceContributorCount": ClientDescribeComplianceByResourceResponseComplianceByResourcesComplianceComplianceContributorCountTypeDef,
    },
    total=False,
)


class ClientDescribeComplianceByResourceResponseComplianceByResourcesComplianceTypeDef(
    _ClientDescribeComplianceByResourceResponseComplianceByResourcesComplianceTypeDef
):
    """
    Type definition for `ClientDescribeComplianceByResourceResponseComplianceByResources` `Compliance`

    Indicates whether the AWS resource complies with all of the AWS Config rules that
    evaluated it.

    - **ComplianceType** *(string) --*

      Indicates whether an AWS resource or AWS Config rule is compliant.

      A resource is compliant if it complies with all of the AWS Config rules that evaluate
      it. A resource is noncompliant if it does not comply with one or more of these rules.

      A rule is compliant if all of the resources that the rule evaluates comply with it. A
      rule is noncompliant if any of these resources do not comply.

      AWS Config returns the ``INSUFFICIENT_DATA`` value when no evaluation results are
      available for the AWS resource or AWS Config rule.

      For the ``Compliance`` data type, AWS Config supports only ``COMPLIANT`` ,
      ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` values. AWS Config does not support the
      ``NOT_APPLICABLE`` value for the ``Compliance`` data type.

    - **ComplianceContributorCount** *(dict) --*

      The number of AWS resources or AWS Config rules that cause a result of
      ``NON_COMPLIANT`` , up to a maximum number.

      - **CappedCount** *(integer) --*

        The number of AWS resources or AWS Config rules responsible for the current
        compliance of the item.

      - **CapExceeded** *(boolean) --*

        Indicates whether the maximum count is reached.
    """


_ClientDescribeComplianceByResourceResponseComplianceByResourcesTypeDef = TypedDict(
    "_ClientDescribeComplianceByResourceResponseComplianceByResourcesTypeDef",
    {
        "ResourceType": str,
        "ResourceId": str,
        "Compliance": ClientDescribeComplianceByResourceResponseComplianceByResourcesComplianceTypeDef,
    },
    total=False,
)


class ClientDescribeComplianceByResourceResponseComplianceByResourcesTypeDef(
    _ClientDescribeComplianceByResourceResponseComplianceByResourcesTypeDef
):
    """
    Type definition for `ClientDescribeComplianceByResourceResponse` `ComplianceByResources`

    Indicates whether an AWS resource that is evaluated according to one or more AWS Config
    rules is compliant. A resource is compliant if it complies with all of the rules that
    evaluate it. A resource is noncompliant if it does not comply with one or more of these
    rules.

    - **ResourceType** *(string) --*

      The type of the AWS resource that was evaluated.

    - **ResourceId** *(string) --*

      The ID of the AWS resource that was evaluated.

    - **Compliance** *(dict) --*

      Indicates whether the AWS resource complies with all of the AWS Config rules that
      evaluated it.

      - **ComplianceType** *(string) --*

        Indicates whether an AWS resource or AWS Config rule is compliant.

        A resource is compliant if it complies with all of the AWS Config rules that evaluate
        it. A resource is noncompliant if it does not comply with one or more of these rules.

        A rule is compliant if all of the resources that the rule evaluates comply with it. A
        rule is noncompliant if any of these resources do not comply.

        AWS Config returns the ``INSUFFICIENT_DATA`` value when no evaluation results are
        available for the AWS resource or AWS Config rule.

        For the ``Compliance`` data type, AWS Config supports only ``COMPLIANT`` ,
        ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` values. AWS Config does not support the
        ``NOT_APPLICABLE`` value for the ``Compliance`` data type.

      - **ComplianceContributorCount** *(dict) --*

        The number of AWS resources or AWS Config rules that cause a result of
        ``NON_COMPLIANT`` , up to a maximum number.

        - **CappedCount** *(integer) --*

          The number of AWS resources or AWS Config rules responsible for the current
          compliance of the item.

        - **CapExceeded** *(boolean) --*

          Indicates whether the maximum count is reached.
    """


_ClientDescribeComplianceByResourceResponseTypeDef = TypedDict(
    "_ClientDescribeComplianceByResourceResponseTypeDef",
    {
        "ComplianceByResources": List[
            ClientDescribeComplianceByResourceResponseComplianceByResourcesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeComplianceByResourceResponseTypeDef(
    _ClientDescribeComplianceByResourceResponseTypeDef
):
    """
    Type definition for `ClientDescribeComplianceByResource` `Response`

    - **ComplianceByResources** *(list) --*

      Indicates whether the specified AWS resource complies with all of the AWS Config rules that
      evaluate it.

      - *(dict) --*

        Indicates whether an AWS resource that is evaluated according to one or more AWS Config
        rules is compliant. A resource is compliant if it complies with all of the rules that
        evaluate it. A resource is noncompliant if it does not comply with one or more of these
        rules.

        - **ResourceType** *(string) --*

          The type of the AWS resource that was evaluated.

        - **ResourceId** *(string) --*

          The ID of the AWS resource that was evaluated.

        - **Compliance** *(dict) --*

          Indicates whether the AWS resource complies with all of the AWS Config rules that
          evaluated it.

          - **ComplianceType** *(string) --*

            Indicates whether an AWS resource or AWS Config rule is compliant.

            A resource is compliant if it complies with all of the AWS Config rules that evaluate
            it. A resource is noncompliant if it does not comply with one or more of these rules.

            A rule is compliant if all of the resources that the rule evaluates comply with it. A
            rule is noncompliant if any of these resources do not comply.

            AWS Config returns the ``INSUFFICIENT_DATA`` value when no evaluation results are
            available for the AWS resource or AWS Config rule.

            For the ``Compliance`` data type, AWS Config supports only ``COMPLIANT`` ,
            ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` values. AWS Config does not support the
            ``NOT_APPLICABLE`` value for the ``Compliance`` data type.

          - **ComplianceContributorCount** *(dict) --*

            The number of AWS resources or AWS Config rules that cause a result of
            ``NON_COMPLIANT`` , up to a maximum number.

            - **CappedCount** *(integer) --*

              The number of AWS resources or AWS Config rules responsible for the current
              compliance of the item.

            - **CapExceeded** *(boolean) --*

              Indicates whether the maximum count is reached.

    - **NextToken** *(string) --*

      The string that you use in a subsequent request to get the next page of results in a
      paginated response.
    """


_ClientDescribeConfigRuleEvaluationStatusResponseConfigRulesEvaluationStatusTypeDef = TypedDict(
    "_ClientDescribeConfigRuleEvaluationStatusResponseConfigRulesEvaluationStatusTypeDef",
    {
        "ConfigRuleName": str,
        "ConfigRuleArn": str,
        "ConfigRuleId": str,
        "LastSuccessfulInvocationTime": datetime,
        "LastFailedInvocationTime": datetime,
        "LastSuccessfulEvaluationTime": datetime,
        "LastFailedEvaluationTime": datetime,
        "FirstActivatedTime": datetime,
        "LastErrorCode": str,
        "LastErrorMessage": str,
        "FirstEvaluationStarted": bool,
    },
    total=False,
)


class ClientDescribeConfigRuleEvaluationStatusResponseConfigRulesEvaluationStatusTypeDef(
    _ClientDescribeConfigRuleEvaluationStatusResponseConfigRulesEvaluationStatusTypeDef
):
    """
    Type definition for `ClientDescribeConfigRuleEvaluationStatusResponse` `ConfigRulesEvaluationStatus`

    Status information for your AWS managed Config rules. The status includes information such
    as the last time the rule ran, the last time it failed, and the related error for the last
    failure.

    This action does not return status information about custom AWS Config rules.

    - **ConfigRuleName** *(string) --*

      The name of the AWS Config rule.

    - **ConfigRuleArn** *(string) --*

      The Amazon Resource Name (ARN) of the AWS Config rule.

    - **ConfigRuleId** *(string) --*

      The ID of the AWS Config rule.

    - **LastSuccessfulInvocationTime** *(datetime) --*

      The time that AWS Config last successfully invoked the AWS Config rule to evaluate your
      AWS resources.

    - **LastFailedInvocationTime** *(datetime) --*

      The time that AWS Config last failed to invoke the AWS Config rule to evaluate your AWS
      resources.

    - **LastSuccessfulEvaluationTime** *(datetime) --*

      The time that AWS Config last successfully evaluated your AWS resources against the rule.

    - **LastFailedEvaluationTime** *(datetime) --*

      The time that AWS Config last failed to evaluate your AWS resources against the rule.

    - **FirstActivatedTime** *(datetime) --*

      The time that you first activated the AWS Config rule.

    - **LastErrorCode** *(string) --*

      The error code that AWS Config returned when the rule last failed.

    - **LastErrorMessage** *(string) --*

      The error message that AWS Config returned when the rule last failed.

    - **FirstEvaluationStarted** *(boolean) --*

      Indicates whether AWS Config has evaluated your resources against the rule at least once.

      * ``true`` - AWS Config has evaluated your AWS resources against the rule at least once.

      * ``false`` - AWS Config has not once finished evaluating your AWS resources against the
      rule.
    """


_ClientDescribeConfigRuleEvaluationStatusResponseTypeDef = TypedDict(
    "_ClientDescribeConfigRuleEvaluationStatusResponseTypeDef",
    {
        "ConfigRulesEvaluationStatus": List[
            ClientDescribeConfigRuleEvaluationStatusResponseConfigRulesEvaluationStatusTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeConfigRuleEvaluationStatusResponseTypeDef(
    _ClientDescribeConfigRuleEvaluationStatusResponseTypeDef
):
    """
    Type definition for `ClientDescribeConfigRuleEvaluationStatus` `Response`

    - **ConfigRulesEvaluationStatus** *(list) --*

      Status information about your AWS managed Config rules.

      - *(dict) --*

        Status information for your AWS managed Config rules. The status includes information such
        as the last time the rule ran, the last time it failed, and the related error for the last
        failure.

        This action does not return status information about custom AWS Config rules.

        - **ConfigRuleName** *(string) --*

          The name of the AWS Config rule.

        - **ConfigRuleArn** *(string) --*

          The Amazon Resource Name (ARN) of the AWS Config rule.

        - **ConfigRuleId** *(string) --*

          The ID of the AWS Config rule.

        - **LastSuccessfulInvocationTime** *(datetime) --*

          The time that AWS Config last successfully invoked the AWS Config rule to evaluate your
          AWS resources.

        - **LastFailedInvocationTime** *(datetime) --*

          The time that AWS Config last failed to invoke the AWS Config rule to evaluate your AWS
          resources.

        - **LastSuccessfulEvaluationTime** *(datetime) --*

          The time that AWS Config last successfully evaluated your AWS resources against the rule.

        - **LastFailedEvaluationTime** *(datetime) --*

          The time that AWS Config last failed to evaluate your AWS resources against the rule.

        - **FirstActivatedTime** *(datetime) --*

          The time that you first activated the AWS Config rule.

        - **LastErrorCode** *(string) --*

          The error code that AWS Config returned when the rule last failed.

        - **LastErrorMessage** *(string) --*

          The error message that AWS Config returned when the rule last failed.

        - **FirstEvaluationStarted** *(boolean) --*

          Indicates whether AWS Config has evaluated your resources against the rule at least once.

          * ``true`` - AWS Config has evaluated your AWS resources against the rule at least once.

          * ``false`` - AWS Config has not once finished evaluating your AWS resources against the
          rule.

    - **NextToken** *(string) --*

      The string that you use in a subsequent request to get the next page of results in a
      paginated response.
    """


_ClientDescribeConfigRulesResponseConfigRulesScopeTypeDef = TypedDict(
    "_ClientDescribeConfigRulesResponseConfigRulesScopeTypeDef",
    {
        "ComplianceResourceTypes": List[str],
        "TagKey": str,
        "TagValue": str,
        "ComplianceResourceId": str,
    },
    total=False,
)


class ClientDescribeConfigRulesResponseConfigRulesScopeTypeDef(
    _ClientDescribeConfigRulesResponseConfigRulesScopeTypeDef
):
    """
    Type definition for `ClientDescribeConfigRulesResponseConfigRules` `Scope`

    Defines which resources can trigger an evaluation for the rule. The scope can include one
    or more resource types, a combination of one resource type and one resource ID, or a
    combination of a tag key and value. Specify a scope to constrain the resources that can
    trigger an evaluation for the rule. If you do not specify a scope, evaluations are
    triggered when any resource in the recording group changes.

    - **ComplianceResourceTypes** *(list) --*

      The resource types of only those AWS resources that you want to trigger an evaluation
      for the rule. You can only specify one type if you also specify a resource ID for
      ``ComplianceResourceId`` .

      - *(string) --*

    - **TagKey** *(string) --*

      The tag key that is applied to only those AWS resources that you want to trigger an
      evaluation for the rule.

    - **TagValue** *(string) --*

      The tag value applied to only those AWS resources that you want to trigger an
      evaluation for the rule. If you specify a value for ``TagValue`` , you must also
      specify a value for ``TagKey`` .

    - **ComplianceResourceId** *(string) --*

      The ID of the only AWS resource that you want to trigger an evaluation for the rule. If
      you specify a resource ID, you must specify one resource type for
      ``ComplianceResourceTypes`` .
    """


_ClientDescribeConfigRulesResponseConfigRulesSourceSourceDetailsTypeDef = TypedDict(
    "_ClientDescribeConfigRulesResponseConfigRulesSourceSourceDetailsTypeDef",
    {"EventSource": str, "MessageType": str, "MaximumExecutionFrequency": str},
    total=False,
)


class ClientDescribeConfigRulesResponseConfigRulesSourceSourceDetailsTypeDef(
    _ClientDescribeConfigRulesResponseConfigRulesSourceSourceDetailsTypeDef
):
    """
    Type definition for `ClientDescribeConfigRulesResponseConfigRulesSource` `SourceDetails`

    Provides the source and the message types that trigger AWS Config to evaluate your
    AWS resources against a rule. It also provides the frequency with which you want AWS
    Config to run evaluations for the rule if the trigger type is periodic. You can
    specify the parameter values for ``SourceDetail`` only for custom rules.

    - **EventSource** *(string) --*

      The source of the event, such as an AWS service, that triggers AWS Config to
      evaluate your AWS resources.

    - **MessageType** *(string) --*

      The type of notification that triggers AWS Config to run an evaluation for a rule.
      You can specify the following notification types:

      * ``ConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config
      delivers a configuration item as a result of a resource change.

      * ``OversizedConfigurationItemChangeNotification`` - Triggers an evaluation when
      AWS Config delivers an oversized configuration item. AWS Config may generate this
      notification type when a resource changes and the notification exceeds the maximum
      size allowed by Amazon SNS.

      * ``ScheduledNotification`` - Triggers a periodic evaluation at the frequency
      specified for ``MaximumExecutionFrequency`` .

      * ``ConfigurationSnapshotDeliveryCompleted`` - Triggers a periodic evaluation when
      AWS Config delivers a configuration snapshot.

      If you want your custom rule to be triggered by configuration changes, specify two
      SourceDetail objects, one for ``ConfigurationItemChangeNotification`` and one for
      ``OversizedConfigurationItemChangeNotification`` .

    - **MaximumExecutionFrequency** *(string) --*

      The frequency at which you want AWS Config to run evaluations for a custom rule
      with a periodic trigger. If you specify a value for ``MaximumExecutionFrequency`` ,
      then ``MessageType`` must use the ``ScheduledNotification`` value.

      .. note::

        By default, rules with a periodic trigger are evaluated every 24 hours. To change
        the frequency, specify a valid value for the ``MaximumExecutionFrequency``
        parameter.

        Based on the valid value you choose, AWS Config runs evaluations once for each
        valid value. For example, if you choose ``Three_Hours`` , AWS Config runs
        evaluations once every three hours. In this case, ``Three_Hours`` is the
        frequency of this rule.
    """


_ClientDescribeConfigRulesResponseConfigRulesSourceTypeDef = TypedDict(
    "_ClientDescribeConfigRulesResponseConfigRulesSourceTypeDef",
    {
        "Owner": str,
        "SourceIdentifier": str,
        "SourceDetails": List[
            ClientDescribeConfigRulesResponseConfigRulesSourceSourceDetailsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeConfigRulesResponseConfigRulesSourceTypeDef(
    _ClientDescribeConfigRulesResponseConfigRulesSourceTypeDef
):
    """
    Type definition for `ClientDescribeConfigRulesResponseConfigRules` `Source`

    Provides the rule owner (AWS or customer), the rule identifier, and the notifications
    that cause the function to evaluate your AWS resources.

    - **Owner** *(string) --*

      Indicates whether AWS or the customer owns and manages the AWS Config rule.

    - **SourceIdentifier** *(string) --*

      For AWS Config managed rules, a predefined identifier from a list. For example,
      ``IAM_PASSWORD_POLICY`` is a managed rule. To reference a managed rule, see `Using AWS
      Managed Config Rules
      <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html>`__
      .

      For custom rules, the identifier is the Amazon Resource Name (ARN) of the rule's AWS
      Lambda function, such as
      ``arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name`` .

    - **SourceDetails** *(list) --*

      Provides the source and type of the event that causes AWS Config to evaluate your AWS
      resources.

      - *(dict) --*

        Provides the source and the message types that trigger AWS Config to evaluate your
        AWS resources against a rule. It also provides the frequency with which you want AWS
        Config to run evaluations for the rule if the trigger type is periodic. You can
        specify the parameter values for ``SourceDetail`` only for custom rules.

        - **EventSource** *(string) --*

          The source of the event, such as an AWS service, that triggers AWS Config to
          evaluate your AWS resources.

        - **MessageType** *(string) --*

          The type of notification that triggers AWS Config to run an evaluation for a rule.
          You can specify the following notification types:

          * ``ConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config
          delivers a configuration item as a result of a resource change.

          * ``OversizedConfigurationItemChangeNotification`` - Triggers an evaluation when
          AWS Config delivers an oversized configuration item. AWS Config may generate this
          notification type when a resource changes and the notification exceeds the maximum
          size allowed by Amazon SNS.

          * ``ScheduledNotification`` - Triggers a periodic evaluation at the frequency
          specified for ``MaximumExecutionFrequency`` .

          * ``ConfigurationSnapshotDeliveryCompleted`` - Triggers a periodic evaluation when
          AWS Config delivers a configuration snapshot.

          If you want your custom rule to be triggered by configuration changes, specify two
          SourceDetail objects, one for ``ConfigurationItemChangeNotification`` and one for
          ``OversizedConfigurationItemChangeNotification`` .

        - **MaximumExecutionFrequency** *(string) --*

          The frequency at which you want AWS Config to run evaluations for a custom rule
          with a periodic trigger. If you specify a value for ``MaximumExecutionFrequency`` ,
          then ``MessageType`` must use the ``ScheduledNotification`` value.

          .. note::

            By default, rules with a periodic trigger are evaluated every 24 hours. To change
            the frequency, specify a valid value for the ``MaximumExecutionFrequency``
            parameter.

            Based on the valid value you choose, AWS Config runs evaluations once for each
            valid value. For example, if you choose ``Three_Hours`` , AWS Config runs
            evaluations once every three hours. In this case, ``Three_Hours`` is the
            frequency of this rule.
    """


_ClientDescribeConfigRulesResponseConfigRulesTypeDef = TypedDict(
    "_ClientDescribeConfigRulesResponseConfigRulesTypeDef",
    {
        "ConfigRuleName": str,
        "ConfigRuleArn": str,
        "ConfigRuleId": str,
        "Description": str,
        "Scope": ClientDescribeConfigRulesResponseConfigRulesScopeTypeDef,
        "Source": ClientDescribeConfigRulesResponseConfigRulesSourceTypeDef,
        "InputParameters": str,
        "MaximumExecutionFrequency": str,
        "ConfigRuleState": str,
        "CreatedBy": str,
    },
    total=False,
)


class ClientDescribeConfigRulesResponseConfigRulesTypeDef(
    _ClientDescribeConfigRulesResponseConfigRulesTypeDef
):
    """
    Type definition for `ClientDescribeConfigRulesResponse` `ConfigRules`

    An AWS Config rule represents an AWS Lambda function that you create for a custom rule or a
    predefined function for an AWS managed rule. The function evaluates configuration items to
    assess whether your AWS resources comply with your desired configurations. This function
    can run when AWS Config detects a configuration change to an AWS resource and at a periodic
    frequency that you choose (for example, every 24 hours).

    .. note::

      You can use the AWS CLI and AWS SDKs if you want to create a rule that triggers
      evaluations for your resources when AWS Config delivers the configuration snapshot. For
      more information, see  ConfigSnapshotDeliveryProperties .

    For more information about developing and using AWS Config rules, see `Evaluating AWS
    Resource Configurations with AWS Config
    <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html>`__ in the
    *AWS Config Developer Guide* .

    - **ConfigRuleName** *(string) --*

      The name that you assign to the AWS Config rule. The name is required if you are adding a
      new rule.

    - **ConfigRuleArn** *(string) --*

      The Amazon Resource Name (ARN) of the AWS Config rule.

    - **ConfigRuleId** *(string) --*

      The ID of the AWS Config rule.

    - **Description** *(string) --*

      The description that you provide for the AWS Config rule.

    - **Scope** *(dict) --*

      Defines which resources can trigger an evaluation for the rule. The scope can include one
      or more resource types, a combination of one resource type and one resource ID, or a
      combination of a tag key and value. Specify a scope to constrain the resources that can
      trigger an evaluation for the rule. If you do not specify a scope, evaluations are
      triggered when any resource in the recording group changes.

      - **ComplianceResourceTypes** *(list) --*

        The resource types of only those AWS resources that you want to trigger an evaluation
        for the rule. You can only specify one type if you also specify a resource ID for
        ``ComplianceResourceId`` .

        - *(string) --*

      - **TagKey** *(string) --*

        The tag key that is applied to only those AWS resources that you want to trigger an
        evaluation for the rule.

      - **TagValue** *(string) --*

        The tag value applied to only those AWS resources that you want to trigger an
        evaluation for the rule. If you specify a value for ``TagValue`` , you must also
        specify a value for ``TagKey`` .

      - **ComplianceResourceId** *(string) --*

        The ID of the only AWS resource that you want to trigger an evaluation for the rule. If
        you specify a resource ID, you must specify one resource type for
        ``ComplianceResourceTypes`` .

    - **Source** *(dict) --*

      Provides the rule owner (AWS or customer), the rule identifier, and the notifications
      that cause the function to evaluate your AWS resources.

      - **Owner** *(string) --*

        Indicates whether AWS or the customer owns and manages the AWS Config rule.

      - **SourceIdentifier** *(string) --*

        For AWS Config managed rules, a predefined identifier from a list. For example,
        ``IAM_PASSWORD_POLICY`` is a managed rule. To reference a managed rule, see `Using AWS
        Managed Config Rules
        <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html>`__
        .

        For custom rules, the identifier is the Amazon Resource Name (ARN) of the rule's AWS
        Lambda function, such as
        ``arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name`` .

      - **SourceDetails** *(list) --*

        Provides the source and type of the event that causes AWS Config to evaluate your AWS
        resources.

        - *(dict) --*

          Provides the source and the message types that trigger AWS Config to evaluate your
          AWS resources against a rule. It also provides the frequency with which you want AWS
          Config to run evaluations for the rule if the trigger type is periodic. You can
          specify the parameter values for ``SourceDetail`` only for custom rules.

          - **EventSource** *(string) --*

            The source of the event, such as an AWS service, that triggers AWS Config to
            evaluate your AWS resources.

          - **MessageType** *(string) --*

            The type of notification that triggers AWS Config to run an evaluation for a rule.
            You can specify the following notification types:

            * ``ConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config
            delivers a configuration item as a result of a resource change.

            * ``OversizedConfigurationItemChangeNotification`` - Triggers an evaluation when
            AWS Config delivers an oversized configuration item. AWS Config may generate this
            notification type when a resource changes and the notification exceeds the maximum
            size allowed by Amazon SNS.

            * ``ScheduledNotification`` - Triggers a periodic evaluation at the frequency
            specified for ``MaximumExecutionFrequency`` .

            * ``ConfigurationSnapshotDeliveryCompleted`` - Triggers a periodic evaluation when
            AWS Config delivers a configuration snapshot.

            If you want your custom rule to be triggered by configuration changes, specify two
            SourceDetail objects, one for ``ConfigurationItemChangeNotification`` and one for
            ``OversizedConfigurationItemChangeNotification`` .

          - **MaximumExecutionFrequency** *(string) --*

            The frequency at which you want AWS Config to run evaluations for a custom rule
            with a periodic trigger. If you specify a value for ``MaximumExecutionFrequency`` ,
            then ``MessageType`` must use the ``ScheduledNotification`` value.

            .. note::

              By default, rules with a periodic trigger are evaluated every 24 hours. To change
              the frequency, specify a valid value for the ``MaximumExecutionFrequency``
              parameter.

              Based on the valid value you choose, AWS Config runs evaluations once for each
              valid value. For example, if you choose ``Three_Hours`` , AWS Config runs
              evaluations once every three hours. In this case, ``Three_Hours`` is the
              frequency of this rule.

    - **InputParameters** *(string) --*

      A string, in JSON format, that is passed to the AWS Config rule Lambda function.

    - **MaximumExecutionFrequency** *(string) --*

      The maximum frequency with which AWS Config runs evaluations for a rule. You can specify
      a value for ``MaximumExecutionFrequency`` when:

      * You are using an AWS managed rule that is triggered at a periodic frequency.

      * Your custom rule is triggered when AWS Config delivers the configuration snapshot. For
      more information, see  ConfigSnapshotDeliveryProperties .

      .. note::

        By default, rules with a periodic trigger are evaluated every 24 hours. To change the
        frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.

    - **ConfigRuleState** *(string) --*

      Indicates whether the AWS Config rule is active or is currently being deleted by AWS
      Config. It can also indicate the evaluation status for the AWS Config rule.

      AWS Config sets the state of the rule to ``EVALUATING`` temporarily after you use the
      ``StartConfigRulesEvaluation`` request to evaluate your resources against the AWS Config
      rule.

      AWS Config sets the state of the rule to ``DELETING_RESULTS`` temporarily after you use
      the ``DeleteEvaluationResults`` request to delete the current evaluation results for the
      AWS Config rule.

      AWS Config temporarily sets the state of a rule to ``DELETING`` after you use the
      ``DeleteConfigRule`` request to delete the rule. After AWS Config deletes the rule, the
      rule and all of its evaluations are erased and are no longer available.

    - **CreatedBy** *(string) --*

      Service principal name of the service that created the rule.

      .. note::

        The field is populated only if the service linked rule is created by a service. The
        field is empty if you create your own rule.
    """


_ClientDescribeConfigRulesResponseTypeDef = TypedDict(
    "_ClientDescribeConfigRulesResponseTypeDef",
    {
        "ConfigRules": List[ClientDescribeConfigRulesResponseConfigRulesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeConfigRulesResponseTypeDef(
    _ClientDescribeConfigRulesResponseTypeDef
):
    """
    Type definition for `ClientDescribeConfigRules` `Response`

    - **ConfigRules** *(list) --*

      The details about your AWS Config rules.

      - *(dict) --*

        An AWS Config rule represents an AWS Lambda function that you create for a custom rule or a
        predefined function for an AWS managed rule. The function evaluates configuration items to
        assess whether your AWS resources comply with your desired configurations. This function
        can run when AWS Config detects a configuration change to an AWS resource and at a periodic
        frequency that you choose (for example, every 24 hours).

        .. note::

          You can use the AWS CLI and AWS SDKs if you want to create a rule that triggers
          evaluations for your resources when AWS Config delivers the configuration snapshot. For
          more information, see  ConfigSnapshotDeliveryProperties .

        For more information about developing and using AWS Config rules, see `Evaluating AWS
        Resource Configurations with AWS Config
        <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html>`__ in the
        *AWS Config Developer Guide* .

        - **ConfigRuleName** *(string) --*

          The name that you assign to the AWS Config rule. The name is required if you are adding a
          new rule.

        - **ConfigRuleArn** *(string) --*

          The Amazon Resource Name (ARN) of the AWS Config rule.

        - **ConfigRuleId** *(string) --*

          The ID of the AWS Config rule.

        - **Description** *(string) --*

          The description that you provide for the AWS Config rule.

        - **Scope** *(dict) --*

          Defines which resources can trigger an evaluation for the rule. The scope can include one
          or more resource types, a combination of one resource type and one resource ID, or a
          combination of a tag key and value. Specify a scope to constrain the resources that can
          trigger an evaluation for the rule. If you do not specify a scope, evaluations are
          triggered when any resource in the recording group changes.

          - **ComplianceResourceTypes** *(list) --*

            The resource types of only those AWS resources that you want to trigger an evaluation
            for the rule. You can only specify one type if you also specify a resource ID for
            ``ComplianceResourceId`` .

            - *(string) --*

          - **TagKey** *(string) --*

            The tag key that is applied to only those AWS resources that you want to trigger an
            evaluation for the rule.

          - **TagValue** *(string) --*

            The tag value applied to only those AWS resources that you want to trigger an
            evaluation for the rule. If you specify a value for ``TagValue`` , you must also
            specify a value for ``TagKey`` .

          - **ComplianceResourceId** *(string) --*

            The ID of the only AWS resource that you want to trigger an evaluation for the rule. If
            you specify a resource ID, you must specify one resource type for
            ``ComplianceResourceTypes`` .

        - **Source** *(dict) --*

          Provides the rule owner (AWS or customer), the rule identifier, and the notifications
          that cause the function to evaluate your AWS resources.

          - **Owner** *(string) --*

            Indicates whether AWS or the customer owns and manages the AWS Config rule.

          - **SourceIdentifier** *(string) --*

            For AWS Config managed rules, a predefined identifier from a list. For example,
            ``IAM_PASSWORD_POLICY`` is a managed rule. To reference a managed rule, see `Using AWS
            Managed Config Rules
            <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html>`__
            .

            For custom rules, the identifier is the Amazon Resource Name (ARN) of the rule's AWS
            Lambda function, such as
            ``arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name`` .

          - **SourceDetails** *(list) --*

            Provides the source and type of the event that causes AWS Config to evaluate your AWS
            resources.

            - *(dict) --*

              Provides the source and the message types that trigger AWS Config to evaluate your
              AWS resources against a rule. It also provides the frequency with which you want AWS
              Config to run evaluations for the rule if the trigger type is periodic. You can
              specify the parameter values for ``SourceDetail`` only for custom rules.

              - **EventSource** *(string) --*

                The source of the event, such as an AWS service, that triggers AWS Config to
                evaluate your AWS resources.

              - **MessageType** *(string) --*

                The type of notification that triggers AWS Config to run an evaluation for a rule.
                You can specify the following notification types:

                * ``ConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config
                delivers a configuration item as a result of a resource change.

                * ``OversizedConfigurationItemChangeNotification`` - Triggers an evaluation when
                AWS Config delivers an oversized configuration item. AWS Config may generate this
                notification type when a resource changes and the notification exceeds the maximum
                size allowed by Amazon SNS.

                * ``ScheduledNotification`` - Triggers a periodic evaluation at the frequency
                specified for ``MaximumExecutionFrequency`` .

                * ``ConfigurationSnapshotDeliveryCompleted`` - Triggers a periodic evaluation when
                AWS Config delivers a configuration snapshot.

                If you want your custom rule to be triggered by configuration changes, specify two
                SourceDetail objects, one for ``ConfigurationItemChangeNotification`` and one for
                ``OversizedConfigurationItemChangeNotification`` .

              - **MaximumExecutionFrequency** *(string) --*

                The frequency at which you want AWS Config to run evaluations for a custom rule
                with a periodic trigger. If you specify a value for ``MaximumExecutionFrequency`` ,
                then ``MessageType`` must use the ``ScheduledNotification`` value.

                .. note::

                  By default, rules with a periodic trigger are evaluated every 24 hours. To change
                  the frequency, specify a valid value for the ``MaximumExecutionFrequency``
                  parameter.

                  Based on the valid value you choose, AWS Config runs evaluations once for each
                  valid value. For example, if you choose ``Three_Hours`` , AWS Config runs
                  evaluations once every three hours. In this case, ``Three_Hours`` is the
                  frequency of this rule.

        - **InputParameters** *(string) --*

          A string, in JSON format, that is passed to the AWS Config rule Lambda function.

        - **MaximumExecutionFrequency** *(string) --*

          The maximum frequency with which AWS Config runs evaluations for a rule. You can specify
          a value for ``MaximumExecutionFrequency`` when:

          * You are using an AWS managed rule that is triggered at a periodic frequency.

          * Your custom rule is triggered when AWS Config delivers the configuration snapshot. For
          more information, see  ConfigSnapshotDeliveryProperties .

          .. note::

            By default, rules with a periodic trigger are evaluated every 24 hours. To change the
            frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.

        - **ConfigRuleState** *(string) --*

          Indicates whether the AWS Config rule is active or is currently being deleted by AWS
          Config. It can also indicate the evaluation status for the AWS Config rule.

          AWS Config sets the state of the rule to ``EVALUATING`` temporarily after you use the
          ``StartConfigRulesEvaluation`` request to evaluate your resources against the AWS Config
          rule.

          AWS Config sets the state of the rule to ``DELETING_RESULTS`` temporarily after you use
          the ``DeleteEvaluationResults`` request to delete the current evaluation results for the
          AWS Config rule.

          AWS Config temporarily sets the state of a rule to ``DELETING`` after you use the
          ``DeleteConfigRule`` request to delete the rule. After AWS Config deletes the rule, the
          rule and all of its evaluations are erased and are no longer available.

        - **CreatedBy** *(string) --*

          Service principal name of the service that created the rule.

          .. note::

            The field is populated only if the service linked rule is created by a service. The
            field is empty if you create your own rule.

    - **NextToken** *(string) --*

      The string that you use in a subsequent request to get the next page of results in a
      paginated response.
    """


_ClientDescribeConfigurationAggregatorSourcesStatusResponseAggregatedSourceStatusListTypeDef = TypedDict(
    "_ClientDescribeConfigurationAggregatorSourcesStatusResponseAggregatedSourceStatusListTypeDef",
    {
        "SourceId": str,
        "SourceType": str,
        "AwsRegion": str,
        "LastUpdateStatus": str,
        "LastUpdateTime": datetime,
        "LastErrorCode": str,
        "LastErrorMessage": str,
    },
    total=False,
)


class ClientDescribeConfigurationAggregatorSourcesStatusResponseAggregatedSourceStatusListTypeDef(
    _ClientDescribeConfigurationAggregatorSourcesStatusResponseAggregatedSourceStatusListTypeDef
):
    """
    Type definition for `ClientDescribeConfigurationAggregatorSourcesStatusResponse` `AggregatedSourceStatusList`

    The current sync status between the source and the aggregator account.

    - **SourceId** *(string) --*

      The source account ID or an organization.

    - **SourceType** *(string) --*

      The source account or an organization.

    - **AwsRegion** *(string) --*

      The region authorized to collect aggregated data.

    - **LastUpdateStatus** *(string) --*

      Filters the last updated status type.

      * Valid value FAILED indicates errors while moving data.

      * Valid value SUCCEEDED indicates the data was successfully moved.

      * Valid value OUTDATED indicates the data is not the most recent.

    - **LastUpdateTime** *(datetime) --*

      The time of the last update.

    - **LastErrorCode** *(string) --*

      The error code that AWS Config returned when the source account aggregation last failed.

    - **LastErrorMessage** *(string) --*

      The message indicating that the source account aggregation failed due to an error.
    """


_ClientDescribeConfigurationAggregatorSourcesStatusResponseTypeDef = TypedDict(
    "_ClientDescribeConfigurationAggregatorSourcesStatusResponseTypeDef",
    {
        "AggregatedSourceStatusList": List[
            ClientDescribeConfigurationAggregatorSourcesStatusResponseAggregatedSourceStatusListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeConfigurationAggregatorSourcesStatusResponseTypeDef(
    _ClientDescribeConfigurationAggregatorSourcesStatusResponseTypeDef
):
    """
    Type definition for `ClientDescribeConfigurationAggregatorSourcesStatus` `Response`

    - **AggregatedSourceStatusList** *(list) --*

      Returns an AggregatedSourceStatus object.

      - *(dict) --*

        The current sync status between the source and the aggregator account.

        - **SourceId** *(string) --*

          The source account ID or an organization.

        - **SourceType** *(string) --*

          The source account or an organization.

        - **AwsRegion** *(string) --*

          The region authorized to collect aggregated data.

        - **LastUpdateStatus** *(string) --*

          Filters the last updated status type.

          * Valid value FAILED indicates errors while moving data.

          * Valid value SUCCEEDED indicates the data was successfully moved.

          * Valid value OUTDATED indicates the data is not the most recent.

        - **LastUpdateTime** *(datetime) --*

          The time of the last update.

        - **LastErrorCode** *(string) --*

          The error code that AWS Config returned when the source account aggregation last failed.

        - **LastErrorMessage** *(string) --*

          The message indicating that the source account aggregation failed due to an error.

    - **NextToken** *(string) --*

      The ``nextToken`` string returned on a previous page that you use to get the next page of
      results in a paginated response.
    """


_ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsAccountAggregationSourcesTypeDef = TypedDict(
    "_ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsAccountAggregationSourcesTypeDef",
    {"AccountIds": List[str], "AllAwsRegions": bool, "AwsRegions": List[str]},
    total=False,
)


class ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsAccountAggregationSourcesTypeDef(
    _ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsAccountAggregationSourcesTypeDef
):
    """
    Type definition for `ClientDescribeConfigurationAggregatorsResponseConfigurationAggregators` `AccountAggregationSources`

    A collection of accounts and regions.

    - **AccountIds** *(list) --*

      The 12-digit account ID of the account being aggregated.

      - *(string) --*

    - **AllAwsRegions** *(boolean) --*

      If true, aggregate existing AWS Config regions and future regions.

    - **AwsRegions** *(list) --*

      The source regions being aggregated.

      - *(string) --*
    """


_ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsOrganizationAggregationSourceTypeDef = TypedDict(
    "_ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsOrganizationAggregationSourceTypeDef",
    {"RoleArn": str, "AwsRegions": List[str], "AllAwsRegions": bool},
    total=False,
)


class ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsOrganizationAggregationSourceTypeDef(
    _ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsOrganizationAggregationSourceTypeDef
):
    """
    Type definition for `ClientDescribeConfigurationAggregatorsResponseConfigurationAggregators` `OrganizationAggregationSource`

    Provides an organization and list of regions to be aggregated.

    - **RoleArn** *(string) --*

      ARN of the IAM role used to retrieve AWS Organization details associated with the
      aggregator account.

    - **AwsRegions** *(list) --*

      The source regions being aggregated.

      - *(string) --*

    - **AllAwsRegions** *(boolean) --*

      If true, aggregate existing AWS Config regions and future regions.
    """


_ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsTypeDef = TypedDict(
    "_ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ConfigurationAggregatorArn": str,
        "AccountAggregationSources": List[
            ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsAccountAggregationSourcesTypeDef
        ],
        "OrganizationAggregationSource": ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsOrganizationAggregationSourceTypeDef,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)


class ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsTypeDef(
    _ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsTypeDef
):
    """
    Type definition for `ClientDescribeConfigurationAggregatorsResponse` `ConfigurationAggregators`

    The details about the configuration aggregator, including information about source
    accounts, regions, and metadata of the aggregator.

    - **ConfigurationAggregatorName** *(string) --*

      The name of the aggregator.

    - **ConfigurationAggregatorArn** *(string) --*

      The Amazon Resource Name (ARN) of the aggregator.

    - **AccountAggregationSources** *(list) --*

      Provides a list of source accounts and regions to be aggregated.

      - *(dict) --*

        A collection of accounts and regions.

        - **AccountIds** *(list) --*

          The 12-digit account ID of the account being aggregated.

          - *(string) --*

        - **AllAwsRegions** *(boolean) --*

          If true, aggregate existing AWS Config regions and future regions.

        - **AwsRegions** *(list) --*

          The source regions being aggregated.

          - *(string) --*

    - **OrganizationAggregationSource** *(dict) --*

      Provides an organization and list of regions to be aggregated.

      - **RoleArn** *(string) --*

        ARN of the IAM role used to retrieve AWS Organization details associated with the
        aggregator account.

      - **AwsRegions** *(list) --*

        The source regions being aggregated.

        - *(string) --*

      - **AllAwsRegions** *(boolean) --*

        If true, aggregate existing AWS Config regions and future regions.

    - **CreationTime** *(datetime) --*

      The time stamp when the configuration aggregator was created.

    - **LastUpdatedTime** *(datetime) --*

      The time of the last update.
    """


_ClientDescribeConfigurationAggregatorsResponseTypeDef = TypedDict(
    "_ClientDescribeConfigurationAggregatorsResponseTypeDef",
    {
        "ConfigurationAggregators": List[
            ClientDescribeConfigurationAggregatorsResponseConfigurationAggregatorsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeConfigurationAggregatorsResponseTypeDef(
    _ClientDescribeConfigurationAggregatorsResponseTypeDef
):
    """
    Type definition for `ClientDescribeConfigurationAggregators` `Response`

    - **ConfigurationAggregators** *(list) --*

      Returns a ConfigurationAggregators object.

      - *(dict) --*

        The details about the configuration aggregator, including information about source
        accounts, regions, and metadata of the aggregator.

        - **ConfigurationAggregatorName** *(string) --*

          The name of the aggregator.

        - **ConfigurationAggregatorArn** *(string) --*

          The Amazon Resource Name (ARN) of the aggregator.

        - **AccountAggregationSources** *(list) --*

          Provides a list of source accounts and regions to be aggregated.

          - *(dict) --*

            A collection of accounts and regions.

            - **AccountIds** *(list) --*

              The 12-digit account ID of the account being aggregated.

              - *(string) --*

            - **AllAwsRegions** *(boolean) --*

              If true, aggregate existing AWS Config regions and future regions.

            - **AwsRegions** *(list) --*

              The source regions being aggregated.

              - *(string) --*

        - **OrganizationAggregationSource** *(dict) --*

          Provides an organization and list of regions to be aggregated.

          - **RoleArn** *(string) --*

            ARN of the IAM role used to retrieve AWS Organization details associated with the
            aggregator account.

          - **AwsRegions** *(list) --*

            The source regions being aggregated.

            - *(string) --*

          - **AllAwsRegions** *(boolean) --*

            If true, aggregate existing AWS Config regions and future regions.

        - **CreationTime** *(datetime) --*

          The time stamp when the configuration aggregator was created.

        - **LastUpdatedTime** *(datetime) --*

          The time of the last update.

    - **NextToken** *(string) --*

      The ``nextToken`` string returned on a previous page that you use to get the next page of
      results in a paginated response.
    """


_ClientDescribeConfigurationRecorderStatusResponseConfigurationRecordersStatusTypeDef = TypedDict(
    "_ClientDescribeConfigurationRecorderStatusResponseConfigurationRecordersStatusTypeDef",
    {
        "name": str,
        "lastStartTime": datetime,
        "lastStopTime": datetime,
        "recording": bool,
        "lastStatus": str,
        "lastErrorCode": str,
        "lastErrorMessage": str,
        "lastStatusChangeTime": datetime,
    },
    total=False,
)


class ClientDescribeConfigurationRecorderStatusResponseConfigurationRecordersStatusTypeDef(
    _ClientDescribeConfigurationRecorderStatusResponseConfigurationRecordersStatusTypeDef
):
    """
    Type definition for `ClientDescribeConfigurationRecorderStatusResponse` `ConfigurationRecordersStatus`

    The current status of the configuration recorder.

    - **name** *(string) --*

      The name of the configuration recorder.

    - **lastStartTime** *(datetime) --*

      The time the recorder was last started.

    - **lastStopTime** *(datetime) --*

      The time the recorder was last stopped.

    - **recording** *(boolean) --*

      Specifies whether or not the recorder is currently recording.

    - **lastStatus** *(string) --*

      The last (previous) status of the recorder.

    - **lastErrorCode** *(string) --*

      The error code indicating that the recording failed.

    - **lastErrorMessage** *(string) --*

      The message indicating that the recording failed due to an error.

    - **lastStatusChangeTime** *(datetime) --*

      The time when the status was last changed.
    """


_ClientDescribeConfigurationRecorderStatusResponseTypeDef = TypedDict(
    "_ClientDescribeConfigurationRecorderStatusResponseTypeDef",
    {
        "ConfigurationRecordersStatus": List[
            ClientDescribeConfigurationRecorderStatusResponseConfigurationRecordersStatusTypeDef
        ]
    },
    total=False,
)


class ClientDescribeConfigurationRecorderStatusResponseTypeDef(
    _ClientDescribeConfigurationRecorderStatusResponseTypeDef
):
    """
    Type definition for `ClientDescribeConfigurationRecorderStatus` `Response`

    The output for the  DescribeConfigurationRecorderStatus action, in JSON format.

    - **ConfigurationRecordersStatus** *(list) --*

      A list that contains status of the specified recorders.

      - *(dict) --*

        The current status of the configuration recorder.

        - **name** *(string) --*

          The name of the configuration recorder.

        - **lastStartTime** *(datetime) --*

          The time the recorder was last started.

        - **lastStopTime** *(datetime) --*

          The time the recorder was last stopped.

        - **recording** *(boolean) --*

          Specifies whether or not the recorder is currently recording.

        - **lastStatus** *(string) --*

          The last (previous) status of the recorder.

        - **lastErrorCode** *(string) --*

          The error code indicating that the recording failed.

        - **lastErrorMessage** *(string) --*

          The message indicating that the recording failed due to an error.

        - **lastStatusChangeTime** *(datetime) --*

          The time when the status was last changed.
    """


_ClientDescribeConfigurationRecordersResponseConfigurationRecordersrecordingGroupTypeDef = TypedDict(
    "_ClientDescribeConfigurationRecordersResponseConfigurationRecordersrecordingGroupTypeDef",
    {
        "allSupported": bool,
        "includeGlobalResourceTypes": bool,
        "resourceTypes": List[str],
    },
    total=False,
)


class ClientDescribeConfigurationRecordersResponseConfigurationRecordersrecordingGroupTypeDef(
    _ClientDescribeConfigurationRecordersResponseConfigurationRecordersrecordingGroupTypeDef
):
    """
    Type definition for `ClientDescribeConfigurationRecordersResponseConfigurationRecorders` `recordingGroup`

    Specifies the types of AWS resources for which AWS Config records configuration changes.

    - **allSupported** *(boolean) --*

      Specifies whether AWS Config records configuration changes for every supported type of
      regional resource.

      If you set this option to ``true`` , when AWS Config adds support for a new type of
      regional resource, it starts recording resources of that type automatically.

      If you set this option to ``true`` , you cannot enumerate a list of ``resourceTypes`` .

    - **includeGlobalResourceTypes** *(boolean) --*

      Specifies whether AWS Config includes all supported types of global resources (for
      example, IAM resources) with the resources that it records.

      Before you can set this option to ``true`` , you must set the ``allSupported`` option
      to ``true`` .

      If you set this option to ``true`` , when AWS Config adds support for a new type of
      global resource, it starts recording resources of that type automatically.

      The configuration details for any global resource are the same in all regions. To
      prevent duplicate configuration items, you should consider customizing AWS Config in
      only one region to record global resources.

    - **resourceTypes** *(list) --*

      A comma-separated list that specifies the types of AWS resources for which AWS Config
      records configuration changes (for example, ``AWS::EC2::Instance`` or
      ``AWS::CloudTrail::Trail`` ).

      Before you can set this option to ``true`` , you must set the ``allSupported`` option
      to ``false`` .

      If you set this option to ``true`` , when AWS Config adds support for a new type of
      resource, it will not record resources of that type unless you manually add that type
      to your recording group.

      For a list of valid ``resourceTypes`` values, see the **resourceType Value** column in
      `Supported AWS Resource Types
      <https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#supported-resources>`__
      .

      - *(string) --*
    """


_ClientDescribeConfigurationRecordersResponseConfigurationRecordersTypeDef = TypedDict(
    "_ClientDescribeConfigurationRecordersResponseConfigurationRecordersTypeDef",
    {
        "name": str,
        "roleARN": str,
        "recordingGroup": ClientDescribeConfigurationRecordersResponseConfigurationRecordersrecordingGroupTypeDef,
    },
    total=False,
)


class ClientDescribeConfigurationRecordersResponseConfigurationRecordersTypeDef(
    _ClientDescribeConfigurationRecordersResponseConfigurationRecordersTypeDef
):
    """
    Type definition for `ClientDescribeConfigurationRecordersResponse` `ConfigurationRecorders`

    An object that represents the recording of configuration changes of an AWS resource.

    - **name** *(string) --*

      The name of the recorder. By default, AWS Config automatically assigns the name "default"
      when creating the configuration recorder. You cannot change the assigned name.

    - **roleARN** *(string) --*

      Amazon Resource Name (ARN) of the IAM role used to describe the AWS resources associated
      with the account.

    - **recordingGroup** *(dict) --*

      Specifies the types of AWS resources for which AWS Config records configuration changes.

      - **allSupported** *(boolean) --*

        Specifies whether AWS Config records configuration changes for every supported type of
        regional resource.

        If you set this option to ``true`` , when AWS Config adds support for a new type of
        regional resource, it starts recording resources of that type automatically.

        If you set this option to ``true`` , you cannot enumerate a list of ``resourceTypes`` .

      - **includeGlobalResourceTypes** *(boolean) --*

        Specifies whether AWS Config includes all supported types of global resources (for
        example, IAM resources) with the resources that it records.

        Before you can set this option to ``true`` , you must set the ``allSupported`` option
        to ``true`` .

        If you set this option to ``true`` , when AWS Config adds support for a new type of
        global resource, it starts recording resources of that type automatically.

        The configuration details for any global resource are the same in all regions. To
        prevent duplicate configuration items, you should consider customizing AWS Config in
        only one region to record global resources.

      - **resourceTypes** *(list) --*

        A comma-separated list that specifies the types of AWS resources for which AWS Config
        records configuration changes (for example, ``AWS::EC2::Instance`` or
        ``AWS::CloudTrail::Trail`` ).

        Before you can set this option to ``true`` , you must set the ``allSupported`` option
        to ``false`` .

        If you set this option to ``true`` , when AWS Config adds support for a new type of
        resource, it will not record resources of that type unless you manually add that type
        to your recording group.

        For a list of valid ``resourceTypes`` values, see the **resourceType Value** column in
        `Supported AWS Resource Types
        <https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#supported-resources>`__
        .

        - *(string) --*
    """


_ClientDescribeConfigurationRecordersResponseTypeDef = TypedDict(
    "_ClientDescribeConfigurationRecordersResponseTypeDef",
    {
        "ConfigurationRecorders": List[
            ClientDescribeConfigurationRecordersResponseConfigurationRecordersTypeDef
        ]
    },
    total=False,
)


class ClientDescribeConfigurationRecordersResponseTypeDef(
    _ClientDescribeConfigurationRecordersResponseTypeDef
):
    """
    Type definition for `ClientDescribeConfigurationRecorders` `Response`

    The output for the  DescribeConfigurationRecorders action.

    - **ConfigurationRecorders** *(list) --*

      A list that contains the descriptions of the specified configuration recorders.

      - *(dict) --*

        An object that represents the recording of configuration changes of an AWS resource.

        - **name** *(string) --*

          The name of the recorder. By default, AWS Config automatically assigns the name "default"
          when creating the configuration recorder. You cannot change the assigned name.

        - **roleARN** *(string) --*

          Amazon Resource Name (ARN) of the IAM role used to describe the AWS resources associated
          with the account.

        - **recordingGroup** *(dict) --*

          Specifies the types of AWS resources for which AWS Config records configuration changes.

          - **allSupported** *(boolean) --*

            Specifies whether AWS Config records configuration changes for every supported type of
            regional resource.

            If you set this option to ``true`` , when AWS Config adds support for a new type of
            regional resource, it starts recording resources of that type automatically.

            If you set this option to ``true`` , you cannot enumerate a list of ``resourceTypes`` .

          - **includeGlobalResourceTypes** *(boolean) --*

            Specifies whether AWS Config includes all supported types of global resources (for
            example, IAM resources) with the resources that it records.

            Before you can set this option to ``true`` , you must set the ``allSupported`` option
            to ``true`` .

            If you set this option to ``true`` , when AWS Config adds support for a new type of
            global resource, it starts recording resources of that type automatically.

            The configuration details for any global resource are the same in all regions. To
            prevent duplicate configuration items, you should consider customizing AWS Config in
            only one region to record global resources.

          - **resourceTypes** *(list) --*

            A comma-separated list that specifies the types of AWS resources for which AWS Config
            records configuration changes (for example, ``AWS::EC2::Instance`` or
            ``AWS::CloudTrail::Trail`` ).

            Before you can set this option to ``true`` , you must set the ``allSupported`` option
            to ``false`` .

            If you set this option to ``true`` , when AWS Config adds support for a new type of
            resource, it will not record resources of that type unless you manually add that type
            to your recording group.

            For a list of valid ``resourceTypes`` values, see the **resourceType Value** column in
            `Supported AWS Resource Types
            <https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#supported-resources>`__
            .

            - *(string) --*
    """


_ClientDescribeConformancePackComplianceFiltersTypeDef = TypedDict(
    "_ClientDescribeConformancePackComplianceFiltersTypeDef",
    {"ConfigRuleNames": List[str], "ComplianceType": str},
    total=False,
)


class ClientDescribeConformancePackComplianceFiltersTypeDef(
    _ClientDescribeConformancePackComplianceFiltersTypeDef
):
    """
    Type definition for `ClientDescribeConformancePackCompliance` `Filters`

    A ``ConformancePackComplianceFilters`` object.

    - **ConfigRuleNames** *(list) --*

      Filters the results by AWS Config rule names.

      - *(string) --*

    - **ComplianceType** *(string) --*

      Filters the results by compliance.

      The allowed values are ``COMPLIANT`` and ``NON_COMPLIANT`` .
    """


_ClientDescribeConformancePackComplianceResponseConformancePackRuleComplianceListTypeDef = TypedDict(
    "_ClientDescribeConformancePackComplianceResponseConformancePackRuleComplianceListTypeDef",
    {"ConfigRuleName": str, "ComplianceType": str},
    total=False,
)


class ClientDescribeConformancePackComplianceResponseConformancePackRuleComplianceListTypeDef(
    _ClientDescribeConformancePackComplianceResponseConformancePackRuleComplianceListTypeDef
):
    """
    Type definition for `ClientDescribeConformancePackComplianceResponse` `ConformancePackRuleComplianceList`

    Compliance information of one or more AWS Config rules within a conformance pack. You can
    filter using AWS Config rule names and compliance types.

    - **ConfigRuleName** *(string) --*

      Filters the results by AWS Config rule name.

    - **ComplianceType** *(string) --*

      Filters the results by compliance.

      The allowed values are ``COMPLIANT`` and ``NON_COMPLIANT`` .
    """


_ClientDescribeConformancePackComplianceResponseTypeDef = TypedDict(
    "_ClientDescribeConformancePackComplianceResponseTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackRuleComplianceList": List[
            ClientDescribeConformancePackComplianceResponseConformancePackRuleComplianceListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeConformancePackComplianceResponseTypeDef(
    _ClientDescribeConformancePackComplianceResponseTypeDef
):
    """
    Type definition for `ClientDescribeConformancePackCompliance` `Response`

    - **ConformancePackName** *(string) --*

      Name of the conformance pack.

    - **ConformancePackRuleComplianceList** *(list) --*

      Returns a list of ``ConformancePackRuleCompliance`` objects.

      - *(dict) --*

        Compliance information of one or more AWS Config rules within a conformance pack. You can
        filter using AWS Config rule names and compliance types.

        - **ConfigRuleName** *(string) --*

          Filters the results by AWS Config rule name.

        - **ComplianceType** *(string) --*

          Filters the results by compliance.

          The allowed values are ``COMPLIANT`` and ``NON_COMPLIANT`` .

    - **NextToken** *(string) --*

      The ``nextToken`` string returned in a previous request that you use to request the next page
      of results in a paginated response.
    """


_ClientDescribeConformancePackStatusResponseConformancePackStatusDetailsTypeDef = TypedDict(
    "_ClientDescribeConformancePackStatusResponseConformancePackStatusDetailsTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackId": str,
        "ConformancePackArn": str,
        "ConformancePackState": str,
        "StackArn": str,
        "ConformancePackStatusReason": str,
        "LastUpdateRequestedTime": datetime,
        "LastUpdateCompletedTime": datetime,
    },
    total=False,
)


class ClientDescribeConformancePackStatusResponseConformancePackStatusDetailsTypeDef(
    _ClientDescribeConformancePackStatusResponseConformancePackStatusDetailsTypeDef
):
    """
    Type definition for `ClientDescribeConformancePackStatusResponse` `ConformancePackStatusDetails`

    Status details of a conformance pack.

    - **ConformancePackName** *(string) --*

      Name of the conformance pack.

    - **ConformancePackId** *(string) --*

      ID of the conformance pack.

    - **ConformancePackArn** *(string) --*

      Amazon Resource Name (ARN) of comformance pack.

    - **ConformancePackState** *(string) --*

      Indicates deployment status of conformance pack.

      AWS Config sets the state of the conformance pack to:

      * CREATE_IN_PROGRESS when a conformance pack creation is in progress for an account.

      * CREATE_COMPLETE when a conformance pack has been successfully created in your account.

      * CREATE_FAILED when a conformance pack creation failed in your account.

      * DELETE_IN_PROGRESS when a conformance pack deletion is in progress.

      * DELETE_FAILED when a conformance pack deletion failed from your account.

    - **StackArn** *(string) --*

      Amazon Resource Name (ARN) of AWS CloudFormation stack.

    - **ConformancePackStatusReason** *(string) --*

      The reason of conformance pack creation failure.

    - **LastUpdateRequestedTime** *(datetime) --*

      Last time when conformation pack creation and update was requested.

    - **LastUpdateCompletedTime** *(datetime) --*

      Last time when conformation pack creation and update was successful.
    """


_ClientDescribeConformancePackStatusResponseTypeDef = TypedDict(
    "_ClientDescribeConformancePackStatusResponseTypeDef",
    {
        "ConformancePackStatusDetails": List[
            ClientDescribeConformancePackStatusResponseConformancePackStatusDetailsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeConformancePackStatusResponseTypeDef(
    _ClientDescribeConformancePackStatusResponseTypeDef
):
    """
    Type definition for `ClientDescribeConformancePackStatus` `Response`

    - **ConformancePackStatusDetails** *(list) --*

      A list of ``ConformancePackStatusDetail`` objects.

      - *(dict) --*

        Status details of a conformance pack.

        - **ConformancePackName** *(string) --*

          Name of the conformance pack.

        - **ConformancePackId** *(string) --*

          ID of the conformance pack.

        - **ConformancePackArn** *(string) --*

          Amazon Resource Name (ARN) of comformance pack.

        - **ConformancePackState** *(string) --*

          Indicates deployment status of conformance pack.

          AWS Config sets the state of the conformance pack to:

          * CREATE_IN_PROGRESS when a conformance pack creation is in progress for an account.

          * CREATE_COMPLETE when a conformance pack has been successfully created in your account.

          * CREATE_FAILED when a conformance pack creation failed in your account.

          * DELETE_IN_PROGRESS when a conformance pack deletion is in progress.

          * DELETE_FAILED when a conformance pack deletion failed from your account.

        - **StackArn** *(string) --*

          Amazon Resource Name (ARN) of AWS CloudFormation stack.

        - **ConformancePackStatusReason** *(string) --*

          The reason of conformance pack creation failure.

        - **LastUpdateRequestedTime** *(datetime) --*

          Last time when conformation pack creation and update was requested.

        - **LastUpdateCompletedTime** *(datetime) --*

          Last time when conformation pack creation and update was successful.

    - **NextToken** *(string) --*

      The ``nextToken`` string returned in a previous request that you use to request the next page
      of results in a paginated response.
    """


_ClientDescribeConformancePacksResponseConformancePackDetailsConformancePackInputParametersTypeDef = TypedDict(
    "_ClientDescribeConformancePacksResponseConformancePackDetailsConformancePackInputParametersTypeDef",
    {"ParameterName": str, "ParameterValue": str},
    total=False,
)


class ClientDescribeConformancePacksResponseConformancePackDetailsConformancePackInputParametersTypeDef(
    _ClientDescribeConformancePacksResponseConformancePackDetailsConformancePackInputParametersTypeDef
):
    """
    Type definition for `ClientDescribeConformancePacksResponseConformancePackDetails` `ConformancePackInputParameters`

    Input parameters in the form of key-value pairs for the conformance pack, both of which
    you define. Keys can have a maximum character length of 128 characters, and values can
    have a maximum length of 256 characters.

    - **ParameterName** *(string) --*

      One part of a key-value pair.

    - **ParameterValue** *(string) --*

      Another part of the key-value pair.
    """


_ClientDescribeConformancePacksResponseConformancePackDetailsTypeDef = TypedDict(
    "_ClientDescribeConformancePacksResponseConformancePackDetailsTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackArn": str,
        "ConformancePackId": str,
        "DeliveryS3Bucket": str,
        "DeliveryS3KeyPrefix": str,
        "ConformancePackInputParameters": List[
            ClientDescribeConformancePacksResponseConformancePackDetailsConformancePackInputParametersTypeDef
        ],
        "LastUpdateRequestedTime": datetime,
        "CreatedBy": str,
    },
    total=False,
)


class ClientDescribeConformancePacksResponseConformancePackDetailsTypeDef(
    _ClientDescribeConformancePacksResponseConformancePackDetailsTypeDef
):
    """
    Type definition for `ClientDescribeConformancePacksResponse` `ConformancePackDetails`

    Returns details of a conformance pack. A conformance pack is a collection of AWS Config
    rules that can be easily deployed in an account and a region.

    - **ConformancePackName** *(string) --*

      Name of the conformance pack.

    - **ConformancePackArn** *(string) --*

      Amazon Resource Name (ARN) of the conformance pack.

    - **ConformancePackId** *(string) --*

      ID of the conformance pack.

    - **DeliveryS3Bucket** *(string) --*

      Location of an Amazon S3 bucket where AWS Config can deliver evaluation results and
      conformance pack template that is used to create a pack.

    - **DeliveryS3KeyPrefix** *(string) --*

      Any folder structure you want to add to an Amazon S3 bucket.

    - **ConformancePackInputParameters** *(list) --*

      A list of ``ConformancePackInputParameter`` objects.

      - *(dict) --*

        Input parameters in the form of key-value pairs for the conformance pack, both of which
        you define. Keys can have a maximum character length of 128 characters, and values can
        have a maximum length of 256 characters.

        - **ParameterName** *(string) --*

          One part of a key-value pair.

        - **ParameterValue** *(string) --*

          Another part of the key-value pair.

    - **LastUpdateRequestedTime** *(datetime) --*

      Last time when conformation pack update was requested.

    - **CreatedBy** *(string) --*
    """


_ClientDescribeConformancePacksResponseTypeDef = TypedDict(
    "_ClientDescribeConformancePacksResponseTypeDef",
    {
        "ConformancePackDetails": List[
            ClientDescribeConformancePacksResponseConformancePackDetailsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeConformancePacksResponseTypeDef(
    _ClientDescribeConformancePacksResponseTypeDef
):
    """
    Type definition for `ClientDescribeConformancePacks` `Response`

    - **ConformancePackDetails** *(list) --*

      Returns a list of ``ConformancePackDetail`` objects.

      - *(dict) --*

        Returns details of a conformance pack. A conformance pack is a collection of AWS Config
        rules that can be easily deployed in an account and a region.

        - **ConformancePackName** *(string) --*

          Name of the conformance pack.

        - **ConformancePackArn** *(string) --*

          Amazon Resource Name (ARN) of the conformance pack.

        - **ConformancePackId** *(string) --*

          ID of the conformance pack.

        - **DeliveryS3Bucket** *(string) --*

          Location of an Amazon S3 bucket where AWS Config can deliver evaluation results and
          conformance pack template that is used to create a pack.

        - **DeliveryS3KeyPrefix** *(string) --*

          Any folder structure you want to add to an Amazon S3 bucket.

        - **ConformancePackInputParameters** *(list) --*

          A list of ``ConformancePackInputParameter`` objects.

          - *(dict) --*

            Input parameters in the form of key-value pairs for the conformance pack, both of which
            you define. Keys can have a maximum character length of 128 characters, and values can
            have a maximum length of 256 characters.

            - **ParameterName** *(string) --*

              One part of a key-value pair.

            - **ParameterValue** *(string) --*

              Another part of the key-value pair.

        - **LastUpdateRequestedTime** *(datetime) --*

          Last time when conformation pack update was requested.

        - **CreatedBy** *(string) --*

    - **NextToken** *(string) --*

      The ``nextToken`` string returned in a previous request that you use to request the next page
      of results in a paginated response.
    """


_ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigHistoryDeliveryInfoTypeDef = TypedDict(
    "_ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigHistoryDeliveryInfoTypeDef",
    {
        "lastStatus": str,
        "lastErrorCode": str,
        "lastErrorMessage": str,
        "lastAttemptTime": datetime,
        "lastSuccessfulTime": datetime,
        "nextDeliveryTime": datetime,
    },
    total=False,
)


class ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigHistoryDeliveryInfoTypeDef(
    _ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigHistoryDeliveryInfoTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatus` `configHistoryDeliveryInfo`

    A list that contains the status of the delivery of the configuration history to the
    specified Amazon S3 bucket.

    - **lastStatus** *(string) --*

      Status of the last attempted delivery.

    - **lastErrorCode** *(string) --*

      The error code from the last attempted delivery.

    - **lastErrorMessage** *(string) --*

      The error message from the last attempted delivery.

    - **lastAttemptTime** *(datetime) --*

      The time of the last attempted delivery.

    - **lastSuccessfulTime** *(datetime) --*

      The time of the last successful delivery.

    - **nextDeliveryTime** *(datetime) --*

      The time that the next delivery occurs.
    """


_ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigSnapshotDeliveryInfoTypeDef = TypedDict(
    "_ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigSnapshotDeliveryInfoTypeDef",
    {
        "lastStatus": str,
        "lastErrorCode": str,
        "lastErrorMessage": str,
        "lastAttemptTime": datetime,
        "lastSuccessfulTime": datetime,
        "nextDeliveryTime": datetime,
    },
    total=False,
)


class ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigSnapshotDeliveryInfoTypeDef(
    _ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigSnapshotDeliveryInfoTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatus` `configSnapshotDeliveryInfo`

    A list containing the status of the delivery of the snapshot to the specified Amazon S3
    bucket.

    - **lastStatus** *(string) --*

      Status of the last attempted delivery.

    - **lastErrorCode** *(string) --*

      The error code from the last attempted delivery.

    - **lastErrorMessage** *(string) --*

      The error message from the last attempted delivery.

    - **lastAttemptTime** *(datetime) --*

      The time of the last attempted delivery.

    - **lastSuccessfulTime** *(datetime) --*

      The time of the last successful delivery.

    - **nextDeliveryTime** *(datetime) --*

      The time that the next delivery occurs.
    """


_ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigStreamDeliveryInfoTypeDef = TypedDict(
    "_ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigStreamDeliveryInfoTypeDef",
    {
        "lastStatus": str,
        "lastErrorCode": str,
        "lastErrorMessage": str,
        "lastStatusChangeTime": datetime,
    },
    total=False,
)


class ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigStreamDeliveryInfoTypeDef(
    _ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigStreamDeliveryInfoTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatus` `configStreamDeliveryInfo`

    A list containing the status of the delivery of the configuration stream notification to
    the specified Amazon SNS topic.

    - **lastStatus** *(string) --*

      Status of the last attempted delivery.

       **Note** Providing an SNS topic on a `DeliveryChannel
       <https://docs.aws.amazon.com/config/latest/APIReference/API_DeliveryChannel.html>`__
       for AWS Config is optional. If the SNS delivery is turned off, the last status will be
       **Not_Applicable** .

    - **lastErrorCode** *(string) --*

      The error code from the last attempted delivery.

    - **lastErrorMessage** *(string) --*

      The error message from the last attempted delivery.

    - **lastStatusChangeTime** *(datetime) --*

      The time from the last status change.
    """


_ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusTypeDef = TypedDict(
    "_ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusTypeDef",
    {
        "name": str,
        "configSnapshotDeliveryInfo": ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigSnapshotDeliveryInfoTypeDef,
        "configHistoryDeliveryInfo": ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigHistoryDeliveryInfoTypeDef,
        "configStreamDeliveryInfo": ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusconfigStreamDeliveryInfoTypeDef,
    },
    total=False,
)


class ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusTypeDef(
    _ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryChannelStatusResponse` `DeliveryChannelsStatus`

    The status of a specified delivery channel.

    Valid values: ``Success`` | ``Failure``

    - **name** *(string) --*

      The name of the delivery channel.

    - **configSnapshotDeliveryInfo** *(dict) --*

      A list containing the status of the delivery of the snapshot to the specified Amazon S3
      bucket.

      - **lastStatus** *(string) --*

        Status of the last attempted delivery.

      - **lastErrorCode** *(string) --*

        The error code from the last attempted delivery.

      - **lastErrorMessage** *(string) --*

        The error message from the last attempted delivery.

      - **lastAttemptTime** *(datetime) --*

        The time of the last attempted delivery.

      - **lastSuccessfulTime** *(datetime) --*

        The time of the last successful delivery.

      - **nextDeliveryTime** *(datetime) --*

        The time that the next delivery occurs.

    - **configHistoryDeliveryInfo** *(dict) --*

      A list that contains the status of the delivery of the configuration history to the
      specified Amazon S3 bucket.

      - **lastStatus** *(string) --*

        Status of the last attempted delivery.

      - **lastErrorCode** *(string) --*

        The error code from the last attempted delivery.

      - **lastErrorMessage** *(string) --*

        The error message from the last attempted delivery.

      - **lastAttemptTime** *(datetime) --*

        The time of the last attempted delivery.

      - **lastSuccessfulTime** *(datetime) --*

        The time of the last successful delivery.

      - **nextDeliveryTime** *(datetime) --*

        The time that the next delivery occurs.

    - **configStreamDeliveryInfo** *(dict) --*

      A list containing the status of the delivery of the configuration stream notification to
      the specified Amazon SNS topic.

      - **lastStatus** *(string) --*

        Status of the last attempted delivery.

         **Note** Providing an SNS topic on a `DeliveryChannel
         <https://docs.aws.amazon.com/config/latest/APIReference/API_DeliveryChannel.html>`__
         for AWS Config is optional. If the SNS delivery is turned off, the last status will be
         **Not_Applicable** .

      - **lastErrorCode** *(string) --*

        The error code from the last attempted delivery.

      - **lastErrorMessage** *(string) --*

        The error message from the last attempted delivery.

      - **lastStatusChangeTime** *(datetime) --*

        The time from the last status change.
    """


_ClientDescribeDeliveryChannelStatusResponseTypeDef = TypedDict(
    "_ClientDescribeDeliveryChannelStatusResponseTypeDef",
    {
        "DeliveryChannelsStatus": List[
            ClientDescribeDeliveryChannelStatusResponseDeliveryChannelsStatusTypeDef
        ]
    },
    total=False,
)


class ClientDescribeDeliveryChannelStatusResponseTypeDef(
    _ClientDescribeDeliveryChannelStatusResponseTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryChannelStatus` `Response`

    The output for the  DescribeDeliveryChannelStatus action.

    - **DeliveryChannelsStatus** *(list) --*

      A list that contains the status of a specified delivery channel.

      - *(dict) --*

        The status of a specified delivery channel.

        Valid values: ``Success`` | ``Failure``

        - **name** *(string) --*

          The name of the delivery channel.

        - **configSnapshotDeliveryInfo** *(dict) --*

          A list containing the status of the delivery of the snapshot to the specified Amazon S3
          bucket.

          - **lastStatus** *(string) --*

            Status of the last attempted delivery.

          - **lastErrorCode** *(string) --*

            The error code from the last attempted delivery.

          - **lastErrorMessage** *(string) --*

            The error message from the last attempted delivery.

          - **lastAttemptTime** *(datetime) --*

            The time of the last attempted delivery.

          - **lastSuccessfulTime** *(datetime) --*

            The time of the last successful delivery.

          - **nextDeliveryTime** *(datetime) --*

            The time that the next delivery occurs.

        - **configHistoryDeliveryInfo** *(dict) --*

          A list that contains the status of the delivery of the configuration history to the
          specified Amazon S3 bucket.

          - **lastStatus** *(string) --*

            Status of the last attempted delivery.

          - **lastErrorCode** *(string) --*

            The error code from the last attempted delivery.

          - **lastErrorMessage** *(string) --*

            The error message from the last attempted delivery.

          - **lastAttemptTime** *(datetime) --*

            The time of the last attempted delivery.

          - **lastSuccessfulTime** *(datetime) --*

            The time of the last successful delivery.

          - **nextDeliveryTime** *(datetime) --*

            The time that the next delivery occurs.

        - **configStreamDeliveryInfo** *(dict) --*

          A list containing the status of the delivery of the configuration stream notification to
          the specified Amazon SNS topic.

          - **lastStatus** *(string) --*

            Status of the last attempted delivery.

             **Note** Providing an SNS topic on a `DeliveryChannel
             <https://docs.aws.amazon.com/config/latest/APIReference/API_DeliveryChannel.html>`__
             for AWS Config is optional. If the SNS delivery is turned off, the last status will be
             **Not_Applicable** .

          - **lastErrorCode** *(string) --*

            The error code from the last attempted delivery.

          - **lastErrorMessage** *(string) --*

            The error message from the last attempted delivery.

          - **lastStatusChangeTime** *(datetime) --*

            The time from the last status change.
    """


_ClientDescribeDeliveryChannelsResponseDeliveryChannelsconfigSnapshotDeliveryPropertiesTypeDef = TypedDict(
    "_ClientDescribeDeliveryChannelsResponseDeliveryChannelsconfigSnapshotDeliveryPropertiesTypeDef",
    {"deliveryFrequency": str},
    total=False,
)


class ClientDescribeDeliveryChannelsResponseDeliveryChannelsconfigSnapshotDeliveryPropertiesTypeDef(
    _ClientDescribeDeliveryChannelsResponseDeliveryChannelsconfigSnapshotDeliveryPropertiesTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryChannelsResponseDeliveryChannels` `configSnapshotDeliveryProperties`

    The options for how often AWS Config delivers configuration snapshots to the Amazon S3
    bucket.

    - **deliveryFrequency** *(string) --*

      The frequency with which AWS Config delivers configuration snapshots.
    """


_ClientDescribeDeliveryChannelsResponseDeliveryChannelsTypeDef = TypedDict(
    "_ClientDescribeDeliveryChannelsResponseDeliveryChannelsTypeDef",
    {
        "name": str,
        "s3BucketName": str,
        "s3KeyPrefix": str,
        "snsTopicARN": str,
        "configSnapshotDeliveryProperties": ClientDescribeDeliveryChannelsResponseDeliveryChannelsconfigSnapshotDeliveryPropertiesTypeDef,
    },
    total=False,
)


class ClientDescribeDeliveryChannelsResponseDeliveryChannelsTypeDef(
    _ClientDescribeDeliveryChannelsResponseDeliveryChannelsTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryChannelsResponse` `DeliveryChannels`

    The channel through which AWS Config delivers notifications and updated configuration
    states.

    - **name** *(string) --*

      The name of the delivery channel. By default, AWS Config assigns the name "default" when
      creating the delivery channel. To change the delivery channel name, you must use the
      DeleteDeliveryChannel action to delete your current delivery channel, and then you must
      use the PutDeliveryChannel command to create a delivery channel that has the desired name.

    - **s3BucketName** *(string) --*

      The name of the Amazon S3 bucket to which AWS Config delivers configuration snapshots and
      configuration history files.

      If you specify a bucket that belongs to another AWS account, that bucket must have
      policies that grant access permissions to AWS Config. For more information, see
      `Permissions for the Amazon S3 Bucket
      <https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-policy.html>`__ in
      the AWS Config Developer Guide.

    - **s3KeyPrefix** *(string) --*

      The prefix for the specified Amazon S3 bucket.

    - **snsTopicARN** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon SNS topic to which AWS Config sends
      notifications about configuration changes.

      If you choose a topic from another account, the topic must have policies that grant
      access permissions to AWS Config. For more information, see `Permissions for the Amazon
      SNS Topic
      <https://docs.aws.amazon.com/config/latest/developerguide/sns-topic-policy.html>`__ in
      the AWS Config Developer Guide.

    - **configSnapshotDeliveryProperties** *(dict) --*

      The options for how often AWS Config delivers configuration snapshots to the Amazon S3
      bucket.

      - **deliveryFrequency** *(string) --*

        The frequency with which AWS Config delivers configuration snapshots.
    """


_ClientDescribeDeliveryChannelsResponseTypeDef = TypedDict(
    "_ClientDescribeDeliveryChannelsResponseTypeDef",
    {
        "DeliveryChannels": List[
            ClientDescribeDeliveryChannelsResponseDeliveryChannelsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeDeliveryChannelsResponseTypeDef(
    _ClientDescribeDeliveryChannelsResponseTypeDef
):
    """
    Type definition for `ClientDescribeDeliveryChannels` `Response`

    The output for the  DescribeDeliveryChannels action.

    - **DeliveryChannels** *(list) --*

      A list that contains the descriptions of the specified delivery channel.

      - *(dict) --*

        The channel through which AWS Config delivers notifications and updated configuration
        states.

        - **name** *(string) --*

          The name of the delivery channel. By default, AWS Config assigns the name "default" when
          creating the delivery channel. To change the delivery channel name, you must use the
          DeleteDeliveryChannel action to delete your current delivery channel, and then you must
          use the PutDeliveryChannel command to create a delivery channel that has the desired name.

        - **s3BucketName** *(string) --*

          The name of the Amazon S3 bucket to which AWS Config delivers configuration snapshots and
          configuration history files.

          If you specify a bucket that belongs to another AWS account, that bucket must have
          policies that grant access permissions to AWS Config. For more information, see
          `Permissions for the Amazon S3 Bucket
          <https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-policy.html>`__ in
          the AWS Config Developer Guide.

        - **s3KeyPrefix** *(string) --*

          The prefix for the specified Amazon S3 bucket.

        - **snsTopicARN** *(string) --*

          The Amazon Resource Name (ARN) of the Amazon SNS topic to which AWS Config sends
          notifications about configuration changes.

          If you choose a topic from another account, the topic must have policies that grant
          access permissions to AWS Config. For more information, see `Permissions for the Amazon
          SNS Topic
          <https://docs.aws.amazon.com/config/latest/developerguide/sns-topic-policy.html>`__ in
          the AWS Config Developer Guide.

        - **configSnapshotDeliveryProperties** *(dict) --*

          The options for how often AWS Config delivers configuration snapshots to the Amazon S3
          bucket.

          - **deliveryFrequency** *(string) --*

            The frequency with which AWS Config delivers configuration snapshots.
    """


_ClientDescribeOrganizationConfigRuleStatusesResponseOrganizationConfigRuleStatusesTypeDef = TypedDict(
    "_ClientDescribeOrganizationConfigRuleStatusesResponseOrganizationConfigRuleStatusesTypeDef",
    {
        "OrganizationConfigRuleName": str,
        "OrganizationRuleStatus": str,
        "ErrorCode": str,
        "ErrorMessage": str,
        "LastUpdateTime": datetime,
    },
    total=False,
)


class ClientDescribeOrganizationConfigRuleStatusesResponseOrganizationConfigRuleStatusesTypeDef(
    _ClientDescribeOrganizationConfigRuleStatusesResponseOrganizationConfigRuleStatusesTypeDef
):
    """
    Type definition for `ClientDescribeOrganizationConfigRuleStatusesResponse` `OrganizationConfigRuleStatuses`

    Returns the status for an organization config rule in an organization.

    - **OrganizationConfigRuleName** *(string) --*

      The name that you assign to organization config rule.

    - **OrganizationRuleStatus** *(string) --*

      Indicates deployment status of an organization config rule. When master account calls
      PutOrganizationConfigRule action for the first time, config rule status is created in all
      the member accounts. When master account calls PutOrganizationConfigRule action for the
      second time, config rule status is updated in all the member accounts. Additionally,
      config rule status is updated when one or more member accounts join or leave an
      organization. Config rule status is deleted when the master account deletes
      OrganizationConfigRule in all the member accounts and disables service access for
      ``config-multiaccountsetup.amazonaws.com`` .

      AWS Config sets the state of the rule to:

      * ``CREATE_SUCCESSFUL`` when an organization config rule has been successfully created in
      all the member accounts.

      * ``CREATE_IN_PROGRESS`` when an organization config rule creation is in progress.

      * ``CREATE_FAILED`` when an organization config rule creation failed in one or more
      member accounts within that organization.

      * ``DELETE_FAILED`` when an organization config rule deletion failed in one or more
      member accounts within that organization.

      * ``DELETE_IN_PROGRESS`` when an organization config rule deletion is in progress.

      * ``DELETE_SUCCESSFUL`` when an organization config rule has been successfully deleted
      from all the member accounts.

      * ``UPDATE_SUCCESSFUL`` when an organization config rule has been successfully updated in
      all the member accounts.

      * ``UPDATE_IN_PROGRESS`` when an organization config rule update is in progress.

      * ``UPDATE_FAILED`` when an organization config rule update failed in one or more member
      accounts within that organization.

    - **ErrorCode** *(string) --*

      An error code that is returned when organization config rule creation or deletion has
      failed.

    - **ErrorMessage** *(string) --*

      An error message indicating that organization config rule creation or deletion failed due
      to an error.

    - **LastUpdateTime** *(datetime) --*

      The timestamp of the last update.
    """


_ClientDescribeOrganizationConfigRuleStatusesResponseTypeDef = TypedDict(
    "_ClientDescribeOrganizationConfigRuleStatusesResponseTypeDef",
    {
        "OrganizationConfigRuleStatuses": List[
            ClientDescribeOrganizationConfigRuleStatusesResponseOrganizationConfigRuleStatusesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeOrganizationConfigRuleStatusesResponseTypeDef(
    _ClientDescribeOrganizationConfigRuleStatusesResponseTypeDef
):
    """
    Type definition for `ClientDescribeOrganizationConfigRuleStatuses` `Response`

    - **OrganizationConfigRuleStatuses** *(list) --*

      A list of ``OrganizationConfigRuleStatus`` objects.

      - *(dict) --*

        Returns the status for an organization config rule in an organization.

        - **OrganizationConfigRuleName** *(string) --*

          The name that you assign to organization config rule.

        - **OrganizationRuleStatus** *(string) --*

          Indicates deployment status of an organization config rule. When master account calls
          PutOrganizationConfigRule action for the first time, config rule status is created in all
          the member accounts. When master account calls PutOrganizationConfigRule action for the
          second time, config rule status is updated in all the member accounts. Additionally,
          config rule status is updated when one or more member accounts join or leave an
          organization. Config rule status is deleted when the master account deletes
          OrganizationConfigRule in all the member accounts and disables service access for
          ``config-multiaccountsetup.amazonaws.com`` .

          AWS Config sets the state of the rule to:

          * ``CREATE_SUCCESSFUL`` when an organization config rule has been successfully created in
          all the member accounts.

          * ``CREATE_IN_PROGRESS`` when an organization config rule creation is in progress.

          * ``CREATE_FAILED`` when an organization config rule creation failed in one or more
          member accounts within that organization.

          * ``DELETE_FAILED`` when an organization config rule deletion failed in one or more
          member accounts within that organization.

          * ``DELETE_IN_PROGRESS`` when an organization config rule deletion is in progress.

          * ``DELETE_SUCCESSFUL`` when an organization config rule has been successfully deleted
          from all the member accounts.

          * ``UPDATE_SUCCESSFUL`` when an organization config rule has been successfully updated in
          all the member accounts.

          * ``UPDATE_IN_PROGRESS`` when an organization config rule update is in progress.

          * ``UPDATE_FAILED`` when an organization config rule update failed in one or more member
          accounts within that organization.

        - **ErrorCode** *(string) --*

          An error code that is returned when organization config rule creation or deletion has
          failed.

        - **ErrorMessage** *(string) --*

          An error message indicating that organization config rule creation or deletion failed due
          to an error.

        - **LastUpdateTime** *(datetime) --*

          The timestamp of the last update.

    - **NextToken** *(string) --*

      The ``nextToken`` string returned on a previous page that you use to get the next page of
      results in a paginated response.
    """


_ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesOrganizationCustomRuleMetadataTypeDef = TypedDict(
    "_ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesOrganizationCustomRuleMetadataTypeDef",
    {
        "Description": str,
        "LambdaFunctionArn": str,
        "OrganizationConfigRuleTriggerTypes": List[str],
        "InputParameters": str,
        "MaximumExecutionFrequency": str,
        "ResourceTypesScope": List[str],
        "ResourceIdScope": str,
        "TagKeyScope": str,
        "TagValueScope": str,
    },
    total=False,
)


class ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesOrganizationCustomRuleMetadataTypeDef(
    _ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesOrganizationCustomRuleMetadataTypeDef
):
    """
    Type definition for `ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRules` `OrganizationCustomRuleMetadata`

    An ``OrganizationCustomRuleMetadata`` object.

    - **Description** *(string) --*

      The description that you provide for organization config rule.

    - **LambdaFunctionArn** *(string) --*

      The lambda function ARN.

    - **OrganizationConfigRuleTriggerTypes** *(list) --*

      The type of notification that triggers AWS Config to run an evaluation for a rule. You
      can specify the following notification types:

      * ``ConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config
      delivers a configuration item as a result of a resource change.

      * ``OversizedConfigurationItemChangeNotification`` - Triggers an evaluation when AWS
      Config delivers an oversized configuration item. AWS Config may generate this
      notification type when a resource changes and the notification exceeds the maximum size
      allowed by Amazon SNS.

      * ``ScheduledNotification`` - Triggers a periodic evaluation at the frequency specified
      for ``MaximumExecutionFrequency`` .

      - *(string) --*

    - **InputParameters** *(string) --*

      A string, in JSON format, that is passed to organization config rule Lambda function.

    - **MaximumExecutionFrequency** *(string) --*

      The maximum frequency with which AWS Config runs evaluations for a rule. Your custom
      rule is triggered when AWS Config delivers the configuration snapshot. For more
      information, see  ConfigSnapshotDeliveryProperties .

      .. note::

        By default, rules with a periodic trigger are evaluated every 24 hours. To change the
        frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.

    - **ResourceTypesScope** *(list) --*

      The type of the AWS resource that was evaluated.

      - *(string) --*

    - **ResourceIdScope** *(string) --*

      The ID of the AWS resource that was evaluated.

    - **TagKeyScope** *(string) --*

      One part of a key-value pair that make up a tag. A key is a general label that acts
      like a category for more specific tag values.

    - **TagValueScope** *(string) --*

      The optional part of a key-value pair that make up a tag. A value acts as a descriptor
      within a tag category (key).
    """


_ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesOrganizationManagedRuleMetadataTypeDef = TypedDict(
    "_ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesOrganizationManagedRuleMetadataTypeDef",
    {
        "Description": str,
        "RuleIdentifier": str,
        "InputParameters": str,
        "MaximumExecutionFrequency": str,
        "ResourceTypesScope": List[str],
        "ResourceIdScope": str,
        "TagKeyScope": str,
        "TagValueScope": str,
    },
    total=False,
)


class ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesOrganizationManagedRuleMetadataTypeDef(
    _ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesOrganizationManagedRuleMetadataTypeDef
):
    """
    Type definition for `ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRules` `OrganizationManagedRuleMetadata`

    An ``OrganizationManagedRuleMetadata`` object.

    - **Description** *(string) --*

      The description that you provide for organization config rule.

    - **RuleIdentifier** *(string) --*

      For organization config managed rules, a predefined identifier from a list. For
      example, ``IAM_PASSWORD_POLICY`` is a managed rule. To reference a managed rule, see
      `Using AWS Managed Config Rules
      <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html>`__
      .

    - **InputParameters** *(string) --*

      A string, in JSON format, that is passed to organization config rule Lambda function.

    - **MaximumExecutionFrequency** *(string) --*

      The maximum frequency with which AWS Config runs evaluations for a rule. You are using
      an AWS managed rule that is triggered at a periodic frequency.

      .. note::

        By default, rules with a periodic trigger are evaluated every 24 hours. To change the
        frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.

    - **ResourceTypesScope** *(list) --*

      The type of the AWS resource that was evaluated.

      - *(string) --*

    - **ResourceIdScope** *(string) --*

      The ID of the AWS resource that was evaluated.

    - **TagKeyScope** *(string) --*

      One part of a key-value pair that make up a tag. A key is a general label that acts
      like a category for more specific tag values.

    - **TagValueScope** *(string) --*

      The optional part of a key-value pair that make up a tag. A value acts as a descriptor
      within a tag category (key).
    """


_ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesTypeDef = TypedDict(
    "_ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesTypeDef",
    {
        "OrganizationConfigRuleName": str,
        "OrganizationConfigRuleArn": str,
        "OrganizationManagedRuleMetadata": ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesOrganizationManagedRuleMetadataTypeDef,
        "OrganizationCustomRuleMetadata": ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesOrganizationCustomRuleMetadataTypeDef,
        "ExcludedAccounts": List[str],
        "LastUpdateTime": datetime,
    },
    total=False,
)


class ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesTypeDef(
    _ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesTypeDef
):
    """
    Type definition for `ClientDescribeOrganizationConfigRulesResponse` `OrganizationConfigRules`

    An organization config rule that has information about config rules that AWS Config creates
    in member accounts.

    - **OrganizationConfigRuleName** *(string) --*

      The name that you assign to organization config rule.

    - **OrganizationConfigRuleArn** *(string) --*

      Amazon Resource Name (ARN) of organization config rule.

    - **OrganizationManagedRuleMetadata** *(dict) --*

      An ``OrganizationManagedRuleMetadata`` object.

      - **Description** *(string) --*

        The description that you provide for organization config rule.

      - **RuleIdentifier** *(string) --*

        For organization config managed rules, a predefined identifier from a list. For
        example, ``IAM_PASSWORD_POLICY`` is a managed rule. To reference a managed rule, see
        `Using AWS Managed Config Rules
        <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html>`__
        .

      - **InputParameters** *(string) --*

        A string, in JSON format, that is passed to organization config rule Lambda function.

      - **MaximumExecutionFrequency** *(string) --*

        The maximum frequency with which AWS Config runs evaluations for a rule. You are using
        an AWS managed rule that is triggered at a periodic frequency.

        .. note::

          By default, rules with a periodic trigger are evaluated every 24 hours. To change the
          frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.

      - **ResourceTypesScope** *(list) --*

        The type of the AWS resource that was evaluated.

        - *(string) --*

      - **ResourceIdScope** *(string) --*

        The ID of the AWS resource that was evaluated.

      - **TagKeyScope** *(string) --*

        One part of a key-value pair that make up a tag. A key is a general label that acts
        like a category for more specific tag values.

      - **TagValueScope** *(string) --*

        The optional part of a key-value pair that make up a tag. A value acts as a descriptor
        within a tag category (key).

    - **OrganizationCustomRuleMetadata** *(dict) --*

      An ``OrganizationCustomRuleMetadata`` object.

      - **Description** *(string) --*

        The description that you provide for organization config rule.

      - **LambdaFunctionArn** *(string) --*

        The lambda function ARN.

      - **OrganizationConfigRuleTriggerTypes** *(list) --*

        The type of notification that triggers AWS Config to run an evaluation for a rule. You
        can specify the following notification types:

        * ``ConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config
        delivers a configuration item as a result of a resource change.

        * ``OversizedConfigurationItemChangeNotification`` - Triggers an evaluation when AWS
        Config delivers an oversized configuration item. AWS Config may generate this
        notification type when a resource changes and the notification exceeds the maximum size
        allowed by Amazon SNS.

        * ``ScheduledNotification`` - Triggers a periodic evaluation at the frequency specified
        for ``MaximumExecutionFrequency`` .

        - *(string) --*

      - **InputParameters** *(string) --*

        A string, in JSON format, that is passed to organization config rule Lambda function.

      - **MaximumExecutionFrequency** *(string) --*

        The maximum frequency with which AWS Config runs evaluations for a rule. Your custom
        rule is triggered when AWS Config delivers the configuration snapshot. For more
        information, see  ConfigSnapshotDeliveryProperties .

        .. note::

          By default, rules with a periodic trigger are evaluated every 24 hours. To change the
          frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.

      - **ResourceTypesScope** *(list) --*

        The type of the AWS resource that was evaluated.

        - *(string) --*

      - **ResourceIdScope** *(string) --*

        The ID of the AWS resource that was evaluated.

      - **TagKeyScope** *(string) --*

        One part of a key-value pair that make up a tag. A key is a general label that acts
        like a category for more specific tag values.

      - **TagValueScope** *(string) --*

        The optional part of a key-value pair that make up a tag. A value acts as a descriptor
        within a tag category (key).

    - **ExcludedAccounts** *(list) --*

      A comma-separated list of accounts excluded from organization config rule.

      - *(string) --*

    - **LastUpdateTime** *(datetime) --*

      The timestamp of the last update.
    """


_ClientDescribeOrganizationConfigRulesResponseTypeDef = TypedDict(
    "_ClientDescribeOrganizationConfigRulesResponseTypeDef",
    {
        "OrganizationConfigRules": List[
            ClientDescribeOrganizationConfigRulesResponseOrganizationConfigRulesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeOrganizationConfigRulesResponseTypeDef(
    _ClientDescribeOrganizationConfigRulesResponseTypeDef
):
    """
    Type definition for `ClientDescribeOrganizationConfigRules` `Response`

    - **OrganizationConfigRules** *(list) --*

      Returns a list of ``OrganizationConfigRule`` objects.

      - *(dict) --*

        An organization config rule that has information about config rules that AWS Config creates
        in member accounts.

        - **OrganizationConfigRuleName** *(string) --*

          The name that you assign to organization config rule.

        - **OrganizationConfigRuleArn** *(string) --*

          Amazon Resource Name (ARN) of organization config rule.

        - **OrganizationManagedRuleMetadata** *(dict) --*

          An ``OrganizationManagedRuleMetadata`` object.

          - **Description** *(string) --*

            The description that you provide for organization config rule.

          - **RuleIdentifier** *(string) --*

            For organization config managed rules, a predefined identifier from a list. For
            example, ``IAM_PASSWORD_POLICY`` is a managed rule. To reference a managed rule, see
            `Using AWS Managed Config Rules
            <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html>`__
            .

          - **InputParameters** *(string) --*

            A string, in JSON format, that is passed to organization config rule Lambda function.

          - **MaximumExecutionFrequency** *(string) --*

            The maximum frequency with which AWS Config runs evaluations for a rule. You are using
            an AWS managed rule that is triggered at a periodic frequency.

            .. note::

              By default, rules with a periodic trigger are evaluated every 24 hours. To change the
              frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.

          - **ResourceTypesScope** *(list) --*

            The type of the AWS resource that was evaluated.

            - *(string) --*

          - **ResourceIdScope** *(string) --*

            The ID of the AWS resource that was evaluated.

          - **TagKeyScope** *(string) --*

            One part of a key-value pair that make up a tag. A key is a general label that acts
            like a category for more specific tag values.

          - **TagValueScope** *(string) --*

            The optional part of a key-value pair that make up a tag. A value acts as a descriptor
            within a tag category (key).

        - **OrganizationCustomRuleMetadata** *(dict) --*

          An ``OrganizationCustomRuleMetadata`` object.

          - **Description** *(string) --*

            The description that you provide for organization config rule.

          - **LambdaFunctionArn** *(string) --*

            The lambda function ARN.

          - **OrganizationConfigRuleTriggerTypes** *(list) --*

            The type of notification that triggers AWS Config to run an evaluation for a rule. You
            can specify the following notification types:

            * ``ConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config
            delivers a configuration item as a result of a resource change.

            * ``OversizedConfigurationItemChangeNotification`` - Triggers an evaluation when AWS
            Config delivers an oversized configuration item. AWS Config may generate this
            notification type when a resource changes and the notification exceeds the maximum size
            allowed by Amazon SNS.

            * ``ScheduledNotification`` - Triggers a periodic evaluation at the frequency specified
            for ``MaximumExecutionFrequency`` .

            - *(string) --*

          - **InputParameters** *(string) --*

            A string, in JSON format, that is passed to organization config rule Lambda function.

          - **MaximumExecutionFrequency** *(string) --*

            The maximum frequency with which AWS Config runs evaluations for a rule. Your custom
            rule is triggered when AWS Config delivers the configuration snapshot. For more
            information, see  ConfigSnapshotDeliveryProperties .

            .. note::

              By default, rules with a periodic trigger are evaluated every 24 hours. To change the
              frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.

          - **ResourceTypesScope** *(list) --*

            The type of the AWS resource that was evaluated.

            - *(string) --*

          - **ResourceIdScope** *(string) --*

            The ID of the AWS resource that was evaluated.

          - **TagKeyScope** *(string) --*

            One part of a key-value pair that make up a tag. A key is a general label that acts
            like a category for more specific tag values.

          - **TagValueScope** *(string) --*

            The optional part of a key-value pair that make up a tag. A value acts as a descriptor
            within a tag category (key).

        - **ExcludedAccounts** *(list) --*

          A comma-separated list of accounts excluded from organization config rule.

          - *(string) --*

        - **LastUpdateTime** *(datetime) --*

          The timestamp of the last update.

    - **NextToken** *(string) --*

      The ``nextToken`` string returned on a previous page that you use to get the next page of
      results in a paginated response.
    """


_ClientDescribeOrganizationConformancePackStatusesResponseOrganizationConformancePackStatusesTypeDef = TypedDict(
    "_ClientDescribeOrganizationConformancePackStatusesResponseOrganizationConformancePackStatusesTypeDef",
    {
        "OrganizationConformancePackName": str,
        "Status": str,
        "ErrorCode": str,
        "ErrorMessage": str,
        "LastUpdateTime": datetime,
    },
    total=False,
)


class ClientDescribeOrganizationConformancePackStatusesResponseOrganizationConformancePackStatusesTypeDef(
    _ClientDescribeOrganizationConformancePackStatusesResponseOrganizationConformancePackStatusesTypeDef
):
    """
    Type definition for `ClientDescribeOrganizationConformancePackStatusesResponse` `OrganizationConformancePackStatuses`

    Returns the status for an organization conformance pack in an organization.

    - **OrganizationConformancePackName** *(string) --*

      The name that you assign to organization conformance pack.

    - **Status** *(string) --*

      Indicates deployment status of an organization conformance pack. When master account
      calls PutOrganizationConformancePack for the first time, conformance pack status is
      created in all the member accounts. When master account calls
      PutOrganizationConformancePack for the second time, conformance pack status is updated in
      all the member accounts. Additionally, conformance pack status is updated when one or
      more member accounts join or leave an organization. Conformance pack status is deleted
      when the master account deletes OrganizationConformancePack in all the member accounts
      and disables service access for ``config-multiaccountsetup.amazonaws.com`` .

      AWS Config sets the state of the conformance pack to:

      * ``CREATE_SUCCESSFUL`` when an organization conformance pack has been successfully
      created in all the member accounts.

      * ``CREATE_IN_PROGRESS`` when an organization conformance pack creation is in progress.

      * ``CREATE_FAILED`` when an organization conformance pack creation failed in one or more
      member accounts within that organization.

      * ``DELETE_FAILED`` when an organization conformance pack deletion failed in one or more
      member accounts within that organization.

      * ``DELETE_IN_PROGRESS`` when an organization conformance pack deletion is in progress.

      * ``DELETE_SUCCESSFUL`` when an organization conformance pack has been successfully
      deleted from all the member accounts.

      * ``UPDATE_SUCCESSFUL`` when an organization conformance pack has been successfully
      updated in all the member accounts.

      * ``UPDATE_IN_PROGRESS`` when an organization conformance pack update is in progress.

      * ``UPDATE_FAILED`` when an organization conformance pack update failed in one or more
      member accounts within that organization.

    - **ErrorCode** *(string) --*

      An error code that is returned when organization conformance pack creation or deletion
      has failed in the member account.

    - **ErrorMessage** *(string) --*

      An error message indicating that organization conformance pack creation or deletion
      failed due to an error.

    - **LastUpdateTime** *(datetime) --*

      The timestamp of the last update.
    """


_ClientDescribeOrganizationConformancePackStatusesResponseTypeDef = TypedDict(
    "_ClientDescribeOrganizationConformancePackStatusesResponseTypeDef",
    {
        "OrganizationConformancePackStatuses": List[
            ClientDescribeOrganizationConformancePackStatusesResponseOrganizationConformancePackStatusesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeOrganizationConformancePackStatusesResponseTypeDef(
    _ClientDescribeOrganizationConformancePackStatusesResponseTypeDef
):
    """
    Type definition for `ClientDescribeOrganizationConformancePackStatuses` `Response`

    - **OrganizationConformancePackStatuses** *(list) --*

      A list of ``OrganizationConformancePackStatus`` objects.

      - *(dict) --*

        Returns the status for an organization conformance pack in an organization.

        - **OrganizationConformancePackName** *(string) --*

          The name that you assign to organization conformance pack.

        - **Status** *(string) --*

          Indicates deployment status of an organization conformance pack. When master account
          calls PutOrganizationConformancePack for the first time, conformance pack status is
          created in all the member accounts. When master account calls
          PutOrganizationConformancePack for the second time, conformance pack status is updated in
          all the member accounts. Additionally, conformance pack status is updated when one or
          more member accounts join or leave an organization. Conformance pack status is deleted
          when the master account deletes OrganizationConformancePack in all the member accounts
          and disables service access for ``config-multiaccountsetup.amazonaws.com`` .

          AWS Config sets the state of the conformance pack to:

          * ``CREATE_SUCCESSFUL`` when an organization conformance pack has been successfully
          created in all the member accounts.

          * ``CREATE_IN_PROGRESS`` when an organization conformance pack creation is in progress.

          * ``CREATE_FAILED`` when an organization conformance pack creation failed in one or more
          member accounts within that organization.

          * ``DELETE_FAILED`` when an organization conformance pack deletion failed in one or more
          member accounts within that organization.

          * ``DELETE_IN_PROGRESS`` when an organization conformance pack deletion is in progress.

          * ``DELETE_SUCCESSFUL`` when an organization conformance pack has been successfully
          deleted from all the member accounts.

          * ``UPDATE_SUCCESSFUL`` when an organization conformance pack has been successfully
          updated in all the member accounts.

          * ``UPDATE_IN_PROGRESS`` when an organization conformance pack update is in progress.

          * ``UPDATE_FAILED`` when an organization conformance pack update failed in one or more
          member accounts within that organization.

        - **ErrorCode** *(string) --*

          An error code that is returned when organization conformance pack creation or deletion
          has failed in the member account.

        - **ErrorMessage** *(string) --*

          An error message indicating that organization conformance pack creation or deletion
          failed due to an error.

        - **LastUpdateTime** *(datetime) --*

          The timestamp of the last update.

    - **NextToken** *(string) --*

      The nextToken string returned on a previous page that you use to get the next page of results
      in a paginated response.
    """


_ClientDescribeOrganizationConformancePacksResponseOrganizationConformancePacksConformancePackInputParametersTypeDef = TypedDict(
    "_ClientDescribeOrganizationConformancePacksResponseOrganizationConformancePacksConformancePackInputParametersTypeDef",
    {"ParameterName": str, "ParameterValue": str},
    total=False,
)


class ClientDescribeOrganizationConformancePacksResponseOrganizationConformancePacksConformancePackInputParametersTypeDef(
    _ClientDescribeOrganizationConformancePacksResponseOrganizationConformancePacksConformancePackInputParametersTypeDef
):
    """
    Type definition for `ClientDescribeOrganizationConformancePacksResponseOrganizationConformancePacks` `ConformancePackInputParameters`

    Input parameters in the form of key-value pairs for the conformance pack, both of which
    you define. Keys can have a maximum character length of 128 characters, and values can
    have a maximum length of 256 characters.

    - **ParameterName** *(string) --*

      One part of a key-value pair.

    - **ParameterValue** *(string) --*

      Another part of the key-value pair.
    """


_ClientDescribeOrganizationConformancePacksResponseOrganizationConformancePacksTypeDef = TypedDict(
    "_ClientDescribeOrganizationConformancePacksResponseOrganizationConformancePacksTypeDef",
    {
        "OrganizationConformancePackName": str,
        "OrganizationConformancePackArn": str,
        "DeliveryS3Bucket": str,
        "DeliveryS3KeyPrefix": str,
        "ConformancePackInputParameters": List[
            ClientDescribeOrganizationConformancePacksResponseOrganizationConformancePacksConformancePackInputParametersTypeDef
        ],
        "ExcludedAccounts": List[str],
        "LastUpdateTime": datetime,
    },
    total=False,
)


class ClientDescribeOrganizationConformancePacksResponseOrganizationConformancePacksTypeDef(
    _ClientDescribeOrganizationConformancePacksResponseOrganizationConformancePacksTypeDef
):
    """
    Type definition for `ClientDescribeOrganizationConformancePacksResponse` `OrganizationConformancePacks`

    An organization conformance pack that has information about conformance packs that AWS
    Config creates in member accounts.

    - **OrganizationConformancePackName** *(string) --*

      The name you assign to an organization conformance pack.

    - **OrganizationConformancePackArn** *(string) --*

      Amazon Resource Name (ARN) of organization conformance pack.

    - **DeliveryS3Bucket** *(string) --*

      Location of an Amazon S3 bucket where AWS Config can deliver evaluation results and
      conformance pack template that is used to create a pack.

    - **DeliveryS3KeyPrefix** *(string) --*

      Any folder structure you want to add to an Amazon S3 bucket.

    - **ConformancePackInputParameters** *(list) --*

      A list of ``ConformancePackInputParameter`` objects.

      - *(dict) --*

        Input parameters in the form of key-value pairs for the conformance pack, both of which
        you define. Keys can have a maximum character length of 128 characters, and values can
        have a maximum length of 256 characters.

        - **ParameterName** *(string) --*

          One part of a key-value pair.

        - **ParameterValue** *(string) --*

          Another part of the key-value pair.

    - **ExcludedAccounts** *(list) --*

      A comma-separated list of accounts excluded from organization conformance pack.

      - *(string) --*

    - **LastUpdateTime** *(datetime) --*

      Last time when organization conformation pack was updated.
    """


_ClientDescribeOrganizationConformancePacksResponseTypeDef = TypedDict(
    "_ClientDescribeOrganizationConformancePacksResponseTypeDef",
    {
        "OrganizationConformancePacks": List[
            ClientDescribeOrganizationConformancePacksResponseOrganizationConformancePacksTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeOrganizationConformancePacksResponseTypeDef(
    _ClientDescribeOrganizationConformancePacksResponseTypeDef
):
    """
    Type definition for `ClientDescribeOrganizationConformancePacks` `Response`

    - **OrganizationConformancePacks** *(list) --*

      Returns a list of OrganizationConformancePacks objects.

      - *(dict) --*

        An organization conformance pack that has information about conformance packs that AWS
        Config creates in member accounts.

        - **OrganizationConformancePackName** *(string) --*

          The name you assign to an organization conformance pack.

        - **OrganizationConformancePackArn** *(string) --*

          Amazon Resource Name (ARN) of organization conformance pack.

        - **DeliveryS3Bucket** *(string) --*

          Location of an Amazon S3 bucket where AWS Config can deliver evaluation results and
          conformance pack template that is used to create a pack.

        - **DeliveryS3KeyPrefix** *(string) --*

          Any folder structure you want to add to an Amazon S3 bucket.

        - **ConformancePackInputParameters** *(list) --*

          A list of ``ConformancePackInputParameter`` objects.

          - *(dict) --*

            Input parameters in the form of key-value pairs for the conformance pack, both of which
            you define. Keys can have a maximum character length of 128 characters, and values can
            have a maximum length of 256 characters.

            - **ParameterName** *(string) --*

              One part of a key-value pair.

            - **ParameterValue** *(string) --*

              Another part of the key-value pair.

        - **ExcludedAccounts** *(list) --*

          A comma-separated list of accounts excluded from organization conformance pack.

          - *(string) --*

        - **LastUpdateTime** *(datetime) --*

          Last time when organization conformation pack was updated.

    - **NextToken** *(string) --*

      The nextToken string returned on a previous page that you use to get the next page of results
      in a paginated response.
    """


_ClientDescribePendingAggregationRequestsResponsePendingAggregationRequestsTypeDef = TypedDict(
    "_ClientDescribePendingAggregationRequestsResponsePendingAggregationRequestsTypeDef",
    {"RequesterAccountId": str, "RequesterAwsRegion": str},
    total=False,
)


class ClientDescribePendingAggregationRequestsResponsePendingAggregationRequestsTypeDef(
    _ClientDescribePendingAggregationRequestsResponsePendingAggregationRequestsTypeDef
):
    """
    Type definition for `ClientDescribePendingAggregationRequestsResponse` `PendingAggregationRequests`

    An object that represents the account ID and region of an aggregator account that is
    requesting authorization but is not yet authorized.

    - **RequesterAccountId** *(string) --*

      The 12-digit account ID of the account requesting to aggregate data.

    - **RequesterAwsRegion** *(string) --*

      The region requesting to aggregate data.
    """


_ClientDescribePendingAggregationRequestsResponseTypeDef = TypedDict(
    "_ClientDescribePendingAggregationRequestsResponseTypeDef",
    {
        "PendingAggregationRequests": List[
            ClientDescribePendingAggregationRequestsResponsePendingAggregationRequestsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribePendingAggregationRequestsResponseTypeDef(
    _ClientDescribePendingAggregationRequestsResponseTypeDef
):
    """
    Type definition for `ClientDescribePendingAggregationRequests` `Response`

    - **PendingAggregationRequests** *(list) --*

      Returns a PendingAggregationRequests object.

      - *(dict) --*

        An object that represents the account ID and region of an aggregator account that is
        requesting authorization but is not yet authorized.

        - **RequesterAccountId** *(string) --*

          The 12-digit account ID of the account requesting to aggregate data.

        - **RequesterAwsRegion** *(string) --*

          The region requesting to aggregate data.

    - **NextToken** *(string) --*

      The ``nextToken`` string returned on a previous page that you use to get the next page of
      results in a paginated response.
    """


_ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsExecutionControlsSsmControlsTypeDef = TypedDict(
    "_ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsExecutionControlsSsmControlsTypeDef",
    {"ConcurrentExecutionRatePercentage": int, "ErrorPercentage": int},
    total=False,
)


class ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsExecutionControlsSsmControlsTypeDef(
    _ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsExecutionControlsSsmControlsTypeDef
):
    """
    Type definition for `ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsExecutionControls` `SsmControls`

    A SsmControls object.

    - **ConcurrentExecutionRatePercentage** *(integer) --*

      The maximum percentage of remediation actions allowed to run in parallel on the
      non-compliant resources for that specific rule. You can specify a percentage, such as
      10%. The default value is 10.

    - **ErrorPercentage** *(integer) --*

      The percentage of errors that are allowed before SSM stops running automations on
      non-compliant resources for that specific rule. You can specify a percentage of
      errors, for example 10%. If you do not specifiy a percentage, the default is 50%. For
      example, if you set the ErrorPercentage to 40% for 10 non-compliant resources, then
      SSM stops running the automations when the fifth error is received.
    """


_ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsExecutionControlsTypeDef = TypedDict(
    "_ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsExecutionControlsTypeDef",
    {
        "SsmControls": ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsExecutionControlsSsmControlsTypeDef
    },
    total=False,
)


class ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsExecutionControlsTypeDef(
    _ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsExecutionControlsTypeDef
):
    """
    Type definition for `ClientDescribeRemediationConfigurationsResponseRemediationConfigurations` `ExecutionControls`

    An ExecutionControls object.

    - **SsmControls** *(dict) --*

      A SsmControls object.

      - **ConcurrentExecutionRatePercentage** *(integer) --*

        The maximum percentage of remediation actions allowed to run in parallel on the
        non-compliant resources for that specific rule. You can specify a percentage, such as
        10%. The default value is 10.

      - **ErrorPercentage** *(integer) --*

        The percentage of errors that are allowed before SSM stops running automations on
        non-compliant resources for that specific rule. You can specify a percentage of
        errors, for example 10%. If you do not specifiy a percentage, the default is 50%. For
        example, if you set the ErrorPercentage to 40% for 10 non-compliant resources, then
        SSM stops running the automations when the fifth error is received.
    """


_ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersResourceValueTypeDef = TypedDict(
    "_ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersResourceValueTypeDef",
    {"Value": str},
    total=False,
)


class ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersResourceValueTypeDef(
    _ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersResourceValueTypeDef
):
    """
    Type definition for `ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParameters` `ResourceValue`

    The value is dynamic and changes at run-time.

    - **Value** *(string) --*

      The value is a resource ID.
    """


_ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersStaticValueTypeDef = TypedDict(
    "_ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersStaticValueTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersStaticValueTypeDef(
    _ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersStaticValueTypeDef
):
    """
    Type definition for `ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParameters` `StaticValue`

    The value is static and does not change at run-time.

    - **Values** *(list) --*

      A list of values. For example, the ARN of the assumed role.

      - *(string) --*
    """


_ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersTypeDef = TypedDict(
    "_ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersTypeDef",
    {
        "ResourceValue": ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersResourceValueTypeDef,
        "StaticValue": ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersStaticValueTypeDef,
    },
    total=False,
)


class ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersTypeDef(
    _ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersTypeDef
):
    """
    Type definition for `ClientDescribeRemediationConfigurationsResponseRemediationConfigurations` `Parameters`

    The value is either a dynamic (resource) value or a static value. You must select
    either a dynamic value or a static value.

    - **ResourceValue** *(dict) --*

      The value is dynamic and changes at run-time.

      - **Value** *(string) --*

        The value is a resource ID.

    - **StaticValue** *(dict) --*

      The value is static and does not change at run-time.

      - **Values** *(list) --*

        A list of values. For example, the ARN of the assumed role.

        - *(string) --*
    """


_ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsTypeDef = TypedDict(
    "_ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsTypeDef",
    {
        "ConfigRuleName": str,
        "TargetType": str,
        "TargetId": str,
        "TargetVersion": str,
        "Parameters": Dict[
            str,
            ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsParametersTypeDef,
        ],
        "ResourceType": str,
        "Automatic": bool,
        "ExecutionControls": ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsExecutionControlsTypeDef,
        "MaximumAutomaticAttempts": int,
        "RetryAttemptSeconds": int,
        "Arn": str,
        "CreatedByService": str,
    },
    total=False,
)


class ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsTypeDef(
    _ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsTypeDef
):
    """
    Type definition for `ClientDescribeRemediationConfigurationsResponse` `RemediationConfigurations`

    An object that represents the details about the remediation configuration that includes the
    remediation action, parameters, and data to execute the action.

    - **ConfigRuleName** *(string) --*

      The name of the AWS Config rule.

    - **TargetType** *(string) --*

      The type of the target. Target executes remediation. For example, SSM document.

    - **TargetId** *(string) --*

      Target ID is the name of the public document.

    - **TargetVersion** *(string) --*

      Version of the target. For example, version of the SSM document.

    - **Parameters** *(dict) --*

      An object of the RemediationParameterValue.

      - *(string) --*

        - *(dict) --*

          The value is either a dynamic (resource) value or a static value. You must select
          either a dynamic value or a static value.

          - **ResourceValue** *(dict) --*

            The value is dynamic and changes at run-time.

            - **Value** *(string) --*

              The value is a resource ID.

          - **StaticValue** *(dict) --*

            The value is static and does not change at run-time.

            - **Values** *(list) --*

              A list of values. For example, the ARN of the assumed role.

              - *(string) --*

    - **ResourceType** *(string) --*

      The type of a resource.

    - **Automatic** *(boolean) --*

      The remediation is triggered automatically.

    - **ExecutionControls** *(dict) --*

      An ExecutionControls object.

      - **SsmControls** *(dict) --*

        A SsmControls object.

        - **ConcurrentExecutionRatePercentage** *(integer) --*

          The maximum percentage of remediation actions allowed to run in parallel on the
          non-compliant resources for that specific rule. You can specify a percentage, such as
          10%. The default value is 10.

        - **ErrorPercentage** *(integer) --*

          The percentage of errors that are allowed before SSM stops running automations on
          non-compliant resources for that specific rule. You can specify a percentage of
          errors, for example 10%. If you do not specifiy a percentage, the default is 50%. For
          example, if you set the ErrorPercentage to 40% for 10 non-compliant resources, then
          SSM stops running the automations when the fifth error is received.

    - **MaximumAutomaticAttempts** *(integer) --*

      The maximum number of failed attempts for auto-remediation. If you do not select a
      number, the default is 5.

      For example, if you specify MaximumAutomaticAttempts as 5 with RetryAttemptsSeconds as 50
      seconds, AWS Config throws an exception after the 5th failed attempt within 50 seconds.

    - **RetryAttemptSeconds** *(integer) --*

      Maximum time in seconds that AWS Config runs auto-remediation. If you do not select a
      number, the default is 60 seconds.

      For example, if you specify RetryAttemptsSeconds as 50 seconds and
      MaximumAutomaticAttempts as 5, AWS Config will run auto-remediations 5 times within 50
      seconds before throwing an exception.

    - **Arn** *(string) --*

      Amazon Resource Name (ARN) of remediation configuration.

    - **CreatedByService** *(string) --*

      Name of the service that owns the service linked rule, if applicable.
    """


_ClientDescribeRemediationConfigurationsResponseTypeDef = TypedDict(
    "_ClientDescribeRemediationConfigurationsResponseTypeDef",
    {
        "RemediationConfigurations": List[
            ClientDescribeRemediationConfigurationsResponseRemediationConfigurationsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeRemediationConfigurationsResponseTypeDef(
    _ClientDescribeRemediationConfigurationsResponseTypeDef
):
    """
    Type definition for `ClientDescribeRemediationConfigurations` `Response`

    - **RemediationConfigurations** *(list) --*

      Returns a remediation configuration object.

      - *(dict) --*

        An object that represents the details about the remediation configuration that includes the
        remediation action, parameters, and data to execute the action.

        - **ConfigRuleName** *(string) --*

          The name of the AWS Config rule.

        - **TargetType** *(string) --*

          The type of the target. Target executes remediation. For example, SSM document.

        - **TargetId** *(string) --*

          Target ID is the name of the public document.

        - **TargetVersion** *(string) --*

          Version of the target. For example, version of the SSM document.

        - **Parameters** *(dict) --*

          An object of the RemediationParameterValue.

          - *(string) --*

            - *(dict) --*

              The value is either a dynamic (resource) value or a static value. You must select
              either a dynamic value or a static value.

              - **ResourceValue** *(dict) --*

                The value is dynamic and changes at run-time.

                - **Value** *(string) --*

                  The value is a resource ID.

              - **StaticValue** *(dict) --*

                The value is static and does not change at run-time.

                - **Values** *(list) --*

                  A list of values. For example, the ARN of the assumed role.

                  - *(string) --*

        - **ResourceType** *(string) --*

          The type of a resource.

        - **Automatic** *(boolean) --*

          The remediation is triggered automatically.

        - **ExecutionControls** *(dict) --*

          An ExecutionControls object.

          - **SsmControls** *(dict) --*

            A SsmControls object.

            - **ConcurrentExecutionRatePercentage** *(integer) --*

              The maximum percentage of remediation actions allowed to run in parallel on the
              non-compliant resources for that specific rule. You can specify a percentage, such as
              10%. The default value is 10.

            - **ErrorPercentage** *(integer) --*

              The percentage of errors that are allowed before SSM stops running automations on
              non-compliant resources for that specific rule. You can specify a percentage of
              errors, for example 10%. If you do not specifiy a percentage, the default is 50%. For
              example, if you set the ErrorPercentage to 40% for 10 non-compliant resources, then
              SSM stops running the automations when the fifth error is received.

        - **MaximumAutomaticAttempts** *(integer) --*

          The maximum number of failed attempts for auto-remediation. If you do not select a
          number, the default is 5.

          For example, if you specify MaximumAutomaticAttempts as 5 with RetryAttemptsSeconds as 50
          seconds, AWS Config throws an exception after the 5th failed attempt within 50 seconds.

        - **RetryAttemptSeconds** *(integer) --*

          Maximum time in seconds that AWS Config runs auto-remediation. If you do not select a
          number, the default is 60 seconds.

          For example, if you specify RetryAttemptsSeconds as 50 seconds and
          MaximumAutomaticAttempts as 5, AWS Config will run auto-remediations 5 times within 50
          seconds before throwing an exception.

        - **Arn** *(string) --*

          Amazon Resource Name (ARN) of remediation configuration.

        - **CreatedByService** *(string) --*

          Name of the service that owns the service linked rule, if applicable.
    """


_ClientDescribeRemediationExceptionsResourceKeysTypeDef = TypedDict(
    "_ClientDescribeRemediationExceptionsResourceKeysTypeDef",
    {"ResourceType": str, "ResourceId": str},
    total=False,
)


class ClientDescribeRemediationExceptionsResourceKeysTypeDef(
    _ClientDescribeRemediationExceptionsResourceKeysTypeDef
):
    """
    Type definition for `ClientDescribeRemediationExceptions` `ResourceKeys`

    The details that identify a resource within AWS Config, including the resource type and
    resource ID.

    - **ResourceType** *(string) --*

      The type of a resource.

    - **ResourceId** *(string) --*

      The ID of the resource (for example., sg-xxxxxx).
    """


_ClientDescribeRemediationExceptionsResponseRemediationExceptionsTypeDef = TypedDict(
    "_ClientDescribeRemediationExceptionsResponseRemediationExceptionsTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceType": str,
        "ResourceId": str,
        "Message": str,
        "ExpirationTime": datetime,
    },
    total=False,
)


class ClientDescribeRemediationExceptionsResponseRemediationExceptionsTypeDef(
    _ClientDescribeRemediationExceptionsResponseRemediationExceptionsTypeDef
):
    """
    Type definition for `ClientDescribeRemediationExceptionsResponse` `RemediationExceptions`

    An object that represents the details about the remediation exception. The details include
    the rule name, an explanation of an exception, the time when the exception will be deleted,
    the resource ID, and resource type.

    - **ConfigRuleName** *(string) --*

      The name of the AWS Config rule.

    - **ResourceType** *(string) --*

      The type of a resource.

    - **ResourceId** *(string) --*

      The ID of the resource (for example., sg-xxxxxx).

    - **Message** *(string) --*

      An explanation of an remediation exception.

    - **ExpirationTime** *(datetime) --*

      The time when the remediation exception will be deleted.
    """


_ClientDescribeRemediationExceptionsResponseTypeDef = TypedDict(
    "_ClientDescribeRemediationExceptionsResponseTypeDef",
    {
        "RemediationExceptions": List[
            ClientDescribeRemediationExceptionsResponseRemediationExceptionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeRemediationExceptionsResponseTypeDef(
    _ClientDescribeRemediationExceptionsResponseTypeDef
):
    """
    Type definition for `ClientDescribeRemediationExceptions` `Response`

    - **RemediationExceptions** *(list) --*

      Returns a list of remediation exception objects.

      - *(dict) --*

        An object that represents the details about the remediation exception. The details include
        the rule name, an explanation of an exception, the time when the exception will be deleted,
        the resource ID, and resource type.

        - **ConfigRuleName** *(string) --*

          The name of the AWS Config rule.

        - **ResourceType** *(string) --*

          The type of a resource.

        - **ResourceId** *(string) --*

          The ID of the resource (for example., sg-xxxxxx).

        - **Message** *(string) --*

          An explanation of an remediation exception.

        - **ExpirationTime** *(datetime) --*

          The time when the remediation exception will be deleted.

    - **NextToken** *(string) --*

      The ``nextToken`` string returned in a previous request that you use to request the next page
      of results in a paginated response.
    """


_ClientDescribeRemediationExecutionStatusResourceKeysTypeDef = TypedDict(
    "_ClientDescribeRemediationExecutionStatusResourceKeysTypeDef",
    {"resourceType": str, "resourceId": str},
)


class ClientDescribeRemediationExecutionStatusResourceKeysTypeDef(
    _ClientDescribeRemediationExecutionStatusResourceKeysTypeDef
):
    """
    Type definition for `ClientDescribeRemediationExecutionStatus` `ResourceKeys`

    The details that identify a resource within AWS Config, including the resource type and
    resource ID.

    - **resourceType** *(string) --* **[REQUIRED]**

      The resource type.

    - **resourceId** *(string) --* **[REQUIRED]**

      The ID of the resource (for example., sg-xxxxxx).
    """


_ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesResourceKeyTypeDef = TypedDict(
    "_ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesResourceKeyTypeDef",
    {"resourceType": str, "resourceId": str},
    total=False,
)


class ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesResourceKeyTypeDef(
    _ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesResourceKeyTypeDef
):
    """
    Type definition for `ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatuses` `ResourceKey`

    The details that identify a resource within AWS Config, including the resource type and
    resource ID.

    - **resourceType** *(string) --*

      The resource type.

    - **resourceId** *(string) --*

      The ID of the resource (for example., sg-xxxxxx).
    """


_ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesStepDetailsTypeDef = TypedDict(
    "_ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesStepDetailsTypeDef",
    {
        "Name": str,
        "State": str,
        "ErrorMessage": str,
        "StartTime": datetime,
        "StopTime": datetime,
    },
    total=False,
)


class ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesStepDetailsTypeDef(
    _ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesStepDetailsTypeDef
):
    """
    Type definition for `ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatuses` `StepDetails`

    Name of the step from the SSM document.

    - **Name** *(string) --*

      The details of the step.

    - **State** *(string) --*

      The valid status of the step.

    - **ErrorMessage** *(string) --*

      An error message if the step was interrupted during execution.

    - **StartTime** *(datetime) --*

      The time when the step started.

    - **StopTime** *(datetime) --*

      The time when the step stopped.
    """


_ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesTypeDef = TypedDict(
    "_ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesTypeDef",
    {
        "ResourceKey": ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesResourceKeyTypeDef,
        "State": str,
        "StepDetails": List[
            ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesStepDetailsTypeDef
        ],
        "InvocationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)


class ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesTypeDef(
    _ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesTypeDef
):
    """
    Type definition for `ClientDescribeRemediationExecutionStatusResponse` `RemediationExecutionStatuses`

    Provides details of the current status of the invoked remediation action for that resource.

    - **ResourceKey** *(dict) --*

      The details that identify a resource within AWS Config, including the resource type and
      resource ID.

      - **resourceType** *(string) --*

        The resource type.

      - **resourceId** *(string) --*

        The ID of the resource (for example., sg-xxxxxx).

    - **State** *(string) --*

      ENUM of the values.

    - **StepDetails** *(list) --*

      Details of every step.

      - *(dict) --*

        Name of the step from the SSM document.

        - **Name** *(string) --*

          The details of the step.

        - **State** *(string) --*

          The valid status of the step.

        - **ErrorMessage** *(string) --*

          An error message if the step was interrupted during execution.

        - **StartTime** *(datetime) --*

          The time when the step started.

        - **StopTime** *(datetime) --*

          The time when the step stopped.

    - **InvocationTime** *(datetime) --*

      Start time when the remediation was executed.

    - **LastUpdatedTime** *(datetime) --*

      The time when the remediation execution was last updated.
    """


_ClientDescribeRemediationExecutionStatusResponseTypeDef = TypedDict(
    "_ClientDescribeRemediationExecutionStatusResponseTypeDef",
    {
        "RemediationExecutionStatuses": List[
            ClientDescribeRemediationExecutionStatusResponseRemediationExecutionStatusesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeRemediationExecutionStatusResponseTypeDef(
    _ClientDescribeRemediationExecutionStatusResponseTypeDef
):
    """
    Type definition for `ClientDescribeRemediationExecutionStatus` `Response`

    - **RemediationExecutionStatuses** *(list) --*

      Returns a list of remediation execution statuses objects.

      - *(dict) --*

        Provides details of the current status of the invoked remediation action for that resource.

        - **ResourceKey** *(dict) --*

          The details that identify a resource within AWS Config, including the resource type and
          resource ID.

          - **resourceType** *(string) --*

            The resource type.

          - **resourceId** *(string) --*

            The ID of the resource (for example., sg-xxxxxx).

        - **State** *(string) --*

          ENUM of the values.

        - **StepDetails** *(list) --*

          Details of every step.

          - *(dict) --*

            Name of the step from the SSM document.

            - **Name** *(string) --*

              The details of the step.

            - **State** *(string) --*

              The valid status of the step.

            - **ErrorMessage** *(string) --*

              An error message if the step was interrupted during execution.

            - **StartTime** *(datetime) --*

              The time when the step started.

            - **StopTime** *(datetime) --*

              The time when the step stopped.

        - **InvocationTime** *(datetime) --*

          Start time when the remediation was executed.

        - **LastUpdatedTime** *(datetime) --*

          The time when the remediation execution was last updated.

    - **NextToken** *(string) --*

      The ``nextToken`` string returned on a previous page that you use to get the next page of
      results in a paginated response.
    """


_ClientDescribeRetentionConfigurationsResponseRetentionConfigurationsTypeDef = TypedDict(
    "_ClientDescribeRetentionConfigurationsResponseRetentionConfigurationsTypeDef",
    {"Name": str, "RetentionPeriodInDays": int},
    total=False,
)


class ClientDescribeRetentionConfigurationsResponseRetentionConfigurationsTypeDef(
    _ClientDescribeRetentionConfigurationsResponseRetentionConfigurationsTypeDef
):
    """
    Type definition for `ClientDescribeRetentionConfigurationsResponse` `RetentionConfigurations`

    An object with the name of the retention configuration and the retention period in days.
    The object stores the configuration for data retention in AWS Config.

    - **Name** *(string) --*

      The name of the retention configuration object.

    - **RetentionPeriodInDays** *(integer) --*

      Number of days AWS Config stores your historical information.

      .. note::

        Currently, only applicable to the configuration item history.
    """


_ClientDescribeRetentionConfigurationsResponseTypeDef = TypedDict(
    "_ClientDescribeRetentionConfigurationsResponseTypeDef",
    {
        "RetentionConfigurations": List[
            ClientDescribeRetentionConfigurationsResponseRetentionConfigurationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeRetentionConfigurationsResponseTypeDef(
    _ClientDescribeRetentionConfigurationsResponseTypeDef
):
    """
    Type definition for `ClientDescribeRetentionConfigurations` `Response`

    - **RetentionConfigurations** *(list) --*

      Returns a retention configuration object.

      - *(dict) --*

        An object with the name of the retention configuration and the retention period in days.
        The object stores the configuration for data retention in AWS Config.

        - **Name** *(string) --*

          The name of the retention configuration object.

        - **RetentionPeriodInDays** *(integer) --*

          Number of days AWS Config stores your historical information.

          .. note::

            Currently, only applicable to the configuration item history.

    - **NextToken** *(string) --*

      The ``nextToken`` string returned on a previous page that you use to get the next page of
      results in a paginated response.
    """


_ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef = TypedDict(
    "_ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    {"ConfigRuleName": str, "ResourceType": str, "ResourceId": str},
    total=False,
)


class ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef(
    _ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef
):
    """
    Type definition for `ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsEvaluationResultIdentifier` `EvaluationResultQualifier`

    Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
    and ID of the evaluated resource.

    - **ConfigRuleName** *(string) --*

      The name of the AWS Config rule that was used in the evaluation.

    - **ResourceType** *(string) --*

      The type of AWS resource that was evaluated.

    - **ResourceId** *(string) --*

      The ID of the evaluated AWS resource.
    """


_ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsEvaluationResultIdentifierTypeDef = TypedDict(
    "_ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsEvaluationResultIdentifierTypeDef",
    {
        "EvaluationResultQualifier": ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef,
        "OrderingTimestamp": datetime,
    },
    total=False,
)


class ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsEvaluationResultIdentifierTypeDef(
    _ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsEvaluationResultIdentifierTypeDef
):
    """
    Type definition for `ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResults` `EvaluationResultIdentifier`

    Uniquely identifies the evaluation result.

    - **EvaluationResultQualifier** *(dict) --*

      Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
      and ID of the evaluated resource.

      - **ConfigRuleName** *(string) --*

        The name of the AWS Config rule that was used in the evaluation.

      - **ResourceType** *(string) --*

        The type of AWS resource that was evaluated.

      - **ResourceId** *(string) --*

        The ID of the evaluated AWS resource.

    - **OrderingTimestamp** *(datetime) --*

      The time of the event that triggered the evaluation of your AWS resources. The time can
      indicate when AWS Config delivered a configuration item change notification, or it can
      indicate when AWS Config delivered the configuration snapshot, depending on which event
      triggered the evaluation.
    """


_ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsTypeDef = TypedDict(
    "_ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsTypeDef",
    {
        "EvaluationResultIdentifier": ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsEvaluationResultIdentifierTypeDef,
        "ComplianceType": str,
        "ResultRecordedTime": datetime,
        "ConfigRuleInvokedTime": datetime,
        "Annotation": str,
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)


class ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsTypeDef(
    _ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsTypeDef
):
    """
    Type definition for `ClientGetAggregateComplianceDetailsByConfigRuleResponse` `AggregateEvaluationResults`

    The details of an AWS Config evaluation for an account ID and region in an aggregator.
    Provides the AWS resource that was evaluated, the compliance of the resource, related time
    stamps, and supplementary information.

    - **EvaluationResultIdentifier** *(dict) --*

      Uniquely identifies the evaluation result.

      - **EvaluationResultQualifier** *(dict) --*

        Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
        and ID of the evaluated resource.

        - **ConfigRuleName** *(string) --*

          The name of the AWS Config rule that was used in the evaluation.

        - **ResourceType** *(string) --*

          The type of AWS resource that was evaluated.

        - **ResourceId** *(string) --*

          The ID of the evaluated AWS resource.

      - **OrderingTimestamp** *(datetime) --*

        The time of the event that triggered the evaluation of your AWS resources. The time can
        indicate when AWS Config delivered a configuration item change notification, or it can
        indicate when AWS Config delivered the configuration snapshot, depending on which event
        triggered the evaluation.

    - **ComplianceType** *(string) --*

      The resource compliance status.

      For the ``AggregationEvaluationResult`` data type, AWS Config supports only the
      ``COMPLIANT`` and ``NON_COMPLIANT`` . AWS Config does not support the ``NOT_APPLICABLE``
      and ``INSUFFICIENT_DATA`` value.

    - **ResultRecordedTime** *(datetime) --*

      The time when AWS Config recorded the aggregate evaluation result.

    - **ConfigRuleInvokedTime** *(datetime) --*

      The time when the AWS Config rule evaluated the AWS resource.

    - **Annotation** *(string) --*

      Supplementary information about how the agrregate evaluation determined the compliance.

    - **AccountId** *(string) --*

      The 12-digit account ID of the source account.

    - **AwsRegion** *(string) --*

      The source region from where the data is aggregated.
    """


_ClientGetAggregateComplianceDetailsByConfigRuleResponseTypeDef = TypedDict(
    "_ClientGetAggregateComplianceDetailsByConfigRuleResponseTypeDef",
    {
        "AggregateEvaluationResults": List[
            ClientGetAggregateComplianceDetailsByConfigRuleResponseAggregateEvaluationResultsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientGetAggregateComplianceDetailsByConfigRuleResponseTypeDef(
    _ClientGetAggregateComplianceDetailsByConfigRuleResponseTypeDef
):
    """
    Type definition for `ClientGetAggregateComplianceDetailsByConfigRule` `Response`

    - **AggregateEvaluationResults** *(list) --*

      Returns an AggregateEvaluationResults object.

      - *(dict) --*

        The details of an AWS Config evaluation for an account ID and region in an aggregator.
        Provides the AWS resource that was evaluated, the compliance of the resource, related time
        stamps, and supplementary information.

        - **EvaluationResultIdentifier** *(dict) --*

          Uniquely identifies the evaluation result.

          - **EvaluationResultQualifier** *(dict) --*

            Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
            and ID of the evaluated resource.

            - **ConfigRuleName** *(string) --*

              The name of the AWS Config rule that was used in the evaluation.

            - **ResourceType** *(string) --*

              The type of AWS resource that was evaluated.

            - **ResourceId** *(string) --*

              The ID of the evaluated AWS resource.

          - **OrderingTimestamp** *(datetime) --*

            The time of the event that triggered the evaluation of your AWS resources. The time can
            indicate when AWS Config delivered a configuration item change notification, or it can
            indicate when AWS Config delivered the configuration snapshot, depending on which event
            triggered the evaluation.

        - **ComplianceType** *(string) --*

          The resource compliance status.

          For the ``AggregationEvaluationResult`` data type, AWS Config supports only the
          ``COMPLIANT`` and ``NON_COMPLIANT`` . AWS Config does not support the ``NOT_APPLICABLE``
          and ``INSUFFICIENT_DATA`` value.

        - **ResultRecordedTime** *(datetime) --*

          The time when AWS Config recorded the aggregate evaluation result.

        - **ConfigRuleInvokedTime** *(datetime) --*

          The time when the AWS Config rule evaluated the AWS resource.

        - **Annotation** *(string) --*

          Supplementary information about how the agrregate evaluation determined the compliance.

        - **AccountId** *(string) --*

          The 12-digit account ID of the source account.

        - **AwsRegion** *(string) --*

          The source region from where the data is aggregated.

    - **NextToken** *(string) --*

      The ``nextToken`` string returned on a previous page that you use to get the next page of
      results in a paginated response.
    """


_ClientGetAggregateConfigRuleComplianceSummaryFiltersTypeDef = TypedDict(
    "_ClientGetAggregateConfigRuleComplianceSummaryFiltersTypeDef",
    {"AccountId": str, "AwsRegion": str},
    total=False,
)


class ClientGetAggregateConfigRuleComplianceSummaryFiltersTypeDef(
    _ClientGetAggregateConfigRuleComplianceSummaryFiltersTypeDef
):
    """
    Type definition for `ClientGetAggregateConfigRuleComplianceSummary` `Filters`

    Filters the results based on the ConfigRuleComplianceSummaryFilters object.

    - **AccountId** *(string) --*

      The 12-digit account ID of the source account.

    - **AwsRegion** *(string) --*

      The source region where the data is aggregated.
    """


_ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryCompliantResourceCountTypeDef = TypedDict(
    "_ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryCompliantResourceCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)


class ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryCompliantResourceCountTypeDef(
    _ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryCompliantResourceCountTypeDef
):
    """
    Type definition for `ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummary` `CompliantResourceCount`

    The number of AWS Config rules or AWS resources that are compliant, up to a maximum of
    25 for rules and 100 for resources.

    - **CappedCount** *(integer) --*

      The number of AWS resources or AWS Config rules responsible for the current
      compliance of the item.

    - **CapExceeded** *(boolean) --*

      Indicates whether the maximum count is reached.
    """


_ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryNonCompliantResourceCountTypeDef = TypedDict(
    "_ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryNonCompliantResourceCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)


class ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryNonCompliantResourceCountTypeDef(
    _ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryNonCompliantResourceCountTypeDef
):
    """
    Type definition for `ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummary` `NonCompliantResourceCount`

    The number of AWS Config rules or AWS resources that are noncompliant, up to a maximum
    of 25 for rules and 100 for resources.

    - **CappedCount** *(integer) --*

      The number of AWS resources or AWS Config rules responsible for the current
      compliance of the item.

    - **CapExceeded** *(boolean) --*

      Indicates whether the maximum count is reached.
    """


_ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryTypeDef = TypedDict(
    "_ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryTypeDef",
    {
        "CompliantResourceCount": ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryCompliantResourceCountTypeDef,
        "NonCompliantResourceCount": ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryNonCompliantResourceCountTypeDef,
        "ComplianceSummaryTimestamp": datetime,
    },
    total=False,
)


class ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryTypeDef(
    _ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryTypeDef
):
    """
    Type definition for `ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCounts` `ComplianceSummary`

    The number of compliant and noncompliant AWS Config rules.

    - **CompliantResourceCount** *(dict) --*

      The number of AWS Config rules or AWS resources that are compliant, up to a maximum of
      25 for rules and 100 for resources.

      - **CappedCount** *(integer) --*

        The number of AWS resources or AWS Config rules responsible for the current
        compliance of the item.

      - **CapExceeded** *(boolean) --*

        Indicates whether the maximum count is reached.

    - **NonCompliantResourceCount** *(dict) --*

      The number of AWS Config rules or AWS resources that are noncompliant, up to a maximum
      of 25 for rules and 100 for resources.

      - **CappedCount** *(integer) --*

        The number of AWS resources or AWS Config rules responsible for the current
        compliance of the item.

      - **CapExceeded** *(boolean) --*

        Indicates whether the maximum count is reached.

    - **ComplianceSummaryTimestamp** *(datetime) --*

      The time that AWS Config created the compliance summary.
    """


_ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsTypeDef = TypedDict(
    "_ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsTypeDef",
    {
        "GroupName": str,
        "ComplianceSummary": ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsComplianceSummaryTypeDef,
    },
    total=False,
)


class ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsTypeDef(
    _ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsTypeDef
):
    """
    Type definition for `ClientGetAggregateConfigRuleComplianceSummaryResponse` `AggregateComplianceCounts`

    Returns the number of compliant and noncompliant rules for one or more accounts and regions
    in an aggregator.

    - **GroupName** *(string) --*

      The 12-digit account ID or region based on the GroupByKey value.

    - **ComplianceSummary** *(dict) --*

      The number of compliant and noncompliant AWS Config rules.

      - **CompliantResourceCount** *(dict) --*

        The number of AWS Config rules or AWS resources that are compliant, up to a maximum of
        25 for rules and 100 for resources.

        - **CappedCount** *(integer) --*

          The number of AWS resources or AWS Config rules responsible for the current
          compliance of the item.

        - **CapExceeded** *(boolean) --*

          Indicates whether the maximum count is reached.

      - **NonCompliantResourceCount** *(dict) --*

        The number of AWS Config rules or AWS resources that are noncompliant, up to a maximum
        of 25 for rules and 100 for resources.

        - **CappedCount** *(integer) --*

          The number of AWS resources or AWS Config rules responsible for the current
          compliance of the item.

        - **CapExceeded** *(boolean) --*

          Indicates whether the maximum count is reached.

      - **ComplianceSummaryTimestamp** *(datetime) --*

        The time that AWS Config created the compliance summary.
    """


_ClientGetAggregateConfigRuleComplianceSummaryResponseTypeDef = TypedDict(
    "_ClientGetAggregateConfigRuleComplianceSummaryResponseTypeDef",
    {
        "GroupByKey": str,
        "AggregateComplianceCounts": List[
            ClientGetAggregateConfigRuleComplianceSummaryResponseAggregateComplianceCountsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientGetAggregateConfigRuleComplianceSummaryResponseTypeDef(
    _ClientGetAggregateConfigRuleComplianceSummaryResponseTypeDef
):
    """
    Type definition for `ClientGetAggregateConfigRuleComplianceSummary` `Response`

    - **GroupByKey** *(string) --*

      Groups the result based on ACCOUNT_ID or AWS_REGION.

    - **AggregateComplianceCounts** *(list) --*

      Returns a list of AggregateComplianceCounts object.

      - *(dict) --*

        Returns the number of compliant and noncompliant rules for one or more accounts and regions
        in an aggregator.

        - **GroupName** *(string) --*

          The 12-digit account ID or region based on the GroupByKey value.

        - **ComplianceSummary** *(dict) --*

          The number of compliant and noncompliant AWS Config rules.

          - **CompliantResourceCount** *(dict) --*

            The number of AWS Config rules or AWS resources that are compliant, up to a maximum of
            25 for rules and 100 for resources.

            - **CappedCount** *(integer) --*

              The number of AWS resources or AWS Config rules responsible for the current
              compliance of the item.

            - **CapExceeded** *(boolean) --*

              Indicates whether the maximum count is reached.

          - **NonCompliantResourceCount** *(dict) --*

            The number of AWS Config rules or AWS resources that are noncompliant, up to a maximum
            of 25 for rules and 100 for resources.

            - **CappedCount** *(integer) --*

              The number of AWS resources or AWS Config rules responsible for the current
              compliance of the item.

            - **CapExceeded** *(boolean) --*

              Indicates whether the maximum count is reached.

          - **ComplianceSummaryTimestamp** *(datetime) --*

            The time that AWS Config created the compliance summary.

    - **NextToken** *(string) --*

      The ``nextToken`` string returned on a previous page that you use to get the next page of
      results in a paginated response.
    """


_ClientGetAggregateDiscoveredResourceCountsFiltersTypeDef = TypedDict(
    "_ClientGetAggregateDiscoveredResourceCountsFiltersTypeDef",
    {"ResourceType": str, "AccountId": str, "Region": str},
    total=False,
)


class ClientGetAggregateDiscoveredResourceCountsFiltersTypeDef(
    _ClientGetAggregateDiscoveredResourceCountsFiltersTypeDef
):
    """
    Type definition for `ClientGetAggregateDiscoveredResourceCounts` `Filters`

    Filters the results based on the ``ResourceCountFilters`` object.

    - **ResourceType** *(string) --*

      The type of the AWS resource.

    - **AccountId** *(string) --*

      The 12-digit ID of the account.

    - **Region** *(string) --*

      The region where the account is located.
    """


_ClientGetAggregateDiscoveredResourceCountsResponseGroupedResourceCountsTypeDef = TypedDict(
    "_ClientGetAggregateDiscoveredResourceCountsResponseGroupedResourceCountsTypeDef",
    {"GroupName": str, "ResourceCount": int},
    total=False,
)


class ClientGetAggregateDiscoveredResourceCountsResponseGroupedResourceCountsTypeDef(
    _ClientGetAggregateDiscoveredResourceCountsResponseGroupedResourceCountsTypeDef
):
    """
    Type definition for `ClientGetAggregateDiscoveredResourceCountsResponse` `GroupedResourceCounts`

    The count of resources that are grouped by the group name.

    - **GroupName** *(string) --*

      The name of the group that can be region, account ID, or resource type. For example,
      region1, region2 if the region was chosen as ``GroupByKey`` .

    - **ResourceCount** *(integer) --*

      The number of resources in the group.
    """


_ClientGetAggregateDiscoveredResourceCountsResponseTypeDef = TypedDict(
    "_ClientGetAggregateDiscoveredResourceCountsResponseTypeDef",
    {
        "TotalDiscoveredResources": int,
        "GroupByKey": str,
        "GroupedResourceCounts": List[
            ClientGetAggregateDiscoveredResourceCountsResponseGroupedResourceCountsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientGetAggregateDiscoveredResourceCountsResponseTypeDef(
    _ClientGetAggregateDiscoveredResourceCountsResponseTypeDef
):
    """
    Type definition for `ClientGetAggregateDiscoveredResourceCounts` `Response`

    - **TotalDiscoveredResources** *(integer) --*

      The total number of resources that are present in an aggregator with the filters that you
      provide.

    - **GroupByKey** *(string) --*

      The key passed into the request object. If ``GroupByKey`` is not provided, the result will be
      empty.

    - **GroupedResourceCounts** *(list) --*

      Returns a list of GroupedResourceCount objects.

      - *(dict) --*

        The count of resources that are grouped by the group name.

        - **GroupName** *(string) --*

          The name of the group that can be region, account ID, or resource type. For example,
          region1, region2 if the region was chosen as ``GroupByKey`` .

        - **ResourceCount** *(integer) --*

          The number of resources in the group.

    - **NextToken** *(string) --*

      The ``nextToken`` string returned on a previous page that you use to get the next page of
      results in a paginated response.
    """


_RequiredClientGetAggregateResourceConfigResourceIdentifierTypeDef = TypedDict(
    "_RequiredClientGetAggregateResourceConfigResourceIdentifierTypeDef",
    {
        "SourceAccountId": str,
        "SourceRegion": str,
        "ResourceId": str,
        "ResourceType": str,
    },
)
_OptionalClientGetAggregateResourceConfigResourceIdentifierTypeDef = TypedDict(
    "_OptionalClientGetAggregateResourceConfigResourceIdentifierTypeDef",
    {"ResourceName": str},
    total=False,
)


class ClientGetAggregateResourceConfigResourceIdentifierTypeDef(
    _RequiredClientGetAggregateResourceConfigResourceIdentifierTypeDef,
    _OptionalClientGetAggregateResourceConfigResourceIdentifierTypeDef,
):
    """
    Type definition for `ClientGetAggregateResourceConfig` `ResourceIdentifier`

    An object that identifies aggregate resource.

    - **SourceAccountId** *(string) --* **[REQUIRED]**

      The 12-digit account ID of the source account.

    - **SourceRegion** *(string) --* **[REQUIRED]**

      The source region where data is aggregated.

    - **ResourceId** *(string) --* **[REQUIRED]**

      The ID of the AWS resource.

    - **ResourceType** *(string) --* **[REQUIRED]**

      The type of the AWS resource.

    - **ResourceName** *(string) --*

      The name of the AWS resource.
    """


_ClientGetAggregateResourceConfigResponseConfigurationItemrelationshipsTypeDef = TypedDict(
    "_ClientGetAggregateResourceConfigResponseConfigurationItemrelationshipsTypeDef",
    {
        "resourceType": str,
        "resourceId": str,
        "resourceName": str,
        "relationshipName": str,
    },
    total=False,
)


class ClientGetAggregateResourceConfigResponseConfigurationItemrelationshipsTypeDef(
    _ClientGetAggregateResourceConfigResponseConfigurationItemrelationshipsTypeDef
):
    """
    Type definition for `ClientGetAggregateResourceConfigResponseConfigurationItem` `relationships`

    The relationship of the related resource to the main resource.

    - **resourceType** *(string) --*

      The resource type of the related resource.

    - **resourceId** *(string) --*

      The ID of the related resource (for example, ``sg-xxxxxx`` ).

    - **resourceName** *(string) --*

      The custom name of the related resource, if available.

    - **relationshipName** *(string) --*

      The type of relationship with the related resource.
    """


_ClientGetAggregateResourceConfigResponseConfigurationItemTypeDef = TypedDict(
    "_ClientGetAggregateResourceConfigResponseConfigurationItemTypeDef",
    {
        "version": str,
        "accountId": str,
        "configurationItemCaptureTime": datetime,
        "configurationItemStatus": str,
        "configurationStateId": str,
        "configurationItemMD5Hash": str,
        "arn": str,
        "resourceType": str,
        "resourceId": str,
        "resourceName": str,
        "awsRegion": str,
        "availabilityZone": str,
        "resourceCreationTime": datetime,
        "tags": Dict[str, str],
        "relatedEvents": List[str],
        "relationships": List[
            ClientGetAggregateResourceConfigResponseConfigurationItemrelationshipsTypeDef
        ],
        "configuration": str,
        "supplementaryConfiguration": Dict[str, str],
    },
    total=False,
)


class ClientGetAggregateResourceConfigResponseConfigurationItemTypeDef(
    _ClientGetAggregateResourceConfigResponseConfigurationItemTypeDef
):
    """
    Type definition for `ClientGetAggregateResourceConfigResponse` `ConfigurationItem`

    Returns a ``ConfigurationItem`` object.

    - **version** *(string) --*

      The version number of the resource configuration.

    - **accountId** *(string) --*

      The 12-digit AWS account ID associated with the resource.

    - **configurationItemCaptureTime** *(datetime) --*

      The time when the configuration recording was initiated.

    - **configurationItemStatus** *(string) --*

      The configuration item status.

    - **configurationStateId** *(string) --*

      An identifier that indicates the ordering of the configuration items of a resource.

    - **configurationItemMD5Hash** *(string) --*

      Unique MD5 hash that represents the configuration item's state.

      You can use MD5 hash to compare the states of two or more configuration items that are
      associated with the same resource.

    - **arn** *(string) --*

      accoun

    - **resourceType** *(string) --*

      The type of AWS resource.

    - **resourceId** *(string) --*

      The ID of the resource (for example, ``sg-xxxxxx`` ).

    - **resourceName** *(string) --*

      The custom name of the resource, if available.

    - **awsRegion** *(string) --*

      The region where the resource resides.

    - **availabilityZone** *(string) --*

      The Availability Zone associated with the resource.

    - **resourceCreationTime** *(datetime) --*

      The time stamp when the resource was created.

    - **tags** *(dict) --*

      A mapping of key value tags associated with the resource.

      - *(string) --*

        - *(string) --*

    - **relatedEvents** *(list) --*

      A list of CloudTrail event IDs.

      A populated field indicates that the current configuration was initiated by the events
      recorded in the CloudTrail log. For more information about CloudTrail, see `What Is AWS
      CloudTrail
      <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/what_is_cloud_trail_top_level.html>`__
      .

      An empty field indicates that the current configuration was not initiated by any event.

      - *(string) --*

    - **relationships** *(list) --*

      A list of related AWS resources.

      - *(dict) --*

        The relationship of the related resource to the main resource.

        - **resourceType** *(string) --*

          The resource type of the related resource.

        - **resourceId** *(string) --*

          The ID of the related resource (for example, ``sg-xxxxxx`` ).

        - **resourceName** *(string) --*

          The custom name of the related resource, if available.

        - **relationshipName** *(string) --*

          The type of relationship with the related resource.

    - **configuration** *(string) --*

      The description of the resource configuration.

    - **supplementaryConfiguration** *(dict) --*

      Configuration attributes that AWS Config returns for certain resource types to supplement
      the information returned for the ``configuration`` parameter.

      - *(string) --*

        - *(string) --*
    """


_ClientGetAggregateResourceConfigResponseTypeDef = TypedDict(
    "_ClientGetAggregateResourceConfigResponseTypeDef",
    {
        "ConfigurationItem": ClientGetAggregateResourceConfigResponseConfigurationItemTypeDef
    },
    total=False,
)


class ClientGetAggregateResourceConfigResponseTypeDef(
    _ClientGetAggregateResourceConfigResponseTypeDef
):
    """
    Type definition for `ClientGetAggregateResourceConfig` `Response`

    - **ConfigurationItem** *(dict) --*

      Returns a ``ConfigurationItem`` object.

      - **version** *(string) --*

        The version number of the resource configuration.

      - **accountId** *(string) --*

        The 12-digit AWS account ID associated with the resource.

      - **configurationItemCaptureTime** *(datetime) --*

        The time when the configuration recording was initiated.

      - **configurationItemStatus** *(string) --*

        The configuration item status.

      - **configurationStateId** *(string) --*

        An identifier that indicates the ordering of the configuration items of a resource.

      - **configurationItemMD5Hash** *(string) --*

        Unique MD5 hash that represents the configuration item's state.

        You can use MD5 hash to compare the states of two or more configuration items that are
        associated with the same resource.

      - **arn** *(string) --*

        accoun

      - **resourceType** *(string) --*

        The type of AWS resource.

      - **resourceId** *(string) --*

        The ID of the resource (for example, ``sg-xxxxxx`` ).

      - **resourceName** *(string) --*

        The custom name of the resource, if available.

      - **awsRegion** *(string) --*

        The region where the resource resides.

      - **availabilityZone** *(string) --*

        The Availability Zone associated with the resource.

      - **resourceCreationTime** *(datetime) --*

        The time stamp when the resource was created.

      - **tags** *(dict) --*

        A mapping of key value tags associated with the resource.

        - *(string) --*

          - *(string) --*

      - **relatedEvents** *(list) --*

        A list of CloudTrail event IDs.

        A populated field indicates that the current configuration was initiated by the events
        recorded in the CloudTrail log. For more information about CloudTrail, see `What Is AWS
        CloudTrail
        <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/what_is_cloud_trail_top_level.html>`__
        .

        An empty field indicates that the current configuration was not initiated by any event.

        - *(string) --*

      - **relationships** *(list) --*

        A list of related AWS resources.

        - *(dict) --*

          The relationship of the related resource to the main resource.

          - **resourceType** *(string) --*

            The resource type of the related resource.

          - **resourceId** *(string) --*

            The ID of the related resource (for example, ``sg-xxxxxx`` ).

          - **resourceName** *(string) --*

            The custom name of the related resource, if available.

          - **relationshipName** *(string) --*

            The type of relationship with the related resource.

      - **configuration** *(string) --*

        The description of the resource configuration.

      - **supplementaryConfiguration** *(dict) --*

        Configuration attributes that AWS Config returns for certain resource types to supplement
        the information returned for the ``configuration`` parameter.

        - *(string) --*

          - *(string) --*
    """


_ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef = TypedDict(
    "_ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    {"ConfigRuleName": str, "ResourceType": str, "ResourceId": str},
    total=False,
)


class ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef(
    _ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef
):
    """
    Type definition for `ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsEvaluationResultIdentifier` `EvaluationResultQualifier`

    Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
    and ID of the evaluated resource.

    - **ConfigRuleName** *(string) --*

      The name of the AWS Config rule that was used in the evaluation.

    - **ResourceType** *(string) --*

      The type of AWS resource that was evaluated.

    - **ResourceId** *(string) --*

      The ID of the evaluated AWS resource.
    """


_ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsEvaluationResultIdentifierTypeDef = TypedDict(
    "_ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsEvaluationResultIdentifierTypeDef",
    {
        "EvaluationResultQualifier": ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef,
        "OrderingTimestamp": datetime,
    },
    total=False,
)


class ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsEvaluationResultIdentifierTypeDef(
    _ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsEvaluationResultIdentifierTypeDef
):
    """
    Type definition for `ClientGetComplianceDetailsByConfigRuleResponseEvaluationResults` `EvaluationResultIdentifier`

    Uniquely identifies the evaluation result.

    - **EvaluationResultQualifier** *(dict) --*

      Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
      and ID of the evaluated resource.

      - **ConfigRuleName** *(string) --*

        The name of the AWS Config rule that was used in the evaluation.

      - **ResourceType** *(string) --*

        The type of AWS resource that was evaluated.

      - **ResourceId** *(string) --*

        The ID of the evaluated AWS resource.

    - **OrderingTimestamp** *(datetime) --*

      The time of the event that triggered the evaluation of your AWS resources. The time can
      indicate when AWS Config delivered a configuration item change notification, or it can
      indicate when AWS Config delivered the configuration snapshot, depending on which event
      triggered the evaluation.
    """


_ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsTypeDef = TypedDict(
    "_ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsTypeDef",
    {
        "EvaluationResultIdentifier": ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsEvaluationResultIdentifierTypeDef,
        "ComplianceType": str,
        "ResultRecordedTime": datetime,
        "ConfigRuleInvokedTime": datetime,
        "Annotation": str,
        "ResultToken": str,
    },
    total=False,
)


class ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsTypeDef(
    _ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsTypeDef
):
    """
    Type definition for `ClientGetComplianceDetailsByConfigRuleResponse` `EvaluationResults`

    The details of an AWS Config evaluation. Provides the AWS resource that was evaluated, the
    compliance of the resource, related time stamps, and supplementary information.

    - **EvaluationResultIdentifier** *(dict) --*

      Uniquely identifies the evaluation result.

      - **EvaluationResultQualifier** *(dict) --*

        Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
        and ID of the evaluated resource.

        - **ConfigRuleName** *(string) --*

          The name of the AWS Config rule that was used in the evaluation.

        - **ResourceType** *(string) --*

          The type of AWS resource that was evaluated.

        - **ResourceId** *(string) --*

          The ID of the evaluated AWS resource.

      - **OrderingTimestamp** *(datetime) --*

        The time of the event that triggered the evaluation of your AWS resources. The time can
        indicate when AWS Config delivered a configuration item change notification, or it can
        indicate when AWS Config delivered the configuration snapshot, depending on which event
        triggered the evaluation.

    - **ComplianceType** *(string) --*

      Indicates whether the AWS resource complies with the AWS Config rule that evaluated it.

      For the ``EvaluationResult`` data type, AWS Config supports only the ``COMPLIANT`` ,
      ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` values. AWS Config does not support the
      ``INSUFFICIENT_DATA`` value for the ``EvaluationResult`` data type.

    - **ResultRecordedTime** *(datetime) --*

      The time when AWS Config recorded the evaluation result.

    - **ConfigRuleInvokedTime** *(datetime) --*

      The time when the AWS Config rule evaluated the AWS resource.

    - **Annotation** *(string) --*

      Supplementary information about how the evaluation determined the compliance.

    - **ResultToken** *(string) --*

      An encrypted token that associates an evaluation with an AWS Config rule. The token
      identifies the rule, the AWS resource being evaluated, and the event that triggered the
      evaluation.
    """


_ClientGetComplianceDetailsByConfigRuleResponseTypeDef = TypedDict(
    "_ClientGetComplianceDetailsByConfigRuleResponseTypeDef",
    {
        "EvaluationResults": List[
            ClientGetComplianceDetailsByConfigRuleResponseEvaluationResultsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientGetComplianceDetailsByConfigRuleResponseTypeDef(
    _ClientGetComplianceDetailsByConfigRuleResponseTypeDef
):
    """
    Type definition for `ClientGetComplianceDetailsByConfigRule` `Response`

    - **EvaluationResults** *(list) --*

      Indicates whether the AWS resource complies with the specified AWS Config rule.

      - *(dict) --*

        The details of an AWS Config evaluation. Provides the AWS resource that was evaluated, the
        compliance of the resource, related time stamps, and supplementary information.

        - **EvaluationResultIdentifier** *(dict) --*

          Uniquely identifies the evaluation result.

          - **EvaluationResultQualifier** *(dict) --*

            Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
            and ID of the evaluated resource.

            - **ConfigRuleName** *(string) --*

              The name of the AWS Config rule that was used in the evaluation.

            - **ResourceType** *(string) --*

              The type of AWS resource that was evaluated.

            - **ResourceId** *(string) --*

              The ID of the evaluated AWS resource.

          - **OrderingTimestamp** *(datetime) --*

            The time of the event that triggered the evaluation of your AWS resources. The time can
            indicate when AWS Config delivered a configuration item change notification, or it can
            indicate when AWS Config delivered the configuration snapshot, depending on which event
            triggered the evaluation.

        - **ComplianceType** *(string) --*

          Indicates whether the AWS resource complies with the AWS Config rule that evaluated it.

          For the ``EvaluationResult`` data type, AWS Config supports only the ``COMPLIANT`` ,
          ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` values. AWS Config does not support the
          ``INSUFFICIENT_DATA`` value for the ``EvaluationResult`` data type.

        - **ResultRecordedTime** *(datetime) --*

          The time when AWS Config recorded the evaluation result.

        - **ConfigRuleInvokedTime** *(datetime) --*

          The time when the AWS Config rule evaluated the AWS resource.

        - **Annotation** *(string) --*

          Supplementary information about how the evaluation determined the compliance.

        - **ResultToken** *(string) --*

          An encrypted token that associates an evaluation with an AWS Config rule. The token
          identifies the rule, the AWS resource being evaluated, and the event that triggered the
          evaluation.

    - **NextToken** *(string) --*

      The string that you use in a subsequent request to get the next page of results in a
      paginated response.
    """


_ClientGetComplianceDetailsByResourceResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef = TypedDict(
    "_ClientGetComplianceDetailsByResourceResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    {"ConfigRuleName": str, "ResourceType": str, "ResourceId": str},
    total=False,
)


class ClientGetComplianceDetailsByResourceResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef(
    _ClientGetComplianceDetailsByResourceResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef
):
    """
    Type definition for `ClientGetComplianceDetailsByResourceResponseEvaluationResultsEvaluationResultIdentifier` `EvaluationResultQualifier`

    Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
    and ID of the evaluated resource.

    - **ConfigRuleName** *(string) --*

      The name of the AWS Config rule that was used in the evaluation.

    - **ResourceType** *(string) --*

      The type of AWS resource that was evaluated.

    - **ResourceId** *(string) --*

      The ID of the evaluated AWS resource.
    """


_ClientGetComplianceDetailsByResourceResponseEvaluationResultsEvaluationResultIdentifierTypeDef = TypedDict(
    "_ClientGetComplianceDetailsByResourceResponseEvaluationResultsEvaluationResultIdentifierTypeDef",
    {
        "EvaluationResultQualifier": ClientGetComplianceDetailsByResourceResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef,
        "OrderingTimestamp": datetime,
    },
    total=False,
)


class ClientGetComplianceDetailsByResourceResponseEvaluationResultsEvaluationResultIdentifierTypeDef(
    _ClientGetComplianceDetailsByResourceResponseEvaluationResultsEvaluationResultIdentifierTypeDef
):
    """
    Type definition for `ClientGetComplianceDetailsByResourceResponseEvaluationResults` `EvaluationResultIdentifier`

    Uniquely identifies the evaluation result.

    - **EvaluationResultQualifier** *(dict) --*

      Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
      and ID of the evaluated resource.

      - **ConfigRuleName** *(string) --*

        The name of the AWS Config rule that was used in the evaluation.

      - **ResourceType** *(string) --*

        The type of AWS resource that was evaluated.

      - **ResourceId** *(string) --*

        The ID of the evaluated AWS resource.

    - **OrderingTimestamp** *(datetime) --*

      The time of the event that triggered the evaluation of your AWS resources. The time can
      indicate when AWS Config delivered a configuration item change notification, or it can
      indicate when AWS Config delivered the configuration snapshot, depending on which event
      triggered the evaluation.
    """


_ClientGetComplianceDetailsByResourceResponseEvaluationResultsTypeDef = TypedDict(
    "_ClientGetComplianceDetailsByResourceResponseEvaluationResultsTypeDef",
    {
        "EvaluationResultIdentifier": ClientGetComplianceDetailsByResourceResponseEvaluationResultsEvaluationResultIdentifierTypeDef,
        "ComplianceType": str,
        "ResultRecordedTime": datetime,
        "ConfigRuleInvokedTime": datetime,
        "Annotation": str,
        "ResultToken": str,
    },
    total=False,
)


class ClientGetComplianceDetailsByResourceResponseEvaluationResultsTypeDef(
    _ClientGetComplianceDetailsByResourceResponseEvaluationResultsTypeDef
):
    """
    Type definition for `ClientGetComplianceDetailsByResourceResponse` `EvaluationResults`

    The details of an AWS Config evaluation. Provides the AWS resource that was evaluated, the
    compliance of the resource, related time stamps, and supplementary information.

    - **EvaluationResultIdentifier** *(dict) --*

      Uniquely identifies the evaluation result.

      - **EvaluationResultQualifier** *(dict) --*

        Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
        and ID of the evaluated resource.

        - **ConfigRuleName** *(string) --*

          The name of the AWS Config rule that was used in the evaluation.

        - **ResourceType** *(string) --*

          The type of AWS resource that was evaluated.

        - **ResourceId** *(string) --*

          The ID of the evaluated AWS resource.

      - **OrderingTimestamp** *(datetime) --*

        The time of the event that triggered the evaluation of your AWS resources. The time can
        indicate when AWS Config delivered a configuration item change notification, or it can
        indicate when AWS Config delivered the configuration snapshot, depending on which event
        triggered the evaluation.

    - **ComplianceType** *(string) --*

      Indicates whether the AWS resource complies with the AWS Config rule that evaluated it.

      For the ``EvaluationResult`` data type, AWS Config supports only the ``COMPLIANT`` ,
      ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` values. AWS Config does not support the
      ``INSUFFICIENT_DATA`` value for the ``EvaluationResult`` data type.

    - **ResultRecordedTime** *(datetime) --*

      The time when AWS Config recorded the evaluation result.

    - **ConfigRuleInvokedTime** *(datetime) --*

      The time when the AWS Config rule evaluated the AWS resource.

    - **Annotation** *(string) --*

      Supplementary information about how the evaluation determined the compliance.

    - **ResultToken** *(string) --*

      An encrypted token that associates an evaluation with an AWS Config rule. The token
      identifies the rule, the AWS resource being evaluated, and the event that triggered the
      evaluation.
    """


_ClientGetComplianceDetailsByResourceResponseTypeDef = TypedDict(
    "_ClientGetComplianceDetailsByResourceResponseTypeDef",
    {
        "EvaluationResults": List[
            ClientGetComplianceDetailsByResourceResponseEvaluationResultsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientGetComplianceDetailsByResourceResponseTypeDef(
    _ClientGetComplianceDetailsByResourceResponseTypeDef
):
    """
    Type definition for `ClientGetComplianceDetailsByResource` `Response`

    - **EvaluationResults** *(list) --*

      Indicates whether the specified AWS resource complies each AWS Config rule.

      - *(dict) --*

        The details of an AWS Config evaluation. Provides the AWS resource that was evaluated, the
        compliance of the resource, related time stamps, and supplementary information.

        - **EvaluationResultIdentifier** *(dict) --*

          Uniquely identifies the evaluation result.

          - **EvaluationResultQualifier** *(dict) --*

            Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
            and ID of the evaluated resource.

            - **ConfigRuleName** *(string) --*

              The name of the AWS Config rule that was used in the evaluation.

            - **ResourceType** *(string) --*

              The type of AWS resource that was evaluated.

            - **ResourceId** *(string) --*

              The ID of the evaluated AWS resource.

          - **OrderingTimestamp** *(datetime) --*

            The time of the event that triggered the evaluation of your AWS resources. The time can
            indicate when AWS Config delivered a configuration item change notification, or it can
            indicate when AWS Config delivered the configuration snapshot, depending on which event
            triggered the evaluation.

        - **ComplianceType** *(string) --*

          Indicates whether the AWS resource complies with the AWS Config rule that evaluated it.

          For the ``EvaluationResult`` data type, AWS Config supports only the ``COMPLIANT`` ,
          ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` values. AWS Config does not support the
          ``INSUFFICIENT_DATA`` value for the ``EvaluationResult`` data type.

        - **ResultRecordedTime** *(datetime) --*

          The time when AWS Config recorded the evaluation result.

        - **ConfigRuleInvokedTime** *(datetime) --*

          The time when the AWS Config rule evaluated the AWS resource.

        - **Annotation** *(string) --*

          Supplementary information about how the evaluation determined the compliance.

        - **ResultToken** *(string) --*

          An encrypted token that associates an evaluation with an AWS Config rule. The token
          identifies the rule, the AWS resource being evaluated, and the event that triggered the
          evaluation.

    - **NextToken** *(string) --*

      The string that you use in a subsequent request to get the next page of results in a
      paginated response.
    """


_ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryCompliantResourceCountTypeDef = TypedDict(
    "_ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryCompliantResourceCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)


class ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryCompliantResourceCountTypeDef(
    _ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryCompliantResourceCountTypeDef
):
    """
    Type definition for `ClientGetComplianceSummaryByConfigRuleResponseComplianceSummary` `CompliantResourceCount`

    The number of AWS Config rules or AWS resources that are compliant, up to a maximum of 25
    for rules and 100 for resources.

    - **CappedCount** *(integer) --*

      The number of AWS resources or AWS Config rules responsible for the current compliance of
      the item.

    - **CapExceeded** *(boolean) --*

      Indicates whether the maximum count is reached.
    """


_ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryNonCompliantResourceCountTypeDef = TypedDict(
    "_ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryNonCompliantResourceCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)


class ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryNonCompliantResourceCountTypeDef(
    _ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryNonCompliantResourceCountTypeDef
):
    """
    Type definition for `ClientGetComplianceSummaryByConfigRuleResponseComplianceSummary` `NonCompliantResourceCount`

    The number of AWS Config rules or AWS resources that are noncompliant, up to a maximum of
    25 for rules and 100 for resources.

    - **CappedCount** *(integer) --*

      The number of AWS resources or AWS Config rules responsible for the current compliance of
      the item.

    - **CapExceeded** *(boolean) --*

      Indicates whether the maximum count is reached.
    """


_ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryTypeDef = TypedDict(
    "_ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryTypeDef",
    {
        "CompliantResourceCount": ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryCompliantResourceCountTypeDef,
        "NonCompliantResourceCount": ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryNonCompliantResourceCountTypeDef,
        "ComplianceSummaryTimestamp": datetime,
    },
    total=False,
)


class ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryTypeDef(
    _ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryTypeDef
):
    """
    Type definition for `ClientGetComplianceSummaryByConfigRuleResponse` `ComplianceSummary`

    The number of AWS Config rules that are compliant and the number that are noncompliant, up to
    a maximum of 25 for each.

    - **CompliantResourceCount** *(dict) --*

      The number of AWS Config rules or AWS resources that are compliant, up to a maximum of 25
      for rules and 100 for resources.

      - **CappedCount** *(integer) --*

        The number of AWS resources or AWS Config rules responsible for the current compliance of
        the item.

      - **CapExceeded** *(boolean) --*

        Indicates whether the maximum count is reached.

    - **NonCompliantResourceCount** *(dict) --*

      The number of AWS Config rules or AWS resources that are noncompliant, up to a maximum of
      25 for rules and 100 for resources.

      - **CappedCount** *(integer) --*

        The number of AWS resources or AWS Config rules responsible for the current compliance of
        the item.

      - **CapExceeded** *(boolean) --*

        Indicates whether the maximum count is reached.

    - **ComplianceSummaryTimestamp** *(datetime) --*

      The time that AWS Config created the compliance summary.
    """


_ClientGetComplianceSummaryByConfigRuleResponseTypeDef = TypedDict(
    "_ClientGetComplianceSummaryByConfigRuleResponseTypeDef",
    {
        "ComplianceSummary": ClientGetComplianceSummaryByConfigRuleResponseComplianceSummaryTypeDef
    },
    total=False,
)


class ClientGetComplianceSummaryByConfigRuleResponseTypeDef(
    _ClientGetComplianceSummaryByConfigRuleResponseTypeDef
):
    """
    Type definition for `ClientGetComplianceSummaryByConfigRule` `Response`

    - **ComplianceSummary** *(dict) --*

      The number of AWS Config rules that are compliant and the number that are noncompliant, up to
      a maximum of 25 for each.

      - **CompliantResourceCount** *(dict) --*

        The number of AWS Config rules or AWS resources that are compliant, up to a maximum of 25
        for rules and 100 for resources.

        - **CappedCount** *(integer) --*

          The number of AWS resources or AWS Config rules responsible for the current compliance of
          the item.

        - **CapExceeded** *(boolean) --*

          Indicates whether the maximum count is reached.

      - **NonCompliantResourceCount** *(dict) --*

        The number of AWS Config rules or AWS resources that are noncompliant, up to a maximum of
        25 for rules and 100 for resources.

        - **CappedCount** *(integer) --*

          The number of AWS resources or AWS Config rules responsible for the current compliance of
          the item.

        - **CapExceeded** *(boolean) --*

          Indicates whether the maximum count is reached.

      - **ComplianceSummaryTimestamp** *(datetime) --*

        The time that AWS Config created the compliance summary.
    """


_ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryCompliantResourceCountTypeDef = TypedDict(
    "_ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryCompliantResourceCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)


class ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryCompliantResourceCountTypeDef(
    _ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryCompliantResourceCountTypeDef
):
    """
    Type definition for `ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummary` `CompliantResourceCount`

    The number of AWS Config rules or AWS resources that are compliant, up to a maximum of
    25 for rules and 100 for resources.

    - **CappedCount** *(integer) --*

      The number of AWS resources or AWS Config rules responsible for the current
      compliance of the item.

    - **CapExceeded** *(boolean) --*

      Indicates whether the maximum count is reached.
    """


_ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryNonCompliantResourceCountTypeDef = TypedDict(
    "_ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryNonCompliantResourceCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)


class ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryNonCompliantResourceCountTypeDef(
    _ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryNonCompliantResourceCountTypeDef
):
    """
    Type definition for `ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummary` `NonCompliantResourceCount`

    The number of AWS Config rules or AWS resources that are noncompliant, up to a maximum
    of 25 for rules and 100 for resources.

    - **CappedCount** *(integer) --*

      The number of AWS resources or AWS Config rules responsible for the current
      compliance of the item.

    - **CapExceeded** *(boolean) --*

      Indicates whether the maximum count is reached.
    """


_ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryTypeDef = TypedDict(
    "_ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryTypeDef",
    {
        "CompliantResourceCount": ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryCompliantResourceCountTypeDef,
        "NonCompliantResourceCount": ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryNonCompliantResourceCountTypeDef,
        "ComplianceSummaryTimestamp": datetime,
    },
    total=False,
)


class ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryTypeDef(
    _ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryTypeDef
):
    """
    Type definition for `ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceType` `ComplianceSummary`

    The number of AWS resources that are compliant or noncompliant, up to a maximum of 100
    for each.

    - **CompliantResourceCount** *(dict) --*

      The number of AWS Config rules or AWS resources that are compliant, up to a maximum of
      25 for rules and 100 for resources.

      - **CappedCount** *(integer) --*

        The number of AWS resources or AWS Config rules responsible for the current
        compliance of the item.

      - **CapExceeded** *(boolean) --*

        Indicates whether the maximum count is reached.

    - **NonCompliantResourceCount** *(dict) --*

      The number of AWS Config rules or AWS resources that are noncompliant, up to a maximum
      of 25 for rules and 100 for resources.

      - **CappedCount** *(integer) --*

        The number of AWS resources or AWS Config rules responsible for the current
        compliance of the item.

      - **CapExceeded** *(boolean) --*

        Indicates whether the maximum count is reached.

    - **ComplianceSummaryTimestamp** *(datetime) --*

      The time that AWS Config created the compliance summary.
    """


_ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeTypeDef = TypedDict(
    "_ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeTypeDef",
    {
        "ResourceType": str,
        "ComplianceSummary": ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeComplianceSummaryTypeDef,
    },
    total=False,
)


class ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeTypeDef(
    _ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeTypeDef
):
    """
    Type definition for `ClientGetComplianceSummaryByResourceTypeResponse` `ComplianceSummariesByResourceType`

    The number of AWS resources of a specific type that are compliant or noncompliant, up to a
    maximum of 100 for each.

    - **ResourceType** *(string) --*

      The type of AWS resource.

    - **ComplianceSummary** *(dict) --*

      The number of AWS resources that are compliant or noncompliant, up to a maximum of 100
      for each.

      - **CompliantResourceCount** *(dict) --*

        The number of AWS Config rules or AWS resources that are compliant, up to a maximum of
        25 for rules and 100 for resources.

        - **CappedCount** *(integer) --*

          The number of AWS resources or AWS Config rules responsible for the current
          compliance of the item.

        - **CapExceeded** *(boolean) --*

          Indicates whether the maximum count is reached.

      - **NonCompliantResourceCount** *(dict) --*

        The number of AWS Config rules or AWS resources that are noncompliant, up to a maximum
        of 25 for rules and 100 for resources.

        - **CappedCount** *(integer) --*

          The number of AWS resources or AWS Config rules responsible for the current
          compliance of the item.

        - **CapExceeded** *(boolean) --*

          Indicates whether the maximum count is reached.

      - **ComplianceSummaryTimestamp** *(datetime) --*

        The time that AWS Config created the compliance summary.
    """


_ClientGetComplianceSummaryByResourceTypeResponseTypeDef = TypedDict(
    "_ClientGetComplianceSummaryByResourceTypeResponseTypeDef",
    {
        "ComplianceSummariesByResourceType": List[
            ClientGetComplianceSummaryByResourceTypeResponseComplianceSummariesByResourceTypeTypeDef
        ]
    },
    total=False,
)


class ClientGetComplianceSummaryByResourceTypeResponseTypeDef(
    _ClientGetComplianceSummaryByResourceTypeResponseTypeDef
):
    """
    Type definition for `ClientGetComplianceSummaryByResourceType` `Response`

    - **ComplianceSummariesByResourceType** *(list) --*

      The number of resources that are compliant and the number that are noncompliant. If one or
      more resource types were provided with the request, the numbers are returned for each
      resource type. The maximum number returned is 100.

      - *(dict) --*

        The number of AWS resources of a specific type that are compliant or noncompliant, up to a
        maximum of 100 for each.

        - **ResourceType** *(string) --*

          The type of AWS resource.

        - **ComplianceSummary** *(dict) --*

          The number of AWS resources that are compliant or noncompliant, up to a maximum of 100
          for each.

          - **CompliantResourceCount** *(dict) --*

            The number of AWS Config rules or AWS resources that are compliant, up to a maximum of
            25 for rules and 100 for resources.

            - **CappedCount** *(integer) --*

              The number of AWS resources or AWS Config rules responsible for the current
              compliance of the item.

            - **CapExceeded** *(boolean) --*

              Indicates whether the maximum count is reached.

          - **NonCompliantResourceCount** *(dict) --*

            The number of AWS Config rules or AWS resources that are noncompliant, up to a maximum
            of 25 for rules and 100 for resources.

            - **CappedCount** *(integer) --*

              The number of AWS resources or AWS Config rules responsible for the current
              compliance of the item.

            - **CapExceeded** *(boolean) --*

              Indicates whether the maximum count is reached.

          - **ComplianceSummaryTimestamp** *(datetime) --*

            The time that AWS Config created the compliance summary.
    """


_ClientGetConformancePackComplianceDetailsFiltersTypeDef = TypedDict(
    "_ClientGetConformancePackComplianceDetailsFiltersTypeDef",
    {
        "ConfigRuleNames": List[str],
        "ComplianceType": str,
        "ResourceType": str,
        "ResourceIds": List[str],
    },
    total=False,
)


class ClientGetConformancePackComplianceDetailsFiltersTypeDef(
    _ClientGetConformancePackComplianceDetailsFiltersTypeDef
):
    """
    Type definition for `ClientGetConformancePackComplianceDetails` `Filters`

    A ``ConformancePackEvaluationFilters`` object.

    - **ConfigRuleNames** *(list) --*

      Filters the results by AWS Config rule names.

      - *(string) --*

    - **ComplianceType** *(string) --*

      Filters the results by compliance.

      The allowed values are ``COMPLIANT`` and ``NON_COMPLIANT`` .

    - **ResourceType** *(string) --*

      Filters the results by the resource type (for example, ``"AWS::EC2::Instance"`` ).

    - **ResourceIds** *(list) --*

      Filters the results by resource IDs.

      - *(string) --*
    """


_ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef = TypedDict(
    "_ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    {"ConfigRuleName": str, "ResourceType": str, "ResourceId": str},
    total=False,
)


class ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef(
    _ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef
):
    """
    Type definition for `ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsEvaluationResultIdentifier` `EvaluationResultQualifier`

    Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
    and ID of the evaluated resource.

    - **ConfigRuleName** *(string) --*

      The name of the AWS Config rule that was used in the evaluation.

    - **ResourceType** *(string) --*

      The type of AWS resource that was evaluated.

    - **ResourceId** *(string) --*

      The ID of the evaluated AWS resource.
    """


_ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsEvaluationResultIdentifierTypeDef = TypedDict(
    "_ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsEvaluationResultIdentifierTypeDef",
    {
        "EvaluationResultQualifier": ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef,
        "OrderingTimestamp": datetime,
    },
    total=False,
)


class ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsEvaluationResultIdentifierTypeDef(
    _ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsEvaluationResultIdentifierTypeDef
):
    """
    Type definition for `ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResults` `EvaluationResultIdentifier`

    Uniquely identifies an evaluation result.

    - **EvaluationResultQualifier** *(dict) --*

      Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
      and ID of the evaluated resource.

      - **ConfigRuleName** *(string) --*

        The name of the AWS Config rule that was used in the evaluation.

      - **ResourceType** *(string) --*

        The type of AWS resource that was evaluated.

      - **ResourceId** *(string) --*

        The ID of the evaluated AWS resource.

    - **OrderingTimestamp** *(datetime) --*

      The time of the event that triggered the evaluation of your AWS resources. The time can
      indicate when AWS Config delivered a configuration item change notification, or it can
      indicate when AWS Config delivered the configuration snapshot, depending on which event
      triggered the evaluation.
    """


_ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsTypeDef = TypedDict(
    "_ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsTypeDef",
    {
        "ComplianceType": str,
        "EvaluationResultIdentifier": ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsEvaluationResultIdentifierTypeDef,
        "ConfigRuleInvokedTime": datetime,
        "ResultRecordedTime": datetime,
        "Annotation": str,
    },
    total=False,
)


class ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsTypeDef(
    _ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsTypeDef
):
    """
    Type definition for `ClientGetConformancePackComplianceDetailsResponse` `ConformancePackRuleEvaluationResults`

    The details of a conformance pack evaluation. Provides AWS Config rule and AWS resource
    type that was evaluated, the compliance of the conformance pack, related time stamps, and
    supplementary information.

    - **ComplianceType** *(string) --*

      Filters the results by compliance.

      The allowed values are ``COMPLIANT`` and ``NON_COMPLIANT`` .

    - **EvaluationResultIdentifier** *(dict) --*

      Uniquely identifies an evaluation result.

      - **EvaluationResultQualifier** *(dict) --*

        Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
        and ID of the evaluated resource.

        - **ConfigRuleName** *(string) --*

          The name of the AWS Config rule that was used in the evaluation.

        - **ResourceType** *(string) --*

          The type of AWS resource that was evaluated.

        - **ResourceId** *(string) --*

          The ID of the evaluated AWS resource.

      - **OrderingTimestamp** *(datetime) --*

        The time of the event that triggered the evaluation of your AWS resources. The time can
        indicate when AWS Config delivered a configuration item change notification, or it can
        indicate when AWS Config delivered the configuration snapshot, depending on which event
        triggered the evaluation.

    - **ConfigRuleInvokedTime** *(datetime) --*

      The time when AWS Config rule evaluated AWS resource.

    - **ResultRecordedTime** *(datetime) --*

      The time when AWS Config recorded the evaluation result.

    - **Annotation** *(string) --*

      Supplementary information about how the evaluation determined the compliance.
    """


_ClientGetConformancePackComplianceDetailsResponseTypeDef = TypedDict(
    "_ClientGetConformancePackComplianceDetailsResponseTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackRuleEvaluationResults": List[
            ClientGetConformancePackComplianceDetailsResponseConformancePackRuleEvaluationResultsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientGetConformancePackComplianceDetailsResponseTypeDef(
    _ClientGetConformancePackComplianceDetailsResponseTypeDef
):
    """
    Type definition for `ClientGetConformancePackComplianceDetails` `Response`

    - **ConformancePackName** *(string) --*

      Name of the conformance pack.

    - **ConformancePackRuleEvaluationResults** *(list) --*

      Returns a list of ``ConformancePackEvaluationResult`` objects.

      - *(dict) --*

        The details of a conformance pack evaluation. Provides AWS Config rule and AWS resource
        type that was evaluated, the compliance of the conformance pack, related time stamps, and
        supplementary information.

        - **ComplianceType** *(string) --*

          Filters the results by compliance.

          The allowed values are ``COMPLIANT`` and ``NON_COMPLIANT`` .

        - **EvaluationResultIdentifier** *(dict) --*

          Uniquely identifies an evaluation result.

          - **EvaluationResultQualifier** *(dict) --*

            Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
            and ID of the evaluated resource.

            - **ConfigRuleName** *(string) --*

              The name of the AWS Config rule that was used in the evaluation.

            - **ResourceType** *(string) --*

              The type of AWS resource that was evaluated.

            - **ResourceId** *(string) --*

              The ID of the evaluated AWS resource.

          - **OrderingTimestamp** *(datetime) --*

            The time of the event that triggered the evaluation of your AWS resources. The time can
            indicate when AWS Config delivered a configuration item change notification, or it can
            indicate when AWS Config delivered the configuration snapshot, depending on which event
            triggered the evaluation.

        - **ConfigRuleInvokedTime** *(datetime) --*

          The time when AWS Config rule evaluated AWS resource.

        - **ResultRecordedTime** *(datetime) --*

          The time when AWS Config recorded the evaluation result.

        - **Annotation** *(string) --*

          Supplementary information about how the evaluation determined the compliance.

    - **NextToken** *(string) --*

      The ``nextToken`` string returned in a previous request that you use to request the next page
      of results in a paginated response.
    """


_ClientGetConformancePackComplianceSummaryResponseConformancePackComplianceSummaryListTypeDef = TypedDict(
    "_ClientGetConformancePackComplianceSummaryResponseConformancePackComplianceSummaryListTypeDef",
    {"ConformancePackName": str, "ConformancePackComplianceStatus": str},
    total=False,
)


class ClientGetConformancePackComplianceSummaryResponseConformancePackComplianceSummaryListTypeDef(
    _ClientGetConformancePackComplianceSummaryResponseConformancePackComplianceSummaryListTypeDef
):
    """
    Type definition for `ClientGetConformancePackComplianceSummaryResponse` `ConformancePackComplianceSummaryList`

    - **ConformancePackName** *(string) --*

    - **ConformancePackComplianceStatus** *(string) --*
    """


_ClientGetConformancePackComplianceSummaryResponseTypeDef = TypedDict(
    "_ClientGetConformancePackComplianceSummaryResponseTypeDef",
    {
        "ConformancePackComplianceSummaryList": List[
            ClientGetConformancePackComplianceSummaryResponseConformancePackComplianceSummaryListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientGetConformancePackComplianceSummaryResponseTypeDef(
    _ClientGetConformancePackComplianceSummaryResponseTypeDef
):
    """
    Type definition for `ClientGetConformancePackComplianceSummary` `Response`

    - **ConformancePackComplianceSummaryList** *(list) --*

      - *(dict) --*

        - **ConformancePackName** *(string) --*

        - **ConformancePackComplianceStatus** *(string) --*

    - **NextToken** *(string) --*
    """


_ClientGetDiscoveredResourceCountsResponseresourceCountsTypeDef = TypedDict(
    "_ClientGetDiscoveredResourceCountsResponseresourceCountsTypeDef",
    {"resourceType": str, "count": int},
    total=False,
)


class ClientGetDiscoveredResourceCountsResponseresourceCountsTypeDef(
    _ClientGetDiscoveredResourceCountsResponseresourceCountsTypeDef
):
    """
    Type definition for `ClientGetDiscoveredResourceCountsResponse` `resourceCounts`

    An object that contains the resource type and the number of resources.

    - **resourceType** *(string) --*

      The resource type (for example, ``"AWS::EC2::Instance"`` ).

    - **count** *(integer) --*

      The number of resources.
    """


_ClientGetDiscoveredResourceCountsResponseTypeDef = TypedDict(
    "_ClientGetDiscoveredResourceCountsResponseTypeDef",
    {
        "totalDiscoveredResources": int,
        "resourceCounts": List[
            ClientGetDiscoveredResourceCountsResponseresourceCountsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientGetDiscoveredResourceCountsResponseTypeDef(
    _ClientGetDiscoveredResourceCountsResponseTypeDef
):
    """
    Type definition for `ClientGetDiscoveredResourceCounts` `Response`

    - **totalDiscoveredResources** *(integer) --*

      The total number of resources that AWS Config is recording in the region for your account. If
      you specify resource types in the request, AWS Config returns only the total number of
      resources for those resource types.

       **Example**

      * AWS Config is recording three resource types in the US East (Ohio) Region for your account:
      25 EC2 instances, 20 IAM users, and 15 S3 buckets, for a total of 60 resources.

      * You make a call to the ``GetDiscoveredResourceCounts`` action and specify the resource
      type, ``"AWS::EC2::Instances"`` , in the request.

      * AWS Config returns 25 for ``totalDiscoveredResources`` .

    - **resourceCounts** *(list) --*

      The list of ``ResourceCount`` objects. Each object is listed in descending order by the
      number of resources.

      - *(dict) --*

        An object that contains the resource type and the number of resources.

        - **resourceType** *(string) --*

          The resource type (for example, ``"AWS::EC2::Instance"`` ).

        - **count** *(integer) --*

          The number of resources.

    - **nextToken** *(string) --*

      The string that you use in a subsequent request to get the next page of results in a
      paginated response.
    """


_ClientGetOrganizationConfigRuleDetailedStatusFiltersTypeDef = TypedDict(
    "_ClientGetOrganizationConfigRuleDetailedStatusFiltersTypeDef",
    {"AccountId": str, "MemberAccountRuleStatus": str},
    total=False,
)


class ClientGetOrganizationConfigRuleDetailedStatusFiltersTypeDef(
    _ClientGetOrganizationConfigRuleDetailedStatusFiltersTypeDef
):
    """
    Type definition for `ClientGetOrganizationConfigRuleDetailedStatus` `Filters`

    A ``StatusDetailFilters`` object.

    - **AccountId** *(string) --*

      The 12-digit account ID of the member account within an organization.

    - **MemberAccountRuleStatus** *(string) --*

      Indicates deployment status for config rule in the member account. When master account calls
      ``PutOrganizationConfigRule`` action for the first time, config rule status is created in the
      member account. When master account calls ``PutOrganizationConfigRule`` action for the second
      time, config rule status is updated in the member account. Config rule status is deleted when
      the master account deletes ``OrganizationConfigRule`` and disables service access for
      ``config-multiaccountsetup.amazonaws.com`` .

      AWS Config sets the state of the rule to:

      * ``CREATE_SUCCESSFUL`` when config rule has been created in the member account.

      * ``CREATE_IN_PROGRESS`` when config rule is being created in the member account.

      * ``CREATE_FAILED`` when config rule creation has failed in the member account.

      * ``DELETE_FAILED`` when config rule deletion has failed in the member account.

      * ``DELETE_IN_PROGRESS`` when config rule is being deleted in the member account.

      * ``DELETE_SUCCESSFUL`` when config rule has been deleted in the member account.

      * ``UPDATE_SUCCESSFUL`` when config rule has been updated in the member account.

      * ``UPDATE_IN_PROGRESS`` when config rule is being updated in the member account.

      * ``UPDATE_FAILED`` when config rule deletion has failed in the member account.
    """


_ClientGetOrganizationConfigRuleDetailedStatusResponseOrganizationConfigRuleDetailedStatusTypeDef = TypedDict(
    "_ClientGetOrganizationConfigRuleDetailedStatusResponseOrganizationConfigRuleDetailedStatusTypeDef",
    {
        "AccountId": str,
        "ConfigRuleName": str,
        "MemberAccountRuleStatus": str,
        "ErrorCode": str,
        "ErrorMessage": str,
        "LastUpdateTime": datetime,
    },
    total=False,
)


class ClientGetOrganizationConfigRuleDetailedStatusResponseOrganizationConfigRuleDetailedStatusTypeDef(
    _ClientGetOrganizationConfigRuleDetailedStatusResponseOrganizationConfigRuleDetailedStatusTypeDef
):
    """
    Type definition for `ClientGetOrganizationConfigRuleDetailedStatusResponse` `OrganizationConfigRuleDetailedStatus`

    Organization config rule creation or deletion status in each member account. This includes
    the name of the rule, the status, error code and error message when the rule creation or
    deletion failed.

    - **AccountId** *(string) --*

      The 12-digit account ID of a member account.

    - **ConfigRuleName** *(string) --*

      The name of config rule deployed in the member account.

    - **MemberAccountRuleStatus** *(string) --*

      Indicates deployment status for config rule in the member account. When master account
      calls ``PutOrganizationConfigRule`` action for the first time, config rule status is
      created in the member account. When master account calls ``PutOrganizationConfigRule``
      action for the second time, config rule status is updated in the member account. Config
      rule status is deleted when the master account deletes ``OrganizationConfigRule`` and
      disables service access for ``config-multiaccountsetup.amazonaws.com`` .

      AWS Config sets the state of the rule to:

      * ``CREATE_SUCCESSFUL`` when config rule has been created in the member account.

      * ``CREATE_IN_PROGRESS`` when config rule is being created in the member account.

      * ``CREATE_FAILED`` when config rule creation has failed in the member account.

      * ``DELETE_FAILED`` when config rule deletion has failed in the member account.

      * ``DELETE_IN_PROGRESS`` when config rule is being deleted in the member account.

      * ``DELETE_SUCCESSFUL`` when config rule has been deleted in the member account.

      * ``UPDATE_SUCCESSFUL`` when config rule has been updated in the member account.

      * ``UPDATE_IN_PROGRESS`` when config rule is being updated in the member account.

      * ``UPDATE_FAILED`` when config rule deletion has failed in the member account.

    - **ErrorCode** *(string) --*

      An error code that is returned when config rule creation or deletion failed in the member
      account.

    - **ErrorMessage** *(string) --*

      An error message indicating that config rule account creation or deletion has failed due
      to an error in the member account.

    - **LastUpdateTime** *(datetime) --*

      The timestamp of the last status update.
    """


_ClientGetOrganizationConfigRuleDetailedStatusResponseTypeDef = TypedDict(
    "_ClientGetOrganizationConfigRuleDetailedStatusResponseTypeDef",
    {
        "OrganizationConfigRuleDetailedStatus": List[
            ClientGetOrganizationConfigRuleDetailedStatusResponseOrganizationConfigRuleDetailedStatusTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientGetOrganizationConfigRuleDetailedStatusResponseTypeDef(
    _ClientGetOrganizationConfigRuleDetailedStatusResponseTypeDef
):
    """
    Type definition for `ClientGetOrganizationConfigRuleDetailedStatus` `Response`

    - **OrganizationConfigRuleDetailedStatus** *(list) --*

      A list of ``MemberAccountStatus`` objects.

      - *(dict) --*

        Organization config rule creation or deletion status in each member account. This includes
        the name of the rule, the status, error code and error message when the rule creation or
        deletion failed.

        - **AccountId** *(string) --*

          The 12-digit account ID of a member account.

        - **ConfigRuleName** *(string) --*

          The name of config rule deployed in the member account.

        - **MemberAccountRuleStatus** *(string) --*

          Indicates deployment status for config rule in the member account. When master account
          calls ``PutOrganizationConfigRule`` action for the first time, config rule status is
          created in the member account. When master account calls ``PutOrganizationConfigRule``
          action for the second time, config rule status is updated in the member account. Config
          rule status is deleted when the master account deletes ``OrganizationConfigRule`` and
          disables service access for ``config-multiaccountsetup.amazonaws.com`` .

          AWS Config sets the state of the rule to:

          * ``CREATE_SUCCESSFUL`` when config rule has been created in the member account.

          * ``CREATE_IN_PROGRESS`` when config rule is being created in the member account.

          * ``CREATE_FAILED`` when config rule creation has failed in the member account.

          * ``DELETE_FAILED`` when config rule deletion has failed in the member account.

          * ``DELETE_IN_PROGRESS`` when config rule is being deleted in the member account.

          * ``DELETE_SUCCESSFUL`` when config rule has been deleted in the member account.

          * ``UPDATE_SUCCESSFUL`` when config rule has been updated in the member account.

          * ``UPDATE_IN_PROGRESS`` when config rule is being updated in the member account.

          * ``UPDATE_FAILED`` when config rule deletion has failed in the member account.

        - **ErrorCode** *(string) --*

          An error code that is returned when config rule creation or deletion failed in the member
          account.

        - **ErrorMessage** *(string) --*

          An error message indicating that config rule account creation or deletion has failed due
          to an error in the member account.

        - **LastUpdateTime** *(datetime) --*

          The timestamp of the last status update.

    - **NextToken** *(string) --*

      The ``nextToken`` string returned on a previous page that you use to get the next page of
      results in a paginated response.
    """


_ClientGetOrganizationConformancePackDetailedStatusFiltersTypeDef = TypedDict(
    "_ClientGetOrganizationConformancePackDetailedStatusFiltersTypeDef",
    {"AccountId": str, "Status": str},
    total=False,
)


class ClientGetOrganizationConformancePackDetailedStatusFiltersTypeDef(
    _ClientGetOrganizationConformancePackDetailedStatusFiltersTypeDef
):
    """
    Type definition for `ClientGetOrganizationConformancePackDetailedStatus` `Filters`

    An ``OrganizationResourceDetailedStatusFilters`` object.

    - **AccountId** *(string) --*

      The 12-digit account ID of the member account within an organization.

    - **Status** *(string) --*

      Indicates deployment status for conformance pack in a member account. When master account calls
      ``PutOrganizationConformancePack`` action for the first time, conformance pack status is
      created in the member account. When master account calls ``PutOrganizationConformancePack``
      action for the second time, conformance pack status is updated in the member account.
      Conformance pack status is deleted when the master account deletes
      ``OrganizationConformancePack`` and disables service access for
      ``config-multiaccountsetup.amazonaws.com`` .

      AWS Config sets the state of the conformance pack to:

      * ``CREATE_SUCCESSFUL`` when conformance pack has been created in the member account.

      * ``CREATE_IN_PROGRESS`` when conformance pack is being created in the member account.

      * ``CREATE_FAILED`` when conformance pack creation has failed in the member account.

      * ``DELETE_FAILED`` when conformance pack deletion has failed in the member account.

      * ``DELETE_IN_PROGRESS`` when conformance pack is being deleted in the member account.

      * ``DELETE_SUCCESSFUL`` when conformance pack has been deleted in the member account.

      * ``UPDATE_SUCCESSFUL`` when conformance pack has been updated in the member account.

      * ``UPDATE_IN_PROGRESS`` when conformance pack is being updated in the member account.

      * ``UPDATE_FAILED`` when conformance pack deletion has failed in the member account.
    """


_ClientGetOrganizationConformancePackDetailedStatusResponseOrganizationConformancePackDetailedStatusesTypeDef = TypedDict(
    "_ClientGetOrganizationConformancePackDetailedStatusResponseOrganizationConformancePackDetailedStatusesTypeDef",
    {
        "AccountId": str,
        "ConformancePackName": str,
        "Status": str,
        "ErrorCode": str,
        "ErrorMessage": str,
        "LastUpdateTime": datetime,
    },
    total=False,
)


class ClientGetOrganizationConformancePackDetailedStatusResponseOrganizationConformancePackDetailedStatusesTypeDef(
    _ClientGetOrganizationConformancePackDetailedStatusResponseOrganizationConformancePackDetailedStatusesTypeDef
):
    """
    Type definition for `ClientGetOrganizationConformancePackDetailedStatusResponse` `OrganizationConformancePackDetailedStatuses`

    Organization conformance pack creation or deletion status in each member account. This
    includes the name of the conformance pack, the status, error code and error message when
    the conformance pack creation or deletion failed.

    - **AccountId** *(string) --*

      The 12-digit account ID of a member account.

    - **ConformancePackName** *(string) --*

      The name of conformance pack deployed in the member account.

    - **Status** *(string) --*

      Indicates deployment status for conformance pack in a member account. When master account
      calls ``PutOrganizationConformancePack`` action for the first time, conformance pack
      status is created in the member account. When master account calls
      ``PutOrganizationConformancePack`` action for the second time, conformance pack status is
      updated in the member account. Conformance pack status is deleted when the master account
      deletes ``OrganizationConformancePack`` and disables service access for
      ``config-multiaccountsetup.amazonaws.com`` .

      AWS Config sets the state of the conformance pack to:

      * ``CREATE_SUCCESSFUL`` when conformance pack has been created in the member account.

      * ``CREATE_IN_PROGRESS`` when conformance pack is being created in the member account.

      * ``CREATE_FAILED`` when conformance pack creation has failed in the member account.

      * ``DELETE_FAILED`` when conformance pack deletion has failed in the member account.

      * ``DELETE_IN_PROGRESS`` when conformance pack is being deleted in the member account.

      * ``DELETE_SUCCESSFUL`` when conformance pack has been deleted in the member account.

      * ``UPDATE_SUCCESSFUL`` when conformance pack has been updated in the member account.

      * ``UPDATE_IN_PROGRESS`` when conformance pack is being updated in the member account.

      * ``UPDATE_FAILED`` when conformance pack deletion has failed in the member account.

    - **ErrorCode** *(string) --*

      An error code that is returned when conformance pack creation or deletion failed in the
      member account.

    - **ErrorMessage** *(string) --*

      An error message indicating that conformance pack account creation or deletion has failed
      due to an error in the member account.

    - **LastUpdateTime** *(datetime) --*

      The timestamp of the last status update.
    """


_ClientGetOrganizationConformancePackDetailedStatusResponseTypeDef = TypedDict(
    "_ClientGetOrganizationConformancePackDetailedStatusResponseTypeDef",
    {
        "OrganizationConformancePackDetailedStatuses": List[
            ClientGetOrganizationConformancePackDetailedStatusResponseOrganizationConformancePackDetailedStatusesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientGetOrganizationConformancePackDetailedStatusResponseTypeDef(
    _ClientGetOrganizationConformancePackDetailedStatusResponseTypeDef
):
    """
    Type definition for `ClientGetOrganizationConformancePackDetailedStatus` `Response`

    - **OrganizationConformancePackDetailedStatuses** *(list) --*

      A list of ``OrganizationConformancePackDetailedStatus`` objects.

      - *(dict) --*

        Organization conformance pack creation or deletion status in each member account. This
        includes the name of the conformance pack, the status, error code and error message when
        the conformance pack creation or deletion failed.

        - **AccountId** *(string) --*

          The 12-digit account ID of a member account.

        - **ConformancePackName** *(string) --*

          The name of conformance pack deployed in the member account.

        - **Status** *(string) --*

          Indicates deployment status for conformance pack in a member account. When master account
          calls ``PutOrganizationConformancePack`` action for the first time, conformance pack
          status is created in the member account. When master account calls
          ``PutOrganizationConformancePack`` action for the second time, conformance pack status is
          updated in the member account. Conformance pack status is deleted when the master account
          deletes ``OrganizationConformancePack`` and disables service access for
          ``config-multiaccountsetup.amazonaws.com`` .

          AWS Config sets the state of the conformance pack to:

          * ``CREATE_SUCCESSFUL`` when conformance pack has been created in the member account.

          * ``CREATE_IN_PROGRESS`` when conformance pack is being created in the member account.

          * ``CREATE_FAILED`` when conformance pack creation has failed in the member account.

          * ``DELETE_FAILED`` when conformance pack deletion has failed in the member account.

          * ``DELETE_IN_PROGRESS`` when conformance pack is being deleted in the member account.

          * ``DELETE_SUCCESSFUL`` when conformance pack has been deleted in the member account.

          * ``UPDATE_SUCCESSFUL`` when conformance pack has been updated in the member account.

          * ``UPDATE_IN_PROGRESS`` when conformance pack is being updated in the member account.

          * ``UPDATE_FAILED`` when conformance pack deletion has failed in the member account.

        - **ErrorCode** *(string) --*

          An error code that is returned when conformance pack creation or deletion failed in the
          member account.

        - **ErrorMessage** *(string) --*

          An error message indicating that conformance pack account creation or deletion has failed
          due to an error in the member account.

        - **LastUpdateTime** *(datetime) --*

          The timestamp of the last status update.

    - **NextToken** *(string) --*

      The nextToken string returned on a previous page that you use to get the next page of results
      in a paginated response.
    """


_ClientGetResourceConfigHistoryResponseconfigurationItemsrelationshipsTypeDef = TypedDict(
    "_ClientGetResourceConfigHistoryResponseconfigurationItemsrelationshipsTypeDef",
    {
        "resourceType": str,
        "resourceId": str,
        "resourceName": str,
        "relationshipName": str,
    },
    total=False,
)


class ClientGetResourceConfigHistoryResponseconfigurationItemsrelationshipsTypeDef(
    _ClientGetResourceConfigHistoryResponseconfigurationItemsrelationshipsTypeDef
):
    """
    Type definition for `ClientGetResourceConfigHistoryResponseconfigurationItems` `relationships`

    The relationship of the related resource to the main resource.

    - **resourceType** *(string) --*

      The resource type of the related resource.

    - **resourceId** *(string) --*

      The ID of the related resource (for example, ``sg-xxxxxx`` ).

    - **resourceName** *(string) --*

      The custom name of the related resource, if available.

    - **relationshipName** *(string) --*

      The type of relationship with the related resource.
    """


_ClientGetResourceConfigHistoryResponseconfigurationItemsTypeDef = TypedDict(
    "_ClientGetResourceConfigHistoryResponseconfigurationItemsTypeDef",
    {
        "version": str,
        "accountId": str,
        "configurationItemCaptureTime": datetime,
        "configurationItemStatus": str,
        "configurationStateId": str,
        "configurationItemMD5Hash": str,
        "arn": str,
        "resourceType": str,
        "resourceId": str,
        "resourceName": str,
        "awsRegion": str,
        "availabilityZone": str,
        "resourceCreationTime": datetime,
        "tags": Dict[str, str],
        "relatedEvents": List[str],
        "relationships": List[
            ClientGetResourceConfigHistoryResponseconfigurationItemsrelationshipsTypeDef
        ],
        "configuration": str,
        "supplementaryConfiguration": Dict[str, str],
    },
    total=False,
)


class ClientGetResourceConfigHistoryResponseconfigurationItemsTypeDef(
    _ClientGetResourceConfigHistoryResponseconfigurationItemsTypeDef
):
    """
    Type definition for `ClientGetResourceConfigHistoryResponse` `configurationItems`

    A list that contains detailed configurations of a specified resource.

    - **version** *(string) --*

      The version number of the resource configuration.

    - **accountId** *(string) --*

      The 12-digit AWS account ID associated with the resource.

    - **configurationItemCaptureTime** *(datetime) --*

      The time when the configuration recording was initiated.

    - **configurationItemStatus** *(string) --*

      The configuration item status.

    - **configurationStateId** *(string) --*

      An identifier that indicates the ordering of the configuration items of a resource.

    - **configurationItemMD5Hash** *(string) --*

      Unique MD5 hash that represents the configuration item's state.

      You can use MD5 hash to compare the states of two or more configuration items that are
      associated with the same resource.

    - **arn** *(string) --*

      accoun

    - **resourceType** *(string) --*

      The type of AWS resource.

    - **resourceId** *(string) --*

      The ID of the resource (for example, ``sg-xxxxxx`` ).

    - **resourceName** *(string) --*

      The custom name of the resource, if available.

    - **awsRegion** *(string) --*

      The region where the resource resides.

    - **availabilityZone** *(string) --*

      The Availability Zone associated with the resource.

    - **resourceCreationTime** *(datetime) --*

      The time stamp when the resource was created.

    - **tags** *(dict) --*

      A mapping of key value tags associated with the resource.

      - *(string) --*

        - *(string) --*

    - **relatedEvents** *(list) --*

      A list of CloudTrail event IDs.

      A populated field indicates that the current configuration was initiated by the events
      recorded in the CloudTrail log. For more information about CloudTrail, see `What Is AWS
      CloudTrail
      <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/what_is_cloud_trail_top_level.html>`__
      .

      An empty field indicates that the current configuration was not initiated by any event.

      - *(string) --*

    - **relationships** *(list) --*

      A list of related AWS resources.

      - *(dict) --*

        The relationship of the related resource to the main resource.

        - **resourceType** *(string) --*

          The resource type of the related resource.

        - **resourceId** *(string) --*

          The ID of the related resource (for example, ``sg-xxxxxx`` ).

        - **resourceName** *(string) --*

          The custom name of the related resource, if available.

        - **relationshipName** *(string) --*

          The type of relationship with the related resource.

    - **configuration** *(string) --*

      The description of the resource configuration.

    - **supplementaryConfiguration** *(dict) --*

      Configuration attributes that AWS Config returns for certain resource types to supplement
      the information returned for the ``configuration`` parameter.

      - *(string) --*

        - *(string) --*
    """


_ClientGetResourceConfigHistoryResponseTypeDef = TypedDict(
    "_ClientGetResourceConfigHistoryResponseTypeDef",
    {
        "configurationItems": List[
            ClientGetResourceConfigHistoryResponseconfigurationItemsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientGetResourceConfigHistoryResponseTypeDef(
    _ClientGetResourceConfigHistoryResponseTypeDef
):
    """
    Type definition for `ClientGetResourceConfigHistory` `Response`

    The output for the  GetResourceConfigHistory action.

    - **configurationItems** *(list) --*

      A list that contains the configuration history of one or more resources.

      - *(dict) --*

        A list that contains detailed configurations of a specified resource.

        - **version** *(string) --*

          The version number of the resource configuration.

        - **accountId** *(string) --*

          The 12-digit AWS account ID associated with the resource.

        - **configurationItemCaptureTime** *(datetime) --*

          The time when the configuration recording was initiated.

        - **configurationItemStatus** *(string) --*

          The configuration item status.

        - **configurationStateId** *(string) --*

          An identifier that indicates the ordering of the configuration items of a resource.

        - **configurationItemMD5Hash** *(string) --*

          Unique MD5 hash that represents the configuration item's state.

          You can use MD5 hash to compare the states of two or more configuration items that are
          associated with the same resource.

        - **arn** *(string) --*

          accoun

        - **resourceType** *(string) --*

          The type of AWS resource.

        - **resourceId** *(string) --*

          The ID of the resource (for example, ``sg-xxxxxx`` ).

        - **resourceName** *(string) --*

          The custom name of the resource, if available.

        - **awsRegion** *(string) --*

          The region where the resource resides.

        - **availabilityZone** *(string) --*

          The Availability Zone associated with the resource.

        - **resourceCreationTime** *(datetime) --*

          The time stamp when the resource was created.

        - **tags** *(dict) --*

          A mapping of key value tags associated with the resource.

          - *(string) --*

            - *(string) --*

        - **relatedEvents** *(list) --*

          A list of CloudTrail event IDs.

          A populated field indicates that the current configuration was initiated by the events
          recorded in the CloudTrail log. For more information about CloudTrail, see `What Is AWS
          CloudTrail
          <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/what_is_cloud_trail_top_level.html>`__
          .

          An empty field indicates that the current configuration was not initiated by any event.

          - *(string) --*

        - **relationships** *(list) --*

          A list of related AWS resources.

          - *(dict) --*

            The relationship of the related resource to the main resource.

            - **resourceType** *(string) --*

              The resource type of the related resource.

            - **resourceId** *(string) --*

              The ID of the related resource (for example, ``sg-xxxxxx`` ).

            - **resourceName** *(string) --*

              The custom name of the related resource, if available.

            - **relationshipName** *(string) --*

              The type of relationship with the related resource.

        - **configuration** *(string) --*

          The description of the resource configuration.

        - **supplementaryConfiguration** *(dict) --*

          Configuration attributes that AWS Config returns for certain resource types to supplement
          the information returned for the ``configuration`` parameter.

          - *(string) --*

            - *(string) --*

    - **nextToken** *(string) --*

      The string that you use in a subsequent request to get the next page of results in a
      paginated response.
    """


_ClientListAggregateDiscoveredResourcesFiltersTypeDef = TypedDict(
    "_ClientListAggregateDiscoveredResourcesFiltersTypeDef",
    {"AccountId": str, "ResourceId": str, "ResourceName": str, "Region": str},
    total=False,
)


class ClientListAggregateDiscoveredResourcesFiltersTypeDef(
    _ClientListAggregateDiscoveredResourcesFiltersTypeDef
):
    """
    Type definition for `ClientListAggregateDiscoveredResources` `Filters`

    Filters the results based on the ``ResourceFilters`` object.

    - **AccountId** *(string) --*

      The 12-digit source account ID.

    - **ResourceId** *(string) --*

      The ID of the resource.

    - **ResourceName** *(string) --*

      The name of the resource.

    - **Region** *(string) --*

      The source region.
    """


_ClientListAggregateDiscoveredResourcesResponseResourceIdentifiersTypeDef = TypedDict(
    "_ClientListAggregateDiscoveredResourcesResponseResourceIdentifiersTypeDef",
    {
        "SourceAccountId": str,
        "SourceRegion": str,
        "ResourceId": str,
        "ResourceType": str,
        "ResourceName": str,
    },
    total=False,
)


class ClientListAggregateDiscoveredResourcesResponseResourceIdentifiersTypeDef(
    _ClientListAggregateDiscoveredResourcesResponseResourceIdentifiersTypeDef
):
    """
    Type definition for `ClientListAggregateDiscoveredResourcesResponse` `ResourceIdentifiers`

    The details that identify a resource that is collected by AWS Config aggregator, including
    the resource type, ID, (if available) the custom resource name, the source account, and
    source region.

    - **SourceAccountId** *(string) --*

      The 12-digit account ID of the source account.

    - **SourceRegion** *(string) --*

      The source region where data is aggregated.

    - **ResourceId** *(string) --*

      The ID of the AWS resource.

    - **ResourceType** *(string) --*

      The type of the AWS resource.

    - **ResourceName** *(string) --*

      The name of the AWS resource.
    """


_ClientListAggregateDiscoveredResourcesResponseTypeDef = TypedDict(
    "_ClientListAggregateDiscoveredResourcesResponseTypeDef",
    {
        "ResourceIdentifiers": List[
            ClientListAggregateDiscoveredResourcesResponseResourceIdentifiersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListAggregateDiscoveredResourcesResponseTypeDef(
    _ClientListAggregateDiscoveredResourcesResponseTypeDef
):
    """
    Type definition for `ClientListAggregateDiscoveredResources` `Response`

    - **ResourceIdentifiers** *(list) --*

      Returns a list of ``ResourceIdentifiers`` objects.

      - *(dict) --*

        The details that identify a resource that is collected by AWS Config aggregator, including
        the resource type, ID, (if available) the custom resource name, the source account, and
        source region.

        - **SourceAccountId** *(string) --*

          The 12-digit account ID of the source account.

        - **SourceRegion** *(string) --*

          The source region where data is aggregated.

        - **ResourceId** *(string) --*

          The ID of the AWS resource.

        - **ResourceType** *(string) --*

          The type of the AWS resource.

        - **ResourceName** *(string) --*

          The name of the AWS resource.

    - **NextToken** *(string) --*

      The ``nextToken`` string returned on a previous page that you use to get the next page of
      results in a paginated response.
    """


_ClientListDiscoveredResourcesResponseresourceIdentifiersTypeDef = TypedDict(
    "_ClientListDiscoveredResourcesResponseresourceIdentifiersTypeDef",
    {
        "resourceType": str,
        "resourceId": str,
        "resourceName": str,
        "resourceDeletionTime": datetime,
    },
    total=False,
)


class ClientListDiscoveredResourcesResponseresourceIdentifiersTypeDef(
    _ClientListDiscoveredResourcesResponseresourceIdentifiersTypeDef
):
    """
    Type definition for `ClientListDiscoveredResourcesResponse` `resourceIdentifiers`

    The details that identify a resource that is discovered by AWS Config, including the
    resource type, ID, and (if available) the custom resource name.

    - **resourceType** *(string) --*

      The type of resource.

    - **resourceId** *(string) --*

      The ID of the resource (for example, ``sg-xxxxxx`` ).

    - **resourceName** *(string) --*

      The custom name of the resource (if available).

    - **resourceDeletionTime** *(datetime) --*

      The time that the resource was deleted.
    """


_ClientListDiscoveredResourcesResponseTypeDef = TypedDict(
    "_ClientListDiscoveredResourcesResponseTypeDef",
    {
        "resourceIdentifiers": List[
            ClientListDiscoveredResourcesResponseresourceIdentifiersTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListDiscoveredResourcesResponseTypeDef(
    _ClientListDiscoveredResourcesResponseTypeDef
):
    """
    Type definition for `ClientListDiscoveredResources` `Response`

    - **resourceIdentifiers** *(list) --*

      The details that identify a resource that is discovered by AWS Config, including the resource
      type, ID, and (if available) the custom resource name.

      - *(dict) --*

        The details that identify a resource that is discovered by AWS Config, including the
        resource type, ID, and (if available) the custom resource name.

        - **resourceType** *(string) --*

          The type of resource.

        - **resourceId** *(string) --*

          The ID of the resource (for example, ``sg-xxxxxx`` ).

        - **resourceName** *(string) --*

          The custom name of the resource (if available).

        - **resourceDeletionTime** *(datetime) --*

          The time that the resource was deleted.

    - **nextToken** *(string) --*

      The string that you use in a subsequent request to get the next page of results in a
      paginated response.
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

    The tags for the resource. The metadata that you apply to a resource to help you categorize
    and organize them. Each tag consists of a key and an optional value, both of which you
    define. Tag keys can have a maximum character length of 128 characters, and tag values can
    have a maximum length of 256 characters.

    - **Key** *(string) --*

      One part of a key-value pair that make up a tag. A key is a general label that acts like
      a category for more specific tag values.

    - **Value** *(string) --*

      The optional part of a key-value pair that make up a tag. A value acts as a descriptor
      within a tag category (key).
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

      The tags for the resource.

      - *(dict) --*

        The tags for the resource. The metadata that you apply to a resource to help you categorize
        and organize them. Each tag consists of a key and an optional value, both of which you
        define. Tag keys can have a maximum character length of 128 characters, and tag values can
        have a maximum length of 256 characters.

        - **Key** *(string) --*

          One part of a key-value pair that make up a tag. A key is a general label that acts like
          a category for more specific tag values.

        - **Value** *(string) --*

          The optional part of a key-value pair that make up a tag. A value acts as a descriptor
          within a tag category (key).

    - **NextToken** *(string) --*

      The ``nextToken`` string returned on a previous page that you use to get the next page of
      results in a paginated response.
    """


_ClientPutAggregationAuthorizationResponseAggregationAuthorizationTypeDef = TypedDict(
    "_ClientPutAggregationAuthorizationResponseAggregationAuthorizationTypeDef",
    {
        "AggregationAuthorizationArn": str,
        "AuthorizedAccountId": str,
        "AuthorizedAwsRegion": str,
        "CreationTime": datetime,
    },
    total=False,
)


class ClientPutAggregationAuthorizationResponseAggregationAuthorizationTypeDef(
    _ClientPutAggregationAuthorizationResponseAggregationAuthorizationTypeDef
):
    """
    Type definition for `ClientPutAggregationAuthorizationResponse` `AggregationAuthorization`

    Returns an AggregationAuthorization object.

    - **AggregationAuthorizationArn** *(string) --*

      The Amazon Resource Name (ARN) of the aggregation object.

    - **AuthorizedAccountId** *(string) --*

      The 12-digit account ID of the account authorized to aggregate data.

    - **AuthorizedAwsRegion** *(string) --*

      The region authorized to collect aggregated data.

    - **CreationTime** *(datetime) --*

      The time stamp when the aggregation authorization was created.
    """


_ClientPutAggregationAuthorizationResponseTypeDef = TypedDict(
    "_ClientPutAggregationAuthorizationResponseTypeDef",
    {
        "AggregationAuthorization": ClientPutAggregationAuthorizationResponseAggregationAuthorizationTypeDef
    },
    total=False,
)


class ClientPutAggregationAuthorizationResponseTypeDef(
    _ClientPutAggregationAuthorizationResponseTypeDef
):
    """
    Type definition for `ClientPutAggregationAuthorization` `Response`

    - **AggregationAuthorization** *(dict) --*

      Returns an AggregationAuthorization object.

      - **AggregationAuthorizationArn** *(string) --*

        The Amazon Resource Name (ARN) of the aggregation object.

      - **AuthorizedAccountId** *(string) --*

        The 12-digit account ID of the account authorized to aggregate data.

      - **AuthorizedAwsRegion** *(string) --*

        The region authorized to collect aggregated data.

      - **CreationTime** *(datetime) --*

        The time stamp when the aggregation authorization was created.
    """


_ClientPutAggregationAuthorizationTagsTypeDef = TypedDict(
    "_ClientPutAggregationAuthorizationTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientPutAggregationAuthorizationTagsTypeDef(
    _ClientPutAggregationAuthorizationTagsTypeDef
):
    """
    Type definition for `ClientPutAggregationAuthorization` `Tags`

    The tags for the resource. The metadata that you apply to a resource to help you categorize and
    organize them. Each tag consists of a key and an optional value, both of which you define. Tag
    keys can have a maximum character length of 128 characters, and tag values can have a maximum
    length of 256 characters.

    - **Key** *(string) --*

      One part of a key-value pair that make up a tag. A key is a general label that acts like a
      category for more specific tag values.

    - **Value** *(string) --*

      The optional part of a key-value pair that make up a tag. A value acts as a descriptor within
      a tag category (key).
    """


_ClientPutConfigRuleConfigRuleScopeTypeDef = TypedDict(
    "_ClientPutConfigRuleConfigRuleScopeTypeDef",
    {
        "ComplianceResourceTypes": List[str],
        "TagKey": str,
        "TagValue": str,
        "ComplianceResourceId": str,
    },
    total=False,
)


class ClientPutConfigRuleConfigRuleScopeTypeDef(
    _ClientPutConfigRuleConfigRuleScopeTypeDef
):
    """
    Type definition for `ClientPutConfigRuleConfigRule` `Scope`

    Defines which resources can trigger an evaluation for the rule. The scope can include one or
    more resource types, a combination of one resource type and one resource ID, or a combination
    of a tag key and value. Specify a scope to constrain the resources that can trigger an
    evaluation for the rule. If you do not specify a scope, evaluations are triggered when any
    resource in the recording group changes.

    - **ComplianceResourceTypes** *(list) --*

      The resource types of only those AWS resources that you want to trigger an evaluation for the
      rule. You can only specify one type if you also specify a resource ID for
      ``ComplianceResourceId`` .

      - *(string) --*

    - **TagKey** *(string) --*

      The tag key that is applied to only those AWS resources that you want to trigger an
      evaluation for the rule.

    - **TagValue** *(string) --*

      The tag value applied to only those AWS resources that you want to trigger an evaluation for
      the rule. If you specify a value for ``TagValue`` , you must also specify a value for
      ``TagKey`` .

    - **ComplianceResourceId** *(string) --*

      The ID of the only AWS resource that you want to trigger an evaluation for the rule. If you
      specify a resource ID, you must specify one resource type for ``ComplianceResourceTypes`` .
    """


_ClientPutConfigRuleConfigRuleSourceSourceDetailsTypeDef = TypedDict(
    "_ClientPutConfigRuleConfigRuleSourceSourceDetailsTypeDef",
    {"EventSource": str, "MessageType": str, "MaximumExecutionFrequency": str},
    total=False,
)


class ClientPutConfigRuleConfigRuleSourceSourceDetailsTypeDef(
    _ClientPutConfigRuleConfigRuleSourceSourceDetailsTypeDef
):
    """
    Type definition for `ClientPutConfigRuleConfigRuleSource` `SourceDetails`

    Provides the source and the message types that trigger AWS Config to evaluate your AWS
    resources against a rule. It also provides the frequency with which you want AWS Config to
    run evaluations for the rule if the trigger type is periodic. You can specify the parameter
    values for ``SourceDetail`` only for custom rules.

    - **EventSource** *(string) --*

      The source of the event, such as an AWS service, that triggers AWS Config to evaluate
      your AWS resources.

    - **MessageType** *(string) --*

      The type of notification that triggers AWS Config to run an evaluation for a rule. You
      can specify the following notification types:

      * ``ConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config
      delivers a configuration item as a result of a resource change.

      * ``OversizedConfigurationItemChangeNotification`` - Triggers an evaluation when AWS
      Config delivers an oversized configuration item. AWS Config may generate this
      notification type when a resource changes and the notification exceeds the maximum size
      allowed by Amazon SNS.

      * ``ScheduledNotification`` - Triggers a periodic evaluation at the frequency specified
      for ``MaximumExecutionFrequency`` .

      * ``ConfigurationSnapshotDeliveryCompleted`` - Triggers a periodic evaluation when AWS
      Config delivers a configuration snapshot.

      If you want your custom rule to be triggered by configuration changes, specify two
      SourceDetail objects, one for ``ConfigurationItemChangeNotification`` and one for
      ``OversizedConfigurationItemChangeNotification`` .

    - **MaximumExecutionFrequency** *(string) --*

      The frequency at which you want AWS Config to run evaluations for a custom rule with a
      periodic trigger. If you specify a value for ``MaximumExecutionFrequency`` , then
      ``MessageType`` must use the ``ScheduledNotification`` value.

      .. note::

        By default, rules with a periodic trigger are evaluated every 24 hours. To change the
        frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.

        Based on the valid value you choose, AWS Config runs evaluations once for each valid
        value. For example, if you choose ``Three_Hours`` , AWS Config runs evaluations once
        every three hours. In this case, ``Three_Hours`` is the frequency of this rule.
    """


_RequiredClientPutConfigRuleConfigRuleSourceTypeDef = TypedDict(
    "_RequiredClientPutConfigRuleConfigRuleSourceTypeDef",
    {"Owner": str, "SourceIdentifier": str},
)
_OptionalClientPutConfigRuleConfigRuleSourceTypeDef = TypedDict(
    "_OptionalClientPutConfigRuleConfigRuleSourceTypeDef",
    {"SourceDetails": List[ClientPutConfigRuleConfigRuleSourceSourceDetailsTypeDef]},
    total=False,
)


class ClientPutConfigRuleConfigRuleSourceTypeDef(
    _RequiredClientPutConfigRuleConfigRuleSourceTypeDef,
    _OptionalClientPutConfigRuleConfigRuleSourceTypeDef,
):
    """
    Type definition for `ClientPutConfigRuleConfigRule` `Source`

    Provides the rule owner (AWS or customer), the rule identifier, and the notifications that
    cause the function to evaluate your AWS resources.

    - **Owner** *(string) --* **[REQUIRED]**

      Indicates whether AWS or the customer owns and manages the AWS Config rule.

    - **SourceIdentifier** *(string) --* **[REQUIRED]**

      For AWS Config managed rules, a predefined identifier from a list. For example,
      ``IAM_PASSWORD_POLICY`` is a managed rule. To reference a managed rule, see `Using AWS
      Managed Config Rules
      <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html>`__
      .

      For custom rules, the identifier is the Amazon Resource Name (ARN) of the rule's AWS Lambda
      function, such as ``arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name`` .

    - **SourceDetails** *(list) --*

      Provides the source and type of the event that causes AWS Config to evaluate your AWS
      resources.

      - *(dict) --*

        Provides the source and the message types that trigger AWS Config to evaluate your AWS
        resources against a rule. It also provides the frequency with which you want AWS Config to
        run evaluations for the rule if the trigger type is periodic. You can specify the parameter
        values for ``SourceDetail`` only for custom rules.

        - **EventSource** *(string) --*

          The source of the event, such as an AWS service, that triggers AWS Config to evaluate
          your AWS resources.

        - **MessageType** *(string) --*

          The type of notification that triggers AWS Config to run an evaluation for a rule. You
          can specify the following notification types:

          * ``ConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config
          delivers a configuration item as a result of a resource change.

          * ``OversizedConfigurationItemChangeNotification`` - Triggers an evaluation when AWS
          Config delivers an oversized configuration item. AWS Config may generate this
          notification type when a resource changes and the notification exceeds the maximum size
          allowed by Amazon SNS.

          * ``ScheduledNotification`` - Triggers a periodic evaluation at the frequency specified
          for ``MaximumExecutionFrequency`` .

          * ``ConfigurationSnapshotDeliveryCompleted`` - Triggers a periodic evaluation when AWS
          Config delivers a configuration snapshot.

          If you want your custom rule to be triggered by configuration changes, specify two
          SourceDetail objects, one for ``ConfigurationItemChangeNotification`` and one for
          ``OversizedConfigurationItemChangeNotification`` .

        - **MaximumExecutionFrequency** *(string) --*

          The frequency at which you want AWS Config to run evaluations for a custom rule with a
          periodic trigger. If you specify a value for ``MaximumExecutionFrequency`` , then
          ``MessageType`` must use the ``ScheduledNotification`` value.

          .. note::

            By default, rules with a periodic trigger are evaluated every 24 hours. To change the
            frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.

            Based on the valid value you choose, AWS Config runs evaluations once for each valid
            value. For example, if you choose ``Three_Hours`` , AWS Config runs evaluations once
            every three hours. In this case, ``Three_Hours`` is the frequency of this rule.
    """


_RequiredClientPutConfigRuleConfigRuleTypeDef = TypedDict(
    "_RequiredClientPutConfigRuleConfigRuleTypeDef",
    {"Source": ClientPutConfigRuleConfigRuleSourceTypeDef},
)
_OptionalClientPutConfigRuleConfigRuleTypeDef = TypedDict(
    "_OptionalClientPutConfigRuleConfigRuleTypeDef",
    {
        "ConfigRuleName": str,
        "ConfigRuleArn": str,
        "ConfigRuleId": str,
        "Description": str,
        "Scope": ClientPutConfigRuleConfigRuleScopeTypeDef,
        "InputParameters": str,
        "MaximumExecutionFrequency": str,
        "ConfigRuleState": str,
        "CreatedBy": str,
    },
    total=False,
)


class ClientPutConfigRuleConfigRuleTypeDef(
    _RequiredClientPutConfigRuleConfigRuleTypeDef,
    _OptionalClientPutConfigRuleConfigRuleTypeDef,
):
    """
    Type definition for `ClientPutConfigRule` `ConfigRule`

    The rule that you want to add to your account.

    - **ConfigRuleName** *(string) --*

      The name that you assign to the AWS Config rule. The name is required if you are adding a new
      rule.

    - **ConfigRuleArn** *(string) --*

      The Amazon Resource Name (ARN) of the AWS Config rule.

    - **ConfigRuleId** *(string) --*

      The ID of the AWS Config rule.

    - **Description** *(string) --*

      The description that you provide for the AWS Config rule.

    - **Scope** *(dict) --*

      Defines which resources can trigger an evaluation for the rule. The scope can include one or
      more resource types, a combination of one resource type and one resource ID, or a combination
      of a tag key and value. Specify a scope to constrain the resources that can trigger an
      evaluation for the rule. If you do not specify a scope, evaluations are triggered when any
      resource in the recording group changes.

      - **ComplianceResourceTypes** *(list) --*

        The resource types of only those AWS resources that you want to trigger an evaluation for the
        rule. You can only specify one type if you also specify a resource ID for
        ``ComplianceResourceId`` .

        - *(string) --*

      - **TagKey** *(string) --*

        The tag key that is applied to only those AWS resources that you want to trigger an
        evaluation for the rule.

      - **TagValue** *(string) --*

        The tag value applied to only those AWS resources that you want to trigger an evaluation for
        the rule. If you specify a value for ``TagValue`` , you must also specify a value for
        ``TagKey`` .

      - **ComplianceResourceId** *(string) --*

        The ID of the only AWS resource that you want to trigger an evaluation for the rule. If you
        specify a resource ID, you must specify one resource type for ``ComplianceResourceTypes`` .

    - **Source** *(dict) --* **[REQUIRED]**

      Provides the rule owner (AWS or customer), the rule identifier, and the notifications that
      cause the function to evaluate your AWS resources.

      - **Owner** *(string) --* **[REQUIRED]**

        Indicates whether AWS or the customer owns and manages the AWS Config rule.

      - **SourceIdentifier** *(string) --* **[REQUIRED]**

        For AWS Config managed rules, a predefined identifier from a list. For example,
        ``IAM_PASSWORD_POLICY`` is a managed rule. To reference a managed rule, see `Using AWS
        Managed Config Rules
        <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html>`__
        .

        For custom rules, the identifier is the Amazon Resource Name (ARN) of the rule's AWS Lambda
        function, such as ``arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name`` .

      - **SourceDetails** *(list) --*

        Provides the source and type of the event that causes AWS Config to evaluate your AWS
        resources.

        - *(dict) --*

          Provides the source and the message types that trigger AWS Config to evaluate your AWS
          resources against a rule. It also provides the frequency with which you want AWS Config to
          run evaluations for the rule if the trigger type is periodic. You can specify the parameter
          values for ``SourceDetail`` only for custom rules.

          - **EventSource** *(string) --*

            The source of the event, such as an AWS service, that triggers AWS Config to evaluate
            your AWS resources.

          - **MessageType** *(string) --*

            The type of notification that triggers AWS Config to run an evaluation for a rule. You
            can specify the following notification types:

            * ``ConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config
            delivers a configuration item as a result of a resource change.

            * ``OversizedConfigurationItemChangeNotification`` - Triggers an evaluation when AWS
            Config delivers an oversized configuration item. AWS Config may generate this
            notification type when a resource changes and the notification exceeds the maximum size
            allowed by Amazon SNS.

            * ``ScheduledNotification`` - Triggers a periodic evaluation at the frequency specified
            for ``MaximumExecutionFrequency`` .

            * ``ConfigurationSnapshotDeliveryCompleted`` - Triggers a periodic evaluation when AWS
            Config delivers a configuration snapshot.

            If you want your custom rule to be triggered by configuration changes, specify two
            SourceDetail objects, one for ``ConfigurationItemChangeNotification`` and one for
            ``OversizedConfigurationItemChangeNotification`` .

          - **MaximumExecutionFrequency** *(string) --*

            The frequency at which you want AWS Config to run evaluations for a custom rule with a
            periodic trigger. If you specify a value for ``MaximumExecutionFrequency`` , then
            ``MessageType`` must use the ``ScheduledNotification`` value.

            .. note::

              By default, rules with a periodic trigger are evaluated every 24 hours. To change the
              frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.

              Based on the valid value you choose, AWS Config runs evaluations once for each valid
              value. For example, if you choose ``Three_Hours`` , AWS Config runs evaluations once
              every three hours. In this case, ``Three_Hours`` is the frequency of this rule.

    - **InputParameters** *(string) --*

      A string, in JSON format, that is passed to the AWS Config rule Lambda function.

    - **MaximumExecutionFrequency** *(string) --*

      The maximum frequency with which AWS Config runs evaluations for a rule. You can specify a
      value for ``MaximumExecutionFrequency`` when:

      * You are using an AWS managed rule that is triggered at a periodic frequency.

      * Your custom rule is triggered when AWS Config delivers the configuration snapshot. For more
      information, see  ConfigSnapshotDeliveryProperties .

      .. note::

        By default, rules with a periodic trigger are evaluated every 24 hours. To change the
        frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.

    - **ConfigRuleState** *(string) --*

      Indicates whether the AWS Config rule is active or is currently being deleted by AWS Config. It
      can also indicate the evaluation status for the AWS Config rule.

      AWS Config sets the state of the rule to ``EVALUATING`` temporarily after you use the
      ``StartConfigRulesEvaluation`` request to evaluate your resources against the AWS Config rule.

      AWS Config sets the state of the rule to ``DELETING_RESULTS`` temporarily after you use the
      ``DeleteEvaluationResults`` request to delete the current evaluation results for the AWS Config
      rule.

      AWS Config temporarily sets the state of a rule to ``DELETING`` after you use the
      ``DeleteConfigRule`` request to delete the rule. After AWS Config deletes the rule, the rule
      and all of its evaluations are erased and are no longer available.

    - **CreatedBy** *(string) --*

      Service principal name of the service that created the rule.

      .. note::

        The field is populated only if the service linked rule is created by a service. The field is
        empty if you create your own rule.
    """


_ClientPutConfigRuleTagsTypeDef = TypedDict(
    "_ClientPutConfigRuleTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientPutConfigRuleTagsTypeDef(_ClientPutConfigRuleTagsTypeDef):
    """
    Type definition for `ClientPutConfigRule` `Tags`

    The tags for the resource. The metadata that you apply to a resource to help you categorize and
    organize them. Each tag consists of a key and an optional value, both of which you define. Tag
    keys can have a maximum character length of 128 characters, and tag values can have a maximum
    length of 256 characters.

    - **Key** *(string) --*

      One part of a key-value pair that make up a tag. A key is a general label that acts like a
      category for more specific tag values.

    - **Value** *(string) --*

      The optional part of a key-value pair that make up a tag. A value acts as a descriptor within
      a tag category (key).
    """


_RequiredClientPutConfigurationAggregatorAccountAggregationSourcesTypeDef = TypedDict(
    "_RequiredClientPutConfigurationAggregatorAccountAggregationSourcesTypeDef",
    {"AccountIds": List[str]},
)
_OptionalClientPutConfigurationAggregatorAccountAggregationSourcesTypeDef = TypedDict(
    "_OptionalClientPutConfigurationAggregatorAccountAggregationSourcesTypeDef",
    {"AllAwsRegions": bool, "AwsRegions": List[str]},
    total=False,
)


class ClientPutConfigurationAggregatorAccountAggregationSourcesTypeDef(
    _RequiredClientPutConfigurationAggregatorAccountAggregationSourcesTypeDef,
    _OptionalClientPutConfigurationAggregatorAccountAggregationSourcesTypeDef,
):
    """
    Type definition for `ClientPutConfigurationAggregator` `AccountAggregationSources`

    A collection of accounts and regions.

    - **AccountIds** *(list) --* **[REQUIRED]**

      The 12-digit account ID of the account being aggregated.

      - *(string) --*

    - **AllAwsRegions** *(boolean) --*

      If true, aggregate existing AWS Config regions and future regions.

    - **AwsRegions** *(list) --*

      The source regions being aggregated.

      - *(string) --*
    """


_RequiredClientPutConfigurationAggregatorOrganizationAggregationSourceTypeDef = TypedDict(
    "_RequiredClientPutConfigurationAggregatorOrganizationAggregationSourceTypeDef",
    {"RoleArn": str},
)
_OptionalClientPutConfigurationAggregatorOrganizationAggregationSourceTypeDef = TypedDict(
    "_OptionalClientPutConfigurationAggregatorOrganizationAggregationSourceTypeDef",
    {"AwsRegions": List[str], "AllAwsRegions": bool},
    total=False,
)


class ClientPutConfigurationAggregatorOrganizationAggregationSourceTypeDef(
    _RequiredClientPutConfigurationAggregatorOrganizationAggregationSourceTypeDef,
    _OptionalClientPutConfigurationAggregatorOrganizationAggregationSourceTypeDef,
):
    """
    Type definition for `ClientPutConfigurationAggregator` `OrganizationAggregationSource`

    An OrganizationAggregationSource object.

    - **RoleArn** *(string) --* **[REQUIRED]**

      ARN of the IAM role used to retrieve AWS Organization details associated with the aggregator
      account.

    - **AwsRegions** *(list) --*

      The source regions being aggregated.

      - *(string) --*

    - **AllAwsRegions** *(boolean) --*

      If true, aggregate existing AWS Config regions and future regions.
    """


_ClientPutConfigurationAggregatorResponseConfigurationAggregatorAccountAggregationSourcesTypeDef = TypedDict(
    "_ClientPutConfigurationAggregatorResponseConfigurationAggregatorAccountAggregationSourcesTypeDef",
    {"AccountIds": List[str], "AllAwsRegions": bool, "AwsRegions": List[str]},
    total=False,
)


class ClientPutConfigurationAggregatorResponseConfigurationAggregatorAccountAggregationSourcesTypeDef(
    _ClientPutConfigurationAggregatorResponseConfigurationAggregatorAccountAggregationSourcesTypeDef
):
    """
    Type definition for `ClientPutConfigurationAggregatorResponseConfigurationAggregator` `AccountAggregationSources`

    A collection of accounts and regions.

    - **AccountIds** *(list) --*

      The 12-digit account ID of the account being aggregated.

      - *(string) --*

    - **AllAwsRegions** *(boolean) --*

      If true, aggregate existing AWS Config regions and future regions.

    - **AwsRegions** *(list) --*

      The source regions being aggregated.

      - *(string) --*
    """


_ClientPutConfigurationAggregatorResponseConfigurationAggregatorOrganizationAggregationSourceTypeDef = TypedDict(
    "_ClientPutConfigurationAggregatorResponseConfigurationAggregatorOrganizationAggregationSourceTypeDef",
    {"RoleArn": str, "AwsRegions": List[str], "AllAwsRegions": bool},
    total=False,
)


class ClientPutConfigurationAggregatorResponseConfigurationAggregatorOrganizationAggregationSourceTypeDef(
    _ClientPutConfigurationAggregatorResponseConfigurationAggregatorOrganizationAggregationSourceTypeDef
):
    """
    Type definition for `ClientPutConfigurationAggregatorResponseConfigurationAggregator` `OrganizationAggregationSource`

    Provides an organization and list of regions to be aggregated.

    - **RoleArn** *(string) --*

      ARN of the IAM role used to retrieve AWS Organization details associated with the
      aggregator account.

    - **AwsRegions** *(list) --*

      The source regions being aggregated.

      - *(string) --*

    - **AllAwsRegions** *(boolean) --*

      If true, aggregate existing AWS Config regions and future regions.
    """


_ClientPutConfigurationAggregatorResponseConfigurationAggregatorTypeDef = TypedDict(
    "_ClientPutConfigurationAggregatorResponseConfigurationAggregatorTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ConfigurationAggregatorArn": str,
        "AccountAggregationSources": List[
            ClientPutConfigurationAggregatorResponseConfigurationAggregatorAccountAggregationSourcesTypeDef
        ],
        "OrganizationAggregationSource": ClientPutConfigurationAggregatorResponseConfigurationAggregatorOrganizationAggregationSourceTypeDef,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)


class ClientPutConfigurationAggregatorResponseConfigurationAggregatorTypeDef(
    _ClientPutConfigurationAggregatorResponseConfigurationAggregatorTypeDef
):
    """
    Type definition for `ClientPutConfigurationAggregatorResponse` `ConfigurationAggregator`

    Returns a ConfigurationAggregator object.

    - **ConfigurationAggregatorName** *(string) --*

      The name of the aggregator.

    - **ConfigurationAggregatorArn** *(string) --*

      The Amazon Resource Name (ARN) of the aggregator.

    - **AccountAggregationSources** *(list) --*

      Provides a list of source accounts and regions to be aggregated.

      - *(dict) --*

        A collection of accounts and regions.

        - **AccountIds** *(list) --*

          The 12-digit account ID of the account being aggregated.

          - *(string) --*

        - **AllAwsRegions** *(boolean) --*

          If true, aggregate existing AWS Config regions and future regions.

        - **AwsRegions** *(list) --*

          The source regions being aggregated.

          - *(string) --*

    - **OrganizationAggregationSource** *(dict) --*

      Provides an organization and list of regions to be aggregated.

      - **RoleArn** *(string) --*

        ARN of the IAM role used to retrieve AWS Organization details associated with the
        aggregator account.

      - **AwsRegions** *(list) --*

        The source regions being aggregated.

        - *(string) --*

      - **AllAwsRegions** *(boolean) --*

        If true, aggregate existing AWS Config regions and future regions.

    - **CreationTime** *(datetime) --*

      The time stamp when the configuration aggregator was created.

    - **LastUpdatedTime** *(datetime) --*

      The time of the last update.
    """


_ClientPutConfigurationAggregatorResponseTypeDef = TypedDict(
    "_ClientPutConfigurationAggregatorResponseTypeDef",
    {
        "ConfigurationAggregator": ClientPutConfigurationAggregatorResponseConfigurationAggregatorTypeDef
    },
    total=False,
)


class ClientPutConfigurationAggregatorResponseTypeDef(
    _ClientPutConfigurationAggregatorResponseTypeDef
):
    """
    Type definition for `ClientPutConfigurationAggregator` `Response`

    - **ConfigurationAggregator** *(dict) --*

      Returns a ConfigurationAggregator object.

      - **ConfigurationAggregatorName** *(string) --*

        The name of the aggregator.

      - **ConfigurationAggregatorArn** *(string) --*

        The Amazon Resource Name (ARN) of the aggregator.

      - **AccountAggregationSources** *(list) --*

        Provides a list of source accounts and regions to be aggregated.

        - *(dict) --*

          A collection of accounts and regions.

          - **AccountIds** *(list) --*

            The 12-digit account ID of the account being aggregated.

            - *(string) --*

          - **AllAwsRegions** *(boolean) --*

            If true, aggregate existing AWS Config regions and future regions.

          - **AwsRegions** *(list) --*

            The source regions being aggregated.

            - *(string) --*

      - **OrganizationAggregationSource** *(dict) --*

        Provides an organization and list of regions to be aggregated.

        - **RoleArn** *(string) --*

          ARN of the IAM role used to retrieve AWS Organization details associated with the
          aggregator account.

        - **AwsRegions** *(list) --*

          The source regions being aggregated.

          - *(string) --*

        - **AllAwsRegions** *(boolean) --*

          If true, aggregate existing AWS Config regions and future regions.

      - **CreationTime** *(datetime) --*

        The time stamp when the configuration aggregator was created.

      - **LastUpdatedTime** *(datetime) --*

        The time of the last update.
    """


_ClientPutConfigurationAggregatorTagsTypeDef = TypedDict(
    "_ClientPutConfigurationAggregatorTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientPutConfigurationAggregatorTagsTypeDef(
    _ClientPutConfigurationAggregatorTagsTypeDef
):
    """
    Type definition for `ClientPutConfigurationAggregator` `Tags`

    The tags for the resource. The metadata that you apply to a resource to help you categorize and
    organize them. Each tag consists of a key and an optional value, both of which you define. Tag
    keys can have a maximum character length of 128 characters, and tag values can have a maximum
    length of 256 characters.

    - **Key** *(string) --*

      One part of a key-value pair that make up a tag. A key is a general label that acts like a
      category for more specific tag values.

    - **Value** *(string) --*

      The optional part of a key-value pair that make up a tag. A value acts as a descriptor within
      a tag category (key).
    """


_ClientPutConfigurationRecorderConfigurationRecorderrecordingGroupTypeDef = TypedDict(
    "_ClientPutConfigurationRecorderConfigurationRecorderrecordingGroupTypeDef",
    {
        "allSupported": bool,
        "includeGlobalResourceTypes": bool,
        "resourceTypes": List[str],
    },
    total=False,
)


class ClientPutConfigurationRecorderConfigurationRecorderrecordingGroupTypeDef(
    _ClientPutConfigurationRecorderConfigurationRecorderrecordingGroupTypeDef
):
    """
    Type definition for `ClientPutConfigurationRecorderConfigurationRecorder` `recordingGroup`

    Specifies the types of AWS resources for which AWS Config records configuration changes.

    - **allSupported** *(boolean) --*

      Specifies whether AWS Config records configuration changes for every supported type of
      regional resource.

      If you set this option to ``true`` , when AWS Config adds support for a new type of regional
      resource, it starts recording resources of that type automatically.

      If you set this option to ``true`` , you cannot enumerate a list of ``resourceTypes`` .

    - **includeGlobalResourceTypes** *(boolean) --*

      Specifies whether AWS Config includes all supported types of global resources (for example,
      IAM resources) with the resources that it records.

      Before you can set this option to ``true`` , you must set the ``allSupported`` option to
      ``true`` .

      If you set this option to ``true`` , when AWS Config adds support for a new type of global
      resource, it starts recording resources of that type automatically.

      The configuration details for any global resource are the same in all regions. To prevent
      duplicate configuration items, you should consider customizing AWS Config in only one region
      to record global resources.

    - **resourceTypes** *(list) --*

      A comma-separated list that specifies the types of AWS resources for which AWS Config records
      configuration changes (for example, ``AWS::EC2::Instance`` or ``AWS::CloudTrail::Trail`` ).

      Before you can set this option to ``true`` , you must set the ``allSupported`` option to
      ``false`` .

      If you set this option to ``true`` , when AWS Config adds support for a new type of resource,
      it will not record resources of that type unless you manually add that type to your recording
      group.

      For a list of valid ``resourceTypes`` values, see the **resourceType Value** column in
      `Supported AWS Resource Types
      <https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#supported-resources>`__
      .

      - *(string) --*
    """


_ClientPutConfigurationRecorderConfigurationRecorderTypeDef = TypedDict(
    "_ClientPutConfigurationRecorderConfigurationRecorderTypeDef",
    {
        "name": str,
        "roleARN": str,
        "recordingGroup": ClientPutConfigurationRecorderConfigurationRecorderrecordingGroupTypeDef,
    },
    total=False,
)


class ClientPutConfigurationRecorderConfigurationRecorderTypeDef(
    _ClientPutConfigurationRecorderConfigurationRecorderTypeDef
):
    """
    Type definition for `ClientPutConfigurationRecorder` `ConfigurationRecorder`

    The configuration recorder object that records each configuration change made to the resources.

    - **name** *(string) --*

      The name of the recorder. By default, AWS Config automatically assigns the name "default" when
      creating the configuration recorder. You cannot change the assigned name.

    - **roleARN** *(string) --*

      Amazon Resource Name (ARN) of the IAM role used to describe the AWS resources associated with
      the account.

    - **recordingGroup** *(dict) --*

      Specifies the types of AWS resources for which AWS Config records configuration changes.

      - **allSupported** *(boolean) --*

        Specifies whether AWS Config records configuration changes for every supported type of
        regional resource.

        If you set this option to ``true`` , when AWS Config adds support for a new type of regional
        resource, it starts recording resources of that type automatically.

        If you set this option to ``true`` , you cannot enumerate a list of ``resourceTypes`` .

      - **includeGlobalResourceTypes** *(boolean) --*

        Specifies whether AWS Config includes all supported types of global resources (for example,
        IAM resources) with the resources that it records.

        Before you can set this option to ``true`` , you must set the ``allSupported`` option to
        ``true`` .

        If you set this option to ``true`` , when AWS Config adds support for a new type of global
        resource, it starts recording resources of that type automatically.

        The configuration details for any global resource are the same in all regions. To prevent
        duplicate configuration items, you should consider customizing AWS Config in only one region
        to record global resources.

      - **resourceTypes** *(list) --*

        A comma-separated list that specifies the types of AWS resources for which AWS Config records
        configuration changes (for example, ``AWS::EC2::Instance`` or ``AWS::CloudTrail::Trail`` ).

        Before you can set this option to ``true`` , you must set the ``allSupported`` option to
        ``false`` .

        If you set this option to ``true`` , when AWS Config adds support for a new type of resource,
        it will not record resources of that type unless you manually add that type to your recording
        group.

        For a list of valid ``resourceTypes`` values, see the **resourceType Value** column in
        `Supported AWS Resource Types
        <https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#supported-resources>`__
        .

        - *(string) --*
    """


_ClientPutConformancePackConformancePackInputParametersTypeDef = TypedDict(
    "_ClientPutConformancePackConformancePackInputParametersTypeDef",
    {"ParameterName": str, "ParameterValue": str},
)


class ClientPutConformancePackConformancePackInputParametersTypeDef(
    _ClientPutConformancePackConformancePackInputParametersTypeDef
):
    """
    Type definition for `ClientPutConformancePack` `ConformancePackInputParameters`

    Input parameters in the form of key-value pairs for the conformance pack, both of which you
    define. Keys can have a maximum character length of 128 characters, and values can have a
    maximum length of 256 characters.

    - **ParameterName** *(string) --* **[REQUIRED]**

      One part of a key-value pair.

    - **ParameterValue** *(string) --* **[REQUIRED]**

      Another part of the key-value pair.
    """


_ClientPutConformancePackResponseTypeDef = TypedDict(
    "_ClientPutConformancePackResponseTypeDef", {"ConformancePackArn": str}, total=False
)


class ClientPutConformancePackResponseTypeDef(_ClientPutConformancePackResponseTypeDef):
    """
    Type definition for `ClientPutConformancePack` `Response`

    - **ConformancePackArn** *(string) --*

      ARN of the conformance pack.
    """


_ClientPutDeliveryChannelDeliveryChannelconfigSnapshotDeliveryPropertiesTypeDef = TypedDict(
    "_ClientPutDeliveryChannelDeliveryChannelconfigSnapshotDeliveryPropertiesTypeDef",
    {"deliveryFrequency": str},
    total=False,
)


class ClientPutDeliveryChannelDeliveryChannelconfigSnapshotDeliveryPropertiesTypeDef(
    _ClientPutDeliveryChannelDeliveryChannelconfigSnapshotDeliveryPropertiesTypeDef
):
    """
    Type definition for `ClientPutDeliveryChannelDeliveryChannel` `configSnapshotDeliveryProperties`

    The options for how often AWS Config delivers configuration snapshots to the Amazon S3 bucket.

    - **deliveryFrequency** *(string) --*

      The frequency with which AWS Config delivers configuration snapshots.
    """


_ClientPutDeliveryChannelDeliveryChannelTypeDef = TypedDict(
    "_ClientPutDeliveryChannelDeliveryChannelTypeDef",
    {
        "name": str,
        "s3BucketName": str,
        "s3KeyPrefix": str,
        "snsTopicARN": str,
        "configSnapshotDeliveryProperties": ClientPutDeliveryChannelDeliveryChannelconfigSnapshotDeliveryPropertiesTypeDef,
    },
    total=False,
)


class ClientPutDeliveryChannelDeliveryChannelTypeDef(
    _ClientPutDeliveryChannelDeliveryChannelTypeDef
):
    """
    Type definition for `ClientPutDeliveryChannel` `DeliveryChannel`

    The configuration delivery channel object that delivers the configuration information to an
    Amazon S3 bucket and to an Amazon SNS topic.

    - **name** *(string) --*

      The name of the delivery channel. By default, AWS Config assigns the name "default" when
      creating the delivery channel. To change the delivery channel name, you must use the
      DeleteDeliveryChannel action to delete your current delivery channel, and then you must use the
      PutDeliveryChannel command to create a delivery channel that has the desired name.

    - **s3BucketName** *(string) --*

      The name of the Amazon S3 bucket to which AWS Config delivers configuration snapshots and
      configuration history files.

      If you specify a bucket that belongs to another AWS account, that bucket must have policies
      that grant access permissions to AWS Config. For more information, see `Permissions for the
      Amazon S3 Bucket
      <https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-policy.html>`__ in the AWS
      Config Developer Guide.

    - **s3KeyPrefix** *(string) --*

      The prefix for the specified Amazon S3 bucket.

    - **snsTopicARN** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon SNS topic to which AWS Config sends notifications
      about configuration changes.

      If you choose a topic from another account, the topic must have policies that grant access
      permissions to AWS Config. For more information, see `Permissions for the Amazon SNS Topic
      <https://docs.aws.amazon.com/config/latest/developerguide/sns-topic-policy.html>`__ in the AWS
      Config Developer Guide.

    - **configSnapshotDeliveryProperties** *(dict) --*

      The options for how often AWS Config delivers configuration snapshots to the Amazon S3 bucket.

      - **deliveryFrequency** *(string) --*

        The frequency with which AWS Config delivers configuration snapshots.
    """


_RequiredClientPutEvaluationsEvaluationsTypeDef = TypedDict(
    "_RequiredClientPutEvaluationsEvaluationsTypeDef",
    {
        "ComplianceResourceType": str,
        "ComplianceResourceId": str,
        "ComplianceType": str,
        "OrderingTimestamp": datetime,
    },
)
_OptionalClientPutEvaluationsEvaluationsTypeDef = TypedDict(
    "_OptionalClientPutEvaluationsEvaluationsTypeDef", {"Annotation": str}, total=False
)


class ClientPutEvaluationsEvaluationsTypeDef(
    _RequiredClientPutEvaluationsEvaluationsTypeDef,
    _OptionalClientPutEvaluationsEvaluationsTypeDef,
):
    """
    Type definition for `ClientPutEvaluations` `Evaluations`

    Identifies an AWS resource and indicates whether it complies with the AWS Config rule that it
    was evaluated against.

    - **ComplianceResourceType** *(string) --* **[REQUIRED]**

      The type of AWS resource that was evaluated.

    - **ComplianceResourceId** *(string) --* **[REQUIRED]**

      The ID of the AWS resource that was evaluated.

    - **ComplianceType** *(string) --* **[REQUIRED]**

      Indicates whether the AWS resource complies with the AWS Config rule that it was evaluated
      against.

      For the ``Evaluation`` data type, AWS Config supports only the ``COMPLIANT`` ,
      ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` values. AWS Config does not support the
      ``INSUFFICIENT_DATA`` value for this data type.

      Similarly, AWS Config does not accept ``INSUFFICIENT_DATA`` as the value for
      ``ComplianceType`` from a ``PutEvaluations`` request. For example, an AWS Lambda function for
      a custom AWS Config rule cannot pass an ``INSUFFICIENT_DATA`` value to AWS Config.

    - **Annotation** *(string) --*

      Supplementary information about how the evaluation determined the compliance.

    - **OrderingTimestamp** *(datetime) --* **[REQUIRED]**

      The time of the event in AWS Config that triggered the evaluation. For event-based
      evaluations, the time indicates when AWS Config created the configuration item that triggered
      the evaluation. For periodic evaluations, the time indicates when AWS Config triggered the
      evaluation at the frequency that you specified (for example, every 24 hours).
    """


_ClientPutEvaluationsResponseFailedEvaluationsTypeDef = TypedDict(
    "_ClientPutEvaluationsResponseFailedEvaluationsTypeDef",
    {
        "ComplianceResourceType": str,
        "ComplianceResourceId": str,
        "ComplianceType": str,
        "Annotation": str,
        "OrderingTimestamp": datetime,
    },
    total=False,
)


class ClientPutEvaluationsResponseFailedEvaluationsTypeDef(
    _ClientPutEvaluationsResponseFailedEvaluationsTypeDef
):
    """
    Type definition for `ClientPutEvaluationsResponse` `FailedEvaluations`

    Identifies an AWS resource and indicates whether it complies with the AWS Config rule that
    it was evaluated against.

    - **ComplianceResourceType** *(string) --*

      The type of AWS resource that was evaluated.

    - **ComplianceResourceId** *(string) --*

      The ID of the AWS resource that was evaluated.

    - **ComplianceType** *(string) --*

      Indicates whether the AWS resource complies with the AWS Config rule that it was
      evaluated against.

      For the ``Evaluation`` data type, AWS Config supports only the ``COMPLIANT`` ,
      ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` values. AWS Config does not support the
      ``INSUFFICIENT_DATA`` value for this data type.

      Similarly, AWS Config does not accept ``INSUFFICIENT_DATA`` as the value for
      ``ComplianceType`` from a ``PutEvaluations`` request. For example, an AWS Lambda function
      for a custom AWS Config rule cannot pass an ``INSUFFICIENT_DATA`` value to AWS Config.

    - **Annotation** *(string) --*

      Supplementary information about how the evaluation determined the compliance.

    - **OrderingTimestamp** *(datetime) --*

      The time of the event in AWS Config that triggered the evaluation. For event-based
      evaluations, the time indicates when AWS Config created the configuration item that
      triggered the evaluation. For periodic evaluations, the time indicates when AWS Config
      triggered the evaluation at the frequency that you specified (for example, every 24
      hours).
    """


_ClientPutEvaluationsResponseTypeDef = TypedDict(
    "_ClientPutEvaluationsResponseTypeDef",
    {"FailedEvaluations": List[ClientPutEvaluationsResponseFailedEvaluationsTypeDef]},
    total=False,
)


class ClientPutEvaluationsResponseTypeDef(_ClientPutEvaluationsResponseTypeDef):
    """
    Type definition for `ClientPutEvaluations` `Response`

    - **FailedEvaluations** *(list) --*

      Requests that failed because of a client or server error.

      - *(dict) --*

        Identifies an AWS resource and indicates whether it complies with the AWS Config rule that
        it was evaluated against.

        - **ComplianceResourceType** *(string) --*

          The type of AWS resource that was evaluated.

        - **ComplianceResourceId** *(string) --*

          The ID of the AWS resource that was evaluated.

        - **ComplianceType** *(string) --*

          Indicates whether the AWS resource complies with the AWS Config rule that it was
          evaluated against.

          For the ``Evaluation`` data type, AWS Config supports only the ``COMPLIANT`` ,
          ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` values. AWS Config does not support the
          ``INSUFFICIENT_DATA`` value for this data type.

          Similarly, AWS Config does not accept ``INSUFFICIENT_DATA`` as the value for
          ``ComplianceType`` from a ``PutEvaluations`` request. For example, an AWS Lambda function
          for a custom AWS Config rule cannot pass an ``INSUFFICIENT_DATA`` value to AWS Config.

        - **Annotation** *(string) --*

          Supplementary information about how the evaluation determined the compliance.

        - **OrderingTimestamp** *(datetime) --*

          The time of the event in AWS Config that triggered the evaluation. For event-based
          evaluations, the time indicates when AWS Config created the configuration item that
          triggered the evaluation. For periodic evaluations, the time indicates when AWS Config
          triggered the evaluation at the frequency that you specified (for example, every 24
          hours).
    """


_RequiredClientPutOrganizationConfigRuleOrganizationCustomRuleMetadataTypeDef = TypedDict(
    "_RequiredClientPutOrganizationConfigRuleOrganizationCustomRuleMetadataTypeDef",
    {"LambdaFunctionArn": str, "OrganizationConfigRuleTriggerTypes": List[str]},
)
_OptionalClientPutOrganizationConfigRuleOrganizationCustomRuleMetadataTypeDef = TypedDict(
    "_OptionalClientPutOrganizationConfigRuleOrganizationCustomRuleMetadataTypeDef",
    {
        "Description": str,
        "InputParameters": str,
        "MaximumExecutionFrequency": str,
        "ResourceTypesScope": List[str],
        "ResourceIdScope": str,
        "TagKeyScope": str,
        "TagValueScope": str,
    },
    total=False,
)


class ClientPutOrganizationConfigRuleOrganizationCustomRuleMetadataTypeDef(
    _RequiredClientPutOrganizationConfigRuleOrganizationCustomRuleMetadataTypeDef,
    _OptionalClientPutOrganizationConfigRuleOrganizationCustomRuleMetadataTypeDef,
):
    """
    Type definition for `ClientPutOrganizationConfigRule` `OrganizationCustomRuleMetadata`

    An ``OrganizationCustomRuleMetadata`` object.

    - **Description** *(string) --*

      The description that you provide for organization config rule.

    - **LambdaFunctionArn** *(string) --* **[REQUIRED]**

      The lambda function ARN.

    - **OrganizationConfigRuleTriggerTypes** *(list) --* **[REQUIRED]**

      The type of notification that triggers AWS Config to run an evaluation for a rule. You can
      specify the following notification types:

      * ``ConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config delivers a
      configuration item as a result of a resource change.

      * ``OversizedConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config
      delivers an oversized configuration item. AWS Config may generate this notification type when a
      resource changes and the notification exceeds the maximum size allowed by Amazon SNS.

      * ``ScheduledNotification`` - Triggers a periodic evaluation at the frequency specified for
      ``MaximumExecutionFrequency`` .

      - *(string) --*

    - **InputParameters** *(string) --*

      A string, in JSON format, that is passed to organization config rule Lambda function.

    - **MaximumExecutionFrequency** *(string) --*

      The maximum frequency with which AWS Config runs evaluations for a rule. Your custom rule is
      triggered when AWS Config delivers the configuration snapshot. For more information, see
      ConfigSnapshotDeliveryProperties .

      .. note::

        By default, rules with a periodic trigger are evaluated every 24 hours. To change the
        frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.

    - **ResourceTypesScope** *(list) --*

      The type of the AWS resource that was evaluated.

      - *(string) --*

    - **ResourceIdScope** *(string) --*

      The ID of the AWS resource that was evaluated.

    - **TagKeyScope** *(string) --*

      One part of a key-value pair that make up a tag. A key is a general label that acts like a
      category for more specific tag values.

    - **TagValueScope** *(string) --*

      The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a
      tag category (key).
    """


_RequiredClientPutOrganizationConfigRuleOrganizationManagedRuleMetadataTypeDef = TypedDict(
    "_RequiredClientPutOrganizationConfigRuleOrganizationManagedRuleMetadataTypeDef",
    {"RuleIdentifier": str},
)
_OptionalClientPutOrganizationConfigRuleOrganizationManagedRuleMetadataTypeDef = TypedDict(
    "_OptionalClientPutOrganizationConfigRuleOrganizationManagedRuleMetadataTypeDef",
    {
        "Description": str,
        "InputParameters": str,
        "MaximumExecutionFrequency": str,
        "ResourceTypesScope": List[str],
        "ResourceIdScope": str,
        "TagKeyScope": str,
        "TagValueScope": str,
    },
    total=False,
)


class ClientPutOrganizationConfigRuleOrganizationManagedRuleMetadataTypeDef(
    _RequiredClientPutOrganizationConfigRuleOrganizationManagedRuleMetadataTypeDef,
    _OptionalClientPutOrganizationConfigRuleOrganizationManagedRuleMetadataTypeDef,
):
    """
    Type definition for `ClientPutOrganizationConfigRule` `OrganizationManagedRuleMetadata`

    An ``OrganizationManagedRuleMetadata`` object.

    - **Description** *(string) --*

      The description that you provide for organization config rule.

    - **RuleIdentifier** *(string) --* **[REQUIRED]**

      For organization config managed rules, a predefined identifier from a list. For example,
      ``IAM_PASSWORD_POLICY`` is a managed rule. To reference a managed rule, see `Using AWS Managed
      Config Rules
      <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html>`__
      .

    - **InputParameters** *(string) --*

      A string, in JSON format, that is passed to organization config rule Lambda function.

    - **MaximumExecutionFrequency** *(string) --*

      The maximum frequency with which AWS Config runs evaluations for a rule. You are using an AWS
      managed rule that is triggered at a periodic frequency.

      .. note::

        By default, rules with a periodic trigger are evaluated every 24 hours. To change the
        frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.

    - **ResourceTypesScope** *(list) --*

      The type of the AWS resource that was evaluated.

      - *(string) --*

    - **ResourceIdScope** *(string) --*

      The ID of the AWS resource that was evaluated.

    - **TagKeyScope** *(string) --*

      One part of a key-value pair that make up a tag. A key is a general label that acts like a
      category for more specific tag values.

    - **TagValueScope** *(string) --*

      The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a
      tag category (key).
    """


_ClientPutOrganizationConfigRuleResponseTypeDef = TypedDict(
    "_ClientPutOrganizationConfigRuleResponseTypeDef",
    {"OrganizationConfigRuleArn": str},
    total=False,
)


class ClientPutOrganizationConfigRuleResponseTypeDef(
    _ClientPutOrganizationConfigRuleResponseTypeDef
):
    """
    Type definition for `ClientPutOrganizationConfigRule` `Response`

    - **OrganizationConfigRuleArn** *(string) --*

      The Amazon Resource Name (ARN) of an organization config rule.
    """


_ClientPutOrganizationConformancePackConformancePackInputParametersTypeDef = TypedDict(
    "_ClientPutOrganizationConformancePackConformancePackInputParametersTypeDef",
    {"ParameterName": str, "ParameterValue": str},
)


class ClientPutOrganizationConformancePackConformancePackInputParametersTypeDef(
    _ClientPutOrganizationConformancePackConformancePackInputParametersTypeDef
):
    """
    Type definition for `ClientPutOrganizationConformancePack` `ConformancePackInputParameters`

    Input parameters in the form of key-value pairs for the conformance pack, both of which you
    define. Keys can have a maximum character length of 128 characters, and values can have a
    maximum length of 256 characters.

    - **ParameterName** *(string) --* **[REQUIRED]**

      One part of a key-value pair.

    - **ParameterValue** *(string) --* **[REQUIRED]**

      Another part of the key-value pair.
    """


_ClientPutOrganizationConformancePackResponseTypeDef = TypedDict(
    "_ClientPutOrganizationConformancePackResponseTypeDef",
    {"OrganizationConformancePackArn": str},
    total=False,
)


class ClientPutOrganizationConformancePackResponseTypeDef(
    _ClientPutOrganizationConformancePackResponseTypeDef
):
    """
    Type definition for `ClientPutOrganizationConformancePack` `Response`

    - **OrganizationConformancePackArn** *(string) --*

      ARN of the organization conformance pack.
    """


_ClientPutRemediationConfigurationsRemediationConfigurationsExecutionControlsSsmControlsTypeDef = TypedDict(
    "_ClientPutRemediationConfigurationsRemediationConfigurationsExecutionControlsSsmControlsTypeDef",
    {"ConcurrentExecutionRatePercentage": int, "ErrorPercentage": int},
    total=False,
)


class ClientPutRemediationConfigurationsRemediationConfigurationsExecutionControlsSsmControlsTypeDef(
    _ClientPutRemediationConfigurationsRemediationConfigurationsExecutionControlsSsmControlsTypeDef
):
    """
    Type definition for `ClientPutRemediationConfigurationsRemediationConfigurationsExecutionControls` `SsmControls`

    A SsmControls object.

    - **ConcurrentExecutionRatePercentage** *(integer) --*

      The maximum percentage of remediation actions allowed to run in parallel on the
      non-compliant resources for that specific rule. You can specify a percentage, such as
      10%. The default value is 10.

    - **ErrorPercentage** *(integer) --*

      The percentage of errors that are allowed before SSM stops running automations on
      non-compliant resources for that specific rule. You can specify a percentage of errors,
      for example 10%. If you do not specifiy a percentage, the default is 50%. For example, if
      you set the ErrorPercentage to 40% for 10 non-compliant resources, then SSM stops running
      the automations when the fifth error is received.
    """


_ClientPutRemediationConfigurationsRemediationConfigurationsExecutionControlsTypeDef = TypedDict(
    "_ClientPutRemediationConfigurationsRemediationConfigurationsExecutionControlsTypeDef",
    {
        "SsmControls": ClientPutRemediationConfigurationsRemediationConfigurationsExecutionControlsSsmControlsTypeDef
    },
    total=False,
)


class ClientPutRemediationConfigurationsRemediationConfigurationsExecutionControlsTypeDef(
    _ClientPutRemediationConfigurationsRemediationConfigurationsExecutionControlsTypeDef
):
    """
    Type definition for `ClientPutRemediationConfigurationsRemediationConfigurations` `ExecutionControls`

    An ExecutionControls object.

    - **SsmControls** *(dict) --*

      A SsmControls object.

      - **ConcurrentExecutionRatePercentage** *(integer) --*

        The maximum percentage of remediation actions allowed to run in parallel on the
        non-compliant resources for that specific rule. You can specify a percentage, such as
        10%. The default value is 10.

      - **ErrorPercentage** *(integer) --*

        The percentage of errors that are allowed before SSM stops running automations on
        non-compliant resources for that specific rule. You can specify a percentage of errors,
        for example 10%. If you do not specifiy a percentage, the default is 50%. For example, if
        you set the ErrorPercentage to 40% for 10 non-compliant resources, then SSM stops running
        the automations when the fifth error is received.
    """


_ClientPutRemediationConfigurationsRemediationConfigurationsParametersResourceValueTypeDef = TypedDict(
    "_ClientPutRemediationConfigurationsRemediationConfigurationsParametersResourceValueTypeDef",
    {"Value": str},
)


class ClientPutRemediationConfigurationsRemediationConfigurationsParametersResourceValueTypeDef(
    _ClientPutRemediationConfigurationsRemediationConfigurationsParametersResourceValueTypeDef
):
    """
    Type definition for `ClientPutRemediationConfigurationsRemediationConfigurationsParameters` `ResourceValue`

    The value is dynamic and changes at run-time.

    - **Value** *(string) --* **[REQUIRED]**

      The value is a resource ID.
    """


_ClientPutRemediationConfigurationsRemediationConfigurationsParametersStaticValueTypeDef = TypedDict(
    "_ClientPutRemediationConfigurationsRemediationConfigurationsParametersStaticValueTypeDef",
    {"Values": List[str]},
)


class ClientPutRemediationConfigurationsRemediationConfigurationsParametersStaticValueTypeDef(
    _ClientPutRemediationConfigurationsRemediationConfigurationsParametersStaticValueTypeDef
):
    """
    Type definition for `ClientPutRemediationConfigurationsRemediationConfigurationsParameters` `StaticValue`

    The value is static and does not change at run-time.

    - **Values** *(list) --* **[REQUIRED]**

      A list of values. For example, the ARN of the assumed role.

      - *(string) --*
    """


_ClientPutRemediationConfigurationsRemediationConfigurationsParametersTypeDef = TypedDict(
    "_ClientPutRemediationConfigurationsRemediationConfigurationsParametersTypeDef",
    {
        "ResourceValue": ClientPutRemediationConfigurationsRemediationConfigurationsParametersResourceValueTypeDef,
        "StaticValue": ClientPutRemediationConfigurationsRemediationConfigurationsParametersStaticValueTypeDef,
    },
    total=False,
)


class ClientPutRemediationConfigurationsRemediationConfigurationsParametersTypeDef(
    _ClientPutRemediationConfigurationsRemediationConfigurationsParametersTypeDef
):
    """
    Type definition for `ClientPutRemediationConfigurationsRemediationConfigurations` `Parameters`

    The value is either a dynamic (resource) value or a static value. You must select either
    a dynamic value or a static value.

    - **ResourceValue** *(dict) --*

      The value is dynamic and changes at run-time.

      - **Value** *(string) --* **[REQUIRED]**

        The value is a resource ID.

    - **StaticValue** *(dict) --*

      The value is static and does not change at run-time.

      - **Values** *(list) --* **[REQUIRED]**

        A list of values. For example, the ARN of the assumed role.

        - *(string) --*
    """


_RequiredClientPutRemediationConfigurationsRemediationConfigurationsTypeDef = TypedDict(
    "_RequiredClientPutRemediationConfigurationsRemediationConfigurationsTypeDef",
    {"ConfigRuleName": str, "TargetType": str, "TargetId": str},
)
_OptionalClientPutRemediationConfigurationsRemediationConfigurationsTypeDef = TypedDict(
    "_OptionalClientPutRemediationConfigurationsRemediationConfigurationsTypeDef",
    {
        "TargetVersion": str,
        "Parameters": Dict[
            str,
            ClientPutRemediationConfigurationsRemediationConfigurationsParametersTypeDef,
        ],
        "ResourceType": str,
        "Automatic": bool,
        "ExecutionControls": ClientPutRemediationConfigurationsRemediationConfigurationsExecutionControlsTypeDef,
        "MaximumAutomaticAttempts": int,
        "RetryAttemptSeconds": int,
        "Arn": str,
        "CreatedByService": str,
    },
    total=False,
)


class ClientPutRemediationConfigurationsRemediationConfigurationsTypeDef(
    _RequiredClientPutRemediationConfigurationsRemediationConfigurationsTypeDef,
    _OptionalClientPutRemediationConfigurationsRemediationConfigurationsTypeDef,
):
    """
    Type definition for `ClientPutRemediationConfigurations` `RemediationConfigurations`

    An object that represents the details about the remediation configuration that includes the
    remediation action, parameters, and data to execute the action.

    - **ConfigRuleName** *(string) --* **[REQUIRED]**

      The name of the AWS Config rule.

    - **TargetType** *(string) --* **[REQUIRED]**

      The type of the target. Target executes remediation. For example, SSM document.

    - **TargetId** *(string) --* **[REQUIRED]**

      Target ID is the name of the public document.

    - **TargetVersion** *(string) --*

      Version of the target. For example, version of the SSM document.

    - **Parameters** *(dict) --*

      An object of the RemediationParameterValue.

      - *(string) --*

        - *(dict) --*

          The value is either a dynamic (resource) value or a static value. You must select either
          a dynamic value or a static value.

          - **ResourceValue** *(dict) --*

            The value is dynamic and changes at run-time.

            - **Value** *(string) --* **[REQUIRED]**

              The value is a resource ID.

          - **StaticValue** *(dict) --*

            The value is static and does not change at run-time.

            - **Values** *(list) --* **[REQUIRED]**

              A list of values. For example, the ARN of the assumed role.

              - *(string) --*

    - **ResourceType** *(string) --*

      The type of a resource.

    - **Automatic** *(boolean) --*

      The remediation is triggered automatically.

    - **ExecutionControls** *(dict) --*

      An ExecutionControls object.

      - **SsmControls** *(dict) --*

        A SsmControls object.

        - **ConcurrentExecutionRatePercentage** *(integer) --*

          The maximum percentage of remediation actions allowed to run in parallel on the
          non-compliant resources for that specific rule. You can specify a percentage, such as
          10%. The default value is 10.

        - **ErrorPercentage** *(integer) --*

          The percentage of errors that are allowed before SSM stops running automations on
          non-compliant resources for that specific rule. You can specify a percentage of errors,
          for example 10%. If you do not specifiy a percentage, the default is 50%. For example, if
          you set the ErrorPercentage to 40% for 10 non-compliant resources, then SSM stops running
          the automations when the fifth error is received.

    - **MaximumAutomaticAttempts** *(integer) --*

      The maximum number of failed attempts for auto-remediation. If you do not select a number,
      the default is 5.

      For example, if you specify MaximumAutomaticAttempts as 5 with RetryAttemptsSeconds as 50
      seconds, AWS Config throws an exception after the 5th failed attempt within 50 seconds.

    - **RetryAttemptSeconds** *(integer) --*

      Maximum time in seconds that AWS Config runs auto-remediation. If you do not select a number,
      the default is 60 seconds.

      For example, if you specify RetryAttemptsSeconds as 50 seconds and MaximumAutomaticAttempts
      as 5, AWS Config will run auto-remediations 5 times within 50 seconds before throwing an
      exception.

    - **Arn** *(string) --*

      Amazon Resource Name (ARN) of remediation configuration.

    - **CreatedByService** *(string) --*

      Name of the service that owns the service linked rule, if applicable.
    """


_ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsExecutionControlsSsmControlsTypeDef = TypedDict(
    "_ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsExecutionControlsSsmControlsTypeDef",
    {"ConcurrentExecutionRatePercentage": int, "ErrorPercentage": int},
    total=False,
)


class ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsExecutionControlsSsmControlsTypeDef(
    _ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsExecutionControlsSsmControlsTypeDef
):
    """
    Type definition for `ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsExecutionControls` `SsmControls`

    A SsmControls object.

    - **ConcurrentExecutionRatePercentage** *(integer) --*

      The maximum percentage of remediation actions allowed to run in parallel on the
      non-compliant resources for that specific rule. You can specify a percentage,
      such as 10%. The default value is 10.

    - **ErrorPercentage** *(integer) --*

      The percentage of errors that are allowed before SSM stops running automations on
      non-compliant resources for that specific rule. You can specify a percentage of
      errors, for example 10%. If you do not specifiy a percentage, the default is 50%.
      For example, if you set the ErrorPercentage to 40% for 10 non-compliant
      resources, then SSM stops running the automations when the fifth error is
      received.
    """


_ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsExecutionControlsTypeDef = TypedDict(
    "_ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsExecutionControlsTypeDef",
    {
        "SsmControls": ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsExecutionControlsSsmControlsTypeDef
    },
    total=False,
)


class ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsExecutionControlsTypeDef(
    _ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsExecutionControlsTypeDef
):
    """
    Type definition for `ClientPutRemediationConfigurationsResponseFailedBatchesFailedItems` `ExecutionControls`

    An ExecutionControls object.

    - **SsmControls** *(dict) --*

      A SsmControls object.

      - **ConcurrentExecutionRatePercentage** *(integer) --*

        The maximum percentage of remediation actions allowed to run in parallel on the
        non-compliant resources for that specific rule. You can specify a percentage,
        such as 10%. The default value is 10.

      - **ErrorPercentage** *(integer) --*

        The percentage of errors that are allowed before SSM stops running automations on
        non-compliant resources for that specific rule. You can specify a percentage of
        errors, for example 10%. If you do not specifiy a percentage, the default is 50%.
        For example, if you set the ErrorPercentage to 40% for 10 non-compliant
        resources, then SSM stops running the automations when the fifth error is
        received.
    """


_ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersResourceValueTypeDef = TypedDict(
    "_ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersResourceValueTypeDef",
    {"Value": str},
    total=False,
)


class ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersResourceValueTypeDef(
    _ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersResourceValueTypeDef
):
    """
    Type definition for `ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParameters` `ResourceValue`

    The value is dynamic and changes at run-time.

    - **Value** *(string) --*

      The value is a resource ID.
    """


_ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersStaticValueTypeDef = TypedDict(
    "_ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersStaticValueTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersStaticValueTypeDef(
    _ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersStaticValueTypeDef
):
    """
    Type definition for `ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParameters` `StaticValue`

    The value is static and does not change at run-time.

    - **Values** *(list) --*

      A list of values. For example, the ARN of the assumed role.

      - *(string) --*
    """


_ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersTypeDef = TypedDict(
    "_ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersTypeDef",
    {
        "ResourceValue": ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersResourceValueTypeDef,
        "StaticValue": ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersStaticValueTypeDef,
    },
    total=False,
)


class ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersTypeDef(
    _ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersTypeDef
):
    """
    Type definition for `ClientPutRemediationConfigurationsResponseFailedBatchesFailedItems` `Parameters`

    The value is either a dynamic (resource) value or a static value. You must select
    either a dynamic value or a static value.

    - **ResourceValue** *(dict) --*

      The value is dynamic and changes at run-time.

      - **Value** *(string) --*

        The value is a resource ID.

    - **StaticValue** *(dict) --*

      The value is static and does not change at run-time.

      - **Values** *(list) --*

        A list of values. For example, the ARN of the assumed role.

        - *(string) --*
    """


_ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsTypeDef = TypedDict(
    "_ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsTypeDef",
    {
        "ConfigRuleName": str,
        "TargetType": str,
        "TargetId": str,
        "TargetVersion": str,
        "Parameters": Dict[
            str,
            ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsParametersTypeDef,
        ],
        "ResourceType": str,
        "Automatic": bool,
        "ExecutionControls": ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsExecutionControlsTypeDef,
        "MaximumAutomaticAttempts": int,
        "RetryAttemptSeconds": int,
        "Arn": str,
        "CreatedByService": str,
    },
    total=False,
)


class ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsTypeDef(
    _ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsTypeDef
):
    """
    Type definition for `ClientPutRemediationConfigurationsResponseFailedBatches` `FailedItems`

    An object that represents the details about the remediation configuration that includes
    the remediation action, parameters, and data to execute the action.

    - **ConfigRuleName** *(string) --*

      The name of the AWS Config rule.

    - **TargetType** *(string) --*

      The type of the target. Target executes remediation. For example, SSM document.

    - **TargetId** *(string) --*

      Target ID is the name of the public document.

    - **TargetVersion** *(string) --*

      Version of the target. For example, version of the SSM document.

    - **Parameters** *(dict) --*

      An object of the RemediationParameterValue.

      - *(string) --*

        - *(dict) --*

          The value is either a dynamic (resource) value or a static value. You must select
          either a dynamic value or a static value.

          - **ResourceValue** *(dict) --*

            The value is dynamic and changes at run-time.

            - **Value** *(string) --*

              The value is a resource ID.

          - **StaticValue** *(dict) --*

            The value is static and does not change at run-time.

            - **Values** *(list) --*

              A list of values. For example, the ARN of the assumed role.

              - *(string) --*

    - **ResourceType** *(string) --*

      The type of a resource.

    - **Automatic** *(boolean) --*

      The remediation is triggered automatically.

    - **ExecutionControls** *(dict) --*

      An ExecutionControls object.

      - **SsmControls** *(dict) --*

        A SsmControls object.

        - **ConcurrentExecutionRatePercentage** *(integer) --*

          The maximum percentage of remediation actions allowed to run in parallel on the
          non-compliant resources for that specific rule. You can specify a percentage,
          such as 10%. The default value is 10.

        - **ErrorPercentage** *(integer) --*

          The percentage of errors that are allowed before SSM stops running automations on
          non-compliant resources for that specific rule. You can specify a percentage of
          errors, for example 10%. If you do not specifiy a percentage, the default is 50%.
          For example, if you set the ErrorPercentage to 40% for 10 non-compliant
          resources, then SSM stops running the automations when the fifth error is
          received.

    - **MaximumAutomaticAttempts** *(integer) --*

      The maximum number of failed attempts for auto-remediation. If you do not select a
      number, the default is 5.

      For example, if you specify MaximumAutomaticAttempts as 5 with RetryAttemptsSeconds
      as 50 seconds, AWS Config throws an exception after the 5th failed attempt within 50
      seconds.

    - **RetryAttemptSeconds** *(integer) --*

      Maximum time in seconds that AWS Config runs auto-remediation. If you do not select a
      number, the default is 60 seconds.

      For example, if you specify RetryAttemptsSeconds as 50 seconds and
      MaximumAutomaticAttempts as 5, AWS Config will run auto-remediations 5 times within
      50 seconds before throwing an exception.

    - **Arn** *(string) --*

      Amazon Resource Name (ARN) of remediation configuration.

    - **CreatedByService** *(string) --*

      Name of the service that owns the service linked rule, if applicable.
    """


_ClientPutRemediationConfigurationsResponseFailedBatchesTypeDef = TypedDict(
    "_ClientPutRemediationConfigurationsResponseFailedBatchesTypeDef",
    {
        "FailureMessage": str,
        "FailedItems": List[
            ClientPutRemediationConfigurationsResponseFailedBatchesFailedItemsTypeDef
        ],
    },
    total=False,
)


class ClientPutRemediationConfigurationsResponseFailedBatchesTypeDef(
    _ClientPutRemediationConfigurationsResponseFailedBatchesTypeDef
):
    """
    Type definition for `ClientPutRemediationConfigurationsResponse` `FailedBatches`

    List of each of the failed remediations with specific reasons.

    - **FailureMessage** *(string) --*

      Returns a failure message. For example, the resource is already compliant.

    - **FailedItems** *(list) --*

      Returns remediation configurations of the failed items.

      - *(dict) --*

        An object that represents the details about the remediation configuration that includes
        the remediation action, parameters, and data to execute the action.

        - **ConfigRuleName** *(string) --*

          The name of the AWS Config rule.

        - **TargetType** *(string) --*

          The type of the target. Target executes remediation. For example, SSM document.

        - **TargetId** *(string) --*

          Target ID is the name of the public document.

        - **TargetVersion** *(string) --*

          Version of the target. For example, version of the SSM document.

        - **Parameters** *(dict) --*

          An object of the RemediationParameterValue.

          - *(string) --*

            - *(dict) --*

              The value is either a dynamic (resource) value or a static value. You must select
              either a dynamic value or a static value.

              - **ResourceValue** *(dict) --*

                The value is dynamic and changes at run-time.

                - **Value** *(string) --*

                  The value is a resource ID.

              - **StaticValue** *(dict) --*

                The value is static and does not change at run-time.

                - **Values** *(list) --*

                  A list of values. For example, the ARN of the assumed role.

                  - *(string) --*

        - **ResourceType** *(string) --*

          The type of a resource.

        - **Automatic** *(boolean) --*

          The remediation is triggered automatically.

        - **ExecutionControls** *(dict) --*

          An ExecutionControls object.

          - **SsmControls** *(dict) --*

            A SsmControls object.

            - **ConcurrentExecutionRatePercentage** *(integer) --*

              The maximum percentage of remediation actions allowed to run in parallel on the
              non-compliant resources for that specific rule. You can specify a percentage,
              such as 10%. The default value is 10.

            - **ErrorPercentage** *(integer) --*

              The percentage of errors that are allowed before SSM stops running automations on
              non-compliant resources for that specific rule. You can specify a percentage of
              errors, for example 10%. If you do not specifiy a percentage, the default is 50%.
              For example, if you set the ErrorPercentage to 40% for 10 non-compliant
              resources, then SSM stops running the automations when the fifth error is
              received.

        - **MaximumAutomaticAttempts** *(integer) --*

          The maximum number of failed attempts for auto-remediation. If you do not select a
          number, the default is 5.

          For example, if you specify MaximumAutomaticAttempts as 5 with RetryAttemptsSeconds
          as 50 seconds, AWS Config throws an exception after the 5th failed attempt within 50
          seconds.

        - **RetryAttemptSeconds** *(integer) --*

          Maximum time in seconds that AWS Config runs auto-remediation. If you do not select a
          number, the default is 60 seconds.

          For example, if you specify RetryAttemptsSeconds as 50 seconds and
          MaximumAutomaticAttempts as 5, AWS Config will run auto-remediations 5 times within
          50 seconds before throwing an exception.

        - **Arn** *(string) --*

          Amazon Resource Name (ARN) of remediation configuration.

        - **CreatedByService** *(string) --*

          Name of the service that owns the service linked rule, if applicable.
    """


_ClientPutRemediationConfigurationsResponseTypeDef = TypedDict(
    "_ClientPutRemediationConfigurationsResponseTypeDef",
    {
        "FailedBatches": List[
            ClientPutRemediationConfigurationsResponseFailedBatchesTypeDef
        ]
    },
    total=False,
)


class ClientPutRemediationConfigurationsResponseTypeDef(
    _ClientPutRemediationConfigurationsResponseTypeDef
):
    """
    Type definition for `ClientPutRemediationConfigurations` `Response`

    - **FailedBatches** *(list) --*

      Returns a list of failed remediation batch objects.

      - *(dict) --*

        List of each of the failed remediations with specific reasons.

        - **FailureMessage** *(string) --*

          Returns a failure message. For example, the resource is already compliant.

        - **FailedItems** *(list) --*

          Returns remediation configurations of the failed items.

          - *(dict) --*

            An object that represents the details about the remediation configuration that includes
            the remediation action, parameters, and data to execute the action.

            - **ConfigRuleName** *(string) --*

              The name of the AWS Config rule.

            - **TargetType** *(string) --*

              The type of the target. Target executes remediation. For example, SSM document.

            - **TargetId** *(string) --*

              Target ID is the name of the public document.

            - **TargetVersion** *(string) --*

              Version of the target. For example, version of the SSM document.

            - **Parameters** *(dict) --*

              An object of the RemediationParameterValue.

              - *(string) --*

                - *(dict) --*

                  The value is either a dynamic (resource) value or a static value. You must select
                  either a dynamic value or a static value.

                  - **ResourceValue** *(dict) --*

                    The value is dynamic and changes at run-time.

                    - **Value** *(string) --*

                      The value is a resource ID.

                  - **StaticValue** *(dict) --*

                    The value is static and does not change at run-time.

                    - **Values** *(list) --*

                      A list of values. For example, the ARN of the assumed role.

                      - *(string) --*

            - **ResourceType** *(string) --*

              The type of a resource.

            - **Automatic** *(boolean) --*

              The remediation is triggered automatically.

            - **ExecutionControls** *(dict) --*

              An ExecutionControls object.

              - **SsmControls** *(dict) --*

                A SsmControls object.

                - **ConcurrentExecutionRatePercentage** *(integer) --*

                  The maximum percentage of remediation actions allowed to run in parallel on the
                  non-compliant resources for that specific rule. You can specify a percentage,
                  such as 10%. The default value is 10.

                - **ErrorPercentage** *(integer) --*

                  The percentage of errors that are allowed before SSM stops running automations on
                  non-compliant resources for that specific rule. You can specify a percentage of
                  errors, for example 10%. If you do not specifiy a percentage, the default is 50%.
                  For example, if you set the ErrorPercentage to 40% for 10 non-compliant
                  resources, then SSM stops running the automations when the fifth error is
                  received.

            - **MaximumAutomaticAttempts** *(integer) --*

              The maximum number of failed attempts for auto-remediation. If you do not select a
              number, the default is 5.

              For example, if you specify MaximumAutomaticAttempts as 5 with RetryAttemptsSeconds
              as 50 seconds, AWS Config throws an exception after the 5th failed attempt within 50
              seconds.

            - **RetryAttemptSeconds** *(integer) --*

              Maximum time in seconds that AWS Config runs auto-remediation. If you do not select a
              number, the default is 60 seconds.

              For example, if you specify RetryAttemptsSeconds as 50 seconds and
              MaximumAutomaticAttempts as 5, AWS Config will run auto-remediations 5 times within
              50 seconds before throwing an exception.

            - **Arn** *(string) --*

              Amazon Resource Name (ARN) of remediation configuration.

            - **CreatedByService** *(string) --*

              Name of the service that owns the service linked rule, if applicable.
    """


_ClientPutRemediationExceptionsResourceKeysTypeDef = TypedDict(
    "_ClientPutRemediationExceptionsResourceKeysTypeDef",
    {"ResourceType": str, "ResourceId": str},
    total=False,
)


class ClientPutRemediationExceptionsResourceKeysTypeDef(
    _ClientPutRemediationExceptionsResourceKeysTypeDef
):
    """
    Type definition for `ClientPutRemediationExceptions` `ResourceKeys`

    The details that identify a resource within AWS Config, including the resource type and
    resource ID.

    - **ResourceType** *(string) --*

      The type of a resource.

    - **ResourceId** *(string) --*

      The ID of the resource (for example., sg-xxxxxx).
    """


_ClientPutRemediationExceptionsResponseFailedBatchesFailedItemsTypeDef = TypedDict(
    "_ClientPutRemediationExceptionsResponseFailedBatchesFailedItemsTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceType": str,
        "ResourceId": str,
        "Message": str,
        "ExpirationTime": datetime,
    },
    total=False,
)


class ClientPutRemediationExceptionsResponseFailedBatchesFailedItemsTypeDef(
    _ClientPutRemediationExceptionsResponseFailedBatchesFailedItemsTypeDef
):
    """
    Type definition for `ClientPutRemediationExceptionsResponseFailedBatches` `FailedItems`

    An object that represents the details about the remediation exception. The details
    include the rule name, an explanation of an exception, the time when the exception will
    be deleted, the resource ID, and resource type.

    - **ConfigRuleName** *(string) --*

      The name of the AWS Config rule.

    - **ResourceType** *(string) --*

      The type of a resource.

    - **ResourceId** *(string) --*

      The ID of the resource (for example., sg-xxxxxx).

    - **Message** *(string) --*

      An explanation of an remediation exception.

    - **ExpirationTime** *(datetime) --*

      The time when the remediation exception will be deleted.
    """


_ClientPutRemediationExceptionsResponseFailedBatchesTypeDef = TypedDict(
    "_ClientPutRemediationExceptionsResponseFailedBatchesTypeDef",
    {
        "FailureMessage": str,
        "FailedItems": List[
            ClientPutRemediationExceptionsResponseFailedBatchesFailedItemsTypeDef
        ],
    },
    total=False,
)


class ClientPutRemediationExceptionsResponseFailedBatchesTypeDef(
    _ClientPutRemediationExceptionsResponseFailedBatchesTypeDef
):
    """
    Type definition for `ClientPutRemediationExceptionsResponse` `FailedBatches`

    List of each of the failed remediation exceptions with specific reasons.

    - **FailureMessage** *(string) --*

      Returns a failure message. For example, the auto-remediation has failed.

    - **FailedItems** *(list) --*

      Returns remediation exception resource key object of the failed items.

      - *(dict) --*

        An object that represents the details about the remediation exception. The details
        include the rule name, an explanation of an exception, the time when the exception will
        be deleted, the resource ID, and resource type.

        - **ConfigRuleName** *(string) --*

          The name of the AWS Config rule.

        - **ResourceType** *(string) --*

          The type of a resource.

        - **ResourceId** *(string) --*

          The ID of the resource (for example., sg-xxxxxx).

        - **Message** *(string) --*

          An explanation of an remediation exception.

        - **ExpirationTime** *(datetime) --*

          The time when the remediation exception will be deleted.
    """


_ClientPutRemediationExceptionsResponseTypeDef = TypedDict(
    "_ClientPutRemediationExceptionsResponseTypeDef",
    {"FailedBatches": List[ClientPutRemediationExceptionsResponseFailedBatchesTypeDef]},
    total=False,
)


class ClientPutRemediationExceptionsResponseTypeDef(
    _ClientPutRemediationExceptionsResponseTypeDef
):
    """
    Type definition for `ClientPutRemediationExceptions` `Response`

    - **FailedBatches** *(list) --*

      Returns a list of failed remediation exceptions batch objects. Each object in the batch
      consists of a list of failed items and failure messages.

      - *(dict) --*

        List of each of the failed remediation exceptions with specific reasons.

        - **FailureMessage** *(string) --*

          Returns a failure message. For example, the auto-remediation has failed.

        - **FailedItems** *(list) --*

          Returns remediation exception resource key object of the failed items.

          - *(dict) --*

            An object that represents the details about the remediation exception. The details
            include the rule name, an explanation of an exception, the time when the exception will
            be deleted, the resource ID, and resource type.

            - **ConfigRuleName** *(string) --*

              The name of the AWS Config rule.

            - **ResourceType** *(string) --*

              The type of a resource.

            - **ResourceId** *(string) --*

              The ID of the resource (for example., sg-xxxxxx).

            - **Message** *(string) --*

              An explanation of an remediation exception.

            - **ExpirationTime** *(datetime) --*

              The time when the remediation exception will be deleted.
    """


_ClientPutRetentionConfigurationResponseRetentionConfigurationTypeDef = TypedDict(
    "_ClientPutRetentionConfigurationResponseRetentionConfigurationTypeDef",
    {"Name": str, "RetentionPeriodInDays": int},
    total=False,
)


class ClientPutRetentionConfigurationResponseRetentionConfigurationTypeDef(
    _ClientPutRetentionConfigurationResponseRetentionConfigurationTypeDef
):
    """
    Type definition for `ClientPutRetentionConfigurationResponse` `RetentionConfiguration`

    Returns a retention configuration object.

    - **Name** *(string) --*

      The name of the retention configuration object.

    - **RetentionPeriodInDays** *(integer) --*

      Number of days AWS Config stores your historical information.

      .. note::

        Currently, only applicable to the configuration item history.
    """


_ClientPutRetentionConfigurationResponseTypeDef = TypedDict(
    "_ClientPutRetentionConfigurationResponseTypeDef",
    {
        "RetentionConfiguration": ClientPutRetentionConfigurationResponseRetentionConfigurationTypeDef
    },
    total=False,
)


class ClientPutRetentionConfigurationResponseTypeDef(
    _ClientPutRetentionConfigurationResponseTypeDef
):
    """
    Type definition for `ClientPutRetentionConfiguration` `Response`

    - **RetentionConfiguration** *(dict) --*

      Returns a retention configuration object.

      - **Name** *(string) --*

        The name of the retention configuration object.

      - **RetentionPeriodInDays** *(integer) --*

        Number of days AWS Config stores your historical information.

        .. note::

          Currently, only applicable to the configuration item history.
    """


_ClientSelectResourceConfigResponseQueryInfoSelectFieldsTypeDef = TypedDict(
    "_ClientSelectResourceConfigResponseQueryInfoSelectFieldsTypeDef",
    {"Name": str},
    total=False,
)


class ClientSelectResourceConfigResponseQueryInfoSelectFieldsTypeDef(
    _ClientSelectResourceConfigResponseQueryInfoSelectFieldsTypeDef
):
    """
    Type definition for `ClientSelectResourceConfigResponseQueryInfo` `SelectFields`

    Details about the fields such as name of the field.

    - **Name** *(string) --*

      Name of the field.
    """


_ClientSelectResourceConfigResponseQueryInfoTypeDef = TypedDict(
    "_ClientSelectResourceConfigResponseQueryInfoTypeDef",
    {
        "SelectFields": List[
            ClientSelectResourceConfigResponseQueryInfoSelectFieldsTypeDef
        ]
    },
    total=False,
)


class ClientSelectResourceConfigResponseQueryInfoTypeDef(
    _ClientSelectResourceConfigResponseQueryInfoTypeDef
):
    """
    Type definition for `ClientSelectResourceConfigResponse` `QueryInfo`

    Returns the ``QueryInfo`` object.

    - **SelectFields** *(list) --*

      Returns a ``FieldInfo`` object.

      - *(dict) --*

        Details about the fields such as name of the field.

        - **Name** *(string) --*

          Name of the field.
    """


_ClientSelectResourceConfigResponseTypeDef = TypedDict(
    "_ClientSelectResourceConfigResponseTypeDef",
    {
        "Results": List[str],
        "QueryInfo": ClientSelectResourceConfigResponseQueryInfoTypeDef,
        "NextToken": str,
    },
    total=False,
)


class ClientSelectResourceConfigResponseTypeDef(
    _ClientSelectResourceConfigResponseTypeDef
):
    """
    Type definition for `ClientSelectResourceConfig` `Response`

    - **Results** *(list) --*

      Returns the results for the SQL query.

      - *(string) --*

    - **QueryInfo** *(dict) --*

      Returns the ``QueryInfo`` object.

      - **SelectFields** *(list) --*

        Returns a ``FieldInfo`` object.

        - *(dict) --*

          Details about the fields such as name of the field.

          - **Name** *(string) --*

            Name of the field.

    - **NextToken** *(string) --*

      The ``nextToken`` string returned in a previous request that you use to request the next page
      of results in a paginated response.
    """


_ClientStartRemediationExecutionResourceKeysTypeDef = TypedDict(
    "_ClientStartRemediationExecutionResourceKeysTypeDef",
    {"resourceType": str, "resourceId": str},
)


class ClientStartRemediationExecutionResourceKeysTypeDef(
    _ClientStartRemediationExecutionResourceKeysTypeDef
):
    """
    Type definition for `ClientStartRemediationExecution` `ResourceKeys`

    The details that identify a resource within AWS Config, including the resource type and
    resource ID.

    - **resourceType** *(string) --* **[REQUIRED]**

      The resource type.

    - **resourceId** *(string) --* **[REQUIRED]**

      The ID of the resource (for example., sg-xxxxxx).
    """


_ClientStartRemediationExecutionResponseFailedItemsTypeDef = TypedDict(
    "_ClientStartRemediationExecutionResponseFailedItemsTypeDef",
    {"resourceType": str, "resourceId": str},
    total=False,
)


class ClientStartRemediationExecutionResponseFailedItemsTypeDef(
    _ClientStartRemediationExecutionResponseFailedItemsTypeDef
):
    """
    Type definition for `ClientStartRemediationExecutionResponse` `FailedItems`

    The details that identify a resource within AWS Config, including the resource type and
    resource ID.

    - **resourceType** *(string) --*

      The resource type.

    - **resourceId** *(string) --*

      The ID of the resource (for example., sg-xxxxxx).
    """


_ClientStartRemediationExecutionResponseTypeDef = TypedDict(
    "_ClientStartRemediationExecutionResponseTypeDef",
    {
        "FailureMessage": str,
        "FailedItems": List[ClientStartRemediationExecutionResponseFailedItemsTypeDef],
    },
    total=False,
)


class ClientStartRemediationExecutionResponseTypeDef(
    _ClientStartRemediationExecutionResponseTypeDef
):
    """
    Type definition for `ClientStartRemediationExecution` `Response`

    - **FailureMessage** *(string) --*

      Returns a failure message. For example, the resource is already compliant.

    - **FailedItems** *(list) --*

      For resources that have failed to start execution, the API returns a resource key object.

      - *(dict) --*

        The details that identify a resource within AWS Config, including the resource type and
        resource ID.

        - **resourceType** *(string) --*

          The resource type.

        - **resourceId** *(string) --*

          The ID of the resource (for example., sg-xxxxxx).
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    Type definition for `ClientTagResource` `Tags`

    The tags for the resource. The metadata that you apply to a resource to help you categorize and
    organize them. Each tag consists of a key and an optional value, both of which you define. Tag
    keys can have a maximum character length of 128 characters, and tag values can have a maximum
    length of 256 characters.

    - **Key** *(string) --*

      One part of a key-value pair that make up a tag. A key is a general label that acts like a
      category for more specific tag values.

    - **Value** *(string) --*

      The optional part of a key-value pair that make up a tag. A value acts as a descriptor within
      a tag category (key).
    """


_DescribeAggregateComplianceByConfigRulesPaginateFiltersTypeDef = TypedDict(
    "_DescribeAggregateComplianceByConfigRulesPaginateFiltersTypeDef",
    {"ConfigRuleName": str, "ComplianceType": str, "AccountId": str, "AwsRegion": str},
    total=False,
)


class DescribeAggregateComplianceByConfigRulesPaginateFiltersTypeDef(
    _DescribeAggregateComplianceByConfigRulesPaginateFiltersTypeDef
):
    """
    Type definition for `DescribeAggregateComplianceByConfigRulesPaginate` `Filters`

    Filters the results by ConfigRuleComplianceFilters object.

    - **ConfigRuleName** *(string) --*

      The name of the AWS Config rule.

    - **ComplianceType** *(string) --*

      The rule compliance status.

      For the ``ConfigRuleComplianceFilters`` data type, AWS Config supports only ``COMPLIANT`` and
      ``NON_COMPLIANT`` . AWS Config does not support the ``NOT_APPLICABLE`` and the
      ``INSUFFICIENT_DATA`` values.

    - **AccountId** *(string) --*

      The 12-digit account ID of the source account.

    - **AwsRegion** *(string) --*

      The source region where the data is aggregated.
    """


_DescribeAggregateComplianceByConfigRulesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeAggregateComplianceByConfigRulesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeAggregateComplianceByConfigRulesPaginatePaginationConfigTypeDef(
    _DescribeAggregateComplianceByConfigRulesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeAggregateComplianceByConfigRulesPaginate` `PaginationConfig`

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


_DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesComplianceComplianceContributorCountTypeDef = TypedDict(
    "_DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesComplianceComplianceContributorCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)


class DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesComplianceComplianceContributorCountTypeDef(
    _DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesComplianceComplianceContributorCountTypeDef
):
    """
    Type definition for `DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesCompliance` `ComplianceContributorCount`

    The number of AWS resources or AWS Config rules that cause a result of
    ``NON_COMPLIANT`` , up to a maximum number.

    - **CappedCount** *(integer) --*

      The number of AWS resources or AWS Config rules responsible for the current
      compliance of the item.

    - **CapExceeded** *(boolean) --*

      Indicates whether the maximum count is reached.
    """


_DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesComplianceTypeDef = TypedDict(
    "_DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesComplianceTypeDef",
    {
        "ComplianceType": str,
        "ComplianceContributorCount": DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesComplianceComplianceContributorCountTypeDef,
    },
    total=False,
)


class DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesComplianceTypeDef(
    _DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesComplianceTypeDef
):
    """
    Type definition for `DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRules` `Compliance`

    Indicates whether an AWS resource or AWS Config rule is compliant and provides the number
    of contributors that affect the compliance.

    - **ComplianceType** *(string) --*

      Indicates whether an AWS resource or AWS Config rule is compliant.

      A resource is compliant if it complies with all of the AWS Config rules that evaluate
      it. A resource is noncompliant if it does not comply with one or more of these rules.

      A rule is compliant if all of the resources that the rule evaluates comply with it. A
      rule is noncompliant if any of these resources do not comply.

      AWS Config returns the ``INSUFFICIENT_DATA`` value when no evaluation results are
      available for the AWS resource or AWS Config rule.

      For the ``Compliance`` data type, AWS Config supports only ``COMPLIANT`` ,
      ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` values. AWS Config does not support the
      ``NOT_APPLICABLE`` value for the ``Compliance`` data type.

    - **ComplianceContributorCount** *(dict) --*

      The number of AWS resources or AWS Config rules that cause a result of
      ``NON_COMPLIANT`` , up to a maximum number.

      - **CappedCount** *(integer) --*

        The number of AWS resources or AWS Config rules responsible for the current
        compliance of the item.

      - **CapExceeded** *(boolean) --*

        Indicates whether the maximum count is reached.
    """


_DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesTypeDef = TypedDict(
    "_DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesTypeDef",
    {
        "ConfigRuleName": str,
        "Compliance": DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesComplianceTypeDef,
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)


class DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesTypeDef(
    _DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesTypeDef
):
    """
    Type definition for `DescribeAggregateComplianceByConfigRulesPaginateResponse` `AggregateComplianceByConfigRules`

    Indicates whether an AWS Config rule is compliant based on account ID, region, compliance,
    and rule name.

    A rule is compliant if all of the resources that the rule evaluated comply with it. It is
    noncompliant if any of these resources do not comply.

    - **ConfigRuleName** *(string) --*

      The name of the AWS Config rule.

    - **Compliance** *(dict) --*

      Indicates whether an AWS resource or AWS Config rule is compliant and provides the number
      of contributors that affect the compliance.

      - **ComplianceType** *(string) --*

        Indicates whether an AWS resource or AWS Config rule is compliant.

        A resource is compliant if it complies with all of the AWS Config rules that evaluate
        it. A resource is noncompliant if it does not comply with one or more of these rules.

        A rule is compliant if all of the resources that the rule evaluates comply with it. A
        rule is noncompliant if any of these resources do not comply.

        AWS Config returns the ``INSUFFICIENT_DATA`` value when no evaluation results are
        available for the AWS resource or AWS Config rule.

        For the ``Compliance`` data type, AWS Config supports only ``COMPLIANT`` ,
        ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` values. AWS Config does not support the
        ``NOT_APPLICABLE`` value for the ``Compliance`` data type.

      - **ComplianceContributorCount** *(dict) --*

        The number of AWS resources or AWS Config rules that cause a result of
        ``NON_COMPLIANT`` , up to a maximum number.

        - **CappedCount** *(integer) --*

          The number of AWS resources or AWS Config rules responsible for the current
          compliance of the item.

        - **CapExceeded** *(boolean) --*

          Indicates whether the maximum count is reached.

    - **AccountId** *(string) --*

      The 12-digit account ID of the source account.

    - **AwsRegion** *(string) --*

      The source region from where the data is aggregated.
    """


_DescribeAggregateComplianceByConfigRulesPaginateResponseTypeDef = TypedDict(
    "_DescribeAggregateComplianceByConfigRulesPaginateResponseTypeDef",
    {
        "AggregateComplianceByConfigRules": List[
            DescribeAggregateComplianceByConfigRulesPaginateResponseAggregateComplianceByConfigRulesTypeDef
        ]
    },
    total=False,
)


class DescribeAggregateComplianceByConfigRulesPaginateResponseTypeDef(
    _DescribeAggregateComplianceByConfigRulesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeAggregateComplianceByConfigRulesPaginate` `Response`

    - **AggregateComplianceByConfigRules** *(list) --*

      Returns a list of AggregateComplianceByConfigRule object.

      - *(dict) --*

        Indicates whether an AWS Config rule is compliant based on account ID, region, compliance,
        and rule name.

        A rule is compliant if all of the resources that the rule evaluated comply with it. It is
        noncompliant if any of these resources do not comply.

        - **ConfigRuleName** *(string) --*

          The name of the AWS Config rule.

        - **Compliance** *(dict) --*

          Indicates whether an AWS resource or AWS Config rule is compliant and provides the number
          of contributors that affect the compliance.

          - **ComplianceType** *(string) --*

            Indicates whether an AWS resource or AWS Config rule is compliant.

            A resource is compliant if it complies with all of the AWS Config rules that evaluate
            it. A resource is noncompliant if it does not comply with one or more of these rules.

            A rule is compliant if all of the resources that the rule evaluates comply with it. A
            rule is noncompliant if any of these resources do not comply.

            AWS Config returns the ``INSUFFICIENT_DATA`` value when no evaluation results are
            available for the AWS resource or AWS Config rule.

            For the ``Compliance`` data type, AWS Config supports only ``COMPLIANT`` ,
            ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` values. AWS Config does not support the
            ``NOT_APPLICABLE`` value for the ``Compliance`` data type.

          - **ComplianceContributorCount** *(dict) --*

            The number of AWS resources or AWS Config rules that cause a result of
            ``NON_COMPLIANT`` , up to a maximum number.

            - **CappedCount** *(integer) --*

              The number of AWS resources or AWS Config rules responsible for the current
              compliance of the item.

            - **CapExceeded** *(boolean) --*

              Indicates whether the maximum count is reached.

        - **AccountId** *(string) --*

          The 12-digit account ID of the source account.

        - **AwsRegion** *(string) --*

          The source region from where the data is aggregated.
    """


_DescribeAggregationAuthorizationsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeAggregationAuthorizationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeAggregationAuthorizationsPaginatePaginationConfigTypeDef(
    _DescribeAggregationAuthorizationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeAggregationAuthorizationsPaginate` `PaginationConfig`

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


_DescribeAggregationAuthorizationsPaginateResponseAggregationAuthorizationsTypeDef = TypedDict(
    "_DescribeAggregationAuthorizationsPaginateResponseAggregationAuthorizationsTypeDef",
    {
        "AggregationAuthorizationArn": str,
        "AuthorizedAccountId": str,
        "AuthorizedAwsRegion": str,
        "CreationTime": datetime,
    },
    total=False,
)


class DescribeAggregationAuthorizationsPaginateResponseAggregationAuthorizationsTypeDef(
    _DescribeAggregationAuthorizationsPaginateResponseAggregationAuthorizationsTypeDef
):
    """
    Type definition for `DescribeAggregationAuthorizationsPaginateResponse` `AggregationAuthorizations`

    An object that represents the authorizations granted to aggregator accounts and regions.

    - **AggregationAuthorizationArn** *(string) --*

      The Amazon Resource Name (ARN) of the aggregation object.

    - **AuthorizedAccountId** *(string) --*

      The 12-digit account ID of the account authorized to aggregate data.

    - **AuthorizedAwsRegion** *(string) --*

      The region authorized to collect aggregated data.

    - **CreationTime** *(datetime) --*

      The time stamp when the aggregation authorization was created.
    """


_DescribeAggregationAuthorizationsPaginateResponseTypeDef = TypedDict(
    "_DescribeAggregationAuthorizationsPaginateResponseTypeDef",
    {
        "AggregationAuthorizations": List[
            DescribeAggregationAuthorizationsPaginateResponseAggregationAuthorizationsTypeDef
        ]
    },
    total=False,
)


class DescribeAggregationAuthorizationsPaginateResponseTypeDef(
    _DescribeAggregationAuthorizationsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeAggregationAuthorizationsPaginate` `Response`

    - **AggregationAuthorizations** *(list) --*

      Returns a list of authorizations granted to various aggregator accounts and regions.

      - *(dict) --*

        An object that represents the authorizations granted to aggregator accounts and regions.

        - **AggregationAuthorizationArn** *(string) --*

          The Amazon Resource Name (ARN) of the aggregation object.

        - **AuthorizedAccountId** *(string) --*

          The 12-digit account ID of the account authorized to aggregate data.

        - **AuthorizedAwsRegion** *(string) --*

          The region authorized to collect aggregated data.

        - **CreationTime** *(datetime) --*

          The time stamp when the aggregation authorization was created.
    """


_DescribeComplianceByConfigRulePaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeComplianceByConfigRulePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class DescribeComplianceByConfigRulePaginatePaginationConfigTypeDef(
    _DescribeComplianceByConfigRulePaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeComplianceByConfigRulePaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesComplianceComplianceContributorCountTypeDef = TypedDict(
    "_DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesComplianceComplianceContributorCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)


class DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesComplianceComplianceContributorCountTypeDef(
    _DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesComplianceComplianceContributorCountTypeDef
):
    """
    Type definition for `DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesCompliance` `ComplianceContributorCount`

    The number of AWS resources or AWS Config rules that cause a result of
    ``NON_COMPLIANT`` , up to a maximum number.

    - **CappedCount** *(integer) --*

      The number of AWS resources or AWS Config rules responsible for the current
      compliance of the item.

    - **CapExceeded** *(boolean) --*

      Indicates whether the maximum count is reached.
    """


_DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesComplianceTypeDef = TypedDict(
    "_DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesComplianceTypeDef",
    {
        "ComplianceType": str,
        "ComplianceContributorCount": DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesComplianceComplianceContributorCountTypeDef,
    },
    total=False,
)


class DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesComplianceTypeDef(
    _DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesComplianceTypeDef
):
    """
    Type definition for `DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRules` `Compliance`

    Indicates whether the AWS Config rule is compliant.

    - **ComplianceType** *(string) --*

      Indicates whether an AWS resource or AWS Config rule is compliant.

      A resource is compliant if it complies with all of the AWS Config rules that evaluate
      it. A resource is noncompliant if it does not comply with one or more of these rules.

      A rule is compliant if all of the resources that the rule evaluates comply with it. A
      rule is noncompliant if any of these resources do not comply.

      AWS Config returns the ``INSUFFICIENT_DATA`` value when no evaluation results are
      available for the AWS resource or AWS Config rule.

      For the ``Compliance`` data type, AWS Config supports only ``COMPLIANT`` ,
      ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` values. AWS Config does not support the
      ``NOT_APPLICABLE`` value for the ``Compliance`` data type.

    - **ComplianceContributorCount** *(dict) --*

      The number of AWS resources or AWS Config rules that cause a result of
      ``NON_COMPLIANT`` , up to a maximum number.

      - **CappedCount** *(integer) --*

        The number of AWS resources or AWS Config rules responsible for the current
        compliance of the item.

      - **CapExceeded** *(boolean) --*

        Indicates whether the maximum count is reached.
    """


_DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesTypeDef = TypedDict(
    "_DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesTypeDef",
    {
        "ConfigRuleName": str,
        "Compliance": DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesComplianceTypeDef,
    },
    total=False,
)


class DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesTypeDef(
    _DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesTypeDef
):
    """
    Type definition for `DescribeComplianceByConfigRulePaginateResponse` `ComplianceByConfigRules`

    Indicates whether an AWS Config rule is compliant. A rule is compliant if all of the
    resources that the rule evaluated comply with it. A rule is noncompliant if any of these
    resources do not comply.

    - **ConfigRuleName** *(string) --*

      The name of the AWS Config rule.

    - **Compliance** *(dict) --*

      Indicates whether the AWS Config rule is compliant.

      - **ComplianceType** *(string) --*

        Indicates whether an AWS resource or AWS Config rule is compliant.

        A resource is compliant if it complies with all of the AWS Config rules that evaluate
        it. A resource is noncompliant if it does not comply with one or more of these rules.

        A rule is compliant if all of the resources that the rule evaluates comply with it. A
        rule is noncompliant if any of these resources do not comply.

        AWS Config returns the ``INSUFFICIENT_DATA`` value when no evaluation results are
        available for the AWS resource or AWS Config rule.

        For the ``Compliance`` data type, AWS Config supports only ``COMPLIANT`` ,
        ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` values. AWS Config does not support the
        ``NOT_APPLICABLE`` value for the ``Compliance`` data type.

      - **ComplianceContributorCount** *(dict) --*

        The number of AWS resources or AWS Config rules that cause a result of
        ``NON_COMPLIANT`` , up to a maximum number.

        - **CappedCount** *(integer) --*

          The number of AWS resources or AWS Config rules responsible for the current
          compliance of the item.

        - **CapExceeded** *(boolean) --*

          Indicates whether the maximum count is reached.
    """


_DescribeComplianceByConfigRulePaginateResponseTypeDef = TypedDict(
    "_DescribeComplianceByConfigRulePaginateResponseTypeDef",
    {
        "ComplianceByConfigRules": List[
            DescribeComplianceByConfigRulePaginateResponseComplianceByConfigRulesTypeDef
        ]
    },
    total=False,
)


class DescribeComplianceByConfigRulePaginateResponseTypeDef(
    _DescribeComplianceByConfigRulePaginateResponseTypeDef
):
    """
    Type definition for `DescribeComplianceByConfigRulePaginate` `Response`

    - **ComplianceByConfigRules** *(list) --*

      Indicates whether each of the specified AWS Config rules is compliant.

      - *(dict) --*

        Indicates whether an AWS Config rule is compliant. A rule is compliant if all of the
        resources that the rule evaluated comply with it. A rule is noncompliant if any of these
        resources do not comply.

        - **ConfigRuleName** *(string) --*

          The name of the AWS Config rule.

        - **Compliance** *(dict) --*

          Indicates whether the AWS Config rule is compliant.

          - **ComplianceType** *(string) --*

            Indicates whether an AWS resource or AWS Config rule is compliant.

            A resource is compliant if it complies with all of the AWS Config rules that evaluate
            it. A resource is noncompliant if it does not comply with one or more of these rules.

            A rule is compliant if all of the resources that the rule evaluates comply with it. A
            rule is noncompliant if any of these resources do not comply.

            AWS Config returns the ``INSUFFICIENT_DATA`` value when no evaluation results are
            available for the AWS resource or AWS Config rule.

            For the ``Compliance`` data type, AWS Config supports only ``COMPLIANT`` ,
            ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` values. AWS Config does not support the
            ``NOT_APPLICABLE`` value for the ``Compliance`` data type.

          - **ComplianceContributorCount** *(dict) --*

            The number of AWS resources or AWS Config rules that cause a result of
            ``NON_COMPLIANT`` , up to a maximum number.

            - **CappedCount** *(integer) --*

              The number of AWS resources or AWS Config rules responsible for the current
              compliance of the item.

            - **CapExceeded** *(boolean) --*

              Indicates whether the maximum count is reached.
    """


_DescribeComplianceByResourcePaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeComplianceByResourcePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class DescribeComplianceByResourcePaginatePaginationConfigTypeDef(
    _DescribeComplianceByResourcePaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeComplianceByResourcePaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeComplianceByResourcePaginateResponseComplianceByResourcesComplianceComplianceContributorCountTypeDef = TypedDict(
    "_DescribeComplianceByResourcePaginateResponseComplianceByResourcesComplianceComplianceContributorCountTypeDef",
    {"CappedCount": int, "CapExceeded": bool},
    total=False,
)


class DescribeComplianceByResourcePaginateResponseComplianceByResourcesComplianceComplianceContributorCountTypeDef(
    _DescribeComplianceByResourcePaginateResponseComplianceByResourcesComplianceComplianceContributorCountTypeDef
):
    """
    Type definition for `DescribeComplianceByResourcePaginateResponseComplianceByResourcesCompliance` `ComplianceContributorCount`

    The number of AWS resources or AWS Config rules that cause a result of
    ``NON_COMPLIANT`` , up to a maximum number.

    - **CappedCount** *(integer) --*

      The number of AWS resources or AWS Config rules responsible for the current
      compliance of the item.

    - **CapExceeded** *(boolean) --*

      Indicates whether the maximum count is reached.
    """


_DescribeComplianceByResourcePaginateResponseComplianceByResourcesComplianceTypeDef = TypedDict(
    "_DescribeComplianceByResourcePaginateResponseComplianceByResourcesComplianceTypeDef",
    {
        "ComplianceType": str,
        "ComplianceContributorCount": DescribeComplianceByResourcePaginateResponseComplianceByResourcesComplianceComplianceContributorCountTypeDef,
    },
    total=False,
)


class DescribeComplianceByResourcePaginateResponseComplianceByResourcesComplianceTypeDef(
    _DescribeComplianceByResourcePaginateResponseComplianceByResourcesComplianceTypeDef
):
    """
    Type definition for `DescribeComplianceByResourcePaginateResponseComplianceByResources` `Compliance`

    Indicates whether the AWS resource complies with all of the AWS Config rules that
    evaluated it.

    - **ComplianceType** *(string) --*

      Indicates whether an AWS resource or AWS Config rule is compliant.

      A resource is compliant if it complies with all of the AWS Config rules that evaluate
      it. A resource is noncompliant if it does not comply with one or more of these rules.

      A rule is compliant if all of the resources that the rule evaluates comply with it. A
      rule is noncompliant if any of these resources do not comply.

      AWS Config returns the ``INSUFFICIENT_DATA`` value when no evaluation results are
      available for the AWS resource or AWS Config rule.

      For the ``Compliance`` data type, AWS Config supports only ``COMPLIANT`` ,
      ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` values. AWS Config does not support the
      ``NOT_APPLICABLE`` value for the ``Compliance`` data type.

    - **ComplianceContributorCount** *(dict) --*

      The number of AWS resources or AWS Config rules that cause a result of
      ``NON_COMPLIANT`` , up to a maximum number.

      - **CappedCount** *(integer) --*

        The number of AWS resources or AWS Config rules responsible for the current
        compliance of the item.

      - **CapExceeded** *(boolean) --*

        Indicates whether the maximum count is reached.
    """


_DescribeComplianceByResourcePaginateResponseComplianceByResourcesTypeDef = TypedDict(
    "_DescribeComplianceByResourcePaginateResponseComplianceByResourcesTypeDef",
    {
        "ResourceType": str,
        "ResourceId": str,
        "Compliance": DescribeComplianceByResourcePaginateResponseComplianceByResourcesComplianceTypeDef,
    },
    total=False,
)


class DescribeComplianceByResourcePaginateResponseComplianceByResourcesTypeDef(
    _DescribeComplianceByResourcePaginateResponseComplianceByResourcesTypeDef
):
    """
    Type definition for `DescribeComplianceByResourcePaginateResponse` `ComplianceByResources`

    Indicates whether an AWS resource that is evaluated according to one or more AWS Config
    rules is compliant. A resource is compliant if it complies with all of the rules that
    evaluate it. A resource is noncompliant if it does not comply with one or more of these
    rules.

    - **ResourceType** *(string) --*

      The type of the AWS resource that was evaluated.

    - **ResourceId** *(string) --*

      The ID of the AWS resource that was evaluated.

    - **Compliance** *(dict) --*

      Indicates whether the AWS resource complies with all of the AWS Config rules that
      evaluated it.

      - **ComplianceType** *(string) --*

        Indicates whether an AWS resource or AWS Config rule is compliant.

        A resource is compliant if it complies with all of the AWS Config rules that evaluate
        it. A resource is noncompliant if it does not comply with one or more of these rules.

        A rule is compliant if all of the resources that the rule evaluates comply with it. A
        rule is noncompliant if any of these resources do not comply.

        AWS Config returns the ``INSUFFICIENT_DATA`` value when no evaluation results are
        available for the AWS resource or AWS Config rule.

        For the ``Compliance`` data type, AWS Config supports only ``COMPLIANT`` ,
        ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` values. AWS Config does not support the
        ``NOT_APPLICABLE`` value for the ``Compliance`` data type.

      - **ComplianceContributorCount** *(dict) --*

        The number of AWS resources or AWS Config rules that cause a result of
        ``NON_COMPLIANT`` , up to a maximum number.

        - **CappedCount** *(integer) --*

          The number of AWS resources or AWS Config rules responsible for the current
          compliance of the item.

        - **CapExceeded** *(boolean) --*

          Indicates whether the maximum count is reached.
    """


_DescribeComplianceByResourcePaginateResponseTypeDef = TypedDict(
    "_DescribeComplianceByResourcePaginateResponseTypeDef",
    {
        "ComplianceByResources": List[
            DescribeComplianceByResourcePaginateResponseComplianceByResourcesTypeDef
        ]
    },
    total=False,
)


class DescribeComplianceByResourcePaginateResponseTypeDef(
    _DescribeComplianceByResourcePaginateResponseTypeDef
):
    """
    Type definition for `DescribeComplianceByResourcePaginate` `Response`

    - **ComplianceByResources** *(list) --*

      Indicates whether the specified AWS resource complies with all of the AWS Config rules that
      evaluate it.

      - *(dict) --*

        Indicates whether an AWS resource that is evaluated according to one or more AWS Config
        rules is compliant. A resource is compliant if it complies with all of the rules that
        evaluate it. A resource is noncompliant if it does not comply with one or more of these
        rules.

        - **ResourceType** *(string) --*

          The type of the AWS resource that was evaluated.

        - **ResourceId** *(string) --*

          The ID of the AWS resource that was evaluated.

        - **Compliance** *(dict) --*

          Indicates whether the AWS resource complies with all of the AWS Config rules that
          evaluated it.

          - **ComplianceType** *(string) --*

            Indicates whether an AWS resource or AWS Config rule is compliant.

            A resource is compliant if it complies with all of the AWS Config rules that evaluate
            it. A resource is noncompliant if it does not comply with one or more of these rules.

            A rule is compliant if all of the resources that the rule evaluates comply with it. A
            rule is noncompliant if any of these resources do not comply.

            AWS Config returns the ``INSUFFICIENT_DATA`` value when no evaluation results are
            available for the AWS resource or AWS Config rule.

            For the ``Compliance`` data type, AWS Config supports only ``COMPLIANT`` ,
            ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` values. AWS Config does not support the
            ``NOT_APPLICABLE`` value for the ``Compliance`` data type.

          - **ComplianceContributorCount** *(dict) --*

            The number of AWS resources or AWS Config rules that cause a result of
            ``NON_COMPLIANT`` , up to a maximum number.

            - **CappedCount** *(integer) --*

              The number of AWS resources or AWS Config rules responsible for the current
              compliance of the item.

            - **CapExceeded** *(boolean) --*

              Indicates whether the maximum count is reached.
    """


_DescribeConfigRuleEvaluationStatusPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeConfigRuleEvaluationStatusPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeConfigRuleEvaluationStatusPaginatePaginationConfigTypeDef(
    _DescribeConfigRuleEvaluationStatusPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeConfigRuleEvaluationStatusPaginate` `PaginationConfig`

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


_DescribeConfigRuleEvaluationStatusPaginateResponseConfigRulesEvaluationStatusTypeDef = TypedDict(
    "_DescribeConfigRuleEvaluationStatusPaginateResponseConfigRulesEvaluationStatusTypeDef",
    {
        "ConfigRuleName": str,
        "ConfigRuleArn": str,
        "ConfigRuleId": str,
        "LastSuccessfulInvocationTime": datetime,
        "LastFailedInvocationTime": datetime,
        "LastSuccessfulEvaluationTime": datetime,
        "LastFailedEvaluationTime": datetime,
        "FirstActivatedTime": datetime,
        "LastErrorCode": str,
        "LastErrorMessage": str,
        "FirstEvaluationStarted": bool,
    },
    total=False,
)


class DescribeConfigRuleEvaluationStatusPaginateResponseConfigRulesEvaluationStatusTypeDef(
    _DescribeConfigRuleEvaluationStatusPaginateResponseConfigRulesEvaluationStatusTypeDef
):
    """
    Type definition for `DescribeConfigRuleEvaluationStatusPaginateResponse` `ConfigRulesEvaluationStatus`

    Status information for your AWS managed Config rules. The status includes information such
    as the last time the rule ran, the last time it failed, and the related error for the last
    failure.

    This action does not return status information about custom AWS Config rules.

    - **ConfigRuleName** *(string) --*

      The name of the AWS Config rule.

    - **ConfigRuleArn** *(string) --*

      The Amazon Resource Name (ARN) of the AWS Config rule.

    - **ConfigRuleId** *(string) --*

      The ID of the AWS Config rule.

    - **LastSuccessfulInvocationTime** *(datetime) --*

      The time that AWS Config last successfully invoked the AWS Config rule to evaluate your
      AWS resources.

    - **LastFailedInvocationTime** *(datetime) --*

      The time that AWS Config last failed to invoke the AWS Config rule to evaluate your AWS
      resources.

    - **LastSuccessfulEvaluationTime** *(datetime) --*

      The time that AWS Config last successfully evaluated your AWS resources against the rule.

    - **LastFailedEvaluationTime** *(datetime) --*

      The time that AWS Config last failed to evaluate your AWS resources against the rule.

    - **FirstActivatedTime** *(datetime) --*

      The time that you first activated the AWS Config rule.

    - **LastErrorCode** *(string) --*

      The error code that AWS Config returned when the rule last failed.

    - **LastErrorMessage** *(string) --*

      The error message that AWS Config returned when the rule last failed.

    - **FirstEvaluationStarted** *(boolean) --*

      Indicates whether AWS Config has evaluated your resources against the rule at least once.

      * ``true`` - AWS Config has evaluated your AWS resources against the rule at least once.

      * ``false`` - AWS Config has not once finished evaluating your AWS resources against the
      rule.
    """


_DescribeConfigRuleEvaluationStatusPaginateResponseTypeDef = TypedDict(
    "_DescribeConfigRuleEvaluationStatusPaginateResponseTypeDef",
    {
        "ConfigRulesEvaluationStatus": List[
            DescribeConfigRuleEvaluationStatusPaginateResponseConfigRulesEvaluationStatusTypeDef
        ]
    },
    total=False,
)


class DescribeConfigRuleEvaluationStatusPaginateResponseTypeDef(
    _DescribeConfigRuleEvaluationStatusPaginateResponseTypeDef
):
    """
    Type definition for `DescribeConfigRuleEvaluationStatusPaginate` `Response`

    - **ConfigRulesEvaluationStatus** *(list) --*

      Status information about your AWS managed Config rules.

      - *(dict) --*

        Status information for your AWS managed Config rules. The status includes information such
        as the last time the rule ran, the last time it failed, and the related error for the last
        failure.

        This action does not return status information about custom AWS Config rules.

        - **ConfigRuleName** *(string) --*

          The name of the AWS Config rule.

        - **ConfigRuleArn** *(string) --*

          The Amazon Resource Name (ARN) of the AWS Config rule.

        - **ConfigRuleId** *(string) --*

          The ID of the AWS Config rule.

        - **LastSuccessfulInvocationTime** *(datetime) --*

          The time that AWS Config last successfully invoked the AWS Config rule to evaluate your
          AWS resources.

        - **LastFailedInvocationTime** *(datetime) --*

          The time that AWS Config last failed to invoke the AWS Config rule to evaluate your AWS
          resources.

        - **LastSuccessfulEvaluationTime** *(datetime) --*

          The time that AWS Config last successfully evaluated your AWS resources against the rule.

        - **LastFailedEvaluationTime** *(datetime) --*

          The time that AWS Config last failed to evaluate your AWS resources against the rule.

        - **FirstActivatedTime** *(datetime) --*

          The time that you first activated the AWS Config rule.

        - **LastErrorCode** *(string) --*

          The error code that AWS Config returned when the rule last failed.

        - **LastErrorMessage** *(string) --*

          The error message that AWS Config returned when the rule last failed.

        - **FirstEvaluationStarted** *(boolean) --*

          Indicates whether AWS Config has evaluated your resources against the rule at least once.

          * ``true`` - AWS Config has evaluated your AWS resources against the rule at least once.

          * ``false`` - AWS Config has not once finished evaluating your AWS resources against the
          rule.
    """


_DescribeConfigRulesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeConfigRulesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class DescribeConfigRulesPaginatePaginationConfigTypeDef(
    _DescribeConfigRulesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeConfigRulesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeConfigRulesPaginateResponseConfigRulesScopeTypeDef = TypedDict(
    "_DescribeConfigRulesPaginateResponseConfigRulesScopeTypeDef",
    {
        "ComplianceResourceTypes": List[str],
        "TagKey": str,
        "TagValue": str,
        "ComplianceResourceId": str,
    },
    total=False,
)


class DescribeConfigRulesPaginateResponseConfigRulesScopeTypeDef(
    _DescribeConfigRulesPaginateResponseConfigRulesScopeTypeDef
):
    """
    Type definition for `DescribeConfigRulesPaginateResponseConfigRules` `Scope`

    Defines which resources can trigger an evaluation for the rule. The scope can include one
    or more resource types, a combination of one resource type and one resource ID, or a
    combination of a tag key and value. Specify a scope to constrain the resources that can
    trigger an evaluation for the rule. If you do not specify a scope, evaluations are
    triggered when any resource in the recording group changes.

    - **ComplianceResourceTypes** *(list) --*

      The resource types of only those AWS resources that you want to trigger an evaluation
      for the rule. You can only specify one type if you also specify a resource ID for
      ``ComplianceResourceId`` .

      - *(string) --*

    - **TagKey** *(string) --*

      The tag key that is applied to only those AWS resources that you want to trigger an
      evaluation for the rule.

    - **TagValue** *(string) --*

      The tag value applied to only those AWS resources that you want to trigger an
      evaluation for the rule. If you specify a value for ``TagValue`` , you must also
      specify a value for ``TagKey`` .

    - **ComplianceResourceId** *(string) --*

      The ID of the only AWS resource that you want to trigger an evaluation for the rule. If
      you specify a resource ID, you must specify one resource type for
      ``ComplianceResourceTypes`` .
    """


_DescribeConfigRulesPaginateResponseConfigRulesSourceSourceDetailsTypeDef = TypedDict(
    "_DescribeConfigRulesPaginateResponseConfigRulesSourceSourceDetailsTypeDef",
    {"EventSource": str, "MessageType": str, "MaximumExecutionFrequency": str},
    total=False,
)


class DescribeConfigRulesPaginateResponseConfigRulesSourceSourceDetailsTypeDef(
    _DescribeConfigRulesPaginateResponseConfigRulesSourceSourceDetailsTypeDef
):
    """
    Type definition for `DescribeConfigRulesPaginateResponseConfigRulesSource` `SourceDetails`

    Provides the source and the message types that trigger AWS Config to evaluate your
    AWS resources against a rule. It also provides the frequency with which you want AWS
    Config to run evaluations for the rule if the trigger type is periodic. You can
    specify the parameter values for ``SourceDetail`` only for custom rules.

    - **EventSource** *(string) --*

      The source of the event, such as an AWS service, that triggers AWS Config to
      evaluate your AWS resources.

    - **MessageType** *(string) --*

      The type of notification that triggers AWS Config to run an evaluation for a rule.
      You can specify the following notification types:

      * ``ConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config
      delivers a configuration item as a result of a resource change.

      * ``OversizedConfigurationItemChangeNotification`` - Triggers an evaluation when
      AWS Config delivers an oversized configuration item. AWS Config may generate this
      notification type when a resource changes and the notification exceeds the maximum
      size allowed by Amazon SNS.

      * ``ScheduledNotification`` - Triggers a periodic evaluation at the frequency
      specified for ``MaximumExecutionFrequency`` .

      * ``ConfigurationSnapshotDeliveryCompleted`` - Triggers a periodic evaluation when
      AWS Config delivers a configuration snapshot.

      If you want your custom rule to be triggered by configuration changes, specify two
      SourceDetail objects, one for ``ConfigurationItemChangeNotification`` and one for
      ``OversizedConfigurationItemChangeNotification`` .

    - **MaximumExecutionFrequency** *(string) --*

      The frequency at which you want AWS Config to run evaluations for a custom rule
      with a periodic trigger. If you specify a value for ``MaximumExecutionFrequency`` ,
      then ``MessageType`` must use the ``ScheduledNotification`` value.

      .. note::

        By default, rules with a periodic trigger are evaluated every 24 hours. To change
        the frequency, specify a valid value for the ``MaximumExecutionFrequency``
        parameter.

        Based on the valid value you choose, AWS Config runs evaluations once for each
        valid value. For example, if you choose ``Three_Hours`` , AWS Config runs
        evaluations once every three hours. In this case, ``Three_Hours`` is the
        frequency of this rule.
    """


_DescribeConfigRulesPaginateResponseConfigRulesSourceTypeDef = TypedDict(
    "_DescribeConfigRulesPaginateResponseConfigRulesSourceTypeDef",
    {
        "Owner": str,
        "SourceIdentifier": str,
        "SourceDetails": List[
            DescribeConfigRulesPaginateResponseConfigRulesSourceSourceDetailsTypeDef
        ],
    },
    total=False,
)


class DescribeConfigRulesPaginateResponseConfigRulesSourceTypeDef(
    _DescribeConfigRulesPaginateResponseConfigRulesSourceTypeDef
):
    """
    Type definition for `DescribeConfigRulesPaginateResponseConfigRules` `Source`

    Provides the rule owner (AWS or customer), the rule identifier, and the notifications
    that cause the function to evaluate your AWS resources.

    - **Owner** *(string) --*

      Indicates whether AWS or the customer owns and manages the AWS Config rule.

    - **SourceIdentifier** *(string) --*

      For AWS Config managed rules, a predefined identifier from a list. For example,
      ``IAM_PASSWORD_POLICY`` is a managed rule. To reference a managed rule, see `Using AWS
      Managed Config Rules
      <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html>`__
      .

      For custom rules, the identifier is the Amazon Resource Name (ARN) of the rule's AWS
      Lambda function, such as
      ``arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name`` .

    - **SourceDetails** *(list) --*

      Provides the source and type of the event that causes AWS Config to evaluate your AWS
      resources.

      - *(dict) --*

        Provides the source and the message types that trigger AWS Config to evaluate your
        AWS resources against a rule. It also provides the frequency with which you want AWS
        Config to run evaluations for the rule if the trigger type is periodic. You can
        specify the parameter values for ``SourceDetail`` only for custom rules.

        - **EventSource** *(string) --*

          The source of the event, such as an AWS service, that triggers AWS Config to
          evaluate your AWS resources.

        - **MessageType** *(string) --*

          The type of notification that triggers AWS Config to run an evaluation for a rule.
          You can specify the following notification types:

          * ``ConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config
          delivers a configuration item as a result of a resource change.

          * ``OversizedConfigurationItemChangeNotification`` - Triggers an evaluation when
          AWS Config delivers an oversized configuration item. AWS Config may generate this
          notification type when a resource changes and the notification exceeds the maximum
          size allowed by Amazon SNS.

          * ``ScheduledNotification`` - Triggers a periodic evaluation at the frequency
          specified for ``MaximumExecutionFrequency`` .

          * ``ConfigurationSnapshotDeliveryCompleted`` - Triggers a periodic evaluation when
          AWS Config delivers a configuration snapshot.

          If you want your custom rule to be triggered by configuration changes, specify two
          SourceDetail objects, one for ``ConfigurationItemChangeNotification`` and one for
          ``OversizedConfigurationItemChangeNotification`` .

        - **MaximumExecutionFrequency** *(string) --*

          The frequency at which you want AWS Config to run evaluations for a custom rule
          with a periodic trigger. If you specify a value for ``MaximumExecutionFrequency`` ,
          then ``MessageType`` must use the ``ScheduledNotification`` value.

          .. note::

            By default, rules with a periodic trigger are evaluated every 24 hours. To change
            the frequency, specify a valid value for the ``MaximumExecutionFrequency``
            parameter.

            Based on the valid value you choose, AWS Config runs evaluations once for each
            valid value. For example, if you choose ``Three_Hours`` , AWS Config runs
            evaluations once every three hours. In this case, ``Three_Hours`` is the
            frequency of this rule.
    """


_DescribeConfigRulesPaginateResponseConfigRulesTypeDef = TypedDict(
    "_DescribeConfigRulesPaginateResponseConfigRulesTypeDef",
    {
        "ConfigRuleName": str,
        "ConfigRuleArn": str,
        "ConfigRuleId": str,
        "Description": str,
        "Scope": DescribeConfigRulesPaginateResponseConfigRulesScopeTypeDef,
        "Source": DescribeConfigRulesPaginateResponseConfigRulesSourceTypeDef,
        "InputParameters": str,
        "MaximumExecutionFrequency": str,
        "ConfigRuleState": str,
        "CreatedBy": str,
    },
    total=False,
)


class DescribeConfigRulesPaginateResponseConfigRulesTypeDef(
    _DescribeConfigRulesPaginateResponseConfigRulesTypeDef
):
    """
    Type definition for `DescribeConfigRulesPaginateResponse` `ConfigRules`

    An AWS Config rule represents an AWS Lambda function that you create for a custom rule or a
    predefined function for an AWS managed rule. The function evaluates configuration items to
    assess whether your AWS resources comply with your desired configurations. This function
    can run when AWS Config detects a configuration change to an AWS resource and at a periodic
    frequency that you choose (for example, every 24 hours).

    .. note::

      You can use the AWS CLI and AWS SDKs if you want to create a rule that triggers
      evaluations for your resources when AWS Config delivers the configuration snapshot. For
      more information, see  ConfigSnapshotDeliveryProperties .

    For more information about developing and using AWS Config rules, see `Evaluating AWS
    Resource Configurations with AWS Config
    <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html>`__ in the
    *AWS Config Developer Guide* .

    - **ConfigRuleName** *(string) --*

      The name that you assign to the AWS Config rule. The name is required if you are adding a
      new rule.

    - **ConfigRuleArn** *(string) --*

      The Amazon Resource Name (ARN) of the AWS Config rule.

    - **ConfigRuleId** *(string) --*

      The ID of the AWS Config rule.

    - **Description** *(string) --*

      The description that you provide for the AWS Config rule.

    - **Scope** *(dict) --*

      Defines which resources can trigger an evaluation for the rule. The scope can include one
      or more resource types, a combination of one resource type and one resource ID, or a
      combination of a tag key and value. Specify a scope to constrain the resources that can
      trigger an evaluation for the rule. If you do not specify a scope, evaluations are
      triggered when any resource in the recording group changes.

      - **ComplianceResourceTypes** *(list) --*

        The resource types of only those AWS resources that you want to trigger an evaluation
        for the rule. You can only specify one type if you also specify a resource ID for
        ``ComplianceResourceId`` .

        - *(string) --*

      - **TagKey** *(string) --*

        The tag key that is applied to only those AWS resources that you want to trigger an
        evaluation for the rule.

      - **TagValue** *(string) --*

        The tag value applied to only those AWS resources that you want to trigger an
        evaluation for the rule. If you specify a value for ``TagValue`` , you must also
        specify a value for ``TagKey`` .

      - **ComplianceResourceId** *(string) --*

        The ID of the only AWS resource that you want to trigger an evaluation for the rule. If
        you specify a resource ID, you must specify one resource type for
        ``ComplianceResourceTypes`` .

    - **Source** *(dict) --*

      Provides the rule owner (AWS or customer), the rule identifier, and the notifications
      that cause the function to evaluate your AWS resources.

      - **Owner** *(string) --*

        Indicates whether AWS or the customer owns and manages the AWS Config rule.

      - **SourceIdentifier** *(string) --*

        For AWS Config managed rules, a predefined identifier from a list. For example,
        ``IAM_PASSWORD_POLICY`` is a managed rule. To reference a managed rule, see `Using AWS
        Managed Config Rules
        <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html>`__
        .

        For custom rules, the identifier is the Amazon Resource Name (ARN) of the rule's AWS
        Lambda function, such as
        ``arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name`` .

      - **SourceDetails** *(list) --*

        Provides the source and type of the event that causes AWS Config to evaluate your AWS
        resources.

        - *(dict) --*

          Provides the source and the message types that trigger AWS Config to evaluate your
          AWS resources against a rule. It also provides the frequency with which you want AWS
          Config to run evaluations for the rule if the trigger type is periodic. You can
          specify the parameter values for ``SourceDetail`` only for custom rules.

          - **EventSource** *(string) --*

            The source of the event, such as an AWS service, that triggers AWS Config to
            evaluate your AWS resources.

          - **MessageType** *(string) --*

            The type of notification that triggers AWS Config to run an evaluation for a rule.
            You can specify the following notification types:

            * ``ConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config
            delivers a configuration item as a result of a resource change.

            * ``OversizedConfigurationItemChangeNotification`` - Triggers an evaluation when
            AWS Config delivers an oversized configuration item. AWS Config may generate this
            notification type when a resource changes and the notification exceeds the maximum
            size allowed by Amazon SNS.

            * ``ScheduledNotification`` - Triggers a periodic evaluation at the frequency
            specified for ``MaximumExecutionFrequency`` .

            * ``ConfigurationSnapshotDeliveryCompleted`` - Triggers a periodic evaluation when
            AWS Config delivers a configuration snapshot.

            If you want your custom rule to be triggered by configuration changes, specify two
            SourceDetail objects, one for ``ConfigurationItemChangeNotification`` and one for
            ``OversizedConfigurationItemChangeNotification`` .

          - **MaximumExecutionFrequency** *(string) --*

            The frequency at which you want AWS Config to run evaluations for a custom rule
            with a periodic trigger. If you specify a value for ``MaximumExecutionFrequency`` ,
            then ``MessageType`` must use the ``ScheduledNotification`` value.

            .. note::

              By default, rules with a periodic trigger are evaluated every 24 hours. To change
              the frequency, specify a valid value for the ``MaximumExecutionFrequency``
              parameter.

              Based on the valid value you choose, AWS Config runs evaluations once for each
              valid value. For example, if you choose ``Three_Hours`` , AWS Config runs
              evaluations once every three hours. In this case, ``Three_Hours`` is the
              frequency of this rule.

    - **InputParameters** *(string) --*

      A string, in JSON format, that is passed to the AWS Config rule Lambda function.

    - **MaximumExecutionFrequency** *(string) --*

      The maximum frequency with which AWS Config runs evaluations for a rule. You can specify
      a value for ``MaximumExecutionFrequency`` when:

      * You are using an AWS managed rule that is triggered at a periodic frequency.

      * Your custom rule is triggered when AWS Config delivers the configuration snapshot. For
      more information, see  ConfigSnapshotDeliveryProperties .

      .. note::

        By default, rules with a periodic trigger are evaluated every 24 hours. To change the
        frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.

    - **ConfigRuleState** *(string) --*

      Indicates whether the AWS Config rule is active or is currently being deleted by AWS
      Config. It can also indicate the evaluation status for the AWS Config rule.

      AWS Config sets the state of the rule to ``EVALUATING`` temporarily after you use the
      ``StartConfigRulesEvaluation`` request to evaluate your resources against the AWS Config
      rule.

      AWS Config sets the state of the rule to ``DELETING_RESULTS`` temporarily after you use
      the ``DeleteEvaluationResults`` request to delete the current evaluation results for the
      AWS Config rule.

      AWS Config temporarily sets the state of a rule to ``DELETING`` after you use the
      ``DeleteConfigRule`` request to delete the rule. After AWS Config deletes the rule, the
      rule and all of its evaluations are erased and are no longer available.

    - **CreatedBy** *(string) --*

      Service principal name of the service that created the rule.

      .. note::

        The field is populated only if the service linked rule is created by a service. The
        field is empty if you create your own rule.
    """


_DescribeConfigRulesPaginateResponseTypeDef = TypedDict(
    "_DescribeConfigRulesPaginateResponseTypeDef",
    {"ConfigRules": List[DescribeConfigRulesPaginateResponseConfigRulesTypeDef]},
    total=False,
)


class DescribeConfigRulesPaginateResponseTypeDef(
    _DescribeConfigRulesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeConfigRulesPaginate` `Response`

    - **ConfigRules** *(list) --*

      The details about your AWS Config rules.

      - *(dict) --*

        An AWS Config rule represents an AWS Lambda function that you create for a custom rule or a
        predefined function for an AWS managed rule. The function evaluates configuration items to
        assess whether your AWS resources comply with your desired configurations. This function
        can run when AWS Config detects a configuration change to an AWS resource and at a periodic
        frequency that you choose (for example, every 24 hours).

        .. note::

          You can use the AWS CLI and AWS SDKs if you want to create a rule that triggers
          evaluations for your resources when AWS Config delivers the configuration snapshot. For
          more information, see  ConfigSnapshotDeliveryProperties .

        For more information about developing and using AWS Config rules, see `Evaluating AWS
        Resource Configurations with AWS Config
        <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html>`__ in the
        *AWS Config Developer Guide* .

        - **ConfigRuleName** *(string) --*

          The name that you assign to the AWS Config rule. The name is required if you are adding a
          new rule.

        - **ConfigRuleArn** *(string) --*

          The Amazon Resource Name (ARN) of the AWS Config rule.

        - **ConfigRuleId** *(string) --*

          The ID of the AWS Config rule.

        - **Description** *(string) --*

          The description that you provide for the AWS Config rule.

        - **Scope** *(dict) --*

          Defines which resources can trigger an evaluation for the rule. The scope can include one
          or more resource types, a combination of one resource type and one resource ID, or a
          combination of a tag key and value. Specify a scope to constrain the resources that can
          trigger an evaluation for the rule. If you do not specify a scope, evaluations are
          triggered when any resource in the recording group changes.

          - **ComplianceResourceTypes** *(list) --*

            The resource types of only those AWS resources that you want to trigger an evaluation
            for the rule. You can only specify one type if you also specify a resource ID for
            ``ComplianceResourceId`` .

            - *(string) --*

          - **TagKey** *(string) --*

            The tag key that is applied to only those AWS resources that you want to trigger an
            evaluation for the rule.

          - **TagValue** *(string) --*

            The tag value applied to only those AWS resources that you want to trigger an
            evaluation for the rule. If you specify a value for ``TagValue`` , you must also
            specify a value for ``TagKey`` .

          - **ComplianceResourceId** *(string) --*

            The ID of the only AWS resource that you want to trigger an evaluation for the rule. If
            you specify a resource ID, you must specify one resource type for
            ``ComplianceResourceTypes`` .

        - **Source** *(dict) --*

          Provides the rule owner (AWS or customer), the rule identifier, and the notifications
          that cause the function to evaluate your AWS resources.

          - **Owner** *(string) --*

            Indicates whether AWS or the customer owns and manages the AWS Config rule.

          - **SourceIdentifier** *(string) --*

            For AWS Config managed rules, a predefined identifier from a list. For example,
            ``IAM_PASSWORD_POLICY`` is a managed rule. To reference a managed rule, see `Using AWS
            Managed Config Rules
            <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html>`__
            .

            For custom rules, the identifier is the Amazon Resource Name (ARN) of the rule's AWS
            Lambda function, such as
            ``arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name`` .

          - **SourceDetails** *(list) --*

            Provides the source and type of the event that causes AWS Config to evaluate your AWS
            resources.

            - *(dict) --*

              Provides the source and the message types that trigger AWS Config to evaluate your
              AWS resources against a rule. It also provides the frequency with which you want AWS
              Config to run evaluations for the rule if the trigger type is periodic. You can
              specify the parameter values for ``SourceDetail`` only for custom rules.

              - **EventSource** *(string) --*

                The source of the event, such as an AWS service, that triggers AWS Config to
                evaluate your AWS resources.

              - **MessageType** *(string) --*

                The type of notification that triggers AWS Config to run an evaluation for a rule.
                You can specify the following notification types:

                * ``ConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config
                delivers a configuration item as a result of a resource change.

                * ``OversizedConfigurationItemChangeNotification`` - Triggers an evaluation when
                AWS Config delivers an oversized configuration item. AWS Config may generate this
                notification type when a resource changes and the notification exceeds the maximum
                size allowed by Amazon SNS.

                * ``ScheduledNotification`` - Triggers a periodic evaluation at the frequency
                specified for ``MaximumExecutionFrequency`` .

                * ``ConfigurationSnapshotDeliveryCompleted`` - Triggers a periodic evaluation when
                AWS Config delivers a configuration snapshot.

                If you want your custom rule to be triggered by configuration changes, specify two
                SourceDetail objects, one for ``ConfigurationItemChangeNotification`` and one for
                ``OversizedConfigurationItemChangeNotification`` .

              - **MaximumExecutionFrequency** *(string) --*

                The frequency at which you want AWS Config to run evaluations for a custom rule
                with a periodic trigger. If you specify a value for ``MaximumExecutionFrequency`` ,
                then ``MessageType`` must use the ``ScheduledNotification`` value.

                .. note::

                  By default, rules with a periodic trigger are evaluated every 24 hours. To change
                  the frequency, specify a valid value for the ``MaximumExecutionFrequency``
                  parameter.

                  Based on the valid value you choose, AWS Config runs evaluations once for each
                  valid value. For example, if you choose ``Three_Hours`` , AWS Config runs
                  evaluations once every three hours. In this case, ``Three_Hours`` is the
                  frequency of this rule.

        - **InputParameters** *(string) --*

          A string, in JSON format, that is passed to the AWS Config rule Lambda function.

        - **MaximumExecutionFrequency** *(string) --*

          The maximum frequency with which AWS Config runs evaluations for a rule. You can specify
          a value for ``MaximumExecutionFrequency`` when:

          * You are using an AWS managed rule that is triggered at a periodic frequency.

          * Your custom rule is triggered when AWS Config delivers the configuration snapshot. For
          more information, see  ConfigSnapshotDeliveryProperties .

          .. note::

            By default, rules with a periodic trigger are evaluated every 24 hours. To change the
            frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.

        - **ConfigRuleState** *(string) --*

          Indicates whether the AWS Config rule is active or is currently being deleted by AWS
          Config. It can also indicate the evaluation status for the AWS Config rule.

          AWS Config sets the state of the rule to ``EVALUATING`` temporarily after you use the
          ``StartConfigRulesEvaluation`` request to evaluate your resources against the AWS Config
          rule.

          AWS Config sets the state of the rule to ``DELETING_RESULTS`` temporarily after you use
          the ``DeleteEvaluationResults`` request to delete the current evaluation results for the
          AWS Config rule.

          AWS Config temporarily sets the state of a rule to ``DELETING`` after you use the
          ``DeleteConfigRule`` request to delete the rule. After AWS Config deletes the rule, the
          rule and all of its evaluations are erased and are no longer available.

        - **CreatedBy** *(string) --*

          Service principal name of the service that created the rule.

          .. note::

            The field is populated only if the service linked rule is created by a service. The
            field is empty if you create your own rule.
    """


_DescribeConfigurationAggregatorSourcesStatusPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeConfigurationAggregatorSourcesStatusPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeConfigurationAggregatorSourcesStatusPaginatePaginationConfigTypeDef(
    _DescribeConfigurationAggregatorSourcesStatusPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeConfigurationAggregatorSourcesStatusPaginate` `PaginationConfig`

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


_DescribeConfigurationAggregatorSourcesStatusPaginateResponseAggregatedSourceStatusListTypeDef = TypedDict(
    "_DescribeConfigurationAggregatorSourcesStatusPaginateResponseAggregatedSourceStatusListTypeDef",
    {
        "SourceId": str,
        "SourceType": str,
        "AwsRegion": str,
        "LastUpdateStatus": str,
        "LastUpdateTime": datetime,
        "LastErrorCode": str,
        "LastErrorMessage": str,
    },
    total=False,
)


class DescribeConfigurationAggregatorSourcesStatusPaginateResponseAggregatedSourceStatusListTypeDef(
    _DescribeConfigurationAggregatorSourcesStatusPaginateResponseAggregatedSourceStatusListTypeDef
):
    """
    Type definition for `DescribeConfigurationAggregatorSourcesStatusPaginateResponse` `AggregatedSourceStatusList`

    The current sync status between the source and the aggregator account.

    - **SourceId** *(string) --*

      The source account ID or an organization.

    - **SourceType** *(string) --*

      The source account or an organization.

    - **AwsRegion** *(string) --*

      The region authorized to collect aggregated data.

    - **LastUpdateStatus** *(string) --*

      Filters the last updated status type.

      * Valid value FAILED indicates errors while moving data.

      * Valid value SUCCEEDED indicates the data was successfully moved.

      * Valid value OUTDATED indicates the data is not the most recent.

    - **LastUpdateTime** *(datetime) --*

      The time of the last update.

    - **LastErrorCode** *(string) --*

      The error code that AWS Config returned when the source account aggregation last failed.

    - **LastErrorMessage** *(string) --*

      The message indicating that the source account aggregation failed due to an error.
    """


_DescribeConfigurationAggregatorSourcesStatusPaginateResponseTypeDef = TypedDict(
    "_DescribeConfigurationAggregatorSourcesStatusPaginateResponseTypeDef",
    {
        "AggregatedSourceStatusList": List[
            DescribeConfigurationAggregatorSourcesStatusPaginateResponseAggregatedSourceStatusListTypeDef
        ]
    },
    total=False,
)


class DescribeConfigurationAggregatorSourcesStatusPaginateResponseTypeDef(
    _DescribeConfigurationAggregatorSourcesStatusPaginateResponseTypeDef
):
    """
    Type definition for `DescribeConfigurationAggregatorSourcesStatusPaginate` `Response`

    - **AggregatedSourceStatusList** *(list) --*

      Returns an AggregatedSourceStatus object.

      - *(dict) --*

        The current sync status between the source and the aggregator account.

        - **SourceId** *(string) --*

          The source account ID or an organization.

        - **SourceType** *(string) --*

          The source account or an organization.

        - **AwsRegion** *(string) --*

          The region authorized to collect aggregated data.

        - **LastUpdateStatus** *(string) --*

          Filters the last updated status type.

          * Valid value FAILED indicates errors while moving data.

          * Valid value SUCCEEDED indicates the data was successfully moved.

          * Valid value OUTDATED indicates the data is not the most recent.

        - **LastUpdateTime** *(datetime) --*

          The time of the last update.

        - **LastErrorCode** *(string) --*

          The error code that AWS Config returned when the source account aggregation last failed.

        - **LastErrorMessage** *(string) --*

          The message indicating that the source account aggregation failed due to an error.
    """


_DescribeConfigurationAggregatorsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeConfigurationAggregatorsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeConfigurationAggregatorsPaginatePaginationConfigTypeDef(
    _DescribeConfigurationAggregatorsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeConfigurationAggregatorsPaginate` `PaginationConfig`

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


_DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsAccountAggregationSourcesTypeDef = TypedDict(
    "_DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsAccountAggregationSourcesTypeDef",
    {"AccountIds": List[str], "AllAwsRegions": bool, "AwsRegions": List[str]},
    total=False,
)


class DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsAccountAggregationSourcesTypeDef(
    _DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsAccountAggregationSourcesTypeDef
):
    """
    Type definition for `DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregators` `AccountAggregationSources`

    A collection of accounts and regions.

    - **AccountIds** *(list) --*

      The 12-digit account ID of the account being aggregated.

      - *(string) --*

    - **AllAwsRegions** *(boolean) --*

      If true, aggregate existing AWS Config regions and future regions.

    - **AwsRegions** *(list) --*

      The source regions being aggregated.

      - *(string) --*
    """


_DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsOrganizationAggregationSourceTypeDef = TypedDict(
    "_DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsOrganizationAggregationSourceTypeDef",
    {"RoleArn": str, "AwsRegions": List[str], "AllAwsRegions": bool},
    total=False,
)


class DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsOrganizationAggregationSourceTypeDef(
    _DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsOrganizationAggregationSourceTypeDef
):
    """
    Type definition for `DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregators` `OrganizationAggregationSource`

    Provides an organization and list of regions to be aggregated.

    - **RoleArn** *(string) --*

      ARN of the IAM role used to retrieve AWS Organization details associated with the
      aggregator account.

    - **AwsRegions** *(list) --*

      The source regions being aggregated.

      - *(string) --*

    - **AllAwsRegions** *(boolean) --*

      If true, aggregate existing AWS Config regions and future regions.
    """


_DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsTypeDef = TypedDict(
    "_DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ConfigurationAggregatorArn": str,
        "AccountAggregationSources": List[
            DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsAccountAggregationSourcesTypeDef
        ],
        "OrganizationAggregationSource": DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsOrganizationAggregationSourceTypeDef,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)


class DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsTypeDef(
    _DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsTypeDef
):
    """
    Type definition for `DescribeConfigurationAggregatorsPaginateResponse` `ConfigurationAggregators`

    The details about the configuration aggregator, including information about source
    accounts, regions, and metadata of the aggregator.

    - **ConfigurationAggregatorName** *(string) --*

      The name of the aggregator.

    - **ConfigurationAggregatorArn** *(string) --*

      The Amazon Resource Name (ARN) of the aggregator.

    - **AccountAggregationSources** *(list) --*

      Provides a list of source accounts and regions to be aggregated.

      - *(dict) --*

        A collection of accounts and regions.

        - **AccountIds** *(list) --*

          The 12-digit account ID of the account being aggregated.

          - *(string) --*

        - **AllAwsRegions** *(boolean) --*

          If true, aggregate existing AWS Config regions and future regions.

        - **AwsRegions** *(list) --*

          The source regions being aggregated.

          - *(string) --*

    - **OrganizationAggregationSource** *(dict) --*

      Provides an organization and list of regions to be aggregated.

      - **RoleArn** *(string) --*

        ARN of the IAM role used to retrieve AWS Organization details associated with the
        aggregator account.

      - **AwsRegions** *(list) --*

        The source regions being aggregated.

        - *(string) --*

      - **AllAwsRegions** *(boolean) --*

        If true, aggregate existing AWS Config regions and future regions.

    - **CreationTime** *(datetime) --*

      The time stamp when the configuration aggregator was created.

    - **LastUpdatedTime** *(datetime) --*

      The time of the last update.
    """


_DescribeConfigurationAggregatorsPaginateResponseTypeDef = TypedDict(
    "_DescribeConfigurationAggregatorsPaginateResponseTypeDef",
    {
        "ConfigurationAggregators": List[
            DescribeConfigurationAggregatorsPaginateResponseConfigurationAggregatorsTypeDef
        ]
    },
    total=False,
)


class DescribeConfigurationAggregatorsPaginateResponseTypeDef(
    _DescribeConfigurationAggregatorsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeConfigurationAggregatorsPaginate` `Response`

    - **ConfigurationAggregators** *(list) --*

      Returns a ConfigurationAggregators object.

      - *(dict) --*

        The details about the configuration aggregator, including information about source
        accounts, regions, and metadata of the aggregator.

        - **ConfigurationAggregatorName** *(string) --*

          The name of the aggregator.

        - **ConfigurationAggregatorArn** *(string) --*

          The Amazon Resource Name (ARN) of the aggregator.

        - **AccountAggregationSources** *(list) --*

          Provides a list of source accounts and regions to be aggregated.

          - *(dict) --*

            A collection of accounts and regions.

            - **AccountIds** *(list) --*

              The 12-digit account ID of the account being aggregated.

              - *(string) --*

            - **AllAwsRegions** *(boolean) --*

              If true, aggregate existing AWS Config regions and future regions.

            - **AwsRegions** *(list) --*

              The source regions being aggregated.

              - *(string) --*

        - **OrganizationAggregationSource** *(dict) --*

          Provides an organization and list of regions to be aggregated.

          - **RoleArn** *(string) --*

            ARN of the IAM role used to retrieve AWS Organization details associated with the
            aggregator account.

          - **AwsRegions** *(list) --*

            The source regions being aggregated.

            - *(string) --*

          - **AllAwsRegions** *(boolean) --*

            If true, aggregate existing AWS Config regions and future regions.

        - **CreationTime** *(datetime) --*

          The time stamp when the configuration aggregator was created.

        - **LastUpdatedTime** *(datetime) --*

          The time of the last update.
    """


_DescribePendingAggregationRequestsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribePendingAggregationRequestsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribePendingAggregationRequestsPaginatePaginationConfigTypeDef(
    _DescribePendingAggregationRequestsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribePendingAggregationRequestsPaginate` `PaginationConfig`

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


_DescribePendingAggregationRequestsPaginateResponsePendingAggregationRequestsTypeDef = TypedDict(
    "_DescribePendingAggregationRequestsPaginateResponsePendingAggregationRequestsTypeDef",
    {"RequesterAccountId": str, "RequesterAwsRegion": str},
    total=False,
)


class DescribePendingAggregationRequestsPaginateResponsePendingAggregationRequestsTypeDef(
    _DescribePendingAggregationRequestsPaginateResponsePendingAggregationRequestsTypeDef
):
    """
    Type definition for `DescribePendingAggregationRequestsPaginateResponse` `PendingAggregationRequests`

    An object that represents the account ID and region of an aggregator account that is
    requesting authorization but is not yet authorized.

    - **RequesterAccountId** *(string) --*

      The 12-digit account ID of the account requesting to aggregate data.

    - **RequesterAwsRegion** *(string) --*

      The region requesting to aggregate data.
    """


_DescribePendingAggregationRequestsPaginateResponseTypeDef = TypedDict(
    "_DescribePendingAggregationRequestsPaginateResponseTypeDef",
    {
        "PendingAggregationRequests": List[
            DescribePendingAggregationRequestsPaginateResponsePendingAggregationRequestsTypeDef
        ]
    },
    total=False,
)


class DescribePendingAggregationRequestsPaginateResponseTypeDef(
    _DescribePendingAggregationRequestsPaginateResponseTypeDef
):
    """
    Type definition for `DescribePendingAggregationRequestsPaginate` `Response`

    - **PendingAggregationRequests** *(list) --*

      Returns a PendingAggregationRequests object.

      - *(dict) --*

        An object that represents the account ID and region of an aggregator account that is
        requesting authorization but is not yet authorized.

        - **RequesterAccountId** *(string) --*

          The 12-digit account ID of the account requesting to aggregate data.

        - **RequesterAwsRegion** *(string) --*

          The region requesting to aggregate data.
    """


_DescribeRemediationExecutionStatusPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeRemediationExecutionStatusPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeRemediationExecutionStatusPaginatePaginationConfigTypeDef(
    _DescribeRemediationExecutionStatusPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeRemediationExecutionStatusPaginate` `PaginationConfig`

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


_DescribeRemediationExecutionStatusPaginateResourceKeysTypeDef = TypedDict(
    "_DescribeRemediationExecutionStatusPaginateResourceKeysTypeDef",
    {"resourceType": str, "resourceId": str},
)


class DescribeRemediationExecutionStatusPaginateResourceKeysTypeDef(
    _DescribeRemediationExecutionStatusPaginateResourceKeysTypeDef
):
    """
    Type definition for `DescribeRemediationExecutionStatusPaginate` `ResourceKeys`

    The details that identify a resource within AWS Config, including the resource type and
    resource ID.

    - **resourceType** *(string) --* **[REQUIRED]**

      The resource type.

    - **resourceId** *(string) --* **[REQUIRED]**

      The ID of the resource (for example., sg-xxxxxx).
    """


_DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesResourceKeyTypeDef = TypedDict(
    "_DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesResourceKeyTypeDef",
    {"resourceType": str, "resourceId": str},
    total=False,
)


class DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesResourceKeyTypeDef(
    _DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesResourceKeyTypeDef
):
    """
    Type definition for `DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatuses` `ResourceKey`

    The details that identify a resource within AWS Config, including the resource type and
    resource ID.

    - **resourceType** *(string) --*

      The resource type.

    - **resourceId** *(string) --*

      The ID of the resource (for example., sg-xxxxxx).
    """


_DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesStepDetailsTypeDef = TypedDict(
    "_DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesStepDetailsTypeDef",
    {
        "Name": str,
        "State": str,
        "ErrorMessage": str,
        "StartTime": datetime,
        "StopTime": datetime,
    },
    total=False,
)


class DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesStepDetailsTypeDef(
    _DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesStepDetailsTypeDef
):
    """
    Type definition for `DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatuses` `StepDetails`

    Name of the step from the SSM document.

    - **Name** *(string) --*

      The details of the step.

    - **State** *(string) --*

      The valid status of the step.

    - **ErrorMessage** *(string) --*

      An error message if the step was interrupted during execution.

    - **StartTime** *(datetime) --*

      The time when the step started.

    - **StopTime** *(datetime) --*

      The time when the step stopped.
    """


_DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesTypeDef = TypedDict(
    "_DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesTypeDef",
    {
        "ResourceKey": DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesResourceKeyTypeDef,
        "State": str,
        "StepDetails": List[
            DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesStepDetailsTypeDef
        ],
        "InvocationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)


class DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesTypeDef(
    _DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesTypeDef
):
    """
    Type definition for `DescribeRemediationExecutionStatusPaginateResponse` `RemediationExecutionStatuses`

    Provides details of the current status of the invoked remediation action for that resource.

    - **ResourceKey** *(dict) --*

      The details that identify a resource within AWS Config, including the resource type and
      resource ID.

      - **resourceType** *(string) --*

        The resource type.

      - **resourceId** *(string) --*

        The ID of the resource (for example., sg-xxxxxx).

    - **State** *(string) --*

      ENUM of the values.

    - **StepDetails** *(list) --*

      Details of every step.

      - *(dict) --*

        Name of the step from the SSM document.

        - **Name** *(string) --*

          The details of the step.

        - **State** *(string) --*

          The valid status of the step.

        - **ErrorMessage** *(string) --*

          An error message if the step was interrupted during execution.

        - **StartTime** *(datetime) --*

          The time when the step started.

        - **StopTime** *(datetime) --*

          The time when the step stopped.

    - **InvocationTime** *(datetime) --*

      Start time when the remediation was executed.

    - **LastUpdatedTime** *(datetime) --*

      The time when the remediation execution was last updated.
    """


_DescribeRemediationExecutionStatusPaginateResponseTypeDef = TypedDict(
    "_DescribeRemediationExecutionStatusPaginateResponseTypeDef",
    {
        "RemediationExecutionStatuses": List[
            DescribeRemediationExecutionStatusPaginateResponseRemediationExecutionStatusesTypeDef
        ]
    },
    total=False,
)


class DescribeRemediationExecutionStatusPaginateResponseTypeDef(
    _DescribeRemediationExecutionStatusPaginateResponseTypeDef
):
    """
    Type definition for `DescribeRemediationExecutionStatusPaginate` `Response`

    - **RemediationExecutionStatuses** *(list) --*

      Returns a list of remediation execution statuses objects.

      - *(dict) --*

        Provides details of the current status of the invoked remediation action for that resource.

        - **ResourceKey** *(dict) --*

          The details that identify a resource within AWS Config, including the resource type and
          resource ID.

          - **resourceType** *(string) --*

            The resource type.

          - **resourceId** *(string) --*

            The ID of the resource (for example., sg-xxxxxx).

        - **State** *(string) --*

          ENUM of the values.

        - **StepDetails** *(list) --*

          Details of every step.

          - *(dict) --*

            Name of the step from the SSM document.

            - **Name** *(string) --*

              The details of the step.

            - **State** *(string) --*

              The valid status of the step.

            - **ErrorMessage** *(string) --*

              An error message if the step was interrupted during execution.

            - **StartTime** *(datetime) --*

              The time when the step started.

            - **StopTime** *(datetime) --*

              The time when the step stopped.

        - **InvocationTime** *(datetime) --*

          Start time when the remediation was executed.

        - **LastUpdatedTime** *(datetime) --*

          The time when the remediation execution was last updated.
    """


_DescribeRetentionConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeRetentionConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class DescribeRetentionConfigurationsPaginatePaginationConfigTypeDef(
    _DescribeRetentionConfigurationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeRetentionConfigurationsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeRetentionConfigurationsPaginateResponseRetentionConfigurationsTypeDef = TypedDict(
    "_DescribeRetentionConfigurationsPaginateResponseRetentionConfigurationsTypeDef",
    {"Name": str, "RetentionPeriodInDays": int},
    total=False,
)


class DescribeRetentionConfigurationsPaginateResponseRetentionConfigurationsTypeDef(
    _DescribeRetentionConfigurationsPaginateResponseRetentionConfigurationsTypeDef
):
    """
    Type definition for `DescribeRetentionConfigurationsPaginateResponse` `RetentionConfigurations`

    An object with the name of the retention configuration and the retention period in days.
    The object stores the configuration for data retention in AWS Config.

    - **Name** *(string) --*

      The name of the retention configuration object.

    - **RetentionPeriodInDays** *(integer) --*

      Number of days AWS Config stores your historical information.

      .. note::

        Currently, only applicable to the configuration item history.
    """


_DescribeRetentionConfigurationsPaginateResponseTypeDef = TypedDict(
    "_DescribeRetentionConfigurationsPaginateResponseTypeDef",
    {
        "RetentionConfigurations": List[
            DescribeRetentionConfigurationsPaginateResponseRetentionConfigurationsTypeDef
        ]
    },
    total=False,
)


class DescribeRetentionConfigurationsPaginateResponseTypeDef(
    _DescribeRetentionConfigurationsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeRetentionConfigurationsPaginate` `Response`

    - **RetentionConfigurations** *(list) --*

      Returns a retention configuration object.

      - *(dict) --*

        An object with the name of the retention configuration and the retention period in days.
        The object stores the configuration for data retention in AWS Config.

        - **Name** *(string) --*

          The name of the retention configuration object.

        - **RetentionPeriodInDays** *(integer) --*

          Number of days AWS Config stores your historical information.

          .. note::

            Currently, only applicable to the configuration item history.
    """


_GetAggregateComplianceDetailsByConfigRulePaginatePaginationConfigTypeDef = TypedDict(
    "_GetAggregateComplianceDetailsByConfigRulePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetAggregateComplianceDetailsByConfigRulePaginatePaginationConfigTypeDef(
    _GetAggregateComplianceDetailsByConfigRulePaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetAggregateComplianceDetailsByConfigRulePaginate` `PaginationConfig`

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


_GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef = TypedDict(
    "_GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    {"ConfigRuleName": str, "ResourceType": str, "ResourceId": str},
    total=False,
)


class GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef(
    _GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef
):
    """
    Type definition for `GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsEvaluationResultIdentifier` `EvaluationResultQualifier`

    Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
    and ID of the evaluated resource.

    - **ConfigRuleName** *(string) --*

      The name of the AWS Config rule that was used in the evaluation.

    - **ResourceType** *(string) --*

      The type of AWS resource that was evaluated.

    - **ResourceId** *(string) --*

      The ID of the evaluated AWS resource.
    """


_GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsEvaluationResultIdentifierTypeDef = TypedDict(
    "_GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsEvaluationResultIdentifierTypeDef",
    {
        "EvaluationResultQualifier": GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef,
        "OrderingTimestamp": datetime,
    },
    total=False,
)


class GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsEvaluationResultIdentifierTypeDef(
    _GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsEvaluationResultIdentifierTypeDef
):
    """
    Type definition for `GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResults` `EvaluationResultIdentifier`

    Uniquely identifies the evaluation result.

    - **EvaluationResultQualifier** *(dict) --*

      Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
      and ID of the evaluated resource.

      - **ConfigRuleName** *(string) --*

        The name of the AWS Config rule that was used in the evaluation.

      - **ResourceType** *(string) --*

        The type of AWS resource that was evaluated.

      - **ResourceId** *(string) --*

        The ID of the evaluated AWS resource.

    - **OrderingTimestamp** *(datetime) --*

      The time of the event that triggered the evaluation of your AWS resources. The time can
      indicate when AWS Config delivered a configuration item change notification, or it can
      indicate when AWS Config delivered the configuration snapshot, depending on which event
      triggered the evaluation.
    """


_GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsTypeDef = TypedDict(
    "_GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsTypeDef",
    {
        "EvaluationResultIdentifier": GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsEvaluationResultIdentifierTypeDef,
        "ComplianceType": str,
        "ResultRecordedTime": datetime,
        "ConfigRuleInvokedTime": datetime,
        "Annotation": str,
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)


class GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsTypeDef(
    _GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsTypeDef
):
    """
    Type definition for `GetAggregateComplianceDetailsByConfigRulePaginateResponse` `AggregateEvaluationResults`

    The details of an AWS Config evaluation for an account ID and region in an aggregator.
    Provides the AWS resource that was evaluated, the compliance of the resource, related time
    stamps, and supplementary information.

    - **EvaluationResultIdentifier** *(dict) --*

      Uniquely identifies the evaluation result.

      - **EvaluationResultQualifier** *(dict) --*

        Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
        and ID of the evaluated resource.

        - **ConfigRuleName** *(string) --*

          The name of the AWS Config rule that was used in the evaluation.

        - **ResourceType** *(string) --*

          The type of AWS resource that was evaluated.

        - **ResourceId** *(string) --*

          The ID of the evaluated AWS resource.

      - **OrderingTimestamp** *(datetime) --*

        The time of the event that triggered the evaluation of your AWS resources. The time can
        indicate when AWS Config delivered a configuration item change notification, or it can
        indicate when AWS Config delivered the configuration snapshot, depending on which event
        triggered the evaluation.

    - **ComplianceType** *(string) --*

      The resource compliance status.

      For the ``AggregationEvaluationResult`` data type, AWS Config supports only the
      ``COMPLIANT`` and ``NON_COMPLIANT`` . AWS Config does not support the ``NOT_APPLICABLE``
      and ``INSUFFICIENT_DATA`` value.

    - **ResultRecordedTime** *(datetime) --*

      The time when AWS Config recorded the aggregate evaluation result.

    - **ConfigRuleInvokedTime** *(datetime) --*

      The time when the AWS Config rule evaluated the AWS resource.

    - **Annotation** *(string) --*

      Supplementary information about how the agrregate evaluation determined the compliance.

    - **AccountId** *(string) --*

      The 12-digit account ID of the source account.

    - **AwsRegion** *(string) --*

      The source region from where the data is aggregated.
    """


_GetAggregateComplianceDetailsByConfigRulePaginateResponseTypeDef = TypedDict(
    "_GetAggregateComplianceDetailsByConfigRulePaginateResponseTypeDef",
    {
        "AggregateEvaluationResults": List[
            GetAggregateComplianceDetailsByConfigRulePaginateResponseAggregateEvaluationResultsTypeDef
        ]
    },
    total=False,
)


class GetAggregateComplianceDetailsByConfigRulePaginateResponseTypeDef(
    _GetAggregateComplianceDetailsByConfigRulePaginateResponseTypeDef
):
    """
    Type definition for `GetAggregateComplianceDetailsByConfigRulePaginate` `Response`

    - **AggregateEvaluationResults** *(list) --*

      Returns an AggregateEvaluationResults object.

      - *(dict) --*

        The details of an AWS Config evaluation for an account ID and region in an aggregator.
        Provides the AWS resource that was evaluated, the compliance of the resource, related time
        stamps, and supplementary information.

        - **EvaluationResultIdentifier** *(dict) --*

          Uniquely identifies the evaluation result.

          - **EvaluationResultQualifier** *(dict) --*

            Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
            and ID of the evaluated resource.

            - **ConfigRuleName** *(string) --*

              The name of the AWS Config rule that was used in the evaluation.

            - **ResourceType** *(string) --*

              The type of AWS resource that was evaluated.

            - **ResourceId** *(string) --*

              The ID of the evaluated AWS resource.

          - **OrderingTimestamp** *(datetime) --*

            The time of the event that triggered the evaluation of your AWS resources. The time can
            indicate when AWS Config delivered a configuration item change notification, or it can
            indicate when AWS Config delivered the configuration snapshot, depending on which event
            triggered the evaluation.

        - **ComplianceType** *(string) --*

          The resource compliance status.

          For the ``AggregationEvaluationResult`` data type, AWS Config supports only the
          ``COMPLIANT`` and ``NON_COMPLIANT`` . AWS Config does not support the ``NOT_APPLICABLE``
          and ``INSUFFICIENT_DATA`` value.

        - **ResultRecordedTime** *(datetime) --*

          The time when AWS Config recorded the aggregate evaluation result.

        - **ConfigRuleInvokedTime** *(datetime) --*

          The time when the AWS Config rule evaluated the AWS resource.

        - **Annotation** *(string) --*

          Supplementary information about how the agrregate evaluation determined the compliance.

        - **AccountId** *(string) --*

          The 12-digit account ID of the source account.

        - **AwsRegion** *(string) --*

          The source region from where the data is aggregated.
    """


_GetComplianceDetailsByConfigRulePaginatePaginationConfigTypeDef = TypedDict(
    "_GetComplianceDetailsByConfigRulePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetComplianceDetailsByConfigRulePaginatePaginationConfigTypeDef(
    _GetComplianceDetailsByConfigRulePaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetComplianceDetailsByConfigRulePaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef = TypedDict(
    "_GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    {"ConfigRuleName": str, "ResourceType": str, "ResourceId": str},
    total=False,
)


class GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef(
    _GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef
):
    """
    Type definition for `GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsEvaluationResultIdentifier` `EvaluationResultQualifier`

    Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
    and ID of the evaluated resource.

    - **ConfigRuleName** *(string) --*

      The name of the AWS Config rule that was used in the evaluation.

    - **ResourceType** *(string) --*

      The type of AWS resource that was evaluated.

    - **ResourceId** *(string) --*

      The ID of the evaluated AWS resource.
    """


_GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsEvaluationResultIdentifierTypeDef = TypedDict(
    "_GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsEvaluationResultIdentifierTypeDef",
    {
        "EvaluationResultQualifier": GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef,
        "OrderingTimestamp": datetime,
    },
    total=False,
)


class GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsEvaluationResultIdentifierTypeDef(
    _GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsEvaluationResultIdentifierTypeDef
):
    """
    Type definition for `GetComplianceDetailsByConfigRulePaginateResponseEvaluationResults` `EvaluationResultIdentifier`

    Uniquely identifies the evaluation result.

    - **EvaluationResultQualifier** *(dict) --*

      Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
      and ID of the evaluated resource.

      - **ConfigRuleName** *(string) --*

        The name of the AWS Config rule that was used in the evaluation.

      - **ResourceType** *(string) --*

        The type of AWS resource that was evaluated.

      - **ResourceId** *(string) --*

        The ID of the evaluated AWS resource.

    - **OrderingTimestamp** *(datetime) --*

      The time of the event that triggered the evaluation of your AWS resources. The time can
      indicate when AWS Config delivered a configuration item change notification, or it can
      indicate when AWS Config delivered the configuration snapshot, depending on which event
      triggered the evaluation.
    """


_GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsTypeDef = TypedDict(
    "_GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsTypeDef",
    {
        "EvaluationResultIdentifier": GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsEvaluationResultIdentifierTypeDef,
        "ComplianceType": str,
        "ResultRecordedTime": datetime,
        "ConfigRuleInvokedTime": datetime,
        "Annotation": str,
        "ResultToken": str,
    },
    total=False,
)


class GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsTypeDef(
    _GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsTypeDef
):
    """
    Type definition for `GetComplianceDetailsByConfigRulePaginateResponse` `EvaluationResults`

    The details of an AWS Config evaluation. Provides the AWS resource that was evaluated, the
    compliance of the resource, related time stamps, and supplementary information.

    - **EvaluationResultIdentifier** *(dict) --*

      Uniquely identifies the evaluation result.

      - **EvaluationResultQualifier** *(dict) --*

        Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
        and ID of the evaluated resource.

        - **ConfigRuleName** *(string) --*

          The name of the AWS Config rule that was used in the evaluation.

        - **ResourceType** *(string) --*

          The type of AWS resource that was evaluated.

        - **ResourceId** *(string) --*

          The ID of the evaluated AWS resource.

      - **OrderingTimestamp** *(datetime) --*

        The time of the event that triggered the evaluation of your AWS resources. The time can
        indicate when AWS Config delivered a configuration item change notification, or it can
        indicate when AWS Config delivered the configuration snapshot, depending on which event
        triggered the evaluation.

    - **ComplianceType** *(string) --*

      Indicates whether the AWS resource complies with the AWS Config rule that evaluated it.

      For the ``EvaluationResult`` data type, AWS Config supports only the ``COMPLIANT`` ,
      ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` values. AWS Config does not support the
      ``INSUFFICIENT_DATA`` value for the ``EvaluationResult`` data type.

    - **ResultRecordedTime** *(datetime) --*

      The time when AWS Config recorded the evaluation result.

    - **ConfigRuleInvokedTime** *(datetime) --*

      The time when the AWS Config rule evaluated the AWS resource.

    - **Annotation** *(string) --*

      Supplementary information about how the evaluation determined the compliance.

    - **ResultToken** *(string) --*

      An encrypted token that associates an evaluation with an AWS Config rule. The token
      identifies the rule, the AWS resource being evaluated, and the event that triggered the
      evaluation.
    """


_GetComplianceDetailsByConfigRulePaginateResponseTypeDef = TypedDict(
    "_GetComplianceDetailsByConfigRulePaginateResponseTypeDef",
    {
        "EvaluationResults": List[
            GetComplianceDetailsByConfigRulePaginateResponseEvaluationResultsTypeDef
        ]
    },
    total=False,
)


class GetComplianceDetailsByConfigRulePaginateResponseTypeDef(
    _GetComplianceDetailsByConfigRulePaginateResponseTypeDef
):
    """
    Type definition for `GetComplianceDetailsByConfigRulePaginate` `Response`

    - **EvaluationResults** *(list) --*

      Indicates whether the AWS resource complies with the specified AWS Config rule.

      - *(dict) --*

        The details of an AWS Config evaluation. Provides the AWS resource that was evaluated, the
        compliance of the resource, related time stamps, and supplementary information.

        - **EvaluationResultIdentifier** *(dict) --*

          Uniquely identifies the evaluation result.

          - **EvaluationResultQualifier** *(dict) --*

            Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
            and ID of the evaluated resource.

            - **ConfigRuleName** *(string) --*

              The name of the AWS Config rule that was used in the evaluation.

            - **ResourceType** *(string) --*

              The type of AWS resource that was evaluated.

            - **ResourceId** *(string) --*

              The ID of the evaluated AWS resource.

          - **OrderingTimestamp** *(datetime) --*

            The time of the event that triggered the evaluation of your AWS resources. The time can
            indicate when AWS Config delivered a configuration item change notification, or it can
            indicate when AWS Config delivered the configuration snapshot, depending on which event
            triggered the evaluation.

        - **ComplianceType** *(string) --*

          Indicates whether the AWS resource complies with the AWS Config rule that evaluated it.

          For the ``EvaluationResult`` data type, AWS Config supports only the ``COMPLIANT`` ,
          ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` values. AWS Config does not support the
          ``INSUFFICIENT_DATA`` value for the ``EvaluationResult`` data type.

        - **ResultRecordedTime** *(datetime) --*

          The time when AWS Config recorded the evaluation result.

        - **ConfigRuleInvokedTime** *(datetime) --*

          The time when the AWS Config rule evaluated the AWS resource.

        - **Annotation** *(string) --*

          Supplementary information about how the evaluation determined the compliance.

        - **ResultToken** *(string) --*

          An encrypted token that associates an evaluation with an AWS Config rule. The token
          identifies the rule, the AWS resource being evaluated, and the event that triggered the
          evaluation.
    """


_GetComplianceDetailsByResourcePaginatePaginationConfigTypeDef = TypedDict(
    "_GetComplianceDetailsByResourcePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetComplianceDetailsByResourcePaginatePaginationConfigTypeDef(
    _GetComplianceDetailsByResourcePaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetComplianceDetailsByResourcePaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetComplianceDetailsByResourcePaginateResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef = TypedDict(
    "_GetComplianceDetailsByResourcePaginateResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef",
    {"ConfigRuleName": str, "ResourceType": str, "ResourceId": str},
    total=False,
)


class GetComplianceDetailsByResourcePaginateResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef(
    _GetComplianceDetailsByResourcePaginateResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef
):
    """
    Type definition for `GetComplianceDetailsByResourcePaginateResponseEvaluationResultsEvaluationResultIdentifier` `EvaluationResultQualifier`

    Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
    and ID of the evaluated resource.

    - **ConfigRuleName** *(string) --*

      The name of the AWS Config rule that was used in the evaluation.

    - **ResourceType** *(string) --*

      The type of AWS resource that was evaluated.

    - **ResourceId** *(string) --*

      The ID of the evaluated AWS resource.
    """


_GetComplianceDetailsByResourcePaginateResponseEvaluationResultsEvaluationResultIdentifierTypeDef = TypedDict(
    "_GetComplianceDetailsByResourcePaginateResponseEvaluationResultsEvaluationResultIdentifierTypeDef",
    {
        "EvaluationResultQualifier": GetComplianceDetailsByResourcePaginateResponseEvaluationResultsEvaluationResultIdentifierEvaluationResultQualifierTypeDef,
        "OrderingTimestamp": datetime,
    },
    total=False,
)


class GetComplianceDetailsByResourcePaginateResponseEvaluationResultsEvaluationResultIdentifierTypeDef(
    _GetComplianceDetailsByResourcePaginateResponseEvaluationResultsEvaluationResultIdentifierTypeDef
):
    """
    Type definition for `GetComplianceDetailsByResourcePaginateResponseEvaluationResults` `EvaluationResultIdentifier`

    Uniquely identifies the evaluation result.

    - **EvaluationResultQualifier** *(dict) --*

      Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
      and ID of the evaluated resource.

      - **ConfigRuleName** *(string) --*

        The name of the AWS Config rule that was used in the evaluation.

      - **ResourceType** *(string) --*

        The type of AWS resource that was evaluated.

      - **ResourceId** *(string) --*

        The ID of the evaluated AWS resource.

    - **OrderingTimestamp** *(datetime) --*

      The time of the event that triggered the evaluation of your AWS resources. The time can
      indicate when AWS Config delivered a configuration item change notification, or it can
      indicate when AWS Config delivered the configuration snapshot, depending on which event
      triggered the evaluation.
    """


_GetComplianceDetailsByResourcePaginateResponseEvaluationResultsTypeDef = TypedDict(
    "_GetComplianceDetailsByResourcePaginateResponseEvaluationResultsTypeDef",
    {
        "EvaluationResultIdentifier": GetComplianceDetailsByResourcePaginateResponseEvaluationResultsEvaluationResultIdentifierTypeDef,
        "ComplianceType": str,
        "ResultRecordedTime": datetime,
        "ConfigRuleInvokedTime": datetime,
        "Annotation": str,
        "ResultToken": str,
    },
    total=False,
)


class GetComplianceDetailsByResourcePaginateResponseEvaluationResultsTypeDef(
    _GetComplianceDetailsByResourcePaginateResponseEvaluationResultsTypeDef
):
    """
    Type definition for `GetComplianceDetailsByResourcePaginateResponse` `EvaluationResults`

    The details of an AWS Config evaluation. Provides the AWS resource that was evaluated, the
    compliance of the resource, related time stamps, and supplementary information.

    - **EvaluationResultIdentifier** *(dict) --*

      Uniquely identifies the evaluation result.

      - **EvaluationResultQualifier** *(dict) --*

        Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
        and ID of the evaluated resource.

        - **ConfigRuleName** *(string) --*

          The name of the AWS Config rule that was used in the evaluation.

        - **ResourceType** *(string) --*

          The type of AWS resource that was evaluated.

        - **ResourceId** *(string) --*

          The ID of the evaluated AWS resource.

      - **OrderingTimestamp** *(datetime) --*

        The time of the event that triggered the evaluation of your AWS resources. The time can
        indicate when AWS Config delivered a configuration item change notification, or it can
        indicate when AWS Config delivered the configuration snapshot, depending on which event
        triggered the evaluation.

    - **ComplianceType** *(string) --*

      Indicates whether the AWS resource complies with the AWS Config rule that evaluated it.

      For the ``EvaluationResult`` data type, AWS Config supports only the ``COMPLIANT`` ,
      ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` values. AWS Config does not support the
      ``INSUFFICIENT_DATA`` value for the ``EvaluationResult`` data type.

    - **ResultRecordedTime** *(datetime) --*

      The time when AWS Config recorded the evaluation result.

    - **ConfigRuleInvokedTime** *(datetime) --*

      The time when the AWS Config rule evaluated the AWS resource.

    - **Annotation** *(string) --*

      Supplementary information about how the evaluation determined the compliance.

    - **ResultToken** *(string) --*

      An encrypted token that associates an evaluation with an AWS Config rule. The token
      identifies the rule, the AWS resource being evaluated, and the event that triggered the
      evaluation.
    """


_GetComplianceDetailsByResourcePaginateResponseTypeDef = TypedDict(
    "_GetComplianceDetailsByResourcePaginateResponseTypeDef",
    {
        "EvaluationResults": List[
            GetComplianceDetailsByResourcePaginateResponseEvaluationResultsTypeDef
        ]
    },
    total=False,
)


class GetComplianceDetailsByResourcePaginateResponseTypeDef(
    _GetComplianceDetailsByResourcePaginateResponseTypeDef
):
    """
    Type definition for `GetComplianceDetailsByResourcePaginate` `Response`

    - **EvaluationResults** *(list) --*

      Indicates whether the specified AWS resource complies each AWS Config rule.

      - *(dict) --*

        The details of an AWS Config evaluation. Provides the AWS resource that was evaluated, the
        compliance of the resource, related time stamps, and supplementary information.

        - **EvaluationResultIdentifier** *(dict) --*

          Uniquely identifies the evaluation result.

          - **EvaluationResultQualifier** *(dict) --*

            Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type
            and ID of the evaluated resource.

            - **ConfigRuleName** *(string) --*

              The name of the AWS Config rule that was used in the evaluation.

            - **ResourceType** *(string) --*

              The type of AWS resource that was evaluated.

            - **ResourceId** *(string) --*

              The ID of the evaluated AWS resource.

          - **OrderingTimestamp** *(datetime) --*

            The time of the event that triggered the evaluation of your AWS resources. The time can
            indicate when AWS Config delivered a configuration item change notification, or it can
            indicate when AWS Config delivered the configuration snapshot, depending on which event
            triggered the evaluation.

        - **ComplianceType** *(string) --*

          Indicates whether the AWS resource complies with the AWS Config rule that evaluated it.

          For the ``EvaluationResult`` data type, AWS Config supports only the ``COMPLIANT`` ,
          ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` values. AWS Config does not support the
          ``INSUFFICIENT_DATA`` value for the ``EvaluationResult`` data type.

        - **ResultRecordedTime** *(datetime) --*

          The time when AWS Config recorded the evaluation result.

        - **ConfigRuleInvokedTime** *(datetime) --*

          The time when the AWS Config rule evaluated the AWS resource.

        - **Annotation** *(string) --*

          Supplementary information about how the evaluation determined the compliance.

        - **ResultToken** *(string) --*

          An encrypted token that associates an evaluation with an AWS Config rule. The token
          identifies the rule, the AWS resource being evaluated, and the event that triggered the
          evaluation.
    """


_GetResourceConfigHistoryPaginatePaginationConfigTypeDef = TypedDict(
    "_GetResourceConfigHistoryPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetResourceConfigHistoryPaginatePaginationConfigTypeDef(
    _GetResourceConfigHistoryPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetResourceConfigHistoryPaginate` `PaginationConfig`

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


_GetResourceConfigHistoryPaginateResponseconfigurationItemsrelationshipsTypeDef = TypedDict(
    "_GetResourceConfigHistoryPaginateResponseconfigurationItemsrelationshipsTypeDef",
    {
        "resourceType": str,
        "resourceId": str,
        "resourceName": str,
        "relationshipName": str,
    },
    total=False,
)


class GetResourceConfigHistoryPaginateResponseconfigurationItemsrelationshipsTypeDef(
    _GetResourceConfigHistoryPaginateResponseconfigurationItemsrelationshipsTypeDef
):
    """
    Type definition for `GetResourceConfigHistoryPaginateResponseconfigurationItems` `relationships`

    The relationship of the related resource to the main resource.

    - **resourceType** *(string) --*

      The resource type of the related resource.

    - **resourceId** *(string) --*

      The ID of the related resource (for example, ``sg-xxxxxx`` ).

    - **resourceName** *(string) --*

      The custom name of the related resource, if available.

    - **relationshipName** *(string) --*

      The type of relationship with the related resource.
    """


_GetResourceConfigHistoryPaginateResponseconfigurationItemsTypeDef = TypedDict(
    "_GetResourceConfigHistoryPaginateResponseconfigurationItemsTypeDef",
    {
        "version": str,
        "accountId": str,
        "configurationItemCaptureTime": datetime,
        "configurationItemStatus": str,
        "configurationStateId": str,
        "configurationItemMD5Hash": str,
        "arn": str,
        "resourceType": str,
        "resourceId": str,
        "resourceName": str,
        "awsRegion": str,
        "availabilityZone": str,
        "resourceCreationTime": datetime,
        "tags": Dict[str, str],
        "relatedEvents": List[str],
        "relationships": List[
            GetResourceConfigHistoryPaginateResponseconfigurationItemsrelationshipsTypeDef
        ],
        "configuration": str,
        "supplementaryConfiguration": Dict[str, str],
    },
    total=False,
)


class GetResourceConfigHistoryPaginateResponseconfigurationItemsTypeDef(
    _GetResourceConfigHistoryPaginateResponseconfigurationItemsTypeDef
):
    """
    Type definition for `GetResourceConfigHistoryPaginateResponse` `configurationItems`

    A list that contains detailed configurations of a specified resource.

    - **version** *(string) --*

      The version number of the resource configuration.

    - **accountId** *(string) --*

      The 12-digit AWS account ID associated with the resource.

    - **configurationItemCaptureTime** *(datetime) --*

      The time when the configuration recording was initiated.

    - **configurationItemStatus** *(string) --*

      The configuration item status.

    - **configurationStateId** *(string) --*

      An identifier that indicates the ordering of the configuration items of a resource.

    - **configurationItemMD5Hash** *(string) --*

      Unique MD5 hash that represents the configuration item's state.

      You can use MD5 hash to compare the states of two or more configuration items that are
      associated with the same resource.

    - **arn** *(string) --*

      accoun

    - **resourceType** *(string) --*

      The type of AWS resource.

    - **resourceId** *(string) --*

      The ID of the resource (for example, ``sg-xxxxxx`` ).

    - **resourceName** *(string) --*

      The custom name of the resource, if available.

    - **awsRegion** *(string) --*

      The region where the resource resides.

    - **availabilityZone** *(string) --*

      The Availability Zone associated with the resource.

    - **resourceCreationTime** *(datetime) --*

      The time stamp when the resource was created.

    - **tags** *(dict) --*

      A mapping of key value tags associated with the resource.

      - *(string) --*

        - *(string) --*

    - **relatedEvents** *(list) --*

      A list of CloudTrail event IDs.

      A populated field indicates that the current configuration was initiated by the events
      recorded in the CloudTrail log. For more information about CloudTrail, see `What Is AWS
      CloudTrail
      <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/what_is_cloud_trail_top_level.html>`__
      .

      An empty field indicates that the current configuration was not initiated by any event.

      - *(string) --*

    - **relationships** *(list) --*

      A list of related AWS resources.

      - *(dict) --*

        The relationship of the related resource to the main resource.

        - **resourceType** *(string) --*

          The resource type of the related resource.

        - **resourceId** *(string) --*

          The ID of the related resource (for example, ``sg-xxxxxx`` ).

        - **resourceName** *(string) --*

          The custom name of the related resource, if available.

        - **relationshipName** *(string) --*

          The type of relationship with the related resource.

    - **configuration** *(string) --*

      The description of the resource configuration.

    - **supplementaryConfiguration** *(dict) --*

      Configuration attributes that AWS Config returns for certain resource types to supplement
      the information returned for the ``configuration`` parameter.

      - *(string) --*

        - *(string) --*
    """


_GetResourceConfigHistoryPaginateResponseTypeDef = TypedDict(
    "_GetResourceConfigHistoryPaginateResponseTypeDef",
    {
        "configurationItems": List[
            GetResourceConfigHistoryPaginateResponseconfigurationItemsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class GetResourceConfigHistoryPaginateResponseTypeDef(
    _GetResourceConfigHistoryPaginateResponseTypeDef
):
    """
    Type definition for `GetResourceConfigHistoryPaginate` `Response`

    The output for the  GetResourceConfigHistory action.

    - **configurationItems** *(list) --*

      A list that contains the configuration history of one or more resources.

      - *(dict) --*

        A list that contains detailed configurations of a specified resource.

        - **version** *(string) --*

          The version number of the resource configuration.

        - **accountId** *(string) --*

          The 12-digit AWS account ID associated with the resource.

        - **configurationItemCaptureTime** *(datetime) --*

          The time when the configuration recording was initiated.

        - **configurationItemStatus** *(string) --*

          The configuration item status.

        - **configurationStateId** *(string) --*

          An identifier that indicates the ordering of the configuration items of a resource.

        - **configurationItemMD5Hash** *(string) --*

          Unique MD5 hash that represents the configuration item's state.

          You can use MD5 hash to compare the states of two or more configuration items that are
          associated with the same resource.

        - **arn** *(string) --*

          accoun

        - **resourceType** *(string) --*

          The type of AWS resource.

        - **resourceId** *(string) --*

          The ID of the resource (for example, ``sg-xxxxxx`` ).

        - **resourceName** *(string) --*

          The custom name of the resource, if available.

        - **awsRegion** *(string) --*

          The region where the resource resides.

        - **availabilityZone** *(string) --*

          The Availability Zone associated with the resource.

        - **resourceCreationTime** *(datetime) --*

          The time stamp when the resource was created.

        - **tags** *(dict) --*

          A mapping of key value tags associated with the resource.

          - *(string) --*

            - *(string) --*

        - **relatedEvents** *(list) --*

          A list of CloudTrail event IDs.

          A populated field indicates that the current configuration was initiated by the events
          recorded in the CloudTrail log. For more information about CloudTrail, see `What Is AWS
          CloudTrail
          <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/what_is_cloud_trail_top_level.html>`__
          .

          An empty field indicates that the current configuration was not initiated by any event.

          - *(string) --*

        - **relationships** *(list) --*

          A list of related AWS resources.

          - *(dict) --*

            The relationship of the related resource to the main resource.

            - **resourceType** *(string) --*

              The resource type of the related resource.

            - **resourceId** *(string) --*

              The ID of the related resource (for example, ``sg-xxxxxx`` ).

            - **resourceName** *(string) --*

              The custom name of the related resource, if available.

            - **relationshipName** *(string) --*

              The type of relationship with the related resource.

        - **configuration** *(string) --*

          The description of the resource configuration.

        - **supplementaryConfiguration** *(dict) --*

          Configuration attributes that AWS Config returns for certain resource types to supplement
          the information returned for the ``configuration`` parameter.

          - *(string) --*

            - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListAggregateDiscoveredResourcesPaginateFiltersTypeDef = TypedDict(
    "_ListAggregateDiscoveredResourcesPaginateFiltersTypeDef",
    {"AccountId": str, "ResourceId": str, "ResourceName": str, "Region": str},
    total=False,
)


class ListAggregateDiscoveredResourcesPaginateFiltersTypeDef(
    _ListAggregateDiscoveredResourcesPaginateFiltersTypeDef
):
    """
    Type definition for `ListAggregateDiscoveredResourcesPaginate` `Filters`

    Filters the results based on the ``ResourceFilters`` object.

    - **AccountId** *(string) --*

      The 12-digit source account ID.

    - **ResourceId** *(string) --*

      The ID of the resource.

    - **ResourceName** *(string) --*

      The name of the resource.

    - **Region** *(string) --*

      The source region.
    """


_ListAggregateDiscoveredResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAggregateDiscoveredResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAggregateDiscoveredResourcesPaginatePaginationConfigTypeDef(
    _ListAggregateDiscoveredResourcesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAggregateDiscoveredResourcesPaginate` `PaginationConfig`

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


_ListAggregateDiscoveredResourcesPaginateResponseResourceIdentifiersTypeDef = TypedDict(
    "_ListAggregateDiscoveredResourcesPaginateResponseResourceIdentifiersTypeDef",
    {
        "SourceAccountId": str,
        "SourceRegion": str,
        "ResourceId": str,
        "ResourceType": str,
        "ResourceName": str,
    },
    total=False,
)


class ListAggregateDiscoveredResourcesPaginateResponseResourceIdentifiersTypeDef(
    _ListAggregateDiscoveredResourcesPaginateResponseResourceIdentifiersTypeDef
):
    """
    Type definition for `ListAggregateDiscoveredResourcesPaginateResponse` `ResourceIdentifiers`

    The details that identify a resource that is collected by AWS Config aggregator, including
    the resource type, ID, (if available) the custom resource name, the source account, and
    source region.

    - **SourceAccountId** *(string) --*

      The 12-digit account ID of the source account.

    - **SourceRegion** *(string) --*

      The source region where data is aggregated.

    - **ResourceId** *(string) --*

      The ID of the AWS resource.

    - **ResourceType** *(string) --*

      The type of the AWS resource.

    - **ResourceName** *(string) --*

      The name of the AWS resource.
    """


_ListAggregateDiscoveredResourcesPaginateResponseTypeDef = TypedDict(
    "_ListAggregateDiscoveredResourcesPaginateResponseTypeDef",
    {
        "ResourceIdentifiers": List[
            ListAggregateDiscoveredResourcesPaginateResponseResourceIdentifiersTypeDef
        ]
    },
    total=False,
)


class ListAggregateDiscoveredResourcesPaginateResponseTypeDef(
    _ListAggregateDiscoveredResourcesPaginateResponseTypeDef
):
    """
    Type definition for `ListAggregateDiscoveredResourcesPaginate` `Response`

    - **ResourceIdentifiers** *(list) --*

      Returns a list of ``ResourceIdentifiers`` objects.

      - *(dict) --*

        The details that identify a resource that is collected by AWS Config aggregator, including
        the resource type, ID, (if available) the custom resource name, the source account, and
        source region.

        - **SourceAccountId** *(string) --*

          The 12-digit account ID of the source account.

        - **SourceRegion** *(string) --*

          The source region where data is aggregated.

        - **ResourceId** *(string) --*

          The ID of the AWS resource.

        - **ResourceType** *(string) --*

          The type of the AWS resource.

        - **ResourceName** *(string) --*

          The name of the AWS resource.
    """


_ListDiscoveredResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDiscoveredResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListDiscoveredResourcesPaginatePaginationConfigTypeDef(
    _ListDiscoveredResourcesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDiscoveredResourcesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListDiscoveredResourcesPaginateResponseresourceIdentifiersTypeDef = TypedDict(
    "_ListDiscoveredResourcesPaginateResponseresourceIdentifiersTypeDef",
    {
        "resourceType": str,
        "resourceId": str,
        "resourceName": str,
        "resourceDeletionTime": datetime,
    },
    total=False,
)


class ListDiscoveredResourcesPaginateResponseresourceIdentifiersTypeDef(
    _ListDiscoveredResourcesPaginateResponseresourceIdentifiersTypeDef
):
    """
    Type definition for `ListDiscoveredResourcesPaginateResponse` `resourceIdentifiers`

    The details that identify a resource that is discovered by AWS Config, including the
    resource type, ID, and (if available) the custom resource name.

    - **resourceType** *(string) --*

      The type of resource.

    - **resourceId** *(string) --*

      The ID of the resource (for example, ``sg-xxxxxx`` ).

    - **resourceName** *(string) --*

      The custom name of the resource (if available).

    - **resourceDeletionTime** *(datetime) --*

      The time that the resource was deleted.
    """


_ListDiscoveredResourcesPaginateResponseTypeDef = TypedDict(
    "_ListDiscoveredResourcesPaginateResponseTypeDef",
    {
        "resourceIdentifiers": List[
            ListDiscoveredResourcesPaginateResponseresourceIdentifiersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListDiscoveredResourcesPaginateResponseTypeDef(
    _ListDiscoveredResourcesPaginateResponseTypeDef
):
    """
    Type definition for `ListDiscoveredResourcesPaginate` `Response`

    - **resourceIdentifiers** *(list) --*

      The details that identify a resource that is discovered by AWS Config, including the resource
      type, ID, and (if available) the custom resource name.

      - *(dict) --*

        The details that identify a resource that is discovered by AWS Config, including the
        resource type, ID, and (if available) the custom resource name.

        - **resourceType** *(string) --*

          The type of resource.

        - **resourceId** *(string) --*

          The ID of the resource (for example, ``sg-xxxxxx`` ).

        - **resourceName** *(string) --*

          The custom name of the resource (if available).

        - **resourceDeletionTime** *(datetime) --*

          The time that the resource was deleted.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """
