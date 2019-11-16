"Main interface for connect Paginators"
from __future__ import annotations

from datetime import datetime
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_connect.type_defs import (
    GetMetricDataPaginateFiltersTypeDef,
    GetMetricDataPaginateHistoricalMetricsTypeDef,
    GetMetricDataPaginatePaginationConfigTypeDef,
    GetMetricDataPaginateResponseTypeDef,
    ListContactFlowsPaginatePaginationConfigTypeDef,
    ListContactFlowsPaginateResponseTypeDef,
    ListHoursOfOperationsPaginatePaginationConfigTypeDef,
    ListHoursOfOperationsPaginateResponseTypeDef,
    ListPhoneNumbersPaginatePaginationConfigTypeDef,
    ListPhoneNumbersPaginateResponseTypeDef,
    ListQueuesPaginatePaginationConfigTypeDef,
    ListQueuesPaginateResponseTypeDef,
    ListRoutingProfilesPaginatePaginationConfigTypeDef,
    ListRoutingProfilesPaginateResponseTypeDef,
    ListSecurityProfilesPaginatePaginationConfigTypeDef,
    ListSecurityProfilesPaginateResponseTypeDef,
    ListUserHierarchyGroupsPaginatePaginationConfigTypeDef,
    ListUserHierarchyGroupsPaginateResponseTypeDef,
    ListUsersPaginatePaginationConfigTypeDef,
    ListUsersPaginateResponseTypeDef,
)


__all__ = (
    "GetMetricDataPaginator",
    "ListContactFlowsPaginator",
    "ListHoursOfOperationsPaginator",
    "ListPhoneNumbersPaginator",
    "ListQueuesPaginator",
    "ListRoutingProfilesPaginator",
    "ListSecurityProfilesPaginator",
    "ListUserHierarchyGroupsPaginator",
    "ListUsersPaginator",
)


class GetMetricDataPaginator(Boto3Paginator):
    """
    Paginator for `get_metric_data`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        InstanceId: str,
        StartTime: datetime,
        EndTime: datetime,
        Filters: GetMetricDataPaginateFiltersTypeDef,
        HistoricalMetrics: List[GetMetricDataPaginateHistoricalMetricsTypeDef],
        Groupings: List[str] = None,
        PaginationConfig: GetMetricDataPaginatePaginationConfigTypeDef = None,
    ) -> GetMetricDataPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Connect.Client.get_metric_data`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/GetMetricData>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              InstanceId='string',
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              Filters={
                  'Queues': [
                      'string',
                  ],
                  'Channels': [
                      'VOICE',
                  ]
              },
              Groupings=[
                  'QUEUE'|'CHANNEL',
              ],
              HistoricalMetrics=[
                  {
                      'Name':
                      'CONTACTS_QUEUED'|'CONTACTS_HANDLED'|'CONTACTS_ABANDONED'|'CONTACTS_CONSULTED'
                      |'CONTACTS_AGENT_HUNG_UP_FIRST'|'CONTACTS_HANDLED_INCOMING'
                      |'CONTACTS_HANDLED_OUTBOUND'|'CONTACTS_HOLD_ABANDONS'|'CONTACTS_TRANSFERRED_IN'
                      |'CONTACTS_TRANSFERRED_OUT'|'CONTACTS_TRANSFERRED_IN_FROM_QUEUE'
                      |'CONTACTS_TRANSFERRED_OUT_FROM_QUEUE'|'CONTACTS_MISSED'|'CALLBACK_CONTACTS_HANDLED'
                      |'API_CONTACTS_HANDLED'|'OCCUPANCY'|'HANDLE_TIME'|'AFTER_CONTACT_WORK_TIME'
                      |'QUEUED_TIME'|'ABANDON_TIME'|'QUEUE_ANSWER_TIME'|'HOLD_TIME'|'INTERACTION_TIME'
                      |'INTERACTION_AND_HOLD_TIME'|'SERVICE_LEVEL',
                      'Threshold': {
                          'Comparison': 'LT',
                          'ThresholdValue': 123.0
                      },
                      'Statistic': 'SUM'|'MAX'|'AVG',
                      'Unit': 'SECONDS'|'COUNT'|'PERCENT'
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

        :type StartTime: datetime
        :param StartTime: **[REQUIRED]**

          The timestamp, in UNIX Epoch time format, at which to start the reporting interval for the
          retrieval of historical metrics data. The time must be specified using a multiple of 5 minutes,
          such as 10:05, 10:10, 10:15.

          The start time cannot be earlier than 24 hours before the time of the request. Historical metrics
          are available only for 24 hours.

        :type EndTime: datetime
        :param EndTime: **[REQUIRED]**

          The timestamp, in UNIX Epoch time format, at which to end the reporting interval for the
          retrieval of historical metrics data. The time must be specified using an interval of 5 minutes,
          such as 11:00, 11:05, 11:10, and must be later than the start time timestamp.

          The time range between the start and end time must be less than 24 hours.

        :type Filters: dict
        :param Filters: **[REQUIRED]**

          The queues, up to 100, or channels, to use to filter the metrics returned. Metric data is
          retrieved only for the resources associated with the queues or channels included in the filter.
          You can include both queue IDs and queue ARNs in the same request. The only supported channel is
          ``VOICE`` .

          - **Queues** *(list) --*

            The queues to use to filter the metrics. You can specify up to 100 queues per request.

            - *(string) --*

          - **Channels** *(list) --*

            The channel to use to filter the metrics.

            - *(string) --*

        :type Groupings: list
        :param Groupings:

          The grouping applied to the metrics returned. For example, when results are grouped by queue, the
          metrics returned are grouped by queue. The values returned apply to the metrics for each queue
          rather than aggregated for all queues.

          The only supported grouping is ``QUEUE`` .

          If no grouping is specified, a summary of metrics for all queues is returned.

          - *(string) --*

        :type HistoricalMetrics: list
        :param HistoricalMetrics: **[REQUIRED]**

          The metrics to retrieve. Specify the name, unit, and statistic for each metric. The following
          historical metrics are available:

            ABANDON_TIME

          Unit: SECONDS

          Statistic: AVG

            AFTER_CONTACT_WORK_TIME

          Unit: SECONDS

          Statistic: AVG

            API_CONTACTS_HANDLED

          Unit: COUNT

          Statistic: SUM

            CALLBACK_CONTACTS_HANDLED

          Unit: COUNT

          Statistic: SUM

            CONTACTS_ABANDONED

          Unit: COUNT

          Statistic: SUM

            CONTACTS_AGENT_HUNG_UP_FIRST

          Unit: COUNT

          Statistic: SUM

            CONTACTS_CONSULTED

          Unit: COUNT

          Statistic: SUM

            CONTACTS_HANDLED

          Unit: COUNT

          Statistic: SUM

            CONTACTS_HANDLED_INCOMING

          Unit: COUNT

          Statistic: SUM

            CONTACTS_HANDLED_OUTBOUND

          Unit: COUNT

          Statistic: SUM

            CONTACTS_HOLD_ABANDONS

          Unit: COUNT

          Statistic: SUM

            CONTACTS_MISSED

          Unit: COUNT

          Statistic: SUM

            CONTACTS_QUEUED

          Unit: COUNT

          Statistic: SUM

            CONTACTS_TRANSFERRED_IN

          Unit: COUNT

          Statistic: SUM

            CONTACTS_TRANSFERRED_IN_FROM_QUEUE

          Unit: COUNT

          Statistic: SUM

            CONTACTS_TRANSFERRED_OUT

          Unit: COUNT

          Statistic: SUM

            CONTACTS_TRANSFERRED_OUT_FROM_QUEUE

          Unit: COUNT

          Statistic: SUM

            HANDLE_TIME

          Unit: SECONDS

          Statistic: AVG

            HOLD_TIME

          Unit: SECONDS

          Statistic: AVG

            INTERACTION_AND_HOLD_TIME

          Unit: SECONDS

          Statistic: AVG

            INTERACTION_TIME

          Unit: SECONDS

          Statistic: AVG

            OCCUPANCY

          Unit: PERCENT

          Statistic: AVG

            QUEUE_ANSWER_TIME

          Unit: SECONDS

          Statistic: AVG

            QUEUED_TIME

          Unit: SECONDS

          Statistic: MAX

            SERVICE_LEVEL

          Unit: PERCENT

          Statistic: AVG

          Threshold: Only "Less than" comparisons are supported, with the following service level
          thresholds: 15, 20, 25, 30, 45, 60, 90, 120, 180, 240, 300, 600

          - *(dict) --*

            Contains information about a historical metric.

            - **Name** *(string) --*

              The name of the metric.

            - **Threshold** *(dict) --*

              The threshold for the metric, used with service level metrics.

              - **Comparison** *(string) --*

                The type of comparison. Only "less than" (LT) comparisons are supported.

              - **ThresholdValue** *(float) --*

                The threshold value to compare.

            - **Statistic** *(string) --*

              The statistic for the metric.

            - **Unit** *(string) --*

              The unit for the metric.

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
                'MetricResults': [
                    {
                        'Dimensions': {
                            'Queue': {
                                'Id': 'string',
                                'Arn': 'string'
                            },
                            'Channel': 'VOICE'
                        },
                        'Collections': [
                            {
                                'Metric': {
                                    'Name':
                                    'CONTACTS_QUEUED'|'CONTACTS_HANDLED'|'CONTACTS_ABANDONED'
                                    |'CONTACTS_CONSULTED'|'CONTACTS_AGENT_HUNG_UP_FIRST'
                                    |'CONTACTS_HANDLED_INCOMING'|'CONTACTS_HANDLED_OUTBOUND'
                                    |'CONTACTS_HOLD_ABANDONS'|'CONTACTS_TRANSFERRED_IN'
                                    |'CONTACTS_TRANSFERRED_OUT'|'CONTACTS_TRANSFERRED_IN_FROM_QUEUE'
                                    |'CONTACTS_TRANSFERRED_OUT_FROM_QUEUE'|'CONTACTS_MISSED'
                                    |'CALLBACK_CONTACTS_HANDLED'|'API_CONTACTS_HANDLED'|'OCCUPANCY'
                                    |'HANDLE_TIME'|'AFTER_CONTACT_WORK_TIME'|'QUEUED_TIME'|'ABANDON_TIME'
                                    |'QUEUE_ANSWER_TIME'|'HOLD_TIME'|'INTERACTION_TIME'
                                    |'INTERACTION_AND_HOLD_TIME'|'SERVICE_LEVEL',
                                    'Threshold': {
                                        'Comparison': 'LT',
                                        'ThresholdValue': 123.0
                                    },
                                    'Statistic': 'SUM'|'MAX'|'AVG',
                                    'Unit': 'SECONDS'|'COUNT'|'PERCENT'
                                },
                                'Value': 123.0
                            },
                        ]
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **MetricResults** *(list) --*

              Information about the historical metrics.

              If no grouping is specified, a summary of metric data is returned.

              - *(dict) --*

                Contains information about the historical metrics retrieved.

                - **Dimensions** *(dict) --*

                  The dimension for the metrics.

                  - **Queue** *(dict) --*

                    Information about the queue for which metrics are returned.

                    - **Id** *(string) --*

                      The identifier of the queue.

                    - **Arn** *(string) --*

                      The Amazon Resource Name (ARN) of the queue.

                  - **Channel** *(string) --*

                    The channel used for grouping and filters.

                - **Collections** *(list) --*

                  The set of metrics.

                  - *(dict) --*

                    Contains the data for a historical metric.

                    - **Metric** *(dict) --*

                      Information about the metric.

                      - **Name** *(string) --*

                        The name of the metric.

                      - **Threshold** *(dict) --*

                        The threshold for the metric, used with service level metrics.

                        - **Comparison** *(string) --*

                          The type of comparison. Only "less than" (LT) comparisons are supported.

                        - **ThresholdValue** *(float) --*

                          The threshold value to compare.

                      - **Statistic** *(string) --*

                        The statistic for the metric.

                      - **Unit** *(string) --*

                        The unit for the metric.

                    - **Value** *(float) --*

                      The value of the metric.

        """


class ListContactFlowsPaginator(Boto3Paginator):
    """
    Paginator for `list_contact_flows`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        InstanceId: str,
        ContactFlowTypes: List[str] = None,
        PaginationConfig: ListContactFlowsPaginatePaginationConfigTypeDef = None,
    ) -> ListContactFlowsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Connect.Client.list_contact_flows`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/ListContactFlows>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              InstanceId='string',
              ContactFlowTypes=[
                  'CONTACT_FLOW'|'CUSTOMER_QUEUE'|'CUSTOMER_HOLD'|'CUSTOMER_WHISPER'|'AGENT_HOLD'
                  |'AGENT_WHISPER'|'OUTBOUND_WHISPER'|'AGENT_TRANSFER'|'QUEUE_TRANSFER',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

        :type ContactFlowTypes: list
        :param ContactFlowTypes:

          The type of contact flow.

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
                'ContactFlowSummaryList': [
                    {
                        'Id': 'string',
                        'Arn': 'string',
                        'Name': 'string',
                        'ContactFlowType':
                        'CONTACT_FLOW'|'CUSTOMER_QUEUE'|'CUSTOMER_HOLD'|'CUSTOMER_WHISPER'|'AGENT_HOLD'
                        |'AGENT_WHISPER'|'OUTBOUND_WHISPER'|'AGENT_TRANSFER'|'QUEUE_TRANSFER'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **ContactFlowSummaryList** *(list) --*

              Information about the contact flows.

              - *(dict) --*

                Contains summary information about a contact flow.

                - **Id** *(string) --*

                  The identifier of the contact flow.

                - **Arn** *(string) --*

                  The Amazon Resource Name (ARN) of the contact flow.

                - **Name** *(string) --*

                  The name of the contact flow.

                - **ContactFlowType** *(string) --*

                  The type of contact flow.

        """


class ListHoursOfOperationsPaginator(Boto3Paginator):
    """
    Paginator for `list_hours_of_operations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        InstanceId: str,
        PaginationConfig: ListHoursOfOperationsPaginatePaginationConfigTypeDef = None,
    ) -> ListHoursOfOperationsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Connect.Client.list_hours_of_operations`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/ListHoursOfOperations>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              InstanceId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

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
                'HoursOfOperationSummaryList': [
                    {
                        'Id': 'string',
                        'Arn': 'string',
                        'Name': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **HoursOfOperationSummaryList** *(list) --*

              Information about the hours of operation.

              - *(dict) --*

                Contains summary information about hours of operation for a contact center.

                - **Id** *(string) --*

                  The identifier of the hours of operation.

                - **Arn** *(string) --*

                  The Amazon Resource Name (ARN) of the hours of operation.

                - **Name** *(string) --*

                  The name of the hours of operation.

        """


class ListPhoneNumbersPaginator(Boto3Paginator):
    """
    Paginator for `list_phone_numbers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        InstanceId: str,
        PhoneNumberTypes: List[str] = None,
        PhoneNumberCountryCodes: List[str] = None,
        PaginationConfig: ListPhoneNumbersPaginatePaginationConfigTypeDef = None,
    ) -> ListPhoneNumbersPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Connect.Client.list_phone_numbers`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/ListPhoneNumbers>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              InstanceId='string',
              PhoneNumberTypes=[
                  'TOLL_FREE'|'DID',
              ],
              PhoneNumberCountryCodes=[
                  'AF'|'AL'|'DZ'|'AS'|'AD'|'AO'|'AI'|'AQ'|'AG'|'AR'|'AM'|'AW'|'AU'|'AT'|'AZ'|'BS'|'BH'|'BD'
                  |'BB'|'BY'|'BE'|'BZ'|'BJ'|'BM'|'BT'|'BO'|'BA'|'BW'|'BR'|'IO'|'VG'|'BN'|'BG'|'BF'|'BI'
                  |'KH'|'CM'|'CA'|'CV'|'KY'|'CF'|'TD'|'CL'|'CN'|'CX'|'CC'|'CO'|'KM'|'CK'|'CR'|'HR'|'CU'
                  |'CW'|'CY'|'CZ'|'CD'|'DK'|'DJ'|'DM'|'DO'|'TL'|'EC'|'EG'|'SV'|'GQ'|'ER'|'EE'|'ET'|'FK'
                  |'FO'|'FJ'|'FI'|'FR'|'PF'|'GA'|'GM'|'GE'|'DE'|'GH'|'GI'|'GR'|'GL'|'GD'|'GU'|'GT'|'GG'
                  |'GN'|'GW'|'GY'|'HT'|'HN'|'HK'|'HU'|'IS'|'IN'|'ID'|'IR'|'IQ'|'IE'|'IM'|'IL'|'IT'|'CI'
                  |'JM'|'JP'|'JE'|'JO'|'KZ'|'KE'|'KI'|'KW'|'KG'|'LA'|'LV'|'LB'|'LS'|'LR'|'LY'|'LI'|'LT'
                  |'LU'|'MO'|'MK'|'MG'|'MW'|'MY'|'MV'|'ML'|'MT'|'MH'|'MR'|'MU'|'YT'|'MX'|'FM'|'MD'|'MC'
                  |'MN'|'ME'|'MS'|'MA'|'MZ'|'MM'|'NA'|'NR'|'NP'|'NL'|'AN'|'NC'|'NZ'|'NI'|'NE'|'NG'|'NU'
                  |'KP'|'MP'|'NO'|'OM'|'PK'|'PW'|'PA'|'PG'|'PY'|'PE'|'PH'|'PN'|'PL'|'PT'|'PR'|'QA'|'CG'
                  |'RE'|'RO'|'RU'|'RW'|'BL'|'SH'|'KN'|'LC'|'MF'|'PM'|'VC'|'WS'|'SM'|'ST'|'SA'|'SN'|'RS'
                  |'SC'|'SL'|'SG'|'SX'|'SK'|'SI'|'SB'|'SO'|'ZA'|'KR'|'ES'|'LK'|'SD'|'SR'|'SJ'|'SZ'|'SE'
                  |'CH'|'SY'|'TW'|'TJ'|'TZ'|'TH'|'TG'|'TK'|'TO'|'TT'|'TN'|'TR'|'TM'|'TC'|'TV'|'VI'|'UG'
                  |'UA'|'AE'|'GB'|'US'|'UY'|'UZ'|'VU'|'VA'|'VE'|'VN'|'WF'|'EH'|'YE'|'ZM'|'ZW',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

        :type PhoneNumberTypes: list
        :param PhoneNumberTypes:

          The type of phone number.

          - *(string) --*

        :type PhoneNumberCountryCodes: list
        :param PhoneNumberCountryCodes:

          The ISO country code.

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
                'PhoneNumberSummaryList': [
                    {
                        'Id': 'string',
                        'Arn': 'string',
                        'PhoneNumber': 'string',
                        'PhoneNumberType': 'TOLL_FREE'|'DID',
                        'PhoneNumberCountryCode':
                        'AF'|'AL'|'DZ'|'AS'|'AD'|'AO'|'AI'|'AQ'|'AG'|'AR'|'AM'|'AW'|'AU'|'AT'|'AZ'|'BS'
                        |'BH'|'BD'|'BB'|'BY'|'BE'|'BZ'|'BJ'|'BM'|'BT'|'BO'|'BA'|'BW'|'BR'|'IO'|'VG'|'BN'
                        |'BG'|'BF'|'BI'|'KH'|'CM'|'CA'|'CV'|'KY'|'CF'|'TD'|'CL'|'CN'|'CX'|'CC'|'CO'|'KM'
                        |'CK'|'CR'|'HR'|'CU'|'CW'|'CY'|'CZ'|'CD'|'DK'|'DJ'|'DM'|'DO'|'TL'|'EC'|'EG'|'SV'
                        |'GQ'|'ER'|'EE'|'ET'|'FK'|'FO'|'FJ'|'FI'|'FR'|'PF'|'GA'|'GM'|'GE'|'DE'|'GH'|'GI'
                        |'GR'|'GL'|'GD'|'GU'|'GT'|'GG'|'GN'|'GW'|'GY'|'HT'|'HN'|'HK'|'HU'|'IS'|'IN'|'ID'
                        |'IR'|'IQ'|'IE'|'IM'|'IL'|'IT'|'CI'|'JM'|'JP'|'JE'|'JO'|'KZ'|'KE'|'KI'|'KW'|'KG'
                        |'LA'|'LV'|'LB'|'LS'|'LR'|'LY'|'LI'|'LT'|'LU'|'MO'|'MK'|'MG'|'MW'|'MY'|'MV'|'ML'
                        |'MT'|'MH'|'MR'|'MU'|'YT'|'MX'|'FM'|'MD'|'MC'|'MN'|'ME'|'MS'|'MA'|'MZ'|'MM'|'NA'
                        |'NR'|'NP'|'NL'|'AN'|'NC'|'NZ'|'NI'|'NE'|'NG'|'NU'|'KP'|'MP'|'NO'|'OM'|'PK'|'PW'
                        |'PA'|'PG'|'PY'|'PE'|'PH'|'PN'|'PL'|'PT'|'PR'|'QA'|'CG'|'RE'|'RO'|'RU'|'RW'|'BL'
                        |'SH'|'KN'|'LC'|'MF'|'PM'|'VC'|'WS'|'SM'|'ST'|'SA'|'SN'|'RS'|'SC'|'SL'|'SG'|'SX'
                        |'SK'|'SI'|'SB'|'SO'|'ZA'|'KR'|'ES'|'LK'|'SD'|'SR'|'SJ'|'SZ'|'SE'|'CH'|'SY'|'TW'
                        |'TJ'|'TZ'|'TH'|'TG'|'TK'|'TO'|'TT'|'TN'|'TR'|'TM'|'TC'|'TV'|'VI'|'UG'|'UA'|'AE'
                        |'GB'|'US'|'UY'|'UZ'|'VU'|'VA'|'VE'|'VN'|'WF'|'EH'|'YE'|'ZM'|'ZW'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **PhoneNumberSummaryList** *(list) --*

              Information about the phone numbers.

              - *(dict) --*

                Contains summary information about a phone number for a contact center.

                - **Id** *(string) --*

                  The identifier of the phone number.

                - **Arn** *(string) --*

                  The Amazon Resource Name (ARN) of the phone number.

                - **PhoneNumber** *(string) --*

                  The phone number.

                - **PhoneNumberType** *(string) --*

                  The type of phone number.

                - **PhoneNumberCountryCode** *(string) --*

                  The ISO country code.

        """


class ListQueuesPaginator(Boto3Paginator):
    """
    Paginator for `list_queues`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        InstanceId: str,
        QueueTypes: List[str] = None,
        PaginationConfig: ListQueuesPaginatePaginationConfigTypeDef = None,
    ) -> ListQueuesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Connect.Client.list_queues`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/ListQueues>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              InstanceId='string',
              QueueTypes=[
                  'STANDARD'|'AGENT',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

        :type QueueTypes: list
        :param QueueTypes:

          The type of queue.

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
                'QueueSummaryList': [
                    {
                        'Id': 'string',
                        'Arn': 'string',
                        'Name': 'string',
                        'QueueType': 'STANDARD'|'AGENT'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **QueueSummaryList** *(list) --*

              Information about the queues.

              - *(dict) --*

                Contains summary information about a queue.

                - **Id** *(string) --*

                  The identifier of the queue.

                - **Arn** *(string) --*

                  The Amazon Resource Name (ARN) of the queue.

                - **Name** *(string) --*

                  The name of the queue.

                - **QueueType** *(string) --*

                  The type of queue.

        """


class ListRoutingProfilesPaginator(Boto3Paginator):
    """
    Paginator for `list_routing_profiles`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        InstanceId: str,
        PaginationConfig: ListRoutingProfilesPaginatePaginationConfigTypeDef = None,
    ) -> ListRoutingProfilesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Connect.Client.list_routing_profiles`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/ListRoutingProfiles>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              InstanceId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

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
                'RoutingProfileSummaryList': [
                    {
                        'Id': 'string',
                        'Arn': 'string',
                        'Name': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **RoutingProfileSummaryList** *(list) --*

              Information about the routing profiles.

              - *(dict) --*

                Contains summary information about a routing profile.

                - **Id** *(string) --*

                  The identifier of the routing profile.

                - **Arn** *(string) --*

                  The Amazon Resource Name (ARN) of the routing profile.

                - **Name** *(string) --*

                  The name of the routing profile.

        """


class ListSecurityProfilesPaginator(Boto3Paginator):
    """
    Paginator for `list_security_profiles`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        InstanceId: str,
        PaginationConfig: ListSecurityProfilesPaginatePaginationConfigTypeDef = None,
    ) -> ListSecurityProfilesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Connect.Client.list_security_profiles`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/ListSecurityProfiles>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              InstanceId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

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
                'SecurityProfileSummaryList': [
                    {
                        'Id': 'string',
                        'Arn': 'string',
                        'Name': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **SecurityProfileSummaryList** *(list) --*

              Information about the security profiles.

              - *(dict) --*

                Contains information about a security profile.

                - **Id** *(string) --*

                  The identifier of the security profile.

                - **Arn** *(string) --*

                  The Amazon Resource Name (ARN) of the security profile.

                - **Name** *(string) --*

                  The name of the security profile.

        """


class ListUserHierarchyGroupsPaginator(Boto3Paginator):
    """
    Paginator for `list_user_hierarchy_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        InstanceId: str,
        PaginationConfig: ListUserHierarchyGroupsPaginatePaginationConfigTypeDef = None,
    ) -> ListUserHierarchyGroupsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Connect.Client.list_user_hierarchy_groups`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/ListUserHierarchyGroups>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              InstanceId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

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
                'UserHierarchyGroupSummaryList': [
                    {
                        'Id': 'string',
                        'Arn': 'string',
                        'Name': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **UserHierarchyGroupSummaryList** *(list) --*

              Information about the hierarchy groups.

              - *(dict) --*

                Contains summary information about a hierarchy group.

                - **Id** *(string) --*

                  The identifier of the hierarchy group.

                - **Arn** *(string) --*

                  The Amazon Resource Name (ARN) of the hierarchy group.

                - **Name** *(string) --*

                  The name of the hierarchy group.

        """


class ListUsersPaginator(Boto3Paginator):
    """
    Paginator for `list_users`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        InstanceId: str,
        PaginationConfig: ListUsersPaginatePaginationConfigTypeDef = None,
    ) -> ListUsersPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Connect.Client.list_users`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/ListUsers>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              InstanceId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

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
                'UserSummaryList': [
                    {
                        'Id': 'string',
                        'Arn': 'string',
                        'Username': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **UserSummaryList** *(list) --*

              Information about the users.

              - *(dict) --*

                Contains summary information about a user.

                - **Id** *(string) --*

                  The identifier of the user account.

                - **Arn** *(string) --*

                  The Amazon Resource Name (ARN) of the user account.

                - **Username** *(string) --*

                  The Amazon Connect user name of the user account.

        """
