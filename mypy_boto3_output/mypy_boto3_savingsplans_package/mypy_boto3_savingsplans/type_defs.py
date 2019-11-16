"Main interface for savingsplans type defs"
from __future__ import annotations

from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateSavingsPlanResponseTypeDef",
    "ClientDescribeSavingsPlanRatesResponsesearchResultspropertiesTypeDef",
    "ClientDescribeSavingsPlanRatesResponsesearchResultsTypeDef",
    "ClientDescribeSavingsPlanRatesResponseTypeDef",
    "ClientDescribeSavingsPlanRatesfiltersTypeDef",
    "ClientDescribeSavingsPlansOfferingRatesResponsesearchResultspropertiesTypeDef",
    "ClientDescribeSavingsPlansOfferingRatesResponsesearchResultssavingsPlanOfferingTypeDef",
    "ClientDescribeSavingsPlansOfferingRatesResponsesearchResultsTypeDef",
    "ClientDescribeSavingsPlansOfferingRatesResponseTypeDef",
    "ClientDescribeSavingsPlansOfferingRatesfiltersTypeDef",
    "ClientDescribeSavingsPlansOfferingsResponsesearchResultspropertiesTypeDef",
    "ClientDescribeSavingsPlansOfferingsResponsesearchResultsTypeDef",
    "ClientDescribeSavingsPlansOfferingsResponseTypeDef",
    "ClientDescribeSavingsPlansOfferingsfiltersTypeDef",
    "ClientDescribeSavingsPlansResponsesavingsPlansTypeDef",
    "ClientDescribeSavingsPlansResponseTypeDef",
    "ClientDescribeSavingsPlansfiltersTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
)


_ClientCreateSavingsPlanResponseTypeDef = TypedDict(
    "_ClientCreateSavingsPlanResponseTypeDef", {"savingsPlanId": str}, total=False
)


class ClientCreateSavingsPlanResponseTypeDef(_ClientCreateSavingsPlanResponseTypeDef):
    """
    Type definition for `ClientCreateSavingsPlan` `Response`

    - **savingsPlanId** *(string) --*

      The ID of the Savings Plan.
    """


_ClientDescribeSavingsPlanRatesResponsesearchResultspropertiesTypeDef = TypedDict(
    "_ClientDescribeSavingsPlanRatesResponsesearchResultspropertiesTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientDescribeSavingsPlanRatesResponsesearchResultspropertiesTypeDef(
    _ClientDescribeSavingsPlanRatesResponsesearchResultspropertiesTypeDef
):
    """
    Type definition for `ClientDescribeSavingsPlanRatesResponsesearchResults` `properties`

    Information about a property.

    - **name** *(string) --*

      The property name.

    - **value** *(string) --*

      The property value.
    """


_ClientDescribeSavingsPlanRatesResponsesearchResultsTypeDef = TypedDict(
    "_ClientDescribeSavingsPlanRatesResponsesearchResultsTypeDef",
    {
        "rate": str,
        "currency": str,
        "unit": str,
        "productType": str,
        "serviceCode": str,
        "usageType": str,
        "operation": str,
        "properties": List[
            ClientDescribeSavingsPlanRatesResponsesearchResultspropertiesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeSavingsPlanRatesResponsesearchResultsTypeDef(
    _ClientDescribeSavingsPlanRatesResponsesearchResultsTypeDef
):
    """
    Type definition for `ClientDescribeSavingsPlanRatesResponse` `searchResults`

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
    """


_ClientDescribeSavingsPlanRatesResponseTypeDef = TypedDict(
    "_ClientDescribeSavingsPlanRatesResponseTypeDef",
    {
        "savingsPlanId": str,
        "searchResults": List[
            ClientDescribeSavingsPlanRatesResponsesearchResultsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeSavingsPlanRatesResponseTypeDef(
    _ClientDescribeSavingsPlanRatesResponseTypeDef
):
    """
    Type definition for `ClientDescribeSavingsPlanRates` `Response`

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


_ClientDescribeSavingsPlanRatesfiltersTypeDef = TypedDict(
    "_ClientDescribeSavingsPlanRatesfiltersTypeDef",
    {"name": str, "values": List[str]},
    total=False,
)


class ClientDescribeSavingsPlanRatesfiltersTypeDef(
    _ClientDescribeSavingsPlanRatesfiltersTypeDef
):
    """
    Type definition for `ClientDescribeSavingsPlanRates` `filters`

    Information about a filter.

    - **name** *(string) --*

      The filter name.

    - **values** *(list) --*

      The filter values.

      - *(string) --*
    """


_ClientDescribeSavingsPlansOfferingRatesResponsesearchResultspropertiesTypeDef = TypedDict(
    "_ClientDescribeSavingsPlansOfferingRatesResponsesearchResultspropertiesTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientDescribeSavingsPlansOfferingRatesResponsesearchResultspropertiesTypeDef(
    _ClientDescribeSavingsPlansOfferingRatesResponsesearchResultspropertiesTypeDef
):
    """
    Type definition for `ClientDescribeSavingsPlansOfferingRatesResponsesearchResults` `properties`

    Information about a property.

    - **name** *(string) --*

      The property name.

    - **value** *(string) --*

      The property value.
    """


_ClientDescribeSavingsPlansOfferingRatesResponsesearchResultssavingsPlanOfferingTypeDef = TypedDict(
    "_ClientDescribeSavingsPlansOfferingRatesResponsesearchResultssavingsPlanOfferingTypeDef",
    {
        "offeringId": str,
        "paymentOption": str,
        "planType": str,
        "durationSeconds": int,
        "currency": str,
        "planDescription": str,
    },
    total=False,
)


class ClientDescribeSavingsPlansOfferingRatesResponsesearchResultssavingsPlanOfferingTypeDef(
    _ClientDescribeSavingsPlansOfferingRatesResponsesearchResultssavingsPlanOfferingTypeDef
):
    """
    Type definition for `ClientDescribeSavingsPlansOfferingRatesResponsesearchResults` `savingsPlanOffering`

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
    """


_ClientDescribeSavingsPlansOfferingRatesResponsesearchResultsTypeDef = TypedDict(
    "_ClientDescribeSavingsPlansOfferingRatesResponsesearchResultsTypeDef",
    {
        "savingsPlanOffering": ClientDescribeSavingsPlansOfferingRatesResponsesearchResultssavingsPlanOfferingTypeDef,
        "rate": str,
        "unit": str,
        "productType": str,
        "serviceCode": str,
        "usageType": str,
        "operation": str,
        "properties": List[
            ClientDescribeSavingsPlansOfferingRatesResponsesearchResultspropertiesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeSavingsPlansOfferingRatesResponsesearchResultsTypeDef(
    _ClientDescribeSavingsPlansOfferingRatesResponsesearchResultsTypeDef
):
    """
    Type definition for `ClientDescribeSavingsPlansOfferingRatesResponse` `searchResults`

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
    """


_ClientDescribeSavingsPlansOfferingRatesResponseTypeDef = TypedDict(
    "_ClientDescribeSavingsPlansOfferingRatesResponseTypeDef",
    {
        "searchResults": List[
            ClientDescribeSavingsPlansOfferingRatesResponsesearchResultsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeSavingsPlansOfferingRatesResponseTypeDef(
    _ClientDescribeSavingsPlansOfferingRatesResponseTypeDef
):
    """
    Type definition for `ClientDescribeSavingsPlansOfferingRates` `Response`

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


_ClientDescribeSavingsPlansOfferingRatesfiltersTypeDef = TypedDict(
    "_ClientDescribeSavingsPlansOfferingRatesfiltersTypeDef",
    {"name": str, "values": List[str]},
    total=False,
)


class ClientDescribeSavingsPlansOfferingRatesfiltersTypeDef(
    _ClientDescribeSavingsPlansOfferingRatesfiltersTypeDef
):
    """
    Type definition for `ClientDescribeSavingsPlansOfferingRates` `filters`

    Information about a filter.

    - **name** *(string) --*

      The filter name.

    - **values** *(list) --*

      The filter values.

      - *(string) --*
    """


_ClientDescribeSavingsPlansOfferingsResponsesearchResultspropertiesTypeDef = TypedDict(
    "_ClientDescribeSavingsPlansOfferingsResponsesearchResultspropertiesTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientDescribeSavingsPlansOfferingsResponsesearchResultspropertiesTypeDef(
    _ClientDescribeSavingsPlansOfferingsResponsesearchResultspropertiesTypeDef
):
    """
    Type definition for `ClientDescribeSavingsPlansOfferingsResponsesearchResults` `properties`

    Information about a property.

    - **name** *(string) --*

      The property name.

    - **value** *(string) --*

      The property value.
    """


_ClientDescribeSavingsPlansOfferingsResponsesearchResultsTypeDef = TypedDict(
    "_ClientDescribeSavingsPlansOfferingsResponsesearchResultsTypeDef",
    {
        "offeringId": str,
        "productTypes": List[str],
        "planType": str,
        "description": str,
        "paymentOption": str,
        "durationSeconds": int,
        "currency": str,
        "serviceCode": str,
        "usageType": str,
        "operation": str,
        "properties": List[
            ClientDescribeSavingsPlansOfferingsResponsesearchResultspropertiesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeSavingsPlansOfferingsResponsesearchResultsTypeDef(
    _ClientDescribeSavingsPlansOfferingsResponsesearchResultsTypeDef
):
    """
    Type definition for `ClientDescribeSavingsPlansOfferingsResponse` `searchResults`

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
    """


_ClientDescribeSavingsPlansOfferingsResponseTypeDef = TypedDict(
    "_ClientDescribeSavingsPlansOfferingsResponseTypeDef",
    {
        "searchResults": List[
            ClientDescribeSavingsPlansOfferingsResponsesearchResultsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeSavingsPlansOfferingsResponseTypeDef(
    _ClientDescribeSavingsPlansOfferingsResponseTypeDef
):
    """
    Type definition for `ClientDescribeSavingsPlansOfferings` `Response`

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


_ClientDescribeSavingsPlansOfferingsfiltersTypeDef = TypedDict(
    "_ClientDescribeSavingsPlansOfferingsfiltersTypeDef",
    {"name": str, "values": List[str]},
    total=False,
)


class ClientDescribeSavingsPlansOfferingsfiltersTypeDef(
    _ClientDescribeSavingsPlansOfferingsfiltersTypeDef
):
    """
    Type definition for `ClientDescribeSavingsPlansOfferings` `filters`

    Information about a filter.

    - **name** *(string) --*

      The filter name.

    - **values** *(list) --*

      The filter values.

      - *(string) --*
    """


_ClientDescribeSavingsPlansResponsesavingsPlansTypeDef = TypedDict(
    "_ClientDescribeSavingsPlansResponsesavingsPlansTypeDef",
    {
        "offeringId": str,
        "savingsPlanId": str,
        "savingsPlanArn": str,
        "description": str,
        "start": str,
        "end": str,
        "state": str,
        "region": str,
        "ec2InstanceFamily": str,
        "savingsPlanType": str,
        "paymentOption": str,
        "productTypes": List[str],
        "currency": str,
        "commitment": str,
        "upfrontPaymentAmount": str,
        "recurringPaymentAmount": str,
        "termDurationInSeconds": int,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientDescribeSavingsPlansResponsesavingsPlansTypeDef(
    _ClientDescribeSavingsPlansResponsesavingsPlansTypeDef
):
    """
    Type definition for `ClientDescribeSavingsPlansResponse` `savingsPlans`

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
    """


_ClientDescribeSavingsPlansResponseTypeDef = TypedDict(
    "_ClientDescribeSavingsPlansResponseTypeDef",
    {
        "savingsPlans": List[ClientDescribeSavingsPlansResponsesavingsPlansTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeSavingsPlansResponseTypeDef(
    _ClientDescribeSavingsPlansResponseTypeDef
):
    """
    Type definition for `ClientDescribeSavingsPlans` `Response`

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


_ClientDescribeSavingsPlansfiltersTypeDef = TypedDict(
    "_ClientDescribeSavingsPlansfiltersTypeDef",
    {"name": str, "values": List[str]},
    total=False,
)


class ClientDescribeSavingsPlansfiltersTypeDef(
    _ClientDescribeSavingsPlansfiltersTypeDef
):
    """
    Type definition for `ClientDescribeSavingsPlans` `filters`

    Information about a filter.

    - **name** *(string) --*

      The filter name.

    - **values** *(list) --*

      The filter value.

      - *(string) --*
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **tags** *(dict) --*

      Information about the tags.

      - *(string) --*

        - *(string) --*
    """
