"Main interface for cloudwatch type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "AlarmDescribeHistoryResponseAlarmHistoryItemsTypeDef",
    "AlarmDescribeHistoryResponseTypeDef",
    "AlarmExistsWaitWaiterConfigTypeDef",
    "AlarmsFilterDimensionsTypeDef",
    "ClientDeleteAnomalyDetectorDimensionsTypeDef",
    "ClientDescribeAlarmHistoryResponseAlarmHistoryItemsTypeDef",
    "ClientDescribeAlarmHistoryResponseTypeDef",
    "ClientDescribeAlarmsForMetricDimensionsTypeDef",
    "ClientDescribeAlarmsForMetricResponseMetricAlarmsDimensionsTypeDef",
    "ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef",
    "ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricTypeDef",
    "ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatTypeDef",
    "ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsTypeDef",
    "ClientDescribeAlarmsForMetricResponseMetricAlarmsTypeDef",
    "ClientDescribeAlarmsForMetricResponseTypeDef",
    "ClientDescribeAlarmsResponseMetricAlarmsDimensionsTypeDef",
    "ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef",
    "ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricTypeDef",
    "ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatTypeDef",
    "ClientDescribeAlarmsResponseMetricAlarmsMetricsTypeDef",
    "ClientDescribeAlarmsResponseMetricAlarmsTypeDef",
    "ClientDescribeAlarmsResponseTypeDef",
    "ClientDescribeAnomalyDetectorsDimensionsTypeDef",
    "ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationExcludedTimeRangesTypeDef",
    "ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationTypeDef",
    "ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsDimensionsTypeDef",
    "ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsTypeDef",
    "ClientDescribeAnomalyDetectorsResponseTypeDef",
    "ClientGetDashboardResponseTypeDef",
    "ClientGetMetricDataMetricDataQueriesMetricStatMetricDimensionsTypeDef",
    "ClientGetMetricDataMetricDataQueriesMetricStatMetricTypeDef",
    "ClientGetMetricDataMetricDataQueriesMetricStatTypeDef",
    "ClientGetMetricDataMetricDataQueriesTypeDef",
    "ClientGetMetricDataResponseMessagesTypeDef",
    "ClientGetMetricDataResponseMetricDataResultsMessagesTypeDef",
    "ClientGetMetricDataResponseMetricDataResultsTypeDef",
    "ClientGetMetricDataResponseTypeDef",
    "ClientGetMetricStatisticsDimensionsTypeDef",
    "ClientGetMetricStatisticsResponseDatapointsTypeDef",
    "ClientGetMetricStatisticsResponseTypeDef",
    "ClientGetMetricWidgetImageResponseTypeDef",
    "ClientListDashboardsResponseDashboardEntriesTypeDef",
    "ClientListDashboardsResponseTypeDef",
    "ClientListMetricsDimensionsTypeDef",
    "ClientListMetricsResponseMetricsDimensionsTypeDef",
    "ClientListMetricsResponseMetricsTypeDef",
    "ClientListMetricsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutAnomalyDetectorConfigurationExcludedTimeRangesTypeDef",
    "ClientPutAnomalyDetectorConfigurationTypeDef",
    "ClientPutAnomalyDetectorDimensionsTypeDef",
    "ClientPutDashboardResponseDashboardValidationMessagesTypeDef",
    "ClientPutDashboardResponseTypeDef",
    "ClientPutMetricAlarmDimensionsTypeDef",
    "ClientPutMetricAlarmMetricsMetricStatMetricDimensionsTypeDef",
    "ClientPutMetricAlarmMetricsMetricStatMetricTypeDef",
    "ClientPutMetricAlarmMetricsMetricStatTypeDef",
    "ClientPutMetricAlarmMetricsTypeDef",
    "ClientPutMetricAlarmTagsTypeDef",
    "ClientPutMetricDataMetricDataDimensionsTypeDef",
    "ClientPutMetricDataMetricDataStatisticValuesTypeDef",
    "ClientPutMetricDataMetricDataTypeDef",
    "ClientTagResourceTagsTypeDef",
    "DescribeAlarmHistoryPaginatePaginationConfigTypeDef",
    "DescribeAlarmHistoryPaginateResponseAlarmHistoryItemsTypeDef",
    "DescribeAlarmHistoryPaginateResponseTypeDef",
    "DescribeAlarmsPaginatePaginationConfigTypeDef",
    "DescribeAlarmsPaginateResponseMetricAlarmsDimensionsTypeDef",
    "DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef",
    "DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatMetricTypeDef",
    "DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatTypeDef",
    "DescribeAlarmsPaginateResponseMetricAlarmsMetricsTypeDef",
    "DescribeAlarmsPaginateResponseMetricAlarmsTypeDef",
    "DescribeAlarmsPaginateResponseTypeDef",
    "GetMetricDataPaginateMetricDataQueriesMetricStatMetricDimensionsTypeDef",
    "GetMetricDataPaginateMetricDataQueriesMetricStatMetricTypeDef",
    "GetMetricDataPaginateMetricDataQueriesMetricStatTypeDef",
    "GetMetricDataPaginateMetricDataQueriesTypeDef",
    "GetMetricDataPaginatePaginationConfigTypeDef",
    "GetMetricDataPaginateResponseMessagesTypeDef",
    "GetMetricDataPaginateResponseMetricDataResultsMessagesTypeDef",
    "GetMetricDataPaginateResponseMetricDataResultsTypeDef",
    "GetMetricDataPaginateResponseTypeDef",
    "ListDashboardsPaginatePaginationConfigTypeDef",
    "ListDashboardsPaginateResponseDashboardEntriesTypeDef",
    "ListDashboardsPaginateResponseTypeDef",
    "ListMetricsPaginateDimensionsTypeDef",
    "ListMetricsPaginatePaginationConfigTypeDef",
    "ListMetricsPaginateResponseMetricsDimensionsTypeDef",
    "ListMetricsPaginateResponseMetricsTypeDef",
    "ListMetricsPaginateResponseTypeDef",
    "MetricGetStatisticsDimensionsTypeDef",
    "MetricGetStatisticsResponseDatapointsTypeDef",
    "MetricGetStatisticsResponseTypeDef",
    "MetricPutAlarmDimensionsTypeDef",
    "MetricPutAlarmMetricsMetricStatMetricDimensionsTypeDef",
    "MetricPutAlarmMetricsMetricStatMetricTypeDef",
    "MetricPutAlarmMetricsMetricStatTypeDef",
    "MetricPutAlarmMetricsTypeDef",
    "MetricPutAlarmTagsTypeDef",
    "MetricsFilterDimensionsTypeDef",
)


_AlarmDescribeHistoryResponseAlarmHistoryItemsTypeDef = TypedDict(
    "_AlarmDescribeHistoryResponseAlarmHistoryItemsTypeDef",
    {
        "AlarmName": str,
        "Timestamp": datetime,
        "HistoryItemType": str,
        "HistorySummary": str,
        "HistoryData": str,
    },
    total=False,
)


class AlarmDescribeHistoryResponseAlarmHistoryItemsTypeDef(
    _AlarmDescribeHistoryResponseAlarmHistoryItemsTypeDef
):
    """
    Type definition for `AlarmDescribeHistoryResponse` `AlarmHistoryItems`

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
    """


_AlarmDescribeHistoryResponseTypeDef = TypedDict(
    "_AlarmDescribeHistoryResponseTypeDef",
    {
        "AlarmHistoryItems": List[AlarmDescribeHistoryResponseAlarmHistoryItemsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class AlarmDescribeHistoryResponseTypeDef(_AlarmDescribeHistoryResponseTypeDef):
    """
    Type definition for `AlarmDescribeHistory` `Response`

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


_AlarmExistsWaitWaiterConfigTypeDef = TypedDict(
    "_AlarmExistsWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class AlarmExistsWaitWaiterConfigTypeDef(_AlarmExistsWaitWaiterConfigTypeDef):
    """
    Type definition for `AlarmExistsWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 5

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 40
    """


_AlarmsFilterDimensionsTypeDef = TypedDict(
    "_AlarmsFilterDimensionsTypeDef", {"Name": str, "Value": str}
)


class AlarmsFilterDimensionsTypeDef(_AlarmsFilterDimensionsTypeDef):
    """
    Type definition for `AlarmsFilter` `Dimensions`

    Expands the identity of a metric.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the dimension.

    - **Value** *(string) --* **[REQUIRED]**

      The value representing the dimension measurement.
    """


_ClientDeleteAnomalyDetectorDimensionsTypeDef = TypedDict(
    "_ClientDeleteAnomalyDetectorDimensionsTypeDef", {"Name": str, "Value": str}
)


class ClientDeleteAnomalyDetectorDimensionsTypeDef(
    _ClientDeleteAnomalyDetectorDimensionsTypeDef
):
    """
    Type definition for `ClientDeleteAnomalyDetector` `Dimensions`

    Expands the identity of a metric.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the dimension.

    - **Value** *(string) --* **[REQUIRED]**

      The value representing the dimension measurement.
    """


_ClientDescribeAlarmHistoryResponseAlarmHistoryItemsTypeDef = TypedDict(
    "_ClientDescribeAlarmHistoryResponseAlarmHistoryItemsTypeDef",
    {
        "AlarmName": str,
        "Timestamp": datetime,
        "HistoryItemType": str,
        "HistorySummary": str,
        "HistoryData": str,
    },
    total=False,
)


class ClientDescribeAlarmHistoryResponseAlarmHistoryItemsTypeDef(
    _ClientDescribeAlarmHistoryResponseAlarmHistoryItemsTypeDef
):
    """
    Type definition for `ClientDescribeAlarmHistoryResponse` `AlarmHistoryItems`

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
    """


_ClientDescribeAlarmHistoryResponseTypeDef = TypedDict(
    "_ClientDescribeAlarmHistoryResponseTypeDef",
    {
        "AlarmHistoryItems": List[
            ClientDescribeAlarmHistoryResponseAlarmHistoryItemsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeAlarmHistoryResponseTypeDef(
    _ClientDescribeAlarmHistoryResponseTypeDef
):
    """
    Type definition for `ClientDescribeAlarmHistory` `Response`

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


_ClientDescribeAlarmsForMetricDimensionsTypeDef = TypedDict(
    "_ClientDescribeAlarmsForMetricDimensionsTypeDef", {"Name": str, "Value": str}
)


class ClientDescribeAlarmsForMetricDimensionsTypeDef(
    _ClientDescribeAlarmsForMetricDimensionsTypeDef
):
    """
    Type definition for `ClientDescribeAlarmsForMetric` `Dimensions`

    Expands the identity of a metric.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the dimension.

    - **Value** *(string) --* **[REQUIRED]**

      The value representing the dimension measurement.
    """


_ClientDescribeAlarmsForMetricResponseMetricAlarmsDimensionsTypeDef = TypedDict(
    "_ClientDescribeAlarmsForMetricResponseMetricAlarmsDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientDescribeAlarmsForMetricResponseMetricAlarmsDimensionsTypeDef(
    _ClientDescribeAlarmsForMetricResponseMetricAlarmsDimensionsTypeDef
):
    """
    Type definition for `ClientDescribeAlarmsForMetricResponseMetricAlarms` `Dimensions`

    Expands the identity of a metric.

    - **Name** *(string) --*

      The name of the dimension.

    - **Value** *(string) --*

      The value representing the dimension measurement.
    """


_ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef = TypedDict(
    "_ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef(
    _ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef
):
    """
    Type definition for `ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetric` `Dimensions`

    Expands the identity of a metric.

    - **Name** *(string) --*

      The name of the dimension.

    - **Value** *(string) --*

      The value representing the dimension measurement.
    """


_ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricTypeDef = TypedDict(
    "_ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[
            ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricTypeDef(
    _ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricTypeDef
):
    """
    Type definition for `ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStat` `Metric`

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
    """


_ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatTypeDef = TypedDict(
    "_ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatTypeDef",
    {
        "Metric": ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricTypeDef,
        "Period": int,
        "Stat": str,
        "Unit": str,
    },
    total=False,
)


class ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatTypeDef(
    _ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatTypeDef
):
    """
    Type definition for `ClientDescribeAlarmsForMetricResponseMetricAlarmsMetrics` `MetricStat`

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
    """


_ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsTypeDef = TypedDict(
    "_ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsTypeDef",
    {
        "Id": str,
        "MetricStat": ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatTypeDef,
        "Expression": str,
        "Label": str,
        "ReturnData": bool,
        "Period": int,
    },
    total=False,
)


class ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsTypeDef(
    _ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsTypeDef
):
    """
    Type definition for `ClientDescribeAlarmsForMetricResponseMetricAlarms` `Metrics`

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
    """


_ClientDescribeAlarmsForMetricResponseMetricAlarmsTypeDef = TypedDict(
    "_ClientDescribeAlarmsForMetricResponseMetricAlarmsTypeDef",
    {
        "AlarmName": str,
        "AlarmArn": str,
        "AlarmDescription": str,
        "AlarmConfigurationUpdatedTimestamp": datetime,
        "ActionsEnabled": bool,
        "OKActions": List[str],
        "AlarmActions": List[str],
        "InsufficientDataActions": List[str],
        "StateValue": str,
        "StateReason": str,
        "StateReasonData": str,
        "StateUpdatedTimestamp": datetime,
        "MetricName": str,
        "Namespace": str,
        "Statistic": str,
        "ExtendedStatistic": str,
        "Dimensions": List[
            ClientDescribeAlarmsForMetricResponseMetricAlarmsDimensionsTypeDef
        ],
        "Period": int,
        "Unit": str,
        "EvaluationPeriods": int,
        "DatapointsToAlarm": int,
        "Threshold": float,
        "ComparisonOperator": str,
        "TreatMissingData": str,
        "EvaluateLowSampleCountPercentile": str,
        "Metrics": List[
            ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsTypeDef
        ],
        "ThresholdMetricId": str,
    },
    total=False,
)


class ClientDescribeAlarmsForMetricResponseMetricAlarmsTypeDef(
    _ClientDescribeAlarmsForMetricResponseMetricAlarmsTypeDef
):
    """
    Type definition for `ClientDescribeAlarmsForMetricResponse` `MetricAlarms`

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


_ClientDescribeAlarmsForMetricResponseTypeDef = TypedDict(
    "_ClientDescribeAlarmsForMetricResponseTypeDef",
    {"MetricAlarms": List[ClientDescribeAlarmsForMetricResponseMetricAlarmsTypeDef]},
    total=False,
)


class ClientDescribeAlarmsForMetricResponseTypeDef(
    _ClientDescribeAlarmsForMetricResponseTypeDef
):
    """
    Type definition for `ClientDescribeAlarmsForMetric` `Response`

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


_ClientDescribeAlarmsResponseMetricAlarmsDimensionsTypeDef = TypedDict(
    "_ClientDescribeAlarmsResponseMetricAlarmsDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientDescribeAlarmsResponseMetricAlarmsDimensionsTypeDef(
    _ClientDescribeAlarmsResponseMetricAlarmsDimensionsTypeDef
):
    """
    Type definition for `ClientDescribeAlarmsResponseMetricAlarms` `Dimensions`

    Expands the identity of a metric.

    - **Name** *(string) --*

      The name of the dimension.

    - **Value** *(string) --*

      The value representing the dimension measurement.
    """


_ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef = TypedDict(
    "_ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef(
    _ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef
):
    """
    Type definition for `ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetric` `Dimensions`

    Expands the identity of a metric.

    - **Name** *(string) --*

      The name of the dimension.

    - **Value** *(string) --*

      The value representing the dimension measurement.
    """


_ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricTypeDef = TypedDict(
    "_ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[
            ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricTypeDef(
    _ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricTypeDef
):
    """
    Type definition for `ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStat` `Metric`

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
    """


_ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatTypeDef = TypedDict(
    "_ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatTypeDef",
    {
        "Metric": ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricTypeDef,
        "Period": int,
        "Stat": str,
        "Unit": str,
    },
    total=False,
)


class ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatTypeDef(
    _ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatTypeDef
):
    """
    Type definition for `ClientDescribeAlarmsResponseMetricAlarmsMetrics` `MetricStat`

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
    """


_ClientDescribeAlarmsResponseMetricAlarmsMetricsTypeDef = TypedDict(
    "_ClientDescribeAlarmsResponseMetricAlarmsMetricsTypeDef",
    {
        "Id": str,
        "MetricStat": ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatTypeDef,
        "Expression": str,
        "Label": str,
        "ReturnData": bool,
        "Period": int,
    },
    total=False,
)


class ClientDescribeAlarmsResponseMetricAlarmsMetricsTypeDef(
    _ClientDescribeAlarmsResponseMetricAlarmsMetricsTypeDef
):
    """
    Type definition for `ClientDescribeAlarmsResponseMetricAlarms` `Metrics`

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
    """


_ClientDescribeAlarmsResponseMetricAlarmsTypeDef = TypedDict(
    "_ClientDescribeAlarmsResponseMetricAlarmsTypeDef",
    {
        "AlarmName": str,
        "AlarmArn": str,
        "AlarmDescription": str,
        "AlarmConfigurationUpdatedTimestamp": datetime,
        "ActionsEnabled": bool,
        "OKActions": List[str],
        "AlarmActions": List[str],
        "InsufficientDataActions": List[str],
        "StateValue": str,
        "StateReason": str,
        "StateReasonData": str,
        "StateUpdatedTimestamp": datetime,
        "MetricName": str,
        "Namespace": str,
        "Statistic": str,
        "ExtendedStatistic": str,
        "Dimensions": List[ClientDescribeAlarmsResponseMetricAlarmsDimensionsTypeDef],
        "Period": int,
        "Unit": str,
        "EvaluationPeriods": int,
        "DatapointsToAlarm": int,
        "Threshold": float,
        "ComparisonOperator": str,
        "TreatMissingData": str,
        "EvaluateLowSampleCountPercentile": str,
        "Metrics": List[ClientDescribeAlarmsResponseMetricAlarmsMetricsTypeDef],
        "ThresholdMetricId": str,
    },
    total=False,
)


class ClientDescribeAlarmsResponseMetricAlarmsTypeDef(
    _ClientDescribeAlarmsResponseMetricAlarmsTypeDef
):
    """
    Type definition for `ClientDescribeAlarmsResponse` `MetricAlarms`

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


_ClientDescribeAlarmsResponseTypeDef = TypedDict(
    "_ClientDescribeAlarmsResponseTypeDef",
    {
        "MetricAlarms": List[ClientDescribeAlarmsResponseMetricAlarmsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeAlarmsResponseTypeDef(_ClientDescribeAlarmsResponseTypeDef):
    """
    Type definition for `ClientDescribeAlarms` `Response`

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


_ClientDescribeAnomalyDetectorsDimensionsTypeDef = TypedDict(
    "_ClientDescribeAnomalyDetectorsDimensionsTypeDef", {"Name": str, "Value": str}
)


class ClientDescribeAnomalyDetectorsDimensionsTypeDef(
    _ClientDescribeAnomalyDetectorsDimensionsTypeDef
):
    """
    Type definition for `ClientDescribeAnomalyDetectors` `Dimensions`

    Expands the identity of a metric.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the dimension.

    - **Value** *(string) --* **[REQUIRED]**

      The value representing the dimension measurement.
    """


_ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationExcludedTimeRangesTypeDef = TypedDict(
    "_ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationExcludedTimeRangesTypeDef",
    {"StartTime": datetime, "EndTime": datetime},
    total=False,
)


class ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationExcludedTimeRangesTypeDef(
    _ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationExcludedTimeRangesTypeDef
):
    """
    Type definition for `ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfiguration` `ExcludedTimeRanges`

    Specifies one range of days or times to exclude from use for training an anomaly
    detection model.

    - **StartTime** *(datetime) --*

      The start time of the range to exclude. The format is ``yyyy-MM-dd'T'HH:mm:ss`` .
      For example, ``2019-07-01T23:59:59`` .

    - **EndTime** *(datetime) --*

      The end time of the range to exclude. The format is ``yyyy-MM-dd'T'HH:mm:ss`` . For
      example, ``2019-07-01T23:59:59`` .
    """


_ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationTypeDef = TypedDict(
    "_ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationTypeDef",
    {
        "ExcludedTimeRanges": List[
            ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationExcludedTimeRangesTypeDef
        ],
        "MetricTimezone": str,
    },
    total=False,
)


class ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationTypeDef(
    _ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeAnomalyDetectorsResponseAnomalyDetectors` `Configuration`

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
    """


_ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsDimensionsTypeDef = TypedDict(
    "_ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsDimensionsTypeDef(
    _ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsDimensionsTypeDef
):
    """
    Type definition for `ClientDescribeAnomalyDetectorsResponseAnomalyDetectors` `Dimensions`

    Expands the identity of a metric.

    - **Name** *(string) --*

      The name of the dimension.

    - **Value** *(string) --*

      The value representing the dimension measurement.
    """


_ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsTypeDef = TypedDict(
    "_ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[
            ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsDimensionsTypeDef
        ],
        "Stat": str,
        "Configuration": ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsTypeDef(
    _ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsTypeDef
):
    """
    Type definition for `ClientDescribeAnomalyDetectorsResponse` `AnomalyDetectors`

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
    """


_ClientDescribeAnomalyDetectorsResponseTypeDef = TypedDict(
    "_ClientDescribeAnomalyDetectorsResponseTypeDef",
    {
        "AnomalyDetectors": List[
            ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeAnomalyDetectorsResponseTypeDef(
    _ClientDescribeAnomalyDetectorsResponseTypeDef
):
    """
    Type definition for `ClientDescribeAnomalyDetectors` `Response`

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


_ClientGetDashboardResponseTypeDef = TypedDict(
    "_ClientGetDashboardResponseTypeDef",
    {"DashboardArn": str, "DashboardBody": str, "DashboardName": str},
    total=False,
)


class ClientGetDashboardResponseTypeDef(_ClientGetDashboardResponseTypeDef):
    """
    Type definition for `ClientGetDashboard` `Response`

    - **DashboardArn** *(string) --*

      The Amazon Resource Name (ARN) of the dashboard.

    - **DashboardBody** *(string) --*

      The detailed information about the dashboard, including what widgets are included and their
      location on the dashboard. For more information about the ``DashboardBody`` syntax, see
      CloudWatch-Dashboard-Body-Structure .

    - **DashboardName** *(string) --*

      The name of the dashboard.
    """


_ClientGetMetricDataMetricDataQueriesMetricStatMetricDimensionsTypeDef = TypedDict(
    "_ClientGetMetricDataMetricDataQueriesMetricStatMetricDimensionsTypeDef",
    {"Name": str, "Value": str},
)


class ClientGetMetricDataMetricDataQueriesMetricStatMetricDimensionsTypeDef(
    _ClientGetMetricDataMetricDataQueriesMetricStatMetricDimensionsTypeDef
):
    """
    Type definition for `ClientGetMetricDataMetricDataQueriesMetricStatMetric` `Dimensions`

    Expands the identity of a metric.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the dimension.

    - **Value** *(string) --* **[REQUIRED]**

      The value representing the dimension measurement.
    """


_ClientGetMetricDataMetricDataQueriesMetricStatMetricTypeDef = TypedDict(
    "_ClientGetMetricDataMetricDataQueriesMetricStatMetricTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[
            ClientGetMetricDataMetricDataQueriesMetricStatMetricDimensionsTypeDef
        ],
    },
    total=False,
)


class ClientGetMetricDataMetricDataQueriesMetricStatMetricTypeDef(
    _ClientGetMetricDataMetricDataQueriesMetricStatMetricTypeDef
):
    """
    Type definition for `ClientGetMetricDataMetricDataQueriesMetricStat` `Metric`

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
    """


_RequiredClientGetMetricDataMetricDataQueriesMetricStatTypeDef = TypedDict(
    "_RequiredClientGetMetricDataMetricDataQueriesMetricStatTypeDef",
    {
        "Metric": ClientGetMetricDataMetricDataQueriesMetricStatMetricTypeDef,
        "Period": int,
        "Stat": str,
    },
)
_OptionalClientGetMetricDataMetricDataQueriesMetricStatTypeDef = TypedDict(
    "_OptionalClientGetMetricDataMetricDataQueriesMetricStatTypeDef",
    {"Unit": str},
    total=False,
)


class ClientGetMetricDataMetricDataQueriesMetricStatTypeDef(
    _RequiredClientGetMetricDataMetricDataQueriesMetricStatTypeDef,
    _OptionalClientGetMetricDataMetricDataQueriesMetricStatTypeDef,
):
    """
    Type definition for `ClientGetMetricDataMetricDataQueries` `MetricStat`

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
    """


_RequiredClientGetMetricDataMetricDataQueriesTypeDef = TypedDict(
    "_RequiredClientGetMetricDataMetricDataQueriesTypeDef", {"Id": str}
)
_OptionalClientGetMetricDataMetricDataQueriesTypeDef = TypedDict(
    "_OptionalClientGetMetricDataMetricDataQueriesTypeDef",
    {
        "MetricStat": ClientGetMetricDataMetricDataQueriesMetricStatTypeDef,
        "Expression": str,
        "Label": str,
        "ReturnData": bool,
        "Period": int,
    },
    total=False,
)


class ClientGetMetricDataMetricDataQueriesTypeDef(
    _RequiredClientGetMetricDataMetricDataQueriesTypeDef,
    _OptionalClientGetMetricDataMetricDataQueriesTypeDef,
):
    """
    Type definition for `ClientGetMetricData` `MetricDataQueries`

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
    """


_ClientGetMetricDataResponseMessagesTypeDef = TypedDict(
    "_ClientGetMetricDataResponseMessagesTypeDef",
    {"Code": str, "Value": str},
    total=False,
)


class ClientGetMetricDataResponseMessagesTypeDef(
    _ClientGetMetricDataResponseMessagesTypeDef
):
    """
    Type definition for `ClientGetMetricDataResponse` `Messages`

    A message returned by the ``GetMetricData`` API, including a code and a description.

    - **Code** *(string) --*

      The error code or status code associated with the message.

    - **Value** *(string) --*

      The message text.
    """


_ClientGetMetricDataResponseMetricDataResultsMessagesTypeDef = TypedDict(
    "_ClientGetMetricDataResponseMetricDataResultsMessagesTypeDef",
    {"Code": str, "Value": str},
    total=False,
)


class ClientGetMetricDataResponseMetricDataResultsMessagesTypeDef(
    _ClientGetMetricDataResponseMetricDataResultsMessagesTypeDef
):
    """
    Type definition for `ClientGetMetricDataResponseMetricDataResults` `Messages`

    A message returned by the ``GetMetricData`` API, including a code and a description.

    - **Code** *(string) --*

      The error code or status code associated with the message.

    - **Value** *(string) --*

      The message text.
    """


_ClientGetMetricDataResponseMetricDataResultsTypeDef = TypedDict(
    "_ClientGetMetricDataResponseMetricDataResultsTypeDef",
    {
        "Id": str,
        "Label": str,
        "Timestamps": List[datetime],
        "Values": List[float],
        "StatusCode": str,
        "Messages": List[ClientGetMetricDataResponseMetricDataResultsMessagesTypeDef],
    },
    total=False,
)


class ClientGetMetricDataResponseMetricDataResultsTypeDef(
    _ClientGetMetricDataResponseMetricDataResultsTypeDef
):
    """
    Type definition for `ClientGetMetricDataResponse` `MetricDataResults`

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
    """


_ClientGetMetricDataResponseTypeDef = TypedDict(
    "_ClientGetMetricDataResponseTypeDef",
    {
        "MetricDataResults": List[ClientGetMetricDataResponseMetricDataResultsTypeDef],
        "NextToken": str,
        "Messages": List[ClientGetMetricDataResponseMessagesTypeDef],
    },
    total=False,
)


class ClientGetMetricDataResponseTypeDef(_ClientGetMetricDataResponseTypeDef):
    """
    Type definition for `ClientGetMetricData` `Response`

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


_ClientGetMetricStatisticsDimensionsTypeDef = TypedDict(
    "_ClientGetMetricStatisticsDimensionsTypeDef", {"Name": str, "Value": str}
)


class ClientGetMetricStatisticsDimensionsTypeDef(
    _ClientGetMetricStatisticsDimensionsTypeDef
):
    """
    Type definition for `ClientGetMetricStatistics` `Dimensions`

    Expands the identity of a metric.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the dimension.

    - **Value** *(string) --* **[REQUIRED]**

      The value representing the dimension measurement.
    """


_ClientGetMetricStatisticsResponseDatapointsTypeDef = TypedDict(
    "_ClientGetMetricStatisticsResponseDatapointsTypeDef",
    {
        "Timestamp": datetime,
        "SampleCount": float,
        "Average": float,
        "Sum": float,
        "Minimum": float,
        "Maximum": float,
        "Unit": str,
        "ExtendedStatistics": Dict[str, float],
    },
    total=False,
)


class ClientGetMetricStatisticsResponseDatapointsTypeDef(
    _ClientGetMetricStatisticsResponseDatapointsTypeDef
):
    """
    Type definition for `ClientGetMetricStatisticsResponse` `Datapoints`

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


_ClientGetMetricStatisticsResponseTypeDef = TypedDict(
    "_ClientGetMetricStatisticsResponseTypeDef",
    {
        "Label": str,
        "Datapoints": List[ClientGetMetricStatisticsResponseDatapointsTypeDef],
    },
    total=False,
)


class ClientGetMetricStatisticsResponseTypeDef(
    _ClientGetMetricStatisticsResponseTypeDef
):
    """
    Type definition for `ClientGetMetricStatistics` `Response`

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


_ClientGetMetricWidgetImageResponseTypeDef = TypedDict(
    "_ClientGetMetricWidgetImageResponseTypeDef",
    {"MetricWidgetImage": bytes},
    total=False,
)


class ClientGetMetricWidgetImageResponseTypeDef(
    _ClientGetMetricWidgetImageResponseTypeDef
):
    """
    Type definition for `ClientGetMetricWidgetImage` `Response`

    - **MetricWidgetImage** *(bytes) --*

      The image of the graph, in the output format specified.
    """


_ClientListDashboardsResponseDashboardEntriesTypeDef = TypedDict(
    "_ClientListDashboardsResponseDashboardEntriesTypeDef",
    {"DashboardName": str, "DashboardArn": str, "LastModified": datetime, "Size": int},
    total=False,
)


class ClientListDashboardsResponseDashboardEntriesTypeDef(
    _ClientListDashboardsResponseDashboardEntriesTypeDef
):
    """
    Type definition for `ClientListDashboardsResponse` `DashboardEntries`

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
    """


_ClientListDashboardsResponseTypeDef = TypedDict(
    "_ClientListDashboardsResponseTypeDef",
    {
        "DashboardEntries": List[ClientListDashboardsResponseDashboardEntriesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListDashboardsResponseTypeDef(_ClientListDashboardsResponseTypeDef):
    """
    Type definition for `ClientListDashboards` `Response`

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


_RequiredClientListMetricsDimensionsTypeDef = TypedDict(
    "_RequiredClientListMetricsDimensionsTypeDef", {"Name": str}
)
_OptionalClientListMetricsDimensionsTypeDef = TypedDict(
    "_OptionalClientListMetricsDimensionsTypeDef", {"Value": str}, total=False
)


class ClientListMetricsDimensionsTypeDef(
    _RequiredClientListMetricsDimensionsTypeDef,
    _OptionalClientListMetricsDimensionsTypeDef,
):
    """
    Type definition for `ClientListMetrics` `Dimensions`

    Represents filters for a dimension.

    - **Name** *(string) --* **[REQUIRED]**

      The dimension name to be matched.

    - **Value** *(string) --*

      The value of the dimension to be matched.
    """


_ClientListMetricsResponseMetricsDimensionsTypeDef = TypedDict(
    "_ClientListMetricsResponseMetricsDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientListMetricsResponseMetricsDimensionsTypeDef(
    _ClientListMetricsResponseMetricsDimensionsTypeDef
):
    """
    Type definition for `ClientListMetricsResponseMetrics` `Dimensions`

    Expands the identity of a metric.

    - **Name** *(string) --*

      The name of the dimension.

    - **Value** *(string) --*

      The value representing the dimension measurement.
    """


_ClientListMetricsResponseMetricsTypeDef = TypedDict(
    "_ClientListMetricsResponseMetricsTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[ClientListMetricsResponseMetricsDimensionsTypeDef],
    },
    total=False,
)


class ClientListMetricsResponseMetricsTypeDef(_ClientListMetricsResponseMetricsTypeDef):
    """
    Type definition for `ClientListMetricsResponse` `Metrics`

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
    """


_ClientListMetricsResponseTypeDef = TypedDict(
    "_ClientListMetricsResponseTypeDef",
    {"Metrics": List[ClientListMetricsResponseMetricsTypeDef], "NextToken": str},
    total=False,
)


class ClientListMetricsResponseTypeDef(_ClientListMetricsResponseTypeDef):
    """
    Type definition for `ClientListMetrics` `Response`

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


_ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListTagsForResourceResponseTagsTypeDef(
    _ClientListTagsForResourceResponseTagsTypeDef
):
    """
    Type definition for `ClientListTagsForResourceResponse` `Tags`

    A key-value pair associated with a CloudWatch resource.

    - **Key** *(string) --*

      A string that you can use to assign a value. The combination of tag keys and values can
      help you organize and categorize your resources.

    - **Value** *(string) --*

      The value for the specified tag key.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

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


_ClientPutAnomalyDetectorConfigurationExcludedTimeRangesTypeDef = TypedDict(
    "_ClientPutAnomalyDetectorConfigurationExcludedTimeRangesTypeDef",
    {"StartTime": datetime, "EndTime": datetime},
)


class ClientPutAnomalyDetectorConfigurationExcludedTimeRangesTypeDef(
    _ClientPutAnomalyDetectorConfigurationExcludedTimeRangesTypeDef
):
    """
    Type definition for `ClientPutAnomalyDetectorConfiguration` `ExcludedTimeRanges`

    Specifies one range of days or times to exclude from use for training an anomaly detection
    model.

    - **StartTime** *(datetime) --* **[REQUIRED]**

      The start time of the range to exclude. The format is ``yyyy-MM-dd'T'HH:mm:ss`` . For
      example, ``2019-07-01T23:59:59`` .

    - **EndTime** *(datetime) --* **[REQUIRED]**

      The end time of the range to exclude. The format is ``yyyy-MM-dd'T'HH:mm:ss`` . For
      example, ``2019-07-01T23:59:59`` .
    """


_ClientPutAnomalyDetectorConfigurationTypeDef = TypedDict(
    "_ClientPutAnomalyDetectorConfigurationTypeDef",
    {
        "ExcludedTimeRanges": List[
            ClientPutAnomalyDetectorConfigurationExcludedTimeRangesTypeDef
        ],
        "MetricTimezone": str,
    },
    total=False,
)


class ClientPutAnomalyDetectorConfigurationTypeDef(
    _ClientPutAnomalyDetectorConfigurationTypeDef
):
    """
    Type definition for `ClientPutAnomalyDetector` `Configuration`

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
    """


_ClientPutAnomalyDetectorDimensionsTypeDef = TypedDict(
    "_ClientPutAnomalyDetectorDimensionsTypeDef", {"Name": str, "Value": str}
)


class ClientPutAnomalyDetectorDimensionsTypeDef(
    _ClientPutAnomalyDetectorDimensionsTypeDef
):
    """
    Type definition for `ClientPutAnomalyDetector` `Dimensions`

    Expands the identity of a metric.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the dimension.

    - **Value** *(string) --* **[REQUIRED]**

      The value representing the dimension measurement.
    """


_ClientPutDashboardResponseDashboardValidationMessagesTypeDef = TypedDict(
    "_ClientPutDashboardResponseDashboardValidationMessagesTypeDef",
    {"DataPath": str, "Message": str},
    total=False,
)


class ClientPutDashboardResponseDashboardValidationMessagesTypeDef(
    _ClientPutDashboardResponseDashboardValidationMessagesTypeDef
):
    """
    Type definition for `ClientPutDashboardResponse` `DashboardValidationMessages`

    An error or warning for the operation.

    - **DataPath** *(string) --*

      The data path related to the message.

    - **Message** *(string) --*

      A message describing the error or warning.
    """


_ClientPutDashboardResponseTypeDef = TypedDict(
    "_ClientPutDashboardResponseTypeDef",
    {
        "DashboardValidationMessages": List[
            ClientPutDashboardResponseDashboardValidationMessagesTypeDef
        ]
    },
    total=False,
)


class ClientPutDashboardResponseTypeDef(_ClientPutDashboardResponseTypeDef):
    """
    Type definition for `ClientPutDashboard` `Response`

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


_ClientPutMetricAlarmDimensionsTypeDef = TypedDict(
    "_ClientPutMetricAlarmDimensionsTypeDef", {"Name": str, "Value": str}
)


class ClientPutMetricAlarmDimensionsTypeDef(_ClientPutMetricAlarmDimensionsTypeDef):
    """
    Type definition for `ClientPutMetricAlarm` `Dimensions`

    Expands the identity of a metric.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the dimension.

    - **Value** *(string) --* **[REQUIRED]**

      The value representing the dimension measurement.
    """


_ClientPutMetricAlarmMetricsMetricStatMetricDimensionsTypeDef = TypedDict(
    "_ClientPutMetricAlarmMetricsMetricStatMetricDimensionsTypeDef",
    {"Name": str, "Value": str},
)


class ClientPutMetricAlarmMetricsMetricStatMetricDimensionsTypeDef(
    _ClientPutMetricAlarmMetricsMetricStatMetricDimensionsTypeDef
):
    """
    Type definition for `ClientPutMetricAlarmMetricsMetricStatMetric` `Dimensions`

    Expands the identity of a metric.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the dimension.

    - **Value** *(string) --* **[REQUIRED]**

      The value representing the dimension measurement.
    """


_ClientPutMetricAlarmMetricsMetricStatMetricTypeDef = TypedDict(
    "_ClientPutMetricAlarmMetricsMetricStatMetricTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[
            ClientPutMetricAlarmMetricsMetricStatMetricDimensionsTypeDef
        ],
    },
    total=False,
)


class ClientPutMetricAlarmMetricsMetricStatMetricTypeDef(
    _ClientPutMetricAlarmMetricsMetricStatMetricTypeDef
):
    """
    Type definition for `ClientPutMetricAlarmMetricsMetricStat` `Metric`

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
    """


_RequiredClientPutMetricAlarmMetricsMetricStatTypeDef = TypedDict(
    "_RequiredClientPutMetricAlarmMetricsMetricStatTypeDef",
    {
        "Metric": ClientPutMetricAlarmMetricsMetricStatMetricTypeDef,
        "Period": int,
        "Stat": str,
    },
)
_OptionalClientPutMetricAlarmMetricsMetricStatTypeDef = TypedDict(
    "_OptionalClientPutMetricAlarmMetricsMetricStatTypeDef", {"Unit": str}, total=False
)


class ClientPutMetricAlarmMetricsMetricStatTypeDef(
    _RequiredClientPutMetricAlarmMetricsMetricStatTypeDef,
    _OptionalClientPutMetricAlarmMetricsMetricStatTypeDef,
):
    """
    Type definition for `ClientPutMetricAlarmMetrics` `MetricStat`

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
    """


_RequiredClientPutMetricAlarmMetricsTypeDef = TypedDict(
    "_RequiredClientPutMetricAlarmMetricsTypeDef", {"Id": str}
)
_OptionalClientPutMetricAlarmMetricsTypeDef = TypedDict(
    "_OptionalClientPutMetricAlarmMetricsTypeDef",
    {
        "MetricStat": ClientPutMetricAlarmMetricsMetricStatTypeDef,
        "Expression": str,
        "Label": str,
        "ReturnData": bool,
        "Period": int,
    },
    total=False,
)


class ClientPutMetricAlarmMetricsTypeDef(
    _RequiredClientPutMetricAlarmMetricsTypeDef,
    _OptionalClientPutMetricAlarmMetricsTypeDef,
):
    """
    Type definition for `ClientPutMetricAlarm` `Metrics`

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
    """


_ClientPutMetricAlarmTagsTypeDef = TypedDict(
    "_ClientPutMetricAlarmTagsTypeDef", {"Key": str, "Value": str}
)


class ClientPutMetricAlarmTagsTypeDef(_ClientPutMetricAlarmTagsTypeDef):
    """
    Type definition for `ClientPutMetricAlarm` `Tags`

    A key-value pair associated with a CloudWatch resource.

    - **Key** *(string) --* **[REQUIRED]**

      A string that you can use to assign a value. The combination of tag keys and values can help
      you organize and categorize your resources.

    - **Value** *(string) --* **[REQUIRED]**

      The value for the specified tag key.
    """


_ClientPutMetricDataMetricDataDimensionsTypeDef = TypedDict(
    "_ClientPutMetricDataMetricDataDimensionsTypeDef", {"Name": str, "Value": str}
)


class ClientPutMetricDataMetricDataDimensionsTypeDef(
    _ClientPutMetricDataMetricDataDimensionsTypeDef
):
    """
    Type definition for `ClientPutMetricDataMetricData` `Dimensions`

    Expands the identity of a metric.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the dimension.

    - **Value** *(string) --* **[REQUIRED]**

      The value representing the dimension measurement.
    """


_ClientPutMetricDataMetricDataStatisticValuesTypeDef = TypedDict(
    "_ClientPutMetricDataMetricDataStatisticValuesTypeDef",
    {"SampleCount": float, "Sum": float, "Minimum": float, "Maximum": float},
)


class ClientPutMetricDataMetricDataStatisticValuesTypeDef(
    _ClientPutMetricDataMetricDataStatisticValuesTypeDef
):
    """
    Type definition for `ClientPutMetricDataMetricData` `StatisticValues`

    The statistical values for the metric.

    - **SampleCount** *(float) --* **[REQUIRED]**

      The number of samples used for the statistic set.

    - **Sum** *(float) --* **[REQUIRED]**

      The sum of values for the sample set.

    - **Minimum** *(float) --* **[REQUIRED]**

      The minimum value of the sample set.

    - **Maximum** *(float) --* **[REQUIRED]**

      The maximum value of the sample set.
    """


_RequiredClientPutMetricDataMetricDataTypeDef = TypedDict(
    "_RequiredClientPutMetricDataMetricDataTypeDef", {"MetricName": str}
)
_OptionalClientPutMetricDataMetricDataTypeDef = TypedDict(
    "_OptionalClientPutMetricDataMetricDataTypeDef",
    {
        "Dimensions": List[ClientPutMetricDataMetricDataDimensionsTypeDef],
        "Timestamp": datetime,
        "Value": float,
        "StatisticValues": ClientPutMetricDataMetricDataStatisticValuesTypeDef,
        "Values": List[float],
        "Counts": List[float],
        "Unit": str,
        "StorageResolution": int,
    },
    total=False,
)


class ClientPutMetricDataMetricDataTypeDef(
    _RequiredClientPutMetricDataMetricDataTypeDef,
    _OptionalClientPutMetricDataMetricDataTypeDef,
):
    """
    Type definition for `ClientPutMetricData` `MetricData`

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
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    Type definition for `ClientTagResource` `Tags`

    A key-value pair associated with a CloudWatch resource.

    - **Key** *(string) --* **[REQUIRED]**

      A string that you can use to assign a value. The combination of tag keys and values can help
      you organize and categorize your resources.

    - **Value** *(string) --* **[REQUIRED]**

      The value for the specified tag key.
    """


_DescribeAlarmHistoryPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeAlarmHistoryPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeAlarmHistoryPaginatePaginationConfigTypeDef(
    _DescribeAlarmHistoryPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeAlarmHistoryPaginate` `PaginationConfig`

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


_DescribeAlarmHistoryPaginateResponseAlarmHistoryItemsTypeDef = TypedDict(
    "_DescribeAlarmHistoryPaginateResponseAlarmHistoryItemsTypeDef",
    {
        "AlarmName": str,
        "Timestamp": datetime,
        "HistoryItemType": str,
        "HistorySummary": str,
        "HistoryData": str,
    },
    total=False,
)


class DescribeAlarmHistoryPaginateResponseAlarmHistoryItemsTypeDef(
    _DescribeAlarmHistoryPaginateResponseAlarmHistoryItemsTypeDef
):
    """
    Type definition for `DescribeAlarmHistoryPaginateResponse` `AlarmHistoryItems`

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
    """


_DescribeAlarmHistoryPaginateResponseTypeDef = TypedDict(
    "_DescribeAlarmHistoryPaginateResponseTypeDef",
    {
        "AlarmHistoryItems": List[
            DescribeAlarmHistoryPaginateResponseAlarmHistoryItemsTypeDef
        ]
    },
    total=False,
)


class DescribeAlarmHistoryPaginateResponseTypeDef(
    _DescribeAlarmHistoryPaginateResponseTypeDef
):
    """
    Type definition for `DescribeAlarmHistoryPaginate` `Response`

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
    """


_DescribeAlarmsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeAlarmsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeAlarmsPaginatePaginationConfigTypeDef(
    _DescribeAlarmsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeAlarmsPaginate` `PaginationConfig`

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


_DescribeAlarmsPaginateResponseMetricAlarmsDimensionsTypeDef = TypedDict(
    "_DescribeAlarmsPaginateResponseMetricAlarmsDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class DescribeAlarmsPaginateResponseMetricAlarmsDimensionsTypeDef(
    _DescribeAlarmsPaginateResponseMetricAlarmsDimensionsTypeDef
):
    """
    Type definition for `DescribeAlarmsPaginateResponseMetricAlarms` `Dimensions`

    Expands the identity of a metric.

    - **Name** *(string) --*

      The name of the dimension.

    - **Value** *(string) --*

      The value representing the dimension measurement.
    """


_DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef = TypedDict(
    "_DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef(
    _DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef
):
    """
    Type definition for `DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatMetric` `Dimensions`

    Expands the identity of a metric.

    - **Name** *(string) --*

      The name of the dimension.

    - **Value** *(string) --*

      The value representing the dimension measurement.
    """


_DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatMetricTypeDef = TypedDict(
    "_DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatMetricTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[
            DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef
        ],
    },
    total=False,
)


class DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatMetricTypeDef(
    _DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatMetricTypeDef
):
    """
    Type definition for `DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStat` `Metric`

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
    """


_DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatTypeDef = TypedDict(
    "_DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatTypeDef",
    {
        "Metric": DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatMetricTypeDef,
        "Period": int,
        "Stat": str,
        "Unit": str,
    },
    total=False,
)


class DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatTypeDef(
    _DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatTypeDef
):
    """
    Type definition for `DescribeAlarmsPaginateResponseMetricAlarmsMetrics` `MetricStat`

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
    """


_DescribeAlarmsPaginateResponseMetricAlarmsMetricsTypeDef = TypedDict(
    "_DescribeAlarmsPaginateResponseMetricAlarmsMetricsTypeDef",
    {
        "Id": str,
        "MetricStat": DescribeAlarmsPaginateResponseMetricAlarmsMetricsMetricStatTypeDef,
        "Expression": str,
        "Label": str,
        "ReturnData": bool,
        "Period": int,
    },
    total=False,
)


class DescribeAlarmsPaginateResponseMetricAlarmsMetricsTypeDef(
    _DescribeAlarmsPaginateResponseMetricAlarmsMetricsTypeDef
):
    """
    Type definition for `DescribeAlarmsPaginateResponseMetricAlarms` `Metrics`

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
    """


_DescribeAlarmsPaginateResponseMetricAlarmsTypeDef = TypedDict(
    "_DescribeAlarmsPaginateResponseMetricAlarmsTypeDef",
    {
        "AlarmName": str,
        "AlarmArn": str,
        "AlarmDescription": str,
        "AlarmConfigurationUpdatedTimestamp": datetime,
        "ActionsEnabled": bool,
        "OKActions": List[str],
        "AlarmActions": List[str],
        "InsufficientDataActions": List[str],
        "StateValue": str,
        "StateReason": str,
        "StateReasonData": str,
        "StateUpdatedTimestamp": datetime,
        "MetricName": str,
        "Namespace": str,
        "Statistic": str,
        "ExtendedStatistic": str,
        "Dimensions": List[DescribeAlarmsPaginateResponseMetricAlarmsDimensionsTypeDef],
        "Period": int,
        "Unit": str,
        "EvaluationPeriods": int,
        "DatapointsToAlarm": int,
        "Threshold": float,
        "ComparisonOperator": str,
        "TreatMissingData": str,
        "EvaluateLowSampleCountPercentile": str,
        "Metrics": List[DescribeAlarmsPaginateResponseMetricAlarmsMetricsTypeDef],
        "ThresholdMetricId": str,
    },
    total=False,
)


class DescribeAlarmsPaginateResponseMetricAlarmsTypeDef(
    _DescribeAlarmsPaginateResponseMetricAlarmsTypeDef
):
    """
    Type definition for `DescribeAlarmsPaginateResponse` `MetricAlarms`

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


_DescribeAlarmsPaginateResponseTypeDef = TypedDict(
    "_DescribeAlarmsPaginateResponseTypeDef",
    {"MetricAlarms": List[DescribeAlarmsPaginateResponseMetricAlarmsTypeDef]},
    total=False,
)


class DescribeAlarmsPaginateResponseTypeDef(_DescribeAlarmsPaginateResponseTypeDef):
    """
    Type definition for `DescribeAlarmsPaginate` `Response`

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
    """


_GetMetricDataPaginateMetricDataQueriesMetricStatMetricDimensionsTypeDef = TypedDict(
    "_GetMetricDataPaginateMetricDataQueriesMetricStatMetricDimensionsTypeDef",
    {"Name": str, "Value": str},
)


class GetMetricDataPaginateMetricDataQueriesMetricStatMetricDimensionsTypeDef(
    _GetMetricDataPaginateMetricDataQueriesMetricStatMetricDimensionsTypeDef
):
    """
    Type definition for `GetMetricDataPaginateMetricDataQueriesMetricStatMetric` `Dimensions`

    Expands the identity of a metric.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the dimension.

    - **Value** *(string) --* **[REQUIRED]**

      The value representing the dimension measurement.
    """


_GetMetricDataPaginateMetricDataQueriesMetricStatMetricTypeDef = TypedDict(
    "_GetMetricDataPaginateMetricDataQueriesMetricStatMetricTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[
            GetMetricDataPaginateMetricDataQueriesMetricStatMetricDimensionsTypeDef
        ],
    },
    total=False,
)


class GetMetricDataPaginateMetricDataQueriesMetricStatMetricTypeDef(
    _GetMetricDataPaginateMetricDataQueriesMetricStatMetricTypeDef
):
    """
    Type definition for `GetMetricDataPaginateMetricDataQueriesMetricStat` `Metric`

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
    """


_RequiredGetMetricDataPaginateMetricDataQueriesMetricStatTypeDef = TypedDict(
    "_RequiredGetMetricDataPaginateMetricDataQueriesMetricStatTypeDef",
    {
        "Metric": GetMetricDataPaginateMetricDataQueriesMetricStatMetricTypeDef,
        "Period": int,
        "Stat": str,
    },
)
_OptionalGetMetricDataPaginateMetricDataQueriesMetricStatTypeDef = TypedDict(
    "_OptionalGetMetricDataPaginateMetricDataQueriesMetricStatTypeDef",
    {"Unit": str},
    total=False,
)


class GetMetricDataPaginateMetricDataQueriesMetricStatTypeDef(
    _RequiredGetMetricDataPaginateMetricDataQueriesMetricStatTypeDef,
    _OptionalGetMetricDataPaginateMetricDataQueriesMetricStatTypeDef,
):
    """
    Type definition for `GetMetricDataPaginateMetricDataQueries` `MetricStat`

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
    """


_RequiredGetMetricDataPaginateMetricDataQueriesTypeDef = TypedDict(
    "_RequiredGetMetricDataPaginateMetricDataQueriesTypeDef", {"Id": str}
)
_OptionalGetMetricDataPaginateMetricDataQueriesTypeDef = TypedDict(
    "_OptionalGetMetricDataPaginateMetricDataQueriesTypeDef",
    {
        "MetricStat": GetMetricDataPaginateMetricDataQueriesMetricStatTypeDef,
        "Expression": str,
        "Label": str,
        "ReturnData": bool,
        "Period": int,
    },
    total=False,
)


class GetMetricDataPaginateMetricDataQueriesTypeDef(
    _RequiredGetMetricDataPaginateMetricDataQueriesTypeDef,
    _OptionalGetMetricDataPaginateMetricDataQueriesTypeDef,
):
    """
    Type definition for `GetMetricDataPaginate` `MetricDataQueries`

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
    """


_GetMetricDataPaginatePaginationConfigTypeDef = TypedDict(
    "_GetMetricDataPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetMetricDataPaginatePaginationConfigTypeDef(
    _GetMetricDataPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetMetricDataPaginate` `PaginationConfig`

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


_GetMetricDataPaginateResponseMessagesTypeDef = TypedDict(
    "_GetMetricDataPaginateResponseMessagesTypeDef",
    {"Code": str, "Value": str},
    total=False,
)


class GetMetricDataPaginateResponseMessagesTypeDef(
    _GetMetricDataPaginateResponseMessagesTypeDef
):
    """
    Type definition for `GetMetricDataPaginateResponse` `Messages`

    A message returned by the ``GetMetricData`` API, including a code and a description.

    - **Code** *(string) --*

      The error code or status code associated with the message.

    - **Value** *(string) --*

      The message text.
    """


_GetMetricDataPaginateResponseMetricDataResultsMessagesTypeDef = TypedDict(
    "_GetMetricDataPaginateResponseMetricDataResultsMessagesTypeDef",
    {"Code": str, "Value": str},
    total=False,
)


class GetMetricDataPaginateResponseMetricDataResultsMessagesTypeDef(
    _GetMetricDataPaginateResponseMetricDataResultsMessagesTypeDef
):
    """
    Type definition for `GetMetricDataPaginateResponseMetricDataResults` `Messages`

    A message returned by the ``GetMetricData`` API, including a code and a description.

    - **Code** *(string) --*

      The error code or status code associated with the message.

    - **Value** *(string) --*

      The message text.
    """


_GetMetricDataPaginateResponseMetricDataResultsTypeDef = TypedDict(
    "_GetMetricDataPaginateResponseMetricDataResultsTypeDef",
    {
        "Id": str,
        "Label": str,
        "Timestamps": List[datetime],
        "Values": List[float],
        "StatusCode": str,
        "Messages": List[GetMetricDataPaginateResponseMetricDataResultsMessagesTypeDef],
    },
    total=False,
)


class GetMetricDataPaginateResponseMetricDataResultsTypeDef(
    _GetMetricDataPaginateResponseMetricDataResultsTypeDef
):
    """
    Type definition for `GetMetricDataPaginateResponse` `MetricDataResults`

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
    """


_GetMetricDataPaginateResponseTypeDef = TypedDict(
    "_GetMetricDataPaginateResponseTypeDef",
    {
        "MetricDataResults": List[
            GetMetricDataPaginateResponseMetricDataResultsTypeDef
        ],
        "Messages": List[GetMetricDataPaginateResponseMessagesTypeDef],
    },
    total=False,
)


class GetMetricDataPaginateResponseTypeDef(_GetMetricDataPaginateResponseTypeDef):
    """
    Type definition for `GetMetricDataPaginate` `Response`

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


_ListDashboardsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDashboardsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListDashboardsPaginatePaginationConfigTypeDef(
    _ListDashboardsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDashboardsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListDashboardsPaginateResponseDashboardEntriesTypeDef = TypedDict(
    "_ListDashboardsPaginateResponseDashboardEntriesTypeDef",
    {"DashboardName": str, "DashboardArn": str, "LastModified": datetime, "Size": int},
    total=False,
)


class ListDashboardsPaginateResponseDashboardEntriesTypeDef(
    _ListDashboardsPaginateResponseDashboardEntriesTypeDef
):
    """
    Type definition for `ListDashboardsPaginateResponse` `DashboardEntries`

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
    """


_ListDashboardsPaginateResponseTypeDef = TypedDict(
    "_ListDashboardsPaginateResponseTypeDef",
    {"DashboardEntries": List[ListDashboardsPaginateResponseDashboardEntriesTypeDef]},
    total=False,
)


class ListDashboardsPaginateResponseTypeDef(_ListDashboardsPaginateResponseTypeDef):
    """
    Type definition for `ListDashboardsPaginate` `Response`

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
    """


_RequiredListMetricsPaginateDimensionsTypeDef = TypedDict(
    "_RequiredListMetricsPaginateDimensionsTypeDef", {"Name": str}
)
_OptionalListMetricsPaginateDimensionsTypeDef = TypedDict(
    "_OptionalListMetricsPaginateDimensionsTypeDef", {"Value": str}, total=False
)


class ListMetricsPaginateDimensionsTypeDef(
    _RequiredListMetricsPaginateDimensionsTypeDef,
    _OptionalListMetricsPaginateDimensionsTypeDef,
):
    """
    Type definition for `ListMetricsPaginate` `Dimensions`

    Represents filters for a dimension.

    - **Name** *(string) --* **[REQUIRED]**

      The dimension name to be matched.

    - **Value** *(string) --*

      The value of the dimension to be matched.
    """


_ListMetricsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListMetricsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListMetricsPaginatePaginationConfigTypeDef(
    _ListMetricsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListMetricsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListMetricsPaginateResponseMetricsDimensionsTypeDef = TypedDict(
    "_ListMetricsPaginateResponseMetricsDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ListMetricsPaginateResponseMetricsDimensionsTypeDef(
    _ListMetricsPaginateResponseMetricsDimensionsTypeDef
):
    """
    Type definition for `ListMetricsPaginateResponseMetrics` `Dimensions`

    Expands the identity of a metric.

    - **Name** *(string) --*

      The name of the dimension.

    - **Value** *(string) --*

      The value representing the dimension measurement.
    """


_ListMetricsPaginateResponseMetricsTypeDef = TypedDict(
    "_ListMetricsPaginateResponseMetricsTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[ListMetricsPaginateResponseMetricsDimensionsTypeDef],
    },
    total=False,
)


class ListMetricsPaginateResponseMetricsTypeDef(
    _ListMetricsPaginateResponseMetricsTypeDef
):
    """
    Type definition for `ListMetricsPaginateResponse` `Metrics`

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
    """


_ListMetricsPaginateResponseTypeDef = TypedDict(
    "_ListMetricsPaginateResponseTypeDef",
    {"Metrics": List[ListMetricsPaginateResponseMetricsTypeDef]},
    total=False,
)


class ListMetricsPaginateResponseTypeDef(_ListMetricsPaginateResponseTypeDef):
    """
    Type definition for `ListMetricsPaginate` `Response`

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
    """


_MetricGetStatisticsDimensionsTypeDef = TypedDict(
    "_MetricGetStatisticsDimensionsTypeDef", {"Name": str, "Value": str}
)


class MetricGetStatisticsDimensionsTypeDef(_MetricGetStatisticsDimensionsTypeDef):
    """
    Type definition for `MetricGetStatistics` `Dimensions`

    Expands the identity of a metric.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the dimension.

    - **Value** *(string) --* **[REQUIRED]**

      The value representing the dimension measurement.
    """


_MetricGetStatisticsResponseDatapointsTypeDef = TypedDict(
    "_MetricGetStatisticsResponseDatapointsTypeDef",
    {
        "Timestamp": datetime,
        "SampleCount": float,
        "Average": float,
        "Sum": float,
        "Minimum": float,
        "Maximum": float,
        "Unit": str,
        "ExtendedStatistics": Dict[str, float],
    },
    total=False,
)


class MetricGetStatisticsResponseDatapointsTypeDef(
    _MetricGetStatisticsResponseDatapointsTypeDef
):
    """
    Type definition for `MetricGetStatisticsResponse` `Datapoints`

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


_MetricGetStatisticsResponseTypeDef = TypedDict(
    "_MetricGetStatisticsResponseTypeDef",
    {"Label": str, "Datapoints": List[MetricGetStatisticsResponseDatapointsTypeDef]},
    total=False,
)


class MetricGetStatisticsResponseTypeDef(_MetricGetStatisticsResponseTypeDef):
    """
    Type definition for `MetricGetStatistics` `Response`

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


_MetricPutAlarmDimensionsTypeDef = TypedDict(
    "_MetricPutAlarmDimensionsTypeDef", {"Name": str, "Value": str}
)


class MetricPutAlarmDimensionsTypeDef(_MetricPutAlarmDimensionsTypeDef):
    """
    Type definition for `MetricPutAlarm` `Dimensions`

    Expands the identity of a metric.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the dimension.

    - **Value** *(string) --* **[REQUIRED]**

      The value representing the dimension measurement.
    """


_MetricPutAlarmMetricsMetricStatMetricDimensionsTypeDef = TypedDict(
    "_MetricPutAlarmMetricsMetricStatMetricDimensionsTypeDef",
    {"Name": str, "Value": str},
)


class MetricPutAlarmMetricsMetricStatMetricDimensionsTypeDef(
    _MetricPutAlarmMetricsMetricStatMetricDimensionsTypeDef
):
    """
    Type definition for `MetricPutAlarmMetricsMetricStatMetric` `Dimensions`

    Expands the identity of a metric.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the dimension.

    - **Value** *(string) --* **[REQUIRED]**

      The value representing the dimension measurement.
    """


_MetricPutAlarmMetricsMetricStatMetricTypeDef = TypedDict(
    "_MetricPutAlarmMetricsMetricStatMetricTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[MetricPutAlarmMetricsMetricStatMetricDimensionsTypeDef],
    },
    total=False,
)


class MetricPutAlarmMetricsMetricStatMetricTypeDef(
    _MetricPutAlarmMetricsMetricStatMetricTypeDef
):
    """
    Type definition for `MetricPutAlarmMetricsMetricStat` `Metric`

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
    """


_RequiredMetricPutAlarmMetricsMetricStatTypeDef = TypedDict(
    "_RequiredMetricPutAlarmMetricsMetricStatTypeDef",
    {
        "Metric": MetricPutAlarmMetricsMetricStatMetricTypeDef,
        "Period": int,
        "Stat": str,
    },
)
_OptionalMetricPutAlarmMetricsMetricStatTypeDef = TypedDict(
    "_OptionalMetricPutAlarmMetricsMetricStatTypeDef", {"Unit": str}, total=False
)


class MetricPutAlarmMetricsMetricStatTypeDef(
    _RequiredMetricPutAlarmMetricsMetricStatTypeDef,
    _OptionalMetricPutAlarmMetricsMetricStatTypeDef,
):
    """
    Type definition for `MetricPutAlarmMetrics` `MetricStat`

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
    """


_RequiredMetricPutAlarmMetricsTypeDef = TypedDict(
    "_RequiredMetricPutAlarmMetricsTypeDef", {"Id": str}
)
_OptionalMetricPutAlarmMetricsTypeDef = TypedDict(
    "_OptionalMetricPutAlarmMetricsTypeDef",
    {
        "MetricStat": MetricPutAlarmMetricsMetricStatTypeDef,
        "Expression": str,
        "Label": str,
        "ReturnData": bool,
        "Period": int,
    },
    total=False,
)


class MetricPutAlarmMetricsTypeDef(
    _RequiredMetricPutAlarmMetricsTypeDef, _OptionalMetricPutAlarmMetricsTypeDef
):
    """
    Type definition for `MetricPutAlarm` `Metrics`

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
    """


_MetricPutAlarmTagsTypeDef = TypedDict(
    "_MetricPutAlarmTagsTypeDef", {"Key": str, "Value": str}
)


class MetricPutAlarmTagsTypeDef(_MetricPutAlarmTagsTypeDef):
    """
    Type definition for `MetricPutAlarm` `Tags`

    A key-value pair associated with a CloudWatch resource.

    - **Key** *(string) --* **[REQUIRED]**

      A string that you can use to assign a value. The combination of tag keys and values can help
      you organize and categorize your resources.

    - **Value** *(string) --* **[REQUIRED]**

      The value for the specified tag key.
    """


_RequiredMetricsFilterDimensionsTypeDef = TypedDict(
    "_RequiredMetricsFilterDimensionsTypeDef", {"Name": str}
)
_OptionalMetricsFilterDimensionsTypeDef = TypedDict(
    "_OptionalMetricsFilterDimensionsTypeDef", {"Value": str}, total=False
)


class MetricsFilterDimensionsTypeDef(
    _RequiredMetricsFilterDimensionsTypeDef, _OptionalMetricsFilterDimensionsTypeDef
):
    """
    Type definition for `MetricsFilter` `Dimensions`

    Represents filters for a dimension.

    - **Name** *(string) --* **[REQUIRED]**

      The dimension name to be matched.

    - **Value** *(string) --*

      The value of the dimension to be matched.
    """
