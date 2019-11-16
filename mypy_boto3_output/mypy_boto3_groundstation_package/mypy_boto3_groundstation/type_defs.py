"Main interface for groundstation type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCancelContactResponseTypeDef",
    "ClientCreateConfigResponseTypeDef",
    "ClientCreateConfigconfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef",
    "ClientCreateConfigconfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef",
    "ClientCreateConfigconfigDataantennaDownlinkConfigspectrumConfigTypeDef",
    "ClientCreateConfigconfigDataantennaDownlinkConfigTypeDef",
    "ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef",
    "ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef",
    "ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef",
    "ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef",
    "ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef",
    "ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigTypeDef",
    "ClientCreateConfigconfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef",
    "ClientCreateConfigconfigDataantennaUplinkConfigspectrumConfigTypeDef",
    "ClientCreateConfigconfigDataantennaUplinkConfigtargetEirpTypeDef",
    "ClientCreateConfigconfigDataantennaUplinkConfigTypeDef",
    "ClientCreateConfigconfigDatadataflowEndpointConfigTypeDef",
    "ClientCreateConfigconfigDatatrackingConfigTypeDef",
    "ClientCreateConfigconfigDatauplinkEchoConfigTypeDef",
    "ClientCreateConfigconfigDataTypeDef",
    "ClientCreateDataflowEndpointGroupResponseTypeDef",
    "ClientCreateDataflowEndpointGroupendpointDetailsendpointaddressTypeDef",
    "ClientCreateDataflowEndpointGroupendpointDetailsendpointTypeDef",
    "ClientCreateDataflowEndpointGroupendpointDetailssecurityDetailsTypeDef",
    "ClientCreateDataflowEndpointGroupendpointDetailsTypeDef",
    "ClientCreateMissionProfileResponseTypeDef",
    "ClientDeleteConfigResponseTypeDef",
    "ClientDeleteDataflowEndpointGroupResponseTypeDef",
    "ClientDeleteMissionProfileResponseTypeDef",
    "ClientDescribeContactResponsemaximumElevationTypeDef",
    "ClientDescribeContactResponseTypeDef",
    "ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef",
    "ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef",
    "ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigTypeDef",
    "ClientGetConfigResponseconfigDataantennaDownlinkConfigTypeDef",
    "ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef",
    "ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef",
    "ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef",
    "ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef",
    "ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef",
    "ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigTypeDef",
    "ClientGetConfigResponseconfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef",
    "ClientGetConfigResponseconfigDataantennaUplinkConfigspectrumConfigTypeDef",
    "ClientGetConfigResponseconfigDataantennaUplinkConfigtargetEirpTypeDef",
    "ClientGetConfigResponseconfigDataantennaUplinkConfigTypeDef",
    "ClientGetConfigResponseconfigDatadataflowEndpointConfigTypeDef",
    "ClientGetConfigResponseconfigDatatrackingConfigTypeDef",
    "ClientGetConfigResponseconfigDatauplinkEchoConfigTypeDef",
    "ClientGetConfigResponseconfigDataTypeDef",
    "ClientGetConfigResponseTypeDef",
    "ClientGetDataflowEndpointGroupResponseendpointsDetailsendpointaddressTypeDef",
    "ClientGetDataflowEndpointGroupResponseendpointsDetailsendpointTypeDef",
    "ClientGetDataflowEndpointGroupResponseendpointsDetailssecurityDetailsTypeDef",
    "ClientGetDataflowEndpointGroupResponseendpointsDetailsTypeDef",
    "ClientGetDataflowEndpointGroupResponseTypeDef",
    "ClientGetMinuteUsageResponseTypeDef",
    "ClientGetMissionProfileResponseTypeDef",
    "ClientGetSatelliteResponseTypeDef",
    "ClientListConfigsResponseconfigListTypeDef",
    "ClientListConfigsResponseTypeDef",
    "ClientListContactsResponsecontactListmaximumElevationTypeDef",
    "ClientListContactsResponsecontactListTypeDef",
    "ClientListContactsResponseTypeDef",
    "ClientListDataflowEndpointGroupsResponsedataflowEndpointGroupListTypeDef",
    "ClientListDataflowEndpointGroupsResponseTypeDef",
    "ClientListGroundStationsResponsegroundStationListTypeDef",
    "ClientListGroundStationsResponseTypeDef",
    "ClientListMissionProfilesResponsemissionProfileListTypeDef",
    "ClientListMissionProfilesResponseTypeDef",
    "ClientListSatellitesResponsesatellitesTypeDef",
    "ClientListSatellitesResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientReserveContactResponseTypeDef",
    "ClientUpdateConfigResponseTypeDef",
    "ClientUpdateConfigconfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef",
    "ClientUpdateConfigconfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef",
    "ClientUpdateConfigconfigDataantennaDownlinkConfigspectrumConfigTypeDef",
    "ClientUpdateConfigconfigDataantennaDownlinkConfigTypeDef",
    "ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef",
    "ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef",
    "ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef",
    "ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef",
    "ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef",
    "ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigTypeDef",
    "ClientUpdateConfigconfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef",
    "ClientUpdateConfigconfigDataantennaUplinkConfigspectrumConfigTypeDef",
    "ClientUpdateConfigconfigDataantennaUplinkConfigtargetEirpTypeDef",
    "ClientUpdateConfigconfigDataantennaUplinkConfigTypeDef",
    "ClientUpdateConfigconfigDatadataflowEndpointConfigTypeDef",
    "ClientUpdateConfigconfigDatatrackingConfigTypeDef",
    "ClientUpdateConfigconfigDatauplinkEchoConfigTypeDef",
    "ClientUpdateConfigconfigDataTypeDef",
    "ClientUpdateMissionProfileResponseTypeDef",
    "ListConfigsPaginatePaginationConfigTypeDef",
    "ListConfigsPaginateResponseconfigListTypeDef",
    "ListConfigsPaginateResponseTypeDef",
    "ListContactsPaginatePaginationConfigTypeDef",
    "ListContactsPaginateResponsecontactListmaximumElevationTypeDef",
    "ListContactsPaginateResponsecontactListTypeDef",
    "ListContactsPaginateResponseTypeDef",
    "ListDataflowEndpointGroupsPaginatePaginationConfigTypeDef",
    "ListDataflowEndpointGroupsPaginateResponsedataflowEndpointGroupListTypeDef",
    "ListDataflowEndpointGroupsPaginateResponseTypeDef",
    "ListGroundStationsPaginatePaginationConfigTypeDef",
    "ListGroundStationsPaginateResponsegroundStationListTypeDef",
    "ListGroundStationsPaginateResponseTypeDef",
    "ListMissionProfilesPaginatePaginationConfigTypeDef",
    "ListMissionProfilesPaginateResponsemissionProfileListTypeDef",
    "ListMissionProfilesPaginateResponseTypeDef",
    "ListSatellitesPaginatePaginationConfigTypeDef",
    "ListSatellitesPaginateResponsesatellitesTypeDef",
    "ListSatellitesPaginateResponseTypeDef",
)


_ClientCancelContactResponseTypeDef = TypedDict(
    "_ClientCancelContactResponseTypeDef", {"contactId": str}, total=False
)


class ClientCancelContactResponseTypeDef(_ClientCancelContactResponseTypeDef):
    """
    Type definition for `ClientCancelContact` `Response`

    - **contactId** *(string) --*

      UUID of a contact.
    """


_ClientCreateConfigResponseTypeDef = TypedDict(
    "_ClientCreateConfigResponseTypeDef",
    {"configArn": str, "configId": str, "configType": str},
    total=False,
)


class ClientCreateConfigResponseTypeDef(_ClientCreateConfigResponseTypeDef):
    """
    Type definition for `ClientCreateConfig` `Response`

    - **configArn** *(string) --*

      ARN of a ``Config`` .

    - **configId** *(string) --*

      UUID of a ``Config`` .

    - **configType** *(string) --*

      Type of a ``Config`` .
    """


_ClientCreateConfigconfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef = TypedDict(
    "_ClientCreateConfigconfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef",
    {"units": str, "value": float},
)


class ClientCreateConfigconfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef(
    _ClientCreateConfigconfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef
):
    """
    Type definition for `ClientCreateConfigconfigDataantennaDownlinkConfigspectrumConfig` `bandwidth`

    Bandwidth of a spectral ``Config`` .

    - **units** *(string) --* **[REQUIRED]**

      Frequency bandwidth units.

    - **value** *(float) --* **[REQUIRED]**

      Frequency bandwidth value.
    """


_ClientCreateConfigconfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef = TypedDict(
    "_ClientCreateConfigconfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef",
    {"units": str, "value": float},
)


class ClientCreateConfigconfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef(
    _ClientCreateConfigconfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef
):
    """
    Type definition for `ClientCreateConfigconfigDataantennaDownlinkConfigspectrumConfig` `centerFrequency`

    Center frequency of a spectral ``Config`` .

    - **units** *(string) --* **[REQUIRED]**

      Frequency units.

    - **value** *(float) --* **[REQUIRED]**

      Frequency value.
    """


_RequiredClientCreateConfigconfigDataantennaDownlinkConfigspectrumConfigTypeDef = TypedDict(
    "_RequiredClientCreateConfigconfigDataantennaDownlinkConfigspectrumConfigTypeDef",
    {
        "bandwidth": ClientCreateConfigconfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef,
        "centerFrequency": ClientCreateConfigconfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef,
    },
)
_OptionalClientCreateConfigconfigDataantennaDownlinkConfigspectrumConfigTypeDef = TypedDict(
    "_OptionalClientCreateConfigconfigDataantennaDownlinkConfigspectrumConfigTypeDef",
    {"polarization": str},
    total=False,
)


class ClientCreateConfigconfigDataantennaDownlinkConfigspectrumConfigTypeDef(
    _RequiredClientCreateConfigconfigDataantennaDownlinkConfigspectrumConfigTypeDef,
    _OptionalClientCreateConfigconfigDataantennaDownlinkConfigspectrumConfigTypeDef,
):
    """
    Type definition for `ClientCreateConfigconfigDataantennaDownlinkConfig` `spectrumConfig`

    Object that describes a spectral ``Config`` .

    - **bandwidth** *(dict) --* **[REQUIRED]**

      Bandwidth of a spectral ``Config`` .

      - **units** *(string) --* **[REQUIRED]**

        Frequency bandwidth units.

      - **value** *(float) --* **[REQUIRED]**

        Frequency bandwidth value.

    - **centerFrequency** *(dict) --* **[REQUIRED]**

      Center frequency of a spectral ``Config`` .

      - **units** *(string) --* **[REQUIRED]**

        Frequency units.

      - **value** *(float) --* **[REQUIRED]**

        Frequency value.

    - **polarization** *(string) --*

      Polarization of a spectral ``Config`` .
    """


_ClientCreateConfigconfigDataantennaDownlinkConfigTypeDef = TypedDict(
    "_ClientCreateConfigconfigDataantennaDownlinkConfigTypeDef",
    {
        "spectrumConfig": ClientCreateConfigconfigDataantennaDownlinkConfigspectrumConfigTypeDef
    },
)


class ClientCreateConfigconfigDataantennaDownlinkConfigTypeDef(
    _ClientCreateConfigconfigDataantennaDownlinkConfigTypeDef
):
    """
    Type definition for `ClientCreateConfigconfigData` `antennaDownlinkConfig`

    Information about how AWS Ground Station should configure an antenna for downlink during a
    contact.

    - **spectrumConfig** *(dict) --* **[REQUIRED]**

      Object that describes a spectral ``Config`` .

      - **bandwidth** *(dict) --* **[REQUIRED]**

        Bandwidth of a spectral ``Config`` .

        - **units** *(string) --* **[REQUIRED]**

          Frequency bandwidth units.

        - **value** *(float) --* **[REQUIRED]**

          Frequency bandwidth value.

      - **centerFrequency** *(dict) --* **[REQUIRED]**

        Center frequency of a spectral ``Config`` .

        - **units** *(string) --* **[REQUIRED]**

          Frequency units.

        - **value** *(float) --* **[REQUIRED]**

          Frequency value.

      - **polarization** *(string) --*

        Polarization of a spectral ``Config`` .
    """


_ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef = TypedDict(
    "_ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef",
    {"unvalidatedJSON": str},
)


class ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef(
    _ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef
):
    """
    Type definition for `ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfig` `decodeConfig`

    Information about the decode ``Config`` .

    - **unvalidatedJSON** *(string) --* **[REQUIRED]**

      Unvalidated JSON of a decode ``Config`` .
    """


_ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef = TypedDict(
    "_ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef",
    {"unvalidatedJSON": str},
)


class ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef(
    _ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef
):
    """
    Type definition for `ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfig` `demodulationConfig`

    Information about the demodulation ``Config`` .

    - **unvalidatedJSON** *(string) --* **[REQUIRED]**

      Unvalidated JSON of a demodulation ``Config`` .
    """


_ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef = TypedDict(
    "_ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef",
    {"units": str, "value": float},
)


class ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef(
    _ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef
):
    """
    Type definition for `ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfig` `bandwidth`

    Bandwidth of a spectral ``Config`` .

    - **units** *(string) --* **[REQUIRED]**

      Frequency bandwidth units.

    - **value** *(float) --* **[REQUIRED]**

      Frequency bandwidth value.
    """


_ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef = TypedDict(
    "_ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef",
    {"units": str, "value": float},
)


class ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef(
    _ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef
):
    """
    Type definition for `ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfig` `centerFrequency`

    Center frequency of a spectral ``Config`` .

    - **units** *(string) --* **[REQUIRED]**

      Frequency units.

    - **value** *(float) --* **[REQUIRED]**

      Frequency value.
    """


_RequiredClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef = TypedDict(
    "_RequiredClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef",
    {
        "bandwidth": ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef,
        "centerFrequency": ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef,
    },
)
_OptionalClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef = TypedDict(
    "_OptionalClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef",
    {"polarization": str},
    total=False,
)


class ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef(
    _RequiredClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef,
    _OptionalClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef,
):
    """
    Type definition for `ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfig` `spectrumConfig`

    Information about the spectral ``Config`` .

    - **bandwidth** *(dict) --* **[REQUIRED]**

      Bandwidth of a spectral ``Config`` .

      - **units** *(string) --* **[REQUIRED]**

        Frequency bandwidth units.

      - **value** *(float) --* **[REQUIRED]**

        Frequency bandwidth value.

    - **centerFrequency** *(dict) --* **[REQUIRED]**

      Center frequency of a spectral ``Config`` .

      - **units** *(string) --* **[REQUIRED]**

        Frequency units.

      - **value** *(float) --* **[REQUIRED]**

        Frequency value.

    - **polarization** *(string) --*

      Polarization of a spectral ``Config`` .
    """


_ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigTypeDef = TypedDict(
    "_ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigTypeDef",
    {
        "decodeConfig": ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef,
        "demodulationConfig": ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef,
        "spectrumConfig": ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef,
    },
)


class ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigTypeDef(
    _ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigTypeDef
):
    """
    Type definition for `ClientCreateConfigconfigData` `antennaDownlinkDemodDecodeConfig`

    Information about how AWS Ground Station should conﬁgure an antenna for downlink demod decode
    during a contact.

    - **decodeConfig** *(dict) --* **[REQUIRED]**

      Information about the decode ``Config`` .

      - **unvalidatedJSON** *(string) --* **[REQUIRED]**

        Unvalidated JSON of a decode ``Config`` .

    - **demodulationConfig** *(dict) --* **[REQUIRED]**

      Information about the demodulation ``Config`` .

      - **unvalidatedJSON** *(string) --* **[REQUIRED]**

        Unvalidated JSON of a demodulation ``Config`` .

    - **spectrumConfig** *(dict) --* **[REQUIRED]**

      Information about the spectral ``Config`` .

      - **bandwidth** *(dict) --* **[REQUIRED]**

        Bandwidth of a spectral ``Config`` .

        - **units** *(string) --* **[REQUIRED]**

          Frequency bandwidth units.

        - **value** *(float) --* **[REQUIRED]**

          Frequency bandwidth value.

      - **centerFrequency** *(dict) --* **[REQUIRED]**

        Center frequency of a spectral ``Config`` .

        - **units** *(string) --* **[REQUIRED]**

          Frequency units.

        - **value** *(float) --* **[REQUIRED]**

          Frequency value.

      - **polarization** *(string) --*

        Polarization of a spectral ``Config`` .
    """


_ClientCreateConfigconfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef = TypedDict(
    "_ClientCreateConfigconfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef",
    {"units": str, "value": float},
)


class ClientCreateConfigconfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef(
    _ClientCreateConfigconfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef
):
    """
    Type definition for `ClientCreateConfigconfigDataantennaUplinkConfigspectrumConfig` `centerFrequency`

    Center frequency of an uplink spectral ``Config`` .

    - **units** *(string) --* **[REQUIRED]**

      Frequency units.

    - **value** *(float) --* **[REQUIRED]**

      Frequency value.
    """


_RequiredClientCreateConfigconfigDataantennaUplinkConfigspectrumConfigTypeDef = TypedDict(
    "_RequiredClientCreateConfigconfigDataantennaUplinkConfigspectrumConfigTypeDef",
    {
        "centerFrequency": ClientCreateConfigconfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef
    },
)
_OptionalClientCreateConfigconfigDataantennaUplinkConfigspectrumConfigTypeDef = TypedDict(
    "_OptionalClientCreateConfigconfigDataantennaUplinkConfigspectrumConfigTypeDef",
    {"polarization": str},
    total=False,
)


class ClientCreateConfigconfigDataantennaUplinkConfigspectrumConfigTypeDef(
    _RequiredClientCreateConfigconfigDataantennaUplinkConfigspectrumConfigTypeDef,
    _OptionalClientCreateConfigconfigDataantennaUplinkConfigspectrumConfigTypeDef,
):
    """
    Type definition for `ClientCreateConfigconfigDataantennaUplinkConfig` `spectrumConfig`

    Information about the uplink spectral ``Config`` .

    - **centerFrequency** *(dict) --* **[REQUIRED]**

      Center frequency of an uplink spectral ``Config`` .

      - **units** *(string) --* **[REQUIRED]**

        Frequency units.

      - **value** *(float) --* **[REQUIRED]**

        Frequency value.

    - **polarization** *(string) --*

      Polarization of an uplink spectral ``Config`` .
    """


_ClientCreateConfigconfigDataantennaUplinkConfigtargetEirpTypeDef = TypedDict(
    "_ClientCreateConfigconfigDataantennaUplinkConfigtargetEirpTypeDef",
    {"units": str, "value": float},
)


class ClientCreateConfigconfigDataantennaUplinkConfigtargetEirpTypeDef(
    _ClientCreateConfigconfigDataantennaUplinkConfigtargetEirpTypeDef
):
    """
    Type definition for `ClientCreateConfigconfigDataantennaUplinkConfig` `targetEirp`

    EIRP of the target.

    - **units** *(string) --* **[REQUIRED]**

      Units of an EIRP.

    - **value** *(float) --* **[REQUIRED]**

      Value of an EIRP.
    """


_ClientCreateConfigconfigDataantennaUplinkConfigTypeDef = TypedDict(
    "_ClientCreateConfigconfigDataantennaUplinkConfigTypeDef",
    {
        "spectrumConfig": ClientCreateConfigconfigDataantennaUplinkConfigspectrumConfigTypeDef,
        "targetEirp": ClientCreateConfigconfigDataantennaUplinkConfigtargetEirpTypeDef,
    },
)


class ClientCreateConfigconfigDataantennaUplinkConfigTypeDef(
    _ClientCreateConfigconfigDataantennaUplinkConfigTypeDef
):
    """
    Type definition for `ClientCreateConfigconfigData` `antennaUplinkConfig`

    Information about how AWS Ground Station should conﬁgure an antenna for uplink during a contact.

    - **spectrumConfig** *(dict) --* **[REQUIRED]**

      Information about the uplink spectral ``Config`` .

      - **centerFrequency** *(dict) --* **[REQUIRED]**

        Center frequency of an uplink spectral ``Config`` .

        - **units** *(string) --* **[REQUIRED]**

          Frequency units.

        - **value** *(float) --* **[REQUIRED]**

          Frequency value.

      - **polarization** *(string) --*

        Polarization of an uplink spectral ``Config`` .

    - **targetEirp** *(dict) --* **[REQUIRED]**

      EIRP of the target.

      - **units** *(string) --* **[REQUIRED]**

        Units of an EIRP.

      - **value** *(float) --* **[REQUIRED]**

        Value of an EIRP.
    """


_ClientCreateConfigconfigDatadataflowEndpointConfigTypeDef = TypedDict(
    "_ClientCreateConfigconfigDatadataflowEndpointConfigTypeDef",
    {"dataflowEndpointName": str},
)


class ClientCreateConfigconfigDatadataflowEndpointConfigTypeDef(
    _ClientCreateConfigconfigDatadataflowEndpointConfigTypeDef
):
    """
    Type definition for `ClientCreateConfigconfigData` `dataflowEndpointConfig`

    Information about the dataflow endpoint ``Config`` .

    - **dataflowEndpointName** *(string) --* **[REQUIRED]**

      Name of a dataflow endpoint.
    """


_ClientCreateConfigconfigDatatrackingConfigTypeDef = TypedDict(
    "_ClientCreateConfigconfigDatatrackingConfigTypeDef", {"autotrack": str}
)


class ClientCreateConfigconfigDatatrackingConfigTypeDef(
    _ClientCreateConfigconfigDatatrackingConfigTypeDef
):
    """
    Type definition for `ClientCreateConfigconfigData` `trackingConfig`

    Object that determines whether tracking should be used during a contact executed with this
    ``Config`` in the mission profile.

    - **autotrack** *(string) --* **[REQUIRED]**

      Current setting for autotrack.
    """


_ClientCreateConfigconfigDatauplinkEchoConfigTypeDef = TypedDict(
    "_ClientCreateConfigconfigDatauplinkEchoConfigTypeDef",
    {"antennaUplinkConfigArn": str, "enabled": bool},
)


class ClientCreateConfigconfigDatauplinkEchoConfigTypeDef(
    _ClientCreateConfigconfigDatauplinkEchoConfigTypeDef
):
    """
    Type definition for `ClientCreateConfigconfigData` `uplinkEchoConfig`

    Information about an uplink echo ``Config`` .

    Parameters from the ``AntennaUplinkConfig`` , corresponding to the specified
    ``AntennaUplinkConfigArn`` , are used when this ``UplinkEchoConfig`` is used in a contact.

    - **antennaUplinkConfigArn** *(string) --* **[REQUIRED]**

      ARN of an uplink ``Config`` .

    - **enabled** *(boolean) --* **[REQUIRED]**

      Whether or not an uplink ``Config`` is enabled.
    """


_ClientCreateConfigconfigDataTypeDef = TypedDict(
    "_ClientCreateConfigconfigDataTypeDef",
    {
        "antennaDownlinkConfig": ClientCreateConfigconfigDataantennaDownlinkConfigTypeDef,
        "antennaDownlinkDemodDecodeConfig": ClientCreateConfigconfigDataantennaDownlinkDemodDecodeConfigTypeDef,
        "antennaUplinkConfig": ClientCreateConfigconfigDataantennaUplinkConfigTypeDef,
        "dataflowEndpointConfig": ClientCreateConfigconfigDatadataflowEndpointConfigTypeDef,
        "trackingConfig": ClientCreateConfigconfigDatatrackingConfigTypeDef,
        "uplinkEchoConfig": ClientCreateConfigconfigDatauplinkEchoConfigTypeDef,
    },
    total=False,
)


class ClientCreateConfigconfigDataTypeDef(_ClientCreateConfigconfigDataTypeDef):
    """
    Type definition for `ClientCreateConfig` `configData`

    Parameters of a ``Config`` .

    - **antennaDownlinkConfig** *(dict) --*

      Information about how AWS Ground Station should configure an antenna for downlink during a
      contact.

      - **spectrumConfig** *(dict) --* **[REQUIRED]**

        Object that describes a spectral ``Config`` .

        - **bandwidth** *(dict) --* **[REQUIRED]**

          Bandwidth of a spectral ``Config`` .

          - **units** *(string) --* **[REQUIRED]**

            Frequency bandwidth units.

          - **value** *(float) --* **[REQUIRED]**

            Frequency bandwidth value.

        - **centerFrequency** *(dict) --* **[REQUIRED]**

          Center frequency of a spectral ``Config`` .

          - **units** *(string) --* **[REQUIRED]**

            Frequency units.

          - **value** *(float) --* **[REQUIRED]**

            Frequency value.

        - **polarization** *(string) --*

          Polarization of a spectral ``Config`` .

    - **antennaDownlinkDemodDecodeConfig** *(dict) --*

      Information about how AWS Ground Station should conﬁgure an antenna for downlink demod decode
      during a contact.

      - **decodeConfig** *(dict) --* **[REQUIRED]**

        Information about the decode ``Config`` .

        - **unvalidatedJSON** *(string) --* **[REQUIRED]**

          Unvalidated JSON of a decode ``Config`` .

      - **demodulationConfig** *(dict) --* **[REQUIRED]**

        Information about the demodulation ``Config`` .

        - **unvalidatedJSON** *(string) --* **[REQUIRED]**

          Unvalidated JSON of a demodulation ``Config`` .

      - **spectrumConfig** *(dict) --* **[REQUIRED]**

        Information about the spectral ``Config`` .

        - **bandwidth** *(dict) --* **[REQUIRED]**

          Bandwidth of a spectral ``Config`` .

          - **units** *(string) --* **[REQUIRED]**

            Frequency bandwidth units.

          - **value** *(float) --* **[REQUIRED]**

            Frequency bandwidth value.

        - **centerFrequency** *(dict) --* **[REQUIRED]**

          Center frequency of a spectral ``Config`` .

          - **units** *(string) --* **[REQUIRED]**

            Frequency units.

          - **value** *(float) --* **[REQUIRED]**

            Frequency value.

        - **polarization** *(string) --*

          Polarization of a spectral ``Config`` .

    - **antennaUplinkConfig** *(dict) --*

      Information about how AWS Ground Station should conﬁgure an antenna for uplink during a contact.

      - **spectrumConfig** *(dict) --* **[REQUIRED]**

        Information about the uplink spectral ``Config`` .

        - **centerFrequency** *(dict) --* **[REQUIRED]**

          Center frequency of an uplink spectral ``Config`` .

          - **units** *(string) --* **[REQUIRED]**

            Frequency units.

          - **value** *(float) --* **[REQUIRED]**

            Frequency value.

        - **polarization** *(string) --*

          Polarization of an uplink spectral ``Config`` .

      - **targetEirp** *(dict) --* **[REQUIRED]**

        EIRP of the target.

        - **units** *(string) --* **[REQUIRED]**

          Units of an EIRP.

        - **value** *(float) --* **[REQUIRED]**

          Value of an EIRP.

    - **dataflowEndpointConfig** *(dict) --*

      Information about the dataflow endpoint ``Config`` .

      - **dataflowEndpointName** *(string) --* **[REQUIRED]**

        Name of a dataflow endpoint.

    - **trackingConfig** *(dict) --*

      Object that determines whether tracking should be used during a contact executed with this
      ``Config`` in the mission profile.

      - **autotrack** *(string) --* **[REQUIRED]**

        Current setting for autotrack.

    - **uplinkEchoConfig** *(dict) --*

      Information about an uplink echo ``Config`` .

      Parameters from the ``AntennaUplinkConfig`` , corresponding to the specified
      ``AntennaUplinkConfigArn`` , are used when this ``UplinkEchoConfig`` is used in a contact.

      - **antennaUplinkConfigArn** *(string) --* **[REQUIRED]**

        ARN of an uplink ``Config`` .

      - **enabled** *(boolean) --* **[REQUIRED]**

        Whether or not an uplink ``Config`` is enabled.
    """


_ClientCreateDataflowEndpointGroupResponseTypeDef = TypedDict(
    "_ClientCreateDataflowEndpointGroupResponseTypeDef",
    {"dataflowEndpointGroupId": str},
    total=False,
)


class ClientCreateDataflowEndpointGroupResponseTypeDef(
    _ClientCreateDataflowEndpointGroupResponseTypeDef
):
    """
    Type definition for `ClientCreateDataflowEndpointGroup` `Response`

    - **dataflowEndpointGroupId** *(string) --*

      ID of a dataflow endpoint group.
    """


_ClientCreateDataflowEndpointGroupendpointDetailsendpointaddressTypeDef = TypedDict(
    "_ClientCreateDataflowEndpointGroupendpointDetailsendpointaddressTypeDef",
    {"name": str, "port": int},
)


class ClientCreateDataflowEndpointGroupendpointDetailsendpointaddressTypeDef(
    _ClientCreateDataflowEndpointGroupendpointDetailsendpointaddressTypeDef
):
    """
    Type definition for `ClientCreateDataflowEndpointGroupendpointDetailsendpoint` `address`

    Socket address of a dataflow endpoint.

    - **name** *(string) --* **[REQUIRED]**

      Name of a socket address.

    - **port** *(integer) --* **[REQUIRED]**

      Port of a socket address.
    """


_ClientCreateDataflowEndpointGroupendpointDetailsendpointTypeDef = TypedDict(
    "_ClientCreateDataflowEndpointGroupendpointDetailsendpointTypeDef",
    {
        "address": ClientCreateDataflowEndpointGroupendpointDetailsendpointaddressTypeDef,
        "name": str,
        "status": str,
    },
    total=False,
)


class ClientCreateDataflowEndpointGroupendpointDetailsendpointTypeDef(
    _ClientCreateDataflowEndpointGroupendpointDetailsendpointTypeDef
):
    """
    Type definition for `ClientCreateDataflowEndpointGroupendpointDetails` `endpoint`

    A dataflow endpoint.

    - **address** *(dict) --*

      Socket address of a dataflow endpoint.

      - **name** *(string) --* **[REQUIRED]**

        Name of a socket address.

      - **port** *(integer) --* **[REQUIRED]**

        Port of a socket address.

    - **name** *(string) --*

      Name of a dataflow endpoint.

    - **status** *(string) --*

      Status of a dataflow endpoint.
    """


_ClientCreateDataflowEndpointGroupendpointDetailssecurityDetailsTypeDef = TypedDict(
    "_ClientCreateDataflowEndpointGroupendpointDetailssecurityDetailsTypeDef",
    {"roleArn": str, "securityGroupIds": List[str], "subnetIds": List[str]},
)


class ClientCreateDataflowEndpointGroupendpointDetailssecurityDetailsTypeDef(
    _ClientCreateDataflowEndpointGroupendpointDetailssecurityDetailsTypeDef
):
    """
    Type definition for `ClientCreateDataflowEndpointGroupendpointDetails` `securityDetails`

    Endpoint security details.

    - **roleArn** *(string) --* **[REQUIRED]**

      ARN to a role needed for connecting streams to your instances.

    - **securityGroupIds** *(list) --* **[REQUIRED]**

      The security groups to attach to the elastic network interfaces.

      - *(string) --*

    - **subnetIds** *(list) --* **[REQUIRED]**

      A list of subnets where AWS Ground Station places elastic network interfaces to send
      streams to your instances.

      - *(string) --*
    """


_ClientCreateDataflowEndpointGroupendpointDetailsTypeDef = TypedDict(
    "_ClientCreateDataflowEndpointGroupendpointDetailsTypeDef",
    {
        "endpoint": ClientCreateDataflowEndpointGroupendpointDetailsendpointTypeDef,
        "securityDetails": ClientCreateDataflowEndpointGroupendpointDetailssecurityDetailsTypeDef,
    },
    total=False,
)


class ClientCreateDataflowEndpointGroupendpointDetailsTypeDef(
    _ClientCreateDataflowEndpointGroupendpointDetailsTypeDef
):
    """
    Type definition for `ClientCreateDataflowEndpointGroup` `endpointDetails`

    Information about the endpoint details.

    - **endpoint** *(dict) --*

      A dataflow endpoint.

      - **address** *(dict) --*

        Socket address of a dataflow endpoint.

        - **name** *(string) --* **[REQUIRED]**

          Name of a socket address.

        - **port** *(integer) --* **[REQUIRED]**

          Port of a socket address.

      - **name** *(string) --*

        Name of a dataflow endpoint.

      - **status** *(string) --*

        Status of a dataflow endpoint.

    - **securityDetails** *(dict) --*

      Endpoint security details.

      - **roleArn** *(string) --* **[REQUIRED]**

        ARN to a role needed for connecting streams to your instances.

      - **securityGroupIds** *(list) --* **[REQUIRED]**

        The security groups to attach to the elastic network interfaces.

        - *(string) --*

      - **subnetIds** *(list) --* **[REQUIRED]**

        A list of subnets where AWS Ground Station places elastic network interfaces to send
        streams to your instances.

        - *(string) --*
    """


_ClientCreateMissionProfileResponseTypeDef = TypedDict(
    "_ClientCreateMissionProfileResponseTypeDef", {"missionProfileId": str}, total=False
)


class ClientCreateMissionProfileResponseTypeDef(
    _ClientCreateMissionProfileResponseTypeDef
):
    """
    Type definition for `ClientCreateMissionProfile` `Response`

    - **missionProfileId** *(string) --*

      ID of a mission profile.
    """


_ClientDeleteConfigResponseTypeDef = TypedDict(
    "_ClientDeleteConfigResponseTypeDef",
    {"configArn": str, "configId": str, "configType": str},
    total=False,
)


class ClientDeleteConfigResponseTypeDef(_ClientDeleteConfigResponseTypeDef):
    """
    Type definition for `ClientDeleteConfig` `Response`

    - **configArn** *(string) --*

      ARN of a ``Config`` .

    - **configId** *(string) --*

      UUID of a ``Config`` .

    - **configType** *(string) --*

      Type of a ``Config`` .
    """


_ClientDeleteDataflowEndpointGroupResponseTypeDef = TypedDict(
    "_ClientDeleteDataflowEndpointGroupResponseTypeDef",
    {"dataflowEndpointGroupId": str},
    total=False,
)


class ClientDeleteDataflowEndpointGroupResponseTypeDef(
    _ClientDeleteDataflowEndpointGroupResponseTypeDef
):
    """
    Type definition for `ClientDeleteDataflowEndpointGroup` `Response`

    - **dataflowEndpointGroupId** *(string) --*

      ID of a dataflow endpoint group.
    """


_ClientDeleteMissionProfileResponseTypeDef = TypedDict(
    "_ClientDeleteMissionProfileResponseTypeDef", {"missionProfileId": str}, total=False
)


class ClientDeleteMissionProfileResponseTypeDef(
    _ClientDeleteMissionProfileResponseTypeDef
):
    """
    Type definition for `ClientDeleteMissionProfile` `Response`

    - **missionProfileId** *(string) --*

      ID of a mission profile.
    """


_ClientDescribeContactResponsemaximumElevationTypeDef = TypedDict(
    "_ClientDescribeContactResponsemaximumElevationTypeDef",
    {"unit": str, "value": float},
    total=False,
)


class ClientDescribeContactResponsemaximumElevationTypeDef(
    _ClientDescribeContactResponsemaximumElevationTypeDef
):
    """
    Type definition for `ClientDescribeContactResponse` `maximumElevation`

    Maximum elevation angle of a contact.

    - **unit** *(string) --*

      Elevation angle units.

    - **value** *(float) --*

      Elevation angle value.
    """


_ClientDescribeContactResponseTypeDef = TypedDict(
    "_ClientDescribeContactResponseTypeDef",
    {
        "contactId": str,
        "contactStatus": str,
        "endTime": datetime,
        "errorMessage": str,
        "groundStation": str,
        "maximumElevation": ClientDescribeContactResponsemaximumElevationTypeDef,
        "missionProfileArn": str,
        "postPassEndTime": datetime,
        "prePassStartTime": datetime,
        "satelliteArn": str,
        "startTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientDescribeContactResponseTypeDef(_ClientDescribeContactResponseTypeDef):
    """
    Type definition for `ClientDescribeContact` `Response`

    - **contactId** *(string) --*

      UUID of a contact.

    - **contactStatus** *(string) --*

      Status of a contact.

    - **endTime** *(datetime) --*

      End time of a contact.

    - **errorMessage** *(string) --*

      Error message for a contact.

    - **groundStation** *(string) --*

      Ground station for a contact.

    - **maximumElevation** *(dict) --*

      Maximum elevation angle of a contact.

      - **unit** *(string) --*

        Elevation angle units.

      - **value** *(float) --*

        Elevation angle value.

    - **missionProfileArn** *(string) --*

      ARN of a mission profile.

    - **postPassEndTime** *(datetime) --*

      Amount of time after a contact ends that you’d like to receive a CloudWatch event indicating
      the pass has finished.

    - **prePassStartTime** *(datetime) --*

      Amount of time prior to contact start you’d like to receive a CloudWatch event indicating an
      upcoming pass.

    - **satelliteArn** *(string) --*

      ARN of a satellite.

    - **startTime** *(datetime) --*

      Start time of a contact.

    - **tags** *(dict) --*

      Tags assigned to a contact.

      - *(string) --*

        - *(string) --*
    """


_ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef",
    {"units": str, "value": float},
    total=False,
)


class ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef(
    _ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef
):
    """
    Type definition for `ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfig` `bandwidth`

    Bandwidth of a spectral ``Config`` .

    - **units** *(string) --*

      Frequency bandwidth units.

    - **value** *(float) --*

      Frequency bandwidth value.
    """


_ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef",
    {"units": str, "value": float},
    total=False,
)


class ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef(
    _ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef
):
    """
    Type definition for `ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfig` `centerFrequency`

    Center frequency of a spectral ``Config`` .

    - **units** *(string) --*

      Frequency units.

    - **value** *(float) --*

      Frequency value.
    """


_ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigTypeDef",
    {
        "bandwidth": ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef,
        "centerFrequency": ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef,
        "polarization": str,
    },
    total=False,
)


class ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigTypeDef(
    _ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigTypeDef
):
    """
    Type definition for `ClientGetConfigResponseconfigDataantennaDownlinkConfig` `spectrumConfig`

    Object that describes a spectral ``Config`` .

    - **bandwidth** *(dict) --*

      Bandwidth of a spectral ``Config`` .

      - **units** *(string) --*

        Frequency bandwidth units.

      - **value** *(float) --*

        Frequency bandwidth value.

    - **centerFrequency** *(dict) --*

      Center frequency of a spectral ``Config`` .

      - **units** *(string) --*

        Frequency units.

      - **value** *(float) --*

        Frequency value.

    - **polarization** *(string) --*

      Polarization of a spectral ``Config`` .
    """


_ClientGetConfigResponseconfigDataantennaDownlinkConfigTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDataantennaDownlinkConfigTypeDef",
    {
        "spectrumConfig": ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigTypeDef
    },
    total=False,
)


class ClientGetConfigResponseconfigDataantennaDownlinkConfigTypeDef(
    _ClientGetConfigResponseconfigDataantennaDownlinkConfigTypeDef
):
    """
    Type definition for `ClientGetConfigResponseconfigData` `antennaDownlinkConfig`

    Information about how AWS Ground Station should configure an antenna for downlink during a
    contact.

    - **spectrumConfig** *(dict) --*

      Object that describes a spectral ``Config`` .

      - **bandwidth** *(dict) --*

        Bandwidth of a spectral ``Config`` .

        - **units** *(string) --*

          Frequency bandwidth units.

        - **value** *(float) --*

          Frequency bandwidth value.

      - **centerFrequency** *(dict) --*

        Center frequency of a spectral ``Config`` .

        - **units** *(string) --*

          Frequency units.

        - **value** *(float) --*

          Frequency value.

      - **polarization** *(string) --*

        Polarization of a spectral ``Config`` .
    """


_ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef",
    {"unvalidatedJSON": str},
    total=False,
)


class ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef(
    _ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef
):
    """
    Type definition for `ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfig` `decodeConfig`

    Information about the decode ``Config`` .

    - **unvalidatedJSON** *(string) --*

      Unvalidated JSON of a decode ``Config`` .
    """


_ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef",
    {"unvalidatedJSON": str},
    total=False,
)


class ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef(
    _ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef
):
    """
    Type definition for `ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfig` `demodulationConfig`

    Information about the demodulation ``Config`` .

    - **unvalidatedJSON** *(string) --*

      Unvalidated JSON of a demodulation ``Config`` .
    """


_ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef",
    {"units": str, "value": float},
    total=False,
)


class ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef(
    _ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef
):
    """
    Type definition for `ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfig` `bandwidth`

    Bandwidth of a spectral ``Config`` .

    - **units** *(string) --*

      Frequency bandwidth units.

    - **value** *(float) --*

      Frequency bandwidth value.
    """


_ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef",
    {"units": str, "value": float},
    total=False,
)


class ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef(
    _ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef
):
    """
    Type definition for `ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfig` `centerFrequency`

    Center frequency of a spectral ``Config`` .

    - **units** *(string) --*

      Frequency units.

    - **value** *(float) --*

      Frequency value.
    """


_ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef",
    {
        "bandwidth": ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef,
        "centerFrequency": ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef,
        "polarization": str,
    },
    total=False,
)


class ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef(
    _ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef
):
    """
    Type definition for `ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfig` `spectrumConfig`

    Information about the spectral ``Config`` .

    - **bandwidth** *(dict) --*

      Bandwidth of a spectral ``Config`` .

      - **units** *(string) --*

        Frequency bandwidth units.

      - **value** *(float) --*

        Frequency bandwidth value.

    - **centerFrequency** *(dict) --*

      Center frequency of a spectral ``Config`` .

      - **units** *(string) --*

        Frequency units.

      - **value** *(float) --*

        Frequency value.

    - **polarization** *(string) --*

      Polarization of a spectral ``Config`` .
    """


_ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigTypeDef",
    {
        "decodeConfig": ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef,
        "demodulationConfig": ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef,
        "spectrumConfig": ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef,
    },
    total=False,
)


class ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigTypeDef(
    _ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigTypeDef
):
    """
    Type definition for `ClientGetConfigResponseconfigData` `antennaDownlinkDemodDecodeConfig`

    Information about how AWS Ground Station should conﬁgure an antenna for downlink demod
    decode during a contact.

    - **decodeConfig** *(dict) --*

      Information about the decode ``Config`` .

      - **unvalidatedJSON** *(string) --*

        Unvalidated JSON of a decode ``Config`` .

    - **demodulationConfig** *(dict) --*

      Information about the demodulation ``Config`` .

      - **unvalidatedJSON** *(string) --*

        Unvalidated JSON of a demodulation ``Config`` .

    - **spectrumConfig** *(dict) --*

      Information about the spectral ``Config`` .

      - **bandwidth** *(dict) --*

        Bandwidth of a spectral ``Config`` .

        - **units** *(string) --*

          Frequency bandwidth units.

        - **value** *(float) --*

          Frequency bandwidth value.

      - **centerFrequency** *(dict) --*

        Center frequency of a spectral ``Config`` .

        - **units** *(string) --*

          Frequency units.

        - **value** *(float) --*

          Frequency value.

      - **polarization** *(string) --*

        Polarization of a spectral ``Config`` .
    """


_ClientGetConfigResponseconfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef",
    {"units": str, "value": float},
    total=False,
)


class ClientGetConfigResponseconfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef(
    _ClientGetConfigResponseconfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef
):
    """
    Type definition for `ClientGetConfigResponseconfigDataantennaUplinkConfigspectrumConfig` `centerFrequency`

    Center frequency of an uplink spectral ``Config`` .

    - **units** *(string) --*

      Frequency units.

    - **value** *(float) --*

      Frequency value.
    """


_ClientGetConfigResponseconfigDataantennaUplinkConfigspectrumConfigTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDataantennaUplinkConfigspectrumConfigTypeDef",
    {
        "centerFrequency": ClientGetConfigResponseconfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef,
        "polarization": str,
    },
    total=False,
)


class ClientGetConfigResponseconfigDataantennaUplinkConfigspectrumConfigTypeDef(
    _ClientGetConfigResponseconfigDataantennaUplinkConfigspectrumConfigTypeDef
):
    """
    Type definition for `ClientGetConfigResponseconfigDataantennaUplinkConfig` `spectrumConfig`

    Information about the uplink spectral ``Config`` .

    - **centerFrequency** *(dict) --*

      Center frequency of an uplink spectral ``Config`` .

      - **units** *(string) --*

        Frequency units.

      - **value** *(float) --*

        Frequency value.

    - **polarization** *(string) --*

      Polarization of an uplink spectral ``Config`` .
    """


_ClientGetConfigResponseconfigDataantennaUplinkConfigtargetEirpTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDataantennaUplinkConfigtargetEirpTypeDef",
    {"units": str, "value": float},
    total=False,
)


class ClientGetConfigResponseconfigDataantennaUplinkConfigtargetEirpTypeDef(
    _ClientGetConfigResponseconfigDataantennaUplinkConfigtargetEirpTypeDef
):
    """
    Type definition for `ClientGetConfigResponseconfigDataantennaUplinkConfig` `targetEirp`

    EIRP of the target.

    - **units** *(string) --*

      Units of an EIRP.

    - **value** *(float) --*

      Value of an EIRP.
    """


_ClientGetConfigResponseconfigDataantennaUplinkConfigTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDataantennaUplinkConfigTypeDef",
    {
        "spectrumConfig": ClientGetConfigResponseconfigDataantennaUplinkConfigspectrumConfigTypeDef,
        "targetEirp": ClientGetConfigResponseconfigDataantennaUplinkConfigtargetEirpTypeDef,
    },
    total=False,
)


class ClientGetConfigResponseconfigDataantennaUplinkConfigTypeDef(
    _ClientGetConfigResponseconfigDataantennaUplinkConfigTypeDef
):
    """
    Type definition for `ClientGetConfigResponseconfigData` `antennaUplinkConfig`

    Information about how AWS Ground Station should conﬁgure an antenna for uplink during a
    contact.

    - **spectrumConfig** *(dict) --*

      Information about the uplink spectral ``Config`` .

      - **centerFrequency** *(dict) --*

        Center frequency of an uplink spectral ``Config`` .

        - **units** *(string) --*

          Frequency units.

        - **value** *(float) --*

          Frequency value.

      - **polarization** *(string) --*

        Polarization of an uplink spectral ``Config`` .

    - **targetEirp** *(dict) --*

      EIRP of the target.

      - **units** *(string) --*

        Units of an EIRP.

      - **value** *(float) --*

        Value of an EIRP.
    """


_ClientGetConfigResponseconfigDatadataflowEndpointConfigTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDatadataflowEndpointConfigTypeDef",
    {"dataflowEndpointName": str},
    total=False,
)


class ClientGetConfigResponseconfigDatadataflowEndpointConfigTypeDef(
    _ClientGetConfigResponseconfigDatadataflowEndpointConfigTypeDef
):
    """
    Type definition for `ClientGetConfigResponseconfigData` `dataflowEndpointConfig`

    Information about the dataflow endpoint ``Config`` .

    - **dataflowEndpointName** *(string) --*

      Name of a dataflow endpoint.
    """


_ClientGetConfigResponseconfigDatatrackingConfigTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDatatrackingConfigTypeDef",
    {"autotrack": str},
    total=False,
)


class ClientGetConfigResponseconfigDatatrackingConfigTypeDef(
    _ClientGetConfigResponseconfigDatatrackingConfigTypeDef
):
    """
    Type definition for `ClientGetConfigResponseconfigData` `trackingConfig`

    Object that determines whether tracking should be used during a contact executed with this
    ``Config`` in the mission profile.

    - **autotrack** *(string) --*

      Current setting for autotrack.
    """


_ClientGetConfigResponseconfigDatauplinkEchoConfigTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDatauplinkEchoConfigTypeDef",
    {"antennaUplinkConfigArn": str, "enabled": bool},
    total=False,
)


class ClientGetConfigResponseconfigDatauplinkEchoConfigTypeDef(
    _ClientGetConfigResponseconfigDatauplinkEchoConfigTypeDef
):
    """
    Type definition for `ClientGetConfigResponseconfigData` `uplinkEchoConfig`

    Information about an uplink echo ``Config`` .

    Parameters from the ``AntennaUplinkConfig`` , corresponding to the specified
    ``AntennaUplinkConfigArn`` , are used when this ``UplinkEchoConfig`` is used in a contact.

    - **antennaUplinkConfigArn** *(string) --*

      ARN of an uplink ``Config`` .

    - **enabled** *(boolean) --*

      Whether or not an uplink ``Config`` is enabled.
    """


_ClientGetConfigResponseconfigDataTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDataTypeDef",
    {
        "antennaDownlinkConfig": ClientGetConfigResponseconfigDataantennaDownlinkConfigTypeDef,
        "antennaDownlinkDemodDecodeConfig": ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigTypeDef,
        "antennaUplinkConfig": ClientGetConfigResponseconfigDataantennaUplinkConfigTypeDef,
        "dataflowEndpointConfig": ClientGetConfigResponseconfigDatadataflowEndpointConfigTypeDef,
        "trackingConfig": ClientGetConfigResponseconfigDatatrackingConfigTypeDef,
        "uplinkEchoConfig": ClientGetConfigResponseconfigDatauplinkEchoConfigTypeDef,
    },
    total=False,
)


class ClientGetConfigResponseconfigDataTypeDef(
    _ClientGetConfigResponseconfigDataTypeDef
):
    """
    Type definition for `ClientGetConfigResponse` `configData`

    Data elements in a ``Config`` .

    - **antennaDownlinkConfig** *(dict) --*

      Information about how AWS Ground Station should configure an antenna for downlink during a
      contact.

      - **spectrumConfig** *(dict) --*

        Object that describes a spectral ``Config`` .

        - **bandwidth** *(dict) --*

          Bandwidth of a spectral ``Config`` .

          - **units** *(string) --*

            Frequency bandwidth units.

          - **value** *(float) --*

            Frequency bandwidth value.

        - **centerFrequency** *(dict) --*

          Center frequency of a spectral ``Config`` .

          - **units** *(string) --*

            Frequency units.

          - **value** *(float) --*

            Frequency value.

        - **polarization** *(string) --*

          Polarization of a spectral ``Config`` .

    - **antennaDownlinkDemodDecodeConfig** *(dict) --*

      Information about how AWS Ground Station should conﬁgure an antenna for downlink demod
      decode during a contact.

      - **decodeConfig** *(dict) --*

        Information about the decode ``Config`` .

        - **unvalidatedJSON** *(string) --*

          Unvalidated JSON of a decode ``Config`` .

      - **demodulationConfig** *(dict) --*

        Information about the demodulation ``Config`` .

        - **unvalidatedJSON** *(string) --*

          Unvalidated JSON of a demodulation ``Config`` .

      - **spectrumConfig** *(dict) --*

        Information about the spectral ``Config`` .

        - **bandwidth** *(dict) --*

          Bandwidth of a spectral ``Config`` .

          - **units** *(string) --*

            Frequency bandwidth units.

          - **value** *(float) --*

            Frequency bandwidth value.

        - **centerFrequency** *(dict) --*

          Center frequency of a spectral ``Config`` .

          - **units** *(string) --*

            Frequency units.

          - **value** *(float) --*

            Frequency value.

        - **polarization** *(string) --*

          Polarization of a spectral ``Config`` .

    - **antennaUplinkConfig** *(dict) --*

      Information about how AWS Ground Station should conﬁgure an antenna for uplink during a
      contact.

      - **spectrumConfig** *(dict) --*

        Information about the uplink spectral ``Config`` .

        - **centerFrequency** *(dict) --*

          Center frequency of an uplink spectral ``Config`` .

          - **units** *(string) --*

            Frequency units.

          - **value** *(float) --*

            Frequency value.

        - **polarization** *(string) --*

          Polarization of an uplink spectral ``Config`` .

      - **targetEirp** *(dict) --*

        EIRP of the target.

        - **units** *(string) --*

          Units of an EIRP.

        - **value** *(float) --*

          Value of an EIRP.

    - **dataflowEndpointConfig** *(dict) --*

      Information about the dataflow endpoint ``Config`` .

      - **dataflowEndpointName** *(string) --*

        Name of a dataflow endpoint.

    - **trackingConfig** *(dict) --*

      Object that determines whether tracking should be used during a contact executed with this
      ``Config`` in the mission profile.

      - **autotrack** *(string) --*

        Current setting for autotrack.

    - **uplinkEchoConfig** *(dict) --*

      Information about an uplink echo ``Config`` .

      Parameters from the ``AntennaUplinkConfig`` , corresponding to the specified
      ``AntennaUplinkConfigArn`` , are used when this ``UplinkEchoConfig`` is used in a contact.

      - **antennaUplinkConfigArn** *(string) --*

        ARN of an uplink ``Config`` .

      - **enabled** *(boolean) --*

        Whether or not an uplink ``Config`` is enabled.
    """


_ClientGetConfigResponseTypeDef = TypedDict(
    "_ClientGetConfigResponseTypeDef",
    {
        "configArn": str,
        "configData": ClientGetConfigResponseconfigDataTypeDef,
        "configId": str,
        "configType": str,
        "name": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetConfigResponseTypeDef(_ClientGetConfigResponseTypeDef):
    """
    Type definition for `ClientGetConfig` `Response`

    - **configArn** *(string) --*

      ARN of a ``Config``

    - **configData** *(dict) --*

      Data elements in a ``Config`` .

      - **antennaDownlinkConfig** *(dict) --*

        Information about how AWS Ground Station should configure an antenna for downlink during a
        contact.

        - **spectrumConfig** *(dict) --*

          Object that describes a spectral ``Config`` .

          - **bandwidth** *(dict) --*

            Bandwidth of a spectral ``Config`` .

            - **units** *(string) --*

              Frequency bandwidth units.

            - **value** *(float) --*

              Frequency bandwidth value.

          - **centerFrequency** *(dict) --*

            Center frequency of a spectral ``Config`` .

            - **units** *(string) --*

              Frequency units.

            - **value** *(float) --*

              Frequency value.

          - **polarization** *(string) --*

            Polarization of a spectral ``Config`` .

      - **antennaDownlinkDemodDecodeConfig** *(dict) --*

        Information about how AWS Ground Station should conﬁgure an antenna for downlink demod
        decode during a contact.

        - **decodeConfig** *(dict) --*

          Information about the decode ``Config`` .

          - **unvalidatedJSON** *(string) --*

            Unvalidated JSON of a decode ``Config`` .

        - **demodulationConfig** *(dict) --*

          Information about the demodulation ``Config`` .

          - **unvalidatedJSON** *(string) --*

            Unvalidated JSON of a demodulation ``Config`` .

        - **spectrumConfig** *(dict) --*

          Information about the spectral ``Config`` .

          - **bandwidth** *(dict) --*

            Bandwidth of a spectral ``Config`` .

            - **units** *(string) --*

              Frequency bandwidth units.

            - **value** *(float) --*

              Frequency bandwidth value.

          - **centerFrequency** *(dict) --*

            Center frequency of a spectral ``Config`` .

            - **units** *(string) --*

              Frequency units.

            - **value** *(float) --*

              Frequency value.

          - **polarization** *(string) --*

            Polarization of a spectral ``Config`` .

      - **antennaUplinkConfig** *(dict) --*

        Information about how AWS Ground Station should conﬁgure an antenna for uplink during a
        contact.

        - **spectrumConfig** *(dict) --*

          Information about the uplink spectral ``Config`` .

          - **centerFrequency** *(dict) --*

            Center frequency of an uplink spectral ``Config`` .

            - **units** *(string) --*

              Frequency units.

            - **value** *(float) --*

              Frequency value.

          - **polarization** *(string) --*

            Polarization of an uplink spectral ``Config`` .

        - **targetEirp** *(dict) --*

          EIRP of the target.

          - **units** *(string) --*

            Units of an EIRP.

          - **value** *(float) --*

            Value of an EIRP.

      - **dataflowEndpointConfig** *(dict) --*

        Information about the dataflow endpoint ``Config`` .

        - **dataflowEndpointName** *(string) --*

          Name of a dataflow endpoint.

      - **trackingConfig** *(dict) --*

        Object that determines whether tracking should be used during a contact executed with this
        ``Config`` in the mission profile.

        - **autotrack** *(string) --*

          Current setting for autotrack.

      - **uplinkEchoConfig** *(dict) --*

        Information about an uplink echo ``Config`` .

        Parameters from the ``AntennaUplinkConfig`` , corresponding to the specified
        ``AntennaUplinkConfigArn`` , are used when this ``UplinkEchoConfig`` is used in a contact.

        - **antennaUplinkConfigArn** *(string) --*

          ARN of an uplink ``Config`` .

        - **enabled** *(boolean) --*

          Whether or not an uplink ``Config`` is enabled.

    - **configId** *(string) --*

      UUID of a ``Config`` .

    - **configType** *(string) --*

      Type of a ``Config`` .

    - **name** *(string) --*

      Name of a ``Config`` .

    - **tags** *(dict) --*

      Tags assigned to a ``Config`` .

      - *(string) --*

        - *(string) --*
    """


_ClientGetDataflowEndpointGroupResponseendpointsDetailsendpointaddressTypeDef = TypedDict(
    "_ClientGetDataflowEndpointGroupResponseendpointsDetailsendpointaddressTypeDef",
    {"name": str, "port": int},
    total=False,
)


class ClientGetDataflowEndpointGroupResponseendpointsDetailsendpointaddressTypeDef(
    _ClientGetDataflowEndpointGroupResponseendpointsDetailsendpointaddressTypeDef
):
    """
    Type definition for `ClientGetDataflowEndpointGroupResponseendpointsDetailsendpoint` `address`

    Socket address of a dataflow endpoint.

    - **name** *(string) --*

      Name of a socket address.

    - **port** *(integer) --*

      Port of a socket address.
    """


_ClientGetDataflowEndpointGroupResponseendpointsDetailsendpointTypeDef = TypedDict(
    "_ClientGetDataflowEndpointGroupResponseendpointsDetailsendpointTypeDef",
    {
        "address": ClientGetDataflowEndpointGroupResponseendpointsDetailsendpointaddressTypeDef,
        "name": str,
        "status": str,
    },
    total=False,
)


class ClientGetDataflowEndpointGroupResponseendpointsDetailsendpointTypeDef(
    _ClientGetDataflowEndpointGroupResponseendpointsDetailsendpointTypeDef
):
    """
    Type definition for `ClientGetDataflowEndpointGroupResponseendpointsDetails` `endpoint`

    A dataflow endpoint.

    - **address** *(dict) --*

      Socket address of a dataflow endpoint.

      - **name** *(string) --*

        Name of a socket address.

      - **port** *(integer) --*

        Port of a socket address.

    - **name** *(string) --*

      Name of a dataflow endpoint.

    - **status** *(string) --*

      Status of a dataflow endpoint.
    """


_ClientGetDataflowEndpointGroupResponseendpointsDetailssecurityDetailsTypeDef = TypedDict(
    "_ClientGetDataflowEndpointGroupResponseendpointsDetailssecurityDetailsTypeDef",
    {"roleArn": str, "securityGroupIds": List[str], "subnetIds": List[str]},
    total=False,
)


class ClientGetDataflowEndpointGroupResponseendpointsDetailssecurityDetailsTypeDef(
    _ClientGetDataflowEndpointGroupResponseendpointsDetailssecurityDetailsTypeDef
):
    """
    Type definition for `ClientGetDataflowEndpointGroupResponseendpointsDetails` `securityDetails`

    Endpoint security details.

    - **roleArn** *(string) --*

      ARN to a role needed for connecting streams to your instances.

    - **securityGroupIds** *(list) --*

      The security groups to attach to the elastic network interfaces.

      - *(string) --*

    - **subnetIds** *(list) --*

      A list of subnets where AWS Ground Station places elastic network interfaces to send
      streams to your instances.

      - *(string) --*
    """


_ClientGetDataflowEndpointGroupResponseendpointsDetailsTypeDef = TypedDict(
    "_ClientGetDataflowEndpointGroupResponseendpointsDetailsTypeDef",
    {
        "endpoint": ClientGetDataflowEndpointGroupResponseendpointsDetailsendpointTypeDef,
        "securityDetails": ClientGetDataflowEndpointGroupResponseendpointsDetailssecurityDetailsTypeDef,
    },
    total=False,
)


class ClientGetDataflowEndpointGroupResponseendpointsDetailsTypeDef(
    _ClientGetDataflowEndpointGroupResponseendpointsDetailsTypeDef
):
    """
    Type definition for `ClientGetDataflowEndpointGroupResponse` `endpointsDetails`

    Information about the endpoint details.

    - **endpoint** *(dict) --*

      A dataflow endpoint.

      - **address** *(dict) --*

        Socket address of a dataflow endpoint.

        - **name** *(string) --*

          Name of a socket address.

        - **port** *(integer) --*

          Port of a socket address.

      - **name** *(string) --*

        Name of a dataflow endpoint.

      - **status** *(string) --*

        Status of a dataflow endpoint.

    - **securityDetails** *(dict) --*

      Endpoint security details.

      - **roleArn** *(string) --*

        ARN to a role needed for connecting streams to your instances.

      - **securityGroupIds** *(list) --*

        The security groups to attach to the elastic network interfaces.

        - *(string) --*

      - **subnetIds** *(list) --*

        A list of subnets where AWS Ground Station places elastic network interfaces to send
        streams to your instances.

        - *(string) --*
    """


_ClientGetDataflowEndpointGroupResponseTypeDef = TypedDict(
    "_ClientGetDataflowEndpointGroupResponseTypeDef",
    {
        "dataflowEndpointGroupArn": str,
        "dataflowEndpointGroupId": str,
        "endpointsDetails": List[
            ClientGetDataflowEndpointGroupResponseendpointsDetailsTypeDef
        ],
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetDataflowEndpointGroupResponseTypeDef(
    _ClientGetDataflowEndpointGroupResponseTypeDef
):
    """
    Type definition for `ClientGetDataflowEndpointGroup` `Response`

    - **dataflowEndpointGroupArn** *(string) --*

      ARN of a dataflow endpoint group.

    - **dataflowEndpointGroupId** *(string) --*

      UUID of a dataflow endpoint group.

    - **endpointsDetails** *(list) --*

      Details of a dataflow endpoint.

      - *(dict) --*

        Information about the endpoint details.

        - **endpoint** *(dict) --*

          A dataflow endpoint.

          - **address** *(dict) --*

            Socket address of a dataflow endpoint.

            - **name** *(string) --*

              Name of a socket address.

            - **port** *(integer) --*

              Port of a socket address.

          - **name** *(string) --*

            Name of a dataflow endpoint.

          - **status** *(string) --*

            Status of a dataflow endpoint.

        - **securityDetails** *(dict) --*

          Endpoint security details.

          - **roleArn** *(string) --*

            ARN to a role needed for connecting streams to your instances.

          - **securityGroupIds** *(list) --*

            The security groups to attach to the elastic network interfaces.

            - *(string) --*

          - **subnetIds** *(list) --*

            A list of subnets where AWS Ground Station places elastic network interfaces to send
            streams to your instances.

            - *(string) --*

    - **tags** *(dict) --*

      Tags assigned to a dataflow endpoint group.

      - *(string) --*

        - *(string) --*
    """


_ClientGetMinuteUsageResponseTypeDef = TypedDict(
    "_ClientGetMinuteUsageResponseTypeDef",
    {
        "estimatedMinutesRemaining": int,
        "isReservedMinutesCustomer": bool,
        "totalReservedMinuteAllocation": int,
        "totalScheduledMinutes": int,
        "upcomingMinutesScheduled": int,
    },
    total=False,
)


class ClientGetMinuteUsageResponseTypeDef(_ClientGetMinuteUsageResponseTypeDef):
    """
    Type definition for `ClientGetMinuteUsage` `Response`

    - **estimatedMinutesRemaining** *(integer) --*

      Estimated number of minutes remaining for an account, specific to the month being requested.

    - **isReservedMinutesCustomer** *(boolean) --*

      Returns whether or not an account has signed up for the reserved minutes pricing plan,
      specific to the month being requested.

    - **totalReservedMinuteAllocation** *(integer) --*

      Total number of reserved minutes allocated, specific to the month being requested.

    - **totalScheduledMinutes** *(integer) --*

      Total scheduled minutes for an account, specific to the month being requested.

    - **upcomingMinutesScheduled** *(integer) --*

      Upcoming minutes scheduled for an account, specific to the month being requested.
    """


_ClientGetMissionProfileResponseTypeDef = TypedDict(
    "_ClientGetMissionProfileResponseTypeDef",
    {
        "contactPostPassDurationSeconds": int,
        "contactPrePassDurationSeconds": int,
        "dataflowEdges": List[List[str]],
        "minimumViableContactDurationSeconds": int,
        "missionProfileArn": str,
        "missionProfileId": str,
        "name": str,
        "region": str,
        "tags": Dict[str, str],
        "trackingConfigArn": str,
    },
    total=False,
)


class ClientGetMissionProfileResponseTypeDef(_ClientGetMissionProfileResponseTypeDef):
    """
    Type definition for `ClientGetMissionProfile` `Response`

    - **contactPostPassDurationSeconds** *(integer) --*

      Amount of time after a contact ends that you’d like to receive a CloudWatch event indicating
      the pass has finished.

    - **contactPrePassDurationSeconds** *(integer) --*

      Amount of time prior to contact start you’d like to receive a CloudWatch event indicating an
      upcoming pass.

    - **dataflowEdges** *(list) --*

      A list of lists of ARNs. Each list of ARNs is an edge, with a from ``Config`` and a to
      ``Config`` .

      - *(list) --*

        - *(string) --*

    - **minimumViableContactDurationSeconds** *(integer) --*

      Smallest amount of time in seconds that you’d like to see for an available contact. AWS
      Ground Station will not present you with contacts shorter than this duration.

    - **missionProfileArn** *(string) --*

      ARN of a mission profile.

    - **missionProfileId** *(string) --*

      ID of a mission profile.

    - **name** *(string) --*

      Name of a mission profile.

    - **region** *(string) --*

      Region of a mission profile.

    - **tags** *(dict) --*

      Tags assigned to a mission profile.

      - *(string) --*

        - *(string) --*

    - **trackingConfigArn** *(string) --*

      ARN of a tracking ``Config`` .
    """


_ClientGetSatelliteResponseTypeDef = TypedDict(
    "_ClientGetSatelliteResponseTypeDef",
    {
        "dateCreated": datetime,
        "lastUpdated": datetime,
        "noradSatelliteID": int,
        "satelliteArn": str,
        "satelliteId": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetSatelliteResponseTypeDef(_ClientGetSatelliteResponseTypeDef):
    """
    Type definition for `ClientGetSatellite` `Response`

    - **dateCreated** *(datetime) --*

      When a satellite was created.

    - **lastUpdated** *(datetime) --*

      When a satellite was last updated.

    - **noradSatelliteID** *(integer) --*

      NORAD satellite ID number.

    - **satelliteArn** *(string) --*

      ARN of a satellite.

    - **satelliteId** *(string) --*

      UUID of a satellite.

    - **tags** *(dict) --*

      Tags assigned to a satellite.

      - *(string) --*

        - *(string) --*
    """


_ClientListConfigsResponseconfigListTypeDef = TypedDict(
    "_ClientListConfigsResponseconfigListTypeDef",
    {"configArn": str, "configId": str, "configType": str, "name": str},
    total=False,
)


class ClientListConfigsResponseconfigListTypeDef(
    _ClientListConfigsResponseconfigListTypeDef
):
    """
    Type definition for `ClientListConfigsResponse` `configList`

    An item in a list of ``Config`` objects.

    - **configArn** *(string) --*

      ARN of a ``Config`` .

    - **configId** *(string) --*

      UUID of a ``Config`` .

    - **configType** *(string) --*

      Type of a ``Config`` .

    - **name** *(string) --*

      Name of a ``Config`` .
    """


_ClientListConfigsResponseTypeDef = TypedDict(
    "_ClientListConfigsResponseTypeDef",
    {"configList": List[ClientListConfigsResponseconfigListTypeDef], "nextToken": str},
    total=False,
)


class ClientListConfigsResponseTypeDef(_ClientListConfigsResponseTypeDef):
    """
    Type definition for `ClientListConfigs` `Response`

    - **configList** *(list) --*

      List of ``Config`` items.

      - *(dict) --*

        An item in a list of ``Config`` objects.

        - **configArn** *(string) --*

          ARN of a ``Config`` .

        - **configId** *(string) --*

          UUID of a ``Config`` .

        - **configType** *(string) --*

          Type of a ``Config`` .

        - **name** *(string) --*

          Name of a ``Config`` .

    - **nextToken** *(string) --*

      Next token returned in the response of a previous ``ListConfigs`` call. Used to get the next
      page of results.
    """


_ClientListContactsResponsecontactListmaximumElevationTypeDef = TypedDict(
    "_ClientListContactsResponsecontactListmaximumElevationTypeDef",
    {"unit": str, "value": float},
    total=False,
)


class ClientListContactsResponsecontactListmaximumElevationTypeDef(
    _ClientListContactsResponsecontactListmaximumElevationTypeDef
):
    """
    Type definition for `ClientListContactsResponsecontactList` `maximumElevation`

    Maximum elevation angle of a contact.

    - **unit** *(string) --*

      Elevation angle units.

    - **value** *(float) --*

      Elevation angle value.
    """


_ClientListContactsResponsecontactListTypeDef = TypedDict(
    "_ClientListContactsResponsecontactListTypeDef",
    {
        "contactId": str,
        "contactStatus": str,
        "endTime": datetime,
        "errorMessage": str,
        "groundStation": str,
        "maximumElevation": ClientListContactsResponsecontactListmaximumElevationTypeDef,
        "missionProfileArn": str,
        "postPassEndTime": datetime,
        "prePassStartTime": datetime,
        "satelliteArn": str,
        "startTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientListContactsResponsecontactListTypeDef(
    _ClientListContactsResponsecontactListTypeDef
):
    """
    Type definition for `ClientListContactsResponse` `contactList`

    Data describing a contact.

    - **contactId** *(string) --*

      UUID of a contact.

    - **contactStatus** *(string) --*

      Status of a contact.

    - **endTime** *(datetime) --*

      End time of a contact.

    - **errorMessage** *(string) --*

      Error message of a contact.

    - **groundStation** *(string) --*

      Name of a ground station.

    - **maximumElevation** *(dict) --*

      Maximum elevation angle of a contact.

      - **unit** *(string) --*

        Elevation angle units.

      - **value** *(float) --*

        Elevation angle value.

    - **missionProfileArn** *(string) --*

      ARN of a mission profile.

    - **postPassEndTime** *(datetime) --*

      Amount of time after a contact ends that you’d like to receive a CloudWatch event
      indicating the pass has finished.

    - **prePassStartTime** *(datetime) --*

      Amount of time prior to contact start you’d like to receive a CloudWatch event indicating
      an upcoming pass.

    - **satelliteArn** *(string) --*

      ARN of a satellite.

    - **startTime** *(datetime) --*

      Start time of a contact.

    - **tags** *(dict) --*

      Tags assigned to a contact.

      - *(string) --*

        - *(string) --*
    """


_ClientListContactsResponseTypeDef = TypedDict(
    "_ClientListContactsResponseTypeDef",
    {
        "contactList": List[ClientListContactsResponsecontactListTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListContactsResponseTypeDef(_ClientListContactsResponseTypeDef):
    """
    Type definition for `ClientListContacts` `Response`

    - **contactList** *(list) --*

      List of contacts.

      - *(dict) --*

        Data describing a contact.

        - **contactId** *(string) --*

          UUID of a contact.

        - **contactStatus** *(string) --*

          Status of a contact.

        - **endTime** *(datetime) --*

          End time of a contact.

        - **errorMessage** *(string) --*

          Error message of a contact.

        - **groundStation** *(string) --*

          Name of a ground station.

        - **maximumElevation** *(dict) --*

          Maximum elevation angle of a contact.

          - **unit** *(string) --*

            Elevation angle units.

          - **value** *(float) --*

            Elevation angle value.

        - **missionProfileArn** *(string) --*

          ARN of a mission profile.

        - **postPassEndTime** *(datetime) --*

          Amount of time after a contact ends that you’d like to receive a CloudWatch event
          indicating the pass has finished.

        - **prePassStartTime** *(datetime) --*

          Amount of time prior to contact start you’d like to receive a CloudWatch event indicating
          an upcoming pass.

        - **satelliteArn** *(string) --*

          ARN of a satellite.

        - **startTime** *(datetime) --*

          Start time of a contact.

        - **tags** *(dict) --*

          Tags assigned to a contact.

          - *(string) --*

            - *(string) --*

    - **nextToken** *(string) --*

      Next token returned in the response of a previous ``ListContacts`` call. Used to get the next
      page of results.
    """


_ClientListDataflowEndpointGroupsResponsedataflowEndpointGroupListTypeDef = TypedDict(
    "_ClientListDataflowEndpointGroupsResponsedataflowEndpointGroupListTypeDef",
    {"dataflowEndpointGroupArn": str, "dataflowEndpointGroupId": str},
    total=False,
)


class ClientListDataflowEndpointGroupsResponsedataflowEndpointGroupListTypeDef(
    _ClientListDataflowEndpointGroupsResponsedataflowEndpointGroupListTypeDef
):
    """
    Type definition for `ClientListDataflowEndpointGroupsResponse` `dataflowEndpointGroupList`

    Item in a list of ``DataflowEndpoint`` groups.

    - **dataflowEndpointGroupArn** *(string) --*

      ARN of a dataflow endpoint group.

    - **dataflowEndpointGroupId** *(string) --*

      UUID of a dataflow endpoint group.
    """


_ClientListDataflowEndpointGroupsResponseTypeDef = TypedDict(
    "_ClientListDataflowEndpointGroupsResponseTypeDef",
    {
        "dataflowEndpointGroupList": List[
            ClientListDataflowEndpointGroupsResponsedataflowEndpointGroupListTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListDataflowEndpointGroupsResponseTypeDef(
    _ClientListDataflowEndpointGroupsResponseTypeDef
):
    """
    Type definition for `ClientListDataflowEndpointGroups` `Response`

    - **dataflowEndpointGroupList** *(list) --*

      A list of dataflow endpoint groups.

      - *(dict) --*

        Item in a list of ``DataflowEndpoint`` groups.

        - **dataflowEndpointGroupArn** *(string) --*

          ARN of a dataflow endpoint group.

        - **dataflowEndpointGroupId** *(string) --*

          UUID of a dataflow endpoint group.

    - **nextToken** *(string) --*

      Next token returned in the response of a previous ``ListDataflowEndpointGroups`` call. Used
      to get the next page of results.
    """


_ClientListGroundStationsResponsegroundStationListTypeDef = TypedDict(
    "_ClientListGroundStationsResponsegroundStationListTypeDef",
    {"groundStationId": str, "groundStationName": str, "region": str},
    total=False,
)


class ClientListGroundStationsResponsegroundStationListTypeDef(
    _ClientListGroundStationsResponsegroundStationListTypeDef
):
    """
    Type definition for `ClientListGroundStationsResponse` `groundStationList`

    Information about the ground station data.

    - **groundStationId** *(string) --*

      ID of a ground station.

    - **groundStationName** *(string) --*

      Name of a ground station.

    - **region** *(string) --*

      Ground station Region.
    """


_ClientListGroundStationsResponseTypeDef = TypedDict(
    "_ClientListGroundStationsResponseTypeDef",
    {
        "groundStationList": List[
            ClientListGroundStationsResponsegroundStationListTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListGroundStationsResponseTypeDef(_ClientListGroundStationsResponseTypeDef):
    """
    Type definition for `ClientListGroundStations` `Response`

    - **groundStationList** *(list) --*

      List of ground stations.

      - *(dict) --*

        Information about the ground station data.

        - **groundStationId** *(string) --*

          ID of a ground station.

        - **groundStationName** *(string) --*

          Name of a ground station.

        - **region** *(string) --*

          Ground station Region.

    - **nextToken** *(string) --*

      Next token that can be supplied in the next call to get the next page of ground stations.
    """


_ClientListMissionProfilesResponsemissionProfileListTypeDef = TypedDict(
    "_ClientListMissionProfilesResponsemissionProfileListTypeDef",
    {"missionProfileArn": str, "missionProfileId": str, "name": str, "region": str},
    total=False,
)


class ClientListMissionProfilesResponsemissionProfileListTypeDef(
    _ClientListMissionProfilesResponsemissionProfileListTypeDef
):
    """
    Type definition for `ClientListMissionProfilesResponse` `missionProfileList`

    Item in a list of mission profiles.

    - **missionProfileArn** *(string) --*

      ARN of a mission profile.

    - **missionProfileId** *(string) --*

      ID of a mission profile.

    - **name** *(string) --*

      Name of a mission profile.

    - **region** *(string) --*

      Region of a mission profile.
    """


_ClientListMissionProfilesResponseTypeDef = TypedDict(
    "_ClientListMissionProfilesResponseTypeDef",
    {
        "missionProfileList": List[
            ClientListMissionProfilesResponsemissionProfileListTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListMissionProfilesResponseTypeDef(
    _ClientListMissionProfilesResponseTypeDef
):
    """
    Type definition for `ClientListMissionProfiles` `Response`

    - **missionProfileList** *(list) --*

      List of mission profiles

      - *(dict) --*

        Item in a list of mission profiles.

        - **missionProfileArn** *(string) --*

          ARN of a mission profile.

        - **missionProfileId** *(string) --*

          ID of a mission profile.

        - **name** *(string) --*

          Name of a mission profile.

        - **region** *(string) --*

          Region of a mission profile.

    - **nextToken** *(string) --*

      Next token returned in the response of a previous ``ListMissionProfiles`` call. Used to get
      the next page of results.
    """


_ClientListSatellitesResponsesatellitesTypeDef = TypedDict(
    "_ClientListSatellitesResponsesatellitesTypeDef",
    {"noradSatelliteID": int, "satelliteArn": str, "satelliteId": str},
    total=False,
)


class ClientListSatellitesResponsesatellitesTypeDef(
    _ClientListSatellitesResponsesatellitesTypeDef
):
    """
    Type definition for `ClientListSatellitesResponse` `satellites`

    Item in a list of satellites.

    - **noradSatelliteID** *(integer) --*

      NORAD satellite ID number.

    - **satelliteArn** *(string) --*

      ARN of a satellite.

    - **satelliteId** *(string) --*

      ID of a satellite.
    """


_ClientListSatellitesResponseTypeDef = TypedDict(
    "_ClientListSatellitesResponseTypeDef",
    {
        "nextToken": str,
        "satellites": List[ClientListSatellitesResponsesatellitesTypeDef],
    },
    total=False,
)


class ClientListSatellitesResponseTypeDef(_ClientListSatellitesResponseTypeDef):
    """
    Type definition for `ClientListSatellites` `Response`

    - **nextToken** *(string) --*

      Next token that can be supplied in the next call to get the next page of satellites.

    - **satellites** *(list) --*

      List of satellites.

      - *(dict) --*

        Item in a list of satellites.

        - **noradSatelliteID** *(integer) --*

          NORAD satellite ID number.

        - **satelliteArn** *(string) --*

          ARN of a satellite.

        - **satelliteId** *(string) --*

          ID of a satellite.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **tags** *(dict) --*

      Tags assigned to a resource.

      - *(string) --*

        - *(string) --*
    """


_ClientReserveContactResponseTypeDef = TypedDict(
    "_ClientReserveContactResponseTypeDef", {"contactId": str}, total=False
)


class ClientReserveContactResponseTypeDef(_ClientReserveContactResponseTypeDef):
    """
    Type definition for `ClientReserveContact` `Response`

    - **contactId** *(string) --*

      UUID of a contact.
    """


_ClientUpdateConfigResponseTypeDef = TypedDict(
    "_ClientUpdateConfigResponseTypeDef",
    {"configArn": str, "configId": str, "configType": str},
    total=False,
)


class ClientUpdateConfigResponseTypeDef(_ClientUpdateConfigResponseTypeDef):
    """
    Type definition for `ClientUpdateConfig` `Response`

    - **configArn** *(string) --*

      ARN of a ``Config`` .

    - **configId** *(string) --*

      UUID of a ``Config`` .

    - **configType** *(string) --*

      Type of a ``Config`` .
    """


_ClientUpdateConfigconfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef = TypedDict(
    "_ClientUpdateConfigconfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef",
    {"units": str, "value": float},
)


class ClientUpdateConfigconfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef(
    _ClientUpdateConfigconfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef
):
    """
    Type definition for `ClientUpdateConfigconfigDataantennaDownlinkConfigspectrumConfig` `bandwidth`

    Bandwidth of a spectral ``Config`` .

    - **units** *(string) --* **[REQUIRED]**

      Frequency bandwidth units.

    - **value** *(float) --* **[REQUIRED]**

      Frequency bandwidth value.
    """


_ClientUpdateConfigconfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef = TypedDict(
    "_ClientUpdateConfigconfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef",
    {"units": str, "value": float},
)


class ClientUpdateConfigconfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef(
    _ClientUpdateConfigconfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef
):
    """
    Type definition for `ClientUpdateConfigconfigDataantennaDownlinkConfigspectrumConfig` `centerFrequency`

    Center frequency of a spectral ``Config`` .

    - **units** *(string) --* **[REQUIRED]**

      Frequency units.

    - **value** *(float) --* **[REQUIRED]**

      Frequency value.
    """


_RequiredClientUpdateConfigconfigDataantennaDownlinkConfigspectrumConfigTypeDef = TypedDict(
    "_RequiredClientUpdateConfigconfigDataantennaDownlinkConfigspectrumConfigTypeDef",
    {
        "bandwidth": ClientUpdateConfigconfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef,
        "centerFrequency": ClientUpdateConfigconfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef,
    },
)
_OptionalClientUpdateConfigconfigDataantennaDownlinkConfigspectrumConfigTypeDef = TypedDict(
    "_OptionalClientUpdateConfigconfigDataantennaDownlinkConfigspectrumConfigTypeDef",
    {"polarization": str},
    total=False,
)


class ClientUpdateConfigconfigDataantennaDownlinkConfigspectrumConfigTypeDef(
    _RequiredClientUpdateConfigconfigDataantennaDownlinkConfigspectrumConfigTypeDef,
    _OptionalClientUpdateConfigconfigDataantennaDownlinkConfigspectrumConfigTypeDef,
):
    """
    Type definition for `ClientUpdateConfigconfigDataantennaDownlinkConfig` `spectrumConfig`

    Object that describes a spectral ``Config`` .

    - **bandwidth** *(dict) --* **[REQUIRED]**

      Bandwidth of a spectral ``Config`` .

      - **units** *(string) --* **[REQUIRED]**

        Frequency bandwidth units.

      - **value** *(float) --* **[REQUIRED]**

        Frequency bandwidth value.

    - **centerFrequency** *(dict) --* **[REQUIRED]**

      Center frequency of a spectral ``Config`` .

      - **units** *(string) --* **[REQUIRED]**

        Frequency units.

      - **value** *(float) --* **[REQUIRED]**

        Frequency value.

    - **polarization** *(string) --*

      Polarization of a spectral ``Config`` .
    """


_ClientUpdateConfigconfigDataantennaDownlinkConfigTypeDef = TypedDict(
    "_ClientUpdateConfigconfigDataantennaDownlinkConfigTypeDef",
    {
        "spectrumConfig": ClientUpdateConfigconfigDataantennaDownlinkConfigspectrumConfigTypeDef
    },
)


class ClientUpdateConfigconfigDataantennaDownlinkConfigTypeDef(
    _ClientUpdateConfigconfigDataantennaDownlinkConfigTypeDef
):
    """
    Type definition for `ClientUpdateConfigconfigData` `antennaDownlinkConfig`

    Information about how AWS Ground Station should configure an antenna for downlink during a
    contact.

    - **spectrumConfig** *(dict) --* **[REQUIRED]**

      Object that describes a spectral ``Config`` .

      - **bandwidth** *(dict) --* **[REQUIRED]**

        Bandwidth of a spectral ``Config`` .

        - **units** *(string) --* **[REQUIRED]**

          Frequency bandwidth units.

        - **value** *(float) --* **[REQUIRED]**

          Frequency bandwidth value.

      - **centerFrequency** *(dict) --* **[REQUIRED]**

        Center frequency of a spectral ``Config`` .

        - **units** *(string) --* **[REQUIRED]**

          Frequency units.

        - **value** *(float) --* **[REQUIRED]**

          Frequency value.

      - **polarization** *(string) --*

        Polarization of a spectral ``Config`` .
    """


_ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef = TypedDict(
    "_ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef",
    {"unvalidatedJSON": str},
)


class ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef(
    _ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef
):
    """
    Type definition for `ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfig` `decodeConfig`

    Information about the decode ``Config`` .

    - **unvalidatedJSON** *(string) --* **[REQUIRED]**

      Unvalidated JSON of a decode ``Config`` .
    """


_ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef = TypedDict(
    "_ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef",
    {"unvalidatedJSON": str},
)


class ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef(
    _ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef
):
    """
    Type definition for `ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfig` `demodulationConfig`

    Information about the demodulation ``Config`` .

    - **unvalidatedJSON** *(string) --* **[REQUIRED]**

      Unvalidated JSON of a demodulation ``Config`` .
    """


_ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef = TypedDict(
    "_ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef",
    {"units": str, "value": float},
)


class ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef(
    _ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef
):
    """
    Type definition for `ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfig` `bandwidth`

    Bandwidth of a spectral ``Config`` .

    - **units** *(string) --* **[REQUIRED]**

      Frequency bandwidth units.

    - **value** *(float) --* **[REQUIRED]**

      Frequency bandwidth value.
    """


_ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef = TypedDict(
    "_ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef",
    {"units": str, "value": float},
)


class ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef(
    _ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef
):
    """
    Type definition for `ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfig` `centerFrequency`

    Center frequency of a spectral ``Config`` .

    - **units** *(string) --* **[REQUIRED]**

      Frequency units.

    - **value** *(float) --* **[REQUIRED]**

      Frequency value.
    """


_RequiredClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef = TypedDict(
    "_RequiredClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef",
    {
        "bandwidth": ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef,
        "centerFrequency": ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef,
    },
)
_OptionalClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef = TypedDict(
    "_OptionalClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef",
    {"polarization": str},
    total=False,
)


class ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef(
    _RequiredClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef,
    _OptionalClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef,
):
    """
    Type definition for `ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfig` `spectrumConfig`

    Information about the spectral ``Config`` .

    - **bandwidth** *(dict) --* **[REQUIRED]**

      Bandwidth of a spectral ``Config`` .

      - **units** *(string) --* **[REQUIRED]**

        Frequency bandwidth units.

      - **value** *(float) --* **[REQUIRED]**

        Frequency bandwidth value.

    - **centerFrequency** *(dict) --* **[REQUIRED]**

      Center frequency of a spectral ``Config`` .

      - **units** *(string) --* **[REQUIRED]**

        Frequency units.

      - **value** *(float) --* **[REQUIRED]**

        Frequency value.

    - **polarization** *(string) --*

      Polarization of a spectral ``Config`` .
    """


_ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigTypeDef = TypedDict(
    "_ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigTypeDef",
    {
        "decodeConfig": ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef,
        "demodulationConfig": ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef,
        "spectrumConfig": ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef,
    },
)


class ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigTypeDef(
    _ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigTypeDef
):
    """
    Type definition for `ClientUpdateConfigconfigData` `antennaDownlinkDemodDecodeConfig`

    Information about how AWS Ground Station should conﬁgure an antenna for downlink demod decode
    during a contact.

    - **decodeConfig** *(dict) --* **[REQUIRED]**

      Information about the decode ``Config`` .

      - **unvalidatedJSON** *(string) --* **[REQUIRED]**

        Unvalidated JSON of a decode ``Config`` .

    - **demodulationConfig** *(dict) --* **[REQUIRED]**

      Information about the demodulation ``Config`` .

      - **unvalidatedJSON** *(string) --* **[REQUIRED]**

        Unvalidated JSON of a demodulation ``Config`` .

    - **spectrumConfig** *(dict) --* **[REQUIRED]**

      Information about the spectral ``Config`` .

      - **bandwidth** *(dict) --* **[REQUIRED]**

        Bandwidth of a spectral ``Config`` .

        - **units** *(string) --* **[REQUIRED]**

          Frequency bandwidth units.

        - **value** *(float) --* **[REQUIRED]**

          Frequency bandwidth value.

      - **centerFrequency** *(dict) --* **[REQUIRED]**

        Center frequency of a spectral ``Config`` .

        - **units** *(string) --* **[REQUIRED]**

          Frequency units.

        - **value** *(float) --* **[REQUIRED]**

          Frequency value.

      - **polarization** *(string) --*

        Polarization of a spectral ``Config`` .
    """


_ClientUpdateConfigconfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef = TypedDict(
    "_ClientUpdateConfigconfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef",
    {"units": str, "value": float},
)


class ClientUpdateConfigconfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef(
    _ClientUpdateConfigconfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef
):
    """
    Type definition for `ClientUpdateConfigconfigDataantennaUplinkConfigspectrumConfig` `centerFrequency`

    Center frequency of an uplink spectral ``Config`` .

    - **units** *(string) --* **[REQUIRED]**

      Frequency units.

    - **value** *(float) --* **[REQUIRED]**

      Frequency value.
    """


_RequiredClientUpdateConfigconfigDataantennaUplinkConfigspectrumConfigTypeDef = TypedDict(
    "_RequiredClientUpdateConfigconfigDataantennaUplinkConfigspectrumConfigTypeDef",
    {
        "centerFrequency": ClientUpdateConfigconfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef
    },
)
_OptionalClientUpdateConfigconfigDataantennaUplinkConfigspectrumConfigTypeDef = TypedDict(
    "_OptionalClientUpdateConfigconfigDataantennaUplinkConfigspectrumConfigTypeDef",
    {"polarization": str},
    total=False,
)


class ClientUpdateConfigconfigDataantennaUplinkConfigspectrumConfigTypeDef(
    _RequiredClientUpdateConfigconfigDataantennaUplinkConfigspectrumConfigTypeDef,
    _OptionalClientUpdateConfigconfigDataantennaUplinkConfigspectrumConfigTypeDef,
):
    """
    Type definition for `ClientUpdateConfigconfigDataantennaUplinkConfig` `spectrumConfig`

    Information about the uplink spectral ``Config`` .

    - **centerFrequency** *(dict) --* **[REQUIRED]**

      Center frequency of an uplink spectral ``Config`` .

      - **units** *(string) --* **[REQUIRED]**

        Frequency units.

      - **value** *(float) --* **[REQUIRED]**

        Frequency value.

    - **polarization** *(string) --*

      Polarization of an uplink spectral ``Config`` .
    """


_ClientUpdateConfigconfigDataantennaUplinkConfigtargetEirpTypeDef = TypedDict(
    "_ClientUpdateConfigconfigDataantennaUplinkConfigtargetEirpTypeDef",
    {"units": str, "value": float},
)


class ClientUpdateConfigconfigDataantennaUplinkConfigtargetEirpTypeDef(
    _ClientUpdateConfigconfigDataantennaUplinkConfigtargetEirpTypeDef
):
    """
    Type definition for `ClientUpdateConfigconfigDataantennaUplinkConfig` `targetEirp`

    EIRP of the target.

    - **units** *(string) --* **[REQUIRED]**

      Units of an EIRP.

    - **value** *(float) --* **[REQUIRED]**

      Value of an EIRP.
    """


_ClientUpdateConfigconfigDataantennaUplinkConfigTypeDef = TypedDict(
    "_ClientUpdateConfigconfigDataantennaUplinkConfigTypeDef",
    {
        "spectrumConfig": ClientUpdateConfigconfigDataantennaUplinkConfigspectrumConfigTypeDef,
        "targetEirp": ClientUpdateConfigconfigDataantennaUplinkConfigtargetEirpTypeDef,
    },
)


class ClientUpdateConfigconfigDataantennaUplinkConfigTypeDef(
    _ClientUpdateConfigconfigDataantennaUplinkConfigTypeDef
):
    """
    Type definition for `ClientUpdateConfigconfigData` `antennaUplinkConfig`

    Information about how AWS Ground Station should conﬁgure an antenna for uplink during a contact.

    - **spectrumConfig** *(dict) --* **[REQUIRED]**

      Information about the uplink spectral ``Config`` .

      - **centerFrequency** *(dict) --* **[REQUIRED]**

        Center frequency of an uplink spectral ``Config`` .

        - **units** *(string) --* **[REQUIRED]**

          Frequency units.

        - **value** *(float) --* **[REQUIRED]**

          Frequency value.

      - **polarization** *(string) --*

        Polarization of an uplink spectral ``Config`` .

    - **targetEirp** *(dict) --* **[REQUIRED]**

      EIRP of the target.

      - **units** *(string) --* **[REQUIRED]**

        Units of an EIRP.

      - **value** *(float) --* **[REQUIRED]**

        Value of an EIRP.
    """


_ClientUpdateConfigconfigDatadataflowEndpointConfigTypeDef = TypedDict(
    "_ClientUpdateConfigconfigDatadataflowEndpointConfigTypeDef",
    {"dataflowEndpointName": str},
)


class ClientUpdateConfigconfigDatadataflowEndpointConfigTypeDef(
    _ClientUpdateConfigconfigDatadataflowEndpointConfigTypeDef
):
    """
    Type definition for `ClientUpdateConfigconfigData` `dataflowEndpointConfig`

    Information about the dataflow endpoint ``Config`` .

    - **dataflowEndpointName** *(string) --* **[REQUIRED]**

      Name of a dataflow endpoint.
    """


_ClientUpdateConfigconfigDatatrackingConfigTypeDef = TypedDict(
    "_ClientUpdateConfigconfigDatatrackingConfigTypeDef", {"autotrack": str}
)


class ClientUpdateConfigconfigDatatrackingConfigTypeDef(
    _ClientUpdateConfigconfigDatatrackingConfigTypeDef
):
    """
    Type definition for `ClientUpdateConfigconfigData` `trackingConfig`

    Object that determines whether tracking should be used during a contact executed with this
    ``Config`` in the mission profile.

    - **autotrack** *(string) --* **[REQUIRED]**

      Current setting for autotrack.
    """


_ClientUpdateConfigconfigDatauplinkEchoConfigTypeDef = TypedDict(
    "_ClientUpdateConfigconfigDatauplinkEchoConfigTypeDef",
    {"antennaUplinkConfigArn": str, "enabled": bool},
)


class ClientUpdateConfigconfigDatauplinkEchoConfigTypeDef(
    _ClientUpdateConfigconfigDatauplinkEchoConfigTypeDef
):
    """
    Type definition for `ClientUpdateConfigconfigData` `uplinkEchoConfig`

    Information about an uplink echo ``Config`` .

    Parameters from the ``AntennaUplinkConfig`` , corresponding to the specified
    ``AntennaUplinkConfigArn`` , are used when this ``UplinkEchoConfig`` is used in a contact.

    - **antennaUplinkConfigArn** *(string) --* **[REQUIRED]**

      ARN of an uplink ``Config`` .

    - **enabled** *(boolean) --* **[REQUIRED]**

      Whether or not an uplink ``Config`` is enabled.
    """


_ClientUpdateConfigconfigDataTypeDef = TypedDict(
    "_ClientUpdateConfigconfigDataTypeDef",
    {
        "antennaDownlinkConfig": ClientUpdateConfigconfigDataantennaDownlinkConfigTypeDef,
        "antennaDownlinkDemodDecodeConfig": ClientUpdateConfigconfigDataantennaDownlinkDemodDecodeConfigTypeDef,
        "antennaUplinkConfig": ClientUpdateConfigconfigDataantennaUplinkConfigTypeDef,
        "dataflowEndpointConfig": ClientUpdateConfigconfigDatadataflowEndpointConfigTypeDef,
        "trackingConfig": ClientUpdateConfigconfigDatatrackingConfigTypeDef,
        "uplinkEchoConfig": ClientUpdateConfigconfigDatauplinkEchoConfigTypeDef,
    },
    total=False,
)


class ClientUpdateConfigconfigDataTypeDef(_ClientUpdateConfigconfigDataTypeDef):
    """
    Type definition for `ClientUpdateConfig` `configData`

    Parameters for a ``Config`` .

    - **antennaDownlinkConfig** *(dict) --*

      Information about how AWS Ground Station should configure an antenna for downlink during a
      contact.

      - **spectrumConfig** *(dict) --* **[REQUIRED]**

        Object that describes a spectral ``Config`` .

        - **bandwidth** *(dict) --* **[REQUIRED]**

          Bandwidth of a spectral ``Config`` .

          - **units** *(string) --* **[REQUIRED]**

            Frequency bandwidth units.

          - **value** *(float) --* **[REQUIRED]**

            Frequency bandwidth value.

        - **centerFrequency** *(dict) --* **[REQUIRED]**

          Center frequency of a spectral ``Config`` .

          - **units** *(string) --* **[REQUIRED]**

            Frequency units.

          - **value** *(float) --* **[REQUIRED]**

            Frequency value.

        - **polarization** *(string) --*

          Polarization of a spectral ``Config`` .

    - **antennaDownlinkDemodDecodeConfig** *(dict) --*

      Information about how AWS Ground Station should conﬁgure an antenna for downlink demod decode
      during a contact.

      - **decodeConfig** *(dict) --* **[REQUIRED]**

        Information about the decode ``Config`` .

        - **unvalidatedJSON** *(string) --* **[REQUIRED]**

          Unvalidated JSON of a decode ``Config`` .

      - **demodulationConfig** *(dict) --* **[REQUIRED]**

        Information about the demodulation ``Config`` .

        - **unvalidatedJSON** *(string) --* **[REQUIRED]**

          Unvalidated JSON of a demodulation ``Config`` .

      - **spectrumConfig** *(dict) --* **[REQUIRED]**

        Information about the spectral ``Config`` .

        - **bandwidth** *(dict) --* **[REQUIRED]**

          Bandwidth of a spectral ``Config`` .

          - **units** *(string) --* **[REQUIRED]**

            Frequency bandwidth units.

          - **value** *(float) --* **[REQUIRED]**

            Frequency bandwidth value.

        - **centerFrequency** *(dict) --* **[REQUIRED]**

          Center frequency of a spectral ``Config`` .

          - **units** *(string) --* **[REQUIRED]**

            Frequency units.

          - **value** *(float) --* **[REQUIRED]**

            Frequency value.

        - **polarization** *(string) --*

          Polarization of a spectral ``Config`` .

    - **antennaUplinkConfig** *(dict) --*

      Information about how AWS Ground Station should conﬁgure an antenna for uplink during a contact.

      - **spectrumConfig** *(dict) --* **[REQUIRED]**

        Information about the uplink spectral ``Config`` .

        - **centerFrequency** *(dict) --* **[REQUIRED]**

          Center frequency of an uplink spectral ``Config`` .

          - **units** *(string) --* **[REQUIRED]**

            Frequency units.

          - **value** *(float) --* **[REQUIRED]**

            Frequency value.

        - **polarization** *(string) --*

          Polarization of an uplink spectral ``Config`` .

      - **targetEirp** *(dict) --* **[REQUIRED]**

        EIRP of the target.

        - **units** *(string) --* **[REQUIRED]**

          Units of an EIRP.

        - **value** *(float) --* **[REQUIRED]**

          Value of an EIRP.

    - **dataflowEndpointConfig** *(dict) --*

      Information about the dataflow endpoint ``Config`` .

      - **dataflowEndpointName** *(string) --* **[REQUIRED]**

        Name of a dataflow endpoint.

    - **trackingConfig** *(dict) --*

      Object that determines whether tracking should be used during a contact executed with this
      ``Config`` in the mission profile.

      - **autotrack** *(string) --* **[REQUIRED]**

        Current setting for autotrack.

    - **uplinkEchoConfig** *(dict) --*

      Information about an uplink echo ``Config`` .

      Parameters from the ``AntennaUplinkConfig`` , corresponding to the specified
      ``AntennaUplinkConfigArn`` , are used when this ``UplinkEchoConfig`` is used in a contact.

      - **antennaUplinkConfigArn** *(string) --* **[REQUIRED]**

        ARN of an uplink ``Config`` .

      - **enabled** *(boolean) --* **[REQUIRED]**

        Whether or not an uplink ``Config`` is enabled.
    """


_ClientUpdateMissionProfileResponseTypeDef = TypedDict(
    "_ClientUpdateMissionProfileResponseTypeDef", {"missionProfileId": str}, total=False
)


class ClientUpdateMissionProfileResponseTypeDef(
    _ClientUpdateMissionProfileResponseTypeDef
):
    """
    Type definition for `ClientUpdateMissionProfile` `Response`

    - **missionProfileId** *(string) --*

      ID of a mission profile.
    """


_ListConfigsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListConfigsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListConfigsPaginatePaginationConfigTypeDef(
    _ListConfigsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListConfigsPaginate` `PaginationConfig`

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


_ListConfigsPaginateResponseconfigListTypeDef = TypedDict(
    "_ListConfigsPaginateResponseconfigListTypeDef",
    {"configArn": str, "configId": str, "configType": str, "name": str},
    total=False,
)


class ListConfigsPaginateResponseconfigListTypeDef(
    _ListConfigsPaginateResponseconfigListTypeDef
):
    """
    Type definition for `ListConfigsPaginateResponse` `configList`

    An item in a list of ``Config`` objects.

    - **configArn** *(string) --*

      ARN of a ``Config`` .

    - **configId** *(string) --*

      UUID of a ``Config`` .

    - **configType** *(string) --*

      Type of a ``Config`` .

    - **name** *(string) --*

      Name of a ``Config`` .
    """


_ListConfigsPaginateResponseTypeDef = TypedDict(
    "_ListConfigsPaginateResponseTypeDef",
    {
        "configList": List[ListConfigsPaginateResponseconfigListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListConfigsPaginateResponseTypeDef(_ListConfigsPaginateResponseTypeDef):
    """
    Type definition for `ListConfigsPaginate` `Response`

    - **configList** *(list) --*

      List of ``Config`` items.

      - *(dict) --*

        An item in a list of ``Config`` objects.

        - **configArn** *(string) --*

          ARN of a ``Config`` .

        - **configId** *(string) --*

          UUID of a ``Config`` .

        - **configType** *(string) --*

          Type of a ``Config`` .

        - **name** *(string) --*

          Name of a ``Config`` .

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListContactsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListContactsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListContactsPaginatePaginationConfigTypeDef(
    _ListContactsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListContactsPaginate` `PaginationConfig`

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


_ListContactsPaginateResponsecontactListmaximumElevationTypeDef = TypedDict(
    "_ListContactsPaginateResponsecontactListmaximumElevationTypeDef",
    {"unit": str, "value": float},
    total=False,
)


class ListContactsPaginateResponsecontactListmaximumElevationTypeDef(
    _ListContactsPaginateResponsecontactListmaximumElevationTypeDef
):
    """
    Type definition for `ListContactsPaginateResponsecontactList` `maximumElevation`

    Maximum elevation angle of a contact.

    - **unit** *(string) --*

      Elevation angle units.

    - **value** *(float) --*

      Elevation angle value.
    """


_ListContactsPaginateResponsecontactListTypeDef = TypedDict(
    "_ListContactsPaginateResponsecontactListTypeDef",
    {
        "contactId": str,
        "contactStatus": str,
        "endTime": datetime,
        "errorMessage": str,
        "groundStation": str,
        "maximumElevation": ListContactsPaginateResponsecontactListmaximumElevationTypeDef,
        "missionProfileArn": str,
        "postPassEndTime": datetime,
        "prePassStartTime": datetime,
        "satelliteArn": str,
        "startTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)


class ListContactsPaginateResponsecontactListTypeDef(
    _ListContactsPaginateResponsecontactListTypeDef
):
    """
    Type definition for `ListContactsPaginateResponse` `contactList`

    Data describing a contact.

    - **contactId** *(string) --*

      UUID of a contact.

    - **contactStatus** *(string) --*

      Status of a contact.

    - **endTime** *(datetime) --*

      End time of a contact.

    - **errorMessage** *(string) --*

      Error message of a contact.

    - **groundStation** *(string) --*

      Name of a ground station.

    - **maximumElevation** *(dict) --*

      Maximum elevation angle of a contact.

      - **unit** *(string) --*

        Elevation angle units.

      - **value** *(float) --*

        Elevation angle value.

    - **missionProfileArn** *(string) --*

      ARN of a mission profile.

    - **postPassEndTime** *(datetime) --*

      Amount of time after a contact ends that you’d like to receive a CloudWatch event
      indicating the pass has finished.

    - **prePassStartTime** *(datetime) --*

      Amount of time prior to contact start you’d like to receive a CloudWatch event indicating
      an upcoming pass.

    - **satelliteArn** *(string) --*

      ARN of a satellite.

    - **startTime** *(datetime) --*

      Start time of a contact.

    - **tags** *(dict) --*

      Tags assigned to a contact.

      - *(string) --*

        - *(string) --*
    """


_ListContactsPaginateResponseTypeDef = TypedDict(
    "_ListContactsPaginateResponseTypeDef",
    {
        "contactList": List[ListContactsPaginateResponsecontactListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListContactsPaginateResponseTypeDef(_ListContactsPaginateResponseTypeDef):
    """
    Type definition for `ListContactsPaginate` `Response`

    - **contactList** *(list) --*

      List of contacts.

      - *(dict) --*

        Data describing a contact.

        - **contactId** *(string) --*

          UUID of a contact.

        - **contactStatus** *(string) --*

          Status of a contact.

        - **endTime** *(datetime) --*

          End time of a contact.

        - **errorMessage** *(string) --*

          Error message of a contact.

        - **groundStation** *(string) --*

          Name of a ground station.

        - **maximumElevation** *(dict) --*

          Maximum elevation angle of a contact.

          - **unit** *(string) --*

            Elevation angle units.

          - **value** *(float) --*

            Elevation angle value.

        - **missionProfileArn** *(string) --*

          ARN of a mission profile.

        - **postPassEndTime** *(datetime) --*

          Amount of time after a contact ends that you’d like to receive a CloudWatch event
          indicating the pass has finished.

        - **prePassStartTime** *(datetime) --*

          Amount of time prior to contact start you’d like to receive a CloudWatch event indicating
          an upcoming pass.

        - **satelliteArn** *(string) --*

          ARN of a satellite.

        - **startTime** *(datetime) --*

          Start time of a contact.

        - **tags** *(dict) --*

          Tags assigned to a contact.

          - *(string) --*

            - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListDataflowEndpointGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDataflowEndpointGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDataflowEndpointGroupsPaginatePaginationConfigTypeDef(
    _ListDataflowEndpointGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDataflowEndpointGroupsPaginate` `PaginationConfig`

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


_ListDataflowEndpointGroupsPaginateResponsedataflowEndpointGroupListTypeDef = TypedDict(
    "_ListDataflowEndpointGroupsPaginateResponsedataflowEndpointGroupListTypeDef",
    {"dataflowEndpointGroupArn": str, "dataflowEndpointGroupId": str},
    total=False,
)


class ListDataflowEndpointGroupsPaginateResponsedataflowEndpointGroupListTypeDef(
    _ListDataflowEndpointGroupsPaginateResponsedataflowEndpointGroupListTypeDef
):
    """
    Type definition for `ListDataflowEndpointGroupsPaginateResponse` `dataflowEndpointGroupList`

    Item in a list of ``DataflowEndpoint`` groups.

    - **dataflowEndpointGroupArn** *(string) --*

      ARN of a dataflow endpoint group.

    - **dataflowEndpointGroupId** *(string) --*

      UUID of a dataflow endpoint group.
    """


_ListDataflowEndpointGroupsPaginateResponseTypeDef = TypedDict(
    "_ListDataflowEndpointGroupsPaginateResponseTypeDef",
    {
        "dataflowEndpointGroupList": List[
            ListDataflowEndpointGroupsPaginateResponsedataflowEndpointGroupListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListDataflowEndpointGroupsPaginateResponseTypeDef(
    _ListDataflowEndpointGroupsPaginateResponseTypeDef
):
    """
    Type definition for `ListDataflowEndpointGroupsPaginate` `Response`

    - **dataflowEndpointGroupList** *(list) --*

      A list of dataflow endpoint groups.

      - *(dict) --*

        Item in a list of ``DataflowEndpoint`` groups.

        - **dataflowEndpointGroupArn** *(string) --*

          ARN of a dataflow endpoint group.

        - **dataflowEndpointGroupId** *(string) --*

          UUID of a dataflow endpoint group.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListGroundStationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListGroundStationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListGroundStationsPaginatePaginationConfigTypeDef(
    _ListGroundStationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListGroundStationsPaginate` `PaginationConfig`

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


_ListGroundStationsPaginateResponsegroundStationListTypeDef = TypedDict(
    "_ListGroundStationsPaginateResponsegroundStationListTypeDef",
    {"groundStationId": str, "groundStationName": str, "region": str},
    total=False,
)


class ListGroundStationsPaginateResponsegroundStationListTypeDef(
    _ListGroundStationsPaginateResponsegroundStationListTypeDef
):
    """
    Type definition for `ListGroundStationsPaginateResponse` `groundStationList`

    Information about the ground station data.

    - **groundStationId** *(string) --*

      ID of a ground station.

    - **groundStationName** *(string) --*

      Name of a ground station.

    - **region** *(string) --*

      Ground station Region.
    """


_ListGroundStationsPaginateResponseTypeDef = TypedDict(
    "_ListGroundStationsPaginateResponseTypeDef",
    {
        "groundStationList": List[
            ListGroundStationsPaginateResponsegroundStationListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListGroundStationsPaginateResponseTypeDef(
    _ListGroundStationsPaginateResponseTypeDef
):
    """
    Type definition for `ListGroundStationsPaginate` `Response`

    - **groundStationList** *(list) --*

      List of ground stations.

      - *(dict) --*

        Information about the ground station data.

        - **groundStationId** *(string) --*

          ID of a ground station.

        - **groundStationName** *(string) --*

          Name of a ground station.

        - **region** *(string) --*

          Ground station Region.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListMissionProfilesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListMissionProfilesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListMissionProfilesPaginatePaginationConfigTypeDef(
    _ListMissionProfilesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListMissionProfilesPaginate` `PaginationConfig`

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


_ListMissionProfilesPaginateResponsemissionProfileListTypeDef = TypedDict(
    "_ListMissionProfilesPaginateResponsemissionProfileListTypeDef",
    {"missionProfileArn": str, "missionProfileId": str, "name": str, "region": str},
    total=False,
)


class ListMissionProfilesPaginateResponsemissionProfileListTypeDef(
    _ListMissionProfilesPaginateResponsemissionProfileListTypeDef
):
    """
    Type definition for `ListMissionProfilesPaginateResponse` `missionProfileList`

    Item in a list of mission profiles.

    - **missionProfileArn** *(string) --*

      ARN of a mission profile.

    - **missionProfileId** *(string) --*

      ID of a mission profile.

    - **name** *(string) --*

      Name of a mission profile.

    - **region** *(string) --*

      Region of a mission profile.
    """


_ListMissionProfilesPaginateResponseTypeDef = TypedDict(
    "_ListMissionProfilesPaginateResponseTypeDef",
    {
        "missionProfileList": List[
            ListMissionProfilesPaginateResponsemissionProfileListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListMissionProfilesPaginateResponseTypeDef(
    _ListMissionProfilesPaginateResponseTypeDef
):
    """
    Type definition for `ListMissionProfilesPaginate` `Response`

    - **missionProfileList** *(list) --*

      List of mission profiles

      - *(dict) --*

        Item in a list of mission profiles.

        - **missionProfileArn** *(string) --*

          ARN of a mission profile.

        - **missionProfileId** *(string) --*

          ID of a mission profile.

        - **name** *(string) --*

          Name of a mission profile.

        - **region** *(string) --*

          Region of a mission profile.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListSatellitesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSatellitesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSatellitesPaginatePaginationConfigTypeDef(
    _ListSatellitesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListSatellitesPaginate` `PaginationConfig`

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


_ListSatellitesPaginateResponsesatellitesTypeDef = TypedDict(
    "_ListSatellitesPaginateResponsesatellitesTypeDef",
    {"noradSatelliteID": int, "satelliteArn": str, "satelliteId": str},
    total=False,
)


class ListSatellitesPaginateResponsesatellitesTypeDef(
    _ListSatellitesPaginateResponsesatellitesTypeDef
):
    """
    Type definition for `ListSatellitesPaginateResponse` `satellites`

    Item in a list of satellites.

    - **noradSatelliteID** *(integer) --*

      NORAD satellite ID number.

    - **satelliteArn** *(string) --*

      ARN of a satellite.

    - **satelliteId** *(string) --*

      ID of a satellite.
    """


_ListSatellitesPaginateResponseTypeDef = TypedDict(
    "_ListSatellitesPaginateResponseTypeDef",
    {
        "satellites": List[ListSatellitesPaginateResponsesatellitesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListSatellitesPaginateResponseTypeDef(_ListSatellitesPaginateResponseTypeDef):
    """
    Type definition for `ListSatellitesPaginate` `Response`

    - **satellites** *(list) --*

      List of satellites.

      - *(dict) --*

        Item in a list of satellites.

        - **noradSatelliteID** *(integer) --*

          NORAD satellite ID number.

        - **satelliteArn** *(string) --*

          ARN of a satellite.

        - **satelliteId** *(string) --*

          ID of a satellite.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """
