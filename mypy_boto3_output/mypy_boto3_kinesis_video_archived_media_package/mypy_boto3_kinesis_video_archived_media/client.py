"Main interface for kinesis-video-archived-media Client"
from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

# pylint: disable=import-self
import mypy_boto3_kinesis_video_archived_media.client as client_scope

# pylint: disable=import-self
import mypy_boto3_kinesis_video_archived_media.paginator as paginator_scope
from mypy_boto3_kinesis_video_archived_media.type_defs import (
    ClientGetDashStreamingSessionUrlDASHFragmentSelectorTypeDef,
    ClientGetDashStreamingSessionUrlResponseTypeDef,
    ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTypeDef,
    ClientGetHlsStreamingSessionUrlResponseTypeDef,
    ClientGetMediaForFragmentListResponseTypeDef,
    ClientListFragmentsFragmentSelectorTypeDef,
    ClientListFragmentsResponseTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> None:
        """
        Check if an operation can be paginated.

        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you'd normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator("create_foo")``.

        :return: ``True`` if the operation can be paginated,
            ``False`` otherwise.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        Generate a presigned url given a client, its method, and arguments

        :type ClientMethod: string
        :param ClientMethod: The client method to presign for

        :type Params: dict
        :param Params: The parameters normally passed to
            ``ClientMethod``.

        :type ExpiresIn: int
        :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)

        :type HttpMethod: string
        :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method's model.

        :returns: The presigned url
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_dash_streaming_session_url(
        self,
        StreamName: str = None,
        StreamARN: str = None,
        PlaybackMode: str = None,
        DisplayFragmentTimestamp: str = None,
        DisplayFragmentNumber: str = None,
        DASHFragmentSelector: ClientGetDashStreamingSessionUrlDASHFragmentSelectorTypeDef = None,
        Expires: int = None,
        MaxManifestFragmentResults: int = None,
    ) -> ClientGetDashStreamingSessionUrlResponseTypeDef:
        """
        Retrieves an MPEG Dynamic Adaptive Streaming over HTTP (DASH) URL for the stream. You can then open
        the URL in a media player to view the stream contents.

        Both the ``StreamName`` and the ``StreamARN`` parameters are optional, but you must specify either
        the ``StreamName`` or the ``StreamARN`` when invoking this API operation.

        An Amazon Kinesis video stream has the following requirements for providing data through MPEG-DASH:

        * The media must contain h.264 or h.265 encoded video and, optionally, AAC or G.711 encoded audio.
        Specifically, the codec ID of track 1 should be ``V_MPEG/ISO/AVC`` (for h.264) or V_MPEGH/ISO/HEVC
        (for H.265). Optionally, the codec ID of track 2 should be ``A_AAC`` (for AAC) or A_MS/ACM (for
        G.711).

        * Data retention must be greater than 0.

        * The video track of each fragment must contain codec private data in the Advanced Video Coding
        (AVC) for H.264 format and HEVC for H.265 format. For more information, see `MPEG-4 specification
        ISO/IEC 14496-15 <https://www.iso.org/standard/55980.html>`__ . For information about adapting
        stream data to a given format, see `NAL Adaptation Flags
        <http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-reference-nal.html>`__ .

        * The audio track (if present) of each fragment must contain codec private data in the AAC format
        (`AAC specification ISO/IEC 13818-7 <https://www.iso.org/standard/43345.html>`__ ) or the `MS Wave
        format <http://www-mmsp.ece.mcgill.ca/Documents/AudioFormats/WAVE/WAVE.html>`__ .

        The following procedure shows how to use MPEG-DASH with Kinesis Video Streams:

        * Get an endpoint using `GetDataEndpoint
        <http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_GetDataEndpoint.html>`__ , specifying
        ``GET_DASH_STREAMING_SESSION_URL`` for the ``APIName`` parameter.

        * Retrieve the MPEG-DASH URL using ``GetDASHStreamingSessionURL`` . Kinesis Video Streams creates
        an MPEG-DASH streaming session to be used for accessing content in a stream using the MPEG-DASH
        protocol. ``GetDASHStreamingSessionURL`` returns an authenticated URL (that includes an encrypted
        session token) for the session's MPEG-DASH *manifest* (the root resource needed for streaming with
        MPEG-DASH).

        .. note::

           Don't share or store this token where an unauthorized entity could access it. The token provides
           access to the content of the stream. Safeguard the token with the same measures that you would
           use with your AWS credentials.

         The media that is made available through the manifest consists only of the requested stream, time
         range, and format. No other media data (such as frames outside the requested window or alternate
         bitrates) is made available.

        * Provide the URL (containing the encrypted session token) for the MPEG-DASH manifest to a media
        player that supports the MPEG-DASH protocol. Kinesis Video Streams makes the initialization
        fragment and media fragments available through the manifest URL. The initialization fragment
        contains the codec private data for the stream, and other data needed to set up the video or audio
        decoder and renderer. The media fragments contain encoded video frames or encoded audio samples.

        * The media player receives the authenticated URL and requests stream metadata and media data
        normally. When the media player requests data, it calls the following actions:

          * **GetDASHManifest:** Retrieves an MPEG DASH manifest, which contains the metadata for the media
          that you want to playback.

          * **GetMP4InitFragment:** Retrieves the MP4 initialization fragment. The media player typically
          loads the initialization fragment before loading any media fragments. This fragment contains the
          "``fytp`` " and "``moov`` " MP4 atoms, and the child atoms that are needed to initialize the
          media player decoder. The initialization fragment does not correspond to a fragment in a Kinesis
          video stream. It contains only the codec private data for the stream and respective track, which
          the media player needs to decode the media frames.

          * **GetMP4MediaFragment:** Retrieves MP4 media fragments. These fragments contain the "``moof`` "
          and "``mdat`` " MP4 atoms and their child atoms, containing the encoded fragment's media frames
          and their timestamps.

          .. note::

             After the first media fragment is made available in a streaming session, any fragments that
             don't contain the same codec private data cause an error to be returned when those different
             media fragments are loaded. Therefore, the codec private data should not change between
             fragments in a session. This also means that the session fails if the fragments in a stream
             change from having only video to having both audio and video.

           Data retrieved with this action is billable. See `Pricing
           <https://aws.amazon.com/kinesis/video-streams/pricing/>`__ for details.

        .. note::

          The following restrictions apply to MPEG-DASH sessions:

          * A streaming session URL should not be shared between players. The service might throttle a
          session if multiple media players are sharing it. For connection limits, see `Kinesis Video
          Streams Limits <http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/limits.html>`__ .

          * A Kinesis video stream can have a maximum of ten active MPEG-DASH streaming sessions. If a new
          session is created when the maximum number of sessions is already active, the oldest (earliest
          created) session is closed. The number of active ``GetMedia`` connections on a Kinesis video
          stream does not count against this limit, and the number of active MPEG-DASH sessions does not
          count against the active ``GetMedia`` connection limit.

          .. note::

             The maximum limits for active HLS and MPEG-DASH streaming sessions are independent of each
             other.

        You can monitor the amount of data that the media player consumes by monitoring the
        ``GetMP4MediaFragment.OutgoingBytes`` Amazon CloudWatch metric. For information about using
        CloudWatch to monitor Kinesis Video Streams, see `Monitoring Kinesis Video Streams
        <http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/monitoring.html>`__ . For pricing
        information, see `Amazon Kinesis Video Streams Pricing
        <https://aws.amazon.com/kinesis/video-streams/pricing/>`__ and `AWS Pricing
        <https://aws.amazon.com/pricing/>`__ . Charges for both HLS sessions and outgoing AWS data apply.

        For more information about HLS, see `HTTP Live Streaming
        <https://developer.apple.com/streaming/>`__ on the `Apple Developer site
        <https://developer.apple.com>`__ .

        .. warning::

          If an error is thrown after invoking a Kinesis Video Streams archived media API, in addition to
          the HTTP status code and the response body, it includes the following pieces of information:

          * ``x-amz-ErrorType`` HTTP header – contains a more specific error type in addition to what the
          HTTP status code provides.

          * ``x-amz-RequestId`` HTTP header – if you want to report an issue to AWS, the support team can
          better diagnose the problem if given the Request Id.

          Both the HTTP status code and the ErrorType header can be utilized to make programmatic decisions
          about whether errors are retry-able and under what conditions, as well as provide information on
          what actions the client programmer might need to take in order to successfully try again.

          For more information, see the **Errors** section at the bottom of this topic, as well as `Common
          Errors <https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/CommonErrors.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kinesis-video-archived-media-2017-09-30/GetDASHStreamingSessionURL>`_
        <https://docs.aws.amazon.com/goto/WebAPI/kinesis-video-archived-media-2017-09-30/GetDASHStreamingSessionURL>`_

        **Request Syntax**
        ::

          response = client.get_dash_streaming_session_url(
              StreamName='string',
              StreamARN='string',
              PlaybackMode='LIVE'|'LIVE_REPLAY'|'ON_DEMAND',
              DisplayFragmentTimestamp='ALWAYS'|'NEVER',
              DisplayFragmentNumber='ALWAYS'|'NEVER',
              DASHFragmentSelector={
                  'FragmentSelectorType': 'PRODUCER_TIMESTAMP'|'SERVER_TIMESTAMP',
                  'TimestampRange': {
                      'StartTimestamp': datetime(2015, 1, 1),
                      'EndTimestamp': datetime(2015, 1, 1)
                  }
              },
              Expires=123,
              MaxManifestFragmentResults=123
          )
        :type StreamName: string
        :param StreamName:

          The name of the stream for which to retrieve the MPEG-DASH manifest URL.

          You must specify either the ``StreamName`` or the ``StreamARN`` .

        :type StreamARN: string
        :param StreamARN:

          The Amazon Resource Name (ARN) of the stream for which to retrieve the MPEG-DASH manifest URL.

          You must specify either the ``StreamName`` or the ``StreamARN`` .

        :type PlaybackMode: string
        :param PlaybackMode:

          Whether to retrieve live, live replay, or archived, on-demand data.

          Features of the three types of sessions include the following:

          * **``LIVE`` ** : For sessions of this type, the MPEG-DASH manifest is continually updated with
          the latest fragments as they become available. We recommend that the media player retrieve a new
          manifest on a one-second interval. When this type of session is played in a media player, the
          user interface typically displays a "live" notification, with no scrubber control for choosing
          the position in the playback window to display.

          .. note::

             In ``LIVE`` mode, the newest available fragments are included in an MPEG-DASH manifest, even
             if there is a gap between fragments (that is, if a fragment is missing). A gap like this might
             cause a media player to halt or cause a jump in playback. In this mode, fragments are not
             added to the MPEG-DASH manifest if they are older than the newest fragment in the playlist. If
             the missing fragment becomes available after a subsequent fragment is added to the manifest,
             the older fragment is not added, and the gap is not filled.

          * **``LIVE_REPLAY`` ** : For sessions of this type, the MPEG-DASH manifest is updated similarly
          to how it is updated for ``LIVE`` mode except that it starts by including fragments from a given
          start time. Instead of fragments being added as they are ingested, fragments are added as the
          duration of the next fragment elapses. For example, if the fragments in the session are two
          seconds long, then a new fragment is added to the manifest every two seconds. This mode is useful
          to be able to start playback from when an event is detected and continue live streaming media
          that has not yet been ingested as of the time of the session creation. This mode is also useful
          to stream previously archived media without being limited by the 1,000 fragment limit in the
          ``ON_DEMAND`` mode.

          * **``ON_DEMAND`` ** : For sessions of this type, the MPEG-DASH manifest contains all the
          fragments for the session, up to the number that is specified in
          ``MaxMediaPlaylistFragmentResults`` . The manifest must be retrieved only once for each session.
          When this type of session is played in a media player, the user interface typically displays a
          scrubber control for choosing the position in the playback window to display.

          In all playback modes, if ``FragmentSelectorType`` is ``PRODUCER_TIMESTAMP`` , and if there are
          multiple fragments with the same start timestamp, the fragment that has the larger fragment
          number (that is, the newer fragment) is included in the MPEG-DASH manifest. The other fragments
          are not included. Fragments that have different timestamps but have overlapping durations are
          still included in the MPEG-DASH manifest. This can lead to unexpected behavior in the media
          player.

          The default is ``LIVE`` .

        :type DisplayFragmentTimestamp: string
        :param DisplayFragmentTimestamp:

          Per the MPEG-DASH specification, the wall-clock time of fragments in the manifest file can be
          derived using attributes in the manifest itself. However, typically, MPEG-DASH compatible media
          players do not properly handle gaps in the media timeline. Kinesis Video Streams adjusts the
          media timeline in the manifest file to enable playback of media with discontinuities. Therefore,
          the wall-clock time derived from the manifest file may be inaccurate. If DisplayFragmentTimestamp
          is set to ``ALWAYS`` , the accurate fragment timestamp is added to each S element in the manifest
          file with the attribute name “kvs:ts”. A custom MPEG-DASH media player is necessary to leverage
          this custom attribute.

          The default value is ``NEVER`` . When  DASHFragmentSelector is ``SERVER_TIMESTAMP`` , the
          timestamps will be the server start timestamps. Similarly, when  DASHFragmentSelector is
          ``PRODUCER_TIMESTAMP`` , the timestamps will be the producer start timestamps.

        :type DisplayFragmentNumber: string
        :param DisplayFragmentNumber:

          Fragments are identified in the manifest file based on their sequence number in the session. If
          DisplayFragmentNumber is set to ``ALWAYS`` , the Kinesis Video Streams fragment number is added
          to each S element in the manifest file with the attribute name “kvs:fn”. These fragment numbers
          can be used for logging or for use with other APIs (e.g. ``GetMedia`` and
          ``GetMediaForFragmentList`` ). A custom MPEG-DASH media player is necessary to leverage these
          this custom attribute.

          The default value is ``NEVER`` .

        :type DASHFragmentSelector: dict
        :param DASHFragmentSelector:

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

        :type Expires: integer
        :param Expires:

          The time in seconds until the requested session expires. This value can be between 300 (5
          minutes) and 43200 (12 hours).

          When a session expires, no new calls to ``GetDashManifest`` , ``GetMP4InitFragment`` , or
          ``GetMP4MediaFragment`` can be made for that session.

          The default is 300 (5 minutes).

        :type MaxManifestFragmentResults: integer
        :param MaxManifestFragmentResults:

          The maximum number of fragments that are returned in the MPEG-DASH manifest.

          When the ``PlaybackMode`` is ``LIVE`` , the most recent fragments are returned up to this value.
          When the ``PlaybackMode`` is ``ON_DEMAND`` , the oldest fragments are returned, up to this
          maximum number.

          When there are a higher number of fragments available in a live MPEG-DASH manifest, video players
          often buffer content before starting playback. Increasing the buffer size increases the playback
          latency, but it decreases the likelihood that rebuffering will occur during playback. We
          recommend that a live MPEG-DASH manifest have a minimum of 3 fragments and a maximum of 10
          fragments.

          The default is 5 fragments if ``PlaybackMode`` is ``LIVE`` or ``LIVE_REPLAY`` , and 1,000 if
          ``PlaybackMode`` is ``ON_DEMAND`` .

          The maximum value of 1,000 fragments corresponds to more than 16 minutes of video on streams with
          1-second fragments, and more than 2 1/2 hours of video on streams with 10-second fragments.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DASHStreamingSessionURL': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **DASHStreamingSessionURL** *(string) --*

              The URL (containing the session token) that a media player can use to retrieve the MPEG-DASH
              manifest.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_hls_streaming_session_url(
        self,
        StreamName: str = None,
        StreamARN: str = None,
        PlaybackMode: str = None,
        HLSFragmentSelector: ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTypeDef = None,
        ContainerFormat: str = None,
        DiscontinuityMode: str = None,
        DisplayFragmentTimestamp: str = None,
        Expires: int = None,
        MaxMediaPlaylistFragmentResults: int = None,
    ) -> ClientGetHlsStreamingSessionUrlResponseTypeDef:
        """
        Retrieves an HTTP Live Streaming (HLS) URL for the stream. You can then open the URL in a browser
        or media player to view the stream contents.

        Both the ``StreamName`` and the ``StreamARN`` parameters are optional, but you must specify either
        the ``StreamName`` or the ``StreamARN`` when invoking this API operation.

        An Amazon Kinesis video stream has the following requirements for providing data through HLS:

        * The media must contain h.264 or h.265 encoded video and, optionally, AAC encoded audio.
        Specifically, the codec ID of track 1 should be ``V_MPEG/ISO/AVC`` (for h.264) or
        ``V_MPEG/ISO/HEVC`` (for h.265). Optionally, the codec ID of track 2 should be ``A_AAC`` .

        * Data retention must be greater than 0.

        * The video track of each fragment must contain codec private data in the Advanced Video Coding
        (AVC) for H.264 format or HEVC for H.265 format (`MPEG-4 specification ISO/IEC 14496-15
        <https://www.iso.org/standard/55980.html>`__ ). For information about adapting stream data to a
        given format, see `NAL Adaptation Flags
        <http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-reference-nal.html>`__ .

        * The audio track (if present) of each fragment must contain codec private data in the AAC format
        (`AAC specification ISO/IEC 13818-7 <https://www.iso.org/standard/43345.html>`__ ).

        Kinesis Video Streams HLS sessions contain fragments in the fragmented MPEG-4 form (also called
        fMP4 or CMAF) or the MPEG-2 form (also called TS chunks, which the HLS specification also
        supports). For more information about HLS fragment types, see the `HLS specification
        <https://tools.ietf.org/html/draft-pantos-http-live-streaming-23>`__ .

        The following procedure shows how to use HLS with Kinesis Video Streams:

        * Get an endpoint using `GetDataEndpoint
        <http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_GetDataEndpoint.html>`__ , specifying
        ``GET_HLS_STREAMING_SESSION_URL`` for the ``APIName`` parameter.

        * Retrieve the HLS URL using ``GetHLSStreamingSessionURL`` . Kinesis Video Streams creates an HLS
        streaming session to be used for accessing content in a stream using the HLS protocol.
        ``GetHLSStreamingSessionURL`` returns an authenticated URL (that includes an encrypted session
        token) for the session's HLS *master playlist* (the root resource needed for streaming with HLS).

        .. note::

           Don't share or store this token where an unauthorized entity could access it. The token provides
           access to the content of the stream. Safeguard the token with the same measures that you would
           use with your AWS credentials.

         The media that is made available through the playlist consists only of the requested stream, time
         range, and format. No other media data (such as frames outside the requested window or alternate
         bitrates) is made available.

        * Provide the URL (containing the encrypted session token) for the HLS master playlist to a media
        player that supports the HLS protocol. Kinesis Video Streams makes the HLS media playlist,
        initialization fragment, and media fragments available through the master playlist URL. The
        initialization fragment contains the codec private data for the stream, and other data needed to
        set up the video or audio decoder and renderer. The media fragments contain H.264-encoded video
        frames or AAC-encoded audio samples.

        * The media player receives the authenticated URL and requests stream metadata and media data
        normally. When the media player requests data, it calls the following actions:

          * **GetHLSMasterPlaylist:** Retrieves an HLS master playlist, which contains a URL for the
          ``GetHLSMediaPlaylist`` action for each track, and additional metadata for the media player,
          including estimated bitrate and resolution.

          * **GetHLSMediaPlaylist:** Retrieves an HLS media playlist, which contains a URL to access the
          MP4 initialization fragment with the ``GetMP4InitFragment`` action, and URLs to access the MP4
          media fragments with the ``GetMP4MediaFragment`` actions. The HLS media playlist also contains
          metadata about the stream that the player needs to play it, such as whether the ``PlaybackMode``
          is ``LIVE`` or ``ON_DEMAND`` . The HLS media playlist is typically static for sessions with a
          ``PlaybackType`` of ``ON_DEMAND`` . The HLS media playlist is continually updated with new
          fragments for sessions with a ``PlaybackType`` of ``LIVE`` . There is a distinct HLS media
          playlist for the video track and the audio track (if applicable) that contains MP4 media URLs for
          the specific track.

          * **GetMP4InitFragment:** Retrieves the MP4 initialization fragment. The media player typically
          loads the initialization fragment before loading any media fragments. This fragment contains the
          "``fytp`` " and "``moov`` " MP4 atoms, and the child atoms that are needed to initialize the
          media player decoder. The initialization fragment does not correspond to a fragment in a Kinesis
          video stream. It contains only the codec private data for the stream and respective track, which
          the media player needs to decode the media frames.

          * **GetMP4MediaFragment:** Retrieves MP4 media fragments. These fragments contain the "``moof`` "
          and "``mdat`` " MP4 atoms and their child atoms, containing the encoded fragment's media frames
          and their timestamps.

          .. note::

             After the first media fragment is made available in a streaming session, any fragments that
             don't contain the same codec private data cause an error to be returned when those different
             media fragments are loaded. Therefore, the codec private data should not change between
             fragments in a session. This also means that the session fails if the fragments in a stream
             change from having only video to having both audio and video.

           Data retrieved with this action is billable. See `Pricing
           <https://aws.amazon.com/kinesis/video-streams/pricing/>`__ for details.

          * **GetTSFragment:** Retrieves MPEG TS fragments containing both initialization and media data
          for all tracks in the stream.

          .. note::

             If the ``ContainerFormat`` is ``MPEG_TS`` , this API is used instead of ``GetMP4InitFragment``
             and ``GetMP4MediaFragment`` to retrieve stream media.

           Data retrieved with this action is billable. For more information, see `Kinesis Video Streams
           pricing <https://aws.amazon.com/kinesis/video-streams/pricing/>`__ .

        .. note::

          The following restrictions apply to HLS sessions:

          * A streaming session URL should not be shared between players. The service might throttle a
          session if multiple media players are sharing it. For connection limits, see `Kinesis Video
          Streams Limits <http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/limits.html>`__ .

          * A Kinesis video stream can have a maximum of ten active HLS streaming sessions. If a new
          session is created when the maximum number of sessions is already active, the oldest (earliest
          created) session is closed. The number of active ``GetMedia`` connections on a Kinesis video
          stream does not count against this limit, and the number of active HLS sessions does not count
          against the active ``GetMedia`` connection limit.

          .. note::

             The maximum limits for active HLS and MPEG-DASH streaming sessions are independent of each
             other.

        You can monitor the amount of data that the media player consumes by monitoring the
        ``GetMP4MediaFragment.OutgoingBytes`` Amazon CloudWatch metric. For information about using
        CloudWatch to monitor Kinesis Video Streams, see `Monitoring Kinesis Video Streams
        <http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/monitoring.html>`__ . For pricing
        information, see `Amazon Kinesis Video Streams Pricing
        <https://aws.amazon.com/kinesis/video-streams/pricing/>`__ and `AWS Pricing
        <https://aws.amazon.com/pricing/>`__ . Charges for both HLS sessions and outgoing AWS data apply.

        For more information about HLS, see `HTTP Live Streaming
        <https://developer.apple.com/streaming/>`__ on the `Apple Developer site
        <https://developer.apple.com>`__ .

        .. warning::

          If an error is thrown after invoking a Kinesis Video Streams archived media API, in addition to
          the HTTP status code and the response body, it includes the following pieces of information:

          * ``x-amz-ErrorType`` HTTP header – contains a more specific error type in addition to what the
          HTTP status code provides.

          * ``x-amz-RequestId`` HTTP header – if you want to report an issue to AWS, the support team can
          better diagnose the problem if given the Request Id.

          Both the HTTP status code and the ErrorType header can be utilized to make programmatic decisions
          about whether errors are retry-able and under what conditions, as well as provide information on
          what actions the client programmer might need to take in order to successfully try again.

          For more information, see the **Errors** section at the bottom of this topic, as well as `Common
          Errors <https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/CommonErrors.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kinesis-video-archived-media-2017-09-30/GetHLSStreamingSessionURL>`_
        <https://docs.aws.amazon.com/goto/WebAPI/kinesis-video-archived-media-2017-09-30/GetHLSStreamingSessionURL>`_

        **Request Syntax**
        ::

          response = client.get_hls_streaming_session_url(
              StreamName='string',
              StreamARN='string',
              PlaybackMode='LIVE'|'LIVE_REPLAY'|'ON_DEMAND',
              HLSFragmentSelector={
                  'FragmentSelectorType': 'PRODUCER_TIMESTAMP'|'SERVER_TIMESTAMP',
                  'TimestampRange': {
                      'StartTimestamp': datetime(2015, 1, 1),
                      'EndTimestamp': datetime(2015, 1, 1)
                  }
              },
              ContainerFormat='FRAGMENTED_MP4'|'MPEG_TS',
              DiscontinuityMode='ALWAYS'|'NEVER'|'ON_DISCONTINUITY',
              DisplayFragmentTimestamp='ALWAYS'|'NEVER',
              Expires=123,
              MaxMediaPlaylistFragmentResults=123
          )
        :type StreamName: string
        :param StreamName:

          The name of the stream for which to retrieve the HLS master playlist URL.

          You must specify either the ``StreamName`` or the ``StreamARN`` .

        :type StreamARN: string
        :param StreamARN:

          The Amazon Resource Name (ARN) of the stream for which to retrieve the HLS master playlist URL.

          You must specify either the ``StreamName`` or the ``StreamARN`` .

        :type PlaybackMode: string
        :param PlaybackMode:

          Whether to retrieve live, live replay, or archived, on-demand data.

          Features of the three types of sessions include the following:

          * **``LIVE`` ** : For sessions of this type, the HLS media playlist is continually updated with
          the latest fragments as they become available. We recommend that the media player retrieve a new
          playlist on a one-second interval. When this type of session is played in a media player, the
          user interface typically displays a "live" notification, with no scrubber control for choosing
          the position in the playback window to display.

          .. note::

             In ``LIVE`` mode, the newest available fragments are included in an HLS media playlist, even
             if there is a gap between fragments (that is, if a fragment is missing). A gap like this might
             cause a media player to halt or cause a jump in playback. In this mode, fragments are not
             added to the HLS media playlist if they are older than the newest fragment in the playlist. If
             the missing fragment becomes available after a subsequent fragment is added to the playlist,
             the older fragment is not added, and the gap is not filled.

          * **``LIVE_REPLAY`` ** : For sessions of this type, the HLS media playlist is updated similarly
          to how it is updated for ``LIVE`` mode except that it starts by including fragments from a given
          start time. Instead of fragments being added as they are ingested, fragments are added as the
          duration of the next fragment elapses. For example, if the fragments in the session are two
          seconds long, then a new fragment is added to the media playlist every two seconds. This mode is
          useful to be able to start playback from when an event is detected and continue live streaming
          media that has not yet been ingested as of the time of the session creation. This mode is also
          useful to stream previously archived media without being limited by the 1,000 fragment limit in
          the ``ON_DEMAND`` mode.

          * **``ON_DEMAND`` ** : For sessions of this type, the HLS media playlist contains all the
          fragments for the session, up to the number that is specified in
          ``MaxMediaPlaylistFragmentResults`` . The playlist must be retrieved only once for each session.
          When this type of session is played in a media player, the user interface typically displays a
          scrubber control for choosing the position in the playback window to display.

          In all playback modes, if ``FragmentSelectorType`` is ``PRODUCER_TIMESTAMP`` , and if there are
          multiple fragments with the same start timestamp, the fragment that has the larger fragment
          number (that is, the newer fragment) is included in the HLS media playlist. The other fragments
          are not included. Fragments that have different timestamps but have overlapping durations are
          still included in the HLS media playlist. This can lead to unexpected behavior in the media
          player.

          The default is ``LIVE`` .

        :type HLSFragmentSelector: dict
        :param HLSFragmentSelector:

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

        :type ContainerFormat: string
        :param ContainerFormat:

          Specifies which format should be used for packaging the media. Specifying the ``FRAGMENTED_MP4``
          container format packages the media into MP4 fragments (fMP4 or CMAF). This is the recommended
          packaging because there is minimal packaging overhead. The other container format option is
          ``MPEG_TS`` . HLS has supported MPEG TS chunks since it was released and is sometimes the only
          supported packaging on older HLS players. MPEG TS typically has a 5-25 percent packaging
          overhead. This means MPEG TS typically requires 5-25 percent more bandwidth and cost than fMP4.

          The default is ``FRAGMENTED_MP4`` .

        :type DiscontinuityMode: string
        :param DiscontinuityMode:

          Specifies when flags marking discontinuities between fragments are added to the media playlists.

          Media players typically build a timeline of media content to play, based on the timestamps of
          each fragment. This means that if there is any overlap or gap between fragments (as is typical if
           HLSFragmentSelector is set to ``SERVER_TIMESTAMP`` ), the media player timeline will also have
           small gaps between fragments in some places, and will overwrite frames in other places. Gaps in
           the media player timeline can cause playback to stall and overlaps can cause playback to be
           jittery. When there are discontinuity flags between fragments, the media player is expected to
           reset the timeline, resulting in the next fragment being played immediately after the previous
           fragment.

          The following modes are supported:

          * ``ALWAYS`` : a discontinuity marker is placed between every fragment in the HLS media playlist.
          It is recommended to use a value of ``ALWAYS`` if the fragment timestamps are not accurate.

          * ``NEVER`` : no discontinuity markers are placed anywhere. It is recommended to use a value of
          ``NEVER`` to ensure the media player timeline most accurately maps to the producer timestamps.

          * ``ON_DISCONTIUNITY`` : a discontinuity marker is placed between fragments that have a gap or
          overlap of more than 50 milliseconds. For most playback scenarios, it is recommended to use a
          value of ``ON_DISCONTINUITY`` so that the media player timeline is only reset when there is a
          significant issue with the media timeline (e.g. a missing fragment).

          The default is ``ALWAYS`` when  HLSFragmentSelector is set to ``SERVER_TIMESTAMP`` , and
          ``NEVER`` when it is set to ``PRODUCER_TIMESTAMP`` .

        :type DisplayFragmentTimestamp: string
        :param DisplayFragmentTimestamp:

          Specifies when the fragment start timestamps should be included in the HLS media playlist.
          Typically, media players report the playhead position as a time relative to the start of the
          first fragment in the playback session. However, when the start timestamps are included in the
          HLS media playlist, some media players might report the current playhead as an absolute time
          based on the fragment timestamps. This can be useful for creating a playback experience that
          shows viewers the wall-clock time of the media.

          The default is ``NEVER`` . When  HLSFragmentSelector is ``SERVER_TIMESTAMP`` , the timestamps
          will be the server start timestamps. Similarly, when  HLSFragmentSelector is
          ``PRODUCER_TIMESTAMP`` , the timestamps will be the producer start timestamps.

        :type Expires: integer
        :param Expires:

          The time in seconds until the requested session expires. This value can be between 300 (5
          minutes) and 43200 (12 hours).

          When a session expires, no new calls to ``GetHLSMasterPlaylist`` , ``GetHLSMediaPlaylist`` ,
          ``GetMP4InitFragment`` , ``GetMP4MediaFragment`` , or ``GetTSFragment`` can be made for that
          session.

          The default is 300 (5 minutes).

        :type MaxMediaPlaylistFragmentResults: integer
        :param MaxMediaPlaylistFragmentResults:

          The maximum number of fragments that are returned in the HLS media playlists.

          When the ``PlaybackMode`` is ``LIVE`` , the most recent fragments are returned up to this value.
          When the ``PlaybackMode`` is ``ON_DEMAND`` , the oldest fragments are returned, up to this
          maximum number.

          When there are a higher number of fragments available in a live HLS media playlist, video players
          often buffer content before starting playback. Increasing the buffer size increases the playback
          latency, but it decreases the likelihood that rebuffering will occur during playback. We
          recommend that a live HLS media playlist have a minimum of 3 fragments and a maximum of 10
          fragments.

          The default is 5 fragments if ``PlaybackMode`` is ``LIVE`` or ``LIVE_REPLAY`` , and 1,000 if
          ``PlaybackMode`` is ``ON_DEMAND`` .

          The maximum value of 1,000 fragments corresponds to more than 16 minutes of video on streams with
          1-second fragments, and more than 2 1/2 hours of video on streams with 10-second fragments.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'HLSStreamingSessionURL': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **HLSStreamingSessionURL** *(string) --*

              The URL (containing the session token) that a media player can use to retrieve the HLS master
              playlist.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_media_for_fragment_list(
        self, StreamName: str, Fragments: List[str]
    ) -> ClientGetMediaForFragmentListResponseTypeDef:
        """
        Gets media for a list of fragments (specified by fragment number) from the archived data in an
        Amazon Kinesis video stream.

        .. note::

          You must first call the ``GetDataEndpoint`` API to get an endpoint. Then send the
          ``GetMediaForFragmentList`` requests to this endpoint using the `--endpoint-url parameter
          <https://docs.aws.amazon.com/cli/latest/reference/>`__ .

        The following limits apply when using the ``GetMediaForFragmentList`` API:

        * A client can call ``GetMediaForFragmentList`` up to five times per second per stream.

        * Kinesis Video Streams sends media data at a rate of up to 25 megabytes per second (or 200
        megabits per second) during a ``GetMediaForFragmentList`` session.

        .. warning::

          If an error is thrown after invoking a Kinesis Video Streams archived media API, in addition to
          the HTTP status code and the response body, it includes the following pieces of information:

          * ``x-amz-ErrorType`` HTTP header – contains a more specific error type in addition to what the
          HTTP status code provides.

          * ``x-amz-RequestId`` HTTP header – if you want to report an issue to AWS, the support team can
          better diagnose the problem if given the Request Id.

          Both the HTTP status code and the ErrorType header can be utilized to make programmatic decisions
          about whether errors are retry-able and under what conditions, as well as provide information on
          what actions the client programmer might need to take in order to successfully try again.

          For more information, see the **Errors** section at the bottom of this topic, as well as `Common
          Errors <https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/CommonErrors.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kinesis-video-archived-media-2017-09-30/GetMediaForFragmentList>`_
        <https://docs.aws.amazon.com/goto/WebAPI/kinesis-video-archived-media-2017-09-30/GetMediaForFragmentList>`_

        **Request Syntax**
        ::

          response = client.get_media_for_fragment_list(
              StreamName='string',
              Fragments=[
                  'string',
              ]
          )
        :type StreamName: string
        :param StreamName: **[REQUIRED]**

          The name of the stream from which to retrieve fragment media.

        :type Fragments: list
        :param Fragments: **[REQUIRED]**

          A list of the numbers of fragments for which to retrieve media. You retrieve these values with
          ListFragments .

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ContentType': 'string',
                'Payload': StreamingBody()
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_fragments(
        self,
        StreamName: str,
        MaxResults: int = None,
        NextToken: str = None,
        FragmentSelector: ClientListFragmentsFragmentSelectorTypeDef = None,
    ) -> ClientListFragmentsResponseTypeDef:
        """
        Returns a list of  Fragment objects from the specified stream and timestamp range within the
        archived data.

        Listing fragments is eventually consistent. This means that even if the producer receives an
        acknowledgment that a fragment is persisted, the result might not be returned immediately from a
        request to ``ListFragments`` . However, results are typically available in less than one second.

        .. note::

          You must first call the ``GetDataEndpoint`` API to get an endpoint. Then send the
          ``ListFragments`` requests to this endpoint using the `--endpoint-url parameter
          <https://docs.aws.amazon.com/cli/latest/reference/>`__ .

        .. warning::

          If an error is thrown after invoking a Kinesis Video Streams archived media API, in addition to
          the HTTP status code and the response body, it includes the following pieces of information:

          * ``x-amz-ErrorType`` HTTP header – contains a more specific error type in addition to what the
          HTTP status code provides.

          * ``x-amz-RequestId`` HTTP header – if you want to report an issue to AWS, the support team can
          better diagnose the problem if given the Request Id.

          Both the HTTP status code and the ErrorType header can be utilized to make programmatic decisions
          about whether errors are retry-able and under what conditions, as well as provide information on
          what actions the client programmer might need to take in order to successfully try again.

          For more information, see the **Errors** section at the bottom of this topic, as well as `Common
          Errors <https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/CommonErrors.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kinesis-video-archived-media-2017-09-30/ListFragments>`_

        **Request Syntax**
        ::

          response = client.list_fragments(
              StreamName='string',
              MaxResults=123,
              NextToken='string',
              FragmentSelector={
                  'FragmentSelectorType': 'PRODUCER_TIMESTAMP'|'SERVER_TIMESTAMP',
                  'TimestampRange': {
                      'StartTimestamp': datetime(2015, 1, 1),
                      'EndTimestamp': datetime(2015, 1, 1)
                  }
              }
          )
        :type StreamName: string
        :param StreamName: **[REQUIRED]**

          The name of the stream from which to retrieve a fragment list.

        :type MaxResults: integer
        :param MaxResults:

          The total number of fragments to return. If the total number of fragments available is more than
          the value specified in ``max-results`` , then a  ListFragmentsOutput$NextToken is provided in the
          output that you can use to resume pagination.

        :type NextToken: string
        :param NextToken:

          A token to specify where to start paginating. This is the  ListFragmentsOutput$NextToken from a
          previously truncated response.

        :type FragmentSelector: dict
        :param FragmentSelector:

          Describes the timestamp range and timestamp origin for the range of fragments to return.

          - **FragmentSelectorType** *(string) --* **[REQUIRED]**

            The origin of the timestamps to use (Server or Producer).

          - **TimestampRange** *(dict) --* **[REQUIRED]**

            The range of timestamps to return.

            - **StartTimestamp** *(datetime) --* **[REQUIRED]**

              The starting timestamp in the range of timestamps for which to return fragments.

            - **EndTimestamp** *(datetime) --* **[REQUIRED]**

              The ending timestamp in the range of timestamps for which to return fragments.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Fragments': [
                    {
                        'FragmentNumber': 'string',
                        'FragmentSizeInBytes': 123,
                        'ProducerTimestamp': datetime(2015, 1, 1),
                        'ServerTimestamp': datetime(2015, 1, 1),
                        'FragmentLengthInMilliseconds': 123
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_fragments"]
    ) -> paginator_scope.ListFragmentsPaginator:
        """
        Get Paginator for `list_fragments` operation.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        """
        Create a paginator for an operation.

        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you'd normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator("create_foo")``.

        :raise OperationNotPageableError: Raised if the operation is not
            pageable.  You can use the ``client.can_paginate`` method to
            check if an operation is pageable.

        :rtype: L{botocore.paginate.Paginator}
        :return: A paginator object.
        """


class Exceptions:
    ClientError: Boto3ClientError
    ClientLimitExceededException: Boto3ClientError
    InvalidArgumentException: Boto3ClientError
    InvalidCodecPrivateDataException: Boto3ClientError
    MissingCodecPrivateDataException: Boto3ClientError
    NoDataRetentionException: Boto3ClientError
    NotAuthorizedException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    UnsupportedStreamMediaTypeException: Boto3ClientError
