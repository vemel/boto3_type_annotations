"Main interface for kinesis-video-media type defs"
from __future__ import annotations

from datetime import datetime
from typing_extensions import TypedDict


__all__ = ("ClientGetMediaResponseTypeDef", "ClientGetMediaStartSelectorTypeDef")


_ClientGetMediaResponseTypeDef = TypedDict(
    "_ClientGetMediaResponseTypeDef", {"ContentType": str}, total=False
)


class ClientGetMediaResponseTypeDef(_ClientGetMediaResponseTypeDef):
    """
    Type definition for `ClientGetMedia` `Response`

    - **ContentType** *(string) --*

      The content type of the requested media.

    - **Payload** (:class:`.StreamingBody`) --

      The payload Kinesis Video Streams returns is a sequence of chunks from the specified stream.
      For information about the chunks, see . The chunks that Kinesis Video Streams returns in the
      ``GetMedia`` call also include the following additional Matroska (MKV) tags:

      * AWS_KINESISVIDEO_CONTINUATION_TOKEN (UTF-8 string) - In the event your ``GetMedia`` call
      terminates, you can use this continuation token in your next request to get the next chunk
      where the last request terminated.

      * AWS_KINESISVIDEO_MILLIS_BEHIND_NOW (UTF-8 string) - Client applications can use this tag
      value to determine how far behind the chunk returned in the response is from the latest chunk
      on the stream.

      * AWS_KINESISVIDEO_FRAGMENT_NUMBER - Fragment number returned in the chunk.

      * AWS_KINESISVIDEO_SERVER_TIMESTAMP - Server timestamp of the fragment.

      * AWS_KINESISVIDEO_PRODUCER_TIMESTAMP - Producer timestamp of the fragment.

      The following tags will be present if an error occurs:

      * AWS_KINESISVIDEO_ERROR_CODE - String description of an error that caused GetMedia to stop.

      * AWS_KINESISVIDEO_ERROR_ID: Integer code of the error.

      The error codes are as follows:

      * 3002 - Error writing to the stream

      * 4000 - Requested fragment is not found

      * 4500 - Access denied for the stream's KMS key

      * 4501 - Stream's KMS key is disabled

      * 4502 - Validation error on the stream's KMS key

      * 4503 - KMS key specified in the stream is unavailable

      * 4504 - Invalid usage of the KMS key specified in the stream

      * 4505 - Invalid state of the KMS key specified in the stream

      * 4506 - Unable to find the KMS key specified in the stream

      * 5000 - Internal error
    """


_RequiredClientGetMediaStartSelectorTypeDef = TypedDict(
    "_RequiredClientGetMediaStartSelectorTypeDef", {"StartSelectorType": str}
)
_OptionalClientGetMediaStartSelectorTypeDef = TypedDict(
    "_OptionalClientGetMediaStartSelectorTypeDef",
    {"AfterFragmentNumber": str, "StartTimestamp": datetime, "ContinuationToken": str},
    total=False,
)


class ClientGetMediaStartSelectorTypeDef(
    _RequiredClientGetMediaStartSelectorTypeDef,
    _OptionalClientGetMediaStartSelectorTypeDef,
):
    """
    Type definition for `ClientGetMedia` `StartSelector`

    Identifies the starting chunk to get from the specified stream.

    - **StartSelectorType** *(string) --* **[REQUIRED]**

      Identifies the fragment on the Kinesis video stream where you want to start getting the data
      from.

      * NOW - Start with the latest chunk on the stream.

      * EARLIEST - Start with earliest available chunk on the stream.

      * FRAGMENT_NUMBER - Start with the chunk after a specific fragment. You must also specify the
      ``AfterFragmentNumber`` parameter.

      * PRODUCER_TIMESTAMP or SERVER_TIMESTAMP - Start with the chunk containing a fragment with the
      specified producer or server timestamp. You specify the timestamp by adding ``StartTimestamp`` .

      * CONTINUATION_TOKEN - Read using the specified continuation token.

      .. note::

        If you choose the NOW, EARLIEST, or CONTINUATION_TOKEN as the ``startSelectorType`` , you
        don't provide any additional information in the ``startSelector`` .

    - **AfterFragmentNumber** *(string) --*

      Specifies the fragment number from where you want the ``GetMedia`` API to start returning the
      fragments.

    - **StartTimestamp** *(datetime) --*

      A timestamp value. This value is required if you choose the PRODUCER_TIMESTAMP or the
      SERVER_TIMESTAMP as the ``startSelectorType`` . The ``GetMedia`` API then starts with the chunk
      containing the fragment that has the specified timestamp.

    - **ContinuationToken** *(string) --*

      Continuation token that Kinesis Video Streams returned in the previous ``GetMedia`` response.
      The ``GetMedia`` API then starts with the chunk identified by the continuation token.
    """
