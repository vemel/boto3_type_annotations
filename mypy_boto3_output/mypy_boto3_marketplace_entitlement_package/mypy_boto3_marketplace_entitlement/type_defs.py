"Main interface for marketplace-entitlement type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientGetEntitlementsResponseEntitlementsValueTypeDef",
    "ClientGetEntitlementsResponseEntitlementsTypeDef",
    "ClientGetEntitlementsResponseTypeDef",
    "GetEntitlementsPaginatePaginationConfigTypeDef",
    "GetEntitlementsPaginateResponseEntitlementsValueTypeDef",
    "GetEntitlementsPaginateResponseEntitlementsTypeDef",
    "GetEntitlementsPaginateResponseTypeDef",
)


_ClientGetEntitlementsResponseEntitlementsValueTypeDef = TypedDict(
    "_ClientGetEntitlementsResponseEntitlementsValueTypeDef",
    {
        "IntegerValue": int,
        "DoubleValue": float,
        "BooleanValue": bool,
        "StringValue": str,
    },
    total=False,
)


class ClientGetEntitlementsResponseEntitlementsValueTypeDef(
    _ClientGetEntitlementsResponseEntitlementsValueTypeDef
):
    """
    Type definition for `ClientGetEntitlementsResponseEntitlements` `Value`

    The EntitlementValue represents the amount of capacity that the customer is entitled to
    for the product.

    - **IntegerValue** *(integer) --*

      The IntegerValue field will be populated with an integer value when the entitlement is
      an integer type. Otherwise, the field will not be set.

    - **DoubleValue** *(float) --*

      The DoubleValue field will be populated with a double value when the entitlement is a
      double type. Otherwise, the field will not be set.

    - **BooleanValue** *(boolean) --*

      The BooleanValue field will be populated with a boolean value when the entitlement is a
      boolean type. Otherwise, the field will not be set.

    - **StringValue** *(string) --*

      The StringValue field will be populated with a string value when the entitlement is a
      string type. Otherwise, the field will not be set.
    """


_ClientGetEntitlementsResponseEntitlementsTypeDef = TypedDict(
    "_ClientGetEntitlementsResponseEntitlementsTypeDef",
    {
        "ProductCode": str,
        "Dimension": str,
        "CustomerIdentifier": str,
        "Value": ClientGetEntitlementsResponseEntitlementsValueTypeDef,
        "ExpirationDate": datetime,
    },
    total=False,
)


class ClientGetEntitlementsResponseEntitlementsTypeDef(
    _ClientGetEntitlementsResponseEntitlementsTypeDef
):
    """
    Type definition for `ClientGetEntitlementsResponse` `Entitlements`

    An entitlement represents capacity in a product owned by the customer. For example, a
    customer might own some number of users or seats in an SaaS application or some amount of
    data capacity in a multi-tenant database.

    - **ProductCode** *(string) --*

      The product code for which the given entitlement applies. Product codes are provided by
      AWS Marketplace when the product listing is created.

    - **Dimension** *(string) --*

      The dimension for which the given entitlement applies. Dimensions represent categories of
      capacity in a product and are specified when the product is listed in AWS Marketplace.

    - **CustomerIdentifier** *(string) --*

      The customer identifier is a handle to each unique customer in an application. Customer
      identifiers are obtained through the ResolveCustomer operation in AWS Marketplace
      Metering Service.

    - **Value** *(dict) --*

      The EntitlementValue represents the amount of capacity that the customer is entitled to
      for the product.

      - **IntegerValue** *(integer) --*

        The IntegerValue field will be populated with an integer value when the entitlement is
        an integer type. Otherwise, the field will not be set.

      - **DoubleValue** *(float) --*

        The DoubleValue field will be populated with a double value when the entitlement is a
        double type. Otherwise, the field will not be set.

      - **BooleanValue** *(boolean) --*

        The BooleanValue field will be populated with a boolean value when the entitlement is a
        boolean type. Otherwise, the field will not be set.

      - **StringValue** *(string) --*

        The StringValue field will be populated with a string value when the entitlement is a
        string type. Otherwise, the field will not be set.

    - **ExpirationDate** *(datetime) --*

      The expiration date represents the minimum date through which this entitlement is
      expected to remain valid. For contractual products listed on AWS Marketplace, the
      expiration date is the date at which the customer will renew or cancel their contract.
      Customers who are opting to renew their contract will still have entitlements with an
      expiration date.
    """


_ClientGetEntitlementsResponseTypeDef = TypedDict(
    "_ClientGetEntitlementsResponseTypeDef",
    {
        "Entitlements": List[ClientGetEntitlementsResponseEntitlementsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientGetEntitlementsResponseTypeDef(_ClientGetEntitlementsResponseTypeDef):
    """
    Type definition for `ClientGetEntitlements` `Response`

    The GetEntitlementsRequest contains results from the GetEntitlements operation.

    - **Entitlements** *(list) --*

      The set of entitlements found through the GetEntitlements operation. If the result contains
      an empty set of entitlements, NextToken might still be present and should be used.

      - *(dict) --*

        An entitlement represents capacity in a product owned by the customer. For example, a
        customer might own some number of users or seats in an SaaS application or some amount of
        data capacity in a multi-tenant database.

        - **ProductCode** *(string) --*

          The product code for which the given entitlement applies. Product codes are provided by
          AWS Marketplace when the product listing is created.

        - **Dimension** *(string) --*

          The dimension for which the given entitlement applies. Dimensions represent categories of
          capacity in a product and are specified when the product is listed in AWS Marketplace.

        - **CustomerIdentifier** *(string) --*

          The customer identifier is a handle to each unique customer in an application. Customer
          identifiers are obtained through the ResolveCustomer operation in AWS Marketplace
          Metering Service.

        - **Value** *(dict) --*

          The EntitlementValue represents the amount of capacity that the customer is entitled to
          for the product.

          - **IntegerValue** *(integer) --*

            The IntegerValue field will be populated with an integer value when the entitlement is
            an integer type. Otherwise, the field will not be set.

          - **DoubleValue** *(float) --*

            The DoubleValue field will be populated with a double value when the entitlement is a
            double type. Otherwise, the field will not be set.

          - **BooleanValue** *(boolean) --*

            The BooleanValue field will be populated with a boolean value when the entitlement is a
            boolean type. Otherwise, the field will not be set.

          - **StringValue** *(string) --*

            The StringValue field will be populated with a string value when the entitlement is a
            string type. Otherwise, the field will not be set.

        - **ExpirationDate** *(datetime) --*

          The expiration date represents the minimum date through which this entitlement is
          expected to remain valid. For contractual products listed on AWS Marketplace, the
          expiration date is the date at which the customer will renew or cancel their contract.
          Customers who are opting to renew their contract will still have entitlements with an
          expiration date.

    - **NextToken** *(string) --*

      For paginated results, use NextToken in subsequent calls to GetEntitlements. If the result
      contains an empty set of entitlements, NextToken might still be present and should be used.
    """


_GetEntitlementsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetEntitlementsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetEntitlementsPaginatePaginationConfigTypeDef(
    _GetEntitlementsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetEntitlementsPaginate` `PaginationConfig`

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


_GetEntitlementsPaginateResponseEntitlementsValueTypeDef = TypedDict(
    "_GetEntitlementsPaginateResponseEntitlementsValueTypeDef",
    {
        "IntegerValue": int,
        "DoubleValue": float,
        "BooleanValue": bool,
        "StringValue": str,
    },
    total=False,
)


class GetEntitlementsPaginateResponseEntitlementsValueTypeDef(
    _GetEntitlementsPaginateResponseEntitlementsValueTypeDef
):
    """
    Type definition for `GetEntitlementsPaginateResponseEntitlements` `Value`

    The EntitlementValue represents the amount of capacity that the customer is entitled to
    for the product.

    - **IntegerValue** *(integer) --*

      The IntegerValue field will be populated with an integer value when the entitlement is
      an integer type. Otherwise, the field will not be set.

    - **DoubleValue** *(float) --*

      The DoubleValue field will be populated with a double value when the entitlement is a
      double type. Otherwise, the field will not be set.

    - **BooleanValue** *(boolean) --*

      The BooleanValue field will be populated with a boolean value when the entitlement is a
      boolean type. Otherwise, the field will not be set.

    - **StringValue** *(string) --*

      The StringValue field will be populated with a string value when the entitlement is a
      string type. Otherwise, the field will not be set.
    """


_GetEntitlementsPaginateResponseEntitlementsTypeDef = TypedDict(
    "_GetEntitlementsPaginateResponseEntitlementsTypeDef",
    {
        "ProductCode": str,
        "Dimension": str,
        "CustomerIdentifier": str,
        "Value": GetEntitlementsPaginateResponseEntitlementsValueTypeDef,
        "ExpirationDate": datetime,
    },
    total=False,
)


class GetEntitlementsPaginateResponseEntitlementsTypeDef(
    _GetEntitlementsPaginateResponseEntitlementsTypeDef
):
    """
    Type definition for `GetEntitlementsPaginateResponse` `Entitlements`

    An entitlement represents capacity in a product owned by the customer. For example, a
    customer might own some number of users or seats in an SaaS application or some amount of
    data capacity in a multi-tenant database.

    - **ProductCode** *(string) --*

      The product code for which the given entitlement applies. Product codes are provided by
      AWS Marketplace when the product listing is created.

    - **Dimension** *(string) --*

      The dimension for which the given entitlement applies. Dimensions represent categories of
      capacity in a product and are specified when the product is listed in AWS Marketplace.

    - **CustomerIdentifier** *(string) --*

      The customer identifier is a handle to each unique customer in an application. Customer
      identifiers are obtained through the ResolveCustomer operation in AWS Marketplace
      Metering Service.

    - **Value** *(dict) --*

      The EntitlementValue represents the amount of capacity that the customer is entitled to
      for the product.

      - **IntegerValue** *(integer) --*

        The IntegerValue field will be populated with an integer value when the entitlement is
        an integer type. Otherwise, the field will not be set.

      - **DoubleValue** *(float) --*

        The DoubleValue field will be populated with a double value when the entitlement is a
        double type. Otherwise, the field will not be set.

      - **BooleanValue** *(boolean) --*

        The BooleanValue field will be populated with a boolean value when the entitlement is a
        boolean type. Otherwise, the field will not be set.

      - **StringValue** *(string) --*

        The StringValue field will be populated with a string value when the entitlement is a
        string type. Otherwise, the field will not be set.

    - **ExpirationDate** *(datetime) --*

      The expiration date represents the minimum date through which this entitlement is
      expected to remain valid. For contractual products listed on AWS Marketplace, the
      expiration date is the date at which the customer will renew or cancel their contract.
      Customers who are opting to renew their contract will still have entitlements with an
      expiration date.
    """


_GetEntitlementsPaginateResponseTypeDef = TypedDict(
    "_GetEntitlementsPaginateResponseTypeDef",
    {"Entitlements": List[GetEntitlementsPaginateResponseEntitlementsTypeDef]},
    total=False,
)


class GetEntitlementsPaginateResponseTypeDef(_GetEntitlementsPaginateResponseTypeDef):
    """
    Type definition for `GetEntitlementsPaginate` `Response`

    The GetEntitlementsRequest contains results from the GetEntitlements operation.

    - **Entitlements** *(list) --*

      The set of entitlements found through the GetEntitlements operation. If the result contains
      an empty set of entitlements, NextToken might still be present and should be used.

      - *(dict) --*

        An entitlement represents capacity in a product owned by the customer. For example, a
        customer might own some number of users or seats in an SaaS application or some amount of
        data capacity in a multi-tenant database.

        - **ProductCode** *(string) --*

          The product code for which the given entitlement applies. Product codes are provided by
          AWS Marketplace when the product listing is created.

        - **Dimension** *(string) --*

          The dimension for which the given entitlement applies. Dimensions represent categories of
          capacity in a product and are specified when the product is listed in AWS Marketplace.

        - **CustomerIdentifier** *(string) --*

          The customer identifier is a handle to each unique customer in an application. Customer
          identifiers are obtained through the ResolveCustomer operation in AWS Marketplace
          Metering Service.

        - **Value** *(dict) --*

          The EntitlementValue represents the amount of capacity that the customer is entitled to
          for the product.

          - **IntegerValue** *(integer) --*

            The IntegerValue field will be populated with an integer value when the entitlement is
            an integer type. Otherwise, the field will not be set.

          - **DoubleValue** *(float) --*

            The DoubleValue field will be populated with a double value when the entitlement is a
            double type. Otherwise, the field will not be set.

          - **BooleanValue** *(boolean) --*

            The BooleanValue field will be populated with a boolean value when the entitlement is a
            boolean type. Otherwise, the field will not be set.

          - **StringValue** *(string) --*

            The StringValue field will be populated with a string value when the entitlement is a
            string type. Otherwise, the field will not be set.

        - **ExpirationDate** *(datetime) --*

          The expiration date represents the minimum date through which this entitlement is
          expected to remain valid. For contractual products listed on AWS Marketplace, the
          expiration date is the date at which the customer will renew or cancel their contract.
          Customers who are opting to renew their contract will still have entitlements with an
          expiration date.
    """
