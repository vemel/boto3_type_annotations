"Main interface for mediapackage-vod Client"
from __future__ import annotations

from typing import Any, Dict
from typing_extensions import Literal, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

# pylint: disable=import-self
import mypy_boto3_mediapackage_vod.client as client_scope

# pylint: disable=import-self
import mypy_boto3_mediapackage_vod.paginator as paginator_scope
from mypy_boto3_mediapackage_vod.type_defs import (
    ClientCreateAssetResponseTypeDef,
    ClientCreatePackagingConfigurationCmafPackageTypeDef,
    ClientCreatePackagingConfigurationDashPackageTypeDef,
    ClientCreatePackagingConfigurationHlsPackageTypeDef,
    ClientCreatePackagingConfigurationMssPackageTypeDef,
    ClientCreatePackagingConfigurationResponseTypeDef,
    ClientCreatePackagingGroupResponseTypeDef,
    ClientDescribeAssetResponseTypeDef,
    ClientDescribePackagingConfigurationResponseTypeDef,
    ClientDescribePackagingGroupResponseTypeDef,
    ClientListAssetsResponseTypeDef,
    ClientListPackagingConfigurationsResponseTypeDef,
    ClientListPackagingGroupsResponseTypeDef,
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
    def create_asset(
        self,
        Id: str,
        PackagingGroupId: str,
        SourceArn: str,
        SourceRoleArn: str,
        ResourceId: str = None,
    ) -> ClientCreateAssetResponseTypeDef:
        """
        Creates a new MediaPackage VOD Asset resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediapackage-vod-2018-11-07/CreateAsset>`_

        **Request Syntax**
        ::

          response = client.create_asset(
              Id='string',
              PackagingGroupId='string',
              ResourceId='string',
              SourceArn='string',
              SourceRoleArn='string'
          )
        :type Id: string
        :param Id: **[REQUIRED]** The unique identifier for the Asset.

        :type PackagingGroupId: string
        :param PackagingGroupId: **[REQUIRED]** The ID of the PackagingGroup for the Asset.

        :type ResourceId: string
        :param ResourceId: The resource ID to include in SPEKE key requests.

        :type SourceArn: string
        :param SourceArn: **[REQUIRED]** ARN of the source object in S3.

        :type SourceRoleArn: string
        :param SourceRoleArn: **[REQUIRED]** The IAM role ARN used to access the source S3 bucket.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'EgressEndpoints': [
                    {
                        'PackagingConfigurationId': 'string',
                        'Url': 'string'
                    },
                ],
                'Id': 'string',
                'PackagingGroupId': 'string',
                'ResourceId': 'string',
                'SourceArn': 'string',
                'SourceRoleArn': 'string'
            }
          **Response Structure**

          - *(dict) --* The new MediaPackage VOD Asset resource.

            - **Arn** *(string) --* The ARN of the Asset.

            - **EgressEndpoints** *(list) --* The list of egress endpoints available for the Asset.

              - *(dict) --* The endpoint URL used to access an Asset using one PackagingConfiguration.

                - **PackagingConfigurationId** *(string) --* The ID of the PackagingConfiguration being
                applied to the Asset.

                - **Url** *(string) --* The URL of the parent manifest for the repackaged Asset.

            - **Id** *(string) --* The unique identifier for the Asset.

            - **PackagingGroupId** *(string) --* The ID of the PackagingGroup for the Asset.

            - **ResourceId** *(string) --* The resource ID to include in SPEKE key requests.

            - **SourceArn** *(string) --* ARN of the source object in S3.

            - **SourceRoleArn** *(string) --* The IAM role_arn used to access the source S3 bucket.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_packaging_configuration(
        self,
        Id: str,
        PackagingGroupId: str,
        CmafPackage: ClientCreatePackagingConfigurationCmafPackageTypeDef = None,
        DashPackage: ClientCreatePackagingConfigurationDashPackageTypeDef = None,
        HlsPackage: ClientCreatePackagingConfigurationHlsPackageTypeDef = None,
        MssPackage: ClientCreatePackagingConfigurationMssPackageTypeDef = None,
    ) -> ClientCreatePackagingConfigurationResponseTypeDef:
        """
        Creates a new MediaPackage VOD PackagingConfiguration resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediapackage-vod-2018-11-07/CreatePackagingConfiguration>`_

        **Request Syntax**
        ::

          response = client.create_packaging_configuration(
              CmafPackage={
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
                              'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                          }
                      },
                  ],
                  'SegmentDurationSeconds': 123
              },
              DashPackage={
                  'DashManifests': [
                      {
                          'ManifestName': 'string',
                          'MinBufferTimeSeconds': 123,
                          'Profile': 'NONE'|'HBBTV_1_5',
                          'StreamSelection': {
                              'MaxVideoBitsPerSecond': 123,
                              'MinVideoBitsPerSecond': 123,
                              'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
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
              HlsPackage={
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
                              'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                          }
                      },
                  ],
                  'SegmentDurationSeconds': 123,
                  'UseAudioRenditionGroup': True|False
              },
              Id='string',
              MssPackage={
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
                              'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                          }
                      },
                  ],
                  'SegmentDurationSeconds': 123
              },
              PackagingGroupId='string'
          )
        :type CmafPackage: dict
        :param CmafPackage: A CMAF packaging configuration.

          - **Encryption** *(dict) --* A CMAF encryption configuration.

            - **SpekeKeyProvider** *(dict) --* **[REQUIRED]** A configuration for accessing an external
            Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

              - **RoleArn** *(string) --* **[REQUIRED]** An Amazon Resource Name (ARN) of an IAM role that
              AWS Elemental MediaPackage will assume when accessing the key provider service.

              - **SystemIds** *(list) --* **[REQUIRED]** The system IDs to include in key requests.

                - *(string) --*

              - **Url** *(string) --* **[REQUIRED]** The URL of the external key provider service.

          - **HlsManifests** *(list) --* **[REQUIRED]** A list of HLS manifest configurations.

            - *(dict) --* An HTTP Live Streaming (HLS) manifest configuration.

              - **AdMarkers** *(string) --* This setting controls how ad markers are included in the
              packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output.
              "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments)
              taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates
              ad markers and blackout tags based on SCTE-35 messages in the input source.

              - **IncludeIframeOnlyStream** *(boolean) --* When enabled, an I-Frame only stream will be
              included in the output.

              - **ManifestName** *(string) --* An optional string to include in the name of the manifest.

              - **ProgramDateTimeIntervalSeconds** *(integer) --* The interval (in seconds) between each
              EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is
              specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time
              of the content. If the interval is not specified, or set to 0, then no
              EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata
              messages will be generated. Note that irrespective of this parameter, if any ID3 Timed
              Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.

              - **RepeatExtXKey** *(boolean) --* When enabled, the EXT-X-KEY tag will be repeated in output
              manifests.

              - **StreamSelection** *(dict) --* A StreamSelection configuration.

                - **MaxVideoBitsPerSecond** *(integer) --* The maximum video bitrate (bps) to include in
                output.

                - **MinVideoBitsPerSecond** *(integer) --* The minimum video bitrate (bps) to include in
                output.

                - **StreamOrder** *(string) --* A directive that determines the order of streams in the
                output.

          - **SegmentDurationSeconds** *(integer) --* Duration (in seconds) of each fragment. Actual
          fragments will be rounded to the nearest multiple of the source fragment duration.

        :type DashPackage: dict
        :param DashPackage: A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.

          - **DashManifests** *(list) --* **[REQUIRED]** A list of DASH manifest configurations.

            - *(dict) --* A DASH manifest configuration.

              - **ManifestName** *(string) --* An optional string to include in the name of the manifest.

              - **MinBufferTimeSeconds** *(integer) --* Minimum duration (in seconds) that a player will
              buffer media before starting the presentation.

              - **Profile** *(string) --* The Dynamic Adaptive Streaming over HTTP (DASH) profile type.
              When set to "HBBTV_1_5", HbbTV 1.5 compliant output is enabled.

              - **StreamSelection** *(dict) --* A StreamSelection configuration.

                - **MaxVideoBitsPerSecond** *(integer) --* The maximum video bitrate (bps) to include in
                output.

                - **MinVideoBitsPerSecond** *(integer) --* The minimum video bitrate (bps) to include in
                output.

                - **StreamOrder** *(string) --* A directive that determines the order of streams in the
                output.

          - **Encryption** *(dict) --* A Dynamic Adaptive Streaming over HTTP (DASH) encryption
          configuration.

            - **SpekeKeyProvider** *(dict) --* **[REQUIRED]** A configuration for accessing an external
            Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

              - **RoleArn** *(string) --* **[REQUIRED]** An Amazon Resource Name (ARN) of an IAM role that
              AWS Elemental MediaPackage will assume when accessing the key provider service.

              - **SystemIds** *(list) --* **[REQUIRED]** The system IDs to include in key requests.

                - *(string) --*

              - **Url** *(string) --* **[REQUIRED]** The URL of the external key provider service.

          - **SegmentDurationSeconds** *(integer) --* Duration (in seconds) of each segment. Actual
          segments will be rounded to the nearest multiple of the source segment duration.

        :type HlsPackage: dict
        :param HlsPackage: An HTTP Live Streaming (HLS) packaging configuration.

          - **Encryption** *(dict) --* An HTTP Live Streaming (HLS) encryption configuration.

            - **ConstantInitializationVector** *(string) --* A constant initialization vector for
            encryption (optional). When not specified the initialization vector will be periodically
            rotated.

            - **EncryptionMethod** *(string) --* The encryption method to use.

            - **SpekeKeyProvider** *(dict) --* **[REQUIRED]** A configuration for accessing an external
            Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

              - **RoleArn** *(string) --* **[REQUIRED]** An Amazon Resource Name (ARN) of an IAM role that
              AWS Elemental MediaPackage will assume when accessing the key provider service.

              - **SystemIds** *(list) --* **[REQUIRED]** The system IDs to include in key requests.

                - *(string) --*

              - **Url** *(string) --* **[REQUIRED]** The URL of the external key provider service.

          - **HlsManifests** *(list) --* **[REQUIRED]** A list of HLS manifest configurations.

            - *(dict) --* An HTTP Live Streaming (HLS) manifest configuration.

              - **AdMarkers** *(string) --* This setting controls how ad markers are included in the
              packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output.
              "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments)
              taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates
              ad markers and blackout tags based on SCTE-35 messages in the input source.

              - **IncludeIframeOnlyStream** *(boolean) --* When enabled, an I-Frame only stream will be
              included in the output.

              - **ManifestName** *(string) --* An optional string to include in the name of the manifest.

              - **ProgramDateTimeIntervalSeconds** *(integer) --* The interval (in seconds) between each
              EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is
              specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time
              of the content. If the interval is not specified, or set to 0, then no
              EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata
              messages will be generated. Note that irrespective of this parameter, if any ID3 Timed
              Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.

              - **RepeatExtXKey** *(boolean) --* When enabled, the EXT-X-KEY tag will be repeated in output
              manifests.

              - **StreamSelection** *(dict) --* A StreamSelection configuration.

                - **MaxVideoBitsPerSecond** *(integer) --* The maximum video bitrate (bps) to include in
                output.

                - **MinVideoBitsPerSecond** *(integer) --* The minimum video bitrate (bps) to include in
                output.

                - **StreamOrder** *(string) --* A directive that determines the order of streams in the
                output.

          - **SegmentDurationSeconds** *(integer) --* Duration (in seconds) of each fragment. Actual
          fragments will be rounded to the nearest multiple of the source fragment duration.

          - **UseAudioRenditionGroup** *(boolean) --* When enabled, audio streams will be placed in
          rendition groups in the output.

        :type Id: string
        :param Id: **[REQUIRED]** The ID of the PackagingConfiguration.

        :type MssPackage: dict
        :param MssPackage: A Microsoft Smooth Streaming (MSS) PackagingConfiguration.

          - **Encryption** *(dict) --* A Microsoft Smooth Streaming (MSS) encryption configuration.

            - **SpekeKeyProvider** *(dict) --* **[REQUIRED]** A configuration for accessing an external
            Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

              - **RoleArn** *(string) --* **[REQUIRED]** An Amazon Resource Name (ARN) of an IAM role that
              AWS Elemental MediaPackage will assume when accessing the key provider service.

              - **SystemIds** *(list) --* **[REQUIRED]** The system IDs to include in key requests.

                - *(string) --*

              - **Url** *(string) --* **[REQUIRED]** The URL of the external key provider service.

          - **MssManifests** *(list) --* **[REQUIRED]** A list of MSS manifest configurations.

            - *(dict) --* A Microsoft Smooth Streaming (MSS) manifest configuration.

              - **ManifestName** *(string) --* An optional string to include in the name of the manifest.

              - **StreamSelection** *(dict) --* A StreamSelection configuration.

                - **MaxVideoBitsPerSecond** *(integer) --* The maximum video bitrate (bps) to include in
                output.

                - **MinVideoBitsPerSecond** *(integer) --* The minimum video bitrate (bps) to include in
                output.

                - **StreamOrder** *(string) --* A directive that determines the order of streams in the
                output.

          - **SegmentDurationSeconds** *(integer) --* The duration (in seconds) of each segment.

        :type PackagingGroupId: string
        :param PackagingGroupId: **[REQUIRED]** The ID of a PackagingGroup.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

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
            }
          **Response Structure**

          - *(dict) --* The new MediaPackage VOD PackagingConfiguration resource.

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

                  - **AdMarkers** *(string) --* This setting controls how ad markers are included in the
                  packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output.
                  "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments)
                  taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED"
                  generates ad markers and blackout tags based on SCTE-35 messages in the input source.

                  - **IncludeIframeOnlyStream** *(boolean) --* When enabled, an I-Frame only stream will be
                  included in the output.

                  - **ManifestName** *(string) --* An optional string to include in the name of the
                  manifest.

                  - **ProgramDateTimeIntervalSeconds** *(integer) --* The interval (in seconds) between
                  each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval
                  is specified ID3Timed Metadata messages will be generated every 5 seconds using the
                  ingest time of the content. If the interval is not specified, or set to 0, then no
                  EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata
                  messages will be generated. Note that irrespective of this parameter, if any ID3 Timed
                  Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS
                  output.

                  - **RepeatExtXKey** *(boolean) --* When enabled, the EXT-X-KEY tag will be repeated in
                  output manifests.

                  - **StreamSelection** *(dict) --* A StreamSelection configuration.

                    - **MaxVideoBitsPerSecond** *(integer) --* The maximum video bitrate (bps) to include
                    in output.

                    - **MinVideoBitsPerSecond** *(integer) --* The minimum video bitrate (bps) to include
                    in output.

                    - **StreamOrder** *(string) --* A directive that determines the order of streams in the
                    output.

              - **SegmentDurationSeconds** *(integer) --* Duration (in seconds) of each fragment. Actual
              fragments will be rounded to the nearest multiple of the source fragment duration.

            - **DashPackage** *(dict) --* A Dynamic Adaptive Streaming over HTTP (DASH) packaging
            configuration.

              - **DashManifests** *(list) --* A list of DASH manifest configurations.

                - *(dict) --* A DASH manifest configuration.

                  - **ManifestName** *(string) --* An optional string to include in the name of the
                  manifest.

                  - **MinBufferTimeSeconds** *(integer) --* Minimum duration (in seconds) that a player
                  will buffer media before starting the presentation.

                  - **Profile** *(string) --* The Dynamic Adaptive Streaming over HTTP (DASH) profile type.
                  When set to "HBBTV_1_5", HbbTV 1.5 compliant output is enabled.

                  - **StreamSelection** *(dict) --* A StreamSelection configuration.

                    - **MaxVideoBitsPerSecond** *(integer) --* The maximum video bitrate (bps) to include
                    in output.

                    - **MinVideoBitsPerSecond** *(integer) --* The minimum video bitrate (bps) to include
                    in output.

                    - **StreamOrder** *(string) --* A directive that determines the order of streams in the
                    output.

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
                encryption (optional). When not specified the initialization vector will be periodically
                rotated.

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

                  - **AdMarkers** *(string) --* This setting controls how ad markers are included in the
                  packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output.
                  "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments)
                  taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED"
                  generates ad markers and blackout tags based on SCTE-35 messages in the input source.

                  - **IncludeIframeOnlyStream** *(boolean) --* When enabled, an I-Frame only stream will be
                  included in the output.

                  - **ManifestName** *(string) --* An optional string to include in the name of the
                  manifest.

                  - **ProgramDateTimeIntervalSeconds** *(integer) --* The interval (in seconds) between
                  each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval
                  is specified ID3Timed Metadata messages will be generated every 5 seconds using the
                  ingest time of the content. If the interval is not specified, or set to 0, then no
                  EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata
                  messages will be generated. Note that irrespective of this parameter, if any ID3 Timed
                  Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS
                  output.

                  - **RepeatExtXKey** *(boolean) --* When enabled, the EXT-X-KEY tag will be repeated in
                  output manifests.

                  - **StreamSelection** *(dict) --* A StreamSelection configuration.

                    - **MaxVideoBitsPerSecond** *(integer) --* The maximum video bitrate (bps) to include
                    in output.

                    - **MinVideoBitsPerSecond** *(integer) --* The minimum video bitrate (bps) to include
                    in output.

                    - **StreamOrder** *(string) --* A directive that determines the order of streams in the
                    output.

              - **SegmentDurationSeconds** *(integer) --* Duration (in seconds) of each fragment. Actual
              fragments will be rounded to the nearest multiple of the source fragment duration.

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

                    - **MaxVideoBitsPerSecond** *(integer) --* The maximum video bitrate (bps) to include
                    in output.

                    - **MinVideoBitsPerSecond** *(integer) --* The minimum video bitrate (bps) to include
                    in output.

                    - **StreamOrder** *(string) --* A directive that determines the order of streams in the
                    output.

              - **SegmentDurationSeconds** *(integer) --* The duration (in seconds) of each segment.

            - **PackagingGroupId** *(string) --* The ID of a PackagingGroup.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_packaging_group(
        self, Id: str
    ) -> ClientCreatePackagingGroupResponseTypeDef:
        """
        Creates a new MediaPackage VOD PackagingGroup resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediapackage-vod-2018-11-07/CreatePackagingGroup>`_

        **Request Syntax**
        ::

          response = client.create_packaging_group(
              Id='string'
          )
        :type Id: string
        :param Id: **[REQUIRED]** The ID of the PackagingGroup.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'Id': 'string'
            }
          **Response Structure**

          - *(dict) --* The new MediaPackage VOD PackagingGroup resource.

            - **Arn** *(string) --* The ARN of the PackagingGroup.

            - **Id** *(string) --* The ID of the PackagingGroup.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_asset(self, Id: str) -> Dict[str, Any]:
        """
        Deletes an existing MediaPackage VOD Asset resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediapackage-vod-2018-11-07/DeleteAsset>`_

        **Request Syntax**
        ::

          response = client.delete_asset(
              Id='string'
          )
        :type Id: string
        :param Id: **[REQUIRED]** The ID of the MediaPackage VOD Asset resource to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --* The MediaPackage VOD Asset resource has been deleted.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_packaging_configuration(self, Id: str) -> Dict[str, Any]:
        """
        Deletes a MediaPackage VOD PackagingConfiguration resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediapackage-vod-2018-11-07/DeletePackagingConfiguration>`_

        **Request Syntax**
        ::

          response = client.delete_packaging_configuration(
              Id='string'
          )
        :type Id: string
        :param Id: **[REQUIRED]** The ID of the MediaPackage VOD PackagingConfiguration resource to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --* The MediaPackage VOD PackagingConfiguration resource has been deleted.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_packaging_group(self, Id: str) -> Dict[str, Any]:
        """
        Deletes a MediaPackage VOD PackagingGroup resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediapackage-vod-2018-11-07/DeletePackagingGroup>`_

        **Request Syntax**
        ::

          response = client.delete_packaging_group(
              Id='string'
          )
        :type Id: string
        :param Id: **[REQUIRED]** The ID of the MediaPackage VOD PackagingGroup resource to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --* The MediaPackage VOD PackagingGroup resource has been deleted.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_asset(self, Id: str) -> ClientDescribeAssetResponseTypeDef:
        """
        Returns a description of a MediaPackage VOD Asset resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediapackage-vod-2018-11-07/DescribeAsset>`_

        **Request Syntax**
        ::

          response = client.describe_asset(
              Id='string'
          )
        :type Id: string
        :param Id: **[REQUIRED]** The ID of an MediaPackage VOD Asset resource.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'EgressEndpoints': [
                    {
                        'PackagingConfigurationId': 'string',
                        'Url': 'string'
                    },
                ],
                'Id': 'string',
                'PackagingGroupId': 'string',
                'ResourceId': 'string',
                'SourceArn': 'string',
                'SourceRoleArn': 'string'
            }
          **Response Structure**

          - *(dict) --* A MediaPackage VOD Asset resource.

            - **Arn** *(string) --* The ARN of the Asset.

            - **EgressEndpoints** *(list) --* The list of egress endpoints available for the Asset.

              - *(dict) --* The endpoint URL used to access an Asset using one PackagingConfiguration.

                - **PackagingConfigurationId** *(string) --* The ID of the PackagingConfiguration being
                applied to the Asset.

                - **Url** *(string) --* The URL of the parent manifest for the repackaged Asset.

            - **Id** *(string) --* The unique identifier for the Asset.

            - **PackagingGroupId** *(string) --* The ID of the PackagingGroup for the Asset.

            - **ResourceId** *(string) --* The resource ID to include in SPEKE key requests.

            - **SourceArn** *(string) --* ARN of the source object in S3.

            - **SourceRoleArn** *(string) --* The IAM role_arn used to access the source S3 bucket.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_packaging_configuration(
        self, Id: str
    ) -> ClientDescribePackagingConfigurationResponseTypeDef:
        """
        Returns a description of a MediaPackage VOD PackagingConfiguration resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediapackage-vod-2018-11-07/DescribePackagingConfiguration>`_
        <https://docs.aws.amazon.com/goto/WebAPI/mediapackage-vod-2018-11-07/DescribePackagingConfiguration>`_

        **Request Syntax**
        ::

          response = client.describe_packaging_configuration(
              Id='string'
          )
        :type Id: string
        :param Id: **[REQUIRED]** The ID of a MediaPackage VOD PackagingConfiguration resource.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

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
            }
          **Response Structure**

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

                  - **AdMarkers** *(string) --* This setting controls how ad markers are included in the
                  packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output.
                  "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments)
                  taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED"
                  generates ad markers and blackout tags based on SCTE-35 messages in the input source.

                  - **IncludeIframeOnlyStream** *(boolean) --* When enabled, an I-Frame only stream will be
                  included in the output.

                  - **ManifestName** *(string) --* An optional string to include in the name of the
                  manifest.

                  - **ProgramDateTimeIntervalSeconds** *(integer) --* The interval (in seconds) between
                  each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval
                  is specified ID3Timed Metadata messages will be generated every 5 seconds using the
                  ingest time of the content. If the interval is not specified, or set to 0, then no
                  EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata
                  messages will be generated. Note that irrespective of this parameter, if any ID3 Timed
                  Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS
                  output.

                  - **RepeatExtXKey** *(boolean) --* When enabled, the EXT-X-KEY tag will be repeated in
                  output manifests.

                  - **StreamSelection** *(dict) --* A StreamSelection configuration.

                    - **MaxVideoBitsPerSecond** *(integer) --* The maximum video bitrate (bps) to include
                    in output.

                    - **MinVideoBitsPerSecond** *(integer) --* The minimum video bitrate (bps) to include
                    in output.

                    - **StreamOrder** *(string) --* A directive that determines the order of streams in the
                    output.

              - **SegmentDurationSeconds** *(integer) --* Duration (in seconds) of each fragment. Actual
              fragments will be rounded to the nearest multiple of the source fragment duration.

            - **DashPackage** *(dict) --* A Dynamic Adaptive Streaming over HTTP (DASH) packaging
            configuration.

              - **DashManifests** *(list) --* A list of DASH manifest configurations.

                - *(dict) --* A DASH manifest configuration.

                  - **ManifestName** *(string) --* An optional string to include in the name of the
                  manifest.

                  - **MinBufferTimeSeconds** *(integer) --* Minimum duration (in seconds) that a player
                  will buffer media before starting the presentation.

                  - **Profile** *(string) --* The Dynamic Adaptive Streaming over HTTP (DASH) profile type.
                  When set to "HBBTV_1_5", HbbTV 1.5 compliant output is enabled.

                  - **StreamSelection** *(dict) --* A StreamSelection configuration.

                    - **MaxVideoBitsPerSecond** *(integer) --* The maximum video bitrate (bps) to include
                    in output.

                    - **MinVideoBitsPerSecond** *(integer) --* The minimum video bitrate (bps) to include
                    in output.

                    - **StreamOrder** *(string) --* A directive that determines the order of streams in the
                    output.

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
                encryption (optional). When not specified the initialization vector will be periodically
                rotated.

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

                  - **AdMarkers** *(string) --* This setting controls how ad markers are included in the
                  packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output.
                  "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments)
                  taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED"
                  generates ad markers and blackout tags based on SCTE-35 messages in the input source.

                  - **IncludeIframeOnlyStream** *(boolean) --* When enabled, an I-Frame only stream will be
                  included in the output.

                  - **ManifestName** *(string) --* An optional string to include in the name of the
                  manifest.

                  - **ProgramDateTimeIntervalSeconds** *(integer) --* The interval (in seconds) between
                  each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval
                  is specified ID3Timed Metadata messages will be generated every 5 seconds using the
                  ingest time of the content. If the interval is not specified, or set to 0, then no
                  EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata
                  messages will be generated. Note that irrespective of this parameter, if any ID3 Timed
                  Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS
                  output.

                  - **RepeatExtXKey** *(boolean) --* When enabled, the EXT-X-KEY tag will be repeated in
                  output manifests.

                  - **StreamSelection** *(dict) --* A StreamSelection configuration.

                    - **MaxVideoBitsPerSecond** *(integer) --* The maximum video bitrate (bps) to include
                    in output.

                    - **MinVideoBitsPerSecond** *(integer) --* The minimum video bitrate (bps) to include
                    in output.

                    - **StreamOrder** *(string) --* A directive that determines the order of streams in the
                    output.

              - **SegmentDurationSeconds** *(integer) --* Duration (in seconds) of each fragment. Actual
              fragments will be rounded to the nearest multiple of the source fragment duration.

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

                    - **MaxVideoBitsPerSecond** *(integer) --* The maximum video bitrate (bps) to include
                    in output.

                    - **MinVideoBitsPerSecond** *(integer) --* The minimum video bitrate (bps) to include
                    in output.

                    - **StreamOrder** *(string) --* A directive that determines the order of streams in the
                    output.

              - **SegmentDurationSeconds** *(integer) --* The duration (in seconds) of each segment.

            - **PackagingGroupId** *(string) --* The ID of a PackagingGroup.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_packaging_group(
        self, Id: str
    ) -> ClientDescribePackagingGroupResponseTypeDef:
        """
        Returns a description of a MediaPackage VOD PackagingGroup resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediapackage-vod-2018-11-07/DescribePackagingGroup>`_

        **Request Syntax**
        ::

          response = client.describe_packaging_group(
              Id='string'
          )
        :type Id: string
        :param Id: **[REQUIRED]** The ID of a MediaPackage VOD PackagingGroup resource.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'Id': 'string'
            }
          **Response Structure**

          - *(dict) --* A MediaPackage VOD PackagingGroup resource.

            - **Arn** *(string) --* The ARN of the PackagingGroup.

            - **Id** *(string) --* The ID of the PackagingGroup.
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
    def list_assets(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        PackagingGroupId: str = None,
    ) -> ClientListAssetsResponseTypeDef:
        """
        Returns a collection of MediaPackage VOD Asset resources.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediapackage-vod-2018-11-07/ListAssets>`_

        **Request Syntax**
        ::

          response = client.list_assets(
              MaxResults=123,
              NextToken='string',
              PackagingGroupId='string'
          )
        :type MaxResults: integer
        :param MaxResults: Upper bound on number of records to return.

        :type NextToken: string
        :param NextToken: A token used to resume pagination from the end of a previous request.

        :type PackagingGroupId: string
        :param PackagingGroupId: Returns Assets associated with the specified PackagingGroup.

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
                'NextToken': 'string'
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

            - **NextToken** *(string) --* A token that can be used to resume pagination from the end of the
            collection.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_packaging_configurations(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        PackagingGroupId: str = None,
    ) -> ClientListPackagingConfigurationsResponseTypeDef:
        """
        Returns a collection of MediaPackage VOD PackagingConfiguration resources.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediapackage-vod-2018-11-07/ListPackagingConfigurations>`_

        **Request Syntax**
        ::

          response = client.list_packaging_configurations(
              MaxResults=123,
              NextToken='string',
              PackagingGroupId='string'
          )
        :type MaxResults: integer
        :param MaxResults: Upper bound on number of records to return.

        :type NextToken: string
        :param NextToken: A token used to resume pagination from the end of a previous request.

        :type PackagingGroupId: string
        :param PackagingGroupId: Returns MediaPackage VOD PackagingConfigurations associated with the
        specified PackagingGroup.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextToken': 'string',
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

            - **NextToken** *(string) --* A token that can be used to resume pagination from the end of the
            collection.

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_packaging_groups(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListPackagingGroupsResponseTypeDef:
        """
        Returns a collection of MediaPackage VOD PackagingGroup resources.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediapackage-vod-2018-11-07/ListPackagingGroups>`_

        **Request Syntax**
        ::

          response = client.list_packaging_groups(
              MaxResults=123,
              NextToken='string'
          )
        :type MaxResults: integer
        :param MaxResults: Upper bound on number of records to return.

        :type NextToken: string
        :param NextToken: A token used to resume pagination from the end of a previous request.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextToken': 'string',
                'PackagingGroups': [
                    {
                        'Arn': 'string',
                        'Id': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --* A collection of MediaPackage VOD PackagingGroup resources.

            - **NextToken** *(string) --* A token that can be used to resume pagination from the end of the
            collection.

            - **PackagingGroups** *(list) --* A list of MediaPackage VOD PackagingGroup resources.

              - *(dict) --* A MediaPackage VOD PackagingGroup resource.

                - **Arn** *(string) --* The ARN of the PackagingGroup.

                - **Id** *(string) --* The ID of the PackagingGroup.

        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_assets"]
    ) -> paginator_scope.ListAssetsPaginator:
        """
        Get Paginator for `list_assets` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_packaging_configurations"]
    ) -> paginator_scope.ListPackagingConfigurationsPaginator:
        """
        Get Paginator for `list_packaging_configurations` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_packaging_groups"]
    ) -> paginator_scope.ListPackagingGroupsPaginator:
        """
        Get Paginator for `list_packaging_groups` operation.
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
    ForbiddenException: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
    NotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
    UnprocessableEntityException: Boto3ClientError
