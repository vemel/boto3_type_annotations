"Main interface for ce type defs"
from __future__ import annotations

from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientGetCostAndUsageFilterDimensionsTypeDef",
    "ClientGetCostAndUsageFilterTagsTypeDef",
    "ClientGetCostAndUsageFilterTypeDef",
    "ClientGetCostAndUsageGroupByTypeDef",
    "ClientGetCostAndUsageResponseGroupDefinitionsTypeDef",
    "ClientGetCostAndUsageResponseResultsByTimeGroupsMetricsTypeDef",
    "ClientGetCostAndUsageResponseResultsByTimeGroupsTypeDef",
    "ClientGetCostAndUsageResponseResultsByTimeTimePeriodTypeDef",
    "ClientGetCostAndUsageResponseResultsByTimeTotalTypeDef",
    "ClientGetCostAndUsageResponseResultsByTimeTypeDef",
    "ClientGetCostAndUsageResponseTypeDef",
    "ClientGetCostAndUsageTimePeriodTypeDef",
    "ClientGetCostAndUsageWithResourcesFilterDimensionsTypeDef",
    "ClientGetCostAndUsageWithResourcesFilterTagsTypeDef",
    "ClientGetCostAndUsageWithResourcesFilterTypeDef",
    "ClientGetCostAndUsageWithResourcesGroupByTypeDef",
    "ClientGetCostAndUsageWithResourcesResponseGroupDefinitionsTypeDef",
    "ClientGetCostAndUsageWithResourcesResponseResultsByTimeGroupsMetricsTypeDef",
    "ClientGetCostAndUsageWithResourcesResponseResultsByTimeGroupsTypeDef",
    "ClientGetCostAndUsageWithResourcesResponseResultsByTimeTimePeriodTypeDef",
    "ClientGetCostAndUsageWithResourcesResponseResultsByTimeTotalTypeDef",
    "ClientGetCostAndUsageWithResourcesResponseResultsByTimeTypeDef",
    "ClientGetCostAndUsageWithResourcesResponseTypeDef",
    "ClientGetCostAndUsageWithResourcesTimePeriodTypeDef",
    "ClientGetCostForecastFilterDimensionsTypeDef",
    "ClientGetCostForecastFilterTagsTypeDef",
    "ClientGetCostForecastFilterTypeDef",
    "ClientGetCostForecastResponseForecastResultsByTimeTimePeriodTypeDef",
    "ClientGetCostForecastResponseForecastResultsByTimeTypeDef",
    "ClientGetCostForecastResponseTotalTypeDef",
    "ClientGetCostForecastResponseTypeDef",
    "ClientGetCostForecastTimePeriodTypeDef",
    "ClientGetDimensionValuesResponseDimensionValuesTypeDef",
    "ClientGetDimensionValuesResponseTypeDef",
    "ClientGetDimensionValuesTimePeriodTypeDef",
    "ClientGetReservationCoverageFilterDimensionsTypeDef",
    "ClientGetReservationCoverageFilterTagsTypeDef",
    "ClientGetReservationCoverageFilterTypeDef",
    "ClientGetReservationCoverageGroupByTypeDef",
    "ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageCostTypeDef",
    "ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageHoursTypeDef",
    "ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageNormalizedUnitsTypeDef",
    "ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageTypeDef",
    "ClientGetReservationCoverageResponseCoveragesByTimeGroupsTypeDef",
    "ClientGetReservationCoverageResponseCoveragesByTimeTimePeriodTypeDef",
    "ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageCostTypeDef",
    "ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageHoursTypeDef",
    "ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageNormalizedUnitsTypeDef",
    "ClientGetReservationCoverageResponseCoveragesByTimeTotalTypeDef",
    "ClientGetReservationCoverageResponseCoveragesByTimeTypeDef",
    "ClientGetReservationCoverageResponseTotalCoverageCostTypeDef",
    "ClientGetReservationCoverageResponseTotalCoverageHoursTypeDef",
    "ClientGetReservationCoverageResponseTotalCoverageNormalizedUnitsTypeDef",
    "ClientGetReservationCoverageResponseTotalTypeDef",
    "ClientGetReservationCoverageResponseTypeDef",
    "ClientGetReservationCoverageTimePeriodTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseMetadataTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsEC2InstanceDetailsTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsESInstanceDetailsTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsElastiCacheInstanceDetailsTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsRDSInstanceDetailsTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsRedshiftInstanceDetailsTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationSummaryTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsServiceSpecificationEC2SpecificationTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsServiceSpecificationTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseTypeDef",
    "ClientGetReservationPurchaseRecommendationServiceSpecificationEC2SpecificationTypeDef",
    "ClientGetReservationPurchaseRecommendationServiceSpecificationTypeDef",
    "ClientGetReservationUtilizationFilterDimensionsTypeDef",
    "ClientGetReservationUtilizationFilterTagsTypeDef",
    "ClientGetReservationUtilizationFilterTypeDef",
    "ClientGetReservationUtilizationGroupByTypeDef",
    "ClientGetReservationUtilizationResponseTotalTypeDef",
    "ClientGetReservationUtilizationResponseUtilizationsByTimeGroupsUtilizationTypeDef",
    "ClientGetReservationUtilizationResponseUtilizationsByTimeGroupsTypeDef",
    "ClientGetReservationUtilizationResponseUtilizationsByTimeTimePeriodTypeDef",
    "ClientGetReservationUtilizationResponseUtilizationsByTimeTotalTypeDef",
    "ClientGetReservationUtilizationResponseUtilizationsByTimeTypeDef",
    "ClientGetReservationUtilizationResponseTypeDef",
    "ClientGetReservationUtilizationTimePeriodTypeDef",
    "ClientGetRightsizingRecommendationFilterDimensionsTypeDef",
    "ClientGetRightsizingRecommendationFilterTagsTypeDef",
    "ClientGetRightsizingRecommendationFilterTypeDef",
    "ClientGetRightsizingRecommendationResponseMetadataTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceDetailsEC2ResourceDetailsTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceDetailsTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceUtilizationEC2ResourceUtilizationTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceUtilizationTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceTagsTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesExpectedResourceUtilizationEC2ResourceUtilizationTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesExpectedResourceUtilizationTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesResourceDetailsEC2ResourceDetailsTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesResourceDetailsTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsTerminateRecommendationDetailTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsTypeDef",
    "ClientGetRightsizingRecommendationResponseSummaryTypeDef",
    "ClientGetRightsizingRecommendationResponseTypeDef",
    "ClientGetSavingsPlansCoverageFilterDimensionsTypeDef",
    "ClientGetSavingsPlansCoverageFilterTagsTypeDef",
    "ClientGetSavingsPlansCoverageFilterTypeDef",
    "ClientGetSavingsPlansCoverageGroupByTypeDef",
    "ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesCoverageTypeDef",
    "ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesTimePeriodTypeDef",
    "ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesTypeDef",
    "ClientGetSavingsPlansCoverageResponseTypeDef",
    "ClientGetSavingsPlansCoverageTimePeriodTypeDef",
    "ClientGetSavingsPlansPurchaseRecommendationResponseMetadataTypeDef",
    "ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationDetailsSavingsPlansDetailsTypeDef",
    "ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationDetailsTypeDef",
    "ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationSummaryTypeDef",
    "ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationTypeDef",
    "ClientGetSavingsPlansPurchaseRecommendationResponseTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsFilterDimensionsTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsFilterTagsTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsFilterTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsAmortizedCommitmentTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsSavingsTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsUtilizationTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsResponseTimePeriodTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsResponseTotalAmortizedCommitmentTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsResponseTotalSavingsTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsResponseTotalUtilizationTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsResponseTotalTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsResponseTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsTimePeriodTypeDef",
    "ClientGetSavingsPlansUtilizationFilterDimensionsTypeDef",
    "ClientGetSavingsPlansUtilizationFilterTagsTypeDef",
    "ClientGetSavingsPlansUtilizationFilterTypeDef",
    "ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeAmortizedCommitmentTypeDef",
    "ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeSavingsTypeDef",
    "ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeTimePeriodTypeDef",
    "ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeUtilizationTypeDef",
    "ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeTypeDef",
    "ClientGetSavingsPlansUtilizationResponseTotalAmortizedCommitmentTypeDef",
    "ClientGetSavingsPlansUtilizationResponseTotalSavingsTypeDef",
    "ClientGetSavingsPlansUtilizationResponseTotalUtilizationTypeDef",
    "ClientGetSavingsPlansUtilizationResponseTotalTypeDef",
    "ClientGetSavingsPlansUtilizationResponseTypeDef",
    "ClientGetSavingsPlansUtilizationTimePeriodTypeDef",
    "ClientGetTagsResponseTypeDef",
    "ClientGetTagsTimePeriodTypeDef",
    "ClientGetUsageForecastFilterDimensionsTypeDef",
    "ClientGetUsageForecastFilterTagsTypeDef",
    "ClientGetUsageForecastFilterTypeDef",
    "ClientGetUsageForecastResponseForecastResultsByTimeTimePeriodTypeDef",
    "ClientGetUsageForecastResponseForecastResultsByTimeTypeDef",
    "ClientGetUsageForecastResponseTotalTypeDef",
    "ClientGetUsageForecastResponseTypeDef",
    "ClientGetUsageForecastTimePeriodTypeDef",
)


_ClientGetCostAndUsageFilterDimensionsTypeDef = TypedDict(
    "_ClientGetCostAndUsageFilterDimensionsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetCostAndUsageFilterDimensionsTypeDef(
    _ClientGetCostAndUsageFilterDimensionsTypeDef
):
    """
    Type definition for `ClientGetCostAndUsageFilter` `Dimensions`

    The specific ``Dimension`` to use for ``Expression`` .

    - **Key** *(string) --*

      The names of the metadata types that you can use to filter and group your results. For
      example, ``AZ`` returns a list of Availability Zones.

    - **Values** *(list) --*

      The metadata values that you can use to filter and group your results. You can use
      ``GetDimensionValues`` to find specific values.

      Valid values for the ``SERVICE`` dimension are ``Amazon Elastic Compute Cloud - Compute`` ,
      ``Amazon Elasticsearch Service`` , ``Amazon ElastiCache`` , ``Amazon Redshift`` , and
      ``Amazon Relational Database Service`` .

      - *(string) --*
    """


_ClientGetCostAndUsageFilterTagsTypeDef = TypedDict(
    "_ClientGetCostAndUsageFilterTagsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetCostAndUsageFilterTagsTypeDef(_ClientGetCostAndUsageFilterTagsTypeDef):
    """
    Type definition for `ClientGetCostAndUsageFilter` `Tags`

    The specific ``Tag`` to use for ``Expression`` .

    - **Key** *(string) --*

      The key for the tag.

    - **Values** *(list) --*

      The specific value of the tag.

      - *(string) --*
    """


_ClientGetCostAndUsageFilterTypeDef = TypedDict(
    "_ClientGetCostAndUsageFilterTypeDef",
    {
        "Or": List[Dict],
        "And": List[Dict],
        "Not": Dict,
        "Dimensions": ClientGetCostAndUsageFilterDimensionsTypeDef,
        "Tags": ClientGetCostAndUsageFilterTagsTypeDef,
    },
    total=False,
)


class ClientGetCostAndUsageFilterTypeDef(_ClientGetCostAndUsageFilterTypeDef):
    """
    Type definition for `ClientGetCostAndUsage` `Filter`

    Filters AWS costs by different dimensions. For example, you can specify ``SERVICE`` and
    ``LINKED_ACCOUNT`` and get the costs that are associated with that account's usage of that
    service. You can nest ``Expression`` objects to define any combination of dimension filters. For
    more information, see `Expression
    <http://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html>`__ .

    - **Or** *(list) --*

      Return results that match either ``Dimension`` object.

      - *(dict) --*

        Use ``Expression`` to filter by cost or by usage. There are two patterns:

        * Simple dimension values - You can set the dimension name and values for the filters that
        you plan to use. For example, you can filter for ``REGION==us-east-1 OR REGION==us-west-1`` .
        The ``Expression`` for that looks like this:  ``{ "Dimensions": { "Key": "REGION", "Values":
        [ "us-east-1", “us-west-1” ] } }``   The list of dimension values are OR'd together to
        retrieve cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects
        using either ``with*`` methods or ``set*`` methods in multiple lines.

        * Compound dimension values with logical operations - You can use multiple ``Expression``
        types and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression``
        objects. This allows you to filter on more advanced options. For example, you can filter on
        ``((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE !=
        DataTransfer)`` . The ``Expression`` for that looks like this:  ``{ "And": [ {"Or": [
        {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": {
        "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE",
        "Values": ["DataTransfer"] }}} ] }``

        .. note::

           Because each ``Expression`` can have only one operator, the service returns an error if
           more than one is specified. The following example shows an ``Expression`` object that
           creates an error.

          ``{ "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [
          "DataTransfer" ] } }``

        .. note::

          For ``GetRightsizingRecommendation`` action, a combination of OR and NOT is not supported.
          OR is not supported between different dimensions, or dimensions and tags. NOT operators
          aren't supported. Dimensions are also limited to ``LINKED_ACCOUNT`` , ``REGION`` , or
          ``RIGHTSIZING_TYPE`` .

    - **And** *(list) --*

      Return results that match both ``Dimension`` objects.

      - *(dict) --*

        Use ``Expression`` to filter by cost or by usage. There are two patterns:

        * Simple dimension values - You can set the dimension name and values for the filters that
        you plan to use. For example, you can filter for ``REGION==us-east-1 OR REGION==us-west-1`` .
        The ``Expression`` for that looks like this:  ``{ "Dimensions": { "Key": "REGION", "Values":
        [ "us-east-1", “us-west-1” ] } }``   The list of dimension values are OR'd together to
        retrieve cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects
        using either ``with*`` methods or ``set*`` methods in multiple lines.

        * Compound dimension values with logical operations - You can use multiple ``Expression``
        types and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression``
        objects. This allows you to filter on more advanced options. For example, you can filter on
        ``((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE !=
        DataTransfer)`` . The ``Expression`` for that looks like this:  ``{ "And": [ {"Or": [
        {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": {
        "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE",
        "Values": ["DataTransfer"] }}} ] }``

        .. note::

           Because each ``Expression`` can have only one operator, the service returns an error if
           more than one is specified. The following example shows an ``Expression`` object that
           creates an error.

          ``{ "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [
          "DataTransfer" ] } }``

        .. note::

          For ``GetRightsizingRecommendation`` action, a combination of OR and NOT is not supported.
          OR is not supported between different dimensions, or dimensions and tags. NOT operators
          aren't supported. Dimensions are also limited to ``LINKED_ACCOUNT`` , ``REGION`` , or
          ``RIGHTSIZING_TYPE`` .

    - **Not** *(dict) --*

      Return results that don't match a ``Dimension`` object.

    - **Dimensions** *(dict) --*

      The specific ``Dimension`` to use for ``Expression`` .

      - **Key** *(string) --*

        The names of the metadata types that you can use to filter and group your results. For
        example, ``AZ`` returns a list of Availability Zones.

      - **Values** *(list) --*

        The metadata values that you can use to filter and group your results. You can use
        ``GetDimensionValues`` to find specific values.

        Valid values for the ``SERVICE`` dimension are ``Amazon Elastic Compute Cloud - Compute`` ,
        ``Amazon Elasticsearch Service`` , ``Amazon ElastiCache`` , ``Amazon Redshift`` , and
        ``Amazon Relational Database Service`` .

        - *(string) --*

    - **Tags** *(dict) --*

      The specific ``Tag`` to use for ``Expression`` .

      - **Key** *(string) --*

        The key for the tag.

      - **Values** *(list) --*

        The specific value of the tag.

        - *(string) --*
    """


_ClientGetCostAndUsageGroupByTypeDef = TypedDict(
    "_ClientGetCostAndUsageGroupByTypeDef", {"Type": str, "Key": str}, total=False
)


class ClientGetCostAndUsageGroupByTypeDef(_ClientGetCostAndUsageGroupByTypeDef):
    """
    Type definition for `ClientGetCostAndUsage` `GroupBy`

    Represents a group when you specify a group by criteria or in the response to a query with a
    specific grouping.

    - **Type** *(string) --*

      The string that represents the type of group.

    - **Key** *(string) --*

      The string that represents a key for a specified group.
    """


_ClientGetCostAndUsageResponseGroupDefinitionsTypeDef = TypedDict(
    "_ClientGetCostAndUsageResponseGroupDefinitionsTypeDef",
    {"Type": str, "Key": str},
    total=False,
)


class ClientGetCostAndUsageResponseGroupDefinitionsTypeDef(
    _ClientGetCostAndUsageResponseGroupDefinitionsTypeDef
):
    """
    Type definition for `ClientGetCostAndUsageResponse` `GroupDefinitions`

    Represents a group when you specify a group by criteria or in the response to a query with
    a specific grouping.

    - **Type** *(string) --*

      The string that represents the type of group.

    - **Key** *(string) --*

      The string that represents a key for a specified group.
    """


_ClientGetCostAndUsageResponseResultsByTimeGroupsMetricsTypeDef = TypedDict(
    "_ClientGetCostAndUsageResponseResultsByTimeGroupsMetricsTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientGetCostAndUsageResponseResultsByTimeGroupsMetricsTypeDef(
    _ClientGetCostAndUsageResponseResultsByTimeGroupsMetricsTypeDef
):
    """
    Type definition for `ClientGetCostAndUsageResponseResultsByTimeGroups` `Metrics`

    The aggregated value for a metric.

    - **Amount** *(string) --*

      The actual number that represents the metric.

    - **Unit** *(string) --*

      The unit that the metric is given in.
    """


_ClientGetCostAndUsageResponseResultsByTimeGroupsTypeDef = TypedDict(
    "_ClientGetCostAndUsageResponseResultsByTimeGroupsTypeDef",
    {
        "Keys": List[str],
        "Metrics": Dict[
            str, ClientGetCostAndUsageResponseResultsByTimeGroupsMetricsTypeDef
        ],
    },
    total=False,
)


class ClientGetCostAndUsageResponseResultsByTimeGroupsTypeDef(
    _ClientGetCostAndUsageResponseResultsByTimeGroupsTypeDef
):
    """
    Type definition for `ClientGetCostAndUsageResponseResultsByTime` `Groups`

    One level of grouped data in the results.

    - **Keys** *(list) --*

      The keys that are included in this group.

      - *(string) --*

    - **Metrics** *(dict) --*

      The metrics that are included in this group.

      - *(string) --*

        - *(dict) --*

          The aggregated value for a metric.

          - **Amount** *(string) --*

            The actual number that represents the metric.

          - **Unit** *(string) --*

            The unit that the metric is given in.
    """


_ClientGetCostAndUsageResponseResultsByTimeTimePeriodTypeDef = TypedDict(
    "_ClientGetCostAndUsageResponseResultsByTimeTimePeriodTypeDef",
    {"Start": str, "End": str},
    total=False,
)


class ClientGetCostAndUsageResponseResultsByTimeTimePeriodTypeDef(
    _ClientGetCostAndUsageResponseResultsByTimeTimePeriodTypeDef
):
    """
    Type definition for `ClientGetCostAndUsageResponseResultsByTime` `TimePeriod`

    The time period that the result covers.

    - **Start** *(string) --*

      The beginning of the time period that you want the usage and costs for. The start date
      is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and
      usage data starting at ``2017-01-01`` up to the end date.

    - **End** *(string) --*

      The end of the time period that you want the usage and costs for. The end date is
      exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage
      data from the start date up to, but not including, ``2017-05-01`` .
    """


_ClientGetCostAndUsageResponseResultsByTimeTotalTypeDef = TypedDict(
    "_ClientGetCostAndUsageResponseResultsByTimeTotalTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientGetCostAndUsageResponseResultsByTimeTotalTypeDef(
    _ClientGetCostAndUsageResponseResultsByTimeTotalTypeDef
):
    """
    Type definition for `ClientGetCostAndUsageResponseResultsByTime` `Total`

    The aggregated value for a metric.

    - **Amount** *(string) --*

      The actual number that represents the metric.

    - **Unit** *(string) --*

      The unit that the metric is given in.
    """


_ClientGetCostAndUsageResponseResultsByTimeTypeDef = TypedDict(
    "_ClientGetCostAndUsageResponseResultsByTimeTypeDef",
    {
        "TimePeriod": ClientGetCostAndUsageResponseResultsByTimeTimePeriodTypeDef,
        "Total": Dict[str, ClientGetCostAndUsageResponseResultsByTimeTotalTypeDef],
        "Groups": List[ClientGetCostAndUsageResponseResultsByTimeGroupsTypeDef],
        "Estimated": bool,
    },
    total=False,
)


class ClientGetCostAndUsageResponseResultsByTimeTypeDef(
    _ClientGetCostAndUsageResponseResultsByTimeTypeDef
):
    """
    Type definition for `ClientGetCostAndUsageResponse` `ResultsByTime`

    The result that is associated with a time period.

    - **TimePeriod** *(dict) --*

      The time period that the result covers.

      - **Start** *(string) --*

        The beginning of the time period that you want the usage and costs for. The start date
        is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and
        usage data starting at ``2017-01-01`` up to the end date.

      - **End** *(string) --*

        The end of the time period that you want the usage and costs for. The end date is
        exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage
        data from the start date up to, but not including, ``2017-05-01`` .

    - **Total** *(dict) --*

      The total amount of cost or usage accrued during the time period.

      - *(string) --*

        - *(dict) --*

          The aggregated value for a metric.

          - **Amount** *(string) --*

            The actual number that represents the metric.

          - **Unit** *(string) --*

            The unit that the metric is given in.

    - **Groups** *(list) --*

      The groups that this time period includes.

      - *(dict) --*

        One level of grouped data in the results.

        - **Keys** *(list) --*

          The keys that are included in this group.

          - *(string) --*

        - **Metrics** *(dict) --*

          The metrics that are included in this group.

          - *(string) --*

            - *(dict) --*

              The aggregated value for a metric.

              - **Amount** *(string) --*

                The actual number that represents the metric.

              - **Unit** *(string) --*

                The unit that the metric is given in.

    - **Estimated** *(boolean) --*

      Whether the result is estimated.
    """


_ClientGetCostAndUsageResponseTypeDef = TypedDict(
    "_ClientGetCostAndUsageResponseTypeDef",
    {
        "NextPageToken": str,
        "GroupDefinitions": List[ClientGetCostAndUsageResponseGroupDefinitionsTypeDef],
        "ResultsByTime": List[ClientGetCostAndUsageResponseResultsByTimeTypeDef],
    },
    total=False,
)


class ClientGetCostAndUsageResponseTypeDef(_ClientGetCostAndUsageResponseTypeDef):
    """
    Type definition for `ClientGetCostAndUsage` `Response`

    - **NextPageToken** *(string) --*

      The token for the next set of retrievable results. AWS provides the token when the response
      from a previous call has more results than the maximum page size.

    - **GroupDefinitions** *(list) --*

      The groups that are specified by the ``Filter`` or ``GroupBy`` parameters in the request.

      - *(dict) --*

        Represents a group when you specify a group by criteria or in the response to a query with
        a specific grouping.

        - **Type** *(string) --*

          The string that represents the type of group.

        - **Key** *(string) --*

          The string that represents a key for a specified group.

    - **ResultsByTime** *(list) --*

      The time period that is covered by the results in the response.

      - *(dict) --*

        The result that is associated with a time period.

        - **TimePeriod** *(dict) --*

          The time period that the result covers.

          - **Start** *(string) --*

            The beginning of the time period that you want the usage and costs for. The start date
            is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and
            usage data starting at ``2017-01-01`` up to the end date.

          - **End** *(string) --*

            The end of the time period that you want the usage and costs for. The end date is
            exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage
            data from the start date up to, but not including, ``2017-05-01`` .

        - **Total** *(dict) --*

          The total amount of cost or usage accrued during the time period.

          - *(string) --*

            - *(dict) --*

              The aggregated value for a metric.

              - **Amount** *(string) --*

                The actual number that represents the metric.

              - **Unit** *(string) --*

                The unit that the metric is given in.

        - **Groups** *(list) --*

          The groups that this time period includes.

          - *(dict) --*

            One level of grouped data in the results.

            - **Keys** *(list) --*

              The keys that are included in this group.

              - *(string) --*

            - **Metrics** *(dict) --*

              The metrics that are included in this group.

              - *(string) --*

                - *(dict) --*

                  The aggregated value for a metric.

                  - **Amount** *(string) --*

                    The actual number that represents the metric.

                  - **Unit** *(string) --*

                    The unit that the metric is given in.

        - **Estimated** *(boolean) --*

          Whether the result is estimated.
    """


_ClientGetCostAndUsageTimePeriodTypeDef = TypedDict(
    "_ClientGetCostAndUsageTimePeriodTypeDef", {"Start": str, "End": str}
)


class ClientGetCostAndUsageTimePeriodTypeDef(_ClientGetCostAndUsageTimePeriodTypeDef):
    """
    Type definition for `ClientGetCostAndUsage` `TimePeriod`

    Sets the start and end dates for retrieving AWS costs. The start date is inclusive, but the end
    date is exclusive. For example, if ``start`` is ``2017-01-01`` and ``end`` is ``2017-05-01`` ,
    then the cost and usage data is retrieved from ``2017-01-01`` up to and including ``2017-04-30``
    but not including ``2017-05-01`` .

    - **Start** *(string) --* **[REQUIRED]**

      The beginning of the time period that you want the usage and costs for. The start date is
      inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data
      starting at ``2017-01-01`` up to the end date.

    - **End** *(string) --* **[REQUIRED]**

      The end of the time period that you want the usage and costs for. The end date is exclusive.
      For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage data from the start
      date up to, but not including, ``2017-05-01`` .
    """


_ClientGetCostAndUsageWithResourcesFilterDimensionsTypeDef = TypedDict(
    "_ClientGetCostAndUsageWithResourcesFilterDimensionsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetCostAndUsageWithResourcesFilterDimensionsTypeDef(
    _ClientGetCostAndUsageWithResourcesFilterDimensionsTypeDef
):
    """
    Type definition for `ClientGetCostAndUsageWithResourcesFilter` `Dimensions`

    The specific ``Dimension`` to use for ``Expression`` .

    - **Key** *(string) --*

      The names of the metadata types that you can use to filter and group your results. For
      example, ``AZ`` returns a list of Availability Zones.

    - **Values** *(list) --*

      The metadata values that you can use to filter and group your results. You can use
      ``GetDimensionValues`` to find specific values.

      Valid values for the ``SERVICE`` dimension are ``Amazon Elastic Compute Cloud - Compute`` ,
      ``Amazon Elasticsearch Service`` , ``Amazon ElastiCache`` , ``Amazon Redshift`` , and
      ``Amazon Relational Database Service`` .

      - *(string) --*
    """


_ClientGetCostAndUsageWithResourcesFilterTagsTypeDef = TypedDict(
    "_ClientGetCostAndUsageWithResourcesFilterTagsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetCostAndUsageWithResourcesFilterTagsTypeDef(
    _ClientGetCostAndUsageWithResourcesFilterTagsTypeDef
):
    """
    Type definition for `ClientGetCostAndUsageWithResourcesFilter` `Tags`

    The specific ``Tag`` to use for ``Expression`` .

    - **Key** *(string) --*

      The key for the tag.

    - **Values** *(list) --*

      The specific value of the tag.

      - *(string) --*
    """


_ClientGetCostAndUsageWithResourcesFilterTypeDef = TypedDict(
    "_ClientGetCostAndUsageWithResourcesFilterTypeDef",
    {
        "Or": List[Dict],
        "And": List[Dict],
        "Not": Dict,
        "Dimensions": ClientGetCostAndUsageWithResourcesFilterDimensionsTypeDef,
        "Tags": ClientGetCostAndUsageWithResourcesFilterTagsTypeDef,
    },
    total=False,
)


class ClientGetCostAndUsageWithResourcesFilterTypeDef(
    _ClientGetCostAndUsageWithResourcesFilterTypeDef
):
    """
    Type definition for `ClientGetCostAndUsageWithResources` `Filter`

    Filters Amazon Web Services costs by different dimensions. For example, you can specify
    ``SERVICE`` and ``LINKED_ACCOUNT`` and get the costs that are associated with that account's
    usage of that service. You can nest ``Expression`` objects to define any combination of dimension
    filters. For more information, see `Expression
    <http://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html>`__ .

    The ``GetCostAndUsageWithResources`` operation requires that you either group by or filter by a
    ``ResourceId`` .

    - **Or** *(list) --*

      Return results that match either ``Dimension`` object.

      - *(dict) --*

        Use ``Expression`` to filter by cost or by usage. There are two patterns:

        * Simple dimension values - You can set the dimension name and values for the filters that
        you plan to use. For example, you can filter for ``REGION==us-east-1 OR REGION==us-west-1`` .
        The ``Expression`` for that looks like this:  ``{ "Dimensions": { "Key": "REGION", "Values":
        [ "us-east-1", “us-west-1” ] } }``   The list of dimension values are OR'd together to
        retrieve cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects
        using either ``with*`` methods or ``set*`` methods in multiple lines.

        * Compound dimension values with logical operations - You can use multiple ``Expression``
        types and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression``
        objects. This allows you to filter on more advanced options. For example, you can filter on
        ``((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE !=
        DataTransfer)`` . The ``Expression`` for that looks like this:  ``{ "And": [ {"Or": [
        {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": {
        "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE",
        "Values": ["DataTransfer"] }}} ] }``

        .. note::

           Because each ``Expression`` can have only one operator, the service returns an error if
           more than one is specified. The following example shows an ``Expression`` object that
           creates an error.

          ``{ "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [
          "DataTransfer" ] } }``

        .. note::

          For ``GetRightsizingRecommendation`` action, a combination of OR and NOT is not supported.
          OR is not supported between different dimensions, or dimensions and tags. NOT operators
          aren't supported. Dimensions are also limited to ``LINKED_ACCOUNT`` , ``REGION`` , or
          ``RIGHTSIZING_TYPE`` .

    - **And** *(list) --*

      Return results that match both ``Dimension`` objects.

      - *(dict) --*

        Use ``Expression`` to filter by cost or by usage. There are two patterns:

        * Simple dimension values - You can set the dimension name and values for the filters that
        you plan to use. For example, you can filter for ``REGION==us-east-1 OR REGION==us-west-1`` .
        The ``Expression`` for that looks like this:  ``{ "Dimensions": { "Key": "REGION", "Values":
        [ "us-east-1", “us-west-1” ] } }``   The list of dimension values are OR'd together to
        retrieve cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects
        using either ``with*`` methods or ``set*`` methods in multiple lines.

        * Compound dimension values with logical operations - You can use multiple ``Expression``
        types and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression``
        objects. This allows you to filter on more advanced options. For example, you can filter on
        ``((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE !=
        DataTransfer)`` . The ``Expression`` for that looks like this:  ``{ "And": [ {"Or": [
        {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": {
        "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE",
        "Values": ["DataTransfer"] }}} ] }``

        .. note::

           Because each ``Expression`` can have only one operator, the service returns an error if
           more than one is specified. The following example shows an ``Expression`` object that
           creates an error.

          ``{ "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [
          "DataTransfer" ] } }``

        .. note::

          For ``GetRightsizingRecommendation`` action, a combination of OR and NOT is not supported.
          OR is not supported between different dimensions, or dimensions and tags. NOT operators
          aren't supported. Dimensions are also limited to ``LINKED_ACCOUNT`` , ``REGION`` , or
          ``RIGHTSIZING_TYPE`` .

    - **Not** *(dict) --*

      Return results that don't match a ``Dimension`` object.

    - **Dimensions** *(dict) --*

      The specific ``Dimension`` to use for ``Expression`` .

      - **Key** *(string) --*

        The names of the metadata types that you can use to filter and group your results. For
        example, ``AZ`` returns a list of Availability Zones.

      - **Values** *(list) --*

        The metadata values that you can use to filter and group your results. You can use
        ``GetDimensionValues`` to find specific values.

        Valid values for the ``SERVICE`` dimension are ``Amazon Elastic Compute Cloud - Compute`` ,
        ``Amazon Elasticsearch Service`` , ``Amazon ElastiCache`` , ``Amazon Redshift`` , and
        ``Amazon Relational Database Service`` .

        - *(string) --*

    - **Tags** *(dict) --*

      The specific ``Tag`` to use for ``Expression`` .

      - **Key** *(string) --*

        The key for the tag.

      - **Values** *(list) --*

        The specific value of the tag.

        - *(string) --*
    """


_ClientGetCostAndUsageWithResourcesGroupByTypeDef = TypedDict(
    "_ClientGetCostAndUsageWithResourcesGroupByTypeDef",
    {"Type": str, "Key": str},
    total=False,
)


class ClientGetCostAndUsageWithResourcesGroupByTypeDef(
    _ClientGetCostAndUsageWithResourcesGroupByTypeDef
):
    """
    Type definition for `ClientGetCostAndUsageWithResources` `GroupBy`

    Represents a group when you specify a group by criteria or in the response to a query with a
    specific grouping.

    - **Type** *(string) --*

      The string that represents the type of group.

    - **Key** *(string) --*

      The string that represents a key for a specified group.
    """


_ClientGetCostAndUsageWithResourcesResponseGroupDefinitionsTypeDef = TypedDict(
    "_ClientGetCostAndUsageWithResourcesResponseGroupDefinitionsTypeDef",
    {"Type": str, "Key": str},
    total=False,
)


class ClientGetCostAndUsageWithResourcesResponseGroupDefinitionsTypeDef(
    _ClientGetCostAndUsageWithResourcesResponseGroupDefinitionsTypeDef
):
    """
    Type definition for `ClientGetCostAndUsageWithResourcesResponse` `GroupDefinitions`

    Represents a group when you specify a group by criteria or in the response to a query with
    a specific grouping.

    - **Type** *(string) --*

      The string that represents the type of group.

    - **Key** *(string) --*

      The string that represents a key for a specified group.
    """


_ClientGetCostAndUsageWithResourcesResponseResultsByTimeGroupsMetricsTypeDef = TypedDict(
    "_ClientGetCostAndUsageWithResourcesResponseResultsByTimeGroupsMetricsTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientGetCostAndUsageWithResourcesResponseResultsByTimeGroupsMetricsTypeDef(
    _ClientGetCostAndUsageWithResourcesResponseResultsByTimeGroupsMetricsTypeDef
):
    """
    Type definition for `ClientGetCostAndUsageWithResourcesResponseResultsByTimeGroups` `Metrics`

    The aggregated value for a metric.

    - **Amount** *(string) --*

      The actual number that represents the metric.

    - **Unit** *(string) --*

      The unit that the metric is given in.
    """


_ClientGetCostAndUsageWithResourcesResponseResultsByTimeGroupsTypeDef = TypedDict(
    "_ClientGetCostAndUsageWithResourcesResponseResultsByTimeGroupsTypeDef",
    {
        "Keys": List[str],
        "Metrics": Dict[
            str,
            ClientGetCostAndUsageWithResourcesResponseResultsByTimeGroupsMetricsTypeDef,
        ],
    },
    total=False,
)


class ClientGetCostAndUsageWithResourcesResponseResultsByTimeGroupsTypeDef(
    _ClientGetCostAndUsageWithResourcesResponseResultsByTimeGroupsTypeDef
):
    """
    Type definition for `ClientGetCostAndUsageWithResourcesResponseResultsByTime` `Groups`

    One level of grouped data in the results.

    - **Keys** *(list) --*

      The keys that are included in this group.

      - *(string) --*

    - **Metrics** *(dict) --*

      The metrics that are included in this group.

      - *(string) --*

        - *(dict) --*

          The aggregated value for a metric.

          - **Amount** *(string) --*

            The actual number that represents the metric.

          - **Unit** *(string) --*

            The unit that the metric is given in.
    """


_ClientGetCostAndUsageWithResourcesResponseResultsByTimeTimePeriodTypeDef = TypedDict(
    "_ClientGetCostAndUsageWithResourcesResponseResultsByTimeTimePeriodTypeDef",
    {"Start": str, "End": str},
    total=False,
)


class ClientGetCostAndUsageWithResourcesResponseResultsByTimeTimePeriodTypeDef(
    _ClientGetCostAndUsageWithResourcesResponseResultsByTimeTimePeriodTypeDef
):
    """
    Type definition for `ClientGetCostAndUsageWithResourcesResponseResultsByTime` `TimePeriod`

    The time period that the result covers.

    - **Start** *(string) --*

      The beginning of the time period that you want the usage and costs for. The start date
      is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and
      usage data starting at ``2017-01-01`` up to the end date.

    - **End** *(string) --*

      The end of the time period that you want the usage and costs for. The end date is
      exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage
      data from the start date up to, but not including, ``2017-05-01`` .
    """


_ClientGetCostAndUsageWithResourcesResponseResultsByTimeTotalTypeDef = TypedDict(
    "_ClientGetCostAndUsageWithResourcesResponseResultsByTimeTotalTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientGetCostAndUsageWithResourcesResponseResultsByTimeTotalTypeDef(
    _ClientGetCostAndUsageWithResourcesResponseResultsByTimeTotalTypeDef
):
    """
    Type definition for `ClientGetCostAndUsageWithResourcesResponseResultsByTime` `Total`

    The aggregated value for a metric.

    - **Amount** *(string) --*

      The actual number that represents the metric.

    - **Unit** *(string) --*

      The unit that the metric is given in.
    """


_ClientGetCostAndUsageWithResourcesResponseResultsByTimeTypeDef = TypedDict(
    "_ClientGetCostAndUsageWithResourcesResponseResultsByTimeTypeDef",
    {
        "TimePeriod": ClientGetCostAndUsageWithResourcesResponseResultsByTimeTimePeriodTypeDef,
        "Total": Dict[
            str, ClientGetCostAndUsageWithResourcesResponseResultsByTimeTotalTypeDef
        ],
        "Groups": List[
            ClientGetCostAndUsageWithResourcesResponseResultsByTimeGroupsTypeDef
        ],
        "Estimated": bool,
    },
    total=False,
)


class ClientGetCostAndUsageWithResourcesResponseResultsByTimeTypeDef(
    _ClientGetCostAndUsageWithResourcesResponseResultsByTimeTypeDef
):
    """
    Type definition for `ClientGetCostAndUsageWithResourcesResponse` `ResultsByTime`

    The result that is associated with a time period.

    - **TimePeriod** *(dict) --*

      The time period that the result covers.

      - **Start** *(string) --*

        The beginning of the time period that you want the usage and costs for. The start date
        is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and
        usage data starting at ``2017-01-01`` up to the end date.

      - **End** *(string) --*

        The end of the time period that you want the usage and costs for. The end date is
        exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage
        data from the start date up to, but not including, ``2017-05-01`` .

    - **Total** *(dict) --*

      The total amount of cost or usage accrued during the time period.

      - *(string) --*

        - *(dict) --*

          The aggregated value for a metric.

          - **Amount** *(string) --*

            The actual number that represents the metric.

          - **Unit** *(string) --*

            The unit that the metric is given in.

    - **Groups** *(list) --*

      The groups that this time period includes.

      - *(dict) --*

        One level of grouped data in the results.

        - **Keys** *(list) --*

          The keys that are included in this group.

          - *(string) --*

        - **Metrics** *(dict) --*

          The metrics that are included in this group.

          - *(string) --*

            - *(dict) --*

              The aggregated value for a metric.

              - **Amount** *(string) --*

                The actual number that represents the metric.

              - **Unit** *(string) --*

                The unit that the metric is given in.

    - **Estimated** *(boolean) --*

      Whether the result is estimated.
    """


_ClientGetCostAndUsageWithResourcesResponseTypeDef = TypedDict(
    "_ClientGetCostAndUsageWithResourcesResponseTypeDef",
    {
        "NextPageToken": str,
        "GroupDefinitions": List[
            ClientGetCostAndUsageWithResourcesResponseGroupDefinitionsTypeDef
        ],
        "ResultsByTime": List[
            ClientGetCostAndUsageWithResourcesResponseResultsByTimeTypeDef
        ],
    },
    total=False,
)


class ClientGetCostAndUsageWithResourcesResponseTypeDef(
    _ClientGetCostAndUsageWithResourcesResponseTypeDef
):
    """
    Type definition for `ClientGetCostAndUsageWithResources` `Response`

    - **NextPageToken** *(string) --*

      The token for the next set of retrievable results. AWS provides the token when the response
      from a previous call has more results than the maximum page size.

    - **GroupDefinitions** *(list) --*

      The groups that are specified by the ``Filter`` or ``GroupBy`` parameters in the request.

      - *(dict) --*

        Represents a group when you specify a group by criteria or in the response to a query with
        a specific grouping.

        - **Type** *(string) --*

          The string that represents the type of group.

        - **Key** *(string) --*

          The string that represents a key for a specified group.

    - **ResultsByTime** *(list) --*

      The time period that is covered by the results in the response.

      - *(dict) --*

        The result that is associated with a time period.

        - **TimePeriod** *(dict) --*

          The time period that the result covers.

          - **Start** *(string) --*

            The beginning of the time period that you want the usage and costs for. The start date
            is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and
            usage data starting at ``2017-01-01`` up to the end date.

          - **End** *(string) --*

            The end of the time period that you want the usage and costs for. The end date is
            exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage
            data from the start date up to, but not including, ``2017-05-01`` .

        - **Total** *(dict) --*

          The total amount of cost or usage accrued during the time period.

          - *(string) --*

            - *(dict) --*

              The aggregated value for a metric.

              - **Amount** *(string) --*

                The actual number that represents the metric.

              - **Unit** *(string) --*

                The unit that the metric is given in.

        - **Groups** *(list) --*

          The groups that this time period includes.

          - *(dict) --*

            One level of grouped data in the results.

            - **Keys** *(list) --*

              The keys that are included in this group.

              - *(string) --*

            - **Metrics** *(dict) --*

              The metrics that are included in this group.

              - *(string) --*

                - *(dict) --*

                  The aggregated value for a metric.

                  - **Amount** *(string) --*

                    The actual number that represents the metric.

                  - **Unit** *(string) --*

                    The unit that the metric is given in.

        - **Estimated** *(boolean) --*

          Whether the result is estimated.
    """


_ClientGetCostAndUsageWithResourcesTimePeriodTypeDef = TypedDict(
    "_ClientGetCostAndUsageWithResourcesTimePeriodTypeDef", {"Start": str, "End": str}
)


class ClientGetCostAndUsageWithResourcesTimePeriodTypeDef(
    _ClientGetCostAndUsageWithResourcesTimePeriodTypeDef
):
    """
    Type definition for `ClientGetCostAndUsageWithResources` `TimePeriod`

    Sets the start and end dates for retrieving Amazon Web Services costs. The range must be within
    the last 14 days (the start date cannot be earlier than 14 days ago). The start date is
    inclusive, but the end date is exclusive. For example, if ``start`` is ``2017-01-01`` and ``end``
    is ``2017-05-01`` , then the cost and usage data is retrieved from ``2017-01-01`` up to and
    including ``2017-04-30`` but not including ``2017-05-01`` .

    - **Start** *(string) --* **[REQUIRED]**

      The beginning of the time period that you want the usage and costs for. The start date is
      inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data
      starting at ``2017-01-01`` up to the end date.

    - **End** *(string) --* **[REQUIRED]**

      The end of the time period that you want the usage and costs for. The end date is exclusive.
      For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage data from the start
      date up to, but not including, ``2017-05-01`` .
    """


_ClientGetCostForecastFilterDimensionsTypeDef = TypedDict(
    "_ClientGetCostForecastFilterDimensionsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetCostForecastFilterDimensionsTypeDef(
    _ClientGetCostForecastFilterDimensionsTypeDef
):
    """
    Type definition for `ClientGetCostForecastFilter` `Dimensions`

    The specific ``Dimension`` to use for ``Expression`` .

    - **Key** *(string) --*

      The names of the metadata types that you can use to filter and group your results. For
      example, ``AZ`` returns a list of Availability Zones.

    - **Values** *(list) --*

      The metadata values that you can use to filter and group your results. You can use
      ``GetDimensionValues`` to find specific values.

      Valid values for the ``SERVICE`` dimension are ``Amazon Elastic Compute Cloud - Compute`` ,
      ``Amazon Elasticsearch Service`` , ``Amazon ElastiCache`` , ``Amazon Redshift`` , and
      ``Amazon Relational Database Service`` .

      - *(string) --*
    """


_ClientGetCostForecastFilterTagsTypeDef = TypedDict(
    "_ClientGetCostForecastFilterTagsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetCostForecastFilterTagsTypeDef(_ClientGetCostForecastFilterTagsTypeDef):
    """
    Type definition for `ClientGetCostForecastFilter` `Tags`

    The specific ``Tag`` to use for ``Expression`` .

    - **Key** *(string) --*

      The key for the tag.

    - **Values** *(list) --*

      The specific value of the tag.

      - *(string) --*
    """


_ClientGetCostForecastFilterTypeDef = TypedDict(
    "_ClientGetCostForecastFilterTypeDef",
    {
        "Or": List[Dict],
        "And": List[Dict],
        "Not": Dict,
        "Dimensions": ClientGetCostForecastFilterDimensionsTypeDef,
        "Tags": ClientGetCostForecastFilterTagsTypeDef,
    },
    total=False,
)


class ClientGetCostForecastFilterTypeDef(_ClientGetCostForecastFilterTypeDef):
    """
    Type definition for `ClientGetCostForecast` `Filter`

    The filters that you want to use to filter your forecast. Cost Explorer API supports all of the
    Cost Explorer filters.

    - **Or** *(list) --*

      Return results that match either ``Dimension`` object.

      - *(dict) --*

        Use ``Expression`` to filter by cost or by usage. There are two patterns:

        * Simple dimension values - You can set the dimension name and values for the filters that
        you plan to use. For example, you can filter for ``REGION==us-east-1 OR REGION==us-west-1`` .
        The ``Expression`` for that looks like this:  ``{ "Dimensions": { "Key": "REGION", "Values":
        [ "us-east-1", “us-west-1” ] } }``   The list of dimension values are OR'd together to
        retrieve cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects
        using either ``with*`` methods or ``set*`` methods in multiple lines.

        * Compound dimension values with logical operations - You can use multiple ``Expression``
        types and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression``
        objects. This allows you to filter on more advanced options. For example, you can filter on
        ``((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE !=
        DataTransfer)`` . The ``Expression`` for that looks like this:  ``{ "And": [ {"Or": [
        {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": {
        "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE",
        "Values": ["DataTransfer"] }}} ] }``

        .. note::

           Because each ``Expression`` can have only one operator, the service returns an error if
           more than one is specified. The following example shows an ``Expression`` object that
           creates an error.

          ``{ "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [
          "DataTransfer" ] } }``

        .. note::

          For ``GetRightsizingRecommendation`` action, a combination of OR and NOT is not supported.
          OR is not supported between different dimensions, or dimensions and tags. NOT operators
          aren't supported. Dimensions are also limited to ``LINKED_ACCOUNT`` , ``REGION`` , or
          ``RIGHTSIZING_TYPE`` .

    - **And** *(list) --*

      Return results that match both ``Dimension`` objects.

      - *(dict) --*

        Use ``Expression`` to filter by cost or by usage. There are two patterns:

        * Simple dimension values - You can set the dimension name and values for the filters that
        you plan to use. For example, you can filter for ``REGION==us-east-1 OR REGION==us-west-1`` .
        The ``Expression`` for that looks like this:  ``{ "Dimensions": { "Key": "REGION", "Values":
        [ "us-east-1", “us-west-1” ] } }``   The list of dimension values are OR'd together to
        retrieve cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects
        using either ``with*`` methods or ``set*`` methods in multiple lines.

        * Compound dimension values with logical operations - You can use multiple ``Expression``
        types and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression``
        objects. This allows you to filter on more advanced options. For example, you can filter on
        ``((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE !=
        DataTransfer)`` . The ``Expression`` for that looks like this:  ``{ "And": [ {"Or": [
        {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": {
        "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE",
        "Values": ["DataTransfer"] }}} ] }``

        .. note::

           Because each ``Expression`` can have only one operator, the service returns an error if
           more than one is specified. The following example shows an ``Expression`` object that
           creates an error.

          ``{ "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [
          "DataTransfer" ] } }``

        .. note::

          For ``GetRightsizingRecommendation`` action, a combination of OR and NOT is not supported.
          OR is not supported between different dimensions, or dimensions and tags. NOT operators
          aren't supported. Dimensions are also limited to ``LINKED_ACCOUNT`` , ``REGION`` , or
          ``RIGHTSIZING_TYPE`` .

    - **Not** *(dict) --*

      Return results that don't match a ``Dimension`` object.

    - **Dimensions** *(dict) --*

      The specific ``Dimension`` to use for ``Expression`` .

      - **Key** *(string) --*

        The names of the metadata types that you can use to filter and group your results. For
        example, ``AZ`` returns a list of Availability Zones.

      - **Values** *(list) --*

        The metadata values that you can use to filter and group your results. You can use
        ``GetDimensionValues`` to find specific values.

        Valid values for the ``SERVICE`` dimension are ``Amazon Elastic Compute Cloud - Compute`` ,
        ``Amazon Elasticsearch Service`` , ``Amazon ElastiCache`` , ``Amazon Redshift`` , and
        ``Amazon Relational Database Service`` .

        - *(string) --*

    - **Tags** *(dict) --*

      The specific ``Tag`` to use for ``Expression`` .

      - **Key** *(string) --*

        The key for the tag.

      - **Values** *(list) --*

        The specific value of the tag.

        - *(string) --*
    """


_ClientGetCostForecastResponseForecastResultsByTimeTimePeriodTypeDef = TypedDict(
    "_ClientGetCostForecastResponseForecastResultsByTimeTimePeriodTypeDef",
    {"Start": str, "End": str},
    total=False,
)


class ClientGetCostForecastResponseForecastResultsByTimeTimePeriodTypeDef(
    _ClientGetCostForecastResponseForecastResultsByTimeTimePeriodTypeDef
):
    """
    Type definition for `ClientGetCostForecastResponseForecastResultsByTime` `TimePeriod`

    The period of time that the forecast covers.

    - **Start** *(string) --*

      The beginning of the time period that you want the usage and costs for. The start date
      is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and
      usage data starting at ``2017-01-01`` up to the end date.

    - **End** *(string) --*

      The end of the time period that you want the usage and costs for. The end date is
      exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage
      data from the start date up to, but not including, ``2017-05-01`` .
    """


_ClientGetCostForecastResponseForecastResultsByTimeTypeDef = TypedDict(
    "_ClientGetCostForecastResponseForecastResultsByTimeTypeDef",
    {
        "TimePeriod": ClientGetCostForecastResponseForecastResultsByTimeTimePeriodTypeDef,
        "MeanValue": str,
        "PredictionIntervalLowerBound": str,
        "PredictionIntervalUpperBound": str,
    },
    total=False,
)


class ClientGetCostForecastResponseForecastResultsByTimeTypeDef(
    _ClientGetCostForecastResponseForecastResultsByTimeTypeDef
):
    """
    Type definition for `ClientGetCostForecastResponse` `ForecastResultsByTime`

    The forecast created for your query.

    - **TimePeriod** *(dict) --*

      The period of time that the forecast covers.

      - **Start** *(string) --*

        The beginning of the time period that you want the usage and costs for. The start date
        is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and
        usage data starting at ``2017-01-01`` up to the end date.

      - **End** *(string) --*

        The end of the time period that you want the usage and costs for. The end date is
        exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage
        data from the start date up to, but not including, ``2017-05-01`` .

    - **MeanValue** *(string) --*

      The mean value of the forecast.

    - **PredictionIntervalLowerBound** *(string) --*

      The lower limit for the prediction interval.

    - **PredictionIntervalUpperBound** *(string) --*

      The upper limit for the prediction interval.
    """


_ClientGetCostForecastResponseTotalTypeDef = TypedDict(
    "_ClientGetCostForecastResponseTotalTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientGetCostForecastResponseTotalTypeDef(
    _ClientGetCostForecastResponseTotalTypeDef
):
    """
    Type definition for `ClientGetCostForecastResponse` `Total`

    How much you are forecasted to spend over the forecast period, in ``USD`` .

    - **Amount** *(string) --*

      The actual number that represents the metric.

    - **Unit** *(string) --*

      The unit that the metric is given in.
    """


_ClientGetCostForecastResponseTypeDef = TypedDict(
    "_ClientGetCostForecastResponseTypeDef",
    {
        "Total": ClientGetCostForecastResponseTotalTypeDef,
        "ForecastResultsByTime": List[
            ClientGetCostForecastResponseForecastResultsByTimeTypeDef
        ],
    },
    total=False,
)


class ClientGetCostForecastResponseTypeDef(_ClientGetCostForecastResponseTypeDef):
    """
    Type definition for `ClientGetCostForecast` `Response`

    - **Total** *(dict) --*

      How much you are forecasted to spend over the forecast period, in ``USD`` .

      - **Amount** *(string) --*

        The actual number that represents the metric.

      - **Unit** *(string) --*

        The unit that the metric is given in.

    - **ForecastResultsByTime** *(list) --*

      The forecasts for your query, in order. For ``DAILY`` forecasts, this is a list of days. For
      ``MONTHLY`` forecasts, this is a list of months.

      - *(dict) --*

        The forecast created for your query.

        - **TimePeriod** *(dict) --*

          The period of time that the forecast covers.

          - **Start** *(string) --*

            The beginning of the time period that you want the usage and costs for. The start date
            is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and
            usage data starting at ``2017-01-01`` up to the end date.

          - **End** *(string) --*

            The end of the time period that you want the usage and costs for. The end date is
            exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage
            data from the start date up to, but not including, ``2017-05-01`` .

        - **MeanValue** *(string) --*

          The mean value of the forecast.

        - **PredictionIntervalLowerBound** *(string) --*

          The lower limit for the prediction interval.

        - **PredictionIntervalUpperBound** *(string) --*

          The upper limit for the prediction interval.
    """


_ClientGetCostForecastTimePeriodTypeDef = TypedDict(
    "_ClientGetCostForecastTimePeriodTypeDef", {"Start": str, "End": str}
)


class ClientGetCostForecastTimePeriodTypeDef(_ClientGetCostForecastTimePeriodTypeDef):
    """
    Type definition for `ClientGetCostForecast` `TimePeriod`

    The period of time that you want the forecast to cover.

    - **Start** *(string) --* **[REQUIRED]**

      The beginning of the time period that you want the usage and costs for. The start date is
      inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data
      starting at ``2017-01-01`` up to the end date.

    - **End** *(string) --* **[REQUIRED]**

      The end of the time period that you want the usage and costs for. The end date is exclusive.
      For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage data from the start
      date up to, but not including, ``2017-05-01`` .
    """


_ClientGetDimensionValuesResponseDimensionValuesTypeDef = TypedDict(
    "_ClientGetDimensionValuesResponseDimensionValuesTypeDef",
    {"Value": str, "Attributes": Dict[str, str]},
    total=False,
)


class ClientGetDimensionValuesResponseDimensionValuesTypeDef(
    _ClientGetDimensionValuesResponseDimensionValuesTypeDef
):
    """
    Type definition for `ClientGetDimensionValuesResponse` `DimensionValues`

    The metadata of a specific type that you can use to filter and group your results. You can
    use ``GetDimensionValues`` to find specific values.

    - **Value** *(string) --*

      The value of a dimension with a specific attribute.

    - **Attributes** *(dict) --*

      The attribute that applies to a specific ``Dimension`` .

      - *(string) --*

        - *(string) --*
    """


_ClientGetDimensionValuesResponseTypeDef = TypedDict(
    "_ClientGetDimensionValuesResponseTypeDef",
    {
        "DimensionValues": List[ClientGetDimensionValuesResponseDimensionValuesTypeDef],
        "ReturnSize": int,
        "TotalSize": int,
        "NextPageToken": str,
    },
    total=False,
)


class ClientGetDimensionValuesResponseTypeDef(_ClientGetDimensionValuesResponseTypeDef):
    """
    Type definition for `ClientGetDimensionValues` `Response`

    - **DimensionValues** *(list) --*

      The filters that you used to filter your request. Some dimensions are available only for a
      specific context.

      If you set the context to ``COST_AND_USAGE`` , you can use the following dimensions for
      searching:

      * AZ - The Availability Zone. An example is ``us-east-1a`` .

      * DATABASE_ENGINE - The Amazon Relational Database Service database. Examples are Aurora or
      MySQL.

      * INSTANCE_TYPE - The type of Amazon EC2 instance. An example is ``m4.xlarge`` .

      * LEGAL_ENTITY_NAME - The name of the organization that sells you AWS services, such as
      Amazon Web Services.

      * LINKED_ACCOUNT - The description in the attribute map that includes the full name of the
      member account. The value field contains the AWS ID of the member account.

      * OPERATING_SYSTEM - The operating system. Examples are Windows or Linux.

      * OPERATION - The action performed. Examples include ``RunInstance`` and ``CreateBucket`` .

      * PLATFORM - The Amazon EC2 operating system. Examples are Windows or Linux.

      * PURCHASE_TYPE - The reservation type of the purchase to which this usage is related.
      Examples include On-Demand Instances and Standard Reserved Instances.

      * SERVICE - The AWS service such as Amazon DynamoDB.

      * USAGE_TYPE - The type of usage. An example is DataTransfer-In-Bytes. The response for the
      ``GetDimensionValues`` operation includes a unit attribute. Examples include GB and Hrs.

      * USAGE_TYPE_GROUP - The grouping of common usage types. An example is Amazon EC2: CloudWatch
      – Alarms. The response for this operation includes a unit attribute.

      * RECORD_TYPE - The different types of charges such as RI fees, usage costs, tax refunds, and
      credits.

      * RESOURCE_ID - The unique identifier of the resource. ResourceId is an opt-in feature only
      available for last 14 days for EC2-Compute Service.

      If you set the context to ``RESERVATIONS`` , you can use the following dimensions for
      searching:

      * AZ - The Availability Zone. An example is ``us-east-1a`` .

      * CACHE_ENGINE - The Amazon ElastiCache operating system. Examples are Windows or Linux.

      * DEPLOYMENT_OPTION - The scope of Amazon Relational Database Service deployments. Valid
      values are ``SingleAZ`` and ``MultiAZ`` .

      * INSTANCE_TYPE - The type of Amazon EC2 instance. An example is ``m4.xlarge`` .

      * LINKED_ACCOUNT - The description in the attribute map that includes the full name of the
      member account. The value field contains the AWS ID of the member account.

      * PLATFORM - The Amazon EC2 operating system. Examples are Windows or Linux.

      * REGION - The AWS Region.

      * SCOPE (Utilization only) - The scope of a Reserved Instance (RI). Values are regional or a
      single Availability Zone.

      * TAG (Coverage only) - The tags that are associated with a Reserved Instance (RI).

      * TENANCY - The tenancy of a resource. Examples are shared or dedicated.

      If you set the context to ``SAVINGS_PLANS`` , you can use the following dimensions for
      searching:

      * SAVINGS_PLANS_TYPE - Type of Savings Plans (EC2 Instance or Compute)

      * PAYMENT_OPTION - Payment option for the given Savings Plans (for example, All Upfront)

      * REGION - The AWS Region.

      * INSTANCE_TYPE_FAMILY - The family of instances (For example, ``m5`` )

      * LINKED_ACCOUNT - The description in the attribute map that includes the full name of the
      member account. The value field contains the AWS ID of the member account.

      * SAVINGS_PLAN_ARN - The unique identifier for your Savings Plan

      - *(dict) --*

        The metadata of a specific type that you can use to filter and group your results. You can
        use ``GetDimensionValues`` to find specific values.

        - **Value** *(string) --*

          The value of a dimension with a specific attribute.

        - **Attributes** *(dict) --*

          The attribute that applies to a specific ``Dimension`` .

          - *(string) --*

            - *(string) --*

    - **ReturnSize** *(integer) --*

      The number of results that AWS returned at one time.

    - **TotalSize** *(integer) --*

      The total number of search results.

    - **NextPageToken** *(string) --*

      The token for the next set of retrievable results. AWS provides the token when the response
      from a previous call has more results than the maximum page size.
    """


_ClientGetDimensionValuesTimePeriodTypeDef = TypedDict(
    "_ClientGetDimensionValuesTimePeriodTypeDef", {"Start": str, "End": str}
)


class ClientGetDimensionValuesTimePeriodTypeDef(
    _ClientGetDimensionValuesTimePeriodTypeDef
):
    """
    Type definition for `ClientGetDimensionValues` `TimePeriod`

    The start and end dates for retrieving the dimension values. The start date is inclusive, but the
    end date is exclusive. For example, if ``start`` is ``2017-01-01`` and ``end`` is ``2017-05-01``
    , then the cost and usage data is retrieved from ``2017-01-01`` up to and including
    ``2017-04-30`` but not including ``2017-05-01`` .

    - **Start** *(string) --* **[REQUIRED]**

      The beginning of the time period that you want the usage and costs for. The start date is
      inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data
      starting at ``2017-01-01`` up to the end date.

    - **End** *(string) --* **[REQUIRED]**

      The end of the time period that you want the usage and costs for. The end date is exclusive.
      For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage data from the start
      date up to, but not including, ``2017-05-01`` .
    """


_ClientGetReservationCoverageFilterDimensionsTypeDef = TypedDict(
    "_ClientGetReservationCoverageFilterDimensionsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetReservationCoverageFilterDimensionsTypeDef(
    _ClientGetReservationCoverageFilterDimensionsTypeDef
):
    """
    Type definition for `ClientGetReservationCoverageFilter` `Dimensions`

    The specific ``Dimension`` to use for ``Expression`` .

    - **Key** *(string) --*

      The names of the metadata types that you can use to filter and group your results. For
      example, ``AZ`` returns a list of Availability Zones.

    - **Values** *(list) --*

      The metadata values that you can use to filter and group your results. You can use
      ``GetDimensionValues`` to find specific values.

      Valid values for the ``SERVICE`` dimension are ``Amazon Elastic Compute Cloud - Compute`` ,
      ``Amazon Elasticsearch Service`` , ``Amazon ElastiCache`` , ``Amazon Redshift`` , and
      ``Amazon Relational Database Service`` .

      - *(string) --*
    """


_ClientGetReservationCoverageFilterTagsTypeDef = TypedDict(
    "_ClientGetReservationCoverageFilterTagsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetReservationCoverageFilterTagsTypeDef(
    _ClientGetReservationCoverageFilterTagsTypeDef
):
    """
    Type definition for `ClientGetReservationCoverageFilter` `Tags`

    The specific ``Tag`` to use for ``Expression`` .

    - **Key** *(string) --*

      The key for the tag.

    - **Values** *(list) --*

      The specific value of the tag.

      - *(string) --*
    """


_ClientGetReservationCoverageFilterTypeDef = TypedDict(
    "_ClientGetReservationCoverageFilterTypeDef",
    {
        "Or": List[Dict],
        "And": List[Dict],
        "Not": Dict,
        "Dimensions": ClientGetReservationCoverageFilterDimensionsTypeDef,
        "Tags": ClientGetReservationCoverageFilterTagsTypeDef,
    },
    total=False,
)


class ClientGetReservationCoverageFilterTypeDef(
    _ClientGetReservationCoverageFilterTypeDef
):
    """
    Type definition for `ClientGetReservationCoverage` `Filter`

    Filters utilization data by dimensions. You can filter by the following dimensions:

    * AZ

    * CACHE_ENGINE

    * DATABASE_ENGINE

    * DEPLOYMENT_OPTION

    * INSTANCE_TYPE

    * LINKED_ACCOUNT

    * OPERATING_SYSTEM

    * PLATFORM

    * REGION

    * SERVICE

    * TAG

    * TENANCY

     ``GetReservationCoverage`` uses the same `Expression
     <http://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html>`__
     object as the other operations, but only ``AND`` is supported among each dimension. You can nest
     only one level deep. If there are multiple values for a dimension, they are OR'd together.

    If you don't provide a ``SERVICE`` filter, Cost Explorer defaults to EC2.

    - **Or** *(list) --*

      Return results that match either ``Dimension`` object.

      - *(dict) --*

        Use ``Expression`` to filter by cost or by usage. There are two patterns:

        * Simple dimension values - You can set the dimension name and values for the filters that
        you plan to use. For example, you can filter for ``REGION==us-east-1 OR REGION==us-west-1`` .
        The ``Expression`` for that looks like this:  ``{ "Dimensions": { "Key": "REGION", "Values":
        [ "us-east-1", “us-west-1” ] } }``   The list of dimension values are OR'd together to
        retrieve cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects
        using either ``with*`` methods or ``set*`` methods in multiple lines.

        * Compound dimension values with logical operations - You can use multiple ``Expression``
        types and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression``
        objects. This allows you to filter on more advanced options. For example, you can filter on
        ``((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE !=
        DataTransfer)`` . The ``Expression`` for that looks like this:  ``{ "And": [ {"Or": [
        {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": {
        "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE",
        "Values": ["DataTransfer"] }}} ] }``

        .. note::

           Because each ``Expression`` can have only one operator, the service returns an error if
           more than one is specified. The following example shows an ``Expression`` object that
           creates an error.

          ``{ "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [
          "DataTransfer" ] } }``

        .. note::

          For ``GetRightsizingRecommendation`` action, a combination of OR and NOT is not supported.
          OR is not supported between different dimensions, or dimensions and tags. NOT operators
          aren't supported. Dimensions are also limited to ``LINKED_ACCOUNT`` , ``REGION`` , or
          ``RIGHTSIZING_TYPE`` .

    - **And** *(list) --*

      Return results that match both ``Dimension`` objects.

      - *(dict) --*

        Use ``Expression`` to filter by cost or by usage. There are two patterns:

        * Simple dimension values - You can set the dimension name and values for the filters that
        you plan to use. For example, you can filter for ``REGION==us-east-1 OR REGION==us-west-1`` .
        The ``Expression`` for that looks like this:  ``{ "Dimensions": { "Key": "REGION", "Values":
        [ "us-east-1", “us-west-1” ] } }``   The list of dimension values are OR'd together to
        retrieve cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects
        using either ``with*`` methods or ``set*`` methods in multiple lines.

        * Compound dimension values with logical operations - You can use multiple ``Expression``
        types and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression``
        objects. This allows you to filter on more advanced options. For example, you can filter on
        ``((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE !=
        DataTransfer)`` . The ``Expression`` for that looks like this:  ``{ "And": [ {"Or": [
        {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": {
        "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE",
        "Values": ["DataTransfer"] }}} ] }``

        .. note::

           Because each ``Expression`` can have only one operator, the service returns an error if
           more than one is specified. The following example shows an ``Expression`` object that
           creates an error.

          ``{ "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [
          "DataTransfer" ] } }``

        .. note::

          For ``GetRightsizingRecommendation`` action, a combination of OR and NOT is not supported.
          OR is not supported between different dimensions, or dimensions and tags. NOT operators
          aren't supported. Dimensions are also limited to ``LINKED_ACCOUNT`` , ``REGION`` , or
          ``RIGHTSIZING_TYPE`` .

    - **Not** *(dict) --*

      Return results that don't match a ``Dimension`` object.

    - **Dimensions** *(dict) --*

      The specific ``Dimension`` to use for ``Expression`` .

      - **Key** *(string) --*

        The names of the metadata types that you can use to filter and group your results. For
        example, ``AZ`` returns a list of Availability Zones.

      - **Values** *(list) --*

        The metadata values that you can use to filter and group your results. You can use
        ``GetDimensionValues`` to find specific values.

        Valid values for the ``SERVICE`` dimension are ``Amazon Elastic Compute Cloud - Compute`` ,
        ``Amazon Elasticsearch Service`` , ``Amazon ElastiCache`` , ``Amazon Redshift`` , and
        ``Amazon Relational Database Service`` .

        - *(string) --*

    - **Tags** *(dict) --*

      The specific ``Tag`` to use for ``Expression`` .

      - **Key** *(string) --*

        The key for the tag.

      - **Values** *(list) --*

        The specific value of the tag.

        - *(string) --*
    """


_ClientGetReservationCoverageGroupByTypeDef = TypedDict(
    "_ClientGetReservationCoverageGroupByTypeDef",
    {"Type": str, "Key": str},
    total=False,
)


class ClientGetReservationCoverageGroupByTypeDef(
    _ClientGetReservationCoverageGroupByTypeDef
):
    """
    Type definition for `ClientGetReservationCoverage` `GroupBy`

    Represents a group when you specify a group by criteria or in the response to a query with a
    specific grouping.

    - **Type** *(string) --*

      The string that represents the type of group.

    - **Key** *(string) --*

      The string that represents a key for a specified group.
    """


_ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageCostTypeDef = TypedDict(
    "_ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageCostTypeDef",
    {"OnDemandCost": str},
    total=False,
)


class ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageCostTypeDef(
    _ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageCostTypeDef
):
    """
    Type definition for `ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverage` `CoverageCost`

    The amount of cost that the reservation covered.

    - **OnDemandCost** *(string) --*

      How much an On-Demand instance cost.
    """


_ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageHoursTypeDef = TypedDict(
    "_ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageHoursTypeDef",
    {
        "OnDemandHours": str,
        "ReservedHours": str,
        "TotalRunningHours": str,
        "CoverageHoursPercentage": str,
    },
    total=False,
)


class ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageHoursTypeDef(
    _ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageHoursTypeDef
):
    """
    Type definition for `ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverage` `CoverageHours`

    The amount of instance usage that the reservation covered, in hours.

    - **OnDemandHours** *(string) --*

      The number of instance running hours that On-Demand Instances covered.

    - **ReservedHours** *(string) --*

      The number of instance running hours that reservations covered.

    - **TotalRunningHours** *(string) --*

      The total instance usage, in hours.

    - **CoverageHoursPercentage** *(string) --*

      The percentage of instance hours that a reservation covered.
    """


_ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageNormalizedUnitsTypeDef = TypedDict(
    "_ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageNormalizedUnitsTypeDef",
    {
        "OnDemandNormalizedUnits": str,
        "ReservedNormalizedUnits": str,
        "TotalRunningNormalizedUnits": str,
        "CoverageNormalizedUnitsPercentage": str,
    },
    total=False,
)


class ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageNormalizedUnitsTypeDef(
    _ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageNormalizedUnitsTypeDef
):
    """
    Type definition for `ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverage` `CoverageNormalizedUnits`

    The amount of instance usage that the reservation covered, in normalized units.

    - **OnDemandNormalizedUnits** *(string) --*

      The number of normalized units that are covered by On-Demand Instances instead of
      a reservation.

    - **ReservedNormalizedUnits** *(string) --*

      The number of normalized units that a reservation covers.

    - **TotalRunningNormalizedUnits** *(string) --*

      The total number of normalized units that you used.

    - **CoverageNormalizedUnitsPercentage** *(string) --*

      The percentage of your used instance normalized units that a reservation covers.
    """


_ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageTypeDef = TypedDict(
    "_ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageTypeDef",
    {
        "CoverageHours": ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageHoursTypeDef,
        "CoverageNormalizedUnits": ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageNormalizedUnitsTypeDef,
        "CoverageCost": ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageCostTypeDef,
    },
    total=False,
)


class ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageTypeDef(
    _ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageTypeDef
):
    """
    Type definition for `ClientGetReservationCoverageResponseCoveragesByTimeGroups` `Coverage`

    How much instance usage this group of reservations covered.

    - **CoverageHours** *(dict) --*

      The amount of instance usage that the reservation covered, in hours.

      - **OnDemandHours** *(string) --*

        The number of instance running hours that On-Demand Instances covered.

      - **ReservedHours** *(string) --*

        The number of instance running hours that reservations covered.

      - **TotalRunningHours** *(string) --*

        The total instance usage, in hours.

      - **CoverageHoursPercentage** *(string) --*

        The percentage of instance hours that a reservation covered.

    - **CoverageNormalizedUnits** *(dict) --*

      The amount of instance usage that the reservation covered, in normalized units.

      - **OnDemandNormalizedUnits** *(string) --*

        The number of normalized units that are covered by On-Demand Instances instead of
        a reservation.

      - **ReservedNormalizedUnits** *(string) --*

        The number of normalized units that a reservation covers.

      - **TotalRunningNormalizedUnits** *(string) --*

        The total number of normalized units that you used.

      - **CoverageNormalizedUnitsPercentage** *(string) --*

        The percentage of your used instance normalized units that a reservation covers.

    - **CoverageCost** *(dict) --*

      The amount of cost that the reservation covered.

      - **OnDemandCost** *(string) --*

        How much an On-Demand instance cost.
    """


_ClientGetReservationCoverageResponseCoveragesByTimeGroupsTypeDef = TypedDict(
    "_ClientGetReservationCoverageResponseCoveragesByTimeGroupsTypeDef",
    {
        "Attributes": Dict[str, str],
        "Coverage": ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageTypeDef,
    },
    total=False,
)


class ClientGetReservationCoverageResponseCoveragesByTimeGroupsTypeDef(
    _ClientGetReservationCoverageResponseCoveragesByTimeGroupsTypeDef
):
    """
    Type definition for `ClientGetReservationCoverageResponseCoveragesByTime` `Groups`

    A group of reservations that share a set of attributes.

    - **Attributes** *(dict) --*

      The attributes for this group of reservations.

      - *(string) --*

        - *(string) --*

    - **Coverage** *(dict) --*

      How much instance usage this group of reservations covered.

      - **CoverageHours** *(dict) --*

        The amount of instance usage that the reservation covered, in hours.

        - **OnDemandHours** *(string) --*

          The number of instance running hours that On-Demand Instances covered.

        - **ReservedHours** *(string) --*

          The number of instance running hours that reservations covered.

        - **TotalRunningHours** *(string) --*

          The total instance usage, in hours.

        - **CoverageHoursPercentage** *(string) --*

          The percentage of instance hours that a reservation covered.

      - **CoverageNormalizedUnits** *(dict) --*

        The amount of instance usage that the reservation covered, in normalized units.

        - **OnDemandNormalizedUnits** *(string) --*

          The number of normalized units that are covered by On-Demand Instances instead of
          a reservation.

        - **ReservedNormalizedUnits** *(string) --*

          The number of normalized units that a reservation covers.

        - **TotalRunningNormalizedUnits** *(string) --*

          The total number of normalized units that you used.

        - **CoverageNormalizedUnitsPercentage** *(string) --*

          The percentage of your used instance normalized units that a reservation covers.

      - **CoverageCost** *(dict) --*

        The amount of cost that the reservation covered.

        - **OnDemandCost** *(string) --*

          How much an On-Demand instance cost.
    """


_ClientGetReservationCoverageResponseCoveragesByTimeTimePeriodTypeDef = TypedDict(
    "_ClientGetReservationCoverageResponseCoveragesByTimeTimePeriodTypeDef",
    {"Start": str, "End": str},
    total=False,
)


class ClientGetReservationCoverageResponseCoveragesByTimeTimePeriodTypeDef(
    _ClientGetReservationCoverageResponseCoveragesByTimeTimePeriodTypeDef
):
    """
    Type definition for `ClientGetReservationCoverageResponseCoveragesByTime` `TimePeriod`

    The period that this coverage was used over.

    - **Start** *(string) --*

      The beginning of the time period that you want the usage and costs for. The start date
      is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and
      usage data starting at ``2017-01-01`` up to the end date.

    - **End** *(string) --*

      The end of the time period that you want the usage and costs for. The end date is
      exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage
      data from the start date up to, but not including, ``2017-05-01`` .
    """


_ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageCostTypeDef = TypedDict(
    "_ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageCostTypeDef",
    {"OnDemandCost": str},
    total=False,
)


class ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageCostTypeDef(
    _ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageCostTypeDef
):
    """
    Type definition for `ClientGetReservationCoverageResponseCoveragesByTimeTotal` `CoverageCost`

    The amount of cost that the reservation covered.

    - **OnDemandCost** *(string) --*

      How much an On-Demand instance cost.
    """


_ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageHoursTypeDef = TypedDict(
    "_ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageHoursTypeDef",
    {
        "OnDemandHours": str,
        "ReservedHours": str,
        "TotalRunningHours": str,
        "CoverageHoursPercentage": str,
    },
    total=False,
)


class ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageHoursTypeDef(
    _ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageHoursTypeDef
):
    """
    Type definition for `ClientGetReservationCoverageResponseCoveragesByTimeTotal` `CoverageHours`

    The amount of instance usage that the reservation covered, in hours.

    - **OnDemandHours** *(string) --*

      The number of instance running hours that On-Demand Instances covered.

    - **ReservedHours** *(string) --*

      The number of instance running hours that reservations covered.

    - **TotalRunningHours** *(string) --*

      The total instance usage, in hours.

    - **CoverageHoursPercentage** *(string) --*

      The percentage of instance hours that a reservation covered.
    """


_ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageNormalizedUnitsTypeDef = TypedDict(
    "_ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageNormalizedUnitsTypeDef",
    {
        "OnDemandNormalizedUnits": str,
        "ReservedNormalizedUnits": str,
        "TotalRunningNormalizedUnits": str,
        "CoverageNormalizedUnitsPercentage": str,
    },
    total=False,
)


class ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageNormalizedUnitsTypeDef(
    _ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageNormalizedUnitsTypeDef
):
    """
    Type definition for `ClientGetReservationCoverageResponseCoveragesByTimeTotal` `CoverageNormalizedUnits`

    The amount of instance usage that the reservation covered, in normalized units.

    - **OnDemandNormalizedUnits** *(string) --*

      The number of normalized units that are covered by On-Demand Instances instead of a
      reservation.

    - **ReservedNormalizedUnits** *(string) --*

      The number of normalized units that a reservation covers.

    - **TotalRunningNormalizedUnits** *(string) --*

      The total number of normalized units that you used.

    - **CoverageNormalizedUnitsPercentage** *(string) --*

      The percentage of your used instance normalized units that a reservation covers.
    """


_ClientGetReservationCoverageResponseCoveragesByTimeTotalTypeDef = TypedDict(
    "_ClientGetReservationCoverageResponseCoveragesByTimeTotalTypeDef",
    {
        "CoverageHours": ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageHoursTypeDef,
        "CoverageNormalizedUnits": ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageNormalizedUnitsTypeDef,
        "CoverageCost": ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageCostTypeDef,
    },
    total=False,
)


class ClientGetReservationCoverageResponseCoveragesByTimeTotalTypeDef(
    _ClientGetReservationCoverageResponseCoveragesByTimeTotalTypeDef
):
    """
    Type definition for `ClientGetReservationCoverageResponseCoveragesByTime` `Total`

    The total reservation coverage, in hours.

    - **CoverageHours** *(dict) --*

      The amount of instance usage that the reservation covered, in hours.

      - **OnDemandHours** *(string) --*

        The number of instance running hours that On-Demand Instances covered.

      - **ReservedHours** *(string) --*

        The number of instance running hours that reservations covered.

      - **TotalRunningHours** *(string) --*

        The total instance usage, in hours.

      - **CoverageHoursPercentage** *(string) --*

        The percentage of instance hours that a reservation covered.

    - **CoverageNormalizedUnits** *(dict) --*

      The amount of instance usage that the reservation covered, in normalized units.

      - **OnDemandNormalizedUnits** *(string) --*

        The number of normalized units that are covered by On-Demand Instances instead of a
        reservation.

      - **ReservedNormalizedUnits** *(string) --*

        The number of normalized units that a reservation covers.

      - **TotalRunningNormalizedUnits** *(string) --*

        The total number of normalized units that you used.

      - **CoverageNormalizedUnitsPercentage** *(string) --*

        The percentage of your used instance normalized units that a reservation covers.

    - **CoverageCost** *(dict) --*

      The amount of cost that the reservation covered.

      - **OnDemandCost** *(string) --*

        How much an On-Demand instance cost.
    """


_ClientGetReservationCoverageResponseCoveragesByTimeTypeDef = TypedDict(
    "_ClientGetReservationCoverageResponseCoveragesByTimeTypeDef",
    {
        "TimePeriod": ClientGetReservationCoverageResponseCoveragesByTimeTimePeriodTypeDef,
        "Groups": List[
            ClientGetReservationCoverageResponseCoveragesByTimeGroupsTypeDef
        ],
        "Total": ClientGetReservationCoverageResponseCoveragesByTimeTotalTypeDef,
    },
    total=False,
)


class ClientGetReservationCoverageResponseCoveragesByTimeTypeDef(
    _ClientGetReservationCoverageResponseCoveragesByTimeTypeDef
):
    """
    Type definition for `ClientGetReservationCoverageResponse` `CoveragesByTime`

    Reservation coverage for a specified period, in hours.

    - **TimePeriod** *(dict) --*

      The period that this coverage was used over.

      - **Start** *(string) --*

        The beginning of the time period that you want the usage and costs for. The start date
        is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and
        usage data starting at ``2017-01-01`` up to the end date.

      - **End** *(string) --*

        The end of the time period that you want the usage and costs for. The end date is
        exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage
        data from the start date up to, but not including, ``2017-05-01`` .

    - **Groups** *(list) --*

      The groups of instances that the reservation covered.

      - *(dict) --*

        A group of reservations that share a set of attributes.

        - **Attributes** *(dict) --*

          The attributes for this group of reservations.

          - *(string) --*

            - *(string) --*

        - **Coverage** *(dict) --*

          How much instance usage this group of reservations covered.

          - **CoverageHours** *(dict) --*

            The amount of instance usage that the reservation covered, in hours.

            - **OnDemandHours** *(string) --*

              The number of instance running hours that On-Demand Instances covered.

            - **ReservedHours** *(string) --*

              The number of instance running hours that reservations covered.

            - **TotalRunningHours** *(string) --*

              The total instance usage, in hours.

            - **CoverageHoursPercentage** *(string) --*

              The percentage of instance hours that a reservation covered.

          - **CoverageNormalizedUnits** *(dict) --*

            The amount of instance usage that the reservation covered, in normalized units.

            - **OnDemandNormalizedUnits** *(string) --*

              The number of normalized units that are covered by On-Demand Instances instead of
              a reservation.

            - **ReservedNormalizedUnits** *(string) --*

              The number of normalized units that a reservation covers.

            - **TotalRunningNormalizedUnits** *(string) --*

              The total number of normalized units that you used.

            - **CoverageNormalizedUnitsPercentage** *(string) --*

              The percentage of your used instance normalized units that a reservation covers.

          - **CoverageCost** *(dict) --*

            The amount of cost that the reservation covered.

            - **OnDemandCost** *(string) --*

              How much an On-Demand instance cost.

    - **Total** *(dict) --*

      The total reservation coverage, in hours.

      - **CoverageHours** *(dict) --*

        The amount of instance usage that the reservation covered, in hours.

        - **OnDemandHours** *(string) --*

          The number of instance running hours that On-Demand Instances covered.

        - **ReservedHours** *(string) --*

          The number of instance running hours that reservations covered.

        - **TotalRunningHours** *(string) --*

          The total instance usage, in hours.

        - **CoverageHoursPercentage** *(string) --*

          The percentage of instance hours that a reservation covered.

      - **CoverageNormalizedUnits** *(dict) --*

        The amount of instance usage that the reservation covered, in normalized units.

        - **OnDemandNormalizedUnits** *(string) --*

          The number of normalized units that are covered by On-Demand Instances instead of a
          reservation.

        - **ReservedNormalizedUnits** *(string) --*

          The number of normalized units that a reservation covers.

        - **TotalRunningNormalizedUnits** *(string) --*

          The total number of normalized units that you used.

        - **CoverageNormalizedUnitsPercentage** *(string) --*

          The percentage of your used instance normalized units that a reservation covers.

      - **CoverageCost** *(dict) --*

        The amount of cost that the reservation covered.

        - **OnDemandCost** *(string) --*

          How much an On-Demand instance cost.
    """


_ClientGetReservationCoverageResponseTotalCoverageCostTypeDef = TypedDict(
    "_ClientGetReservationCoverageResponseTotalCoverageCostTypeDef",
    {"OnDemandCost": str},
    total=False,
)


class ClientGetReservationCoverageResponseTotalCoverageCostTypeDef(
    _ClientGetReservationCoverageResponseTotalCoverageCostTypeDef
):
    """
    Type definition for `ClientGetReservationCoverageResponseTotal` `CoverageCost`

    The amount of cost that the reservation covered.

    - **OnDemandCost** *(string) --*

      How much an On-Demand instance cost.
    """


_ClientGetReservationCoverageResponseTotalCoverageHoursTypeDef = TypedDict(
    "_ClientGetReservationCoverageResponseTotalCoverageHoursTypeDef",
    {
        "OnDemandHours": str,
        "ReservedHours": str,
        "TotalRunningHours": str,
        "CoverageHoursPercentage": str,
    },
    total=False,
)


class ClientGetReservationCoverageResponseTotalCoverageHoursTypeDef(
    _ClientGetReservationCoverageResponseTotalCoverageHoursTypeDef
):
    """
    Type definition for `ClientGetReservationCoverageResponseTotal` `CoverageHours`

    The amount of instance usage that the reservation covered, in hours.

    - **OnDemandHours** *(string) --*

      The number of instance running hours that On-Demand Instances covered.

    - **ReservedHours** *(string) --*

      The number of instance running hours that reservations covered.

    - **TotalRunningHours** *(string) --*

      The total instance usage, in hours.

    - **CoverageHoursPercentage** *(string) --*

      The percentage of instance hours that a reservation covered.
    """


_ClientGetReservationCoverageResponseTotalCoverageNormalizedUnitsTypeDef = TypedDict(
    "_ClientGetReservationCoverageResponseTotalCoverageNormalizedUnitsTypeDef",
    {
        "OnDemandNormalizedUnits": str,
        "ReservedNormalizedUnits": str,
        "TotalRunningNormalizedUnits": str,
        "CoverageNormalizedUnitsPercentage": str,
    },
    total=False,
)


class ClientGetReservationCoverageResponseTotalCoverageNormalizedUnitsTypeDef(
    _ClientGetReservationCoverageResponseTotalCoverageNormalizedUnitsTypeDef
):
    """
    Type definition for `ClientGetReservationCoverageResponseTotal` `CoverageNormalizedUnits`

    The amount of instance usage that the reservation covered, in normalized units.

    - **OnDemandNormalizedUnits** *(string) --*

      The number of normalized units that are covered by On-Demand Instances instead of a
      reservation.

    - **ReservedNormalizedUnits** *(string) --*

      The number of normalized units that a reservation covers.

    - **TotalRunningNormalizedUnits** *(string) --*

      The total number of normalized units that you used.

    - **CoverageNormalizedUnitsPercentage** *(string) --*

      The percentage of your used instance normalized units that a reservation covers.
    """


_ClientGetReservationCoverageResponseTotalTypeDef = TypedDict(
    "_ClientGetReservationCoverageResponseTotalTypeDef",
    {
        "CoverageHours": ClientGetReservationCoverageResponseTotalCoverageHoursTypeDef,
        "CoverageNormalizedUnits": ClientGetReservationCoverageResponseTotalCoverageNormalizedUnitsTypeDef,
        "CoverageCost": ClientGetReservationCoverageResponseTotalCoverageCostTypeDef,
    },
    total=False,
)


class ClientGetReservationCoverageResponseTotalTypeDef(
    _ClientGetReservationCoverageResponseTotalTypeDef
):
    """
    Type definition for `ClientGetReservationCoverageResponse` `Total`

    The total amount of instance usage that a reservation covered.

    - **CoverageHours** *(dict) --*

      The amount of instance usage that the reservation covered, in hours.

      - **OnDemandHours** *(string) --*

        The number of instance running hours that On-Demand Instances covered.

      - **ReservedHours** *(string) --*

        The number of instance running hours that reservations covered.

      - **TotalRunningHours** *(string) --*

        The total instance usage, in hours.

      - **CoverageHoursPercentage** *(string) --*

        The percentage of instance hours that a reservation covered.

    - **CoverageNormalizedUnits** *(dict) --*

      The amount of instance usage that the reservation covered, in normalized units.

      - **OnDemandNormalizedUnits** *(string) --*

        The number of normalized units that are covered by On-Demand Instances instead of a
        reservation.

      - **ReservedNormalizedUnits** *(string) --*

        The number of normalized units that a reservation covers.

      - **TotalRunningNormalizedUnits** *(string) --*

        The total number of normalized units that you used.

      - **CoverageNormalizedUnitsPercentage** *(string) --*

        The percentage of your used instance normalized units that a reservation covers.

    - **CoverageCost** *(dict) --*

      The amount of cost that the reservation covered.

      - **OnDemandCost** *(string) --*

        How much an On-Demand instance cost.
    """


_ClientGetReservationCoverageResponseTypeDef = TypedDict(
    "_ClientGetReservationCoverageResponseTypeDef",
    {
        "CoveragesByTime": List[
            ClientGetReservationCoverageResponseCoveragesByTimeTypeDef
        ],
        "Total": ClientGetReservationCoverageResponseTotalTypeDef,
        "NextPageToken": str,
    },
    total=False,
)


class ClientGetReservationCoverageResponseTypeDef(
    _ClientGetReservationCoverageResponseTypeDef
):
    """
    Type definition for `ClientGetReservationCoverage` `Response`

    - **CoveragesByTime** *(list) --*

      The amount of time that your reservations covered.

      - *(dict) --*

        Reservation coverage for a specified period, in hours.

        - **TimePeriod** *(dict) --*

          The period that this coverage was used over.

          - **Start** *(string) --*

            The beginning of the time period that you want the usage and costs for. The start date
            is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and
            usage data starting at ``2017-01-01`` up to the end date.

          - **End** *(string) --*

            The end of the time period that you want the usage and costs for. The end date is
            exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage
            data from the start date up to, but not including, ``2017-05-01`` .

        - **Groups** *(list) --*

          The groups of instances that the reservation covered.

          - *(dict) --*

            A group of reservations that share a set of attributes.

            - **Attributes** *(dict) --*

              The attributes for this group of reservations.

              - *(string) --*

                - *(string) --*

            - **Coverage** *(dict) --*

              How much instance usage this group of reservations covered.

              - **CoverageHours** *(dict) --*

                The amount of instance usage that the reservation covered, in hours.

                - **OnDemandHours** *(string) --*

                  The number of instance running hours that On-Demand Instances covered.

                - **ReservedHours** *(string) --*

                  The number of instance running hours that reservations covered.

                - **TotalRunningHours** *(string) --*

                  The total instance usage, in hours.

                - **CoverageHoursPercentage** *(string) --*

                  The percentage of instance hours that a reservation covered.

              - **CoverageNormalizedUnits** *(dict) --*

                The amount of instance usage that the reservation covered, in normalized units.

                - **OnDemandNormalizedUnits** *(string) --*

                  The number of normalized units that are covered by On-Demand Instances instead of
                  a reservation.

                - **ReservedNormalizedUnits** *(string) --*

                  The number of normalized units that a reservation covers.

                - **TotalRunningNormalizedUnits** *(string) --*

                  The total number of normalized units that you used.

                - **CoverageNormalizedUnitsPercentage** *(string) --*

                  The percentage of your used instance normalized units that a reservation covers.

              - **CoverageCost** *(dict) --*

                The amount of cost that the reservation covered.

                - **OnDemandCost** *(string) --*

                  How much an On-Demand instance cost.

        - **Total** *(dict) --*

          The total reservation coverage, in hours.

          - **CoverageHours** *(dict) --*

            The amount of instance usage that the reservation covered, in hours.

            - **OnDemandHours** *(string) --*

              The number of instance running hours that On-Demand Instances covered.

            - **ReservedHours** *(string) --*

              The number of instance running hours that reservations covered.

            - **TotalRunningHours** *(string) --*

              The total instance usage, in hours.

            - **CoverageHoursPercentage** *(string) --*

              The percentage of instance hours that a reservation covered.

          - **CoverageNormalizedUnits** *(dict) --*

            The amount of instance usage that the reservation covered, in normalized units.

            - **OnDemandNormalizedUnits** *(string) --*

              The number of normalized units that are covered by On-Demand Instances instead of a
              reservation.

            - **ReservedNormalizedUnits** *(string) --*

              The number of normalized units that a reservation covers.

            - **TotalRunningNormalizedUnits** *(string) --*

              The total number of normalized units that you used.

            - **CoverageNormalizedUnitsPercentage** *(string) --*

              The percentage of your used instance normalized units that a reservation covers.

          - **CoverageCost** *(dict) --*

            The amount of cost that the reservation covered.

            - **OnDemandCost** *(string) --*

              How much an On-Demand instance cost.

    - **Total** *(dict) --*

      The total amount of instance usage that a reservation covered.

      - **CoverageHours** *(dict) --*

        The amount of instance usage that the reservation covered, in hours.

        - **OnDemandHours** *(string) --*

          The number of instance running hours that On-Demand Instances covered.

        - **ReservedHours** *(string) --*

          The number of instance running hours that reservations covered.

        - **TotalRunningHours** *(string) --*

          The total instance usage, in hours.

        - **CoverageHoursPercentage** *(string) --*

          The percentage of instance hours that a reservation covered.

      - **CoverageNormalizedUnits** *(dict) --*

        The amount of instance usage that the reservation covered, in normalized units.

        - **OnDemandNormalizedUnits** *(string) --*

          The number of normalized units that are covered by On-Demand Instances instead of a
          reservation.

        - **ReservedNormalizedUnits** *(string) --*

          The number of normalized units that a reservation covers.

        - **TotalRunningNormalizedUnits** *(string) --*

          The total number of normalized units that you used.

        - **CoverageNormalizedUnitsPercentage** *(string) --*

          The percentage of your used instance normalized units that a reservation covers.

      - **CoverageCost** *(dict) --*

        The amount of cost that the reservation covered.

        - **OnDemandCost** *(string) --*

          How much an On-Demand instance cost.

    - **NextPageToken** *(string) --*

      The token for the next set of retrievable results. AWS provides the token when the response
      from a previous call has more results than the maximum page size.
    """


_ClientGetReservationCoverageTimePeriodTypeDef = TypedDict(
    "_ClientGetReservationCoverageTimePeriodTypeDef", {"Start": str, "End": str}
)


class ClientGetReservationCoverageTimePeriodTypeDef(
    _ClientGetReservationCoverageTimePeriodTypeDef
):
    """
    Type definition for `ClientGetReservationCoverage` `TimePeriod`

    The start and end dates of the period that you want to retrieve data about reservation coverage
    for. You can retrieve data for a maximum of 13 months: the last 12 months and the current month.
    The start date is inclusive, but the end date is exclusive. For example, if ``start`` is
    ``2017-01-01`` and ``end`` is ``2017-05-01`` , then the cost and usage data is retrieved from
    ``2017-01-01`` up to and including ``2017-04-30`` but not including ``2017-05-01`` .

    - **Start** *(string) --* **[REQUIRED]**

      The beginning of the time period that you want the usage and costs for. The start date is
      inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data
      starting at ``2017-01-01`` up to the end date.

    - **End** *(string) --* **[REQUIRED]**

      The end of the time period that you want the usage and costs for. The end date is exclusive.
      For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage data from the start
      date up to, but not including, ``2017-05-01`` .
    """


_ClientGetReservationPurchaseRecommendationResponseMetadataTypeDef = TypedDict(
    "_ClientGetReservationPurchaseRecommendationResponseMetadataTypeDef",
    {"RecommendationId": str, "GenerationTimestamp": str},
    total=False,
)


class ClientGetReservationPurchaseRecommendationResponseMetadataTypeDef(
    _ClientGetReservationPurchaseRecommendationResponseMetadataTypeDef
):
    """
    Type definition for `ClientGetReservationPurchaseRecommendationResponse` `Metadata`

    Information about this specific recommendation call, such as the time stamp for when Cost
    Explorer generated this recommendation.

    - **RecommendationId** *(string) --*

      The ID for this specific recommendation.

    - **GenerationTimestamp** *(string) --*

      The time stamp for when AWS made this recommendation.
    """


_ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsEC2InstanceDetailsTypeDef = TypedDict(
    "_ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsEC2InstanceDetailsTypeDef",
    {
        "Family": str,
        "InstanceType": str,
        "Region": str,
        "AvailabilityZone": str,
        "Platform": str,
        "Tenancy": str,
        "CurrentGeneration": bool,
        "SizeFlexEligible": bool,
    },
    total=False,
)


class ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsEC2InstanceDetailsTypeDef(
    _ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsEC2InstanceDetailsTypeDef
):
    """
    Type definition for `ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetails` `EC2InstanceDetails`

    The Amazon EC2 instances that AWS recommends that you purchase.

    - **Family** *(string) --*

      The instance family of the recommended reservation.

    - **InstanceType** *(string) --*

      The type of instance that AWS recommends.

    - **Region** *(string) --*

      The AWS Region of the recommended reservation.

    - **AvailabilityZone** *(string) --*

      The Availability Zone of the recommended reservation.

    - **Platform** *(string) --*

      The platform of the recommended reservation. The platform is the specific
      combination of operating system, license model, and software on an instance.

    - **Tenancy** *(string) --*

      Whether the recommended reservation is dedicated or shared.

    - **CurrentGeneration** *(boolean) --*

      Whether the recommendation is for a current-generation instance.

    - **SizeFlexEligible** *(boolean) --*

      Whether the recommended reservation is size flexible.
    """


_ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsESInstanceDetailsTypeDef = TypedDict(
    "_ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsESInstanceDetailsTypeDef",
    {
        "InstanceClass": str,
        "InstanceSize": str,
        "Region": str,
        "CurrentGeneration": bool,
        "SizeFlexEligible": bool,
    },
    total=False,
)


class ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsESInstanceDetailsTypeDef(
    _ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsESInstanceDetailsTypeDef
):
    """
    Type definition for `ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetails` `ESInstanceDetails`

    The Amazon ES instances that AWS recommends that you purchase.

    - **InstanceClass** *(string) --*

      The class of instance that AWS recommends.

    - **InstanceSize** *(string) --*

      The size of instance that AWS recommends.

    - **Region** *(string) --*

      The AWS Region of the recommended reservation.

    - **CurrentGeneration** *(boolean) --*

      Whether the recommendation is for a current-generation instance.

    - **SizeFlexEligible** *(boolean) --*

      Whether the recommended reservation is size flexible.
    """


_ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsElastiCacheInstanceDetailsTypeDef = TypedDict(
    "_ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsElastiCacheInstanceDetailsTypeDef",
    {
        "Family": str,
        "NodeType": str,
        "Region": str,
        "ProductDescription": str,
        "CurrentGeneration": bool,
        "SizeFlexEligible": bool,
    },
    total=False,
)


class ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsElastiCacheInstanceDetailsTypeDef(
    _ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsElastiCacheInstanceDetailsTypeDef
):
    """
    Type definition for `ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetails` `ElastiCacheInstanceDetails`

    The ElastiCache instances that AWS recommends that you purchase.

    - **Family** *(string) --*

      The instance family of the recommended reservation.

    - **NodeType** *(string) --*

      The type of node that AWS recommends.

    - **Region** *(string) --*

      The AWS Region of the recommended reservation.

    - **ProductDescription** *(string) --*

      The description of the recommended reservation.

    - **CurrentGeneration** *(boolean) --*

      Whether the recommendation is for a current generation instance.

    - **SizeFlexEligible** *(boolean) --*

      Whether the recommended reservation is size flexible.
    """


_ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsRDSInstanceDetailsTypeDef = TypedDict(
    "_ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsRDSInstanceDetailsTypeDef",
    {
        "Family": str,
        "InstanceType": str,
        "Region": str,
        "DatabaseEngine": str,
        "DatabaseEdition": str,
        "DeploymentOption": str,
        "LicenseModel": str,
        "CurrentGeneration": bool,
        "SizeFlexEligible": bool,
    },
    total=False,
)


class ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsRDSInstanceDetailsTypeDef(
    _ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsRDSInstanceDetailsTypeDef
):
    """
    Type definition for `ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetails` `RDSInstanceDetails`

    The Amazon RDS instances that AWS recommends that you purchase.

    - **Family** *(string) --*

      The instance family of the recommended reservation.

    - **InstanceType** *(string) --*

      The type of instance that AWS recommends.

    - **Region** *(string) --*

      The AWS Region of the recommended reservation.

    - **DatabaseEngine** *(string) --*

      The database engine that the recommended reservation supports.

    - **DatabaseEdition** *(string) --*

      The database edition that the recommended reservation supports.

    - **DeploymentOption** *(string) --*

      Whether the recommendation is for a reservation in a single Availability Zone or
      a reservation with a backup in a second Availability Zone.

    - **LicenseModel** *(string) --*

      The license model that the recommended reservation supports.

    - **CurrentGeneration** *(boolean) --*

      Whether the recommendation is for a current-generation instance.

    - **SizeFlexEligible** *(boolean) --*

      Whether the recommended reservation is size flexible.
    """


_ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsRedshiftInstanceDetailsTypeDef = TypedDict(
    "_ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsRedshiftInstanceDetailsTypeDef",
    {
        "Family": str,
        "NodeType": str,
        "Region": str,
        "CurrentGeneration": bool,
        "SizeFlexEligible": bool,
    },
    total=False,
)


class ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsRedshiftInstanceDetailsTypeDef(
    _ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsRedshiftInstanceDetailsTypeDef
):
    """
    Type definition for `ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetails` `RedshiftInstanceDetails`

    The Amazon Redshift instances that AWS recommends that you purchase.

    - **Family** *(string) --*

      The instance family of the recommended reservation.

    - **NodeType** *(string) --*

      The type of node that AWS recommends.

    - **Region** *(string) --*

      The AWS Region of the recommended reservation.

    - **CurrentGeneration** *(boolean) --*

      Whether the recommendation is for a current-generation instance.

    - **SizeFlexEligible** *(boolean) --*

      Whether the recommended reservation is size flexible.
    """


_ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsTypeDef = TypedDict(
    "_ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsTypeDef",
    {
        "EC2InstanceDetails": ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsEC2InstanceDetailsTypeDef,
        "RDSInstanceDetails": ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsRDSInstanceDetailsTypeDef,
        "RedshiftInstanceDetails": ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsRedshiftInstanceDetailsTypeDef,
        "ElastiCacheInstanceDetails": ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsElastiCacheInstanceDetailsTypeDef,
        "ESInstanceDetails": ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsESInstanceDetailsTypeDef,
    },
    total=False,
)


class ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsTypeDef(
    _ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsTypeDef
):
    """
    Type definition for `ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetails` `InstanceDetails`

    Details about the instances that AWS recommends that you purchase.

    - **EC2InstanceDetails** *(dict) --*

      The Amazon EC2 instances that AWS recommends that you purchase.

      - **Family** *(string) --*

        The instance family of the recommended reservation.

      - **InstanceType** *(string) --*

        The type of instance that AWS recommends.

      - **Region** *(string) --*

        The AWS Region of the recommended reservation.

      - **AvailabilityZone** *(string) --*

        The Availability Zone of the recommended reservation.

      - **Platform** *(string) --*

        The platform of the recommended reservation. The platform is the specific
        combination of operating system, license model, and software on an instance.

      - **Tenancy** *(string) --*

        Whether the recommended reservation is dedicated or shared.

      - **CurrentGeneration** *(boolean) --*

        Whether the recommendation is for a current-generation instance.

      - **SizeFlexEligible** *(boolean) --*

        Whether the recommended reservation is size flexible.

    - **RDSInstanceDetails** *(dict) --*

      The Amazon RDS instances that AWS recommends that you purchase.

      - **Family** *(string) --*

        The instance family of the recommended reservation.

      - **InstanceType** *(string) --*

        The type of instance that AWS recommends.

      - **Region** *(string) --*

        The AWS Region of the recommended reservation.

      - **DatabaseEngine** *(string) --*

        The database engine that the recommended reservation supports.

      - **DatabaseEdition** *(string) --*

        The database edition that the recommended reservation supports.

      - **DeploymentOption** *(string) --*

        Whether the recommendation is for a reservation in a single Availability Zone or
        a reservation with a backup in a second Availability Zone.

      - **LicenseModel** *(string) --*

        The license model that the recommended reservation supports.

      - **CurrentGeneration** *(boolean) --*

        Whether the recommendation is for a current-generation instance.

      - **SizeFlexEligible** *(boolean) --*

        Whether the recommended reservation is size flexible.

    - **RedshiftInstanceDetails** *(dict) --*

      The Amazon Redshift instances that AWS recommends that you purchase.

      - **Family** *(string) --*

        The instance family of the recommended reservation.

      - **NodeType** *(string) --*

        The type of node that AWS recommends.

      - **Region** *(string) --*

        The AWS Region of the recommended reservation.

      - **CurrentGeneration** *(boolean) --*

        Whether the recommendation is for a current-generation instance.

      - **SizeFlexEligible** *(boolean) --*

        Whether the recommended reservation is size flexible.

    - **ElastiCacheInstanceDetails** *(dict) --*

      The ElastiCache instances that AWS recommends that you purchase.

      - **Family** *(string) --*

        The instance family of the recommended reservation.

      - **NodeType** *(string) --*

        The type of node that AWS recommends.

      - **Region** *(string) --*

        The AWS Region of the recommended reservation.

      - **ProductDescription** *(string) --*

        The description of the recommended reservation.

      - **CurrentGeneration** *(boolean) --*

        Whether the recommendation is for a current generation instance.

      - **SizeFlexEligible** *(boolean) --*

        Whether the recommended reservation is size flexible.

    - **ESInstanceDetails** *(dict) --*

      The Amazon ES instances that AWS recommends that you purchase.

      - **InstanceClass** *(string) --*

        The class of instance that AWS recommends.

      - **InstanceSize** *(string) --*

        The size of instance that AWS recommends.

      - **Region** *(string) --*

        The AWS Region of the recommended reservation.

      - **CurrentGeneration** *(boolean) --*

        Whether the recommendation is for a current-generation instance.

      - **SizeFlexEligible** *(boolean) --*

        Whether the recommended reservation is size flexible.
    """


_ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsTypeDef = TypedDict(
    "_ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsTypeDef",
    {
        "AccountId": str,
        "InstanceDetails": ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsTypeDef,
        "RecommendedNumberOfInstancesToPurchase": str,
        "RecommendedNormalizedUnitsToPurchase": str,
        "MinimumNumberOfInstancesUsedPerHour": str,
        "MinimumNormalizedUnitsUsedPerHour": str,
        "MaximumNumberOfInstancesUsedPerHour": str,
        "MaximumNormalizedUnitsUsedPerHour": str,
        "AverageNumberOfInstancesUsedPerHour": str,
        "AverageNormalizedUnitsUsedPerHour": str,
        "AverageUtilization": str,
        "EstimatedBreakEvenInMonths": str,
        "CurrencyCode": str,
        "EstimatedMonthlySavingsAmount": str,
        "EstimatedMonthlySavingsPercentage": str,
        "EstimatedMonthlyOnDemandCost": str,
        "EstimatedReservationCostForLookbackPeriod": str,
        "UpfrontCost": str,
        "RecurringStandardMonthlyCost": str,
    },
    total=False,
)


class ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsTypeDef(
    _ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsTypeDef
):
    """
    Type definition for `ClientGetReservationPurchaseRecommendationResponseRecommendations` `RecommendationDetails`

    Details about your recommended reservation purchase.

    - **AccountId** *(string) --*

      The account that this RI recommendation is for.

    - **InstanceDetails** *(dict) --*

      Details about the instances that AWS recommends that you purchase.

      - **EC2InstanceDetails** *(dict) --*

        The Amazon EC2 instances that AWS recommends that you purchase.

        - **Family** *(string) --*

          The instance family of the recommended reservation.

        - **InstanceType** *(string) --*

          The type of instance that AWS recommends.

        - **Region** *(string) --*

          The AWS Region of the recommended reservation.

        - **AvailabilityZone** *(string) --*

          The Availability Zone of the recommended reservation.

        - **Platform** *(string) --*

          The platform of the recommended reservation. The platform is the specific
          combination of operating system, license model, and software on an instance.

        - **Tenancy** *(string) --*

          Whether the recommended reservation is dedicated or shared.

        - **CurrentGeneration** *(boolean) --*

          Whether the recommendation is for a current-generation instance.

        - **SizeFlexEligible** *(boolean) --*

          Whether the recommended reservation is size flexible.

      - **RDSInstanceDetails** *(dict) --*

        The Amazon RDS instances that AWS recommends that you purchase.

        - **Family** *(string) --*

          The instance family of the recommended reservation.

        - **InstanceType** *(string) --*

          The type of instance that AWS recommends.

        - **Region** *(string) --*

          The AWS Region of the recommended reservation.

        - **DatabaseEngine** *(string) --*

          The database engine that the recommended reservation supports.

        - **DatabaseEdition** *(string) --*

          The database edition that the recommended reservation supports.

        - **DeploymentOption** *(string) --*

          Whether the recommendation is for a reservation in a single Availability Zone or
          a reservation with a backup in a second Availability Zone.

        - **LicenseModel** *(string) --*

          The license model that the recommended reservation supports.

        - **CurrentGeneration** *(boolean) --*

          Whether the recommendation is for a current-generation instance.

        - **SizeFlexEligible** *(boolean) --*

          Whether the recommended reservation is size flexible.

      - **RedshiftInstanceDetails** *(dict) --*

        The Amazon Redshift instances that AWS recommends that you purchase.

        - **Family** *(string) --*

          The instance family of the recommended reservation.

        - **NodeType** *(string) --*

          The type of node that AWS recommends.

        - **Region** *(string) --*

          The AWS Region of the recommended reservation.

        - **CurrentGeneration** *(boolean) --*

          Whether the recommendation is for a current-generation instance.

        - **SizeFlexEligible** *(boolean) --*

          Whether the recommended reservation is size flexible.

      - **ElastiCacheInstanceDetails** *(dict) --*

        The ElastiCache instances that AWS recommends that you purchase.

        - **Family** *(string) --*

          The instance family of the recommended reservation.

        - **NodeType** *(string) --*

          The type of node that AWS recommends.

        - **Region** *(string) --*

          The AWS Region of the recommended reservation.

        - **ProductDescription** *(string) --*

          The description of the recommended reservation.

        - **CurrentGeneration** *(boolean) --*

          Whether the recommendation is for a current generation instance.

        - **SizeFlexEligible** *(boolean) --*

          Whether the recommended reservation is size flexible.

      - **ESInstanceDetails** *(dict) --*

        The Amazon ES instances that AWS recommends that you purchase.

        - **InstanceClass** *(string) --*

          The class of instance that AWS recommends.

        - **InstanceSize** *(string) --*

          The size of instance that AWS recommends.

        - **Region** *(string) --*

          The AWS Region of the recommended reservation.

        - **CurrentGeneration** *(boolean) --*

          Whether the recommendation is for a current-generation instance.

        - **SizeFlexEligible** *(boolean) --*

          Whether the recommended reservation is size flexible.

    - **RecommendedNumberOfInstancesToPurchase** *(string) --*

      The number of instances that AWS recommends that you purchase.

    - **RecommendedNormalizedUnitsToPurchase** *(string) --*

      The number of normalized units that AWS recommends that you purchase.

    - **MinimumNumberOfInstancesUsedPerHour** *(string) --*

      The minimum number of instances that you used in an hour during the historical
      period. AWS uses this to calculate your recommended reservation purchases.

    - **MinimumNormalizedUnitsUsedPerHour** *(string) --*

      The minimum number of normalized units that you used in an hour during the historical
      period. AWS uses this to calculate your recommended reservation purchases.

    - **MaximumNumberOfInstancesUsedPerHour** *(string) --*

      The maximum number of instances that you used in an hour during the historical
      period. AWS uses this to calculate your recommended reservation purchases.

    - **MaximumNormalizedUnitsUsedPerHour** *(string) --*

      The maximum number of normalized units that you used in an hour during the historical
      period. AWS uses this to calculate your recommended reservation purchases.

    - **AverageNumberOfInstancesUsedPerHour** *(string) --*

      The average number of instances that you used in an hour during the historical
      period. AWS uses this to calculate your recommended reservation purchases.

    - **AverageNormalizedUnitsUsedPerHour** *(string) --*

      The average number of normalized units that you used in an hour during the historical
      period. AWS uses this to calculate your recommended reservation purchases.

    - **AverageUtilization** *(string) --*

      The average utilization of your instances. AWS uses this to calculate your
      recommended reservation purchases.

    - **EstimatedBreakEvenInMonths** *(string) --*

      How long AWS estimates that it takes for this instance to start saving you money, in
      months.

    - **CurrencyCode** *(string) --*

      The currency code that AWS used to calculate the costs for this instance.

    - **EstimatedMonthlySavingsAmount** *(string) --*

      How much AWS estimates that this specific recommendation could save you in a month.

    - **EstimatedMonthlySavingsPercentage** *(string) --*

      How much AWS estimates that this specific recommendation could save you in a month,
      as a percentage of your overall costs.

    - **EstimatedMonthlyOnDemandCost** *(string) --*

      How much AWS estimates that you spend on On-Demand Instances in a month.

    - **EstimatedReservationCostForLookbackPeriod** *(string) --*

      How much AWS estimates that you would have spent for all usage during the specified
      historical period if you had a reservation.

    - **UpfrontCost** *(string) --*

      How much purchasing this instance costs you upfront.

    - **RecurringStandardMonthlyCost** *(string) --*

      How much purchasing this instance costs you on a monthly basis.
    """


_ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationSummaryTypeDef = TypedDict(
    "_ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationSummaryTypeDef",
    {
        "TotalEstimatedMonthlySavingsAmount": str,
        "TotalEstimatedMonthlySavingsPercentage": str,
        "CurrencyCode": str,
    },
    total=False,
)


class ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationSummaryTypeDef(
    _ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationSummaryTypeDef
):
    """
    Type definition for `ClientGetReservationPurchaseRecommendationResponseRecommendations` `RecommendationSummary`

    A summary about the recommended purchase.

    - **TotalEstimatedMonthlySavingsAmount** *(string) --*

      The total amount that AWS estimates that this recommendation could save you in a month.

    - **TotalEstimatedMonthlySavingsPercentage** *(string) --*

      The total amount that AWS estimates that this recommendation could save you in a month,
      as a percentage of your costs.

    - **CurrencyCode** *(string) --*

      The currency code used for this recommendation.
    """


_ClientGetReservationPurchaseRecommendationResponseRecommendationsServiceSpecificationEC2SpecificationTypeDef = TypedDict(
    "_ClientGetReservationPurchaseRecommendationResponseRecommendationsServiceSpecificationEC2SpecificationTypeDef",
    {"OfferingClass": str},
    total=False,
)


class ClientGetReservationPurchaseRecommendationResponseRecommendationsServiceSpecificationEC2SpecificationTypeDef(
    _ClientGetReservationPurchaseRecommendationResponseRecommendationsServiceSpecificationEC2SpecificationTypeDef
):
    """
    Type definition for `ClientGetReservationPurchaseRecommendationResponseRecommendationsServiceSpecification` `EC2Specification`

    The Amazon EC2 hardware specifications that you want AWS to provide recommendations for.

    - **OfferingClass** *(string) --*

      Whether you want a recommendation for standard or convertible reservations.
    """


_ClientGetReservationPurchaseRecommendationResponseRecommendationsServiceSpecificationTypeDef = TypedDict(
    "_ClientGetReservationPurchaseRecommendationResponseRecommendationsServiceSpecificationTypeDef",
    {
        "EC2Specification": ClientGetReservationPurchaseRecommendationResponseRecommendationsServiceSpecificationEC2SpecificationTypeDef
    },
    total=False,
)


class ClientGetReservationPurchaseRecommendationResponseRecommendationsServiceSpecificationTypeDef(
    _ClientGetReservationPurchaseRecommendationResponseRecommendationsServiceSpecificationTypeDef
):
    """
    Type definition for `ClientGetReservationPurchaseRecommendationResponseRecommendations` `ServiceSpecification`

    Hardware specifications for the service that you want recommendations for.

    - **EC2Specification** *(dict) --*

      The Amazon EC2 hardware specifications that you want AWS to provide recommendations for.

      - **OfferingClass** *(string) --*

        Whether you want a recommendation for standard or convertible reservations.
    """


_ClientGetReservationPurchaseRecommendationResponseRecommendationsTypeDef = TypedDict(
    "_ClientGetReservationPurchaseRecommendationResponseRecommendationsTypeDef",
    {
        "AccountScope": str,
        "LookbackPeriodInDays": str,
        "TermInYears": str,
        "PaymentOption": str,
        "ServiceSpecification": ClientGetReservationPurchaseRecommendationResponseRecommendationsServiceSpecificationTypeDef,
        "RecommendationDetails": List[
            ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsTypeDef
        ],
        "RecommendationSummary": ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationSummaryTypeDef,
    },
    total=False,
)


class ClientGetReservationPurchaseRecommendationResponseRecommendationsTypeDef(
    _ClientGetReservationPurchaseRecommendationResponseRecommendationsTypeDef
):
    """
    Type definition for `ClientGetReservationPurchaseRecommendationResponse` `Recommendations`

    A specific reservation that AWS recommends for purchase.

    - **AccountScope** *(string) --*

      The account scope that AWS recommends that you purchase this instance for. For example,
      you can purchase this reservation for an entire organization in AWS Organizations.

    - **LookbackPeriodInDays** *(string) --*

      How many days of previous usage that AWS considers when making this recommendation.

    - **TermInYears** *(string) --*

      The term of the reservation that you want recommendations for, in years.

    - **PaymentOption** *(string) --*

      The payment option for the reservation. For example, ``AllUpfront`` or ``NoUpfront`` .

    - **ServiceSpecification** *(dict) --*

      Hardware specifications for the service that you want recommendations for.

      - **EC2Specification** *(dict) --*

        The Amazon EC2 hardware specifications that you want AWS to provide recommendations for.

        - **OfferingClass** *(string) --*

          Whether you want a recommendation for standard or convertible reservations.

    - **RecommendationDetails** *(list) --*

      Details about the recommended purchases.

      - *(dict) --*

        Details about your recommended reservation purchase.

        - **AccountId** *(string) --*

          The account that this RI recommendation is for.

        - **InstanceDetails** *(dict) --*

          Details about the instances that AWS recommends that you purchase.

          - **EC2InstanceDetails** *(dict) --*

            The Amazon EC2 instances that AWS recommends that you purchase.

            - **Family** *(string) --*

              The instance family of the recommended reservation.

            - **InstanceType** *(string) --*

              The type of instance that AWS recommends.

            - **Region** *(string) --*

              The AWS Region of the recommended reservation.

            - **AvailabilityZone** *(string) --*

              The Availability Zone of the recommended reservation.

            - **Platform** *(string) --*

              The platform of the recommended reservation. The platform is the specific
              combination of operating system, license model, and software on an instance.

            - **Tenancy** *(string) --*

              Whether the recommended reservation is dedicated or shared.

            - **CurrentGeneration** *(boolean) --*

              Whether the recommendation is for a current-generation instance.

            - **SizeFlexEligible** *(boolean) --*

              Whether the recommended reservation is size flexible.

          - **RDSInstanceDetails** *(dict) --*

            The Amazon RDS instances that AWS recommends that you purchase.

            - **Family** *(string) --*

              The instance family of the recommended reservation.

            - **InstanceType** *(string) --*

              The type of instance that AWS recommends.

            - **Region** *(string) --*

              The AWS Region of the recommended reservation.

            - **DatabaseEngine** *(string) --*

              The database engine that the recommended reservation supports.

            - **DatabaseEdition** *(string) --*

              The database edition that the recommended reservation supports.

            - **DeploymentOption** *(string) --*

              Whether the recommendation is for a reservation in a single Availability Zone or
              a reservation with a backup in a second Availability Zone.

            - **LicenseModel** *(string) --*

              The license model that the recommended reservation supports.

            - **CurrentGeneration** *(boolean) --*

              Whether the recommendation is for a current-generation instance.

            - **SizeFlexEligible** *(boolean) --*

              Whether the recommended reservation is size flexible.

          - **RedshiftInstanceDetails** *(dict) --*

            The Amazon Redshift instances that AWS recommends that you purchase.

            - **Family** *(string) --*

              The instance family of the recommended reservation.

            - **NodeType** *(string) --*

              The type of node that AWS recommends.

            - **Region** *(string) --*

              The AWS Region of the recommended reservation.

            - **CurrentGeneration** *(boolean) --*

              Whether the recommendation is for a current-generation instance.

            - **SizeFlexEligible** *(boolean) --*

              Whether the recommended reservation is size flexible.

          - **ElastiCacheInstanceDetails** *(dict) --*

            The ElastiCache instances that AWS recommends that you purchase.

            - **Family** *(string) --*

              The instance family of the recommended reservation.

            - **NodeType** *(string) --*

              The type of node that AWS recommends.

            - **Region** *(string) --*

              The AWS Region of the recommended reservation.

            - **ProductDescription** *(string) --*

              The description of the recommended reservation.

            - **CurrentGeneration** *(boolean) --*

              Whether the recommendation is for a current generation instance.

            - **SizeFlexEligible** *(boolean) --*

              Whether the recommended reservation is size flexible.

          - **ESInstanceDetails** *(dict) --*

            The Amazon ES instances that AWS recommends that you purchase.

            - **InstanceClass** *(string) --*

              The class of instance that AWS recommends.

            - **InstanceSize** *(string) --*

              The size of instance that AWS recommends.

            - **Region** *(string) --*

              The AWS Region of the recommended reservation.

            - **CurrentGeneration** *(boolean) --*

              Whether the recommendation is for a current-generation instance.

            - **SizeFlexEligible** *(boolean) --*

              Whether the recommended reservation is size flexible.

        - **RecommendedNumberOfInstancesToPurchase** *(string) --*

          The number of instances that AWS recommends that you purchase.

        - **RecommendedNormalizedUnitsToPurchase** *(string) --*

          The number of normalized units that AWS recommends that you purchase.

        - **MinimumNumberOfInstancesUsedPerHour** *(string) --*

          The minimum number of instances that you used in an hour during the historical
          period. AWS uses this to calculate your recommended reservation purchases.

        - **MinimumNormalizedUnitsUsedPerHour** *(string) --*

          The minimum number of normalized units that you used in an hour during the historical
          period. AWS uses this to calculate your recommended reservation purchases.

        - **MaximumNumberOfInstancesUsedPerHour** *(string) --*

          The maximum number of instances that you used in an hour during the historical
          period. AWS uses this to calculate your recommended reservation purchases.

        - **MaximumNormalizedUnitsUsedPerHour** *(string) --*

          The maximum number of normalized units that you used in an hour during the historical
          period. AWS uses this to calculate your recommended reservation purchases.

        - **AverageNumberOfInstancesUsedPerHour** *(string) --*

          The average number of instances that you used in an hour during the historical
          period. AWS uses this to calculate your recommended reservation purchases.

        - **AverageNormalizedUnitsUsedPerHour** *(string) --*

          The average number of normalized units that you used in an hour during the historical
          period. AWS uses this to calculate your recommended reservation purchases.

        - **AverageUtilization** *(string) --*

          The average utilization of your instances. AWS uses this to calculate your
          recommended reservation purchases.

        - **EstimatedBreakEvenInMonths** *(string) --*

          How long AWS estimates that it takes for this instance to start saving you money, in
          months.

        - **CurrencyCode** *(string) --*

          The currency code that AWS used to calculate the costs for this instance.

        - **EstimatedMonthlySavingsAmount** *(string) --*

          How much AWS estimates that this specific recommendation could save you in a month.

        - **EstimatedMonthlySavingsPercentage** *(string) --*

          How much AWS estimates that this specific recommendation could save you in a month,
          as a percentage of your overall costs.

        - **EstimatedMonthlyOnDemandCost** *(string) --*

          How much AWS estimates that you spend on On-Demand Instances in a month.

        - **EstimatedReservationCostForLookbackPeriod** *(string) --*

          How much AWS estimates that you would have spent for all usage during the specified
          historical period if you had a reservation.

        - **UpfrontCost** *(string) --*

          How much purchasing this instance costs you upfront.

        - **RecurringStandardMonthlyCost** *(string) --*

          How much purchasing this instance costs you on a monthly basis.

    - **RecommendationSummary** *(dict) --*

      A summary about the recommended purchase.

      - **TotalEstimatedMonthlySavingsAmount** *(string) --*

        The total amount that AWS estimates that this recommendation could save you in a month.

      - **TotalEstimatedMonthlySavingsPercentage** *(string) --*

        The total amount that AWS estimates that this recommendation could save you in a month,
        as a percentage of your costs.

      - **CurrencyCode** *(string) --*

        The currency code used for this recommendation.
    """


_ClientGetReservationPurchaseRecommendationResponseTypeDef = TypedDict(
    "_ClientGetReservationPurchaseRecommendationResponseTypeDef",
    {
        "Metadata": ClientGetReservationPurchaseRecommendationResponseMetadataTypeDef,
        "Recommendations": List[
            ClientGetReservationPurchaseRecommendationResponseRecommendationsTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)


class ClientGetReservationPurchaseRecommendationResponseTypeDef(
    _ClientGetReservationPurchaseRecommendationResponseTypeDef
):
    """
    Type definition for `ClientGetReservationPurchaseRecommendation` `Response`

    - **Metadata** *(dict) --*

      Information about this specific recommendation call, such as the time stamp for when Cost
      Explorer generated this recommendation.

      - **RecommendationId** *(string) --*

        The ID for this specific recommendation.

      - **GenerationTimestamp** *(string) --*

        The time stamp for when AWS made this recommendation.

    - **Recommendations** *(list) --*

      Recommendations for reservations to purchase.

      - *(dict) --*

        A specific reservation that AWS recommends for purchase.

        - **AccountScope** *(string) --*

          The account scope that AWS recommends that you purchase this instance for. For example,
          you can purchase this reservation for an entire organization in AWS Organizations.

        - **LookbackPeriodInDays** *(string) --*

          How many days of previous usage that AWS considers when making this recommendation.

        - **TermInYears** *(string) --*

          The term of the reservation that you want recommendations for, in years.

        - **PaymentOption** *(string) --*

          The payment option for the reservation. For example, ``AllUpfront`` or ``NoUpfront`` .

        - **ServiceSpecification** *(dict) --*

          Hardware specifications for the service that you want recommendations for.

          - **EC2Specification** *(dict) --*

            The Amazon EC2 hardware specifications that you want AWS to provide recommendations for.

            - **OfferingClass** *(string) --*

              Whether you want a recommendation for standard or convertible reservations.

        - **RecommendationDetails** *(list) --*

          Details about the recommended purchases.

          - *(dict) --*

            Details about your recommended reservation purchase.

            - **AccountId** *(string) --*

              The account that this RI recommendation is for.

            - **InstanceDetails** *(dict) --*

              Details about the instances that AWS recommends that you purchase.

              - **EC2InstanceDetails** *(dict) --*

                The Amazon EC2 instances that AWS recommends that you purchase.

                - **Family** *(string) --*

                  The instance family of the recommended reservation.

                - **InstanceType** *(string) --*

                  The type of instance that AWS recommends.

                - **Region** *(string) --*

                  The AWS Region of the recommended reservation.

                - **AvailabilityZone** *(string) --*

                  The Availability Zone of the recommended reservation.

                - **Platform** *(string) --*

                  The platform of the recommended reservation. The platform is the specific
                  combination of operating system, license model, and software on an instance.

                - **Tenancy** *(string) --*

                  Whether the recommended reservation is dedicated or shared.

                - **CurrentGeneration** *(boolean) --*

                  Whether the recommendation is for a current-generation instance.

                - **SizeFlexEligible** *(boolean) --*

                  Whether the recommended reservation is size flexible.

              - **RDSInstanceDetails** *(dict) --*

                The Amazon RDS instances that AWS recommends that you purchase.

                - **Family** *(string) --*

                  The instance family of the recommended reservation.

                - **InstanceType** *(string) --*

                  The type of instance that AWS recommends.

                - **Region** *(string) --*

                  The AWS Region of the recommended reservation.

                - **DatabaseEngine** *(string) --*

                  The database engine that the recommended reservation supports.

                - **DatabaseEdition** *(string) --*

                  The database edition that the recommended reservation supports.

                - **DeploymentOption** *(string) --*

                  Whether the recommendation is for a reservation in a single Availability Zone or
                  a reservation with a backup in a second Availability Zone.

                - **LicenseModel** *(string) --*

                  The license model that the recommended reservation supports.

                - **CurrentGeneration** *(boolean) --*

                  Whether the recommendation is for a current-generation instance.

                - **SizeFlexEligible** *(boolean) --*

                  Whether the recommended reservation is size flexible.

              - **RedshiftInstanceDetails** *(dict) --*

                The Amazon Redshift instances that AWS recommends that you purchase.

                - **Family** *(string) --*

                  The instance family of the recommended reservation.

                - **NodeType** *(string) --*

                  The type of node that AWS recommends.

                - **Region** *(string) --*

                  The AWS Region of the recommended reservation.

                - **CurrentGeneration** *(boolean) --*

                  Whether the recommendation is for a current-generation instance.

                - **SizeFlexEligible** *(boolean) --*

                  Whether the recommended reservation is size flexible.

              - **ElastiCacheInstanceDetails** *(dict) --*

                The ElastiCache instances that AWS recommends that you purchase.

                - **Family** *(string) --*

                  The instance family of the recommended reservation.

                - **NodeType** *(string) --*

                  The type of node that AWS recommends.

                - **Region** *(string) --*

                  The AWS Region of the recommended reservation.

                - **ProductDescription** *(string) --*

                  The description of the recommended reservation.

                - **CurrentGeneration** *(boolean) --*

                  Whether the recommendation is for a current generation instance.

                - **SizeFlexEligible** *(boolean) --*

                  Whether the recommended reservation is size flexible.

              - **ESInstanceDetails** *(dict) --*

                The Amazon ES instances that AWS recommends that you purchase.

                - **InstanceClass** *(string) --*

                  The class of instance that AWS recommends.

                - **InstanceSize** *(string) --*

                  The size of instance that AWS recommends.

                - **Region** *(string) --*

                  The AWS Region of the recommended reservation.

                - **CurrentGeneration** *(boolean) --*

                  Whether the recommendation is for a current-generation instance.

                - **SizeFlexEligible** *(boolean) --*

                  Whether the recommended reservation is size flexible.

            - **RecommendedNumberOfInstancesToPurchase** *(string) --*

              The number of instances that AWS recommends that you purchase.

            - **RecommendedNormalizedUnitsToPurchase** *(string) --*

              The number of normalized units that AWS recommends that you purchase.

            - **MinimumNumberOfInstancesUsedPerHour** *(string) --*

              The minimum number of instances that you used in an hour during the historical
              period. AWS uses this to calculate your recommended reservation purchases.

            - **MinimumNormalizedUnitsUsedPerHour** *(string) --*

              The minimum number of normalized units that you used in an hour during the historical
              period. AWS uses this to calculate your recommended reservation purchases.

            - **MaximumNumberOfInstancesUsedPerHour** *(string) --*

              The maximum number of instances that you used in an hour during the historical
              period. AWS uses this to calculate your recommended reservation purchases.

            - **MaximumNormalizedUnitsUsedPerHour** *(string) --*

              The maximum number of normalized units that you used in an hour during the historical
              period. AWS uses this to calculate your recommended reservation purchases.

            - **AverageNumberOfInstancesUsedPerHour** *(string) --*

              The average number of instances that you used in an hour during the historical
              period. AWS uses this to calculate your recommended reservation purchases.

            - **AverageNormalizedUnitsUsedPerHour** *(string) --*

              The average number of normalized units that you used in an hour during the historical
              period. AWS uses this to calculate your recommended reservation purchases.

            - **AverageUtilization** *(string) --*

              The average utilization of your instances. AWS uses this to calculate your
              recommended reservation purchases.

            - **EstimatedBreakEvenInMonths** *(string) --*

              How long AWS estimates that it takes for this instance to start saving you money, in
              months.

            - **CurrencyCode** *(string) --*

              The currency code that AWS used to calculate the costs for this instance.

            - **EstimatedMonthlySavingsAmount** *(string) --*

              How much AWS estimates that this specific recommendation could save you in a month.

            - **EstimatedMonthlySavingsPercentage** *(string) --*

              How much AWS estimates that this specific recommendation could save you in a month,
              as a percentage of your overall costs.

            - **EstimatedMonthlyOnDemandCost** *(string) --*

              How much AWS estimates that you spend on On-Demand Instances in a month.

            - **EstimatedReservationCostForLookbackPeriod** *(string) --*

              How much AWS estimates that you would have spent for all usage during the specified
              historical period if you had a reservation.

            - **UpfrontCost** *(string) --*

              How much purchasing this instance costs you upfront.

            - **RecurringStandardMonthlyCost** *(string) --*

              How much purchasing this instance costs you on a monthly basis.

        - **RecommendationSummary** *(dict) --*

          A summary about the recommended purchase.

          - **TotalEstimatedMonthlySavingsAmount** *(string) --*

            The total amount that AWS estimates that this recommendation could save you in a month.

          - **TotalEstimatedMonthlySavingsPercentage** *(string) --*

            The total amount that AWS estimates that this recommendation could save you in a month,
            as a percentage of your costs.

          - **CurrencyCode** *(string) --*

            The currency code used for this recommendation.

    - **NextPageToken** *(string) --*

      The pagination token for the next set of retrievable results.
    """


_ClientGetReservationPurchaseRecommendationServiceSpecificationEC2SpecificationTypeDef = TypedDict(
    "_ClientGetReservationPurchaseRecommendationServiceSpecificationEC2SpecificationTypeDef",
    {"OfferingClass": str},
    total=False,
)


class ClientGetReservationPurchaseRecommendationServiceSpecificationEC2SpecificationTypeDef(
    _ClientGetReservationPurchaseRecommendationServiceSpecificationEC2SpecificationTypeDef
):
    """
    Type definition for `ClientGetReservationPurchaseRecommendationServiceSpecification` `EC2Specification`

    The Amazon EC2 hardware specifications that you want AWS to provide recommendations for.

    - **OfferingClass** *(string) --*

      Whether you want a recommendation for standard or convertible reservations.
    """


_ClientGetReservationPurchaseRecommendationServiceSpecificationTypeDef = TypedDict(
    "_ClientGetReservationPurchaseRecommendationServiceSpecificationTypeDef",
    {
        "EC2Specification": ClientGetReservationPurchaseRecommendationServiceSpecificationEC2SpecificationTypeDef
    },
    total=False,
)


class ClientGetReservationPurchaseRecommendationServiceSpecificationTypeDef(
    _ClientGetReservationPurchaseRecommendationServiceSpecificationTypeDef
):
    """
    Type definition for `ClientGetReservationPurchaseRecommendation` `ServiceSpecification`

    The hardware specifications for the service instances that you want recommendations for, such as
    standard or convertible Amazon EC2 instances.

    - **EC2Specification** *(dict) --*

      The Amazon EC2 hardware specifications that you want AWS to provide recommendations for.

      - **OfferingClass** *(string) --*

        Whether you want a recommendation for standard or convertible reservations.
    """


_ClientGetReservationUtilizationFilterDimensionsTypeDef = TypedDict(
    "_ClientGetReservationUtilizationFilterDimensionsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetReservationUtilizationFilterDimensionsTypeDef(
    _ClientGetReservationUtilizationFilterDimensionsTypeDef
):
    """
    Type definition for `ClientGetReservationUtilizationFilter` `Dimensions`

    The specific ``Dimension`` to use for ``Expression`` .

    - **Key** *(string) --*

      The names of the metadata types that you can use to filter and group your results. For
      example, ``AZ`` returns a list of Availability Zones.

    - **Values** *(list) --*

      The metadata values that you can use to filter and group your results. You can use
      ``GetDimensionValues`` to find specific values.

      Valid values for the ``SERVICE`` dimension are ``Amazon Elastic Compute Cloud - Compute`` ,
      ``Amazon Elasticsearch Service`` , ``Amazon ElastiCache`` , ``Amazon Redshift`` , and
      ``Amazon Relational Database Service`` .

      - *(string) --*
    """


_ClientGetReservationUtilizationFilterTagsTypeDef = TypedDict(
    "_ClientGetReservationUtilizationFilterTagsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetReservationUtilizationFilterTagsTypeDef(
    _ClientGetReservationUtilizationFilterTagsTypeDef
):
    """
    Type definition for `ClientGetReservationUtilizationFilter` `Tags`

    The specific ``Tag`` to use for ``Expression`` .

    - **Key** *(string) --*

      The key for the tag.

    - **Values** *(list) --*

      The specific value of the tag.

      - *(string) --*
    """


_ClientGetReservationUtilizationFilterTypeDef = TypedDict(
    "_ClientGetReservationUtilizationFilterTypeDef",
    {
        "Or": List[Dict],
        "And": List[Dict],
        "Not": Dict,
        "Dimensions": ClientGetReservationUtilizationFilterDimensionsTypeDef,
        "Tags": ClientGetReservationUtilizationFilterTagsTypeDef,
    },
    total=False,
)


class ClientGetReservationUtilizationFilterTypeDef(
    _ClientGetReservationUtilizationFilterTypeDef
):
    """
    Type definition for `ClientGetReservationUtilization` `Filter`

    Filters utilization data by dimensions. You can filter by the following dimensions:

    * AZ

    * CACHE_ENGINE

    * DATABASE_ENGINE

    * DEPLOYMENT_OPTION

    * INSTANCE_TYPE

    * LINKED_ACCOUNT

    * OPERATING_SYSTEM

    * PLATFORM

    * REGION

    * SERVICE

    * SCOPE

    * TENANCY

     ``GetReservationUtilization`` uses the same `Expression
     <http://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html>`__
     object as the other operations, but only ``AND`` is supported among each dimension, and nesting
     is supported up to only one level deep. If there are multiple values for a dimension, they are
     OR'd together.

    - **Or** *(list) --*

      Return results that match either ``Dimension`` object.

      - *(dict) --*

        Use ``Expression`` to filter by cost or by usage. There are two patterns:

        * Simple dimension values - You can set the dimension name and values for the filters that
        you plan to use. For example, you can filter for ``REGION==us-east-1 OR REGION==us-west-1`` .
        The ``Expression`` for that looks like this:  ``{ "Dimensions": { "Key": "REGION", "Values":
        [ "us-east-1", “us-west-1” ] } }``   The list of dimension values are OR'd together to
        retrieve cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects
        using either ``with*`` methods or ``set*`` methods in multiple lines.

        * Compound dimension values with logical operations - You can use multiple ``Expression``
        types and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression``
        objects. This allows you to filter on more advanced options. For example, you can filter on
        ``((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE !=
        DataTransfer)`` . The ``Expression`` for that looks like this:  ``{ "And": [ {"Or": [
        {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": {
        "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE",
        "Values": ["DataTransfer"] }}} ] }``

        .. note::

           Because each ``Expression`` can have only one operator, the service returns an error if
           more than one is specified. The following example shows an ``Expression`` object that
           creates an error.

          ``{ "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [
          "DataTransfer" ] } }``

        .. note::

          For ``GetRightsizingRecommendation`` action, a combination of OR and NOT is not supported.
          OR is not supported between different dimensions, or dimensions and tags. NOT operators
          aren't supported. Dimensions are also limited to ``LINKED_ACCOUNT`` , ``REGION`` , or
          ``RIGHTSIZING_TYPE`` .

    - **And** *(list) --*

      Return results that match both ``Dimension`` objects.

      - *(dict) --*

        Use ``Expression`` to filter by cost or by usage. There are two patterns:

        * Simple dimension values - You can set the dimension name and values for the filters that
        you plan to use. For example, you can filter for ``REGION==us-east-1 OR REGION==us-west-1`` .
        The ``Expression`` for that looks like this:  ``{ "Dimensions": { "Key": "REGION", "Values":
        [ "us-east-1", “us-west-1” ] } }``   The list of dimension values are OR'd together to
        retrieve cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects
        using either ``with*`` methods or ``set*`` methods in multiple lines.

        * Compound dimension values with logical operations - You can use multiple ``Expression``
        types and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression``
        objects. This allows you to filter on more advanced options. For example, you can filter on
        ``((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE !=
        DataTransfer)`` . The ``Expression`` for that looks like this:  ``{ "And": [ {"Or": [
        {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": {
        "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE",
        "Values": ["DataTransfer"] }}} ] }``

        .. note::

           Because each ``Expression`` can have only one operator, the service returns an error if
           more than one is specified. The following example shows an ``Expression`` object that
           creates an error.

          ``{ "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [
          "DataTransfer" ] } }``

        .. note::

          For ``GetRightsizingRecommendation`` action, a combination of OR and NOT is not supported.
          OR is not supported between different dimensions, or dimensions and tags. NOT operators
          aren't supported. Dimensions are also limited to ``LINKED_ACCOUNT`` , ``REGION`` , or
          ``RIGHTSIZING_TYPE`` .

    - **Not** *(dict) --*

      Return results that don't match a ``Dimension`` object.

    - **Dimensions** *(dict) --*

      The specific ``Dimension`` to use for ``Expression`` .

      - **Key** *(string) --*

        The names of the metadata types that you can use to filter and group your results. For
        example, ``AZ`` returns a list of Availability Zones.

      - **Values** *(list) --*

        The metadata values that you can use to filter and group your results. You can use
        ``GetDimensionValues`` to find specific values.

        Valid values for the ``SERVICE`` dimension are ``Amazon Elastic Compute Cloud - Compute`` ,
        ``Amazon Elasticsearch Service`` , ``Amazon ElastiCache`` , ``Amazon Redshift`` , and
        ``Amazon Relational Database Service`` .

        - *(string) --*

    - **Tags** *(dict) --*

      The specific ``Tag`` to use for ``Expression`` .

      - **Key** *(string) --*

        The key for the tag.

      - **Values** *(list) --*

        The specific value of the tag.

        - *(string) --*
    """


_ClientGetReservationUtilizationGroupByTypeDef = TypedDict(
    "_ClientGetReservationUtilizationGroupByTypeDef",
    {"Type": str, "Key": str},
    total=False,
)


class ClientGetReservationUtilizationGroupByTypeDef(
    _ClientGetReservationUtilizationGroupByTypeDef
):
    """
    Type definition for `ClientGetReservationUtilization` `GroupBy`

    Represents a group when you specify a group by criteria or in the response to a query with a
    specific grouping.

    - **Type** *(string) --*

      The string that represents the type of group.

    - **Key** *(string) --*

      The string that represents a key for a specified group.
    """


_ClientGetReservationUtilizationResponseTotalTypeDef = TypedDict(
    "_ClientGetReservationUtilizationResponseTotalTypeDef",
    {
        "UtilizationPercentage": str,
        "UtilizationPercentageInUnits": str,
        "PurchasedHours": str,
        "PurchasedUnits": str,
        "TotalActualHours": str,
        "TotalActualUnits": str,
        "UnusedHours": str,
        "UnusedUnits": str,
        "OnDemandCostOfRIHoursUsed": str,
        "NetRISavings": str,
        "TotalPotentialRISavings": str,
        "AmortizedUpfrontFee": str,
        "AmortizedRecurringFee": str,
        "TotalAmortizedFee": str,
    },
    total=False,
)


class ClientGetReservationUtilizationResponseTotalTypeDef(
    _ClientGetReservationUtilizationResponseTotalTypeDef
):
    """
    Type definition for `ClientGetReservationUtilizationResponse` `Total`

    The total amount of time that you used your RIs.

    - **UtilizationPercentage** *(string) --*

      The percentage of reservation time that you used.

    - **UtilizationPercentageInUnits** *(string) --*

      The percentage of Amazon EC2 reservation time that you used, converted to normalized units.
      Normalized units are available only for Amazon EC2 usage after November 11, 2017.

    - **PurchasedHours** *(string) --*

      How many reservation hours that you purchased.

    - **PurchasedUnits** *(string) --*

      How many Amazon EC2 reservation hours that you purchased, converted to normalized units.
      Normalized units are available only for Amazon EC2 usage after November 11, 2017.

    - **TotalActualHours** *(string) --*

      The total number of reservation hours that you used.

    - **TotalActualUnits** *(string) --*

      The total number of Amazon EC2 reservation hours that you used, converted to normalized
      units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

    - **UnusedHours** *(string) --*

      The number of reservation hours that you didn't use.

    - **UnusedUnits** *(string) --*

      The number of Amazon EC2 reservation hours that you didn't use, converted to normalized
      units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

    - **OnDemandCostOfRIHoursUsed** *(string) --*

      How much your reservation would cost if charged On-Demand rates.

    - **NetRISavings** *(string) --*

      How much you saved due to purchasing and utilizing reservation. AWS calculates this by
      subtracting ``TotalAmortizedFee`` from ``OnDemandCostOfRIHoursUsed`` .

    - **TotalPotentialRISavings** *(string) --*

      How much you could save if you use your entire reservation.

    - **AmortizedUpfrontFee** *(string) --*

      The upfront cost of your reservation, amortized over the reservation period.

    - **AmortizedRecurringFee** *(string) --*

      The monthly cost of your reservation, amortized over the reservation period.

    - **TotalAmortizedFee** *(string) --*

      The total cost of your reservation, amortized over the reservation period.
    """


_ClientGetReservationUtilizationResponseUtilizationsByTimeGroupsUtilizationTypeDef = TypedDict(
    "_ClientGetReservationUtilizationResponseUtilizationsByTimeGroupsUtilizationTypeDef",
    {
        "UtilizationPercentage": str,
        "UtilizationPercentageInUnits": str,
        "PurchasedHours": str,
        "PurchasedUnits": str,
        "TotalActualHours": str,
        "TotalActualUnits": str,
        "UnusedHours": str,
        "UnusedUnits": str,
        "OnDemandCostOfRIHoursUsed": str,
        "NetRISavings": str,
        "TotalPotentialRISavings": str,
        "AmortizedUpfrontFee": str,
        "AmortizedRecurringFee": str,
        "TotalAmortizedFee": str,
    },
    total=False,
)


class ClientGetReservationUtilizationResponseUtilizationsByTimeGroupsUtilizationTypeDef(
    _ClientGetReservationUtilizationResponseUtilizationsByTimeGroupsUtilizationTypeDef
):
    """
    Type definition for `ClientGetReservationUtilizationResponseUtilizationsByTimeGroups` `Utilization`

    How much you used this group of reservations.

    - **UtilizationPercentage** *(string) --*

      The percentage of reservation time that you used.

    - **UtilizationPercentageInUnits** *(string) --*

      The percentage of Amazon EC2 reservation time that you used, converted to
      normalized units. Normalized units are available only for Amazon EC2 usage after
      November 11, 2017.

    - **PurchasedHours** *(string) --*

      How many reservation hours that you purchased.

    - **PurchasedUnits** *(string) --*

      How many Amazon EC2 reservation hours that you purchased, converted to normalized
      units. Normalized units are available only for Amazon EC2 usage after November 11,
      2017.

    - **TotalActualHours** *(string) --*

      The total number of reservation hours that you used.

    - **TotalActualUnits** *(string) --*

      The total number of Amazon EC2 reservation hours that you used, converted to
      normalized units. Normalized units are available only for Amazon EC2 usage after
      November 11, 2017.

    - **UnusedHours** *(string) --*

      The number of reservation hours that you didn't use.

    - **UnusedUnits** *(string) --*

      The number of Amazon EC2 reservation hours that you didn't use, converted to
      normalized units. Normalized units are available only for Amazon EC2 usage after
      November 11, 2017.

    - **OnDemandCostOfRIHoursUsed** *(string) --*

      How much your reservation would cost if charged On-Demand rates.

    - **NetRISavings** *(string) --*

      How much you saved due to purchasing and utilizing reservation. AWS calculates this
      by subtracting ``TotalAmortizedFee`` from ``OnDemandCostOfRIHoursUsed`` .

    - **TotalPotentialRISavings** *(string) --*

      How much you could save if you use your entire reservation.

    - **AmortizedUpfrontFee** *(string) --*

      The upfront cost of your reservation, amortized over the reservation period.

    - **AmortizedRecurringFee** *(string) --*

      The monthly cost of your reservation, amortized over the reservation period.

    - **TotalAmortizedFee** *(string) --*

      The total cost of your reservation, amortized over the reservation period.
    """


_ClientGetReservationUtilizationResponseUtilizationsByTimeGroupsTypeDef = TypedDict(
    "_ClientGetReservationUtilizationResponseUtilizationsByTimeGroupsTypeDef",
    {
        "Key": str,
        "Value": str,
        "Attributes": Dict[str, str],
        "Utilization": ClientGetReservationUtilizationResponseUtilizationsByTimeGroupsUtilizationTypeDef,
    },
    total=False,
)


class ClientGetReservationUtilizationResponseUtilizationsByTimeGroupsTypeDef(
    _ClientGetReservationUtilizationResponseUtilizationsByTimeGroupsTypeDef
):
    """
    Type definition for `ClientGetReservationUtilizationResponseUtilizationsByTime` `Groups`

    A group of reservations that share a set of attributes.

    - **Key** *(string) --*

      The key for a specific reservation attribute.

    - **Value** *(string) --*

      The value of a specific reservation attribute.

    - **Attributes** *(dict) --*

      The attributes for this group of reservations.

      - *(string) --*

        - *(string) --*

    - **Utilization** *(dict) --*

      How much you used this group of reservations.

      - **UtilizationPercentage** *(string) --*

        The percentage of reservation time that you used.

      - **UtilizationPercentageInUnits** *(string) --*

        The percentage of Amazon EC2 reservation time that you used, converted to
        normalized units. Normalized units are available only for Amazon EC2 usage after
        November 11, 2017.

      - **PurchasedHours** *(string) --*

        How many reservation hours that you purchased.

      - **PurchasedUnits** *(string) --*

        How many Amazon EC2 reservation hours that you purchased, converted to normalized
        units. Normalized units are available only for Amazon EC2 usage after November 11,
        2017.

      - **TotalActualHours** *(string) --*

        The total number of reservation hours that you used.

      - **TotalActualUnits** *(string) --*

        The total number of Amazon EC2 reservation hours that you used, converted to
        normalized units. Normalized units are available only for Amazon EC2 usage after
        November 11, 2017.

      - **UnusedHours** *(string) --*

        The number of reservation hours that you didn't use.

      - **UnusedUnits** *(string) --*

        The number of Amazon EC2 reservation hours that you didn't use, converted to
        normalized units. Normalized units are available only for Amazon EC2 usage after
        November 11, 2017.

      - **OnDemandCostOfRIHoursUsed** *(string) --*

        How much your reservation would cost if charged On-Demand rates.

      - **NetRISavings** *(string) --*

        How much you saved due to purchasing and utilizing reservation. AWS calculates this
        by subtracting ``TotalAmortizedFee`` from ``OnDemandCostOfRIHoursUsed`` .

      - **TotalPotentialRISavings** *(string) --*

        How much you could save if you use your entire reservation.

      - **AmortizedUpfrontFee** *(string) --*

        The upfront cost of your reservation, amortized over the reservation period.

      - **AmortizedRecurringFee** *(string) --*

        The monthly cost of your reservation, amortized over the reservation period.

      - **TotalAmortizedFee** *(string) --*

        The total cost of your reservation, amortized over the reservation period.
    """


_ClientGetReservationUtilizationResponseUtilizationsByTimeTimePeriodTypeDef = TypedDict(
    "_ClientGetReservationUtilizationResponseUtilizationsByTimeTimePeriodTypeDef",
    {"Start": str, "End": str},
    total=False,
)


class ClientGetReservationUtilizationResponseUtilizationsByTimeTimePeriodTypeDef(
    _ClientGetReservationUtilizationResponseUtilizationsByTimeTimePeriodTypeDef
):
    """
    Type definition for `ClientGetReservationUtilizationResponseUtilizationsByTime` `TimePeriod`

    The period of time that this utilization was used for.

    - **Start** *(string) --*

      The beginning of the time period that you want the usage and costs for. The start date
      is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and
      usage data starting at ``2017-01-01`` up to the end date.

    - **End** *(string) --*

      The end of the time period that you want the usage and costs for. The end date is
      exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage
      data from the start date up to, but not including, ``2017-05-01`` .
    """


_ClientGetReservationUtilizationResponseUtilizationsByTimeTotalTypeDef = TypedDict(
    "_ClientGetReservationUtilizationResponseUtilizationsByTimeTotalTypeDef",
    {
        "UtilizationPercentage": str,
        "UtilizationPercentageInUnits": str,
        "PurchasedHours": str,
        "PurchasedUnits": str,
        "TotalActualHours": str,
        "TotalActualUnits": str,
        "UnusedHours": str,
        "UnusedUnits": str,
        "OnDemandCostOfRIHoursUsed": str,
        "NetRISavings": str,
        "TotalPotentialRISavings": str,
        "AmortizedUpfrontFee": str,
        "AmortizedRecurringFee": str,
        "TotalAmortizedFee": str,
    },
    total=False,
)


class ClientGetReservationUtilizationResponseUtilizationsByTimeTotalTypeDef(
    _ClientGetReservationUtilizationResponseUtilizationsByTimeTotalTypeDef
):
    """
    Type definition for `ClientGetReservationUtilizationResponseUtilizationsByTime` `Total`

    The total number of reservation hours that were used.

    - **UtilizationPercentage** *(string) --*

      The percentage of reservation time that you used.

    - **UtilizationPercentageInUnits** *(string) --*

      The percentage of Amazon EC2 reservation time that you used, converted to normalized
      units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

    - **PurchasedHours** *(string) --*

      How many reservation hours that you purchased.

    - **PurchasedUnits** *(string) --*

      How many Amazon EC2 reservation hours that you purchased, converted to normalized
      units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

    - **TotalActualHours** *(string) --*

      The total number of reservation hours that you used.

    - **TotalActualUnits** *(string) --*

      The total number of Amazon EC2 reservation hours that you used, converted to normalized
      units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

    - **UnusedHours** *(string) --*

      The number of reservation hours that you didn't use.

    - **UnusedUnits** *(string) --*

      The number of Amazon EC2 reservation hours that you didn't use, converted to normalized
      units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

    - **OnDemandCostOfRIHoursUsed** *(string) --*

      How much your reservation would cost if charged On-Demand rates.

    - **NetRISavings** *(string) --*

      How much you saved due to purchasing and utilizing reservation. AWS calculates this by
      subtracting ``TotalAmortizedFee`` from ``OnDemandCostOfRIHoursUsed`` .

    - **TotalPotentialRISavings** *(string) --*

      How much you could save if you use your entire reservation.

    - **AmortizedUpfrontFee** *(string) --*

      The upfront cost of your reservation, amortized over the reservation period.

    - **AmortizedRecurringFee** *(string) --*

      The monthly cost of your reservation, amortized over the reservation period.

    - **TotalAmortizedFee** *(string) --*

      The total cost of your reservation, amortized over the reservation period.
    """


_ClientGetReservationUtilizationResponseUtilizationsByTimeTypeDef = TypedDict(
    "_ClientGetReservationUtilizationResponseUtilizationsByTimeTypeDef",
    {
        "TimePeriod": ClientGetReservationUtilizationResponseUtilizationsByTimeTimePeriodTypeDef,
        "Groups": List[
            ClientGetReservationUtilizationResponseUtilizationsByTimeGroupsTypeDef
        ],
        "Total": ClientGetReservationUtilizationResponseUtilizationsByTimeTotalTypeDef,
    },
    total=False,
)


class ClientGetReservationUtilizationResponseUtilizationsByTimeTypeDef(
    _ClientGetReservationUtilizationResponseUtilizationsByTimeTypeDef
):
    """
    Type definition for `ClientGetReservationUtilizationResponse` `UtilizationsByTime`

    The amount of utilization, in hours.

    - **TimePeriod** *(dict) --*

      The period of time that this utilization was used for.

      - **Start** *(string) --*

        The beginning of the time period that you want the usage and costs for. The start date
        is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and
        usage data starting at ``2017-01-01`` up to the end date.

      - **End** *(string) --*

        The end of the time period that you want the usage and costs for. The end date is
        exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage
        data from the start date up to, but not including, ``2017-05-01`` .

    - **Groups** *(list) --*

      The groups that this utilization result uses.

      - *(dict) --*

        A group of reservations that share a set of attributes.

        - **Key** *(string) --*

          The key for a specific reservation attribute.

        - **Value** *(string) --*

          The value of a specific reservation attribute.

        - **Attributes** *(dict) --*

          The attributes for this group of reservations.

          - *(string) --*

            - *(string) --*

        - **Utilization** *(dict) --*

          How much you used this group of reservations.

          - **UtilizationPercentage** *(string) --*

            The percentage of reservation time that you used.

          - **UtilizationPercentageInUnits** *(string) --*

            The percentage of Amazon EC2 reservation time that you used, converted to
            normalized units. Normalized units are available only for Amazon EC2 usage after
            November 11, 2017.

          - **PurchasedHours** *(string) --*

            How many reservation hours that you purchased.

          - **PurchasedUnits** *(string) --*

            How many Amazon EC2 reservation hours that you purchased, converted to normalized
            units. Normalized units are available only for Amazon EC2 usage after November 11,
            2017.

          - **TotalActualHours** *(string) --*

            The total number of reservation hours that you used.

          - **TotalActualUnits** *(string) --*

            The total number of Amazon EC2 reservation hours that you used, converted to
            normalized units. Normalized units are available only for Amazon EC2 usage after
            November 11, 2017.

          - **UnusedHours** *(string) --*

            The number of reservation hours that you didn't use.

          - **UnusedUnits** *(string) --*

            The number of Amazon EC2 reservation hours that you didn't use, converted to
            normalized units. Normalized units are available only for Amazon EC2 usage after
            November 11, 2017.

          - **OnDemandCostOfRIHoursUsed** *(string) --*

            How much your reservation would cost if charged On-Demand rates.

          - **NetRISavings** *(string) --*

            How much you saved due to purchasing and utilizing reservation. AWS calculates this
            by subtracting ``TotalAmortizedFee`` from ``OnDemandCostOfRIHoursUsed`` .

          - **TotalPotentialRISavings** *(string) --*

            How much you could save if you use your entire reservation.

          - **AmortizedUpfrontFee** *(string) --*

            The upfront cost of your reservation, amortized over the reservation period.

          - **AmortizedRecurringFee** *(string) --*

            The monthly cost of your reservation, amortized over the reservation period.

          - **TotalAmortizedFee** *(string) --*

            The total cost of your reservation, amortized over the reservation period.

    - **Total** *(dict) --*

      The total number of reservation hours that were used.

      - **UtilizationPercentage** *(string) --*

        The percentage of reservation time that you used.

      - **UtilizationPercentageInUnits** *(string) --*

        The percentage of Amazon EC2 reservation time that you used, converted to normalized
        units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

      - **PurchasedHours** *(string) --*

        How many reservation hours that you purchased.

      - **PurchasedUnits** *(string) --*

        How many Amazon EC2 reservation hours that you purchased, converted to normalized
        units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

      - **TotalActualHours** *(string) --*

        The total number of reservation hours that you used.

      - **TotalActualUnits** *(string) --*

        The total number of Amazon EC2 reservation hours that you used, converted to normalized
        units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

      - **UnusedHours** *(string) --*

        The number of reservation hours that you didn't use.

      - **UnusedUnits** *(string) --*

        The number of Amazon EC2 reservation hours that you didn't use, converted to normalized
        units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

      - **OnDemandCostOfRIHoursUsed** *(string) --*

        How much your reservation would cost if charged On-Demand rates.

      - **NetRISavings** *(string) --*

        How much you saved due to purchasing and utilizing reservation. AWS calculates this by
        subtracting ``TotalAmortizedFee`` from ``OnDemandCostOfRIHoursUsed`` .

      - **TotalPotentialRISavings** *(string) --*

        How much you could save if you use your entire reservation.

      - **AmortizedUpfrontFee** *(string) --*

        The upfront cost of your reservation, amortized over the reservation period.

      - **AmortizedRecurringFee** *(string) --*

        The monthly cost of your reservation, amortized over the reservation period.

      - **TotalAmortizedFee** *(string) --*

        The total cost of your reservation, amortized over the reservation period.
    """


_ClientGetReservationUtilizationResponseTypeDef = TypedDict(
    "_ClientGetReservationUtilizationResponseTypeDef",
    {
        "UtilizationsByTime": List[
            ClientGetReservationUtilizationResponseUtilizationsByTimeTypeDef
        ],
        "Total": ClientGetReservationUtilizationResponseTotalTypeDef,
        "NextPageToken": str,
    },
    total=False,
)


class ClientGetReservationUtilizationResponseTypeDef(
    _ClientGetReservationUtilizationResponseTypeDef
):
    """
    Type definition for `ClientGetReservationUtilization` `Response`

    - **UtilizationsByTime** *(list) --*

      The amount of time that you used your RIs.

      - *(dict) --*

        The amount of utilization, in hours.

        - **TimePeriod** *(dict) --*

          The period of time that this utilization was used for.

          - **Start** *(string) --*

            The beginning of the time period that you want the usage and costs for. The start date
            is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and
            usage data starting at ``2017-01-01`` up to the end date.

          - **End** *(string) --*

            The end of the time period that you want the usage and costs for. The end date is
            exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage
            data from the start date up to, but not including, ``2017-05-01`` .

        - **Groups** *(list) --*

          The groups that this utilization result uses.

          - *(dict) --*

            A group of reservations that share a set of attributes.

            - **Key** *(string) --*

              The key for a specific reservation attribute.

            - **Value** *(string) --*

              The value of a specific reservation attribute.

            - **Attributes** *(dict) --*

              The attributes for this group of reservations.

              - *(string) --*

                - *(string) --*

            - **Utilization** *(dict) --*

              How much you used this group of reservations.

              - **UtilizationPercentage** *(string) --*

                The percentage of reservation time that you used.

              - **UtilizationPercentageInUnits** *(string) --*

                The percentage of Amazon EC2 reservation time that you used, converted to
                normalized units. Normalized units are available only for Amazon EC2 usage after
                November 11, 2017.

              - **PurchasedHours** *(string) --*

                How many reservation hours that you purchased.

              - **PurchasedUnits** *(string) --*

                How many Amazon EC2 reservation hours that you purchased, converted to normalized
                units. Normalized units are available only for Amazon EC2 usage after November 11,
                2017.

              - **TotalActualHours** *(string) --*

                The total number of reservation hours that you used.

              - **TotalActualUnits** *(string) --*

                The total number of Amazon EC2 reservation hours that you used, converted to
                normalized units. Normalized units are available only for Amazon EC2 usage after
                November 11, 2017.

              - **UnusedHours** *(string) --*

                The number of reservation hours that you didn't use.

              - **UnusedUnits** *(string) --*

                The number of Amazon EC2 reservation hours that you didn't use, converted to
                normalized units. Normalized units are available only for Amazon EC2 usage after
                November 11, 2017.

              - **OnDemandCostOfRIHoursUsed** *(string) --*

                How much your reservation would cost if charged On-Demand rates.

              - **NetRISavings** *(string) --*

                How much you saved due to purchasing and utilizing reservation. AWS calculates this
                by subtracting ``TotalAmortizedFee`` from ``OnDemandCostOfRIHoursUsed`` .

              - **TotalPotentialRISavings** *(string) --*

                How much you could save if you use your entire reservation.

              - **AmortizedUpfrontFee** *(string) --*

                The upfront cost of your reservation, amortized over the reservation period.

              - **AmortizedRecurringFee** *(string) --*

                The monthly cost of your reservation, amortized over the reservation period.

              - **TotalAmortizedFee** *(string) --*

                The total cost of your reservation, amortized over the reservation period.

        - **Total** *(dict) --*

          The total number of reservation hours that were used.

          - **UtilizationPercentage** *(string) --*

            The percentage of reservation time that you used.

          - **UtilizationPercentageInUnits** *(string) --*

            The percentage of Amazon EC2 reservation time that you used, converted to normalized
            units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

          - **PurchasedHours** *(string) --*

            How many reservation hours that you purchased.

          - **PurchasedUnits** *(string) --*

            How many Amazon EC2 reservation hours that you purchased, converted to normalized
            units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

          - **TotalActualHours** *(string) --*

            The total number of reservation hours that you used.

          - **TotalActualUnits** *(string) --*

            The total number of Amazon EC2 reservation hours that you used, converted to normalized
            units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

          - **UnusedHours** *(string) --*

            The number of reservation hours that you didn't use.

          - **UnusedUnits** *(string) --*

            The number of Amazon EC2 reservation hours that you didn't use, converted to normalized
            units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

          - **OnDemandCostOfRIHoursUsed** *(string) --*

            How much your reservation would cost if charged On-Demand rates.

          - **NetRISavings** *(string) --*

            How much you saved due to purchasing and utilizing reservation. AWS calculates this by
            subtracting ``TotalAmortizedFee`` from ``OnDemandCostOfRIHoursUsed`` .

          - **TotalPotentialRISavings** *(string) --*

            How much you could save if you use your entire reservation.

          - **AmortizedUpfrontFee** *(string) --*

            The upfront cost of your reservation, amortized over the reservation period.

          - **AmortizedRecurringFee** *(string) --*

            The monthly cost of your reservation, amortized over the reservation period.

          - **TotalAmortizedFee** *(string) --*

            The total cost of your reservation, amortized over the reservation period.

    - **Total** *(dict) --*

      The total amount of time that you used your RIs.

      - **UtilizationPercentage** *(string) --*

        The percentage of reservation time that you used.

      - **UtilizationPercentageInUnits** *(string) --*

        The percentage of Amazon EC2 reservation time that you used, converted to normalized units.
        Normalized units are available only for Amazon EC2 usage after November 11, 2017.

      - **PurchasedHours** *(string) --*

        How many reservation hours that you purchased.

      - **PurchasedUnits** *(string) --*

        How many Amazon EC2 reservation hours that you purchased, converted to normalized units.
        Normalized units are available only for Amazon EC2 usage after November 11, 2017.

      - **TotalActualHours** *(string) --*

        The total number of reservation hours that you used.

      - **TotalActualUnits** *(string) --*

        The total number of Amazon EC2 reservation hours that you used, converted to normalized
        units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

      - **UnusedHours** *(string) --*

        The number of reservation hours that you didn't use.

      - **UnusedUnits** *(string) --*

        The number of Amazon EC2 reservation hours that you didn't use, converted to normalized
        units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

      - **OnDemandCostOfRIHoursUsed** *(string) --*

        How much your reservation would cost if charged On-Demand rates.

      - **NetRISavings** *(string) --*

        How much you saved due to purchasing and utilizing reservation. AWS calculates this by
        subtracting ``TotalAmortizedFee`` from ``OnDemandCostOfRIHoursUsed`` .

      - **TotalPotentialRISavings** *(string) --*

        How much you could save if you use your entire reservation.

      - **AmortizedUpfrontFee** *(string) --*

        The upfront cost of your reservation, amortized over the reservation period.

      - **AmortizedRecurringFee** *(string) --*

        The monthly cost of your reservation, amortized over the reservation period.

      - **TotalAmortizedFee** *(string) --*

        The total cost of your reservation, amortized over the reservation period.

    - **NextPageToken** *(string) --*

      The token for the next set of retrievable results. AWS provides the token when the response
      from a previous call has more results than the maximum page size.
    """


_ClientGetReservationUtilizationTimePeriodTypeDef = TypedDict(
    "_ClientGetReservationUtilizationTimePeriodTypeDef", {"Start": str, "End": str}
)


class ClientGetReservationUtilizationTimePeriodTypeDef(
    _ClientGetReservationUtilizationTimePeriodTypeDef
):
    """
    Type definition for `ClientGetReservationUtilization` `TimePeriod`

    Sets the start and end dates for retrieving RI utilization. The start date is inclusive, but the
    end date is exclusive. For example, if ``start`` is ``2017-01-01`` and ``end`` is ``2017-05-01``
    , then the cost and usage data is retrieved from ``2017-01-01`` up to and including
    ``2017-04-30`` but not including ``2017-05-01`` .

    - **Start** *(string) --* **[REQUIRED]**

      The beginning of the time period that you want the usage and costs for. The start date is
      inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data
      starting at ``2017-01-01`` up to the end date.

    - **End** *(string) --* **[REQUIRED]**

      The end of the time period that you want the usage and costs for. The end date is exclusive.
      For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage data from the start
      date up to, but not including, ``2017-05-01`` .
    """


_ClientGetRightsizingRecommendationFilterDimensionsTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationFilterDimensionsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetRightsizingRecommendationFilterDimensionsTypeDef(
    _ClientGetRightsizingRecommendationFilterDimensionsTypeDef
):
    """
    Type definition for `ClientGetRightsizingRecommendationFilter` `Dimensions`

    The specific ``Dimension`` to use for ``Expression`` .

    - **Key** *(string) --*

      The names of the metadata types that you can use to filter and group your results. For
      example, ``AZ`` returns a list of Availability Zones.

    - **Values** *(list) --*

      The metadata values that you can use to filter and group your results. You can use
      ``GetDimensionValues`` to find specific values.

      Valid values for the ``SERVICE`` dimension are ``Amazon Elastic Compute Cloud - Compute`` ,
      ``Amazon Elasticsearch Service`` , ``Amazon ElastiCache`` , ``Amazon Redshift`` , and
      ``Amazon Relational Database Service`` .

      - *(string) --*
    """


_ClientGetRightsizingRecommendationFilterTagsTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationFilterTagsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetRightsizingRecommendationFilterTagsTypeDef(
    _ClientGetRightsizingRecommendationFilterTagsTypeDef
):
    """
    Type definition for `ClientGetRightsizingRecommendationFilter` `Tags`

    The specific ``Tag`` to use for ``Expression`` .

    - **Key** *(string) --*

      The key for the tag.

    - **Values** *(list) --*

      The specific value of the tag.

      - *(string) --*
    """


_ClientGetRightsizingRecommendationFilterTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationFilterTypeDef",
    {
        "Or": List[Dict],
        "And": List[Dict],
        "Not": Dict,
        "Dimensions": ClientGetRightsizingRecommendationFilterDimensionsTypeDef,
        "Tags": ClientGetRightsizingRecommendationFilterTagsTypeDef,
    },
    total=False,
)


class ClientGetRightsizingRecommendationFilterTypeDef(
    _ClientGetRightsizingRecommendationFilterTypeDef
):
    """
    Type definition for `ClientGetRightsizingRecommendation` `Filter`

    Use ``Expression`` to filter by cost or by usage. There are two patterns:

    * Simple dimension values - You can set the dimension name and values for the filters that you
    plan to use. For example, you can filter for ``REGION==us-east-1 OR REGION==us-west-1`` . The
    ``Expression`` for that looks like this:  ``{ "Dimensions": { "Key": "REGION", "Values": [
    "us-east-1", “us-west-1” ] } }``   The list of dimension values are OR'd together to retrieve
    cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects using either
    ``with*`` methods or ``set*`` methods in multiple lines.

    * Compound dimension values with logical operations - You can use multiple ``Expression`` types
    and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression`` objects.
    This allows you to filter on more advanced options. For example, you can filter on ``((REGION ==
    us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer)`` .
    The ``Expression`` for that looks like this:  ``{ "And": [ {"Or": [ {"Dimensions": { "Key":
    "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": { "Key": "TagName", "Values":
    ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE", "Values": ["DataTransfer"] }}} ]
    }``

    .. note::

       Because each ``Expression`` can have only one operator, the service returns an error if more
       than one is specified. The following example shows an ``Expression`` object that creates an
       error.

      ``{ "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [ "DataTransfer"
      ] } }``

    .. note::

      For ``GetRightsizingRecommendation`` action, a combination of OR and NOT is not supported. OR
      is not supported between different dimensions, or dimensions and tags. NOT operators aren't
      supported. Dimensions are also limited to ``LINKED_ACCOUNT`` , ``REGION`` , or
      ``RIGHTSIZING_TYPE`` .

    - **Or** *(list) --*

      Return results that match either ``Dimension`` object.

      - *(dict) --*

        Use ``Expression`` to filter by cost or by usage. There are two patterns:

        * Simple dimension values - You can set the dimension name and values for the filters that
        you plan to use. For example, you can filter for ``REGION==us-east-1 OR REGION==us-west-1`` .
        The ``Expression`` for that looks like this:  ``{ "Dimensions": { "Key": "REGION", "Values":
        [ "us-east-1", “us-west-1” ] } }``   The list of dimension values are OR'd together to
        retrieve cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects
        using either ``with*`` methods or ``set*`` methods in multiple lines.

        * Compound dimension values with logical operations - You can use multiple ``Expression``
        types and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression``
        objects. This allows you to filter on more advanced options. For example, you can filter on
        ``((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE !=
        DataTransfer)`` . The ``Expression`` for that looks like this:  ``{ "And": [ {"Or": [
        {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": {
        "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE",
        "Values": ["DataTransfer"] }}} ] }``

        .. note::

           Because each ``Expression`` can have only one operator, the service returns an error if
           more than one is specified. The following example shows an ``Expression`` object that
           creates an error.

          ``{ "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [
          "DataTransfer" ] } }``

        .. note::

          For ``GetRightsizingRecommendation`` action, a combination of OR and NOT is not supported.
          OR is not supported between different dimensions, or dimensions and tags. NOT operators
          aren't supported. Dimensions are also limited to ``LINKED_ACCOUNT`` , ``REGION`` , or
          ``RIGHTSIZING_TYPE`` .

    - **And** *(list) --*

      Return results that match both ``Dimension`` objects.

      - *(dict) --*

        Use ``Expression`` to filter by cost or by usage. There are two patterns:

        * Simple dimension values - You can set the dimension name and values for the filters that
        you plan to use. For example, you can filter for ``REGION==us-east-1 OR REGION==us-west-1`` .
        The ``Expression`` for that looks like this:  ``{ "Dimensions": { "Key": "REGION", "Values":
        [ "us-east-1", “us-west-1” ] } }``   The list of dimension values are OR'd together to
        retrieve cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects
        using either ``with*`` methods or ``set*`` methods in multiple lines.

        * Compound dimension values with logical operations - You can use multiple ``Expression``
        types and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression``
        objects. This allows you to filter on more advanced options. For example, you can filter on
        ``((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE !=
        DataTransfer)`` . The ``Expression`` for that looks like this:  ``{ "And": [ {"Or": [
        {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": {
        "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE",
        "Values": ["DataTransfer"] }}} ] }``

        .. note::

           Because each ``Expression`` can have only one operator, the service returns an error if
           more than one is specified. The following example shows an ``Expression`` object that
           creates an error.

          ``{ "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [
          "DataTransfer" ] } }``

        .. note::

          For ``GetRightsizingRecommendation`` action, a combination of OR and NOT is not supported.
          OR is not supported between different dimensions, or dimensions and tags. NOT operators
          aren't supported. Dimensions are also limited to ``LINKED_ACCOUNT`` , ``REGION`` , or
          ``RIGHTSIZING_TYPE`` .

    - **Not** *(dict) --*

      Return results that don't match a ``Dimension`` object.

    - **Dimensions** *(dict) --*

      The specific ``Dimension`` to use for ``Expression`` .

      - **Key** *(string) --*

        The names of the metadata types that you can use to filter and group your results. For
        example, ``AZ`` returns a list of Availability Zones.

      - **Values** *(list) --*

        The metadata values that you can use to filter and group your results. You can use
        ``GetDimensionValues`` to find specific values.

        Valid values for the ``SERVICE`` dimension are ``Amazon Elastic Compute Cloud - Compute`` ,
        ``Amazon Elasticsearch Service`` , ``Amazon ElastiCache`` , ``Amazon Redshift`` , and
        ``Amazon Relational Database Service`` .

        - *(string) --*

    - **Tags** *(dict) --*

      The specific ``Tag`` to use for ``Expression`` .

      - **Key** *(string) --*

        The key for the tag.

      - **Values** *(list) --*

        The specific value of the tag.

        - *(string) --*
    """


_ClientGetRightsizingRecommendationResponseMetadataTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseMetadataTypeDef",
    {"RecommendationId": str, "GenerationTimestamp": str, "LookbackPeriodInDays": str},
    total=False,
)


class ClientGetRightsizingRecommendationResponseMetadataTypeDef(
    _ClientGetRightsizingRecommendationResponseMetadataTypeDef
):
    """
    Type definition for `ClientGetRightsizingRecommendationResponse` `Metadata`

    Information regarding this specific recommendation set.

    - **RecommendationId** *(string) --*

      The ID for this specific recommendation.

    - **GenerationTimestamp** *(string) --*

      The time stamp for when Amazon Web Services made this recommendation.

    - **LookbackPeriodInDays** *(string) --*

      How many days of previous usage that Amazon Web Services considers when making this
      recommendation.
    """


_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceDetailsEC2ResourceDetailsTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceDetailsEC2ResourceDetailsTypeDef",
    {
        "HourlyOnDemandRate": str,
        "InstanceType": str,
        "Platform": str,
        "Region": str,
        "Sku": str,
        "Memory": str,
        "NetworkPerformance": str,
        "Storage": str,
        "Vcpu": str,
    },
    total=False,
)


class ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceDetailsEC2ResourceDetailsTypeDef(
    _ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceDetailsEC2ResourceDetailsTypeDef
):
    """
    Type definition for `ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceDetails` `EC2ResourceDetails`

    Details on the Amazon EC2 resource.

    - **HourlyOnDemandRate** *(string) --*

      Hourly public On Demand rate for the instance type.

    - **InstanceType** *(string) --*

      The type of Amazon Web Services instance.

    - **Platform** *(string) --*

      The platform of the Amazon Web Services instance. The platform is the specific
      combination of operating system, license model, and software on an instance.

    - **Region** *(string) --*

      The Amazon Web Services Region of the instance.

    - **Sku** *(string) --*

      The SKU of the product.

    - **Memory** *(string) --*

      Memory capacity of Amazon Web Services instance.

    - **NetworkPerformance** *(string) --*

      Network performance capacity of the Amazon Web Services instance.

    - **Storage** *(string) --*

      The disk storage of the Amazon Web Services instance (Not EBS storage).

    - **Vcpu** *(string) --*

      Number of VCPU cores in the Amazon Web Services instance type.
    """


_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceDetailsTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceDetailsTypeDef",
    {
        "EC2ResourceDetails": ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceDetailsEC2ResourceDetailsTypeDef
    },
    total=False,
)


class ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceDetailsTypeDef(
    _ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceDetailsTypeDef
):
    """
    Type definition for `ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstance` `ResourceDetails`

    Details about the resource and utilization.

    - **EC2ResourceDetails** *(dict) --*

      Details on the Amazon EC2 resource.

      - **HourlyOnDemandRate** *(string) --*

        Hourly public On Demand rate for the instance type.

      - **InstanceType** *(string) --*

        The type of Amazon Web Services instance.

      - **Platform** *(string) --*

        The platform of the Amazon Web Services instance. The platform is the specific
        combination of operating system, license model, and software on an instance.

      - **Region** *(string) --*

        The Amazon Web Services Region of the instance.

      - **Sku** *(string) --*

        The SKU of the product.

      - **Memory** *(string) --*

        Memory capacity of Amazon Web Services instance.

      - **NetworkPerformance** *(string) --*

        Network performance capacity of the Amazon Web Services instance.

      - **Storage** *(string) --*

        The disk storage of the Amazon Web Services instance (Not EBS storage).

      - **Vcpu** *(string) --*

        Number of VCPU cores in the Amazon Web Services instance type.
    """


_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceUtilizationEC2ResourceUtilizationTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceUtilizationEC2ResourceUtilizationTypeDef",
    {
        "MaxCpuUtilizationPercentage": str,
        "MaxMemoryUtilizationPercentage": str,
        "MaxStorageUtilizationPercentage": str,
    },
    total=False,
)


class ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceUtilizationEC2ResourceUtilizationTypeDef(
    _ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceUtilizationEC2ResourceUtilizationTypeDef
):
    """
    Type definition for `ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceUtilization` `EC2ResourceUtilization`

    Utilization of current Amazon EC2 Instance

    - **MaxCpuUtilizationPercentage** *(string) --*

      Maximum observed or expected CPU utilization of the instance.

    - **MaxMemoryUtilizationPercentage** *(string) --*

      Maximum observed or expected memory utilization of the instance.

    - **MaxStorageUtilizationPercentage** *(string) --*

      Maximum observed or expected storage utilization of the instance (does not measure
      EBS storage).
    """


_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceUtilizationTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceUtilizationTypeDef",
    {
        "EC2ResourceUtilization": ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceUtilizationEC2ResourceUtilizationTypeDef
    },
    total=False,
)


class ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceUtilizationTypeDef(
    _ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceUtilizationTypeDef
):
    """
    Type definition for `ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstance` `ResourceUtilization`

    Utilization information of the current instance during the lookback period.

    - **EC2ResourceUtilization** *(dict) --*

      Utilization of current Amazon EC2 Instance

      - **MaxCpuUtilizationPercentage** *(string) --*

        Maximum observed or expected CPU utilization of the instance.

      - **MaxMemoryUtilizationPercentage** *(string) --*

        Maximum observed or expected memory utilization of the instance.

      - **MaxStorageUtilizationPercentage** *(string) --*

        Maximum observed or expected storage utilization of the instance (does not measure
        EBS storage).
    """


_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceTagsTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceTagsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceTagsTypeDef(
    _ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceTagsTypeDef
):
    """
    Type definition for `ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstance` `Tags`

    The values that are available for a tag.

    - **Key** *(string) --*

      The key for the tag.

    - **Values** *(list) --*

      The specific value of the tag.

      - *(string) --*
    """


_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceTypeDef",
    {
        "ResourceId": str,
        "Tags": List[
            ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceTagsTypeDef
        ],
        "ResourceDetails": ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceDetailsTypeDef,
        "ResourceUtilization": ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceUtilizationTypeDef,
        "ReservationCoveredHoursInLookbackPeriod": str,
        "SavingsPlansCoveredHoursInLookbackPeriod": str,
        "OnDemandHoursInLookbackPeriod": str,
        "TotalRunningHoursInLookbackPeriod": str,
        "MonthlyCost": str,
        "CurrencyCode": str,
    },
    total=False,
)


class ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceTypeDef(
    _ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceTypeDef
):
    """
    Type definition for `ClientGetRightsizingRecommendationResponseRightsizingRecommendations` `CurrentInstance`

    Context regarding the current instance.

    - **ResourceId** *(string) --*

      Resource ID of the current instance.

    - **Tags** *(list) --*

      Cost allocation resource tags applied to the instance.

      - *(dict) --*

        The values that are available for a tag.

        - **Key** *(string) --*

          The key for the tag.

        - **Values** *(list) --*

          The specific value of the tag.

          - *(string) --*

    - **ResourceDetails** *(dict) --*

      Details about the resource and utilization.

      - **EC2ResourceDetails** *(dict) --*

        Details on the Amazon EC2 resource.

        - **HourlyOnDemandRate** *(string) --*

          Hourly public On Demand rate for the instance type.

        - **InstanceType** *(string) --*

          The type of Amazon Web Services instance.

        - **Platform** *(string) --*

          The platform of the Amazon Web Services instance. The platform is the specific
          combination of operating system, license model, and software on an instance.

        - **Region** *(string) --*

          The Amazon Web Services Region of the instance.

        - **Sku** *(string) --*

          The SKU of the product.

        - **Memory** *(string) --*

          Memory capacity of Amazon Web Services instance.

        - **NetworkPerformance** *(string) --*

          Network performance capacity of the Amazon Web Services instance.

        - **Storage** *(string) --*

          The disk storage of the Amazon Web Services instance (Not EBS storage).

        - **Vcpu** *(string) --*

          Number of VCPU cores in the Amazon Web Services instance type.

    - **ResourceUtilization** *(dict) --*

      Utilization information of the current instance during the lookback period.

      - **EC2ResourceUtilization** *(dict) --*

        Utilization of current Amazon EC2 Instance

        - **MaxCpuUtilizationPercentage** *(string) --*

          Maximum observed or expected CPU utilization of the instance.

        - **MaxMemoryUtilizationPercentage** *(string) --*

          Maximum observed or expected memory utilization of the instance.

        - **MaxStorageUtilizationPercentage** *(string) --*

          Maximum observed or expected storage utilization of the instance (does not measure
          EBS storage).

    - **ReservationCoveredHoursInLookbackPeriod** *(string) --*

      Number of hours during the lookback period covered by reservations.

    - **SavingsPlansCoveredHoursInLookbackPeriod** *(string) --*

      Number of hours during the lookback period covered by Savings Plans.

    - **OnDemandHoursInLookbackPeriod** *(string) --*

      Number of hours during the lookback period billed at On Demand rates.

    - **TotalRunningHoursInLookbackPeriod** *(string) --*

      The total number of hours the instance ran during the lookback period.

    - **MonthlyCost** *(string) --*

      Current On Demand cost of operating this instance on a monthly basis.

    - **CurrencyCode** *(string) --*

      The currency code that Amazon Web Services used to calculate the costs for this
      instance.
    """


_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesExpectedResourceUtilizationEC2ResourceUtilizationTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesExpectedResourceUtilizationEC2ResourceUtilizationTypeDef",
    {
        "MaxCpuUtilizationPercentage": str,
        "MaxMemoryUtilizationPercentage": str,
        "MaxStorageUtilizationPercentage": str,
    },
    total=False,
)


class ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesExpectedResourceUtilizationEC2ResourceUtilizationTypeDef(
    _ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesExpectedResourceUtilizationEC2ResourceUtilizationTypeDef
):
    """
    Type definition for `ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesExpectedResourceUtilization` `EC2ResourceUtilization`

    Utilization of current Amazon EC2 Instance

    - **MaxCpuUtilizationPercentage** *(string) --*

      Maximum observed or expected CPU utilization of the instance.

    - **MaxMemoryUtilizationPercentage** *(string) --*

      Maximum observed or expected memory utilization of the instance.

    - **MaxStorageUtilizationPercentage** *(string) --*

      Maximum observed or expected storage utilization of the instance (does not
      measure EBS storage).
    """


_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesExpectedResourceUtilizationTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesExpectedResourceUtilizationTypeDef",
    {
        "EC2ResourceUtilization": ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesExpectedResourceUtilizationEC2ResourceUtilizationTypeDef
    },
    total=False,
)


class ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesExpectedResourceUtilizationTypeDef(
    _ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesExpectedResourceUtilizationTypeDef
):
    """
    Type definition for `ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstances` `ExpectedResourceUtilization`

    Expected utilization metrics for target instance type.

    - **EC2ResourceUtilization** *(dict) --*

      Utilization of current Amazon EC2 Instance

      - **MaxCpuUtilizationPercentage** *(string) --*

        Maximum observed or expected CPU utilization of the instance.

      - **MaxMemoryUtilizationPercentage** *(string) --*

        Maximum observed or expected memory utilization of the instance.

      - **MaxStorageUtilizationPercentage** *(string) --*

        Maximum observed or expected storage utilization of the instance (does not
        measure EBS storage).
    """


_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesResourceDetailsEC2ResourceDetailsTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesResourceDetailsEC2ResourceDetailsTypeDef",
    {
        "HourlyOnDemandRate": str,
        "InstanceType": str,
        "Platform": str,
        "Region": str,
        "Sku": str,
        "Memory": str,
        "NetworkPerformance": str,
        "Storage": str,
        "Vcpu": str,
    },
    total=False,
)


class ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesResourceDetailsEC2ResourceDetailsTypeDef(
    _ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesResourceDetailsEC2ResourceDetailsTypeDef
):
    """
    Type definition for `ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesResourceDetails` `EC2ResourceDetails`

    Details on the Amazon EC2 resource.

    - **HourlyOnDemandRate** *(string) --*

      Hourly public On Demand rate for the instance type.

    - **InstanceType** *(string) --*

      The type of Amazon Web Services instance.

    - **Platform** *(string) --*

      The platform of the Amazon Web Services instance. The platform is the specific
      combination of operating system, license model, and software on an instance.

    - **Region** *(string) --*

      The Amazon Web Services Region of the instance.

    - **Sku** *(string) --*

      The SKU of the product.

    - **Memory** *(string) --*

      Memory capacity of Amazon Web Services instance.

    - **NetworkPerformance** *(string) --*

      Network performance capacity of the Amazon Web Services instance.

    - **Storage** *(string) --*

      The disk storage of the Amazon Web Services instance (Not EBS storage).

    - **Vcpu** *(string) --*

      Number of VCPU cores in the Amazon Web Services instance type.
    """


_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesResourceDetailsTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesResourceDetailsTypeDef",
    {
        "EC2ResourceDetails": ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesResourceDetailsEC2ResourceDetailsTypeDef
    },
    total=False,
)


class ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesResourceDetailsTypeDef(
    _ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesResourceDetailsTypeDef
):
    """
    Type definition for `ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstances` `ResourceDetails`

    Details on the target instance type.

    - **EC2ResourceDetails** *(dict) --*

      Details on the Amazon EC2 resource.

      - **HourlyOnDemandRate** *(string) --*

        Hourly public On Demand rate for the instance type.

      - **InstanceType** *(string) --*

        The type of Amazon Web Services instance.

      - **Platform** *(string) --*

        The platform of the Amazon Web Services instance. The platform is the specific
        combination of operating system, license model, and software on an instance.

      - **Region** *(string) --*

        The Amazon Web Services Region of the instance.

      - **Sku** *(string) --*

        The SKU of the product.

      - **Memory** *(string) --*

        Memory capacity of Amazon Web Services instance.

      - **NetworkPerformance** *(string) --*

        Network performance capacity of the Amazon Web Services instance.

      - **Storage** *(string) --*

        The disk storage of the Amazon Web Services instance (Not EBS storage).

      - **Vcpu** *(string) --*

        Number of VCPU cores in the Amazon Web Services instance type.
    """


_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesTypeDef",
    {
        "EstimatedMonthlyCost": str,
        "EstimatedMonthlySavings": str,
        "CurrencyCode": str,
        "DefaultTargetInstance": bool,
        "ResourceDetails": ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesResourceDetailsTypeDef,
        "ExpectedResourceUtilization": ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesExpectedResourceUtilizationTypeDef,
    },
    total=False,
)


class ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesTypeDef(
    _ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesTypeDef
):
    """
    Type definition for `ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetail` `TargetInstances`

    Details on recommended instance.

    - **EstimatedMonthlyCost** *(string) --*

      Expected cost to operate this instance type on a monthly basis.

    - **EstimatedMonthlySavings** *(string) --*

      Estimated savings resulting from modification, on a monthly basis.

    - **CurrencyCode** *(string) --*

      The currency code that Amazon Web Services used to calculate the costs for this
      instance.

    - **DefaultTargetInstance** *(boolean) --*

      Indicates whether or not this recommendation is the defaulted Amazon Web Services
      recommendation.

    - **ResourceDetails** *(dict) --*

      Details on the target instance type.

      - **EC2ResourceDetails** *(dict) --*

        Details on the Amazon EC2 resource.

        - **HourlyOnDemandRate** *(string) --*

          Hourly public On Demand rate for the instance type.

        - **InstanceType** *(string) --*

          The type of Amazon Web Services instance.

        - **Platform** *(string) --*

          The platform of the Amazon Web Services instance. The platform is the specific
          combination of operating system, license model, and software on an instance.

        - **Region** *(string) --*

          The Amazon Web Services Region of the instance.

        - **Sku** *(string) --*

          The SKU of the product.

        - **Memory** *(string) --*

          Memory capacity of Amazon Web Services instance.

        - **NetworkPerformance** *(string) --*

          Network performance capacity of the Amazon Web Services instance.

        - **Storage** *(string) --*

          The disk storage of the Amazon Web Services instance (Not EBS storage).

        - **Vcpu** *(string) --*

          Number of VCPU cores in the Amazon Web Services instance type.

    - **ExpectedResourceUtilization** *(dict) --*

      Expected utilization metrics for target instance type.

      - **EC2ResourceUtilization** *(dict) --*

        Utilization of current Amazon EC2 Instance

        - **MaxCpuUtilizationPercentage** *(string) --*

          Maximum observed or expected CPU utilization of the instance.

        - **MaxMemoryUtilizationPercentage** *(string) --*

          Maximum observed or expected memory utilization of the instance.

        - **MaxStorageUtilizationPercentage** *(string) --*

          Maximum observed or expected storage utilization of the instance (does not
          measure EBS storage).
    """


_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTypeDef",
    {
        "TargetInstances": List[
            ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesTypeDef
        ]
    },
    total=False,
)


class ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTypeDef(
    _ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTypeDef
):
    """
    Type definition for `ClientGetRightsizingRecommendationResponseRightsizingRecommendations` `ModifyRecommendationDetail`

    Details for modification recommendations.

    - **TargetInstances** *(list) --*

      Identifies whether this instance type is the Amazon Web Services default recommendation.

      - *(dict) --*

        Details on recommended instance.

        - **EstimatedMonthlyCost** *(string) --*

          Expected cost to operate this instance type on a monthly basis.

        - **EstimatedMonthlySavings** *(string) --*

          Estimated savings resulting from modification, on a monthly basis.

        - **CurrencyCode** *(string) --*

          The currency code that Amazon Web Services used to calculate the costs for this
          instance.

        - **DefaultTargetInstance** *(boolean) --*

          Indicates whether or not this recommendation is the defaulted Amazon Web Services
          recommendation.

        - **ResourceDetails** *(dict) --*

          Details on the target instance type.

          - **EC2ResourceDetails** *(dict) --*

            Details on the Amazon EC2 resource.

            - **HourlyOnDemandRate** *(string) --*

              Hourly public On Demand rate for the instance type.

            - **InstanceType** *(string) --*

              The type of Amazon Web Services instance.

            - **Platform** *(string) --*

              The platform of the Amazon Web Services instance. The platform is the specific
              combination of operating system, license model, and software on an instance.

            - **Region** *(string) --*

              The Amazon Web Services Region of the instance.

            - **Sku** *(string) --*

              The SKU of the product.

            - **Memory** *(string) --*

              Memory capacity of Amazon Web Services instance.

            - **NetworkPerformance** *(string) --*

              Network performance capacity of the Amazon Web Services instance.

            - **Storage** *(string) --*

              The disk storage of the Amazon Web Services instance (Not EBS storage).

            - **Vcpu** *(string) --*

              Number of VCPU cores in the Amazon Web Services instance type.

        - **ExpectedResourceUtilization** *(dict) --*

          Expected utilization metrics for target instance type.

          - **EC2ResourceUtilization** *(dict) --*

            Utilization of current Amazon EC2 Instance

            - **MaxCpuUtilizationPercentage** *(string) --*

              Maximum observed or expected CPU utilization of the instance.

            - **MaxMemoryUtilizationPercentage** *(string) --*

              Maximum observed or expected memory utilization of the instance.

            - **MaxStorageUtilizationPercentage** *(string) --*

              Maximum observed or expected storage utilization of the instance (does not
              measure EBS storage).
    """


_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsTerminateRecommendationDetailTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsTerminateRecommendationDetailTypeDef",
    {"EstimatedMonthlySavings": str, "CurrencyCode": str},
    total=False,
)


class ClientGetRightsizingRecommendationResponseRightsizingRecommendationsTerminateRecommendationDetailTypeDef(
    _ClientGetRightsizingRecommendationResponseRightsizingRecommendationsTerminateRecommendationDetailTypeDef
):
    """
    Type definition for `ClientGetRightsizingRecommendationResponseRightsizingRecommendations` `TerminateRecommendationDetail`

    Details for termination recommendations.

    - **EstimatedMonthlySavings** *(string) --*

      Estimated savings resulting from modification, on a monthly basis.

    - **CurrencyCode** *(string) --*

      The currency code that Amazon Web Services used to calculate the costs for this
      instance.
    """


_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsTypeDef",
    {
        "AccountId": str,
        "CurrentInstance": ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceTypeDef,
        "RightsizingType": str,
        "ModifyRecommendationDetail": ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTypeDef,
        "TerminateRecommendationDetail": ClientGetRightsizingRecommendationResponseRightsizingRecommendationsTerminateRecommendationDetailTypeDef,
    },
    total=False,
)


class ClientGetRightsizingRecommendationResponseRightsizingRecommendationsTypeDef(
    _ClientGetRightsizingRecommendationResponseRightsizingRecommendationsTypeDef
):
    """
    Type definition for `ClientGetRightsizingRecommendationResponse` `RightsizingRecommendations`

    Recommendations to rightsize resources.

    - **AccountId** *(string) --*

      The account that this recommendation is for.

    - **CurrentInstance** *(dict) --*

      Context regarding the current instance.

      - **ResourceId** *(string) --*

        Resource ID of the current instance.

      - **Tags** *(list) --*

        Cost allocation resource tags applied to the instance.

        - *(dict) --*

          The values that are available for a tag.

          - **Key** *(string) --*

            The key for the tag.

          - **Values** *(list) --*

            The specific value of the tag.

            - *(string) --*

      - **ResourceDetails** *(dict) --*

        Details about the resource and utilization.

        - **EC2ResourceDetails** *(dict) --*

          Details on the Amazon EC2 resource.

          - **HourlyOnDemandRate** *(string) --*

            Hourly public On Demand rate for the instance type.

          - **InstanceType** *(string) --*

            The type of Amazon Web Services instance.

          - **Platform** *(string) --*

            The platform of the Amazon Web Services instance. The platform is the specific
            combination of operating system, license model, and software on an instance.

          - **Region** *(string) --*

            The Amazon Web Services Region of the instance.

          - **Sku** *(string) --*

            The SKU of the product.

          - **Memory** *(string) --*

            Memory capacity of Amazon Web Services instance.

          - **NetworkPerformance** *(string) --*

            Network performance capacity of the Amazon Web Services instance.

          - **Storage** *(string) --*

            The disk storage of the Amazon Web Services instance (Not EBS storage).

          - **Vcpu** *(string) --*

            Number of VCPU cores in the Amazon Web Services instance type.

      - **ResourceUtilization** *(dict) --*

        Utilization information of the current instance during the lookback period.

        - **EC2ResourceUtilization** *(dict) --*

          Utilization of current Amazon EC2 Instance

          - **MaxCpuUtilizationPercentage** *(string) --*

            Maximum observed or expected CPU utilization of the instance.

          - **MaxMemoryUtilizationPercentage** *(string) --*

            Maximum observed or expected memory utilization of the instance.

          - **MaxStorageUtilizationPercentage** *(string) --*

            Maximum observed or expected storage utilization of the instance (does not measure
            EBS storage).

      - **ReservationCoveredHoursInLookbackPeriod** *(string) --*

        Number of hours during the lookback period covered by reservations.

      - **SavingsPlansCoveredHoursInLookbackPeriod** *(string) --*

        Number of hours during the lookback period covered by Savings Plans.

      - **OnDemandHoursInLookbackPeriod** *(string) --*

        Number of hours during the lookback period billed at On Demand rates.

      - **TotalRunningHoursInLookbackPeriod** *(string) --*

        The total number of hours the instance ran during the lookback period.

      - **MonthlyCost** *(string) --*

        Current On Demand cost of operating this instance on a monthly basis.

      - **CurrencyCode** *(string) --*

        The currency code that Amazon Web Services used to calculate the costs for this
        instance.

    - **RightsizingType** *(string) --*

      Recommendation to either terminate or modify the resource.

    - **ModifyRecommendationDetail** *(dict) --*

      Details for modification recommendations.

      - **TargetInstances** *(list) --*

        Identifies whether this instance type is the Amazon Web Services default recommendation.

        - *(dict) --*

          Details on recommended instance.

          - **EstimatedMonthlyCost** *(string) --*

            Expected cost to operate this instance type on a monthly basis.

          - **EstimatedMonthlySavings** *(string) --*

            Estimated savings resulting from modification, on a monthly basis.

          - **CurrencyCode** *(string) --*

            The currency code that Amazon Web Services used to calculate the costs for this
            instance.

          - **DefaultTargetInstance** *(boolean) --*

            Indicates whether or not this recommendation is the defaulted Amazon Web Services
            recommendation.

          - **ResourceDetails** *(dict) --*

            Details on the target instance type.

            - **EC2ResourceDetails** *(dict) --*

              Details on the Amazon EC2 resource.

              - **HourlyOnDemandRate** *(string) --*

                Hourly public On Demand rate for the instance type.

              - **InstanceType** *(string) --*

                The type of Amazon Web Services instance.

              - **Platform** *(string) --*

                The platform of the Amazon Web Services instance. The platform is the specific
                combination of operating system, license model, and software on an instance.

              - **Region** *(string) --*

                The Amazon Web Services Region of the instance.

              - **Sku** *(string) --*

                The SKU of the product.

              - **Memory** *(string) --*

                Memory capacity of Amazon Web Services instance.

              - **NetworkPerformance** *(string) --*

                Network performance capacity of the Amazon Web Services instance.

              - **Storage** *(string) --*

                The disk storage of the Amazon Web Services instance (Not EBS storage).

              - **Vcpu** *(string) --*

                Number of VCPU cores in the Amazon Web Services instance type.

          - **ExpectedResourceUtilization** *(dict) --*

            Expected utilization metrics for target instance type.

            - **EC2ResourceUtilization** *(dict) --*

              Utilization of current Amazon EC2 Instance

              - **MaxCpuUtilizationPercentage** *(string) --*

                Maximum observed or expected CPU utilization of the instance.

              - **MaxMemoryUtilizationPercentage** *(string) --*

                Maximum observed or expected memory utilization of the instance.

              - **MaxStorageUtilizationPercentage** *(string) --*

                Maximum observed or expected storage utilization of the instance (does not
                measure EBS storage).

    - **TerminateRecommendationDetail** *(dict) --*

      Details for termination recommendations.

      - **EstimatedMonthlySavings** *(string) --*

        Estimated savings resulting from modification, on a monthly basis.

      - **CurrencyCode** *(string) --*

        The currency code that Amazon Web Services used to calculate the costs for this
        instance.
    """


_ClientGetRightsizingRecommendationResponseSummaryTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseSummaryTypeDef",
    {
        "TotalRecommendationCount": str,
        "EstimatedTotalMonthlySavingsAmount": str,
        "SavingsCurrencyCode": str,
        "SavingsPercentage": str,
    },
    total=False,
)


class ClientGetRightsizingRecommendationResponseSummaryTypeDef(
    _ClientGetRightsizingRecommendationResponseSummaryTypeDef
):
    """
    Type definition for `ClientGetRightsizingRecommendationResponse` `Summary`

    Summary of this recommendation set.

    - **TotalRecommendationCount** *(string) --*

      Total number of instance recommendations.

    - **EstimatedTotalMonthlySavingsAmount** *(string) --*

      Estimated total savings resulting from modifications, on a monthly basis.

    - **SavingsCurrencyCode** *(string) --*

      The currency code that Amazon Web Services used to calculate the savings.

    - **SavingsPercentage** *(string) --*

      Savings percentage based on the recommended modifications, relative to the total On Demand
      costs associated with these instances.
    """


_ClientGetRightsizingRecommendationResponseTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseTypeDef",
    {
        "Metadata": ClientGetRightsizingRecommendationResponseMetadataTypeDef,
        "Summary": ClientGetRightsizingRecommendationResponseSummaryTypeDef,
        "RightsizingRecommendations": List[
            ClientGetRightsizingRecommendationResponseRightsizingRecommendationsTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)


class ClientGetRightsizingRecommendationResponseTypeDef(
    _ClientGetRightsizingRecommendationResponseTypeDef
):
    """
    Type definition for `ClientGetRightsizingRecommendation` `Response`

    - **Metadata** *(dict) --*

      Information regarding this specific recommendation set.

      - **RecommendationId** *(string) --*

        The ID for this specific recommendation.

      - **GenerationTimestamp** *(string) --*

        The time stamp for when Amazon Web Services made this recommendation.

      - **LookbackPeriodInDays** *(string) --*

        How many days of previous usage that Amazon Web Services considers when making this
        recommendation.

    - **Summary** *(dict) --*

      Summary of this recommendation set.

      - **TotalRecommendationCount** *(string) --*

        Total number of instance recommendations.

      - **EstimatedTotalMonthlySavingsAmount** *(string) --*

        Estimated total savings resulting from modifications, on a monthly basis.

      - **SavingsCurrencyCode** *(string) --*

        The currency code that Amazon Web Services used to calculate the savings.

      - **SavingsPercentage** *(string) --*

        Savings percentage based on the recommended modifications, relative to the total On Demand
        costs associated with these instances.

    - **RightsizingRecommendations** *(list) --*

      Recommendations to rightsize resources.

      - *(dict) --*

        Recommendations to rightsize resources.

        - **AccountId** *(string) --*

          The account that this recommendation is for.

        - **CurrentInstance** *(dict) --*

          Context regarding the current instance.

          - **ResourceId** *(string) --*

            Resource ID of the current instance.

          - **Tags** *(list) --*

            Cost allocation resource tags applied to the instance.

            - *(dict) --*

              The values that are available for a tag.

              - **Key** *(string) --*

                The key for the tag.

              - **Values** *(list) --*

                The specific value of the tag.

                - *(string) --*

          - **ResourceDetails** *(dict) --*

            Details about the resource and utilization.

            - **EC2ResourceDetails** *(dict) --*

              Details on the Amazon EC2 resource.

              - **HourlyOnDemandRate** *(string) --*

                Hourly public On Demand rate for the instance type.

              - **InstanceType** *(string) --*

                The type of Amazon Web Services instance.

              - **Platform** *(string) --*

                The platform of the Amazon Web Services instance. The platform is the specific
                combination of operating system, license model, and software on an instance.

              - **Region** *(string) --*

                The Amazon Web Services Region of the instance.

              - **Sku** *(string) --*

                The SKU of the product.

              - **Memory** *(string) --*

                Memory capacity of Amazon Web Services instance.

              - **NetworkPerformance** *(string) --*

                Network performance capacity of the Amazon Web Services instance.

              - **Storage** *(string) --*

                The disk storage of the Amazon Web Services instance (Not EBS storage).

              - **Vcpu** *(string) --*

                Number of VCPU cores in the Amazon Web Services instance type.

          - **ResourceUtilization** *(dict) --*

            Utilization information of the current instance during the lookback period.

            - **EC2ResourceUtilization** *(dict) --*

              Utilization of current Amazon EC2 Instance

              - **MaxCpuUtilizationPercentage** *(string) --*

                Maximum observed or expected CPU utilization of the instance.

              - **MaxMemoryUtilizationPercentage** *(string) --*

                Maximum observed or expected memory utilization of the instance.

              - **MaxStorageUtilizationPercentage** *(string) --*

                Maximum observed or expected storage utilization of the instance (does not measure
                EBS storage).

          - **ReservationCoveredHoursInLookbackPeriod** *(string) --*

            Number of hours during the lookback period covered by reservations.

          - **SavingsPlansCoveredHoursInLookbackPeriod** *(string) --*

            Number of hours during the lookback period covered by Savings Plans.

          - **OnDemandHoursInLookbackPeriod** *(string) --*

            Number of hours during the lookback period billed at On Demand rates.

          - **TotalRunningHoursInLookbackPeriod** *(string) --*

            The total number of hours the instance ran during the lookback period.

          - **MonthlyCost** *(string) --*

            Current On Demand cost of operating this instance on a monthly basis.

          - **CurrencyCode** *(string) --*

            The currency code that Amazon Web Services used to calculate the costs for this
            instance.

        - **RightsizingType** *(string) --*

          Recommendation to either terminate or modify the resource.

        - **ModifyRecommendationDetail** *(dict) --*

          Details for modification recommendations.

          - **TargetInstances** *(list) --*

            Identifies whether this instance type is the Amazon Web Services default recommendation.

            - *(dict) --*

              Details on recommended instance.

              - **EstimatedMonthlyCost** *(string) --*

                Expected cost to operate this instance type on a monthly basis.

              - **EstimatedMonthlySavings** *(string) --*

                Estimated savings resulting from modification, on a monthly basis.

              - **CurrencyCode** *(string) --*

                The currency code that Amazon Web Services used to calculate the costs for this
                instance.

              - **DefaultTargetInstance** *(boolean) --*

                Indicates whether or not this recommendation is the defaulted Amazon Web Services
                recommendation.

              - **ResourceDetails** *(dict) --*

                Details on the target instance type.

                - **EC2ResourceDetails** *(dict) --*

                  Details on the Amazon EC2 resource.

                  - **HourlyOnDemandRate** *(string) --*

                    Hourly public On Demand rate for the instance type.

                  - **InstanceType** *(string) --*

                    The type of Amazon Web Services instance.

                  - **Platform** *(string) --*

                    The platform of the Amazon Web Services instance. The platform is the specific
                    combination of operating system, license model, and software on an instance.

                  - **Region** *(string) --*

                    The Amazon Web Services Region of the instance.

                  - **Sku** *(string) --*

                    The SKU of the product.

                  - **Memory** *(string) --*

                    Memory capacity of Amazon Web Services instance.

                  - **NetworkPerformance** *(string) --*

                    Network performance capacity of the Amazon Web Services instance.

                  - **Storage** *(string) --*

                    The disk storage of the Amazon Web Services instance (Not EBS storage).

                  - **Vcpu** *(string) --*

                    Number of VCPU cores in the Amazon Web Services instance type.

              - **ExpectedResourceUtilization** *(dict) --*

                Expected utilization metrics for target instance type.

                - **EC2ResourceUtilization** *(dict) --*

                  Utilization of current Amazon EC2 Instance

                  - **MaxCpuUtilizationPercentage** *(string) --*

                    Maximum observed or expected CPU utilization of the instance.

                  - **MaxMemoryUtilizationPercentage** *(string) --*

                    Maximum observed or expected memory utilization of the instance.

                  - **MaxStorageUtilizationPercentage** *(string) --*

                    Maximum observed or expected storage utilization of the instance (does not
                    measure EBS storage).

        - **TerminateRecommendationDetail** *(dict) --*

          Details for termination recommendations.

          - **EstimatedMonthlySavings** *(string) --*

            Estimated savings resulting from modification, on a monthly basis.

          - **CurrencyCode** *(string) --*

            The currency code that Amazon Web Services used to calculate the costs for this
            instance.

    - **NextPageToken** *(string) --*

      The token to retrieve the next set of results.
    """


_ClientGetSavingsPlansCoverageFilterDimensionsTypeDef = TypedDict(
    "_ClientGetSavingsPlansCoverageFilterDimensionsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetSavingsPlansCoverageFilterDimensionsTypeDef(
    _ClientGetSavingsPlansCoverageFilterDimensionsTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansCoverageFilter` `Dimensions`

    The specific ``Dimension`` to use for ``Expression`` .

    - **Key** *(string) --*

      The names of the metadata types that you can use to filter and group your results. For
      example, ``AZ`` returns a list of Availability Zones.

    - **Values** *(list) --*

      The metadata values that you can use to filter and group your results. You can use
      ``GetDimensionValues`` to find specific values.

      Valid values for the ``SERVICE`` dimension are ``Amazon Elastic Compute Cloud - Compute`` ,
      ``Amazon Elasticsearch Service`` , ``Amazon ElastiCache`` , ``Amazon Redshift`` , and
      ``Amazon Relational Database Service`` .

      - *(string) --*
    """


_ClientGetSavingsPlansCoverageFilterTagsTypeDef = TypedDict(
    "_ClientGetSavingsPlansCoverageFilterTagsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetSavingsPlansCoverageFilterTagsTypeDef(
    _ClientGetSavingsPlansCoverageFilterTagsTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansCoverageFilter` `Tags`

    The specific ``Tag`` to use for ``Expression`` .

    - **Key** *(string) --*

      The key for the tag.

    - **Values** *(list) --*

      The specific value of the tag.

      - *(string) --*
    """


_ClientGetSavingsPlansCoverageFilterTypeDef = TypedDict(
    "_ClientGetSavingsPlansCoverageFilterTypeDef",
    {
        "Or": List[Dict],
        "And": List[Dict],
        "Not": Dict,
        "Dimensions": ClientGetSavingsPlansCoverageFilterDimensionsTypeDef,
        "Tags": ClientGetSavingsPlansCoverageFilterTagsTypeDef,
    },
    total=False,
)


class ClientGetSavingsPlansCoverageFilterTypeDef(
    _ClientGetSavingsPlansCoverageFilterTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansCoverage` `Filter`

    Filters Savings Plans coverage data by dimensions. You can filter data for Savings Plans usage
    with the following dimensions:

    * ``LINKED_ACCOUNT``

    * ``REGION``

    * ``SERVICE``

    * ``INSTANCE_FAMILY``

     ``GetSavingsPlansCoverage`` uses the same `Expression
     <http://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html>`__
     object as the other operations, but only ``AND`` is supported among each dimension. If there are
     multiple values for a dimension, they are OR'd together.

    - **Or** *(list) --*

      Return results that match either ``Dimension`` object.

      - *(dict) --*

        Use ``Expression`` to filter by cost or by usage. There are two patterns:

        * Simple dimension values - You can set the dimension name and values for the filters that
        you plan to use. For example, you can filter for ``REGION==us-east-1 OR REGION==us-west-1`` .
        The ``Expression`` for that looks like this:  ``{ "Dimensions": { "Key": "REGION", "Values":
        [ "us-east-1", “us-west-1” ] } }``   The list of dimension values are OR'd together to
        retrieve cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects
        using either ``with*`` methods or ``set*`` methods in multiple lines.

        * Compound dimension values with logical operations - You can use multiple ``Expression``
        types and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression``
        objects. This allows you to filter on more advanced options. For example, you can filter on
        ``((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE !=
        DataTransfer)`` . The ``Expression`` for that looks like this:  ``{ "And": [ {"Or": [
        {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": {
        "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE",
        "Values": ["DataTransfer"] }}} ] }``

        .. note::

           Because each ``Expression`` can have only one operator, the service returns an error if
           more than one is specified. The following example shows an ``Expression`` object that
           creates an error.

          ``{ "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [
          "DataTransfer" ] } }``

        .. note::

          For ``GetRightsizingRecommendation`` action, a combination of OR and NOT is not supported.
          OR is not supported between different dimensions, or dimensions and tags. NOT operators
          aren't supported. Dimensions are also limited to ``LINKED_ACCOUNT`` , ``REGION`` , or
          ``RIGHTSIZING_TYPE`` .

    - **And** *(list) --*

      Return results that match both ``Dimension`` objects.

      - *(dict) --*

        Use ``Expression`` to filter by cost or by usage. There are two patterns:

        * Simple dimension values - You can set the dimension name and values for the filters that
        you plan to use. For example, you can filter for ``REGION==us-east-1 OR REGION==us-west-1`` .
        The ``Expression`` for that looks like this:  ``{ "Dimensions": { "Key": "REGION", "Values":
        [ "us-east-1", “us-west-1” ] } }``   The list of dimension values are OR'd together to
        retrieve cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects
        using either ``with*`` methods or ``set*`` methods in multiple lines.

        * Compound dimension values with logical operations - You can use multiple ``Expression``
        types and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression``
        objects. This allows you to filter on more advanced options. For example, you can filter on
        ``((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE !=
        DataTransfer)`` . The ``Expression`` for that looks like this:  ``{ "And": [ {"Or": [
        {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": {
        "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE",
        "Values": ["DataTransfer"] }}} ] }``

        .. note::

           Because each ``Expression`` can have only one operator, the service returns an error if
           more than one is specified. The following example shows an ``Expression`` object that
           creates an error.

          ``{ "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [
          "DataTransfer" ] } }``

        .. note::

          For ``GetRightsizingRecommendation`` action, a combination of OR and NOT is not supported.
          OR is not supported between different dimensions, or dimensions and tags. NOT operators
          aren't supported. Dimensions are also limited to ``LINKED_ACCOUNT`` , ``REGION`` , or
          ``RIGHTSIZING_TYPE`` .

    - **Not** *(dict) --*

      Return results that don't match a ``Dimension`` object.

    - **Dimensions** *(dict) --*

      The specific ``Dimension`` to use for ``Expression`` .

      - **Key** *(string) --*

        The names of the metadata types that you can use to filter and group your results. For
        example, ``AZ`` returns a list of Availability Zones.

      - **Values** *(list) --*

        The metadata values that you can use to filter and group your results. You can use
        ``GetDimensionValues`` to find specific values.

        Valid values for the ``SERVICE`` dimension are ``Amazon Elastic Compute Cloud - Compute`` ,
        ``Amazon Elasticsearch Service`` , ``Amazon ElastiCache`` , ``Amazon Redshift`` , and
        ``Amazon Relational Database Service`` .

        - *(string) --*

    - **Tags** *(dict) --*

      The specific ``Tag`` to use for ``Expression`` .

      - **Key** *(string) --*

        The key for the tag.

      - **Values** *(list) --*

        The specific value of the tag.

        - *(string) --*
    """


_ClientGetSavingsPlansCoverageGroupByTypeDef = TypedDict(
    "_ClientGetSavingsPlansCoverageGroupByTypeDef",
    {"Type": str, "Key": str},
    total=False,
)


class ClientGetSavingsPlansCoverageGroupByTypeDef(
    _ClientGetSavingsPlansCoverageGroupByTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansCoverage` `GroupBy`

    Represents a group when you specify a group by criteria or in the response to a query with a
    specific grouping.

    - **Type** *(string) --*

      The string that represents the type of group.

    - **Key** *(string) --*

      The string that represents a key for a specified group.
    """


_ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesCoverageTypeDef = TypedDict(
    "_ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesCoverageTypeDef",
    {
        "SpendCoveredBySavingsPlans": str,
        "OnDemandCost": str,
        "TotalCost": str,
        "CoveragePercentage": str,
    },
    total=False,
)


class ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesCoverageTypeDef(
    _ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesCoverageTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansCoverageResponseSavingsPlansCoverages` `Coverage`

    The amount of Savings Plans eligible usage that the Savings Plans covered.

    - **SpendCoveredBySavingsPlans** *(string) --*

      The amount of your Amazon Web Services usage that is covered by a Savings Plans.

    - **OnDemandCost** *(string) --*

      The cost of your Amazon Web Services usage at the public On-Demand rate.

    - **TotalCost** *(string) --*

      The total cost of your Amazon Web Services usage, regardless of your purchase option.

    - **CoveragePercentage** *(string) --*

      The percentage of your existing Savings Planscovered usage, divided by all of your
      eligible Savings Plans usage in an account(or set of accounts).
    """


_ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesTimePeriodTypeDef = TypedDict(
    "_ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesTimePeriodTypeDef",
    {"Start": str, "End": str},
    total=False,
)


class ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesTimePeriodTypeDef(
    _ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesTimePeriodTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansCoverageResponseSavingsPlansCoverages` `TimePeriod`

    The time period that you want the usage and costs for.

    - **Start** *(string) --*

      The beginning of the time period that you want the usage and costs for. The start date
      is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and
      usage data starting at ``2017-01-01`` up to the end date.

    - **End** *(string) --*

      The end of the time period that you want the usage and costs for. The end date is
      exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage
      data from the start date up to, but not including, ``2017-05-01`` .
    """


_ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesTypeDef = TypedDict(
    "_ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesTypeDef",
    {
        "Attributes": Dict[str, str],
        "Coverage": ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesCoverageTypeDef,
        "TimePeriod": ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesTimePeriodTypeDef,
    },
    total=False,
)


class ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesTypeDef(
    _ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansCoverageResponse` `SavingsPlansCoverages`

    The amount of Savings Plans eligible usage that is covered by Savings Plans. All
    calculations consider the On-Demand equivalent of your Savings Plans usage.

    - **Attributes** *(dict) --*

      The attribute that applies to a specific ``Dimension`` .

      - *(string) --*

        - *(string) --*

    - **Coverage** *(dict) --*

      The amount of Savings Plans eligible usage that the Savings Plans covered.

      - **SpendCoveredBySavingsPlans** *(string) --*

        The amount of your Amazon Web Services usage that is covered by a Savings Plans.

      - **OnDemandCost** *(string) --*

        The cost of your Amazon Web Services usage at the public On-Demand rate.

      - **TotalCost** *(string) --*

        The total cost of your Amazon Web Services usage, regardless of your purchase option.

      - **CoveragePercentage** *(string) --*

        The percentage of your existing Savings Planscovered usage, divided by all of your
        eligible Savings Plans usage in an account(or set of accounts).

    - **TimePeriod** *(dict) --*

      The time period that you want the usage and costs for.

      - **Start** *(string) --*

        The beginning of the time period that you want the usage and costs for. The start date
        is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and
        usage data starting at ``2017-01-01`` up to the end date.

      - **End** *(string) --*

        The end of the time period that you want the usage and costs for. The end date is
        exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage
        data from the start date up to, but not including, ``2017-05-01`` .
    """


_ClientGetSavingsPlansCoverageResponseTypeDef = TypedDict(
    "_ClientGetSavingsPlansCoverageResponseTypeDef",
    {
        "SavingsPlansCoverages": List[
            ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientGetSavingsPlansCoverageResponseTypeDef(
    _ClientGetSavingsPlansCoverageResponseTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansCoverage` `Response`

    - **SavingsPlansCoverages** *(list) --*

      The amount of spend that your Savings Plans covered.

      - *(dict) --*

        The amount of Savings Plans eligible usage that is covered by Savings Plans. All
        calculations consider the On-Demand equivalent of your Savings Plans usage.

        - **Attributes** *(dict) --*

          The attribute that applies to a specific ``Dimension`` .

          - *(string) --*

            - *(string) --*

        - **Coverage** *(dict) --*

          The amount of Savings Plans eligible usage that the Savings Plans covered.

          - **SpendCoveredBySavingsPlans** *(string) --*

            The amount of your Amazon Web Services usage that is covered by a Savings Plans.

          - **OnDemandCost** *(string) --*

            The cost of your Amazon Web Services usage at the public On-Demand rate.

          - **TotalCost** *(string) --*

            The total cost of your Amazon Web Services usage, regardless of your purchase option.

          - **CoveragePercentage** *(string) --*

            The percentage of your existing Savings Planscovered usage, divided by all of your
            eligible Savings Plans usage in an account(or set of accounts).

        - **TimePeriod** *(dict) --*

          The time period that you want the usage and costs for.

          - **Start** *(string) --*

            The beginning of the time period that you want the usage and costs for. The start date
            is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and
            usage data starting at ``2017-01-01`` up to the end date.

          - **End** *(string) --*

            The end of the time period that you want the usage and costs for. The end date is
            exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage
            data from the start date up to, but not including, ``2017-05-01`` .

    - **NextToken** *(string) --*

      The token to retrieve the next set of results. Amazon Web Services provides the token when
      the response from a previous call has more results than the maximum page size.
    """


_ClientGetSavingsPlansCoverageTimePeriodTypeDef = TypedDict(
    "_ClientGetSavingsPlansCoverageTimePeriodTypeDef", {"Start": str, "End": str}
)


class ClientGetSavingsPlansCoverageTimePeriodTypeDef(
    _ClientGetSavingsPlansCoverageTimePeriodTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansCoverage` `TimePeriod`

    The time period that you want the usage and costs for. The ``Start`` date must be within 13
    months. The ``End`` date must be after the ``Start`` date, and before the current date. Future
    dates can't be used as an ``End`` date.

    - **Start** *(string) --* **[REQUIRED]**

      The beginning of the time period that you want the usage and costs for. The start date is
      inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data
      starting at ``2017-01-01`` up to the end date.

    - **End** *(string) --* **[REQUIRED]**

      The end of the time period that you want the usage and costs for. The end date is exclusive.
      For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage data from the start
      date up to, but not including, ``2017-05-01`` .
    """


_ClientGetSavingsPlansPurchaseRecommendationResponseMetadataTypeDef = TypedDict(
    "_ClientGetSavingsPlansPurchaseRecommendationResponseMetadataTypeDef",
    {"RecommendationId": str, "GenerationTimestamp": str},
    total=False,
)


class ClientGetSavingsPlansPurchaseRecommendationResponseMetadataTypeDef(
    _ClientGetSavingsPlansPurchaseRecommendationResponseMetadataTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansPurchaseRecommendationResponse` `Metadata`

    Information regarding this specific recommendation set.

    - **RecommendationId** *(string) --*

      The unique identifier for the recommendation set.

    - **GenerationTimestamp** *(string) --*

      The timestamp showing when the recommendations were generated.
    """


_ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationDetailsSavingsPlansDetailsTypeDef = TypedDict(
    "_ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationDetailsSavingsPlansDetailsTypeDef",
    {"Region": str, "InstanceFamily": str, "OfferingId": str},
    total=False,
)


class ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationDetailsSavingsPlansDetailsTypeDef(
    _ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationDetailsSavingsPlansDetailsTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationDetails` `SavingsPlansDetails`

    Details for your recommended Savings Plans.

    - **Region** *(string) --*

      A collection of AWS resources in a geographic area. Each AWS Region is isolated and
      independent of the other Regions.

    - **InstanceFamily** *(string) --*

      A group of instance types that Savings Plans applies to.

    - **OfferingId** *(string) --*

      The unique ID used to distinguish Savings Plans from one another.
    """


_ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationDetailsTypeDef = TypedDict(
    "_ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationDetailsTypeDef",
    {
        "SavingsPlansDetails": ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationDetailsSavingsPlansDetailsTypeDef,
        "AccountId": str,
        "UpfrontCost": str,
        "EstimatedROI": str,
        "CurrencyCode": str,
        "EstimatedSPCost": str,
        "EstimatedOnDemandCost": str,
        "EstimatedOnDemandCostWithCurrentCommitment": str,
        "EstimatedSavingsAmount": str,
        "EstimatedSavingsPercentage": str,
        "HourlyCommitmentToPurchase": str,
        "EstimatedAverageUtilization": str,
        "EstimatedMonthlySavingsAmount": str,
        "CurrentMinimumHourlyOnDemandSpend": str,
        "CurrentMaximumHourlyOnDemandSpend": str,
        "CurrentAverageHourlyOnDemandSpend": str,
    },
    total=False,
)


class ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationDetailsTypeDef(
    _ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationDetailsTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendation` `SavingsPlansPurchaseRecommendationDetails`

    Details for your recommended Savings Plans.

    - **SavingsPlansDetails** *(dict) --*

      Details for your recommended Savings Plans.

      - **Region** *(string) --*

        A collection of AWS resources in a geographic area. Each AWS Region is isolated and
        independent of the other Regions.

      - **InstanceFamily** *(string) --*

        A group of instance types that Savings Plans applies to.

      - **OfferingId** *(string) --*

        The unique ID used to distinguish Savings Plans from one another.

    - **AccountId** *(string) --*

      The ``AccountID`` the recommendation is generated for.

    - **UpfrontCost** *(string) --*

      The upfront cost of the recommended Savings Plans, based on the selected payment option.

    - **EstimatedROI** *(string) --*

      The estimated return on investment based on the recommended Savings Plans purchased.
      This is calculated as ``estimatedSavingsAmount`` / ``estimatedSPCost`` *100.

    - **CurrencyCode** *(string) --*

      The currency code Amazon Web Services used to generate the recommendations and present
      potential savings.

    - **EstimatedSPCost** *(string) --*

      The cost of the recommended Savings Plans over the length of the lookback period.

    - **EstimatedOnDemandCost** *(string) --*

      The remaining On-Demand cost estimated to not be covered by the recommended Savings
      Plans, over the length of the lookback period.

    - **EstimatedOnDemandCostWithCurrentCommitment** *(string) --*

      The estimated On-Demand costs you would expect with no additional commitment, based on
      your usage of the selected time period and the Savings Plans you own.

    - **EstimatedSavingsAmount** *(string) --*

      The estimated savings amount based on the recommended Savings Plans over the length of
      the lookback period.

    - **EstimatedSavingsPercentage** *(string) --*

      The estimated savings percentage relative to the total cost of applicable On-Demand
      usage over the lookback period.

    - **HourlyCommitmentToPurchase** *(string) --*

      The recommended hourly commitment level for the Savings Plans type, and configuration
      based on the usage during the lookback period.

    - **EstimatedAverageUtilization** *(string) --*

      The estimated utilization of the recommended Savings Plans.

    - **EstimatedMonthlySavingsAmount** *(string) --*

      The estimated monthly savings amount, based on the recommended Savings Plans.

    - **CurrentMinimumHourlyOnDemandSpend** *(string) --*

      The lowest value of hourly On-Demand spend over the lookback period of the applicable
      usage type.

    - **CurrentMaximumHourlyOnDemandSpend** *(string) --*

      The highest value of hourly On-Demand spend over the lookback period of the applicable
      usage type.

    - **CurrentAverageHourlyOnDemandSpend** *(string) --*

      The average value of hourly On-Demand spend over the lookback period of the applicable
      usage type.
    """


_ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationSummaryTypeDef = TypedDict(
    "_ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationSummaryTypeDef",
    {
        "EstimatedROI": str,
        "CurrencyCode": str,
        "EstimatedTotalCost": str,
        "CurrentOnDemandSpend": str,
        "EstimatedSavingsAmount": str,
        "TotalRecommendationCount": str,
        "DailyCommitmentToPurchase": str,
        "HourlyCommitmentToPurchase": str,
        "EstimatedSavingsPercentage": str,
        "EstimatedMonthlySavingsAmount": str,
        "EstimatedOnDemandCostWithCurrentCommitment": str,
    },
    total=False,
)


class ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationSummaryTypeDef(
    _ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationSummaryTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendation` `SavingsPlansPurchaseRecommendationSummary`

    Summary metrics for your Savings Plans Recommendations.

    - **EstimatedROI** *(string) --*

      The estimated return on investment based on the recommended Savings Plans and estimated
      savings.

    - **CurrencyCode** *(string) --*

      The currency code Amazon Web Services used to generate the recommendations and present
      potential savings.

    - **EstimatedTotalCost** *(string) --*

      The estimated total cost of the usage after purchasing the recommended Savings Plans.
      This is a sum of the cost of Savings Plans during this term, and the remaining On-Demand
      usage.

    - **CurrentOnDemandSpend** *(string) --*

      The current total on demand spend of the applicable usage types over the lookback period.

    - **EstimatedSavingsAmount** *(string) --*

      The estimated total savings over the lookback period, based on the purchase of the
      recommended Savings Plans.

    - **TotalRecommendationCount** *(string) --*

      The aggregate number of Savings Plans recommendations that exist for your account.

    - **DailyCommitmentToPurchase** *(string) --*

      The recommended Savings Plans cost on a daily (24 hourly) basis.

    - **HourlyCommitmentToPurchase** *(string) --*

      The recommended hourly commitment based on the recommendation parameters.

    - **EstimatedSavingsPercentage** *(string) --*

      The estimated savings relative to the total cost of On-Demand usage, over the lookback
      period. This is calculated as ``estimatedSavingsAmount`` / ``CurrentOnDemandSpend`` *100.

    - **EstimatedMonthlySavingsAmount** *(string) --*

      The estimated monthly savings amount, based on the recommended Savings Plans purchase.

    - **EstimatedOnDemandCostWithCurrentCommitment** *(string) --*

      The estimated On-Demand costs you would expect with no additional commitment, based on
      your usage of the selected time period and the Savings Plans you own.
    """


_ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationTypeDef = TypedDict(
    "_ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationTypeDef",
    {
        "SavingsPlansType": str,
        "TermInYears": str,
        "PaymentOption": str,
        "LookbackPeriodInDays": str,
        "SavingsPlansPurchaseRecommendationDetails": List[
            ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationDetailsTypeDef
        ],
        "SavingsPlansPurchaseRecommendationSummary": ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationSummaryTypeDef,
    },
    total=False,
)


class ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationTypeDef(
    _ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansPurchaseRecommendationResponse` `SavingsPlansPurchaseRecommendation`

    Contains your request parameters, Savings Plan Recommendations Summary, and Details.

    - **SavingsPlansType** *(string) --*

      The requested Savings Plans recommendation type.

    - **TermInYears** *(string) --*

      The Savings Plans recommendation term in years, used to generate the recommendation.

    - **PaymentOption** *(string) --*

      The payment option used to generate the recommendation.

    - **LookbackPeriodInDays** *(string) --*

      The lookback period in days, used to generate the recommendation.

    - **SavingsPlansPurchaseRecommendationDetails** *(list) --*

      Details for the Savings Plans we recommend you to purchase to cover existing, Savings Plans
      eligible workloads.

      - *(dict) --*

        Details for your recommended Savings Plans.

        - **SavingsPlansDetails** *(dict) --*

          Details for your recommended Savings Plans.

          - **Region** *(string) --*

            A collection of AWS resources in a geographic area. Each AWS Region is isolated and
            independent of the other Regions.

          - **InstanceFamily** *(string) --*

            A group of instance types that Savings Plans applies to.

          - **OfferingId** *(string) --*

            The unique ID used to distinguish Savings Plans from one another.

        - **AccountId** *(string) --*

          The ``AccountID`` the recommendation is generated for.

        - **UpfrontCost** *(string) --*

          The upfront cost of the recommended Savings Plans, based on the selected payment option.

        - **EstimatedROI** *(string) --*

          The estimated return on investment based on the recommended Savings Plans purchased.
          This is calculated as ``estimatedSavingsAmount`` / ``estimatedSPCost`` *100.

        - **CurrencyCode** *(string) --*

          The currency code Amazon Web Services used to generate the recommendations and present
          potential savings.

        - **EstimatedSPCost** *(string) --*

          The cost of the recommended Savings Plans over the length of the lookback period.

        - **EstimatedOnDemandCost** *(string) --*

          The remaining On-Demand cost estimated to not be covered by the recommended Savings
          Plans, over the length of the lookback period.

        - **EstimatedOnDemandCostWithCurrentCommitment** *(string) --*

          The estimated On-Demand costs you would expect with no additional commitment, based on
          your usage of the selected time period and the Savings Plans you own.

        - **EstimatedSavingsAmount** *(string) --*

          The estimated savings amount based on the recommended Savings Plans over the length of
          the lookback period.

        - **EstimatedSavingsPercentage** *(string) --*

          The estimated savings percentage relative to the total cost of applicable On-Demand
          usage over the lookback period.

        - **HourlyCommitmentToPurchase** *(string) --*

          The recommended hourly commitment level for the Savings Plans type, and configuration
          based on the usage during the lookback period.

        - **EstimatedAverageUtilization** *(string) --*

          The estimated utilization of the recommended Savings Plans.

        - **EstimatedMonthlySavingsAmount** *(string) --*

          The estimated monthly savings amount, based on the recommended Savings Plans.

        - **CurrentMinimumHourlyOnDemandSpend** *(string) --*

          The lowest value of hourly On-Demand spend over the lookback period of the applicable
          usage type.

        - **CurrentMaximumHourlyOnDemandSpend** *(string) --*

          The highest value of hourly On-Demand spend over the lookback period of the applicable
          usage type.

        - **CurrentAverageHourlyOnDemandSpend** *(string) --*

          The average value of hourly On-Demand spend over the lookback period of the applicable
          usage type.

    - **SavingsPlansPurchaseRecommendationSummary** *(dict) --*

      Summary metrics for your Savings Plans Recommendations.

      - **EstimatedROI** *(string) --*

        The estimated return on investment based on the recommended Savings Plans and estimated
        savings.

      - **CurrencyCode** *(string) --*

        The currency code Amazon Web Services used to generate the recommendations and present
        potential savings.

      - **EstimatedTotalCost** *(string) --*

        The estimated total cost of the usage after purchasing the recommended Savings Plans.
        This is a sum of the cost of Savings Plans during this term, and the remaining On-Demand
        usage.

      - **CurrentOnDemandSpend** *(string) --*

        The current total on demand spend of the applicable usage types over the lookback period.

      - **EstimatedSavingsAmount** *(string) --*

        The estimated total savings over the lookback period, based on the purchase of the
        recommended Savings Plans.

      - **TotalRecommendationCount** *(string) --*

        The aggregate number of Savings Plans recommendations that exist for your account.

      - **DailyCommitmentToPurchase** *(string) --*

        The recommended Savings Plans cost on a daily (24 hourly) basis.

      - **HourlyCommitmentToPurchase** *(string) --*

        The recommended hourly commitment based on the recommendation parameters.

      - **EstimatedSavingsPercentage** *(string) --*

        The estimated savings relative to the total cost of On-Demand usage, over the lookback
        period. This is calculated as ``estimatedSavingsAmount`` / ``CurrentOnDemandSpend`` *100.

      - **EstimatedMonthlySavingsAmount** *(string) --*

        The estimated monthly savings amount, based on the recommended Savings Plans purchase.

      - **EstimatedOnDemandCostWithCurrentCommitment** *(string) --*

        The estimated On-Demand costs you would expect with no additional commitment, based on
        your usage of the selected time period and the Savings Plans you own.
    """


_ClientGetSavingsPlansPurchaseRecommendationResponseTypeDef = TypedDict(
    "_ClientGetSavingsPlansPurchaseRecommendationResponseTypeDef",
    {
        "Metadata": ClientGetSavingsPlansPurchaseRecommendationResponseMetadataTypeDef,
        "SavingsPlansPurchaseRecommendation": ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationTypeDef,
        "NextPageToken": str,
    },
    total=False,
)


class ClientGetSavingsPlansPurchaseRecommendationResponseTypeDef(
    _ClientGetSavingsPlansPurchaseRecommendationResponseTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansPurchaseRecommendation` `Response`

    - **Metadata** *(dict) --*

      Information regarding this specific recommendation set.

      - **RecommendationId** *(string) --*

        The unique identifier for the recommendation set.

      - **GenerationTimestamp** *(string) --*

        The timestamp showing when the recommendations were generated.

    - **SavingsPlansPurchaseRecommendation** *(dict) --*

      Contains your request parameters, Savings Plan Recommendations Summary, and Details.

      - **SavingsPlansType** *(string) --*

        The requested Savings Plans recommendation type.

      - **TermInYears** *(string) --*

        The Savings Plans recommendation term in years, used to generate the recommendation.

      - **PaymentOption** *(string) --*

        The payment option used to generate the recommendation.

      - **LookbackPeriodInDays** *(string) --*

        The lookback period in days, used to generate the recommendation.

      - **SavingsPlansPurchaseRecommendationDetails** *(list) --*

        Details for the Savings Plans we recommend you to purchase to cover existing, Savings Plans
        eligible workloads.

        - *(dict) --*

          Details for your recommended Savings Plans.

          - **SavingsPlansDetails** *(dict) --*

            Details for your recommended Savings Plans.

            - **Region** *(string) --*

              A collection of AWS resources in a geographic area. Each AWS Region is isolated and
              independent of the other Regions.

            - **InstanceFamily** *(string) --*

              A group of instance types that Savings Plans applies to.

            - **OfferingId** *(string) --*

              The unique ID used to distinguish Savings Plans from one another.

          - **AccountId** *(string) --*

            The ``AccountID`` the recommendation is generated for.

          - **UpfrontCost** *(string) --*

            The upfront cost of the recommended Savings Plans, based on the selected payment option.

          - **EstimatedROI** *(string) --*

            The estimated return on investment based on the recommended Savings Plans purchased.
            This is calculated as ``estimatedSavingsAmount`` / ``estimatedSPCost`` *100.

          - **CurrencyCode** *(string) --*

            The currency code Amazon Web Services used to generate the recommendations and present
            potential savings.

          - **EstimatedSPCost** *(string) --*

            The cost of the recommended Savings Plans over the length of the lookback period.

          - **EstimatedOnDemandCost** *(string) --*

            The remaining On-Demand cost estimated to not be covered by the recommended Savings
            Plans, over the length of the lookback period.

          - **EstimatedOnDemandCostWithCurrentCommitment** *(string) --*

            The estimated On-Demand costs you would expect with no additional commitment, based on
            your usage of the selected time period and the Savings Plans you own.

          - **EstimatedSavingsAmount** *(string) --*

            The estimated savings amount based on the recommended Savings Plans over the length of
            the lookback period.

          - **EstimatedSavingsPercentage** *(string) --*

            The estimated savings percentage relative to the total cost of applicable On-Demand
            usage over the lookback period.

          - **HourlyCommitmentToPurchase** *(string) --*

            The recommended hourly commitment level for the Savings Plans type, and configuration
            based on the usage during the lookback period.

          - **EstimatedAverageUtilization** *(string) --*

            The estimated utilization of the recommended Savings Plans.

          - **EstimatedMonthlySavingsAmount** *(string) --*

            The estimated monthly savings amount, based on the recommended Savings Plans.

          - **CurrentMinimumHourlyOnDemandSpend** *(string) --*

            The lowest value of hourly On-Demand spend over the lookback period of the applicable
            usage type.

          - **CurrentMaximumHourlyOnDemandSpend** *(string) --*

            The highest value of hourly On-Demand spend over the lookback period of the applicable
            usage type.

          - **CurrentAverageHourlyOnDemandSpend** *(string) --*

            The average value of hourly On-Demand spend over the lookback period of the applicable
            usage type.

      - **SavingsPlansPurchaseRecommendationSummary** *(dict) --*

        Summary metrics for your Savings Plans Recommendations.

        - **EstimatedROI** *(string) --*

          The estimated return on investment based on the recommended Savings Plans and estimated
          savings.

        - **CurrencyCode** *(string) --*

          The currency code Amazon Web Services used to generate the recommendations and present
          potential savings.

        - **EstimatedTotalCost** *(string) --*

          The estimated total cost of the usage after purchasing the recommended Savings Plans.
          This is a sum of the cost of Savings Plans during this term, and the remaining On-Demand
          usage.

        - **CurrentOnDemandSpend** *(string) --*

          The current total on demand spend of the applicable usage types over the lookback period.

        - **EstimatedSavingsAmount** *(string) --*

          The estimated total savings over the lookback period, based on the purchase of the
          recommended Savings Plans.

        - **TotalRecommendationCount** *(string) --*

          The aggregate number of Savings Plans recommendations that exist for your account.

        - **DailyCommitmentToPurchase** *(string) --*

          The recommended Savings Plans cost on a daily (24 hourly) basis.

        - **HourlyCommitmentToPurchase** *(string) --*

          The recommended hourly commitment based on the recommendation parameters.

        - **EstimatedSavingsPercentage** *(string) --*

          The estimated savings relative to the total cost of On-Demand usage, over the lookback
          period. This is calculated as ``estimatedSavingsAmount`` / ``CurrentOnDemandSpend`` *100.

        - **EstimatedMonthlySavingsAmount** *(string) --*

          The estimated monthly savings amount, based on the recommended Savings Plans purchase.

        - **EstimatedOnDemandCostWithCurrentCommitment** *(string) --*

          The estimated On-Demand costs you would expect with no additional commitment, based on
          your usage of the selected time period and the Savings Plans you own.

    - **NextPageToken** *(string) --*

      The token for the next set of retrievable results. AWS provides the token when the response
      from a previous call has more results than the maximum page size.
    """


_ClientGetSavingsPlansUtilizationDetailsFilterDimensionsTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationDetailsFilterDimensionsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetSavingsPlansUtilizationDetailsFilterDimensionsTypeDef(
    _ClientGetSavingsPlansUtilizationDetailsFilterDimensionsTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansUtilizationDetailsFilter` `Dimensions`

    The specific ``Dimension`` to use for ``Expression`` .

    - **Key** *(string) --*

      The names of the metadata types that you can use to filter and group your results. For
      example, ``AZ`` returns a list of Availability Zones.

    - **Values** *(list) --*

      The metadata values that you can use to filter and group your results. You can use
      ``GetDimensionValues`` to find specific values.

      Valid values for the ``SERVICE`` dimension are ``Amazon Elastic Compute Cloud - Compute`` ,
      ``Amazon Elasticsearch Service`` , ``Amazon ElastiCache`` , ``Amazon Redshift`` , and
      ``Amazon Relational Database Service`` .

      - *(string) --*
    """


_ClientGetSavingsPlansUtilizationDetailsFilterTagsTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationDetailsFilterTagsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetSavingsPlansUtilizationDetailsFilterTagsTypeDef(
    _ClientGetSavingsPlansUtilizationDetailsFilterTagsTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansUtilizationDetailsFilter` `Tags`

    The specific ``Tag`` to use for ``Expression`` .

    - **Key** *(string) --*

      The key for the tag.

    - **Values** *(list) --*

      The specific value of the tag.

      - *(string) --*
    """


_ClientGetSavingsPlansUtilizationDetailsFilterTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationDetailsFilterTypeDef",
    {
        "Or": List[Dict],
        "And": List[Dict],
        "Not": Dict,
        "Dimensions": ClientGetSavingsPlansUtilizationDetailsFilterDimensionsTypeDef,
        "Tags": ClientGetSavingsPlansUtilizationDetailsFilterTagsTypeDef,
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationDetailsFilterTypeDef(
    _ClientGetSavingsPlansUtilizationDetailsFilterTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansUtilizationDetails` `Filter`

    Filters Savings Plans utilization coverage data for active Savings Plans dimensions. You can
    filter data with the following dimensions:

    * ``LINKED_ACCOUNT``

    * ``SAVINGS_PLAN_ARN``

    * ``REGION``

    * ``PAYMENT_OPTION``

    * ``INSTANCE_TYPE_FAMILY``

     ``GetSavingsPlansUtilizationDetails`` uses the same `Expression
     <http://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html>`__
     object as the other operations, but only ``AND`` is supported among each dimension.

    - **Or** *(list) --*

      Return results that match either ``Dimension`` object.

      - *(dict) --*

        Use ``Expression`` to filter by cost or by usage. There are two patterns:

        * Simple dimension values - You can set the dimension name and values for the filters that
        you plan to use. For example, you can filter for ``REGION==us-east-1 OR REGION==us-west-1`` .
        The ``Expression`` for that looks like this:  ``{ "Dimensions": { "Key": "REGION", "Values":
        [ "us-east-1", “us-west-1” ] } }``   The list of dimension values are OR'd together to
        retrieve cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects
        using either ``with*`` methods or ``set*`` methods in multiple lines.

        * Compound dimension values with logical operations - You can use multiple ``Expression``
        types and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression``
        objects. This allows you to filter on more advanced options. For example, you can filter on
        ``((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE !=
        DataTransfer)`` . The ``Expression`` for that looks like this:  ``{ "And": [ {"Or": [
        {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": {
        "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE",
        "Values": ["DataTransfer"] }}} ] }``

        .. note::

           Because each ``Expression`` can have only one operator, the service returns an error if
           more than one is specified. The following example shows an ``Expression`` object that
           creates an error.

          ``{ "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [
          "DataTransfer" ] } }``

        .. note::

          For ``GetRightsizingRecommendation`` action, a combination of OR and NOT is not supported.
          OR is not supported between different dimensions, or dimensions and tags. NOT operators
          aren't supported. Dimensions are also limited to ``LINKED_ACCOUNT`` , ``REGION`` , or
          ``RIGHTSIZING_TYPE`` .

    - **And** *(list) --*

      Return results that match both ``Dimension`` objects.

      - *(dict) --*

        Use ``Expression`` to filter by cost or by usage. There are two patterns:

        * Simple dimension values - You can set the dimension name and values for the filters that
        you plan to use. For example, you can filter for ``REGION==us-east-1 OR REGION==us-west-1`` .
        The ``Expression`` for that looks like this:  ``{ "Dimensions": { "Key": "REGION", "Values":
        [ "us-east-1", “us-west-1” ] } }``   The list of dimension values are OR'd together to
        retrieve cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects
        using either ``with*`` methods or ``set*`` methods in multiple lines.

        * Compound dimension values with logical operations - You can use multiple ``Expression``
        types and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression``
        objects. This allows you to filter on more advanced options. For example, you can filter on
        ``((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE !=
        DataTransfer)`` . The ``Expression`` for that looks like this:  ``{ "And": [ {"Or": [
        {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": {
        "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE",
        "Values": ["DataTransfer"] }}} ] }``

        .. note::

           Because each ``Expression`` can have only one operator, the service returns an error if
           more than one is specified. The following example shows an ``Expression`` object that
           creates an error.

          ``{ "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [
          "DataTransfer" ] } }``

        .. note::

          For ``GetRightsizingRecommendation`` action, a combination of OR and NOT is not supported.
          OR is not supported between different dimensions, or dimensions and tags. NOT operators
          aren't supported. Dimensions are also limited to ``LINKED_ACCOUNT`` , ``REGION`` , or
          ``RIGHTSIZING_TYPE`` .

    - **Not** *(dict) --*

      Return results that don't match a ``Dimension`` object.

    - **Dimensions** *(dict) --*

      The specific ``Dimension`` to use for ``Expression`` .

      - **Key** *(string) --*

        The names of the metadata types that you can use to filter and group your results. For
        example, ``AZ`` returns a list of Availability Zones.

      - **Values** *(list) --*

        The metadata values that you can use to filter and group your results. You can use
        ``GetDimensionValues`` to find specific values.

        Valid values for the ``SERVICE`` dimension are ``Amazon Elastic Compute Cloud - Compute`` ,
        ``Amazon Elasticsearch Service`` , ``Amazon ElastiCache`` , ``Amazon Redshift`` , and
        ``Amazon Relational Database Service`` .

        - *(string) --*

    - **Tags** *(dict) --*

      The specific ``Tag`` to use for ``Expression`` .

      - **Key** *(string) --*

        The key for the tag.

      - **Values** *(list) --*

        The specific value of the tag.

        - *(string) --*
    """


_ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsAmortizedCommitmentTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsAmortizedCommitmentTypeDef",
    {
        "AmortizedRecurringCommitment": str,
        "AmortizedUpfrontCommitment": str,
        "TotalAmortizedCommitment": str,
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsAmortizedCommitmentTypeDef(
    _ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsAmortizedCommitmentTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetails` `AmortizedCommitment`

    The total amortized commitment for a Savings Plans. Includes the sum of the upfront and
    recurring Savings Plans fees.

    - **AmortizedRecurringCommitment** *(string) --*

      The amortized amount of your Savings Plans commitment that was purchased with either a
      ``Partial`` or a ``NoUpfront`` .

    - **AmortizedUpfrontCommitment** *(string) --*

      The amortized amount of your Savings Plans commitment that was purchased with an
      ``Upfront`` or ``PartialUpfront`` Savings Plans.

    - **TotalAmortizedCommitment** *(string) --*

      The total amortized amount of your Savings Plans commitment, regardless of your Savings
      Plans purchase method.
    """


_ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsSavingsTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsSavingsTypeDef",
    {"NetSavings": str, "OnDemandCostEquivalent": str},
    total=False,
)


class ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsSavingsTypeDef(
    _ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsSavingsTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetails` `Savings`

    The amount saved by using existing Savings Plans. Savings returns both net savings from
    savings plans as well as the ``onDemandCostEquivalent`` of the Savings Plans when
    considering the utilization rate.

    - **NetSavings** *(string) --*

      The savings amount that you are accumulating for the usage that is covered by a Savings
      Plans, when compared to the On-Demand equivalent of the same usage.

    - **OnDemandCostEquivalent** *(string) --*

      How much the amount that the usage would have cost if it was accrued at the On-Demand
      rate.
    """


_ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsUtilizationTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsUtilizationTypeDef",
    {
        "TotalCommitment": str,
        "UsedCommitment": str,
        "UnusedCommitment": str,
        "UtilizationPercentage": str,
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsUtilizationTypeDef(
    _ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsUtilizationTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetails` `Utilization`

    A ratio of your effectiveness of using existing Savings Plans to apply to workloads that
    are Savings Plans eligible.

    - **TotalCommitment** *(string) --*

      The total amount of Savings Plans commitment that's been purchased in an account (or
      set of accounts).

    - **UsedCommitment** *(string) --*

      The amount of your Savings Plans commitment that was consumed from Savings Plans
      eligible usage in a specific period.

    - **UnusedCommitment** *(string) --*

      The amount of your Savings Plans commitment that was not consumed from Savings Plans
      eligible usage in a specific period.

    - **UtilizationPercentage** *(string) --*

      The amount of ``UsedCommitment`` divided by the ``TotalCommitment`` for your Savings
      Plans.
    """


_ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsTypeDef",
    {
        "SavingsPlanArn": str,
        "Attributes": Dict[str, str],
        "Utilization": ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsUtilizationTypeDef,
        "Savings": ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsSavingsTypeDef,
        "AmortizedCommitment": ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsAmortizedCommitmentTypeDef,
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsTypeDef(
    _ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansUtilizationDetailsResponse` `SavingsPlansUtilizationDetails`

    A single daily or monthly Savings Plans utilization rate, and details for your account.
    Master accounts in an organization have access to member accounts. You can use
    ``GetDimensionValues`` to determine the possible dimension values.

    - **SavingsPlanArn** *(string) --*

      The unique Amazon Resource Name (ARN) for a particular Savings Plan.

    - **Attributes** *(dict) --*

      The attribute that applies to a specific ``Dimension`` .

      - *(string) --*

        - *(string) --*

    - **Utilization** *(dict) --*

      A ratio of your effectiveness of using existing Savings Plans to apply to workloads that
      are Savings Plans eligible.

      - **TotalCommitment** *(string) --*

        The total amount of Savings Plans commitment that's been purchased in an account (or
        set of accounts).

      - **UsedCommitment** *(string) --*

        The amount of your Savings Plans commitment that was consumed from Savings Plans
        eligible usage in a specific period.

      - **UnusedCommitment** *(string) --*

        The amount of your Savings Plans commitment that was not consumed from Savings Plans
        eligible usage in a specific period.

      - **UtilizationPercentage** *(string) --*

        The amount of ``UsedCommitment`` divided by the ``TotalCommitment`` for your Savings
        Plans.

    - **Savings** *(dict) --*

      The amount saved by using existing Savings Plans. Savings returns both net savings from
      savings plans as well as the ``onDemandCostEquivalent`` of the Savings Plans when
      considering the utilization rate.

      - **NetSavings** *(string) --*

        The savings amount that you are accumulating for the usage that is covered by a Savings
        Plans, when compared to the On-Demand equivalent of the same usage.

      - **OnDemandCostEquivalent** *(string) --*

        How much the amount that the usage would have cost if it was accrued at the On-Demand
        rate.

    - **AmortizedCommitment** *(dict) --*

      The total amortized commitment for a Savings Plans. Includes the sum of the upfront and
      recurring Savings Plans fees.

      - **AmortizedRecurringCommitment** *(string) --*

        The amortized amount of your Savings Plans commitment that was purchased with either a
        ``Partial`` or a ``NoUpfront`` .

      - **AmortizedUpfrontCommitment** *(string) --*

        The amortized amount of your Savings Plans commitment that was purchased with an
        ``Upfront`` or ``PartialUpfront`` Savings Plans.

      - **TotalAmortizedCommitment** *(string) --*

        The total amortized amount of your Savings Plans commitment, regardless of your Savings
        Plans purchase method.
    """


_ClientGetSavingsPlansUtilizationDetailsResponseTimePeriodTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationDetailsResponseTimePeriodTypeDef",
    {"Start": str, "End": str},
    total=False,
)


class ClientGetSavingsPlansUtilizationDetailsResponseTimePeriodTypeDef(
    _ClientGetSavingsPlansUtilizationDetailsResponseTimePeriodTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansUtilizationDetailsResponse` `TimePeriod`

    The time period that you want the usage and costs for.

    - **Start** *(string) --*

      The beginning of the time period that you want the usage and costs for. The start date is
      inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data
      starting at ``2017-01-01`` up to the end date.

    - **End** *(string) --*

      The end of the time period that you want the usage and costs for. The end date is
      exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage data
      from the start date up to, but not including, ``2017-05-01`` .
    """


_ClientGetSavingsPlansUtilizationDetailsResponseTotalAmortizedCommitmentTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationDetailsResponseTotalAmortizedCommitmentTypeDef",
    {
        "AmortizedRecurringCommitment": str,
        "AmortizedUpfrontCommitment": str,
        "TotalAmortizedCommitment": str,
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationDetailsResponseTotalAmortizedCommitmentTypeDef(
    _ClientGetSavingsPlansUtilizationDetailsResponseTotalAmortizedCommitmentTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansUtilizationDetailsResponseTotal` `AmortizedCommitment`

    The total amortized commitment for a Savings Plans. This includes the sum of the upfront
    and recurring Savings Plans fees.

    - **AmortizedRecurringCommitment** *(string) --*

      The amortized amount of your Savings Plans commitment that was purchased with either a
      ``Partial`` or a ``NoUpfront`` .

    - **AmortizedUpfrontCommitment** *(string) --*

      The amortized amount of your Savings Plans commitment that was purchased with an
      ``Upfront`` or ``PartialUpfront`` Savings Plans.

    - **TotalAmortizedCommitment** *(string) --*

      The total amortized amount of your Savings Plans commitment, regardless of your Savings
      Plans purchase method.
    """


_ClientGetSavingsPlansUtilizationDetailsResponseTotalSavingsTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationDetailsResponseTotalSavingsTypeDef",
    {"NetSavings": str, "OnDemandCostEquivalent": str},
    total=False,
)


class ClientGetSavingsPlansUtilizationDetailsResponseTotalSavingsTypeDef(
    _ClientGetSavingsPlansUtilizationDetailsResponseTotalSavingsTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansUtilizationDetailsResponseTotal` `Savings`

    The amount saved by using existing Savings Plans. Savings returns both net savings from
    Savings Plans, as well as the ``onDemandCostEquivalent`` of the Savings Plans when
    considering the utilization rate.

    - **NetSavings** *(string) --*

      The savings amount that you are accumulating for the usage that is covered by a Savings
      Plans, when compared to the On-Demand equivalent of the same usage.

    - **OnDemandCostEquivalent** *(string) --*

      How much the amount that the usage would have cost if it was accrued at the On-Demand
      rate.
    """


_ClientGetSavingsPlansUtilizationDetailsResponseTotalUtilizationTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationDetailsResponseTotalUtilizationTypeDef",
    {
        "TotalCommitment": str,
        "UsedCommitment": str,
        "UnusedCommitment": str,
        "UtilizationPercentage": str,
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationDetailsResponseTotalUtilizationTypeDef(
    _ClientGetSavingsPlansUtilizationDetailsResponseTotalUtilizationTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansUtilizationDetailsResponseTotal` `Utilization`

    A ratio of your effectiveness of using existing Savings Plans to apply to workloads that
    are Savings Plans eligible.

    - **TotalCommitment** *(string) --*

      The total amount of Savings Plans commitment that's been purchased in an account (or set
      of accounts).

    - **UsedCommitment** *(string) --*

      The amount of your Savings Plans commitment that was consumed from Savings Plans eligible
      usage in a specific period.

    - **UnusedCommitment** *(string) --*

      The amount of your Savings Plans commitment that was not consumed from Savings Plans
      eligible usage in a specific period.

    - **UtilizationPercentage** *(string) --*

      The amount of ``UsedCommitment`` divided by the ``TotalCommitment`` for your Savings
      Plans.
    """


_ClientGetSavingsPlansUtilizationDetailsResponseTotalTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationDetailsResponseTotalTypeDef",
    {
        "Utilization": ClientGetSavingsPlansUtilizationDetailsResponseTotalUtilizationTypeDef,
        "Savings": ClientGetSavingsPlansUtilizationDetailsResponseTotalSavingsTypeDef,
        "AmortizedCommitment": ClientGetSavingsPlansUtilizationDetailsResponseTotalAmortizedCommitmentTypeDef,
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationDetailsResponseTotalTypeDef(
    _ClientGetSavingsPlansUtilizationDetailsResponseTotalTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansUtilizationDetailsResponse` `Total`

    The total Savings Plans utilization, regardless of time period.

    - **Utilization** *(dict) --*

      A ratio of your effectiveness of using existing Savings Plans to apply to workloads that
      are Savings Plans eligible.

      - **TotalCommitment** *(string) --*

        The total amount of Savings Plans commitment that's been purchased in an account (or set
        of accounts).

      - **UsedCommitment** *(string) --*

        The amount of your Savings Plans commitment that was consumed from Savings Plans eligible
        usage in a specific period.

      - **UnusedCommitment** *(string) --*

        The amount of your Savings Plans commitment that was not consumed from Savings Plans
        eligible usage in a specific period.

      - **UtilizationPercentage** *(string) --*

        The amount of ``UsedCommitment`` divided by the ``TotalCommitment`` for your Savings
        Plans.

    - **Savings** *(dict) --*

      The amount saved by using existing Savings Plans. Savings returns both net savings from
      Savings Plans, as well as the ``onDemandCostEquivalent`` of the Savings Plans when
      considering the utilization rate.

      - **NetSavings** *(string) --*

        The savings amount that you are accumulating for the usage that is covered by a Savings
        Plans, when compared to the On-Demand equivalent of the same usage.

      - **OnDemandCostEquivalent** *(string) --*

        How much the amount that the usage would have cost if it was accrued at the On-Demand
        rate.

    - **AmortizedCommitment** *(dict) --*

      The total amortized commitment for a Savings Plans. This includes the sum of the upfront
      and recurring Savings Plans fees.

      - **AmortizedRecurringCommitment** *(string) --*

        The amortized amount of your Savings Plans commitment that was purchased with either a
        ``Partial`` or a ``NoUpfront`` .

      - **AmortizedUpfrontCommitment** *(string) --*

        The amortized amount of your Savings Plans commitment that was purchased with an
        ``Upfront`` or ``PartialUpfront`` Savings Plans.

      - **TotalAmortizedCommitment** *(string) --*

        The total amortized amount of your Savings Plans commitment, regardless of your Savings
        Plans purchase method.
    """


_ClientGetSavingsPlansUtilizationDetailsResponseTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationDetailsResponseTypeDef",
    {
        "SavingsPlansUtilizationDetails": List[
            ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsTypeDef
        ],
        "Total": ClientGetSavingsPlansUtilizationDetailsResponseTotalTypeDef,
        "TimePeriod": ClientGetSavingsPlansUtilizationDetailsResponseTimePeriodTypeDef,
        "NextToken": str,
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationDetailsResponseTypeDef(
    _ClientGetSavingsPlansUtilizationDetailsResponseTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansUtilizationDetails` `Response`

    - **SavingsPlansUtilizationDetails** *(list) --*

      Retrieves a single daily or monthly Savings Plans utilization rate and details for your
      account.

      - *(dict) --*

        A single daily or monthly Savings Plans utilization rate, and details for your account.
        Master accounts in an organization have access to member accounts. You can use
        ``GetDimensionValues`` to determine the possible dimension values.

        - **SavingsPlanArn** *(string) --*

          The unique Amazon Resource Name (ARN) for a particular Savings Plan.

        - **Attributes** *(dict) --*

          The attribute that applies to a specific ``Dimension`` .

          - *(string) --*

            - *(string) --*

        - **Utilization** *(dict) --*

          A ratio of your effectiveness of using existing Savings Plans to apply to workloads that
          are Savings Plans eligible.

          - **TotalCommitment** *(string) --*

            The total amount of Savings Plans commitment that's been purchased in an account (or
            set of accounts).

          - **UsedCommitment** *(string) --*

            The amount of your Savings Plans commitment that was consumed from Savings Plans
            eligible usage in a specific period.

          - **UnusedCommitment** *(string) --*

            The amount of your Savings Plans commitment that was not consumed from Savings Plans
            eligible usage in a specific period.

          - **UtilizationPercentage** *(string) --*

            The amount of ``UsedCommitment`` divided by the ``TotalCommitment`` for your Savings
            Plans.

        - **Savings** *(dict) --*

          The amount saved by using existing Savings Plans. Savings returns both net savings from
          savings plans as well as the ``onDemandCostEquivalent`` of the Savings Plans when
          considering the utilization rate.

          - **NetSavings** *(string) --*

            The savings amount that you are accumulating for the usage that is covered by a Savings
            Plans, when compared to the On-Demand equivalent of the same usage.

          - **OnDemandCostEquivalent** *(string) --*

            How much the amount that the usage would have cost if it was accrued at the On-Demand
            rate.

        - **AmortizedCommitment** *(dict) --*

          The total amortized commitment for a Savings Plans. Includes the sum of the upfront and
          recurring Savings Plans fees.

          - **AmortizedRecurringCommitment** *(string) --*

            The amortized amount of your Savings Plans commitment that was purchased with either a
            ``Partial`` or a ``NoUpfront`` .

          - **AmortizedUpfrontCommitment** *(string) --*

            The amortized amount of your Savings Plans commitment that was purchased with an
            ``Upfront`` or ``PartialUpfront`` Savings Plans.

          - **TotalAmortizedCommitment** *(string) --*

            The total amortized amount of your Savings Plans commitment, regardless of your Savings
            Plans purchase method.

    - **Total** *(dict) --*

      The total Savings Plans utilization, regardless of time period.

      - **Utilization** *(dict) --*

        A ratio of your effectiveness of using existing Savings Plans to apply to workloads that
        are Savings Plans eligible.

        - **TotalCommitment** *(string) --*

          The total amount of Savings Plans commitment that's been purchased in an account (or set
          of accounts).

        - **UsedCommitment** *(string) --*

          The amount of your Savings Plans commitment that was consumed from Savings Plans eligible
          usage in a specific period.

        - **UnusedCommitment** *(string) --*

          The amount of your Savings Plans commitment that was not consumed from Savings Plans
          eligible usage in a specific period.

        - **UtilizationPercentage** *(string) --*

          The amount of ``UsedCommitment`` divided by the ``TotalCommitment`` for your Savings
          Plans.

      - **Savings** *(dict) --*

        The amount saved by using existing Savings Plans. Savings returns both net savings from
        Savings Plans, as well as the ``onDemandCostEquivalent`` of the Savings Plans when
        considering the utilization rate.

        - **NetSavings** *(string) --*

          The savings amount that you are accumulating for the usage that is covered by a Savings
          Plans, when compared to the On-Demand equivalent of the same usage.

        - **OnDemandCostEquivalent** *(string) --*

          How much the amount that the usage would have cost if it was accrued at the On-Demand
          rate.

      - **AmortizedCommitment** *(dict) --*

        The total amortized commitment for a Savings Plans. This includes the sum of the upfront
        and recurring Savings Plans fees.

        - **AmortizedRecurringCommitment** *(string) --*

          The amortized amount of your Savings Plans commitment that was purchased with either a
          ``Partial`` or a ``NoUpfront`` .

        - **AmortizedUpfrontCommitment** *(string) --*

          The amortized amount of your Savings Plans commitment that was purchased with an
          ``Upfront`` or ``PartialUpfront`` Savings Plans.

        - **TotalAmortizedCommitment** *(string) --*

          The total amortized amount of your Savings Plans commitment, regardless of your Savings
          Plans purchase method.

    - **TimePeriod** *(dict) --*

      The time period that you want the usage and costs for.

      - **Start** *(string) --*

        The beginning of the time period that you want the usage and costs for. The start date is
        inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data
        starting at ``2017-01-01`` up to the end date.

      - **End** *(string) --*

        The end of the time period that you want the usage and costs for. The end date is
        exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage data
        from the start date up to, but not including, ``2017-05-01`` .

    - **NextToken** *(string) --*

      The token to retrieve the next set of results. Amazon Web Services provides the token when
      the response from a previous call has more results than the maximum page size.
    """


_ClientGetSavingsPlansUtilizationDetailsTimePeriodTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationDetailsTimePeriodTypeDef",
    {"Start": str, "End": str},
)


class ClientGetSavingsPlansUtilizationDetailsTimePeriodTypeDef(
    _ClientGetSavingsPlansUtilizationDetailsTimePeriodTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansUtilizationDetails` `TimePeriod`

    The time period that you want the usage and costs for. The ``Start`` date must be within 13
    months. The ``End`` date must be after the ``Start`` date, and before the current date. Future
    dates can't be used as an ``End`` date.

    - **Start** *(string) --* **[REQUIRED]**

      The beginning of the time period that you want the usage and costs for. The start date is
      inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data
      starting at ``2017-01-01`` up to the end date.

    - **End** *(string) --* **[REQUIRED]**

      The end of the time period that you want the usage and costs for. The end date is exclusive.
      For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage data from the start
      date up to, but not including, ``2017-05-01`` .
    """


_ClientGetSavingsPlansUtilizationFilterDimensionsTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationFilterDimensionsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetSavingsPlansUtilizationFilterDimensionsTypeDef(
    _ClientGetSavingsPlansUtilizationFilterDimensionsTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansUtilizationFilter` `Dimensions`

    The specific ``Dimension`` to use for ``Expression`` .

    - **Key** *(string) --*

      The names of the metadata types that you can use to filter and group your results. For
      example, ``AZ`` returns a list of Availability Zones.

    - **Values** *(list) --*

      The metadata values that you can use to filter and group your results. You can use
      ``GetDimensionValues`` to find specific values.

      Valid values for the ``SERVICE`` dimension are ``Amazon Elastic Compute Cloud - Compute`` ,
      ``Amazon Elasticsearch Service`` , ``Amazon ElastiCache`` , ``Amazon Redshift`` , and
      ``Amazon Relational Database Service`` .

      - *(string) --*
    """


_ClientGetSavingsPlansUtilizationFilterTagsTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationFilterTagsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetSavingsPlansUtilizationFilterTagsTypeDef(
    _ClientGetSavingsPlansUtilizationFilterTagsTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansUtilizationFilter` `Tags`

    The specific ``Tag`` to use for ``Expression`` .

    - **Key** *(string) --*

      The key for the tag.

    - **Values** *(list) --*

      The specific value of the tag.

      - *(string) --*
    """


_ClientGetSavingsPlansUtilizationFilterTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationFilterTypeDef",
    {
        "Or": List[Dict],
        "And": List[Dict],
        "Not": Dict,
        "Dimensions": ClientGetSavingsPlansUtilizationFilterDimensionsTypeDef,
        "Tags": ClientGetSavingsPlansUtilizationFilterTagsTypeDef,
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationFilterTypeDef(
    _ClientGetSavingsPlansUtilizationFilterTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansUtilization` `Filter`

    Filters Savings Plans utilization coverage data for active Savings Plans dimensions. You can
    filter data with the following dimensions:

    * ``LINKED_ACCOUNT``

    * ``SAVINGS_PLAN_ARN``

    * ``SAVINGS_PLANS_TYPE``

    * ``REGION``

    * ``PAYMENT_OPTION``

    * ``INSTANCE_TYPE_FAMILY``

     ``GetSavingsPlansUtilization`` uses the same `Expression
     <http://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html>`__
     object as the other operations, but only ``AND`` is supported among each dimension.

    - **Or** *(list) --*

      Return results that match either ``Dimension`` object.

      - *(dict) --*

        Use ``Expression`` to filter by cost or by usage. There are two patterns:

        * Simple dimension values - You can set the dimension name and values for the filters that
        you plan to use. For example, you can filter for ``REGION==us-east-1 OR REGION==us-west-1`` .
        The ``Expression`` for that looks like this:  ``{ "Dimensions": { "Key": "REGION", "Values":
        [ "us-east-1", “us-west-1” ] } }``   The list of dimension values are OR'd together to
        retrieve cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects
        using either ``with*`` methods or ``set*`` methods in multiple lines.

        * Compound dimension values with logical operations - You can use multiple ``Expression``
        types and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression``
        objects. This allows you to filter on more advanced options. For example, you can filter on
        ``((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE !=
        DataTransfer)`` . The ``Expression`` for that looks like this:  ``{ "And": [ {"Or": [
        {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": {
        "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE",
        "Values": ["DataTransfer"] }}} ] }``

        .. note::

           Because each ``Expression`` can have only one operator, the service returns an error if
           more than one is specified. The following example shows an ``Expression`` object that
           creates an error.

          ``{ "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [
          "DataTransfer" ] } }``

        .. note::

          For ``GetRightsizingRecommendation`` action, a combination of OR and NOT is not supported.
          OR is not supported between different dimensions, or dimensions and tags. NOT operators
          aren't supported. Dimensions are also limited to ``LINKED_ACCOUNT`` , ``REGION`` , or
          ``RIGHTSIZING_TYPE`` .

    - **And** *(list) --*

      Return results that match both ``Dimension`` objects.

      - *(dict) --*

        Use ``Expression`` to filter by cost or by usage. There are two patterns:

        * Simple dimension values - You can set the dimension name and values for the filters that
        you plan to use. For example, you can filter for ``REGION==us-east-1 OR REGION==us-west-1`` .
        The ``Expression`` for that looks like this:  ``{ "Dimensions": { "Key": "REGION", "Values":
        [ "us-east-1", “us-west-1” ] } }``   The list of dimension values are OR'd together to
        retrieve cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects
        using either ``with*`` methods or ``set*`` methods in multiple lines.

        * Compound dimension values with logical operations - You can use multiple ``Expression``
        types and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression``
        objects. This allows you to filter on more advanced options. For example, you can filter on
        ``((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE !=
        DataTransfer)`` . The ``Expression`` for that looks like this:  ``{ "And": [ {"Or": [
        {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": {
        "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE",
        "Values": ["DataTransfer"] }}} ] }``

        .. note::

           Because each ``Expression`` can have only one operator, the service returns an error if
           more than one is specified. The following example shows an ``Expression`` object that
           creates an error.

          ``{ "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [
          "DataTransfer" ] } }``

        .. note::

          For ``GetRightsizingRecommendation`` action, a combination of OR and NOT is not supported.
          OR is not supported between different dimensions, or dimensions and tags. NOT operators
          aren't supported. Dimensions are also limited to ``LINKED_ACCOUNT`` , ``REGION`` , or
          ``RIGHTSIZING_TYPE`` .

    - **Not** *(dict) --*

      Return results that don't match a ``Dimension`` object.

    - **Dimensions** *(dict) --*

      The specific ``Dimension`` to use for ``Expression`` .

      - **Key** *(string) --*

        The names of the metadata types that you can use to filter and group your results. For
        example, ``AZ`` returns a list of Availability Zones.

      - **Values** *(list) --*

        The metadata values that you can use to filter and group your results. You can use
        ``GetDimensionValues`` to find specific values.

        Valid values for the ``SERVICE`` dimension are ``Amazon Elastic Compute Cloud - Compute`` ,
        ``Amazon Elasticsearch Service`` , ``Amazon ElastiCache`` , ``Amazon Redshift`` , and
        ``Amazon Relational Database Service`` .

        - *(string) --*

    - **Tags** *(dict) --*

      The specific ``Tag`` to use for ``Expression`` .

      - **Key** *(string) --*

        The key for the tag.

      - **Values** *(list) --*

        The specific value of the tag.

        - *(string) --*
    """


_ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeAmortizedCommitmentTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeAmortizedCommitmentTypeDef",
    {
        "AmortizedRecurringCommitment": str,
        "AmortizedUpfrontCommitment": str,
        "TotalAmortizedCommitment": str,
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeAmortizedCommitmentTypeDef(
    _ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeAmortizedCommitmentTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTime` `AmortizedCommitment`

    The total amortized commitment for a Savings Plans. This includes the sum of the upfront
    and recurring Savings Plans fees.

    - **AmortizedRecurringCommitment** *(string) --*

      The amortized amount of your Savings Plans commitment that was purchased with either a
      ``Partial`` or a ``NoUpfront`` .

    - **AmortizedUpfrontCommitment** *(string) --*

      The amortized amount of your Savings Plans commitment that was purchased with an
      ``Upfront`` or ``PartialUpfront`` Savings Plans.

    - **TotalAmortizedCommitment** *(string) --*

      The total amortized amount of your Savings Plans commitment, regardless of your Savings
      Plans purchase method.
    """


_ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeSavingsTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeSavingsTypeDef",
    {"NetSavings": str, "OnDemandCostEquivalent": str},
    total=False,
)


class ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeSavingsTypeDef(
    _ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeSavingsTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTime` `Savings`

    The amount saved by using existing Savings Plans. Savings returns both net savings from
    Savings Plans as well as the ``onDemandCostEquivalent`` of the Savings Plans when
    considering the utilization rate.

    - **NetSavings** *(string) --*

      The savings amount that you are accumulating for the usage that is covered by a Savings
      Plans, when compared to the On-Demand equivalent of the same usage.

    - **OnDemandCostEquivalent** *(string) --*

      How much the amount that the usage would have cost if it was accrued at the On-Demand
      rate.
    """


_ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeTimePeriodTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeTimePeriodTypeDef",
    {"Start": str, "End": str},
    total=False,
)


class ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeTimePeriodTypeDef(
    _ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeTimePeriodTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTime` `TimePeriod`

    The time period that you want the usage and costs for.

    - **Start** *(string) --*

      The beginning of the time period that you want the usage and costs for. The start date
      is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and
      usage data starting at ``2017-01-01`` up to the end date.

    - **End** *(string) --*

      The end of the time period that you want the usage and costs for. The end date is
      exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage
      data from the start date up to, but not including, ``2017-05-01`` .
    """


_ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeUtilizationTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeUtilizationTypeDef",
    {
        "TotalCommitment": str,
        "UsedCommitment": str,
        "UnusedCommitment": str,
        "UtilizationPercentage": str,
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeUtilizationTypeDef(
    _ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeUtilizationTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTime` `Utilization`

    A ratio of your effectiveness of using existing Savings Plans to apply to workloads that
    are Savings Plans eligible.

    - **TotalCommitment** *(string) --*

      The total amount of Savings Plans commitment that's been purchased in an account (or
      set of accounts).

    - **UsedCommitment** *(string) --*

      The amount of your Savings Plans commitment that was consumed from Savings Plans
      eligible usage in a specific period.

    - **UnusedCommitment** *(string) --*

      The amount of your Savings Plans commitment that was not consumed from Savings Plans
      eligible usage in a specific period.

    - **UtilizationPercentage** *(string) --*

      The amount of ``UsedCommitment`` divided by the ``TotalCommitment`` for your Savings
      Plans.
    """


_ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeTypeDef",
    {
        "TimePeriod": ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeTimePeriodTypeDef,
        "Utilization": ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeUtilizationTypeDef,
        "Savings": ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeSavingsTypeDef,
        "AmortizedCommitment": ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeAmortizedCommitmentTypeDef,
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeTypeDef(
    _ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansUtilizationResponse` `SavingsPlansUtilizationsByTime`

    The amount of Savings Plans utilization, in hours.

    - **TimePeriod** *(dict) --*

      The time period that you want the usage and costs for.

      - **Start** *(string) --*

        The beginning of the time period that you want the usage and costs for. The start date
        is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and
        usage data starting at ``2017-01-01`` up to the end date.

      - **End** *(string) --*

        The end of the time period that you want the usage and costs for. The end date is
        exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage
        data from the start date up to, but not including, ``2017-05-01`` .

    - **Utilization** *(dict) --*

      A ratio of your effectiveness of using existing Savings Plans to apply to workloads that
      are Savings Plans eligible.

      - **TotalCommitment** *(string) --*

        The total amount of Savings Plans commitment that's been purchased in an account (or
        set of accounts).

      - **UsedCommitment** *(string) --*

        The amount of your Savings Plans commitment that was consumed from Savings Plans
        eligible usage in a specific period.

      - **UnusedCommitment** *(string) --*

        The amount of your Savings Plans commitment that was not consumed from Savings Plans
        eligible usage in a specific period.

      - **UtilizationPercentage** *(string) --*

        The amount of ``UsedCommitment`` divided by the ``TotalCommitment`` for your Savings
        Plans.

    - **Savings** *(dict) --*

      The amount saved by using existing Savings Plans. Savings returns both net savings from
      Savings Plans as well as the ``onDemandCostEquivalent`` of the Savings Plans when
      considering the utilization rate.

      - **NetSavings** *(string) --*

        The savings amount that you are accumulating for the usage that is covered by a Savings
        Plans, when compared to the On-Demand equivalent of the same usage.

      - **OnDemandCostEquivalent** *(string) --*

        How much the amount that the usage would have cost if it was accrued at the On-Demand
        rate.

    - **AmortizedCommitment** *(dict) --*

      The total amortized commitment for a Savings Plans. This includes the sum of the upfront
      and recurring Savings Plans fees.

      - **AmortizedRecurringCommitment** *(string) --*

        The amortized amount of your Savings Plans commitment that was purchased with either a
        ``Partial`` or a ``NoUpfront`` .

      - **AmortizedUpfrontCommitment** *(string) --*

        The amortized amount of your Savings Plans commitment that was purchased with an
        ``Upfront`` or ``PartialUpfront`` Savings Plans.

      - **TotalAmortizedCommitment** *(string) --*

        The total amortized amount of your Savings Plans commitment, regardless of your Savings
        Plans purchase method.
    """


_ClientGetSavingsPlansUtilizationResponseTotalAmortizedCommitmentTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationResponseTotalAmortizedCommitmentTypeDef",
    {
        "AmortizedRecurringCommitment": str,
        "AmortizedUpfrontCommitment": str,
        "TotalAmortizedCommitment": str,
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationResponseTotalAmortizedCommitmentTypeDef(
    _ClientGetSavingsPlansUtilizationResponseTotalAmortizedCommitmentTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansUtilizationResponseTotal` `AmortizedCommitment`

    The total amortized commitment for a Savings Plans. This includes the sum of the upfront
    and recurring Savings Plans fees.

    - **AmortizedRecurringCommitment** *(string) --*

      The amortized amount of your Savings Plans commitment that was purchased with either a
      ``Partial`` or a ``NoUpfront`` .

    - **AmortizedUpfrontCommitment** *(string) --*

      The amortized amount of your Savings Plans commitment that was purchased with an
      ``Upfront`` or ``PartialUpfront`` Savings Plans.

    - **TotalAmortizedCommitment** *(string) --*

      The total amortized amount of your Savings Plans commitment, regardless of your Savings
      Plans purchase method.
    """


_ClientGetSavingsPlansUtilizationResponseTotalSavingsTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationResponseTotalSavingsTypeDef",
    {"NetSavings": str, "OnDemandCostEquivalent": str},
    total=False,
)


class ClientGetSavingsPlansUtilizationResponseTotalSavingsTypeDef(
    _ClientGetSavingsPlansUtilizationResponseTotalSavingsTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansUtilizationResponseTotal` `Savings`

    The amount saved by using existing Savings Plans. Savings returns both net savings from
    Savings Plans, as well as the ``onDemandCostEquivalent`` of the Savings Plans when
    considering the utilization rate.

    - **NetSavings** *(string) --*

      The savings amount that you are accumulating for the usage that is covered by a Savings
      Plans, when compared to the On-Demand equivalent of the same usage.

    - **OnDemandCostEquivalent** *(string) --*

      How much the amount that the usage would have cost if it was accrued at the On-Demand
      rate.
    """


_ClientGetSavingsPlansUtilizationResponseTotalUtilizationTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationResponseTotalUtilizationTypeDef",
    {
        "TotalCommitment": str,
        "UsedCommitment": str,
        "UnusedCommitment": str,
        "UtilizationPercentage": str,
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationResponseTotalUtilizationTypeDef(
    _ClientGetSavingsPlansUtilizationResponseTotalUtilizationTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansUtilizationResponseTotal` `Utilization`

    A ratio of your effectiveness of using existing Savings Plans to apply to workloads that
    are Savings Plans eligible.

    - **TotalCommitment** *(string) --*

      The total amount of Savings Plans commitment that's been purchased in an account (or set
      of accounts).

    - **UsedCommitment** *(string) --*

      The amount of your Savings Plans commitment that was consumed from Savings Plans eligible
      usage in a specific period.

    - **UnusedCommitment** *(string) --*

      The amount of your Savings Plans commitment that was not consumed from Savings Plans
      eligible usage in a specific period.

    - **UtilizationPercentage** *(string) --*

      The amount of ``UsedCommitment`` divided by the ``TotalCommitment`` for your Savings
      Plans.
    """


_ClientGetSavingsPlansUtilizationResponseTotalTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationResponseTotalTypeDef",
    {
        "Utilization": ClientGetSavingsPlansUtilizationResponseTotalUtilizationTypeDef,
        "Savings": ClientGetSavingsPlansUtilizationResponseTotalSavingsTypeDef,
        "AmortizedCommitment": ClientGetSavingsPlansUtilizationResponseTotalAmortizedCommitmentTypeDef,
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationResponseTotalTypeDef(
    _ClientGetSavingsPlansUtilizationResponseTotalTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansUtilizationResponse` `Total`

    The total amount of cost/commitment that you used your Savings Plans, regardless of date
    ranges.

    - **Utilization** *(dict) --*

      A ratio of your effectiveness of using existing Savings Plans to apply to workloads that
      are Savings Plans eligible.

      - **TotalCommitment** *(string) --*

        The total amount of Savings Plans commitment that's been purchased in an account (or set
        of accounts).

      - **UsedCommitment** *(string) --*

        The amount of your Savings Plans commitment that was consumed from Savings Plans eligible
        usage in a specific period.

      - **UnusedCommitment** *(string) --*

        The amount of your Savings Plans commitment that was not consumed from Savings Plans
        eligible usage in a specific period.

      - **UtilizationPercentage** *(string) --*

        The amount of ``UsedCommitment`` divided by the ``TotalCommitment`` for your Savings
        Plans.

    - **Savings** *(dict) --*

      The amount saved by using existing Savings Plans. Savings returns both net savings from
      Savings Plans, as well as the ``onDemandCostEquivalent`` of the Savings Plans when
      considering the utilization rate.

      - **NetSavings** *(string) --*

        The savings amount that you are accumulating for the usage that is covered by a Savings
        Plans, when compared to the On-Demand equivalent of the same usage.

      - **OnDemandCostEquivalent** *(string) --*

        How much the amount that the usage would have cost if it was accrued at the On-Demand
        rate.

    - **AmortizedCommitment** *(dict) --*

      The total amortized commitment for a Savings Plans. This includes the sum of the upfront
      and recurring Savings Plans fees.

      - **AmortizedRecurringCommitment** *(string) --*

        The amortized amount of your Savings Plans commitment that was purchased with either a
        ``Partial`` or a ``NoUpfront`` .

      - **AmortizedUpfrontCommitment** *(string) --*

        The amortized amount of your Savings Plans commitment that was purchased with an
        ``Upfront`` or ``PartialUpfront`` Savings Plans.

      - **TotalAmortizedCommitment** *(string) --*

        The total amortized amount of your Savings Plans commitment, regardless of your Savings
        Plans purchase method.
    """


_ClientGetSavingsPlansUtilizationResponseTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationResponseTypeDef",
    {
        "SavingsPlansUtilizationsByTime": List[
            ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeTypeDef
        ],
        "Total": ClientGetSavingsPlansUtilizationResponseTotalTypeDef,
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationResponseTypeDef(
    _ClientGetSavingsPlansUtilizationResponseTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansUtilization` `Response`

    - **SavingsPlansUtilizationsByTime** *(list) --*

      The amount of cost/commitment you used your Savings Plans. This allows you to specify date
      ranges.

      - *(dict) --*

        The amount of Savings Plans utilization, in hours.

        - **TimePeriod** *(dict) --*

          The time period that you want the usage and costs for.

          - **Start** *(string) --*

            The beginning of the time period that you want the usage and costs for. The start date
            is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and
            usage data starting at ``2017-01-01`` up to the end date.

          - **End** *(string) --*

            The end of the time period that you want the usage and costs for. The end date is
            exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage
            data from the start date up to, but not including, ``2017-05-01`` .

        - **Utilization** *(dict) --*

          A ratio of your effectiveness of using existing Savings Plans to apply to workloads that
          are Savings Plans eligible.

          - **TotalCommitment** *(string) --*

            The total amount of Savings Plans commitment that's been purchased in an account (or
            set of accounts).

          - **UsedCommitment** *(string) --*

            The amount of your Savings Plans commitment that was consumed from Savings Plans
            eligible usage in a specific period.

          - **UnusedCommitment** *(string) --*

            The amount of your Savings Plans commitment that was not consumed from Savings Plans
            eligible usage in a specific period.

          - **UtilizationPercentage** *(string) --*

            The amount of ``UsedCommitment`` divided by the ``TotalCommitment`` for your Savings
            Plans.

        - **Savings** *(dict) --*

          The amount saved by using existing Savings Plans. Savings returns both net savings from
          Savings Plans as well as the ``onDemandCostEquivalent`` of the Savings Plans when
          considering the utilization rate.

          - **NetSavings** *(string) --*

            The savings amount that you are accumulating for the usage that is covered by a Savings
            Plans, when compared to the On-Demand equivalent of the same usage.

          - **OnDemandCostEquivalent** *(string) --*

            How much the amount that the usage would have cost if it was accrued at the On-Demand
            rate.

        - **AmortizedCommitment** *(dict) --*

          The total amortized commitment for a Savings Plans. This includes the sum of the upfront
          and recurring Savings Plans fees.

          - **AmortizedRecurringCommitment** *(string) --*

            The amortized amount of your Savings Plans commitment that was purchased with either a
            ``Partial`` or a ``NoUpfront`` .

          - **AmortizedUpfrontCommitment** *(string) --*

            The amortized amount of your Savings Plans commitment that was purchased with an
            ``Upfront`` or ``PartialUpfront`` Savings Plans.

          - **TotalAmortizedCommitment** *(string) --*

            The total amortized amount of your Savings Plans commitment, regardless of your Savings
            Plans purchase method.

    - **Total** *(dict) --*

      The total amount of cost/commitment that you used your Savings Plans, regardless of date
      ranges.

      - **Utilization** *(dict) --*

        A ratio of your effectiveness of using existing Savings Plans to apply to workloads that
        are Savings Plans eligible.

        - **TotalCommitment** *(string) --*

          The total amount of Savings Plans commitment that's been purchased in an account (or set
          of accounts).

        - **UsedCommitment** *(string) --*

          The amount of your Savings Plans commitment that was consumed from Savings Plans eligible
          usage in a specific period.

        - **UnusedCommitment** *(string) --*

          The amount of your Savings Plans commitment that was not consumed from Savings Plans
          eligible usage in a specific period.

        - **UtilizationPercentage** *(string) --*

          The amount of ``UsedCommitment`` divided by the ``TotalCommitment`` for your Savings
          Plans.

      - **Savings** *(dict) --*

        The amount saved by using existing Savings Plans. Savings returns both net savings from
        Savings Plans, as well as the ``onDemandCostEquivalent`` of the Savings Plans when
        considering the utilization rate.

        - **NetSavings** *(string) --*

          The savings amount that you are accumulating for the usage that is covered by a Savings
          Plans, when compared to the On-Demand equivalent of the same usage.

        - **OnDemandCostEquivalent** *(string) --*

          How much the amount that the usage would have cost if it was accrued at the On-Demand
          rate.

      - **AmortizedCommitment** *(dict) --*

        The total amortized commitment for a Savings Plans. This includes the sum of the upfront
        and recurring Savings Plans fees.

        - **AmortizedRecurringCommitment** *(string) --*

          The amortized amount of your Savings Plans commitment that was purchased with either a
          ``Partial`` or a ``NoUpfront`` .

        - **AmortizedUpfrontCommitment** *(string) --*

          The amortized amount of your Savings Plans commitment that was purchased with an
          ``Upfront`` or ``PartialUpfront`` Savings Plans.

        - **TotalAmortizedCommitment** *(string) --*

          The total amortized amount of your Savings Plans commitment, regardless of your Savings
          Plans purchase method.
    """


_ClientGetSavingsPlansUtilizationTimePeriodTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationTimePeriodTypeDef", {"Start": str, "End": str}
)


class ClientGetSavingsPlansUtilizationTimePeriodTypeDef(
    _ClientGetSavingsPlansUtilizationTimePeriodTypeDef
):
    """
    Type definition for `ClientGetSavingsPlansUtilization` `TimePeriod`

    The time period that you want the usage and costs for. The ``Start`` date must be within 13
    months. The ``End`` date must be after the ``Start`` date, and before the current date. Future
    dates can't be used as an ``End`` date.

    - **Start** *(string) --* **[REQUIRED]**

      The beginning of the time period that you want the usage and costs for. The start date is
      inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data
      starting at ``2017-01-01`` up to the end date.

    - **End** *(string) --* **[REQUIRED]**

      The end of the time period that you want the usage and costs for. The end date is exclusive.
      For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage data from the start
      date up to, but not including, ``2017-05-01`` .
    """


_ClientGetTagsResponseTypeDef = TypedDict(
    "_ClientGetTagsResponseTypeDef",
    {"NextPageToken": str, "Tags": List[str], "ReturnSize": int, "TotalSize": int},
    total=False,
)


class ClientGetTagsResponseTypeDef(_ClientGetTagsResponseTypeDef):
    """
    Type definition for `ClientGetTags` `Response`

    - **NextPageToken** *(string) --*

      The token for the next set of retrievable results. AWS provides the token when the response
      from a previous call has more results than the maximum page size.

    - **Tags** *(list) --*

      The tags that match your request.

      - *(string) --*

    - **ReturnSize** *(integer) --*

      The number of query results that AWS returns at a time.

    - **TotalSize** *(integer) --*

      The total number of query results.
    """


_ClientGetTagsTimePeriodTypeDef = TypedDict(
    "_ClientGetTagsTimePeriodTypeDef", {"Start": str, "End": str}
)


class ClientGetTagsTimePeriodTypeDef(_ClientGetTagsTimePeriodTypeDef):
    """
    Type definition for `ClientGetTags` `TimePeriod`

    The start and end dates for retrieving the dimension values. The start date is inclusive, but the
    end date is exclusive. For example, if ``start`` is ``2017-01-01`` and ``end`` is ``2017-05-01``
    , then the cost and usage data is retrieved from ``2017-01-01`` up to and including
    ``2017-04-30`` but not including ``2017-05-01`` .

    - **Start** *(string) --* **[REQUIRED]**

      The beginning of the time period that you want the usage and costs for. The start date is
      inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data
      starting at ``2017-01-01`` up to the end date.

    - **End** *(string) --* **[REQUIRED]**

      The end of the time period that you want the usage and costs for. The end date is exclusive.
      For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage data from the start
      date up to, but not including, ``2017-05-01`` .
    """


_ClientGetUsageForecastFilterDimensionsTypeDef = TypedDict(
    "_ClientGetUsageForecastFilterDimensionsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetUsageForecastFilterDimensionsTypeDef(
    _ClientGetUsageForecastFilterDimensionsTypeDef
):
    """
    Type definition for `ClientGetUsageForecastFilter` `Dimensions`

    The specific ``Dimension`` to use for ``Expression`` .

    - **Key** *(string) --*

      The names of the metadata types that you can use to filter and group your results. For
      example, ``AZ`` returns a list of Availability Zones.

    - **Values** *(list) --*

      The metadata values that you can use to filter and group your results. You can use
      ``GetDimensionValues`` to find specific values.

      Valid values for the ``SERVICE`` dimension are ``Amazon Elastic Compute Cloud - Compute`` ,
      ``Amazon Elasticsearch Service`` , ``Amazon ElastiCache`` , ``Amazon Redshift`` , and
      ``Amazon Relational Database Service`` .

      - *(string) --*
    """


_ClientGetUsageForecastFilterTagsTypeDef = TypedDict(
    "_ClientGetUsageForecastFilterTagsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetUsageForecastFilterTagsTypeDef(_ClientGetUsageForecastFilterTagsTypeDef):
    """
    Type definition for `ClientGetUsageForecastFilter` `Tags`

    The specific ``Tag`` to use for ``Expression`` .

    - **Key** *(string) --*

      The key for the tag.

    - **Values** *(list) --*

      The specific value of the tag.

      - *(string) --*
    """


_ClientGetUsageForecastFilterTypeDef = TypedDict(
    "_ClientGetUsageForecastFilterTypeDef",
    {
        "Or": List[Dict],
        "And": List[Dict],
        "Not": Dict,
        "Dimensions": ClientGetUsageForecastFilterDimensionsTypeDef,
        "Tags": ClientGetUsageForecastFilterTagsTypeDef,
    },
    total=False,
)


class ClientGetUsageForecastFilterTypeDef(_ClientGetUsageForecastFilterTypeDef):
    """
    Type definition for `ClientGetUsageForecast` `Filter`

    The filters that you want to use to filter your forecast. Cost Explorer API supports all of the
    Cost Explorer filters.

    - **Or** *(list) --*

      Return results that match either ``Dimension`` object.

      - *(dict) --*

        Use ``Expression`` to filter by cost or by usage. There are two patterns:

        * Simple dimension values - You can set the dimension name and values for the filters that
        you plan to use. For example, you can filter for ``REGION==us-east-1 OR REGION==us-west-1`` .
        The ``Expression`` for that looks like this:  ``{ "Dimensions": { "Key": "REGION", "Values":
        [ "us-east-1", “us-west-1” ] } }``   The list of dimension values are OR'd together to
        retrieve cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects
        using either ``with*`` methods or ``set*`` methods in multiple lines.

        * Compound dimension values with logical operations - You can use multiple ``Expression``
        types and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression``
        objects. This allows you to filter on more advanced options. For example, you can filter on
        ``((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE !=
        DataTransfer)`` . The ``Expression`` for that looks like this:  ``{ "And": [ {"Or": [
        {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": {
        "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE",
        "Values": ["DataTransfer"] }}} ] }``

        .. note::

           Because each ``Expression`` can have only one operator, the service returns an error if
           more than one is specified. The following example shows an ``Expression`` object that
           creates an error.

          ``{ "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [
          "DataTransfer" ] } }``

        .. note::

          For ``GetRightsizingRecommendation`` action, a combination of OR and NOT is not supported.
          OR is not supported between different dimensions, or dimensions and tags. NOT operators
          aren't supported. Dimensions are also limited to ``LINKED_ACCOUNT`` , ``REGION`` , or
          ``RIGHTSIZING_TYPE`` .

    - **And** *(list) --*

      Return results that match both ``Dimension`` objects.

      - *(dict) --*

        Use ``Expression`` to filter by cost or by usage. There are two patterns:

        * Simple dimension values - You can set the dimension name and values for the filters that
        you plan to use. For example, you can filter for ``REGION==us-east-1 OR REGION==us-west-1`` .
        The ``Expression`` for that looks like this:  ``{ "Dimensions": { "Key": "REGION", "Values":
        [ "us-east-1", “us-west-1” ] } }``   The list of dimension values are OR'd together to
        retrieve cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects
        using either ``with*`` methods or ``set*`` methods in multiple lines.

        * Compound dimension values with logical operations - You can use multiple ``Expression``
        types and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression``
        objects. This allows you to filter on more advanced options. For example, you can filter on
        ``((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE !=
        DataTransfer)`` . The ``Expression`` for that looks like this:  ``{ "And": [ {"Or": [
        {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": {
        "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE",
        "Values": ["DataTransfer"] }}} ] }``

        .. note::

           Because each ``Expression`` can have only one operator, the service returns an error if
           more than one is specified. The following example shows an ``Expression`` object that
           creates an error.

          ``{ "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [
          "DataTransfer" ] } }``

        .. note::

          For ``GetRightsizingRecommendation`` action, a combination of OR and NOT is not supported.
          OR is not supported between different dimensions, or dimensions and tags. NOT operators
          aren't supported. Dimensions are also limited to ``LINKED_ACCOUNT`` , ``REGION`` , or
          ``RIGHTSIZING_TYPE`` .

    - **Not** *(dict) --*

      Return results that don't match a ``Dimension`` object.

    - **Dimensions** *(dict) --*

      The specific ``Dimension`` to use for ``Expression`` .

      - **Key** *(string) --*

        The names of the metadata types that you can use to filter and group your results. For
        example, ``AZ`` returns a list of Availability Zones.

      - **Values** *(list) --*

        The metadata values that you can use to filter and group your results. You can use
        ``GetDimensionValues`` to find specific values.

        Valid values for the ``SERVICE`` dimension are ``Amazon Elastic Compute Cloud - Compute`` ,
        ``Amazon Elasticsearch Service`` , ``Amazon ElastiCache`` , ``Amazon Redshift`` , and
        ``Amazon Relational Database Service`` .

        - *(string) --*

    - **Tags** *(dict) --*

      The specific ``Tag`` to use for ``Expression`` .

      - **Key** *(string) --*

        The key for the tag.

      - **Values** *(list) --*

        The specific value of the tag.

        - *(string) --*
    """


_ClientGetUsageForecastResponseForecastResultsByTimeTimePeriodTypeDef = TypedDict(
    "_ClientGetUsageForecastResponseForecastResultsByTimeTimePeriodTypeDef",
    {"Start": str, "End": str},
    total=False,
)


class ClientGetUsageForecastResponseForecastResultsByTimeTimePeriodTypeDef(
    _ClientGetUsageForecastResponseForecastResultsByTimeTimePeriodTypeDef
):
    """
    Type definition for `ClientGetUsageForecastResponseForecastResultsByTime` `TimePeriod`

    The period of time that the forecast covers.

    - **Start** *(string) --*

      The beginning of the time period that you want the usage and costs for. The start date
      is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and
      usage data starting at ``2017-01-01`` up to the end date.

    - **End** *(string) --*

      The end of the time period that you want the usage and costs for. The end date is
      exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage
      data from the start date up to, but not including, ``2017-05-01`` .
    """


_ClientGetUsageForecastResponseForecastResultsByTimeTypeDef = TypedDict(
    "_ClientGetUsageForecastResponseForecastResultsByTimeTypeDef",
    {
        "TimePeriod": ClientGetUsageForecastResponseForecastResultsByTimeTimePeriodTypeDef,
        "MeanValue": str,
        "PredictionIntervalLowerBound": str,
        "PredictionIntervalUpperBound": str,
    },
    total=False,
)


class ClientGetUsageForecastResponseForecastResultsByTimeTypeDef(
    _ClientGetUsageForecastResponseForecastResultsByTimeTypeDef
):
    """
    Type definition for `ClientGetUsageForecastResponse` `ForecastResultsByTime`

    The forecast created for your query.

    - **TimePeriod** *(dict) --*

      The period of time that the forecast covers.

      - **Start** *(string) --*

        The beginning of the time period that you want the usage and costs for. The start date
        is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and
        usage data starting at ``2017-01-01`` up to the end date.

      - **End** *(string) --*

        The end of the time period that you want the usage and costs for. The end date is
        exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage
        data from the start date up to, but not including, ``2017-05-01`` .

    - **MeanValue** *(string) --*

      The mean value of the forecast.

    - **PredictionIntervalLowerBound** *(string) --*

      The lower limit for the prediction interval.

    - **PredictionIntervalUpperBound** *(string) --*

      The upper limit for the prediction interval.
    """


_ClientGetUsageForecastResponseTotalTypeDef = TypedDict(
    "_ClientGetUsageForecastResponseTotalTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientGetUsageForecastResponseTotalTypeDef(
    _ClientGetUsageForecastResponseTotalTypeDef
):
    """
    Type definition for `ClientGetUsageForecastResponse` `Total`

    How much you're forecasted to use over the forecast period.

    - **Amount** *(string) --*

      The actual number that represents the metric.

    - **Unit** *(string) --*

      The unit that the metric is given in.
    """


_ClientGetUsageForecastResponseTypeDef = TypedDict(
    "_ClientGetUsageForecastResponseTypeDef",
    {
        "Total": ClientGetUsageForecastResponseTotalTypeDef,
        "ForecastResultsByTime": List[
            ClientGetUsageForecastResponseForecastResultsByTimeTypeDef
        ],
    },
    total=False,
)


class ClientGetUsageForecastResponseTypeDef(_ClientGetUsageForecastResponseTypeDef):
    """
    Type definition for `ClientGetUsageForecast` `Response`

    - **Total** *(dict) --*

      How much you're forecasted to use over the forecast period.

      - **Amount** *(string) --*

        The actual number that represents the metric.

      - **Unit** *(string) --*

        The unit that the metric is given in.

    - **ForecastResultsByTime** *(list) --*

      The forecasts for your query, in order. For ``DAILY`` forecasts, this is a list of days. For
      ``MONTHLY`` forecasts, this is a list of months.

      - *(dict) --*

        The forecast created for your query.

        - **TimePeriod** *(dict) --*

          The period of time that the forecast covers.

          - **Start** *(string) --*

            The beginning of the time period that you want the usage and costs for. The start date
            is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and
            usage data starting at ``2017-01-01`` up to the end date.

          - **End** *(string) --*

            The end of the time period that you want the usage and costs for. The end date is
            exclusive. For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage
            data from the start date up to, but not including, ``2017-05-01`` .

        - **MeanValue** *(string) --*

          The mean value of the forecast.

        - **PredictionIntervalLowerBound** *(string) --*

          The lower limit for the prediction interval.

        - **PredictionIntervalUpperBound** *(string) --*

          The upper limit for the prediction interval.
    """


_ClientGetUsageForecastTimePeriodTypeDef = TypedDict(
    "_ClientGetUsageForecastTimePeriodTypeDef", {"Start": str, "End": str}
)


class ClientGetUsageForecastTimePeriodTypeDef(_ClientGetUsageForecastTimePeriodTypeDef):
    """
    Type definition for `ClientGetUsageForecast` `TimePeriod`

    The start and end dates of the period that you want to retrieve usage forecast for. The start
    date is inclusive, but the end date is exclusive. For example, if ``start`` is ``2017-01-01`` and
    ``end`` is ``2017-05-01`` , then the cost and usage data is retrieved from ``2017-01-01`` up to
    and including ``2017-04-30`` but not including ``2017-05-01`` .

    - **Start** *(string) --* **[REQUIRED]**

      The beginning of the time period that you want the usage and costs for. The start date is
      inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data
      starting at ``2017-01-01`` up to the end date.

    - **End** *(string) --* **[REQUIRED]**

      The end of the time period that you want the usage and costs for. The end date is exclusive.
      For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage data from the start
      date up to, but not including, ``2017-05-01`` .
    """
