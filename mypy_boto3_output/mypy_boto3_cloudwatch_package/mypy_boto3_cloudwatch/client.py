"Main interface for cloudwatch Client"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List
from typing_extensions import Literal, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from botocore.waiter import Waiter as Boto3Waiter

# pylint: disable=import-self
import mypy_boto3_cloudwatch.client as client_scope

# pylint: disable=import-self
import mypy_boto3_cloudwatch.paginator as paginator_scope
from mypy_boto3_cloudwatch.type_defs import (
    ClientDeleteAnomalyDetectorDimensionsTypeDef,
    ClientDescribeAlarmHistoryResponseTypeDef,
    ClientDescribeAlarmsForMetricDimensionsTypeDef,
    ClientDescribeAlarmsForMetricResponseTypeDef,
    ClientDescribeAlarmsResponseTypeDef,
    ClientDescribeAnomalyDetectorsDimensionsTypeDef,
    ClientDescribeAnomalyDetectorsResponseTypeDef,
    ClientGetDashboardResponseTypeDef,
    ClientGetMetricDataMetricDataQueriesTypeDef,
    ClientGetMetricDataResponseTypeDef,
    ClientGetMetricStatisticsDimensionsTypeDef,
    ClientGetMetricStatisticsResponseTypeDef,
    ClientGetMetricWidgetImageResponseTypeDef,
    ClientListDashboardsResponseTypeDef,
    ClientListMetricsDimensionsTypeDef,
    ClientListMetricsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientPutAnomalyDetectorConfigurationTypeDef,
    ClientPutAnomalyDetectorDimensionsTypeDef,
    ClientPutDashboardResponseTypeDef,
    ClientPutMetricAlarmDimensionsTypeDef,
    ClientPutMetricAlarmMetricsTypeDef,
    ClientPutMetricAlarmTagsTypeDef,
    ClientPutMetricDataMetricDataTypeDef,
    ClientTagResourceTagsTypeDef,
)

# pylint: disable=import-self
import mypy_boto3_cloudwatch.waiter as waiter_scope


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
    def delete_alarms(self, AlarmNames: List[str]) -> None:
        """
        Deletes the specified alarms. You can delete up to 50 alarms in one operation. In the event of an
        error, no alarms are deleted.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DeleteAlarms>`_

        **Request Syntax**
        ::

          response = client.delete_alarms(
              AlarmNames=[
                  'string',
              ]
          )
        :type AlarmNames: list
        :param AlarmNames: **[REQUIRED]**

          The alarms to be deleted.

          - *(string) --*

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_anomaly_detector(
        self,
        Namespace: str,
        MetricName: str,
        Stat: str,
        Dimensions: List[ClientDeleteAnomalyDetectorDimensionsTypeDef] = None,
    ) -> Dict[str, Any]:
        """
        Deletes the specified anomaly detection model from your account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DeleteAnomalyDetector>`_

        **Request Syntax**
        ::

          response = client.delete_anomaly_detector(
              Namespace='string',
              MetricName='string',
              Dimensions=[
                  {
                      'Name': 'string',
                      'Value': 'string'
                  },
              ],
              Stat='string'
          )
        :type Namespace: string
        :param Namespace: **[REQUIRED]**

          The namespace associated with the anomaly detection model to delete.

        :type MetricName: string
        :param MetricName: **[REQUIRED]**

          The metric name associated with the anomaly detection model to delete.

        :type Dimensions: list
        :param Dimensions:

          The metric dimensions associated with the anomaly detection model to delete.

          - *(dict) --*

            Expands the identity of a metric.

            - **Name** *(string) --* **[REQUIRED]**

              The name of the dimension.

            - **Value** *(string) --* **[REQUIRED]**

              The value representing the dimension measurement.

        :type Stat: string
        :param Stat: **[REQUIRED]**

          The statistic associated with the anomaly detection model to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_dashboards(self, DashboardNames: List[str]) -> Dict[str, Any]:
        """
        Deletes all dashboards that you specify. You may specify up to 100 dashboards to delete. If there
        is an error during this call, no dashboards are deleted.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DeleteDashboards>`_

        **Request Syntax**
        ::

          response = client.delete_dashboards(
              DashboardNames=[
                  'string',
              ]
          )
        :type DashboardNames: list
        :param DashboardNames: **[REQUIRED]**

          The dashboards to be deleted. This parameter is required.

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
    def describe_alarm_history(
        self,
        AlarmName: str = None,
        HistoryItemType: str = None,
        StartDate: datetime = None,
        EndDate: datetime = None,
        MaxRecords: int = None,
        NextToken: str = None,
    ) -> ClientDescribeAlarmHistoryResponseTypeDef:
        """
        Retrieves the history for the specified alarm. You can filter the results by date range or item
        type. If an alarm name is not specified, the histories for all alarms are returned.

        CloudWatch retains the history of an alarm even if you delete the alarm.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarmHistory>`_

        **Request Syntax**
        ::

          response = client.describe_alarm_history(
              AlarmName='string',
              HistoryItemType='ConfigurationUpdate'|'StateUpdate'|'Action',
              StartDate=datetime(2015, 1, 1),
              EndDate=datetime(2015, 1, 1),
              MaxRecords=123,
              NextToken='string'
          )
        :type AlarmName: string
        :param AlarmName:

          The name of the alarm.

        :type HistoryItemType: string
        :param HistoryItemType:

          The type of alarm histories to retrieve.

        :type StartDate: datetime
        :param StartDate:

          The starting date to retrieve alarm history.

        :type EndDate: datetime
        :param EndDate:

          The ending date to retrieve alarm history.

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of alarm history records to retrieve.

        :type NextToken: string
        :param NextToken:

          The token returned by a previous call to indicate that there is more data available.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AlarmHistoryItems': [
                    {
                        'AlarmName': 'string',
                        'Timestamp': datetime(2015, 1, 1),
                        'HistoryItemType': 'ConfigurationUpdate'|'StateUpdate'|'Action',
                        'HistorySummary': 'string',
                        'HistoryData': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **AlarmHistoryItems** *(list) --*

              The alarm histories, in JSON format.

              - *(dict) --*

                Represents the history of a specific alarm.

                - **AlarmName** *(string) --*

                  The descriptive name for the alarm.

                - **Timestamp** *(datetime) --*

                  The time stamp for the alarm history item.

                - **HistoryItemType** *(string) --*

                  The type of alarm history item.

                - **HistorySummary** *(string) --*

                  A summary of the alarm history, in text format.

                - **HistoryData** *(string) --*

                  Data about the alarm, in JSON format.

            - **NextToken** *(string) --*

              The token that marks the start of the next batch of returned results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_alarms(
        self,
        AlarmNames: List[str] = None,
        AlarmNamePrefix: str = None,
        StateValue: str = None,
        ActionPrefix: str = None,
        MaxRecords: int = None,
        NextToken: str = None,
    ) -> ClientDescribeAlarmsResponseTypeDef:
        """
        Retrieves the specified alarms. If no alarms are specified, all alarms are returned. Alarms can be
        retrieved by using only a prefix for the alarm name, the alarm state, or a prefix for any action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarms>`_

        **Request Syntax**
        ::

          response = client.describe_alarms(
              AlarmNames=[
                  'string',
              ],
              AlarmNamePrefix='string',
              StateValue='OK'|'ALARM'|'INSUFFICIENT_DATA',
              ActionPrefix='string',
              MaxRecords=123,
              NextToken='string'
          )
        :type AlarmNames: list
        :param AlarmNames:

          The names of the alarms.

          - *(string) --*

        :type AlarmNamePrefix: string
        :param AlarmNamePrefix:

          The alarm name prefix. If this parameter is specified, you cannot specify ``AlarmNames`` .

        :type StateValue: string
        :param StateValue:

          The state value to be used in matching alarms.

        :type ActionPrefix: string
        :param ActionPrefix:

          The action name prefix.

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of alarm descriptions to retrieve.

        :type NextToken: string
        :param NextToken:

          The token returned by a previous call to indicate that there is more data available.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'MetricAlarms': [
                    {
                        'AlarmName': 'string',
                        'AlarmArn': 'string',
                        'AlarmDescription': 'string',
                        'AlarmConfigurationUpdatedTimestamp': datetime(2015, 1, 1),
                        'ActionsEnabled': True|False,
                        'OKActions': [
                            'string',
                        ],
                        'AlarmActions': [
                            'string',
                        ],
                        'InsufficientDataActions': [
                            'string',
                        ],
                        'StateValue': 'OK'|'ALARM'|'INSUFFICIENT_DATA',
                        'StateReason': 'string',
                        'StateReasonData': 'string',
                        'StateUpdatedTimestamp': datetime(2015, 1, 1),
                        'MetricName': 'string',
                        'Namespace': 'string',
                        'Statistic': 'SampleCount'|'Average'|'Sum'|'Minimum'|'Maximum',
                        'ExtendedStatistic': 'string',
                        'Dimensions': [
                            {
                                'Name': 'string',
                                'Value': 'string'
                            },
                        ],
                        'Period': 123,
                        'Unit':
                        'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'
                        |'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'
                        |'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'
                        |'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'
                        |'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
                        'EvaluationPeriods': 123,
                        'DatapointsToAlarm': 123,
                        'Threshold': 123.0,
                        'ComparisonOperator':
                        'GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'
                        |'LessThanOrEqualToThreshold'|'LessThanLowerOrGreaterThanUpperThreshold'
                        |'LessThanLowerThreshold'|'GreaterThanUpperThreshold',
                        'TreatMissingData': 'string',
                        'EvaluateLowSampleCountPercentile': 'string',
                        'Metrics': [
                            {
                                'Id': 'string',
                                'MetricStat': {
                                    'Metric': {
                                        'Namespace': 'string',
                                        'MetricName': 'string',
                                        'Dimensions': [
                                            {
                                                'Name': 'string',
                                                'Value': 'string'
                                            },
                                        ]
                                    },
                                    'Period': 123,
                                    'Stat': 'string',
                                    'Unit':
                                    'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'
                                    |'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'
                                    |'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'
                                    |'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'
                                    |'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'
                                    |'Terabits/Second'|'Count/Second'|'None'
                                },
                                'Expression': 'string',
                                'Label': 'string',
                                'ReturnData': True|False,
                                'Period': 123
                            },
                        ],
                        'ThresholdMetricId': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **MetricAlarms** *(list) --*

              The information for the specified alarms.

              - *(dict) --*

                Represents an alarm.

                - **AlarmName** *(string) --*

                  The name of the alarm.

                - **AlarmArn** *(string) --*

                  The Amazon Resource Name (ARN) of the alarm.

                - **AlarmDescription** *(string) --*

                  The description of the alarm.

                - **AlarmConfigurationUpdatedTimestamp** *(datetime) --*

                  The time stamp of the last update to the alarm configuration.

                - **ActionsEnabled** *(boolean) --*

                  Indicates whether actions should be executed during any changes to the alarm state.

                - **OKActions** *(list) --*

                  The actions to execute when this alarm transitions to the ``OK`` state from any other
                  state. Each action is specified as an Amazon Resource Name (ARN).

                  - *(string) --*

                - **AlarmActions** *(list) --*

                  The actions to execute when this alarm transitions to the ``ALARM`` state from any other
                  state. Each action is specified as an Amazon Resource Name (ARN).

                  - *(string) --*

                - **InsufficientDataActions** *(list) --*

                  The actions to execute when this alarm transitions to the ``INSUFFICIENT_DATA`` state
                  from any other state. Each action is specified as an Amazon Resource Name (ARN).

                  - *(string) --*

                - **StateValue** *(string) --*

                  The state value for the alarm.

                - **StateReason** *(string) --*

                  An explanation for the alarm state, in text format.

                - **StateReasonData** *(string) --*

                  An explanation for the alarm state, in JSON format.

                - **StateUpdatedTimestamp** *(datetime) --*

                  The time stamp of the last update to the alarm state.

                - **MetricName** *(string) --*

                  The name of the metric associated with the alarm, if this is an alarm based on a single
                  metric.

                - **Namespace** *(string) --*

                  The namespace of the metric associated with the alarm.

                - **Statistic** *(string) --*

                  The statistic for the metric associated with the alarm, other than percentile. For
                  percentile statistics, use ``ExtendedStatistic`` .

                - **ExtendedStatistic** *(string) --*

                  The percentile statistic for the metric associated with the alarm. Specify a value
                  between p0.0 and p100.

                - **Dimensions** *(list) --*

                  The dimensions for the metric associated with the alarm.

                  - *(dict) --*

                    Expands the identity of a metric.

                    - **Name** *(string) --*

                      The name of the dimension.

                    - **Value** *(string) --*

                      The value representing the dimension measurement.

                - **Period** *(integer) --*

                  The period, in seconds, over which the statistic is applied.

                - **Unit** *(string) --*

                  The unit of the metric associated with the alarm.

                - **EvaluationPeriods** *(integer) --*

                  The number of periods over which data is compared to the specified threshold.

                - **DatapointsToAlarm** *(integer) --*

                  The number of datapoints that must be breaching to trigger the alarm.

                - **Threshold** *(float) --*

                  The value to compare with the specified statistic.

                - **ComparisonOperator** *(string) --*

                  The arithmetic operation to use when comparing the specified statistic and threshold. The
                  specified statistic value is used as the first operand.

                - **TreatMissingData** *(string) --*

                  Sets how this alarm is to handle missing data points. If this parameter is omitted, the
                  default behavior of ``missing`` is used.

                - **EvaluateLowSampleCountPercentile** *(string) --*

                  Used only for alarms based on percentiles. If ``ignore`` , the alarm state does not
                  change during periods with too few data points to be statistically significant. If
                  ``evaluate`` or this parameter is not used, the alarm is always evaluated and possibly
                  changes state no matter how many data points are available.

                - **Metrics** *(list) --*

                  An array of MetricDataQuery structures, used in an alarm based on a metric math
                  expression. Each structure either retrieves a metric or performs a math expression. One
                  item in the Metrics array is the math expression that the alarm watches. This expression
                  by designated by having ``ReturnValue`` set to true.

                  - *(dict) --*

                    This structure is used in both ``GetMetricData`` and ``PutMetricAlarm`` . The supported
                    use of this structure is different for those two operations.

                    When used in ``GetMetricData`` , it indicates the metric data to return, and whether
                    this call is just retrieving a batch set of data for one metric, or is performing a
                    math expression on metric data. A single ``GetMetricData`` call can include up to 100
                    ``MetricDataQuery`` structures.

                    When used in ``PutMetricAlarm`` , it enables you to create an alarm based on a metric
                    math expression. Each ``MetricDataQuery`` in the array specifies either a metric to
                    retrieve, or a math expression to be performed on retrieved metrics. A single
                    ``PutMetricAlarm`` call can include up to 20 ``MetricDataQuery`` structures in the
                    array. The 20 structures can include as many as 10 structures that contain a
                    ``MetricStat`` parameter to retrieve a metric, and as many as 10 structures that
                    contain the ``Expression`` parameter to perform a math expression. Of those
                    ``Expression`` structures, one must have ``True`` as the value for ``ReturnData`` . The
                    result of this expression is the value the alarm watches.

                    Any expression used in a ``PutMetricAlarm`` operation must return a single time series.
                    For more information, see `Metric Math Syntax and Functions
                    <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax>`__
                    in the *Amazon CloudWatch User Guide* .

                    Some of the parameters of this structure also have different uses whether you are using
                    this structure in a ``GetMetricData`` operation or a ``PutMetricAlarm`` operation.
                    These differences are explained in the following parameter list.

                    - **Id** *(string) --*

                      A short name used to tie this object to the results in the response. This name must
                      be unique within a single call to ``GetMetricData`` . If you are performing math
                      expressions on this set of data, this name represents that data and can serve as a
                      variable in the mathematical expression. The valid characters are letters, numbers,
                      and underscore. The first character must be a lowercase letter.

                    - **MetricStat** *(dict) --*

                      The metric to be returned, along with statistics, period, and units. Use this
                      parameter only if this object is retrieving a metric and not performing a math
                      expression on returned data.

                      Within one MetricDataQuery object, you must specify either ``Expression`` or
                      ``MetricStat`` but not both.

                      - **Metric** *(dict) --*

                        The metric to return, including the metric name, namespace, and dimensions.

                        - **Namespace** *(string) --*

                          The namespace of the metric.

                        - **MetricName** *(string) --*

                          The name of the metric. This is a required field.

                        - **Dimensions** *(list) --*

                          The dimensions for the metric.

                          - *(dict) --*

                            Expands the identity of a metric.

                            - **Name** *(string) --*

                              The name of the dimension.

                            - **Value** *(string) --*

                              The value representing the dimension measurement.

                      - **Period** *(integer) --*

                        The granularity, in seconds, of the returned data points. For metrics with regular
                        resolution, a period can be as short as one minute (60 seconds) and must be a
                        multiple of 60. For high-resolution metrics that are collected at intervals of less
                        than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60.
                        High-resolution metrics are those metrics stored by a ``PutMetricData`` call that
                        includes a ``StorageResolution`` of 1 second.

                        If the ``StartTime`` parameter specifies a time stamp that is greater than 3 hours
                        ago, you must specify the period as follows or no data points in that time range is
                        returned:

                        * Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1
                        minute).

                        * Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).

                        * Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).

                      - **Stat** *(string) --*

                        The statistic to return. It can include any CloudWatch statistic or extended
                        statistic.

                      - **Unit** *(string) --*

                        When you are using a ``Put`` operation, this defines what unit you want to use when
                        storing the metric.

                        In a ``Get`` operation, if you omit ``Unit`` then all data that was collected with
                        any unit is returned, along with the corresponding units that were specified when
                        the data was reported to CloudWatch. If you specify a unit, the operation returns
                        only data data that was collected with that unit specified. If you specify a unit
                        that does not match the data collected, the results of the operation are null.
                        CloudWatch does not perform unit conversions.

                    - **Expression** *(string) --*

                      The math expression to be performed on the returned data, if this object is
                      performing a math expression. This expression can use the ``Id`` of the other metrics
                      to refer to those metrics, and can also use the ``Id`` of other expressions to use
                      the result of those expressions. For more information about metric math expressions,
                      see `Metric Math Syntax and Functions
                      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax>`__
                      in the *Amazon CloudWatch User Guide* .

                      Within each MetricDataQuery object, you must specify either ``Expression`` or
                      ``MetricStat`` but not both.

                    - **Label** *(string) --*

                      A human-readable label for this metric or expression. This is especially useful if
                      this is an expression, so that you know what the value represents. If the metric or
                      expression is shown in a CloudWatch dashboard widget, the label is shown. If Label is
                      omitted, CloudWatch generates a default.

                    - **ReturnData** *(boolean) --*

                      When used in ``GetMetricData`` , this option indicates whether to return the
                      timestamps and raw data values of this metric. If you are performing this call just
                      to do math expressions and do not also need the raw data returned, you can specify
                      ``False`` . If you omit this, the default of ``True`` is used.

                      When used in ``PutMetricAlarm`` , specify ``True`` for the one expression result to
                      use as the alarm. For all other metrics and expressions in the same
                      ``PutMetricAlarm`` operation, specify ``ReturnData`` as False.

                    - **Period** *(integer) --*

                      The granularity, in seconds, of the returned data points. For metrics with regular
                      resolution, a period can be as short as one minute (60 seconds) and must be a
                      multiple of 60. For high-resolution metrics that are collected at intervals of less
                      than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60.
                      High-resolution metrics are those metrics stored by a ``PutMetricData`` operation
                      that includes a ``StorageResolution of 1 second`` .

                      Use this field only when you are performing a ``GetMetricData`` operation, and only
                      when you are specifying the ``Expression`` field. Do not use this field with a
                      ``PutMetricAlarm`` operation or when you are specifying a ``MetricStat`` in a
                      ``GetMetricData`` operation.

                - **ThresholdMetricId** *(string) --*

                  In an alarm based on an anomaly detection model, this is the ID of the
                  ``ANOMALY_DETECTION_BAND`` function used as the threshold for the alarm.

            - **NextToken** *(string) --*

              The token that marks the start of the next batch of returned results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_alarms_for_metric(
        self,
        MetricName: str,
        Namespace: str,
        Statistic: str = None,
        ExtendedStatistic: str = None,
        Dimensions: List[ClientDescribeAlarmsForMetricDimensionsTypeDef] = None,
        Period: int = None,
        Unit: str = None,
    ) -> ClientDescribeAlarmsForMetricResponseTypeDef:
        """
        Retrieves the alarms for the specified metric. To filter the results, specify a statistic, period,
        or unit.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarmsForMetric>`_

        **Request Syntax**
        ::

          response = client.describe_alarms_for_metric(
              MetricName='string',
              Namespace='string',
              Statistic='SampleCount'|'Average'|'Sum'|'Minimum'|'Maximum',
              ExtendedStatistic='string',
              Dimensions=[
                  {
                      'Name': 'string',
                      'Value': 'string'
                  },
              ],
              Period=123,
              Unit=
                  'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'
                  |'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'
                  |'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'
                  |'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'
                  |'Terabits/Second'|'Count/Second'|'None'
          )
        :type MetricName: string
        :param MetricName: **[REQUIRED]**

          The name of the metric.

        :type Namespace: string
        :param Namespace: **[REQUIRED]**

          The namespace of the metric.

        :type Statistic: string
        :param Statistic:

          The statistic for the metric, other than percentiles. For percentile statistics, use
          ``ExtendedStatistics`` .

        :type ExtendedStatistic: string
        :param ExtendedStatistic:

          The percentile statistic for the metric. Specify a value between p0.0 and p100.

        :type Dimensions: list
        :param Dimensions:

          The dimensions associated with the metric. If the metric has any associated dimensions, you must
          specify them in order for the call to succeed.

          - *(dict) --*

            Expands the identity of a metric.

            - **Name** *(string) --* **[REQUIRED]**

              The name of the dimension.

            - **Value** *(string) --* **[REQUIRED]**

              The value representing the dimension measurement.

        :type Period: integer
        :param Period:

          The period, in seconds, over which the statistic is applied.

        :type Unit: string
        :param Unit:

          The unit for the metric.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'MetricAlarms': [
                    {
                        'AlarmName': 'string',
                        'AlarmArn': 'string',
                        'AlarmDescription': 'string',
                        'AlarmConfigurationUpdatedTimestamp': datetime(2015, 1, 1),
                        'ActionsEnabled': True|False,
                        'OKActions': [
                            'string',
                        ],
                        'AlarmActions': [
                            'string',
                        ],
                        'InsufficientDataActions': [
                            'string',
                        ],
                        'StateValue': 'OK'|'ALARM'|'INSUFFICIENT_DATA',
                        'StateReason': 'string',
                        'StateReasonData': 'string',
                        'StateUpdatedTimestamp': datetime(2015, 1, 1),
                        'MetricName': 'string',
                        'Namespace': 'string',
                        'Statistic': 'SampleCount'|'Average'|'Sum'|'Minimum'|'Maximum',
                        'ExtendedStatistic': 'string',
                        'Dimensions': [
                            {
                                'Name': 'string',
                                'Value': 'string'
                            },
                        ],
                        'Period': 123,
                        'Unit':
                        'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'
                        |'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'
                        |'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'
                        |'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'
                        |'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
                        'EvaluationPeriods': 123,
                        'DatapointsToAlarm': 123,
                        'Threshold': 123.0,
                        'ComparisonOperator':
                        'GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'
                        |'LessThanOrEqualToThreshold'|'LessThanLowerOrGreaterThanUpperThreshold'
                        |'LessThanLowerThreshold'|'GreaterThanUpperThreshold',
                        'TreatMissingData': 'string',
                        'EvaluateLowSampleCountPercentile': 'string',
                        'Metrics': [
                            {
                                'Id': 'string',
                                'MetricStat': {
                                    'Metric': {
                                        'Namespace': 'string',
                                        'MetricName': 'string',
                                        'Dimensions': [
                                            {
                                                'Name': 'string',
                                                'Value': 'string'
                                            },
                                        ]
                                    },
                                    'Period': 123,
                                    'Stat': 'string',
                                    'Unit':
                                    'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'
                                    |'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'
                                    |'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'
                                    |'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'
                                    |'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'
                                    |'Terabits/Second'|'Count/Second'|'None'
                                },
                                'Expression': 'string',
                                'Label': 'string',
                                'ReturnData': True|False,
                                'Period': 123
                            },
                        ],
                        'ThresholdMetricId': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **MetricAlarms** *(list) --*

              The information for each alarm with the specified metric.

              - *(dict) --*

                Represents an alarm.

                - **AlarmName** *(string) --*

                  The name of the alarm.

                - **AlarmArn** *(string) --*

                  The Amazon Resource Name (ARN) of the alarm.

                - **AlarmDescription** *(string) --*

                  The description of the alarm.

                - **AlarmConfigurationUpdatedTimestamp** *(datetime) --*

                  The time stamp of the last update to the alarm configuration.

                - **ActionsEnabled** *(boolean) --*

                  Indicates whether actions should be executed during any changes to the alarm state.

                - **OKActions** *(list) --*

                  The actions to execute when this alarm transitions to the ``OK`` state from any other
                  state. Each action is specified as an Amazon Resource Name (ARN).

                  - *(string) --*

                - **AlarmActions** *(list) --*

                  The actions to execute when this alarm transitions to the ``ALARM`` state from any other
                  state. Each action is specified as an Amazon Resource Name (ARN).

                  - *(string) --*

                - **InsufficientDataActions** *(list) --*

                  The actions to execute when this alarm transitions to the ``INSUFFICIENT_DATA`` state
                  from any other state. Each action is specified as an Amazon Resource Name (ARN).

                  - *(string) --*

                - **StateValue** *(string) --*

                  The state value for the alarm.

                - **StateReason** *(string) --*

                  An explanation for the alarm state, in text format.

                - **StateReasonData** *(string) --*

                  An explanation for the alarm state, in JSON format.

                - **StateUpdatedTimestamp** *(datetime) --*

                  The time stamp of the last update to the alarm state.

                - **MetricName** *(string) --*

                  The name of the metric associated with the alarm, if this is an alarm based on a single
                  metric.

                - **Namespace** *(string) --*

                  The namespace of the metric associated with the alarm.

                - **Statistic** *(string) --*

                  The statistic for the metric associated with the alarm, other than percentile. For
                  percentile statistics, use ``ExtendedStatistic`` .

                - **ExtendedStatistic** *(string) --*

                  The percentile statistic for the metric associated with the alarm. Specify a value
                  between p0.0 and p100.

                - **Dimensions** *(list) --*

                  The dimensions for the metric associated with the alarm.

                  - *(dict) --*

                    Expands the identity of a metric.

                    - **Name** *(string) --*

                      The name of the dimension.

                    - **Value** *(string) --*

                      The value representing the dimension measurement.

                - **Period** *(integer) --*

                  The period, in seconds, over which the statistic is applied.

                - **Unit** *(string) --*

                  The unit of the metric associated with the alarm.

                - **EvaluationPeriods** *(integer) --*

                  The number of periods over which data is compared to the specified threshold.

                - **DatapointsToAlarm** *(integer) --*

                  The number of datapoints that must be breaching to trigger the alarm.

                - **Threshold** *(float) --*

                  The value to compare with the specified statistic.

                - **ComparisonOperator** *(string) --*

                  The arithmetic operation to use when comparing the specified statistic and threshold. The
                  specified statistic value is used as the first operand.

                - **TreatMissingData** *(string) --*

                  Sets how this alarm is to handle missing data points. If this parameter is omitted, the
                  default behavior of ``missing`` is used.

                - **EvaluateLowSampleCountPercentile** *(string) --*

                  Used only for alarms based on percentiles. If ``ignore`` , the alarm state does not
                  change during periods with too few data points to be statistically significant. If
                  ``evaluate`` or this parameter is not used, the alarm is always evaluated and possibly
                  changes state no matter how many data points are available.

                - **Metrics** *(list) --*

                  An array of MetricDataQuery structures, used in an alarm based on a metric math
                  expression. Each structure either retrieves a metric or performs a math expression. One
                  item in the Metrics array is the math expression that the alarm watches. This expression
                  by designated by having ``ReturnValue`` set to true.

                  - *(dict) --*

                    This structure is used in both ``GetMetricData`` and ``PutMetricAlarm`` . The supported
                    use of this structure is different for those two operations.

                    When used in ``GetMetricData`` , it indicates the metric data to return, and whether
                    this call is just retrieving a batch set of data for one metric, or is performing a
                    math expression on metric data. A single ``GetMetricData`` call can include up to 100
                    ``MetricDataQuery`` structures.

                    When used in ``PutMetricAlarm`` , it enables you to create an alarm based on a metric
                    math expression. Each ``MetricDataQuery`` in the array specifies either a metric to
                    retrieve, or a math expression to be performed on retrieved metrics. A single
                    ``PutMetricAlarm`` call can include up to 20 ``MetricDataQuery`` structures in the
                    array. The 20 structures can include as many as 10 structures that contain a
                    ``MetricStat`` parameter to retrieve a metric, and as many as 10 structures that
                    contain the ``Expression`` parameter to perform a math expression. Of those
                    ``Expression`` structures, one must have ``True`` as the value for ``ReturnData`` . The
                    result of this expression is the value the alarm watches.

                    Any expression used in a ``PutMetricAlarm`` operation must return a single time series.
                    For more information, see `Metric Math Syntax and Functions
                    <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax>`__
                    in the *Amazon CloudWatch User Guide* .

                    Some of the parameters of this structure also have different uses whether you are using
                    this structure in a ``GetMetricData`` operation or a ``PutMetricAlarm`` operation.
                    These differences are explained in the following parameter list.

                    - **Id** *(string) --*

                      A short name used to tie this object to the results in the response. This name must
                      be unique within a single call to ``GetMetricData`` . If you are performing math
                      expressions on this set of data, this name represents that data and can serve as a
                      variable in the mathematical expression. The valid characters are letters, numbers,
                      and underscore. The first character must be a lowercase letter.

                    - **MetricStat** *(dict) --*

                      The metric to be returned, along with statistics, period, and units. Use this
                      parameter only if this object is retrieving a metric and not performing a math
                      expression on returned data.

                      Within one MetricDataQuery object, you must specify either ``Expression`` or
                      ``MetricStat`` but not both.

                      - **Metric** *(dict) --*

                        The metric to return, including the metric name, namespace, and dimensions.

                        - **Namespace** *(string) --*

                          The namespace of the metric.

                        - **MetricName** *(string) --*

                          The name of the metric. This is a required field.

                        - **Dimensions** *(list) --*

                          The dimensions for the metric.

                          - *(dict) --*

                            Expands the identity of a metric.

                            - **Name** *(string) --*

                              The name of the dimension.

                            - **Value** *(string) --*

                              The value representing the dimension measurement.

                      - **Period** *(integer) --*

                        The granularity, in seconds, of the returned data points. For metrics with regular
                        resolution, a period can be as short as one minute (60 seconds) and must be a
                        multiple of 60. For high-resolution metrics that are collected at intervals of less
                        than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60.
                        High-resolution metrics are those metrics stored by a ``PutMetricData`` call that
                        includes a ``StorageResolution`` of 1 second.

                        If the ``StartTime`` parameter specifies a time stamp that is greater than 3 hours
                        ago, you must specify the period as follows or no data points in that time range is
                        returned:

                        * Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1
                        minute).

                        * Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).

                        * Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).

                      - **Stat** *(string) --*

                        The statistic to return. It can include any CloudWatch statistic or extended
                        statistic.

                      - **Unit** *(string) --*

                        When you are using a ``Put`` operation, this defines what unit you want to use when
                        storing the metric.

                        In a ``Get`` operation, if you omit ``Unit`` then all data that was collected with
                        any unit is returned, along with the corresponding units that were specified when
                        the data was reported to CloudWatch. If you specify a unit, the operation returns
                        only data data that was collected with that unit specified. If you specify a unit
                        that does not match the data collected, the results of the operation are null.
                        CloudWatch does not perform unit conversions.

                    - **Expression** *(string) --*

                      The math expression to be performed on the returned data, if this object is
                      performing a math expression. This expression can use the ``Id`` of the other metrics
                      to refer to those metrics, and can also use the ``Id`` of other expressions to use
                      the result of those expressions. For more information about metric math expressions,
                      see `Metric Math Syntax and Functions
                      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax>`__
                      in the *Amazon CloudWatch User Guide* .

                      Within each MetricDataQuery object, you must specify either ``Expression`` or
                      ``MetricStat`` but not both.

                    - **Label** *(string) --*

                      A human-readable label for this metric or expression. This is especially useful if
                      this is an expression, so that you know what the value represents. If the metric or
                      expression is shown in a CloudWatch dashboard widget, the label is shown. If Label is
                      omitted, CloudWatch generates a default.

                    - **ReturnData** *(boolean) --*

                      When used in ``GetMetricData`` , this option indicates whether to return the
                      timestamps and raw data values of this metric. If you are performing this call just
                      to do math expressions and do not also need the raw data returned, you can specify
                      ``False`` . If you omit this, the default of ``True`` is used.

                      When used in ``PutMetricAlarm`` , specify ``True`` for the one expression result to
                      use as the alarm. For all other metrics and expressions in the same
                      ``PutMetricAlarm`` operation, specify ``ReturnData`` as False.

                    - **Period** *(integer) --*

                      The granularity, in seconds, of the returned data points. For metrics with regular
                      resolution, a period can be as short as one minute (60 seconds) and must be a
                      multiple of 60. For high-resolution metrics that are collected at intervals of less
                      than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60.
                      High-resolution metrics are those metrics stored by a ``PutMetricData`` operation
                      that includes a ``StorageResolution of 1 second`` .

                      Use this field only when you are performing a ``GetMetricData`` operation, and only
                      when you are specifying the ``Expression`` field. Do not use this field with a
                      ``PutMetricAlarm`` operation or when you are specifying a ``MetricStat`` in a
                      ``GetMetricData`` operation.

                - **ThresholdMetricId** *(string) --*

                  In an alarm based on an anomaly detection model, this is the ID of the
                  ``ANOMALY_DETECTION_BAND`` function used as the threshold for the alarm.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_anomaly_detectors(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        Namespace: str = None,
        MetricName: str = None,
        Dimensions: List[ClientDescribeAnomalyDetectorsDimensionsTypeDef] = None,
    ) -> ClientDescribeAnomalyDetectorsResponseTypeDef:
        """
        Lists the anomaly detection models that you have created in your account. You can list all models
        in your account or filter the results to only the models that are related to a certain namespace,
        metric name, or metric dimension.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAnomalyDetectors>`_

        **Request Syntax**
        ::

          response = client.describe_anomaly_detectors(
              NextToken='string',
              MaxResults=123,
              Namespace='string',
              MetricName='string',
              Dimensions=[
                  {
                      'Name': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type NextToken: string
        :param NextToken:

          Use the token returned by the previous operation to request the next page of results.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in one operation. The maximum value you can specify is 10.

          To retrieve the remaining results, make another call with the returned ``NextToken`` value.

        :type Namespace: string
        :param Namespace:

          Limits the results to only the anomaly detection models that are associated with the specified
          namespace.

        :type MetricName: string
        :param MetricName:

          Limits the results to only the anomaly detection models that are associated with the specified
          metric name. If there are multiple metrics with this name in different namespaces that have
          anomaly detection models, they're all returned.

        :type Dimensions: list
        :param Dimensions:

          Limits the results to only the anomaly detection models that are associated with the specified
          metric dimensions. If there are multiple metrics that have these dimensions and have anomaly
          detection models associated, they're all returned.

          - *(dict) --*

            Expands the identity of a metric.

            - **Name** *(string) --* **[REQUIRED]**

              The name of the dimension.

            - **Value** *(string) --* **[REQUIRED]**

              The value representing the dimension measurement.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AnomalyDetectors': [
                    {
                        'Namespace': 'string',
                        'MetricName': 'string',
                        'Dimensions': [
                            {
                                'Name': 'string',
                                'Value': 'string'
                            },
                        ],
                        'Stat': 'string',
                        'Configuration': {
                            'ExcludedTimeRanges': [
                                {
                                    'StartTime': datetime(2015, 1, 1),
                                    'EndTime': datetime(2015, 1, 1)
                                },
                            ],
                            'MetricTimezone': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **AnomalyDetectors** *(list) --*

              The list of anomaly detection models returned by the operation.

              - *(dict) --*

                An anomaly detection model associated with a particular CloudWatch metric athresnd
                statistic. You can use the model to display a band of expected normal values when the
                metric is graphed.

                - **Namespace** *(string) --*

                  The namespace of the metric associated with the anomaly detection model.

                - **MetricName** *(string) --*

                  The name of the metric associated with the anomaly detection model.

                - **Dimensions** *(list) --*

                  The metric dimensions associated with the anomaly detection model.

                  - *(dict) --*

                    Expands the identity of a metric.

                    - **Name** *(string) --*

                      The name of the dimension.

                    - **Value** *(string) --*

                      The value representing the dimension measurement.

                - **Stat** *(string) --*

                  The statistic associated with the anomaly detection model.

                - **Configuration** *(dict) --*

                  The configuration specifies details about how the anomaly detection model is to be
                  trained, including time ranges to exclude from use for training the model, and the time
                  zone to use for the metric.

                  - **ExcludedTimeRanges** *(list) --*

                    An array of time ranges to exclude from use when the anomaly detection model is
                    trained. Use this to make sure that events that could cause unusual values for the
                    metric, such as deployments, aren't used when CloudWatch creates the model.

                    - *(dict) --*

                      Specifies one range of days or times to exclude from use for training an anomaly
                      detection model.

                      - **StartTime** *(datetime) --*

                        The start time of the range to exclude. The format is ``yyyy-MM-dd'T'HH:mm:ss`` .
                        For example, ``2019-07-01T23:59:59`` .

                      - **EndTime** *(datetime) --*

                        The end time of the range to exclude. The format is ``yyyy-MM-dd'T'HH:mm:ss`` . For
                        example, ``2019-07-01T23:59:59`` .

                  - **MetricTimezone** *(string) --*

                    The time zone to use for the metric. This is useful to enable the model to
                    automatically account for daylight savings time changes if the metric is sensitive to
                    such time changes.

                    To specify a time zone, use the name of the time zone as specified in the standard tz
                    database. For more information, see `tz database
                    <https://en.wikipedia.org/wiki/Tz_database>`__ .

            - **NextToken** *(string) --*

              A token that you can use in a subsequent operation to retrieve the next set of results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_alarm_actions(self, AlarmNames: List[str]) -> None:
        """
        Disables the actions for the specified alarms. When an alarm's actions are disabled, the alarm
        actions do not execute when the alarm state changes.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DisableAlarmActions>`_

        **Request Syntax**
        ::

          response = client.disable_alarm_actions(
              AlarmNames=[
                  'string',
              ]
          )
        :type AlarmNames: list
        :param AlarmNames: **[REQUIRED]**

          The names of the alarms.

          - *(string) --*

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_alarm_actions(self, AlarmNames: List[str]) -> None:
        """
        Enables the actions for the specified alarms.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/EnableAlarmActions>`_

        **Request Syntax**
        ::

          response = client.enable_alarm_actions(
              AlarmNames=[
                  'string',
              ]
          )
        :type AlarmNames: list
        :param AlarmNames: **[REQUIRED]**

          The names of the alarms.

          - *(string) --*

        :returns: None
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
    def get_dashboard(self, DashboardName: str) -> ClientGetDashboardResponseTypeDef:
        """
        Displays the details of the dashboard that you specify.

        To copy an existing dashboard, use ``GetDashboard`` , and then use the data returned within
        ``DashboardBody`` as the template for the new dashboard when you call ``PutDashboard`` to create
        the copy.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/GetDashboard>`_

        **Request Syntax**
        ::

          response = client.get_dashboard(
              DashboardName='string'
          )
        :type DashboardName: string
        :param DashboardName: **[REQUIRED]**

          The name of the dashboard to be described.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DashboardArn': 'string',
                'DashboardBody': 'string',
                'DashboardName': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **DashboardArn** *(string) --*

              The Amazon Resource Name (ARN) of the dashboard.

            - **DashboardBody** *(string) --*

              The detailed information about the dashboard, including what widgets are included and their
              location on the dashboard. For more information about the ``DashboardBody`` syntax, see
              CloudWatch-Dashboard-Body-Structure .

            - **DashboardName** *(string) --*

              The name of the dashboard.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_metric_data(
        self,
        MetricDataQueries: List[ClientGetMetricDataMetricDataQueriesTypeDef],
        StartTime: datetime,
        EndTime: datetime,
        NextToken: str = None,
        ScanBy: str = None,
        MaxDatapoints: int = None,
    ) -> ClientGetMetricDataResponseTypeDef:
        """
        You can use the ``GetMetricData`` API to retrieve as many as 100 different metrics in a single
        request, with a total of as many as 100,800 datapoints. You can also optionally perform math
        expressions on the values of the returned statistics, to create new time series that represent new
        insights into your data. For example, using Lambda metrics, you could divide the Errors metric by
        the Invocations metric to get an error rate time series. For more information about metric math
        expressions, see `Metric Math Syntax and Functions
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax>`__
        in the *Amazon CloudWatch User Guide* .

        Calls to the ``GetMetricData`` API have a different pricing structure than calls to
        ``GetMetricStatistics`` . For more information about pricing, see `Amazon CloudWatch Pricing
        <https://aws.amazon.com/cloudwatch/pricing/>`__ .

        Amazon CloudWatch retains metric data as follows:

        * Data points with a period of less than 60 seconds are available for 3 hours. These data points
        are high-resolution metrics and are available only for custom metrics that have been defined with a
        ``StorageResolution`` of 1.

        * Data points with a period of 60 seconds (1-minute) are available for 15 days.

        * Data points with a period of 300 seconds (5-minute) are available for 63 days.

        * Data points with a period of 3600 seconds (1 hour) are available for 455 days (15 months).

        Data points that are initially published with a shorter period are aggregated together for
        long-term storage. For example, if you collect data using a period of 1 minute, the data remains
        available for 15 days with 1-minute resolution. After 15 days, this data is still available, but is
        aggregated and retrievable only with a resolution of 5 minutes. After 63 days, the data is further
        aggregated and is available with a resolution of 1 hour.

        If you omit ``Unit`` in your request, all data that was collected with any unit is returned, along
        with the corresponding units that were specified when the data was reported to CloudWatch. If you
        specify a unit, the operation returns only data data that was collected with that unit specified.
        If you specify a unit that does not match the data collected, the results of the operation are
        null. CloudWatch does not perform unit conversions.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/GetMetricData>`_

        **Request Syntax**
        ::

          response = client.get_metric_data(
              MetricDataQueries=[
                  {
                      'Id': 'string',
                      'MetricStat': {
                          'Metric': {
                              'Namespace': 'string',
                              'MetricName': 'string',
                              'Dimensions': [
                                  {
                                      'Name': 'string',
                                      'Value': 'string'
                                  },
                              ]
                          },
                          'Period': 123,
                          'Stat': 'string',
                          'Unit':
                          'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'
                          |'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'
                          |'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'
                          |'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'
                          |'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None'
                      },
                      'Expression': 'string',
                      'Label': 'string',
                      'ReturnData': True|False,
                      'Period': 123
                  },
              ],
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              NextToken='string',
              ScanBy='TimestampDescending'|'TimestampAscending',
              MaxDatapoints=123
          )
        :type MetricDataQueries: list
        :param MetricDataQueries: **[REQUIRED]**

          The metric queries to be returned. A single ``GetMetricData`` call can include as many as 100
          ``MetricDataQuery`` structures. Each of these structures can specify either a metric to retrieve,
          or a math expression to perform on retrieved data.

          - *(dict) --*

            This structure is used in both ``GetMetricData`` and ``PutMetricAlarm`` . The supported use of
            this structure is different for those two operations.

            When used in ``GetMetricData`` , it indicates the metric data to return, and whether this call
            is just retrieving a batch set of data for one metric, or is performing a math expression on
            metric data. A single ``GetMetricData`` call can include up to 100 ``MetricDataQuery``
            structures.

            When used in ``PutMetricAlarm`` , it enables you to create an alarm based on a metric math
            expression. Each ``MetricDataQuery`` in the array specifies either a metric to retrieve, or a
            math expression to be performed on retrieved metrics. A single ``PutMetricAlarm`` call can
            include up to 20 ``MetricDataQuery`` structures in the array. The 20 structures can include as
            many as 10 structures that contain a ``MetricStat`` parameter to retrieve a metric, and as many
            as 10 structures that contain the ``Expression`` parameter to perform a math expression. Of
            those ``Expression`` structures, one must have ``True`` as the value for ``ReturnData`` . The
            result of this expression is the value the alarm watches.

            Any expression used in a ``PutMetricAlarm`` operation must return a single time series. For
            more information, see `Metric Math Syntax and Functions
            <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax>`__
            in the *Amazon CloudWatch User Guide* .

            Some of the parameters of this structure also have different uses whether you are using this
            structure in a ``GetMetricData`` operation or a ``PutMetricAlarm`` operation. These differences
            are explained in the following parameter list.

            - **Id** *(string) --* **[REQUIRED]**

              A short name used to tie this object to the results in the response. This name must be unique
              within a single call to ``GetMetricData`` . If you are performing math expressions on this
              set of data, this name represents that data and can serve as a variable in the mathematical
              expression. The valid characters are letters, numbers, and underscore. The first character
              must be a lowercase letter.

            - **MetricStat** *(dict) --*

              The metric to be returned, along with statistics, period, and units. Use this parameter only
              if this object is retrieving a metric and not performing a math expression on returned data.

              Within one MetricDataQuery object, you must specify either ``Expression`` or ``MetricStat``
              but not both.

              - **Metric** *(dict) --* **[REQUIRED]**

                The metric to return, including the metric name, namespace, and dimensions.

                - **Namespace** *(string) --*

                  The namespace of the metric.

                - **MetricName** *(string) --*

                  The name of the metric. This is a required field.

                - **Dimensions** *(list) --*

                  The dimensions for the metric.

                  - *(dict) --*

                    Expands the identity of a metric.

                    - **Name** *(string) --* **[REQUIRED]**

                      The name of the dimension.

                    - **Value** *(string) --* **[REQUIRED]**

                      The value representing the dimension measurement.

              - **Period** *(integer) --* **[REQUIRED]**

                The granularity, in seconds, of the returned data points. For metrics with regular
                resolution, a period can be as short as one minute (60 seconds) and must be a multiple of
                60. For high-resolution metrics that are collected at intervals of less than one minute,
                the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are
                those metrics stored by a ``PutMetricData`` call that includes a ``StorageResolution`` of 1
                second.

                If the ``StartTime`` parameter specifies a time stamp that is greater than 3 hours ago, you
                must specify the period as follows or no data points in that time range is returned:

                * Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).

                * Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).

                * Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).

              - **Stat** *(string) --* **[REQUIRED]**

                The statistic to return. It can include any CloudWatch statistic or extended statistic.

              - **Unit** *(string) --*

                When you are using a ``Put`` operation, this defines what unit you want to use when storing
                the metric.

                In a ``Get`` operation, if you omit ``Unit`` then all data that was collected with any unit
                is returned, along with the corresponding units that were specified when the data was
                reported to CloudWatch. If you specify a unit, the operation returns only data data that
                was collected with that unit specified. If you specify a unit that does not match the data
                collected, the results of the operation are null. CloudWatch does not perform unit
                conversions.

            - **Expression** *(string) --*

              The math expression to be performed on the returned data, if this object is performing a math
              expression. This expression can use the ``Id`` of the other metrics to refer to those
              metrics, and can also use the ``Id`` of other expressions to use the result of those
              expressions. For more information about metric math expressions, see `Metric Math Syntax and
              Functions
              <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax>`__
              in the *Amazon CloudWatch User Guide* .

              Within each MetricDataQuery object, you must specify either ``Expression`` or ``MetricStat``
              but not both.

            - **Label** *(string) --*

              A human-readable label for this metric or expression. This is especially useful if this is an
              expression, so that you know what the value represents. If the metric or expression is shown
              in a CloudWatch dashboard widget, the label is shown. If Label is omitted, CloudWatch
              generates a default.

            - **ReturnData** *(boolean) --*

              When used in ``GetMetricData`` , this option indicates whether to return the timestamps and
              raw data values of this metric. If you are performing this call just to do math expressions
              and do not also need the raw data returned, you can specify ``False`` . If you omit this, the
              default of ``True`` is used.

              When used in ``PutMetricAlarm`` , specify ``True`` for the one expression result to use as
              the alarm. For all other metrics and expressions in the same ``PutMetricAlarm`` operation,
              specify ``ReturnData`` as False.

            - **Period** *(integer) --*

              The granularity, in seconds, of the returned data points. For metrics with regular
              resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60.
              For high-resolution metrics that are collected at intervals of less than one minute, the
              period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those
              metrics stored by a ``PutMetricData`` operation that includes a ``StorageResolution of 1
              second`` .

              Use this field only when you are performing a ``GetMetricData`` operation, and only when you
              are specifying the ``Expression`` field. Do not use this field with a ``PutMetricAlarm``
              operation or when you are specifying a ``MetricStat`` in a ``GetMetricData`` operation.

        :type StartTime: datetime
        :param StartTime: **[REQUIRED]**

          The time stamp indicating the earliest data to be returned.

          The value specified is inclusive; results include data points with the specified time stamp.

          CloudWatch rounds the specified time stamp as follows:

          * Start time less than 15 days ago - Round down to the nearest whole minute. For example,
          12:32:34 is rounded down to 12:32:00.

          * Start time between 15 and 63 days ago - Round down to the nearest 5-minute clock interval. For
          example, 12:32:34 is rounded down to 12:30:00.

          * Start time greater than 63 days ago - Round down to the nearest 1-hour clock interval. For
          example, 12:32:34 is rounded down to 12:00:00.

          If you set ``Period`` to 5, 10, or 30, the start time of your request is rounded down to the
          nearest time that corresponds to even 5-, 10-, or 30-second divisions of a minute. For example,
          if you make a query at (HH:mm:ss) 01:05:23 for the previous 10-second period, the start time of
          your request is rounded down and you receive data from 01:05:10 to 01:05:20. If you make a query
          at 15:07:17 for the previous 5 minutes of data, using a period of 5 seconds, you receive data
          timestamped between 15:02:15 and 15:07:15.

          For better performance, specify ``StartTime`` and ``EndTime`` values that align with the value of
          the metric's ``Period`` and sync up with the beginning and end of an hour. For example, if the
          ``Period`` of a metric is 5 minutes, specifying 12:05 or 12:30 as ``StartTime`` can get a faster
          response from CloudWatch than setting 12:07 or 12:29 as the ``StartTime`` .

        :type EndTime: datetime
        :param EndTime: **[REQUIRED]**

          The time stamp indicating the latest data to be returned.

          The value specified is exclusive; results include data points up to the specified time stamp.

          For better performance, specify ``StartTime`` and ``EndTime`` values that align with the value of
          the metric's ``Period`` and sync up with the beginning and end of an hour. For example, if the
          ``Period`` of a metric is 5 minutes, specifying 12:05 or 12:30 as ``EndTime`` can get a faster
          response from CloudWatch than setting 12:07 or 12:29 as the ``EndTime`` .

        :type NextToken: string
        :param NextToken:

          Include this value, if it was returned by the previous call, to get the next set of data points.

        :type ScanBy: string
        :param ScanBy:

          The order in which data points should be returned. ``TimestampDescending`` returns the newest
          data first and paginates when the ``MaxDatapoints`` limit is reached. ``TimestampAscending``
          returns the oldest data first and paginates when the ``MaxDatapoints`` limit is reached.

        :type MaxDatapoints: integer
        :param MaxDatapoints:

          The maximum number of data points the request should return before paginating. If you omit this,
          the default of 100,800 is used.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'MetricDataResults': [
                    {
                        'Id': 'string',
                        'Label': 'string',
                        'Timestamps': [
                            datetime(2015, 1, 1),
                        ],
                        'Values': [
                            123.0,
                        ],
                        'StatusCode': 'Complete'|'InternalError'|'PartialData',
                        'Messages': [
                            {
                                'Code': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                ],
                'NextToken': 'string',
                'Messages': [
                    {
                        'Code': 'string',
                        'Value': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **MetricDataResults** *(list) --*

              The metrics that are returned, including the metric name, namespace, and dimensions.

              - *(dict) --*

                A ``GetMetricData`` call returns an array of ``MetricDataResult`` structures. Each of these
                structures includes the data points for that metric, along with the timestamps of those
                data points and other identifying information.

                - **Id** *(string) --*

                  The short name you specified to represent this metric.

                - **Label** *(string) --*

                  The human-readable label associated with the data.

                - **Timestamps** *(list) --*

                  The timestamps for the data points, formatted in Unix timestamp format. The number of
                  timestamps always matches the number of values and the value for Timestamps[x] is
                  Values[x].

                  - *(datetime) --*

                - **Values** *(list) --*

                  The data points for the metric corresponding to ``Timestamps`` . The number of values
                  always matches the number of timestamps and the timestamp for Values[x] is Timestamps[x].

                  - *(float) --*

                - **StatusCode** *(string) --*

                  The status of the returned data. ``Complete`` indicates that all data points in the
                  requested time range were returned. ``PartialData`` means that an incomplete set of data
                  points were returned. You can use the ``NextToken`` value that was returned and repeat
                  your request to get more data points. ``NextToken`` is not returned if you are performing
                  a math expression. ``InternalError`` indicates that an error occurred. Retry your request
                  using ``NextToken`` , if present.

                - **Messages** *(list) --*

                  A list of messages with additional information about the data returned.

                  - *(dict) --*

                    A message returned by the ``GetMetricData`` API, including a code and a description.

                    - **Code** *(string) --*

                      The error code or status code associated with the message.

                    - **Value** *(string) --*

                      The message text.

            - **NextToken** *(string) --*

              A token that marks the next batch of returned results.

            - **Messages** *(list) --*

              Contains a message about this ``GetMetricData`` operation, if the operation results in such a
              message. An example of a message that may be returned is ``Maximum number of allowed metrics
              exceeded`` . If there is a message, as much of the operation as possible is still executed.

              A message appears here only if it is related to the global ``GetMetricData`` operation. Any
              message about a specific metric returned by the operation appears in the ``MetricDataResult``
              object returned for that metric.

              - *(dict) --*

                A message returned by the ``GetMetricData`` API, including a code and a description.

                - **Code** *(string) --*

                  The error code or status code associated with the message.

                - **Value** *(string) --*

                  The message text.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_metric_statistics(
        self,
        Namespace: str,
        MetricName: str,
        StartTime: datetime,
        EndTime: datetime,
        Period: int,
        Dimensions: List[ClientGetMetricStatisticsDimensionsTypeDef] = None,
        Statistics: List[str] = None,
        ExtendedStatistics: List[str] = None,
        Unit: str = None,
    ) -> ClientGetMetricStatisticsResponseTypeDef:
        """
        Gets statistics for the specified metric.

        The maximum number of data points returned from a single call is 1,440. If you request more than
        1,440 data points, CloudWatch returns an error. To reduce the number of data points, you can narrow
        the specified time range and make multiple requests across adjacent time ranges, or you can
        increase the specified period. Data points are not returned in chronological order.

        CloudWatch aggregates data points based on the length of the period that you specify. For example,
        if you request statistics with a one-hour period, CloudWatch aggregates all data points with time
        stamps that fall within each one-hour period. Therefore, the number of values aggregated by
        CloudWatch is larger than the number of data points returned.

        CloudWatch needs raw data points to calculate percentile statistics. If you publish data using a
        statistic set instead, you can only retrieve percentile statistics for this data if one of the
        following conditions is true:

        * The SampleCount value of the statistic set is 1.

        * The Min and the Max values of the statistic set are equal.

        Percentile statistics are not available for metrics when any of the metric values are negative
        numbers.

        Amazon CloudWatch retains metric data as follows:

        * Data points with a period of less than 60 seconds are available for 3 hours. These data points
        are high-resolution metrics and are available only for custom metrics that have been defined with a
        ``StorageResolution`` of 1.

        * Data points with a period of 60 seconds (1-minute) are available for 15 days.

        * Data points with a period of 300 seconds (5-minute) are available for 63 days.

        * Data points with a period of 3600 seconds (1 hour) are available for 455 days (15 months).

        Data points that are initially published with a shorter period are aggregated together for
        long-term storage. For example, if you collect data using a period of 1 minute, the data remains
        available for 15 days with 1-minute resolution. After 15 days, this data is still available, but is
        aggregated and retrievable only with a resolution of 5 minutes. After 63 days, the data is further
        aggregated and is available with a resolution of 1 hour.

        CloudWatch started retaining 5-minute and 1-hour metric data as of July 9, 2016.

        For information about metrics and dimensions supported by AWS services, see the `Amazon CloudWatch
        Metrics and Dimensions Reference
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CW_Support_For_AWS.html>`__ in the
        *Amazon CloudWatch User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/GetMetricStatistics>`_

        **Request Syntax**
        ::

          response = client.get_metric_statistics(
              Namespace='string',
              MetricName='string',
              Dimensions=[
                  {
                      'Name': 'string',
                      'Value': 'string'
                  },
              ],
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              Period=123,
              Statistics=[
                  'SampleCount'|'Average'|'Sum'|'Minimum'|'Maximum',
              ],
              ExtendedStatistics=[
                  'string',
              ],
              Unit=
                  'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'
                  |'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'
                  |'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'
                  |'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'
                  |'Terabits/Second'|'Count/Second'|'None'
          )
        :type Namespace: string
        :param Namespace: **[REQUIRED]**

          The namespace of the metric, with or without spaces.

        :type MetricName: string
        :param MetricName: **[REQUIRED]**

          The name of the metric, with or without spaces.

        :type Dimensions: list
        :param Dimensions:

          The dimensions. If the metric contains multiple dimensions, you must include a value for each
          dimension. CloudWatch treats each unique combination of dimensions as a separate metric. If a
          specific combination of dimensions was not published, you can't retrieve statistics for it. You
          must specify the same dimensions that were used when the metrics were created. For an example,
          see `Dimension Combinations
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#dimension-combinations>`__
          in the *Amazon CloudWatch User Guide* . For more information about specifying dimensions, see
          `Publishing Metrics
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html>`__ in the
          *Amazon CloudWatch User Guide* .

          - *(dict) --*

            Expands the identity of a metric.

            - **Name** *(string) --* **[REQUIRED]**

              The name of the dimension.

            - **Value** *(string) --* **[REQUIRED]**

              The value representing the dimension measurement.

        :type StartTime: datetime
        :param StartTime: **[REQUIRED]**

          The time stamp that determines the first data point to return. Start times are evaluated relative
          to the time that CloudWatch receives the request.

          The value specified is inclusive; results include data points with the specified time stamp. The
          time stamp must be in ISO 8601 UTC format (for example, 2016-10-03T23:00:00Z).

          CloudWatch rounds the specified time stamp as follows:

          * Start time less than 15 days ago - Round down to the nearest whole minute. For example,
          12:32:34 is rounded down to 12:32:00.

          * Start time between 15 and 63 days ago - Round down to the nearest 5-minute clock interval. For
          example, 12:32:34 is rounded down to 12:30:00.

          * Start time greater than 63 days ago - Round down to the nearest 1-hour clock interval. For
          example, 12:32:34 is rounded down to 12:00:00.

          If you set ``Period`` to 5, 10, or 30, the start time of your request is rounded down to the
          nearest time that corresponds to even 5-, 10-, or 30-second divisions of a minute. For example,
          if you make a query at (HH:mm:ss) 01:05:23 for the previous 10-second period, the start time of
          your request is rounded down and you receive data from 01:05:10 to 01:05:20. If you make a query
          at 15:07:17 for the previous 5 minutes of data, using a period of 5 seconds, you receive data
          timestamped between 15:02:15 and 15:07:15.

        :type EndTime: datetime
        :param EndTime: **[REQUIRED]**

          The time stamp that determines the last data point to return.

          The value specified is exclusive; results include data points up to the specified time stamp. The
          time stamp must be in ISO 8601 UTC format (for example, 2016-10-10T23:00:00Z).

        :type Period: integer
        :param Period: **[REQUIRED]**

          The granularity, in seconds, of the returned data points. For metrics with regular resolution, a
          period can be as short as one minute (60 seconds) and must be a multiple of 60. For
          high-resolution metrics that are collected at intervals of less than one minute, the period can
          be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a
          ``PutMetricData`` call that includes a ``StorageResolution`` of 1 second.

          If the ``StartTime`` parameter specifies a time stamp that is greater than 3 hours ago, you must
          specify the period as follows or no data points in that time range is returned:

          * Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).

          * Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).

          * Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).

        :type Statistics: list
        :param Statistics:

          The metric statistics, other than percentile. For percentile statistics, use
          ``ExtendedStatistics`` . When calling ``GetMetricStatistics`` , you must specify either
          ``Statistics`` or ``ExtendedStatistics`` , but not both.

          - *(string) --*

        :type ExtendedStatistics: list
        :param ExtendedStatistics:

          The percentile statistics. Specify values between p0.0 and p100. When calling
          ``GetMetricStatistics`` , you must specify either ``Statistics`` or ``ExtendedStatistics`` , but
          not both. Percentile statistics are not available for metrics when any of the metric values are
          negative numbers.

          - *(string) --*

        :type Unit: string
        :param Unit:

          The unit for a given metric. If you omit ``Unit`` , all data that was collected with any unit is
          returned, along with the corresponding units that were specified when the data was reported to
          CloudWatch. If you specify a unit, the operation returns only data data that was collected with
          that unit specified. If you specify a unit that does not match the data collected, the results of
          the operation are null. CloudWatch does not perform unit conversions.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Label': 'string',
                'Datapoints': [
                    {
                        'Timestamp': datetime(2015, 1, 1),
                        'SampleCount': 123.0,
                        'Average': 123.0,
                        'Sum': 123.0,
                        'Minimum': 123.0,
                        'Maximum': 123.0,
                        'Unit':
                        'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'
                        |'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'
                        |'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'
                        |'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'
                        |'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
                        'ExtendedStatistics': {
                            'string': 123.0
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Label** *(string) --*

              A label for the specified metric.

            - **Datapoints** *(list) --*

              The data points for the specified metric.

              - *(dict) --*

                Encapsulates the statistical data that CloudWatch computes from metric data.

                - **Timestamp** *(datetime) --*

                  The time stamp used for the data point.

                - **SampleCount** *(float) --*

                  The number of metric values that contributed to the aggregate value of this data point.

                - **Average** *(float) --*

                  The average of the metric values that correspond to the data point.

                - **Sum** *(float) --*

                  The sum of the metric values for the data point.

                - **Minimum** *(float) --*

                  The minimum metric value for the data point.

                - **Maximum** *(float) --*

                  The maximum metric value for the data point.

                - **Unit** *(string) --*

                  The standard unit for the data point.

                - **ExtendedStatistics** *(dict) --*

                  The percentile statistic for the data point.

                  - *(string) --*

                    - *(float) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_metric_widget_image(
        self, MetricWidget: str, OutputFormat: str = None
    ) -> ClientGetMetricWidgetImageResponseTypeDef:
        """
        You can use the ``GetMetricWidgetImage`` API to retrieve a snapshot graph of one or more Amazon
        CloudWatch metrics as a bitmap image. You can then embed this image into your services and
        products, such as wiki pages, reports, and documents. You could also retrieve images regularly,
        such as every minute, and create your own custom live dashboard.

        The graph you retrieve can include all CloudWatch metric graph features, including metric math and
        horizontal and vertical annotations.

        There is a limit of 20 transactions per second for this API. Each ``GetMetricWidgetImage`` action
        has the following limits:

        * As many as 100 metrics in the graph.

        * Up to 100 KB uncompressed payload.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/GetMetricWidgetImage>`_

        **Request Syntax**
        ::

          response = client.get_metric_widget_image(
              MetricWidget='string',
              OutputFormat='string'
          )
        :type MetricWidget: string
        :param MetricWidget: **[REQUIRED]**

          A JSON string that defines the bitmap graph to be retrieved. The string includes the metrics to
          include in the graph, statistics, annotations, title, axis limits, and so on. You can include
          only one ``MetricWidget`` parameter in each ``GetMetricWidgetImage`` call.

          For more information about the syntax of ``MetricWidget`` see  CloudWatch-Metric-Widget-Structure
          .

          If any metric on the graph could not load all the requested data points, an orange triangle with
          an exclamation point appears next to the graph legend.

        :type OutputFormat: string
        :param OutputFormat:

          The format of the resulting image. Only PNG images are supported.

          The default is ``png`` . If you specify ``png`` , the API returns an HTTP response with the
          content-type set to ``text/xml`` . The image data is in a ``MetricWidgetImage`` field. For
          example:

           ``<GetMetricWidgetImageResponse xmlns=<URLstring>>``

           ``<GetMetricWidgetImageResult>``

           ``<MetricWidgetImage>``

           ``iVBORw0KGgoAAAANSUhEUgAAAlgAAAGQEAYAAAAip...``

           ``</MetricWidgetImage>``

           ``</GetMetricWidgetImageResult>``

           ``<ResponseMetadata>``

           ``<RequestId>6f0d4192-4d42-11e8-82c1-f539a07e0e3b</RequestId>``

           ``</ResponseMetadata>``

           ``</GetMetricWidgetImageResponse>``

          The ``image/png`` setting is intended only for custom HTTP requests. For most use cases, and all
          actions using an AWS SDK, you should use ``png`` . If you specify ``image/png`` , the HTTP
          response has a content-type set to ``image/png`` , and the body of the response is a PNG image.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'MetricWidgetImage': b'bytes'
            }
          **Response Structure**

          - *(dict) --*

            - **MetricWidgetImage** *(bytes) --*

              The image of the graph, in the output format specified.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_dashboards(
        self, DashboardNamePrefix: str = None, NextToken: str = None
    ) -> ClientListDashboardsResponseTypeDef:
        """
        Returns a list of the dashboards for your account. If you include ``DashboardNamePrefix`` , only
        those dashboards with names starting with the prefix are listed. Otherwise, all dashboards in your
        account are listed.

         ``ListDashboards`` returns up to 1000 results on one page. If there are more than 1000 dashboards,
         you can call ``ListDashboards`` again and include the value you received for ``NextToken`` in the
         first call, to receive the next 1000 results.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/ListDashboards>`_

        **Request Syntax**
        ::

          response = client.list_dashboards(
              DashboardNamePrefix='string',
              NextToken='string'
          )
        :type DashboardNamePrefix: string
        :param DashboardNamePrefix:

          If you specify this parameter, only the dashboards with names starting with the specified string
          are listed. The maximum length is 255, and valid characters are A-Z, a-z, 0-9, ".", "-", and "_".

        :type NextToken: string
        :param NextToken:

          The token returned by a previous call to indicate that there is more data available.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DashboardEntries': [
                    {
                        'DashboardName': 'string',
                        'DashboardArn': 'string',
                        'LastModified': datetime(2015, 1, 1),
                        'Size': 123
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **DashboardEntries** *(list) --*

              The list of matching dashboards.

              - *(dict) --*

                Represents a specific dashboard.

                - **DashboardName** *(string) --*

                  The name of the dashboard.

                - **DashboardArn** *(string) --*

                  The Amazon Resource Name (ARN) of the dashboard.

                - **LastModified** *(datetime) --*

                  The time stamp of when the dashboard was last modified, either by an API call or through
                  the console. This number is expressed as the number of milliseconds since Jan 1, 1970
                  00:00:00 UTC.

                - **Size** *(integer) --*

                  The size of the dashboard, in bytes.

            - **NextToken** *(string) --*

              The token that marks the start of the next batch of returned results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_metrics(
        self,
        Namespace: str = None,
        MetricName: str = None,
        Dimensions: List[ClientListMetricsDimensionsTypeDef] = None,
        NextToken: str = None,
    ) -> ClientListMetricsResponseTypeDef:
        """
        List the specified metrics. You can use the returned metrics with  GetMetricData or
        GetMetricStatistics to obtain statistical data.

        Up to 500 results are returned for any one call. To retrieve additional results, use the returned
        token with subsequent calls.

        After you create a metric, allow up to fifteen minutes before the metric appears. Statistics about
        the metric, however, are available sooner using  GetMetricData or  GetMetricStatistics .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/ListMetrics>`_

        **Request Syntax**
        ::

          response = client.list_metrics(
              Namespace='string',
              MetricName='string',
              Dimensions=[
                  {
                      'Name': 'string',
                      'Value': 'string'
                  },
              ],
              NextToken='string'
          )
        :type Namespace: string
        :param Namespace:

          The namespace to filter against.

        :type MetricName: string
        :param MetricName:

          The name of the metric to filter against.

        :type Dimensions: list
        :param Dimensions:

          The dimensions to filter against.

          - *(dict) --*

            Represents filters for a dimension.

            - **Name** *(string) --* **[REQUIRED]**

              The dimension name to be matched.

            - **Value** *(string) --*

              The value of the dimension to be matched.

        :type NextToken: string
        :param NextToken:

          The token returned by a previous call to indicate that there is more data available.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Metrics': [
                    {
                        'Namespace': 'string',
                        'MetricName': 'string',
                        'Dimensions': [
                            {
                                'Name': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Metrics** *(list) --*

              The metrics.

              - *(dict) --*

                Represents a specific metric.

                - **Namespace** *(string) --*

                  The namespace of the metric.

                - **MetricName** *(string) --*

                  The name of the metric. This is a required field.

                - **Dimensions** *(list) --*

                  The dimensions for the metric.

                  - *(dict) --*

                    Expands the identity of a metric.

                    - **Name** *(string) --*

                      The name of the dimension.

                    - **Value** *(string) --*

                      The value representing the dimension measurement.

            - **NextToken** *(string) --*

              The token that marks the start of the next batch of returned results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, ResourceARN: str
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        Displays the tags associated with a CloudWatch resource. Alarms support tagging.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/ListTagsForResource>`_

        **Request Syntax**
        ::

          response = client.list_tags_for_resource(
              ResourceARN='string'
          )
        :type ResourceARN: string
        :param ResourceARN: **[REQUIRED]**

          The ARN of the CloudWatch resource that you want to view tags for. For more information on ARN
          format, see `Example ARNs
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-cloudwatch>`__
          in the *Amazon Web Services General Reference* .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Tags** *(list) --*

              The list of tag keys and values associated with the resource you specified.

              - *(dict) --*

                A key-value pair associated with a CloudWatch resource.

                - **Key** *(string) --*

                  A string that you can use to assign a value. The combination of tag keys and values can
                  help you organize and categorize your resources.

                - **Value** *(string) --*

                  The value for the specified tag key.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_anomaly_detector(
        self,
        Namespace: str,
        MetricName: str,
        Stat: str,
        Dimensions: List[ClientPutAnomalyDetectorDimensionsTypeDef] = None,
        Configuration: ClientPutAnomalyDetectorConfigurationTypeDef = None,
    ) -> Dict[str, Any]:
        """
        Creates an anomaly detection model for a CloudWatch metric. You can use the model to display a band
        of expected normal values when the metric is graphed.

        For more information, see `CloudWatch Anomaly Detection
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html>`__
        .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/PutAnomalyDetector>`_

        **Request Syntax**
        ::

          response = client.put_anomaly_detector(
              Namespace='string',
              MetricName='string',
              Dimensions=[
                  {
                      'Name': 'string',
                      'Value': 'string'
                  },
              ],
              Stat='string',
              Configuration={
                  'ExcludedTimeRanges': [
                      {
                          'StartTime': datetime(2015, 1, 1),
                          'EndTime': datetime(2015, 1, 1)
                      },
                  ],
                  'MetricTimezone': 'string'
              }
          )
        :type Namespace: string
        :param Namespace: **[REQUIRED]**

          The namespace of the metric to create the anomaly detection model for.

        :type MetricName: string
        :param MetricName: **[REQUIRED]**

          The name of the metric to create the anomaly detection model for.

        :type Dimensions: list
        :param Dimensions:

          The metric dimensions to create the anomaly detection model for.

          - *(dict) --*

            Expands the identity of a metric.

            - **Name** *(string) --* **[REQUIRED]**

              The name of the dimension.

            - **Value** *(string) --* **[REQUIRED]**

              The value representing the dimension measurement.

        :type Stat: string
        :param Stat: **[REQUIRED]**

          The statistic to use for the metric and the anomaly detection model.

        :type Configuration: dict
        :param Configuration:

          The configuration specifies details about how the anomaly detection model is to be trained,
          including time ranges to exclude when training and updating the model. You can specify as many as
          10 time ranges.

          The configuration can also include the time zone to use for the metric.

          You can in

          - **ExcludedTimeRanges** *(list) --*

            An array of time ranges to exclude from use when the anomaly detection model is trained. Use
            this to make sure that events that could cause unusual values for the metric, such as
            deployments, aren't used when CloudWatch creates the model.

            - *(dict) --*

              Specifies one range of days or times to exclude from use for training an anomaly detection
              model.

              - **StartTime** *(datetime) --* **[REQUIRED]**

                The start time of the range to exclude. The format is ``yyyy-MM-dd'T'HH:mm:ss`` . For
                example, ``2019-07-01T23:59:59`` .

              - **EndTime** *(datetime) --* **[REQUIRED]**

                The end time of the range to exclude. The format is ``yyyy-MM-dd'T'HH:mm:ss`` . For
                example, ``2019-07-01T23:59:59`` .

          - **MetricTimezone** *(string) --*

            The time zone to use for the metric. This is useful to enable the model to automatically
            account for daylight savings time changes if the metric is sensitive to such time changes.

            To specify a time zone, use the name of the time zone as specified in the standard tz database.
            For more information, see `tz database <https://en.wikipedia.org/wiki/Tz_database>`__ .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_dashboard(
        self, DashboardName: str, DashboardBody: str
    ) -> ClientPutDashboardResponseTypeDef:
        """
        Creates a dashboard if it does not already exist, or updates an existing dashboard. If you update a
        dashboard, the entire contents are replaced with what you specify here.

        All dashboards in your account are global, not region-specific.

        A simple way to create a dashboard using ``PutDashboard`` is to copy an existing dashboard. To copy
        an existing dashboard using the console, you can load the dashboard and then use the View/edit
        source command in the Actions menu to display the JSON block for that dashboard. Another way to
        copy a dashboard is to use ``GetDashboard`` , and then use the data returned within
        ``DashboardBody`` as the template for the new dashboard when you call ``PutDashboard`` .

        When you create a dashboard with ``PutDashboard`` , a good practice is to add a text widget at the
        top of the dashboard with a message that the dashboard was created by script and should not be
        changed in the console. This message could also point console users to the location of the
        ``DashboardBody`` script or the CloudFormation template used to create the dashboard.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/PutDashboard>`_

        **Request Syntax**
        ::

          response = client.put_dashboard(
              DashboardName='string',
              DashboardBody='string'
          )
        :type DashboardName: string
        :param DashboardName: **[REQUIRED]**

          The name of the dashboard. If a dashboard with this name already exists, this call modifies that
          dashboard, replacing its current contents. Otherwise, a new dashboard is created. The maximum
          length is 255, and valid characters are A-Z, a-z, 0-9, "-", and "_". This parameter is required.

        :type DashboardBody: string
        :param DashboardBody: **[REQUIRED]**

          The detailed information about the dashboard in JSON format, including the widgets to include and
          their location on the dashboard. This parameter is required.

          For more information about the syntax, see  CloudWatch-Dashboard-Body-Structure .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DashboardValidationMessages': [
                    {
                        'DataPath': 'string',
                        'Message': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **DashboardValidationMessages** *(list) --*

              If the input for ``PutDashboard`` was correct and the dashboard was successfully created or
              modified, this result is empty.

              If this result includes only warning messages, then the input was valid enough for the
              dashboard to be created or modified, but some elements of the dashboard may not render.

              If this result includes error messages, the input was not valid and the operation failed.

              - *(dict) --*

                An error or warning for the operation.

                - **DataPath** *(string) --*

                  The data path related to the message.

                - **Message** *(string) --*

                  A message describing the error or warning.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_metric_alarm(
        self,
        AlarmName: str,
        EvaluationPeriods: int,
        ComparisonOperator: str,
        AlarmDescription: str = None,
        ActionsEnabled: bool = None,
        OKActions: List[str] = None,
        AlarmActions: List[str] = None,
        InsufficientDataActions: List[str] = None,
        MetricName: str = None,
        Namespace: str = None,
        Statistic: str = None,
        ExtendedStatistic: str = None,
        Dimensions: List[ClientPutMetricAlarmDimensionsTypeDef] = None,
        Period: int = None,
        Unit: str = None,
        DatapointsToAlarm: int = None,
        Threshold: float = None,
        TreatMissingData: str = None,
        EvaluateLowSampleCountPercentile: str = None,
        Metrics: List[ClientPutMetricAlarmMetricsTypeDef] = None,
        Tags: List[ClientPutMetricAlarmTagsTypeDef] = None,
        ThresholdMetricId: str = None,
    ) -> None:
        """
        Creates or updates an alarm and associates it with the specified metric, metric math expression, or
        anomaly detection model.

        Alarms based on anomaly detection models cannot have Auto Scaling actions.

        When this operation creates an alarm, the alarm state is immediately set to ``INSUFFICIENT_DATA`` .
        The alarm is then evaluated and its state is set appropriately. Any actions associated with the new
        state are then executed.

        When you update an existing alarm, its state is left unchanged, but the update completely
        overwrites the previous configuration of the alarm.

        If you are an IAM user, you must have Amazon EC2 permissions for some alarm operations:

        * ``iam:CreateServiceLinkedRole`` for all alarms with EC2 actions

        * ``ec2:DescribeInstanceStatus`` and ``ec2:DescribeInstances`` for all alarms on EC2 instance
        status metrics

        * ``ec2:StopInstances`` for alarms with stop actions

        * ``ec2:TerminateInstances`` for alarms with terminate actions

        * No specific permissions are needed for alarms with recover actions

        If you have read/write permissions for Amazon CloudWatch but not for Amazon EC2, you can still
        create an alarm, but the stop or terminate actions are not performed. However, if you are later
        granted the required permissions, the alarm actions that you created earlier are performed.

        If you are using an IAM role (for example, an EC2 instance profile), you cannot stop or terminate
        the instance using alarm actions. However, you can still see the alarm state and perform any other
        actions such as Amazon SNS notifications or Auto Scaling policies.

        If you are using temporary security credentials granted using AWS STS, you cannot stop or terminate
        an EC2 instance using alarm actions.

        The first time you create an alarm in the AWS Management Console, the CLI, or by using the
        PutMetricAlarm API, CloudWatch creates the necessary service-linked role for you. The
        service-linked role is called ``AWSServiceRoleForCloudWatchEvents`` . For more information, see
        `AWS service-linked role
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role>`__
        .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/PutMetricAlarm>`_

        **Request Syntax**
        ::

          response = client.put_metric_alarm(
              AlarmName='string',
              AlarmDescription='string',
              ActionsEnabled=True|False,
              OKActions=[
                  'string',
              ],
              AlarmActions=[
                  'string',
              ],
              InsufficientDataActions=[
                  'string',
              ],
              MetricName='string',
              Namespace='string',
              Statistic='SampleCount'|'Average'|'Sum'|'Minimum'|'Maximum',
              ExtendedStatistic='string',
              Dimensions=[
                  {
                      'Name': 'string',
                      'Value': 'string'
                  },
              ],
              Period=123,
              Unit=
                  'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'
                  |'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'
                  |'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'
                  |'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'
                  |'Terabits/Second'|'Count/Second'|'None',
              EvaluationPeriods=123,
              DatapointsToAlarm=123,
              Threshold=123.0,
              ComparisonOperator=
                  'GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'
                  |'LessThanOrEqualToThreshold'|'LessThanLowerOrGreaterThanUpperThreshold'
                  |'LessThanLowerThreshold'|'GreaterThanUpperThreshold',
              TreatMissingData='string',
              EvaluateLowSampleCountPercentile='string',
              Metrics=[
                  {
                      'Id': 'string',
                      'MetricStat': {
                          'Metric': {
                              'Namespace': 'string',
                              'MetricName': 'string',
                              'Dimensions': [
                                  {
                                      'Name': 'string',
                                      'Value': 'string'
                                  },
                              ]
                          },
                          'Period': 123,
                          'Stat': 'string',
                          'Unit':
                          'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'
                          |'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'
                          |'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'
                          |'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'
                          |'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None'
                      },
                      'Expression': 'string',
                      'Label': 'string',
                      'ReturnData': True|False,
                      'Period': 123
                  },
              ],
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ],
              ThresholdMetricId='string'
          )
        :type AlarmName: string
        :param AlarmName: **[REQUIRED]**

          The name for the alarm. This name must be unique within your AWS account.

        :type AlarmDescription: string
        :param AlarmDescription:

          The description for the alarm.

        :type ActionsEnabled: boolean
        :param ActionsEnabled:

          Indicates whether actions should be executed during any changes to the alarm state. The default
          is ``TRUE`` .

        :type OKActions: list
        :param OKActions:

          The actions to execute when this alarm transitions to an ``OK`` state from any other state. Each
          action is specified as an Amazon Resource Name (ARN).

          Valid Values: ``arn:aws:automate:*region* :ec2:stop`` | ``arn:aws:automate:*region*
          :ec2:terminate`` | ``arn:aws:automate:*region* :ec2:recover`` | ``arn:aws:automate:*region*
          :ec2:reboot`` | ``arn:aws:sns:*region* :*account-id* :*sns-topic-name* `` |
          ``arn:aws:autoscaling:*region* :*account-id* :scalingPolicy:*policy-id*
          autoScalingGroupName/*group-friendly-name* :policyName/*policy-friendly-name* ``

          Valid Values (for use with IAM roles): ``arn:aws:swf:*region* :*account-id*
          :action/actions/AWS_EC2.InstanceId.Stop/1.0`` | ``arn:aws:swf:*region* :*account-id*
          :action/actions/AWS_EC2.InstanceId.Terminate/1.0`` | ``arn:aws:swf:*region* :*account-id*
          :action/actions/AWS_EC2.InstanceId.Reboot/1.0``

          - *(string) --*

        :type AlarmActions: list
        :param AlarmActions:

          The actions to execute when this alarm transitions to the ``ALARM`` state from any other state.
          Each action is specified as an Amazon Resource Name (ARN).

          Valid Values: ``arn:aws:automate:*region* :ec2:stop`` | ``arn:aws:automate:*region*
          :ec2:terminate`` | ``arn:aws:automate:*region* :ec2:recover`` | ``arn:aws:automate:*region*
          :ec2:reboot`` | ``arn:aws:sns:*region* :*account-id* :*sns-topic-name* `` |
          ``arn:aws:autoscaling:*region* :*account-id* :scalingPolicy:*policy-id*
          autoScalingGroupName/*group-friendly-name* :policyName/*policy-friendly-name* ``

          Valid Values (for use with IAM roles): ``arn:aws:swf:*region* :*account-id*
          :action/actions/AWS_EC2.InstanceId.Stop/1.0`` | ``arn:aws:swf:*region* :*account-id*
          :action/actions/AWS_EC2.InstanceId.Terminate/1.0`` | ``arn:aws:swf:*region* :*account-id*
          :action/actions/AWS_EC2.InstanceId.Reboot/1.0``

          - *(string) --*

        :type InsufficientDataActions: list
        :param InsufficientDataActions:

          The actions to execute when this alarm transitions to the ``INSUFFICIENT_DATA`` state from any
          other state. Each action is specified as an Amazon Resource Name (ARN).

          Valid Values: ``arn:aws:automate:*region* :ec2:stop`` | ``arn:aws:automate:*region*
          :ec2:terminate`` | ``arn:aws:automate:*region* :ec2:recover`` | ``arn:aws:automate:*region*
          :ec2:reboot`` | ``arn:aws:sns:*region* :*account-id* :*sns-topic-name* `` |
          ``arn:aws:autoscaling:*region* :*account-id* :scalingPolicy:*policy-id*
          autoScalingGroupName/*group-friendly-name* :policyName/*policy-friendly-name* ``

          Valid Values (for use with IAM roles): ``>arn:aws:swf:*region* :*account-id*
          :action/actions/AWS_EC2.InstanceId.Stop/1.0`` | ``arn:aws:swf:*region* :*account-id*
          :action/actions/AWS_EC2.InstanceId.Terminate/1.0`` | ``arn:aws:swf:*region* :*account-id*
          :action/actions/AWS_EC2.InstanceId.Reboot/1.0``

          - *(string) --*

        :type MetricName: string
        :param MetricName:

          The name for the metric associated with the alarm. For each ``PutMetricAlarm`` operation, you
          must specify either ``MetricName`` or a ``Metrics`` array.

          If you are creating an alarm based on a math expression, you cannot specify this parameter, or
          any of the ``Dimensions`` , ``Period`` , ``Namespace`` , ``Statistic`` , or ``ExtendedStatistic``
          parameters. Instead, you specify all this information in the ``Metrics`` array.

        :type Namespace: string
        :param Namespace:

          The namespace for the metric associated specified in ``MetricName`` .

        :type Statistic: string
        :param Statistic:

          The statistic for the metric specified in ``MetricName`` , other than percentile. For percentile
          statistics, use ``ExtendedStatistic`` . When you call ``PutMetricAlarm`` and specify a
          ``MetricName`` , you must specify either ``Statistic`` or ``ExtendedStatistic,`` but not both.

        :type ExtendedStatistic: string
        :param ExtendedStatistic:

          The percentile statistic for the metric specified in ``MetricName`` . Specify a value between
          p0.0 and p100. When you call ``PutMetricAlarm`` and specify a ``MetricName`` , you must specify
          either ``Statistic`` or ``ExtendedStatistic,`` but not both.

        :type Dimensions: list
        :param Dimensions:

          The dimensions for the metric specified in ``MetricName`` .

          - *(dict) --*

            Expands the identity of a metric.

            - **Name** *(string) --* **[REQUIRED]**

              The name of the dimension.

            - **Value** *(string) --* **[REQUIRED]**

              The value representing the dimension measurement.

        :type Period: integer
        :param Period:

          The length, in seconds, used each time the metric specified in ``MetricName`` is evaluated. Valid
          values are 10, 30, and any multiple of 60.

           ``Period`` is required for alarms based on static thresholds. If you are creating an alarm based
           on a metric math expression, you specify the period for each metric within the objects in the
           ``Metrics`` array.

          Be sure to specify 10 or 30 only for metrics that are stored by a ``PutMetricData`` call with a
          ``StorageResolution`` of 1. If you specify a period of 10 or 30 for a metric that does not have
          sub-minute resolution, the alarm still attempts to gather data at the period rate that you
          specify. In this case, it does not receive data for the attempts that do not correspond to a
          one-minute data resolution, and the alarm may often lapse into INSUFFICENT_DATA status.
          Specifying 10 or 30 also sets this alarm as a high-resolution alarm, which has a higher charge
          than other alarms. For more information about pricing, see `Amazon CloudWatch Pricing
          <https://aws.amazon.com/cloudwatch/pricing/>`__ .

          An alarm's total current evaluation period can be no longer than one day, so ``Period``
          multiplied by ``EvaluationPeriods`` cannot be more than 86,400 seconds.

        :type Unit: string
        :param Unit:

          The unit of measure for the statistic. For example, the units for the Amazon EC2 NetworkIn metric
          are Bytes because NetworkIn tracks the number of bytes that an instance receives on all network
          interfaces. You can also specify a unit when you create a custom metric. Units help provide
          conceptual meaning to your data. Metric data points that specify a unit of measure, such as
          Percent, are aggregated separately.

          If you don't specify ``Unit`` , CloudWatch retrieves all unit types that have been published for
          the metric and attempts to evaluate the alarm. Usually metrics are published with only one unit,
          so the alarm will work as intended.

          However, if the metric is published with multiple types of units and you don't specify a unit,
          the alarm's behavior is not defined and will behave un-predictably.

          We recommend omitting ``Unit`` so that you don't inadvertently specify an incorrect unit that is
          not published for this metric. Doing so causes the alarm to be stuck in the ``INSUFFICIENT DATA``
          state.

        :type EvaluationPeriods: integer
        :param EvaluationPeriods: **[REQUIRED]**

          The number of periods over which data is compared to the specified threshold. If you are setting
          an alarm that requires that a number of consecutive data points be breaching to trigger the
          alarm, this value specifies that number. If you are setting an "M out of N" alarm, this value is
          the N.

          An alarm's total current evaluation period can be no longer than one day, so this number
          multiplied by ``Period`` cannot be more than 86,400 seconds.

        :type DatapointsToAlarm: integer
        :param DatapointsToAlarm:

          The number of datapoints that must be breaching to trigger the alarm. This is used only if you
          are setting an "M out of N" alarm. In that case, this value is the M. For more information, see
          `Evaluating an Alarm
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarm-evaluation>`__
          in the *Amazon CloudWatch User Guide* .

        :type Threshold: float
        :param Threshold:

          The value against which the specified statistic is compared.

          This parameter is required for alarms based on static thresholds, but should not be used for
          alarms based on anomaly detection models.

        :type ComparisonOperator: string
        :param ComparisonOperator: **[REQUIRED]**

          The arithmetic operation to use when comparing the specified statistic and threshold. The
          specified statistic value is used as the first operand.

          The values ``LessThanLowerOrGreaterThanUpperThreshold`` , ``LessThanLowerThreshold`` , and
          ``GreaterThanUpperThreshold`` are used only for alarms based on anomaly detection models.

        :type TreatMissingData: string
        :param TreatMissingData:

          Sets how this alarm is to handle missing data points. If ``TreatMissingData`` is omitted, the
          default behavior of ``missing`` is used. For more information, see `Configuring How CloudWatch
          Alarms Treats Missing Data
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-missing-data>`__
          .

          Valid Values: ``breaching | notBreaching | ignore | missing``

        :type EvaluateLowSampleCountPercentile: string
        :param EvaluateLowSampleCountPercentile:

          Used only for alarms based on percentiles. If you specify ``ignore`` , the alarm state does not
          change during periods with too few data points to be statistically significant. If you specify
          ``evaluate`` or omit this parameter, the alarm is always evaluated and possibly changes state no
          matter how many data points are available. For more information, see `Percentile-Based CloudWatch
          Alarms and Low Data Samples
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#percentiles-with-low-samples>`__
          .

          Valid Values: ``evaluate | ignore``

        :type Metrics: list
        :param Metrics:

          An array of ``MetricDataQuery`` structures that enable you to create an alarm based on the result
          of a metric math expression. For each ``PutMetricAlarm`` operation, you must specify either
          ``MetricName`` or a ``Metrics`` array.

          Each item in the ``Metrics`` array either retrieves a metric or performs a math expression.

          One item in the ``Metrics`` array is the expression that the alarm watches. You designate this
          expression by setting ``ReturnValue`` to true for this object in the array. For more information,
          see  MetricDataQuery .

          If you use the ``Metrics`` parameter, you cannot include the ``MetricName`` , ``Dimensions`` ,
          ``Period`` , ``Namespace`` , ``Statistic`` , or ``ExtendedStatistic`` parameters of
          ``PutMetricAlarm`` in the same operation. Instead, you retrieve the metrics you are using in your
          math expression as part of the ``Metrics`` array.

          - *(dict) --*

            This structure is used in both ``GetMetricData`` and ``PutMetricAlarm`` . The supported use of
            this structure is different for those two operations.

            When used in ``GetMetricData`` , it indicates the metric data to return, and whether this call
            is just retrieving a batch set of data for one metric, or is performing a math expression on
            metric data. A single ``GetMetricData`` call can include up to 100 ``MetricDataQuery``
            structures.

            When used in ``PutMetricAlarm`` , it enables you to create an alarm based on a metric math
            expression. Each ``MetricDataQuery`` in the array specifies either a metric to retrieve, or a
            math expression to be performed on retrieved metrics. A single ``PutMetricAlarm`` call can
            include up to 20 ``MetricDataQuery`` structures in the array. The 20 structures can include as
            many as 10 structures that contain a ``MetricStat`` parameter to retrieve a metric, and as many
            as 10 structures that contain the ``Expression`` parameter to perform a math expression. Of
            those ``Expression`` structures, one must have ``True`` as the value for ``ReturnData`` . The
            result of this expression is the value the alarm watches.

            Any expression used in a ``PutMetricAlarm`` operation must return a single time series. For
            more information, see `Metric Math Syntax and Functions
            <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax>`__
            in the *Amazon CloudWatch User Guide* .

            Some of the parameters of this structure also have different uses whether you are using this
            structure in a ``GetMetricData`` operation or a ``PutMetricAlarm`` operation. These differences
            are explained in the following parameter list.

            - **Id** *(string) --* **[REQUIRED]**

              A short name used to tie this object to the results in the response. This name must be unique
              within a single call to ``GetMetricData`` . If you are performing math expressions on this
              set of data, this name represents that data and can serve as a variable in the mathematical
              expression. The valid characters are letters, numbers, and underscore. The first character
              must be a lowercase letter.

            - **MetricStat** *(dict) --*

              The metric to be returned, along with statistics, period, and units. Use this parameter only
              if this object is retrieving a metric and not performing a math expression on returned data.

              Within one MetricDataQuery object, you must specify either ``Expression`` or ``MetricStat``
              but not both.

              - **Metric** *(dict) --* **[REQUIRED]**

                The metric to return, including the metric name, namespace, and dimensions.

                - **Namespace** *(string) --*

                  The namespace of the metric.

                - **MetricName** *(string) --*

                  The name of the metric. This is a required field.

                - **Dimensions** *(list) --*

                  The dimensions for the metric.

                  - *(dict) --*

                    Expands the identity of a metric.

                    - **Name** *(string) --* **[REQUIRED]**

                      The name of the dimension.

                    - **Value** *(string) --* **[REQUIRED]**

                      The value representing the dimension measurement.

              - **Period** *(integer) --* **[REQUIRED]**

                The granularity, in seconds, of the returned data points. For metrics with regular
                resolution, a period can be as short as one minute (60 seconds) and must be a multiple of
                60. For high-resolution metrics that are collected at intervals of less than one minute,
                the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are
                those metrics stored by a ``PutMetricData`` call that includes a ``StorageResolution`` of 1
                second.

                If the ``StartTime`` parameter specifies a time stamp that is greater than 3 hours ago, you
                must specify the period as follows or no data points in that time range is returned:

                * Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).

                * Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).

                * Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).

              - **Stat** *(string) --* **[REQUIRED]**

                The statistic to return. It can include any CloudWatch statistic or extended statistic.

              - **Unit** *(string) --*

                When you are using a ``Put`` operation, this defines what unit you want to use when storing
                the metric.

                In a ``Get`` operation, if you omit ``Unit`` then all data that was collected with any unit
                is returned, along with the corresponding units that were specified when the data was
                reported to CloudWatch. If you specify a unit, the operation returns only data data that
                was collected with that unit specified. If you specify a unit that does not match the data
                collected, the results of the operation are null. CloudWatch does not perform unit
                conversions.

            - **Expression** *(string) --*

              The math expression to be performed on the returned data, if this object is performing a math
              expression. This expression can use the ``Id`` of the other metrics to refer to those
              metrics, and can also use the ``Id`` of other expressions to use the result of those
              expressions. For more information about metric math expressions, see `Metric Math Syntax and
              Functions
              <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax>`__
              in the *Amazon CloudWatch User Guide* .

              Within each MetricDataQuery object, you must specify either ``Expression`` or ``MetricStat``
              but not both.

            - **Label** *(string) --*

              A human-readable label for this metric or expression. This is especially useful if this is an
              expression, so that you know what the value represents. If the metric or expression is shown
              in a CloudWatch dashboard widget, the label is shown. If Label is omitted, CloudWatch
              generates a default.

            - **ReturnData** *(boolean) --*

              When used in ``GetMetricData`` , this option indicates whether to return the timestamps and
              raw data values of this metric. If you are performing this call just to do math expressions
              and do not also need the raw data returned, you can specify ``False`` . If you omit this, the
              default of ``True`` is used.

              When used in ``PutMetricAlarm`` , specify ``True`` for the one expression result to use as
              the alarm. For all other metrics and expressions in the same ``PutMetricAlarm`` operation,
              specify ``ReturnData`` as False.

            - **Period** *(integer) --*

              The granularity, in seconds, of the returned data points. For metrics with regular
              resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60.
              For high-resolution metrics that are collected at intervals of less than one minute, the
              period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those
              metrics stored by a ``PutMetricData`` operation that includes a ``StorageResolution of 1
              second`` .

              Use this field only when you are performing a ``GetMetricData`` operation, and only when you
              are specifying the ``Expression`` field. Do not use this field with a ``PutMetricAlarm``
              operation or when you are specifying a ``MetricStat`` in a ``GetMetricData`` operation.

        :type Tags: list
        :param Tags:

          A list of key-value pairs to associate with the alarm. You can associate as many as 50 tags with
          an alarm.

          Tags can help you organize and categorize your resources. You can also use them to scope user
          permissions, by granting a user permission to access or change only resources with certain tag
          values.

          - *(dict) --*

            A key-value pair associated with a CloudWatch resource.

            - **Key** *(string) --* **[REQUIRED]**

              A string that you can use to assign a value. The combination of tag keys and values can help
              you organize and categorize your resources.

            - **Value** *(string) --* **[REQUIRED]**

              The value for the specified tag key.

        :type ThresholdMetricId: string
        :param ThresholdMetricId:

          If this is an alarm based on an anomaly detection model, make this value match the ID of the
          ``ANOMALY_DETECTION_BAND`` function.

          For an example of how to use this parameter, see the **Anomaly Detection Model Alarm** example on
          this page.

          If your alarm uses this parameter, it cannot have Auto Scaling actions.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_metric_data(
        self, Namespace: str, MetricData: List[ClientPutMetricDataMetricDataTypeDef]
    ) -> None:
        """
        Publishes metric data points to Amazon CloudWatch. CloudWatch associates the data points with the
        specified metric. If the specified metric does not exist, CloudWatch creates the metric. When
        CloudWatch creates a metric, it can take up to fifteen minutes for the metric to appear in calls to
         ListMetrics .

        You can publish either individual data points in the ``Value`` field, or arrays of values and the
        number of times each value occurred during the period by using the ``Values`` and ``Counts`` fields
        in the ``MetricDatum`` structure. Using the ``Values`` and ``Counts`` method enables you to publish
        up to 150 values per metric with one ``PutMetricData`` request, and supports retrieving percentile
        statistics on this data.

        Each ``PutMetricData`` request is limited to 40 KB in size for HTTP POST requests. You can send a
        payload compressed by gzip. Each request is also limited to no more than 20 different metrics.

        Although the ``Value`` parameter accepts numbers of type ``Double`` , CloudWatch rejects values
        that are either too small or too large. Values must be in the range of 8.515920e-109 to
        1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2). In addition, special values (for example, NaN,
        +Infinity, -Infinity) are not supported.

        You can use up to 10 dimensions per metric to further clarify what data the metric collects. Each
        dimension consists of a Name and Value pair. For more information about specifying dimensions, see
        `Publishing Metrics
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html>`__ in the
        *Amazon CloudWatch User Guide* .

        Data points with time stamps from 24 hours ago or longer can take at least 48 hours to become
        available for  GetMetricData or  GetMetricStatistics from the time they are submitted.

        CloudWatch needs raw data points to calculate percentile statistics. If you publish data using a
        statistic set instead, you can only retrieve percentile statistics for this data if one of the
        following conditions is true:

        * The ``SampleCount`` value of the statistic set is 1 and ``Min`` , ``Max`` , and ``Sum`` are all
        equal.

        * The ``Min`` and ``Max`` are equal, and ``Sum`` is equal to ``Min`` multiplied by ``SampleCount`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/PutMetricData>`_

        **Request Syntax**
        ::

          response = client.put_metric_data(
              Namespace='string',
              MetricData=[
                  {
                      'MetricName': 'string',
                      'Dimensions': [
                          {
                              'Name': 'string',
                              'Value': 'string'
                          },
                      ],
                      'Timestamp': datetime(2015, 1, 1),
                      'Value': 123.0,
                      'StatisticValues': {
                          'SampleCount': 123.0,
                          'Sum': 123.0,
                          'Minimum': 123.0,
                          'Maximum': 123.0
                      },
                      'Values': [
                          123.0,
                      ],
                      'Counts': [
                          123.0,
                      ],
                      'Unit':
                      'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'
                      |'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'
                      |'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'
                      |'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'
                      |'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
                      'StorageResolution': 123
                  },
              ]
          )
        :type Namespace: string
        :param Namespace: **[REQUIRED]**

          The namespace for the metric data.

          To avoid conflicts with AWS service namespaces, you should not specify a namespace that begins
          with ``AWS/``

        :type MetricData: list
        :param MetricData: **[REQUIRED]**

          The data for the metric. The array can include no more than 20 metrics per call.

          - *(dict) --*

            Encapsulates the information sent to either create a metric or add new values to be aggregated
            into an existing metric.

            - **MetricName** *(string) --* **[REQUIRED]**

              The name of the metric.

            - **Dimensions** *(list) --*

              The dimensions associated with the metric.

              - *(dict) --*

                Expands the identity of a metric.

                - **Name** *(string) --* **[REQUIRED]**

                  The name of the dimension.

                - **Value** *(string) --* **[REQUIRED]**

                  The value representing the dimension measurement.

            - **Timestamp** *(datetime) --*

              The time the metric data was received, expressed as the number of milliseconds since Jan 1,
              1970 00:00:00 UTC.

            - **Value** *(float) --*

              The value for the metric.

              Although the parameter accepts numbers of type Double, CloudWatch rejects values that are
              either too small or too large. Values must be in the range of 8.515920e-109 to 1.174271e+108
              (Base 10) or 2e-360 to 2e360 (Base 2). In addition, special values (for example, NaN,
              +Infinity, -Infinity) are not supported.

            - **StatisticValues** *(dict) --*

              The statistical values for the metric.

              - **SampleCount** *(float) --* **[REQUIRED]**

                The number of samples used for the statistic set.

              - **Sum** *(float) --* **[REQUIRED]**

                The sum of values for the sample set.

              - **Minimum** *(float) --* **[REQUIRED]**

                The minimum value of the sample set.

              - **Maximum** *(float) --* **[REQUIRED]**

                The maximum value of the sample set.

            - **Values** *(list) --*

              Array of numbers representing the values for the metric during the period. Each unique value
              is listed just once in this array, and the corresponding number in the ``Counts`` array
              specifies the number of times that value occurred during the period. You can include up to
              150 unique values in each ``PutMetricData`` action that specifies a ``Values`` array.

              Although the ``Values`` array accepts numbers of type ``Double`` , CloudWatch rejects values
              that are either too small or too large. Values must be in the range of 8.515920e-109 to
              1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2). In addition, special values (for
              example, NaN, +Infinity, -Infinity) are not supported.

              - *(float) --*

            - **Counts** *(list) --*

              Array of numbers that is used along with the ``Values`` array. Each number in the ``Count``
              array is the number of times the corresponding value in the ``Values`` array occurred during
              the period.

              If you omit the ``Counts`` array, the default of 1 is used as the value for each count. If
              you include a ``Counts`` array, it must include the same amount of values as the ``Values``
              array.

              - *(float) --*

            - **Unit** *(string) --*

              When you are using a ``Put`` operation, this defines what unit you want to use when storing
              the metric.

              In a ``Get`` operation, this displays the unit that is used for the metric.

            - **StorageResolution** *(integer) --*

              Valid values are 1 and 60. Setting this to 1 specifies this metric as a high-resolution
              metric, so that CloudWatch stores the metric with sub-minute resolution down to one second.
              Setting this to 60 specifies this metric as a regular-resolution metric, which CloudWatch
              stores at 1-minute resolution. Currently, high resolution is available only for custom
              metrics. For more information about high-resolution metrics, see `High-Resolution Metrics
              <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html#high-resolution-metrics>`__
              in the *Amazon CloudWatch User Guide* .

              This field is optional, if you do not specify it the default of 60 is used.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_alarm_state(
        self,
        AlarmName: str,
        StateValue: str,
        StateReason: str,
        StateReasonData: str = None,
    ) -> None:
        """
        Temporarily sets the state of an alarm for testing purposes. When the updated state differs from
        the previous value, the action configured for the appropriate state is invoked. For example, if
        your alarm is configured to send an Amazon SNS message when an alarm is triggered, temporarily
        changing the alarm state to ``ALARM`` sends an SNS message. The alarm returns to its actual state
        (often within seconds). Because the alarm state change happens quickly, it is typically only
        visible in the alarm's **History** tab in the Amazon CloudWatch console or through
        DescribeAlarmHistory .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/SetAlarmState>`_

        **Request Syntax**
        ::

          response = client.set_alarm_state(
              AlarmName='string',
              StateValue='OK'|'ALARM'|'INSUFFICIENT_DATA',
              StateReason='string',
              StateReasonData='string'
          )
        :type AlarmName: string
        :param AlarmName: **[REQUIRED]**

          The name for the alarm. This name must be unique within the AWS account. The maximum length is
          255 characters.

        :type StateValue: string
        :param StateValue: **[REQUIRED]**

          The value of the state.

        :type StateReason: string
        :param StateReason: **[REQUIRED]**

          The reason that this alarm is set to this specific state, in text format.

        :type StateReasonData: string
        :param StateReasonData:

          The reason that this alarm is set to this specific state, in JSON format.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(
        self, ResourceARN: str, Tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified CloudWatch resource. Currently, the
        only CloudWatch resources that can be tagged are alarms.

        Tags can help you organize and categorize your resources. You can also use them to scope user
        permissions, by granting a user permission to access or change only resources with certain tag
        values.

        Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters.

        You can use the ``TagResource`` action with an alarm that already has tags. If you specify a new
        tag key for the alarm, this tag is appended to the list of tags associated with the alarm. If you
        specify a tag key that is already associated with the alarm, the new tag value that you specify
        replaces the previous value for that tag.

        You can associate as many as 50 tags with a resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/TagResource>`_

        **Request Syntax**
        ::

          response = client.tag_resource(
              ResourceARN='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type ResourceARN: string
        :param ResourceARN: **[REQUIRED]**

          The ARN of the CloudWatch alarm that you're adding tags to. The ARN format is
          ``arn:aws:cloudwatch:*Region* :*account-id* :alarm:*alarm-name* ``

        :type Tags: list
        :param Tags: **[REQUIRED]**

          The list of key-value pairs to associate with the alarm.

          - *(dict) --*

            A key-value pair associated with a CloudWatch resource.

            - **Key** *(string) --* **[REQUIRED]**

              A string that you can use to assign a value. The combination of tag keys and values can help
              you organize and categorize your resources.

            - **Value** *(string) --* **[REQUIRED]**

              The value for the specified tag key.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from the specified resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/UntagResource>`_

        **Request Syntax**
        ::

          response = client.untag_resource(
              ResourceARN='string',
              TagKeys=[
                  'string',
              ]
          )
        :type ResourceARN: string
        :param ResourceARN: **[REQUIRED]**

          The ARN of the CloudWatch resource that you're removing tags from. For more information on ARN
          format, see `Example ARNs
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-cloudwatch>`__
          in the *Amazon Web Services General Reference* .

        :type TagKeys: list
        :param TagKeys: **[REQUIRED]**

          The list of tag keys to remove from the resource.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_alarm_history"]
    ) -> paginator_scope.DescribeAlarmHistoryPaginator:
        """
        Get Paginator for `describe_alarm_history` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_alarms"]
    ) -> paginator_scope.DescribeAlarmsPaginator:
        """
        Get Paginator for `describe_alarms` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_metric_data"]
    ) -> paginator_scope.GetMetricDataPaginator:
        """
        Get Paginator for `get_metric_data` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_dashboards"]
    ) -> paginator_scope.ListDashboardsPaginator:
        """
        Get Paginator for `list_dashboards` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_metrics"]
    ) -> paginator_scope.ListMetricsPaginator:
        """
        Get Paginator for `list_metrics` operation.
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

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["alarm_exists"]
    ) -> waiter_scope.AlarmExistsWaiter:
        """
        Get Waiter `alarm_exists`.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(self, waiter_name: str) -> Boto3Waiter:
        """
        Returns an object that can wait for some condition.

        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.

        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """


class Exceptions:
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    DashboardInvalidInputError: Boto3ClientError
    DashboardNotFoundError: Boto3ClientError
    InternalServiceFault: Boto3ClientError
    InvalidFormatFault: Boto3ClientError
    InvalidNextToken: Boto3ClientError
    InvalidParameterCombinationException: Boto3ClientError
    InvalidParameterValueException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    LimitExceededFault: Boto3ClientError
    MissingRequiredParameterException: Boto3ClientError
    ResourceNotFound: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
