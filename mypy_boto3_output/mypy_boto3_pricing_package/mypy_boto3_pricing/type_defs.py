"Main interface for pricing type defs"
from __future__ import annotations

from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientDescribeServicesResponseServicesTypeDef",
    "ClientDescribeServicesResponseTypeDef",
    "ClientGetAttributeValuesResponseAttributeValuesTypeDef",
    "ClientGetAttributeValuesResponseTypeDef",
    "ClientGetProductsFiltersTypeDef",
    "ClientGetProductsResponseTypeDef",
    "DescribeServicesPaginatePaginationConfigTypeDef",
    "DescribeServicesPaginateResponseServicesTypeDef",
    "DescribeServicesPaginateResponseTypeDef",
    "GetAttributeValuesPaginatePaginationConfigTypeDef",
    "GetAttributeValuesPaginateResponseAttributeValuesTypeDef",
    "GetAttributeValuesPaginateResponseTypeDef",
    "GetProductsPaginateFiltersTypeDef",
    "GetProductsPaginatePaginationConfigTypeDef",
    "GetProductsPaginateResponseTypeDef",
)


_ClientDescribeServicesResponseServicesTypeDef = TypedDict(
    "_ClientDescribeServicesResponseServicesTypeDef",
    {"ServiceCode": str, "AttributeNames": List[str]},
    total=False,
)


class ClientDescribeServicesResponseServicesTypeDef(
    _ClientDescribeServicesResponseServicesTypeDef
):
    """
    Type definition for `ClientDescribeServicesResponse` `Services`

    The metadata for a service, such as the service code and available attribute names.

    - **ServiceCode** *(string) --*

      The code for the AWS service.

    - **AttributeNames** *(list) --*

      The attributes that are available for this service.

      - *(string) --*
    """


_ClientDescribeServicesResponseTypeDef = TypedDict(
    "_ClientDescribeServicesResponseTypeDef",
    {
        "Services": List[ClientDescribeServicesResponseServicesTypeDef],
        "FormatVersion": str,
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeServicesResponseTypeDef(_ClientDescribeServicesResponseTypeDef):
    """
    Type definition for `ClientDescribeServices` `Response`

    - **Services** *(list) --*

      The service metadata for the service or services in the response.

      - *(dict) --*

        The metadata for a service, such as the service code and available attribute names.

        - **ServiceCode** *(string) --*

          The code for the AWS service.

        - **AttributeNames** *(list) --*

          The attributes that are available for this service.

          - *(string) --*

    - **FormatVersion** *(string) --*

      The format version of the response. For example, ``aws_v1`` .

    - **NextToken** *(string) --*

      The pagination token for the next set of retreivable results.
    """


_ClientGetAttributeValuesResponseAttributeValuesTypeDef = TypedDict(
    "_ClientGetAttributeValuesResponseAttributeValuesTypeDef",
    {"Value": str},
    total=False,
)


class ClientGetAttributeValuesResponseAttributeValuesTypeDef(
    _ClientGetAttributeValuesResponseAttributeValuesTypeDef
):
    """
    Type definition for `ClientGetAttributeValuesResponse` `AttributeValues`

    The values of a given attribute, such as ``Throughput Optimized HDD`` or ``Provisioned
    IOPS`` for the ``Amazon EC2``  ``volumeType`` attribute.

    - **Value** *(string) --*

      The specific value of an ``attributeName`` .
    """


_ClientGetAttributeValuesResponseTypeDef = TypedDict(
    "_ClientGetAttributeValuesResponseTypeDef",
    {
        "AttributeValues": List[ClientGetAttributeValuesResponseAttributeValuesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientGetAttributeValuesResponseTypeDef(_ClientGetAttributeValuesResponseTypeDef):
    """
    Type definition for `ClientGetAttributeValues` `Response`

    - **AttributeValues** *(list) --*

      The list of values for an attribute. For example, ``Throughput Optimized HDD`` and
      ``Provisioned IOPS`` are two available values for the ``AmazonEC2``  ``volumeType`` .

      - *(dict) --*

        The values of a given attribute, such as ``Throughput Optimized HDD`` or ``Provisioned
        IOPS`` for the ``Amazon EC2``  ``volumeType`` attribute.

        - **Value** *(string) --*

          The specific value of an ``attributeName`` .

    - **NextToken** *(string) --*

      The pagination token that indicates the next set of results to retrieve.
    """


_ClientGetProductsFiltersTypeDef = TypedDict(
    "_ClientGetProductsFiltersTypeDef", {"Type": str, "Field": str, "Value": str}
)


class ClientGetProductsFiltersTypeDef(_ClientGetProductsFiltersTypeDef):
    """
    Type definition for `ClientGetProducts` `Filters`

    The constraints that you want all returned products to match.

    - **Type** *(string) --* **[REQUIRED]**

      The type of filter that you want to use.

      Valid values are: ``TERM_MATCH`` . ``TERM_MATCH`` returns only products that match both the
      given filter field and the given value.

    - **Field** *(string) --* **[REQUIRED]**

      The product metadata field that you want to filter on. You can filter by just the service
      code to see all products for a specific service, filter by just the attribute name to see a
      specific attribute for multiple services, or use both a service code and an attribute name to
      retrieve only products that match both fields.

      Valid values include: ``ServiceCode`` , and all attribute names

      For example, you can filter by the ``AmazonEC2`` service code and the ``volumeType``
      attribute name to get the prices for only Amazon EC2 volumes.

    - **Value** *(string) --* **[REQUIRED]**

      The service code or attribute value that you want to filter by. If you are filtering by
      service code this is the actual service code, such as ``AmazonEC2`` . If you are filtering by
      attribute name, this is the attribute value that you want the returned products to match,
      such as a ``Provisioned IOPS`` volume.
    """


_ClientGetProductsResponseTypeDef = TypedDict(
    "_ClientGetProductsResponseTypeDef",
    {"FormatVersion": str, "PriceList": List[str], "NextToken": str},
    total=False,
)


class ClientGetProductsResponseTypeDef(_ClientGetProductsResponseTypeDef):
    """
    Type definition for `ClientGetProducts` `Response`

    - **FormatVersion** *(string) --*

      The format version of the response. For example, aws_v1.

    - **PriceList** *(list) --*

      The list of products that match your filters. The list contains both the product metadata and
      the price information.

      - *(string) --*

    - **NextToken** *(string) --*

      The pagination token that indicates the next set of results to retrieve.
    """


_DescribeServicesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeServicesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeServicesPaginatePaginationConfigTypeDef(
    _DescribeServicesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeServicesPaginate` `PaginationConfig`

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


_DescribeServicesPaginateResponseServicesTypeDef = TypedDict(
    "_DescribeServicesPaginateResponseServicesTypeDef",
    {"ServiceCode": str, "AttributeNames": List[str]},
    total=False,
)


class DescribeServicesPaginateResponseServicesTypeDef(
    _DescribeServicesPaginateResponseServicesTypeDef
):
    """
    Type definition for `DescribeServicesPaginateResponse` `Services`

    The metadata for a service, such as the service code and available attribute names.

    - **ServiceCode** *(string) --*

      The code for the AWS service.

    - **AttributeNames** *(list) --*

      The attributes that are available for this service.

      - *(string) --*
    """


_DescribeServicesPaginateResponseTypeDef = TypedDict(
    "_DescribeServicesPaginateResponseTypeDef",
    {
        "Services": List[DescribeServicesPaginateResponseServicesTypeDef],
        "FormatVersion": str,
    },
    total=False,
)


class DescribeServicesPaginateResponseTypeDef(_DescribeServicesPaginateResponseTypeDef):
    """
    Type definition for `DescribeServicesPaginate` `Response`

    - **Services** *(list) --*

      The service metadata for the service or services in the response.

      - *(dict) --*

        The metadata for a service, such as the service code and available attribute names.

        - **ServiceCode** *(string) --*

          The code for the AWS service.

        - **AttributeNames** *(list) --*

          The attributes that are available for this service.

          - *(string) --*

    - **FormatVersion** *(string) --*

      The format version of the response. For example, ``aws_v1`` .
    """


_GetAttributeValuesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetAttributeValuesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetAttributeValuesPaginatePaginationConfigTypeDef(
    _GetAttributeValuesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetAttributeValuesPaginate` `PaginationConfig`

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


_GetAttributeValuesPaginateResponseAttributeValuesTypeDef = TypedDict(
    "_GetAttributeValuesPaginateResponseAttributeValuesTypeDef",
    {"Value": str},
    total=False,
)


class GetAttributeValuesPaginateResponseAttributeValuesTypeDef(
    _GetAttributeValuesPaginateResponseAttributeValuesTypeDef
):
    """
    Type definition for `GetAttributeValuesPaginateResponse` `AttributeValues`

    The values of a given attribute, such as ``Throughput Optimized HDD`` or ``Provisioned
    IOPS`` for the ``Amazon EC2``  ``volumeType`` attribute.

    - **Value** *(string) --*

      The specific value of an ``attributeName`` .
    """


_GetAttributeValuesPaginateResponseTypeDef = TypedDict(
    "_GetAttributeValuesPaginateResponseTypeDef",
    {"AttributeValues": List[GetAttributeValuesPaginateResponseAttributeValuesTypeDef]},
    total=False,
)


class GetAttributeValuesPaginateResponseTypeDef(
    _GetAttributeValuesPaginateResponseTypeDef
):
    """
    Type definition for `GetAttributeValuesPaginate` `Response`

    - **AttributeValues** *(list) --*

      The list of values for an attribute. For example, ``Throughput Optimized HDD`` and
      ``Provisioned IOPS`` are two available values for the ``AmazonEC2``  ``volumeType`` .

      - *(dict) --*

        The values of a given attribute, such as ``Throughput Optimized HDD`` or ``Provisioned
        IOPS`` for the ``Amazon EC2``  ``volumeType`` attribute.

        - **Value** *(string) --*

          The specific value of an ``attributeName`` .
    """


_GetProductsPaginateFiltersTypeDef = TypedDict(
    "_GetProductsPaginateFiltersTypeDef", {"Type": str, "Field": str, "Value": str}
)


class GetProductsPaginateFiltersTypeDef(_GetProductsPaginateFiltersTypeDef):
    """
    Type definition for `GetProductsPaginate` `Filters`

    The constraints that you want all returned products to match.

    - **Type** *(string) --* **[REQUIRED]**

      The type of filter that you want to use.

      Valid values are: ``TERM_MATCH`` . ``TERM_MATCH`` returns only products that match both the
      given filter field and the given value.

    - **Field** *(string) --* **[REQUIRED]**

      The product metadata field that you want to filter on. You can filter by just the service
      code to see all products for a specific service, filter by just the attribute name to see a
      specific attribute for multiple services, or use both a service code and an attribute name to
      retrieve only products that match both fields.

      Valid values include: ``ServiceCode`` , and all attribute names

      For example, you can filter by the ``AmazonEC2`` service code and the ``volumeType``
      attribute name to get the prices for only Amazon EC2 volumes.

    - **Value** *(string) --* **[REQUIRED]**

      The service code or attribute value that you want to filter by. If you are filtering by
      service code this is the actual service code, such as ``AmazonEC2`` . If you are filtering by
      attribute name, this is the attribute value that you want the returned products to match,
      such as a ``Provisioned IOPS`` volume.
    """


_GetProductsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetProductsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetProductsPaginatePaginationConfigTypeDef(
    _GetProductsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetProductsPaginate` `PaginationConfig`

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


_GetProductsPaginateResponseTypeDef = TypedDict(
    "_GetProductsPaginateResponseTypeDef",
    {"FormatVersion": str, "PriceList": List[str]},
    total=False,
)


class GetProductsPaginateResponseTypeDef(_GetProductsPaginateResponseTypeDef):
    """
    Type definition for `GetProductsPaginate` `Response`

    - **FormatVersion** *(string) --*

      The format version of the response. For example, aws_v1.

    - **PriceList** *(list) --*

      The list of products that match your filters. The list contains both the product metadata and
      the price information.

      - *(string) --*
    """
