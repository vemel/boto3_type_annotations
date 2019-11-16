"Main interface for resourcegroupstaggingapi type defs"
from __future__ import annotations

from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientGetResourcesResponseResourceTagMappingListTagsTypeDef",
    "ClientGetResourcesResponseResourceTagMappingListTypeDef",
    "ClientGetResourcesResponseTypeDef",
    "ClientGetResourcesTagFiltersTypeDef",
    "ClientGetTagKeysResponseTypeDef",
    "ClientGetTagValuesResponseTypeDef",
    "ClientTagResourcesResponseFailedResourcesMapTypeDef",
    "ClientTagResourcesResponseTypeDef",
    "ClientUntagResourcesResponseFailedResourcesMapTypeDef",
    "ClientUntagResourcesResponseTypeDef",
    "GetResourcesPaginatePaginationConfigTypeDef",
    "GetResourcesPaginateResponseResourceTagMappingListTagsTypeDef",
    "GetResourcesPaginateResponseResourceTagMappingListTypeDef",
    "GetResourcesPaginateResponseTypeDef",
    "GetResourcesPaginateTagFiltersTypeDef",
    "GetTagKeysPaginatePaginationConfigTypeDef",
    "GetTagKeysPaginateResponseTypeDef",
    "GetTagValuesPaginatePaginationConfigTypeDef",
    "GetTagValuesPaginateResponseTypeDef",
)


_ClientGetResourcesResponseResourceTagMappingListTagsTypeDef = TypedDict(
    "_ClientGetResourcesResponseResourceTagMappingListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetResourcesResponseResourceTagMappingListTagsTypeDef(
    _ClientGetResourcesResponseResourceTagMappingListTagsTypeDef
):
    """
    Type definition for `ClientGetResourcesResponseResourceTagMappingList` `Tags`

    The metadata that you apply to AWS resources to help you categorize and organize them.
    Each tag consists of a key and an optional value, both of which you define. For more
    information, see `Tag Basics
    <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-basics>`__ in
    the *Amazon EC2 User Guide for Linux Instances* .

    - **Key** *(string) --*

      One part of a key-value pair that make up a tag. A key is a general label that acts
      like a category for more specific tag values.

    - **Value** *(string) --*

      The optional part of a key-value pair that make up a tag. A value acts as a
      descriptor within a tag category (key).
    """


_ClientGetResourcesResponseResourceTagMappingListTypeDef = TypedDict(
    "_ClientGetResourcesResponseResourceTagMappingListTypeDef",
    {
        "ResourceARN": str,
        "Tags": List[ClientGetResourcesResponseResourceTagMappingListTagsTypeDef],
    },
    total=False,
)


class ClientGetResourcesResponseResourceTagMappingListTypeDef(
    _ClientGetResourcesResponseResourceTagMappingListTypeDef
):
    """
    Type definition for `ClientGetResourcesResponse` `ResourceTagMappingList`

    A list of resource ARNs and the tags (keys and values) that are associated with each.

    - **ResourceARN** *(string) --*

      The ARN of the resource.

    - **Tags** *(list) --*

      The tags that have been applied to one or more AWS resources.

      - *(dict) --*

        The metadata that you apply to AWS resources to help you categorize and organize them.
        Each tag consists of a key and an optional value, both of which you define. For more
        information, see `Tag Basics
        <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-basics>`__ in
        the *Amazon EC2 User Guide for Linux Instances* .

        - **Key** *(string) --*

          One part of a key-value pair that make up a tag. A key is a general label that acts
          like a category for more specific tag values.

        - **Value** *(string) --*

          The optional part of a key-value pair that make up a tag. A value acts as a
          descriptor within a tag category (key).
    """


_ClientGetResourcesResponseTypeDef = TypedDict(
    "_ClientGetResourcesResponseTypeDef",
    {
        "PaginationToken": str,
        "ResourceTagMappingList": List[
            ClientGetResourcesResponseResourceTagMappingListTypeDef
        ],
    },
    total=False,
)


class ClientGetResourcesResponseTypeDef(_ClientGetResourcesResponseTypeDef):
    """
    Type definition for `ClientGetResources` `Response`

    - **PaginationToken** *(string) --*

      A string that indicates that the response contains more data than can be returned in a single
      response. To receive additional data, specify this string for the ``PaginationToken`` value
      in a subsequent request.

    - **ResourceTagMappingList** *(list) --*

      A list of resource ARNs and the tags (keys and values) associated with each.

      - *(dict) --*

        A list of resource ARNs and the tags (keys and values) that are associated with each.

        - **ResourceARN** *(string) --*

          The ARN of the resource.

        - **Tags** *(list) --*

          The tags that have been applied to one or more AWS resources.

          - *(dict) --*

            The metadata that you apply to AWS resources to help you categorize and organize them.
            Each tag consists of a key and an optional value, both of which you define. For more
            information, see `Tag Basics
            <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-basics>`__ in
            the *Amazon EC2 User Guide for Linux Instances* .

            - **Key** *(string) --*

              One part of a key-value pair that make up a tag. A key is a general label that acts
              like a category for more specific tag values.

            - **Value** *(string) --*

              The optional part of a key-value pair that make up a tag. A value acts as a
              descriptor within a tag category (key).
    """


_ClientGetResourcesTagFiltersTypeDef = TypedDict(
    "_ClientGetResourcesTagFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetResourcesTagFiltersTypeDef(_ClientGetResourcesTagFiltersTypeDef):
    """
    Type definition for `ClientGetResources` `TagFilters`

    A list of tags (keys and values) that are used to specify the associated resources.

    - **Key** *(string) --*

      One part of a key-value pair that make up a tag. A key is a general label that acts like a
      category for more specific tag values.

    - **Values** *(list) --*

      The optional part of a key-value pair that make up a tag. A value acts as a descriptor within
      a tag category (key).

      - *(string) --*
    """


_ClientGetTagKeysResponseTypeDef = TypedDict(
    "_ClientGetTagKeysResponseTypeDef",
    {"PaginationToken": str, "TagKeys": List[str]},
    total=False,
)


class ClientGetTagKeysResponseTypeDef(_ClientGetTagKeysResponseTypeDef):
    """
    Type definition for `ClientGetTagKeys` `Response`

    - **PaginationToken** *(string) --*

      A string that indicates that the response contains more data than can be returned in a single
      response. To receive additional data, specify this string for the ``PaginationToken`` value
      in a subsequent request.

    - **TagKeys** *(list) --*

      A list of all tag keys in the AWS account.

      - *(string) --*
    """


_ClientGetTagValuesResponseTypeDef = TypedDict(
    "_ClientGetTagValuesResponseTypeDef",
    {"PaginationToken": str, "TagValues": List[str]},
    total=False,
)


class ClientGetTagValuesResponseTypeDef(_ClientGetTagValuesResponseTypeDef):
    """
    Type definition for `ClientGetTagValues` `Response`

    - **PaginationToken** *(string) --*

      A string that indicates that the response contains more data than can be returned in a single
      response. To receive additional data, specify this string for the ``PaginationToken`` value
      in a subsequent request.

    - **TagValues** *(list) --*

      A list of all tag values for the specified key in the AWS account.

      - *(string) --*
    """


_ClientTagResourcesResponseFailedResourcesMapTypeDef = TypedDict(
    "_ClientTagResourcesResponseFailedResourcesMapTypeDef",
    {"StatusCode": int, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientTagResourcesResponseFailedResourcesMapTypeDef(
    _ClientTagResourcesResponseFailedResourcesMapTypeDef
):
    """
    Type definition for `ClientTagResourcesResponse` `FailedResourcesMap`

    Details of the common errors that all actions return.

    - **StatusCode** *(integer) --*

      The HTTP status code of the common error.

    - **ErrorCode** *(string) --*

      The code of the common error. Valid values include ``InternalServiceException`` ,
      ``InvalidParameterException`` , and any valid error code returned by the AWS service
      that hosts the resource that you want to tag.

    - **ErrorMessage** *(string) --*

      The message of the common error.
    """


_ClientTagResourcesResponseTypeDef = TypedDict(
    "_ClientTagResourcesResponseTypeDef",
    {
        "FailedResourcesMap": Dict[
            str, ClientTagResourcesResponseFailedResourcesMapTypeDef
        ]
    },
    total=False,
)


class ClientTagResourcesResponseTypeDef(_ClientTagResourcesResponseTypeDef):
    """
    Type definition for `ClientTagResources` `Response`

    - **FailedResourcesMap** *(dict) --*

      Details of resources that could not be tagged. An error code, status code, and error message
      are returned for each failed item.

      - *(string) --*

        - *(dict) --*

          Details of the common errors that all actions return.

          - **StatusCode** *(integer) --*

            The HTTP status code of the common error.

          - **ErrorCode** *(string) --*

            The code of the common error. Valid values include ``InternalServiceException`` ,
            ``InvalidParameterException`` , and any valid error code returned by the AWS service
            that hosts the resource that you want to tag.

          - **ErrorMessage** *(string) --*

            The message of the common error.
    """


_ClientUntagResourcesResponseFailedResourcesMapTypeDef = TypedDict(
    "_ClientUntagResourcesResponseFailedResourcesMapTypeDef",
    {"StatusCode": int, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientUntagResourcesResponseFailedResourcesMapTypeDef(
    _ClientUntagResourcesResponseFailedResourcesMapTypeDef
):
    """
    Type definition for `ClientUntagResourcesResponse` `FailedResourcesMap`

    Details of the common errors that all actions return.

    - **StatusCode** *(integer) --*

      The HTTP status code of the common error.

    - **ErrorCode** *(string) --*

      The code of the common error. Valid values include ``InternalServiceException`` ,
      ``InvalidParameterException`` , and any valid error code returned by the AWS service
      that hosts the resource that you want to tag.

    - **ErrorMessage** *(string) --*

      The message of the common error.
    """


_ClientUntagResourcesResponseTypeDef = TypedDict(
    "_ClientUntagResourcesResponseTypeDef",
    {
        "FailedResourcesMap": Dict[
            str, ClientUntagResourcesResponseFailedResourcesMapTypeDef
        ]
    },
    total=False,
)


class ClientUntagResourcesResponseTypeDef(_ClientUntagResourcesResponseTypeDef):
    """
    Type definition for `ClientUntagResources` `Response`

    - **FailedResourcesMap** *(dict) --*

      Details of resources that could not be untagged. An error code, status code, and error
      message are returned for each failed item.

      - *(string) --*

        - *(dict) --*

          Details of the common errors that all actions return.

          - **StatusCode** *(integer) --*

            The HTTP status code of the common error.

          - **ErrorCode** *(string) --*

            The code of the common error. Valid values include ``InternalServiceException`` ,
            ``InvalidParameterException`` , and any valid error code returned by the AWS service
            that hosts the resource that you want to tag.

          - **ErrorMessage** *(string) --*

            The message of the common error.
    """


_GetResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetResourcesPaginatePaginationConfigTypeDef(
    _GetResourcesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetResourcesPaginate` `PaginationConfig`

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


_GetResourcesPaginateResponseResourceTagMappingListTagsTypeDef = TypedDict(
    "_GetResourcesPaginateResponseResourceTagMappingListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class GetResourcesPaginateResponseResourceTagMappingListTagsTypeDef(
    _GetResourcesPaginateResponseResourceTagMappingListTagsTypeDef
):
    """
    Type definition for `GetResourcesPaginateResponseResourceTagMappingList` `Tags`

    The metadata that you apply to AWS resources to help you categorize and organize them.
    Each tag consists of a key and an optional value, both of which you define. For more
    information, see `Tag Basics
    <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-basics>`__ in
    the *Amazon EC2 User Guide for Linux Instances* .

    - **Key** *(string) --*

      One part of a key-value pair that make up a tag. A key is a general label that acts
      like a category for more specific tag values.

    - **Value** *(string) --*

      The optional part of a key-value pair that make up a tag. A value acts as a
      descriptor within a tag category (key).
    """


_GetResourcesPaginateResponseResourceTagMappingListTypeDef = TypedDict(
    "_GetResourcesPaginateResponseResourceTagMappingListTypeDef",
    {
        "ResourceARN": str,
        "Tags": List[GetResourcesPaginateResponseResourceTagMappingListTagsTypeDef],
    },
    total=False,
)


class GetResourcesPaginateResponseResourceTagMappingListTypeDef(
    _GetResourcesPaginateResponseResourceTagMappingListTypeDef
):
    """
    Type definition for `GetResourcesPaginateResponse` `ResourceTagMappingList`

    A list of resource ARNs and the tags (keys and values) that are associated with each.

    - **ResourceARN** *(string) --*

      The ARN of the resource.

    - **Tags** *(list) --*

      The tags that have been applied to one or more AWS resources.

      - *(dict) --*

        The metadata that you apply to AWS resources to help you categorize and organize them.
        Each tag consists of a key and an optional value, both of which you define. For more
        information, see `Tag Basics
        <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-basics>`__ in
        the *Amazon EC2 User Guide for Linux Instances* .

        - **Key** *(string) --*

          One part of a key-value pair that make up a tag. A key is a general label that acts
          like a category for more specific tag values.

        - **Value** *(string) --*

          The optional part of a key-value pair that make up a tag. A value acts as a
          descriptor within a tag category (key).
    """


_GetResourcesPaginateResponseTypeDef = TypedDict(
    "_GetResourcesPaginateResponseTypeDef",
    {
        "ResourceTagMappingList": List[
            GetResourcesPaginateResponseResourceTagMappingListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class GetResourcesPaginateResponseTypeDef(_GetResourcesPaginateResponseTypeDef):
    """
    Type definition for `GetResourcesPaginate` `Response`

    - **ResourceTagMappingList** *(list) --*

      A list of resource ARNs and the tags (keys and values) associated with each.

      - *(dict) --*

        A list of resource ARNs and the tags (keys and values) that are associated with each.

        - **ResourceARN** *(string) --*

          The ARN of the resource.

        - **Tags** *(list) --*

          The tags that have been applied to one or more AWS resources.

          - *(dict) --*

            The metadata that you apply to AWS resources to help you categorize and organize them.
            Each tag consists of a key and an optional value, both of which you define. For more
            information, see `Tag Basics
            <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-basics>`__ in
            the *Amazon EC2 User Guide for Linux Instances* .

            - **Key** *(string) --*

              One part of a key-value pair that make up a tag. A key is a general label that acts
              like a category for more specific tag values.

            - **Value** *(string) --*

              The optional part of a key-value pair that make up a tag. A value acts as a
              descriptor within a tag category (key).

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_GetResourcesPaginateTagFiltersTypeDef = TypedDict(
    "_GetResourcesPaginateTagFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class GetResourcesPaginateTagFiltersTypeDef(_GetResourcesPaginateTagFiltersTypeDef):
    """
    Type definition for `GetResourcesPaginate` `TagFilters`

    A list of tags (keys and values) that are used to specify the associated resources.

    - **Key** *(string) --*

      One part of a key-value pair that make up a tag. A key is a general label that acts like a
      category for more specific tag values.

    - **Values** *(list) --*

      The optional part of a key-value pair that make up a tag. A value acts as a descriptor within
      a tag category (key).

      - *(string) --*
    """


_GetTagKeysPaginatePaginationConfigTypeDef = TypedDict(
    "_GetTagKeysPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetTagKeysPaginatePaginationConfigTypeDef(
    _GetTagKeysPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetTagKeysPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetTagKeysPaginateResponseTypeDef = TypedDict(
    "_GetTagKeysPaginateResponseTypeDef",
    {"TagKeys": List[str], "NextToken": str},
    total=False,
)


class GetTagKeysPaginateResponseTypeDef(_GetTagKeysPaginateResponseTypeDef):
    """
    Type definition for `GetTagKeysPaginate` `Response`

    - **TagKeys** *(list) --*

      A list of all tag keys in the AWS account.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_GetTagValuesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetTagValuesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetTagValuesPaginatePaginationConfigTypeDef(
    _GetTagValuesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetTagValuesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetTagValuesPaginateResponseTypeDef = TypedDict(
    "_GetTagValuesPaginateResponseTypeDef",
    {"TagValues": List[str], "NextToken": str},
    total=False,
)


class GetTagValuesPaginateResponseTypeDef(_GetTagValuesPaginateResponseTypeDef):
    """
    Type definition for `GetTagValuesPaginate` `Response`

    - **TagValues** *(list) --*

      A list of all tag values for the specified key in the AWS account.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """
