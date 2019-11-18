"Main interface for logs type defs"
from __future__ import annotations

from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateExportTaskResponseTypeDef",
    "ClientDescribeDestinationsResponsedestinationsTypeDef",
    "ClientDescribeDestinationsResponseTypeDef",
    "ClientDescribeExportTasksResponseexportTasksexecutionInfoTypeDef",
    "ClientDescribeExportTasksResponseexportTasksstatusTypeDef",
    "ClientDescribeExportTasksResponseexportTasksTypeDef",
    "ClientDescribeExportTasksResponseTypeDef",
    "ClientDescribeLogGroupsResponselogGroupsTypeDef",
    "ClientDescribeLogGroupsResponseTypeDef",
    "ClientDescribeLogStreamsResponselogStreamsTypeDef",
    "ClientDescribeLogStreamsResponseTypeDef",
    "ClientDescribeMetricFiltersResponsemetricFiltersmetricTransformationsTypeDef",
    "ClientDescribeMetricFiltersResponsemetricFiltersTypeDef",
    "ClientDescribeMetricFiltersResponseTypeDef",
    "ClientDescribeQueriesResponsequeriesTypeDef",
    "ClientDescribeQueriesResponseTypeDef",
    "ClientDescribeResourcePoliciesResponseresourcePoliciesTypeDef",
    "ClientDescribeResourcePoliciesResponseTypeDef",
    "ClientDescribeSubscriptionFiltersResponsesubscriptionFiltersTypeDef",
    "ClientDescribeSubscriptionFiltersResponseTypeDef",
    "ClientFilterLogEventsResponseeventsTypeDef",
    "ClientFilterLogEventsResponsesearchedLogStreamsTypeDef",
    "ClientFilterLogEventsResponseTypeDef",
    "ClientGetLogEventsResponseeventsTypeDef",
    "ClientGetLogEventsResponseTypeDef",
    "ClientGetLogGroupFieldsResponselogGroupFieldsTypeDef",
    "ClientGetLogGroupFieldsResponseTypeDef",
    "ClientGetLogRecordResponseTypeDef",
    "ClientGetQueryResultsResponseresultsTypeDef",
    "ClientGetQueryResultsResponsestatisticsTypeDef",
    "ClientGetQueryResultsResponseTypeDef",
    "ClientListTagsLogGroupResponseTypeDef",
    "ClientPutDestinationResponsedestinationTypeDef",
    "ClientPutDestinationResponseTypeDef",
    "ClientPutLogEventsResponserejectedLogEventsInfoTypeDef",
    "ClientPutLogEventsResponseTypeDef",
    "ClientPutLogEventslogEventsTypeDef",
    "ClientPutMetricFiltermetricTransformationsTypeDef",
    "ClientPutResourcePolicyResponseresourcePolicyTypeDef",
    "ClientPutResourcePolicyResponseTypeDef",
    "ClientStartQueryResponseTypeDef",
    "ClientStopQueryResponseTypeDef",
    "ClientTestMetricFilterResponsematchesTypeDef",
    "ClientTestMetricFilterResponseTypeDef",
    "DescribeDestinationsPaginatePaginationConfigTypeDef",
    "DescribeDestinationsPaginateResponsedestinationsTypeDef",
    "DescribeDestinationsPaginateResponseTypeDef",
    "DescribeExportTasksPaginatePaginationConfigTypeDef",
    "DescribeExportTasksPaginateResponseexportTasksexecutionInfoTypeDef",
    "DescribeExportTasksPaginateResponseexportTasksstatusTypeDef",
    "DescribeExportTasksPaginateResponseexportTasksTypeDef",
    "DescribeExportTasksPaginateResponseTypeDef",
    "DescribeLogGroupsPaginatePaginationConfigTypeDef",
    "DescribeLogGroupsPaginateResponselogGroupsTypeDef",
    "DescribeLogGroupsPaginateResponseTypeDef",
    "DescribeLogStreamsPaginatePaginationConfigTypeDef",
    "DescribeLogStreamsPaginateResponselogStreamsTypeDef",
    "DescribeLogStreamsPaginateResponseTypeDef",
    "DescribeMetricFiltersPaginatePaginationConfigTypeDef",
    "DescribeMetricFiltersPaginateResponsemetricFiltersmetricTransformationsTypeDef",
    "DescribeMetricFiltersPaginateResponsemetricFiltersTypeDef",
    "DescribeMetricFiltersPaginateResponseTypeDef",
    "DescribeQueriesPaginatePaginationConfigTypeDef",
    "DescribeQueriesPaginateResponsequeriesTypeDef",
    "DescribeQueriesPaginateResponseTypeDef",
    "DescribeResourcePoliciesPaginatePaginationConfigTypeDef",
    "DescribeResourcePoliciesPaginateResponseresourcePoliciesTypeDef",
    "DescribeResourcePoliciesPaginateResponseTypeDef",
    "DescribeSubscriptionFiltersPaginatePaginationConfigTypeDef",
    "DescribeSubscriptionFiltersPaginateResponsesubscriptionFiltersTypeDef",
    "DescribeSubscriptionFiltersPaginateResponseTypeDef",
    "FilterLogEventsPaginatePaginationConfigTypeDef",
    "FilterLogEventsPaginateResponseeventsTypeDef",
    "FilterLogEventsPaginateResponsesearchedLogStreamsTypeDef",
    "FilterLogEventsPaginateResponseTypeDef",
)


_ClientCreateExportTaskResponseTypeDef = TypedDict(
    "_ClientCreateExportTaskResponseTypeDef", {"taskId": str}, total=False
)


class ClientCreateExportTaskResponseTypeDef(_ClientCreateExportTaskResponseTypeDef):
    """
    Type definition for `ClientCreateExportTask` `Response`

    - **taskId** *(string) --*

      The ID of the export task.
    """


_ClientDescribeDestinationsResponsedestinationsTypeDef = TypedDict(
    "_ClientDescribeDestinationsResponsedestinationsTypeDef",
    {
        "destinationName": str,
        "targetArn": str,
        "roleArn": str,
        "accessPolicy": str,
        "arn": str,
        "creationTime": int,
    },
    total=False,
)


class ClientDescribeDestinationsResponsedestinationsTypeDef(
    _ClientDescribeDestinationsResponsedestinationsTypeDef
):
    """
    Type definition for `ClientDescribeDestinationsResponse` `destinations`

    Represents a cross-account destination that receives subscription log events.

    - **destinationName** *(string) --*

      The name of the destination.

    - **targetArn** *(string) --*

      The Amazon Resource Name (ARN) of the physical target to where the log events are
      delivered (for example, a Kinesis stream).

    - **roleArn** *(string) --*

      A role for impersonation, used when delivering log events to the target.

    - **accessPolicy** *(string) --*

      An IAM policy document that governs which AWS accounts can create subscription filters
      against this destination.

    - **arn** *(string) --*

      The ARN of this destination.

    - **creationTime** *(integer) --*

      The creation time of the destination, expressed as the number of milliseconds after Jan
      1, 1970 00:00:00 UTC.
    """


_ClientDescribeDestinationsResponseTypeDef = TypedDict(
    "_ClientDescribeDestinationsResponseTypeDef",
    {
        "destinations": List[ClientDescribeDestinationsResponsedestinationsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeDestinationsResponseTypeDef(
    _ClientDescribeDestinationsResponseTypeDef
):
    """
    Type definition for `ClientDescribeDestinations` `Response`

    - **destinations** *(list) --*

      The destinations.

      - *(dict) --*

        Represents a cross-account destination that receives subscription log events.

        - **destinationName** *(string) --*

          The name of the destination.

        - **targetArn** *(string) --*

          The Amazon Resource Name (ARN) of the physical target to where the log events are
          delivered (for example, a Kinesis stream).

        - **roleArn** *(string) --*

          A role for impersonation, used when delivering log events to the target.

        - **accessPolicy** *(string) --*

          An IAM policy document that governs which AWS accounts can create subscription filters
          against this destination.

        - **arn** *(string) --*

          The ARN of this destination.

        - **creationTime** *(integer) --*

          The creation time of the destination, expressed as the number of milliseconds after Jan
          1, 1970 00:00:00 UTC.

    - **nextToken** *(string) --*

      The token for the next set of items to return. The token expires after 24 hours.
    """


_ClientDescribeExportTasksResponseexportTasksexecutionInfoTypeDef = TypedDict(
    "_ClientDescribeExportTasksResponseexportTasksexecutionInfoTypeDef",
    {"creationTime": int, "completionTime": int},
    total=False,
)


class ClientDescribeExportTasksResponseexportTasksexecutionInfoTypeDef(
    _ClientDescribeExportTasksResponseexportTasksexecutionInfoTypeDef
):
    """
    Type definition for `ClientDescribeExportTasksResponseexportTasks` `executionInfo`

    Execution info about the export task.

    - **creationTime** *(integer) --*

      The creation time of the export task, expressed as the number of milliseconds after Jan
      1, 1970 00:00:00 UTC.

    - **completionTime** *(integer) --*

      The completion time of the export task, expressed as the number of milliseconds after
      Jan 1, 1970 00:00:00 UTC.
    """


_ClientDescribeExportTasksResponseexportTasksstatusTypeDef = TypedDict(
    "_ClientDescribeExportTasksResponseexportTasksstatusTypeDef",
    {"code": str, "message": str},
    total=False,
)


class ClientDescribeExportTasksResponseexportTasksstatusTypeDef(
    _ClientDescribeExportTasksResponseexportTasksstatusTypeDef
):
    """
    Type definition for `ClientDescribeExportTasksResponseexportTasks` `status`

    The status of the export task.

    - **code** *(string) --*

      The status code of the export task.

    - **message** *(string) --*

      The status message related to the status code.
    """


_ClientDescribeExportTasksResponseexportTasksTypeDef = TypedDict(
    "_ClientDescribeExportTasksResponseexportTasksTypeDef",
    {
        "taskId": str,
        "taskName": str,
        "logGroupName": str,
        "from": int,
        "to": int,
        "destination": str,
        "destinationPrefix": str,
        "status": ClientDescribeExportTasksResponseexportTasksstatusTypeDef,
        "executionInfo": ClientDescribeExportTasksResponseexportTasksexecutionInfoTypeDef,
    },
    total=False,
)


class ClientDescribeExportTasksResponseexportTasksTypeDef(
    _ClientDescribeExportTasksResponseexportTasksTypeDef
):
    """
    Type definition for `ClientDescribeExportTasksResponse` `exportTasks`

    Represents an export task.

    - **taskId** *(string) --*

      The ID of the export task.

    - **taskName** *(string) --*

      The name of the export task.

    - **logGroupName** *(string) --*

      The name of the log group from which logs data was exported.

    - **from** *(integer) --*

      The start time, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.
      Events with a timestamp before this time are not exported.

    - **to** *(integer) --*

      The end time, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.
      Events with a timestamp later than this time are not exported.

    - **destination** *(string) --*

      The name of Amazon S3 bucket to which the log data was exported.

    - **destinationPrefix** *(string) --*

      The prefix that was used as the start of Amazon S3 key for every object exported.

    - **status** *(dict) --*

      The status of the export task.

      - **code** *(string) --*

        The status code of the export task.

      - **message** *(string) --*

        The status message related to the status code.

    - **executionInfo** *(dict) --*

      Execution info about the export task.

      - **creationTime** *(integer) --*

        The creation time of the export task, expressed as the number of milliseconds after Jan
        1, 1970 00:00:00 UTC.

      - **completionTime** *(integer) --*

        The completion time of the export task, expressed as the number of milliseconds after
        Jan 1, 1970 00:00:00 UTC.
    """


_ClientDescribeExportTasksResponseTypeDef = TypedDict(
    "_ClientDescribeExportTasksResponseTypeDef",
    {
        "exportTasks": List[ClientDescribeExportTasksResponseexportTasksTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeExportTasksResponseTypeDef(
    _ClientDescribeExportTasksResponseTypeDef
):
    """
    Type definition for `ClientDescribeExportTasks` `Response`

    - **exportTasks** *(list) --*

      The export tasks.

      - *(dict) --*

        Represents an export task.

        - **taskId** *(string) --*

          The ID of the export task.

        - **taskName** *(string) --*

          The name of the export task.

        - **logGroupName** *(string) --*

          The name of the log group from which logs data was exported.

        - **from** *(integer) --*

          The start time, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.
          Events with a timestamp before this time are not exported.

        - **to** *(integer) --*

          The end time, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.
          Events with a timestamp later than this time are not exported.

        - **destination** *(string) --*

          The name of Amazon S3 bucket to which the log data was exported.

        - **destinationPrefix** *(string) --*

          The prefix that was used as the start of Amazon S3 key for every object exported.

        - **status** *(dict) --*

          The status of the export task.

          - **code** *(string) --*

            The status code of the export task.

          - **message** *(string) --*

            The status message related to the status code.

        - **executionInfo** *(dict) --*

          Execution info about the export task.

          - **creationTime** *(integer) --*

            The creation time of the export task, expressed as the number of milliseconds after Jan
            1, 1970 00:00:00 UTC.

          - **completionTime** *(integer) --*

            The completion time of the export task, expressed as the number of milliseconds after
            Jan 1, 1970 00:00:00 UTC.

    - **nextToken** *(string) --*

      The token for the next set of items to return. The token expires after 24 hours.
    """


_ClientDescribeLogGroupsResponselogGroupsTypeDef = TypedDict(
    "_ClientDescribeLogGroupsResponselogGroupsTypeDef",
    {
        "logGroupName": str,
        "creationTime": int,
        "retentionInDays": int,
        "metricFilterCount": int,
        "arn": str,
        "storedBytes": int,
        "kmsKeyId": str,
    },
    total=False,
)


class ClientDescribeLogGroupsResponselogGroupsTypeDef(
    _ClientDescribeLogGroupsResponselogGroupsTypeDef
):
    """
    Type definition for `ClientDescribeLogGroupsResponse` `logGroups`

    Represents a log group.

    - **logGroupName** *(string) --*

      The name of the log group.

    - **creationTime** *(integer) --*

      The creation time of the log group, expressed as the number of milliseconds after Jan 1,
      1970 00:00:00 UTC.

    - **retentionInDays** *(integer) --*

      The number of days to retain the log events in the specified log group. Possible values
      are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, and 3653.

    - **metricFilterCount** *(integer) --*

      The number of metric filters.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the log group.

    - **storedBytes** *(integer) --*

      The number of bytes stored.

    - **kmsKeyId** *(string) --*

      The Amazon Resource Name (ARN) of the CMK to use when encrypting log data.
    """


_ClientDescribeLogGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeLogGroupsResponseTypeDef",
    {
        "logGroups": List[ClientDescribeLogGroupsResponselogGroupsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeLogGroupsResponseTypeDef(_ClientDescribeLogGroupsResponseTypeDef):
    """
    Type definition for `ClientDescribeLogGroups` `Response`

    - **logGroups** *(list) --*

      The log groups.

      - *(dict) --*

        Represents a log group.

        - **logGroupName** *(string) --*

          The name of the log group.

        - **creationTime** *(integer) --*

          The creation time of the log group, expressed as the number of milliseconds after Jan 1,
          1970 00:00:00 UTC.

        - **retentionInDays** *(integer) --*

          The number of days to retain the log events in the specified log group. Possible values
          are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, and 3653.

        - **metricFilterCount** *(integer) --*

          The number of metric filters.

        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the log group.

        - **storedBytes** *(integer) --*

          The number of bytes stored.

        - **kmsKeyId** *(string) --*

          The Amazon Resource Name (ARN) of the CMK to use when encrypting log data.

    - **nextToken** *(string) --*

      The token for the next set of items to return. The token expires after 24 hours.
    """


_ClientDescribeLogStreamsResponselogStreamsTypeDef = TypedDict(
    "_ClientDescribeLogStreamsResponselogStreamsTypeDef",
    {
        "logStreamName": str,
        "creationTime": int,
        "firstEventTimestamp": int,
        "lastEventTimestamp": int,
        "lastIngestionTime": int,
        "uploadSequenceToken": str,
        "arn": str,
        "storedBytes": int,
    },
    total=False,
)


class ClientDescribeLogStreamsResponselogStreamsTypeDef(
    _ClientDescribeLogStreamsResponselogStreamsTypeDef
):
    """
    Type definition for `ClientDescribeLogStreamsResponse` `logStreams`

    Represents a log stream, which is a sequence of log events from a single emitter of logs.

    - **logStreamName** *(string) --*

      The name of the log stream.

    - **creationTime** *(integer) --*

      The creation time of the stream, expressed as the number of milliseconds after Jan 1,
      1970 00:00:00 UTC.

    - **firstEventTimestamp** *(integer) --*

      The time of the first event, expressed as the number of milliseconds after Jan 1, 1970
      00:00:00 UTC.

    - **lastEventTimestamp** *(integer) --*

      The time of the most recent log event in the log stream in CloudWatch Logs. This number
      is expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. The
      ``lastEventTime`` value updates on an eventual consistency basis. It typically updates in
      less than an hour from ingestion, but may take longer in some rare situations.

    - **lastIngestionTime** *(integer) --*

      The ingestion time, expressed as the number of milliseconds after Jan 1, 1970 00:00:00
      UTC.

    - **uploadSequenceToken** *(string) --*

      The sequence token.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the log stream.

    - **storedBytes** *(integer) --*

      The number of bytes stored.

       **IMPORTANT:** On June 17, 2019, this parameter was deprecated for log streams, and is
       always reported as zero. This change applies only to log streams. The ``storedBytes``
       parameter for log groups is not affected.
    """


_ClientDescribeLogStreamsResponseTypeDef = TypedDict(
    "_ClientDescribeLogStreamsResponseTypeDef",
    {
        "logStreams": List[ClientDescribeLogStreamsResponselogStreamsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeLogStreamsResponseTypeDef(_ClientDescribeLogStreamsResponseTypeDef):
    """
    Type definition for `ClientDescribeLogStreams` `Response`

    - **logStreams** *(list) --*

      The log streams.

      - *(dict) --*

        Represents a log stream, which is a sequence of log events from a single emitter of logs.

        - **logStreamName** *(string) --*

          The name of the log stream.

        - **creationTime** *(integer) --*

          The creation time of the stream, expressed as the number of milliseconds after Jan 1,
          1970 00:00:00 UTC.

        - **firstEventTimestamp** *(integer) --*

          The time of the first event, expressed as the number of milliseconds after Jan 1, 1970
          00:00:00 UTC.

        - **lastEventTimestamp** *(integer) --*

          The time of the most recent log event in the log stream in CloudWatch Logs. This number
          is expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. The
          ``lastEventTime`` value updates on an eventual consistency basis. It typically updates in
          less than an hour from ingestion, but may take longer in some rare situations.

        - **lastIngestionTime** *(integer) --*

          The ingestion time, expressed as the number of milliseconds after Jan 1, 1970 00:00:00
          UTC.

        - **uploadSequenceToken** *(string) --*

          The sequence token.

        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the log stream.

        - **storedBytes** *(integer) --*

          The number of bytes stored.

           **IMPORTANT:** On June 17, 2019, this parameter was deprecated for log streams, and is
           always reported as zero. This change applies only to log streams. The ``storedBytes``
           parameter for log groups is not affected.

    - **nextToken** *(string) --*

      The token for the next set of items to return. The token expires after 24 hours.
    """


_ClientDescribeMetricFiltersResponsemetricFiltersmetricTransformationsTypeDef = TypedDict(
    "_ClientDescribeMetricFiltersResponsemetricFiltersmetricTransformationsTypeDef",
    {
        "metricName": str,
        "metricNamespace": str,
        "metricValue": str,
        "defaultValue": float,
    },
    total=False,
)


class ClientDescribeMetricFiltersResponsemetricFiltersmetricTransformationsTypeDef(
    _ClientDescribeMetricFiltersResponsemetricFiltersmetricTransformationsTypeDef
):
    """
    Type definition for `ClientDescribeMetricFiltersResponsemetricFilters` `metricTransformations`

    Indicates how to transform ingested log events to metric data in a CloudWatch metric.

    - **metricName** *(string) --*

      The name of the CloudWatch metric.

    - **metricNamespace** *(string) --*

      The namespace of the CloudWatch metric.

    - **metricValue** *(string) --*

      The value to publish to the CloudWatch metric when a filter pattern matches a log
      event.

    - **defaultValue** *(float) --*

      (Optional) The value to emit when a filter pattern does not match a log event. This
      value can be null.
    """


_ClientDescribeMetricFiltersResponsemetricFiltersTypeDef = TypedDict(
    "_ClientDescribeMetricFiltersResponsemetricFiltersTypeDef",
    {
        "filterName": str,
        "filterPattern": str,
        "metricTransformations": List[
            ClientDescribeMetricFiltersResponsemetricFiltersmetricTransformationsTypeDef
        ],
        "creationTime": int,
        "logGroupName": str,
    },
    total=False,
)


class ClientDescribeMetricFiltersResponsemetricFiltersTypeDef(
    _ClientDescribeMetricFiltersResponsemetricFiltersTypeDef
):
    """
    Type definition for `ClientDescribeMetricFiltersResponse` `metricFilters`

    Metric filters express how CloudWatch Logs would extract metric observations from ingested
    log events and transform them into metric data in a CloudWatch metric.

    - **filterName** *(string) --*

      The name of the metric filter.

    - **filterPattern** *(string) --*

      A symbolic description of how CloudWatch Logs should interpret the data in each log
      event. For example, a log event may contain timestamps, IP addresses, strings, and so on.
      You use the filter pattern to specify what to look for in the log event message.

    - **metricTransformations** *(list) --*

      The metric transformations.

      - *(dict) --*

        Indicates how to transform ingested log events to metric data in a CloudWatch metric.

        - **metricName** *(string) --*

          The name of the CloudWatch metric.

        - **metricNamespace** *(string) --*

          The namespace of the CloudWatch metric.

        - **metricValue** *(string) --*

          The value to publish to the CloudWatch metric when a filter pattern matches a log
          event.

        - **defaultValue** *(float) --*

          (Optional) The value to emit when a filter pattern does not match a log event. This
          value can be null.

    - **creationTime** *(integer) --*

      The creation time of the metric filter, expressed as the number of milliseconds after Jan
      1, 1970 00:00:00 UTC.

    - **logGroupName** *(string) --*

      The name of the log group.
    """


_ClientDescribeMetricFiltersResponseTypeDef = TypedDict(
    "_ClientDescribeMetricFiltersResponseTypeDef",
    {
        "metricFilters": List[ClientDescribeMetricFiltersResponsemetricFiltersTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeMetricFiltersResponseTypeDef(
    _ClientDescribeMetricFiltersResponseTypeDef
):
    """
    Type definition for `ClientDescribeMetricFilters` `Response`

    - **metricFilters** *(list) --*

      The metric filters.

      - *(dict) --*

        Metric filters express how CloudWatch Logs would extract metric observations from ingested
        log events and transform them into metric data in a CloudWatch metric.

        - **filterName** *(string) --*

          The name of the metric filter.

        - **filterPattern** *(string) --*

          A symbolic description of how CloudWatch Logs should interpret the data in each log
          event. For example, a log event may contain timestamps, IP addresses, strings, and so on.
          You use the filter pattern to specify what to look for in the log event message.

        - **metricTransformations** *(list) --*

          The metric transformations.

          - *(dict) --*

            Indicates how to transform ingested log events to metric data in a CloudWatch metric.

            - **metricName** *(string) --*

              The name of the CloudWatch metric.

            - **metricNamespace** *(string) --*

              The namespace of the CloudWatch metric.

            - **metricValue** *(string) --*

              The value to publish to the CloudWatch metric when a filter pattern matches a log
              event.

            - **defaultValue** *(float) --*

              (Optional) The value to emit when a filter pattern does not match a log event. This
              value can be null.

        - **creationTime** *(integer) --*

          The creation time of the metric filter, expressed as the number of milliseconds after Jan
          1, 1970 00:00:00 UTC.

        - **logGroupName** *(string) --*

          The name of the log group.

    - **nextToken** *(string) --*

      The token for the next set of items to return. The token expires after 24 hours.
    """


_ClientDescribeQueriesResponsequeriesTypeDef = TypedDict(
    "_ClientDescribeQueriesResponsequeriesTypeDef",
    {
        "queryId": str,
        "queryString": str,
        "status": str,
        "createTime": int,
        "logGroupName": str,
    },
    total=False,
)


class ClientDescribeQueriesResponsequeriesTypeDef(
    _ClientDescribeQueriesResponsequeriesTypeDef
):
    """
    Type definition for `ClientDescribeQueriesResponse` `queries`

    Information about one CloudWatch Logs Insights query that matches the request in a
    ``DescribeQueries`` operation.

    - **queryId** *(string) --*

      The unique ID number of this query.

    - **queryString** *(string) --*

      The query string used in this query.

    - **status** *(string) --*

      The status of this query. Possible values are ``Cancelled`` , ``Complete`` , ``Failed`` ,
      ``Running`` , ``Scheduled`` , and ``Unknown`` .

    - **createTime** *(integer) --*

      The date and time that this query was created.

    - **logGroupName** *(string) --*

      The name of the log group scanned by this query.
    """


_ClientDescribeQueriesResponseTypeDef = TypedDict(
    "_ClientDescribeQueriesResponseTypeDef",
    {"queries": List[ClientDescribeQueriesResponsequeriesTypeDef], "nextToken": str},
    total=False,
)


class ClientDescribeQueriesResponseTypeDef(_ClientDescribeQueriesResponseTypeDef):
    """
    Type definition for `ClientDescribeQueries` `Response`

    - **queries** *(list) --*

      The list of queries that match the request.

      - *(dict) --*

        Information about one CloudWatch Logs Insights query that matches the request in a
        ``DescribeQueries`` operation.

        - **queryId** *(string) --*

          The unique ID number of this query.

        - **queryString** *(string) --*

          The query string used in this query.

        - **status** *(string) --*

          The status of this query. Possible values are ``Cancelled`` , ``Complete`` , ``Failed`` ,
          ``Running`` , ``Scheduled`` , and ``Unknown`` .

        - **createTime** *(integer) --*

          The date and time that this query was created.

        - **logGroupName** *(string) --*

          The name of the log group scanned by this query.

    - **nextToken** *(string) --*

      The token for the next set of items to return. The token expires after 24 hours.
    """


_ClientDescribeResourcePoliciesResponseresourcePoliciesTypeDef = TypedDict(
    "_ClientDescribeResourcePoliciesResponseresourcePoliciesTypeDef",
    {"policyName": str, "policyDocument": str, "lastUpdatedTime": int},
    total=False,
)


class ClientDescribeResourcePoliciesResponseresourcePoliciesTypeDef(
    _ClientDescribeResourcePoliciesResponseresourcePoliciesTypeDef
):
    """
    Type definition for `ClientDescribeResourcePoliciesResponse` `resourcePolicies`

    A policy enabling one or more entities to put logs to a log group in this account.

    - **policyName** *(string) --*

      The name of the resource policy.

    - **policyDocument** *(string) --*

      The details of the policy.

    - **lastUpdatedTime** *(integer) --*

      Timestamp showing when this policy was last updated, expressed as the number of
      milliseconds after Jan 1, 1970 00:00:00 UTC.
    """


_ClientDescribeResourcePoliciesResponseTypeDef = TypedDict(
    "_ClientDescribeResourcePoliciesResponseTypeDef",
    {
        "resourcePolicies": List[
            ClientDescribeResourcePoliciesResponseresourcePoliciesTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeResourcePoliciesResponseTypeDef(
    _ClientDescribeResourcePoliciesResponseTypeDef
):
    """
    Type definition for `ClientDescribeResourcePolicies` `Response`

    - **resourcePolicies** *(list) --*

      The resource policies that exist in this account.

      - *(dict) --*

        A policy enabling one or more entities to put logs to a log group in this account.

        - **policyName** *(string) --*

          The name of the resource policy.

        - **policyDocument** *(string) --*

          The details of the policy.

        - **lastUpdatedTime** *(integer) --*

          Timestamp showing when this policy was last updated, expressed as the number of
          milliseconds after Jan 1, 1970 00:00:00 UTC.

    - **nextToken** *(string) --*

      The token for the next set of items to return. The token expires after 24 hours.
    """


_ClientDescribeSubscriptionFiltersResponsesubscriptionFiltersTypeDef = TypedDict(
    "_ClientDescribeSubscriptionFiltersResponsesubscriptionFiltersTypeDef",
    {
        "filterName": str,
        "logGroupName": str,
        "filterPattern": str,
        "destinationArn": str,
        "roleArn": str,
        "distribution": str,
        "creationTime": int,
    },
    total=False,
)


class ClientDescribeSubscriptionFiltersResponsesubscriptionFiltersTypeDef(
    _ClientDescribeSubscriptionFiltersResponsesubscriptionFiltersTypeDef
):
    """
    Type definition for `ClientDescribeSubscriptionFiltersResponse` `subscriptionFilters`

    Represents a subscription filter.

    - **filterName** *(string) --*

      The name of the subscription filter.

    - **logGroupName** *(string) --*

      The name of the log group.

    - **filterPattern** *(string) --*

      A symbolic description of how CloudWatch Logs should interpret the data in each log
      event. For example, a log event may contain timestamps, IP addresses, strings, and so on.
      You use the filter pattern to specify what to look for in the log event message.

    - **destinationArn** *(string) --*

      The Amazon Resource Name (ARN) of the destination.

    - **roleArn** *(string) --*

    - **distribution** *(string) --*

      The method used to distribute log data to the destination, which can be either random or
      grouped by log stream.

    - **creationTime** *(integer) --*

      The creation time of the subscription filter, expressed as the number of milliseconds
      after Jan 1, 1970 00:00:00 UTC.
    """


_ClientDescribeSubscriptionFiltersResponseTypeDef = TypedDict(
    "_ClientDescribeSubscriptionFiltersResponseTypeDef",
    {
        "subscriptionFilters": List[
            ClientDescribeSubscriptionFiltersResponsesubscriptionFiltersTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeSubscriptionFiltersResponseTypeDef(
    _ClientDescribeSubscriptionFiltersResponseTypeDef
):
    """
    Type definition for `ClientDescribeSubscriptionFilters` `Response`

    - **subscriptionFilters** *(list) --*

      The subscription filters.

      - *(dict) --*

        Represents a subscription filter.

        - **filterName** *(string) --*

          The name of the subscription filter.

        - **logGroupName** *(string) --*

          The name of the log group.

        - **filterPattern** *(string) --*

          A symbolic description of how CloudWatch Logs should interpret the data in each log
          event. For example, a log event may contain timestamps, IP addresses, strings, and so on.
          You use the filter pattern to specify what to look for in the log event message.

        - **destinationArn** *(string) --*

          The Amazon Resource Name (ARN) of the destination.

        - **roleArn** *(string) --*

        - **distribution** *(string) --*

          The method used to distribute log data to the destination, which can be either random or
          grouped by log stream.

        - **creationTime** *(integer) --*

          The creation time of the subscription filter, expressed as the number of milliseconds
          after Jan 1, 1970 00:00:00 UTC.

    - **nextToken** *(string) --*

      The token for the next set of items to return. The token expires after 24 hours.
    """


_ClientFilterLogEventsResponseeventsTypeDef = TypedDict(
    "_ClientFilterLogEventsResponseeventsTypeDef",
    {
        "logStreamName": str,
        "timestamp": int,
        "message": str,
        "ingestionTime": int,
        "eventId": str,
    },
    total=False,
)


class ClientFilterLogEventsResponseeventsTypeDef(
    _ClientFilterLogEventsResponseeventsTypeDef
):
    """
    Type definition for `ClientFilterLogEventsResponse` `events`

    Represents a matched event.

    - **logStreamName** *(string) --*

      The name of the log stream to which this event belongs.

    - **timestamp** *(integer) --*

      The time the event occurred, expressed as the number of milliseconds after Jan 1, 1970
      00:00:00 UTC.

    - **message** *(string) --*

      The data contained in the log event.

    - **ingestionTime** *(integer) --*

      The time the event was ingested, expressed as the number of milliseconds after Jan 1,
      1970 00:00:00 UTC.

    - **eventId** *(string) --*

      The ID of the event.
    """


_ClientFilterLogEventsResponsesearchedLogStreamsTypeDef = TypedDict(
    "_ClientFilterLogEventsResponsesearchedLogStreamsTypeDef",
    {"logStreamName": str, "searchedCompletely": bool},
    total=False,
)


class ClientFilterLogEventsResponsesearchedLogStreamsTypeDef(
    _ClientFilterLogEventsResponsesearchedLogStreamsTypeDef
):
    """
    Type definition for `ClientFilterLogEventsResponse` `searchedLogStreams`

    Represents the search status of a log stream.

    - **logStreamName** *(string) --*

      The name of the log stream.

    - **searchedCompletely** *(boolean) --*

      Indicates whether all the events in this log stream were searched.
    """


_ClientFilterLogEventsResponseTypeDef = TypedDict(
    "_ClientFilterLogEventsResponseTypeDef",
    {
        "events": List[ClientFilterLogEventsResponseeventsTypeDef],
        "searchedLogStreams": List[
            ClientFilterLogEventsResponsesearchedLogStreamsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientFilterLogEventsResponseTypeDef(_ClientFilterLogEventsResponseTypeDef):
    """
    Type definition for `ClientFilterLogEvents` `Response`

    - **events** *(list) --*

      The matched events.

      - *(dict) --*

        Represents a matched event.

        - **logStreamName** *(string) --*

          The name of the log stream to which this event belongs.

        - **timestamp** *(integer) --*

          The time the event occurred, expressed as the number of milliseconds after Jan 1, 1970
          00:00:00 UTC.

        - **message** *(string) --*

          The data contained in the log event.

        - **ingestionTime** *(integer) --*

          The time the event was ingested, expressed as the number of milliseconds after Jan 1,
          1970 00:00:00 UTC.

        - **eventId** *(string) --*

          The ID of the event.

    - **searchedLogStreams** *(list) --*

      Indicates which log streams have been searched and whether each has been searched completely.

      - *(dict) --*

        Represents the search status of a log stream.

        - **logStreamName** *(string) --*

          The name of the log stream.

        - **searchedCompletely** *(boolean) --*

          Indicates whether all the events in this log stream were searched.

    - **nextToken** *(string) --*

      The token to use when requesting the next set of items. The token expires after 24 hours.
    """


_ClientGetLogEventsResponseeventsTypeDef = TypedDict(
    "_ClientGetLogEventsResponseeventsTypeDef",
    {"timestamp": int, "message": str, "ingestionTime": int},
    total=False,
)


class ClientGetLogEventsResponseeventsTypeDef(_ClientGetLogEventsResponseeventsTypeDef):
    """
    Type definition for `ClientGetLogEventsResponse` `events`

    Represents a log event.

    - **timestamp** *(integer) --*

      The time the event occurred, expressed as the number of milliseconds after Jan 1, 1970
      00:00:00 UTC.

    - **message** *(string) --*

      The data contained in the log event.

    - **ingestionTime** *(integer) --*

      The time the event was ingested, expressed as the number of milliseconds after Jan 1,
      1970 00:00:00 UTC.
    """


_ClientGetLogEventsResponseTypeDef = TypedDict(
    "_ClientGetLogEventsResponseTypeDef",
    {
        "events": List[ClientGetLogEventsResponseeventsTypeDef],
        "nextForwardToken": str,
        "nextBackwardToken": str,
    },
    total=False,
)


class ClientGetLogEventsResponseTypeDef(_ClientGetLogEventsResponseTypeDef):
    """
    Type definition for `ClientGetLogEvents` `Response`

    - **events** *(list) --*

      The events.

      - *(dict) --*

        Represents a log event.

        - **timestamp** *(integer) --*

          The time the event occurred, expressed as the number of milliseconds after Jan 1, 1970
          00:00:00 UTC.

        - **message** *(string) --*

          The data contained in the log event.

        - **ingestionTime** *(integer) --*

          The time the event was ingested, expressed as the number of milliseconds after Jan 1,
          1970 00:00:00 UTC.

    - **nextForwardToken** *(string) --*

      The token for the next set of items in the forward direction. The token expires after 24
      hours. If you have reached the end of the stream, it will return the same token you passed in.

    - **nextBackwardToken** *(string) --*

      The token for the next set of items in the backward direction. The token expires after 24
      hours. This token will never be null. If you have reached the end of the stream, it will
      return the same token you passed in.
    """


_ClientGetLogGroupFieldsResponselogGroupFieldsTypeDef = TypedDict(
    "_ClientGetLogGroupFieldsResponselogGroupFieldsTypeDef",
    {"name": str, "percent": int},
    total=False,
)


class ClientGetLogGroupFieldsResponselogGroupFieldsTypeDef(
    _ClientGetLogGroupFieldsResponselogGroupFieldsTypeDef
):
    """
    Type definition for `ClientGetLogGroupFieldsResponse` `logGroupFields`

    The fields contained in log events found by a ``GetLogGroupFields`` operation, along with
    the percentage of queried log events in which each field appears.

    - **name** *(string) --*

      The name of a log field.

    - **percent** *(integer) --*

      The percentage of log events queried that contained the field.
    """


_ClientGetLogGroupFieldsResponseTypeDef = TypedDict(
    "_ClientGetLogGroupFieldsResponseTypeDef",
    {"logGroupFields": List[ClientGetLogGroupFieldsResponselogGroupFieldsTypeDef]},
    total=False,
)


class ClientGetLogGroupFieldsResponseTypeDef(_ClientGetLogGroupFieldsResponseTypeDef):
    """
    Type definition for `ClientGetLogGroupFields` `Response`

    - **logGroupFields** *(list) --*

      The array of fields found in the query. Each object in the array contains the name of the
      field, along with the percentage of time it appeared in the log events that were queried.

      - *(dict) --*

        The fields contained in log events found by a ``GetLogGroupFields`` operation, along with
        the percentage of queried log events in which each field appears.

        - **name** *(string) --*

          The name of a log field.

        - **percent** *(integer) --*

          The percentage of log events queried that contained the field.
    """


_ClientGetLogRecordResponseTypeDef = TypedDict(
    "_ClientGetLogRecordResponseTypeDef", {"logRecord": Dict[str, str]}, total=False
)


class ClientGetLogRecordResponseTypeDef(_ClientGetLogRecordResponseTypeDef):
    """
    Type definition for `ClientGetLogRecord` `Response`

    - **logRecord** *(dict) --*

      The requested log event, as a JSON string.

      - *(string) --*

        - *(string) --*
    """


_ClientGetQueryResultsResponseresultsTypeDef = TypedDict(
    "_ClientGetQueryResultsResponseresultsTypeDef",
    {"field": str, "value": str},
    total=False,
)


class ClientGetQueryResultsResponseresultsTypeDef(
    _ClientGetQueryResultsResponseresultsTypeDef
):
    """
    Type definition for `ClientGetQueryResultsResponse` `results`

    Contains one field from one log event returned by a CloudWatch Logs Insights query, along
    with the value of that field.

    - **field** *(string) --*

      The log event field.

    - **value** *(string) --*

      The value of this field.
    """


_ClientGetQueryResultsResponsestatisticsTypeDef = TypedDict(
    "_ClientGetQueryResultsResponsestatisticsTypeDef",
    {"recordsMatched": float, "recordsScanned": float, "bytesScanned": float},
    total=False,
)


class ClientGetQueryResultsResponsestatisticsTypeDef(
    _ClientGetQueryResultsResponsestatisticsTypeDef
):
    """
    Type definition for `ClientGetQueryResultsResponse` `statistics`

    Includes the number of log events scanned by the query, the number of log events that matched
    the query criteria, and the total number of bytes in the log events that were scanned.

    - **recordsMatched** *(float) --*

      The number of log events that matched the query string.

    - **recordsScanned** *(float) --*

      The total number of log events scanned during the query.

    - **bytesScanned** *(float) --*

      The total number of bytes in the log events scanned during the query.
    """


_ClientGetQueryResultsResponseTypeDef = TypedDict(
    "_ClientGetQueryResultsResponseTypeDef",
    {
        "results": List[List[ClientGetQueryResultsResponseresultsTypeDef]],
        "statistics": ClientGetQueryResultsResponsestatisticsTypeDef,
        "status": str,
    },
    total=False,
)


class ClientGetQueryResultsResponseTypeDef(_ClientGetQueryResultsResponseTypeDef):
    """
    Type definition for `ClientGetQueryResults` `Response`

    - **results** *(list) --*

      The log events that matched the query criteria during the most recent time it ran.

      The ``results`` value is an array of arrays. Each log event is one object in the top-level
      array. Each of these log event objects is an array of ``field`` /``value`` pairs.

      - *(list) --*

        - *(dict) --*

          Contains one field from one log event returned by a CloudWatch Logs Insights query, along
          with the value of that field.

          - **field** *(string) --*

            The log event field.

          - **value** *(string) --*

            The value of this field.

    - **statistics** *(dict) --*

      Includes the number of log events scanned by the query, the number of log events that matched
      the query criteria, and the total number of bytes in the log events that were scanned.

      - **recordsMatched** *(float) --*

        The number of log events that matched the query string.

      - **recordsScanned** *(float) --*

        The total number of log events scanned during the query.

      - **bytesScanned** *(float) --*

        The total number of bytes in the log events scanned during the query.

    - **status** *(string) --*

      The status of the most recent running of the query. Possible values are ``Cancelled`` ,
      ``Complete`` , ``Failed`` , ``Running`` , ``Scheduled`` , ``Timeout`` , and ``Unknown`` .

      Queries time out after 15 minutes of execution. To avoid having your queries time out, reduce
      the time range being searched, or partition your query into a number of queries.
    """


_ClientListTagsLogGroupResponseTypeDef = TypedDict(
    "_ClientListTagsLogGroupResponseTypeDef", {"tags": Dict[str, str]}, total=False
)


class ClientListTagsLogGroupResponseTypeDef(_ClientListTagsLogGroupResponseTypeDef):
    """
    Type definition for `ClientListTagsLogGroup` `Response`

    - **tags** *(dict) --*

      The tags for the log group.

      - *(string) --*

        - *(string) --*
    """


_ClientPutDestinationResponsedestinationTypeDef = TypedDict(
    "_ClientPutDestinationResponsedestinationTypeDef",
    {
        "destinationName": str,
        "targetArn": str,
        "roleArn": str,
        "accessPolicy": str,
        "arn": str,
        "creationTime": int,
    },
    total=False,
)


class ClientPutDestinationResponsedestinationTypeDef(
    _ClientPutDestinationResponsedestinationTypeDef
):
    """
    Type definition for `ClientPutDestinationResponse` `destination`

    The destination.

    - **destinationName** *(string) --*

      The name of the destination.

    - **targetArn** *(string) --*

      The Amazon Resource Name (ARN) of the physical target to where the log events are delivered
      (for example, a Kinesis stream).

    - **roleArn** *(string) --*

      A role for impersonation, used when delivering log events to the target.

    - **accessPolicy** *(string) --*

      An IAM policy document that governs which AWS accounts can create subscription filters
      against this destination.

    - **arn** *(string) --*

      The ARN of this destination.

    - **creationTime** *(integer) --*

      The creation time of the destination, expressed as the number of milliseconds after Jan 1,
      1970 00:00:00 UTC.
    """


_ClientPutDestinationResponseTypeDef = TypedDict(
    "_ClientPutDestinationResponseTypeDef",
    {"destination": ClientPutDestinationResponsedestinationTypeDef},
    total=False,
)


class ClientPutDestinationResponseTypeDef(_ClientPutDestinationResponseTypeDef):
    """
    Type definition for `ClientPutDestination` `Response`

    - **destination** *(dict) --*

      The destination.

      - **destinationName** *(string) --*

        The name of the destination.

      - **targetArn** *(string) --*

        The Amazon Resource Name (ARN) of the physical target to where the log events are delivered
        (for example, a Kinesis stream).

      - **roleArn** *(string) --*

        A role for impersonation, used when delivering log events to the target.

      - **accessPolicy** *(string) --*

        An IAM policy document that governs which AWS accounts can create subscription filters
        against this destination.

      - **arn** *(string) --*

        The ARN of this destination.

      - **creationTime** *(integer) --*

        The creation time of the destination, expressed as the number of milliseconds after Jan 1,
        1970 00:00:00 UTC.
    """


_ClientPutLogEventsResponserejectedLogEventsInfoTypeDef = TypedDict(
    "_ClientPutLogEventsResponserejectedLogEventsInfoTypeDef",
    {
        "tooNewLogEventStartIndex": int,
        "tooOldLogEventEndIndex": int,
        "expiredLogEventEndIndex": int,
    },
    total=False,
)


class ClientPutLogEventsResponserejectedLogEventsInfoTypeDef(
    _ClientPutLogEventsResponserejectedLogEventsInfoTypeDef
):
    """
    Type definition for `ClientPutLogEventsResponse` `rejectedLogEventsInfo`

    The rejected events.

    - **tooNewLogEventStartIndex** *(integer) --*

      The log events that are too new.

    - **tooOldLogEventEndIndex** *(integer) --*

      The log events that are too old.

    - **expiredLogEventEndIndex** *(integer) --*

      The expired log events.
    """


_ClientPutLogEventsResponseTypeDef = TypedDict(
    "_ClientPutLogEventsResponseTypeDef",
    {
        "nextSequenceToken": str,
        "rejectedLogEventsInfo": ClientPutLogEventsResponserejectedLogEventsInfoTypeDef,
    },
    total=False,
)


class ClientPutLogEventsResponseTypeDef(_ClientPutLogEventsResponseTypeDef):
    """
    Type definition for `ClientPutLogEvents` `Response`

    - **nextSequenceToken** *(string) --*

      The next sequence token.

    - **rejectedLogEventsInfo** *(dict) --*

      The rejected events.

      - **tooNewLogEventStartIndex** *(integer) --*

        The log events that are too new.

      - **tooOldLogEventEndIndex** *(integer) --*

        The log events that are too old.

      - **expiredLogEventEndIndex** *(integer) --*

        The expired log events.
    """


_ClientPutLogEventslogEventsTypeDef = TypedDict(
    "_ClientPutLogEventslogEventsTypeDef", {"timestamp": int, "message": str}
)


class ClientPutLogEventslogEventsTypeDef(_ClientPutLogEventslogEventsTypeDef):
    """
    Type definition for `ClientPutLogEvents` `logEvents`

    Represents a log event, which is a record of activity that was recorded by the application or
    resource being monitored.

    - **timestamp** *(integer) --* **[REQUIRED]**

      The time the event occurred, expressed as the number of milliseconds after Jan 1, 1970
      00:00:00 UTC.

    - **message** *(string) --* **[REQUIRED]**

      The raw event message.
    """


_RequiredClientPutMetricFiltermetricTransformationsTypeDef = TypedDict(
    "_RequiredClientPutMetricFiltermetricTransformationsTypeDef",
    {"metricName": str, "metricNamespace": str, "metricValue": str},
)
_OptionalClientPutMetricFiltermetricTransformationsTypeDef = TypedDict(
    "_OptionalClientPutMetricFiltermetricTransformationsTypeDef",
    {"defaultValue": float},
    total=False,
)


class ClientPutMetricFiltermetricTransformationsTypeDef(
    _RequiredClientPutMetricFiltermetricTransformationsTypeDef,
    _OptionalClientPutMetricFiltermetricTransformationsTypeDef,
):
    """
    Type definition for `ClientPutMetricFilter` `metricTransformations`

    Indicates how to transform ingested log events to metric data in a CloudWatch metric.

    - **metricName** *(string) --* **[REQUIRED]**

      The name of the CloudWatch metric.

    - **metricNamespace** *(string) --* **[REQUIRED]**

      The namespace of the CloudWatch metric.

    - **metricValue** *(string) --* **[REQUIRED]**

      The value to publish to the CloudWatch metric when a filter pattern matches a log event.

    - **defaultValue** *(float) --*

      (Optional) The value to emit when a filter pattern does not match a log event. This value can
      be null.
    """


_ClientPutResourcePolicyResponseresourcePolicyTypeDef = TypedDict(
    "_ClientPutResourcePolicyResponseresourcePolicyTypeDef",
    {"policyName": str, "policyDocument": str, "lastUpdatedTime": int},
    total=False,
)


class ClientPutResourcePolicyResponseresourcePolicyTypeDef(
    _ClientPutResourcePolicyResponseresourcePolicyTypeDef
):
    """
    Type definition for `ClientPutResourcePolicyResponse` `resourcePolicy`

    The new policy.

    - **policyName** *(string) --*

      The name of the resource policy.

    - **policyDocument** *(string) --*

      The details of the policy.

    - **lastUpdatedTime** *(integer) --*

      Timestamp showing when this policy was last updated, expressed as the number of
      milliseconds after Jan 1, 1970 00:00:00 UTC.
    """


_ClientPutResourcePolicyResponseTypeDef = TypedDict(
    "_ClientPutResourcePolicyResponseTypeDef",
    {"resourcePolicy": ClientPutResourcePolicyResponseresourcePolicyTypeDef},
    total=False,
)


class ClientPutResourcePolicyResponseTypeDef(_ClientPutResourcePolicyResponseTypeDef):
    """
    Type definition for `ClientPutResourcePolicy` `Response`

    - **resourcePolicy** *(dict) --*

      The new policy.

      - **policyName** *(string) --*

        The name of the resource policy.

      - **policyDocument** *(string) --*

        The details of the policy.

      - **lastUpdatedTime** *(integer) --*

        Timestamp showing when this policy was last updated, expressed as the number of
        milliseconds after Jan 1, 1970 00:00:00 UTC.
    """


_ClientStartQueryResponseTypeDef = TypedDict(
    "_ClientStartQueryResponseTypeDef", {"queryId": str}, total=False
)


class ClientStartQueryResponseTypeDef(_ClientStartQueryResponseTypeDef):
    """
    Type definition for `ClientStartQuery` `Response`

    - **queryId** *(string) --*

      The unique ID of the query.
    """


_ClientStopQueryResponseTypeDef = TypedDict(
    "_ClientStopQueryResponseTypeDef", {"success": bool}, total=False
)


class ClientStopQueryResponseTypeDef(_ClientStopQueryResponseTypeDef):
    """
    Type definition for `ClientStopQuery` `Response`

    - **success** *(boolean) --*

      This is true if the query was stopped by the ``StopQuery`` operation.
    """


_ClientTestMetricFilterResponsematchesTypeDef = TypedDict(
    "_ClientTestMetricFilterResponsematchesTypeDef",
    {"eventNumber": int, "eventMessage": str, "extractedValues": Dict[str, str]},
    total=False,
)


class ClientTestMetricFilterResponsematchesTypeDef(
    _ClientTestMetricFilterResponsematchesTypeDef
):
    """
    Type definition for `ClientTestMetricFilterResponse` `matches`

    Represents a matched event.

    - **eventNumber** *(integer) --*

      The event number.

    - **eventMessage** *(string) --*

      The raw event data.

    - **extractedValues** *(dict) --*

      The values extracted from the event data by the filter.

      - *(string) --*

        - *(string) --*
    """


_ClientTestMetricFilterResponseTypeDef = TypedDict(
    "_ClientTestMetricFilterResponseTypeDef",
    {"matches": List[ClientTestMetricFilterResponsematchesTypeDef]},
    total=False,
)


class ClientTestMetricFilterResponseTypeDef(_ClientTestMetricFilterResponseTypeDef):
    """
    Type definition for `ClientTestMetricFilter` `Response`

    - **matches** *(list) --*

      The matched events.

      - *(dict) --*

        Represents a matched event.

        - **eventNumber** *(integer) --*

          The event number.

        - **eventMessage** *(string) --*

          The raw event data.

        - **extractedValues** *(dict) --*

          The values extracted from the event data by the filter.

          - *(string) --*

            - *(string) --*
    """


_DescribeDestinationsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDestinationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDestinationsPaginatePaginationConfigTypeDef(
    _DescribeDestinationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeDestinationsPaginate` `PaginationConfig`

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


_DescribeDestinationsPaginateResponsedestinationsTypeDef = TypedDict(
    "_DescribeDestinationsPaginateResponsedestinationsTypeDef",
    {
        "destinationName": str,
        "targetArn": str,
        "roleArn": str,
        "accessPolicy": str,
        "arn": str,
        "creationTime": int,
    },
    total=False,
)


class DescribeDestinationsPaginateResponsedestinationsTypeDef(
    _DescribeDestinationsPaginateResponsedestinationsTypeDef
):
    """
    Type definition for `DescribeDestinationsPaginateResponse` `destinations`

    Represents a cross-account destination that receives subscription log events.

    - **destinationName** *(string) --*

      The name of the destination.

    - **targetArn** *(string) --*

      The Amazon Resource Name (ARN) of the physical target to where the log events are
      delivered (for example, a Kinesis stream).

    - **roleArn** *(string) --*

      A role for impersonation, used when delivering log events to the target.

    - **accessPolicy** *(string) --*

      An IAM policy document that governs which AWS accounts can create subscription filters
      against this destination.

    - **arn** *(string) --*

      The ARN of this destination.

    - **creationTime** *(integer) --*

      The creation time of the destination, expressed as the number of milliseconds after Jan
      1, 1970 00:00:00 UTC.
    """


_DescribeDestinationsPaginateResponseTypeDef = TypedDict(
    "_DescribeDestinationsPaginateResponseTypeDef",
    {
        "destinations": List[DescribeDestinationsPaginateResponsedestinationsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeDestinationsPaginateResponseTypeDef(
    _DescribeDestinationsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeDestinationsPaginate` `Response`

    - **destinations** *(list) --*

      The destinations.

      - *(dict) --*

        Represents a cross-account destination that receives subscription log events.

        - **destinationName** *(string) --*

          The name of the destination.

        - **targetArn** *(string) --*

          The Amazon Resource Name (ARN) of the physical target to where the log events are
          delivered (for example, a Kinesis stream).

        - **roleArn** *(string) --*

          A role for impersonation, used when delivering log events to the target.

        - **accessPolicy** *(string) --*

          An IAM policy document that governs which AWS accounts can create subscription filters
          against this destination.

        - **arn** *(string) --*

          The ARN of this destination.

        - **creationTime** *(integer) --*

          The creation time of the destination, expressed as the number of milliseconds after Jan
          1, 1970 00:00:00 UTC.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeExportTasksPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeExportTasksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeExportTasksPaginatePaginationConfigTypeDef(
    _DescribeExportTasksPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeExportTasksPaginate` `PaginationConfig`

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


_DescribeExportTasksPaginateResponseexportTasksexecutionInfoTypeDef = TypedDict(
    "_DescribeExportTasksPaginateResponseexportTasksexecutionInfoTypeDef",
    {"creationTime": int, "completionTime": int},
    total=False,
)


class DescribeExportTasksPaginateResponseexportTasksexecutionInfoTypeDef(
    _DescribeExportTasksPaginateResponseexportTasksexecutionInfoTypeDef
):
    """
    Type definition for `DescribeExportTasksPaginateResponseexportTasks` `executionInfo`

    Execution info about the export task.

    - **creationTime** *(integer) --*

      The creation time of the export task, expressed as the number of milliseconds after Jan
      1, 1970 00:00:00 UTC.

    - **completionTime** *(integer) --*

      The completion time of the export task, expressed as the number of milliseconds after
      Jan 1, 1970 00:00:00 UTC.
    """


_DescribeExportTasksPaginateResponseexportTasksstatusTypeDef = TypedDict(
    "_DescribeExportTasksPaginateResponseexportTasksstatusTypeDef",
    {"code": str, "message": str},
    total=False,
)


class DescribeExportTasksPaginateResponseexportTasksstatusTypeDef(
    _DescribeExportTasksPaginateResponseexportTasksstatusTypeDef
):
    """
    Type definition for `DescribeExportTasksPaginateResponseexportTasks` `status`

    The status of the export task.

    - **code** *(string) --*

      The status code of the export task.

    - **message** *(string) --*

      The status message related to the status code.
    """


_DescribeExportTasksPaginateResponseexportTasksTypeDef = TypedDict(
    "_DescribeExportTasksPaginateResponseexportTasksTypeDef",
    {
        "taskId": str,
        "taskName": str,
        "logGroupName": str,
        "from": int,
        "to": int,
        "destination": str,
        "destinationPrefix": str,
        "status": DescribeExportTasksPaginateResponseexportTasksstatusTypeDef,
        "executionInfo": DescribeExportTasksPaginateResponseexportTasksexecutionInfoTypeDef,
    },
    total=False,
)


class DescribeExportTasksPaginateResponseexportTasksTypeDef(
    _DescribeExportTasksPaginateResponseexportTasksTypeDef
):
    """
    Type definition for `DescribeExportTasksPaginateResponse` `exportTasks`

    Represents an export task.

    - **taskId** *(string) --*

      The ID of the export task.

    - **taskName** *(string) --*

      The name of the export task.

    - **logGroupName** *(string) --*

      The name of the log group from which logs data was exported.

    - **from** *(integer) --*

      The start time, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.
      Events with a timestamp before this time are not exported.

    - **to** *(integer) --*

      The end time, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.
      Events with a timestamp later than this time are not exported.

    - **destination** *(string) --*

      The name of Amazon S3 bucket to which the log data was exported.

    - **destinationPrefix** *(string) --*

      The prefix that was used as the start of Amazon S3 key for every object exported.

    - **status** *(dict) --*

      The status of the export task.

      - **code** *(string) --*

        The status code of the export task.

      - **message** *(string) --*

        The status message related to the status code.

    - **executionInfo** *(dict) --*

      Execution info about the export task.

      - **creationTime** *(integer) --*

        The creation time of the export task, expressed as the number of milliseconds after Jan
        1, 1970 00:00:00 UTC.

      - **completionTime** *(integer) --*

        The completion time of the export task, expressed as the number of milliseconds after
        Jan 1, 1970 00:00:00 UTC.
    """


_DescribeExportTasksPaginateResponseTypeDef = TypedDict(
    "_DescribeExportTasksPaginateResponseTypeDef",
    {
        "exportTasks": List[DescribeExportTasksPaginateResponseexportTasksTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeExportTasksPaginateResponseTypeDef(
    _DescribeExportTasksPaginateResponseTypeDef
):
    """
    Type definition for `DescribeExportTasksPaginate` `Response`

    - **exportTasks** *(list) --*

      The export tasks.

      - *(dict) --*

        Represents an export task.

        - **taskId** *(string) --*

          The ID of the export task.

        - **taskName** *(string) --*

          The name of the export task.

        - **logGroupName** *(string) --*

          The name of the log group from which logs data was exported.

        - **from** *(integer) --*

          The start time, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.
          Events with a timestamp before this time are not exported.

        - **to** *(integer) --*

          The end time, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.
          Events with a timestamp later than this time are not exported.

        - **destination** *(string) --*

          The name of Amazon S3 bucket to which the log data was exported.

        - **destinationPrefix** *(string) --*

          The prefix that was used as the start of Amazon S3 key for every object exported.

        - **status** *(dict) --*

          The status of the export task.

          - **code** *(string) --*

            The status code of the export task.

          - **message** *(string) --*

            The status message related to the status code.

        - **executionInfo** *(dict) --*

          Execution info about the export task.

          - **creationTime** *(integer) --*

            The creation time of the export task, expressed as the number of milliseconds after Jan
            1, 1970 00:00:00 UTC.

          - **completionTime** *(integer) --*

            The completion time of the export task, expressed as the number of milliseconds after
            Jan 1, 1970 00:00:00 UTC.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeLogGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeLogGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeLogGroupsPaginatePaginationConfigTypeDef(
    _DescribeLogGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeLogGroupsPaginate` `PaginationConfig`

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


_DescribeLogGroupsPaginateResponselogGroupsTypeDef = TypedDict(
    "_DescribeLogGroupsPaginateResponselogGroupsTypeDef",
    {
        "logGroupName": str,
        "creationTime": int,
        "retentionInDays": int,
        "metricFilterCount": int,
        "arn": str,
        "storedBytes": int,
        "kmsKeyId": str,
    },
    total=False,
)


class DescribeLogGroupsPaginateResponselogGroupsTypeDef(
    _DescribeLogGroupsPaginateResponselogGroupsTypeDef
):
    """
    Type definition for `DescribeLogGroupsPaginateResponse` `logGroups`

    Represents a log group.

    - **logGroupName** *(string) --*

      The name of the log group.

    - **creationTime** *(integer) --*

      The creation time of the log group, expressed as the number of milliseconds after Jan 1,
      1970 00:00:00 UTC.

    - **retentionInDays** *(integer) --*

      The number of days to retain the log events in the specified log group. Possible values
      are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, and 3653.

    - **metricFilterCount** *(integer) --*

      The number of metric filters.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the log group.

    - **storedBytes** *(integer) --*

      The number of bytes stored.

    - **kmsKeyId** *(string) --*

      The Amazon Resource Name (ARN) of the CMK to use when encrypting log data.
    """


_DescribeLogGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeLogGroupsPaginateResponseTypeDef",
    {
        "logGroups": List[DescribeLogGroupsPaginateResponselogGroupsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeLogGroupsPaginateResponseTypeDef(
    _DescribeLogGroupsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeLogGroupsPaginate` `Response`

    - **logGroups** *(list) --*

      The log groups.

      - *(dict) --*

        Represents a log group.

        - **logGroupName** *(string) --*

          The name of the log group.

        - **creationTime** *(integer) --*

          The creation time of the log group, expressed as the number of milliseconds after Jan 1,
          1970 00:00:00 UTC.

        - **retentionInDays** *(integer) --*

          The number of days to retain the log events in the specified log group. Possible values
          are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, and 3653.

        - **metricFilterCount** *(integer) --*

          The number of metric filters.

        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the log group.

        - **storedBytes** *(integer) --*

          The number of bytes stored.

        - **kmsKeyId** *(string) --*

          The Amazon Resource Name (ARN) of the CMK to use when encrypting log data.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeLogStreamsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeLogStreamsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeLogStreamsPaginatePaginationConfigTypeDef(
    _DescribeLogStreamsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeLogStreamsPaginate` `PaginationConfig`

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


_DescribeLogStreamsPaginateResponselogStreamsTypeDef = TypedDict(
    "_DescribeLogStreamsPaginateResponselogStreamsTypeDef",
    {
        "logStreamName": str,
        "creationTime": int,
        "firstEventTimestamp": int,
        "lastEventTimestamp": int,
        "lastIngestionTime": int,
        "uploadSequenceToken": str,
        "arn": str,
        "storedBytes": int,
    },
    total=False,
)


class DescribeLogStreamsPaginateResponselogStreamsTypeDef(
    _DescribeLogStreamsPaginateResponselogStreamsTypeDef
):
    """
    Type definition for `DescribeLogStreamsPaginateResponse` `logStreams`

    Represents a log stream, which is a sequence of log events from a single emitter of logs.

    - **logStreamName** *(string) --*

      The name of the log stream.

    - **creationTime** *(integer) --*

      The creation time of the stream, expressed as the number of milliseconds after Jan 1,
      1970 00:00:00 UTC.

    - **firstEventTimestamp** *(integer) --*

      The time of the first event, expressed as the number of milliseconds after Jan 1, 1970
      00:00:00 UTC.

    - **lastEventTimestamp** *(integer) --*

      The time of the most recent log event in the log stream in CloudWatch Logs. This number
      is expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. The
      ``lastEventTime`` value updates on an eventual consistency basis. It typically updates in
      less than an hour from ingestion, but may take longer in some rare situations.

    - **lastIngestionTime** *(integer) --*

      The ingestion time, expressed as the number of milliseconds after Jan 1, 1970 00:00:00
      UTC.

    - **uploadSequenceToken** *(string) --*

      The sequence token.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the log stream.

    - **storedBytes** *(integer) --*

      The number of bytes stored.

       **IMPORTANT:** On June 17, 2019, this parameter was deprecated for log streams, and is
       always reported as zero. This change applies only to log streams. The ``storedBytes``
       parameter for log groups is not affected.
    """


_DescribeLogStreamsPaginateResponseTypeDef = TypedDict(
    "_DescribeLogStreamsPaginateResponseTypeDef",
    {
        "logStreams": List[DescribeLogStreamsPaginateResponselogStreamsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeLogStreamsPaginateResponseTypeDef(
    _DescribeLogStreamsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeLogStreamsPaginate` `Response`

    - **logStreams** *(list) --*

      The log streams.

      - *(dict) --*

        Represents a log stream, which is a sequence of log events from a single emitter of logs.

        - **logStreamName** *(string) --*

          The name of the log stream.

        - **creationTime** *(integer) --*

          The creation time of the stream, expressed as the number of milliseconds after Jan 1,
          1970 00:00:00 UTC.

        - **firstEventTimestamp** *(integer) --*

          The time of the first event, expressed as the number of milliseconds after Jan 1, 1970
          00:00:00 UTC.

        - **lastEventTimestamp** *(integer) --*

          The time of the most recent log event in the log stream in CloudWatch Logs. This number
          is expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. The
          ``lastEventTime`` value updates on an eventual consistency basis. It typically updates in
          less than an hour from ingestion, but may take longer in some rare situations.

        - **lastIngestionTime** *(integer) --*

          The ingestion time, expressed as the number of milliseconds after Jan 1, 1970 00:00:00
          UTC.

        - **uploadSequenceToken** *(string) --*

          The sequence token.

        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the log stream.

        - **storedBytes** *(integer) --*

          The number of bytes stored.

           **IMPORTANT:** On June 17, 2019, this parameter was deprecated for log streams, and is
           always reported as zero. This change applies only to log streams. The ``storedBytes``
           parameter for log groups is not affected.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeMetricFiltersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeMetricFiltersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeMetricFiltersPaginatePaginationConfigTypeDef(
    _DescribeMetricFiltersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeMetricFiltersPaginate` `PaginationConfig`

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


_DescribeMetricFiltersPaginateResponsemetricFiltersmetricTransformationsTypeDef = TypedDict(
    "_DescribeMetricFiltersPaginateResponsemetricFiltersmetricTransformationsTypeDef",
    {
        "metricName": str,
        "metricNamespace": str,
        "metricValue": str,
        "defaultValue": float,
    },
    total=False,
)


class DescribeMetricFiltersPaginateResponsemetricFiltersmetricTransformationsTypeDef(
    _DescribeMetricFiltersPaginateResponsemetricFiltersmetricTransformationsTypeDef
):
    """
    Type definition for `DescribeMetricFiltersPaginateResponsemetricFilters` `metricTransformations`

    Indicates how to transform ingested log events to metric data in a CloudWatch metric.

    - **metricName** *(string) --*

      The name of the CloudWatch metric.

    - **metricNamespace** *(string) --*

      The namespace of the CloudWatch metric.

    - **metricValue** *(string) --*

      The value to publish to the CloudWatch metric when a filter pattern matches a log
      event.

    - **defaultValue** *(float) --*

      (Optional) The value to emit when a filter pattern does not match a log event. This
      value can be null.
    """


_DescribeMetricFiltersPaginateResponsemetricFiltersTypeDef = TypedDict(
    "_DescribeMetricFiltersPaginateResponsemetricFiltersTypeDef",
    {
        "filterName": str,
        "filterPattern": str,
        "metricTransformations": List[
            DescribeMetricFiltersPaginateResponsemetricFiltersmetricTransformationsTypeDef
        ],
        "creationTime": int,
        "logGroupName": str,
    },
    total=False,
)


class DescribeMetricFiltersPaginateResponsemetricFiltersTypeDef(
    _DescribeMetricFiltersPaginateResponsemetricFiltersTypeDef
):
    """
    Type definition for `DescribeMetricFiltersPaginateResponse` `metricFilters`

    Metric filters express how CloudWatch Logs would extract metric observations from ingested
    log events and transform them into metric data in a CloudWatch metric.

    - **filterName** *(string) --*

      The name of the metric filter.

    - **filterPattern** *(string) --*

      A symbolic description of how CloudWatch Logs should interpret the data in each log
      event. For example, a log event may contain timestamps, IP addresses, strings, and so on.
      You use the filter pattern to specify what to look for in the log event message.

    - **metricTransformations** *(list) --*

      The metric transformations.

      - *(dict) --*

        Indicates how to transform ingested log events to metric data in a CloudWatch metric.

        - **metricName** *(string) --*

          The name of the CloudWatch metric.

        - **metricNamespace** *(string) --*

          The namespace of the CloudWatch metric.

        - **metricValue** *(string) --*

          The value to publish to the CloudWatch metric when a filter pattern matches a log
          event.

        - **defaultValue** *(float) --*

          (Optional) The value to emit when a filter pattern does not match a log event. This
          value can be null.

    - **creationTime** *(integer) --*

      The creation time of the metric filter, expressed as the number of milliseconds after Jan
      1, 1970 00:00:00 UTC.

    - **logGroupName** *(string) --*

      The name of the log group.
    """


_DescribeMetricFiltersPaginateResponseTypeDef = TypedDict(
    "_DescribeMetricFiltersPaginateResponseTypeDef",
    {
        "metricFilters": List[
            DescribeMetricFiltersPaginateResponsemetricFiltersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeMetricFiltersPaginateResponseTypeDef(
    _DescribeMetricFiltersPaginateResponseTypeDef
):
    """
    Type definition for `DescribeMetricFiltersPaginate` `Response`

    - **metricFilters** *(list) --*

      The metric filters.

      - *(dict) --*

        Metric filters express how CloudWatch Logs would extract metric observations from ingested
        log events and transform them into metric data in a CloudWatch metric.

        - **filterName** *(string) --*

          The name of the metric filter.

        - **filterPattern** *(string) --*

          A symbolic description of how CloudWatch Logs should interpret the data in each log
          event. For example, a log event may contain timestamps, IP addresses, strings, and so on.
          You use the filter pattern to specify what to look for in the log event message.

        - **metricTransformations** *(list) --*

          The metric transformations.

          - *(dict) --*

            Indicates how to transform ingested log events to metric data in a CloudWatch metric.

            - **metricName** *(string) --*

              The name of the CloudWatch metric.

            - **metricNamespace** *(string) --*

              The namespace of the CloudWatch metric.

            - **metricValue** *(string) --*

              The value to publish to the CloudWatch metric when a filter pattern matches a log
              event.

            - **defaultValue** *(float) --*

              (Optional) The value to emit when a filter pattern does not match a log event. This
              value can be null.

        - **creationTime** *(integer) --*

          The creation time of the metric filter, expressed as the number of milliseconds after Jan
          1, 1970 00:00:00 UTC.

        - **logGroupName** *(string) --*

          The name of the log group.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeQueriesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeQueriesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeQueriesPaginatePaginationConfigTypeDef(
    _DescribeQueriesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeQueriesPaginate` `PaginationConfig`

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


_DescribeQueriesPaginateResponsequeriesTypeDef = TypedDict(
    "_DescribeQueriesPaginateResponsequeriesTypeDef",
    {
        "queryId": str,
        "queryString": str,
        "status": str,
        "createTime": int,
        "logGroupName": str,
    },
    total=False,
)


class DescribeQueriesPaginateResponsequeriesTypeDef(
    _DescribeQueriesPaginateResponsequeriesTypeDef
):
    """
    Type definition for `DescribeQueriesPaginateResponse` `queries`

    Information about one CloudWatch Logs Insights query that matches the request in a
    ``DescribeQueries`` operation.

    - **queryId** *(string) --*

      The unique ID number of this query.

    - **queryString** *(string) --*

      The query string used in this query.

    - **status** *(string) --*

      The status of this query. Possible values are ``Cancelled`` , ``Complete`` , ``Failed`` ,
      ``Running`` , ``Scheduled`` , and ``Unknown`` .

    - **createTime** *(integer) --*

      The date and time that this query was created.

    - **logGroupName** *(string) --*

      The name of the log group scanned by this query.
    """


_DescribeQueriesPaginateResponseTypeDef = TypedDict(
    "_DescribeQueriesPaginateResponseTypeDef",
    {"queries": List[DescribeQueriesPaginateResponsequeriesTypeDef], "NextToken": str},
    total=False,
)


class DescribeQueriesPaginateResponseTypeDef(_DescribeQueriesPaginateResponseTypeDef):
    """
    Type definition for `DescribeQueriesPaginate` `Response`

    - **queries** *(list) --*

      The list of queries that match the request.

      - *(dict) --*

        Information about one CloudWatch Logs Insights query that matches the request in a
        ``DescribeQueries`` operation.

        - **queryId** *(string) --*

          The unique ID number of this query.

        - **queryString** *(string) --*

          The query string used in this query.

        - **status** *(string) --*

          The status of this query. Possible values are ``Cancelled`` , ``Complete`` , ``Failed`` ,
          ``Running`` , ``Scheduled`` , and ``Unknown`` .

        - **createTime** *(integer) --*

          The date and time that this query was created.

        - **logGroupName** *(string) --*

          The name of the log group scanned by this query.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeResourcePoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeResourcePoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeResourcePoliciesPaginatePaginationConfigTypeDef(
    _DescribeResourcePoliciesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeResourcePoliciesPaginate` `PaginationConfig`

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


_DescribeResourcePoliciesPaginateResponseresourcePoliciesTypeDef = TypedDict(
    "_DescribeResourcePoliciesPaginateResponseresourcePoliciesTypeDef",
    {"policyName": str, "policyDocument": str, "lastUpdatedTime": int},
    total=False,
)


class DescribeResourcePoliciesPaginateResponseresourcePoliciesTypeDef(
    _DescribeResourcePoliciesPaginateResponseresourcePoliciesTypeDef
):
    """
    Type definition for `DescribeResourcePoliciesPaginateResponse` `resourcePolicies`

    A policy enabling one or more entities to put logs to a log group in this account.

    - **policyName** *(string) --*

      The name of the resource policy.

    - **policyDocument** *(string) --*

      The details of the policy.

    - **lastUpdatedTime** *(integer) --*

      Timestamp showing when this policy was last updated, expressed as the number of
      milliseconds after Jan 1, 1970 00:00:00 UTC.
    """


_DescribeResourcePoliciesPaginateResponseTypeDef = TypedDict(
    "_DescribeResourcePoliciesPaginateResponseTypeDef",
    {
        "resourcePolicies": List[
            DescribeResourcePoliciesPaginateResponseresourcePoliciesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeResourcePoliciesPaginateResponseTypeDef(
    _DescribeResourcePoliciesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeResourcePoliciesPaginate` `Response`

    - **resourcePolicies** *(list) --*

      The resource policies that exist in this account.

      - *(dict) --*

        A policy enabling one or more entities to put logs to a log group in this account.

        - **policyName** *(string) --*

          The name of the resource policy.

        - **policyDocument** *(string) --*

          The details of the policy.

        - **lastUpdatedTime** *(integer) --*

          Timestamp showing when this policy was last updated, expressed as the number of
          milliseconds after Jan 1, 1970 00:00:00 UTC.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeSubscriptionFiltersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeSubscriptionFiltersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeSubscriptionFiltersPaginatePaginationConfigTypeDef(
    _DescribeSubscriptionFiltersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeSubscriptionFiltersPaginate` `PaginationConfig`

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


_DescribeSubscriptionFiltersPaginateResponsesubscriptionFiltersTypeDef = TypedDict(
    "_DescribeSubscriptionFiltersPaginateResponsesubscriptionFiltersTypeDef",
    {
        "filterName": str,
        "logGroupName": str,
        "filterPattern": str,
        "destinationArn": str,
        "roleArn": str,
        "distribution": str,
        "creationTime": int,
    },
    total=False,
)


class DescribeSubscriptionFiltersPaginateResponsesubscriptionFiltersTypeDef(
    _DescribeSubscriptionFiltersPaginateResponsesubscriptionFiltersTypeDef
):
    """
    Type definition for `DescribeSubscriptionFiltersPaginateResponse` `subscriptionFilters`

    Represents a subscription filter.

    - **filterName** *(string) --*

      The name of the subscription filter.

    - **logGroupName** *(string) --*

      The name of the log group.

    - **filterPattern** *(string) --*

      A symbolic description of how CloudWatch Logs should interpret the data in each log
      event. For example, a log event may contain timestamps, IP addresses, strings, and so on.
      You use the filter pattern to specify what to look for in the log event message.

    - **destinationArn** *(string) --*

      The Amazon Resource Name (ARN) of the destination.

    - **roleArn** *(string) --*

    - **distribution** *(string) --*

      The method used to distribute log data to the destination, which can be either random or
      grouped by log stream.

    - **creationTime** *(integer) --*

      The creation time of the subscription filter, expressed as the number of milliseconds
      after Jan 1, 1970 00:00:00 UTC.
    """


_DescribeSubscriptionFiltersPaginateResponseTypeDef = TypedDict(
    "_DescribeSubscriptionFiltersPaginateResponseTypeDef",
    {
        "subscriptionFilters": List[
            DescribeSubscriptionFiltersPaginateResponsesubscriptionFiltersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeSubscriptionFiltersPaginateResponseTypeDef(
    _DescribeSubscriptionFiltersPaginateResponseTypeDef
):
    """
    Type definition for `DescribeSubscriptionFiltersPaginate` `Response`

    - **subscriptionFilters** *(list) --*

      The subscription filters.

      - *(dict) --*

        Represents a subscription filter.

        - **filterName** *(string) --*

          The name of the subscription filter.

        - **logGroupName** *(string) --*

          The name of the log group.

        - **filterPattern** *(string) --*

          A symbolic description of how CloudWatch Logs should interpret the data in each log
          event. For example, a log event may contain timestamps, IP addresses, strings, and so on.
          You use the filter pattern to specify what to look for in the log event message.

        - **destinationArn** *(string) --*

          The Amazon Resource Name (ARN) of the destination.

        - **roleArn** *(string) --*

        - **distribution** *(string) --*

          The method used to distribute log data to the destination, which can be either random or
          grouped by log stream.

        - **creationTime** *(integer) --*

          The creation time of the subscription filter, expressed as the number of milliseconds
          after Jan 1, 1970 00:00:00 UTC.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_FilterLogEventsPaginatePaginationConfigTypeDef = TypedDict(
    "_FilterLogEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class FilterLogEventsPaginatePaginationConfigTypeDef(
    _FilterLogEventsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `FilterLogEventsPaginate` `PaginationConfig`

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


_FilterLogEventsPaginateResponseeventsTypeDef = TypedDict(
    "_FilterLogEventsPaginateResponseeventsTypeDef",
    {
        "logStreamName": str,
        "timestamp": int,
        "message": str,
        "ingestionTime": int,
        "eventId": str,
    },
    total=False,
)


class FilterLogEventsPaginateResponseeventsTypeDef(
    _FilterLogEventsPaginateResponseeventsTypeDef
):
    """
    Type definition for `FilterLogEventsPaginateResponse` `events`

    Represents a matched event.

    - **logStreamName** *(string) --*

      The name of the log stream to which this event belongs.

    - **timestamp** *(integer) --*

      The time the event occurred, expressed as the number of milliseconds after Jan 1, 1970
      00:00:00 UTC.

    - **message** *(string) --*

      The data contained in the log event.

    - **ingestionTime** *(integer) --*

      The time the event was ingested, expressed as the number of milliseconds after Jan 1,
      1970 00:00:00 UTC.

    - **eventId** *(string) --*

      The ID of the event.
    """


_FilterLogEventsPaginateResponsesearchedLogStreamsTypeDef = TypedDict(
    "_FilterLogEventsPaginateResponsesearchedLogStreamsTypeDef",
    {"logStreamName": str, "searchedCompletely": bool},
    total=False,
)


class FilterLogEventsPaginateResponsesearchedLogStreamsTypeDef(
    _FilterLogEventsPaginateResponsesearchedLogStreamsTypeDef
):
    """
    Type definition for `FilterLogEventsPaginateResponse` `searchedLogStreams`

    Represents the search status of a log stream.

    - **logStreamName** *(string) --*

      The name of the log stream.

    - **searchedCompletely** *(boolean) --*

      Indicates whether all the events in this log stream were searched.
    """


_FilterLogEventsPaginateResponseTypeDef = TypedDict(
    "_FilterLogEventsPaginateResponseTypeDef",
    {
        "events": List[FilterLogEventsPaginateResponseeventsTypeDef],
        "searchedLogStreams": List[
            FilterLogEventsPaginateResponsesearchedLogStreamsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class FilterLogEventsPaginateResponseTypeDef(_FilterLogEventsPaginateResponseTypeDef):
    """
    Type definition for `FilterLogEventsPaginate` `Response`

    - **events** *(list) --*

      The matched events.

      - *(dict) --*

        Represents a matched event.

        - **logStreamName** *(string) --*

          The name of the log stream to which this event belongs.

        - **timestamp** *(integer) --*

          The time the event occurred, expressed as the number of milliseconds after Jan 1, 1970
          00:00:00 UTC.

        - **message** *(string) --*

          The data contained in the log event.

        - **ingestionTime** *(integer) --*

          The time the event was ingested, expressed as the number of milliseconds after Jan 1,
          1970 00:00:00 UTC.

        - **eventId** *(string) --*

          The ID of the event.

    - **searchedLogStreams** *(list) --*

      Indicates which log streams have been searched and whether each has been searched completely.

      - *(dict) --*

        Represents the search status of a log stream.

        - **logStreamName** *(string) --*

          The name of the log stream.

        - **searchedCompletely** *(boolean) --*

          Indicates whether all the events in this log stream were searched.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """
