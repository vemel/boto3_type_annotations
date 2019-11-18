"Main interface for savingsplans Client"
from __future__ import annotations

from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_savingsplans.client as client_scope
from mypy_boto3_savingsplans.type_defs import (
    ClientCreateSavingsPlanResponseTypeDef,
    ClientDescribeSavingsPlanRatesResponseTypeDef,
    ClientDescribeSavingsPlanRatesfiltersTypeDef,
    ClientDescribeSavingsPlansOfferingRatesResponseTypeDef,
    ClientDescribeSavingsPlansOfferingRatesfiltersTypeDef,
    ClientDescribeSavingsPlansOfferingsResponseTypeDef,
    ClientDescribeSavingsPlansOfferingsfiltersTypeDef,
    ClientDescribeSavingsPlansResponseTypeDef,
    ClientDescribeSavingsPlansfiltersTypeDef,
    ClientListTagsForResourceResponseTypeDef,
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
    def create_savings_plan(
        self,
        savingsPlanOfferingId: str,
        commitment: str,
        upfrontPaymentAmount: str = None,
        clientToken: str = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateSavingsPlanResponseTypeDef:
        """
        Creates a Savings Plan.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/savingsplans-2019-06-28/CreateSavingsPlan>`_

        **Request Syntax**
        ::

          response = client.create_savings_plan(
              savingsPlanOfferingId='string',
              commitment='string',
              upfrontPaymentAmount='string',
              clientToken='string',
              tags={
                  'string': 'string'
              }
          )
        :type savingsPlanOfferingId: string
        :param savingsPlanOfferingId: **[REQUIRED]**

          The ID of the offering.

        :type commitment: string
        :param commitment: **[REQUIRED]**

          The hourly commitment, in USD. This is a value between 0.001 and 1 million. You cannot specify
          more than three digits after the decimal point.

        :type upfrontPaymentAmount: string
        :param upfrontPaymentAmount:

          The up-front payment amount. This is a whole number between 50 and 99 percent of the total value
          of the Savings Plan. This parameter is supported only if the payment option is ``Partial
          Upfront`` .

        :type clientToken: string
        :param clientToken:

          Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

          This field is autopopulated if not provided.

        :type tags: dict
        :param tags:

          One or more tags.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'savingsPlanId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **savingsPlanId** *(string) --*

              The ID of the Savings Plan.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_savings_plan_rates(
        self,
        savingsPlanId: str,
        filters: List[ClientDescribeSavingsPlanRatesfiltersTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientDescribeSavingsPlanRatesResponseTypeDef:
        """
        Describes the specified Savings Plans rates.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/savingsplans-2019-06-28/DescribeSavingsPlanRates>`_

        **Request Syntax**
        ::

          response = client.describe_savings_plan_rates(
              savingsPlanId='string',
              filters=[
                  {
                      'name':
                      'region'|'instanceType'|'productDescription'|'tenancy'|'productType'|'serviceCode'
                      |'usageType'|'operation',
                      'values': [
                          'string',
                      ]
                  },
              ],
              nextToken='string',
              maxResults=123
          )
        :type savingsPlanId: string
        :param savingsPlanId: **[REQUIRED]**

          The ID of the Savings Plan.

        :type filters: list
        :param filters:

          The filters.

          - *(dict) --*

            Information about a filter.

            - **name** *(string) --*

              The filter name.

            - **values** *(list) --*

              The filter values.

              - *(string) --*

        :type nextToken: string
        :param nextToken:

          The token for the next page of results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return with a single call. To retrieve additional results, make
          another call with the returned token value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'savingsPlanId': 'string',
                'searchResults': [
                    {
                        'rate': 'string',
                        'currency': 'CNY'|'USD',
                        'unit': 'Hrs',
                        'productType': 'EC2'|'Fargate',
                        'serviceCode': 'AmazonEC2'|'AmazonECS',
                        'usageType': 'string',
                        'operation': 'string',
                        'properties': [
                            {
                                'name':
                                'region'|'instanceType'|'instanceFamily'|'productDescription'|'tenancy',
                                'value': 'string'
                            },
                        ]
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **savingsPlanId** *(string) --*

              The ID of the Savings Plan.

            - **searchResults** *(list) --*

              Information about the Savings Plans rates.

              - *(dict) --*

                Information about a Savings Plan rate.

                - **rate** *(string) --*

                  The rate.

                - **currency** *(string) --*

                  The currency.

                - **unit** *(string) --*

                  The unit.

                - **productType** *(string) --*

                  The product type.

                - **serviceCode** *(string) --*

                  The service.

                - **usageType** *(string) --*

                  The usage details of the line item in the billing report.

                - **operation** *(string) --*

                  The specific AWS operation for the line item in the billing report.

                - **properties** *(list) --*

                  The properties.

                  - *(dict) --*

                    Information about a property.

                    - **name** *(string) --*

                      The property name.

                    - **value** *(string) --*

                      The property value.

            - **nextToken** *(string) --*

              The token to use to retrieve the next page of results. This value is null when there are no
              more results to return.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_savings_plans(
        self,
        savingsPlanArns: List[str] = None,
        savingsPlanIds: List[str] = None,
        nextToken: str = None,
        maxResults: int = None,
        states: List[str] = None,
        filters: List[ClientDescribeSavingsPlansfiltersTypeDef] = None,
    ) -> ClientDescribeSavingsPlansResponseTypeDef:
        """
        Describes the specified Savings Plans.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/savingsplans-2019-06-28/DescribeSavingsPlans>`_

        **Request Syntax**
        ::

          response = client.describe_savings_plans(
              savingsPlanArns=[
                  'string',
              ],
              savingsPlanIds=[
                  'string',
              ],
              nextToken='string',
              maxResults=123,
              states=[
                  'payment-pending'|'payment-failed'|'active'|'retired',
              ],
              filters=[
                  {
                      'name':
                      'region'|'ec2-instance-family'|'commitment'|'upfront'|'term'|'savings-plan-type'
                      |'payment-option'|'start'|'end',
                      'values': [
                          'string',
                      ]
                  },
              ]
          )
        :type savingsPlanArns: list
        :param savingsPlanArns:

          The Amazon Resource Names (ARN) of the Savings Plans.

          - *(string) --*

        :type savingsPlanIds: list
        :param savingsPlanIds:

          The IDs of the Savings Plans.

          - *(string) --*

        :type nextToken: string
        :param nextToken:

          The token for the next page of results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return with a single call. To retrieve additional results, make
          another call with the returned token value.

        :type states: list
        :param states:

          The states.

          - *(string) --*

        :type filters: list
        :param filters:

          The filters.

          - *(dict) --*

            Information about a filter.

            - **name** *(string) --*

              The filter name.

            - **values** *(list) --*

              The filter value.

              - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'savingsPlans': [
                    {
                        'offeringId': 'string',
                        'savingsPlanId': 'string',
                        'savingsPlanArn': 'string',
                        'description': 'string',
                        'start': 'string',
                        'end': 'string',
                        'state': 'payment-pending'|'payment-failed'|'active'|'retired',
                        'region': 'string',
                        'ec2InstanceFamily': 'string',
                        'savingsPlanType': 'Compute'|'EC2Instance',
                        'paymentOption': 'All Upfront'|'Partial Upfront'|'No Upfront',
                        'productTypes': [
                            'EC2'|'Fargate',
                        ],
                        'currency': 'CNY'|'USD',
                        'commitment': 'string',
                        'upfrontPaymentAmount': 'string',
                        'recurringPaymentAmount': 'string',
                        'termDurationInSeconds': 123,
                        'tags': {
                            'string': 'string'
                        }
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **savingsPlans** *(list) --*

              Information about the Savings Plans.

              - *(dict) --*

                Information about a Savings Plan.

                - **offeringId** *(string) --*

                  The ID of the offering.

                - **savingsPlanId** *(string) --*

                  The ID of the Savings Plan.

                - **savingsPlanArn** *(string) --*

                  The Amazon Resource Name (ARN) of the Savings Plan.

                - **description** *(string) --*

                  The description.

                - **start** *(string) --*

                  The start time.

                - **end** *(string) --*

                  The end time.

                - **state** *(string) --*

                  The state.

                - **region** *(string) --*

                  The AWS Region.

                - **ec2InstanceFamily** *(string) --*

                  The EC2 instance family.

                - **savingsPlanType** *(string) --*

                  The plan type.

                - **paymentOption** *(string) --*

                  The payment option.

                - **productTypes** *(list) --*

                  The product types.

                  - *(string) --*

                - **currency** *(string) --*

                  The currency.

                - **commitment** *(string) --*

                  The hourly commitment, in USD.

                - **upfrontPaymentAmount** *(string) --*

                  The up-front payment amount.

                - **recurringPaymentAmount** *(string) --*

                  The recurring payment amount.

                - **termDurationInSeconds** *(integer) --*

                  The duration of the term, in seconds.

                - **tags** *(dict) --*

                  One or more tags.

                  - *(string) --*

                    - *(string) --*

            - **nextToken** *(string) --*

              The token to use to retrieve the next page of results. This value is null when there are no
              more results to return.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_savings_plans_offering_rates(
        self,
        savingsPlanOfferingIds: List[str] = None,
        savingsPlanPaymentOptions: List[str] = None,
        savingsPlanTypes: List[str] = None,
        products: List[str] = None,
        serviceCodes: List[str] = None,
        usageTypes: List[str] = None,
        operations: List[str] = None,
        filters: List[ClientDescribeSavingsPlansOfferingRatesfiltersTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientDescribeSavingsPlansOfferingRatesResponseTypeDef:
        """
        Describes the specified Savings Plans offering rates.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/savingsplans-2019-06-28/DescribeSavingsPlansOfferingRates>`_
        <https://docs.aws.amazon.com/goto/WebAPI/savingsplans-2019-06-28/DescribeSavingsPlansOfferingRates>`_

        **Request Syntax**
        ::

          response = client.describe_savings_plans_offering_rates(
              savingsPlanOfferingIds=[
                  'string',
              ],
              savingsPlanPaymentOptions=[
                  'All Upfront'|'Partial Upfront'|'No Upfront',
              ],
              savingsPlanTypes=[
                  'Compute'|'EC2Instance',
              ],
              products=[
                  'EC2'|'Fargate',
              ],
              serviceCodes=[
                  'AmazonEC2'|'AmazonECS',
              ],
              usageTypes=[
                  'string',
              ],
              operations=[
                  'string',
              ],
              filters=[
                  {
                      'name':
                      'region'|'instanceFamily'|'instanceType'|'productDescription'|'tenancy'|'productId',
                      'values': [
                          'string',
                      ]
                  },
              ],
              nextToken='string',
              maxResults=123
          )
        :type savingsPlanOfferingIds: list
        :param savingsPlanOfferingIds:

          The IDs of the offerings.

          - *(string) --*

        :type savingsPlanPaymentOptions: list
        :param savingsPlanPaymentOptions:

          The payment options.

          - *(string) --*

        :type savingsPlanTypes: list
        :param savingsPlanTypes:

          The plan types.

          - *(string) --*

        :type products: list
        :param products:

          The AWS products.

          - *(string) --*

        :type serviceCodes: list
        :param serviceCodes:

          The services.

          - *(string) --*

        :type usageTypes: list
        :param usageTypes:

          The usage details of the line item in the billing report.

          - *(string) --*

        :type operations: list
        :param operations:

          The specific AWS operation for the line item in the billing report.

          - *(string) --*

        :type filters: list
        :param filters:

          The filters.

          - *(dict) --*

            Information about a filter.

            - **name** *(string) --*

              The filter name.

            - **values** *(list) --*

              The filter values.

              - *(string) --*

        :type nextToken: string
        :param nextToken:

          The token for the next page of results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return with a single call. To retrieve additional results, make
          another call with the returned token value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'searchResults': [
                    {
                        'savingsPlanOffering': {
                            'offeringId': 'string',
                            'paymentOption': 'All Upfront'|'Partial Upfront'|'No Upfront',
                            'planType': 'Compute'|'EC2Instance',
                            'durationSeconds': 123,
                            'currency': 'CNY'|'USD',
                            'planDescription': 'string'
                        },
                        'rate': 'string',
                        'unit': 'Hrs',
                        'productType': 'EC2'|'Fargate',
                        'serviceCode': 'AmazonEC2'|'AmazonECS',
                        'usageType': 'string',
                        'operation': 'string',
                        'properties': [
                            {
                                'name': 'string',
                                'value': 'string'
                            },
                        ]
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **searchResults** *(list) --*

              Information about the Savings Plans offering rates.

              - *(dict) --*

                Information about a Savings Plan offering rate.

                - **savingsPlanOffering** *(dict) --*

                  The Savings Plan offering.

                  - **offeringId** *(string) --*

                    The ID of the offering.

                  - **paymentOption** *(string) --*

                    The payment option.

                  - **planType** *(string) --*

                    The plan type.

                  - **durationSeconds** *(integer) --*

                    The duration, in seconds.

                  - **currency** *(string) --*

                    The currency.

                  - **planDescription** *(string) --*

                    The description.

                - **rate** *(string) --*

                  The Savings Plan rate.

                - **unit** *(string) --*

                  The unit.

                - **productType** *(string) --*

                  The product type.

                - **serviceCode** *(string) --*

                  The service.

                - **usageType** *(string) --*

                  The usage details of the line item in the billing report.

                - **operation** *(string) --*

                  The specific AWS operation for the line item in the billing report.

                - **properties** *(list) --*

                  The properties.

                  - *(dict) --*

                    Information about a property.

                    - **name** *(string) --*

                      The property name.

                    - **value** *(string) --*

                      The property value.

            - **nextToken** *(string) --*

              The token to use to retrieve the next page of results. This value is null when there are no
              more results to return.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_savings_plans_offerings(
        self,
        offeringIds: List[str] = None,
        paymentOptions: List[str] = None,
        productType: str = None,
        planTypes: List[str] = None,
        durations: List[int] = None,
        currencies: List[str] = None,
        descriptions: List[str] = None,
        serviceCodes: List[str] = None,
        usageTypes: List[str] = None,
        operations: List[str] = None,
        filters: List[ClientDescribeSavingsPlansOfferingsfiltersTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientDescribeSavingsPlansOfferingsResponseTypeDef:
        """
        Describes the specified Savings Plans offerings.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/savingsplans-2019-06-28/DescribeSavingsPlansOfferings>`_

        **Request Syntax**
        ::

          response = client.describe_savings_plans_offerings(
              offeringIds=[
                  'string',
              ],
              paymentOptions=[
                  'All Upfront'|'Partial Upfront'|'No Upfront',
              ],
              productType='EC2'|'Fargate',
              planTypes=[
                  'Compute'|'EC2Instance',
              ],
              durations=[
                  123,
              ],
              currencies=[
                  'CNY'|'USD',
              ],
              descriptions=[
                  'string',
              ],
              serviceCodes=[
                  'string',
              ],
              usageTypes=[
                  'string',
              ],
              operations=[
                  'string',
              ],
              filters=[
                  {
                      'name': 'region'|'instanceFamily',
                      'values': [
                          'string',
                      ]
                  },
              ],
              nextToken='string',
              maxResults=123
          )
        :type offeringIds: list
        :param offeringIds:

          The IDs of the offerings.

          - *(string) --*

        :type paymentOptions: list
        :param paymentOptions:

          The payment options.

          - *(string) --*

        :type productType: string
        :param productType:

          The product type.

        :type planTypes: list
        :param planTypes:

          The plan type.

          - *(string) --*

        :type durations: list
        :param durations:

          The durations, in seconds.

          - *(integer) --*

        :type currencies: list
        :param currencies:

          The currencies.

          - *(string) --*

        :type descriptions: list
        :param descriptions:

          The descriptions.

          - *(string) --*

        :type serviceCodes: list
        :param serviceCodes:

          The services.

          - *(string) --*

        :type usageTypes: list
        :param usageTypes:

          The usage details of the line item in the billing report.

          - *(string) --*

        :type operations: list
        :param operations:

          The specific AWS operation for the line item in the billing report.

          - *(string) --*

        :type filters: list
        :param filters:

          The filters.

          - *(dict) --*

            Information about a filter.

            - **name** *(string) --*

              The filter name.

            - **values** *(list) --*

              The filter values.

              - *(string) --*

        :type nextToken: string
        :param nextToken:

          The token for the next page of results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return with a single call. To retrieve additional results, make
          another call with the returned token value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'searchResults': [
                    {
                        'offeringId': 'string',
                        'productTypes': [
                            'EC2'|'Fargate',
                        ],
                        'planType': 'Compute'|'EC2Instance',
                        'description': 'string',
                        'paymentOption': 'All Upfront'|'Partial Upfront'|'No Upfront',
                        'durationSeconds': 123,
                        'currency': 'CNY'|'USD',
                        'serviceCode': 'string',
                        'usageType': 'string',
                        'operation': 'string',
                        'properties': [
                            {
                                'name': 'region'|'instanceFamily',
                                'value': 'string'
                            },
                        ]
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **searchResults** *(list) --*

              Information about the Savings Plans offerings.

              - *(dict) --*

                Information about a Savings Plan offering.

                - **offeringId** *(string) --*

                  The ID of the offering.

                - **productTypes** *(list) --*

                  The product type.

                  - *(string) --*

                - **planType** *(string) --*

                  The plan type.

                - **description** *(string) --*

                  The description.

                - **paymentOption** *(string) --*

                  The payment option.

                - **durationSeconds** *(integer) --*

                  The duration, in seconds.

                - **currency** *(string) --*

                  The currency.

                - **serviceCode** *(string) --*

                  The service.

                - **usageType** *(string) --*

                  The usage details of the line item in the billing report.

                - **operation** *(string) --*

                  The specific AWS operation for the line item in the billing report.

                - **properties** *(list) --*

                  The properties.

                  - *(dict) --*

                    Information about a property.

                    - **name** *(string) --*

                      The property name.

                    - **value** *(string) --*

                      The property value.

            - **nextToken** *(string) --*

              The token to use to retrieve the next page of results. This value is null when there are no
              more results to return.

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
    def list_tags_for_resource(
        self, resourceArn: str
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        Lists the tags for the specified resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/savingsplans-2019-06-28/ListTagsForResource>`_

        **Request Syntax**
        ::

          response = client.list_tags_for_resource(
              resourceArn='string'
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'tags': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **tags** *(dict) --*

              Information about the tags.

              - *(string) --*

                - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds the specified tags to the specified resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/savingsplans-2019-06-28/TagResource>`_

        **Request Syntax**
        ::

          response = client.tag_resource(
              resourceArn='string',
              tags={
                  'string': 'string'
              }
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource.

        :type tags: dict
        :param tags: **[REQUIRED]**

          One or more tags. For example, { "tags": {"key1":"value1", "key2":"value2"} }.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/savingsplans-2019-06-28/UntagResource>`_

        **Request Syntax**
        ::

          response = client.untag_resource(
              resourceArn='string',
              tagKeys=[
                  'string',
              ]
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource.

        :type tagKeys: list
        :param tagKeys: **[REQUIRED]**

          The tag keys.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalServerException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceQuotaExceededException: Boto3ClientError
    ValidationException: Boto3ClientError
