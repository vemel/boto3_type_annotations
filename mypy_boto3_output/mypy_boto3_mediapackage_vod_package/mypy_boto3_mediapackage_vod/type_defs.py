"Main interface for mediapackage-vod type defs"
from __future__ import annotations

from typing import Any, Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateAssetResponseEgressEndpointsTypeDef",
    "ClientCreateAssetResponseTypeDef",
    "ClientCreatePackagingConfigurationCmafPackageEncryptionTypeDef",
    "ClientCreatePackagingConfigurationCmafPackageHlsManifestsStreamSelectionTypeDef",
    "ClientCreatePackagingConfigurationCmafPackageHlsManifestsTypeDef",
    "ClientCreatePackagingConfigurationCmafPackageTypeDef",
    "ClientCreatePackagingConfigurationDashPackageDashManifestsStreamSelectionTypeDef",
    "ClientCreatePackagingConfigurationDashPackageDashManifestsTypeDef",
    "ClientCreatePackagingConfigurationDashPackageTypeDef",
    "ClientCreatePackagingConfigurationHlsPackageEncryptionTypeDef",
    "ClientCreatePackagingConfigurationHlsPackageHlsManifestsStreamSelectionTypeDef",
    "ClientCreatePackagingConfigurationHlsPackageHlsManifestsTypeDef",
    "ClientCreatePackagingConfigurationHlsPackageTypeDef",
    "ClientCreatePackagingConfigurationMssPackageEncryptionTypeDef",
    "ClientCreatePackagingConfigurationMssPackageMssManifestsStreamSelectionTypeDef",
    "ClientCreatePackagingConfigurationMssPackageMssManifestsTypeDef",
    "ClientCreatePackagingConfigurationMssPackageTypeDef",
    "ClientCreatePackagingConfigurationResponseCmafPackageEncryptionTypeDef",
    "ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef",
    "ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef",
    "ClientCreatePackagingConfigurationResponseCmafPackageTypeDef",
    "ClientCreatePackagingConfigurationResponseHlsPackageEncryptionTypeDef",
    "ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef",
    "ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef",
    "ClientCreatePackagingConfigurationResponseHlsPackageTypeDef",
    "ClientCreatePackagingConfigurationResponseMssPackageEncryptionTypeDef",
    "ClientCreatePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef",
    "ClientCreatePackagingConfigurationResponseMssPackageMssManifestsTypeDef",
    "ClientCreatePackagingConfigurationResponseMssPackageTypeDef",
    "ClientCreatePackagingConfigurationResponseTypeDef",
    "ClientCreatePackagingGroupResponseTypeDef",
    "ClientDescribeAssetResponseEgressEndpointsTypeDef",
    "ClientDescribeAssetResponseTypeDef",
    "ClientDescribePackagingConfigurationResponseCmafPackageEncryptionTypeDef",
    "ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef",
    "ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef",
    "ClientDescribePackagingConfigurationResponseCmafPackageTypeDef",
    "ClientDescribePackagingConfigurationResponseHlsPackageEncryptionTypeDef",
    "ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef",
    "ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef",
    "ClientDescribePackagingConfigurationResponseHlsPackageTypeDef",
    "ClientDescribePackagingConfigurationResponseMssPackageEncryptionTypeDef",
    "ClientDescribePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef",
    "ClientDescribePackagingConfigurationResponseMssPackageMssManifestsTypeDef",
    "ClientDescribePackagingConfigurationResponseMssPackageTypeDef",
    "ClientDescribePackagingConfigurationResponseTypeDef",
    "ClientDescribePackagingGroupResponseTypeDef",
    "ClientListAssetsResponseAssetsTypeDef",
    "ClientListAssetsResponseTypeDef",
    "ClientListPackagingConfigurationsResponseTypeDef",
    "ClientListPackagingGroupsResponsePackagingGroupsTypeDef",
    "ClientListPackagingGroupsResponseTypeDef",
    "ListAssetsPaginatePaginationConfigTypeDef",
    "ListAssetsPaginateResponseAssetsTypeDef",
    "ListAssetsPaginateResponseTypeDef",
    "ListPackagingConfigurationsPaginatePaginationConfigTypeDef",
    "ListPackagingConfigurationsPaginateResponseTypeDef",
    "ListPackagingGroupsPaginatePaginationConfigTypeDef",
    "ListPackagingGroupsPaginateResponsePackagingGroupsTypeDef",
    "ListPackagingGroupsPaginateResponseTypeDef",
)


_ClientCreateAssetResponseEgressEndpointsTypeDef = TypedDict(
    "_ClientCreateAssetResponseEgressEndpointsTypeDef",
    {"PackagingConfigurationId": str, "Url": str},
    total=False,
)


class ClientCreateAssetResponseEgressEndpointsTypeDef(
    _ClientCreateAssetResponseEgressEndpointsTypeDef
):
    """
    Type definition for `ClientCreateAssetResponse` `EgressEndpoints`

    - **PackagingConfigurationId** *(string) --* The ID of the PackagingConfiguration being
    applied to the Asset.

    - **Url** *(string) --* The URL of the parent manifest for the repackaged Asset.
    """


_ClientCreateAssetResponseTypeDef = TypedDict(
    "_ClientCreateAssetResponseTypeDef",
    {
        "Arn": str,
        "EgressEndpoints": List[ClientCreateAssetResponseEgressEndpointsTypeDef],
        "Id": str,
        "PackagingGroupId": str,
        "ResourceId": str,
        "SourceArn": str,
        "SourceRoleArn": str,
    },
    total=False,
)


class ClientCreateAssetResponseTypeDef(_ClientCreateAssetResponseTypeDef):
    """
    Type definition for `ClientCreateAsset` `Response`

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


_ClientCreatePackagingConfigurationCmafPackageEncryptionTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationCmafPackageEncryptionTypeDef",
    {"SpekeKeyProvider": Dict[str, Any]},
)


class ClientCreatePackagingConfigurationCmafPackageEncryptionTypeDef(
    _ClientCreatePackagingConfigurationCmafPackageEncryptionTypeDef
):
    """
    Type definition for `ClientCreatePackagingConfigurationCmafPackage` `Encryption`

    - **SpekeKeyProvider** *(dict) --* **[REQUIRED]** A configuration for accessing an external
    Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

      - **RoleArn** *(string) --* **[REQUIRED]** An Amazon Resource Name (ARN) of an IAM role that
      AWS Elemental MediaPackage will assume when accessing the key provider service.

      - **SystemIds** *(list) --* **[REQUIRED]** The system IDs to include in key requests.

        - *(string) --*

      - **Url** *(string) --* **[REQUIRED]** The URL of the external key provider service.
    """


_ClientCreatePackagingConfigurationCmafPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationCmafPackageHlsManifestsStreamSelectionTypeDef",
    {"MaxVideoBitsPerSecond": int, "MinVideoBitsPerSecond": int, "StreamOrder": str},
    total=False,
)


class ClientCreatePackagingConfigurationCmafPackageHlsManifestsStreamSelectionTypeDef(
    _ClientCreatePackagingConfigurationCmafPackageHlsManifestsStreamSelectionTypeDef
):
    """
    Type definition for `ClientCreatePackagingConfigurationCmafPackageHlsManifests` `StreamSelection`

    - **MaxVideoBitsPerSecond** *(integer) --* The maximum video bitrate (bps) to include in
    output.

    - **MinVideoBitsPerSecond** *(integer) --* The minimum video bitrate (bps) to include in
    output.

    - **StreamOrder** *(string) --* A directive that determines the order of streams in the
    output.
    """


_ClientCreatePackagingConfigurationCmafPackageHlsManifestsTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationCmafPackageHlsManifestsTypeDef",
    {
        "AdMarkers": str,
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "ProgramDateTimeIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "StreamSelection": ClientCreatePackagingConfigurationCmafPackageHlsManifestsStreamSelectionTypeDef,
    },
    total=False,
)


class ClientCreatePackagingConfigurationCmafPackageHlsManifestsTypeDef(
    _ClientCreatePackagingConfigurationCmafPackageHlsManifestsTypeDef
):
    """
    Type definition for `ClientCreatePackagingConfigurationCmafPackage` `HlsManifests`

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
    """


_RequiredClientCreatePackagingConfigurationCmafPackageTypeDef = TypedDict(
    "_RequiredClientCreatePackagingConfigurationCmafPackageTypeDef",
    {
        "HlsManifests": List[
            ClientCreatePackagingConfigurationCmafPackageHlsManifestsTypeDef
        ]
    },
)
_OptionalClientCreatePackagingConfigurationCmafPackageTypeDef = TypedDict(
    "_OptionalClientCreatePackagingConfigurationCmafPackageTypeDef",
    {
        "Encryption": ClientCreatePackagingConfigurationCmafPackageEncryptionTypeDef,
        "SegmentDurationSeconds": int,
    },
    total=False,
)


class ClientCreatePackagingConfigurationCmafPackageTypeDef(
    _RequiredClientCreatePackagingConfigurationCmafPackageTypeDef,
    _OptionalClientCreatePackagingConfigurationCmafPackageTypeDef,
):
    """
    Type definition for `ClientCreatePackagingConfiguration` `CmafPackage`

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
    """


_ClientCreatePackagingConfigurationDashPackageDashManifestsStreamSelectionTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationDashPackageDashManifestsStreamSelectionTypeDef",
    {"MaxVideoBitsPerSecond": int, "MinVideoBitsPerSecond": int, "StreamOrder": str},
    total=False,
)


class ClientCreatePackagingConfigurationDashPackageDashManifestsStreamSelectionTypeDef(
    _ClientCreatePackagingConfigurationDashPackageDashManifestsStreamSelectionTypeDef
):
    """
    Type definition for `ClientCreatePackagingConfigurationDashPackageDashManifests` `StreamSelection`

    - **MaxVideoBitsPerSecond** *(integer) --* The maximum video bitrate (bps) to include in
    output.

    - **MinVideoBitsPerSecond** *(integer) --* The minimum video bitrate (bps) to include in
    output.

    - **StreamOrder** *(string) --* A directive that determines the order of streams in the
    output.
    """


_ClientCreatePackagingConfigurationDashPackageDashManifestsTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationDashPackageDashManifestsTypeDef",
    {
        "ManifestName": str,
        "MinBufferTimeSeconds": int,
        "Profile": str,
        "StreamSelection": ClientCreatePackagingConfigurationDashPackageDashManifestsStreamSelectionTypeDef,
    },
    total=False,
)


class ClientCreatePackagingConfigurationDashPackageDashManifestsTypeDef(
    _ClientCreatePackagingConfigurationDashPackageDashManifestsTypeDef
):
    """
    Type definition for `ClientCreatePackagingConfigurationDashPackage` `DashManifests`

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
    """


_RequiredClientCreatePackagingConfigurationDashPackageTypeDef = TypedDict(
    "_RequiredClientCreatePackagingConfigurationDashPackageTypeDef",
    {
        "DashManifests": List[
            ClientCreatePackagingConfigurationDashPackageDashManifestsTypeDef
        ]
    },
)
_OptionalClientCreatePackagingConfigurationDashPackageTypeDef = TypedDict(
    "_OptionalClientCreatePackagingConfigurationDashPackageTypeDef",
    {"Encryption": Dict[str, Any], "SegmentDurationSeconds": int},
    total=False,
)


class ClientCreatePackagingConfigurationDashPackageTypeDef(
    _RequiredClientCreatePackagingConfigurationDashPackageTypeDef,
    _OptionalClientCreatePackagingConfigurationDashPackageTypeDef,
):
    """
    Type definition for `ClientCreatePackagingConfiguration` `DashPackage`

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
    """


_RequiredClientCreatePackagingConfigurationHlsPackageEncryptionTypeDef = TypedDict(
    "_RequiredClientCreatePackagingConfigurationHlsPackageEncryptionTypeDef",
    {"SpekeKeyProvider": Dict[str, Any]},
)
_OptionalClientCreatePackagingConfigurationHlsPackageEncryptionTypeDef = TypedDict(
    "_OptionalClientCreatePackagingConfigurationHlsPackageEncryptionTypeDef",
    {"ConstantInitializationVector": str, "EncryptionMethod": str},
    total=False,
)


class ClientCreatePackagingConfigurationHlsPackageEncryptionTypeDef(
    _RequiredClientCreatePackagingConfigurationHlsPackageEncryptionTypeDef,
    _OptionalClientCreatePackagingConfigurationHlsPackageEncryptionTypeDef,
):
    """
    Type definition for `ClientCreatePackagingConfigurationHlsPackage` `Encryption`

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
    """


_ClientCreatePackagingConfigurationHlsPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationHlsPackageHlsManifestsStreamSelectionTypeDef",
    {"MaxVideoBitsPerSecond": int, "MinVideoBitsPerSecond": int, "StreamOrder": str},
    total=False,
)


class ClientCreatePackagingConfigurationHlsPackageHlsManifestsStreamSelectionTypeDef(
    _ClientCreatePackagingConfigurationHlsPackageHlsManifestsStreamSelectionTypeDef
):
    """
    Type definition for `ClientCreatePackagingConfigurationHlsPackageHlsManifests` `StreamSelection`

    - **MaxVideoBitsPerSecond** *(integer) --* The maximum video bitrate (bps) to include in
    output.

    - **MinVideoBitsPerSecond** *(integer) --* The minimum video bitrate (bps) to include in
    output.

    - **StreamOrder** *(string) --* A directive that determines the order of streams in the
    output.
    """


_ClientCreatePackagingConfigurationHlsPackageHlsManifestsTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationHlsPackageHlsManifestsTypeDef",
    {
        "AdMarkers": str,
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "ProgramDateTimeIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "StreamSelection": ClientCreatePackagingConfigurationHlsPackageHlsManifestsStreamSelectionTypeDef,
    },
    total=False,
)


class ClientCreatePackagingConfigurationHlsPackageHlsManifestsTypeDef(
    _ClientCreatePackagingConfigurationHlsPackageHlsManifestsTypeDef
):
    """
    Type definition for `ClientCreatePackagingConfigurationHlsPackage` `HlsManifests`

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
    """


_RequiredClientCreatePackagingConfigurationHlsPackageTypeDef = TypedDict(
    "_RequiredClientCreatePackagingConfigurationHlsPackageTypeDef",
    {
        "HlsManifests": List[
            ClientCreatePackagingConfigurationHlsPackageHlsManifestsTypeDef
        ]
    },
)
_OptionalClientCreatePackagingConfigurationHlsPackageTypeDef = TypedDict(
    "_OptionalClientCreatePackagingConfigurationHlsPackageTypeDef",
    {
        "Encryption": ClientCreatePackagingConfigurationHlsPackageEncryptionTypeDef,
        "SegmentDurationSeconds": int,
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)


class ClientCreatePackagingConfigurationHlsPackageTypeDef(
    _RequiredClientCreatePackagingConfigurationHlsPackageTypeDef,
    _OptionalClientCreatePackagingConfigurationHlsPackageTypeDef,
):
    """
    Type definition for `ClientCreatePackagingConfiguration` `HlsPackage`

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
    """


_ClientCreatePackagingConfigurationMssPackageEncryptionTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationMssPackageEncryptionTypeDef",
    {"SpekeKeyProvider": Dict[str, Any]},
)


class ClientCreatePackagingConfigurationMssPackageEncryptionTypeDef(
    _ClientCreatePackagingConfigurationMssPackageEncryptionTypeDef
):
    """
    Type definition for `ClientCreatePackagingConfigurationMssPackage` `Encryption`

    - **SpekeKeyProvider** *(dict) --* **[REQUIRED]** A configuration for accessing an external
    Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

      - **RoleArn** *(string) --* **[REQUIRED]** An Amazon Resource Name (ARN) of an IAM role that
      AWS Elemental MediaPackage will assume when accessing the key provider service.

      - **SystemIds** *(list) --* **[REQUIRED]** The system IDs to include in key requests.

        - *(string) --*

      - **Url** *(string) --* **[REQUIRED]** The URL of the external key provider service.
    """


_ClientCreatePackagingConfigurationMssPackageMssManifestsStreamSelectionTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationMssPackageMssManifestsStreamSelectionTypeDef",
    {"MaxVideoBitsPerSecond": int, "MinVideoBitsPerSecond": int, "StreamOrder": str},
    total=False,
)


class ClientCreatePackagingConfigurationMssPackageMssManifestsStreamSelectionTypeDef(
    _ClientCreatePackagingConfigurationMssPackageMssManifestsStreamSelectionTypeDef
):
    """
    Type definition for `ClientCreatePackagingConfigurationMssPackageMssManifests` `StreamSelection`

    - **MaxVideoBitsPerSecond** *(integer) --* The maximum video bitrate (bps) to include in
    output.

    - **MinVideoBitsPerSecond** *(integer) --* The minimum video bitrate (bps) to include in
    output.

    - **StreamOrder** *(string) --* A directive that determines the order of streams in the
    output.
    """


_ClientCreatePackagingConfigurationMssPackageMssManifestsTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationMssPackageMssManifestsTypeDef",
    {
        "ManifestName": str,
        "StreamSelection": ClientCreatePackagingConfigurationMssPackageMssManifestsStreamSelectionTypeDef,
    },
    total=False,
)


class ClientCreatePackagingConfigurationMssPackageMssManifestsTypeDef(
    _ClientCreatePackagingConfigurationMssPackageMssManifestsTypeDef
):
    """
    Type definition for `ClientCreatePackagingConfigurationMssPackage` `MssManifests`

    - **ManifestName** *(string) --* An optional string to include in the name of the manifest.

    - **StreamSelection** *(dict) --* A StreamSelection configuration.

      - **MaxVideoBitsPerSecond** *(integer) --* The maximum video bitrate (bps) to include in
      output.

      - **MinVideoBitsPerSecond** *(integer) --* The minimum video bitrate (bps) to include in
      output.

      - **StreamOrder** *(string) --* A directive that determines the order of streams in the
      output.
    """


_RequiredClientCreatePackagingConfigurationMssPackageTypeDef = TypedDict(
    "_RequiredClientCreatePackagingConfigurationMssPackageTypeDef",
    {
        "MssManifests": List[
            ClientCreatePackagingConfigurationMssPackageMssManifestsTypeDef
        ]
    },
)
_OptionalClientCreatePackagingConfigurationMssPackageTypeDef = TypedDict(
    "_OptionalClientCreatePackagingConfigurationMssPackageTypeDef",
    {
        "Encryption": ClientCreatePackagingConfigurationMssPackageEncryptionTypeDef,
        "SegmentDurationSeconds": int,
    },
    total=False,
)


class ClientCreatePackagingConfigurationMssPackageTypeDef(
    _RequiredClientCreatePackagingConfigurationMssPackageTypeDef,
    _OptionalClientCreatePackagingConfigurationMssPackageTypeDef,
):
    """
    Type definition for `ClientCreatePackagingConfiguration` `MssPackage`

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
    """


_ClientCreatePackagingConfigurationResponseCmafPackageEncryptionTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseCmafPackageEncryptionTypeDef",
    {"SpekeKeyProvider": Dict[str, Any]},
    total=False,
)


class ClientCreatePackagingConfigurationResponseCmafPackageEncryptionTypeDef(
    _ClientCreatePackagingConfigurationResponseCmafPackageEncryptionTypeDef
):
    """
    Type definition for `ClientCreatePackagingConfigurationResponseCmafPackage` `Encryption`

    - **SpekeKeyProvider** *(dict) --* A configuration for accessing an external Secure
    Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

      - **RoleArn** *(string) --* An Amazon Resource Name (ARN) of an IAM role that AWS
      Elemental MediaPackage will assume when accessing the key provider service.

      - **SystemIds** *(list) --* The system IDs to include in key requests.

        - *(string) --*

      - **Url** *(string) --* The URL of the external key provider service.
    """


_ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef",
    {"MaxVideoBitsPerSecond": int, "MinVideoBitsPerSecond": int, "StreamOrder": str},
    total=False,
)


class ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef(
    _ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef
):
    """
    Type definition for `ClientCreatePackagingConfigurationResponseCmafPackageHlsManifests` `StreamSelection`

    - **MaxVideoBitsPerSecond** *(integer) --* The maximum video bitrate (bps) to include
    in output.

    - **MinVideoBitsPerSecond** *(integer) --* The minimum video bitrate (bps) to include
    in output.

    - **StreamOrder** *(string) --* A directive that determines the order of streams in the
    output.
    """


_ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef",
    {
        "AdMarkers": str,
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "ProgramDateTimeIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "StreamSelection": ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef,
    },
    total=False,
)


class ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef(
    _ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef
):
    """
    Type definition for `ClientCreatePackagingConfigurationResponseCmafPackage` `HlsManifests`

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
    """


_ClientCreatePackagingConfigurationResponseCmafPackageTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseCmafPackageTypeDef",
    {
        "Encryption": ClientCreatePackagingConfigurationResponseCmafPackageEncryptionTypeDef,
        "HlsManifests": List[
            ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
    },
    total=False,
)


class ClientCreatePackagingConfigurationResponseCmafPackageTypeDef(
    _ClientCreatePackagingConfigurationResponseCmafPackageTypeDef
):
    """
    Type definition for `ClientCreatePackagingConfigurationResponse` `CmafPackage`

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
    """


_ClientCreatePackagingConfigurationResponseHlsPackageEncryptionTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseHlsPackageEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": str,
        "SpekeKeyProvider": Dict[str, Any],
    },
    total=False,
)


class ClientCreatePackagingConfigurationResponseHlsPackageEncryptionTypeDef(
    _ClientCreatePackagingConfigurationResponseHlsPackageEncryptionTypeDef
):
    """
    Type definition for `ClientCreatePackagingConfigurationResponseHlsPackage` `Encryption`

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
    """


_ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef",
    {"MaxVideoBitsPerSecond": int, "MinVideoBitsPerSecond": int, "StreamOrder": str},
    total=False,
)


class ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef(
    _ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef
):
    """
    Type definition for `ClientCreatePackagingConfigurationResponseHlsPackageHlsManifests` `StreamSelection`

    - **MaxVideoBitsPerSecond** *(integer) --* The maximum video bitrate (bps) to include
    in output.

    - **MinVideoBitsPerSecond** *(integer) --* The minimum video bitrate (bps) to include
    in output.

    - **StreamOrder** *(string) --* A directive that determines the order of streams in the
    output.
    """


_ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef",
    {
        "AdMarkers": str,
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "ProgramDateTimeIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "StreamSelection": ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef,
    },
    total=False,
)


class ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef(
    _ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef
):
    """
    Type definition for `ClientCreatePackagingConfigurationResponseHlsPackage` `HlsManifests`

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
    """


_ClientCreatePackagingConfigurationResponseHlsPackageTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseHlsPackageTypeDef",
    {
        "Encryption": ClientCreatePackagingConfigurationResponseHlsPackageEncryptionTypeDef,
        "HlsManifests": List[
            ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)


class ClientCreatePackagingConfigurationResponseHlsPackageTypeDef(
    _ClientCreatePackagingConfigurationResponseHlsPackageTypeDef
):
    """
    Type definition for `ClientCreatePackagingConfigurationResponse` `HlsPackage`

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
    """


_ClientCreatePackagingConfigurationResponseMssPackageEncryptionTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseMssPackageEncryptionTypeDef",
    {"SpekeKeyProvider": Dict[str, Any]},
    total=False,
)


class ClientCreatePackagingConfigurationResponseMssPackageEncryptionTypeDef(
    _ClientCreatePackagingConfigurationResponseMssPackageEncryptionTypeDef
):
    """
    Type definition for `ClientCreatePackagingConfigurationResponseMssPackage` `Encryption`

    - **SpekeKeyProvider** *(dict) --* A configuration for accessing an external Secure
    Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

      - **RoleArn** *(string) --* An Amazon Resource Name (ARN) of an IAM role that AWS
      Elemental MediaPackage will assume when accessing the key provider service.

      - **SystemIds** *(list) --* The system IDs to include in key requests.

        - *(string) --*

      - **Url** *(string) --* The URL of the external key provider service.
    """


_ClientCreatePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef",
    {"MaxVideoBitsPerSecond": int, "MinVideoBitsPerSecond": int, "StreamOrder": str},
    total=False,
)


class ClientCreatePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef(
    _ClientCreatePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef
):
    """
    Type definition for `ClientCreatePackagingConfigurationResponseMssPackageMssManifests` `StreamSelection`

    - **MaxVideoBitsPerSecond** *(integer) --* The maximum video bitrate (bps) to include
    in output.

    - **MinVideoBitsPerSecond** *(integer) --* The minimum video bitrate (bps) to include
    in output.

    - **StreamOrder** *(string) --* A directive that determines the order of streams in the
    output.
    """


_ClientCreatePackagingConfigurationResponseMssPackageMssManifestsTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseMssPackageMssManifestsTypeDef",
    {
        "ManifestName": str,
        "StreamSelection": ClientCreatePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef,
    },
    total=False,
)


class ClientCreatePackagingConfigurationResponseMssPackageMssManifestsTypeDef(
    _ClientCreatePackagingConfigurationResponseMssPackageMssManifestsTypeDef
):
    """
    Type definition for `ClientCreatePackagingConfigurationResponseMssPackage` `MssManifests`

    - **ManifestName** *(string) --* An optional string to include in the name of the
    manifest.

    - **StreamSelection** *(dict) --* A StreamSelection configuration.

      - **MaxVideoBitsPerSecond** *(integer) --* The maximum video bitrate (bps) to include
      in output.

      - **MinVideoBitsPerSecond** *(integer) --* The minimum video bitrate (bps) to include
      in output.

      - **StreamOrder** *(string) --* A directive that determines the order of streams in the
      output.
    """


_ClientCreatePackagingConfigurationResponseMssPackageTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseMssPackageTypeDef",
    {
        "Encryption": ClientCreatePackagingConfigurationResponseMssPackageEncryptionTypeDef,
        "MssManifests": List[
            ClientCreatePackagingConfigurationResponseMssPackageMssManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
    },
    total=False,
)


class ClientCreatePackagingConfigurationResponseMssPackageTypeDef(
    _ClientCreatePackagingConfigurationResponseMssPackageTypeDef
):
    """
    Type definition for `ClientCreatePackagingConfigurationResponse` `MssPackage`

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
    """


_ClientCreatePackagingConfigurationResponseTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseTypeDef",
    {
        "Arn": str,
        "CmafPackage": ClientCreatePackagingConfigurationResponseCmafPackageTypeDef,
        "DashPackage": Dict[str, Any],
        "HlsPackage": ClientCreatePackagingConfigurationResponseHlsPackageTypeDef,
        "Id": str,
        "MssPackage": ClientCreatePackagingConfigurationResponseMssPackageTypeDef,
        "PackagingGroupId": str,
    },
    total=False,
)


class ClientCreatePackagingConfigurationResponseTypeDef(
    _ClientCreatePackagingConfigurationResponseTypeDef
):
    """
    Type definition for `ClientCreatePackagingConfiguration` `Response`

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


_ClientCreatePackagingGroupResponseTypeDef = TypedDict(
    "_ClientCreatePackagingGroupResponseTypeDef", {"Arn": str, "Id": str}, total=False
)


class ClientCreatePackagingGroupResponseTypeDef(
    _ClientCreatePackagingGroupResponseTypeDef
):
    """
    Type definition for `ClientCreatePackagingGroup` `Response`

    - **Arn** *(string) --* The ARN of the PackagingGroup.

    - **Id** *(string) --* The ID of the PackagingGroup.
    """


_ClientDescribeAssetResponseEgressEndpointsTypeDef = TypedDict(
    "_ClientDescribeAssetResponseEgressEndpointsTypeDef",
    {"PackagingConfigurationId": str, "Url": str},
    total=False,
)


class ClientDescribeAssetResponseEgressEndpointsTypeDef(
    _ClientDescribeAssetResponseEgressEndpointsTypeDef
):
    """
    Type definition for `ClientDescribeAssetResponse` `EgressEndpoints`

    - **PackagingConfigurationId** *(string) --* The ID of the PackagingConfiguration being
    applied to the Asset.

    - **Url** *(string) --* The URL of the parent manifest for the repackaged Asset.
    """


_ClientDescribeAssetResponseTypeDef = TypedDict(
    "_ClientDescribeAssetResponseTypeDef",
    {
        "Arn": str,
        "EgressEndpoints": List[ClientDescribeAssetResponseEgressEndpointsTypeDef],
        "Id": str,
        "PackagingGroupId": str,
        "ResourceId": str,
        "SourceArn": str,
        "SourceRoleArn": str,
    },
    total=False,
)


class ClientDescribeAssetResponseTypeDef(_ClientDescribeAssetResponseTypeDef):
    """
    Type definition for `ClientDescribeAsset` `Response`

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


_ClientDescribePackagingConfigurationResponseCmafPackageEncryptionTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseCmafPackageEncryptionTypeDef",
    {"SpekeKeyProvider": Dict[str, Any]},
    total=False,
)


class ClientDescribePackagingConfigurationResponseCmafPackageEncryptionTypeDef(
    _ClientDescribePackagingConfigurationResponseCmafPackageEncryptionTypeDef
):
    """
    Type definition for `ClientDescribePackagingConfigurationResponseCmafPackage` `Encryption`

    - **SpekeKeyProvider** *(dict) --* A configuration for accessing an external Secure
    Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

      - **RoleArn** *(string) --* An Amazon Resource Name (ARN) of an IAM role that AWS
      Elemental MediaPackage will assume when accessing the key provider service.

      - **SystemIds** *(list) --* The system IDs to include in key requests.

        - *(string) --*

      - **Url** *(string) --* The URL of the external key provider service.
    """


_ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef",
    {"MaxVideoBitsPerSecond": int, "MinVideoBitsPerSecond": int, "StreamOrder": str},
    total=False,
)


class ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef(
    _ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef
):
    """
    Type definition for `ClientDescribePackagingConfigurationResponseCmafPackageHlsManifests` `StreamSelection`

    - **MaxVideoBitsPerSecond** *(integer) --* The maximum video bitrate (bps) to include
    in output.

    - **MinVideoBitsPerSecond** *(integer) --* The minimum video bitrate (bps) to include
    in output.

    - **StreamOrder** *(string) --* A directive that determines the order of streams in the
    output.
    """


_ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef",
    {
        "AdMarkers": str,
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "ProgramDateTimeIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "StreamSelection": ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef,
    },
    total=False,
)


class ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef(
    _ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef
):
    """
    Type definition for `ClientDescribePackagingConfigurationResponseCmafPackage` `HlsManifests`

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
    """


_ClientDescribePackagingConfigurationResponseCmafPackageTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseCmafPackageTypeDef",
    {
        "Encryption": ClientDescribePackagingConfigurationResponseCmafPackageEncryptionTypeDef,
        "HlsManifests": List[
            ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
    },
    total=False,
)


class ClientDescribePackagingConfigurationResponseCmafPackageTypeDef(
    _ClientDescribePackagingConfigurationResponseCmafPackageTypeDef
):
    """
    Type definition for `ClientDescribePackagingConfigurationResponse` `CmafPackage`

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
    """


_ClientDescribePackagingConfigurationResponseHlsPackageEncryptionTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseHlsPackageEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": str,
        "SpekeKeyProvider": Dict[str, Any],
    },
    total=False,
)


class ClientDescribePackagingConfigurationResponseHlsPackageEncryptionTypeDef(
    _ClientDescribePackagingConfigurationResponseHlsPackageEncryptionTypeDef
):
    """
    Type definition for `ClientDescribePackagingConfigurationResponseHlsPackage` `Encryption`

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
    """


_ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef",
    {"MaxVideoBitsPerSecond": int, "MinVideoBitsPerSecond": int, "StreamOrder": str},
    total=False,
)


class ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef(
    _ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef
):
    """
    Type definition for `ClientDescribePackagingConfigurationResponseHlsPackageHlsManifests` `StreamSelection`

    - **MaxVideoBitsPerSecond** *(integer) --* The maximum video bitrate (bps) to include
    in output.

    - **MinVideoBitsPerSecond** *(integer) --* The minimum video bitrate (bps) to include
    in output.

    - **StreamOrder** *(string) --* A directive that determines the order of streams in the
    output.
    """


_ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef",
    {
        "AdMarkers": str,
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "ProgramDateTimeIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "StreamSelection": ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef,
    },
    total=False,
)


class ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef(
    _ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef
):
    """
    Type definition for `ClientDescribePackagingConfigurationResponseHlsPackage` `HlsManifests`

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
    """


_ClientDescribePackagingConfigurationResponseHlsPackageTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseHlsPackageTypeDef",
    {
        "Encryption": ClientDescribePackagingConfigurationResponseHlsPackageEncryptionTypeDef,
        "HlsManifests": List[
            ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)


class ClientDescribePackagingConfigurationResponseHlsPackageTypeDef(
    _ClientDescribePackagingConfigurationResponseHlsPackageTypeDef
):
    """
    Type definition for `ClientDescribePackagingConfigurationResponse` `HlsPackage`

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
    """


_ClientDescribePackagingConfigurationResponseMssPackageEncryptionTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseMssPackageEncryptionTypeDef",
    {"SpekeKeyProvider": Dict[str, Any]},
    total=False,
)


class ClientDescribePackagingConfigurationResponseMssPackageEncryptionTypeDef(
    _ClientDescribePackagingConfigurationResponseMssPackageEncryptionTypeDef
):
    """
    Type definition for `ClientDescribePackagingConfigurationResponseMssPackage` `Encryption`

    - **SpekeKeyProvider** *(dict) --* A configuration for accessing an external Secure
    Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

      - **RoleArn** *(string) --* An Amazon Resource Name (ARN) of an IAM role that AWS
      Elemental MediaPackage will assume when accessing the key provider service.

      - **SystemIds** *(list) --* The system IDs to include in key requests.

        - *(string) --*

      - **Url** *(string) --* The URL of the external key provider service.
    """


_ClientDescribePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef",
    {"MaxVideoBitsPerSecond": int, "MinVideoBitsPerSecond": int, "StreamOrder": str},
    total=False,
)


class ClientDescribePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef(
    _ClientDescribePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef
):
    """
    Type definition for `ClientDescribePackagingConfigurationResponseMssPackageMssManifests` `StreamSelection`

    - **MaxVideoBitsPerSecond** *(integer) --* The maximum video bitrate (bps) to include
    in output.

    - **MinVideoBitsPerSecond** *(integer) --* The minimum video bitrate (bps) to include
    in output.

    - **StreamOrder** *(string) --* A directive that determines the order of streams in the
    output.
    """


_ClientDescribePackagingConfigurationResponseMssPackageMssManifestsTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseMssPackageMssManifestsTypeDef",
    {
        "ManifestName": str,
        "StreamSelection": ClientDescribePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef,
    },
    total=False,
)


class ClientDescribePackagingConfigurationResponseMssPackageMssManifestsTypeDef(
    _ClientDescribePackagingConfigurationResponseMssPackageMssManifestsTypeDef
):
    """
    Type definition for `ClientDescribePackagingConfigurationResponseMssPackage` `MssManifests`

    - **ManifestName** *(string) --* An optional string to include in the name of the
    manifest.

    - **StreamSelection** *(dict) --* A StreamSelection configuration.

      - **MaxVideoBitsPerSecond** *(integer) --* The maximum video bitrate (bps) to include
      in output.

      - **MinVideoBitsPerSecond** *(integer) --* The minimum video bitrate (bps) to include
      in output.

      - **StreamOrder** *(string) --* A directive that determines the order of streams in the
      output.
    """


_ClientDescribePackagingConfigurationResponseMssPackageTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseMssPackageTypeDef",
    {
        "Encryption": ClientDescribePackagingConfigurationResponseMssPackageEncryptionTypeDef,
        "MssManifests": List[
            ClientDescribePackagingConfigurationResponseMssPackageMssManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
    },
    total=False,
)


class ClientDescribePackagingConfigurationResponseMssPackageTypeDef(
    _ClientDescribePackagingConfigurationResponseMssPackageTypeDef
):
    """
    Type definition for `ClientDescribePackagingConfigurationResponse` `MssPackage`

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
    """


_ClientDescribePackagingConfigurationResponseTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseTypeDef",
    {
        "Arn": str,
        "CmafPackage": ClientDescribePackagingConfigurationResponseCmafPackageTypeDef,
        "DashPackage": Dict[str, Any],
        "HlsPackage": ClientDescribePackagingConfigurationResponseHlsPackageTypeDef,
        "Id": str,
        "MssPackage": ClientDescribePackagingConfigurationResponseMssPackageTypeDef,
        "PackagingGroupId": str,
    },
    total=False,
)


class ClientDescribePackagingConfigurationResponseTypeDef(
    _ClientDescribePackagingConfigurationResponseTypeDef
):
    """
    Type definition for `ClientDescribePackagingConfiguration` `Response`

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


_ClientDescribePackagingGroupResponseTypeDef = TypedDict(
    "_ClientDescribePackagingGroupResponseTypeDef", {"Arn": str, "Id": str}, total=False
)


class ClientDescribePackagingGroupResponseTypeDef(
    _ClientDescribePackagingGroupResponseTypeDef
):
    """
    Type definition for `ClientDescribePackagingGroup` `Response`

    - **Arn** *(string) --* The ARN of the PackagingGroup.

    - **Id** *(string) --* The ID of the PackagingGroup.
    """


_ClientListAssetsResponseAssetsTypeDef = TypedDict(
    "_ClientListAssetsResponseAssetsTypeDef",
    {
        "Arn": str,
        "Id": str,
        "PackagingGroupId": str,
        "ResourceId": str,
        "SourceArn": str,
        "SourceRoleArn": str,
    },
    total=False,
)


class ClientListAssetsResponseAssetsTypeDef(_ClientListAssetsResponseAssetsTypeDef):
    """
    Type definition for `ClientListAssetsResponse` `Assets`

    - **Arn** *(string) --* The ARN of the Asset.

    - **Id** *(string) --* The unique identifier for the Asset.

    - **PackagingGroupId** *(string) --* The ID of the PackagingGroup for the Asset.

    - **ResourceId** *(string) --* The resource ID to include in SPEKE key requests.

    - **SourceArn** *(string) --* ARN of the source object in S3.

    - **SourceRoleArn** *(string) --* The IAM role ARN used to access the source S3 bucket.
    """


_ClientListAssetsResponseTypeDef = TypedDict(
    "_ClientListAssetsResponseTypeDef",
    {"Assets": List[ClientListAssetsResponseAssetsTypeDef], "NextToken": str},
    total=False,
)


class ClientListAssetsResponseTypeDef(_ClientListAssetsResponseTypeDef):
    """
    Type definition for `ClientListAssets` `Response`

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


_ClientListPackagingConfigurationsResponseTypeDef = TypedDict(
    "_ClientListPackagingConfigurationsResponseTypeDef",
    {"NextToken": str, "PackagingConfigurations": List[Any]},
    total=False,
)


class ClientListPackagingConfigurationsResponseTypeDef(
    _ClientListPackagingConfigurationsResponseTypeDef
):
    """
    Type definition for `ClientListPackagingConfigurations` `Response`

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


_ClientListPackagingGroupsResponsePackagingGroupsTypeDef = TypedDict(
    "_ClientListPackagingGroupsResponsePackagingGroupsTypeDef",
    {"Arn": str, "Id": str},
    total=False,
)


class ClientListPackagingGroupsResponsePackagingGroupsTypeDef(
    _ClientListPackagingGroupsResponsePackagingGroupsTypeDef
):
    """
    Type definition for `ClientListPackagingGroupsResponse` `PackagingGroups`

    - **Arn** *(string) --* The ARN of the PackagingGroup.

    - **Id** *(string) --* The ID of the PackagingGroup.
    """


_ClientListPackagingGroupsResponseTypeDef = TypedDict(
    "_ClientListPackagingGroupsResponseTypeDef",
    {
        "NextToken": str,
        "PackagingGroups": List[
            ClientListPackagingGroupsResponsePackagingGroupsTypeDef
        ],
    },
    total=False,
)


class ClientListPackagingGroupsResponseTypeDef(
    _ClientListPackagingGroupsResponseTypeDef
):
    """
    Type definition for `ClientListPackagingGroups` `Response`

    - **NextToken** *(string) --* A token that can be used to resume pagination from the end of the
    collection.

    - **PackagingGroups** *(list) --* A list of MediaPackage VOD PackagingGroup resources.

      - *(dict) --* A MediaPackage VOD PackagingGroup resource.

        - **Arn** *(string) --* The ARN of the PackagingGroup.

        - **Id** *(string) --* The ID of the PackagingGroup.
    """


_ListAssetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAssetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAssetsPaginatePaginationConfigTypeDef(
    _ListAssetsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAssetsPaginate` `PaginationConfig`

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


_ListAssetsPaginateResponseAssetsTypeDef = TypedDict(
    "_ListAssetsPaginateResponseAssetsTypeDef",
    {
        "Arn": str,
        "Id": str,
        "PackagingGroupId": str,
        "ResourceId": str,
        "SourceArn": str,
        "SourceRoleArn": str,
    },
    total=False,
)


class ListAssetsPaginateResponseAssetsTypeDef(_ListAssetsPaginateResponseAssetsTypeDef):
    """
    Type definition for `ListAssetsPaginateResponse` `Assets`

    - **Arn** *(string) --* The ARN of the Asset.

    - **Id** *(string) --* The unique identifier for the Asset.

    - **PackagingGroupId** *(string) --* The ID of the PackagingGroup for the Asset.

    - **ResourceId** *(string) --* The resource ID to include in SPEKE key requests.

    - **SourceArn** *(string) --* ARN of the source object in S3.

    - **SourceRoleArn** *(string) --* The IAM role ARN used to access the source S3 bucket.
    """


_ListAssetsPaginateResponseTypeDef = TypedDict(
    "_ListAssetsPaginateResponseTypeDef",
    {"Assets": List[ListAssetsPaginateResponseAssetsTypeDef]},
    total=False,
)


class ListAssetsPaginateResponseTypeDef(_ListAssetsPaginateResponseTypeDef):
    """
    Type definition for `ListAssetsPaginate` `Response`

    - **Assets** *(list) --* A list of MediaPackage VOD Asset resources.

      - *(dict) --* A MediaPackage VOD Asset resource.

        - **Arn** *(string) --* The ARN of the Asset.

        - **Id** *(string) --* The unique identifier for the Asset.

        - **PackagingGroupId** *(string) --* The ID of the PackagingGroup for the Asset.

        - **ResourceId** *(string) --* The resource ID to include in SPEKE key requests.

        - **SourceArn** *(string) --* ARN of the source object in S3.

        - **SourceRoleArn** *(string) --* The IAM role ARN used to access the source S3 bucket.
    """


_ListPackagingConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPackagingConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPackagingConfigurationsPaginatePaginationConfigTypeDef(
    _ListPackagingConfigurationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListPackagingConfigurationsPaginate` `PaginationConfig`

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


_ListPackagingConfigurationsPaginateResponseTypeDef = TypedDict(
    "_ListPackagingConfigurationsPaginateResponseTypeDef",
    {"PackagingConfigurations": List[Any]},
    total=False,
)


class ListPackagingConfigurationsPaginateResponseTypeDef(
    _ListPackagingConfigurationsPaginateResponseTypeDef
):
    """
    Type definition for `ListPackagingConfigurationsPaginate` `Response`

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


_ListPackagingGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPackagingGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPackagingGroupsPaginatePaginationConfigTypeDef(
    _ListPackagingGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListPackagingGroupsPaginate` `PaginationConfig`

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


_ListPackagingGroupsPaginateResponsePackagingGroupsTypeDef = TypedDict(
    "_ListPackagingGroupsPaginateResponsePackagingGroupsTypeDef",
    {"Arn": str, "Id": str},
    total=False,
)


class ListPackagingGroupsPaginateResponsePackagingGroupsTypeDef(
    _ListPackagingGroupsPaginateResponsePackagingGroupsTypeDef
):
    """
    Type definition for `ListPackagingGroupsPaginateResponse` `PackagingGroups`

    - **Arn** *(string) --* The ARN of the PackagingGroup.

    - **Id** *(string) --* The ID of the PackagingGroup.
    """


_ListPackagingGroupsPaginateResponseTypeDef = TypedDict(
    "_ListPackagingGroupsPaginateResponseTypeDef",
    {
        "PackagingGroups": List[
            ListPackagingGroupsPaginateResponsePackagingGroupsTypeDef
        ]
    },
    total=False,
)


class ListPackagingGroupsPaginateResponseTypeDef(
    _ListPackagingGroupsPaginateResponseTypeDef
):
    """
    Type definition for `ListPackagingGroupsPaginate` `Response`

    - **PackagingGroups** *(list) --* A list of MediaPackage VOD PackagingGroup resources.

      - *(dict) --* A MediaPackage VOD PackagingGroup resource.

        - **Arn** *(string) --* The ARN of the PackagingGroup.

        - **Id** *(string) --* The ID of the PackagingGroup.
    """
