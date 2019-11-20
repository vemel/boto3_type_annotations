"Main interface for ce Client"
from __future__ import annotations

from typing import Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_ce.client as client_scope
from mypy_boto3_ce.type_defs import (
    ClientGetCostAndUsageFilterTypeDef,
    ClientGetCostAndUsageGroupByTypeDef,
    ClientGetCostAndUsageResponseTypeDef,
    ClientGetCostAndUsageTimePeriodTypeDef,
    ClientGetCostAndUsageWithResourcesFilterTypeDef,
    ClientGetCostAndUsageWithResourcesGroupByTypeDef,
    ClientGetCostAndUsageWithResourcesResponseTypeDef,
    ClientGetCostAndUsageWithResourcesTimePeriodTypeDef,
    ClientGetCostForecastFilterTypeDef,
    ClientGetCostForecastResponseTypeDef,
    ClientGetCostForecastTimePeriodTypeDef,
    ClientGetDimensionValuesResponseTypeDef,
    ClientGetDimensionValuesTimePeriodTypeDef,
    ClientGetReservationCoverageFilterTypeDef,
    ClientGetReservationCoverageGroupByTypeDef,
    ClientGetReservationCoverageResponseTypeDef,
    ClientGetReservationCoverageTimePeriodTypeDef,
    ClientGetReservationPurchaseRecommendationResponseTypeDef,
    ClientGetReservationPurchaseRecommendationServiceSpecificationTypeDef,
    ClientGetReservationUtilizationFilterTypeDef,
    ClientGetReservationUtilizationGroupByTypeDef,
    ClientGetReservationUtilizationResponseTypeDef,
    ClientGetReservationUtilizationTimePeriodTypeDef,
    ClientGetRightsizingRecommendationFilterTypeDef,
    ClientGetRightsizingRecommendationResponseTypeDef,
    ClientGetSavingsPlansCoverageFilterTypeDef,
    ClientGetSavingsPlansCoverageGroupByTypeDef,
    ClientGetSavingsPlansCoverageResponseTypeDef,
    ClientGetSavingsPlansCoverageTimePeriodTypeDef,
    ClientGetSavingsPlansPurchaseRecommendationResponseTypeDef,
    ClientGetSavingsPlansUtilizationDetailsFilterTypeDef,
    ClientGetSavingsPlansUtilizationDetailsResponseTypeDef,
    ClientGetSavingsPlansUtilizationDetailsTimePeriodTypeDef,
    ClientGetSavingsPlansUtilizationFilterTypeDef,
    ClientGetSavingsPlansUtilizationResponseTypeDef,
    ClientGetSavingsPlansUtilizationTimePeriodTypeDef,
    ClientGetTagsResponseTypeDef,
    ClientGetTagsTimePeriodTypeDef,
    ClientGetUsageForecastFilterTypeDef,
    ClientGetUsageForecastResponseTypeDef,
    ClientGetUsageForecastTimePeriodTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> None:
        """
        Check if an operation can be paginated.

        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you'd normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator("create_foo")``.

        :return: ``True`` if the operation can be paginated,
            ``False`` otherwise.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        Generate a presigned url given a client, its method, and arguments

        :type ClientMethod: string
        :param ClientMethod: The client method to presign for

        :type Params: dict
        :param Params: The parameters normally passed to
            ``ClientMethod``.

        :type ExpiresIn: int
        :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)

        :type HttpMethod: string
        :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method's model.

        :returns: The presigned url
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_cost_and_usage(
        self,
        TimePeriod: ClientGetCostAndUsageTimePeriodTypeDef,
        Granularity: str = None,
        Filter: ClientGetCostAndUsageFilterTypeDef = None,
        Metrics: List[str] = None,
        GroupBy: List[ClientGetCostAndUsageGroupByTypeDef] = None,
        NextPageToken: str = None,
    ) -> ClientGetCostAndUsageResponseTypeDef:
        """
        Retrieves cost and usage metrics for your account. You can specify which cost and usage-related
        metric, such as ``BlendedCosts`` or ``UsageQuantity`` , that you want the request to return. You
        can also filter and group your data by various dimensions, such as ``SERVICE`` or ``AZ`` , in a
        specific time range. For a complete list of valid dimensions, see the `GetDimensionValues
        <http://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetDimensionValues.html>`__
        operation. Master accounts in an organization in AWS Organizations have access to all member
        accounts.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ce-2017-10-25/GetCostAndUsage>`_

        **Request Syntax**
        ::

          response = client.get_cost_and_usage(
              TimePeriod={
                  'Start': 'string',
                  'End': 'string'
              },
              Granularity='DAILY'|'MONTHLY'|'HOURLY',
              Filter={
                  'Or': [
                      {'... recursive ...'},
                  ],
                  'And': [
                      {'... recursive ...'},
                  ],
                  'Not': {'... recursive ...'},
                  'Dimensions': {
                      'Key':
                      'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'
                      |'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'
                      |'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'
                      |'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'
                      |'RESERVATION_ID'|'RESOURCE_ID'|'RIGHTSIZING_TYPE'|'SAVINGS_PLANS_TYPE'
                      |'SAVINGS_PLAN_ARN'|'PAYMENT_OPTION',
                      'Values': [
                          'string',
                      ]
                  },
                  'Tags': {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
                  }
              },
              Metrics=[
                  'string',
              ],
              GroupBy=[
                  {
                      'Type': 'DIMENSION'|'TAG',
                      'Key': 'string'
                  },
              ],
              NextPageToken='string'
          )
        :type TimePeriod: dict
        :param TimePeriod: **[REQUIRED]**

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

        :type Granularity: string
        :param Granularity:

          Sets the AWS cost granularity to ``MONTHLY`` or ``DAILY`` , or ``HOURLY`` . If ``Granularity``
          isn't set, the response object doesn't include the ``Granularity`` , either ``MONTHLY`` or
          ``DAILY`` , or ``HOURLY`` .

        :type Filter: dict
        :param Filter:

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

        :type Metrics: list
        :param Metrics:

          Which metrics are returned in the query. For more information about blended and unblended rates,
          see `Why does the "blended" annotation appear on some line items in my bill?
          <https://aws.amazon.com/premiumsupport/knowledge-center/blended-rates-intro/>`__ .

          Valid values are ``AmortizedCost`` , ``BlendedCost`` , ``NetAmortizedCost`` ,
          ``NetUnblendedCost`` , ``NormalizedUsageAmount`` , ``UnblendedCost`` , and ``UsageQuantity`` .

          .. note::

            If you return the ``UsageQuantity`` metric, the service aggregates all usage numbers without
            taking into account the units. For example, if you aggregate ``usageQuantity`` across all of
            Amazon EC2, the results aren't meaningful because Amazon EC2 compute hours and data transfer
            are measured in different units (for example, hours vs. GB). To get more meaningful
            ``UsageQuantity`` metrics, filter by ``UsageType`` or ``UsageTypeGroups`` .

           ``Metrics`` is required for ``GetCostAndUsage`` requests.

          - *(string) --*

        :type GroupBy: list
        :param GroupBy:

          You can group AWS costs using up to two different groups, either dimensions, tag keys, or both.

          When you group by tag key, you get all tag values, including empty strings.

          Valid values are ``AZ`` , ``INSTANCE_TYPE`` , ``LEGAL_ENTITY_NAME`` , ``LINKED_ACCOUNT`` ,
          ``OPERATION`` , ``PLATFORM`` , ``PURCHASE_TYPE`` , ``SERVICE`` , ``TAGS`` , ``TENANCY`` ,
          ``RECORD_TYPE`` , and ``USAGE_TYPE`` .

          - *(dict) --*

            Represents a group when you specify a group by criteria or in the response to a query with a
            specific grouping.

            - **Type** *(string) --*

              The string that represents the type of group.

            - **Key** *(string) --*

              The string that represents a key for a specified group.

        :type NextPageToken: string
        :param NextPageToken:

          The token to retrieve the next set of results. AWS provides the token when the response from a
          previous call has more results than the maximum page size.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextPageToken': 'string',
                'GroupDefinitions': [
                    {
                        'Type': 'DIMENSION'|'TAG',
                        'Key': 'string'
                    },
                ],
                'ResultsByTime': [
                    {
                        'TimePeriod': {
                            'Start': 'string',
                            'End': 'string'
                        },
                        'Total': {
                            'string': {
                                'Amount': 'string',
                                'Unit': 'string'
                            }
                        },
                        'Groups': [
                            {
                                'Keys': [
                                    'string',
                                ],
                                'Metrics': {
                                    'string': {
                                        'Amount': 'string',
                                        'Unit': 'string'
                                    }
                                }
                            },
                        ],
                        'Estimated': True|False
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_cost_and_usage_with_resources(
        self,
        TimePeriod: ClientGetCostAndUsageWithResourcesTimePeriodTypeDef,
        Granularity: str = None,
        Filter: ClientGetCostAndUsageWithResourcesFilterTypeDef = None,
        Metrics: List[str] = None,
        GroupBy: List[ClientGetCostAndUsageWithResourcesGroupByTypeDef] = None,
        NextPageToken: str = None,
    ) -> ClientGetCostAndUsageWithResourcesResponseTypeDef:
        """
        Retrieves cost and usage metrics with resources for your account. You can specify which cost and
        usage-related metric, such as ``BlendedCosts`` or ``UsageQuantity`` , that you want the request to
        return. You can also filter and group your data by various dimensions, such as ``SERVICE`` or
        ``AZ`` , in a specific time range. For a complete list of valid dimensions, see the
        `GetDimensionValues
        <http://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetDimensionValues.html>`__
        operation. Master accounts in an organization in AWS Organizations have access to all member
        accounts. This API is currently available for the Amazon Elastic Compute Cloud – Compute service
        only.

        .. note::

          This is an opt-in only feature. You can enable this feature from the Cost Explorer Settings page.
          For information on how to access the Settings page, see `Controlling Access for Cost Explorer
          <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ce-access.html>`__ in the *AWS
          Billing and Cost Management User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ce-2017-10-25/GetCostAndUsageWithResources>`_

        **Request Syntax**
        ::

          response = client.get_cost_and_usage_with_resources(
              TimePeriod={
                  'Start': 'string',
                  'End': 'string'
              },
              Granularity='DAILY'|'MONTHLY'|'HOURLY',
              Filter={
                  'Or': [
                      {'... recursive ...'},
                  ],
                  'And': [
                      {'... recursive ...'},
                  ],
                  'Not': {'... recursive ...'},
                  'Dimensions': {
                      'Key':
                      'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'
                      |'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'
                      |'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'
                      |'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'
                      |'RESERVATION_ID'|'RESOURCE_ID'|'RIGHTSIZING_TYPE'|'SAVINGS_PLANS_TYPE'
                      |'SAVINGS_PLAN_ARN'|'PAYMENT_OPTION',
                      'Values': [
                          'string',
                      ]
                  },
                  'Tags': {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
                  }
              },
              Metrics=[
                  'string',
              ],
              GroupBy=[
                  {
                      'Type': 'DIMENSION'|'TAG',
                      'Key': 'string'
                  },
              ],
              NextPageToken='string'
          )
        :type TimePeriod: dict
        :param TimePeriod: **[REQUIRED]**

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

        :type Granularity: string
        :param Granularity:

          Sets the AWS cost granularity to ``MONTHLY`` , ``DAILY`` , or ``HOURLY`` . If ``Granularity``
          isn't set, the response object doesn't include the ``Granularity`` , ``MONTHLY`` , ``DAILY`` , or
          ``HOURLY`` .

        :type Filter: dict
        :param Filter:

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

        :type Metrics: list
        :param Metrics:

          Which metrics are returned in the query. For more information about blended and unblended rates,
          see `Why does the "blended" annotation appear on some line items in my bill?
          <https://aws.amazon.com/premiumsupport/knowledge-center/blended-rates-intro/>`__ .

          Valid values are ``AmortizedCost`` , ``BlendedCost`` , ``NetAmortizedCost`` ,
          ``NetUnblendedCost`` , ``NormalizedUsageAmount`` , ``UnblendedCost`` , and ``UsageQuantity`` .

          .. note::

            If you return the ``UsageQuantity`` metric, the service aggregates all usage numbers without
            taking the units into account. For example, if you aggregate ``usageQuantity`` across all of
            Amazon EC2, the results aren't meaningful because Amazon EC2 compute hours and data transfer
            are measured in different units (for example, hours vs. GB). To get more meaningful
            ``UsageQuantity`` metrics, filter by ``UsageType`` or ``UsageTypeGroups`` .

           ``Metrics`` is required for ``GetCostAndUsageWithResources`` requests.

          - *(string) --*

        :type GroupBy: list
        :param GroupBy:

          You can group Amazon Web Services costs using up to two different groups: either dimensions, tag
          keys, or both.

          - *(dict) --*

            Represents a group when you specify a group by criteria or in the response to a query with a
            specific grouping.

            - **Type** *(string) --*

              The string that represents the type of group.

            - **Key** *(string) --*

              The string that represents a key for a specified group.

        :type NextPageToken: string
        :param NextPageToken:

          The token to retrieve the next set of results. AWS provides the token when the response from a
          previous call has more results than the maximum page size.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextPageToken': 'string',
                'GroupDefinitions': [
                    {
                        'Type': 'DIMENSION'|'TAG',
                        'Key': 'string'
                    },
                ],
                'ResultsByTime': [
                    {
                        'TimePeriod': {
                            'Start': 'string',
                            'End': 'string'
                        },
                        'Total': {
                            'string': {
                                'Amount': 'string',
                                'Unit': 'string'
                            }
                        },
                        'Groups': [
                            {
                                'Keys': [
                                    'string',
                                ],
                                'Metrics': {
                                    'string': {
                                        'Amount': 'string',
                                        'Unit': 'string'
                                    }
                                }
                            },
                        ],
                        'Estimated': True|False
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_cost_forecast(
        self,
        TimePeriod: ClientGetCostForecastTimePeriodTypeDef,
        Metric: str,
        Granularity: str,
        Filter: ClientGetCostForecastFilterTypeDef = None,
        PredictionIntervalLevel: int = None,
    ) -> ClientGetCostForecastResponseTypeDef:
        """
        Retrieves a forecast for how much Amazon Web Services predicts that you will spend over the
        forecast time period that you select, based on your past costs.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ce-2017-10-25/GetCostForecast>`_

        **Request Syntax**
        ::

          response = client.get_cost_forecast(
              TimePeriod={
                  'Start': 'string',
                  'End': 'string'
              },
              Metric=
                  'BLENDED_COST'|'UNBLENDED_COST'|'AMORTIZED_COST'|'NET_UNBLENDED_COST'
                  |'NET_AMORTIZED_COST'|'USAGE_QUANTITY'|'NORMALIZED_USAGE_AMOUNT',
              Granularity='DAILY'|'MONTHLY'|'HOURLY',
              Filter={
                  'Or': [
                      {'... recursive ...'},
                  ],
                  'And': [
                      {'... recursive ...'},
                  ],
                  'Not': {'... recursive ...'},
                  'Dimensions': {
                      'Key':
                      'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'
                      |'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'
                      |'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'
                      |'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'
                      |'RESERVATION_ID'|'RESOURCE_ID'|'RIGHTSIZING_TYPE'|'SAVINGS_PLANS_TYPE'
                      |'SAVINGS_PLAN_ARN'|'PAYMENT_OPTION',
                      'Values': [
                          'string',
                      ]
                  },
                  'Tags': {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
                  }
              },
              PredictionIntervalLevel=123
          )
        :type TimePeriod: dict
        :param TimePeriod: **[REQUIRED]**

          The period of time that you want the forecast to cover.

          - **Start** *(string) --* **[REQUIRED]**

            The beginning of the time period that you want the usage and costs for. The start date is
            inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data
            starting at ``2017-01-01`` up to the end date.

          - **End** *(string) --* **[REQUIRED]**

            The end of the time period that you want the usage and costs for. The end date is exclusive.
            For example, if ``end`` is ``2017-05-01`` , AWS retrieves cost and usage data from the start
            date up to, but not including, ``2017-05-01`` .

        :type Metric: string
        :param Metric: **[REQUIRED]**

          Which metric Cost Explorer uses to create your forecast. For more information about blended and
          unblended rates, see `Why does the "blended" annotation appear on some line items in my bill?
          <https://aws.amazon.com/premiumsupport/knowledge-center/blended-rates-intro/>`__ .

          Valid values for a ``GetCostForecast`` call are the following:

          * AMORTIZED_COST

          * BLENDED_COST

          * NET_AMORTIZED_COST

          * NET_UNBLENDED_COST

          * UNBLENDED_COST

        :type Granularity: string
        :param Granularity: **[REQUIRED]**

          How granular you want the forecast to be. You can get 3 months of ``DAILY`` forecasts or 12
          months of ``MONTHLY`` forecasts.

          The ``GetCostForecast`` operation supports only ``DAILY`` and ``MONTHLY`` granularities.

        :type Filter: dict
        :param Filter:

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

        :type PredictionIntervalLevel: integer
        :param PredictionIntervalLevel:

          Cost Explorer always returns the mean forecast as a single point. You can request a prediction
          interval around the mean by specifying a confidence level. The higher the confidence level, the
          more confident Cost Explorer is about the actual value falling in the prediction interval. Higher
          confidence levels result in wider prediction intervals.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Total': {
                    'Amount': 'string',
                    'Unit': 'string'
                },
                'ForecastResultsByTime': [
                    {
                        'TimePeriod': {
                            'Start': 'string',
                            'End': 'string'
                        },
                        'MeanValue': 'string',
                        'PredictionIntervalLowerBound': 'string',
                        'PredictionIntervalUpperBound': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_dimension_values(
        self,
        TimePeriod: ClientGetDimensionValuesTimePeriodTypeDef,
        Dimension: str,
        SearchString: str = None,
        Context: str = None,
        NextPageToken: str = None,
    ) -> ClientGetDimensionValuesResponseTypeDef:
        """
        Retrieves all available filter values for a specified filter over a period of time. You can search
        the dimension values for an arbitrary string.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ce-2017-10-25/GetDimensionValues>`_

        **Request Syntax**
        ::

          response = client.get_dimension_values(
              SearchString='string',
              TimePeriod={
                  'Start': 'string',
                  'End': 'string'
              },
              Dimension=
                  'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'
                  |'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'
                  |'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'|'DATABASE_ENGINE'
                  |'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'|'RESERVATION_ID'|'RESOURCE_ID'
                  |'RIGHTSIZING_TYPE'|'SAVINGS_PLANS_TYPE'|'SAVINGS_PLAN_ARN'|'PAYMENT_OPTION',
              Context='COST_AND_USAGE'|'RESERVATIONS'|'SAVINGS_PLANS',
              NextPageToken='string'
          )
        :type SearchString: string
        :param SearchString:

          The value that you want to search the filter values for.

        :type TimePeriod: dict
        :param TimePeriod: **[REQUIRED]**

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

        :type Dimension: string
        :param Dimension: **[REQUIRED]**

          The name of the dimension. Each ``Dimension`` is available for a different ``Context`` . For more
          information, see ``Context`` .

        :type Context: string
        :param Context:

          The context for the call to ``GetDimensionValues`` . This can be ``RESERVATIONS`` or
          ``COST_AND_USAGE`` . The default value is ``COST_AND_USAGE`` . If the context is set to
          ``RESERVATIONS`` , the resulting dimension values can be used in the
          ``GetReservationUtilization`` operation. If the context is set to ``COST_AND_USAGE`` , the
          resulting dimension values can be used in the ``GetCostAndUsage`` operation.

          If you set the context to ``COST_AND_USAGE`` , you can use the following dimensions for searching:

          * AZ - The Availability Zone. An example is ``us-east-1a`` .

          * DATABASE_ENGINE - The Amazon Relational Database Service database. Examples are Aurora or MySQL.

          * INSTANCE_TYPE - The type of Amazon EC2 instance. An example is ``m4.xlarge`` .

          * LEGAL_ENTITY_NAME - The name of the organization that sells you AWS services, such as Amazon
          Web Services.

          * LINKED_ACCOUNT - The description in the attribute map that includes the full name of the member
          account. The value field contains the AWS ID of the member account.

          * OPERATING_SYSTEM - The operating system. Examples are Windows or Linux.

          * OPERATION - The action performed. Examples include ``RunInstance`` and ``CreateBucket`` .

          * PLATFORM - The Amazon EC2 operating system. Examples are Windows or Linux.

          * PURCHASE_TYPE - The reservation type of the purchase to which this usage is related. Examples
          include On-Demand Instances and Standard Reserved Instances.

          * SERVICE - The AWS service such as Amazon DynamoDB.

          * USAGE_TYPE - The type of usage. An example is DataTransfer-In-Bytes. The response for the
          ``GetDimensionValues`` operation includes a unit attribute. Examples include GB and Hrs.

          * USAGE_TYPE_GROUP - The grouping of common usage types. An example is Amazon EC2: CloudWatch –
          Alarms. The response for this operation includes a unit attribute.

          * RECORD_TYPE - The different types of charges such as RI fees, usage costs, tax refunds, and
          credits.

          * RESOURCE_ID - The unique identifier of the resource. ResourceId is an opt-in feature only
          available for last 14 days for EC2-Compute Service.

          If you set the context to ``RESERVATIONS`` , you can use the following dimensions for searching:

          * AZ - The Availability Zone. An example is ``us-east-1a`` .

          * CACHE_ENGINE - The Amazon ElastiCache operating system. Examples are Windows or Linux.

          * DEPLOYMENT_OPTION - The scope of Amazon Relational Database Service deployments. Valid values
          are ``SingleAZ`` and ``MultiAZ`` .

          * INSTANCE_TYPE - The type of Amazon EC2 instance. An example is ``m4.xlarge`` .

          * LINKED_ACCOUNT - The description in the attribute map that includes the full name of the member
          account. The value field contains the AWS ID of the member account.

          * PLATFORM - The Amazon EC2 operating system. Examples are Windows or Linux.

          * REGION - The AWS Region.

          * SCOPE (Utilization only) - The scope of a Reserved Instance (RI). Values are regional or a
          single Availability Zone.

          * TAG (Coverage only) - The tags that are associated with a Reserved Instance (RI).

          * TENANCY - The tenancy of a resource. Examples are shared or dedicated.

          If you set the context to ``SAVINGS_PLANS`` , you can use the following dimensions for searching:

          * SAVINGS_PLANS_TYPE - Type of Savings Plans (EC2 Instance or Compute)

          * PAYMENT_OPTION - Payment option for the given Savings Plans (for example, All Upfront)

          * REGION - The AWS Region.

          * INSTANCE_TYPE_FAMILY - The family of instances (For example, ``m5`` )

          * LINKED_ACCOUNT - The description in the attribute map that includes the full name of the member
          account. The value field contains the AWS ID of the member account.

          * SAVINGS_PLAN_ARN - The unique identifier for your Savings Plan

        :type NextPageToken: string
        :param NextPageToken:

          The token to retrieve the next set of results. AWS provides the token when the response from a
          previous call has more results than the maximum page size.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DimensionValues': [
                    {
                        'Value': 'string',
                        'Attributes': {
                            'string': 'string'
                        }
                    },
                ],
                'ReturnSize': 123,
                'TotalSize': 123,
                'NextPageToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_reservation_coverage(
        self,
        TimePeriod: ClientGetReservationCoverageTimePeriodTypeDef,
        GroupBy: List[ClientGetReservationCoverageGroupByTypeDef] = None,
        Granularity: str = None,
        Filter: ClientGetReservationCoverageFilterTypeDef = None,
        Metrics: List[str] = None,
        NextPageToken: str = None,
    ) -> ClientGetReservationCoverageResponseTypeDef:
        """
        Retrieves the reservation coverage for your account. This enables you to see how much of your
        Amazon Elastic Compute Cloud, Amazon ElastiCache, Amazon Relational Database Service, or Amazon
        Redshift usage is covered by a reservation. An organization's master account can see the coverage
        of the associated member accounts. For any time period, you can filter data about reservation usage
        by the following dimensions:

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

        To determine valid values for a dimension, use the ``GetDimensionValues`` operation.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ce-2017-10-25/GetReservationCoverage>`_

        **Request Syntax**
        ::

          response = client.get_reservation_coverage(
              TimePeriod={
                  'Start': 'string',
                  'End': 'string'
              },
              GroupBy=[
                  {
                      'Type': 'DIMENSION'|'TAG',
                      'Key': 'string'
                  },
              ],
              Granularity='DAILY'|'MONTHLY'|'HOURLY',
              Filter={
                  'Or': [
                      {'... recursive ...'},
                  ],
                  'And': [
                      {'... recursive ...'},
                  ],
                  'Not': {'... recursive ...'},
                  'Dimensions': {
                      'Key':
                      'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'
                      |'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'
                      |'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'
                      |'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'
                      |'RESERVATION_ID'|'RESOURCE_ID'|'RIGHTSIZING_TYPE'|'SAVINGS_PLANS_TYPE'
                      |'SAVINGS_PLAN_ARN'|'PAYMENT_OPTION',
                      'Values': [
                          'string',
                      ]
                  },
                  'Tags': {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
                  }
              },
              Metrics=[
                  'string',
              ],
              NextPageToken='string'
          )
        :type TimePeriod: dict
        :param TimePeriod: **[REQUIRED]**

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

        :type GroupBy: list
        :param GroupBy:

          You can group the data by the following attributes:

          * AZ

          * CACHE_ENGINE

          * DATABASE_ENGINE

          * DEPLOYMENT_OPTION

          * INSTANCE_TYPE

          * LINKED_ACCOUNT

          * OPERATING_SYSTEM

          * PLATFORM

          * REGION

          * TENANCY

          - *(dict) --*

            Represents a group when you specify a group by criteria or in the response to a query with a
            specific grouping.

            - **Type** *(string) --*

              The string that represents the type of group.

            - **Key** *(string) --*

              The string that represents a key for a specified group.

        :type Granularity: string
        :param Granularity:

          The granularity of the AWS cost data for the reservation. Valid values are ``MONTHLY`` and
          ``DAILY`` .

          If ``GroupBy`` is set, ``Granularity`` can't be set. If ``Granularity`` isn't set, the response
          object doesn't include ``Granularity`` , either ``MONTHLY`` or ``DAILY`` .

          The ``GetReservationCoverage`` operation supports only ``DAILY`` and ``MONTHLY`` granularities.

        :type Filter: dict
        :param Filter:

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

        :type Metrics: list
        :param Metrics:

          The measurement that you want your reservation coverage reported in.

          Valid values are ``Hour`` , ``Unit`` , and ``Cost`` . You can use multiple values in a request.

          - *(string) --*

        :type NextPageToken: string
        :param NextPageToken:

          The token to retrieve the next set of results. AWS provides the token when the response from a
          previous call has more results than the maximum page size.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CoveragesByTime': [
                    {
                        'TimePeriod': {
                            'Start': 'string',
                            'End': 'string'
                        },
                        'Groups': [
                            {
                                'Attributes': {
                                    'string': 'string'
                                },
                                'Coverage': {
                                    'CoverageHours': {
                                        'OnDemandHours': 'string',
                                        'ReservedHours': 'string',
                                        'TotalRunningHours': 'string',
                                        'CoverageHoursPercentage': 'string'
                                    },
                                    'CoverageNormalizedUnits': {
                                        'OnDemandNormalizedUnits': 'string',
                                        'ReservedNormalizedUnits': 'string',
                                        'TotalRunningNormalizedUnits': 'string',
                                        'CoverageNormalizedUnitsPercentage': 'string'
                                    },
                                    'CoverageCost': {
                                        'OnDemandCost': 'string'
                                    }
                                }
                            },
                        ],
                        'Total': {
                            'CoverageHours': {
                                'OnDemandHours': 'string',
                                'ReservedHours': 'string',
                                'TotalRunningHours': 'string',
                                'CoverageHoursPercentage': 'string'
                            },
                            'CoverageNormalizedUnits': {
                                'OnDemandNormalizedUnits': 'string',
                                'ReservedNormalizedUnits': 'string',
                                'TotalRunningNormalizedUnits': 'string',
                                'CoverageNormalizedUnitsPercentage': 'string'
                            },
                            'CoverageCost': {
                                'OnDemandCost': 'string'
                            }
                        }
                    },
                ],
                'Total': {
                    'CoverageHours': {
                        'OnDemandHours': 'string',
                        'ReservedHours': 'string',
                        'TotalRunningHours': 'string',
                        'CoverageHoursPercentage': 'string'
                    },
                    'CoverageNormalizedUnits': {
                        'OnDemandNormalizedUnits': 'string',
                        'ReservedNormalizedUnits': 'string',
                        'TotalRunningNormalizedUnits': 'string',
                        'CoverageNormalizedUnitsPercentage': 'string'
                    },
                    'CoverageCost': {
                        'OnDemandCost': 'string'
                    }
                },
                'NextPageToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_reservation_purchase_recommendation(
        self,
        Service: str,
        AccountId: str = None,
        AccountScope: str = None,
        LookbackPeriodInDays: str = None,
        TermInYears: str = None,
        PaymentOption: str = None,
        ServiceSpecification: ClientGetReservationPurchaseRecommendationServiceSpecificationTypeDef = None,
        PageSize: int = None,
        NextPageToken: str = None,
    ) -> ClientGetReservationPurchaseRecommendationResponseTypeDef:
        """
        Gets recommendations for which reservations to purchase. These recommendations could help you
        reduce your costs. Reservations provide a discounted hourly rate (up to 75%) compared to On-Demand
        pricing.

        AWS generates your recommendations by identifying your On-Demand usage during a specific time
        period and collecting your usage into categories that are eligible for a reservation. After AWS has
        these categories, it simulates every combination of reservations in each category of usage to
        identify the best number of each type of RI to purchase to maximize your estimated savings.

        For example, AWS automatically aggregates your Amazon EC2 Linux, shared tenancy, and c4 family
        usage in the US West (Oregon) Region and recommends that you buy size-flexible regional
        reservations to apply to the c4 family usage. AWS recommends the smallest size instance in an
        instance family. This makes it easier to purchase a size-flexible RI. AWS also shows the equal
        number of normalized units so that you can purchase any instance size that you want. For this
        example, your RI recommendation would be for ``c4.large`` because that is the smallest size
        instance in the c4 instance family.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ce-2017-10-25/GetReservationPurchaseRecommendation>`_

        **Request Syntax**
        ::

          response = client.get_reservation_purchase_recommendation(
              AccountId='string',
              Service='string',
              AccountScope='PAYER'|'LINKED',
              LookbackPeriodInDays='SEVEN_DAYS'|'THIRTY_DAYS'|'SIXTY_DAYS',
              TermInYears='ONE_YEAR'|'THREE_YEARS',
              PaymentOption=
                  'NO_UPFRONT'|'PARTIAL_UPFRONT'|'ALL_UPFRONT'|'LIGHT_UTILIZATION'|'MEDIUM_UTILIZATION'
                  |'HEAVY_UTILIZATION',
              ServiceSpecification={
                  'EC2Specification': {
                      'OfferingClass': 'STANDARD'|'CONVERTIBLE'
                  }
              },
              PageSize=123,
              NextPageToken='string'
          )
        :type AccountId: string
        :param AccountId:

          The account ID that is associated with the recommendation.

        :type Service: string
        :param Service: **[REQUIRED]**

          The specific service that you want recommendations for.

        :type AccountScope: string
        :param AccountScope:

          The account scope that you want recommendations for. ``PAYER`` means that AWS includes the master
          account and any member accounts when it calculates its recommendations. ``LINKED`` means that AWS
          includes only member accounts when it calculates its recommendations.

          Valid values are ``PAYER`` and ``LINKED`` .

        :type LookbackPeriodInDays: string
        :param LookbackPeriodInDays:

          The number of previous days that you want AWS to consider when it calculates your recommendations.

        :type TermInYears: string
        :param TermInYears:

          The reservation term that you want recommendations for.

        :type PaymentOption: string
        :param PaymentOption:

          The reservation purchase option that you want recommendations for.

        :type ServiceSpecification: dict
        :param ServiceSpecification:

          The hardware specifications for the service instances that you want recommendations for, such as
          standard or convertible Amazon EC2 instances.

          - **EC2Specification** *(dict) --*

            The Amazon EC2 hardware specifications that you want AWS to provide recommendations for.

            - **OfferingClass** *(string) --*

              Whether you want a recommendation for standard or convertible reservations.

        :type PageSize: integer
        :param PageSize:

          The number of recommendations that you want returned in a single response object.

        :type NextPageToken: string
        :param NextPageToken:

          The pagination token that indicates the next set of results that you want to retrieve.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Metadata': {
                    'RecommendationId': 'string',
                    'GenerationTimestamp': 'string'
                },
                'Recommendations': [
                    {
                        'AccountScope': 'PAYER'|'LINKED',
                        'LookbackPeriodInDays': 'SEVEN_DAYS'|'THIRTY_DAYS'|'SIXTY_DAYS',
                        'TermInYears': 'ONE_YEAR'|'THREE_YEARS',
                        'PaymentOption':
                        'NO_UPFRONT'|'PARTIAL_UPFRONT'|'ALL_UPFRONT'|'LIGHT_UTILIZATION'
                        |'MEDIUM_UTILIZATION'|'HEAVY_UTILIZATION',
                        'ServiceSpecification': {
                            'EC2Specification': {
                                'OfferingClass': 'STANDARD'|'CONVERTIBLE'
                            }
                        },
                        'RecommendationDetails': [
                            {
                                'AccountId': 'string',
                                'InstanceDetails': {
                                    'EC2InstanceDetails': {
                                        'Family': 'string',
                                        'InstanceType': 'string',
                                        'Region': 'string',
                                        'AvailabilityZone': 'string',
                                        'Platform': 'string',
                                        'Tenancy': 'string',
                                        'CurrentGeneration': True|False,
                                        'SizeFlexEligible': True|False
                                    },
                                    'RDSInstanceDetails': {
                                        'Family': 'string',
                                        'InstanceType': 'string',
                                        'Region': 'string',
                                        'DatabaseEngine': 'string',
                                        'DatabaseEdition': 'string',
                                        'DeploymentOption': 'string',
                                        'LicenseModel': 'string',
                                        'CurrentGeneration': True|False,
                                        'SizeFlexEligible': True|False
                                    },
                                    'RedshiftInstanceDetails': {
                                        'Family': 'string',
                                        'NodeType': 'string',
                                        'Region': 'string',
                                        'CurrentGeneration': True|False,
                                        'SizeFlexEligible': True|False
                                    },
                                    'ElastiCacheInstanceDetails': {
                                        'Family': 'string',
                                        'NodeType': 'string',
                                        'Region': 'string',
                                        'ProductDescription': 'string',
                                        'CurrentGeneration': True|False,
                                        'SizeFlexEligible': True|False
                                    },
                                    'ESInstanceDetails': {
                                        'InstanceClass': 'string',
                                        'InstanceSize': 'string',
                                        'Region': 'string',
                                        'CurrentGeneration': True|False,
                                        'SizeFlexEligible': True|False
                                    }
                                },
                                'RecommendedNumberOfInstancesToPurchase': 'string',
                                'RecommendedNormalizedUnitsToPurchase': 'string',
                                'MinimumNumberOfInstancesUsedPerHour': 'string',
                                'MinimumNormalizedUnitsUsedPerHour': 'string',
                                'MaximumNumberOfInstancesUsedPerHour': 'string',
                                'MaximumNormalizedUnitsUsedPerHour': 'string',
                                'AverageNumberOfInstancesUsedPerHour': 'string',
                                'AverageNormalizedUnitsUsedPerHour': 'string',
                                'AverageUtilization': 'string',
                                'EstimatedBreakEvenInMonths': 'string',
                                'CurrencyCode': 'string',
                                'EstimatedMonthlySavingsAmount': 'string',
                                'EstimatedMonthlySavingsPercentage': 'string',
                                'EstimatedMonthlyOnDemandCost': 'string',
                                'EstimatedReservationCostForLookbackPeriod': 'string',
                                'UpfrontCost': 'string',
                                'RecurringStandardMonthlyCost': 'string'
                            },
                        ],
                        'RecommendationSummary': {
                            'TotalEstimatedMonthlySavingsAmount': 'string',
                            'TotalEstimatedMonthlySavingsPercentage': 'string',
                            'CurrencyCode': 'string'
                        }
                    },
                ],
                'NextPageToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_reservation_utilization(
        self,
        TimePeriod: ClientGetReservationUtilizationTimePeriodTypeDef,
        GroupBy: List[ClientGetReservationUtilizationGroupByTypeDef] = None,
        Granularity: str = None,
        Filter: ClientGetReservationUtilizationFilterTypeDef = None,
        NextPageToken: str = None,
    ) -> ClientGetReservationUtilizationResponseTypeDef:
        """
        Retrieves the reservation utilization for your account. Master accounts in an organization have
        access to member accounts. You can filter data by dimensions in a time period. You can use
        ``GetDimensionValues`` to determine the possible dimension values. Currently, you can group only by
        ``SUBSCRIPTION_ID`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ce-2017-10-25/GetReservationUtilization>`_

        **Request Syntax**
        ::

          response = client.get_reservation_utilization(
              TimePeriod={
                  'Start': 'string',
                  'End': 'string'
              },
              GroupBy=[
                  {
                      'Type': 'DIMENSION'|'TAG',
                      'Key': 'string'
                  },
              ],
              Granularity='DAILY'|'MONTHLY'|'HOURLY',
              Filter={
                  'Or': [
                      {'... recursive ...'},
                  ],
                  'And': [
                      {'... recursive ...'},
                  ],
                  'Not': {'... recursive ...'},
                  'Dimensions': {
                      'Key':
                      'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'
                      |'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'
                      |'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'
                      |'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'
                      |'RESERVATION_ID'|'RESOURCE_ID'|'RIGHTSIZING_TYPE'|'SAVINGS_PLANS_TYPE'
                      |'SAVINGS_PLAN_ARN'|'PAYMENT_OPTION',
                      'Values': [
                          'string',
                      ]
                  },
                  'Tags': {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
                  }
              },
              NextPageToken='string'
          )
        :type TimePeriod: dict
        :param TimePeriod: **[REQUIRED]**

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

        :type GroupBy: list
        :param GroupBy:

          Groups only by ``SUBSCRIPTION_ID`` . Metadata is included.

          - *(dict) --*

            Represents a group when you specify a group by criteria or in the response to a query with a
            specific grouping.

            - **Type** *(string) --*

              The string that represents the type of group.

            - **Key** *(string) --*

              The string that represents a key for a specified group.

        :type Granularity: string
        :param Granularity:

          If ``GroupBy`` is set, ``Granularity`` can't be set. If ``Granularity`` isn't set, the response
          object doesn't include ``Granularity`` , either ``MONTHLY`` or ``DAILY`` . If both ``GroupBy``
          and ``Granularity`` aren't set, ``GetReservationUtilization`` defaults to ``DAILY`` .

          The ``GetReservationUtilization`` operation supports only ``DAILY`` and ``MONTHLY`` granularities.

        :type Filter: dict
        :param Filter:

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

        :type NextPageToken: string
        :param NextPageToken:

          The token to retrieve the next set of results. AWS provides the token when the response from a
          previous call has more results than the maximum page size.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UtilizationsByTime': [
                    {
                        'TimePeriod': {
                            'Start': 'string',
                            'End': 'string'
                        },
                        'Groups': [
                            {
                                'Key': 'string',
                                'Value': 'string',
                                'Attributes': {
                                    'string': 'string'
                                },
                                'Utilization': {
                                    'UtilizationPercentage': 'string',
                                    'UtilizationPercentageInUnits': 'string',
                                    'PurchasedHours': 'string',
                                    'PurchasedUnits': 'string',
                                    'TotalActualHours': 'string',
                                    'TotalActualUnits': 'string',
                                    'UnusedHours': 'string',
                                    'UnusedUnits': 'string',
                                    'OnDemandCostOfRIHoursUsed': 'string',
                                    'NetRISavings': 'string',
                                    'TotalPotentialRISavings': 'string',
                                    'AmortizedUpfrontFee': 'string',
                                    'AmortizedRecurringFee': 'string',
                                    'TotalAmortizedFee': 'string'
                                }
                            },
                        ],
                        'Total': {
                            'UtilizationPercentage': 'string',
                            'UtilizationPercentageInUnits': 'string',
                            'PurchasedHours': 'string',
                            'PurchasedUnits': 'string',
                            'TotalActualHours': 'string',
                            'TotalActualUnits': 'string',
                            'UnusedHours': 'string',
                            'UnusedUnits': 'string',
                            'OnDemandCostOfRIHoursUsed': 'string',
                            'NetRISavings': 'string',
                            'TotalPotentialRISavings': 'string',
                            'AmortizedUpfrontFee': 'string',
                            'AmortizedRecurringFee': 'string',
                            'TotalAmortizedFee': 'string'
                        }
                    },
                ],
                'Total': {
                    'UtilizationPercentage': 'string',
                    'UtilizationPercentageInUnits': 'string',
                    'PurchasedHours': 'string',
                    'PurchasedUnits': 'string',
                    'TotalActualHours': 'string',
                    'TotalActualUnits': 'string',
                    'UnusedHours': 'string',
                    'UnusedUnits': 'string',
                    'OnDemandCostOfRIHoursUsed': 'string',
                    'NetRISavings': 'string',
                    'TotalPotentialRISavings': 'string',
                    'AmortizedUpfrontFee': 'string',
                    'AmortizedRecurringFee': 'string',
                    'TotalAmortizedFee': 'string'
                },
                'NextPageToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_rightsizing_recommendation(
        self,
        Service: str,
        Filter: ClientGetRightsizingRecommendationFilterTypeDef = None,
        PageSize: int = None,
        NextPageToken: str = None,
    ) -> ClientGetRightsizingRecommendationResponseTypeDef:
        """
        Creates recommendations that helps you save cost by identifying idle and underutilized Amazon EC2
        instances.

        Recommendations are generated to either downsize or terminate instances, along with providing
        savings detail and metrics. For details on calculation and function, see `Optimizing Your Cost with
        Rightsizing Recommendations
        <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ce-what-is.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ce-2017-10-25/GetRightsizingRecommendation>`_

        **Request Syntax**
        ::

          response = client.get_rightsizing_recommendation(
              Filter={
                  'Or': [
                      {'... recursive ...'},
                  ],
                  'And': [
                      {'... recursive ...'},
                  ],
                  'Not': {'... recursive ...'},
                  'Dimensions': {
                      'Key':
                      'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'
                      |'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'
                      |'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'
                      |'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'
                      |'RESERVATION_ID'|'RESOURCE_ID'|'RIGHTSIZING_TYPE'|'SAVINGS_PLANS_TYPE'
                      |'SAVINGS_PLAN_ARN'|'PAYMENT_OPTION',
                      'Values': [
                          'string',
                      ]
                  },
                  'Tags': {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
                  }
              },
              Service='string',
              PageSize=123,
              NextPageToken='string'
          )
        :type Filter: dict
        :param Filter:

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

        :type Service: string
        :param Service: **[REQUIRED]**

          The specific service that you want recommendations for. The only valid value for
          ``GetRightsizingRecommendation`` is "``AmazonEC2`` ".

        :type PageSize: integer
        :param PageSize:

          The number of recommendations that you want returned in a single response object.

        :type NextPageToken: string
        :param NextPageToken:

          The pagination token that indicates the next set of results that you want to retrieve.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Metadata': {
                    'RecommendationId': 'string',
                    'GenerationTimestamp': 'string',
                    'LookbackPeriodInDays': 'SEVEN_DAYS'|'THIRTY_DAYS'|'SIXTY_DAYS'
                },
                'Summary': {
                    'TotalRecommendationCount': 'string',
                    'EstimatedTotalMonthlySavingsAmount': 'string',
                    'SavingsCurrencyCode': 'string',
                    'SavingsPercentage': 'string'
                },
                'RightsizingRecommendations': [
                    {
                        'AccountId': 'string',
                        'CurrentInstance': {
                            'ResourceId': 'string',
                            'Tags': [
                                {
                                    'Key': 'string',
                                    'Values': [
                                        'string',
                                    ]
                                },
                            ],
                            'ResourceDetails': {
                                'EC2ResourceDetails': {
                                    'HourlyOnDemandRate': 'string',
                                    'InstanceType': 'string',
                                    'Platform': 'string',
                                    'Region': 'string',
                                    'Sku': 'string',
                                    'Memory': 'string',
                                    'NetworkPerformance': 'string',
                                    'Storage': 'string',
                                    'Vcpu': 'string'
                                }
                            },
                            'ResourceUtilization': {
                                'EC2ResourceUtilization': {
                                    'MaxCpuUtilizationPercentage': 'string',
                                    'MaxMemoryUtilizationPercentage': 'string',
                                    'MaxStorageUtilizationPercentage': 'string'
                                }
                            },
                            'ReservationCoveredHoursInLookbackPeriod': 'string',
                            'SavingsPlansCoveredHoursInLookbackPeriod': 'string',
                            'OnDemandHoursInLookbackPeriod': 'string',
                            'TotalRunningHoursInLookbackPeriod': 'string',
                            'MonthlyCost': 'string',
                            'CurrencyCode': 'string'
                        },
                        'RightsizingType': 'TERMINATE'|'MODIFY',
                        'ModifyRecommendationDetail': {
                            'TargetInstances': [
                                {
                                    'EstimatedMonthlyCost': 'string',
                                    'EstimatedMonthlySavings': 'string',
                                    'CurrencyCode': 'string',
                                    'DefaultTargetInstance': True|False,
                                    'ResourceDetails': {
                                        'EC2ResourceDetails': {
                                            'HourlyOnDemandRate': 'string',
                                            'InstanceType': 'string',
                                            'Platform': 'string',
                                            'Region': 'string',
                                            'Sku': 'string',
                                            'Memory': 'string',
                                            'NetworkPerformance': 'string',
                                            'Storage': 'string',
                                            'Vcpu': 'string'
                                        }
                                    },
                                    'ExpectedResourceUtilization': {
                                        'EC2ResourceUtilization': {
                                            'MaxCpuUtilizationPercentage': 'string',
                                            'MaxMemoryUtilizationPercentage': 'string',
                                            'MaxStorageUtilizationPercentage': 'string'
                                        }
                                    }
                                },
                            ]
                        },
                        'TerminateRecommendationDetail': {
                            'EstimatedMonthlySavings': 'string',
                            'CurrencyCode': 'string'
                        }
                    },
                ],
                'NextPageToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_savings_plans_coverage(
        self,
        TimePeriod: ClientGetSavingsPlansCoverageTimePeriodTypeDef,
        GroupBy: List[ClientGetSavingsPlansCoverageGroupByTypeDef] = None,
        Granularity: str = None,
        Filter: ClientGetSavingsPlansCoverageFilterTypeDef = None,
        Metrics: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientGetSavingsPlansCoverageResponseTypeDef:
        """
        Retrieves the Savings Plans covered for your account. This enables you to see how much of your cost
        is covered by a Savings Plan. An organization’s master account can see the coverage of the
        associated member accounts. For any time period, you can filter data for Savings Plans usage with
        the following dimensions:

        * ``LINKED_ACCOUNT``

        * ``REGION``

        * ``SERVICE``

        * ``INSTANCE_FAMILY``

        To determine valid values for a dimension, use the ``GetDimensionValues`` operation.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ce-2017-10-25/GetSavingsPlansCoverage>`_

        **Request Syntax**
        ::

          response = client.get_savings_plans_coverage(
              TimePeriod={
                  'Start': 'string',
                  'End': 'string'
              },
              GroupBy=[
                  {
                      'Type': 'DIMENSION'|'TAG',
                      'Key': 'string'
                  },
              ],
              Granularity='DAILY'|'MONTHLY'|'HOURLY',
              Filter={
                  'Or': [
                      {'... recursive ...'},
                  ],
                  'And': [
                      {'... recursive ...'},
                  ],
                  'Not': {'... recursive ...'},
                  'Dimensions': {
                      'Key':
                      'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'
                      |'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'
                      |'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'
                      |'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'
                      |'RESERVATION_ID'|'RESOURCE_ID'|'RIGHTSIZING_TYPE'|'SAVINGS_PLANS_TYPE'
                      |'SAVINGS_PLAN_ARN'|'PAYMENT_OPTION',
                      'Values': [
                          'string',
                      ]
                  },
                  'Tags': {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
                  }
              },
              Metrics=[
                  'string',
              ],
              NextToken='string',
              MaxResults=123
          )
        :type TimePeriod: dict
        :param TimePeriod: **[REQUIRED]**

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

        :type GroupBy: list
        :param GroupBy:

          You can group the data using the attributes ``INSTANCE_FAMILY`` , ``REGION`` , or ``SERVICE`` .

          - *(dict) --*

            Represents a group when you specify a group by criteria or in the response to a query with a
            specific grouping.

            - **Type** *(string) --*

              The string that represents the type of group.

            - **Key** *(string) --*

              The string that represents a key for a specified group.

        :type Granularity: string
        :param Granularity:

          The granularity of the Amazon Web Services cost data for your Savings Plans. ``Granularity``
          can't be set if ``GroupBy`` is set.

          The ``GetSavingsPlansCoverage`` operation supports only ``DAILY`` and ``MONTHLY`` granularities.

        :type Filter: dict
        :param Filter:

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

        :type Metrics: list
        :param Metrics:

          The measurement that you want your Savings Plans coverage reported in. The only valid value is
          ``SpendCoveredBySavingsPlans`` .

          - *(string) --*

        :type NextToken: string
        :param NextToken:

          The token to retrieve the next set of results. Amazon Web Services provides the token when the
          response from a previous call has more results than the maximum page size.

        :type MaxResults: integer
        :param MaxResults:

          The number of items to be returned in a response. The default is ``20`` , with a minimum value of
          ``1`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'SavingsPlansCoverages': [
                    {
                        'Attributes': {
                            'string': 'string'
                        },
                        'Coverage': {
                            'SpendCoveredBySavingsPlans': 'string',
                            'OnDemandCost': 'string',
                            'TotalCost': 'string',
                            'CoveragePercentage': 'string'
                        },
                        'TimePeriod': {
                            'Start': 'string',
                            'End': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_savings_plans_purchase_recommendation(
        self,
        SavingsPlansType: str,
        TermInYears: str,
        PaymentOption: str,
        LookbackPeriodInDays: str,
        NextPageToken: str = None,
        PageSize: int = None,
    ) -> ClientGetSavingsPlansPurchaseRecommendationResponseTypeDef:
        """
        Retrieves your request parameters, Savings Plan Recommendations Summary and Details.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ce-2017-10-25/GetSavingsPlansPurchaseRecommendation>`_

        **Request Syntax**
        ::

          response = client.get_savings_plans_purchase_recommendation(
              SavingsPlansType='COMPUTE_SP'|'EC2_INSTANCE_SP',
              TermInYears='ONE_YEAR'|'THREE_YEARS',
              PaymentOption=
                  'NO_UPFRONT'|'PARTIAL_UPFRONT'|'ALL_UPFRONT'|'LIGHT_UTILIZATION'|'MEDIUM_UTILIZATION'
                  |'HEAVY_UTILIZATION',
              NextPageToken='string',
              PageSize=123,
              LookbackPeriodInDays='SEVEN_DAYS'|'THIRTY_DAYS'|'SIXTY_DAYS'
          )
        :type SavingsPlansType: string
        :param SavingsPlansType: **[REQUIRED]**

          The Savings Plans recommendation type requested.

        :type TermInYears: string
        :param TermInYears: **[REQUIRED]**

          The savings plan recommendation term used to generated these recommendations.

        :type PaymentOption: string
        :param PaymentOption: **[REQUIRED]**

          The payment option used to generate these recommendations.

        :type NextPageToken: string
        :param NextPageToken:

          The token to retrieve the next set of results. Amazon Web Services provides the token when the
          response from a previous call has more results than the maximum page size.

        :type PageSize: integer
        :param PageSize:

          The number of recommendations that you want returned in a single response object.

        :type LookbackPeriodInDays: string
        :param LookbackPeriodInDays: **[REQUIRED]**

          The lookback period used to generate the recommendation.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Metadata': {
                    'RecommendationId': 'string',
                    'GenerationTimestamp': 'string'
                },
                'SavingsPlansPurchaseRecommendation': {
                    'SavingsPlansType': 'COMPUTE_SP'|'EC2_INSTANCE_SP',
                    'TermInYears': 'ONE_YEAR'|'THREE_YEARS',
                    'PaymentOption':
                    'NO_UPFRONT'|'PARTIAL_UPFRONT'|'ALL_UPFRONT'|'LIGHT_UTILIZATION'|'MEDIUM_UTILIZATION'
                    |'HEAVY_UTILIZATION',
                    'LookbackPeriodInDays': 'SEVEN_DAYS'|'THIRTY_DAYS'|'SIXTY_DAYS',
                    'SavingsPlansPurchaseRecommendationDetails': [
                        {
                            'SavingsPlansDetails': {
                                'Region': 'string',
                                'InstanceFamily': 'string',
                                'OfferingId': 'string'
                            },
                            'AccountId': 'string',
                            'UpfrontCost': 'string',
                            'EstimatedROI': 'string',
                            'CurrencyCode': 'string',
                            'EstimatedSPCost': 'string',
                            'EstimatedOnDemandCost': 'string',
                            'EstimatedOnDemandCostWithCurrentCommitment': 'string',
                            'EstimatedSavingsAmount': 'string',
                            'EstimatedSavingsPercentage': 'string',
                            'HourlyCommitmentToPurchase': 'string',
                            'EstimatedAverageUtilization': 'string',
                            'EstimatedMonthlySavingsAmount': 'string',
                            'CurrentMinimumHourlyOnDemandSpend': 'string',
                            'CurrentMaximumHourlyOnDemandSpend': 'string',
                            'CurrentAverageHourlyOnDemandSpend': 'string'
                        },
                    ],
                    'SavingsPlansPurchaseRecommendationSummary': {
                        'EstimatedROI': 'string',
                        'CurrencyCode': 'string',
                        'EstimatedTotalCost': 'string',
                        'CurrentOnDemandSpend': 'string',
                        'EstimatedSavingsAmount': 'string',
                        'TotalRecommendationCount': 'string',
                        'DailyCommitmentToPurchase': 'string',
                        'HourlyCommitmentToPurchase': 'string',
                        'EstimatedSavingsPercentage': 'string',
                        'EstimatedMonthlySavingsAmount': 'string',
                        'EstimatedOnDemandCostWithCurrentCommitment': 'string'
                    }
                },
                'NextPageToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_savings_plans_utilization(
        self,
        TimePeriod: ClientGetSavingsPlansUtilizationTimePeriodTypeDef,
        Granularity: str = None,
        Filter: ClientGetSavingsPlansUtilizationFilterTypeDef = None,
    ) -> ClientGetSavingsPlansUtilizationResponseTypeDef:
        """
        Retrieves the Savings Plans utilization for your account across date ranges with daily or monthly
        granularity. Master accounts in an organization have access to member accounts. You can use
        ``GetDimensionValues`` in ``SAVINGS_PLANS`` to determine the possible dimension values.

        .. note::

          You cannot group by any dimension values for ``GetSavingsPlansUtilization`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ce-2017-10-25/GetSavingsPlansUtilization>`_

        **Request Syntax**
        ::

          response = client.get_savings_plans_utilization(
              TimePeriod={
                  'Start': 'string',
                  'End': 'string'
              },
              Granularity='DAILY'|'MONTHLY'|'HOURLY',
              Filter={
                  'Or': [
                      {'... recursive ...'},
                  ],
                  'And': [
                      {'... recursive ...'},
                  ],
                  'Not': {'... recursive ...'},
                  'Dimensions': {
                      'Key':
                      'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'
                      |'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'
                      |'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'
                      |'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'
                      |'RESERVATION_ID'|'RESOURCE_ID'|'RIGHTSIZING_TYPE'|'SAVINGS_PLANS_TYPE'
                      |'SAVINGS_PLAN_ARN'|'PAYMENT_OPTION',
                      'Values': [
                          'string',
                      ]
                  },
                  'Tags': {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
                  }
              }
          )
        :type TimePeriod: dict
        :param TimePeriod: **[REQUIRED]**

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

        :type Granularity: string
        :param Granularity:

          The granularity of the Amazon Web Services utillization data for your Savings Plans.

          The ``GetSavingsPlansUtilization`` operation supports only ``DAILY`` and ``MONTHLY``
          granularities.

        :type Filter: dict
        :param Filter:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'SavingsPlansUtilizationsByTime': [
                    {
                        'TimePeriod': {
                            'Start': 'string',
                            'End': 'string'
                        },
                        'Utilization': {
                            'TotalCommitment': 'string',
                            'UsedCommitment': 'string',
                            'UnusedCommitment': 'string',
                            'UtilizationPercentage': 'string'
                        },
                        'Savings': {
                            'NetSavings': 'string',
                            'OnDemandCostEquivalent': 'string'
                        },
                        'AmortizedCommitment': {
                            'AmortizedRecurringCommitment': 'string',
                            'AmortizedUpfrontCommitment': 'string',
                            'TotalAmortizedCommitment': 'string'
                        }
                    },
                ],
                'Total': {
                    'Utilization': {
                        'TotalCommitment': 'string',
                        'UsedCommitment': 'string',
                        'UnusedCommitment': 'string',
                        'UtilizationPercentage': 'string'
                    },
                    'Savings': {
                        'NetSavings': 'string',
                        'OnDemandCostEquivalent': 'string'
                    },
                    'AmortizedCommitment': {
                        'AmortizedRecurringCommitment': 'string',
                        'AmortizedUpfrontCommitment': 'string',
                        'TotalAmortizedCommitment': 'string'
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_savings_plans_utilization_details(
        self,
        TimePeriod: ClientGetSavingsPlansUtilizationDetailsTimePeriodTypeDef,
        Filter: ClientGetSavingsPlansUtilizationDetailsFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientGetSavingsPlansUtilizationDetailsResponseTypeDef:
        """
        Retrieves attribute data along with aggregate utilization and savings data for a given time period.
        This doesn't support granular or grouped data (daily/monthly) in response. You can't retrieve data
        by dates in a single response similar to ``GetSavingsPlanUtilization`` , but you have the option to
        make multiple calls to ``GetSavingsPlanUtilizationDetails`` by providing individual dates. You can
        use ``GetDimensionValues`` in ``SAVINGS_PLANS`` to determine the possible dimension values.

        .. note::

           ``GetSavingsPlanUtilizationDetails`` internally groups data by ``SavingsPlansArn`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ce-2017-10-25/GetSavingsPlansUtilizationDetails>`_

        **Request Syntax**
        ::

          response = client.get_savings_plans_utilization_details(
              TimePeriod={
                  'Start': 'string',
                  'End': 'string'
              },
              Filter={
                  'Or': [
                      {'... recursive ...'},
                  ],
                  'And': [
                      {'... recursive ...'},
                  ],
                  'Not': {'... recursive ...'},
                  'Dimensions': {
                      'Key':
                      'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'
                      |'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'
                      |'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'
                      |'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'
                      |'RESERVATION_ID'|'RESOURCE_ID'|'RIGHTSIZING_TYPE'|'SAVINGS_PLANS_TYPE'
                      |'SAVINGS_PLAN_ARN'|'PAYMENT_OPTION',
                      'Values': [
                          'string',
                      ]
                  },
                  'Tags': {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
                  }
              },
              NextToken='string',
              MaxResults=123
          )
        :type TimePeriod: dict
        :param TimePeriod: **[REQUIRED]**

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

        :type Filter: dict
        :param Filter:

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

        :type NextToken: string
        :param NextToken:

          The token to retrieve the next set of results. Amazon Web Services provides the token when the
          response from a previous call has more results than the maximum page size.

        :type MaxResults: integer
        :param MaxResults:

          The number of items to be returned in a response. The default is ``20`` , with a minimum value of
          ``1`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'SavingsPlansUtilizationDetails': [
                    {
                        'SavingsPlanArn': 'string',
                        'Attributes': {
                            'string': 'string'
                        },
                        'Utilization': {
                            'TotalCommitment': 'string',
                            'UsedCommitment': 'string',
                            'UnusedCommitment': 'string',
                            'UtilizationPercentage': 'string'
                        },
                        'Savings': {
                            'NetSavings': 'string',
                            'OnDemandCostEquivalent': 'string'
                        },
                        'AmortizedCommitment': {
                            'AmortizedRecurringCommitment': 'string',
                            'AmortizedUpfrontCommitment': 'string',
                            'TotalAmortizedCommitment': 'string'
                        }
                    },
                ],
                'Total': {
                    'Utilization': {
                        'TotalCommitment': 'string',
                        'UsedCommitment': 'string',
                        'UnusedCommitment': 'string',
                        'UtilizationPercentage': 'string'
                    },
                    'Savings': {
                        'NetSavings': 'string',
                        'OnDemandCostEquivalent': 'string'
                    },
                    'AmortizedCommitment': {
                        'AmortizedRecurringCommitment': 'string',
                        'AmortizedUpfrontCommitment': 'string',
                        'TotalAmortizedCommitment': 'string'
                    }
                },
                'TimePeriod': {
                    'Start': 'string',
                    'End': 'string'
                },
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_tags(
        self,
        TimePeriod: ClientGetTagsTimePeriodTypeDef,
        SearchString: str = None,
        TagKey: str = None,
        NextPageToken: str = None,
    ) -> ClientGetTagsResponseTypeDef:
        """
        Queries for available tag keys and tag values for a specified period. You can search the tag values
        for an arbitrary string.

        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ce-2017-10-25/GetTags>`_

        **Request Syntax**
        ::

          response = client.get_tags(
              SearchString='string',
              TimePeriod={
                  'Start': 'string',
                  'End': 'string'
              },
              TagKey='string',
              NextPageToken='string'
          )
        :type SearchString: string
        :param SearchString:

          The value that you want to search for.

        :type TimePeriod: dict
        :param TimePeriod: **[REQUIRED]**

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

        :type TagKey: string
        :param TagKey:

          The key of the tag that you want to return values for.

        :type NextPageToken: string
        :param NextPageToken:

          The token to retrieve the next set of results. AWS provides the token when the response from a
          previous call has more results than the maximum page size.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextPageToken': 'string',
                'Tags': [
                    'string',
                ],
                'ReturnSize': 123,
                'TotalSize': 123
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_usage_forecast(
        self,
        TimePeriod: ClientGetUsageForecastTimePeriodTypeDef,
        Metric: str,
        Granularity: str,
        Filter: ClientGetUsageForecastFilterTypeDef = None,
        PredictionIntervalLevel: int = None,
    ) -> ClientGetUsageForecastResponseTypeDef:
        """
        Retrieves a forecast for how much Amazon Web Services predicts that you will use over the forecast
        time period that you select, based on your past usage.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ce-2017-10-25/GetUsageForecast>`_

        **Request Syntax**
        ::

          response = client.get_usage_forecast(
              TimePeriod={
                  'Start': 'string',
                  'End': 'string'
              },
              Metric=
                  'BLENDED_COST'|'UNBLENDED_COST'|'AMORTIZED_COST'|'NET_UNBLENDED_COST'
                  |'NET_AMORTIZED_COST'|'USAGE_QUANTITY'|'NORMALIZED_USAGE_AMOUNT',
              Granularity='DAILY'|'MONTHLY'|'HOURLY',
              Filter={
                  'Or': [
                      {'... recursive ...'},
                  ],
                  'And': [
                      {'... recursive ...'},
                  ],
                  'Not': {'... recursive ...'},
                  'Dimensions': {
                      'Key':
                      'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'
                      |'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'
                      |'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'
                      |'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'
                      |'RESERVATION_ID'|'RESOURCE_ID'|'RIGHTSIZING_TYPE'|'SAVINGS_PLANS_TYPE'
                      |'SAVINGS_PLAN_ARN'|'PAYMENT_OPTION',
                      'Values': [
                          'string',
                      ]
                  },
                  'Tags': {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
                  }
              },
              PredictionIntervalLevel=123
          )
        :type TimePeriod: dict
        :param TimePeriod: **[REQUIRED]**

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

        :type Metric: string
        :param Metric: **[REQUIRED]**

          Which metric Cost Explorer uses to create your forecast.

          Valid values for a ``GetUsageForecast`` call are the following:

          * USAGE_QUANTITY

          * NORMALIZED_USAGE_AMOUNT

        :type Granularity: string
        :param Granularity: **[REQUIRED]**

          How granular you want the forecast to be. You can get 3 months of ``DAILY`` forecasts or 12
          months of ``MONTHLY`` forecasts.

          The ``GetUsageForecast`` operation supports only ``DAILY`` and ``MONTHLY`` granularities.

        :type Filter: dict
        :param Filter:

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

        :type PredictionIntervalLevel: integer
        :param PredictionIntervalLevel:

          Cost Explorer always returns the mean forecast as a single point. You can request a prediction
          interval around the mean by specifying a confidence level. The higher the confidence level, the
          more confident Cost Explorer is about the actual value falling in the prediction interval. Higher
          confidence levels result in wider prediction intervals.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Total': {
                    'Amount': 'string',
                    'Unit': 'string'
                },
                'ForecastResultsByTime': [
                    {
                        'TimePeriod': {
                            'Start': 'string',
                            'End': 'string'
                        },
                        'MeanValue': 'string',
                        'PredictionIntervalLowerBound': 'string',
                        'PredictionIntervalUpperBound': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

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


class Exceptions:
    BillExpirationException: Boto3ClientError
    ClientError: Boto3ClientError
    DataUnavailableException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    RequestChangedException: Boto3ClientError
    UnresolvableUsageUnitException: Boto3ClientError
