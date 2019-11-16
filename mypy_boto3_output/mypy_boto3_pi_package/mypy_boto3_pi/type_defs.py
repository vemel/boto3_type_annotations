"Main interface for pi type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientDescribeDimensionKeysGroupByTypeDef",
    "ClientDescribeDimensionKeysPartitionByTypeDef",
    "ClientDescribeDimensionKeysResponseKeysTypeDef",
    "ClientDescribeDimensionKeysResponsePartitionKeysTypeDef",
    "ClientDescribeDimensionKeysResponseTypeDef",
    "ClientGetResourceMetricsMetricQueriesGroupByTypeDef",
    "ClientGetResourceMetricsMetricQueriesTypeDef",
    "ClientGetResourceMetricsResponseMetricListDataPointsTypeDef",
    "ClientGetResourceMetricsResponseMetricListKeyTypeDef",
    "ClientGetResourceMetricsResponseMetricListTypeDef",
    "ClientGetResourceMetricsResponseTypeDef",
)


_RequiredClientDescribeDimensionKeysGroupByTypeDef = TypedDict(
    "_RequiredClientDescribeDimensionKeysGroupByTypeDef", {"Group": str}
)
_OptionalClientDescribeDimensionKeysGroupByTypeDef = TypedDict(
    "_OptionalClientDescribeDimensionKeysGroupByTypeDef",
    {"Dimensions": List[str], "Limit": int},
    total=False,
)


class ClientDescribeDimensionKeysGroupByTypeDef(
    _RequiredClientDescribeDimensionKeysGroupByTypeDef,
    _OptionalClientDescribeDimensionKeysGroupByTypeDef,
):
    """
    Type definition for `ClientDescribeDimensionKeys` `GroupBy`

    A specification for how to aggregate the data points from a query result. You must specify a
    valid dimension group. Performance Insights will return all of the dimensions within that group,
    unless you provide the names of specific dimensions within that group. You can also request that
    Performance Insights return a limited number of values for a dimension.

    - **Group** *(string) --* **[REQUIRED]**

      The name of the dimension group. Valid values are:

      * ``db.user``

      * ``db.host``

      * ``db.sql``

      * ``db.sql_tokenized``

      * ``db.wait_event``

      * ``db.wait_event_type``

    - **Dimensions** *(list) --*

      A list of specific dimensions from a dimension group. If this parameter is not present, then it
      signifies that all of the dimensions in the group were requested, or are present in the
      response.

      Valid values for elements in the ``Dimensions`` array are:

      * db.user.id

      * db.user.name

      * db.host.id

      * db.host.name

      * db.sql.id

      * db.sql.db_id

      * db.sql.statement

      * db.sql.tokenized_id

      * db.sql_tokenized.id

      * db.sql_tokenized.db_id

      * db.sql_tokenized.statement

      * db.wait_event.name

      * db.wait_event.type

      * db.wait_event_type.name

      - *(string) --*

    - **Limit** *(integer) --*

      The maximum number of items to fetch for this dimension group.
    """


_RequiredClientDescribeDimensionKeysPartitionByTypeDef = TypedDict(
    "_RequiredClientDescribeDimensionKeysPartitionByTypeDef", {"Group": str}
)
_OptionalClientDescribeDimensionKeysPartitionByTypeDef = TypedDict(
    "_OptionalClientDescribeDimensionKeysPartitionByTypeDef",
    {"Dimensions": List[str], "Limit": int},
    total=False,
)


class ClientDescribeDimensionKeysPartitionByTypeDef(
    _RequiredClientDescribeDimensionKeysPartitionByTypeDef,
    _OptionalClientDescribeDimensionKeysPartitionByTypeDef,
):
    """
    Type definition for `ClientDescribeDimensionKeys` `PartitionBy`

    For each dimension specified in ``GroupBy`` , specify a secondary dimension to further subdivide
    the partition keys in the response.

    - **Group** *(string) --* **[REQUIRED]**

      The name of the dimension group. Valid values are:

      * ``db.user``

      * ``db.host``

      * ``db.sql``

      * ``db.sql_tokenized``

      * ``db.wait_event``

      * ``db.wait_event_type``

    - **Dimensions** *(list) --*

      A list of specific dimensions from a dimension group. If this parameter is not present, then it
      signifies that all of the dimensions in the group were requested, or are present in the
      response.

      Valid values for elements in the ``Dimensions`` array are:

      * db.user.id

      * db.user.name

      * db.host.id

      * db.host.name

      * db.sql.id

      * db.sql.db_id

      * db.sql.statement

      * db.sql.tokenized_id

      * db.sql_tokenized.id

      * db.sql_tokenized.db_id

      * db.sql_tokenized.statement

      * db.wait_event.name

      * db.wait_event.type

      * db.wait_event_type.name

      - *(string) --*

    - **Limit** *(integer) --*

      The maximum number of items to fetch for this dimension group.
    """


_ClientDescribeDimensionKeysResponseKeysTypeDef = TypedDict(
    "_ClientDescribeDimensionKeysResponseKeysTypeDef",
    {"Dimensions": Dict[str, str], "Total": float, "Partitions": List[float]},
    total=False,
)


class ClientDescribeDimensionKeysResponseKeysTypeDef(
    _ClientDescribeDimensionKeysResponseKeysTypeDef
):
    """
    Type definition for `ClientDescribeDimensionKeysResponse` `Keys`

    An array of descriptions and aggregated values for each dimension within a dimension group.

    - **Dimensions** *(dict) --*

      A map of name-value pairs for the dimensions in the group.

      - *(string) --*

        - *(string) --*

    - **Total** *(float) --*

      The aggregated metric value for the dimension(s), over the requested time range.

    - **Partitions** *(list) --*

      If ``PartitionBy`` was specified, ``PartitionKeys`` contains the dimensions that were.

      - *(float) --*
    """


_ClientDescribeDimensionKeysResponsePartitionKeysTypeDef = TypedDict(
    "_ClientDescribeDimensionKeysResponsePartitionKeysTypeDef",
    {"Dimensions": Dict[str, str]},
    total=False,
)


class ClientDescribeDimensionKeysResponsePartitionKeysTypeDef(
    _ClientDescribeDimensionKeysResponsePartitionKeysTypeDef
):
    """
    Type definition for `ClientDescribeDimensionKeysResponse` `PartitionKeys`

    If ``PartitionBy`` was specified in a ``DescribeDimensionKeys`` request, the dimensions are
    returned in an array. Each element in the array specifies one dimension.

    - **Dimensions** *(dict) --*

      A dimension map that contains the dimension(s) for this partition.

      - *(string) --*

        - *(string) --*
    """


_ClientDescribeDimensionKeysResponseTypeDef = TypedDict(
    "_ClientDescribeDimensionKeysResponseTypeDef",
    {
        "AlignedStartTime": datetime,
        "AlignedEndTime": datetime,
        "PartitionKeys": List[ClientDescribeDimensionKeysResponsePartitionKeysTypeDef],
        "Keys": List[ClientDescribeDimensionKeysResponseKeysTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeDimensionKeysResponseTypeDef(
    _ClientDescribeDimensionKeysResponseTypeDef
):
    """
    Type definition for `ClientDescribeDimensionKeys` `Response`

    - **AlignedStartTime** *(datetime) --*

      The start time for the returned dimension keys, after alignment to a granular boundary (as
      specified by ``PeriodInSeconds`` ). ``AlignedStartTime`` will be less than or equal to the
      value of the user-specified ``StartTime`` .

    - **AlignedEndTime** *(datetime) --*

      The end time for the returned dimension keys, after alignment to a granular boundary (as
      specified by ``PeriodInSeconds`` ). ``AlignedEndTime`` will be greater than or equal to the
      value of the user-specified ``Endtime`` .

    - **PartitionKeys** *(list) --*

      If ``PartitionBy`` was present in the request, ``PartitionKeys`` contains the breakdown of
      dimension keys by the specified partitions.

      - *(dict) --*

        If ``PartitionBy`` was specified in a ``DescribeDimensionKeys`` request, the dimensions are
        returned in an array. Each element in the array specifies one dimension.

        - **Dimensions** *(dict) --*

          A dimension map that contains the dimension(s) for this partition.

          - *(string) --*

            - *(string) --*

    - **Keys** *(list) --*

      The dimension keys that were requested.

      - *(dict) --*

        An array of descriptions and aggregated values for each dimension within a dimension group.

        - **Dimensions** *(dict) --*

          A map of name-value pairs for the dimensions in the group.

          - *(string) --*

            - *(string) --*

        - **Total** *(float) --*

          The aggregated metric value for the dimension(s), over the requested time range.

        - **Partitions** *(list) --*

          If ``PartitionBy`` was specified, ``PartitionKeys`` contains the dimensions that were.

          - *(float) --*

    - **NextToken** *(string) --*

      An optional pagination token provided by a previous request. If this parameter is specified,
      the response includes only records beyond the token, up to the value specified by
      ``MaxRecords`` .
    """


_RequiredClientGetResourceMetricsMetricQueriesGroupByTypeDef = TypedDict(
    "_RequiredClientGetResourceMetricsMetricQueriesGroupByTypeDef", {"Group": str}
)
_OptionalClientGetResourceMetricsMetricQueriesGroupByTypeDef = TypedDict(
    "_OptionalClientGetResourceMetricsMetricQueriesGroupByTypeDef",
    {"Dimensions": List[str], "Limit": int},
    total=False,
)


class ClientGetResourceMetricsMetricQueriesGroupByTypeDef(
    _RequiredClientGetResourceMetricsMetricQueriesGroupByTypeDef,
    _OptionalClientGetResourceMetricsMetricQueriesGroupByTypeDef,
):
    """
    Type definition for `ClientGetResourceMetricsMetricQueries` `GroupBy`

    A specification for how to aggregate the data points from a query result. You must specify a
    valid dimension group. Performance Insights will return all of the dimensions within that
    group, unless you provide the names of specific dimensions within that group. You can also
    request that Performance Insights return a limited number of values for a dimension.

    - **Group** *(string) --* **[REQUIRED]**

      The name of the dimension group. Valid values are:

      * ``db.user``

      * ``db.host``

      * ``db.sql``

      * ``db.sql_tokenized``

      * ``db.wait_event``

      * ``db.wait_event_type``

    - **Dimensions** *(list) --*

      A list of specific dimensions from a dimension group. If this parameter is not present,
      then it signifies that all of the dimensions in the group were requested, or are present in
      the response.

      Valid values for elements in the ``Dimensions`` array are:

      * db.user.id

      * db.user.name

      * db.host.id

      * db.host.name

      * db.sql.id

      * db.sql.db_id

      * db.sql.statement

      * db.sql.tokenized_id

      * db.sql_tokenized.id

      * db.sql_tokenized.db_id

      * db.sql_tokenized.statement

      * db.wait_event.name

      * db.wait_event.type

      * db.wait_event_type.name

      - *(string) --*

    - **Limit** *(integer) --*

      The maximum number of items to fetch for this dimension group.
    """


_RequiredClientGetResourceMetricsMetricQueriesTypeDef = TypedDict(
    "_RequiredClientGetResourceMetricsMetricQueriesTypeDef", {"Metric": str}
)
_OptionalClientGetResourceMetricsMetricQueriesTypeDef = TypedDict(
    "_OptionalClientGetResourceMetricsMetricQueriesTypeDef",
    {
        "GroupBy": ClientGetResourceMetricsMetricQueriesGroupByTypeDef,
        "Filter": Dict[str, str],
    },
    total=False,
)


class ClientGetResourceMetricsMetricQueriesTypeDef(
    _RequiredClientGetResourceMetricsMetricQueriesTypeDef,
    _OptionalClientGetResourceMetricsMetricQueriesTypeDef,
):
    """
    Type definition for `ClientGetResourceMetrics` `MetricQueries`

    A single query to be processed. You must provide the metric to query. If no other parameters
    are specified, Performance Insights returns all of the data points for that metric. You can
    optionally request that the data points be aggregated by dimension group ( ``GroupBy`` ), and
    return only those data points that match your criteria (``Filter`` ).

    - **Metric** *(string) --* **[REQUIRED]**

      The name of a Performance Insights metric to be measured.

      Valid values for ``Metric`` are:

      * ``db.load.avg`` - a scaled representation of the number of active sessions for the database
      engine.

      * ``db.sampledload.avg`` - the raw number of active sessions for the database engine.

    - **GroupBy** *(dict) --*

      A specification for how to aggregate the data points from a query result. You must specify a
      valid dimension group. Performance Insights will return all of the dimensions within that
      group, unless you provide the names of specific dimensions within that group. You can also
      request that Performance Insights return a limited number of values for a dimension.

      - **Group** *(string) --* **[REQUIRED]**

        The name of the dimension group. Valid values are:

        * ``db.user``

        * ``db.host``

        * ``db.sql``

        * ``db.sql_tokenized``

        * ``db.wait_event``

        * ``db.wait_event_type``

      - **Dimensions** *(list) --*

        A list of specific dimensions from a dimension group. If this parameter is not present,
        then it signifies that all of the dimensions in the group were requested, or are present in
        the response.

        Valid values for elements in the ``Dimensions`` array are:

        * db.user.id

        * db.user.name

        * db.host.id

        * db.host.name

        * db.sql.id

        * db.sql.db_id

        * db.sql.statement

        * db.sql.tokenized_id

        * db.sql_tokenized.id

        * db.sql_tokenized.db_id

        * db.sql_tokenized.statement

        * db.wait_event.name

        * db.wait_event.type

        * db.wait_event_type.name

        - *(string) --*

      - **Limit** *(integer) --*

        The maximum number of items to fetch for this dimension group.

    - **Filter** *(dict) --*

      One or more filters to apply in the request. Restrictions:

      * Any number of filters by the same dimension, as specified in the ``GroupBy`` parameter.

      * A single filter for any other dimension in this dimension group.

      - *(string) --*

        - *(string) --*
    """


_ClientGetResourceMetricsResponseMetricListDataPointsTypeDef = TypedDict(
    "_ClientGetResourceMetricsResponseMetricListDataPointsTypeDef",
    {"Timestamp": datetime, "Value": float},
    total=False,
)


class ClientGetResourceMetricsResponseMetricListDataPointsTypeDef(
    _ClientGetResourceMetricsResponseMetricListDataPointsTypeDef
):
    """
    Type definition for `ClientGetResourceMetricsResponseMetricList` `DataPoints`

    A timestamp, and a single numerical value, which together represent a measurement at a
    particular point in time.

    - **Timestamp** *(datetime) --*

      The time, in epoch format, associated with a particular ``Value`` .

    - **Value** *(float) --*

      The actual value associated with a particular ``Timestamp`` .
    """


_ClientGetResourceMetricsResponseMetricListKeyTypeDef = TypedDict(
    "_ClientGetResourceMetricsResponseMetricListKeyTypeDef",
    {"Metric": str, "Dimensions": Dict[str, str]},
    total=False,
)


class ClientGetResourceMetricsResponseMetricListKeyTypeDef(
    _ClientGetResourceMetricsResponseMetricListKeyTypeDef
):
    """
    Type definition for `ClientGetResourceMetricsResponseMetricList` `Key`

    The dimension(s) to which the data points apply.

    - **Metric** *(string) --*

      The name of a Performance Insights metric to be measured.

      Valid values for ``Metric`` are:

      * ``db.load.avg`` - a scaled representation of the number of active sessions for the
      database engine.

      * ``db.sampledload.avg`` - the raw number of active sessions for the database engine.

    - **Dimensions** *(dict) --*

      The valid dimensions for the metric.

      - *(string) --*

        - *(string) --*
    """


_ClientGetResourceMetricsResponseMetricListTypeDef = TypedDict(
    "_ClientGetResourceMetricsResponseMetricListTypeDef",
    {
        "Key": ClientGetResourceMetricsResponseMetricListKeyTypeDef,
        "DataPoints": List[ClientGetResourceMetricsResponseMetricListDataPointsTypeDef],
    },
    total=False,
)


class ClientGetResourceMetricsResponseMetricListTypeDef(
    _ClientGetResourceMetricsResponseMetricListTypeDef
):
    """
    Type definition for `ClientGetResourceMetricsResponse` `MetricList`

    A time-ordered series of data points, correpsonding to a dimension of a Performance
    Insights metric.

    - **Key** *(dict) --*

      The dimension(s) to which the data points apply.

      - **Metric** *(string) --*

        The name of a Performance Insights metric to be measured.

        Valid values for ``Metric`` are:

        * ``db.load.avg`` - a scaled representation of the number of active sessions for the
        database engine.

        * ``db.sampledload.avg`` - the raw number of active sessions for the database engine.

      - **Dimensions** *(dict) --*

        The valid dimensions for the metric.

        - *(string) --*

          - *(string) --*

    - **DataPoints** *(list) --*

      An array of timestamp-value pairs, representing measurements over a period of time.

      - *(dict) --*

        A timestamp, and a single numerical value, which together represent a measurement at a
        particular point in time.

        - **Timestamp** *(datetime) --*

          The time, in epoch format, associated with a particular ``Value`` .

        - **Value** *(float) --*

          The actual value associated with a particular ``Timestamp`` .
    """


_ClientGetResourceMetricsResponseTypeDef = TypedDict(
    "_ClientGetResourceMetricsResponseTypeDef",
    {
        "AlignedStartTime": datetime,
        "AlignedEndTime": datetime,
        "Identifier": str,
        "MetricList": List[ClientGetResourceMetricsResponseMetricListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientGetResourceMetricsResponseTypeDef(_ClientGetResourceMetricsResponseTypeDef):
    """
    Type definition for `ClientGetResourceMetrics` `Response`

    - **AlignedStartTime** *(datetime) --*

      The start time for the returned metrics, after alignment to a granular boundary (as specified
      by ``PeriodInSeconds`` ). ``AlignedStartTime`` will be less than or equal to the value of the
      user-specified ``StartTime`` .

    - **AlignedEndTime** *(datetime) --*

      The end time for the returned metrics, after alignment to a granular boundary (as specified
      by ``PeriodInSeconds`` ). ``AlignedEndTime`` will be greater than or equal to the value of
      the user-specified ``Endtime`` .

    - **Identifier** *(string) --*

      An immutable, AWS Region-unique identifier for a data source. Performance Insights gathers
      metrics from this data source.

      To use an Amazon RDS instance as a data source, you specify its ``DbiResourceId`` value - for
      example: ``db-FAIHNTYBKTGAUSUZQYPDS2GW4A``

    - **MetricList** *(list) --*

      An array of metric results,, where each array element contains all of the data points for a
      particular dimension.

      - *(dict) --*

        A time-ordered series of data points, correpsonding to a dimension of a Performance
        Insights metric.

        - **Key** *(dict) --*

          The dimension(s) to which the data points apply.

          - **Metric** *(string) --*

            The name of a Performance Insights metric to be measured.

            Valid values for ``Metric`` are:

            * ``db.load.avg`` - a scaled representation of the number of active sessions for the
            database engine.

            * ``db.sampledload.avg`` - the raw number of active sessions for the database engine.

          - **Dimensions** *(dict) --*

            The valid dimensions for the metric.

            - *(string) --*

              - *(string) --*

        - **DataPoints** *(list) --*

          An array of timestamp-value pairs, representing measurements over a period of time.

          - *(dict) --*

            A timestamp, and a single numerical value, which together represent a measurement at a
            particular point in time.

            - **Timestamp** *(datetime) --*

              The time, in epoch format, associated with a particular ``Value`` .

            - **Value** *(float) --*

              The actual value associated with a particular ``Timestamp`` .

    - **NextToken** *(string) --*

      An optional pagination token provided by a previous request. If this parameter is specified,
      the response includes only records beyond the token, up to the value specified by
      ``MaxRecords`` .
    """
