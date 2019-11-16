"Main interface for mediapackage-vod Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_mediapackage_vod.type_defs import (
    ListAssetsPaginatePaginationConfigTypeDef,
    ListAssetsPaginateResponseTypeDef,
    ListPackagingConfigurationsPaginatePaginationConfigTypeDef,
    ListPackagingConfigurationsPaginateResponseTypeDef,
    ListPackagingGroupsPaginatePaginationConfigTypeDef,
    ListPackagingGroupsPaginateResponseTypeDef,
)


__all__ = (
    "ListAssetsPaginator",
    "ListPackagingConfigurationsPaginator",
    "ListPackagingGroupsPaginator",
)


class ListAssetsPaginator(Boto3Paginator):
    """
    Paginator for `list_assets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PackagingGroupId: str = None,
        PaginationConfig: ListAssetsPaginatePaginationConfigTypeDef = None,
    ) -> ListAssetsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`MediaPackageVod.Client.list_assets`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediapackage-vod-2018-11-07/ListAssets>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PackagingGroupId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type PackagingGroupId: string
        :param PackagingGroupId: Returns Assets associated with the specified PackagingGroup.

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Assets': [
                    {
                        'Arn': 'string',
                        'Id': 'string',
                        'PackagingGroupId': 'string',
                        'ResourceId': 'string',
                        'SourceArn': 'string',
                        'SourceRoleArn': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --* A collection of MediaPackage VOD Asset resources.

            - **Assets** *(list) --* A list of MediaPackage VOD Asset resources.

              - *(dict) --* A MediaPackage VOD Asset resource.

                - **Arn** *(string) --* The ARN of the Asset.

                - **Id** *(string) --* The unique identifier for the Asset.

                - **PackagingGroupId** *(string) --* The ID of the PackagingGroup for the Asset.

                - **ResourceId** *(string) --* The resource ID to include in SPEKE key requests.

                - **SourceArn** *(string) --* ARN of the source object in S3.

                - **SourceRoleArn** *(string) --* The IAM role ARN used to access the source S3 bucket.

        """


class ListPackagingConfigurationsPaginator(Boto3Paginator):
    """
    Paginator for `list_packaging_configurations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PackagingGroupId: str = None,
        PaginationConfig: ListPackagingConfigurationsPaginatePaginationConfigTypeDef = None,
    ) -> ListPackagingConfigurationsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`MediaPackageVod.Client.list_packaging_configurations`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediapackage-vod-2018-11-07/ListPackagingConfigurations>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PackagingGroupId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type PackagingGroupId: string
        :param PackagingGroupId: Returns MediaPackage VOD PackagingConfigurations associated with the
        specified PackagingGroup.

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PackagingConfigurations': [
                    {
                        'Arn': 'string',
                        'CmafPackage': {
                            'Encryption': {
                                'SpekeKeyProvider': {
                                    'RoleArn': 'string',
                                    'SystemIds': [
                                        'string',
                                    ],
                                    'Url': 'string'
                                }
                            },
                            'HlsManifests': [
                                {
                                    'AdMarkers': 'NONE'|'SCTE35_ENHANCED'|'PASSTHROUGH',
                                    'IncludeIframeOnlyStream': True|False,
                                    'ManifestName': 'string',
                                    'ProgramDateTimeIntervalSeconds': 123,
                                    'RepeatExtXKey': True|False,
                                    'StreamSelection': {
                                        'MaxVideoBitsPerSecond': 123,
                                        'MinVideoBitsPerSecond': 123,
                                        'StreamOrder':
                                        'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                                    }
                                },
                            ],
                            'SegmentDurationSeconds': 123
                        },
                        'DashPackage': {
                            'DashManifests': [
                                {
                                    'ManifestName': 'string',
                                    'MinBufferTimeSeconds': 123,
                                    'Profile': 'NONE'|'HBBTV_1_5',
                                    'StreamSelection': {
                                        'MaxVideoBitsPerSecond': 123,
                                        'MinVideoBitsPerSecond': 123,
                                        'StreamOrder':
                                        'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                                    }
                                },
                            ],
                            'Encryption': {
                                'SpekeKeyProvider': {
                                    'RoleArn': 'string',
                                    'SystemIds': [
                                        'string',
                                    ],
                                    'Url': 'string'
                                }
                            },
                            'SegmentDurationSeconds': 123
                        },
                        'HlsPackage': {
                            'Encryption': {
                                'ConstantInitializationVector': 'string',
                                'EncryptionMethod': 'AES_128'|'SAMPLE_AES',
                                'SpekeKeyProvider': {
                                    'RoleArn': 'string',
                                    'SystemIds': [
                                        'string',
                                    ],
                                    'Url': 'string'
                                }
                            },
                            'HlsManifests': [
                                {
                                    'AdMarkers': 'NONE'|'SCTE35_ENHANCED'|'PASSTHROUGH',
                                    'IncludeIframeOnlyStream': True|False,
                                    'ManifestName': 'string',
                                    'ProgramDateTimeIntervalSeconds': 123,
                                    'RepeatExtXKey': True|False,
                                    'StreamSelection': {
                                        'MaxVideoBitsPerSecond': 123,
                                        'MinVideoBitsPerSecond': 123,
                                        'StreamOrder':
                                        'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                                    }
                                },
                            ],
                            'SegmentDurationSeconds': 123,
                            'UseAudioRenditionGroup': True|False
                        },
                        'Id': 'string',
                        'MssPackage': {
                            'Encryption': {
                                'SpekeKeyProvider': {
                                    'RoleArn': 'string',
                                    'SystemIds': [
                                        'string',
                                    ],
                                    'Url': 'string'
                                }
                            },
                            'MssManifests': [
                                {
                                    'ManifestName': 'string',
                                    'StreamSelection': {
                                        'MaxVideoBitsPerSecond': 123,
                                        'MinVideoBitsPerSecond': 123,
                                        'StreamOrder':
                                        'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                                    }
                                },
                            ],
                            'SegmentDurationSeconds': 123
                        },
                        'PackagingGroupId': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --* A collection of MediaPackage VOD PackagingConfiguration resources.

            - **PackagingConfigurations** *(list) --* A list of MediaPackage VOD PackagingConfiguration
            resources.

              - *(dict) --* A MediaPackage VOD PackagingConfiguration resource.

                - **Arn** *(string) --* The ARN of the PackagingConfiguration.

                - **CmafPackage** *(dict) --* A CMAF packaging configuration.

                  - **Encryption** *(dict) --* A CMAF encryption configuration.

                    - **SpekeKeyProvider** *(dict) --* A configuration for accessing an external Secure
                    Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

                      - **RoleArn** *(string) --* An Amazon Resource Name (ARN) of an IAM role that AWS
                      Elemental MediaPackage will assume when accessing the key provider service.

                      - **SystemIds** *(list) --* The system IDs to include in key requests.

                        - *(string) --*

                      - **Url** *(string) --* The URL of the external key provider service.

                  - **HlsManifests** *(list) --* A list of HLS manifest configurations.

                    - *(dict) --* An HTTP Live Streaming (HLS) manifest configuration.

                      - **AdMarkers** *(string) --* This setting controls how ad markers are included in
                      the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output.
                      "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers
                      (comments) taken directly from the input HTTP Live Streaming (HLS) manifest.
                      "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in
                      the input source.

                      - **IncludeIframeOnlyStream** *(boolean) --* When enabled, an I-Frame only stream
                      will be included in the output.

                      - **ManifestName** *(string) --* An optional string to include in the name of the
                      manifest.

                      - **ProgramDateTimeIntervalSeconds** *(integer) --* The interval (in seconds) between
                      each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an
                      interval is specified ID3Timed Metadata messages will be generated every 5 seconds
                      using the ingest time of the content. If the interval is not specified, or set to 0,
                      then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed
                      Metadata messages will be generated. Note that irrespective of this parameter, if any
                      ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed
                      through to HLS output.

                      - **RepeatExtXKey** *(boolean) --* When enabled, the EXT-X-KEY tag will be repeated
                      in output manifests.

                      - **StreamSelection** *(dict) --* A StreamSelection configuration.

                        - **MaxVideoBitsPerSecond** *(integer) --* The maximum video bitrate (bps) to
                        include in output.

                        - **MinVideoBitsPerSecond** *(integer) --* The minimum video bitrate (bps) to
                        include in output.

                        - **StreamOrder** *(string) --* A directive that determines the order of streams in
                        the output.

                  - **SegmentDurationSeconds** *(integer) --* Duration (in seconds) of each fragment.
                  Actual fragments will be rounded to the nearest multiple of the source fragment duration.

                - **DashPackage** *(dict) --* A Dynamic Adaptive Streaming over HTTP (DASH) packaging
                configuration.

                  - **DashManifests** *(list) --* A list of DASH manifest configurations.

                    - *(dict) --* A DASH manifest configuration.

                      - **ManifestName** *(string) --* An optional string to include in the name of the
                      manifest.

                      - **MinBufferTimeSeconds** *(integer) --* Minimum duration (in seconds) that a player
                      will buffer media before starting the presentation.

                      - **Profile** *(string) --* The Dynamic Adaptive Streaming over HTTP (DASH) profile
                      type. When set to "HBBTV_1_5", HbbTV 1.5 compliant output is enabled.

                      - **StreamSelection** *(dict) --* A StreamSelection configuration.

                        - **MaxVideoBitsPerSecond** *(integer) --* The maximum video bitrate (bps) to
                        include in output.

                        - **MinVideoBitsPerSecond** *(integer) --* The minimum video bitrate (bps) to
                        include in output.

                        - **StreamOrder** *(string) --* A directive that determines the order of streams in
                        the output.

                  - **Encryption** *(dict) --* A Dynamic Adaptive Streaming over HTTP (DASH) encryption
                  configuration.

                    - **SpekeKeyProvider** *(dict) --* A configuration for accessing an external Secure
                    Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

                      - **RoleArn** *(string) --* An Amazon Resource Name (ARN) of an IAM role that AWS
                      Elemental MediaPackage will assume when accessing the key provider service.

                      - **SystemIds** *(list) --* The system IDs to include in key requests.

                        - *(string) --*

                      - **Url** *(string) --* The URL of the external key provider service.

                  - **SegmentDurationSeconds** *(integer) --* Duration (in seconds) of each segment. Actual
                  segments will be rounded to the nearest multiple of the source segment duration.

                - **HlsPackage** *(dict) --* An HTTP Live Streaming (HLS) packaging configuration.

                  - **Encryption** *(dict) --* An HTTP Live Streaming (HLS) encryption configuration.

                    - **ConstantInitializationVector** *(string) --* A constant initialization vector for
                    encryption (optional). When not specified the initialization vector will be
                    periodically rotated.

                    - **EncryptionMethod** *(string) --* The encryption method to use.

                    - **SpekeKeyProvider** *(dict) --* A configuration for accessing an external Secure
                    Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

                      - **RoleArn** *(string) --* An Amazon Resource Name (ARN) of an IAM role that AWS
                      Elemental MediaPackage will assume when accessing the key provider service.

                      - **SystemIds** *(list) --* The system IDs to include in key requests.

                        - *(string) --*

                      - **Url** *(string) --* The URL of the external key provider service.

                  - **HlsManifests** *(list) --* A list of HLS manifest configurations.

                    - *(dict) --* An HTTP Live Streaming (HLS) manifest configuration.

                      - **AdMarkers** *(string) --* This setting controls how ad markers are included in
                      the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output.
                      "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers
                      (comments) taken directly from the input HTTP Live Streaming (HLS) manifest.
                      "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in
                      the input source.

                      - **IncludeIframeOnlyStream** *(boolean) --* When enabled, an I-Frame only stream
                      will be included in the output.

                      - **ManifestName** *(string) --* An optional string to include in the name of the
                      manifest.

                      - **ProgramDateTimeIntervalSeconds** *(integer) --* The interval (in seconds) between
                      each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an
                      interval is specified ID3Timed Metadata messages will be generated every 5 seconds
                      using the ingest time of the content. If the interval is not specified, or set to 0,
                      then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed
                      Metadata messages will be generated. Note that irrespective of this parameter, if any
                      ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed
                      through to HLS output.

                      - **RepeatExtXKey** *(boolean) --* When enabled, the EXT-X-KEY tag will be repeated
                      in output manifests.

                      - **StreamSelection** *(dict) --* A StreamSelection configuration.

                        - **MaxVideoBitsPerSecond** *(integer) --* The maximum video bitrate (bps) to
                        include in output.

                        - **MinVideoBitsPerSecond** *(integer) --* The minimum video bitrate (bps) to
                        include in output.

                        - **StreamOrder** *(string) --* A directive that determines the order of streams in
                        the output.

                  - **SegmentDurationSeconds** *(integer) --* Duration (in seconds) of each fragment.
                  Actual fragments will be rounded to the nearest multiple of the source fragment duration.

                  - **UseAudioRenditionGroup** *(boolean) --* When enabled, audio streams will be placed in
                  rendition groups in the output.

                - **Id** *(string) --* The ID of the PackagingConfiguration.

                - **MssPackage** *(dict) --* A Microsoft Smooth Streaming (MSS) PackagingConfiguration.

                  - **Encryption** *(dict) --* A Microsoft Smooth Streaming (MSS) encryption configuration.

                    - **SpekeKeyProvider** *(dict) --* A configuration for accessing an external Secure
                    Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

                      - **RoleArn** *(string) --* An Amazon Resource Name (ARN) of an IAM role that AWS
                      Elemental MediaPackage will assume when accessing the key provider service.

                      - **SystemIds** *(list) --* The system IDs to include in key requests.

                        - *(string) --*

                      - **Url** *(string) --* The URL of the external key provider service.

                  - **MssManifests** *(list) --* A list of MSS manifest configurations.

                    - *(dict) --* A Microsoft Smooth Streaming (MSS) manifest configuration.

                      - **ManifestName** *(string) --* An optional string to include in the name of the
                      manifest.

                      - **StreamSelection** *(dict) --* A StreamSelection configuration.

                        - **MaxVideoBitsPerSecond** *(integer) --* The maximum video bitrate (bps) to
                        include in output.

                        - **MinVideoBitsPerSecond** *(integer) --* The minimum video bitrate (bps) to
                        include in output.

                        - **StreamOrder** *(string) --* A directive that determines the order of streams in
                        the output.

                  - **SegmentDurationSeconds** *(integer) --* The duration (in seconds) of each segment.

                - **PackagingGroupId** *(string) --* The ID of a PackagingGroup.

        """


class ListPackagingGroupsPaginator(Boto3Paginator):
    """
    Paginator for `list_packaging_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PaginationConfig: ListPackagingGroupsPaginatePaginationConfigTypeDef = None,
    ) -> ListPackagingGroupsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`MediaPackageVod.Client.list_packaging_groups`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediapackage-vod-2018-11-07/ListPackagingGroups>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PackagingGroups': [
                    {
                        'Arn': 'string',
                        'Id': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --* A collection of MediaPackage VOD PackagingGroup resources.

            - **PackagingGroups** *(list) --* A list of MediaPackage VOD PackagingGroup resources.

              - *(dict) --* A MediaPackage VOD PackagingGroup resource.

                - **Arn** *(string) --* The ARN of the PackagingGroup.

                - **Id** *(string) --* The ID of the PackagingGroup.

        """
