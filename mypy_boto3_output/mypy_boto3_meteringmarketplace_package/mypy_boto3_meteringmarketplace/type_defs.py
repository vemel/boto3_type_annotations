"Main interface for meteringmarketplace type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientBatchMeterUsageResponseResultsUsageRecordTypeDef",
    "ClientBatchMeterUsageResponseResultsTypeDef",
    "ClientBatchMeterUsageResponseUnprocessedRecordsTypeDef",
    "ClientBatchMeterUsageResponseTypeDef",
    "ClientBatchMeterUsageUsageRecordsTypeDef",
    "ClientMeterUsageResponseTypeDef",
    "ClientRegisterUsageResponseTypeDef",
    "ClientResolveCustomerResponseTypeDef",
)


_ClientBatchMeterUsageResponseResultsUsageRecordTypeDef = TypedDict(
    "_ClientBatchMeterUsageResponseResultsUsageRecordTypeDef",
    {
        "Timestamp": datetime,
        "CustomerIdentifier": str,
        "Dimension": str,
        "Quantity": int,
    },
    total=False,
)


class ClientBatchMeterUsageResponseResultsUsageRecordTypeDef(
    _ClientBatchMeterUsageResponseResultsUsageRecordTypeDef
):
    """
    Type definition for `ClientBatchMeterUsageResponseResults` `UsageRecord`

    The UsageRecord that was part of the BatchMeterUsage request.

    - **Timestamp** *(datetime) --*

      Timestamp, in UTC, for which the usage is being reported.

      Your application can meter usage for up to one hour in the past. Make sure the
      timestamp value is not before the start of the software usage.

    - **CustomerIdentifier** *(string) --*

      The CustomerIdentifier is obtained through the ResolveCustomer operation and represents
      an individual buyer in your application.

    - **Dimension** *(string) --*

      During the process of registering a product on AWS Marketplace, up to eight dimensions
      are specified. These represent different units of value in your application.

    - **Quantity** *(integer) --*

      The quantity of usage consumed by the customer for the given dimension and time.
      Defaults to ``0`` if not specified.
    """


_ClientBatchMeterUsageResponseResultsTypeDef = TypedDict(
    "_ClientBatchMeterUsageResponseResultsTypeDef",
    {
        "UsageRecord": ClientBatchMeterUsageResponseResultsUsageRecordTypeDef,
        "MeteringRecordId": str,
        "Status": str,
    },
    total=False,
)


class ClientBatchMeterUsageResponseResultsTypeDef(
    _ClientBatchMeterUsageResponseResultsTypeDef
):
    """
    Type definition for `ClientBatchMeterUsageResponse` `Results`

    A UsageRecordResult indicates the status of a given UsageRecord processed by
    BatchMeterUsage.

    - **UsageRecord** *(dict) --*

      The UsageRecord that was part of the BatchMeterUsage request.

      - **Timestamp** *(datetime) --*

        Timestamp, in UTC, for which the usage is being reported.

        Your application can meter usage for up to one hour in the past. Make sure the
        timestamp value is not before the start of the software usage.

      - **CustomerIdentifier** *(string) --*

        The CustomerIdentifier is obtained through the ResolveCustomer operation and represents
        an individual buyer in your application.

      - **Dimension** *(string) --*

        During the process of registering a product on AWS Marketplace, up to eight dimensions
        are specified. These represent different units of value in your application.

      - **Quantity** *(integer) --*

        The quantity of usage consumed by the customer for the given dimension and time.
        Defaults to ``0`` if not specified.

    - **MeteringRecordId** *(string) --*

      The MeteringRecordId is a unique identifier for this metering event.

    - **Status** *(string) --*

      The UsageRecordResult Status indicates the status of an individual UsageRecord processed
      by BatchMeterUsage.

      * *Success* - The UsageRecord was accepted and honored by BatchMeterUsage.

      * *CustomerNotSubscribed* - The CustomerIdentifier specified is not subscribed to your
      product. The UsageRecord was not honored. Future UsageRecords for this customer will fail
      until the customer subscribes to your product.

      * *DuplicateRecord* - Indicates that the UsageRecord was invalid and not honored. A
      previously metered UsageRecord had the same customer, dimension, and time, but a
      different quantity.
    """


_ClientBatchMeterUsageResponseUnprocessedRecordsTypeDef = TypedDict(
    "_ClientBatchMeterUsageResponseUnprocessedRecordsTypeDef",
    {
        "Timestamp": datetime,
        "CustomerIdentifier": str,
        "Dimension": str,
        "Quantity": int,
    },
    total=False,
)


class ClientBatchMeterUsageResponseUnprocessedRecordsTypeDef(
    _ClientBatchMeterUsageResponseUnprocessedRecordsTypeDef
):
    """
    Type definition for `ClientBatchMeterUsageResponse` `UnprocessedRecords`

    A UsageRecord indicates a quantity of usage for a given product, customer, dimension and
    time.

    Multiple requests with the same UsageRecords as input will be deduplicated to prevent
    double charges.

    - **Timestamp** *(datetime) --*

      Timestamp, in UTC, for which the usage is being reported.

      Your application can meter usage for up to one hour in the past. Make sure the timestamp
      value is not before the start of the software usage.

    - **CustomerIdentifier** *(string) --*

      The CustomerIdentifier is obtained through the ResolveCustomer operation and represents
      an individual buyer in your application.

    - **Dimension** *(string) --*

      During the process of registering a product on AWS Marketplace, up to eight dimensions
      are specified. These represent different units of value in your application.

    - **Quantity** *(integer) --*

      The quantity of usage consumed by the customer for the given dimension and time. Defaults
      to ``0`` if not specified.
    """


_ClientBatchMeterUsageResponseTypeDef = TypedDict(
    "_ClientBatchMeterUsageResponseTypeDef",
    {
        "Results": List[ClientBatchMeterUsageResponseResultsTypeDef],
        "UnprocessedRecords": List[
            ClientBatchMeterUsageResponseUnprocessedRecordsTypeDef
        ],
    },
    total=False,
)


class ClientBatchMeterUsageResponseTypeDef(_ClientBatchMeterUsageResponseTypeDef):
    """
    Type definition for `ClientBatchMeterUsage` `Response`

    Contains the UsageRecords processed by BatchMeterUsage and any records that have failed due to
    transient error.

    - **Results** *(list) --*

      Contains all UsageRecords processed by BatchMeterUsage. These records were either honored by
      AWS Marketplace Metering Service or were invalid.

      - *(dict) --*

        A UsageRecordResult indicates the status of a given UsageRecord processed by
        BatchMeterUsage.

        - **UsageRecord** *(dict) --*

          The UsageRecord that was part of the BatchMeterUsage request.

          - **Timestamp** *(datetime) --*

            Timestamp, in UTC, for which the usage is being reported.

            Your application can meter usage for up to one hour in the past. Make sure the
            timestamp value is not before the start of the software usage.

          - **CustomerIdentifier** *(string) --*

            The CustomerIdentifier is obtained through the ResolveCustomer operation and represents
            an individual buyer in your application.

          - **Dimension** *(string) --*

            During the process of registering a product on AWS Marketplace, up to eight dimensions
            are specified. These represent different units of value in your application.

          - **Quantity** *(integer) --*

            The quantity of usage consumed by the customer for the given dimension and time.
            Defaults to ``0`` if not specified.

        - **MeteringRecordId** *(string) --*

          The MeteringRecordId is a unique identifier for this metering event.

        - **Status** *(string) --*

          The UsageRecordResult Status indicates the status of an individual UsageRecord processed
          by BatchMeterUsage.

          * *Success* - The UsageRecord was accepted and honored by BatchMeterUsage.

          * *CustomerNotSubscribed* - The CustomerIdentifier specified is not subscribed to your
          product. The UsageRecord was not honored. Future UsageRecords for this customer will fail
          until the customer subscribes to your product.

          * *DuplicateRecord* - Indicates that the UsageRecord was invalid and not honored. A
          previously metered UsageRecord had the same customer, dimension, and time, but a
          different quantity.

    - **UnprocessedRecords** *(list) --*

      Contains all UsageRecords that were not processed by BatchMeterUsage. This is a list of
      UsageRecords. You can retry the failed request by making another BatchMeterUsage call with
      this list as input in the BatchMeterUsageRequest.

      - *(dict) --*

        A UsageRecord indicates a quantity of usage for a given product, customer, dimension and
        time.

        Multiple requests with the same UsageRecords as input will be deduplicated to prevent
        double charges.

        - **Timestamp** *(datetime) --*

          Timestamp, in UTC, for which the usage is being reported.

          Your application can meter usage for up to one hour in the past. Make sure the timestamp
          value is not before the start of the software usage.

        - **CustomerIdentifier** *(string) --*

          The CustomerIdentifier is obtained through the ResolveCustomer operation and represents
          an individual buyer in your application.

        - **Dimension** *(string) --*

          During the process of registering a product on AWS Marketplace, up to eight dimensions
          are specified. These represent different units of value in your application.

        - **Quantity** *(integer) --*

          The quantity of usage consumed by the customer for the given dimension and time. Defaults
          to ``0`` if not specified.
    """


_RequiredClientBatchMeterUsageUsageRecordsTypeDef = TypedDict(
    "_RequiredClientBatchMeterUsageUsageRecordsTypeDef",
    {"Timestamp": datetime, "CustomerIdentifier": str, "Dimension": str},
)
_OptionalClientBatchMeterUsageUsageRecordsTypeDef = TypedDict(
    "_OptionalClientBatchMeterUsageUsageRecordsTypeDef", {"Quantity": int}, total=False
)


class ClientBatchMeterUsageUsageRecordsTypeDef(
    _RequiredClientBatchMeterUsageUsageRecordsTypeDef,
    _OptionalClientBatchMeterUsageUsageRecordsTypeDef,
):
    """
    Type definition for `ClientBatchMeterUsage` `UsageRecords`

    A UsageRecord indicates a quantity of usage for a given product, customer, dimension and time.

    Multiple requests with the same UsageRecords as input will be deduplicated to prevent double
    charges.

    - **Timestamp** *(datetime) --* **[REQUIRED]**

      Timestamp, in UTC, for which the usage is being reported.

      Your application can meter usage for up to one hour in the past. Make sure the timestamp
      value is not before the start of the software usage.

    - **CustomerIdentifier** *(string) --* **[REQUIRED]**

      The CustomerIdentifier is obtained through the ResolveCustomer operation and represents an
      individual buyer in your application.

    - **Dimension** *(string) --* **[REQUIRED]**

      During the process of registering a product on AWS Marketplace, up to eight dimensions are
      specified. These represent different units of value in your application.

    - **Quantity** *(integer) --*

      The quantity of usage consumed by the customer for the given dimension and time. Defaults to
      ``0`` if not specified.
    """


_ClientMeterUsageResponseTypeDef = TypedDict(
    "_ClientMeterUsageResponseTypeDef", {"MeteringRecordId": str}, total=False
)


class ClientMeterUsageResponseTypeDef(_ClientMeterUsageResponseTypeDef):
    """
    Type definition for `ClientMeterUsage` `Response`

    - **MeteringRecordId** *(string) --*

      Metering record id.
    """


_ClientRegisterUsageResponseTypeDef = TypedDict(
    "_ClientRegisterUsageResponseTypeDef",
    {"PublicKeyRotationTimestamp": datetime, "Signature": str},
    total=False,
)


class ClientRegisterUsageResponseTypeDef(_ClientRegisterUsageResponseTypeDef):
    """
    Type definition for `ClientRegisterUsage` `Response`

    - **PublicKeyRotationTimestamp** *(datetime) --*

      (Optional) Only included when public key version has expired

    - **Signature** *(string) --*

      JWT Token
    """


_ClientResolveCustomerResponseTypeDef = TypedDict(
    "_ClientResolveCustomerResponseTypeDef",
    {"CustomerIdentifier": str, "ProductCode": str},
    total=False,
)


class ClientResolveCustomerResponseTypeDef(_ClientResolveCustomerResponseTypeDef):
    """
    Type definition for `ClientResolveCustomer` `Response`

    The result of the ResolveCustomer operation. Contains the CustomerIdentifier and product code.

    - **CustomerIdentifier** *(string) --*

      The CustomerIdentifier is used to identify an individual customer in your application. Calls
      to BatchMeterUsage require CustomerIdentifiers for each UsageRecord.

    - **ProductCode** *(string) --*

      The product code is returned to confirm that the buyer is registering for your product.
      Subsequent BatchMeterUsage calls should be made using this product code.
    """
