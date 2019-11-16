"Main interface for xray type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "BatchGetTracesPaginatePaginationConfigTypeDef",
    "BatchGetTracesPaginateResponseTracesSegmentsTypeDef",
    "BatchGetTracesPaginateResponseTracesTypeDef",
    "BatchGetTracesPaginateResponseTypeDef",
    "ClientBatchGetTracesResponseTracesSegmentsTypeDef",
    "ClientBatchGetTracesResponseTracesTypeDef",
    "ClientBatchGetTracesResponseTypeDef",
    "ClientCreateGroupResponseGroupTypeDef",
    "ClientCreateGroupResponseTypeDef",
    "ClientCreateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef",
    "ClientCreateSamplingRuleResponseSamplingRuleRecordTypeDef",
    "ClientCreateSamplingRuleResponseTypeDef",
    "ClientCreateSamplingRuleSamplingRuleTypeDef",
    "ClientDeleteSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef",
    "ClientDeleteSamplingRuleResponseSamplingRuleRecordTypeDef",
    "ClientDeleteSamplingRuleResponseTypeDef",
    "ClientGetEncryptionConfigResponseEncryptionConfigTypeDef",
    "ClientGetEncryptionConfigResponseTypeDef",
    "ClientGetGroupResponseGroupTypeDef",
    "ClientGetGroupResponseTypeDef",
    "ClientGetGroupsResponseGroupsTypeDef",
    "ClientGetGroupsResponseTypeDef",
    "ClientGetSamplingRulesResponseSamplingRuleRecordsSamplingRuleTypeDef",
    "ClientGetSamplingRulesResponseSamplingRuleRecordsTypeDef",
    "ClientGetSamplingRulesResponseTypeDef",
    "ClientGetSamplingStatisticSummariesResponseSamplingStatisticSummariesTypeDef",
    "ClientGetSamplingStatisticSummariesResponseTypeDef",
    "ClientGetSamplingTargetsResponseSamplingTargetDocumentsTypeDef",
    "ClientGetSamplingTargetsResponseUnprocessedStatisticsTypeDef",
    "ClientGetSamplingTargetsResponseTypeDef",
    "ClientGetSamplingTargetsSamplingStatisticsDocumentsTypeDef",
    "ClientGetServiceGraphResponseServicesDurationHistogramTypeDef",
    "ClientGetServiceGraphResponseServicesEdgesAliasesTypeDef",
    "ClientGetServiceGraphResponseServicesEdgesResponseTimeHistogramTypeDef",
    "ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef",
    "ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef",
    "ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsTypeDef",
    "ClientGetServiceGraphResponseServicesEdgesTypeDef",
    "ClientGetServiceGraphResponseServicesResponseTimeHistogramTypeDef",
    "ClientGetServiceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef",
    "ClientGetServiceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef",
    "ClientGetServiceGraphResponseServicesSummaryStatisticsTypeDef",
    "ClientGetServiceGraphResponseServicesTypeDef",
    "ClientGetServiceGraphResponseTypeDef",
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef",
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef",
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsTypeDef",
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsResponseTimeHistogramTypeDef",
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef",
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef",
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsTypeDef",
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsTypeDef",
    "ClientGetTimeSeriesServiceStatisticsResponseTypeDef",
    "ClientGetTraceGraphResponseServicesDurationHistogramTypeDef",
    "ClientGetTraceGraphResponseServicesEdgesAliasesTypeDef",
    "ClientGetTraceGraphResponseServicesEdgesResponseTimeHistogramTypeDef",
    "ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef",
    "ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef",
    "ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsTypeDef",
    "ClientGetTraceGraphResponseServicesEdgesTypeDef",
    "ClientGetTraceGraphResponseServicesResponseTimeHistogramTypeDef",
    "ClientGetTraceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef",
    "ClientGetTraceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef",
    "ClientGetTraceGraphResponseServicesSummaryStatisticsTypeDef",
    "ClientGetTraceGraphResponseServicesTypeDef",
    "ClientGetTraceGraphResponseTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesAnnotationsAnnotationValueTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesAnnotationsServiceIdsTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesAnnotationsTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesAvailabilityZonesTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesEntryPointTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesHttpTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesInstanceIdsTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesResourceARNsTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesEntityPathTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesServiceIdsTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesUsersServiceIdsTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesUsersTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesTypeDef",
    "ClientGetTraceSummariesResponseTypeDef",
    "ClientGetTraceSummariesSamplingStrategyTypeDef",
    "ClientPutEncryptionConfigResponseEncryptionConfigTypeDef",
    "ClientPutEncryptionConfigResponseTypeDef",
    "ClientPutTelemetryRecordsTelemetryRecordsBackendConnectionErrorsTypeDef",
    "ClientPutTelemetryRecordsTelemetryRecordsTypeDef",
    "ClientPutTraceSegmentsResponseUnprocessedTraceSegmentsTypeDef",
    "ClientPutTraceSegmentsResponseTypeDef",
    "ClientUpdateGroupResponseGroupTypeDef",
    "ClientUpdateGroupResponseTypeDef",
    "ClientUpdateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef",
    "ClientUpdateSamplingRuleResponseSamplingRuleRecordTypeDef",
    "ClientUpdateSamplingRuleResponseTypeDef",
    "ClientUpdateSamplingRuleSamplingRuleUpdateTypeDef",
    "GetGroupsPaginatePaginationConfigTypeDef",
    "GetGroupsPaginateResponseGroupsTypeDef",
    "GetGroupsPaginateResponseTypeDef",
    "GetSamplingRulesPaginatePaginationConfigTypeDef",
    "GetSamplingRulesPaginateResponseSamplingRuleRecordsSamplingRuleTypeDef",
    "GetSamplingRulesPaginateResponseSamplingRuleRecordsTypeDef",
    "GetSamplingRulesPaginateResponseTypeDef",
    "GetSamplingStatisticSummariesPaginatePaginationConfigTypeDef",
    "GetSamplingStatisticSummariesPaginateResponseSamplingStatisticSummariesTypeDef",
    "GetSamplingStatisticSummariesPaginateResponseTypeDef",
    "GetServiceGraphPaginatePaginationConfigTypeDef",
    "GetServiceGraphPaginateResponseServicesDurationHistogramTypeDef",
    "GetServiceGraphPaginateResponseServicesEdgesAliasesTypeDef",
    "GetServiceGraphPaginateResponseServicesEdgesResponseTimeHistogramTypeDef",
    "GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef",
    "GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef",
    "GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsTypeDef",
    "GetServiceGraphPaginateResponseServicesEdgesTypeDef",
    "GetServiceGraphPaginateResponseServicesResponseTimeHistogramTypeDef",
    "GetServiceGraphPaginateResponseServicesSummaryStatisticsErrorStatisticsTypeDef",
    "GetServiceGraphPaginateResponseServicesSummaryStatisticsFaultStatisticsTypeDef",
    "GetServiceGraphPaginateResponseServicesSummaryStatisticsTypeDef",
    "GetServiceGraphPaginateResponseServicesTypeDef",
    "GetServiceGraphPaginateResponseTypeDef",
    "GetTimeSeriesServiceStatisticsPaginatePaginationConfigTypeDef",
    "GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef",
    "GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef",
    "GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsTypeDef",
    "GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsResponseTimeHistogramTypeDef",
    "GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef",
    "GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef",
    "GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsTypeDef",
    "GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsTypeDef",
    "GetTimeSeriesServiceStatisticsPaginateResponseTypeDef",
    "GetTraceGraphPaginatePaginationConfigTypeDef",
    "GetTraceGraphPaginateResponseServicesDurationHistogramTypeDef",
    "GetTraceGraphPaginateResponseServicesEdgesAliasesTypeDef",
    "GetTraceGraphPaginateResponseServicesEdgesResponseTimeHistogramTypeDef",
    "GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef",
    "GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef",
    "GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsTypeDef",
    "GetTraceGraphPaginateResponseServicesEdgesTypeDef",
    "GetTraceGraphPaginateResponseServicesResponseTimeHistogramTypeDef",
    "GetTraceGraphPaginateResponseServicesSummaryStatisticsErrorStatisticsTypeDef",
    "GetTraceGraphPaginateResponseServicesSummaryStatisticsFaultStatisticsTypeDef",
    "GetTraceGraphPaginateResponseServicesSummaryStatisticsTypeDef",
    "GetTraceGraphPaginateResponseServicesTypeDef",
    "GetTraceGraphPaginateResponseTypeDef",
    "GetTraceSummariesPaginatePaginationConfigTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesAnnotationsAnnotationValueTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesAnnotationsServiceIdsTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesAnnotationsTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesAvailabilityZonesTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesEntryPointTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesEntityPathTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesEntityPathTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesHttpTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesInstanceIdsTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesResourceARNsTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesServicesEntityPathTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesServicesTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesServiceIdsTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesUsersServiceIdsTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesUsersTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesTypeDef",
    "GetTraceSummariesPaginateResponseTypeDef",
    "GetTraceSummariesPaginateSamplingStrategyTypeDef",
)


_BatchGetTracesPaginatePaginationConfigTypeDef = TypedDict(
    "_BatchGetTracesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class BatchGetTracesPaginatePaginationConfigTypeDef(
    _BatchGetTracesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `BatchGetTracesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_BatchGetTracesPaginateResponseTracesSegmentsTypeDef = TypedDict(
    "_BatchGetTracesPaginateResponseTracesSegmentsTypeDef",
    {"Id": str, "Document": str},
    total=False,
)


class BatchGetTracesPaginateResponseTracesSegmentsTypeDef(
    _BatchGetTracesPaginateResponseTracesSegmentsTypeDef
):
    """
    Type definition for `BatchGetTracesPaginateResponseTraces` `Segments`

    A segment from a trace that has been ingested by the X-Ray service. The segment can be
    compiled from documents uploaded with  PutTraceSegments , or an ``inferred`` segment
    for a downstream service, generated from a subsegment sent by the service that called
    it.

    For the full segment document schema, see `AWS X-Ray Segment Documents
    <https://docs.aws.amazon.com/xray/latest/devguide/xray-api-segmentdocuments.html>`__ in
    the *AWS X-Ray Developer Guide* .

    - **Id** *(string) --*

      The segment's ID.

    - **Document** *(string) --*

      The segment document.
    """


_BatchGetTracesPaginateResponseTracesTypeDef = TypedDict(
    "_BatchGetTracesPaginateResponseTracesTypeDef",
    {
        "Id": str,
        "Duration": float,
        "Segments": List[BatchGetTracesPaginateResponseTracesSegmentsTypeDef],
    },
    total=False,
)


class BatchGetTracesPaginateResponseTracesTypeDef(
    _BatchGetTracesPaginateResponseTracesTypeDef
):
    """
    Type definition for `BatchGetTracesPaginateResponse` `Traces`

    A collection of segment documents with matching trace IDs.

    - **Id** *(string) --*

      The unique identifier for the request that generated the trace's segments and subsegments.

    - **Duration** *(float) --*

      The length of time in seconds between the start time of the root segment and the end time
      of the last segment that completed.

    - **Segments** *(list) --*

      Segment documents for the segments and subsegments that comprise the trace.

      - *(dict) --*

        A segment from a trace that has been ingested by the X-Ray service. The segment can be
        compiled from documents uploaded with  PutTraceSegments , or an ``inferred`` segment
        for a downstream service, generated from a subsegment sent by the service that called
        it.

        For the full segment document schema, see `AWS X-Ray Segment Documents
        <https://docs.aws.amazon.com/xray/latest/devguide/xray-api-segmentdocuments.html>`__ in
        the *AWS X-Ray Developer Guide* .

        - **Id** *(string) --*

          The segment's ID.

        - **Document** *(string) --*

          The segment document.
    """


_BatchGetTracesPaginateResponseTypeDef = TypedDict(
    "_BatchGetTracesPaginateResponseTypeDef",
    {
        "Traces": List[BatchGetTracesPaginateResponseTracesTypeDef],
        "UnprocessedTraceIds": List[str],
    },
    total=False,
)


class BatchGetTracesPaginateResponseTypeDef(_BatchGetTracesPaginateResponseTypeDef):
    """
    Type definition for `BatchGetTracesPaginate` `Response`

    - **Traces** *(list) --*

      Full traces for the specified requests.

      - *(dict) --*

        A collection of segment documents with matching trace IDs.

        - **Id** *(string) --*

          The unique identifier for the request that generated the trace's segments and subsegments.

        - **Duration** *(float) --*

          The length of time in seconds between the start time of the root segment and the end time
          of the last segment that completed.

        - **Segments** *(list) --*

          Segment documents for the segments and subsegments that comprise the trace.

          - *(dict) --*

            A segment from a trace that has been ingested by the X-Ray service. The segment can be
            compiled from documents uploaded with  PutTraceSegments , or an ``inferred`` segment
            for a downstream service, generated from a subsegment sent by the service that called
            it.

            For the full segment document schema, see `AWS X-Ray Segment Documents
            <https://docs.aws.amazon.com/xray/latest/devguide/xray-api-segmentdocuments.html>`__ in
            the *AWS X-Ray Developer Guide* .

            - **Id** *(string) --*

              The segment's ID.

            - **Document** *(string) --*

              The segment document.

    - **UnprocessedTraceIds** *(list) --*

      Trace IDs of requests that haven't been processed.

      - *(string) --*
    """


_ClientBatchGetTracesResponseTracesSegmentsTypeDef = TypedDict(
    "_ClientBatchGetTracesResponseTracesSegmentsTypeDef",
    {"Id": str, "Document": str},
    total=False,
)


class ClientBatchGetTracesResponseTracesSegmentsTypeDef(
    _ClientBatchGetTracesResponseTracesSegmentsTypeDef
):
    """
    Type definition for `ClientBatchGetTracesResponseTraces` `Segments`

    A segment from a trace that has been ingested by the X-Ray service. The segment can be
    compiled from documents uploaded with  PutTraceSegments , or an ``inferred`` segment
    for a downstream service, generated from a subsegment sent by the service that called
    it.

    For the full segment document schema, see `AWS X-Ray Segment Documents
    <https://docs.aws.amazon.com/xray/latest/devguide/xray-api-segmentdocuments.html>`__ in
    the *AWS X-Ray Developer Guide* .

    - **Id** *(string) --*

      The segment's ID.

    - **Document** *(string) --*

      The segment document.
    """


_ClientBatchGetTracesResponseTracesTypeDef = TypedDict(
    "_ClientBatchGetTracesResponseTracesTypeDef",
    {
        "Id": str,
        "Duration": float,
        "Segments": List[ClientBatchGetTracesResponseTracesSegmentsTypeDef],
    },
    total=False,
)


class ClientBatchGetTracesResponseTracesTypeDef(
    _ClientBatchGetTracesResponseTracesTypeDef
):
    """
    Type definition for `ClientBatchGetTracesResponse` `Traces`

    A collection of segment documents with matching trace IDs.

    - **Id** *(string) --*

      The unique identifier for the request that generated the trace's segments and subsegments.

    - **Duration** *(float) --*

      The length of time in seconds between the start time of the root segment and the end time
      of the last segment that completed.

    - **Segments** *(list) --*

      Segment documents for the segments and subsegments that comprise the trace.

      - *(dict) --*

        A segment from a trace that has been ingested by the X-Ray service. The segment can be
        compiled from documents uploaded with  PutTraceSegments , or an ``inferred`` segment
        for a downstream service, generated from a subsegment sent by the service that called
        it.

        For the full segment document schema, see `AWS X-Ray Segment Documents
        <https://docs.aws.amazon.com/xray/latest/devguide/xray-api-segmentdocuments.html>`__ in
        the *AWS X-Ray Developer Guide* .

        - **Id** *(string) --*

          The segment's ID.

        - **Document** *(string) --*

          The segment document.
    """


_ClientBatchGetTracesResponseTypeDef = TypedDict(
    "_ClientBatchGetTracesResponseTypeDef",
    {
        "Traces": List[ClientBatchGetTracesResponseTracesTypeDef],
        "UnprocessedTraceIds": List[str],
        "NextToken": str,
    },
    total=False,
)


class ClientBatchGetTracesResponseTypeDef(_ClientBatchGetTracesResponseTypeDef):
    """
    Type definition for `ClientBatchGetTraces` `Response`

    - **Traces** *(list) --*

      Full traces for the specified requests.

      - *(dict) --*

        A collection of segment documents with matching trace IDs.

        - **Id** *(string) --*

          The unique identifier for the request that generated the trace's segments and subsegments.

        - **Duration** *(float) --*

          The length of time in seconds between the start time of the root segment and the end time
          of the last segment that completed.

        - **Segments** *(list) --*

          Segment documents for the segments and subsegments that comprise the trace.

          - *(dict) --*

            A segment from a trace that has been ingested by the X-Ray service. The segment can be
            compiled from documents uploaded with  PutTraceSegments , or an ``inferred`` segment
            for a downstream service, generated from a subsegment sent by the service that called
            it.

            For the full segment document schema, see `AWS X-Ray Segment Documents
            <https://docs.aws.amazon.com/xray/latest/devguide/xray-api-segmentdocuments.html>`__ in
            the *AWS X-Ray Developer Guide* .

            - **Id** *(string) --*

              The segment's ID.

            - **Document** *(string) --*

              The segment document.

    - **UnprocessedTraceIds** *(list) --*

      Trace IDs of requests that haven't been processed.

      - *(string) --*

    - **NextToken** *(string) --*

      Pagination token. Not used.
    """


_ClientCreateGroupResponseGroupTypeDef = TypedDict(
    "_ClientCreateGroupResponseGroupTypeDef",
    {"GroupName": str, "GroupARN": str, "FilterExpression": str},
    total=False,
)


class ClientCreateGroupResponseGroupTypeDef(_ClientCreateGroupResponseGroupTypeDef):
    """
    Type definition for `ClientCreateGroupResponse` `Group`

    The group that was created. Contains the name of the group that was created, the ARN of the
    group that was generated based on the group name, and the filter expression that was assigned
    to the group.

    - **GroupName** *(string) --*

      The unique case-sensitive name of the group.

    - **GroupARN** *(string) --*

      The ARN of the group generated based on the GroupName.

    - **FilterExpression** *(string) --*

      The filter expression defining the parameters to include traces.
    """


_ClientCreateGroupResponseTypeDef = TypedDict(
    "_ClientCreateGroupResponseTypeDef",
    {"Group": ClientCreateGroupResponseGroupTypeDef},
    total=False,
)


class ClientCreateGroupResponseTypeDef(_ClientCreateGroupResponseTypeDef):
    """
    Type definition for `ClientCreateGroup` `Response`

    - **Group** *(dict) --*

      The group that was created. Contains the name of the group that was created, the ARN of the
      group that was generated based on the group name, and the filter expression that was assigned
      to the group.

      - **GroupName** *(string) --*

        The unique case-sensitive name of the group.

      - **GroupARN** *(string) --*

        The ARN of the group generated based on the GroupName.

      - **FilterExpression** *(string) --*

        The filter expression defining the parameters to include traces.
    """


_ClientCreateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef = TypedDict(
    "_ClientCreateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef",
    {
        "RuleName": str,
        "RuleARN": str,
        "ResourceARN": str,
        "Priority": int,
        "FixedRate": float,
        "ReservoirSize": int,
        "ServiceName": str,
        "ServiceType": str,
        "Host": str,
        "HTTPMethod": str,
        "URLPath": str,
        "Version": int,
        "Attributes": Dict[str, str],
    },
    total=False,
)


class ClientCreateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef(
    _ClientCreateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef
):
    """
    Type definition for `ClientCreateSamplingRuleResponseSamplingRuleRecord` `SamplingRule`

    The sampling rule.

    - **RuleName** *(string) --*

      The name of the sampling rule. Specify a rule by either name or ARN, but not both.

    - **RuleARN** *(string) --*

      The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.

    - **ResourceARN** *(string) --*

      Matches the ARN of the AWS resource on which the service runs.

    - **Priority** *(integer) --*

      The priority of the sampling rule.

    - **FixedRate** *(float) --*

      The percentage of matching requests to instrument, after the reservoir is exhausted.

    - **ReservoirSize** *(integer) --*

      A fixed number of matching requests to instrument per second, prior to applying the fixed
      rate. The reservoir is not used directly by services, but applies to all services using
      the rule collectively.

    - **ServiceName** *(string) --*

      Matches the ``name`` that the service uses to identify itself in segments.

    - **ServiceType** *(string) --*

      Matches the ``origin`` that the service uses to identify its type in segments.

    - **Host** *(string) --*

      Matches the hostname from a request URL.

    - **HTTPMethod** *(string) --*

      Matches the HTTP method of a request.

    - **URLPath** *(string) --*

      Matches the path from a request URL.

    - **Version** *(integer) --*

      The version of the sampling rule format (``1`` ).

    - **Attributes** *(dict) --*

      Matches attributes derived from the request.

      - *(string) --*

        - *(string) --*
    """


_ClientCreateSamplingRuleResponseSamplingRuleRecordTypeDef = TypedDict(
    "_ClientCreateSamplingRuleResponseSamplingRuleRecordTypeDef",
    {
        "SamplingRule": ClientCreateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
    },
    total=False,
)


class ClientCreateSamplingRuleResponseSamplingRuleRecordTypeDef(
    _ClientCreateSamplingRuleResponseSamplingRuleRecordTypeDef
):
    """
    Type definition for `ClientCreateSamplingRuleResponse` `SamplingRuleRecord`

    The saved rule definition and metadata.

    - **SamplingRule** *(dict) --*

      The sampling rule.

      - **RuleName** *(string) --*

        The name of the sampling rule. Specify a rule by either name or ARN, but not both.

      - **RuleARN** *(string) --*

        The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.

      - **ResourceARN** *(string) --*

        Matches the ARN of the AWS resource on which the service runs.

      - **Priority** *(integer) --*

        The priority of the sampling rule.

      - **FixedRate** *(float) --*

        The percentage of matching requests to instrument, after the reservoir is exhausted.

      - **ReservoirSize** *(integer) --*

        A fixed number of matching requests to instrument per second, prior to applying the fixed
        rate. The reservoir is not used directly by services, but applies to all services using
        the rule collectively.

      - **ServiceName** *(string) --*

        Matches the ``name`` that the service uses to identify itself in segments.

      - **ServiceType** *(string) --*

        Matches the ``origin`` that the service uses to identify its type in segments.

      - **Host** *(string) --*

        Matches the hostname from a request URL.

      - **HTTPMethod** *(string) --*

        Matches the HTTP method of a request.

      - **URLPath** *(string) --*

        Matches the path from a request URL.

      - **Version** *(integer) --*

        The version of the sampling rule format (``1`` ).

      - **Attributes** *(dict) --*

        Matches attributes derived from the request.

        - *(string) --*

          - *(string) --*

    - **CreatedAt** *(datetime) --*

      When the rule was created.

    - **ModifiedAt** *(datetime) --*

      When the rule was last modified.
    """


_ClientCreateSamplingRuleResponseTypeDef = TypedDict(
    "_ClientCreateSamplingRuleResponseTypeDef",
    {"SamplingRuleRecord": ClientCreateSamplingRuleResponseSamplingRuleRecordTypeDef},
    total=False,
)


class ClientCreateSamplingRuleResponseTypeDef(_ClientCreateSamplingRuleResponseTypeDef):
    """
    Type definition for `ClientCreateSamplingRule` `Response`

    - **SamplingRuleRecord** *(dict) --*

      The saved rule definition and metadata.

      - **SamplingRule** *(dict) --*

        The sampling rule.

        - **RuleName** *(string) --*

          The name of the sampling rule. Specify a rule by either name or ARN, but not both.

        - **RuleARN** *(string) --*

          The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.

        - **ResourceARN** *(string) --*

          Matches the ARN of the AWS resource on which the service runs.

        - **Priority** *(integer) --*

          The priority of the sampling rule.

        - **FixedRate** *(float) --*

          The percentage of matching requests to instrument, after the reservoir is exhausted.

        - **ReservoirSize** *(integer) --*

          A fixed number of matching requests to instrument per second, prior to applying the fixed
          rate. The reservoir is not used directly by services, but applies to all services using
          the rule collectively.

        - **ServiceName** *(string) --*

          Matches the ``name`` that the service uses to identify itself in segments.

        - **ServiceType** *(string) --*

          Matches the ``origin`` that the service uses to identify its type in segments.

        - **Host** *(string) --*

          Matches the hostname from a request URL.

        - **HTTPMethod** *(string) --*

          Matches the HTTP method of a request.

        - **URLPath** *(string) --*

          Matches the path from a request URL.

        - **Version** *(integer) --*

          The version of the sampling rule format (``1`` ).

        - **Attributes** *(dict) --*

          Matches attributes derived from the request.

          - *(string) --*

            - *(string) --*

      - **CreatedAt** *(datetime) --*

        When the rule was created.

      - **ModifiedAt** *(datetime) --*

        When the rule was last modified.
    """


_RequiredClientCreateSamplingRuleSamplingRuleTypeDef = TypedDict(
    "_RequiredClientCreateSamplingRuleSamplingRuleTypeDef",
    {
        "ResourceARN": str,
        "Priority": int,
        "FixedRate": float,
        "ReservoirSize": int,
        "ServiceName": str,
        "ServiceType": str,
        "Host": str,
        "HTTPMethod": str,
        "URLPath": str,
        "Version": int,
    },
)
_OptionalClientCreateSamplingRuleSamplingRuleTypeDef = TypedDict(
    "_OptionalClientCreateSamplingRuleSamplingRuleTypeDef",
    {"RuleName": str, "RuleARN": str, "Attributes": Dict[str, str]},
    total=False,
)


class ClientCreateSamplingRuleSamplingRuleTypeDef(
    _RequiredClientCreateSamplingRuleSamplingRuleTypeDef,
    _OptionalClientCreateSamplingRuleSamplingRuleTypeDef,
):
    """
    Type definition for `ClientCreateSamplingRule` `SamplingRule`

    The rule definition.

    - **RuleName** *(string) --*

      The name of the sampling rule. Specify a rule by either name or ARN, but not both.

    - **RuleARN** *(string) --*

      The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.

    - **ResourceARN** *(string) --* **[REQUIRED]**

      Matches the ARN of the AWS resource on which the service runs.

    - **Priority** *(integer) --* **[REQUIRED]**

      The priority of the sampling rule.

    - **FixedRate** *(float) --* **[REQUIRED]**

      The percentage of matching requests to instrument, after the reservoir is exhausted.

    - **ReservoirSize** *(integer) --* **[REQUIRED]**

      A fixed number of matching requests to instrument per second, prior to applying the fixed rate.
      The reservoir is not used directly by services, but applies to all services using the rule
      collectively.

    - **ServiceName** *(string) --* **[REQUIRED]**

      Matches the ``name`` that the service uses to identify itself in segments.

    - **ServiceType** *(string) --* **[REQUIRED]**

      Matches the ``origin`` that the service uses to identify its type in segments.

    - **Host** *(string) --* **[REQUIRED]**

      Matches the hostname from a request URL.

    - **HTTPMethod** *(string) --* **[REQUIRED]**

      Matches the HTTP method of a request.

    - **URLPath** *(string) --* **[REQUIRED]**

      Matches the path from a request URL.

    - **Version** *(integer) --* **[REQUIRED]**

      The version of the sampling rule format (``1`` ).

    - **Attributes** *(dict) --*

      Matches attributes derived from the request.

      - *(string) --*

        - *(string) --*
    """


_ClientDeleteSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef = TypedDict(
    "_ClientDeleteSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef",
    {
        "RuleName": str,
        "RuleARN": str,
        "ResourceARN": str,
        "Priority": int,
        "FixedRate": float,
        "ReservoirSize": int,
        "ServiceName": str,
        "ServiceType": str,
        "Host": str,
        "HTTPMethod": str,
        "URLPath": str,
        "Version": int,
        "Attributes": Dict[str, str],
    },
    total=False,
)


class ClientDeleteSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef(
    _ClientDeleteSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef
):
    """
    Type definition for `ClientDeleteSamplingRuleResponseSamplingRuleRecord` `SamplingRule`

    The sampling rule.

    - **RuleName** *(string) --*

      The name of the sampling rule. Specify a rule by either name or ARN, but not both.

    - **RuleARN** *(string) --*

      The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.

    - **ResourceARN** *(string) --*

      Matches the ARN of the AWS resource on which the service runs.

    - **Priority** *(integer) --*

      The priority of the sampling rule.

    - **FixedRate** *(float) --*

      The percentage of matching requests to instrument, after the reservoir is exhausted.

    - **ReservoirSize** *(integer) --*

      A fixed number of matching requests to instrument per second, prior to applying the fixed
      rate. The reservoir is not used directly by services, but applies to all services using
      the rule collectively.

    - **ServiceName** *(string) --*

      Matches the ``name`` that the service uses to identify itself in segments.

    - **ServiceType** *(string) --*

      Matches the ``origin`` that the service uses to identify its type in segments.

    - **Host** *(string) --*

      Matches the hostname from a request URL.

    - **HTTPMethod** *(string) --*

      Matches the HTTP method of a request.

    - **URLPath** *(string) --*

      Matches the path from a request URL.

    - **Version** *(integer) --*

      The version of the sampling rule format (``1`` ).

    - **Attributes** *(dict) --*

      Matches attributes derived from the request.

      - *(string) --*

        - *(string) --*
    """


_ClientDeleteSamplingRuleResponseSamplingRuleRecordTypeDef = TypedDict(
    "_ClientDeleteSamplingRuleResponseSamplingRuleRecordTypeDef",
    {
        "SamplingRule": ClientDeleteSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
    },
    total=False,
)


class ClientDeleteSamplingRuleResponseSamplingRuleRecordTypeDef(
    _ClientDeleteSamplingRuleResponseSamplingRuleRecordTypeDef
):
    """
    Type definition for `ClientDeleteSamplingRuleResponse` `SamplingRuleRecord`

    The deleted rule definition and metadata.

    - **SamplingRule** *(dict) --*

      The sampling rule.

      - **RuleName** *(string) --*

        The name of the sampling rule. Specify a rule by either name or ARN, but not both.

      - **RuleARN** *(string) --*

        The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.

      - **ResourceARN** *(string) --*

        Matches the ARN of the AWS resource on which the service runs.

      - **Priority** *(integer) --*

        The priority of the sampling rule.

      - **FixedRate** *(float) --*

        The percentage of matching requests to instrument, after the reservoir is exhausted.

      - **ReservoirSize** *(integer) --*

        A fixed number of matching requests to instrument per second, prior to applying the fixed
        rate. The reservoir is not used directly by services, but applies to all services using
        the rule collectively.

      - **ServiceName** *(string) --*

        Matches the ``name`` that the service uses to identify itself in segments.

      - **ServiceType** *(string) --*

        Matches the ``origin`` that the service uses to identify its type in segments.

      - **Host** *(string) --*

        Matches the hostname from a request URL.

      - **HTTPMethod** *(string) --*

        Matches the HTTP method of a request.

      - **URLPath** *(string) --*

        Matches the path from a request URL.

      - **Version** *(integer) --*

        The version of the sampling rule format (``1`` ).

      - **Attributes** *(dict) --*

        Matches attributes derived from the request.

        - *(string) --*

          - *(string) --*

    - **CreatedAt** *(datetime) --*

      When the rule was created.

    - **ModifiedAt** *(datetime) --*

      When the rule was last modified.
    """


_ClientDeleteSamplingRuleResponseTypeDef = TypedDict(
    "_ClientDeleteSamplingRuleResponseTypeDef",
    {"SamplingRuleRecord": ClientDeleteSamplingRuleResponseSamplingRuleRecordTypeDef},
    total=False,
)


class ClientDeleteSamplingRuleResponseTypeDef(_ClientDeleteSamplingRuleResponseTypeDef):
    """
    Type definition for `ClientDeleteSamplingRule` `Response`

    - **SamplingRuleRecord** *(dict) --*

      The deleted rule definition and metadata.

      - **SamplingRule** *(dict) --*

        The sampling rule.

        - **RuleName** *(string) --*

          The name of the sampling rule. Specify a rule by either name or ARN, but not both.

        - **RuleARN** *(string) --*

          The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.

        - **ResourceARN** *(string) --*

          Matches the ARN of the AWS resource on which the service runs.

        - **Priority** *(integer) --*

          The priority of the sampling rule.

        - **FixedRate** *(float) --*

          The percentage of matching requests to instrument, after the reservoir is exhausted.

        - **ReservoirSize** *(integer) --*

          A fixed number of matching requests to instrument per second, prior to applying the fixed
          rate. The reservoir is not used directly by services, but applies to all services using
          the rule collectively.

        - **ServiceName** *(string) --*

          Matches the ``name`` that the service uses to identify itself in segments.

        - **ServiceType** *(string) --*

          Matches the ``origin`` that the service uses to identify its type in segments.

        - **Host** *(string) --*

          Matches the hostname from a request URL.

        - **HTTPMethod** *(string) --*

          Matches the HTTP method of a request.

        - **URLPath** *(string) --*

          Matches the path from a request URL.

        - **Version** *(integer) --*

          The version of the sampling rule format (``1`` ).

        - **Attributes** *(dict) --*

          Matches attributes derived from the request.

          - *(string) --*

            - *(string) --*

      - **CreatedAt** *(datetime) --*

        When the rule was created.

      - **ModifiedAt** *(datetime) --*

        When the rule was last modified.
    """


_ClientGetEncryptionConfigResponseEncryptionConfigTypeDef = TypedDict(
    "_ClientGetEncryptionConfigResponseEncryptionConfigTypeDef",
    {"KeyId": str, "Status": str, "Type": str},
    total=False,
)


class ClientGetEncryptionConfigResponseEncryptionConfigTypeDef(
    _ClientGetEncryptionConfigResponseEncryptionConfigTypeDef
):
    """
    Type definition for `ClientGetEncryptionConfigResponse` `EncryptionConfig`

    The encryption configuration document.

    - **KeyId** *(string) --*

      The ID of the customer master key (CMK) used for encryption, if applicable.

    - **Status** *(string) --*

      The encryption status. While the status is ``UPDATING`` , X-Ray may encrypt data with a
      combination of the new and old settings.

    - **Type** *(string) --*

      The type of encryption. Set to ``KMS`` for encryption with CMKs. Set to ``NONE`` for
      default encryption.
    """


_ClientGetEncryptionConfigResponseTypeDef = TypedDict(
    "_ClientGetEncryptionConfigResponseTypeDef",
    {"EncryptionConfig": ClientGetEncryptionConfigResponseEncryptionConfigTypeDef},
    total=False,
)


class ClientGetEncryptionConfigResponseTypeDef(
    _ClientGetEncryptionConfigResponseTypeDef
):
    """
    Type definition for `ClientGetEncryptionConfig` `Response`

    - **EncryptionConfig** *(dict) --*

      The encryption configuration document.

      - **KeyId** *(string) --*

        The ID of the customer master key (CMK) used for encryption, if applicable.

      - **Status** *(string) --*

        The encryption status. While the status is ``UPDATING`` , X-Ray may encrypt data with a
        combination of the new and old settings.

      - **Type** *(string) --*

        The type of encryption. Set to ``KMS`` for encryption with CMKs. Set to ``NONE`` for
        default encryption.
    """


_ClientGetGroupResponseGroupTypeDef = TypedDict(
    "_ClientGetGroupResponseGroupTypeDef",
    {"GroupName": str, "GroupARN": str, "FilterExpression": str},
    total=False,
)


class ClientGetGroupResponseGroupTypeDef(_ClientGetGroupResponseGroupTypeDef):
    """
    Type definition for `ClientGetGroupResponse` `Group`

    The group that was requested. Contains the name of the group, the ARN of the group, and the
    filter expression that assigned to the group.

    - **GroupName** *(string) --*

      The unique case-sensitive name of the group.

    - **GroupARN** *(string) --*

      The ARN of the group generated based on the GroupName.

    - **FilterExpression** *(string) --*

      The filter expression defining the parameters to include traces.
    """


_ClientGetGroupResponseTypeDef = TypedDict(
    "_ClientGetGroupResponseTypeDef",
    {"Group": ClientGetGroupResponseGroupTypeDef},
    total=False,
)


class ClientGetGroupResponseTypeDef(_ClientGetGroupResponseTypeDef):
    """
    Type definition for `ClientGetGroup` `Response`

    - **Group** *(dict) --*

      The group that was requested. Contains the name of the group, the ARN of the group, and the
      filter expression that assigned to the group.

      - **GroupName** *(string) --*

        The unique case-sensitive name of the group.

      - **GroupARN** *(string) --*

        The ARN of the group generated based on the GroupName.

      - **FilterExpression** *(string) --*

        The filter expression defining the parameters to include traces.
    """


_ClientGetGroupsResponseGroupsTypeDef = TypedDict(
    "_ClientGetGroupsResponseGroupsTypeDef",
    {"GroupName": str, "GroupARN": str, "FilterExpression": str},
    total=False,
)


class ClientGetGroupsResponseGroupsTypeDef(_ClientGetGroupsResponseGroupsTypeDef):
    """
    Type definition for `ClientGetGroupsResponse` `Groups`

    Details for a group without metadata.

    - **GroupName** *(string) --*

      The unique case-sensitive name of the group.

    - **GroupARN** *(string) --*

      The ARN of the group generated based on the GroupName.

    - **FilterExpression** *(string) --*

      The filter expression defining the parameters to include traces.
    """


_ClientGetGroupsResponseTypeDef = TypedDict(
    "_ClientGetGroupsResponseTypeDef",
    {"Groups": List[ClientGetGroupsResponseGroupsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetGroupsResponseTypeDef(_ClientGetGroupsResponseTypeDef):
    """
    Type definition for `ClientGetGroups` `Response`

    - **Groups** *(list) --*

      The collection of all active groups.

      - *(dict) --*

        Details for a group without metadata.

        - **GroupName** *(string) --*

          The unique case-sensitive name of the group.

        - **GroupARN** *(string) --*

          The ARN of the group generated based on the GroupName.

        - **FilterExpression** *(string) --*

          The filter expression defining the parameters to include traces.

    - **NextToken** *(string) --*

      Pagination token. Not used.
    """


_ClientGetSamplingRulesResponseSamplingRuleRecordsSamplingRuleTypeDef = TypedDict(
    "_ClientGetSamplingRulesResponseSamplingRuleRecordsSamplingRuleTypeDef",
    {
        "RuleName": str,
        "RuleARN": str,
        "ResourceARN": str,
        "Priority": int,
        "FixedRate": float,
        "ReservoirSize": int,
        "ServiceName": str,
        "ServiceType": str,
        "Host": str,
        "HTTPMethod": str,
        "URLPath": str,
        "Version": int,
        "Attributes": Dict[str, str],
    },
    total=False,
)


class ClientGetSamplingRulesResponseSamplingRuleRecordsSamplingRuleTypeDef(
    _ClientGetSamplingRulesResponseSamplingRuleRecordsSamplingRuleTypeDef
):
    """
    Type definition for `ClientGetSamplingRulesResponseSamplingRuleRecords` `SamplingRule`

    The sampling rule.

    - **RuleName** *(string) --*

      The name of the sampling rule. Specify a rule by either name or ARN, but not both.

    - **RuleARN** *(string) --*

      The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.

    - **ResourceARN** *(string) --*

      Matches the ARN of the AWS resource on which the service runs.

    - **Priority** *(integer) --*

      The priority of the sampling rule.

    - **FixedRate** *(float) --*

      The percentage of matching requests to instrument, after the reservoir is exhausted.

    - **ReservoirSize** *(integer) --*

      A fixed number of matching requests to instrument per second, prior to applying the
      fixed rate. The reservoir is not used directly by services, but applies to all services
      using the rule collectively.

    - **ServiceName** *(string) --*

      Matches the ``name`` that the service uses to identify itself in segments.

    - **ServiceType** *(string) --*

      Matches the ``origin`` that the service uses to identify its type in segments.

    - **Host** *(string) --*

      Matches the hostname from a request URL.

    - **HTTPMethod** *(string) --*

      Matches the HTTP method of a request.

    - **URLPath** *(string) --*

      Matches the path from a request URL.

    - **Version** *(integer) --*

      The version of the sampling rule format (``1`` ).

    - **Attributes** *(dict) --*

      Matches attributes derived from the request.

      - *(string) --*

        - *(string) --*
    """


_ClientGetSamplingRulesResponseSamplingRuleRecordsTypeDef = TypedDict(
    "_ClientGetSamplingRulesResponseSamplingRuleRecordsTypeDef",
    {
        "SamplingRule": ClientGetSamplingRulesResponseSamplingRuleRecordsSamplingRuleTypeDef,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
    },
    total=False,
)


class ClientGetSamplingRulesResponseSamplingRuleRecordsTypeDef(
    _ClientGetSamplingRulesResponseSamplingRuleRecordsTypeDef
):
    """
    Type definition for `ClientGetSamplingRulesResponse` `SamplingRuleRecords`

    A  SamplingRule and its metadata.

    - **SamplingRule** *(dict) --*

      The sampling rule.

      - **RuleName** *(string) --*

        The name of the sampling rule. Specify a rule by either name or ARN, but not both.

      - **RuleARN** *(string) --*

        The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.

      - **ResourceARN** *(string) --*

        Matches the ARN of the AWS resource on which the service runs.

      - **Priority** *(integer) --*

        The priority of the sampling rule.

      - **FixedRate** *(float) --*

        The percentage of matching requests to instrument, after the reservoir is exhausted.

      - **ReservoirSize** *(integer) --*

        A fixed number of matching requests to instrument per second, prior to applying the
        fixed rate. The reservoir is not used directly by services, but applies to all services
        using the rule collectively.

      - **ServiceName** *(string) --*

        Matches the ``name`` that the service uses to identify itself in segments.

      - **ServiceType** *(string) --*

        Matches the ``origin`` that the service uses to identify its type in segments.

      - **Host** *(string) --*

        Matches the hostname from a request URL.

      - **HTTPMethod** *(string) --*

        Matches the HTTP method of a request.

      - **URLPath** *(string) --*

        Matches the path from a request URL.

      - **Version** *(integer) --*

        The version of the sampling rule format (``1`` ).

      - **Attributes** *(dict) --*

        Matches attributes derived from the request.

        - *(string) --*

          - *(string) --*

    - **CreatedAt** *(datetime) --*

      When the rule was created.

    - **ModifiedAt** *(datetime) --*

      When the rule was last modified.
    """


_ClientGetSamplingRulesResponseTypeDef = TypedDict(
    "_ClientGetSamplingRulesResponseTypeDef",
    {
        "SamplingRuleRecords": List[
            ClientGetSamplingRulesResponseSamplingRuleRecordsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientGetSamplingRulesResponseTypeDef(_ClientGetSamplingRulesResponseTypeDef):
    """
    Type definition for `ClientGetSamplingRules` `Response`

    - **SamplingRuleRecords** *(list) --*

      Rule definitions and metadata.

      - *(dict) --*

        A  SamplingRule and its metadata.

        - **SamplingRule** *(dict) --*

          The sampling rule.

          - **RuleName** *(string) --*

            The name of the sampling rule. Specify a rule by either name or ARN, but not both.

          - **RuleARN** *(string) --*

            The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.

          - **ResourceARN** *(string) --*

            Matches the ARN of the AWS resource on which the service runs.

          - **Priority** *(integer) --*

            The priority of the sampling rule.

          - **FixedRate** *(float) --*

            The percentage of matching requests to instrument, after the reservoir is exhausted.

          - **ReservoirSize** *(integer) --*

            A fixed number of matching requests to instrument per second, prior to applying the
            fixed rate. The reservoir is not used directly by services, but applies to all services
            using the rule collectively.

          - **ServiceName** *(string) --*

            Matches the ``name`` that the service uses to identify itself in segments.

          - **ServiceType** *(string) --*

            Matches the ``origin`` that the service uses to identify its type in segments.

          - **Host** *(string) --*

            Matches the hostname from a request URL.

          - **HTTPMethod** *(string) --*

            Matches the HTTP method of a request.

          - **URLPath** *(string) --*

            Matches the path from a request URL.

          - **Version** *(integer) --*

            The version of the sampling rule format (``1`` ).

          - **Attributes** *(dict) --*

            Matches attributes derived from the request.

            - *(string) --*

              - *(string) --*

        - **CreatedAt** *(datetime) --*

          When the rule was created.

        - **ModifiedAt** *(datetime) --*

          When the rule was last modified.

    - **NextToken** *(string) --*

      Pagination token. Not used.
    """


_ClientGetSamplingStatisticSummariesResponseSamplingStatisticSummariesTypeDef = TypedDict(
    "_ClientGetSamplingStatisticSummariesResponseSamplingStatisticSummariesTypeDef",
    {
        "RuleName": str,
        "Timestamp": datetime,
        "RequestCount": int,
        "BorrowCount": int,
        "SampledCount": int,
    },
    total=False,
)


class ClientGetSamplingStatisticSummariesResponseSamplingStatisticSummariesTypeDef(
    _ClientGetSamplingStatisticSummariesResponseSamplingStatisticSummariesTypeDef
):
    """
    Type definition for `ClientGetSamplingStatisticSummariesResponse` `SamplingStatisticSummaries`

    Aggregated request sampling data for a sampling rule across all services for a 10 second
    window.

    - **RuleName** *(string) --*

      The name of the sampling rule.

    - **Timestamp** *(datetime) --*

      The start time of the reporting window.

    - **RequestCount** *(integer) --*

      The number of requests that matched the rule.

    - **BorrowCount** *(integer) --*

      The number of requests recorded with borrowed reservoir quota.

    - **SampledCount** *(integer) --*

      The number of requests recorded.
    """


_ClientGetSamplingStatisticSummariesResponseTypeDef = TypedDict(
    "_ClientGetSamplingStatisticSummariesResponseTypeDef",
    {
        "SamplingStatisticSummaries": List[
            ClientGetSamplingStatisticSummariesResponseSamplingStatisticSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientGetSamplingStatisticSummariesResponseTypeDef(
    _ClientGetSamplingStatisticSummariesResponseTypeDef
):
    """
    Type definition for `ClientGetSamplingStatisticSummaries` `Response`

    - **SamplingStatisticSummaries** *(list) --*

      Information about the number of requests instrumented for each sampling rule.

      - *(dict) --*

        Aggregated request sampling data for a sampling rule across all services for a 10 second
        window.

        - **RuleName** *(string) --*

          The name of the sampling rule.

        - **Timestamp** *(datetime) --*

          The start time of the reporting window.

        - **RequestCount** *(integer) --*

          The number of requests that matched the rule.

        - **BorrowCount** *(integer) --*

          The number of requests recorded with borrowed reservoir quota.

        - **SampledCount** *(integer) --*

          The number of requests recorded.

    - **NextToken** *(string) --*

      Pagination token. Not used.
    """


_ClientGetSamplingTargetsResponseSamplingTargetDocumentsTypeDef = TypedDict(
    "_ClientGetSamplingTargetsResponseSamplingTargetDocumentsTypeDef",
    {
        "RuleName": str,
        "FixedRate": float,
        "ReservoirQuota": int,
        "ReservoirQuotaTTL": datetime,
        "Interval": int,
    },
    total=False,
)


class ClientGetSamplingTargetsResponseSamplingTargetDocumentsTypeDef(
    _ClientGetSamplingTargetsResponseSamplingTargetDocumentsTypeDef
):
    """
    Type definition for `ClientGetSamplingTargetsResponse` `SamplingTargetDocuments`

    Temporary changes to a sampling rule configuration. To meet the global sampling target for
    a rule, X-Ray calculates a new reservoir for each service based on the recent sampling
    results of all services that called  GetSamplingTargets .

    - **RuleName** *(string) --*

      The name of the sampling rule.

    - **FixedRate** *(float) --*

      The percentage of matching requests to instrument, after the reservoir is exhausted.

    - **ReservoirQuota** *(integer) --*

      The number of requests per second that X-Ray allocated this service.

    - **ReservoirQuotaTTL** *(datetime) --*

      When the reservoir quota expires.

    - **Interval** *(integer) --*

      The number of seconds for the service to wait before getting sampling targets again.
    """


_ClientGetSamplingTargetsResponseUnprocessedStatisticsTypeDef = TypedDict(
    "_ClientGetSamplingTargetsResponseUnprocessedStatisticsTypeDef",
    {"RuleName": str, "ErrorCode": str, "Message": str},
    total=False,
)


class ClientGetSamplingTargetsResponseUnprocessedStatisticsTypeDef(
    _ClientGetSamplingTargetsResponseUnprocessedStatisticsTypeDef
):
    """
    Type definition for `ClientGetSamplingTargetsResponse` `UnprocessedStatistics`

    Sampling statistics from a call to  GetSamplingTargets that X-Ray could not process.

    - **RuleName** *(string) --*

      The name of the sampling rule.

    - **ErrorCode** *(string) --*

      The error code.

    - **Message** *(string) --*

      The error message.
    """


_ClientGetSamplingTargetsResponseTypeDef = TypedDict(
    "_ClientGetSamplingTargetsResponseTypeDef",
    {
        "SamplingTargetDocuments": List[
            ClientGetSamplingTargetsResponseSamplingTargetDocumentsTypeDef
        ],
        "LastRuleModification": datetime,
        "UnprocessedStatistics": List[
            ClientGetSamplingTargetsResponseUnprocessedStatisticsTypeDef
        ],
    },
    total=False,
)


class ClientGetSamplingTargetsResponseTypeDef(_ClientGetSamplingTargetsResponseTypeDef):
    """
    Type definition for `ClientGetSamplingTargets` `Response`

    - **SamplingTargetDocuments** *(list) --*

      Updated rules that the service should use to sample requests.

      - *(dict) --*

        Temporary changes to a sampling rule configuration. To meet the global sampling target for
        a rule, X-Ray calculates a new reservoir for each service based on the recent sampling
        results of all services that called  GetSamplingTargets .

        - **RuleName** *(string) --*

          The name of the sampling rule.

        - **FixedRate** *(float) --*

          The percentage of matching requests to instrument, after the reservoir is exhausted.

        - **ReservoirQuota** *(integer) --*

          The number of requests per second that X-Ray allocated this service.

        - **ReservoirQuotaTTL** *(datetime) --*

          When the reservoir quota expires.

        - **Interval** *(integer) --*

          The number of seconds for the service to wait before getting sampling targets again.

    - **LastRuleModification** *(datetime) --*

      The last time a user changed the sampling rule configuration. If the sampling rule
      configuration changed since the service last retrieved it, the service should call
      GetSamplingRules to get the latest version.

    - **UnprocessedStatistics** *(list) --*

      Information about  SamplingStatisticsDocument that X-Ray could not process.

      - *(dict) --*

        Sampling statistics from a call to  GetSamplingTargets that X-Ray could not process.

        - **RuleName** *(string) --*

          The name of the sampling rule.

        - **ErrorCode** *(string) --*

          The error code.

        - **Message** *(string) --*

          The error message.
    """


_RequiredClientGetSamplingTargetsSamplingStatisticsDocumentsTypeDef = TypedDict(
    "_RequiredClientGetSamplingTargetsSamplingStatisticsDocumentsTypeDef",
    {
        "RuleName": str,
        "ClientID": str,
        "Timestamp": datetime,
        "RequestCount": int,
        "SampledCount": int,
    },
)
_OptionalClientGetSamplingTargetsSamplingStatisticsDocumentsTypeDef = TypedDict(
    "_OptionalClientGetSamplingTargetsSamplingStatisticsDocumentsTypeDef",
    {"BorrowCount": int},
    total=False,
)


class ClientGetSamplingTargetsSamplingStatisticsDocumentsTypeDef(
    _RequiredClientGetSamplingTargetsSamplingStatisticsDocumentsTypeDef,
    _OptionalClientGetSamplingTargetsSamplingStatisticsDocumentsTypeDef,
):
    """
    Type definition for `ClientGetSamplingTargets` `SamplingStatisticsDocuments`

    Request sampling results for a single rule from a service. Results are for the last 10 seconds
    unless the service has been assigned a longer reporting interval after a previous call to
    GetSamplingTargets .

    - **RuleName** *(string) --* **[REQUIRED]**

      The name of the sampling rule.

    - **ClientID** *(string) --* **[REQUIRED]**

      A unique identifier for the service in hexadecimal.

    - **Timestamp** *(datetime) --* **[REQUIRED]**

      The current time.

    - **RequestCount** *(integer) --* **[REQUIRED]**

      The number of requests that matched the rule.

    - **SampledCount** *(integer) --* **[REQUIRED]**

      The number of requests recorded.

    - **BorrowCount** *(integer) --*

      The number of requests recorded with borrowed reservoir quota.
    """


_ClientGetServiceGraphResponseServicesDurationHistogramTypeDef = TypedDict(
    "_ClientGetServiceGraphResponseServicesDurationHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)


class ClientGetServiceGraphResponseServicesDurationHistogramTypeDef(
    _ClientGetServiceGraphResponseServicesDurationHistogramTypeDef
):
    """
    Type definition for `ClientGetServiceGraphResponseServices` `DurationHistogram`

    An entry in a histogram for a statistic. A histogram maps the range of observed values
    on the X axis, and the prevalence of each value on the Y axis.

    - **Value** *(float) --*

      The value of the entry.

    - **Count** *(integer) --*

      The prevalence of the entry.
    """


_ClientGetServiceGraphResponseServicesEdgesAliasesTypeDef = TypedDict(
    "_ClientGetServiceGraphResponseServicesEdgesAliasesTypeDef",
    {"Name": str, "Names": List[str], "Type": str},
    total=False,
)


class ClientGetServiceGraphResponseServicesEdgesAliasesTypeDef(
    _ClientGetServiceGraphResponseServicesEdgesAliasesTypeDef
):
    """
    Type definition for `ClientGetServiceGraphResponseServicesEdges` `Aliases`

    An alias for an edge.

    - **Name** *(string) --*

      The canonical name of the alias.

    - **Names** *(list) --*

      A list of names for the alias, including the canonical name.

      - *(string) --*

    - **Type** *(string) --*

      The type of the alias.
    """


_ClientGetServiceGraphResponseServicesEdgesResponseTimeHistogramTypeDef = TypedDict(
    "_ClientGetServiceGraphResponseServicesEdgesResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)


class ClientGetServiceGraphResponseServicesEdgesResponseTimeHistogramTypeDef(
    _ClientGetServiceGraphResponseServicesEdgesResponseTimeHistogramTypeDef
):
    """
    Type definition for `ClientGetServiceGraphResponseServicesEdges` `ResponseTimeHistogram`

    An entry in a histogram for a statistic. A histogram maps the range of observed
    values on the X axis, and the prevalence of each value on the Y axis.

    - **Value** *(float) --*

      The value of the entry.

    - **Count** *(integer) --*

      The prevalence of the entry.
    """


_ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "_ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)


class ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef(
    _ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef
):
    """
    Type definition for `ClientGetServiceGraphResponseServicesEdgesSummaryStatistics` `ErrorStatistics`

    Information about requests that failed with a 4xx Client Error status code.

    - **ThrottleCount** *(integer) --*

      The number of requests that failed with a 419 throttling status code.

    - **OtherCount** *(integer) --*

      The number of requests that failed with untracked 4xx Client Error status codes.

    - **TotalCount** *(integer) --*

      The total number of requests that failed with a 4xx Client Error status code.
    """


_ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "_ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)


class ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef(
    _ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef
):
    """
    Type definition for `ClientGetServiceGraphResponseServicesEdgesSummaryStatistics` `FaultStatistics`

    Information about requests that failed with a 5xx Server Error status code.

    - **OtherCount** *(integer) --*

      The number of requests that failed with untracked 5xx Server Error status codes.

    - **TotalCount** *(integer) --*

      The total number of requests that failed with a 5xx Server Error status code.
    """


_ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsTypeDef = TypedDict(
    "_ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)


class ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsTypeDef(
    _ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsTypeDef
):
    """
    Type definition for `ClientGetServiceGraphResponseServicesEdges` `SummaryStatistics`

    Response statistics for segments on the edge.

    - **OkCount** *(integer) --*

      The number of requests that completed with a 2xx Success status code.

    - **ErrorStatistics** *(dict) --*

      Information about requests that failed with a 4xx Client Error status code.

      - **ThrottleCount** *(integer) --*

        The number of requests that failed with a 419 throttling status code.

      - **OtherCount** *(integer) --*

        The number of requests that failed with untracked 4xx Client Error status codes.

      - **TotalCount** *(integer) --*

        The total number of requests that failed with a 4xx Client Error status code.

    - **FaultStatistics** *(dict) --*

      Information about requests that failed with a 5xx Server Error status code.

      - **OtherCount** *(integer) --*

        The number of requests that failed with untracked 5xx Server Error status codes.

      - **TotalCount** *(integer) --*

        The total number of requests that failed with a 5xx Server Error status code.

    - **TotalCount** *(integer) --*

      The total number of completed requests.

    - **TotalResponseTime** *(float) --*

      The aggregate response time of completed requests.
    """


_ClientGetServiceGraphResponseServicesEdgesTypeDef = TypedDict(
    "_ClientGetServiceGraphResponseServicesEdgesTypeDef",
    {
        "ReferenceId": int,
        "StartTime": datetime,
        "EndTime": datetime,
        "SummaryStatistics": ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsTypeDef,
        "ResponseTimeHistogram": List[
            ClientGetServiceGraphResponseServicesEdgesResponseTimeHistogramTypeDef
        ],
        "Aliases": List[ClientGetServiceGraphResponseServicesEdgesAliasesTypeDef],
    },
    total=False,
)


class ClientGetServiceGraphResponseServicesEdgesTypeDef(
    _ClientGetServiceGraphResponseServicesEdgesTypeDef
):
    """
    Type definition for `ClientGetServiceGraphResponseServices` `Edges`

    Information about a connection between two services.

    - **ReferenceId** *(integer) --*

      Identifier of the edge. Unique within a service map.

    - **StartTime** *(datetime) --*

      The start time of the first segment on the edge.

    - **EndTime** *(datetime) --*

      The end time of the last segment on the edge.

    - **SummaryStatistics** *(dict) --*

      Response statistics for segments on the edge.

      - **OkCount** *(integer) --*

        The number of requests that completed with a 2xx Success status code.

      - **ErrorStatistics** *(dict) --*

        Information about requests that failed with a 4xx Client Error status code.

        - **ThrottleCount** *(integer) --*

          The number of requests that failed with a 419 throttling status code.

        - **OtherCount** *(integer) --*

          The number of requests that failed with untracked 4xx Client Error status codes.

        - **TotalCount** *(integer) --*

          The total number of requests that failed with a 4xx Client Error status code.

      - **FaultStatistics** *(dict) --*

        Information about requests that failed with a 5xx Server Error status code.

        - **OtherCount** *(integer) --*

          The number of requests that failed with untracked 5xx Server Error status codes.

        - **TotalCount** *(integer) --*

          The total number of requests that failed with a 5xx Server Error status code.

      - **TotalCount** *(integer) --*

        The total number of completed requests.

      - **TotalResponseTime** *(float) --*

        The aggregate response time of completed requests.

    - **ResponseTimeHistogram** *(list) --*

      A histogram that maps the spread of client response times on an edge.

      - *(dict) --*

        An entry in a histogram for a statistic. A histogram maps the range of observed
        values on the X axis, and the prevalence of each value on the Y axis.

        - **Value** *(float) --*

          The value of the entry.

        - **Count** *(integer) --*

          The prevalence of the entry.

    - **Aliases** *(list) --*

      Aliases for the edge.

      - *(dict) --*

        An alias for an edge.

        - **Name** *(string) --*

          The canonical name of the alias.

        - **Names** *(list) --*

          A list of names for the alias, including the canonical name.

          - *(string) --*

        - **Type** *(string) --*

          The type of the alias.
    """


_ClientGetServiceGraphResponseServicesResponseTimeHistogramTypeDef = TypedDict(
    "_ClientGetServiceGraphResponseServicesResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)


class ClientGetServiceGraphResponseServicesResponseTimeHistogramTypeDef(
    _ClientGetServiceGraphResponseServicesResponseTimeHistogramTypeDef
):
    """
    Type definition for `ClientGetServiceGraphResponseServices` `ResponseTimeHistogram`

    An entry in a histogram for a statistic. A histogram maps the range of observed values
    on the X axis, and the prevalence of each value on the Y axis.

    - **Value** *(float) --*

      The value of the entry.

    - **Count** *(integer) --*

      The prevalence of the entry.
    """


_ClientGetServiceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "_ClientGetServiceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)


class ClientGetServiceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef(
    _ClientGetServiceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef
):
    """
    Type definition for `ClientGetServiceGraphResponseServicesSummaryStatistics` `ErrorStatistics`

    Information about requests that failed with a 4xx Client Error status code.

    - **ThrottleCount** *(integer) --*

      The number of requests that failed with a 419 throttling status code.

    - **OtherCount** *(integer) --*

      The number of requests that failed with untracked 4xx Client Error status codes.

    - **TotalCount** *(integer) --*

      The total number of requests that failed with a 4xx Client Error status code.
    """


_ClientGetServiceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "_ClientGetServiceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)


class ClientGetServiceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef(
    _ClientGetServiceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef
):
    """
    Type definition for `ClientGetServiceGraphResponseServicesSummaryStatistics` `FaultStatistics`

    Information about requests that failed with a 5xx Server Error status code.

    - **OtherCount** *(integer) --*

      The number of requests that failed with untracked 5xx Server Error status codes.

    - **TotalCount** *(integer) --*

      The total number of requests that failed with a 5xx Server Error status code.
    """


_ClientGetServiceGraphResponseServicesSummaryStatisticsTypeDef = TypedDict(
    "_ClientGetServiceGraphResponseServicesSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": ClientGetServiceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": ClientGetServiceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)


class ClientGetServiceGraphResponseServicesSummaryStatisticsTypeDef(
    _ClientGetServiceGraphResponseServicesSummaryStatisticsTypeDef
):
    """
    Type definition for `ClientGetServiceGraphResponseServices` `SummaryStatistics`

    Aggregated statistics for the service.

    - **OkCount** *(integer) --*

      The number of requests that completed with a 2xx Success status code.

    - **ErrorStatistics** *(dict) --*

      Information about requests that failed with a 4xx Client Error status code.

      - **ThrottleCount** *(integer) --*

        The number of requests that failed with a 419 throttling status code.

      - **OtherCount** *(integer) --*

        The number of requests that failed with untracked 4xx Client Error status codes.

      - **TotalCount** *(integer) --*

        The total number of requests that failed with a 4xx Client Error status code.

    - **FaultStatistics** *(dict) --*

      Information about requests that failed with a 5xx Server Error status code.

      - **OtherCount** *(integer) --*

        The number of requests that failed with untracked 5xx Server Error status codes.

      - **TotalCount** *(integer) --*

        The total number of requests that failed with a 5xx Server Error status code.

    - **TotalCount** *(integer) --*

      The total number of completed requests.

    - **TotalResponseTime** *(float) --*

      The aggregate response time of completed requests.
    """


_ClientGetServiceGraphResponseServicesTypeDef = TypedDict(
    "_ClientGetServiceGraphResponseServicesTypeDef",
    {
        "ReferenceId": int,
        "Name": str,
        "Names": List[str],
        "Root": bool,
        "AccountId": str,
        "Type": str,
        "State": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "Edges": List[ClientGetServiceGraphResponseServicesEdgesTypeDef],
        "SummaryStatistics": ClientGetServiceGraphResponseServicesSummaryStatisticsTypeDef,
        "DurationHistogram": List[
            ClientGetServiceGraphResponseServicesDurationHistogramTypeDef
        ],
        "ResponseTimeHistogram": List[
            ClientGetServiceGraphResponseServicesResponseTimeHistogramTypeDef
        ],
    },
    total=False,
)


class ClientGetServiceGraphResponseServicesTypeDef(
    _ClientGetServiceGraphResponseServicesTypeDef
):
    """
    Type definition for `ClientGetServiceGraphResponse` `Services`

    Information about an application that processed requests, users that made requests, or
    downstream services, resources and applications that an application used.

    - **ReferenceId** *(integer) --*

      Identifier for the service. Unique within the service map.

    - **Name** *(string) --*

      The canonical name of the service.

    - **Names** *(list) --*

      A list of names for the service, including the canonical name.

      - *(string) --*

    - **Root** *(boolean) --*

      Indicates that the service was the first service to process a request.

    - **AccountId** *(string) --*

      Identifier of the AWS account in which the service runs.

    - **Type** *(string) --*

      The type of service.

      * AWS Resource - The type of an AWS resource. For example, ``AWS::EC2::Instance`` for a
      application running on Amazon EC2 or ``AWS::DynamoDB::Table`` for an Amazon DynamoDB
      table that the application used.

      * AWS Service - The type of an AWS service. For example, ``AWS::DynamoDB`` for downstream
      calls to Amazon DynamoDB that didn't target a specific table.

      * ``client`` - Represents the clients that sent requests to a root service.

      * ``remote`` - A downstream service of indeterminate type.

    - **State** *(string) --*

      The service's state.

    - **StartTime** *(datetime) --*

      The start time of the first segment that the service generated.

    - **EndTime** *(datetime) --*

      The end time of the last segment that the service generated.

    - **Edges** *(list) --*

      Connections to downstream services.

      - *(dict) --*

        Information about a connection between two services.

        - **ReferenceId** *(integer) --*

          Identifier of the edge. Unique within a service map.

        - **StartTime** *(datetime) --*

          The start time of the first segment on the edge.

        - **EndTime** *(datetime) --*

          The end time of the last segment on the edge.

        - **SummaryStatistics** *(dict) --*

          Response statistics for segments on the edge.

          - **OkCount** *(integer) --*

            The number of requests that completed with a 2xx Success status code.

          - **ErrorStatistics** *(dict) --*

            Information about requests that failed with a 4xx Client Error status code.

            - **ThrottleCount** *(integer) --*

              The number of requests that failed with a 419 throttling status code.

            - **OtherCount** *(integer) --*

              The number of requests that failed with untracked 4xx Client Error status codes.

            - **TotalCount** *(integer) --*

              The total number of requests that failed with a 4xx Client Error status code.

          - **FaultStatistics** *(dict) --*

            Information about requests that failed with a 5xx Server Error status code.

            - **OtherCount** *(integer) --*

              The number of requests that failed with untracked 5xx Server Error status codes.

            - **TotalCount** *(integer) --*

              The total number of requests that failed with a 5xx Server Error status code.

          - **TotalCount** *(integer) --*

            The total number of completed requests.

          - **TotalResponseTime** *(float) --*

            The aggregate response time of completed requests.

        - **ResponseTimeHistogram** *(list) --*

          A histogram that maps the spread of client response times on an edge.

          - *(dict) --*

            An entry in a histogram for a statistic. A histogram maps the range of observed
            values on the X axis, and the prevalence of each value on the Y axis.

            - **Value** *(float) --*

              The value of the entry.

            - **Count** *(integer) --*

              The prevalence of the entry.

        - **Aliases** *(list) --*

          Aliases for the edge.

          - *(dict) --*

            An alias for an edge.

            - **Name** *(string) --*

              The canonical name of the alias.

            - **Names** *(list) --*

              A list of names for the alias, including the canonical name.

              - *(string) --*

            - **Type** *(string) --*

              The type of the alias.

    - **SummaryStatistics** *(dict) --*

      Aggregated statistics for the service.

      - **OkCount** *(integer) --*

        The number of requests that completed with a 2xx Success status code.

      - **ErrorStatistics** *(dict) --*

        Information about requests that failed with a 4xx Client Error status code.

        - **ThrottleCount** *(integer) --*

          The number of requests that failed with a 419 throttling status code.

        - **OtherCount** *(integer) --*

          The number of requests that failed with untracked 4xx Client Error status codes.

        - **TotalCount** *(integer) --*

          The total number of requests that failed with a 4xx Client Error status code.

      - **FaultStatistics** *(dict) --*

        Information about requests that failed with a 5xx Server Error status code.

        - **OtherCount** *(integer) --*

          The number of requests that failed with untracked 5xx Server Error status codes.

        - **TotalCount** *(integer) --*

          The total number of requests that failed with a 5xx Server Error status code.

      - **TotalCount** *(integer) --*

        The total number of completed requests.

      - **TotalResponseTime** *(float) --*

        The aggregate response time of completed requests.

    - **DurationHistogram** *(list) --*

      A histogram that maps the spread of service durations.

      - *(dict) --*

        An entry in a histogram for a statistic. A histogram maps the range of observed values
        on the X axis, and the prevalence of each value on the Y axis.

        - **Value** *(float) --*

          The value of the entry.

        - **Count** *(integer) --*

          The prevalence of the entry.

    - **ResponseTimeHistogram** *(list) --*

      A histogram that maps the spread of service response times.

      - *(dict) --*

        An entry in a histogram for a statistic. A histogram maps the range of observed values
        on the X axis, and the prevalence of each value on the Y axis.

        - **Value** *(float) --*

          The value of the entry.

        - **Count** *(integer) --*

          The prevalence of the entry.
    """


_ClientGetServiceGraphResponseTypeDef = TypedDict(
    "_ClientGetServiceGraphResponseTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "Services": List[ClientGetServiceGraphResponseServicesTypeDef],
        "ContainsOldGroupVersions": bool,
        "NextToken": str,
    },
    total=False,
)


class ClientGetServiceGraphResponseTypeDef(_ClientGetServiceGraphResponseTypeDef):
    """
    Type definition for `ClientGetServiceGraph` `Response`

    - **StartTime** *(datetime) --*

      The start of the time frame for which the graph was generated.

    - **EndTime** *(datetime) --*

      The end of the time frame for which the graph was generated.

    - **Services** *(list) --*

      The services that have processed a traced request during the specified time frame.

      - *(dict) --*

        Information about an application that processed requests, users that made requests, or
        downstream services, resources and applications that an application used.

        - **ReferenceId** *(integer) --*

          Identifier for the service. Unique within the service map.

        - **Name** *(string) --*

          The canonical name of the service.

        - **Names** *(list) --*

          A list of names for the service, including the canonical name.

          - *(string) --*

        - **Root** *(boolean) --*

          Indicates that the service was the first service to process a request.

        - **AccountId** *(string) --*

          Identifier of the AWS account in which the service runs.

        - **Type** *(string) --*

          The type of service.

          * AWS Resource - The type of an AWS resource. For example, ``AWS::EC2::Instance`` for a
          application running on Amazon EC2 or ``AWS::DynamoDB::Table`` for an Amazon DynamoDB
          table that the application used.

          * AWS Service - The type of an AWS service. For example, ``AWS::DynamoDB`` for downstream
          calls to Amazon DynamoDB that didn't target a specific table.

          * ``client`` - Represents the clients that sent requests to a root service.

          * ``remote`` - A downstream service of indeterminate type.

        - **State** *(string) --*

          The service's state.

        - **StartTime** *(datetime) --*

          The start time of the first segment that the service generated.

        - **EndTime** *(datetime) --*

          The end time of the last segment that the service generated.

        - **Edges** *(list) --*

          Connections to downstream services.

          - *(dict) --*

            Information about a connection between two services.

            - **ReferenceId** *(integer) --*

              Identifier of the edge. Unique within a service map.

            - **StartTime** *(datetime) --*

              The start time of the first segment on the edge.

            - **EndTime** *(datetime) --*

              The end time of the last segment on the edge.

            - **SummaryStatistics** *(dict) --*

              Response statistics for segments on the edge.

              - **OkCount** *(integer) --*

                The number of requests that completed with a 2xx Success status code.

              - **ErrorStatistics** *(dict) --*

                Information about requests that failed with a 4xx Client Error status code.

                - **ThrottleCount** *(integer) --*

                  The number of requests that failed with a 419 throttling status code.

                - **OtherCount** *(integer) --*

                  The number of requests that failed with untracked 4xx Client Error status codes.

                - **TotalCount** *(integer) --*

                  The total number of requests that failed with a 4xx Client Error status code.

              - **FaultStatistics** *(dict) --*

                Information about requests that failed with a 5xx Server Error status code.

                - **OtherCount** *(integer) --*

                  The number of requests that failed with untracked 5xx Server Error status codes.

                - **TotalCount** *(integer) --*

                  The total number of requests that failed with a 5xx Server Error status code.

              - **TotalCount** *(integer) --*

                The total number of completed requests.

              - **TotalResponseTime** *(float) --*

                The aggregate response time of completed requests.

            - **ResponseTimeHistogram** *(list) --*

              A histogram that maps the spread of client response times on an edge.

              - *(dict) --*

                An entry in a histogram for a statistic. A histogram maps the range of observed
                values on the X axis, and the prevalence of each value on the Y axis.

                - **Value** *(float) --*

                  The value of the entry.

                - **Count** *(integer) --*

                  The prevalence of the entry.

            - **Aliases** *(list) --*

              Aliases for the edge.

              - *(dict) --*

                An alias for an edge.

                - **Name** *(string) --*

                  The canonical name of the alias.

                - **Names** *(list) --*

                  A list of names for the alias, including the canonical name.

                  - *(string) --*

                - **Type** *(string) --*

                  The type of the alias.

        - **SummaryStatistics** *(dict) --*

          Aggregated statistics for the service.

          - **OkCount** *(integer) --*

            The number of requests that completed with a 2xx Success status code.

          - **ErrorStatistics** *(dict) --*

            Information about requests that failed with a 4xx Client Error status code.

            - **ThrottleCount** *(integer) --*

              The number of requests that failed with a 419 throttling status code.

            - **OtherCount** *(integer) --*

              The number of requests that failed with untracked 4xx Client Error status codes.

            - **TotalCount** *(integer) --*

              The total number of requests that failed with a 4xx Client Error status code.

          - **FaultStatistics** *(dict) --*

            Information about requests that failed with a 5xx Server Error status code.

            - **OtherCount** *(integer) --*

              The number of requests that failed with untracked 5xx Server Error status codes.

            - **TotalCount** *(integer) --*

              The total number of requests that failed with a 5xx Server Error status code.

          - **TotalCount** *(integer) --*

            The total number of completed requests.

          - **TotalResponseTime** *(float) --*

            The aggregate response time of completed requests.

        - **DurationHistogram** *(list) --*

          A histogram that maps the spread of service durations.

          - *(dict) --*

            An entry in a histogram for a statistic. A histogram maps the range of observed values
            on the X axis, and the prevalence of each value on the Y axis.

            - **Value** *(float) --*

              The value of the entry.

            - **Count** *(integer) --*

              The prevalence of the entry.

        - **ResponseTimeHistogram** *(list) --*

          A histogram that maps the spread of service response times.

          - *(dict) --*

            An entry in a histogram for a statistic. A histogram maps the range of observed values
            on the X axis, and the prevalence of each value on the Y axis.

            - **Value** *(float) --*

              The value of the entry.

            - **Count** *(integer) --*

              The prevalence of the entry.

    - **ContainsOldGroupVersions** *(boolean) --*

      A flag indicating whether the group's filter expression has been consistent, or if the
      returned service graph may show traces from an older version of the group's filter expression.

    - **NextToken** *(string) --*

      Pagination token. Not used.
    """


_ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "_ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)


class ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef(
    _ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef
):
    """
    Type definition for `ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatistics` `ErrorStatistics`

    Information about requests that failed with a 4xx Client Error status code.

    - **ThrottleCount** *(integer) --*

      The number of requests that failed with a 419 throttling status code.

    - **OtherCount** *(integer) --*

      The number of requests that failed with untracked 4xx Client Error status codes.

    - **TotalCount** *(integer) --*

      The total number of requests that failed with a 4xx Client Error status code.
    """


_ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "_ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)


class ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef(
    _ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef
):
    """
    Type definition for `ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatistics` `FaultStatistics`

    Information about requests that failed with a 5xx Server Error status code.

    - **OtherCount** *(integer) --*

      The number of requests that failed with untracked 5xx Server Error status codes.

    - **TotalCount** *(integer) --*

      The total number of requests that failed with a 5xx Server Error status code.
    """


_ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsTypeDef = TypedDict(
    "_ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)


class ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsTypeDef(
    _ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsTypeDef
):
    """
    Type definition for `ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatistics` `EdgeSummaryStatistics`

    Response statistics for an edge.

    - **OkCount** *(integer) --*

      The number of requests that completed with a 2xx Success status code.

    - **ErrorStatistics** *(dict) --*

      Information about requests that failed with a 4xx Client Error status code.

      - **ThrottleCount** *(integer) --*

        The number of requests that failed with a 419 throttling status code.

      - **OtherCount** *(integer) --*

        The number of requests that failed with untracked 4xx Client Error status codes.

      - **TotalCount** *(integer) --*

        The total number of requests that failed with a 4xx Client Error status code.

    - **FaultStatistics** *(dict) --*

      Information about requests that failed with a 5xx Server Error status code.

      - **OtherCount** *(integer) --*

        The number of requests that failed with untracked 5xx Server Error status codes.

      - **TotalCount** *(integer) --*

        The total number of requests that failed with a 5xx Server Error status code.

    - **TotalCount** *(integer) --*

      The total number of completed requests.

    - **TotalResponseTime** *(float) --*

      The aggregate response time of completed requests.
    """


_ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsResponseTimeHistogramTypeDef = TypedDict(
    "_ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)


class ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsResponseTimeHistogramTypeDef(
    _ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsResponseTimeHistogramTypeDef
):
    """
    Type definition for `ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatistics` `ResponseTimeHistogram`

    An entry in a histogram for a statistic. A histogram maps the range of observed values
    on the X axis, and the prevalence of each value on the Y axis.

    - **Value** *(float) --*

      The value of the entry.

    - **Count** *(integer) --*

      The prevalence of the entry.
    """


_ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "_ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)


class ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef(
    _ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef
):
    """
    Type definition for `ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatistics` `ErrorStatistics`

    Information about requests that failed with a 4xx Client Error status code.

    - **ThrottleCount** *(integer) --*

      The number of requests that failed with a 419 throttling status code.

    - **OtherCount** *(integer) --*

      The number of requests that failed with untracked 4xx Client Error status codes.

    - **TotalCount** *(integer) --*

      The total number of requests that failed with a 4xx Client Error status code.
    """


_ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "_ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)


class ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef(
    _ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef
):
    """
    Type definition for `ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatistics` `FaultStatistics`

    Information about requests that failed with a 5xx Server Error status code.

    - **OtherCount** *(integer) --*

      The number of requests that failed with untracked 5xx Server Error status codes.

    - **TotalCount** *(integer) --*

      The total number of requests that failed with a 5xx Server Error status code.
    """


_ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsTypeDef = TypedDict(
    "_ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)


class ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsTypeDef(
    _ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsTypeDef
):
    """
    Type definition for `ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatistics` `ServiceSummaryStatistics`

    Response statistics for a service.

    - **OkCount** *(integer) --*

      The number of requests that completed with a 2xx Success status code.

    - **ErrorStatistics** *(dict) --*

      Information about requests that failed with a 4xx Client Error status code.

      - **ThrottleCount** *(integer) --*

        The number of requests that failed with a 419 throttling status code.

      - **OtherCount** *(integer) --*

        The number of requests that failed with untracked 4xx Client Error status codes.

      - **TotalCount** *(integer) --*

        The total number of requests that failed with a 4xx Client Error status code.

    - **FaultStatistics** *(dict) --*

      Information about requests that failed with a 5xx Server Error status code.

      - **OtherCount** *(integer) --*

        The number of requests that failed with untracked 5xx Server Error status codes.

      - **TotalCount** *(integer) --*

        The total number of requests that failed with a 5xx Server Error status code.

    - **TotalCount** *(integer) --*

      The total number of completed requests.

    - **TotalResponseTime** *(float) --*

      The aggregate response time of completed requests.
    """


_ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsTypeDef = TypedDict(
    "_ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsTypeDef",
    {
        "Timestamp": datetime,
        "EdgeSummaryStatistics": ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsTypeDef,
        "ServiceSummaryStatistics": ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsTypeDef,
        "ResponseTimeHistogram": List[
            ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsResponseTimeHistogramTypeDef
        ],
    },
    total=False,
)


class ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsTypeDef(
    _ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsTypeDef
):
    """
    Type definition for `ClientGetTimeSeriesServiceStatisticsResponse` `TimeSeriesServiceStatistics`

    A list of TimeSeriesStatistic structures.

    - **Timestamp** *(datetime) --*

      Timestamp of the window for which statistics are aggregated.

    - **EdgeSummaryStatistics** *(dict) --*

      Response statistics for an edge.

      - **OkCount** *(integer) --*

        The number of requests that completed with a 2xx Success status code.

      - **ErrorStatistics** *(dict) --*

        Information about requests that failed with a 4xx Client Error status code.

        - **ThrottleCount** *(integer) --*

          The number of requests that failed with a 419 throttling status code.

        - **OtherCount** *(integer) --*

          The number of requests that failed with untracked 4xx Client Error status codes.

        - **TotalCount** *(integer) --*

          The total number of requests that failed with a 4xx Client Error status code.

      - **FaultStatistics** *(dict) --*

        Information about requests that failed with a 5xx Server Error status code.

        - **OtherCount** *(integer) --*

          The number of requests that failed with untracked 5xx Server Error status codes.

        - **TotalCount** *(integer) --*

          The total number of requests that failed with a 5xx Server Error status code.

      - **TotalCount** *(integer) --*

        The total number of completed requests.

      - **TotalResponseTime** *(float) --*

        The aggregate response time of completed requests.

    - **ServiceSummaryStatistics** *(dict) --*

      Response statistics for a service.

      - **OkCount** *(integer) --*

        The number of requests that completed with a 2xx Success status code.

      - **ErrorStatistics** *(dict) --*

        Information about requests that failed with a 4xx Client Error status code.

        - **ThrottleCount** *(integer) --*

          The number of requests that failed with a 419 throttling status code.

        - **OtherCount** *(integer) --*

          The number of requests that failed with untracked 4xx Client Error status codes.

        - **TotalCount** *(integer) --*

          The total number of requests that failed with a 4xx Client Error status code.

      - **FaultStatistics** *(dict) --*

        Information about requests that failed with a 5xx Server Error status code.

        - **OtherCount** *(integer) --*

          The number of requests that failed with untracked 5xx Server Error status codes.

        - **TotalCount** *(integer) --*

          The total number of requests that failed with a 5xx Server Error status code.

      - **TotalCount** *(integer) --*

        The total number of completed requests.

      - **TotalResponseTime** *(float) --*

        The aggregate response time of completed requests.

    - **ResponseTimeHistogram** *(list) --*

      The response time histogram for the selected entities.

      - *(dict) --*

        An entry in a histogram for a statistic. A histogram maps the range of observed values
        on the X axis, and the prevalence of each value on the Y axis.

        - **Value** *(float) --*

          The value of the entry.

        - **Count** *(integer) --*

          The prevalence of the entry.
    """


_ClientGetTimeSeriesServiceStatisticsResponseTypeDef = TypedDict(
    "_ClientGetTimeSeriesServiceStatisticsResponseTypeDef",
    {
        "TimeSeriesServiceStatistics": List[
            ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsTypeDef
        ],
        "ContainsOldGroupVersions": bool,
        "NextToken": str,
    },
    total=False,
)


class ClientGetTimeSeriesServiceStatisticsResponseTypeDef(
    _ClientGetTimeSeriesServiceStatisticsResponseTypeDef
):
    """
    Type definition for `ClientGetTimeSeriesServiceStatistics` `Response`

    - **TimeSeriesServiceStatistics** *(list) --*

      The collection of statistics.

      - *(dict) --*

        A list of TimeSeriesStatistic structures.

        - **Timestamp** *(datetime) --*

          Timestamp of the window for which statistics are aggregated.

        - **EdgeSummaryStatistics** *(dict) --*

          Response statistics for an edge.

          - **OkCount** *(integer) --*

            The number of requests that completed with a 2xx Success status code.

          - **ErrorStatistics** *(dict) --*

            Information about requests that failed with a 4xx Client Error status code.

            - **ThrottleCount** *(integer) --*

              The number of requests that failed with a 419 throttling status code.

            - **OtherCount** *(integer) --*

              The number of requests that failed with untracked 4xx Client Error status codes.

            - **TotalCount** *(integer) --*

              The total number of requests that failed with a 4xx Client Error status code.

          - **FaultStatistics** *(dict) --*

            Information about requests that failed with a 5xx Server Error status code.

            - **OtherCount** *(integer) --*

              The number of requests that failed with untracked 5xx Server Error status codes.

            - **TotalCount** *(integer) --*

              The total number of requests that failed with a 5xx Server Error status code.

          - **TotalCount** *(integer) --*

            The total number of completed requests.

          - **TotalResponseTime** *(float) --*

            The aggregate response time of completed requests.

        - **ServiceSummaryStatistics** *(dict) --*

          Response statistics for a service.

          - **OkCount** *(integer) --*

            The number of requests that completed with a 2xx Success status code.

          - **ErrorStatistics** *(dict) --*

            Information about requests that failed with a 4xx Client Error status code.

            - **ThrottleCount** *(integer) --*

              The number of requests that failed with a 419 throttling status code.

            - **OtherCount** *(integer) --*

              The number of requests that failed with untracked 4xx Client Error status codes.

            - **TotalCount** *(integer) --*

              The total number of requests that failed with a 4xx Client Error status code.

          - **FaultStatistics** *(dict) --*

            Information about requests that failed with a 5xx Server Error status code.

            - **OtherCount** *(integer) --*

              The number of requests that failed with untracked 5xx Server Error status codes.

            - **TotalCount** *(integer) --*

              The total number of requests that failed with a 5xx Server Error status code.

          - **TotalCount** *(integer) --*

            The total number of completed requests.

          - **TotalResponseTime** *(float) --*

            The aggregate response time of completed requests.

        - **ResponseTimeHistogram** *(list) --*

          The response time histogram for the selected entities.

          - *(dict) --*

            An entry in a histogram for a statistic. A histogram maps the range of observed values
            on the X axis, and the prevalence of each value on the Y axis.

            - **Value** *(float) --*

              The value of the entry.

            - **Count** *(integer) --*

              The prevalence of the entry.

    - **ContainsOldGroupVersions** *(boolean) --*

      A flag indicating whether or not a group's filter expression has been consistent, or if a
      returned aggregation may show statistics from an older version of the group's filter
      expression.

    - **NextToken** *(string) --*

      Pagination token. Not used.
    """


_ClientGetTraceGraphResponseServicesDurationHistogramTypeDef = TypedDict(
    "_ClientGetTraceGraphResponseServicesDurationHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)


class ClientGetTraceGraphResponseServicesDurationHistogramTypeDef(
    _ClientGetTraceGraphResponseServicesDurationHistogramTypeDef
):
    """
    Type definition for `ClientGetTraceGraphResponseServices` `DurationHistogram`

    An entry in a histogram for a statistic. A histogram maps the range of observed values
    on the X axis, and the prevalence of each value on the Y axis.

    - **Value** *(float) --*

      The value of the entry.

    - **Count** *(integer) --*

      The prevalence of the entry.
    """


_ClientGetTraceGraphResponseServicesEdgesAliasesTypeDef = TypedDict(
    "_ClientGetTraceGraphResponseServicesEdgesAliasesTypeDef",
    {"Name": str, "Names": List[str], "Type": str},
    total=False,
)


class ClientGetTraceGraphResponseServicesEdgesAliasesTypeDef(
    _ClientGetTraceGraphResponseServicesEdgesAliasesTypeDef
):
    """
    Type definition for `ClientGetTraceGraphResponseServicesEdges` `Aliases`

    An alias for an edge.

    - **Name** *(string) --*

      The canonical name of the alias.

    - **Names** *(list) --*

      A list of names for the alias, including the canonical name.

      - *(string) --*

    - **Type** *(string) --*

      The type of the alias.
    """


_ClientGetTraceGraphResponseServicesEdgesResponseTimeHistogramTypeDef = TypedDict(
    "_ClientGetTraceGraphResponseServicesEdgesResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)


class ClientGetTraceGraphResponseServicesEdgesResponseTimeHistogramTypeDef(
    _ClientGetTraceGraphResponseServicesEdgesResponseTimeHistogramTypeDef
):
    """
    Type definition for `ClientGetTraceGraphResponseServicesEdges` `ResponseTimeHistogram`

    An entry in a histogram for a statistic. A histogram maps the range of observed
    values on the X axis, and the prevalence of each value on the Y axis.

    - **Value** *(float) --*

      The value of the entry.

    - **Count** *(integer) --*

      The prevalence of the entry.
    """


_ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "_ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)


class ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef(
    _ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef
):
    """
    Type definition for `ClientGetTraceGraphResponseServicesEdgesSummaryStatistics` `ErrorStatistics`

    Information about requests that failed with a 4xx Client Error status code.

    - **ThrottleCount** *(integer) --*

      The number of requests that failed with a 419 throttling status code.

    - **OtherCount** *(integer) --*

      The number of requests that failed with untracked 4xx Client Error status codes.

    - **TotalCount** *(integer) --*

      The total number of requests that failed with a 4xx Client Error status code.
    """


_ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "_ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)


class ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef(
    _ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef
):
    """
    Type definition for `ClientGetTraceGraphResponseServicesEdgesSummaryStatistics` `FaultStatistics`

    Information about requests that failed with a 5xx Server Error status code.

    - **OtherCount** *(integer) --*

      The number of requests that failed with untracked 5xx Server Error status codes.

    - **TotalCount** *(integer) --*

      The total number of requests that failed with a 5xx Server Error status code.
    """


_ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsTypeDef = TypedDict(
    "_ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)


class ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsTypeDef(
    _ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsTypeDef
):
    """
    Type definition for `ClientGetTraceGraphResponseServicesEdges` `SummaryStatistics`

    Response statistics for segments on the edge.

    - **OkCount** *(integer) --*

      The number of requests that completed with a 2xx Success status code.

    - **ErrorStatistics** *(dict) --*

      Information about requests that failed with a 4xx Client Error status code.

      - **ThrottleCount** *(integer) --*

        The number of requests that failed with a 419 throttling status code.

      - **OtherCount** *(integer) --*

        The number of requests that failed with untracked 4xx Client Error status codes.

      - **TotalCount** *(integer) --*

        The total number of requests that failed with a 4xx Client Error status code.

    - **FaultStatistics** *(dict) --*

      Information about requests that failed with a 5xx Server Error status code.

      - **OtherCount** *(integer) --*

        The number of requests that failed with untracked 5xx Server Error status codes.

      - **TotalCount** *(integer) --*

        The total number of requests that failed with a 5xx Server Error status code.

    - **TotalCount** *(integer) --*

      The total number of completed requests.

    - **TotalResponseTime** *(float) --*

      The aggregate response time of completed requests.
    """


_ClientGetTraceGraphResponseServicesEdgesTypeDef = TypedDict(
    "_ClientGetTraceGraphResponseServicesEdgesTypeDef",
    {
        "ReferenceId": int,
        "StartTime": datetime,
        "EndTime": datetime,
        "SummaryStatistics": ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsTypeDef,
        "ResponseTimeHistogram": List[
            ClientGetTraceGraphResponseServicesEdgesResponseTimeHistogramTypeDef
        ],
        "Aliases": List[ClientGetTraceGraphResponseServicesEdgesAliasesTypeDef],
    },
    total=False,
)


class ClientGetTraceGraphResponseServicesEdgesTypeDef(
    _ClientGetTraceGraphResponseServicesEdgesTypeDef
):
    """
    Type definition for `ClientGetTraceGraphResponseServices` `Edges`

    Information about a connection between two services.

    - **ReferenceId** *(integer) --*

      Identifier of the edge. Unique within a service map.

    - **StartTime** *(datetime) --*

      The start time of the first segment on the edge.

    - **EndTime** *(datetime) --*

      The end time of the last segment on the edge.

    - **SummaryStatistics** *(dict) --*

      Response statistics for segments on the edge.

      - **OkCount** *(integer) --*

        The number of requests that completed with a 2xx Success status code.

      - **ErrorStatistics** *(dict) --*

        Information about requests that failed with a 4xx Client Error status code.

        - **ThrottleCount** *(integer) --*

          The number of requests that failed with a 419 throttling status code.

        - **OtherCount** *(integer) --*

          The number of requests that failed with untracked 4xx Client Error status codes.

        - **TotalCount** *(integer) --*

          The total number of requests that failed with a 4xx Client Error status code.

      - **FaultStatistics** *(dict) --*

        Information about requests that failed with a 5xx Server Error status code.

        - **OtherCount** *(integer) --*

          The number of requests that failed with untracked 5xx Server Error status codes.

        - **TotalCount** *(integer) --*

          The total number of requests that failed with a 5xx Server Error status code.

      - **TotalCount** *(integer) --*

        The total number of completed requests.

      - **TotalResponseTime** *(float) --*

        The aggregate response time of completed requests.

    - **ResponseTimeHistogram** *(list) --*

      A histogram that maps the spread of client response times on an edge.

      - *(dict) --*

        An entry in a histogram for a statistic. A histogram maps the range of observed
        values on the X axis, and the prevalence of each value on the Y axis.

        - **Value** *(float) --*

          The value of the entry.

        - **Count** *(integer) --*

          The prevalence of the entry.

    - **Aliases** *(list) --*

      Aliases for the edge.

      - *(dict) --*

        An alias for an edge.

        - **Name** *(string) --*

          The canonical name of the alias.

        - **Names** *(list) --*

          A list of names for the alias, including the canonical name.

          - *(string) --*

        - **Type** *(string) --*

          The type of the alias.
    """


_ClientGetTraceGraphResponseServicesResponseTimeHistogramTypeDef = TypedDict(
    "_ClientGetTraceGraphResponseServicesResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)


class ClientGetTraceGraphResponseServicesResponseTimeHistogramTypeDef(
    _ClientGetTraceGraphResponseServicesResponseTimeHistogramTypeDef
):
    """
    Type definition for `ClientGetTraceGraphResponseServices` `ResponseTimeHistogram`

    An entry in a histogram for a statistic. A histogram maps the range of observed values
    on the X axis, and the prevalence of each value on the Y axis.

    - **Value** *(float) --*

      The value of the entry.

    - **Count** *(integer) --*

      The prevalence of the entry.
    """


_ClientGetTraceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "_ClientGetTraceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)


class ClientGetTraceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef(
    _ClientGetTraceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef
):
    """
    Type definition for `ClientGetTraceGraphResponseServicesSummaryStatistics` `ErrorStatistics`

    Information about requests that failed with a 4xx Client Error status code.

    - **ThrottleCount** *(integer) --*

      The number of requests that failed with a 419 throttling status code.

    - **OtherCount** *(integer) --*

      The number of requests that failed with untracked 4xx Client Error status codes.

    - **TotalCount** *(integer) --*

      The total number of requests that failed with a 4xx Client Error status code.
    """


_ClientGetTraceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "_ClientGetTraceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)


class ClientGetTraceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef(
    _ClientGetTraceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef
):
    """
    Type definition for `ClientGetTraceGraphResponseServicesSummaryStatistics` `FaultStatistics`

    Information about requests that failed with a 5xx Server Error status code.

    - **OtherCount** *(integer) --*

      The number of requests that failed with untracked 5xx Server Error status codes.

    - **TotalCount** *(integer) --*

      The total number of requests that failed with a 5xx Server Error status code.
    """


_ClientGetTraceGraphResponseServicesSummaryStatisticsTypeDef = TypedDict(
    "_ClientGetTraceGraphResponseServicesSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": ClientGetTraceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": ClientGetTraceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)


class ClientGetTraceGraphResponseServicesSummaryStatisticsTypeDef(
    _ClientGetTraceGraphResponseServicesSummaryStatisticsTypeDef
):
    """
    Type definition for `ClientGetTraceGraphResponseServices` `SummaryStatistics`

    Aggregated statistics for the service.

    - **OkCount** *(integer) --*

      The number of requests that completed with a 2xx Success status code.

    - **ErrorStatistics** *(dict) --*

      Information about requests that failed with a 4xx Client Error status code.

      - **ThrottleCount** *(integer) --*

        The number of requests that failed with a 419 throttling status code.

      - **OtherCount** *(integer) --*

        The number of requests that failed with untracked 4xx Client Error status codes.

      - **TotalCount** *(integer) --*

        The total number of requests that failed with a 4xx Client Error status code.

    - **FaultStatistics** *(dict) --*

      Information about requests that failed with a 5xx Server Error status code.

      - **OtherCount** *(integer) --*

        The number of requests that failed with untracked 5xx Server Error status codes.

      - **TotalCount** *(integer) --*

        The total number of requests that failed with a 5xx Server Error status code.

    - **TotalCount** *(integer) --*

      The total number of completed requests.

    - **TotalResponseTime** *(float) --*

      The aggregate response time of completed requests.
    """


_ClientGetTraceGraphResponseServicesTypeDef = TypedDict(
    "_ClientGetTraceGraphResponseServicesTypeDef",
    {
        "ReferenceId": int,
        "Name": str,
        "Names": List[str],
        "Root": bool,
        "AccountId": str,
        "Type": str,
        "State": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "Edges": List[ClientGetTraceGraphResponseServicesEdgesTypeDef],
        "SummaryStatistics": ClientGetTraceGraphResponseServicesSummaryStatisticsTypeDef,
        "DurationHistogram": List[
            ClientGetTraceGraphResponseServicesDurationHistogramTypeDef
        ],
        "ResponseTimeHistogram": List[
            ClientGetTraceGraphResponseServicesResponseTimeHistogramTypeDef
        ],
    },
    total=False,
)


class ClientGetTraceGraphResponseServicesTypeDef(
    _ClientGetTraceGraphResponseServicesTypeDef
):
    """
    Type definition for `ClientGetTraceGraphResponse` `Services`

    Information about an application that processed requests, users that made requests, or
    downstream services, resources and applications that an application used.

    - **ReferenceId** *(integer) --*

      Identifier for the service. Unique within the service map.

    - **Name** *(string) --*

      The canonical name of the service.

    - **Names** *(list) --*

      A list of names for the service, including the canonical name.

      - *(string) --*

    - **Root** *(boolean) --*

      Indicates that the service was the first service to process a request.

    - **AccountId** *(string) --*

      Identifier of the AWS account in which the service runs.

    - **Type** *(string) --*

      The type of service.

      * AWS Resource - The type of an AWS resource. For example, ``AWS::EC2::Instance`` for a
      application running on Amazon EC2 or ``AWS::DynamoDB::Table`` for an Amazon DynamoDB
      table that the application used.

      * AWS Service - The type of an AWS service. For example, ``AWS::DynamoDB`` for downstream
      calls to Amazon DynamoDB that didn't target a specific table.

      * ``client`` - Represents the clients that sent requests to a root service.

      * ``remote`` - A downstream service of indeterminate type.

    - **State** *(string) --*

      The service's state.

    - **StartTime** *(datetime) --*

      The start time of the first segment that the service generated.

    - **EndTime** *(datetime) --*

      The end time of the last segment that the service generated.

    - **Edges** *(list) --*

      Connections to downstream services.

      - *(dict) --*

        Information about a connection between two services.

        - **ReferenceId** *(integer) --*

          Identifier of the edge. Unique within a service map.

        - **StartTime** *(datetime) --*

          The start time of the first segment on the edge.

        - **EndTime** *(datetime) --*

          The end time of the last segment on the edge.

        - **SummaryStatistics** *(dict) --*

          Response statistics for segments on the edge.

          - **OkCount** *(integer) --*

            The number of requests that completed with a 2xx Success status code.

          - **ErrorStatistics** *(dict) --*

            Information about requests that failed with a 4xx Client Error status code.

            - **ThrottleCount** *(integer) --*

              The number of requests that failed with a 419 throttling status code.

            - **OtherCount** *(integer) --*

              The number of requests that failed with untracked 4xx Client Error status codes.

            - **TotalCount** *(integer) --*

              The total number of requests that failed with a 4xx Client Error status code.

          - **FaultStatistics** *(dict) --*

            Information about requests that failed with a 5xx Server Error status code.

            - **OtherCount** *(integer) --*

              The number of requests that failed with untracked 5xx Server Error status codes.

            - **TotalCount** *(integer) --*

              The total number of requests that failed with a 5xx Server Error status code.

          - **TotalCount** *(integer) --*

            The total number of completed requests.

          - **TotalResponseTime** *(float) --*

            The aggregate response time of completed requests.

        - **ResponseTimeHistogram** *(list) --*

          A histogram that maps the spread of client response times on an edge.

          - *(dict) --*

            An entry in a histogram for a statistic. A histogram maps the range of observed
            values on the X axis, and the prevalence of each value on the Y axis.

            - **Value** *(float) --*

              The value of the entry.

            - **Count** *(integer) --*

              The prevalence of the entry.

        - **Aliases** *(list) --*

          Aliases for the edge.

          - *(dict) --*

            An alias for an edge.

            - **Name** *(string) --*

              The canonical name of the alias.

            - **Names** *(list) --*

              A list of names for the alias, including the canonical name.

              - *(string) --*

            - **Type** *(string) --*

              The type of the alias.

    - **SummaryStatistics** *(dict) --*

      Aggregated statistics for the service.

      - **OkCount** *(integer) --*

        The number of requests that completed with a 2xx Success status code.

      - **ErrorStatistics** *(dict) --*

        Information about requests that failed with a 4xx Client Error status code.

        - **ThrottleCount** *(integer) --*

          The number of requests that failed with a 419 throttling status code.

        - **OtherCount** *(integer) --*

          The number of requests that failed with untracked 4xx Client Error status codes.

        - **TotalCount** *(integer) --*

          The total number of requests that failed with a 4xx Client Error status code.

      - **FaultStatistics** *(dict) --*

        Information about requests that failed with a 5xx Server Error status code.

        - **OtherCount** *(integer) --*

          The number of requests that failed with untracked 5xx Server Error status codes.

        - **TotalCount** *(integer) --*

          The total number of requests that failed with a 5xx Server Error status code.

      - **TotalCount** *(integer) --*

        The total number of completed requests.

      - **TotalResponseTime** *(float) --*

        The aggregate response time of completed requests.

    - **DurationHistogram** *(list) --*

      A histogram that maps the spread of service durations.

      - *(dict) --*

        An entry in a histogram for a statistic. A histogram maps the range of observed values
        on the X axis, and the prevalence of each value on the Y axis.

        - **Value** *(float) --*

          The value of the entry.

        - **Count** *(integer) --*

          The prevalence of the entry.

    - **ResponseTimeHistogram** *(list) --*

      A histogram that maps the spread of service response times.

      - *(dict) --*

        An entry in a histogram for a statistic. A histogram maps the range of observed values
        on the X axis, and the prevalence of each value on the Y axis.

        - **Value** *(float) --*

          The value of the entry.

        - **Count** *(integer) --*

          The prevalence of the entry.
    """


_ClientGetTraceGraphResponseTypeDef = TypedDict(
    "_ClientGetTraceGraphResponseTypeDef",
    {"Services": List[ClientGetTraceGraphResponseServicesTypeDef], "NextToken": str},
    total=False,
)


class ClientGetTraceGraphResponseTypeDef(_ClientGetTraceGraphResponseTypeDef):
    """
    Type definition for `ClientGetTraceGraph` `Response`

    - **Services** *(list) --*

      The services that have processed one of the specified requests.

      - *(dict) --*

        Information about an application that processed requests, users that made requests, or
        downstream services, resources and applications that an application used.

        - **ReferenceId** *(integer) --*

          Identifier for the service. Unique within the service map.

        - **Name** *(string) --*

          The canonical name of the service.

        - **Names** *(list) --*

          A list of names for the service, including the canonical name.

          - *(string) --*

        - **Root** *(boolean) --*

          Indicates that the service was the first service to process a request.

        - **AccountId** *(string) --*

          Identifier of the AWS account in which the service runs.

        - **Type** *(string) --*

          The type of service.

          * AWS Resource - The type of an AWS resource. For example, ``AWS::EC2::Instance`` for a
          application running on Amazon EC2 or ``AWS::DynamoDB::Table`` for an Amazon DynamoDB
          table that the application used.

          * AWS Service - The type of an AWS service. For example, ``AWS::DynamoDB`` for downstream
          calls to Amazon DynamoDB that didn't target a specific table.

          * ``client`` - Represents the clients that sent requests to a root service.

          * ``remote`` - A downstream service of indeterminate type.

        - **State** *(string) --*

          The service's state.

        - **StartTime** *(datetime) --*

          The start time of the first segment that the service generated.

        - **EndTime** *(datetime) --*

          The end time of the last segment that the service generated.

        - **Edges** *(list) --*

          Connections to downstream services.

          - *(dict) --*

            Information about a connection between two services.

            - **ReferenceId** *(integer) --*

              Identifier of the edge. Unique within a service map.

            - **StartTime** *(datetime) --*

              The start time of the first segment on the edge.

            - **EndTime** *(datetime) --*

              The end time of the last segment on the edge.

            - **SummaryStatistics** *(dict) --*

              Response statistics for segments on the edge.

              - **OkCount** *(integer) --*

                The number of requests that completed with a 2xx Success status code.

              - **ErrorStatistics** *(dict) --*

                Information about requests that failed with a 4xx Client Error status code.

                - **ThrottleCount** *(integer) --*

                  The number of requests that failed with a 419 throttling status code.

                - **OtherCount** *(integer) --*

                  The number of requests that failed with untracked 4xx Client Error status codes.

                - **TotalCount** *(integer) --*

                  The total number of requests that failed with a 4xx Client Error status code.

              - **FaultStatistics** *(dict) --*

                Information about requests that failed with a 5xx Server Error status code.

                - **OtherCount** *(integer) --*

                  The number of requests that failed with untracked 5xx Server Error status codes.

                - **TotalCount** *(integer) --*

                  The total number of requests that failed with a 5xx Server Error status code.

              - **TotalCount** *(integer) --*

                The total number of completed requests.

              - **TotalResponseTime** *(float) --*

                The aggregate response time of completed requests.

            - **ResponseTimeHistogram** *(list) --*

              A histogram that maps the spread of client response times on an edge.

              - *(dict) --*

                An entry in a histogram for a statistic. A histogram maps the range of observed
                values on the X axis, and the prevalence of each value on the Y axis.

                - **Value** *(float) --*

                  The value of the entry.

                - **Count** *(integer) --*

                  The prevalence of the entry.

            - **Aliases** *(list) --*

              Aliases for the edge.

              - *(dict) --*

                An alias for an edge.

                - **Name** *(string) --*

                  The canonical name of the alias.

                - **Names** *(list) --*

                  A list of names for the alias, including the canonical name.

                  - *(string) --*

                - **Type** *(string) --*

                  The type of the alias.

        - **SummaryStatistics** *(dict) --*

          Aggregated statistics for the service.

          - **OkCount** *(integer) --*

            The number of requests that completed with a 2xx Success status code.

          - **ErrorStatistics** *(dict) --*

            Information about requests that failed with a 4xx Client Error status code.

            - **ThrottleCount** *(integer) --*

              The number of requests that failed with a 419 throttling status code.

            - **OtherCount** *(integer) --*

              The number of requests that failed with untracked 4xx Client Error status codes.

            - **TotalCount** *(integer) --*

              The total number of requests that failed with a 4xx Client Error status code.

          - **FaultStatistics** *(dict) --*

            Information about requests that failed with a 5xx Server Error status code.

            - **OtherCount** *(integer) --*

              The number of requests that failed with untracked 5xx Server Error status codes.

            - **TotalCount** *(integer) --*

              The total number of requests that failed with a 5xx Server Error status code.

          - **TotalCount** *(integer) --*

            The total number of completed requests.

          - **TotalResponseTime** *(float) --*

            The aggregate response time of completed requests.

        - **DurationHistogram** *(list) --*

          A histogram that maps the spread of service durations.

          - *(dict) --*

            An entry in a histogram for a statistic. A histogram maps the range of observed values
            on the X axis, and the prevalence of each value on the Y axis.

            - **Value** *(float) --*

              The value of the entry.

            - **Count** *(integer) --*

              The prevalence of the entry.

        - **ResponseTimeHistogram** *(list) --*

          A histogram that maps the spread of service response times.

          - *(dict) --*

            An entry in a histogram for a statistic. A histogram maps the range of observed values
            on the X axis, and the prevalence of each value on the Y axis.

            - **Value** *(float) --*

              The value of the entry.

            - **Count** *(integer) --*

              The prevalence of the entry.

    - **NextToken** *(string) --*

      Pagination token. Not used.
    """


_ClientGetTraceSummariesResponseTraceSummariesAnnotationsAnnotationValueTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesAnnotationsAnnotationValueTypeDef",
    {"NumberValue": float, "BooleanValue": bool, "StringValue": str},
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesAnnotationsAnnotationValueTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesAnnotationsAnnotationValueTypeDef
):
    """
    Type definition for `ClientGetTraceSummariesResponseTraceSummariesAnnotations` `AnnotationValue`

    Values of the annotation.

    - **NumberValue** *(float) --*

      Value for a Number annotation.

    - **BooleanValue** *(boolean) --*

      Value for a Boolean annotation.

    - **StringValue** *(string) --*

      Value for a String annotation.
    """


_ClientGetTraceSummariesResponseTraceSummariesAnnotationsServiceIdsTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesAnnotationsServiceIdsTypeDef",
    {"Name": str, "Names": List[str], "AccountId": str, "Type": str},
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesAnnotationsServiceIdsTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesAnnotationsServiceIdsTypeDef
):
    """
    Type definition for `ClientGetTraceSummariesResponseTraceSummariesAnnotations` `ServiceIds`

    - **Name** *(string) --*

    - **Names** *(list) --*

      - *(string) --*

    - **AccountId** *(string) --*

    - **Type** *(string) --*
    """


_ClientGetTraceSummariesResponseTraceSummariesAnnotationsTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesAnnotationsTypeDef",
    {
        "AnnotationValue": ClientGetTraceSummariesResponseTraceSummariesAnnotationsAnnotationValueTypeDef,
        "ServiceIds": List[
            ClientGetTraceSummariesResponseTraceSummariesAnnotationsServiceIdsTypeDef
        ],
    },
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesAnnotationsTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesAnnotationsTypeDef
):
    """
    Type definition for `ClientGetTraceSummariesResponseTraceSummaries` `Annotations`

    Information about a segment annotation.

    - **AnnotationValue** *(dict) --*

      Values of the annotation.

      - **NumberValue** *(float) --*

        Value for a Number annotation.

      - **BooleanValue** *(boolean) --*

        Value for a Boolean annotation.

      - **StringValue** *(string) --*

        Value for a String annotation.

    - **ServiceIds** *(list) --*

      Services to which the annotation applies.

      - *(dict) --*

        - **Name** *(string) --*

        - **Names** *(list) --*

          - *(string) --*

        - **AccountId** *(string) --*

        - **Type** *(string) --*
    """


_ClientGetTraceSummariesResponseTraceSummariesAvailabilityZonesTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesAvailabilityZonesTypeDef",
    {"Name": str},
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesAvailabilityZonesTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesAvailabilityZonesTypeDef
):
    """
    Type definition for `ClientGetTraceSummariesResponseTraceSummaries` `AvailabilityZones`

    A list of availability zones corresponding to the segments in a trace.

    - **Name** *(string) --*

      The name of a corresponding availability zone.
    """


_ClientGetTraceSummariesResponseTraceSummariesEntryPointTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesEntryPointTypeDef",
    {"Name": str, "Names": List[str], "AccountId": str, "Type": str},
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesEntryPointTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesEntryPointTypeDef
):
    """
    Type definition for `ClientGetTraceSummariesResponseTraceSummaries` `EntryPoint`

    The root of a trace.

    - **Name** *(string) --*

    - **Names** *(list) --*

      - *(string) --*

    - **AccountId** *(string) --*

    - **Type** *(string) --*
    """


_ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef",
    {"Name": str, "Message": str},
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef
):
    """
    Type definition for `ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPath` `Exceptions`

    The exception associated with a root cause.

    - **Name** *(string) --*

      The name of the exception.

    - **Message** *(string) --*

      The message of the exception.
    """


_ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathTypeDef",
    {
        "Name": str,
        "Exceptions": List[
            ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef
        ],
        "Remote": bool,
    },
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathTypeDef
):
    """
    Type definition for `ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServices` `EntityPath`

    A collection of segments and corresponding subsegments associated to a trace
    summary error.

    - **Name** *(string) --*

      The name of the entity.

    - **Exceptions** *(list) --*

      The types and messages of the exceptions.

      - *(dict) --*

        The exception associated with a root cause.

        - **Name** *(string) --*

          The name of the exception.

        - **Message** *(string) --*

          The message of the exception.

    - **Remote** *(boolean) --*

      A flag that denotes a remote subsegment.
    """


_ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesTypeDef",
    {
        "Name": str,
        "Names": List[str],
        "Type": str,
        "AccountId": str,
        "EntityPath": List[
            ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathTypeDef
        ],
        "Inferred": bool,
    },
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesTypeDef
):
    """
    Type definition for `ClientGetTraceSummariesResponseTraceSummariesErrorRootCauses` `Services`

    A collection of fields identifying the services in a trace summary error.

    - **Name** *(string) --*

      The service name.

    - **Names** *(list) --*

      A collection of associated service names.

      - *(string) --*

    - **Type** *(string) --*

      The type associated to the service.

    - **AccountId** *(string) --*

      The account ID associated to the service.

    - **EntityPath** *(list) --*

      The path of root cause entities found on the service.

      - *(dict) --*

        A collection of segments and corresponding subsegments associated to a trace
        summary error.

        - **Name** *(string) --*

          The name of the entity.

        - **Exceptions** *(list) --*

          The types and messages of the exceptions.

          - *(dict) --*

            The exception associated with a root cause.

            - **Name** *(string) --*

              The name of the exception.

            - **Message** *(string) --*

              The message of the exception.

        - **Remote** *(boolean) --*

          A flag that denotes a remote subsegment.

    - **Inferred** *(boolean) --*

      A Boolean value indicating if the service is inferred from the trace.
    """


_ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesTypeDef",
    {
        "Services": List[
            ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesTypeDef
        ]
    },
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesTypeDef
):
    """
    Type definition for `ClientGetTraceSummariesResponseTraceSummaries` `ErrorRootCauses`

    The root cause of a trace summary error.

    - **Services** *(list) --*

      A list of services corresponding to an error. A service identifies a segment and it
      contains a name, account ID, type, and inferred flag.

      - *(dict) --*

        A collection of fields identifying the services in a trace summary error.

        - **Name** *(string) --*

          The service name.

        - **Names** *(list) --*

          A collection of associated service names.

          - *(string) --*

        - **Type** *(string) --*

          The type associated to the service.

        - **AccountId** *(string) --*

          The account ID associated to the service.

        - **EntityPath** *(list) --*

          The path of root cause entities found on the service.

          - *(dict) --*

            A collection of segments and corresponding subsegments associated to a trace
            summary error.

            - **Name** *(string) --*

              The name of the entity.

            - **Exceptions** *(list) --*

              The types and messages of the exceptions.

              - *(dict) --*

                The exception associated with a root cause.

                - **Name** *(string) --*

                  The name of the exception.

                - **Message** *(string) --*

                  The message of the exception.

            - **Remote** *(boolean) --*

              A flag that denotes a remote subsegment.

        - **Inferred** *(boolean) --*

          A Boolean value indicating if the service is inferred from the trace.
    """


_ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef",
    {"Name": str, "Message": str},
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef
):
    """
    Type definition for `ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPath` `Exceptions`

    The exception associated with a root cause.

    - **Name** *(string) --*

      The name of the exception.

    - **Message** *(string) --*

      The message of the exception.
    """


_ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathTypeDef",
    {
        "Name": str,
        "Exceptions": List[
            ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef
        ],
        "Remote": bool,
    },
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathTypeDef
):
    """
    Type definition for `ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServices` `EntityPath`

    A collection of segments and corresponding subsegments associated to a trace
    summary fault error.

    - **Name** *(string) --*

      The name of the entity.

    - **Exceptions** *(list) --*

      The types and messages of the exceptions.

      - *(dict) --*

        The exception associated with a root cause.

        - **Name** *(string) --*

          The name of the exception.

        - **Message** *(string) --*

          The message of the exception.

    - **Remote** *(boolean) --*

      A flag that denotes a remote subsegment.
    """


_ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesTypeDef",
    {
        "Name": str,
        "Names": List[str],
        "Type": str,
        "AccountId": str,
        "EntityPath": List[
            ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathTypeDef
        ],
        "Inferred": bool,
    },
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesTypeDef
):
    """
    Type definition for `ClientGetTraceSummariesResponseTraceSummariesFaultRootCauses` `Services`

    A collection of fields identifying the services in a trace summary fault.

    - **Name** *(string) --*

      The service name.

    - **Names** *(list) --*

      A collection of associated service names.

      - *(string) --*

    - **Type** *(string) --*

      The type associated to the service.

    - **AccountId** *(string) --*

      The account ID associated to the service.

    - **EntityPath** *(list) --*

      The path of root cause entities found on the service.

      - *(dict) --*

        A collection of segments and corresponding subsegments associated to a trace
        summary fault error.

        - **Name** *(string) --*

          The name of the entity.

        - **Exceptions** *(list) --*

          The types and messages of the exceptions.

          - *(dict) --*

            The exception associated with a root cause.

            - **Name** *(string) --*

              The name of the exception.

            - **Message** *(string) --*

              The message of the exception.

        - **Remote** *(boolean) --*

          A flag that denotes a remote subsegment.

    - **Inferred** *(boolean) --*

      A Boolean value indicating if the service is inferred from the trace.
    """


_ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesTypeDef",
    {
        "Services": List[
            ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesTypeDef
        ]
    },
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesTypeDef
):
    """
    Type definition for `ClientGetTraceSummariesResponseTraceSummaries` `FaultRootCauses`

    The root cause information for a trace summary fault.

    - **Services** *(list) --*

      A list of corresponding services. A service identifies a segment and it contains a
      name, account ID, type, and inferred flag.

      - *(dict) --*

        A collection of fields identifying the services in a trace summary fault.

        - **Name** *(string) --*

          The service name.

        - **Names** *(list) --*

          A collection of associated service names.

          - *(string) --*

        - **Type** *(string) --*

          The type associated to the service.

        - **AccountId** *(string) --*

          The account ID associated to the service.

        - **EntityPath** *(list) --*

          The path of root cause entities found on the service.

          - *(dict) --*

            A collection of segments and corresponding subsegments associated to a trace
            summary fault error.

            - **Name** *(string) --*

              The name of the entity.

            - **Exceptions** *(list) --*

              The types and messages of the exceptions.

              - *(dict) --*

                The exception associated with a root cause.

                - **Name** *(string) --*

                  The name of the exception.

                - **Message** *(string) --*

                  The message of the exception.

            - **Remote** *(boolean) --*

              A flag that denotes a remote subsegment.

        - **Inferred** *(boolean) --*

          A Boolean value indicating if the service is inferred from the trace.
    """


_ClientGetTraceSummariesResponseTraceSummariesHttpTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesHttpTypeDef",
    {
        "HttpURL": str,
        "HttpStatus": int,
        "HttpMethod": str,
        "UserAgent": str,
        "ClientIp": str,
    },
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesHttpTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesHttpTypeDef
):
    """
    Type definition for `ClientGetTraceSummariesResponseTraceSummaries` `Http`

    Information about the HTTP request served by the trace.

    - **HttpURL** *(string) --*

      The request URL.

    - **HttpStatus** *(integer) --*

      The response status.

    - **HttpMethod** *(string) --*

      The request method.

    - **UserAgent** *(string) --*

      The request's user agent string.

    - **ClientIp** *(string) --*

      The IP address of the requestor.
    """


_ClientGetTraceSummariesResponseTraceSummariesInstanceIdsTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesInstanceIdsTypeDef",
    {"Id": str},
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesInstanceIdsTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesInstanceIdsTypeDef
):
    """
    Type definition for `ClientGetTraceSummariesResponseTraceSummaries` `InstanceIds`

    A list of EC2 instance IDs corresponding to the segments in a trace.

    - **Id** *(string) --*

      The ID of a corresponding EC2 instance.
    """


_ClientGetTraceSummariesResponseTraceSummariesResourceARNsTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesResourceARNsTypeDef",
    {"ARN": str},
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesResourceARNsTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesResourceARNsTypeDef
):
    """
    Type definition for `ClientGetTraceSummariesResponseTraceSummaries` `ResourceARNs`

    A list of resources ARNs corresponding to the segments in a trace.

    - **ARN** *(string) --*

      The ARN of a corresponding resource.
    """


_ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesEntityPathTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesEntityPathTypeDef",
    {"Name": str, "Coverage": float, "Remote": bool},
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesEntityPathTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesEntityPathTypeDef
):
    """
    Type definition for `ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServices` `EntityPath`

    A collection of segments and corresponding subsegments associated to a response
    time warning.

    - **Name** *(string) --*

      The name of the entity.

    - **Coverage** *(float) --*

      The types and messages of the exceptions.

    - **Remote** *(boolean) --*

      A flag that denotes a remote subsegment.
    """


_ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesTypeDef",
    {
        "Name": str,
        "Names": List[str],
        "Type": str,
        "AccountId": str,
        "EntityPath": List[
            ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesEntityPathTypeDef
        ],
        "Inferred": bool,
    },
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesTypeDef
):
    """
    Type definition for `ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCauses` `Services`

    A collection of fields identifying the service in a response time warning.

    - **Name** *(string) --*

      The service name.

    - **Names** *(list) --*

      A collection of associated service names.

      - *(string) --*

    - **Type** *(string) --*

      The type associated to the service.

    - **AccountId** *(string) --*

      The account ID associated to the service.

    - **EntityPath** *(list) --*

      The path of root cause entities found on the service.

      - *(dict) --*

        A collection of segments and corresponding subsegments associated to a response
        time warning.

        - **Name** *(string) --*

          The name of the entity.

        - **Coverage** *(float) --*

          The types and messages of the exceptions.

        - **Remote** *(boolean) --*

          A flag that denotes a remote subsegment.

    - **Inferred** *(boolean) --*

      A Boolean value indicating if the service is inferred from the trace.
    """


_ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesTypeDef",
    {
        "Services": List[
            ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesTypeDef
        ]
    },
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesTypeDef
):
    """
    Type definition for `ClientGetTraceSummariesResponseTraceSummaries` `ResponseTimeRootCauses`

    The root cause information for a response time warning.

    - **Services** *(list) --*

      A list of corresponding services. A service identifies a segment and contains a name,
      account ID, type, and inferred flag.

      - *(dict) --*

        A collection of fields identifying the service in a response time warning.

        - **Name** *(string) --*

          The service name.

        - **Names** *(list) --*

          A collection of associated service names.

          - *(string) --*

        - **Type** *(string) --*

          The type associated to the service.

        - **AccountId** *(string) --*

          The account ID associated to the service.

        - **EntityPath** *(list) --*

          The path of root cause entities found on the service.

          - *(dict) --*

            A collection of segments and corresponding subsegments associated to a response
            time warning.

            - **Name** *(string) --*

              The name of the entity.

            - **Coverage** *(float) --*

              The types and messages of the exceptions.

            - **Remote** *(boolean) --*

              A flag that denotes a remote subsegment.

        - **Inferred** *(boolean) --*

          A Boolean value indicating if the service is inferred from the trace.
    """


_ClientGetTraceSummariesResponseTraceSummariesServiceIdsTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesServiceIdsTypeDef",
    {"Name": str, "Names": List[str], "AccountId": str, "Type": str},
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesServiceIdsTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesServiceIdsTypeDef
):
    """
    Type definition for `ClientGetTraceSummariesResponseTraceSummaries` `ServiceIds`

    - **Name** *(string) --*

    - **Names** *(list) --*

      - *(string) --*

    - **AccountId** *(string) --*

    - **Type** *(string) --*
    """


_ClientGetTraceSummariesResponseTraceSummariesUsersServiceIdsTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesUsersServiceIdsTypeDef",
    {"Name": str, "Names": List[str], "AccountId": str, "Type": str},
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesUsersServiceIdsTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesUsersServiceIdsTypeDef
):
    """
    Type definition for `ClientGetTraceSummariesResponseTraceSummariesUsers` `ServiceIds`

    - **Name** *(string) --*

    - **Names** *(list) --*

      - *(string) --*

    - **AccountId** *(string) --*

    - **Type** *(string) --*
    """


_ClientGetTraceSummariesResponseTraceSummariesUsersTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesUsersTypeDef",
    {
        "UserName": str,
        "ServiceIds": List[
            ClientGetTraceSummariesResponseTraceSummariesUsersServiceIdsTypeDef
        ],
    },
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesUsersTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesUsersTypeDef
):
    """
    Type definition for `ClientGetTraceSummariesResponseTraceSummaries` `Users`

    Information about a user recorded in segment documents.

    - **UserName** *(string) --*

      The user's name.

    - **ServiceIds** *(list) --*

      Services that the user's request hit.

      - *(dict) --*

        - **Name** *(string) --*

        - **Names** *(list) --*

          - *(string) --*

        - **AccountId** *(string) --*

        - **Type** *(string) --*
    """


_ClientGetTraceSummariesResponseTraceSummariesTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesTypeDef",
    {
        "Id": str,
        "Duration": float,
        "ResponseTime": float,
        "HasFault": bool,
        "HasError": bool,
        "HasThrottle": bool,
        "IsPartial": bool,
        "Http": ClientGetTraceSummariesResponseTraceSummariesHttpTypeDef,
        "Annotations": Dict[
            str, List[ClientGetTraceSummariesResponseTraceSummariesAnnotationsTypeDef]
        ],
        "Users": List[ClientGetTraceSummariesResponseTraceSummariesUsersTypeDef],
        "ServiceIds": List[
            ClientGetTraceSummariesResponseTraceSummariesServiceIdsTypeDef
        ],
        "ResourceARNs": List[
            ClientGetTraceSummariesResponseTraceSummariesResourceARNsTypeDef
        ],
        "InstanceIds": List[
            ClientGetTraceSummariesResponseTraceSummariesInstanceIdsTypeDef
        ],
        "AvailabilityZones": List[
            ClientGetTraceSummariesResponseTraceSummariesAvailabilityZonesTypeDef
        ],
        "EntryPoint": ClientGetTraceSummariesResponseTraceSummariesEntryPointTypeDef,
        "FaultRootCauses": List[
            ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesTypeDef
        ],
        "ErrorRootCauses": List[
            ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesTypeDef
        ],
        "ResponseTimeRootCauses": List[
            ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesTypeDef
        ],
        "Revision": int,
        "MatchedEventTime": datetime,
    },
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesTypeDef
):
    """
    Type definition for `ClientGetTraceSummariesResponse` `TraceSummaries`

    Metadata generated from the segment documents in a trace.

    - **Id** *(string) --*

      The unique identifier for the request that generated the trace's segments and subsegments.

    - **Duration** *(float) --*

      The length of time in seconds between the start time of the root segment and the end time
      of the last segment that completed.

    - **ResponseTime** *(float) --*

      The length of time in seconds between the start and end times of the root segment. If the
      service performs work asynchronously, the response time measures the time before the
      response is sent to the user, while the duration measures the amount of time before the
      last traced activity completes.

    - **HasFault** *(boolean) --*

      One or more of the segment documents has a 500 series error.

    - **HasError** *(boolean) --*

      One or more of the segment documents has a 400 series error.

    - **HasThrottle** *(boolean) --*

      One or more of the segment documents has a 429 throttling error.

    - **IsPartial** *(boolean) --*

      One or more of the segment documents is in progress.

    - **Http** *(dict) --*

      Information about the HTTP request served by the trace.

      - **HttpURL** *(string) --*

        The request URL.

      - **HttpStatus** *(integer) --*

        The response status.

      - **HttpMethod** *(string) --*

        The request method.

      - **UserAgent** *(string) --*

        The request's user agent string.

      - **ClientIp** *(string) --*

        The IP address of the requestor.

    - **Annotations** *(dict) --*

      Annotations from the trace's segment documents.

      - *(string) --*

        - *(list) --*

          - *(dict) --*

            Information about a segment annotation.

            - **AnnotationValue** *(dict) --*

              Values of the annotation.

              - **NumberValue** *(float) --*

                Value for a Number annotation.

              - **BooleanValue** *(boolean) --*

                Value for a Boolean annotation.

              - **StringValue** *(string) --*

                Value for a String annotation.

            - **ServiceIds** *(list) --*

              Services to which the annotation applies.

              - *(dict) --*

                - **Name** *(string) --*

                - **Names** *(list) --*

                  - *(string) --*

                - **AccountId** *(string) --*

                - **Type** *(string) --*

    - **Users** *(list) --*

      Users from the trace's segment documents.

      - *(dict) --*

        Information about a user recorded in segment documents.

        - **UserName** *(string) --*

          The user's name.

        - **ServiceIds** *(list) --*

          Services that the user's request hit.

          - *(dict) --*

            - **Name** *(string) --*

            - **Names** *(list) --*

              - *(string) --*

            - **AccountId** *(string) --*

            - **Type** *(string) --*

    - **ServiceIds** *(list) --*

      Service IDs from the trace's segment documents.

      - *(dict) --*

        - **Name** *(string) --*

        - **Names** *(list) --*

          - *(string) --*

        - **AccountId** *(string) --*

        - **Type** *(string) --*

    - **ResourceARNs** *(list) --*

      A list of resource ARNs for any resource corresponding to the trace segments.

      - *(dict) --*

        A list of resources ARNs corresponding to the segments in a trace.

        - **ARN** *(string) --*

          The ARN of a corresponding resource.

    - **InstanceIds** *(list) --*

      A list of EC2 instance IDs for any instance corresponding to the trace segments.

      - *(dict) --*

        A list of EC2 instance IDs corresponding to the segments in a trace.

        - **Id** *(string) --*

          The ID of a corresponding EC2 instance.

    - **AvailabilityZones** *(list) --*

      A list of availability zones for any zone corresponding to the trace segments.

      - *(dict) --*

        A list of availability zones corresponding to the segments in a trace.

        - **Name** *(string) --*

          The name of a corresponding availability zone.

    - **EntryPoint** *(dict) --*

      The root of a trace.

      - **Name** *(string) --*

      - **Names** *(list) --*

        - *(string) --*

      - **AccountId** *(string) --*

      - **Type** *(string) --*

    - **FaultRootCauses** *(list) --*

      A collection of FaultRootCause structures corresponding to the the trace segments.

      - *(dict) --*

        The root cause information for a trace summary fault.

        - **Services** *(list) --*

          A list of corresponding services. A service identifies a segment and it contains a
          name, account ID, type, and inferred flag.

          - *(dict) --*

            A collection of fields identifying the services in a trace summary fault.

            - **Name** *(string) --*

              The service name.

            - **Names** *(list) --*

              A collection of associated service names.

              - *(string) --*

            - **Type** *(string) --*

              The type associated to the service.

            - **AccountId** *(string) --*

              The account ID associated to the service.

            - **EntityPath** *(list) --*

              The path of root cause entities found on the service.

              - *(dict) --*

                A collection of segments and corresponding subsegments associated to a trace
                summary fault error.

                - **Name** *(string) --*

                  The name of the entity.

                - **Exceptions** *(list) --*

                  The types and messages of the exceptions.

                  - *(dict) --*

                    The exception associated with a root cause.

                    - **Name** *(string) --*

                      The name of the exception.

                    - **Message** *(string) --*

                      The message of the exception.

                - **Remote** *(boolean) --*

                  A flag that denotes a remote subsegment.

            - **Inferred** *(boolean) --*

              A Boolean value indicating if the service is inferred from the trace.

    - **ErrorRootCauses** *(list) --*

      A collection of ErrorRootCause structures corresponding to the trace segments.

      - *(dict) --*

        The root cause of a trace summary error.

        - **Services** *(list) --*

          A list of services corresponding to an error. A service identifies a segment and it
          contains a name, account ID, type, and inferred flag.

          - *(dict) --*

            A collection of fields identifying the services in a trace summary error.

            - **Name** *(string) --*

              The service name.

            - **Names** *(list) --*

              A collection of associated service names.

              - *(string) --*

            - **Type** *(string) --*

              The type associated to the service.

            - **AccountId** *(string) --*

              The account ID associated to the service.

            - **EntityPath** *(list) --*

              The path of root cause entities found on the service.

              - *(dict) --*

                A collection of segments and corresponding subsegments associated to a trace
                summary error.

                - **Name** *(string) --*

                  The name of the entity.

                - **Exceptions** *(list) --*

                  The types and messages of the exceptions.

                  - *(dict) --*

                    The exception associated with a root cause.

                    - **Name** *(string) --*

                      The name of the exception.

                    - **Message** *(string) --*

                      The message of the exception.

                - **Remote** *(boolean) --*

                  A flag that denotes a remote subsegment.

            - **Inferred** *(boolean) --*

              A Boolean value indicating if the service is inferred from the trace.

    - **ResponseTimeRootCauses** *(list) --*

      A collection of ResponseTimeRootCause structures corresponding to the trace segments.

      - *(dict) --*

        The root cause information for a response time warning.

        - **Services** *(list) --*

          A list of corresponding services. A service identifies a segment and contains a name,
          account ID, type, and inferred flag.

          - *(dict) --*

            A collection of fields identifying the service in a response time warning.

            - **Name** *(string) --*

              The service name.

            - **Names** *(list) --*

              A collection of associated service names.

              - *(string) --*

            - **Type** *(string) --*

              The type associated to the service.

            - **AccountId** *(string) --*

              The account ID associated to the service.

            - **EntityPath** *(list) --*

              The path of root cause entities found on the service.

              - *(dict) --*

                A collection of segments and corresponding subsegments associated to a response
                time warning.

                - **Name** *(string) --*

                  The name of the entity.

                - **Coverage** *(float) --*

                  The types and messages of the exceptions.

                - **Remote** *(boolean) --*

                  A flag that denotes a remote subsegment.

            - **Inferred** *(boolean) --*

              A Boolean value indicating if the service is inferred from the trace.

    - **Revision** *(integer) --*

      The revision number of a trace.

    - **MatchedEventTime** *(datetime) --*

      The matched time stamp of a defined event.
    """


_ClientGetTraceSummariesResponseTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTypeDef",
    {
        "TraceSummaries": List[ClientGetTraceSummariesResponseTraceSummariesTypeDef],
        "ApproximateTime": datetime,
        "TracesProcessedCount": int,
        "NextToken": str,
    },
    total=False,
)


class ClientGetTraceSummariesResponseTypeDef(_ClientGetTraceSummariesResponseTypeDef):
    """
    Type definition for `ClientGetTraceSummaries` `Response`

    - **TraceSummaries** *(list) --*

      Trace IDs and metadata for traces that were found in the specified time frame.

      - *(dict) --*

        Metadata generated from the segment documents in a trace.

        - **Id** *(string) --*

          The unique identifier for the request that generated the trace's segments and subsegments.

        - **Duration** *(float) --*

          The length of time in seconds between the start time of the root segment and the end time
          of the last segment that completed.

        - **ResponseTime** *(float) --*

          The length of time in seconds between the start and end times of the root segment. If the
          service performs work asynchronously, the response time measures the time before the
          response is sent to the user, while the duration measures the amount of time before the
          last traced activity completes.

        - **HasFault** *(boolean) --*

          One or more of the segment documents has a 500 series error.

        - **HasError** *(boolean) --*

          One or more of the segment documents has a 400 series error.

        - **HasThrottle** *(boolean) --*

          One or more of the segment documents has a 429 throttling error.

        - **IsPartial** *(boolean) --*

          One or more of the segment documents is in progress.

        - **Http** *(dict) --*

          Information about the HTTP request served by the trace.

          - **HttpURL** *(string) --*

            The request URL.

          - **HttpStatus** *(integer) --*

            The response status.

          - **HttpMethod** *(string) --*

            The request method.

          - **UserAgent** *(string) --*

            The request's user agent string.

          - **ClientIp** *(string) --*

            The IP address of the requestor.

        - **Annotations** *(dict) --*

          Annotations from the trace's segment documents.

          - *(string) --*

            - *(list) --*

              - *(dict) --*

                Information about a segment annotation.

                - **AnnotationValue** *(dict) --*

                  Values of the annotation.

                  - **NumberValue** *(float) --*

                    Value for a Number annotation.

                  - **BooleanValue** *(boolean) --*

                    Value for a Boolean annotation.

                  - **StringValue** *(string) --*

                    Value for a String annotation.

                - **ServiceIds** *(list) --*

                  Services to which the annotation applies.

                  - *(dict) --*

                    - **Name** *(string) --*

                    - **Names** *(list) --*

                      - *(string) --*

                    - **AccountId** *(string) --*

                    - **Type** *(string) --*

        - **Users** *(list) --*

          Users from the trace's segment documents.

          - *(dict) --*

            Information about a user recorded in segment documents.

            - **UserName** *(string) --*

              The user's name.

            - **ServiceIds** *(list) --*

              Services that the user's request hit.

              - *(dict) --*

                - **Name** *(string) --*

                - **Names** *(list) --*

                  - *(string) --*

                - **AccountId** *(string) --*

                - **Type** *(string) --*

        - **ServiceIds** *(list) --*

          Service IDs from the trace's segment documents.

          - *(dict) --*

            - **Name** *(string) --*

            - **Names** *(list) --*

              - *(string) --*

            - **AccountId** *(string) --*

            - **Type** *(string) --*

        - **ResourceARNs** *(list) --*

          A list of resource ARNs for any resource corresponding to the trace segments.

          - *(dict) --*

            A list of resources ARNs corresponding to the segments in a trace.

            - **ARN** *(string) --*

              The ARN of a corresponding resource.

        - **InstanceIds** *(list) --*

          A list of EC2 instance IDs for any instance corresponding to the trace segments.

          - *(dict) --*

            A list of EC2 instance IDs corresponding to the segments in a trace.

            - **Id** *(string) --*

              The ID of a corresponding EC2 instance.

        - **AvailabilityZones** *(list) --*

          A list of availability zones for any zone corresponding to the trace segments.

          - *(dict) --*

            A list of availability zones corresponding to the segments in a trace.

            - **Name** *(string) --*

              The name of a corresponding availability zone.

        - **EntryPoint** *(dict) --*

          The root of a trace.

          - **Name** *(string) --*

          - **Names** *(list) --*

            - *(string) --*

          - **AccountId** *(string) --*

          - **Type** *(string) --*

        - **FaultRootCauses** *(list) --*

          A collection of FaultRootCause structures corresponding to the the trace segments.

          - *(dict) --*

            The root cause information for a trace summary fault.

            - **Services** *(list) --*

              A list of corresponding services. A service identifies a segment and it contains a
              name, account ID, type, and inferred flag.

              - *(dict) --*

                A collection of fields identifying the services in a trace summary fault.

                - **Name** *(string) --*

                  The service name.

                - **Names** *(list) --*

                  A collection of associated service names.

                  - *(string) --*

                - **Type** *(string) --*

                  The type associated to the service.

                - **AccountId** *(string) --*

                  The account ID associated to the service.

                - **EntityPath** *(list) --*

                  The path of root cause entities found on the service.

                  - *(dict) --*

                    A collection of segments and corresponding subsegments associated to a trace
                    summary fault error.

                    - **Name** *(string) --*

                      The name of the entity.

                    - **Exceptions** *(list) --*

                      The types and messages of the exceptions.

                      - *(dict) --*

                        The exception associated with a root cause.

                        - **Name** *(string) --*

                          The name of the exception.

                        - **Message** *(string) --*

                          The message of the exception.

                    - **Remote** *(boolean) --*

                      A flag that denotes a remote subsegment.

                - **Inferred** *(boolean) --*

                  A Boolean value indicating if the service is inferred from the trace.

        - **ErrorRootCauses** *(list) --*

          A collection of ErrorRootCause structures corresponding to the trace segments.

          - *(dict) --*

            The root cause of a trace summary error.

            - **Services** *(list) --*

              A list of services corresponding to an error. A service identifies a segment and it
              contains a name, account ID, type, and inferred flag.

              - *(dict) --*

                A collection of fields identifying the services in a trace summary error.

                - **Name** *(string) --*

                  The service name.

                - **Names** *(list) --*

                  A collection of associated service names.

                  - *(string) --*

                - **Type** *(string) --*

                  The type associated to the service.

                - **AccountId** *(string) --*

                  The account ID associated to the service.

                - **EntityPath** *(list) --*

                  The path of root cause entities found on the service.

                  - *(dict) --*

                    A collection of segments and corresponding subsegments associated to a trace
                    summary error.

                    - **Name** *(string) --*

                      The name of the entity.

                    - **Exceptions** *(list) --*

                      The types and messages of the exceptions.

                      - *(dict) --*

                        The exception associated with a root cause.

                        - **Name** *(string) --*

                          The name of the exception.

                        - **Message** *(string) --*

                          The message of the exception.

                    - **Remote** *(boolean) --*

                      A flag that denotes a remote subsegment.

                - **Inferred** *(boolean) --*

                  A Boolean value indicating if the service is inferred from the trace.

        - **ResponseTimeRootCauses** *(list) --*

          A collection of ResponseTimeRootCause structures corresponding to the trace segments.

          - *(dict) --*

            The root cause information for a response time warning.

            - **Services** *(list) --*

              A list of corresponding services. A service identifies a segment and contains a name,
              account ID, type, and inferred flag.

              - *(dict) --*

                A collection of fields identifying the service in a response time warning.

                - **Name** *(string) --*

                  The service name.

                - **Names** *(list) --*

                  A collection of associated service names.

                  - *(string) --*

                - **Type** *(string) --*

                  The type associated to the service.

                - **AccountId** *(string) --*

                  The account ID associated to the service.

                - **EntityPath** *(list) --*

                  The path of root cause entities found on the service.

                  - *(dict) --*

                    A collection of segments and corresponding subsegments associated to a response
                    time warning.

                    - **Name** *(string) --*

                      The name of the entity.

                    - **Coverage** *(float) --*

                      The types and messages of the exceptions.

                    - **Remote** *(boolean) --*

                      A flag that denotes a remote subsegment.

                - **Inferred** *(boolean) --*

                  A Boolean value indicating if the service is inferred from the trace.

        - **Revision** *(integer) --*

          The revision number of a trace.

        - **MatchedEventTime** *(datetime) --*

          The matched time stamp of a defined event.

    - **ApproximateTime** *(datetime) --*

      The start time of this page of results.

    - **TracesProcessedCount** *(integer) --*

      The total number of traces processed, including traces that did not match the specified
      filter expression.

    - **NextToken** *(string) --*

      If the requested time frame contained more than one page of results, you can use this token
      to retrieve the next page. The first page contains the most most recent results, closest to
      the end of the time frame.
    """


_ClientGetTraceSummariesSamplingStrategyTypeDef = TypedDict(
    "_ClientGetTraceSummariesSamplingStrategyTypeDef",
    {"Name": str, "Value": float},
    total=False,
)


class ClientGetTraceSummariesSamplingStrategyTypeDef(
    _ClientGetTraceSummariesSamplingStrategyTypeDef
):
    """
    Type definition for `ClientGetTraceSummaries` `SamplingStrategy`

    A paramater to indicate whether to enable sampling on trace summaries. Input parameters are Name
    and Value.

    - **Name** *(string) --*

      The name of a sampling rule.

    - **Value** *(float) --*

      The value of a sampling rule.
    """


_ClientPutEncryptionConfigResponseEncryptionConfigTypeDef = TypedDict(
    "_ClientPutEncryptionConfigResponseEncryptionConfigTypeDef",
    {"KeyId": str, "Status": str, "Type": str},
    total=False,
)


class ClientPutEncryptionConfigResponseEncryptionConfigTypeDef(
    _ClientPutEncryptionConfigResponseEncryptionConfigTypeDef
):
    """
    Type definition for `ClientPutEncryptionConfigResponse` `EncryptionConfig`

    The new encryption configuration.

    - **KeyId** *(string) --*

      The ID of the customer master key (CMK) used for encryption, if applicable.

    - **Status** *(string) --*

      The encryption status. While the status is ``UPDATING`` , X-Ray may encrypt data with a
      combination of the new and old settings.

    - **Type** *(string) --*

      The type of encryption. Set to ``KMS`` for encryption with CMKs. Set to ``NONE`` for
      default encryption.
    """


_ClientPutEncryptionConfigResponseTypeDef = TypedDict(
    "_ClientPutEncryptionConfigResponseTypeDef",
    {"EncryptionConfig": ClientPutEncryptionConfigResponseEncryptionConfigTypeDef},
    total=False,
)


class ClientPutEncryptionConfigResponseTypeDef(
    _ClientPutEncryptionConfigResponseTypeDef
):
    """
    Type definition for `ClientPutEncryptionConfig` `Response`

    - **EncryptionConfig** *(dict) --*

      The new encryption configuration.

      - **KeyId** *(string) --*

        The ID of the customer master key (CMK) used for encryption, if applicable.

      - **Status** *(string) --*

        The encryption status. While the status is ``UPDATING`` , X-Ray may encrypt data with a
        combination of the new and old settings.

      - **Type** *(string) --*

        The type of encryption. Set to ``KMS`` for encryption with CMKs. Set to ``NONE`` for
        default encryption.
    """


_ClientPutTelemetryRecordsTelemetryRecordsBackendConnectionErrorsTypeDef = TypedDict(
    "_ClientPutTelemetryRecordsTelemetryRecordsBackendConnectionErrorsTypeDef",
    {
        "TimeoutCount": int,
        "ConnectionRefusedCount": int,
        "HTTPCode4XXCount": int,
        "HTTPCode5XXCount": int,
        "UnknownHostCount": int,
        "OtherCount": int,
    },
    total=False,
)


class ClientPutTelemetryRecordsTelemetryRecordsBackendConnectionErrorsTypeDef(
    _ClientPutTelemetryRecordsTelemetryRecordsBackendConnectionErrorsTypeDef
):
    """
    Type definition for `ClientPutTelemetryRecordsTelemetryRecords` `BackendConnectionErrors`

    - **TimeoutCount** *(integer) --*

    - **ConnectionRefusedCount** *(integer) --*

    - **HTTPCode4XXCount** *(integer) --*

    - **HTTPCode5XXCount** *(integer) --*

    - **UnknownHostCount** *(integer) --*

    - **OtherCount** *(integer) --*
    """


_RequiredClientPutTelemetryRecordsTelemetryRecordsTypeDef = TypedDict(
    "_RequiredClientPutTelemetryRecordsTelemetryRecordsTypeDef", {"Timestamp": datetime}
)
_OptionalClientPutTelemetryRecordsTelemetryRecordsTypeDef = TypedDict(
    "_OptionalClientPutTelemetryRecordsTelemetryRecordsTypeDef",
    {
        "SegmentsReceivedCount": int,
        "SegmentsSentCount": int,
        "SegmentsSpilloverCount": int,
        "SegmentsRejectedCount": int,
        "BackendConnectionErrors": ClientPutTelemetryRecordsTelemetryRecordsBackendConnectionErrorsTypeDef,
    },
    total=False,
)


class ClientPutTelemetryRecordsTelemetryRecordsTypeDef(
    _RequiredClientPutTelemetryRecordsTelemetryRecordsTypeDef,
    _OptionalClientPutTelemetryRecordsTelemetryRecordsTypeDef,
):
    """
    Type definition for `ClientPutTelemetryRecords` `TelemetryRecords`

    - **Timestamp** *(datetime) --* **[REQUIRED]**

    - **SegmentsReceivedCount** *(integer) --*

    - **SegmentsSentCount** *(integer) --*

    - **SegmentsSpilloverCount** *(integer) --*

    - **SegmentsRejectedCount** *(integer) --*

    - **BackendConnectionErrors** *(dict) --*

      - **TimeoutCount** *(integer) --*

      - **ConnectionRefusedCount** *(integer) --*

      - **HTTPCode4XXCount** *(integer) --*

      - **HTTPCode5XXCount** *(integer) --*

      - **UnknownHostCount** *(integer) --*

      - **OtherCount** *(integer) --*
    """


_ClientPutTraceSegmentsResponseUnprocessedTraceSegmentsTypeDef = TypedDict(
    "_ClientPutTraceSegmentsResponseUnprocessedTraceSegmentsTypeDef",
    {"Id": str, "ErrorCode": str, "Message": str},
    total=False,
)


class ClientPutTraceSegmentsResponseUnprocessedTraceSegmentsTypeDef(
    _ClientPutTraceSegmentsResponseUnprocessedTraceSegmentsTypeDef
):
    """
    Type definition for `ClientPutTraceSegmentsResponse` `UnprocessedTraceSegments`

    Information about a segment that failed processing.

    - **Id** *(string) --*

      The segment's ID.

    - **ErrorCode** *(string) --*

      The error that caused processing to fail.

    - **Message** *(string) --*

      The error message.
    """


_ClientPutTraceSegmentsResponseTypeDef = TypedDict(
    "_ClientPutTraceSegmentsResponseTypeDef",
    {
        "UnprocessedTraceSegments": List[
            ClientPutTraceSegmentsResponseUnprocessedTraceSegmentsTypeDef
        ]
    },
    total=False,
)


class ClientPutTraceSegmentsResponseTypeDef(_ClientPutTraceSegmentsResponseTypeDef):
    """
    Type definition for `ClientPutTraceSegments` `Response`

    - **UnprocessedTraceSegments** *(list) --*

      Segments that failed processing.

      - *(dict) --*

        Information about a segment that failed processing.

        - **Id** *(string) --*

          The segment's ID.

        - **ErrorCode** *(string) --*

          The error that caused processing to fail.

        - **Message** *(string) --*

          The error message.
    """


_ClientUpdateGroupResponseGroupTypeDef = TypedDict(
    "_ClientUpdateGroupResponseGroupTypeDef",
    {"GroupName": str, "GroupARN": str, "FilterExpression": str},
    total=False,
)


class ClientUpdateGroupResponseGroupTypeDef(_ClientUpdateGroupResponseGroupTypeDef):
    """
    Type definition for `ClientUpdateGroupResponse` `Group`

    The group that was updated. Contains the name of the group that was updated, the ARN of the
    group that was updated, and the updated filter expression assigned to the group.

    - **GroupName** *(string) --*

      The unique case-sensitive name of the group.

    - **GroupARN** *(string) --*

      The ARN of the group generated based on the GroupName.

    - **FilterExpression** *(string) --*

      The filter expression defining the parameters to include traces.
    """


_ClientUpdateGroupResponseTypeDef = TypedDict(
    "_ClientUpdateGroupResponseTypeDef",
    {"Group": ClientUpdateGroupResponseGroupTypeDef},
    total=False,
)


class ClientUpdateGroupResponseTypeDef(_ClientUpdateGroupResponseTypeDef):
    """
    Type definition for `ClientUpdateGroup` `Response`

    - **Group** *(dict) --*

      The group that was updated. Contains the name of the group that was updated, the ARN of the
      group that was updated, and the updated filter expression assigned to the group.

      - **GroupName** *(string) --*

        The unique case-sensitive name of the group.

      - **GroupARN** *(string) --*

        The ARN of the group generated based on the GroupName.

      - **FilterExpression** *(string) --*

        The filter expression defining the parameters to include traces.
    """


_ClientUpdateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef = TypedDict(
    "_ClientUpdateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef",
    {
        "RuleName": str,
        "RuleARN": str,
        "ResourceARN": str,
        "Priority": int,
        "FixedRate": float,
        "ReservoirSize": int,
        "ServiceName": str,
        "ServiceType": str,
        "Host": str,
        "HTTPMethod": str,
        "URLPath": str,
        "Version": int,
        "Attributes": Dict[str, str],
    },
    total=False,
)


class ClientUpdateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef(
    _ClientUpdateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef
):
    """
    Type definition for `ClientUpdateSamplingRuleResponseSamplingRuleRecord` `SamplingRule`

    The sampling rule.

    - **RuleName** *(string) --*

      The name of the sampling rule. Specify a rule by either name or ARN, but not both.

    - **RuleARN** *(string) --*

      The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.

    - **ResourceARN** *(string) --*

      Matches the ARN of the AWS resource on which the service runs.

    - **Priority** *(integer) --*

      The priority of the sampling rule.

    - **FixedRate** *(float) --*

      The percentage of matching requests to instrument, after the reservoir is exhausted.

    - **ReservoirSize** *(integer) --*

      A fixed number of matching requests to instrument per second, prior to applying the fixed
      rate. The reservoir is not used directly by services, but applies to all services using
      the rule collectively.

    - **ServiceName** *(string) --*

      Matches the ``name`` that the service uses to identify itself in segments.

    - **ServiceType** *(string) --*

      Matches the ``origin`` that the service uses to identify its type in segments.

    - **Host** *(string) --*

      Matches the hostname from a request URL.

    - **HTTPMethod** *(string) --*

      Matches the HTTP method of a request.

    - **URLPath** *(string) --*

      Matches the path from a request URL.

    - **Version** *(integer) --*

      The version of the sampling rule format (``1`` ).

    - **Attributes** *(dict) --*

      Matches attributes derived from the request.

      - *(string) --*

        - *(string) --*
    """


_ClientUpdateSamplingRuleResponseSamplingRuleRecordTypeDef = TypedDict(
    "_ClientUpdateSamplingRuleResponseSamplingRuleRecordTypeDef",
    {
        "SamplingRule": ClientUpdateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
    },
    total=False,
)


class ClientUpdateSamplingRuleResponseSamplingRuleRecordTypeDef(
    _ClientUpdateSamplingRuleResponseSamplingRuleRecordTypeDef
):
    """
    Type definition for `ClientUpdateSamplingRuleResponse` `SamplingRuleRecord`

    The updated rule definition and metadata.

    - **SamplingRule** *(dict) --*

      The sampling rule.

      - **RuleName** *(string) --*

        The name of the sampling rule. Specify a rule by either name or ARN, but not both.

      - **RuleARN** *(string) --*

        The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.

      - **ResourceARN** *(string) --*

        Matches the ARN of the AWS resource on which the service runs.

      - **Priority** *(integer) --*

        The priority of the sampling rule.

      - **FixedRate** *(float) --*

        The percentage of matching requests to instrument, after the reservoir is exhausted.

      - **ReservoirSize** *(integer) --*

        A fixed number of matching requests to instrument per second, prior to applying the fixed
        rate. The reservoir is not used directly by services, but applies to all services using
        the rule collectively.

      - **ServiceName** *(string) --*

        Matches the ``name`` that the service uses to identify itself in segments.

      - **ServiceType** *(string) --*

        Matches the ``origin`` that the service uses to identify its type in segments.

      - **Host** *(string) --*

        Matches the hostname from a request URL.

      - **HTTPMethod** *(string) --*

        Matches the HTTP method of a request.

      - **URLPath** *(string) --*

        Matches the path from a request URL.

      - **Version** *(integer) --*

        The version of the sampling rule format (``1`` ).

      - **Attributes** *(dict) --*

        Matches attributes derived from the request.

        - *(string) --*

          - *(string) --*

    - **CreatedAt** *(datetime) --*

      When the rule was created.

    - **ModifiedAt** *(datetime) --*

      When the rule was last modified.
    """


_ClientUpdateSamplingRuleResponseTypeDef = TypedDict(
    "_ClientUpdateSamplingRuleResponseTypeDef",
    {"SamplingRuleRecord": ClientUpdateSamplingRuleResponseSamplingRuleRecordTypeDef},
    total=False,
)


class ClientUpdateSamplingRuleResponseTypeDef(_ClientUpdateSamplingRuleResponseTypeDef):
    """
    Type definition for `ClientUpdateSamplingRule` `Response`

    - **SamplingRuleRecord** *(dict) --*

      The updated rule definition and metadata.

      - **SamplingRule** *(dict) --*

        The sampling rule.

        - **RuleName** *(string) --*

          The name of the sampling rule. Specify a rule by either name or ARN, but not both.

        - **RuleARN** *(string) --*

          The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.

        - **ResourceARN** *(string) --*

          Matches the ARN of the AWS resource on which the service runs.

        - **Priority** *(integer) --*

          The priority of the sampling rule.

        - **FixedRate** *(float) --*

          The percentage of matching requests to instrument, after the reservoir is exhausted.

        - **ReservoirSize** *(integer) --*

          A fixed number of matching requests to instrument per second, prior to applying the fixed
          rate. The reservoir is not used directly by services, but applies to all services using
          the rule collectively.

        - **ServiceName** *(string) --*

          Matches the ``name`` that the service uses to identify itself in segments.

        - **ServiceType** *(string) --*

          Matches the ``origin`` that the service uses to identify its type in segments.

        - **Host** *(string) --*

          Matches the hostname from a request URL.

        - **HTTPMethod** *(string) --*

          Matches the HTTP method of a request.

        - **URLPath** *(string) --*

          Matches the path from a request URL.

        - **Version** *(integer) --*

          The version of the sampling rule format (``1`` ).

        - **Attributes** *(dict) --*

          Matches attributes derived from the request.

          - *(string) --*

            - *(string) --*

      - **CreatedAt** *(datetime) --*

        When the rule was created.

      - **ModifiedAt** *(datetime) --*

        When the rule was last modified.
    """


_ClientUpdateSamplingRuleSamplingRuleUpdateTypeDef = TypedDict(
    "_ClientUpdateSamplingRuleSamplingRuleUpdateTypeDef",
    {
        "RuleName": str,
        "RuleARN": str,
        "ResourceARN": str,
        "Priority": int,
        "FixedRate": float,
        "ReservoirSize": int,
        "Host": str,
        "ServiceName": str,
        "ServiceType": str,
        "HTTPMethod": str,
        "URLPath": str,
        "Attributes": Dict[str, str],
    },
    total=False,
)


class ClientUpdateSamplingRuleSamplingRuleUpdateTypeDef(
    _ClientUpdateSamplingRuleSamplingRuleUpdateTypeDef
):
    """
    Type definition for `ClientUpdateSamplingRule` `SamplingRuleUpdate`

    The rule and fields to change.

    - **RuleName** *(string) --*

      The name of the sampling rule. Specify a rule by either name or ARN, but not both.

    - **RuleARN** *(string) --*

      The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.

    - **ResourceARN** *(string) --*

      Matches the ARN of the AWS resource on which the service runs.

    - **Priority** *(integer) --*

      The priority of the sampling rule.

    - **FixedRate** *(float) --*

      The percentage of matching requests to instrument, after the reservoir is exhausted.

    - **ReservoirSize** *(integer) --*

      A fixed number of matching requests to instrument per second, prior to applying the fixed rate.
      The reservoir is not used directly by services, but applies to all services using the rule
      collectively.

    - **Host** *(string) --*

      Matches the hostname from a request URL.

    - **ServiceName** *(string) --*

      Matches the ``name`` that the service uses to identify itself in segments.

    - **ServiceType** *(string) --*

      Matches the ``origin`` that the service uses to identify its type in segments.

    - **HTTPMethod** *(string) --*

      Matches the HTTP method of a request.

    - **URLPath** *(string) --*

      Matches the path from a request URL.

    - **Attributes** *(dict) --*

      Matches attributes derived from the request.

      - *(string) --*

        - *(string) --*
    """


_GetGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetGroupsPaginatePaginationConfigTypeDef(
    _GetGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetGroupsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetGroupsPaginateResponseGroupsTypeDef = TypedDict(
    "_GetGroupsPaginateResponseGroupsTypeDef",
    {"GroupName": str, "GroupARN": str, "FilterExpression": str},
    total=False,
)


class GetGroupsPaginateResponseGroupsTypeDef(_GetGroupsPaginateResponseGroupsTypeDef):
    """
    Type definition for `GetGroupsPaginateResponse` `Groups`

    Details for a group without metadata.

    - **GroupName** *(string) --*

      The unique case-sensitive name of the group.

    - **GroupARN** *(string) --*

      The ARN of the group generated based on the GroupName.

    - **FilterExpression** *(string) --*

      The filter expression defining the parameters to include traces.
    """


_GetGroupsPaginateResponseTypeDef = TypedDict(
    "_GetGroupsPaginateResponseTypeDef",
    {"Groups": List[GetGroupsPaginateResponseGroupsTypeDef]},
    total=False,
)


class GetGroupsPaginateResponseTypeDef(_GetGroupsPaginateResponseTypeDef):
    """
    Type definition for `GetGroupsPaginate` `Response`

    - **Groups** *(list) --*

      The collection of all active groups.

      - *(dict) --*

        Details for a group without metadata.

        - **GroupName** *(string) --*

          The unique case-sensitive name of the group.

        - **GroupARN** *(string) --*

          The ARN of the group generated based on the GroupName.

        - **FilterExpression** *(string) --*

          The filter expression defining the parameters to include traces.
    """


_GetSamplingRulesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetSamplingRulesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetSamplingRulesPaginatePaginationConfigTypeDef(
    _GetSamplingRulesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetSamplingRulesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetSamplingRulesPaginateResponseSamplingRuleRecordsSamplingRuleTypeDef = TypedDict(
    "_GetSamplingRulesPaginateResponseSamplingRuleRecordsSamplingRuleTypeDef",
    {
        "RuleName": str,
        "RuleARN": str,
        "ResourceARN": str,
        "Priority": int,
        "FixedRate": float,
        "ReservoirSize": int,
        "ServiceName": str,
        "ServiceType": str,
        "Host": str,
        "HTTPMethod": str,
        "URLPath": str,
        "Version": int,
        "Attributes": Dict[str, str],
    },
    total=False,
)


class GetSamplingRulesPaginateResponseSamplingRuleRecordsSamplingRuleTypeDef(
    _GetSamplingRulesPaginateResponseSamplingRuleRecordsSamplingRuleTypeDef
):
    """
    Type definition for `GetSamplingRulesPaginateResponseSamplingRuleRecords` `SamplingRule`

    The sampling rule.

    - **RuleName** *(string) --*

      The name of the sampling rule. Specify a rule by either name or ARN, but not both.

    - **RuleARN** *(string) --*

      The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.

    - **ResourceARN** *(string) --*

      Matches the ARN of the AWS resource on which the service runs.

    - **Priority** *(integer) --*

      The priority of the sampling rule.

    - **FixedRate** *(float) --*

      The percentage of matching requests to instrument, after the reservoir is exhausted.

    - **ReservoirSize** *(integer) --*

      A fixed number of matching requests to instrument per second, prior to applying the
      fixed rate. The reservoir is not used directly by services, but applies to all services
      using the rule collectively.

    - **ServiceName** *(string) --*

      Matches the ``name`` that the service uses to identify itself in segments.

    - **ServiceType** *(string) --*

      Matches the ``origin`` that the service uses to identify its type in segments.

    - **Host** *(string) --*

      Matches the hostname from a request URL.

    - **HTTPMethod** *(string) --*

      Matches the HTTP method of a request.

    - **URLPath** *(string) --*

      Matches the path from a request URL.

    - **Version** *(integer) --*

      The version of the sampling rule format (``1`` ).

    - **Attributes** *(dict) --*

      Matches attributes derived from the request.

      - *(string) --*

        - *(string) --*
    """


_GetSamplingRulesPaginateResponseSamplingRuleRecordsTypeDef = TypedDict(
    "_GetSamplingRulesPaginateResponseSamplingRuleRecordsTypeDef",
    {
        "SamplingRule": GetSamplingRulesPaginateResponseSamplingRuleRecordsSamplingRuleTypeDef,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
    },
    total=False,
)


class GetSamplingRulesPaginateResponseSamplingRuleRecordsTypeDef(
    _GetSamplingRulesPaginateResponseSamplingRuleRecordsTypeDef
):
    """
    Type definition for `GetSamplingRulesPaginateResponse` `SamplingRuleRecords`

    A  SamplingRule and its metadata.

    - **SamplingRule** *(dict) --*

      The sampling rule.

      - **RuleName** *(string) --*

        The name of the sampling rule. Specify a rule by either name or ARN, but not both.

      - **RuleARN** *(string) --*

        The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.

      - **ResourceARN** *(string) --*

        Matches the ARN of the AWS resource on which the service runs.

      - **Priority** *(integer) --*

        The priority of the sampling rule.

      - **FixedRate** *(float) --*

        The percentage of matching requests to instrument, after the reservoir is exhausted.

      - **ReservoirSize** *(integer) --*

        A fixed number of matching requests to instrument per second, prior to applying the
        fixed rate. The reservoir is not used directly by services, but applies to all services
        using the rule collectively.

      - **ServiceName** *(string) --*

        Matches the ``name`` that the service uses to identify itself in segments.

      - **ServiceType** *(string) --*

        Matches the ``origin`` that the service uses to identify its type in segments.

      - **Host** *(string) --*

        Matches the hostname from a request URL.

      - **HTTPMethod** *(string) --*

        Matches the HTTP method of a request.

      - **URLPath** *(string) --*

        Matches the path from a request URL.

      - **Version** *(integer) --*

        The version of the sampling rule format (``1`` ).

      - **Attributes** *(dict) --*

        Matches attributes derived from the request.

        - *(string) --*

          - *(string) --*

    - **CreatedAt** *(datetime) --*

      When the rule was created.

    - **ModifiedAt** *(datetime) --*

      When the rule was last modified.
    """


_GetSamplingRulesPaginateResponseTypeDef = TypedDict(
    "_GetSamplingRulesPaginateResponseTypeDef",
    {
        "SamplingRuleRecords": List[
            GetSamplingRulesPaginateResponseSamplingRuleRecordsTypeDef
        ]
    },
    total=False,
)


class GetSamplingRulesPaginateResponseTypeDef(_GetSamplingRulesPaginateResponseTypeDef):
    """
    Type definition for `GetSamplingRulesPaginate` `Response`

    - **SamplingRuleRecords** *(list) --*

      Rule definitions and metadata.

      - *(dict) --*

        A  SamplingRule and its metadata.

        - **SamplingRule** *(dict) --*

          The sampling rule.

          - **RuleName** *(string) --*

            The name of the sampling rule. Specify a rule by either name or ARN, but not both.

          - **RuleARN** *(string) --*

            The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.

          - **ResourceARN** *(string) --*

            Matches the ARN of the AWS resource on which the service runs.

          - **Priority** *(integer) --*

            The priority of the sampling rule.

          - **FixedRate** *(float) --*

            The percentage of matching requests to instrument, after the reservoir is exhausted.

          - **ReservoirSize** *(integer) --*

            A fixed number of matching requests to instrument per second, prior to applying the
            fixed rate. The reservoir is not used directly by services, but applies to all services
            using the rule collectively.

          - **ServiceName** *(string) --*

            Matches the ``name`` that the service uses to identify itself in segments.

          - **ServiceType** *(string) --*

            Matches the ``origin`` that the service uses to identify its type in segments.

          - **Host** *(string) --*

            Matches the hostname from a request URL.

          - **HTTPMethod** *(string) --*

            Matches the HTTP method of a request.

          - **URLPath** *(string) --*

            Matches the path from a request URL.

          - **Version** *(integer) --*

            The version of the sampling rule format (``1`` ).

          - **Attributes** *(dict) --*

            Matches attributes derived from the request.

            - *(string) --*

              - *(string) --*

        - **CreatedAt** *(datetime) --*

          When the rule was created.

        - **ModifiedAt** *(datetime) --*

          When the rule was last modified.
    """


_GetSamplingStatisticSummariesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetSamplingStatisticSummariesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetSamplingStatisticSummariesPaginatePaginationConfigTypeDef(
    _GetSamplingStatisticSummariesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetSamplingStatisticSummariesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetSamplingStatisticSummariesPaginateResponseSamplingStatisticSummariesTypeDef = TypedDict(
    "_GetSamplingStatisticSummariesPaginateResponseSamplingStatisticSummariesTypeDef",
    {
        "RuleName": str,
        "Timestamp": datetime,
        "RequestCount": int,
        "BorrowCount": int,
        "SampledCount": int,
    },
    total=False,
)


class GetSamplingStatisticSummariesPaginateResponseSamplingStatisticSummariesTypeDef(
    _GetSamplingStatisticSummariesPaginateResponseSamplingStatisticSummariesTypeDef
):
    """
    Type definition for `GetSamplingStatisticSummariesPaginateResponse` `SamplingStatisticSummaries`

    Aggregated request sampling data for a sampling rule across all services for a 10 second
    window.

    - **RuleName** *(string) --*

      The name of the sampling rule.

    - **Timestamp** *(datetime) --*

      The start time of the reporting window.

    - **RequestCount** *(integer) --*

      The number of requests that matched the rule.

    - **BorrowCount** *(integer) --*

      The number of requests recorded with borrowed reservoir quota.

    - **SampledCount** *(integer) --*

      The number of requests recorded.
    """


_GetSamplingStatisticSummariesPaginateResponseTypeDef = TypedDict(
    "_GetSamplingStatisticSummariesPaginateResponseTypeDef",
    {
        "SamplingStatisticSummaries": List[
            GetSamplingStatisticSummariesPaginateResponseSamplingStatisticSummariesTypeDef
        ]
    },
    total=False,
)


class GetSamplingStatisticSummariesPaginateResponseTypeDef(
    _GetSamplingStatisticSummariesPaginateResponseTypeDef
):
    """
    Type definition for `GetSamplingStatisticSummariesPaginate` `Response`

    - **SamplingStatisticSummaries** *(list) --*

      Information about the number of requests instrumented for each sampling rule.

      - *(dict) --*

        Aggregated request sampling data for a sampling rule across all services for a 10 second
        window.

        - **RuleName** *(string) --*

          The name of the sampling rule.

        - **Timestamp** *(datetime) --*

          The start time of the reporting window.

        - **RequestCount** *(integer) --*

          The number of requests that matched the rule.

        - **BorrowCount** *(integer) --*

          The number of requests recorded with borrowed reservoir quota.

        - **SampledCount** *(integer) --*

          The number of requests recorded.
    """


_GetServiceGraphPaginatePaginationConfigTypeDef = TypedDict(
    "_GetServiceGraphPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetServiceGraphPaginatePaginationConfigTypeDef(
    _GetServiceGraphPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetServiceGraphPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetServiceGraphPaginateResponseServicesDurationHistogramTypeDef = TypedDict(
    "_GetServiceGraphPaginateResponseServicesDurationHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)


class GetServiceGraphPaginateResponseServicesDurationHistogramTypeDef(
    _GetServiceGraphPaginateResponseServicesDurationHistogramTypeDef
):
    """
    Type definition for `GetServiceGraphPaginateResponseServices` `DurationHistogram`

    An entry in a histogram for a statistic. A histogram maps the range of observed values
    on the X axis, and the prevalence of each value on the Y axis.

    - **Value** *(float) --*

      The value of the entry.

    - **Count** *(integer) --*

      The prevalence of the entry.
    """


_GetServiceGraphPaginateResponseServicesEdgesAliasesTypeDef = TypedDict(
    "_GetServiceGraphPaginateResponseServicesEdgesAliasesTypeDef",
    {"Name": str, "Names": List[str], "Type": str},
    total=False,
)


class GetServiceGraphPaginateResponseServicesEdgesAliasesTypeDef(
    _GetServiceGraphPaginateResponseServicesEdgesAliasesTypeDef
):
    """
    Type definition for `GetServiceGraphPaginateResponseServicesEdges` `Aliases`

    An alias for an edge.

    - **Name** *(string) --*

      The canonical name of the alias.

    - **Names** *(list) --*

      A list of names for the alias, including the canonical name.

      - *(string) --*

    - **Type** *(string) --*

      The type of the alias.
    """


_GetServiceGraphPaginateResponseServicesEdgesResponseTimeHistogramTypeDef = TypedDict(
    "_GetServiceGraphPaginateResponseServicesEdgesResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)


class GetServiceGraphPaginateResponseServicesEdgesResponseTimeHistogramTypeDef(
    _GetServiceGraphPaginateResponseServicesEdgesResponseTimeHistogramTypeDef
):
    """
    Type definition for `GetServiceGraphPaginateResponseServicesEdges` `ResponseTimeHistogram`

    An entry in a histogram for a statistic. A histogram maps the range of observed
    values on the X axis, and the prevalence of each value on the Y axis.

    - **Value** *(float) --*

      The value of the entry.

    - **Count** *(integer) --*

      The prevalence of the entry.
    """


_GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "_GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)


class GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef(
    _GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef
):
    """
    Type definition for `GetServiceGraphPaginateResponseServicesEdgesSummaryStatistics` `ErrorStatistics`

    Information about requests that failed with a 4xx Client Error status code.

    - **ThrottleCount** *(integer) --*

      The number of requests that failed with a 419 throttling status code.

    - **OtherCount** *(integer) --*

      The number of requests that failed with untracked 4xx Client Error status codes.

    - **TotalCount** *(integer) --*

      The total number of requests that failed with a 4xx Client Error status code.
    """


_GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "_GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)


class GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef(
    _GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef
):
    """
    Type definition for `GetServiceGraphPaginateResponseServicesEdgesSummaryStatistics` `FaultStatistics`

    Information about requests that failed with a 5xx Server Error status code.

    - **OtherCount** *(integer) --*

      The number of requests that failed with untracked 5xx Server Error status codes.

    - **TotalCount** *(integer) --*

      The total number of requests that failed with a 5xx Server Error status code.
    """


_GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsTypeDef = TypedDict(
    "_GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)


class GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsTypeDef(
    _GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsTypeDef
):
    """
    Type definition for `GetServiceGraphPaginateResponseServicesEdges` `SummaryStatistics`

    Response statistics for segments on the edge.

    - **OkCount** *(integer) --*

      The number of requests that completed with a 2xx Success status code.

    - **ErrorStatistics** *(dict) --*

      Information about requests that failed with a 4xx Client Error status code.

      - **ThrottleCount** *(integer) --*

        The number of requests that failed with a 419 throttling status code.

      - **OtherCount** *(integer) --*

        The number of requests that failed with untracked 4xx Client Error status codes.

      - **TotalCount** *(integer) --*

        The total number of requests that failed with a 4xx Client Error status code.

    - **FaultStatistics** *(dict) --*

      Information about requests that failed with a 5xx Server Error status code.

      - **OtherCount** *(integer) --*

        The number of requests that failed with untracked 5xx Server Error status codes.

      - **TotalCount** *(integer) --*

        The total number of requests that failed with a 5xx Server Error status code.

    - **TotalCount** *(integer) --*

      The total number of completed requests.

    - **TotalResponseTime** *(float) --*

      The aggregate response time of completed requests.
    """


_GetServiceGraphPaginateResponseServicesEdgesTypeDef = TypedDict(
    "_GetServiceGraphPaginateResponseServicesEdgesTypeDef",
    {
        "ReferenceId": int,
        "StartTime": datetime,
        "EndTime": datetime,
        "SummaryStatistics": GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsTypeDef,
        "ResponseTimeHistogram": List[
            GetServiceGraphPaginateResponseServicesEdgesResponseTimeHistogramTypeDef
        ],
        "Aliases": List[GetServiceGraphPaginateResponseServicesEdgesAliasesTypeDef],
    },
    total=False,
)


class GetServiceGraphPaginateResponseServicesEdgesTypeDef(
    _GetServiceGraphPaginateResponseServicesEdgesTypeDef
):
    """
    Type definition for `GetServiceGraphPaginateResponseServices` `Edges`

    Information about a connection between two services.

    - **ReferenceId** *(integer) --*

      Identifier of the edge. Unique within a service map.

    - **StartTime** *(datetime) --*

      The start time of the first segment on the edge.

    - **EndTime** *(datetime) --*

      The end time of the last segment on the edge.

    - **SummaryStatistics** *(dict) --*

      Response statistics for segments on the edge.

      - **OkCount** *(integer) --*

        The number of requests that completed with a 2xx Success status code.

      - **ErrorStatistics** *(dict) --*

        Information about requests that failed with a 4xx Client Error status code.

        - **ThrottleCount** *(integer) --*

          The number of requests that failed with a 419 throttling status code.

        - **OtherCount** *(integer) --*

          The number of requests that failed with untracked 4xx Client Error status codes.

        - **TotalCount** *(integer) --*

          The total number of requests that failed with a 4xx Client Error status code.

      - **FaultStatistics** *(dict) --*

        Information about requests that failed with a 5xx Server Error status code.

        - **OtherCount** *(integer) --*

          The number of requests that failed with untracked 5xx Server Error status codes.

        - **TotalCount** *(integer) --*

          The total number of requests that failed with a 5xx Server Error status code.

      - **TotalCount** *(integer) --*

        The total number of completed requests.

      - **TotalResponseTime** *(float) --*

        The aggregate response time of completed requests.

    - **ResponseTimeHistogram** *(list) --*

      A histogram that maps the spread of client response times on an edge.

      - *(dict) --*

        An entry in a histogram for a statistic. A histogram maps the range of observed
        values on the X axis, and the prevalence of each value on the Y axis.

        - **Value** *(float) --*

          The value of the entry.

        - **Count** *(integer) --*

          The prevalence of the entry.

    - **Aliases** *(list) --*

      Aliases for the edge.

      - *(dict) --*

        An alias for an edge.

        - **Name** *(string) --*

          The canonical name of the alias.

        - **Names** *(list) --*

          A list of names for the alias, including the canonical name.

          - *(string) --*

        - **Type** *(string) --*

          The type of the alias.
    """


_GetServiceGraphPaginateResponseServicesResponseTimeHistogramTypeDef = TypedDict(
    "_GetServiceGraphPaginateResponseServicesResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)


class GetServiceGraphPaginateResponseServicesResponseTimeHistogramTypeDef(
    _GetServiceGraphPaginateResponseServicesResponseTimeHistogramTypeDef
):
    """
    Type definition for `GetServiceGraphPaginateResponseServices` `ResponseTimeHistogram`

    An entry in a histogram for a statistic. A histogram maps the range of observed values
    on the X axis, and the prevalence of each value on the Y axis.

    - **Value** *(float) --*

      The value of the entry.

    - **Count** *(integer) --*

      The prevalence of the entry.
    """


_GetServiceGraphPaginateResponseServicesSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "_GetServiceGraphPaginateResponseServicesSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)


class GetServiceGraphPaginateResponseServicesSummaryStatisticsErrorStatisticsTypeDef(
    _GetServiceGraphPaginateResponseServicesSummaryStatisticsErrorStatisticsTypeDef
):
    """
    Type definition for `GetServiceGraphPaginateResponseServicesSummaryStatistics` `ErrorStatistics`

    Information about requests that failed with a 4xx Client Error status code.

    - **ThrottleCount** *(integer) --*

      The number of requests that failed with a 419 throttling status code.

    - **OtherCount** *(integer) --*

      The number of requests that failed with untracked 4xx Client Error status codes.

    - **TotalCount** *(integer) --*

      The total number of requests that failed with a 4xx Client Error status code.
    """


_GetServiceGraphPaginateResponseServicesSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "_GetServiceGraphPaginateResponseServicesSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)


class GetServiceGraphPaginateResponseServicesSummaryStatisticsFaultStatisticsTypeDef(
    _GetServiceGraphPaginateResponseServicesSummaryStatisticsFaultStatisticsTypeDef
):
    """
    Type definition for `GetServiceGraphPaginateResponseServicesSummaryStatistics` `FaultStatistics`

    Information about requests that failed with a 5xx Server Error status code.

    - **OtherCount** *(integer) --*

      The number of requests that failed with untracked 5xx Server Error status codes.

    - **TotalCount** *(integer) --*

      The total number of requests that failed with a 5xx Server Error status code.
    """


_GetServiceGraphPaginateResponseServicesSummaryStatisticsTypeDef = TypedDict(
    "_GetServiceGraphPaginateResponseServicesSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": GetServiceGraphPaginateResponseServicesSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": GetServiceGraphPaginateResponseServicesSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)


class GetServiceGraphPaginateResponseServicesSummaryStatisticsTypeDef(
    _GetServiceGraphPaginateResponseServicesSummaryStatisticsTypeDef
):
    """
    Type definition for `GetServiceGraphPaginateResponseServices` `SummaryStatistics`

    Aggregated statistics for the service.

    - **OkCount** *(integer) --*

      The number of requests that completed with a 2xx Success status code.

    - **ErrorStatistics** *(dict) --*

      Information about requests that failed with a 4xx Client Error status code.

      - **ThrottleCount** *(integer) --*

        The number of requests that failed with a 419 throttling status code.

      - **OtherCount** *(integer) --*

        The number of requests that failed with untracked 4xx Client Error status codes.

      - **TotalCount** *(integer) --*

        The total number of requests that failed with a 4xx Client Error status code.

    - **FaultStatistics** *(dict) --*

      Information about requests that failed with a 5xx Server Error status code.

      - **OtherCount** *(integer) --*

        The number of requests that failed with untracked 5xx Server Error status codes.

      - **TotalCount** *(integer) --*

        The total number of requests that failed with a 5xx Server Error status code.

    - **TotalCount** *(integer) --*

      The total number of completed requests.

    - **TotalResponseTime** *(float) --*

      The aggregate response time of completed requests.
    """


_GetServiceGraphPaginateResponseServicesTypeDef = TypedDict(
    "_GetServiceGraphPaginateResponseServicesTypeDef",
    {
        "ReferenceId": int,
        "Name": str,
        "Names": List[str],
        "Root": bool,
        "AccountId": str,
        "Type": str,
        "State": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "Edges": List[GetServiceGraphPaginateResponseServicesEdgesTypeDef],
        "SummaryStatistics": GetServiceGraphPaginateResponseServicesSummaryStatisticsTypeDef,
        "DurationHistogram": List[
            GetServiceGraphPaginateResponseServicesDurationHistogramTypeDef
        ],
        "ResponseTimeHistogram": List[
            GetServiceGraphPaginateResponseServicesResponseTimeHistogramTypeDef
        ],
    },
    total=False,
)


class GetServiceGraphPaginateResponseServicesTypeDef(
    _GetServiceGraphPaginateResponseServicesTypeDef
):
    """
    Type definition for `GetServiceGraphPaginateResponse` `Services`

    Information about an application that processed requests, users that made requests, or
    downstream services, resources and applications that an application used.

    - **ReferenceId** *(integer) --*

      Identifier for the service. Unique within the service map.

    - **Name** *(string) --*

      The canonical name of the service.

    - **Names** *(list) --*

      A list of names for the service, including the canonical name.

      - *(string) --*

    - **Root** *(boolean) --*

      Indicates that the service was the first service to process a request.

    - **AccountId** *(string) --*

      Identifier of the AWS account in which the service runs.

    - **Type** *(string) --*

      The type of service.

      * AWS Resource - The type of an AWS resource. For example, ``AWS::EC2::Instance`` for a
      application running on Amazon EC2 or ``AWS::DynamoDB::Table`` for an Amazon DynamoDB
      table that the application used.

      * AWS Service - The type of an AWS service. For example, ``AWS::DynamoDB`` for downstream
      calls to Amazon DynamoDB that didn't target a specific table.

      * ``client`` - Represents the clients that sent requests to a root service.

      * ``remote`` - A downstream service of indeterminate type.

    - **State** *(string) --*

      The service's state.

    - **StartTime** *(datetime) --*

      The start time of the first segment that the service generated.

    - **EndTime** *(datetime) --*

      The end time of the last segment that the service generated.

    - **Edges** *(list) --*

      Connections to downstream services.

      - *(dict) --*

        Information about a connection between two services.

        - **ReferenceId** *(integer) --*

          Identifier of the edge. Unique within a service map.

        - **StartTime** *(datetime) --*

          The start time of the first segment on the edge.

        - **EndTime** *(datetime) --*

          The end time of the last segment on the edge.

        - **SummaryStatistics** *(dict) --*

          Response statistics for segments on the edge.

          - **OkCount** *(integer) --*

            The number of requests that completed with a 2xx Success status code.

          - **ErrorStatistics** *(dict) --*

            Information about requests that failed with a 4xx Client Error status code.

            - **ThrottleCount** *(integer) --*

              The number of requests that failed with a 419 throttling status code.

            - **OtherCount** *(integer) --*

              The number of requests that failed with untracked 4xx Client Error status codes.

            - **TotalCount** *(integer) --*

              The total number of requests that failed with a 4xx Client Error status code.

          - **FaultStatistics** *(dict) --*

            Information about requests that failed with a 5xx Server Error status code.

            - **OtherCount** *(integer) --*

              The number of requests that failed with untracked 5xx Server Error status codes.

            - **TotalCount** *(integer) --*

              The total number of requests that failed with a 5xx Server Error status code.

          - **TotalCount** *(integer) --*

            The total number of completed requests.

          - **TotalResponseTime** *(float) --*

            The aggregate response time of completed requests.

        - **ResponseTimeHistogram** *(list) --*

          A histogram that maps the spread of client response times on an edge.

          - *(dict) --*

            An entry in a histogram for a statistic. A histogram maps the range of observed
            values on the X axis, and the prevalence of each value on the Y axis.

            - **Value** *(float) --*

              The value of the entry.

            - **Count** *(integer) --*

              The prevalence of the entry.

        - **Aliases** *(list) --*

          Aliases for the edge.

          - *(dict) --*

            An alias for an edge.

            - **Name** *(string) --*

              The canonical name of the alias.

            - **Names** *(list) --*

              A list of names for the alias, including the canonical name.

              - *(string) --*

            - **Type** *(string) --*

              The type of the alias.

    - **SummaryStatistics** *(dict) --*

      Aggregated statistics for the service.

      - **OkCount** *(integer) --*

        The number of requests that completed with a 2xx Success status code.

      - **ErrorStatistics** *(dict) --*

        Information about requests that failed with a 4xx Client Error status code.

        - **ThrottleCount** *(integer) --*

          The number of requests that failed with a 419 throttling status code.

        - **OtherCount** *(integer) --*

          The number of requests that failed with untracked 4xx Client Error status codes.

        - **TotalCount** *(integer) --*

          The total number of requests that failed with a 4xx Client Error status code.

      - **FaultStatistics** *(dict) --*

        Information about requests that failed with a 5xx Server Error status code.

        - **OtherCount** *(integer) --*

          The number of requests that failed with untracked 5xx Server Error status codes.

        - **TotalCount** *(integer) --*

          The total number of requests that failed with a 5xx Server Error status code.

      - **TotalCount** *(integer) --*

        The total number of completed requests.

      - **TotalResponseTime** *(float) --*

        The aggregate response time of completed requests.

    - **DurationHistogram** *(list) --*

      A histogram that maps the spread of service durations.

      - *(dict) --*

        An entry in a histogram for a statistic. A histogram maps the range of observed values
        on the X axis, and the prevalence of each value on the Y axis.

        - **Value** *(float) --*

          The value of the entry.

        - **Count** *(integer) --*

          The prevalence of the entry.

    - **ResponseTimeHistogram** *(list) --*

      A histogram that maps the spread of service response times.

      - *(dict) --*

        An entry in a histogram for a statistic. A histogram maps the range of observed values
        on the X axis, and the prevalence of each value on the Y axis.

        - **Value** *(float) --*

          The value of the entry.

        - **Count** *(integer) --*

          The prevalence of the entry.
    """


_GetServiceGraphPaginateResponseTypeDef = TypedDict(
    "_GetServiceGraphPaginateResponseTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "Services": List[GetServiceGraphPaginateResponseServicesTypeDef],
        "ContainsOldGroupVersions": bool,
    },
    total=False,
)


class GetServiceGraphPaginateResponseTypeDef(_GetServiceGraphPaginateResponseTypeDef):
    """
    Type definition for `GetServiceGraphPaginate` `Response`

    - **StartTime** *(datetime) --*

      The start of the time frame for which the graph was generated.

    - **EndTime** *(datetime) --*

      The end of the time frame for which the graph was generated.

    - **Services** *(list) --*

      The services that have processed a traced request during the specified time frame.

      - *(dict) --*

        Information about an application that processed requests, users that made requests, or
        downstream services, resources and applications that an application used.

        - **ReferenceId** *(integer) --*

          Identifier for the service. Unique within the service map.

        - **Name** *(string) --*

          The canonical name of the service.

        - **Names** *(list) --*

          A list of names for the service, including the canonical name.

          - *(string) --*

        - **Root** *(boolean) --*

          Indicates that the service was the first service to process a request.

        - **AccountId** *(string) --*

          Identifier of the AWS account in which the service runs.

        - **Type** *(string) --*

          The type of service.

          * AWS Resource - The type of an AWS resource. For example, ``AWS::EC2::Instance`` for a
          application running on Amazon EC2 or ``AWS::DynamoDB::Table`` for an Amazon DynamoDB
          table that the application used.

          * AWS Service - The type of an AWS service. For example, ``AWS::DynamoDB`` for downstream
          calls to Amazon DynamoDB that didn't target a specific table.

          * ``client`` - Represents the clients that sent requests to a root service.

          * ``remote`` - A downstream service of indeterminate type.

        - **State** *(string) --*

          The service's state.

        - **StartTime** *(datetime) --*

          The start time of the first segment that the service generated.

        - **EndTime** *(datetime) --*

          The end time of the last segment that the service generated.

        - **Edges** *(list) --*

          Connections to downstream services.

          - *(dict) --*

            Information about a connection between two services.

            - **ReferenceId** *(integer) --*

              Identifier of the edge. Unique within a service map.

            - **StartTime** *(datetime) --*

              The start time of the first segment on the edge.

            - **EndTime** *(datetime) --*

              The end time of the last segment on the edge.

            - **SummaryStatistics** *(dict) --*

              Response statistics for segments on the edge.

              - **OkCount** *(integer) --*

                The number of requests that completed with a 2xx Success status code.

              - **ErrorStatistics** *(dict) --*

                Information about requests that failed with a 4xx Client Error status code.

                - **ThrottleCount** *(integer) --*

                  The number of requests that failed with a 419 throttling status code.

                - **OtherCount** *(integer) --*

                  The number of requests that failed with untracked 4xx Client Error status codes.

                - **TotalCount** *(integer) --*

                  The total number of requests that failed with a 4xx Client Error status code.

              - **FaultStatistics** *(dict) --*

                Information about requests that failed with a 5xx Server Error status code.

                - **OtherCount** *(integer) --*

                  The number of requests that failed with untracked 5xx Server Error status codes.

                - **TotalCount** *(integer) --*

                  The total number of requests that failed with a 5xx Server Error status code.

              - **TotalCount** *(integer) --*

                The total number of completed requests.

              - **TotalResponseTime** *(float) --*

                The aggregate response time of completed requests.

            - **ResponseTimeHistogram** *(list) --*

              A histogram that maps the spread of client response times on an edge.

              - *(dict) --*

                An entry in a histogram for a statistic. A histogram maps the range of observed
                values on the X axis, and the prevalence of each value on the Y axis.

                - **Value** *(float) --*

                  The value of the entry.

                - **Count** *(integer) --*

                  The prevalence of the entry.

            - **Aliases** *(list) --*

              Aliases for the edge.

              - *(dict) --*

                An alias for an edge.

                - **Name** *(string) --*

                  The canonical name of the alias.

                - **Names** *(list) --*

                  A list of names for the alias, including the canonical name.

                  - *(string) --*

                - **Type** *(string) --*

                  The type of the alias.

        - **SummaryStatistics** *(dict) --*

          Aggregated statistics for the service.

          - **OkCount** *(integer) --*

            The number of requests that completed with a 2xx Success status code.

          - **ErrorStatistics** *(dict) --*

            Information about requests that failed with a 4xx Client Error status code.

            - **ThrottleCount** *(integer) --*

              The number of requests that failed with a 419 throttling status code.

            - **OtherCount** *(integer) --*

              The number of requests that failed with untracked 4xx Client Error status codes.

            - **TotalCount** *(integer) --*

              The total number of requests that failed with a 4xx Client Error status code.

          - **FaultStatistics** *(dict) --*

            Information about requests that failed with a 5xx Server Error status code.

            - **OtherCount** *(integer) --*

              The number of requests that failed with untracked 5xx Server Error status codes.

            - **TotalCount** *(integer) --*

              The total number of requests that failed with a 5xx Server Error status code.

          - **TotalCount** *(integer) --*

            The total number of completed requests.

          - **TotalResponseTime** *(float) --*

            The aggregate response time of completed requests.

        - **DurationHistogram** *(list) --*

          A histogram that maps the spread of service durations.

          - *(dict) --*

            An entry in a histogram for a statistic. A histogram maps the range of observed values
            on the X axis, and the prevalence of each value on the Y axis.

            - **Value** *(float) --*

              The value of the entry.

            - **Count** *(integer) --*

              The prevalence of the entry.

        - **ResponseTimeHistogram** *(list) --*

          A histogram that maps the spread of service response times.

          - *(dict) --*

            An entry in a histogram for a statistic. A histogram maps the range of observed values
            on the X axis, and the prevalence of each value on the Y axis.

            - **Value** *(float) --*

              The value of the entry.

            - **Count** *(integer) --*

              The prevalence of the entry.

    - **ContainsOldGroupVersions** *(boolean) --*

      A flag indicating whether the group's filter expression has been consistent, or if the
      returned service graph may show traces from an older version of the group's filter expression.
    """


_GetTimeSeriesServiceStatisticsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetTimeSeriesServiceStatisticsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetTimeSeriesServiceStatisticsPaginatePaginationConfigTypeDef(
    _GetTimeSeriesServiceStatisticsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetTimeSeriesServiceStatisticsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "_GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)


class GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef(
    _GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef
):
    """
    Type definition for `GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatistics` `ErrorStatistics`

    Information about requests that failed with a 4xx Client Error status code.

    - **ThrottleCount** *(integer) --*

      The number of requests that failed with a 419 throttling status code.

    - **OtherCount** *(integer) --*

      The number of requests that failed with untracked 4xx Client Error status codes.

    - **TotalCount** *(integer) --*

      The total number of requests that failed with a 4xx Client Error status code.
    """


_GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "_GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)


class GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef(
    _GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef
):
    """
    Type definition for `GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatistics` `FaultStatistics`

    Information about requests that failed with a 5xx Server Error status code.

    - **OtherCount** *(integer) --*

      The number of requests that failed with untracked 5xx Server Error status codes.

    - **TotalCount** *(integer) --*

      The total number of requests that failed with a 5xx Server Error status code.
    """


_GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsTypeDef = TypedDict(
    "_GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)


class GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsTypeDef(
    _GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsTypeDef
):
    """
    Type definition for `GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatistics` `EdgeSummaryStatistics`

    Response statistics for an edge.

    - **OkCount** *(integer) --*

      The number of requests that completed with a 2xx Success status code.

    - **ErrorStatistics** *(dict) --*

      Information about requests that failed with a 4xx Client Error status code.

      - **ThrottleCount** *(integer) --*

        The number of requests that failed with a 419 throttling status code.

      - **OtherCount** *(integer) --*

        The number of requests that failed with untracked 4xx Client Error status codes.

      - **TotalCount** *(integer) --*

        The total number of requests that failed with a 4xx Client Error status code.

    - **FaultStatistics** *(dict) --*

      Information about requests that failed with a 5xx Server Error status code.

      - **OtherCount** *(integer) --*

        The number of requests that failed with untracked 5xx Server Error status codes.

      - **TotalCount** *(integer) --*

        The total number of requests that failed with a 5xx Server Error status code.

    - **TotalCount** *(integer) --*

      The total number of completed requests.

    - **TotalResponseTime** *(float) --*

      The aggregate response time of completed requests.
    """


_GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsResponseTimeHistogramTypeDef = TypedDict(
    "_GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)


class GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsResponseTimeHistogramTypeDef(
    _GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsResponseTimeHistogramTypeDef
):
    """
    Type definition for `GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatistics` `ResponseTimeHistogram`

    An entry in a histogram for a statistic. A histogram maps the range of observed values
    on the X axis, and the prevalence of each value on the Y axis.

    - **Value** *(float) --*

      The value of the entry.

    - **Count** *(integer) --*

      The prevalence of the entry.
    """


_GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "_GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)


class GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef(
    _GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef
):
    """
    Type definition for `GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatistics` `ErrorStatistics`

    Information about requests that failed with a 4xx Client Error status code.

    - **ThrottleCount** *(integer) --*

      The number of requests that failed with a 419 throttling status code.

    - **OtherCount** *(integer) --*

      The number of requests that failed with untracked 4xx Client Error status codes.

    - **TotalCount** *(integer) --*

      The total number of requests that failed with a 4xx Client Error status code.
    """


_GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "_GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)


class GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef(
    _GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef
):
    """
    Type definition for `GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatistics` `FaultStatistics`

    Information about requests that failed with a 5xx Server Error status code.

    - **OtherCount** *(integer) --*

      The number of requests that failed with untracked 5xx Server Error status codes.

    - **TotalCount** *(integer) --*

      The total number of requests that failed with a 5xx Server Error status code.
    """


_GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsTypeDef = TypedDict(
    "_GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)


class GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsTypeDef(
    _GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsTypeDef
):
    """
    Type definition for `GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatistics` `ServiceSummaryStatistics`

    Response statistics for a service.

    - **OkCount** *(integer) --*

      The number of requests that completed with a 2xx Success status code.

    - **ErrorStatistics** *(dict) --*

      Information about requests that failed with a 4xx Client Error status code.

      - **ThrottleCount** *(integer) --*

        The number of requests that failed with a 419 throttling status code.

      - **OtherCount** *(integer) --*

        The number of requests that failed with untracked 4xx Client Error status codes.

      - **TotalCount** *(integer) --*

        The total number of requests that failed with a 4xx Client Error status code.

    - **FaultStatistics** *(dict) --*

      Information about requests that failed with a 5xx Server Error status code.

      - **OtherCount** *(integer) --*

        The number of requests that failed with untracked 5xx Server Error status codes.

      - **TotalCount** *(integer) --*

        The total number of requests that failed with a 5xx Server Error status code.

    - **TotalCount** *(integer) --*

      The total number of completed requests.

    - **TotalResponseTime** *(float) --*

      The aggregate response time of completed requests.
    """


_GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsTypeDef = TypedDict(
    "_GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsTypeDef",
    {
        "Timestamp": datetime,
        "EdgeSummaryStatistics": GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsTypeDef,
        "ServiceSummaryStatistics": GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsTypeDef,
        "ResponseTimeHistogram": List[
            GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsResponseTimeHistogramTypeDef
        ],
    },
    total=False,
)


class GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsTypeDef(
    _GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsTypeDef
):
    """
    Type definition for `GetTimeSeriesServiceStatisticsPaginateResponse` `TimeSeriesServiceStatistics`

    A list of TimeSeriesStatistic structures.

    - **Timestamp** *(datetime) --*

      Timestamp of the window for which statistics are aggregated.

    - **EdgeSummaryStatistics** *(dict) --*

      Response statistics for an edge.

      - **OkCount** *(integer) --*

        The number of requests that completed with a 2xx Success status code.

      - **ErrorStatistics** *(dict) --*

        Information about requests that failed with a 4xx Client Error status code.

        - **ThrottleCount** *(integer) --*

          The number of requests that failed with a 419 throttling status code.

        - **OtherCount** *(integer) --*

          The number of requests that failed with untracked 4xx Client Error status codes.

        - **TotalCount** *(integer) --*

          The total number of requests that failed with a 4xx Client Error status code.

      - **FaultStatistics** *(dict) --*

        Information about requests that failed with a 5xx Server Error status code.

        - **OtherCount** *(integer) --*

          The number of requests that failed with untracked 5xx Server Error status codes.

        - **TotalCount** *(integer) --*

          The total number of requests that failed with a 5xx Server Error status code.

      - **TotalCount** *(integer) --*

        The total number of completed requests.

      - **TotalResponseTime** *(float) --*

        The aggregate response time of completed requests.

    - **ServiceSummaryStatistics** *(dict) --*

      Response statistics for a service.

      - **OkCount** *(integer) --*

        The number of requests that completed with a 2xx Success status code.

      - **ErrorStatistics** *(dict) --*

        Information about requests that failed with a 4xx Client Error status code.

        - **ThrottleCount** *(integer) --*

          The number of requests that failed with a 419 throttling status code.

        - **OtherCount** *(integer) --*

          The number of requests that failed with untracked 4xx Client Error status codes.

        - **TotalCount** *(integer) --*

          The total number of requests that failed with a 4xx Client Error status code.

      - **FaultStatistics** *(dict) --*

        Information about requests that failed with a 5xx Server Error status code.

        - **OtherCount** *(integer) --*

          The number of requests that failed with untracked 5xx Server Error status codes.

        - **TotalCount** *(integer) --*

          The total number of requests that failed with a 5xx Server Error status code.

      - **TotalCount** *(integer) --*

        The total number of completed requests.

      - **TotalResponseTime** *(float) --*

        The aggregate response time of completed requests.

    - **ResponseTimeHistogram** *(list) --*

      The response time histogram for the selected entities.

      - *(dict) --*

        An entry in a histogram for a statistic. A histogram maps the range of observed values
        on the X axis, and the prevalence of each value on the Y axis.

        - **Value** *(float) --*

          The value of the entry.

        - **Count** *(integer) --*

          The prevalence of the entry.
    """


_GetTimeSeriesServiceStatisticsPaginateResponseTypeDef = TypedDict(
    "_GetTimeSeriesServiceStatisticsPaginateResponseTypeDef",
    {
        "TimeSeriesServiceStatistics": List[
            GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsTypeDef
        ],
        "ContainsOldGroupVersions": bool,
    },
    total=False,
)


class GetTimeSeriesServiceStatisticsPaginateResponseTypeDef(
    _GetTimeSeriesServiceStatisticsPaginateResponseTypeDef
):
    """
    Type definition for `GetTimeSeriesServiceStatisticsPaginate` `Response`

    - **TimeSeriesServiceStatistics** *(list) --*

      The collection of statistics.

      - *(dict) --*

        A list of TimeSeriesStatistic structures.

        - **Timestamp** *(datetime) --*

          Timestamp of the window for which statistics are aggregated.

        - **EdgeSummaryStatistics** *(dict) --*

          Response statistics for an edge.

          - **OkCount** *(integer) --*

            The number of requests that completed with a 2xx Success status code.

          - **ErrorStatistics** *(dict) --*

            Information about requests that failed with a 4xx Client Error status code.

            - **ThrottleCount** *(integer) --*

              The number of requests that failed with a 419 throttling status code.

            - **OtherCount** *(integer) --*

              The number of requests that failed with untracked 4xx Client Error status codes.

            - **TotalCount** *(integer) --*

              The total number of requests that failed with a 4xx Client Error status code.

          - **FaultStatistics** *(dict) --*

            Information about requests that failed with a 5xx Server Error status code.

            - **OtherCount** *(integer) --*

              The number of requests that failed with untracked 5xx Server Error status codes.

            - **TotalCount** *(integer) --*

              The total number of requests that failed with a 5xx Server Error status code.

          - **TotalCount** *(integer) --*

            The total number of completed requests.

          - **TotalResponseTime** *(float) --*

            The aggregate response time of completed requests.

        - **ServiceSummaryStatistics** *(dict) --*

          Response statistics for a service.

          - **OkCount** *(integer) --*

            The number of requests that completed with a 2xx Success status code.

          - **ErrorStatistics** *(dict) --*

            Information about requests that failed with a 4xx Client Error status code.

            - **ThrottleCount** *(integer) --*

              The number of requests that failed with a 419 throttling status code.

            - **OtherCount** *(integer) --*

              The number of requests that failed with untracked 4xx Client Error status codes.

            - **TotalCount** *(integer) --*

              The total number of requests that failed with a 4xx Client Error status code.

          - **FaultStatistics** *(dict) --*

            Information about requests that failed with a 5xx Server Error status code.

            - **OtherCount** *(integer) --*

              The number of requests that failed with untracked 5xx Server Error status codes.

            - **TotalCount** *(integer) --*

              The total number of requests that failed with a 5xx Server Error status code.

          - **TotalCount** *(integer) --*

            The total number of completed requests.

          - **TotalResponseTime** *(float) --*

            The aggregate response time of completed requests.

        - **ResponseTimeHistogram** *(list) --*

          The response time histogram for the selected entities.

          - *(dict) --*

            An entry in a histogram for a statistic. A histogram maps the range of observed values
            on the X axis, and the prevalence of each value on the Y axis.

            - **Value** *(float) --*

              The value of the entry.

            - **Count** *(integer) --*

              The prevalence of the entry.

    - **ContainsOldGroupVersions** *(boolean) --*

      A flag indicating whether or not a group's filter expression has been consistent, or if a
      returned aggregation may show statistics from an older version of the group's filter
      expression.
    """


_GetTraceGraphPaginatePaginationConfigTypeDef = TypedDict(
    "_GetTraceGraphPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetTraceGraphPaginatePaginationConfigTypeDef(
    _GetTraceGraphPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetTraceGraphPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetTraceGraphPaginateResponseServicesDurationHistogramTypeDef = TypedDict(
    "_GetTraceGraphPaginateResponseServicesDurationHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)


class GetTraceGraphPaginateResponseServicesDurationHistogramTypeDef(
    _GetTraceGraphPaginateResponseServicesDurationHistogramTypeDef
):
    """
    Type definition for `GetTraceGraphPaginateResponseServices` `DurationHistogram`

    An entry in a histogram for a statistic. A histogram maps the range of observed values
    on the X axis, and the prevalence of each value on the Y axis.

    - **Value** *(float) --*

      The value of the entry.

    - **Count** *(integer) --*

      The prevalence of the entry.
    """


_GetTraceGraphPaginateResponseServicesEdgesAliasesTypeDef = TypedDict(
    "_GetTraceGraphPaginateResponseServicesEdgesAliasesTypeDef",
    {"Name": str, "Names": List[str], "Type": str},
    total=False,
)


class GetTraceGraphPaginateResponseServicesEdgesAliasesTypeDef(
    _GetTraceGraphPaginateResponseServicesEdgesAliasesTypeDef
):
    """
    Type definition for `GetTraceGraphPaginateResponseServicesEdges` `Aliases`

    An alias for an edge.

    - **Name** *(string) --*

      The canonical name of the alias.

    - **Names** *(list) --*

      A list of names for the alias, including the canonical name.

      - *(string) --*

    - **Type** *(string) --*

      The type of the alias.
    """


_GetTraceGraphPaginateResponseServicesEdgesResponseTimeHistogramTypeDef = TypedDict(
    "_GetTraceGraphPaginateResponseServicesEdgesResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)


class GetTraceGraphPaginateResponseServicesEdgesResponseTimeHistogramTypeDef(
    _GetTraceGraphPaginateResponseServicesEdgesResponseTimeHistogramTypeDef
):
    """
    Type definition for `GetTraceGraphPaginateResponseServicesEdges` `ResponseTimeHistogram`

    An entry in a histogram for a statistic. A histogram maps the range of observed
    values on the X axis, and the prevalence of each value on the Y axis.

    - **Value** *(float) --*

      The value of the entry.

    - **Count** *(integer) --*

      The prevalence of the entry.
    """


_GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "_GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)


class GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef(
    _GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef
):
    """
    Type definition for `GetTraceGraphPaginateResponseServicesEdgesSummaryStatistics` `ErrorStatistics`

    Information about requests that failed with a 4xx Client Error status code.

    - **ThrottleCount** *(integer) --*

      The number of requests that failed with a 419 throttling status code.

    - **OtherCount** *(integer) --*

      The number of requests that failed with untracked 4xx Client Error status codes.

    - **TotalCount** *(integer) --*

      The total number of requests that failed with a 4xx Client Error status code.
    """


_GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "_GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)


class GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef(
    _GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef
):
    """
    Type definition for `GetTraceGraphPaginateResponseServicesEdgesSummaryStatistics` `FaultStatistics`

    Information about requests that failed with a 5xx Server Error status code.

    - **OtherCount** *(integer) --*

      The number of requests that failed with untracked 5xx Server Error status codes.

    - **TotalCount** *(integer) --*

      The total number of requests that failed with a 5xx Server Error status code.
    """


_GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsTypeDef = TypedDict(
    "_GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)


class GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsTypeDef(
    _GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsTypeDef
):
    """
    Type definition for `GetTraceGraphPaginateResponseServicesEdges` `SummaryStatistics`

    Response statistics for segments on the edge.

    - **OkCount** *(integer) --*

      The number of requests that completed with a 2xx Success status code.

    - **ErrorStatistics** *(dict) --*

      Information about requests that failed with a 4xx Client Error status code.

      - **ThrottleCount** *(integer) --*

        The number of requests that failed with a 419 throttling status code.

      - **OtherCount** *(integer) --*

        The number of requests that failed with untracked 4xx Client Error status codes.

      - **TotalCount** *(integer) --*

        The total number of requests that failed with a 4xx Client Error status code.

    - **FaultStatistics** *(dict) --*

      Information about requests that failed with a 5xx Server Error status code.

      - **OtherCount** *(integer) --*

        The number of requests that failed with untracked 5xx Server Error status codes.

      - **TotalCount** *(integer) --*

        The total number of requests that failed with a 5xx Server Error status code.

    - **TotalCount** *(integer) --*

      The total number of completed requests.

    - **TotalResponseTime** *(float) --*

      The aggregate response time of completed requests.
    """


_GetTraceGraphPaginateResponseServicesEdgesTypeDef = TypedDict(
    "_GetTraceGraphPaginateResponseServicesEdgesTypeDef",
    {
        "ReferenceId": int,
        "StartTime": datetime,
        "EndTime": datetime,
        "SummaryStatistics": GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsTypeDef,
        "ResponseTimeHistogram": List[
            GetTraceGraphPaginateResponseServicesEdgesResponseTimeHistogramTypeDef
        ],
        "Aliases": List[GetTraceGraphPaginateResponseServicesEdgesAliasesTypeDef],
    },
    total=False,
)


class GetTraceGraphPaginateResponseServicesEdgesTypeDef(
    _GetTraceGraphPaginateResponseServicesEdgesTypeDef
):
    """
    Type definition for `GetTraceGraphPaginateResponseServices` `Edges`

    Information about a connection between two services.

    - **ReferenceId** *(integer) --*

      Identifier of the edge. Unique within a service map.

    - **StartTime** *(datetime) --*

      The start time of the first segment on the edge.

    - **EndTime** *(datetime) --*

      The end time of the last segment on the edge.

    - **SummaryStatistics** *(dict) --*

      Response statistics for segments on the edge.

      - **OkCount** *(integer) --*

        The number of requests that completed with a 2xx Success status code.

      - **ErrorStatistics** *(dict) --*

        Information about requests that failed with a 4xx Client Error status code.

        - **ThrottleCount** *(integer) --*

          The number of requests that failed with a 419 throttling status code.

        - **OtherCount** *(integer) --*

          The number of requests that failed with untracked 4xx Client Error status codes.

        - **TotalCount** *(integer) --*

          The total number of requests that failed with a 4xx Client Error status code.

      - **FaultStatistics** *(dict) --*

        Information about requests that failed with a 5xx Server Error status code.

        - **OtherCount** *(integer) --*

          The number of requests that failed with untracked 5xx Server Error status codes.

        - **TotalCount** *(integer) --*

          The total number of requests that failed with a 5xx Server Error status code.

      - **TotalCount** *(integer) --*

        The total number of completed requests.

      - **TotalResponseTime** *(float) --*

        The aggregate response time of completed requests.

    - **ResponseTimeHistogram** *(list) --*

      A histogram that maps the spread of client response times on an edge.

      - *(dict) --*

        An entry in a histogram for a statistic. A histogram maps the range of observed
        values on the X axis, and the prevalence of each value on the Y axis.

        - **Value** *(float) --*

          The value of the entry.

        - **Count** *(integer) --*

          The prevalence of the entry.

    - **Aliases** *(list) --*

      Aliases for the edge.

      - *(dict) --*

        An alias for an edge.

        - **Name** *(string) --*

          The canonical name of the alias.

        - **Names** *(list) --*

          A list of names for the alias, including the canonical name.

          - *(string) --*

        - **Type** *(string) --*

          The type of the alias.
    """


_GetTraceGraphPaginateResponseServicesResponseTimeHistogramTypeDef = TypedDict(
    "_GetTraceGraphPaginateResponseServicesResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)


class GetTraceGraphPaginateResponseServicesResponseTimeHistogramTypeDef(
    _GetTraceGraphPaginateResponseServicesResponseTimeHistogramTypeDef
):
    """
    Type definition for `GetTraceGraphPaginateResponseServices` `ResponseTimeHistogram`

    An entry in a histogram for a statistic. A histogram maps the range of observed values
    on the X axis, and the prevalence of each value on the Y axis.

    - **Value** *(float) --*

      The value of the entry.

    - **Count** *(integer) --*

      The prevalence of the entry.
    """


_GetTraceGraphPaginateResponseServicesSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "_GetTraceGraphPaginateResponseServicesSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)


class GetTraceGraphPaginateResponseServicesSummaryStatisticsErrorStatisticsTypeDef(
    _GetTraceGraphPaginateResponseServicesSummaryStatisticsErrorStatisticsTypeDef
):
    """
    Type definition for `GetTraceGraphPaginateResponseServicesSummaryStatistics` `ErrorStatistics`

    Information about requests that failed with a 4xx Client Error status code.

    - **ThrottleCount** *(integer) --*

      The number of requests that failed with a 419 throttling status code.

    - **OtherCount** *(integer) --*

      The number of requests that failed with untracked 4xx Client Error status codes.

    - **TotalCount** *(integer) --*

      The total number of requests that failed with a 4xx Client Error status code.
    """


_GetTraceGraphPaginateResponseServicesSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "_GetTraceGraphPaginateResponseServicesSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)


class GetTraceGraphPaginateResponseServicesSummaryStatisticsFaultStatisticsTypeDef(
    _GetTraceGraphPaginateResponseServicesSummaryStatisticsFaultStatisticsTypeDef
):
    """
    Type definition for `GetTraceGraphPaginateResponseServicesSummaryStatistics` `FaultStatistics`

    Information about requests that failed with a 5xx Server Error status code.

    - **OtherCount** *(integer) --*

      The number of requests that failed with untracked 5xx Server Error status codes.

    - **TotalCount** *(integer) --*

      The total number of requests that failed with a 5xx Server Error status code.
    """


_GetTraceGraphPaginateResponseServicesSummaryStatisticsTypeDef = TypedDict(
    "_GetTraceGraphPaginateResponseServicesSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": GetTraceGraphPaginateResponseServicesSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": GetTraceGraphPaginateResponseServicesSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)


class GetTraceGraphPaginateResponseServicesSummaryStatisticsTypeDef(
    _GetTraceGraphPaginateResponseServicesSummaryStatisticsTypeDef
):
    """
    Type definition for `GetTraceGraphPaginateResponseServices` `SummaryStatistics`

    Aggregated statistics for the service.

    - **OkCount** *(integer) --*

      The number of requests that completed with a 2xx Success status code.

    - **ErrorStatistics** *(dict) --*

      Information about requests that failed with a 4xx Client Error status code.

      - **ThrottleCount** *(integer) --*

        The number of requests that failed with a 419 throttling status code.

      - **OtherCount** *(integer) --*

        The number of requests that failed with untracked 4xx Client Error status codes.

      - **TotalCount** *(integer) --*

        The total number of requests that failed with a 4xx Client Error status code.

    - **FaultStatistics** *(dict) --*

      Information about requests that failed with a 5xx Server Error status code.

      - **OtherCount** *(integer) --*

        The number of requests that failed with untracked 5xx Server Error status codes.

      - **TotalCount** *(integer) --*

        The total number of requests that failed with a 5xx Server Error status code.

    - **TotalCount** *(integer) --*

      The total number of completed requests.

    - **TotalResponseTime** *(float) --*

      The aggregate response time of completed requests.
    """


_GetTraceGraphPaginateResponseServicesTypeDef = TypedDict(
    "_GetTraceGraphPaginateResponseServicesTypeDef",
    {
        "ReferenceId": int,
        "Name": str,
        "Names": List[str],
        "Root": bool,
        "AccountId": str,
        "Type": str,
        "State": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "Edges": List[GetTraceGraphPaginateResponseServicesEdgesTypeDef],
        "SummaryStatistics": GetTraceGraphPaginateResponseServicesSummaryStatisticsTypeDef,
        "DurationHistogram": List[
            GetTraceGraphPaginateResponseServicesDurationHistogramTypeDef
        ],
        "ResponseTimeHistogram": List[
            GetTraceGraphPaginateResponseServicesResponseTimeHistogramTypeDef
        ],
    },
    total=False,
)


class GetTraceGraphPaginateResponseServicesTypeDef(
    _GetTraceGraphPaginateResponseServicesTypeDef
):
    """
    Type definition for `GetTraceGraphPaginateResponse` `Services`

    Information about an application that processed requests, users that made requests, or
    downstream services, resources and applications that an application used.

    - **ReferenceId** *(integer) --*

      Identifier for the service. Unique within the service map.

    - **Name** *(string) --*

      The canonical name of the service.

    - **Names** *(list) --*

      A list of names for the service, including the canonical name.

      - *(string) --*

    - **Root** *(boolean) --*

      Indicates that the service was the first service to process a request.

    - **AccountId** *(string) --*

      Identifier of the AWS account in which the service runs.

    - **Type** *(string) --*

      The type of service.

      * AWS Resource - The type of an AWS resource. For example, ``AWS::EC2::Instance`` for a
      application running on Amazon EC2 or ``AWS::DynamoDB::Table`` for an Amazon DynamoDB
      table that the application used.

      * AWS Service - The type of an AWS service. For example, ``AWS::DynamoDB`` for downstream
      calls to Amazon DynamoDB that didn't target a specific table.

      * ``client`` - Represents the clients that sent requests to a root service.

      * ``remote`` - A downstream service of indeterminate type.

    - **State** *(string) --*

      The service's state.

    - **StartTime** *(datetime) --*

      The start time of the first segment that the service generated.

    - **EndTime** *(datetime) --*

      The end time of the last segment that the service generated.

    - **Edges** *(list) --*

      Connections to downstream services.

      - *(dict) --*

        Information about a connection between two services.

        - **ReferenceId** *(integer) --*

          Identifier of the edge. Unique within a service map.

        - **StartTime** *(datetime) --*

          The start time of the first segment on the edge.

        - **EndTime** *(datetime) --*

          The end time of the last segment on the edge.

        - **SummaryStatistics** *(dict) --*

          Response statistics for segments on the edge.

          - **OkCount** *(integer) --*

            The number of requests that completed with a 2xx Success status code.

          - **ErrorStatistics** *(dict) --*

            Information about requests that failed with a 4xx Client Error status code.

            - **ThrottleCount** *(integer) --*

              The number of requests that failed with a 419 throttling status code.

            - **OtherCount** *(integer) --*

              The number of requests that failed with untracked 4xx Client Error status codes.

            - **TotalCount** *(integer) --*

              The total number of requests that failed with a 4xx Client Error status code.

          - **FaultStatistics** *(dict) --*

            Information about requests that failed with a 5xx Server Error status code.

            - **OtherCount** *(integer) --*

              The number of requests that failed with untracked 5xx Server Error status codes.

            - **TotalCount** *(integer) --*

              The total number of requests that failed with a 5xx Server Error status code.

          - **TotalCount** *(integer) --*

            The total number of completed requests.

          - **TotalResponseTime** *(float) --*

            The aggregate response time of completed requests.

        - **ResponseTimeHistogram** *(list) --*

          A histogram that maps the spread of client response times on an edge.

          - *(dict) --*

            An entry in a histogram for a statistic. A histogram maps the range of observed
            values on the X axis, and the prevalence of each value on the Y axis.

            - **Value** *(float) --*

              The value of the entry.

            - **Count** *(integer) --*

              The prevalence of the entry.

        - **Aliases** *(list) --*

          Aliases for the edge.

          - *(dict) --*

            An alias for an edge.

            - **Name** *(string) --*

              The canonical name of the alias.

            - **Names** *(list) --*

              A list of names for the alias, including the canonical name.

              - *(string) --*

            - **Type** *(string) --*

              The type of the alias.

    - **SummaryStatistics** *(dict) --*

      Aggregated statistics for the service.

      - **OkCount** *(integer) --*

        The number of requests that completed with a 2xx Success status code.

      - **ErrorStatistics** *(dict) --*

        Information about requests that failed with a 4xx Client Error status code.

        - **ThrottleCount** *(integer) --*

          The number of requests that failed with a 419 throttling status code.

        - **OtherCount** *(integer) --*

          The number of requests that failed with untracked 4xx Client Error status codes.

        - **TotalCount** *(integer) --*

          The total number of requests that failed with a 4xx Client Error status code.

      - **FaultStatistics** *(dict) --*

        Information about requests that failed with a 5xx Server Error status code.

        - **OtherCount** *(integer) --*

          The number of requests that failed with untracked 5xx Server Error status codes.

        - **TotalCount** *(integer) --*

          The total number of requests that failed with a 5xx Server Error status code.

      - **TotalCount** *(integer) --*

        The total number of completed requests.

      - **TotalResponseTime** *(float) --*

        The aggregate response time of completed requests.

    - **DurationHistogram** *(list) --*

      A histogram that maps the spread of service durations.

      - *(dict) --*

        An entry in a histogram for a statistic. A histogram maps the range of observed values
        on the X axis, and the prevalence of each value on the Y axis.

        - **Value** *(float) --*

          The value of the entry.

        - **Count** *(integer) --*

          The prevalence of the entry.

    - **ResponseTimeHistogram** *(list) --*

      A histogram that maps the spread of service response times.

      - *(dict) --*

        An entry in a histogram for a statistic. A histogram maps the range of observed values
        on the X axis, and the prevalence of each value on the Y axis.

        - **Value** *(float) --*

          The value of the entry.

        - **Count** *(integer) --*

          The prevalence of the entry.
    """


_GetTraceGraphPaginateResponseTypeDef = TypedDict(
    "_GetTraceGraphPaginateResponseTypeDef",
    {"Services": List[GetTraceGraphPaginateResponseServicesTypeDef]},
    total=False,
)


class GetTraceGraphPaginateResponseTypeDef(_GetTraceGraphPaginateResponseTypeDef):
    """
    Type definition for `GetTraceGraphPaginate` `Response`

    - **Services** *(list) --*

      The services that have processed one of the specified requests.

      - *(dict) --*

        Information about an application that processed requests, users that made requests, or
        downstream services, resources and applications that an application used.

        - **ReferenceId** *(integer) --*

          Identifier for the service. Unique within the service map.

        - **Name** *(string) --*

          The canonical name of the service.

        - **Names** *(list) --*

          A list of names for the service, including the canonical name.

          - *(string) --*

        - **Root** *(boolean) --*

          Indicates that the service was the first service to process a request.

        - **AccountId** *(string) --*

          Identifier of the AWS account in which the service runs.

        - **Type** *(string) --*

          The type of service.

          * AWS Resource - The type of an AWS resource. For example, ``AWS::EC2::Instance`` for a
          application running on Amazon EC2 or ``AWS::DynamoDB::Table`` for an Amazon DynamoDB
          table that the application used.

          * AWS Service - The type of an AWS service. For example, ``AWS::DynamoDB`` for downstream
          calls to Amazon DynamoDB that didn't target a specific table.

          * ``client`` - Represents the clients that sent requests to a root service.

          * ``remote`` - A downstream service of indeterminate type.

        - **State** *(string) --*

          The service's state.

        - **StartTime** *(datetime) --*

          The start time of the first segment that the service generated.

        - **EndTime** *(datetime) --*

          The end time of the last segment that the service generated.

        - **Edges** *(list) --*

          Connections to downstream services.

          - *(dict) --*

            Information about a connection between two services.

            - **ReferenceId** *(integer) --*

              Identifier of the edge. Unique within a service map.

            - **StartTime** *(datetime) --*

              The start time of the first segment on the edge.

            - **EndTime** *(datetime) --*

              The end time of the last segment on the edge.

            - **SummaryStatistics** *(dict) --*

              Response statistics for segments on the edge.

              - **OkCount** *(integer) --*

                The number of requests that completed with a 2xx Success status code.

              - **ErrorStatistics** *(dict) --*

                Information about requests that failed with a 4xx Client Error status code.

                - **ThrottleCount** *(integer) --*

                  The number of requests that failed with a 419 throttling status code.

                - **OtherCount** *(integer) --*

                  The number of requests that failed with untracked 4xx Client Error status codes.

                - **TotalCount** *(integer) --*

                  The total number of requests that failed with a 4xx Client Error status code.

              - **FaultStatistics** *(dict) --*

                Information about requests that failed with a 5xx Server Error status code.

                - **OtherCount** *(integer) --*

                  The number of requests that failed with untracked 5xx Server Error status codes.

                - **TotalCount** *(integer) --*

                  The total number of requests that failed with a 5xx Server Error status code.

              - **TotalCount** *(integer) --*

                The total number of completed requests.

              - **TotalResponseTime** *(float) --*

                The aggregate response time of completed requests.

            - **ResponseTimeHistogram** *(list) --*

              A histogram that maps the spread of client response times on an edge.

              - *(dict) --*

                An entry in a histogram for a statistic. A histogram maps the range of observed
                values on the X axis, and the prevalence of each value on the Y axis.

                - **Value** *(float) --*

                  The value of the entry.

                - **Count** *(integer) --*

                  The prevalence of the entry.

            - **Aliases** *(list) --*

              Aliases for the edge.

              - *(dict) --*

                An alias for an edge.

                - **Name** *(string) --*

                  The canonical name of the alias.

                - **Names** *(list) --*

                  A list of names for the alias, including the canonical name.

                  - *(string) --*

                - **Type** *(string) --*

                  The type of the alias.

        - **SummaryStatistics** *(dict) --*

          Aggregated statistics for the service.

          - **OkCount** *(integer) --*

            The number of requests that completed with a 2xx Success status code.

          - **ErrorStatistics** *(dict) --*

            Information about requests that failed with a 4xx Client Error status code.

            - **ThrottleCount** *(integer) --*

              The number of requests that failed with a 419 throttling status code.

            - **OtherCount** *(integer) --*

              The number of requests that failed with untracked 4xx Client Error status codes.

            - **TotalCount** *(integer) --*

              The total number of requests that failed with a 4xx Client Error status code.

          - **FaultStatistics** *(dict) --*

            Information about requests that failed with a 5xx Server Error status code.

            - **OtherCount** *(integer) --*

              The number of requests that failed with untracked 5xx Server Error status codes.

            - **TotalCount** *(integer) --*

              The total number of requests that failed with a 5xx Server Error status code.

          - **TotalCount** *(integer) --*

            The total number of completed requests.

          - **TotalResponseTime** *(float) --*

            The aggregate response time of completed requests.

        - **DurationHistogram** *(list) --*

          A histogram that maps the spread of service durations.

          - *(dict) --*

            An entry in a histogram for a statistic. A histogram maps the range of observed values
            on the X axis, and the prevalence of each value on the Y axis.

            - **Value** *(float) --*

              The value of the entry.

            - **Count** *(integer) --*

              The prevalence of the entry.

        - **ResponseTimeHistogram** *(list) --*

          A histogram that maps the spread of service response times.

          - *(dict) --*

            An entry in a histogram for a statistic. A histogram maps the range of observed values
            on the X axis, and the prevalence of each value on the Y axis.

            - **Value** *(float) --*

              The value of the entry.

            - **Count** *(integer) --*

              The prevalence of the entry.
    """


_GetTraceSummariesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetTraceSummariesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetTraceSummariesPaginatePaginationConfigTypeDef(
    _GetTraceSummariesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetTraceSummariesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetTraceSummariesPaginateResponseTraceSummariesAnnotationsAnnotationValueTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesAnnotationsAnnotationValueTypeDef",
    {"NumberValue": float, "BooleanValue": bool, "StringValue": str},
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesAnnotationsAnnotationValueTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesAnnotationsAnnotationValueTypeDef
):
    """
    Type definition for `GetTraceSummariesPaginateResponseTraceSummariesAnnotations` `AnnotationValue`

    Values of the annotation.

    - **NumberValue** *(float) --*

      Value for a Number annotation.

    - **BooleanValue** *(boolean) --*

      Value for a Boolean annotation.

    - **StringValue** *(string) --*

      Value for a String annotation.
    """


_GetTraceSummariesPaginateResponseTraceSummariesAnnotationsServiceIdsTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesAnnotationsServiceIdsTypeDef",
    {"Name": str, "Names": List[str], "AccountId": str, "Type": str},
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesAnnotationsServiceIdsTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesAnnotationsServiceIdsTypeDef
):
    """
    Type definition for `GetTraceSummariesPaginateResponseTraceSummariesAnnotations` `ServiceIds`

    - **Name** *(string) --*

    - **Names** *(list) --*

      - *(string) --*

    - **AccountId** *(string) --*

    - **Type** *(string) --*
    """


_GetTraceSummariesPaginateResponseTraceSummariesAnnotationsTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesAnnotationsTypeDef",
    {
        "AnnotationValue": GetTraceSummariesPaginateResponseTraceSummariesAnnotationsAnnotationValueTypeDef,
        "ServiceIds": List[
            GetTraceSummariesPaginateResponseTraceSummariesAnnotationsServiceIdsTypeDef
        ],
    },
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesAnnotationsTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesAnnotationsTypeDef
):
    """
    Type definition for `GetTraceSummariesPaginateResponseTraceSummaries` `Annotations`

    Information about a segment annotation.

    - **AnnotationValue** *(dict) --*

      Values of the annotation.

      - **NumberValue** *(float) --*

        Value for a Number annotation.

      - **BooleanValue** *(boolean) --*

        Value for a Boolean annotation.

      - **StringValue** *(string) --*

        Value for a String annotation.

    - **ServiceIds** *(list) --*

      Services to which the annotation applies.

      - *(dict) --*

        - **Name** *(string) --*

        - **Names** *(list) --*

          - *(string) --*

        - **AccountId** *(string) --*

        - **Type** *(string) --*
    """


_GetTraceSummariesPaginateResponseTraceSummariesAvailabilityZonesTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesAvailabilityZonesTypeDef",
    {"Name": str},
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesAvailabilityZonesTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesAvailabilityZonesTypeDef
):
    """
    Type definition for `GetTraceSummariesPaginateResponseTraceSummaries` `AvailabilityZones`

    A list of availability zones corresponding to the segments in a trace.

    - **Name** *(string) --*

      The name of a corresponding availability zone.
    """


_GetTraceSummariesPaginateResponseTraceSummariesEntryPointTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesEntryPointTypeDef",
    {"Name": str, "Names": List[str], "AccountId": str, "Type": str},
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesEntryPointTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesEntryPointTypeDef
):
    """
    Type definition for `GetTraceSummariesPaginateResponseTraceSummaries` `EntryPoint`

    The root of a trace.

    - **Name** *(string) --*

    - **Names** *(list) --*

      - *(string) --*

    - **AccountId** *(string) --*

    - **Type** *(string) --*
    """


_GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef",
    {"Name": str, "Message": str},
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef
):
    """
    Type definition for `GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesEntityPath` `Exceptions`

    The exception associated with a root cause.

    - **Name** *(string) --*

      The name of the exception.

    - **Message** *(string) --*

      The message of the exception.
    """


_GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesEntityPathTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesEntityPathTypeDef",
    {
        "Name": str,
        "Exceptions": List[
            GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef
        ],
        "Remote": bool,
    },
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesEntityPathTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesEntityPathTypeDef
):
    """
    Type definition for `GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServices` `EntityPath`

    A collection of segments and corresponding subsegments associated to a trace
    summary error.

    - **Name** *(string) --*

      The name of the entity.

    - **Exceptions** *(list) --*

      The types and messages of the exceptions.

      - *(dict) --*

        The exception associated with a root cause.

        - **Name** *(string) --*

          The name of the exception.

        - **Message** *(string) --*

          The message of the exception.

    - **Remote** *(boolean) --*

      A flag that denotes a remote subsegment.
    """


_GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesTypeDef",
    {
        "Name": str,
        "Names": List[str],
        "Type": str,
        "AccountId": str,
        "EntityPath": List[
            GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesEntityPathTypeDef
        ],
        "Inferred": bool,
    },
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesTypeDef
):
    """
    Type definition for `GetTraceSummariesPaginateResponseTraceSummariesErrorRootCauses` `Services`

    A collection of fields identifying the services in a trace summary error.

    - **Name** *(string) --*

      The service name.

    - **Names** *(list) --*

      A collection of associated service names.

      - *(string) --*

    - **Type** *(string) --*

      The type associated to the service.

    - **AccountId** *(string) --*

      The account ID associated to the service.

    - **EntityPath** *(list) --*

      The path of root cause entities found on the service.

      - *(dict) --*

        A collection of segments and corresponding subsegments associated to a trace
        summary error.

        - **Name** *(string) --*

          The name of the entity.

        - **Exceptions** *(list) --*

          The types and messages of the exceptions.

          - *(dict) --*

            The exception associated with a root cause.

            - **Name** *(string) --*

              The name of the exception.

            - **Message** *(string) --*

              The message of the exception.

        - **Remote** *(boolean) --*

          A flag that denotes a remote subsegment.

    - **Inferred** *(boolean) --*

      A Boolean value indicating if the service is inferred from the trace.
    """


_GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesTypeDef",
    {
        "Services": List[
            GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesTypeDef
        ]
    },
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesTypeDef
):
    """
    Type definition for `GetTraceSummariesPaginateResponseTraceSummaries` `ErrorRootCauses`

    The root cause of a trace summary error.

    - **Services** *(list) --*

      A list of services corresponding to an error. A service identifies a segment and it
      contains a name, account ID, type, and inferred flag.

      - *(dict) --*

        A collection of fields identifying the services in a trace summary error.

        - **Name** *(string) --*

          The service name.

        - **Names** *(list) --*

          A collection of associated service names.

          - *(string) --*

        - **Type** *(string) --*

          The type associated to the service.

        - **AccountId** *(string) --*

          The account ID associated to the service.

        - **EntityPath** *(list) --*

          The path of root cause entities found on the service.

          - *(dict) --*

            A collection of segments and corresponding subsegments associated to a trace
            summary error.

            - **Name** *(string) --*

              The name of the entity.

            - **Exceptions** *(list) --*

              The types and messages of the exceptions.

              - *(dict) --*

                The exception associated with a root cause.

                - **Name** *(string) --*

                  The name of the exception.

                - **Message** *(string) --*

                  The message of the exception.

            - **Remote** *(boolean) --*

              A flag that denotes a remote subsegment.

        - **Inferred** *(boolean) --*

          A Boolean value indicating if the service is inferred from the trace.
    """


_GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef",
    {"Name": str, "Message": str},
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef
):
    """
    Type definition for `GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesEntityPath` `Exceptions`

    The exception associated with a root cause.

    - **Name** *(string) --*

      The name of the exception.

    - **Message** *(string) --*

      The message of the exception.
    """


_GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesEntityPathTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesEntityPathTypeDef",
    {
        "Name": str,
        "Exceptions": List[
            GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef
        ],
        "Remote": bool,
    },
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesEntityPathTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesEntityPathTypeDef
):
    """
    Type definition for `GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServices` `EntityPath`

    A collection of segments and corresponding subsegments associated to a trace
    summary fault error.

    - **Name** *(string) --*

      The name of the entity.

    - **Exceptions** *(list) --*

      The types and messages of the exceptions.

      - *(dict) --*

        The exception associated with a root cause.

        - **Name** *(string) --*

          The name of the exception.

        - **Message** *(string) --*

          The message of the exception.

    - **Remote** *(boolean) --*

      A flag that denotes a remote subsegment.
    """


_GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesTypeDef",
    {
        "Name": str,
        "Names": List[str],
        "Type": str,
        "AccountId": str,
        "EntityPath": List[
            GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesEntityPathTypeDef
        ],
        "Inferred": bool,
    },
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesTypeDef
):
    """
    Type definition for `GetTraceSummariesPaginateResponseTraceSummariesFaultRootCauses` `Services`

    A collection of fields identifying the services in a trace summary fault.

    - **Name** *(string) --*

      The service name.

    - **Names** *(list) --*

      A collection of associated service names.

      - *(string) --*

    - **Type** *(string) --*

      The type associated to the service.

    - **AccountId** *(string) --*

      The account ID associated to the service.

    - **EntityPath** *(list) --*

      The path of root cause entities found on the service.

      - *(dict) --*

        A collection of segments and corresponding subsegments associated to a trace
        summary fault error.

        - **Name** *(string) --*

          The name of the entity.

        - **Exceptions** *(list) --*

          The types and messages of the exceptions.

          - *(dict) --*

            The exception associated with a root cause.

            - **Name** *(string) --*

              The name of the exception.

            - **Message** *(string) --*

              The message of the exception.

        - **Remote** *(boolean) --*

          A flag that denotes a remote subsegment.

    - **Inferred** *(boolean) --*

      A Boolean value indicating if the service is inferred from the trace.
    """


_GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesTypeDef",
    {
        "Services": List[
            GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesTypeDef
        ]
    },
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesTypeDef
):
    """
    Type definition for `GetTraceSummariesPaginateResponseTraceSummaries` `FaultRootCauses`

    The root cause information for a trace summary fault.

    - **Services** *(list) --*

      A list of corresponding services. A service identifies a segment and it contains a
      name, account ID, type, and inferred flag.

      - *(dict) --*

        A collection of fields identifying the services in a trace summary fault.

        - **Name** *(string) --*

          The service name.

        - **Names** *(list) --*

          A collection of associated service names.

          - *(string) --*

        - **Type** *(string) --*

          The type associated to the service.

        - **AccountId** *(string) --*

          The account ID associated to the service.

        - **EntityPath** *(list) --*

          The path of root cause entities found on the service.

          - *(dict) --*

            A collection of segments and corresponding subsegments associated to a trace
            summary fault error.

            - **Name** *(string) --*

              The name of the entity.

            - **Exceptions** *(list) --*

              The types and messages of the exceptions.

              - *(dict) --*

                The exception associated with a root cause.

                - **Name** *(string) --*

                  The name of the exception.

                - **Message** *(string) --*

                  The message of the exception.

            - **Remote** *(boolean) --*

              A flag that denotes a remote subsegment.

        - **Inferred** *(boolean) --*

          A Boolean value indicating if the service is inferred from the trace.
    """


_GetTraceSummariesPaginateResponseTraceSummariesHttpTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesHttpTypeDef",
    {
        "HttpURL": str,
        "HttpStatus": int,
        "HttpMethod": str,
        "UserAgent": str,
        "ClientIp": str,
    },
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesHttpTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesHttpTypeDef
):
    """
    Type definition for `GetTraceSummariesPaginateResponseTraceSummaries` `Http`

    Information about the HTTP request served by the trace.

    - **HttpURL** *(string) --*

      The request URL.

    - **HttpStatus** *(integer) --*

      The response status.

    - **HttpMethod** *(string) --*

      The request method.

    - **UserAgent** *(string) --*

      The request's user agent string.

    - **ClientIp** *(string) --*

      The IP address of the requestor.
    """


_GetTraceSummariesPaginateResponseTraceSummariesInstanceIdsTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesInstanceIdsTypeDef",
    {"Id": str},
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesInstanceIdsTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesInstanceIdsTypeDef
):
    """
    Type definition for `GetTraceSummariesPaginateResponseTraceSummaries` `InstanceIds`

    A list of EC2 instance IDs corresponding to the segments in a trace.

    - **Id** *(string) --*

      The ID of a corresponding EC2 instance.
    """


_GetTraceSummariesPaginateResponseTraceSummariesResourceARNsTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesResourceARNsTypeDef",
    {"ARN": str},
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesResourceARNsTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesResourceARNsTypeDef
):
    """
    Type definition for `GetTraceSummariesPaginateResponseTraceSummaries` `ResourceARNs`

    A list of resources ARNs corresponding to the segments in a trace.

    - **ARN** *(string) --*

      The ARN of a corresponding resource.
    """


_GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesServicesEntityPathTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesServicesEntityPathTypeDef",
    {"Name": str, "Coverage": float, "Remote": bool},
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesServicesEntityPathTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesServicesEntityPathTypeDef
):
    """
    Type definition for `GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesServices` `EntityPath`

    A collection of segments and corresponding subsegments associated to a response
    time warning.

    - **Name** *(string) --*

      The name of the entity.

    - **Coverage** *(float) --*

      The types and messages of the exceptions.

    - **Remote** *(boolean) --*

      A flag that denotes a remote subsegment.
    """


_GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesServicesTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesServicesTypeDef",
    {
        "Name": str,
        "Names": List[str],
        "Type": str,
        "AccountId": str,
        "EntityPath": List[
            GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesServicesEntityPathTypeDef
        ],
        "Inferred": bool,
    },
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesServicesTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesServicesTypeDef
):
    """
    Type definition for `GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCauses` `Services`

    A collection of fields identifying the service in a response time warning.

    - **Name** *(string) --*

      The service name.

    - **Names** *(list) --*

      A collection of associated service names.

      - *(string) --*

    - **Type** *(string) --*

      The type associated to the service.

    - **AccountId** *(string) --*

      The account ID associated to the service.

    - **EntityPath** *(list) --*

      The path of root cause entities found on the service.

      - *(dict) --*

        A collection of segments and corresponding subsegments associated to a response
        time warning.

        - **Name** *(string) --*

          The name of the entity.

        - **Coverage** *(float) --*

          The types and messages of the exceptions.

        - **Remote** *(boolean) --*

          A flag that denotes a remote subsegment.

    - **Inferred** *(boolean) --*

      A Boolean value indicating if the service is inferred from the trace.
    """


_GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesTypeDef",
    {
        "Services": List[
            GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesServicesTypeDef
        ]
    },
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesTypeDef
):
    """
    Type definition for `GetTraceSummariesPaginateResponseTraceSummaries` `ResponseTimeRootCauses`

    The root cause information for a response time warning.

    - **Services** *(list) --*

      A list of corresponding services. A service identifies a segment and contains a name,
      account ID, type, and inferred flag.

      - *(dict) --*

        A collection of fields identifying the service in a response time warning.

        - **Name** *(string) --*

          The service name.

        - **Names** *(list) --*

          A collection of associated service names.

          - *(string) --*

        - **Type** *(string) --*

          The type associated to the service.

        - **AccountId** *(string) --*

          The account ID associated to the service.

        - **EntityPath** *(list) --*

          The path of root cause entities found on the service.

          - *(dict) --*

            A collection of segments and corresponding subsegments associated to a response
            time warning.

            - **Name** *(string) --*

              The name of the entity.

            - **Coverage** *(float) --*

              The types and messages of the exceptions.

            - **Remote** *(boolean) --*

              A flag that denotes a remote subsegment.

        - **Inferred** *(boolean) --*

          A Boolean value indicating if the service is inferred from the trace.
    """


_GetTraceSummariesPaginateResponseTraceSummariesServiceIdsTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesServiceIdsTypeDef",
    {"Name": str, "Names": List[str], "AccountId": str, "Type": str},
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesServiceIdsTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesServiceIdsTypeDef
):
    """
    Type definition for `GetTraceSummariesPaginateResponseTraceSummaries` `ServiceIds`

    - **Name** *(string) --*

    - **Names** *(list) --*

      - *(string) --*

    - **AccountId** *(string) --*

    - **Type** *(string) --*
    """


_GetTraceSummariesPaginateResponseTraceSummariesUsersServiceIdsTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesUsersServiceIdsTypeDef",
    {"Name": str, "Names": List[str], "AccountId": str, "Type": str},
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesUsersServiceIdsTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesUsersServiceIdsTypeDef
):
    """
    Type definition for `GetTraceSummariesPaginateResponseTraceSummariesUsers` `ServiceIds`

    - **Name** *(string) --*

    - **Names** *(list) --*

      - *(string) --*

    - **AccountId** *(string) --*

    - **Type** *(string) --*
    """


_GetTraceSummariesPaginateResponseTraceSummariesUsersTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesUsersTypeDef",
    {
        "UserName": str,
        "ServiceIds": List[
            GetTraceSummariesPaginateResponseTraceSummariesUsersServiceIdsTypeDef
        ],
    },
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesUsersTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesUsersTypeDef
):
    """
    Type definition for `GetTraceSummariesPaginateResponseTraceSummaries` `Users`

    Information about a user recorded in segment documents.

    - **UserName** *(string) --*

      The user's name.

    - **ServiceIds** *(list) --*

      Services that the user's request hit.

      - *(dict) --*

        - **Name** *(string) --*

        - **Names** *(list) --*

          - *(string) --*

        - **AccountId** *(string) --*

        - **Type** *(string) --*
    """


_GetTraceSummariesPaginateResponseTraceSummariesTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesTypeDef",
    {
        "Id": str,
        "Duration": float,
        "ResponseTime": float,
        "HasFault": bool,
        "HasError": bool,
        "HasThrottle": bool,
        "IsPartial": bool,
        "Http": GetTraceSummariesPaginateResponseTraceSummariesHttpTypeDef,
        "Annotations": Dict[
            str, List[GetTraceSummariesPaginateResponseTraceSummariesAnnotationsTypeDef]
        ],
        "Users": List[GetTraceSummariesPaginateResponseTraceSummariesUsersTypeDef],
        "ServiceIds": List[
            GetTraceSummariesPaginateResponseTraceSummariesServiceIdsTypeDef
        ],
        "ResourceARNs": List[
            GetTraceSummariesPaginateResponseTraceSummariesResourceARNsTypeDef
        ],
        "InstanceIds": List[
            GetTraceSummariesPaginateResponseTraceSummariesInstanceIdsTypeDef
        ],
        "AvailabilityZones": List[
            GetTraceSummariesPaginateResponseTraceSummariesAvailabilityZonesTypeDef
        ],
        "EntryPoint": GetTraceSummariesPaginateResponseTraceSummariesEntryPointTypeDef,
        "FaultRootCauses": List[
            GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesTypeDef
        ],
        "ErrorRootCauses": List[
            GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesTypeDef
        ],
        "ResponseTimeRootCauses": List[
            GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesTypeDef
        ],
        "Revision": int,
        "MatchedEventTime": datetime,
    },
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesTypeDef
):
    """
    Type definition for `GetTraceSummariesPaginateResponse` `TraceSummaries`

    Metadata generated from the segment documents in a trace.

    - **Id** *(string) --*

      The unique identifier for the request that generated the trace's segments and subsegments.

    - **Duration** *(float) --*

      The length of time in seconds between the start time of the root segment and the end time
      of the last segment that completed.

    - **ResponseTime** *(float) --*

      The length of time in seconds between the start and end times of the root segment. If the
      service performs work asynchronously, the response time measures the time before the
      response is sent to the user, while the duration measures the amount of time before the
      last traced activity completes.

    - **HasFault** *(boolean) --*

      One or more of the segment documents has a 500 series error.

    - **HasError** *(boolean) --*

      One or more of the segment documents has a 400 series error.

    - **HasThrottle** *(boolean) --*

      One or more of the segment documents has a 429 throttling error.

    - **IsPartial** *(boolean) --*

      One or more of the segment documents is in progress.

    - **Http** *(dict) --*

      Information about the HTTP request served by the trace.

      - **HttpURL** *(string) --*

        The request URL.

      - **HttpStatus** *(integer) --*

        The response status.

      - **HttpMethod** *(string) --*

        The request method.

      - **UserAgent** *(string) --*

        The request's user agent string.

      - **ClientIp** *(string) --*

        The IP address of the requestor.

    - **Annotations** *(dict) --*

      Annotations from the trace's segment documents.

      - *(string) --*

        - *(list) --*

          - *(dict) --*

            Information about a segment annotation.

            - **AnnotationValue** *(dict) --*

              Values of the annotation.

              - **NumberValue** *(float) --*

                Value for a Number annotation.

              - **BooleanValue** *(boolean) --*

                Value for a Boolean annotation.

              - **StringValue** *(string) --*

                Value for a String annotation.

            - **ServiceIds** *(list) --*

              Services to which the annotation applies.

              - *(dict) --*

                - **Name** *(string) --*

                - **Names** *(list) --*

                  - *(string) --*

                - **AccountId** *(string) --*

                - **Type** *(string) --*

    - **Users** *(list) --*

      Users from the trace's segment documents.

      - *(dict) --*

        Information about a user recorded in segment documents.

        - **UserName** *(string) --*

          The user's name.

        - **ServiceIds** *(list) --*

          Services that the user's request hit.

          - *(dict) --*

            - **Name** *(string) --*

            - **Names** *(list) --*

              - *(string) --*

            - **AccountId** *(string) --*

            - **Type** *(string) --*

    - **ServiceIds** *(list) --*

      Service IDs from the trace's segment documents.

      - *(dict) --*

        - **Name** *(string) --*

        - **Names** *(list) --*

          - *(string) --*

        - **AccountId** *(string) --*

        - **Type** *(string) --*

    - **ResourceARNs** *(list) --*

      A list of resource ARNs for any resource corresponding to the trace segments.

      - *(dict) --*

        A list of resources ARNs corresponding to the segments in a trace.

        - **ARN** *(string) --*

          The ARN of a corresponding resource.

    - **InstanceIds** *(list) --*

      A list of EC2 instance IDs for any instance corresponding to the trace segments.

      - *(dict) --*

        A list of EC2 instance IDs corresponding to the segments in a trace.

        - **Id** *(string) --*

          The ID of a corresponding EC2 instance.

    - **AvailabilityZones** *(list) --*

      A list of availability zones for any zone corresponding to the trace segments.

      - *(dict) --*

        A list of availability zones corresponding to the segments in a trace.

        - **Name** *(string) --*

          The name of a corresponding availability zone.

    - **EntryPoint** *(dict) --*

      The root of a trace.

      - **Name** *(string) --*

      - **Names** *(list) --*

        - *(string) --*

      - **AccountId** *(string) --*

      - **Type** *(string) --*

    - **FaultRootCauses** *(list) --*

      A collection of FaultRootCause structures corresponding to the the trace segments.

      - *(dict) --*

        The root cause information for a trace summary fault.

        - **Services** *(list) --*

          A list of corresponding services. A service identifies a segment and it contains a
          name, account ID, type, and inferred flag.

          - *(dict) --*

            A collection of fields identifying the services in a trace summary fault.

            - **Name** *(string) --*

              The service name.

            - **Names** *(list) --*

              A collection of associated service names.

              - *(string) --*

            - **Type** *(string) --*

              The type associated to the service.

            - **AccountId** *(string) --*

              The account ID associated to the service.

            - **EntityPath** *(list) --*

              The path of root cause entities found on the service.

              - *(dict) --*

                A collection of segments and corresponding subsegments associated to a trace
                summary fault error.

                - **Name** *(string) --*

                  The name of the entity.

                - **Exceptions** *(list) --*

                  The types and messages of the exceptions.

                  - *(dict) --*

                    The exception associated with a root cause.

                    - **Name** *(string) --*

                      The name of the exception.

                    - **Message** *(string) --*

                      The message of the exception.

                - **Remote** *(boolean) --*

                  A flag that denotes a remote subsegment.

            - **Inferred** *(boolean) --*

              A Boolean value indicating if the service is inferred from the trace.

    - **ErrorRootCauses** *(list) --*

      A collection of ErrorRootCause structures corresponding to the trace segments.

      - *(dict) --*

        The root cause of a trace summary error.

        - **Services** *(list) --*

          A list of services corresponding to an error. A service identifies a segment and it
          contains a name, account ID, type, and inferred flag.

          - *(dict) --*

            A collection of fields identifying the services in a trace summary error.

            - **Name** *(string) --*

              The service name.

            - **Names** *(list) --*

              A collection of associated service names.

              - *(string) --*

            - **Type** *(string) --*

              The type associated to the service.

            - **AccountId** *(string) --*

              The account ID associated to the service.

            - **EntityPath** *(list) --*

              The path of root cause entities found on the service.

              - *(dict) --*

                A collection of segments and corresponding subsegments associated to a trace
                summary error.

                - **Name** *(string) --*

                  The name of the entity.

                - **Exceptions** *(list) --*

                  The types and messages of the exceptions.

                  - *(dict) --*

                    The exception associated with a root cause.

                    - **Name** *(string) --*

                      The name of the exception.

                    - **Message** *(string) --*

                      The message of the exception.

                - **Remote** *(boolean) --*

                  A flag that denotes a remote subsegment.

            - **Inferred** *(boolean) --*

              A Boolean value indicating if the service is inferred from the trace.

    - **ResponseTimeRootCauses** *(list) --*

      A collection of ResponseTimeRootCause structures corresponding to the trace segments.

      - *(dict) --*

        The root cause information for a response time warning.

        - **Services** *(list) --*

          A list of corresponding services. A service identifies a segment and contains a name,
          account ID, type, and inferred flag.

          - *(dict) --*

            A collection of fields identifying the service in a response time warning.

            - **Name** *(string) --*

              The service name.

            - **Names** *(list) --*

              A collection of associated service names.

              - *(string) --*

            - **Type** *(string) --*

              The type associated to the service.

            - **AccountId** *(string) --*

              The account ID associated to the service.

            - **EntityPath** *(list) --*

              The path of root cause entities found on the service.

              - *(dict) --*

                A collection of segments and corresponding subsegments associated to a response
                time warning.

                - **Name** *(string) --*

                  The name of the entity.

                - **Coverage** *(float) --*

                  The types and messages of the exceptions.

                - **Remote** *(boolean) --*

                  A flag that denotes a remote subsegment.

            - **Inferred** *(boolean) --*

              A Boolean value indicating if the service is inferred from the trace.

    - **Revision** *(integer) --*

      The revision number of a trace.

    - **MatchedEventTime** *(datetime) --*

      The matched time stamp of a defined event.
    """


_GetTraceSummariesPaginateResponseTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTypeDef",
    {
        "TraceSummaries": List[GetTraceSummariesPaginateResponseTraceSummariesTypeDef],
        "ApproximateTime": datetime,
        "TracesProcessedCount": int,
    },
    total=False,
)


class GetTraceSummariesPaginateResponseTypeDef(
    _GetTraceSummariesPaginateResponseTypeDef
):
    """
    Type definition for `GetTraceSummariesPaginate` `Response`

    - **TraceSummaries** *(list) --*

      Trace IDs and metadata for traces that were found in the specified time frame.

      - *(dict) --*

        Metadata generated from the segment documents in a trace.

        - **Id** *(string) --*

          The unique identifier for the request that generated the trace's segments and subsegments.

        - **Duration** *(float) --*

          The length of time in seconds between the start time of the root segment and the end time
          of the last segment that completed.

        - **ResponseTime** *(float) --*

          The length of time in seconds between the start and end times of the root segment. If the
          service performs work asynchronously, the response time measures the time before the
          response is sent to the user, while the duration measures the amount of time before the
          last traced activity completes.

        - **HasFault** *(boolean) --*

          One or more of the segment documents has a 500 series error.

        - **HasError** *(boolean) --*

          One or more of the segment documents has a 400 series error.

        - **HasThrottle** *(boolean) --*

          One or more of the segment documents has a 429 throttling error.

        - **IsPartial** *(boolean) --*

          One or more of the segment documents is in progress.

        - **Http** *(dict) --*

          Information about the HTTP request served by the trace.

          - **HttpURL** *(string) --*

            The request URL.

          - **HttpStatus** *(integer) --*

            The response status.

          - **HttpMethod** *(string) --*

            The request method.

          - **UserAgent** *(string) --*

            The request's user agent string.

          - **ClientIp** *(string) --*

            The IP address of the requestor.

        - **Annotations** *(dict) --*

          Annotations from the trace's segment documents.

          - *(string) --*

            - *(list) --*

              - *(dict) --*

                Information about a segment annotation.

                - **AnnotationValue** *(dict) --*

                  Values of the annotation.

                  - **NumberValue** *(float) --*

                    Value for a Number annotation.

                  - **BooleanValue** *(boolean) --*

                    Value for a Boolean annotation.

                  - **StringValue** *(string) --*

                    Value for a String annotation.

                - **ServiceIds** *(list) --*

                  Services to which the annotation applies.

                  - *(dict) --*

                    - **Name** *(string) --*

                    - **Names** *(list) --*

                      - *(string) --*

                    - **AccountId** *(string) --*

                    - **Type** *(string) --*

        - **Users** *(list) --*

          Users from the trace's segment documents.

          - *(dict) --*

            Information about a user recorded in segment documents.

            - **UserName** *(string) --*

              The user's name.

            - **ServiceIds** *(list) --*

              Services that the user's request hit.

              - *(dict) --*

                - **Name** *(string) --*

                - **Names** *(list) --*

                  - *(string) --*

                - **AccountId** *(string) --*

                - **Type** *(string) --*

        - **ServiceIds** *(list) --*

          Service IDs from the trace's segment documents.

          - *(dict) --*

            - **Name** *(string) --*

            - **Names** *(list) --*

              - *(string) --*

            - **AccountId** *(string) --*

            - **Type** *(string) --*

        - **ResourceARNs** *(list) --*

          A list of resource ARNs for any resource corresponding to the trace segments.

          - *(dict) --*

            A list of resources ARNs corresponding to the segments in a trace.

            - **ARN** *(string) --*

              The ARN of a corresponding resource.

        - **InstanceIds** *(list) --*

          A list of EC2 instance IDs for any instance corresponding to the trace segments.

          - *(dict) --*

            A list of EC2 instance IDs corresponding to the segments in a trace.

            - **Id** *(string) --*

              The ID of a corresponding EC2 instance.

        - **AvailabilityZones** *(list) --*

          A list of availability zones for any zone corresponding to the trace segments.

          - *(dict) --*

            A list of availability zones corresponding to the segments in a trace.

            - **Name** *(string) --*

              The name of a corresponding availability zone.

        - **EntryPoint** *(dict) --*

          The root of a trace.

          - **Name** *(string) --*

          - **Names** *(list) --*

            - *(string) --*

          - **AccountId** *(string) --*

          - **Type** *(string) --*

        - **FaultRootCauses** *(list) --*

          A collection of FaultRootCause structures corresponding to the the trace segments.

          - *(dict) --*

            The root cause information for a trace summary fault.

            - **Services** *(list) --*

              A list of corresponding services. A service identifies a segment and it contains a
              name, account ID, type, and inferred flag.

              - *(dict) --*

                A collection of fields identifying the services in a trace summary fault.

                - **Name** *(string) --*

                  The service name.

                - **Names** *(list) --*

                  A collection of associated service names.

                  - *(string) --*

                - **Type** *(string) --*

                  The type associated to the service.

                - **AccountId** *(string) --*

                  The account ID associated to the service.

                - **EntityPath** *(list) --*

                  The path of root cause entities found on the service.

                  - *(dict) --*

                    A collection of segments and corresponding subsegments associated to a trace
                    summary fault error.

                    - **Name** *(string) --*

                      The name of the entity.

                    - **Exceptions** *(list) --*

                      The types and messages of the exceptions.

                      - *(dict) --*

                        The exception associated with a root cause.

                        - **Name** *(string) --*

                          The name of the exception.

                        - **Message** *(string) --*

                          The message of the exception.

                    - **Remote** *(boolean) --*

                      A flag that denotes a remote subsegment.

                - **Inferred** *(boolean) --*

                  A Boolean value indicating if the service is inferred from the trace.

        - **ErrorRootCauses** *(list) --*

          A collection of ErrorRootCause structures corresponding to the trace segments.

          - *(dict) --*

            The root cause of a trace summary error.

            - **Services** *(list) --*

              A list of services corresponding to an error. A service identifies a segment and it
              contains a name, account ID, type, and inferred flag.

              - *(dict) --*

                A collection of fields identifying the services in a trace summary error.

                - **Name** *(string) --*

                  The service name.

                - **Names** *(list) --*

                  A collection of associated service names.

                  - *(string) --*

                - **Type** *(string) --*

                  The type associated to the service.

                - **AccountId** *(string) --*

                  The account ID associated to the service.

                - **EntityPath** *(list) --*

                  The path of root cause entities found on the service.

                  - *(dict) --*

                    A collection of segments and corresponding subsegments associated to a trace
                    summary error.

                    - **Name** *(string) --*

                      The name of the entity.

                    - **Exceptions** *(list) --*

                      The types and messages of the exceptions.

                      - *(dict) --*

                        The exception associated with a root cause.

                        - **Name** *(string) --*

                          The name of the exception.

                        - **Message** *(string) --*

                          The message of the exception.

                    - **Remote** *(boolean) --*

                      A flag that denotes a remote subsegment.

                - **Inferred** *(boolean) --*

                  A Boolean value indicating if the service is inferred from the trace.

        - **ResponseTimeRootCauses** *(list) --*

          A collection of ResponseTimeRootCause structures corresponding to the trace segments.

          - *(dict) --*

            The root cause information for a response time warning.

            - **Services** *(list) --*

              A list of corresponding services. A service identifies a segment and contains a name,
              account ID, type, and inferred flag.

              - *(dict) --*

                A collection of fields identifying the service in a response time warning.

                - **Name** *(string) --*

                  The service name.

                - **Names** *(list) --*

                  A collection of associated service names.

                  - *(string) --*

                - **Type** *(string) --*

                  The type associated to the service.

                - **AccountId** *(string) --*

                  The account ID associated to the service.

                - **EntityPath** *(list) --*

                  The path of root cause entities found on the service.

                  - *(dict) --*

                    A collection of segments and corresponding subsegments associated to a response
                    time warning.

                    - **Name** *(string) --*

                      The name of the entity.

                    - **Coverage** *(float) --*

                      The types and messages of the exceptions.

                    - **Remote** *(boolean) --*

                      A flag that denotes a remote subsegment.

                - **Inferred** *(boolean) --*

                  A Boolean value indicating if the service is inferred from the trace.

        - **Revision** *(integer) --*

          The revision number of a trace.

        - **MatchedEventTime** *(datetime) --*

          The matched time stamp of a defined event.

    - **ApproximateTime** *(datetime) --*

      The start time of this page of results.

    - **TracesProcessedCount** *(integer) --*

      The total number of traces processed, including traces that did not match the specified
      filter expression.
    """


_GetTraceSummariesPaginateSamplingStrategyTypeDef = TypedDict(
    "_GetTraceSummariesPaginateSamplingStrategyTypeDef",
    {"Name": str, "Value": float},
    total=False,
)


class GetTraceSummariesPaginateSamplingStrategyTypeDef(
    _GetTraceSummariesPaginateSamplingStrategyTypeDef
):
    """
    Type definition for `GetTraceSummariesPaginate` `SamplingStrategy`

    A paramater to indicate whether to enable sampling on trace summaries. Input parameters are Name
    and Value.

    - **Name** *(string) --*

      The name of a sampling rule.

    - **Value** *(float) --*

      The value of a sampling rule.
    """
