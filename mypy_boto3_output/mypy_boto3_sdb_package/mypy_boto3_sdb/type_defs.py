"Main interface for sdb type defs"
from __future__ import annotations

from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientBatchDeleteAttributesItemsAttributesTypeDef",
    "ClientBatchDeleteAttributesItemsTypeDef",
    "ClientBatchPutAttributesItemsAttributesTypeDef",
    "ClientBatchPutAttributesItemsTypeDef",
    "ClientDomainMetadataResponseTypeDef",
    "ClientGetAttributesResponseAttributesTypeDef",
    "ClientGetAttributesResponseTypeDef",
    "ClientListDomainsResponseTypeDef",
    "ClientPutAttributesAttributesTypeDef",
    "ClientSelectResponseItemsAttributesTypeDef",
    "ClientSelectResponseItemsTypeDef",
    "ClientSelectResponseTypeDef",
    "ListDomainsPaginatePaginationConfigTypeDef",
    "ListDomainsPaginateResponseTypeDef",
    "SelectPaginatePaginationConfigTypeDef",
    "SelectPaginateResponseItemsAttributesTypeDef",
    "SelectPaginateResponseItemsTypeDef",
    "SelectPaginateResponseTypeDef",
)


_RequiredClientBatchDeleteAttributesItemsAttributesTypeDef = TypedDict(
    "_RequiredClientBatchDeleteAttributesItemsAttributesTypeDef",
    {"Name": str, "Value": str},
)
_OptionalClientBatchDeleteAttributesItemsAttributesTypeDef = TypedDict(
    "_OptionalClientBatchDeleteAttributesItemsAttributesTypeDef",
    {"AlternateNameEncoding": str, "AlternateValueEncoding": str},
    total=False,
)


class ClientBatchDeleteAttributesItemsAttributesTypeDef(
    _RequiredClientBatchDeleteAttributesItemsAttributesTypeDef,
    _OptionalClientBatchDeleteAttributesItemsAttributesTypeDef,
):
    """
    Type definition for `ClientBatchDeleteAttributesItems` `Attributes`

    - **Name** *(string) --* **[REQUIRED]** The name of the attribute.

    - **AlternateNameEncoding** *(string) --*

    - **Value** *(string) --* **[REQUIRED]** The value of the attribute.

    - **AlternateValueEncoding** *(string) --*
    """


_RequiredClientBatchDeleteAttributesItemsTypeDef = TypedDict(
    "_RequiredClientBatchDeleteAttributesItemsTypeDef", {"Name": str}
)
_OptionalClientBatchDeleteAttributesItemsTypeDef = TypedDict(
    "_OptionalClientBatchDeleteAttributesItemsTypeDef",
    {"Attributes": List[ClientBatchDeleteAttributesItemsAttributesTypeDef]},
    total=False,
)


class ClientBatchDeleteAttributesItemsTypeDef(
    _RequiredClientBatchDeleteAttributesItemsTypeDef,
    _OptionalClientBatchDeleteAttributesItemsTypeDef,
):
    """
    Type definition for `ClientBatchDeleteAttributes` `Items`

    - **Name** *(string) --* **[REQUIRED]**

    - **Attributes** *(list) --*

      - *(dict) --*

        - **Name** *(string) --* **[REQUIRED]** The name of the attribute.

        - **AlternateNameEncoding** *(string) --*

        - **Value** *(string) --* **[REQUIRED]** The value of the attribute.

        - **AlternateValueEncoding** *(string) --*
    """


_RequiredClientBatchPutAttributesItemsAttributesTypeDef = TypedDict(
    "_RequiredClientBatchPutAttributesItemsAttributesTypeDef",
    {"Name": str, "Value": str},
)
_OptionalClientBatchPutAttributesItemsAttributesTypeDef = TypedDict(
    "_OptionalClientBatchPutAttributesItemsAttributesTypeDef",
    {"Replace": bool},
    total=False,
)


class ClientBatchPutAttributesItemsAttributesTypeDef(
    _RequiredClientBatchPutAttributesItemsAttributesTypeDef,
    _OptionalClientBatchPutAttributesItemsAttributesTypeDef,
):
    """
    Type definition for `ClientBatchPutAttributesItems` `Attributes`

    - **Name** *(string) --* **[REQUIRED]** The name of the replaceable attribute.

    - **Value** *(string) --* **[REQUIRED]** The value of the replaceable attribute.

    - **Replace** *(boolean) --* A flag specifying whether or not to replace the
    attribute/value pair or to add a new attribute/value pair. The default setting is ``false``
    .
    """


_ClientBatchPutAttributesItemsTypeDef = TypedDict(
    "_ClientBatchPutAttributesItemsTypeDef",
    {"Name": str, "Attributes": List[ClientBatchPutAttributesItemsAttributesTypeDef]},
)


class ClientBatchPutAttributesItemsTypeDef(_ClientBatchPutAttributesItemsTypeDef):
    """
    Type definition for `ClientBatchPutAttributes` `Items`

    - **Name** *(string) --* **[REQUIRED]** The name of the replaceable item.

    - **Attributes** *(list) --* **[REQUIRED]** The list of attributes for a replaceable item.

      - *(dict) --*

        - **Name** *(string) --* **[REQUIRED]** The name of the replaceable attribute.

        - **Value** *(string) --* **[REQUIRED]** The value of the replaceable attribute.

        - **Replace** *(boolean) --* A flag specifying whether or not to replace the
        attribute/value pair or to add a new attribute/value pair. The default setting is ``false``
        .
    """


_ClientDomainMetadataResponseTypeDef = TypedDict(
    "_ClientDomainMetadataResponseTypeDef",
    {
        "ItemCount": int,
        "ItemNamesSizeBytes": int,
        "AttributeNameCount": int,
        "AttributeNamesSizeBytes": int,
        "AttributeValueCount": int,
        "AttributeValuesSizeBytes": int,
        "Timestamp": int,
    },
    total=False,
)


class ClientDomainMetadataResponseTypeDef(_ClientDomainMetadataResponseTypeDef):
    """
    Type definition for `ClientDomainMetadata` `Response`

    - **ItemCount** *(integer) --* The number of all items in the domain.

    - **ItemNamesSizeBytes** *(integer) --* The total size of all item names in the domain, in
    bytes.

    - **AttributeNameCount** *(integer) --* The number of unique attribute names in the domain.

    - **AttributeNamesSizeBytes** *(integer) --* The total size of all unique attribute names in
    the domain, in bytes.

    - **AttributeValueCount** *(integer) --* The number of all attribute name/value pairs in the
    domain.

    - **AttributeValuesSizeBytes** *(integer) --* The total size of all attribute values in the
    domain, in bytes.

    - **Timestamp** *(integer) --* The data and time when metadata was calculated, in Epoch (UNIX)
    seconds.
    """


_ClientGetAttributesResponseAttributesTypeDef = TypedDict(
    "_ClientGetAttributesResponseAttributesTypeDef",
    {
        "Name": str,
        "AlternateNameEncoding": str,
        "Value": str,
        "AlternateValueEncoding": str,
    },
    total=False,
)


class ClientGetAttributesResponseAttributesTypeDef(
    _ClientGetAttributesResponseAttributesTypeDef
):
    """
    Type definition for `ClientGetAttributesResponse` `Attributes`

    - **Name** *(string) --* The name of the attribute.

    - **AlternateNameEncoding** *(string) --*

    - **Value** *(string) --* The value of the attribute.

    - **AlternateValueEncoding** *(string) --*
    """


_ClientGetAttributesResponseTypeDef = TypedDict(
    "_ClientGetAttributesResponseTypeDef",
    {"Attributes": List[ClientGetAttributesResponseAttributesTypeDef]},
    total=False,
)


class ClientGetAttributesResponseTypeDef(_ClientGetAttributesResponseTypeDef):
    """
    Type definition for `ClientGetAttributes` `Response`

    - **Attributes** *(list) --* The list of attributes returned by the operation.

      - *(dict) --*

        - **Name** *(string) --* The name of the attribute.

        - **AlternateNameEncoding** *(string) --*

        - **Value** *(string) --* The value of the attribute.

        - **AlternateValueEncoding** *(string) --*
    """


_ClientListDomainsResponseTypeDef = TypedDict(
    "_ClientListDomainsResponseTypeDef",
    {"DomainNames": List[str], "NextToken": str},
    total=False,
)


class ClientListDomainsResponseTypeDef(_ClientListDomainsResponseTypeDef):
    """
    Type definition for `ClientListDomains` `Response`

    - **DomainNames** *(list) --* A list of domain names that match the expression.

      - *(string) --*

    - **NextToken** *(string) --* An opaque token indicating that there are more domains than the
    specified ``MaxNumberOfDomains`` still available.
    """


_RequiredClientPutAttributesAttributesTypeDef = TypedDict(
    "_RequiredClientPutAttributesAttributesTypeDef", {"Name": str, "Value": str}
)
_OptionalClientPutAttributesAttributesTypeDef = TypedDict(
    "_OptionalClientPutAttributesAttributesTypeDef", {"Replace": bool}, total=False
)


class ClientPutAttributesAttributesTypeDef(
    _RequiredClientPutAttributesAttributesTypeDef,
    _OptionalClientPutAttributesAttributesTypeDef,
):
    """
    Type definition for `ClientPutAttributes` `Attributes`

    - **Name** *(string) --* **[REQUIRED]** The name of the replaceable attribute.

    - **Value** *(string) --* **[REQUIRED]** The value of the replaceable attribute.

    - **Replace** *(boolean) --* A flag specifying whether or not to replace the attribute/value
    pair or to add a new attribute/value pair. The default setting is ``false`` .
    """


_ClientSelectResponseItemsAttributesTypeDef = TypedDict(
    "_ClientSelectResponseItemsAttributesTypeDef",
    {
        "Name": str,
        "AlternateNameEncoding": str,
        "Value": str,
        "AlternateValueEncoding": str,
    },
    total=False,
)


class ClientSelectResponseItemsAttributesTypeDef(
    _ClientSelectResponseItemsAttributesTypeDef
):
    """
    Type definition for `ClientSelectResponseItems` `Attributes`

    - **Name** *(string) --* The name of the attribute.

    - **AlternateNameEncoding** *(string) --*

    - **Value** *(string) --* The value of the attribute.

    - **AlternateValueEncoding** *(string) --*
    """


_ClientSelectResponseItemsTypeDef = TypedDict(
    "_ClientSelectResponseItemsTypeDef",
    {
        "Name": str,
        "AlternateNameEncoding": str,
        "Attributes": List[ClientSelectResponseItemsAttributesTypeDef],
    },
    total=False,
)


class ClientSelectResponseItemsTypeDef(_ClientSelectResponseItemsTypeDef):
    """
    Type definition for `ClientSelectResponse` `Items`

    - **Name** *(string) --* The name of the item.

    - **AlternateNameEncoding** *(string) --*

    - **Attributes** *(list) --* A list of attributes.

      - *(dict) --*

        - **Name** *(string) --* The name of the attribute.

        - **AlternateNameEncoding** *(string) --*

        - **Value** *(string) --* The value of the attribute.

        - **AlternateValueEncoding** *(string) --*
    """


_ClientSelectResponseTypeDef = TypedDict(
    "_ClientSelectResponseTypeDef",
    {"Items": List[ClientSelectResponseItemsTypeDef], "NextToken": str},
    total=False,
)


class ClientSelectResponseTypeDef(_ClientSelectResponseTypeDef):
    """
    Type definition for `ClientSelect` `Response`

    - **Items** *(list) --* A list of items that match the select expression.

      - *(dict) --*

        - **Name** *(string) --* The name of the item.

        - **AlternateNameEncoding** *(string) --*

        - **Attributes** *(list) --* A list of attributes.

          - *(dict) --*

            - **Name** *(string) --* The name of the attribute.

            - **AlternateNameEncoding** *(string) --*

            - **Value** *(string) --* The value of the attribute.

            - **AlternateValueEncoding** *(string) --*

    - **NextToken** *(string) --* An opaque token indicating that more items than
    ``MaxNumberOfItems`` were matched, the response size exceeded 1 megabyte, or the execution time
    exceeded 5 seconds.
    """


_ListDomainsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDomainsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDomainsPaginatePaginationConfigTypeDef(
    _ListDomainsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDomainsPaginate` `PaginationConfig`

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


_ListDomainsPaginateResponseTypeDef = TypedDict(
    "_ListDomainsPaginateResponseTypeDef", {"DomainNames": List[str]}, total=False
)


class ListDomainsPaginateResponseTypeDef(_ListDomainsPaginateResponseTypeDef):
    """
    Type definition for `ListDomainsPaginate` `Response`

    - **DomainNames** *(list) --* A list of domain names that match the expression.

      - *(string) --*
    """


_SelectPaginatePaginationConfigTypeDef = TypedDict(
    "_SelectPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class SelectPaginatePaginationConfigTypeDef(_SelectPaginatePaginationConfigTypeDef):
    """
    Type definition for `SelectPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_SelectPaginateResponseItemsAttributesTypeDef = TypedDict(
    "_SelectPaginateResponseItemsAttributesTypeDef",
    {
        "Name": str,
        "AlternateNameEncoding": str,
        "Value": str,
        "AlternateValueEncoding": str,
    },
    total=False,
)


class SelectPaginateResponseItemsAttributesTypeDef(
    _SelectPaginateResponseItemsAttributesTypeDef
):
    """
    Type definition for `SelectPaginateResponseItems` `Attributes`

    - **Name** *(string) --* The name of the attribute.

    - **AlternateNameEncoding** *(string) --*

    - **Value** *(string) --* The value of the attribute.

    - **AlternateValueEncoding** *(string) --*
    """


_SelectPaginateResponseItemsTypeDef = TypedDict(
    "_SelectPaginateResponseItemsTypeDef",
    {
        "Name": str,
        "AlternateNameEncoding": str,
        "Attributes": List[SelectPaginateResponseItemsAttributesTypeDef],
    },
    total=False,
)


class SelectPaginateResponseItemsTypeDef(_SelectPaginateResponseItemsTypeDef):
    """
    Type definition for `SelectPaginateResponse` `Items`

    - **Name** *(string) --* The name of the item.

    - **AlternateNameEncoding** *(string) --*

    - **Attributes** *(list) --* A list of attributes.

      - *(dict) --*

        - **Name** *(string) --* The name of the attribute.

        - **AlternateNameEncoding** *(string) --*

        - **Value** *(string) --* The value of the attribute.

        - **AlternateValueEncoding** *(string) --*
    """


_SelectPaginateResponseTypeDef = TypedDict(
    "_SelectPaginateResponseTypeDef",
    {"Items": List[SelectPaginateResponseItemsTypeDef]},
    total=False,
)


class SelectPaginateResponseTypeDef(_SelectPaginateResponseTypeDef):
    """
    Type definition for `SelectPaginate` `Response`

    - **Items** *(list) --* A list of items that match the select expression.

      - *(dict) --*

        - **Name** *(string) --* The name of the item.

        - **AlternateNameEncoding** *(string) --*

        - **Attributes** *(list) --* A list of attributes.

          - *(dict) --*

            - **Name** *(string) --* The name of the attribute.

            - **AlternateNameEncoding** *(string) --*

            - **Value** *(string) --* The value of the attribute.

            - **AlternateValueEncoding** *(string) --*
    """
