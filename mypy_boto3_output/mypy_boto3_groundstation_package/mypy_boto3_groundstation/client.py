"Main interface for groundstation Client"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List
from typing_extensions import Literal, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

# pylint: disable=import-self
import mypy_boto3_groundstation.client as client_scope

# pylint: disable=import-self
import mypy_boto3_groundstation.paginator as paginator_scope
from mypy_boto3_groundstation.type_defs import (
    ClientCancelContactResponseTypeDef,
    ClientCreateConfigResponseTypeDef,
    ClientCreateConfigconfigDataTypeDef,
    ClientCreateDataflowEndpointGroupResponseTypeDef,
    ClientCreateDataflowEndpointGroupendpointDetailsTypeDef,
    ClientCreateMissionProfileResponseTypeDef,
    ClientDeleteConfigResponseTypeDef,
    ClientDeleteDataflowEndpointGroupResponseTypeDef,
    ClientDeleteMissionProfileResponseTypeDef,
    ClientDescribeContactResponseTypeDef,
    ClientGetConfigResponseTypeDef,
    ClientGetDataflowEndpointGroupResponseTypeDef,
    ClientGetMinuteUsageResponseTypeDef,
    ClientGetMissionProfileResponseTypeDef,
    ClientGetSatelliteResponseTypeDef,
    ClientListConfigsResponseTypeDef,
    ClientListContactsResponseTypeDef,
    ClientListDataflowEndpointGroupsResponseTypeDef,
    ClientListGroundStationsResponseTypeDef,
    ClientListMissionProfilesResponseTypeDef,
    ClientListSatellitesResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientReserveContactResponseTypeDef,
    ClientUpdateConfigResponseTypeDef,
    ClientUpdateConfigconfigDataTypeDef,
    ClientUpdateMissionProfileResponseTypeDef,
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
    def cancel_contact(self, contactId: str) -> ClientCancelContactResponseTypeDef:
        """
        Cancels a contact with a specified contact ID.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/CancelContact>`_

        **Request Syntax**
        ::

          response = client.cancel_contact(
              contactId='string'
          )
        :type contactId: string
        :param contactId: **[REQUIRED]**

          UUID of a contact.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'contactId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **contactId** *(string) --*

              UUID of a contact.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_config(
        self,
        configData: ClientCreateConfigconfigDataTypeDef,
        name: str,
        tags: Dict[str, str] = None,
    ) -> ClientCreateConfigResponseTypeDef:
        """
        Creates a ``Config`` with the specified ``configData`` parameters.

        Only one type of ``configData`` can be specified.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/CreateConfig>`_

        **Request Syntax**
        ::

          response = client.create_config(
              configData={
                  'antennaDownlinkConfig': {
                      'spectrumConfig': {
                          'bandwidth': {
                              'units': 'GHz'|'MHz'|'kHz',
                              'value': 123.0
                          },
                          'centerFrequency': {
                              'units': 'GHz'|'MHz'|'kHz',
                              'value': 123.0
                          },
                          'polarization': 'LEFT_HAND'|'NONE'|'RIGHT_HAND'
                      }
                  },
                  'antennaDownlinkDemodDecodeConfig': {
                      'decodeConfig': {
                          'unvalidatedJSON': 'string'
                      },
                      'demodulationConfig': {
                          'unvalidatedJSON': 'string'
                      },
                      'spectrumConfig': {
                          'bandwidth': {
                              'units': 'GHz'|'MHz'|'kHz',
                              'value': 123.0
                          },
                          'centerFrequency': {
                              'units': 'GHz'|'MHz'|'kHz',
                              'value': 123.0
                          },
                          'polarization': 'LEFT_HAND'|'NONE'|'RIGHT_HAND'
                      }
                  },
                  'antennaUplinkConfig': {
                      'spectrumConfig': {
                          'centerFrequency': {
                              'units': 'GHz'|'MHz'|'kHz',
                              'value': 123.0
                          },
                          'polarization': 'LEFT_HAND'|'NONE'|'RIGHT_HAND'
                      },
                      'targetEirp': {
                          'units': 'dBW',
                          'value': 123.0
                      }
                  },
                  'dataflowEndpointConfig': {
                      'dataflowEndpointName': 'string'
                  },
                  'trackingConfig': {
                      'autotrack': 'PREFERRED'|'REMOVED'|'REQUIRED'
                  },
                  'uplinkEchoConfig': {
                      'antennaUplinkConfigArn': 'string',
                      'enabled': True|False
                  }
              },
              name='string',
              tags={
                  'string': 'string'
              }
          )
        :type configData: dict
        :param configData: **[REQUIRED]**

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

        :type name: string
        :param name: **[REQUIRED]**

          Name of a ``Config`` .

        :type tags: dict
        :param tags:

          Tags assigned to a ``Config`` .

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'configArn': 'string',
                'configId': 'string',
                'configType':
                'antenna-downlink'|'antenna-downlink-demod-decode'|'antenna-uplink'|'dataflow-endpoint'
                |'tracking'|'uplink-echo'
            }
          **Response Structure**

          - *(dict) --*

            - **configArn** *(string) --*

              ARN of a ``Config`` .

            - **configId** *(string) --*

              UUID of a ``Config`` .

            - **configType** *(string) --*

              Type of a ``Config`` .

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_dataflow_endpoint_group(
        self,
        endpointDetails: List[ClientCreateDataflowEndpointGroupendpointDetailsTypeDef],
        tags: Dict[str, str] = None,
    ) -> ClientCreateDataflowEndpointGroupResponseTypeDef:
        """
        Creates a ``DataflowEndpoint`` group containing the specified list of ``DataflowEndpoint`` objects.

        The ``name`` field in each endpoint is used in your mission profile ``DataflowEndpointConfig`` to
        specify which endpoints to use during a contact.

        When a contact uses multiple ``DataflowEndpointConfig`` objects, each ``Config`` must match a
        ``DataflowEndpoint`` in the same group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/CreateDataflowEndpointGroup>`_

        **Request Syntax**
        ::

          response = client.create_dataflow_endpoint_group(
              endpointDetails=[
                  {
                      'endpoint': {
                          'address': {
                              'name': 'string',
                              'port': 123
                          },
                          'name': 'string',
                          'status': 'created'|'creating'|'deleted'|'deleting'|'failed'
                      },
                      'securityDetails': {
                          'roleArn': 'string',
                          'securityGroupIds': [
                              'string',
                          ],
                          'subnetIds': [
                              'string',
                          ]
                      }
                  },
              ],
              tags={
                  'string': 'string'
              }
          )
        :type endpointDetails: list
        :param endpointDetails: **[REQUIRED]**

          Endpoint details of each endpoint in the dataflow endpoint group.

          - *(dict) --*

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

        :type tags: dict
        :param tags:

          Tags of a dataflow endpoint group.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'dataflowEndpointGroupId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **dataflowEndpointGroupId** *(string) --*

              ID of a dataflow endpoint group.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_mission_profile(
        self,
        dataflowEdges: List[List[str]],
        minimumViableContactDurationSeconds: int,
        name: str,
        trackingConfigArn: str,
        contactPostPassDurationSeconds: int = None,
        contactPrePassDurationSeconds: int = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateMissionProfileResponseTypeDef:
        """
        Creates a mission profile.

         ``dataflowEdges`` is a list of lists of strings. Each lower level list of strings has two
         elements: a *from ARN* and a *to ARN* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/CreateMissionProfile>`_

        **Request Syntax**
        ::

          response = client.create_mission_profile(
              contactPostPassDurationSeconds=123,
              contactPrePassDurationSeconds=123,
              dataflowEdges=[
                  [
                      'string',
                  ],
              ],
              minimumViableContactDurationSeconds=123,
              name='string',
              tags={
                  'string': 'string'
              },
              trackingConfigArn='string'
          )
        :type contactPostPassDurationSeconds: integer
        :param contactPostPassDurationSeconds:

          Amount of time after a contact ends that you’d like to receive a CloudWatch event indicating the
          pass has finished.

        :type contactPrePassDurationSeconds: integer
        :param contactPrePassDurationSeconds:

          Amount of time prior to contact start you’d like to receive a CloudWatch event indicating an
          upcoming pass.

        :type dataflowEdges: list
        :param dataflowEdges: **[REQUIRED]**

          A list of lists of ARNs. Each list of ARNs is an edge, with a from ``Config`` and a to ``Config``
          .

          - *(list) --*

            - *(string) --*

        :type minimumViableContactDurationSeconds: integer
        :param minimumViableContactDurationSeconds: **[REQUIRED]**

          Smallest amount of time in seconds that you’d like to see for an available contact. AWS Ground
          Station will not present you with contacts shorter than this duration.

        :type name: string
        :param name: **[REQUIRED]**

          Name of a mission profile.

        :type tags: dict
        :param tags:

          Tags assigned to a mission profile.

          - *(string) --*

            - *(string) --*

        :type trackingConfigArn: string
        :param trackingConfigArn: **[REQUIRED]**

          ARN of a tracking ``Config`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'missionProfileId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **missionProfileId** *(string) --*

              ID of a mission profile.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_config(
        self, configId: str, configType: str
    ) -> ClientDeleteConfigResponseTypeDef:
        """
        Deletes a ``Config`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/DeleteConfig>`_

        **Request Syntax**
        ::

          response = client.delete_config(
              configId='string',
              configType=
                  'antenna-downlink'|'antenna-downlink-demod-decode'|'antenna-uplink'|'dataflow-endpoint'
                  |'tracking'|'uplink-echo'
          )
        :type configId: string
        :param configId: **[REQUIRED]**

          UUID of a ``Config`` .

        :type configType: string
        :param configType: **[REQUIRED]**

          Type of a ``Config`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'configArn': 'string',
                'configId': 'string',
                'configType':
                'antenna-downlink'|'antenna-downlink-demod-decode'|'antenna-uplink'|'dataflow-endpoint'
                |'tracking'|'uplink-echo'
            }
          **Response Structure**

          - *(dict) --*

            - **configArn** *(string) --*

              ARN of a ``Config`` .

            - **configId** *(string) --*

              UUID of a ``Config`` .

            - **configType** *(string) --*

              Type of a ``Config`` .

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_dataflow_endpoint_group(
        self, dataflowEndpointGroupId: str
    ) -> ClientDeleteDataflowEndpointGroupResponseTypeDef:
        """
        Deletes a dataflow endpoint group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/DeleteDataflowEndpointGroup>`_

        **Request Syntax**
        ::

          response = client.delete_dataflow_endpoint_group(
              dataflowEndpointGroupId='string'
          )
        :type dataflowEndpointGroupId: string
        :param dataflowEndpointGroupId: **[REQUIRED]**

          ID of a dataflow endpoint group.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'dataflowEndpointGroupId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **dataflowEndpointGroupId** *(string) --*

              ID of a dataflow endpoint group.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_mission_profile(
        self, missionProfileId: str
    ) -> ClientDeleteMissionProfileResponseTypeDef:
        """
        Deletes a mission profile.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/DeleteMissionProfile>`_

        **Request Syntax**
        ::

          response = client.delete_mission_profile(
              missionProfileId='string'
          )
        :type missionProfileId: string
        :param missionProfileId: **[REQUIRED]**

          UUID of a mission profile.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'missionProfileId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **missionProfileId** *(string) --*

              ID of a mission profile.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_contact(self, contactId: str) -> ClientDescribeContactResponseTypeDef:
        """
        Describes an existing contact.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/DescribeContact>`_

        **Request Syntax**
        ::

          response = client.describe_contact(
              contactId='string'
          )
        :type contactId: string
        :param contactId: **[REQUIRED]**

          UUID of a contact.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'contactId': 'string',
                'contactStatus':
                'AVAILABLE'|'AWS_CANCELLED'|'CANCELLED'|'COMPLETED'|'FAILED'|'FAILED_TO_SCHEDULE'|'PASS'
                |'POSTPASS'|'PREPASS'|'SCHEDULED'|'SCHEDULING',
                'endTime': datetime(2015, 1, 1),
                'errorMessage': 'string',
                'groundStation': 'string',
                'maximumElevation': {
                    'unit': 'DEGREE_ANGLE'|'RADIAN',
                    'value': 123.0
                },
                'missionProfileArn': 'string',
                'postPassEndTime': datetime(2015, 1, 1),
                'prePassStartTime': datetime(2015, 1, 1),
                'satelliteArn': 'string',
                'startTime': datetime(2015, 1, 1),
                'tags': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

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
    def get_config(
        self, configId: str, configType: str
    ) -> ClientGetConfigResponseTypeDef:
        """
        Returns ``Config`` information.

        Only one ``Config`` response can be returned.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/GetConfig>`_

        **Request Syntax**
        ::

          response = client.get_config(
              configId='string',
              configType=
                  'antenna-downlink'|'antenna-downlink-demod-decode'|'antenna-uplink'|'dataflow-endpoint'
                  |'tracking'|'uplink-echo'
          )
        :type configId: string
        :param configId: **[REQUIRED]**

          UUID of a ``Config`` .

        :type configType: string
        :param configType: **[REQUIRED]**

          Type of a ``Config`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'configArn': 'string',
                'configData': {
                    'antennaDownlinkConfig': {
                        'spectrumConfig': {
                            'bandwidth': {
                                'units': 'GHz'|'MHz'|'kHz',
                                'value': 123.0
                            },
                            'centerFrequency': {
                                'units': 'GHz'|'MHz'|'kHz',
                                'value': 123.0
                            },
                            'polarization': 'LEFT_HAND'|'NONE'|'RIGHT_HAND'
                        }
                    },
                    'antennaDownlinkDemodDecodeConfig': {
                        'decodeConfig': {
                            'unvalidatedJSON': 'string'
                        },
                        'demodulationConfig': {
                            'unvalidatedJSON': 'string'
                        },
                        'spectrumConfig': {
                            'bandwidth': {
                                'units': 'GHz'|'MHz'|'kHz',
                                'value': 123.0
                            },
                            'centerFrequency': {
                                'units': 'GHz'|'MHz'|'kHz',
                                'value': 123.0
                            },
                            'polarization': 'LEFT_HAND'|'NONE'|'RIGHT_HAND'
                        }
                    },
                    'antennaUplinkConfig': {
                        'spectrumConfig': {
                            'centerFrequency': {
                                'units': 'GHz'|'MHz'|'kHz',
                                'value': 123.0
                            },
                            'polarization': 'LEFT_HAND'|'NONE'|'RIGHT_HAND'
                        },
                        'targetEirp': {
                            'units': 'dBW',
                            'value': 123.0
                        }
                    },
                    'dataflowEndpointConfig': {
                        'dataflowEndpointName': 'string'
                    },
                    'trackingConfig': {
                        'autotrack': 'PREFERRED'|'REMOVED'|'REQUIRED'
                    },
                    'uplinkEchoConfig': {
                        'antennaUplinkConfigArn': 'string',
                        'enabled': True|False
                    }
                },
                'configId': 'string',
                'configType':
                'antenna-downlink'|'antenna-downlink-demod-decode'|'antenna-uplink'|'dataflow-endpoint'
                |'tracking'|'uplink-echo',
                'name': 'string',
                'tags': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_dataflow_endpoint_group(
        self, dataflowEndpointGroupId: str
    ) -> ClientGetDataflowEndpointGroupResponseTypeDef:
        """
        Returns the dataflow endpoint group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/GetDataflowEndpointGroup>`_

        **Request Syntax**
        ::

          response = client.get_dataflow_endpoint_group(
              dataflowEndpointGroupId='string'
          )
        :type dataflowEndpointGroupId: string
        :param dataflowEndpointGroupId: **[REQUIRED]**

          UUID of a dataflow endpoint group.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'dataflowEndpointGroupArn': 'string',
                'dataflowEndpointGroupId': 'string',
                'endpointsDetails': [
                    {
                        'endpoint': {
                            'address': {
                                'name': 'string',
                                'port': 123
                            },
                            'name': 'string',
                            'status': 'created'|'creating'|'deleted'|'deleting'|'failed'
                        },
                        'securityDetails': {
                            'roleArn': 'string',
                            'securityGroupIds': [
                                'string',
                            ],
                            'subnetIds': [
                                'string',
                            ]
                        }
                    },
                ],
                'tags': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_minute_usage(
        self, month: int, year: int
    ) -> ClientGetMinuteUsageResponseTypeDef:
        """
        Returns the number of minutes used by account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/GetMinuteUsage>`_

        **Request Syntax**
        ::

          response = client.get_minute_usage(
              month=123,
              year=123
          )
        :type month: integer
        :param month: **[REQUIRED]**

          The month being requested, with a value of 1-12.

        :type year: integer
        :param year: **[REQUIRED]**

          The year being requested, in the format of YYYY.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'estimatedMinutesRemaining': 123,
                'isReservedMinutesCustomer': True|False,
                'totalReservedMinuteAllocation': 123,
                'totalScheduledMinutes': 123,
                'upcomingMinutesScheduled': 123
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_mission_profile(
        self, missionProfileId: str
    ) -> ClientGetMissionProfileResponseTypeDef:
        """
        Returns a mission profile.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/GetMissionProfile>`_

        **Request Syntax**
        ::

          response = client.get_mission_profile(
              missionProfileId='string'
          )
        :type missionProfileId: string
        :param missionProfileId: **[REQUIRED]**

          UUID of a mission profile.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'contactPostPassDurationSeconds': 123,
                'contactPrePassDurationSeconds': 123,
                'dataflowEdges': [
                    [
                        'string',
                    ],
                ],
                'minimumViableContactDurationSeconds': 123,
                'missionProfileArn': 'string',
                'missionProfileId': 'string',
                'name': 'string',
                'region': 'string',
                'tags': {
                    'string': 'string'
                },
                'trackingConfigArn': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_satellite(self, satelliteId: str) -> ClientGetSatelliteResponseTypeDef:
        """
        Returns a satellite.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/GetSatellite>`_

        **Request Syntax**
        ::

          response = client.get_satellite(
              satelliteId='string'
          )
        :type satelliteId: string
        :param satelliteId: **[REQUIRED]**

          UUID of a satellite.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'dateCreated': datetime(2015, 1, 1),
                'lastUpdated': datetime(2015, 1, 1),
                'noradSatelliteID': 123,
                'satelliteArn': 'string',
                'satelliteId': 'string',
                'tags': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_configs(
        self, maxResults: int = None, nextToken: str = None
    ) -> ClientListConfigsResponseTypeDef:
        """
        Returns a list of ``Config`` objects.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/ListConfigs>`_

        **Request Syntax**
        ::

          response = client.list_configs(
              maxResults=123,
              nextToken='string'
          )
        :type maxResults: integer
        :param maxResults:

          Maximum number of ``Configs`` returned.

        :type nextToken: string
        :param nextToken:

          Next token returned in the request of a previous ``ListConfigs`` call. Used to get the next page
          of results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'configList': [
                    {
                        'configArn': 'string',
                        'configId': 'string',
                        'configType':
                        'antenna-downlink'|'antenna-downlink-demod-decode'|'antenna-uplink'
                        |'dataflow-endpoint'|'tracking'|'uplink-echo',
                        'name': 'string'
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_contacts(
        self,
        endTime: datetime,
        startTime: datetime,
        statusList: List[str],
        groundStation: str = None,
        maxResults: int = None,
        missionProfileArn: str = None,
        nextToken: str = None,
        satelliteArn: str = None,
    ) -> ClientListContactsResponseTypeDef:
        """
        Returns a list of contacts.

        If ``statusList`` contains AVAILABLE, the request must include ``groundstation`` ,
        ``missionprofileArn`` , and ``satelliteArn`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/ListContacts>`_

        **Request Syntax**
        ::

          response = client.list_contacts(
              endTime=datetime(2015, 1, 1),
              groundStation='string',
              maxResults=123,
              missionProfileArn='string',
              nextToken='string',
              satelliteArn='string',
              startTime=datetime(2015, 1, 1),
              statusList=[
                  'AVAILABLE'|'AWS_CANCELLED'|'CANCELLED'|'COMPLETED'|'FAILED'|'FAILED_TO_SCHEDULE'|'PASS'
                  |'POSTPASS'|'PREPASS'|'SCHEDULED'|'SCHEDULING',
              ]
          )
        :type endTime: datetime
        :param endTime: **[REQUIRED]**

          End time of a contact.

        :type groundStation: string
        :param groundStation:

          Name of a ground station.

        :type maxResults: integer
        :param maxResults:

          Maximum number of contacts returned.

        :type missionProfileArn: string
        :param missionProfileArn:

          ARN of a mission profile.

        :type nextToken: string
        :param nextToken:

          Next token returned in the request of a previous ``ListContacts`` call. Used to get the next page
          of results.

        :type satelliteArn: string
        :param satelliteArn:

          ARN of a satellite.

        :type startTime: datetime
        :param startTime: **[REQUIRED]**

          Start time of a contact.

        :type statusList: list
        :param statusList: **[REQUIRED]**

          Status of a contact reservation.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'contactList': [
                    {
                        'contactId': 'string',
                        'contactStatus':
                        'AVAILABLE'|'AWS_CANCELLED'|'CANCELLED'|'COMPLETED'|'FAILED'|'FAILED_TO_SCHEDULE'
                        |'PASS'|'POSTPASS'|'PREPASS'|'SCHEDULED'|'SCHEDULING',
                        'endTime': datetime(2015, 1, 1),
                        'errorMessage': 'string',
                        'groundStation': 'string',
                        'maximumElevation': {
                            'unit': 'DEGREE_ANGLE'|'RADIAN',
                            'value': 123.0
                        },
                        'missionProfileArn': 'string',
                        'postPassEndTime': datetime(2015, 1, 1),
                        'prePassStartTime': datetime(2015, 1, 1),
                        'satelliteArn': 'string',
                        'startTime': datetime(2015, 1, 1),
                        'tags': {
                            'string': 'string'
                        }
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_dataflow_endpoint_groups(
        self, maxResults: int = None, nextToken: str = None
    ) -> ClientListDataflowEndpointGroupsResponseTypeDef:
        """
        Returns a list of ``DataflowEndpoint`` groups.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/ListDataflowEndpointGroups>`_

        **Request Syntax**
        ::

          response = client.list_dataflow_endpoint_groups(
              maxResults=123,
              nextToken='string'
          )
        :type maxResults: integer
        :param maxResults:

          Maximum number of dataflow endpoint groups returned.

        :type nextToken: string
        :param nextToken:

          Next token returned in the request of a previous ``ListDataflowEndpointGroups`` call. Used to get
          the next page of results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'dataflowEndpointGroupList': [
                    {
                        'dataflowEndpointGroupArn': 'string',
                        'dataflowEndpointGroupId': 'string'
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_ground_stations(
        self, maxResults: int = None, nextToken: str = None
    ) -> ClientListGroundStationsResponseTypeDef:
        """
        Returns a list of ground stations.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/ListGroundStations>`_

        **Request Syntax**
        ::

          response = client.list_ground_stations(
              maxResults=123,
              nextToken='string'
          )
        :type maxResults: integer
        :param maxResults:

          Maximum number of ground stations returned.

        :type nextToken: string
        :param nextToken:

          Next token that can be supplied in the next call to get the next page of ground stations.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'groundStationList': [
                    {
                        'groundStationId': 'string',
                        'groundStationName': 'string',
                        'region': 'string'
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_mission_profiles(
        self, maxResults: int = None, nextToken: str = None
    ) -> ClientListMissionProfilesResponseTypeDef:
        """
        Returns a list of mission profiles.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/ListMissionProfiles>`_

        **Request Syntax**
        ::

          response = client.list_mission_profiles(
              maxResults=123,
              nextToken='string'
          )
        :type maxResults: integer
        :param maxResults:

          Maximum number of mission profiles returned.

        :type nextToken: string
        :param nextToken:

          Next token returned in the request of a previous ``ListMissionProfiles`` call. Used to get the
          next page of results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'missionProfileList': [
                    {
                        'missionProfileArn': 'string',
                        'missionProfileId': 'string',
                        'name': 'string',
                        'region': 'string'
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_satellites(
        self, maxResults: int = None, nextToken: str = None
    ) -> ClientListSatellitesResponseTypeDef:
        """
        Returns a list of satellites.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/ListSatellites>`_

        **Request Syntax**
        ::

          response = client.list_satellites(
              maxResults=123,
              nextToken='string'
          )
        :type maxResults: integer
        :param maxResults:

          Maximum number of satellites returned.

        :type nextToken: string
        :param nextToken:

          Next token that can be supplied in the next call to get the next page of satellites.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'nextToken': 'string',
                'satellites': [
                    {
                        'noradSatelliteID': 123,
                        'satelliteArn': 'string',
                        'satelliteId': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, resourceArn: str
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags or a specified resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/ListTagsForResource>`_

        **Request Syntax**
        ::

          response = client.list_tags_for_resource(
              resourceArn='string'
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**

          ARN of a resource.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'tags': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **tags** *(dict) --*

              Tags assigned to a resource.

              - *(string) --*

                - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reserve_contact(
        self,
        endTime: datetime,
        groundStation: str,
        missionProfileArn: str,
        satelliteArn: str,
        startTime: datetime,
        tags: Dict[str, str] = None,
    ) -> ClientReserveContactResponseTypeDef:
        """
        Reserves a contact using specified parameters.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/ReserveContact>`_

        **Request Syntax**
        ::

          response = client.reserve_contact(
              endTime=datetime(2015, 1, 1),
              groundStation='string',
              missionProfileArn='string',
              satelliteArn='string',
              startTime=datetime(2015, 1, 1),
              tags={
                  'string': 'string'
              }
          )
        :type endTime: datetime
        :param endTime: **[REQUIRED]**

          End time of a contact.

        :type groundStation: string
        :param groundStation: **[REQUIRED]**

          Name of a ground station.

        :type missionProfileArn: string
        :param missionProfileArn: **[REQUIRED]**

          ARN of a mission profile.

        :type satelliteArn: string
        :param satelliteArn: **[REQUIRED]**

          ARN of a satellite

        :type startTime: datetime
        :param startTime: **[REQUIRED]**

          Start time of a contact.

        :type tags: dict
        :param tags:

          Tags assigned to a contact.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'contactId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **contactId** *(string) --*

              UUID of a contact.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(
        self, resourceArn: str, tags: Dict[str, str] = None
    ) -> Dict[str, Any]:
        """
        Assigns a tag to a resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/TagResource>`_

        **Request Syntax**
        ::

          response = client.tag_resource(
              resourceArn='string',
              tags={
                  'string': 'string'
              }
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**

          ARN of a resource tag.

        :type tags: dict
        :param tags:

          Tags assigned to a resource.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Deassigns a resource tag.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/UntagResource>`_

        **Request Syntax**
        ::

          response = client.untag_resource(
              resourceArn='string',
              tagKeys=[
                  'string',
              ]
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**

          ARN of a resource.

        :type tagKeys: list
        :param tagKeys: **[REQUIRED]**

          Keys of a resource tag.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_config(
        self,
        configData: ClientUpdateConfigconfigDataTypeDef,
        configId: str,
        configType: str,
        name: str,
    ) -> ClientUpdateConfigResponseTypeDef:
        """
        Updates the ``Config`` used when scheduling contacts.

        Updating a ``Config`` will not update the execution parameters for existing future contacts
        scheduled with this ``Config`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/UpdateConfig>`_

        **Request Syntax**
        ::

          response = client.update_config(
              configData={
                  'antennaDownlinkConfig': {
                      'spectrumConfig': {
                          'bandwidth': {
                              'units': 'GHz'|'MHz'|'kHz',
                              'value': 123.0
                          },
                          'centerFrequency': {
                              'units': 'GHz'|'MHz'|'kHz',
                              'value': 123.0
                          },
                          'polarization': 'LEFT_HAND'|'NONE'|'RIGHT_HAND'
                      }
                  },
                  'antennaDownlinkDemodDecodeConfig': {
                      'decodeConfig': {
                          'unvalidatedJSON': 'string'
                      },
                      'demodulationConfig': {
                          'unvalidatedJSON': 'string'
                      },
                      'spectrumConfig': {
                          'bandwidth': {
                              'units': 'GHz'|'MHz'|'kHz',
                              'value': 123.0
                          },
                          'centerFrequency': {
                              'units': 'GHz'|'MHz'|'kHz',
                              'value': 123.0
                          },
                          'polarization': 'LEFT_HAND'|'NONE'|'RIGHT_HAND'
                      }
                  },
                  'antennaUplinkConfig': {
                      'spectrumConfig': {
                          'centerFrequency': {
                              'units': 'GHz'|'MHz'|'kHz',
                              'value': 123.0
                          },
                          'polarization': 'LEFT_HAND'|'NONE'|'RIGHT_HAND'
                      },
                      'targetEirp': {
                          'units': 'dBW',
                          'value': 123.0
                      }
                  },
                  'dataflowEndpointConfig': {
                      'dataflowEndpointName': 'string'
                  },
                  'trackingConfig': {
                      'autotrack': 'PREFERRED'|'REMOVED'|'REQUIRED'
                  },
                  'uplinkEchoConfig': {
                      'antennaUplinkConfigArn': 'string',
                      'enabled': True|False
                  }
              },
              configId='string',
              configType=
                  'antenna-downlink'|'antenna-downlink-demod-decode'|'antenna-uplink'|'dataflow-endpoint'
                  |'tracking'|'uplink-echo',
              name='string'
          )
        :type configData: dict
        :param configData: **[REQUIRED]**

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

        :type configId: string
        :param configId: **[REQUIRED]**

          UUID of a ``Config`` .

        :type configType: string
        :param configType: **[REQUIRED]**

          Type of a ``Config`` .

        :type name: string
        :param name: **[REQUIRED]**

          Name of a ``Config`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'configArn': 'string',
                'configId': 'string',
                'configType':
                'antenna-downlink'|'antenna-downlink-demod-decode'|'antenna-uplink'|'dataflow-endpoint'
                |'tracking'|'uplink-echo'
            }
          **Response Structure**

          - *(dict) --*

            - **configArn** *(string) --*

              ARN of a ``Config`` .

            - **configId** *(string) --*

              UUID of a ``Config`` .

            - **configType** *(string) --*

              Type of a ``Config`` .

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_mission_profile(
        self,
        missionProfileId: str,
        contactPostPassDurationSeconds: int = None,
        contactPrePassDurationSeconds: int = None,
        dataflowEdges: List[List[str]] = None,
        minimumViableContactDurationSeconds: int = None,
        name: str = None,
        trackingConfigArn: str = None,
    ) -> ClientUpdateMissionProfileResponseTypeDef:
        """
        Updates a mission profile.

        Updating a mission profile will not update the execution parameters for existing future contacts.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/UpdateMissionProfile>`_

        **Request Syntax**
        ::

          response = client.update_mission_profile(
              contactPostPassDurationSeconds=123,
              contactPrePassDurationSeconds=123,
              dataflowEdges=[
                  [
                      'string',
                  ],
              ],
              minimumViableContactDurationSeconds=123,
              missionProfileId='string',
              name='string',
              trackingConfigArn='string'
          )
        :type contactPostPassDurationSeconds: integer
        :param contactPostPassDurationSeconds:

          Amount of time after a contact ends that you’d like to receive a CloudWatch event indicating the
          pass has finished.

        :type contactPrePassDurationSeconds: integer
        :param contactPrePassDurationSeconds:

          Amount of time after a contact ends that you’d like to receive a CloudWatch event indicating the
          pass has finished.

        :type dataflowEdges: list
        :param dataflowEdges:

          A list of lists of ARNs. Each list of ARNs is an edge, with a from ``Config`` and a to ``Config``
          .

          - *(list) --*

            - *(string) --*

        :type minimumViableContactDurationSeconds: integer
        :param minimumViableContactDurationSeconds:

          Smallest amount of time in seconds that you’d like to see for an available contact. AWS Ground
          Station will not present you with contacts shorter than this duration.

        :type missionProfileId: string
        :param missionProfileId: **[REQUIRED]**

          ID of a mission profile.

        :type name: string
        :param name:

          Name of a mission profile.

        :type trackingConfigArn: string
        :param trackingConfigArn:

          ARN of a tracking ``Config`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'missionProfileId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **missionProfileId** *(string) --*

              ID of a mission profile.

        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_configs"]
    ) -> paginator_scope.ListConfigsPaginator:
        """
        Get Paginator for `list_configs` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_contacts"]
    ) -> paginator_scope.ListContactsPaginator:
        """
        Get Paginator for `list_contacts` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_dataflow_endpoint_groups"]
    ) -> paginator_scope.ListDataflowEndpointGroupsPaginator:
        """
        Get Paginator for `list_dataflow_endpoint_groups` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_ground_stations"]
    ) -> paginator_scope.ListGroundStationsPaginator:
        """
        Get Paginator for `list_ground_stations` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_mission_profiles"]
    ) -> paginator_scope.ListMissionProfilesPaginator:
        """
        Get Paginator for `list_mission_profiles` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_satellites"]
    ) -> paginator_scope.ListSatellitesPaginator:
        """
        Get Paginator for `list_satellites` operation.
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
    DependencyException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
