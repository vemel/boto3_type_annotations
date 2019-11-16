"Main interface for mediastore-data type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientDescribeObjectResponseTypeDef",
    "ClientGetObjectResponseTypeDef",
    "ClientListItemsResponseItemsTypeDef",
    "ClientListItemsResponseTypeDef",
    "ClientPutObjectResponseTypeDef",
    "ListItemsPaginatePaginationConfigTypeDef",
    "ListItemsPaginateResponseItemsTypeDef",
    "ListItemsPaginateResponseTypeDef",
)


_ClientDescribeObjectResponseTypeDef = TypedDict(
    "_ClientDescribeObjectResponseTypeDef",
    {
        "ETag": str,
        "ContentType": str,
        "ContentLength": int,
        "CacheControl": str,
        "LastModified": datetime,
    },
    total=False,
)


class ClientDescribeObjectResponseTypeDef(_ClientDescribeObjectResponseTypeDef):
    """
    Type definition for `ClientDescribeObject` `Response`

    - **ETag** *(string) --*

      The ETag that represents a unique instance of the object.

    - **ContentType** *(string) --*

      The content type of the object.

    - **ContentLength** *(integer) --*

      The length of the object in bytes.

    - **CacheControl** *(string) --*

      An optional ``CacheControl`` header that allows the caller to control the object's cache
      behavior. Headers can be passed in as specified in the HTTP at
      `https\\://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9
      <https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9>`__ .

      Headers with a custom user-defined value are also accepted.

    - **LastModified** *(datetime) --*

      The date and time that the object was last modified.
    """


_ClientGetObjectResponseTypeDef = TypedDict(
    "_ClientGetObjectResponseTypeDef",
    {
        "CacheControl": str,
        "ContentRange": str,
        "ContentLength": int,
        "ContentType": str,
        "ETag": str,
        "LastModified": datetime,
        "StatusCode": int,
    },
    total=False,
)


class ClientGetObjectResponseTypeDef(_ClientGetObjectResponseTypeDef):
    """
    Type definition for `ClientGetObject` `Response`

    - **Body** (:class:`.StreamingBody`) --

      The bytes of the object.

    - **CacheControl** *(string) --*

      An optional ``CacheControl`` header that allows the caller to control the object's cache
      behavior. Headers can be passed in as specified in the HTTP spec at
      `https\\://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9
      <https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9>`__ .

      Headers with a custom user-defined value are also accepted.

    - **ContentRange** *(string) --*

      The range of bytes to retrieve.

    - **ContentLength** *(integer) --*

      The length of the object in bytes.

    - **ContentType** *(string) --*

      The content type of the object.

    - **ETag** *(string) --*

      The ETag that represents a unique instance of the object.

    - **LastModified** *(datetime) --*

      The date and time that the object was last modified.

    - **StatusCode** *(integer) --*

      The HTML status code of the request. Status codes ranging from 200 to 299 indicate success.
      All other status codes indicate the type of error that occurred.
    """


_ClientListItemsResponseItemsTypeDef = TypedDict(
    "_ClientListItemsResponseItemsTypeDef",
    {
        "Name": str,
        "Type": str,
        "ETag": str,
        "LastModified": datetime,
        "ContentType": str,
        "ContentLength": int,
    },
    total=False,
)


class ClientListItemsResponseItemsTypeDef(_ClientListItemsResponseItemsTypeDef):
    """
    Type definition for `ClientListItemsResponse` `Items`

    A metadata entry for a folder or object.

    - **Name** *(string) --*

      The name of the item.

    - **Type** *(string) --*

      The item type (folder or object).

    - **ETag** *(string) --*

      The ETag that represents a unique instance of the item.

    - **LastModified** *(datetime) --*

      The date and time that the item was last modified.

    - **ContentType** *(string) --*

      The content type of the item.

    - **ContentLength** *(integer) --*

      The length of the item in bytes.
    """


_ClientListItemsResponseTypeDef = TypedDict(
    "_ClientListItemsResponseTypeDef",
    {"Items": List[ClientListItemsResponseItemsTypeDef], "NextToken": str},
    total=False,
)


class ClientListItemsResponseTypeDef(_ClientListItemsResponseTypeDef):
    """
    Type definition for `ClientListItems` `Response`

    - **Items** *(list) --*

      The metadata entries for the folders and objects at the requested path.

      - *(dict) --*

        A metadata entry for a folder or object.

        - **Name** *(string) --*

          The name of the item.

        - **Type** *(string) --*

          The item type (folder or object).

        - **ETag** *(string) --*

          The ETag that represents a unique instance of the item.

        - **LastModified** *(datetime) --*

          The date and time that the item was last modified.

        - **ContentType** *(string) --*

          The content type of the item.

        - **ContentLength** *(integer) --*

          The length of the item in bytes.

    - **NextToken** *(string) --*

      The token that can be used in a request to view the next set of results. For example, you
      submit a ``ListItems`` request that matches 2,000 items with ``MaxResults`` set at 500. The
      service returns the first batch of results (up to 500) and a ``NextToken`` value that can be
      used to fetch the next batch of results.
    """


_ClientPutObjectResponseTypeDef = TypedDict(
    "_ClientPutObjectResponseTypeDef",
    {"ContentSHA256": str, "ETag": str, "StorageClass": str},
    total=False,
)


class ClientPutObjectResponseTypeDef(_ClientPutObjectResponseTypeDef):
    """
    Type definition for `ClientPutObject` `Response`

    - **ContentSHA256** *(string) --*

      The SHA256 digest of the object that is persisted.

    - **ETag** *(string) --*

      Unique identifier of the object in the container.

    - **StorageClass** *(string) --*

      The storage class where the object was persisted. The class should be “Temporal”.
    """


_ListItemsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListItemsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListItemsPaginatePaginationConfigTypeDef(
    _ListItemsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListItemsPaginate` `PaginationConfig`

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


_ListItemsPaginateResponseItemsTypeDef = TypedDict(
    "_ListItemsPaginateResponseItemsTypeDef",
    {
        "Name": str,
        "Type": str,
        "ETag": str,
        "LastModified": datetime,
        "ContentType": str,
        "ContentLength": int,
    },
    total=False,
)


class ListItemsPaginateResponseItemsTypeDef(_ListItemsPaginateResponseItemsTypeDef):
    """
    Type definition for `ListItemsPaginateResponse` `Items`

    A metadata entry for a folder or object.

    - **Name** *(string) --*

      The name of the item.

    - **Type** *(string) --*

      The item type (folder or object).

    - **ETag** *(string) --*

      The ETag that represents a unique instance of the item.

    - **LastModified** *(datetime) --*

      The date and time that the item was last modified.

    - **ContentType** *(string) --*

      The content type of the item.

    - **ContentLength** *(integer) --*

      The length of the item in bytes.
    """


_ListItemsPaginateResponseTypeDef = TypedDict(
    "_ListItemsPaginateResponseTypeDef",
    {"Items": List[ListItemsPaginateResponseItemsTypeDef]},
    total=False,
)


class ListItemsPaginateResponseTypeDef(_ListItemsPaginateResponseTypeDef):
    """
    Type definition for `ListItemsPaginate` `Response`

    - **Items** *(list) --*

      The metadata entries for the folders and objects at the requested path.

      - *(dict) --*

        A metadata entry for a folder or object.

        - **Name** *(string) --*

          The name of the item.

        - **Type** *(string) --*

          The item type (folder or object).

        - **ETag** *(string) --*

          The ETag that represents a unique instance of the item.

        - **LastModified** *(datetime) --*

          The date and time that the item was last modified.

        - **ContentType** *(string) --*

          The content type of the item.

        - **ContentLength** *(integer) --*

          The length of the item in bytes.
    """
