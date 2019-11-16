"Main interface for kinesis-video-archived-media type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientGetDashStreamingSessionUrlDASHFragmentSelectorTimestampRangeTypeDef",
    "ClientGetDashStreamingSessionUrlDASHFragmentSelectorTypeDef",
    "ClientGetDashStreamingSessionUrlResponseTypeDef",
    "ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTimestampRangeTypeDef",
    "ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTypeDef",
    "ClientGetHlsStreamingSessionUrlResponseTypeDef",
    "ClientGetMediaForFragmentListResponseTypeDef",
    "ClientListFragmentsFragmentSelectorTimestampRangeTypeDef",
    "ClientListFragmentsFragmentSelectorTypeDef",
    "ClientListFragmentsResponseFragmentsTypeDef",
    "ClientListFragmentsResponseTypeDef",
    "ListFragmentsPaginateFragmentSelectorTimestampRangeTypeDef",
    "ListFragmentsPaginateFragmentSelectorTypeDef",
    "ListFragmentsPaginatePaginationConfigTypeDef",
    "ListFragmentsPaginateResponseFragmentsTypeDef",
    "ListFragmentsPaginateResponseTypeDef",
)


_ClientGetDashStreamingSessionUrlDASHFragmentSelectorTimestampRangeTypeDef = TypedDict(
    "_ClientGetDashStreamingSessionUrlDASHFragmentSelectorTimestampRangeTypeDef",
    {"StartTimestamp": datetime, "EndTimestamp": datetime},
    total=False,
)


class ClientGetDashStreamingSessionUrlDASHFragmentSelectorTimestampRangeTypeDef(
    _ClientGetDashStreamingSessionUrlDASHFragmentSelectorTimestampRangeTypeDef
):
    """
    Type definition for `ClientGetDashStreamingSessionUrlDASHFragmentSelector` `TimestampRange`

    The start and end of the timestamp range for the requested media.

    This value should not be present if ``PlaybackType`` is ``LIVE`` .

    - **StartTimestamp** *(datetime) --*

      The start of the timestamp range for the requested media.

      If the ``DASHTimestampRange`` value is specified, the ``StartTimestamp`` value is required.

      .. note::

        This value is inclusive. Fragments that start before the ``StartTimestamp`` and continue
        past it are included in the session. If ``FragmentSelectorType`` is ``SERVER_TIMESTAMP`` ,
        the ``StartTimestamp`` must be later than the stream head.

    - **EndTimestamp** *(datetime) --*

      The end of the timestamp range for the requested media. This value must be within 3 hours of
      the specified ``StartTimestamp`` , and it must be later than the ``StartTimestamp`` value.

      If ``FragmentSelectorType`` for the request is ``SERVER_TIMESTAMP`` , this value must be in
      the past.

      The ``EndTimestamp`` value is required for ``ON_DEMAND`` mode, but optional for
      ``LIVE_REPLAY`` mode. If the ``EndTimestamp`` is not set for ``LIVE_REPLAY`` mode then the
      session will continue to include newly ingested fragments until the session expires.

      .. note::

        This value is inclusive. The ``EndTimestamp`` is compared to the (starting) timestamp of
        the fragment. Fragments that start before the ``EndTimestamp`` value and continue past it
        are included in the session.
    """


_ClientGetDashStreamingSessionUrlDASHFragmentSelectorTypeDef = TypedDict(
    "_ClientGetDashStreamingSessionUrlDASHFragmentSelectorTypeDef",
    {
        "FragmentSelectorType": str,
        "TimestampRange": ClientGetDashStreamingSessionUrlDASHFragmentSelectorTimestampRangeTypeDef,
    },
    total=False,
)


class ClientGetDashStreamingSessionUrlDASHFragmentSelectorTypeDef(
    _ClientGetDashStreamingSessionUrlDASHFragmentSelectorTypeDef
):
    """
    Type definition for `ClientGetDashStreamingSessionUrl` `DASHFragmentSelector`

    The time range of the requested fragment and the source of the timestamps.

    This parameter is required if ``PlaybackMode`` is ``ON_DEMAND`` or ``LIVE_REPLAY`` . This
    parameter is optional if PlaybackMode is ``LIVE`` . If ``PlaybackMode`` is ``LIVE`` , the
    ``FragmentSelectorType`` can be set, but the ``TimestampRange`` should not be set. If
    ``PlaybackMode`` is ``ON_DEMAND`` or ``LIVE_REPLAY`` , both ``FragmentSelectorType`` and
    ``TimestampRange`` must be set.

    - **FragmentSelectorType** *(string) --*

      The source of the timestamps for the requested media.

      When ``FragmentSelectorType`` is set to ``PRODUCER_TIMESTAMP`` and
      GetDASHStreamingSessionURLInput$PlaybackMode is ``ON_DEMAND`` or ``LIVE_REPLAY`` , the first
      fragment ingested with a producer timestamp within the specified
      FragmentSelector$TimestampRange is included in the media playlist. In addition, the fragments
      with producer timestamps within the ``TimestampRange`` ingested immediately following the first
      fragment (up to the  GetDASHStreamingSessionURLInput$MaxManifestFragmentResults value) are
      included.

      Fragments that have duplicate producer timestamps are deduplicated. This means that if
      producers are producing a stream of fragments with producer timestamps that are approximately
      equal to the true clock time, the MPEG-DASH manifest will contain all of the fragments within
      the requested timestamp range. If some fragments are ingested within the same time range and
      very different points in time, only the oldest ingested collection of fragments are returned.

      When ``FragmentSelectorType`` is set to ``PRODUCER_TIMESTAMP`` and
      GetDASHStreamingSessionURLInput$PlaybackMode is ``LIVE`` , the producer timestamps are used in
      the MP4 fragments and for deduplication. But the most recently ingested fragments based on
      server timestamps are included in the MPEG-DASH manifest. This means that even if fragments
      ingested in the past have producer timestamps with values now, they are not included in the HLS
      media playlist.

      The default is ``SERVER_TIMESTAMP`` .

    - **TimestampRange** *(dict) --*

      The start and end of the timestamp range for the requested media.

      This value should not be present if ``PlaybackType`` is ``LIVE`` .

      - **StartTimestamp** *(datetime) --*

        The start of the timestamp range for the requested media.

        If the ``DASHTimestampRange`` value is specified, the ``StartTimestamp`` value is required.

        .. note::

          This value is inclusive. Fragments that start before the ``StartTimestamp`` and continue
          past it are included in the session. If ``FragmentSelectorType`` is ``SERVER_TIMESTAMP`` ,
          the ``StartTimestamp`` must be later than the stream head.

      - **EndTimestamp** *(datetime) --*

        The end of the timestamp range for the requested media. This value must be within 3 hours of
        the specified ``StartTimestamp`` , and it must be later than the ``StartTimestamp`` value.

        If ``FragmentSelectorType`` for the request is ``SERVER_TIMESTAMP`` , this value must be in
        the past.

        The ``EndTimestamp`` value is required for ``ON_DEMAND`` mode, but optional for
        ``LIVE_REPLAY`` mode. If the ``EndTimestamp`` is not set for ``LIVE_REPLAY`` mode then the
        session will continue to include newly ingested fragments until the session expires.

        .. note::

          This value is inclusive. The ``EndTimestamp`` is compared to the (starting) timestamp of
          the fragment. Fragments that start before the ``EndTimestamp`` value and continue past it
          are included in the session.
    """


_ClientGetDashStreamingSessionUrlResponseTypeDef = TypedDict(
    "_ClientGetDashStreamingSessionUrlResponseTypeDef",
    {"DASHStreamingSessionURL": str},
    total=False,
)


class ClientGetDashStreamingSessionUrlResponseTypeDef(
    _ClientGetDashStreamingSessionUrlResponseTypeDef
):
    """
    Type definition for `ClientGetDashStreamingSessionUrl` `Response`

    - **DASHStreamingSessionURL** *(string) --*

      The URL (containing the session token) that a media player can use to retrieve the MPEG-DASH
      manifest.
    """


_ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTimestampRangeTypeDef = TypedDict(
    "_ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTimestampRangeTypeDef",
    {"StartTimestamp": datetime, "EndTimestamp": datetime},
    total=False,
)


class ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTimestampRangeTypeDef(
    _ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTimestampRangeTypeDef
):
    """
    Type definition for `ClientGetHlsStreamingSessionUrlHLSFragmentSelector` `TimestampRange`

    The start and end of the timestamp range for the requested media.

    This value should not be present if ``PlaybackType`` is ``LIVE`` .

    - **StartTimestamp** *(datetime) --*

      The start of the timestamp range for the requested media.

      If the ``HLSTimestampRange`` value is specified, the ``StartTimestamp`` value is required.

      .. note::

        This value is inclusive. Fragments that start before the ``StartTimestamp`` and continue
        past it are included in the session. If ``FragmentSelectorType`` is ``SERVER_TIMESTAMP`` ,
        the ``StartTimestamp`` must be later than the stream head.

    - **EndTimestamp** *(datetime) --*

      The end of the timestamp range for the requested media. This value must be within 3 hours of
      the specified ``StartTimestamp`` , and it must be later than the ``StartTimestamp`` value.

      If ``FragmentSelectorType`` for the request is ``SERVER_TIMESTAMP`` , this value must be in
      the past.

      The ``EndTimestamp`` value is required for ``ON_DEMAND`` mode, but optional for
      ``LIVE_REPLAY`` mode. If the ``EndTimestamp`` is not set for ``LIVE_REPLAY`` mode then the
      session will continue to include newly ingested fragments until the session expires.

      .. note::

        This value is inclusive. The ``EndTimestamp`` is compared to the (starting) timestamp of
        the fragment. Fragments that start before the ``EndTimestamp`` value and continue past it
        are included in the session.
    """


_ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTypeDef = TypedDict(
    "_ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTypeDef",
    {
        "FragmentSelectorType": str,
        "TimestampRange": ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTimestampRangeTypeDef,
    },
    total=False,
)


class ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTypeDef(
    _ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTypeDef
):
    """
    Type definition for `ClientGetHlsStreamingSessionUrl` `HLSFragmentSelector`

    The time range of the requested fragment and the source of the timestamps.

    This parameter is required if ``PlaybackMode`` is ``ON_DEMAND`` or ``LIVE_REPLAY`` . This
    parameter is optional if PlaybackMode is ``LIVE`` . If ``PlaybackMode`` is ``LIVE`` , the
    ``FragmentSelectorType`` can be set, but the ``TimestampRange`` should not be set. If
    ``PlaybackMode`` is ``ON_DEMAND`` or ``LIVE_REPLAY`` , both ``FragmentSelectorType`` and
    ``TimestampRange`` must be set.

    - **FragmentSelectorType** *(string) --*

      The source of the timestamps for the requested media.

      When ``FragmentSelectorType`` is set to ``PRODUCER_TIMESTAMP`` and
      GetHLSStreamingSessionURLInput$PlaybackMode is ``ON_DEMAND`` or ``LIVE_REPLAY`` , the first
      fragment ingested with a producer timestamp within the specified
      FragmentSelector$TimestampRange is included in the media playlist. In addition, the fragments
      with producer timestamps within the ``TimestampRange`` ingested immediately following the first
      fragment (up to the  GetHLSStreamingSessionURLInput$MaxMediaPlaylistFragmentResults value) are
      included.

      Fragments that have duplicate producer timestamps are deduplicated. This means that if
      producers are producing a stream of fragments with producer timestamps that are approximately
      equal to the true clock time, the HLS media playlists will contain all of the fragments within
      the requested timestamp range. If some fragments are ingested within the same time range and
      very different points in time, only the oldest ingested collection of fragments are returned.

      When ``FragmentSelectorType`` is set to ``PRODUCER_TIMESTAMP`` and
      GetHLSStreamingSessionURLInput$PlaybackMode is ``LIVE`` , the producer timestamps are used in
      the MP4 fragments and for deduplication. But the most recently ingested fragments based on
      server timestamps are included in the HLS media playlist. This means that even if fragments
      ingested in the past have producer timestamps with values now, they are not included in the HLS
      media playlist.

      The default is ``SERVER_TIMESTAMP`` .

    - **TimestampRange** *(dict) --*

      The start and end of the timestamp range for the requested media.

      This value should not be present if ``PlaybackType`` is ``LIVE`` .

      - **StartTimestamp** *(datetime) --*

        The start of the timestamp range for the requested media.

        If the ``HLSTimestampRange`` value is specified, the ``StartTimestamp`` value is required.

        .. note::

          This value is inclusive. Fragments that start before the ``StartTimestamp`` and continue
          past it are included in the session. If ``FragmentSelectorType`` is ``SERVER_TIMESTAMP`` ,
          the ``StartTimestamp`` must be later than the stream head.

      - **EndTimestamp** *(datetime) --*

        The end of the timestamp range for the requested media. This value must be within 3 hours of
        the specified ``StartTimestamp`` , and it must be later than the ``StartTimestamp`` value.

        If ``FragmentSelectorType`` for the request is ``SERVER_TIMESTAMP`` , this value must be in
        the past.

        The ``EndTimestamp`` value is required for ``ON_DEMAND`` mode, but optional for
        ``LIVE_REPLAY`` mode. If the ``EndTimestamp`` is not set for ``LIVE_REPLAY`` mode then the
        session will continue to include newly ingested fragments until the session expires.

        .. note::

          This value is inclusive. The ``EndTimestamp`` is compared to the (starting) timestamp of
          the fragment. Fragments that start before the ``EndTimestamp`` value and continue past it
          are included in the session.
    """


_ClientGetHlsStreamingSessionUrlResponseTypeDef = TypedDict(
    "_ClientGetHlsStreamingSessionUrlResponseTypeDef",
    {"HLSStreamingSessionURL": str},
    total=False,
)


class ClientGetHlsStreamingSessionUrlResponseTypeDef(
    _ClientGetHlsStreamingSessionUrlResponseTypeDef
):
    """
    Type definition for `ClientGetHlsStreamingSessionUrl` `Response`

    - **HLSStreamingSessionURL** *(string) --*

      The URL (containing the session token) that a media player can use to retrieve the HLS master
      playlist.
    """


_ClientGetMediaForFragmentListResponseTypeDef = TypedDict(
    "_ClientGetMediaForFragmentListResponseTypeDef", {"ContentType": str}, total=False
)


class ClientGetMediaForFragmentListResponseTypeDef(
    _ClientGetMediaForFragmentListResponseTypeDef
):
    """
    Type definition for `ClientGetMediaForFragmentList` `Response`

    - **ContentType** *(string) --*

      The content type of the requested media.

    - **Payload** (:class:`.StreamingBody`) --

      The payload that Kinesis Video Streams returns is a sequence of chunks from the specified
      stream. For information about the chunks, see `PutMedia
      <http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_dataplane_PutMedia.html>`__ .
      The chunks that Kinesis Video Streams returns in the ``GetMediaForFragmentList`` call also
      include the following additional Matroska (MKV) tags:

      * AWS_KINESISVIDEO_FRAGMENT_NUMBER - Fragment number returned in the chunk.

      * AWS_KINESISVIDEO_SERVER_SIDE_TIMESTAMP - Server-side timestamp of the fragment.

      * AWS_KINESISVIDEO_PRODUCER_SIDE_TIMESTAMP - Producer-side timestamp of the fragment.

      The following tags will be included if an exception occurs:

      * AWS_KINESISVIDEO_FRAGMENT_NUMBER - The number of the fragment that threw the exception

      * AWS_KINESISVIDEO_EXCEPTION_ERROR_CODE - The integer code of the exception

      * AWS_KINESISVIDEO_EXCEPTION_MESSAGE - A text description of the exception
    """


_ClientListFragmentsFragmentSelectorTimestampRangeTypeDef = TypedDict(
    "_ClientListFragmentsFragmentSelectorTimestampRangeTypeDef",
    {"StartTimestamp": datetime, "EndTimestamp": datetime},
)


class ClientListFragmentsFragmentSelectorTimestampRangeTypeDef(
    _ClientListFragmentsFragmentSelectorTimestampRangeTypeDef
):
    """
    Type definition for `ClientListFragmentsFragmentSelector` `TimestampRange`

    The range of timestamps to return.

    - **StartTimestamp** *(datetime) --* **[REQUIRED]**

      The starting timestamp in the range of timestamps for which to return fragments.

    - **EndTimestamp** *(datetime) --* **[REQUIRED]**

      The ending timestamp in the range of timestamps for which to return fragments.
    """


_ClientListFragmentsFragmentSelectorTypeDef = TypedDict(
    "_ClientListFragmentsFragmentSelectorTypeDef",
    {
        "FragmentSelectorType": str,
        "TimestampRange": ClientListFragmentsFragmentSelectorTimestampRangeTypeDef,
    },
)


class ClientListFragmentsFragmentSelectorTypeDef(
    _ClientListFragmentsFragmentSelectorTypeDef
):
    """
    Type definition for `ClientListFragments` `FragmentSelector`

    Describes the timestamp range and timestamp origin for the range of fragments to return.

    - **FragmentSelectorType** *(string) --* **[REQUIRED]**

      The origin of the timestamps to use (Server or Producer).

    - **TimestampRange** *(dict) --* **[REQUIRED]**

      The range of timestamps to return.

      - **StartTimestamp** *(datetime) --* **[REQUIRED]**

        The starting timestamp in the range of timestamps for which to return fragments.

      - **EndTimestamp** *(datetime) --* **[REQUIRED]**

        The ending timestamp in the range of timestamps for which to return fragments.
    """


_ClientListFragmentsResponseFragmentsTypeDef = TypedDict(
    "_ClientListFragmentsResponseFragmentsTypeDef",
    {
        "FragmentNumber": str,
        "FragmentSizeInBytes": int,
        "ProducerTimestamp": datetime,
        "ServerTimestamp": datetime,
        "FragmentLengthInMilliseconds": int,
    },
    total=False,
)


class ClientListFragmentsResponseFragmentsTypeDef(
    _ClientListFragmentsResponseFragmentsTypeDef
):
    """
    Type definition for `ClientListFragmentsResponse` `Fragments`

    Represents a segment of video or other time-delimited data.

    - **FragmentNumber** *(string) --*

      The unique identifier of the fragment. This value monotonically increases based on the
      ingestion order.

    - **FragmentSizeInBytes** *(integer) --*

      The total fragment size, including information about the fragment and contained media
      data.

    - **ProducerTimestamp** *(datetime) --*

      The timestamp from the producer corresponding to the fragment.

    - **ServerTimestamp** *(datetime) --*

      The timestamp from the AWS server corresponding to the fragment.

    - **FragmentLengthInMilliseconds** *(integer) --*

      The playback duration or other time value associated with the fragment.
    """


_ClientListFragmentsResponseTypeDef = TypedDict(
    "_ClientListFragmentsResponseTypeDef",
    {"Fragments": List[ClientListFragmentsResponseFragmentsTypeDef], "NextToken": str},
    total=False,
)


class ClientListFragmentsResponseTypeDef(_ClientListFragmentsResponseTypeDef):
    """
    Type definition for `ClientListFragments` `Response`

    - **Fragments** *(list) --*

      A list of archived  Fragment objects from the stream that meet the selector criteria. Results
      are in no specific order, even across pages.

      - *(dict) --*

        Represents a segment of video or other time-delimited data.

        - **FragmentNumber** *(string) --*

          The unique identifier of the fragment. This value monotonically increases based on the
          ingestion order.

        - **FragmentSizeInBytes** *(integer) --*

          The total fragment size, including information about the fragment and contained media
          data.

        - **ProducerTimestamp** *(datetime) --*

          The timestamp from the producer corresponding to the fragment.

        - **ServerTimestamp** *(datetime) --*

          The timestamp from the AWS server corresponding to the fragment.

        - **FragmentLengthInMilliseconds** *(integer) --*

          The playback duration or other time value associated with the fragment.

    - **NextToken** *(string) --*

      If the returned list is truncated, the operation returns this token to use to retrieve the
      next page of results. This value is ``null`` when there are no more results to return.
    """


_ListFragmentsPaginateFragmentSelectorTimestampRangeTypeDef = TypedDict(
    "_ListFragmentsPaginateFragmentSelectorTimestampRangeTypeDef",
    {"StartTimestamp": datetime, "EndTimestamp": datetime},
)


class ListFragmentsPaginateFragmentSelectorTimestampRangeTypeDef(
    _ListFragmentsPaginateFragmentSelectorTimestampRangeTypeDef
):
    """
    Type definition for `ListFragmentsPaginateFragmentSelector` `TimestampRange`

    The range of timestamps to return.

    - **StartTimestamp** *(datetime) --* **[REQUIRED]**

      The starting timestamp in the range of timestamps for which to return fragments.

    - **EndTimestamp** *(datetime) --* **[REQUIRED]**

      The ending timestamp in the range of timestamps for which to return fragments.
    """


_ListFragmentsPaginateFragmentSelectorTypeDef = TypedDict(
    "_ListFragmentsPaginateFragmentSelectorTypeDef",
    {
        "FragmentSelectorType": str,
        "TimestampRange": ListFragmentsPaginateFragmentSelectorTimestampRangeTypeDef,
    },
)


class ListFragmentsPaginateFragmentSelectorTypeDef(
    _ListFragmentsPaginateFragmentSelectorTypeDef
):
    """
    Type definition for `ListFragmentsPaginate` `FragmentSelector`

    Describes the timestamp range and timestamp origin for the range of fragments to return.

    - **FragmentSelectorType** *(string) --* **[REQUIRED]**

      The origin of the timestamps to use (Server or Producer).

    - **TimestampRange** *(dict) --* **[REQUIRED]**

      The range of timestamps to return.

      - **StartTimestamp** *(datetime) --* **[REQUIRED]**

        The starting timestamp in the range of timestamps for which to return fragments.

      - **EndTimestamp** *(datetime) --* **[REQUIRED]**

        The ending timestamp in the range of timestamps for which to return fragments.
    """


_ListFragmentsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListFragmentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListFragmentsPaginatePaginationConfigTypeDef(
    _ListFragmentsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListFragmentsPaginate` `PaginationConfig`

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


_ListFragmentsPaginateResponseFragmentsTypeDef = TypedDict(
    "_ListFragmentsPaginateResponseFragmentsTypeDef",
    {
        "FragmentNumber": str,
        "FragmentSizeInBytes": int,
        "ProducerTimestamp": datetime,
        "ServerTimestamp": datetime,
        "FragmentLengthInMilliseconds": int,
    },
    total=False,
)


class ListFragmentsPaginateResponseFragmentsTypeDef(
    _ListFragmentsPaginateResponseFragmentsTypeDef
):
    """
    Type definition for `ListFragmentsPaginateResponse` `Fragments`

    Represents a segment of video or other time-delimited data.

    - **FragmentNumber** *(string) --*

      The unique identifier of the fragment. This value monotonically increases based on the
      ingestion order.

    - **FragmentSizeInBytes** *(integer) --*

      The total fragment size, including information about the fragment and contained media
      data.

    - **ProducerTimestamp** *(datetime) --*

      The timestamp from the producer corresponding to the fragment.

    - **ServerTimestamp** *(datetime) --*

      The timestamp from the AWS server corresponding to the fragment.

    - **FragmentLengthInMilliseconds** *(integer) --*

      The playback duration or other time value associated with the fragment.
    """


_ListFragmentsPaginateResponseTypeDef = TypedDict(
    "_ListFragmentsPaginateResponseTypeDef",
    {"Fragments": List[ListFragmentsPaginateResponseFragmentsTypeDef]},
    total=False,
)


class ListFragmentsPaginateResponseTypeDef(_ListFragmentsPaginateResponseTypeDef):
    """
    Type definition for `ListFragmentsPaginate` `Response`

    - **Fragments** *(list) --*

      A list of archived  Fragment objects from the stream that meet the selector criteria. Results
      are in no specific order, even across pages.

      - *(dict) --*

        Represents a segment of video or other time-delimited data.

        - **FragmentNumber** *(string) --*

          The unique identifier of the fragment. This value monotonically increases based on the
          ingestion order.

        - **FragmentSizeInBytes** *(integer) --*

          The total fragment size, including information about the fragment and contained media
          data.

        - **ProducerTimestamp** *(datetime) --*

          The timestamp from the producer corresponding to the fragment.

        - **ServerTimestamp** *(datetime) --*

          The timestamp from the AWS server corresponding to the fragment.

        - **FragmentLengthInMilliseconds** *(integer) --*

          The playback duration or other time value associated with the fragment.
    """
