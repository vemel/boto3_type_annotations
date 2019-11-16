"Main interface for kinesisvideo type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateStreamResponseTypeDef",
    "ClientDescribeStreamResponseStreamInfoTypeDef",
    "ClientDescribeStreamResponseTypeDef",
    "ClientGetDataEndpointResponseTypeDef",
    "ClientListStreamsResponseStreamInfoListTypeDef",
    "ClientListStreamsResponseTypeDef",
    "ClientListStreamsStreamNameConditionTypeDef",
    "ClientListTagsForStreamResponseTypeDef",
    "ListStreamsPaginatePaginationConfigTypeDef",
    "ListStreamsPaginateResponseStreamInfoListTypeDef",
    "ListStreamsPaginateResponseTypeDef",
    "ListStreamsPaginateStreamNameConditionTypeDef",
)


_ClientCreateStreamResponseTypeDef = TypedDict(
    "_ClientCreateStreamResponseTypeDef", {"StreamARN": str}, total=False
)


class ClientCreateStreamResponseTypeDef(_ClientCreateStreamResponseTypeDef):
    """
    Type definition for `ClientCreateStream` `Response`

    - **StreamARN** *(string) --*

      The Amazon Resource Name (ARN) of the stream.
    """


_ClientDescribeStreamResponseStreamInfoTypeDef = TypedDict(
    "_ClientDescribeStreamResponseStreamInfoTypeDef",
    {
        "DeviceName": str,
        "StreamName": str,
        "StreamARN": str,
        "MediaType": str,
        "KmsKeyId": str,
        "Version": str,
        "Status": str,
        "CreationTime": datetime,
        "DataRetentionInHours": int,
    },
    total=False,
)


class ClientDescribeStreamResponseStreamInfoTypeDef(
    _ClientDescribeStreamResponseStreamInfoTypeDef
):
    """
    Type definition for `ClientDescribeStreamResponse` `StreamInfo`

    An object that describes the stream.

    - **DeviceName** *(string) --*

      The name of the device that is associated with the stream.

    - **StreamName** *(string) --*

      The name of the stream.

    - **StreamARN** *(string) --*

      The Amazon Resource Name (ARN) of the stream.

    - **MediaType** *(string) --*

      The ``MediaType`` of the stream.

    - **KmsKeyId** *(string) --*

      The ID of the AWS Key Management Service (AWS KMS) key that Kinesis Video Streams uses to
      encrypt data on the stream.

    - **Version** *(string) --*

      The version of the stream.

    - **Status** *(string) --*

      The status of the stream.

    - **CreationTime** *(datetime) --*

      A time stamp that indicates when the stream was created.

    - **DataRetentionInHours** *(integer) --*

      How long the stream retains data, in hours.
    """


_ClientDescribeStreamResponseTypeDef = TypedDict(
    "_ClientDescribeStreamResponseTypeDef",
    {"StreamInfo": ClientDescribeStreamResponseStreamInfoTypeDef},
    total=False,
)


class ClientDescribeStreamResponseTypeDef(_ClientDescribeStreamResponseTypeDef):
    """
    Type definition for `ClientDescribeStream` `Response`

    - **StreamInfo** *(dict) --*

      An object that describes the stream.

      - **DeviceName** *(string) --*

        The name of the device that is associated with the stream.

      - **StreamName** *(string) --*

        The name of the stream.

      - **StreamARN** *(string) --*

        The Amazon Resource Name (ARN) of the stream.

      - **MediaType** *(string) --*

        The ``MediaType`` of the stream.

      - **KmsKeyId** *(string) --*

        The ID of the AWS Key Management Service (AWS KMS) key that Kinesis Video Streams uses to
        encrypt data on the stream.

      - **Version** *(string) --*

        The version of the stream.

      - **Status** *(string) --*

        The status of the stream.

      - **CreationTime** *(datetime) --*

        A time stamp that indicates when the stream was created.

      - **DataRetentionInHours** *(integer) --*

        How long the stream retains data, in hours.
    """


_ClientGetDataEndpointResponseTypeDef = TypedDict(
    "_ClientGetDataEndpointResponseTypeDef", {"DataEndpoint": str}, total=False
)


class ClientGetDataEndpointResponseTypeDef(_ClientGetDataEndpointResponseTypeDef):
    """
    Type definition for `ClientGetDataEndpoint` `Response`

    - **DataEndpoint** *(string) --*

      The endpoint value. To read data from the stream or to write data to it, specify this
      endpoint in your application.
    """


_ClientListStreamsResponseStreamInfoListTypeDef = TypedDict(
    "_ClientListStreamsResponseStreamInfoListTypeDef",
    {
        "DeviceName": str,
        "StreamName": str,
        "StreamARN": str,
        "MediaType": str,
        "KmsKeyId": str,
        "Version": str,
        "Status": str,
        "CreationTime": datetime,
        "DataRetentionInHours": int,
    },
    total=False,
)


class ClientListStreamsResponseStreamInfoListTypeDef(
    _ClientListStreamsResponseStreamInfoListTypeDef
):
    """
    Type definition for `ClientListStreamsResponse` `StreamInfoList`

    An object describing a Kinesis video stream.

    - **DeviceName** *(string) --*

      The name of the device that is associated with the stream.

    - **StreamName** *(string) --*

      The name of the stream.

    - **StreamARN** *(string) --*

      The Amazon Resource Name (ARN) of the stream.

    - **MediaType** *(string) --*

      The ``MediaType`` of the stream.

    - **KmsKeyId** *(string) --*

      The ID of the AWS Key Management Service (AWS KMS) key that Kinesis Video Streams uses to
      encrypt data on the stream.

    - **Version** *(string) --*

      The version of the stream.

    - **Status** *(string) --*

      The status of the stream.

    - **CreationTime** *(datetime) --*

      A time stamp that indicates when the stream was created.

    - **DataRetentionInHours** *(integer) --*

      How long the stream retains data, in hours.
    """


_ClientListStreamsResponseTypeDef = TypedDict(
    "_ClientListStreamsResponseTypeDef",
    {
        "StreamInfoList": List[ClientListStreamsResponseStreamInfoListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListStreamsResponseTypeDef(_ClientListStreamsResponseTypeDef):
    """
    Type definition for `ClientListStreams` `Response`

    - **StreamInfoList** *(list) --*

      An array of ``StreamInfo`` objects.

      - *(dict) --*

        An object describing a Kinesis video stream.

        - **DeviceName** *(string) --*

          The name of the device that is associated with the stream.

        - **StreamName** *(string) --*

          The name of the stream.

        - **StreamARN** *(string) --*

          The Amazon Resource Name (ARN) of the stream.

        - **MediaType** *(string) --*

          The ``MediaType`` of the stream.

        - **KmsKeyId** *(string) --*

          The ID of the AWS Key Management Service (AWS KMS) key that Kinesis Video Streams uses to
          encrypt data on the stream.

        - **Version** *(string) --*

          The version of the stream.

        - **Status** *(string) --*

          The status of the stream.

        - **CreationTime** *(datetime) --*

          A time stamp that indicates when the stream was created.

        - **DataRetentionInHours** *(integer) --*

          How long the stream retains data, in hours.

    - **NextToken** *(string) --*

      If the response is truncated, the call returns this element with a token. To get the next
      batch of streams, use this token in your next request.
    """


_ClientListStreamsStreamNameConditionTypeDef = TypedDict(
    "_ClientListStreamsStreamNameConditionTypeDef",
    {"ComparisonOperator": str, "ComparisonValue": str},
    total=False,
)


class ClientListStreamsStreamNameConditionTypeDef(
    _ClientListStreamsStreamNameConditionTypeDef
):
    """
    Type definition for `ClientListStreams` `StreamNameCondition`

    Optional: Returns only streams that satisfy a specific condition. Currently, you can specify only
    the prefix of a stream name as a condition.

    - **ComparisonOperator** *(string) --*

      A comparison operator. Currently, you can specify only the ``BEGINS_WITH`` operator, which
      finds streams whose names start with a given prefix.

    - **ComparisonValue** *(string) --*

      A value to compare.
    """


_ClientListTagsForStreamResponseTypeDef = TypedDict(
    "_ClientListTagsForStreamResponseTypeDef",
    {"NextToken": str, "Tags": Dict[str, str]},
    total=False,
)


class ClientListTagsForStreamResponseTypeDef(_ClientListTagsForStreamResponseTypeDef):
    """
    Type definition for `ClientListTagsForStream` `Response`

    - **NextToken** *(string) --*

      If you specify this parameter and the result of a ``ListTags`` call is truncated, the
      response includes a token that you can use in the next request to fetch the next set of tags.

    - **Tags** *(dict) --*

      A map of tag keys and values associated with the specified stream.

      - *(string) --*

        - *(string) --*
    """


_ListStreamsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListStreamsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListStreamsPaginatePaginationConfigTypeDef(
    _ListStreamsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListStreamsPaginate` `PaginationConfig`

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


_ListStreamsPaginateResponseStreamInfoListTypeDef = TypedDict(
    "_ListStreamsPaginateResponseStreamInfoListTypeDef",
    {
        "DeviceName": str,
        "StreamName": str,
        "StreamARN": str,
        "MediaType": str,
        "KmsKeyId": str,
        "Version": str,
        "Status": str,
        "CreationTime": datetime,
        "DataRetentionInHours": int,
    },
    total=False,
)


class ListStreamsPaginateResponseStreamInfoListTypeDef(
    _ListStreamsPaginateResponseStreamInfoListTypeDef
):
    """
    Type definition for `ListStreamsPaginateResponse` `StreamInfoList`

    An object describing a Kinesis video stream.

    - **DeviceName** *(string) --*

      The name of the device that is associated with the stream.

    - **StreamName** *(string) --*

      The name of the stream.

    - **StreamARN** *(string) --*

      The Amazon Resource Name (ARN) of the stream.

    - **MediaType** *(string) --*

      The ``MediaType`` of the stream.

    - **KmsKeyId** *(string) --*

      The ID of the AWS Key Management Service (AWS KMS) key that Kinesis Video Streams uses to
      encrypt data on the stream.

    - **Version** *(string) --*

      The version of the stream.

    - **Status** *(string) --*

      The status of the stream.

    - **CreationTime** *(datetime) --*

      A time stamp that indicates when the stream was created.

    - **DataRetentionInHours** *(integer) --*

      How long the stream retains data, in hours.
    """


_ListStreamsPaginateResponseTypeDef = TypedDict(
    "_ListStreamsPaginateResponseTypeDef",
    {"StreamInfoList": List[ListStreamsPaginateResponseStreamInfoListTypeDef]},
    total=False,
)


class ListStreamsPaginateResponseTypeDef(_ListStreamsPaginateResponseTypeDef):
    """
    Type definition for `ListStreamsPaginate` `Response`

    - **StreamInfoList** *(list) --*

      An array of ``StreamInfo`` objects.

      - *(dict) --*

        An object describing a Kinesis video stream.

        - **DeviceName** *(string) --*

          The name of the device that is associated with the stream.

        - **StreamName** *(string) --*

          The name of the stream.

        - **StreamARN** *(string) --*

          The Amazon Resource Name (ARN) of the stream.

        - **MediaType** *(string) --*

          The ``MediaType`` of the stream.

        - **KmsKeyId** *(string) --*

          The ID of the AWS Key Management Service (AWS KMS) key that Kinesis Video Streams uses to
          encrypt data on the stream.

        - **Version** *(string) --*

          The version of the stream.

        - **Status** *(string) --*

          The status of the stream.

        - **CreationTime** *(datetime) --*

          A time stamp that indicates when the stream was created.

        - **DataRetentionInHours** *(integer) --*

          How long the stream retains data, in hours.
    """


_ListStreamsPaginateStreamNameConditionTypeDef = TypedDict(
    "_ListStreamsPaginateStreamNameConditionTypeDef",
    {"ComparisonOperator": str, "ComparisonValue": str},
    total=False,
)


class ListStreamsPaginateStreamNameConditionTypeDef(
    _ListStreamsPaginateStreamNameConditionTypeDef
):
    """
    Type definition for `ListStreamsPaginate` `StreamNameCondition`

    Optional: Returns only streams that satisfy a specific condition. Currently, you can specify only
    the prefix of a stream name as a condition.

    - **ComparisonOperator** *(string) --*

      A comparison operator. Currently, you can specify only the ``BEGINS_WITH`` operator, which
      finds streams whose names start with a given prefix.

    - **ComparisonValue** *(string) --*

      A value to compare.
    """
