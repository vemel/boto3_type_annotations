"Main interface for groundstation Paginators"
from __future__ import annotations

from datetime import datetime
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_groundstation.type_defs import (
    ListConfigsPaginatePaginationConfigTypeDef,
    ListConfigsPaginateResponseTypeDef,
    ListContactsPaginatePaginationConfigTypeDef,
    ListContactsPaginateResponseTypeDef,
    ListDataflowEndpointGroupsPaginatePaginationConfigTypeDef,
    ListDataflowEndpointGroupsPaginateResponseTypeDef,
    ListGroundStationsPaginatePaginationConfigTypeDef,
    ListGroundStationsPaginateResponseTypeDef,
    ListMissionProfilesPaginatePaginationConfigTypeDef,
    ListMissionProfilesPaginateResponseTypeDef,
    ListSatellitesPaginatePaginationConfigTypeDef,
    ListSatellitesPaginateResponseTypeDef,
)


__all__ = (
    "ListConfigsPaginator",
    "ListContactsPaginator",
    "ListDataflowEndpointGroupsPaginator",
    "ListGroundStationsPaginator",
    "ListMissionProfilesPaginator",
    "ListSatellitesPaginator",
)


class ListConfigsPaginator(Boto3Paginator):
    """
    Paginator for `list_configs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListConfigsPaginatePaginationConfigTypeDef = None
    ) -> ListConfigsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`GroundStation.Client.list_configs`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/ListConfigs>`_

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
                'NextToken': 'string'
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

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class ListContactsPaginator(Boto3Paginator):
    """
    Paginator for `list_contacts`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        endTime: datetime,
        startTime: datetime,
        statusList: List[str],
        groundStation: str = None,
        missionProfileArn: str = None,
        satelliteArn: str = None,
        PaginationConfig: ListContactsPaginatePaginationConfigTypeDef = None,
    ) -> ListContactsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`GroundStation.Client.list_contacts`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/ListContacts>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              endTime=datetime(2015, 1, 1),
              groundStation='string',
              missionProfileArn='string',
              satelliteArn='string',
              startTime=datetime(2015, 1, 1),
              statusList=[
                  'AVAILABLE'|'AWS_CANCELLED'|'CANCELLED'|'COMPLETED'|'FAILED'|'FAILED_TO_SCHEDULE'|'PASS'
                  |'POSTPASS'|'PREPASS'|'SCHEDULED'|'SCHEDULING',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type endTime: datetime
        :param endTime: **[REQUIRED]**

          End time of a contact.

        :type groundStation: string
        :param groundStation:

          Name of a ground station.

        :type missionProfileArn: string
        :param missionProfileArn:

          ARN of a mission profile.

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
                'NextToken': 'string'
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

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class ListDataflowEndpointGroupsPaginator(Boto3Paginator):
    """
    Paginator for `list_dataflow_endpoint_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PaginationConfig: ListDataflowEndpointGroupsPaginatePaginationConfigTypeDef = None,
    ) -> ListDataflowEndpointGroupsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`GroundStation.Client.list_dataflow_endpoint_groups`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/ListDataflowEndpointGroups>`_

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
                'dataflowEndpointGroupList': [
                    {
                        'dataflowEndpointGroupArn': 'string',
                        'dataflowEndpointGroupId': 'string'
                    },
                ],
                'NextToken': 'string'
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

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class ListGroundStationsPaginator(Boto3Paginator):
    """
    Paginator for `list_ground_stations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListGroundStationsPaginatePaginationConfigTypeDef = None
    ) -> ListGroundStationsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`GroundStation.Client.list_ground_stations`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/ListGroundStations>`_

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
                'groundStationList': [
                    {
                        'groundStationId': 'string',
                        'groundStationName': 'string',
                        'region': 'string'
                    },
                ],
                'NextToken': 'string'
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

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class ListMissionProfilesPaginator(Boto3Paginator):
    """
    Paginator for `list_mission_profiles`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PaginationConfig: ListMissionProfilesPaginatePaginationConfigTypeDef = None,
    ) -> ListMissionProfilesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`GroundStation.Client.list_mission_profiles`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/ListMissionProfiles>`_

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
                'missionProfileList': [
                    {
                        'missionProfileArn': 'string',
                        'missionProfileId': 'string',
                        'name': 'string',
                        'region': 'string'
                    },
                ],
                'NextToken': 'string'
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

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class ListSatellitesPaginator(Boto3Paginator):
    """
    Paginator for `list_satellites`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListSatellitesPaginatePaginationConfigTypeDef = None
    ) -> ListSatellitesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`GroundStation.Client.list_satellites`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/ListSatellites>`_

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
                'satellites': [
                    {
                        'noradSatelliteID': 123,
                        'satelliteArn': 'string',
                        'satelliteId': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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
