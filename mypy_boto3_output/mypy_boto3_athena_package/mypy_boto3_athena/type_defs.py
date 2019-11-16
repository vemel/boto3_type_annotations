"Main interface for athena type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientBatchGetNamedQueryResponseNamedQueriesTypeDef",
    "ClientBatchGetNamedQueryResponseUnprocessedNamedQueryIdsTypeDef",
    "ClientBatchGetNamedQueryResponseTypeDef",
    "ClientBatchGetQueryExecutionResponseQueryExecutionsQueryExecutionContextTypeDef",
    "ClientBatchGetQueryExecutionResponseQueryExecutionsResultConfigurationEncryptionConfigurationTypeDef",
    "ClientBatchGetQueryExecutionResponseQueryExecutionsResultConfigurationTypeDef",
    "ClientBatchGetQueryExecutionResponseQueryExecutionsStatisticsTypeDef",
    "ClientBatchGetQueryExecutionResponseQueryExecutionsStatusTypeDef",
    "ClientBatchGetQueryExecutionResponseQueryExecutionsTypeDef",
    "ClientBatchGetQueryExecutionResponseUnprocessedQueryExecutionIdsTypeDef",
    "ClientBatchGetQueryExecutionResponseTypeDef",
    "ClientCreateNamedQueryResponseTypeDef",
    "ClientCreateWorkGroupConfigurationResultConfigurationEncryptionConfigurationTypeDef",
    "ClientCreateWorkGroupConfigurationResultConfigurationTypeDef",
    "ClientCreateWorkGroupConfigurationTypeDef",
    "ClientCreateWorkGroupTagsTypeDef",
    "ClientGetNamedQueryResponseNamedQueryTypeDef",
    "ClientGetNamedQueryResponseTypeDef",
    "ClientGetQueryExecutionResponseQueryExecutionQueryExecutionContextTypeDef",
    "ClientGetQueryExecutionResponseQueryExecutionResultConfigurationEncryptionConfigurationTypeDef",
    "ClientGetQueryExecutionResponseQueryExecutionResultConfigurationTypeDef",
    "ClientGetQueryExecutionResponseQueryExecutionStatisticsTypeDef",
    "ClientGetQueryExecutionResponseQueryExecutionStatusTypeDef",
    "ClientGetQueryExecutionResponseQueryExecutionTypeDef",
    "ClientGetQueryExecutionResponseTypeDef",
    "ClientGetQueryResultsResponseResultSetResultSetMetadataColumnInfoTypeDef",
    "ClientGetQueryResultsResponseResultSetResultSetMetadataTypeDef",
    "ClientGetQueryResultsResponseResultSetRowsDataTypeDef",
    "ClientGetQueryResultsResponseResultSetRowsTypeDef",
    "ClientGetQueryResultsResponseResultSetTypeDef",
    "ClientGetQueryResultsResponseTypeDef",
    "ClientGetWorkGroupResponseWorkGroupConfigurationResultConfigurationEncryptionConfigurationTypeDef",
    "ClientGetWorkGroupResponseWorkGroupConfigurationResultConfigurationTypeDef",
    "ClientGetWorkGroupResponseWorkGroupConfigurationTypeDef",
    "ClientGetWorkGroupResponseWorkGroupTypeDef",
    "ClientGetWorkGroupResponseTypeDef",
    "ClientListNamedQueriesResponseTypeDef",
    "ClientListQueryExecutionsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListWorkGroupsResponseWorkGroupsTypeDef",
    "ClientListWorkGroupsResponseTypeDef",
    "ClientStartQueryExecutionQueryExecutionContextTypeDef",
    "ClientStartQueryExecutionResponseTypeDef",
    "ClientStartQueryExecutionResultConfigurationEncryptionConfigurationTypeDef",
    "ClientStartQueryExecutionResultConfigurationTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateWorkGroupConfigurationUpdatesResultConfigurationUpdatesEncryptionConfigurationTypeDef",
    "ClientUpdateWorkGroupConfigurationUpdatesResultConfigurationUpdatesTypeDef",
    "ClientUpdateWorkGroupConfigurationUpdatesTypeDef",
    "GetQueryResultsPaginatePaginationConfigTypeDef",
    "GetQueryResultsPaginateResponseResultSetResultSetMetadataColumnInfoTypeDef",
    "GetQueryResultsPaginateResponseResultSetResultSetMetadataTypeDef",
    "GetQueryResultsPaginateResponseResultSetRowsDataTypeDef",
    "GetQueryResultsPaginateResponseResultSetRowsTypeDef",
    "GetQueryResultsPaginateResponseResultSetTypeDef",
    "GetQueryResultsPaginateResponseTypeDef",
    "ListNamedQueriesPaginatePaginationConfigTypeDef",
    "ListNamedQueriesPaginateResponseTypeDef",
    "ListQueryExecutionsPaginatePaginationConfigTypeDef",
    "ListQueryExecutionsPaginateResponseTypeDef",
)


_ClientBatchGetNamedQueryResponseNamedQueriesTypeDef = TypedDict(
    "_ClientBatchGetNamedQueryResponseNamedQueriesTypeDef",
    {
        "Name": str,
        "Description": str,
        "Database": str,
        "QueryString": str,
        "NamedQueryId": str,
        "WorkGroup": str,
    },
    total=False,
)


class ClientBatchGetNamedQueryResponseNamedQueriesTypeDef(
    _ClientBatchGetNamedQueryResponseNamedQueriesTypeDef
):
    """
    Type definition for `ClientBatchGetNamedQueryResponse` `NamedQueries`

    A query, where ``QueryString`` is the list of SQL query statements that comprise the query.

    - **Name** *(string) --*

      The query name.

    - **Description** *(string) --*

      The query description.

    - **Database** *(string) --*

      The database to which the query belongs.

    - **QueryString** *(string) --*

      The SQL query statements that comprise the query.

    - **NamedQueryId** *(string) --*

      The unique identifier of the query.

    - **WorkGroup** *(string) --*

      The name of the workgroup that contains the named query.
    """


_ClientBatchGetNamedQueryResponseUnprocessedNamedQueryIdsTypeDef = TypedDict(
    "_ClientBatchGetNamedQueryResponseUnprocessedNamedQueryIdsTypeDef",
    {"NamedQueryId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchGetNamedQueryResponseUnprocessedNamedQueryIdsTypeDef(
    _ClientBatchGetNamedQueryResponseUnprocessedNamedQueryIdsTypeDef
):
    """
    Type definition for `ClientBatchGetNamedQueryResponse` `UnprocessedNamedQueryIds`

    Information about a named query ID that could not be processed.

    - **NamedQueryId** *(string) --*

      The unique identifier of the named query.

    - **ErrorCode** *(string) --*

      The error code returned when the processing request for the named query failed, if
      applicable.

    - **ErrorMessage** *(string) --*

      The error message returned when the processing request for the named query failed, if
      applicable.
    """


_ClientBatchGetNamedQueryResponseTypeDef = TypedDict(
    "_ClientBatchGetNamedQueryResponseTypeDef",
    {
        "NamedQueries": List[ClientBatchGetNamedQueryResponseNamedQueriesTypeDef],
        "UnprocessedNamedQueryIds": List[
            ClientBatchGetNamedQueryResponseUnprocessedNamedQueryIdsTypeDef
        ],
    },
    total=False,
)


class ClientBatchGetNamedQueryResponseTypeDef(_ClientBatchGetNamedQueryResponseTypeDef):
    """
    Type definition for `ClientBatchGetNamedQuery` `Response`

    - **NamedQueries** *(list) --*

      Information about the named query IDs submitted.

      - *(dict) --*

        A query, where ``QueryString`` is the list of SQL query statements that comprise the query.

        - **Name** *(string) --*

          The query name.

        - **Description** *(string) --*

          The query description.

        - **Database** *(string) --*

          The database to which the query belongs.

        - **QueryString** *(string) --*

          The SQL query statements that comprise the query.

        - **NamedQueryId** *(string) --*

          The unique identifier of the query.

        - **WorkGroup** *(string) --*

          The name of the workgroup that contains the named query.

    - **UnprocessedNamedQueryIds** *(list) --*

      Information about provided query IDs.

      - *(dict) --*

        Information about a named query ID that could not be processed.

        - **NamedQueryId** *(string) --*

          The unique identifier of the named query.

        - **ErrorCode** *(string) --*

          The error code returned when the processing request for the named query failed, if
          applicable.

        - **ErrorMessage** *(string) --*

          The error message returned when the processing request for the named query failed, if
          applicable.
    """


_ClientBatchGetQueryExecutionResponseQueryExecutionsQueryExecutionContextTypeDef = TypedDict(
    "_ClientBatchGetQueryExecutionResponseQueryExecutionsQueryExecutionContextTypeDef",
    {"Database": str},
    total=False,
)


class ClientBatchGetQueryExecutionResponseQueryExecutionsQueryExecutionContextTypeDef(
    _ClientBatchGetQueryExecutionResponseQueryExecutionsQueryExecutionContextTypeDef
):
    """
    Type definition for `ClientBatchGetQueryExecutionResponseQueryExecutions` `QueryExecutionContext`

    The database in which the query execution occurred.

    - **Database** *(string) --*

      The name of the database.
    """


_ClientBatchGetQueryExecutionResponseQueryExecutionsResultConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "_ClientBatchGetQueryExecutionResponseQueryExecutionsResultConfigurationEncryptionConfigurationTypeDef",
    {"EncryptionOption": str, "KmsKey": str},
    total=False,
)


class ClientBatchGetQueryExecutionResponseQueryExecutionsResultConfigurationEncryptionConfigurationTypeDef(
    _ClientBatchGetQueryExecutionResponseQueryExecutionsResultConfigurationEncryptionConfigurationTypeDef
):
    """
    Type definition for `ClientBatchGetQueryExecutionResponseQueryExecutionsResultConfiguration` `EncryptionConfiguration`

    If query results are encrypted in Amazon S3, indicates the encryption option used (for
    example, ``SSE-KMS`` or ``CSE-KMS`` ) and key information. This is a client-side
    setting. If workgroup settings override client-side settings, then the query uses the
    encryption configuration that is specified for the workgroup, and also uses the
    location for storing query results specified in the workgroup. See
    WorkGroupConfiguration$EnforceWorkGroupConfiguration and `Workgroup Settings Override
    Client-Side Settings
    <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`__ .

    - **EncryptionOption** *(string) --*

      Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys
      (``SSE-S3`` ), server-side encryption with KMS-managed keys (``SSE-KMS`` ), or
      client-side encryption with KMS-managed keys (CSE-KMS) is used.

      If a query runs in a workgroup and the workgroup overrides client-side settings, then
      the workgroup's setting for encryption is used. It specifies whether query results
      must be encrypted, for all queries that run in this workgroup.

    - **KmsKey** *(string) --*

      For ``SSE-KMS`` and ``CSE-KMS`` , this is the KMS key ARN or ID.
    """


_ClientBatchGetQueryExecutionResponseQueryExecutionsResultConfigurationTypeDef = TypedDict(
    "_ClientBatchGetQueryExecutionResponseQueryExecutionsResultConfigurationTypeDef",
    {
        "OutputLocation": str,
        "EncryptionConfiguration": ClientBatchGetQueryExecutionResponseQueryExecutionsResultConfigurationEncryptionConfigurationTypeDef,
    },
    total=False,
)


class ClientBatchGetQueryExecutionResponseQueryExecutionsResultConfigurationTypeDef(
    _ClientBatchGetQueryExecutionResponseQueryExecutionsResultConfigurationTypeDef
):
    """
    Type definition for `ClientBatchGetQueryExecutionResponseQueryExecutions` `ResultConfiguration`

    The location in Amazon S3 where query results were stored and the encryption option, if
    any, used for query results. These are known as "client-side settings". If workgroup
    settings override client-side settings, then the query uses the location for the query
    results and the encryption configuration that are specified for the workgroup.

    - **OutputLocation** *(string) --*

      The location in Amazon S3 where your query results are stored, such as
      ``s3://path/to/query/bucket/`` . To run the query, you must specify the query results
      location using one of the ways: either for individual queries using either this setting
      (client-side), or in the workgroup, using  WorkGroupConfiguration . If none of them is
      set, Athena issues an error that no output location is provided. For more information,
      see `Query Results <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`__ . If
      workgroup settings override client-side settings, then the query uses the settings
      specified for the workgroup. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration .

    - **EncryptionConfiguration** *(dict) --*

      If query results are encrypted in Amazon S3, indicates the encryption option used (for
      example, ``SSE-KMS`` or ``CSE-KMS`` ) and key information. This is a client-side
      setting. If workgroup settings override client-side settings, then the query uses the
      encryption configuration that is specified for the workgroup, and also uses the
      location for storing query results specified in the workgroup. See
      WorkGroupConfiguration$EnforceWorkGroupConfiguration and `Workgroup Settings Override
      Client-Side Settings
      <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`__ .

      - **EncryptionOption** *(string) --*

        Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys
        (``SSE-S3`` ), server-side encryption with KMS-managed keys (``SSE-KMS`` ), or
        client-side encryption with KMS-managed keys (CSE-KMS) is used.

        If a query runs in a workgroup and the workgroup overrides client-side settings, then
        the workgroup's setting for encryption is used. It specifies whether query results
        must be encrypted, for all queries that run in this workgroup.

      - **KmsKey** *(string) --*

        For ``SSE-KMS`` and ``CSE-KMS`` , this is the KMS key ARN or ID.
    """


_ClientBatchGetQueryExecutionResponseQueryExecutionsStatisticsTypeDef = TypedDict(
    "_ClientBatchGetQueryExecutionResponseQueryExecutionsStatisticsTypeDef",
    {
        "EngineExecutionTimeInMillis": int,
        "DataScannedInBytes": int,
        "DataManifestLocation": str,
    },
    total=False,
)


class ClientBatchGetQueryExecutionResponseQueryExecutionsStatisticsTypeDef(
    _ClientBatchGetQueryExecutionResponseQueryExecutionsStatisticsTypeDef
):
    """
    Type definition for `ClientBatchGetQueryExecutionResponseQueryExecutions` `Statistics`

    The location of a manifest file that tracks file locations generated by the query, the
    amount of data scanned by the query, and the amount of time that it took the query to run.

    - **EngineExecutionTimeInMillis** *(integer) --*

      The number of milliseconds that the query took to execute.

    - **DataScannedInBytes** *(integer) --*

      The number of bytes in the data that was queried.

    - **DataManifestLocation** *(string) --*

      The location and file name of a data manifest file. The manifest file is saved to the
      Athena query results location in Amazon S3. It tracks files that the query wrote to
      Amazon S3. If the query fails, the manifest file also tracks files that the query
      intended to write. The manifest is useful for identifying orphaned files resulting from
      a failed query. For more information, see `Working with Query Output Files
      <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`__ in the *Amazon Athena
      User Guide* .
    """


_ClientBatchGetQueryExecutionResponseQueryExecutionsStatusTypeDef = TypedDict(
    "_ClientBatchGetQueryExecutionResponseQueryExecutionsStatusTypeDef",
    {
        "State": str,
        "StateChangeReason": str,
        "SubmissionDateTime": datetime,
        "CompletionDateTime": datetime,
    },
    total=False,
)


class ClientBatchGetQueryExecutionResponseQueryExecutionsStatusTypeDef(
    _ClientBatchGetQueryExecutionResponseQueryExecutionsStatusTypeDef
):
    """
    Type definition for `ClientBatchGetQueryExecutionResponseQueryExecutions` `Status`

    The completion date, current state, submission time, and state change reason (if
    applicable) for the query execution.

    - **State** *(string) --*

      The state of query execution. ``QUEUED`` state is listed but is not used by Athena and
      is reserved for future use. ``RUNNING`` indicates that the query has been submitted to
      the service, and Athena will execute the query as soon as resources are available.
      ``SUCCEEDED`` indicates that the query completed without errors. ``FAILED`` indicates
      that the query experienced an error and did not complete processing. ``CANCELLED``
      indicates that a user input interrupted query execution.

    - **StateChangeReason** *(string) --*

      Further detail about the status of the query.

    - **SubmissionDateTime** *(datetime) --*

      The date and time that the query was submitted.

    - **CompletionDateTime** *(datetime) --*

      The date and time that the query completed.
    """


_ClientBatchGetQueryExecutionResponseQueryExecutionsTypeDef = TypedDict(
    "_ClientBatchGetQueryExecutionResponseQueryExecutionsTypeDef",
    {
        "QueryExecutionId": str,
        "Query": str,
        "StatementType": str,
        "ResultConfiguration": ClientBatchGetQueryExecutionResponseQueryExecutionsResultConfigurationTypeDef,
        "QueryExecutionContext": ClientBatchGetQueryExecutionResponseQueryExecutionsQueryExecutionContextTypeDef,
        "Status": ClientBatchGetQueryExecutionResponseQueryExecutionsStatusTypeDef,
        "Statistics": ClientBatchGetQueryExecutionResponseQueryExecutionsStatisticsTypeDef,
        "WorkGroup": str,
    },
    total=False,
)


class ClientBatchGetQueryExecutionResponseQueryExecutionsTypeDef(
    _ClientBatchGetQueryExecutionResponseQueryExecutionsTypeDef
):
    """
    Type definition for `ClientBatchGetQueryExecutionResponse` `QueryExecutions`

    Information about a single instance of a query execution.

    - **QueryExecutionId** *(string) --*

      The unique identifier for each query execution.

    - **Query** *(string) --*

      The SQL query statements which the query execution ran.

    - **StatementType** *(string) --*

      The type of query statement that was run. ``DDL`` indicates DDL query statements. ``DML``
      indicates DML (Data Manipulation Language) query statements, such as ``CREATE TABLE AS
      SELECT`` . ``UTILITY`` indicates query statements other than DDL and DML, such as ``SHOW
      CREATE TABLE`` , or ``DESCRIBE <table>`` .

    - **ResultConfiguration** *(dict) --*

      The location in Amazon S3 where query results were stored and the encryption option, if
      any, used for query results. These are known as "client-side settings". If workgroup
      settings override client-side settings, then the query uses the location for the query
      results and the encryption configuration that are specified for the workgroup.

      - **OutputLocation** *(string) --*

        The location in Amazon S3 where your query results are stored, such as
        ``s3://path/to/query/bucket/`` . To run the query, you must specify the query results
        location using one of the ways: either for individual queries using either this setting
        (client-side), or in the workgroup, using  WorkGroupConfiguration . If none of them is
        set, Athena issues an error that no output location is provided. For more information,
        see `Query Results <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`__ . If
        workgroup settings override client-side settings, then the query uses the settings
        specified for the workgroup. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration .

      - **EncryptionConfiguration** *(dict) --*

        If query results are encrypted in Amazon S3, indicates the encryption option used (for
        example, ``SSE-KMS`` or ``CSE-KMS`` ) and key information. This is a client-side
        setting. If workgroup settings override client-side settings, then the query uses the
        encryption configuration that is specified for the workgroup, and also uses the
        location for storing query results specified in the workgroup. See
        WorkGroupConfiguration$EnforceWorkGroupConfiguration and `Workgroup Settings Override
        Client-Side Settings
        <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`__ .

        - **EncryptionOption** *(string) --*

          Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys
          (``SSE-S3`` ), server-side encryption with KMS-managed keys (``SSE-KMS`` ), or
          client-side encryption with KMS-managed keys (CSE-KMS) is used.

          If a query runs in a workgroup and the workgroup overrides client-side settings, then
          the workgroup's setting for encryption is used. It specifies whether query results
          must be encrypted, for all queries that run in this workgroup.

        - **KmsKey** *(string) --*

          For ``SSE-KMS`` and ``CSE-KMS`` , this is the KMS key ARN or ID.

    - **QueryExecutionContext** *(dict) --*

      The database in which the query execution occurred.

      - **Database** *(string) --*

        The name of the database.

    - **Status** *(dict) --*

      The completion date, current state, submission time, and state change reason (if
      applicable) for the query execution.

      - **State** *(string) --*

        The state of query execution. ``QUEUED`` state is listed but is not used by Athena and
        is reserved for future use. ``RUNNING`` indicates that the query has been submitted to
        the service, and Athena will execute the query as soon as resources are available.
        ``SUCCEEDED`` indicates that the query completed without errors. ``FAILED`` indicates
        that the query experienced an error and did not complete processing. ``CANCELLED``
        indicates that a user input interrupted query execution.

      - **StateChangeReason** *(string) --*

        Further detail about the status of the query.

      - **SubmissionDateTime** *(datetime) --*

        The date and time that the query was submitted.

      - **CompletionDateTime** *(datetime) --*

        The date and time that the query completed.

    - **Statistics** *(dict) --*

      The location of a manifest file that tracks file locations generated by the query, the
      amount of data scanned by the query, and the amount of time that it took the query to run.

      - **EngineExecutionTimeInMillis** *(integer) --*

        The number of milliseconds that the query took to execute.

      - **DataScannedInBytes** *(integer) --*

        The number of bytes in the data that was queried.

      - **DataManifestLocation** *(string) --*

        The location and file name of a data manifest file. The manifest file is saved to the
        Athena query results location in Amazon S3. It tracks files that the query wrote to
        Amazon S3. If the query fails, the manifest file also tracks files that the query
        intended to write. The manifest is useful for identifying orphaned files resulting from
        a failed query. For more information, see `Working with Query Output Files
        <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`__ in the *Amazon Athena
        User Guide* .

    - **WorkGroup** *(string) --*

      The name of the workgroup in which the query ran.
    """


_ClientBatchGetQueryExecutionResponseUnprocessedQueryExecutionIdsTypeDef = TypedDict(
    "_ClientBatchGetQueryExecutionResponseUnprocessedQueryExecutionIdsTypeDef",
    {"QueryExecutionId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchGetQueryExecutionResponseUnprocessedQueryExecutionIdsTypeDef(
    _ClientBatchGetQueryExecutionResponseUnprocessedQueryExecutionIdsTypeDef
):
    """
    Type definition for `ClientBatchGetQueryExecutionResponse` `UnprocessedQueryExecutionIds`

    Describes a query execution that failed to process.

    - **QueryExecutionId** *(string) --*

      The unique identifier of the query execution.

    - **ErrorCode** *(string) --*

      The error code returned when the query execution failed to process, if applicable.

    - **ErrorMessage** *(string) --*

      The error message returned when the query execution failed to process, if applicable.
    """


_ClientBatchGetQueryExecutionResponseTypeDef = TypedDict(
    "_ClientBatchGetQueryExecutionResponseTypeDef",
    {
        "QueryExecutions": List[
            ClientBatchGetQueryExecutionResponseQueryExecutionsTypeDef
        ],
        "UnprocessedQueryExecutionIds": List[
            ClientBatchGetQueryExecutionResponseUnprocessedQueryExecutionIdsTypeDef
        ],
    },
    total=False,
)


class ClientBatchGetQueryExecutionResponseTypeDef(
    _ClientBatchGetQueryExecutionResponseTypeDef
):
    """
    Type definition for `ClientBatchGetQueryExecution` `Response`

    - **QueryExecutions** *(list) --*

      Information about a query execution.

      - *(dict) --*

        Information about a single instance of a query execution.

        - **QueryExecutionId** *(string) --*

          The unique identifier for each query execution.

        - **Query** *(string) --*

          The SQL query statements which the query execution ran.

        - **StatementType** *(string) --*

          The type of query statement that was run. ``DDL`` indicates DDL query statements. ``DML``
          indicates DML (Data Manipulation Language) query statements, such as ``CREATE TABLE AS
          SELECT`` . ``UTILITY`` indicates query statements other than DDL and DML, such as ``SHOW
          CREATE TABLE`` , or ``DESCRIBE <table>`` .

        - **ResultConfiguration** *(dict) --*

          The location in Amazon S3 where query results were stored and the encryption option, if
          any, used for query results. These are known as "client-side settings". If workgroup
          settings override client-side settings, then the query uses the location for the query
          results and the encryption configuration that are specified for the workgroup.

          - **OutputLocation** *(string) --*

            The location in Amazon S3 where your query results are stored, such as
            ``s3://path/to/query/bucket/`` . To run the query, you must specify the query results
            location using one of the ways: either for individual queries using either this setting
            (client-side), or in the workgroup, using  WorkGroupConfiguration . If none of them is
            set, Athena issues an error that no output location is provided. For more information,
            see `Query Results <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`__ . If
            workgroup settings override client-side settings, then the query uses the settings
            specified for the workgroup. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration .

          - **EncryptionConfiguration** *(dict) --*

            If query results are encrypted in Amazon S3, indicates the encryption option used (for
            example, ``SSE-KMS`` or ``CSE-KMS`` ) and key information. This is a client-side
            setting. If workgroup settings override client-side settings, then the query uses the
            encryption configuration that is specified for the workgroup, and also uses the
            location for storing query results specified in the workgroup. See
            WorkGroupConfiguration$EnforceWorkGroupConfiguration and `Workgroup Settings Override
            Client-Side Settings
            <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`__ .

            - **EncryptionOption** *(string) --*

              Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys
              (``SSE-S3`` ), server-side encryption with KMS-managed keys (``SSE-KMS`` ), or
              client-side encryption with KMS-managed keys (CSE-KMS) is used.

              If a query runs in a workgroup and the workgroup overrides client-side settings, then
              the workgroup's setting for encryption is used. It specifies whether query results
              must be encrypted, for all queries that run in this workgroup.

            - **KmsKey** *(string) --*

              For ``SSE-KMS`` and ``CSE-KMS`` , this is the KMS key ARN or ID.

        - **QueryExecutionContext** *(dict) --*

          The database in which the query execution occurred.

          - **Database** *(string) --*

            The name of the database.

        - **Status** *(dict) --*

          The completion date, current state, submission time, and state change reason (if
          applicable) for the query execution.

          - **State** *(string) --*

            The state of query execution. ``QUEUED`` state is listed but is not used by Athena and
            is reserved for future use. ``RUNNING`` indicates that the query has been submitted to
            the service, and Athena will execute the query as soon as resources are available.
            ``SUCCEEDED`` indicates that the query completed without errors. ``FAILED`` indicates
            that the query experienced an error and did not complete processing. ``CANCELLED``
            indicates that a user input interrupted query execution.

          - **StateChangeReason** *(string) --*

            Further detail about the status of the query.

          - **SubmissionDateTime** *(datetime) --*

            The date and time that the query was submitted.

          - **CompletionDateTime** *(datetime) --*

            The date and time that the query completed.

        - **Statistics** *(dict) --*

          The location of a manifest file that tracks file locations generated by the query, the
          amount of data scanned by the query, and the amount of time that it took the query to run.

          - **EngineExecutionTimeInMillis** *(integer) --*

            The number of milliseconds that the query took to execute.

          - **DataScannedInBytes** *(integer) --*

            The number of bytes in the data that was queried.

          - **DataManifestLocation** *(string) --*

            The location and file name of a data manifest file. The manifest file is saved to the
            Athena query results location in Amazon S3. It tracks files that the query wrote to
            Amazon S3. If the query fails, the manifest file also tracks files that the query
            intended to write. The manifest is useful for identifying orphaned files resulting from
            a failed query. For more information, see `Working with Query Output Files
            <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`__ in the *Amazon Athena
            User Guide* .

        - **WorkGroup** *(string) --*

          The name of the workgroup in which the query ran.

    - **UnprocessedQueryExecutionIds** *(list) --*

      Information about the query executions that failed to run.

      - *(dict) --*

        Describes a query execution that failed to process.

        - **QueryExecutionId** *(string) --*

          The unique identifier of the query execution.

        - **ErrorCode** *(string) --*

          The error code returned when the query execution failed to process, if applicable.

        - **ErrorMessage** *(string) --*

          The error message returned when the query execution failed to process, if applicable.
    """


_ClientCreateNamedQueryResponseTypeDef = TypedDict(
    "_ClientCreateNamedQueryResponseTypeDef", {"NamedQueryId": str}, total=False
)


class ClientCreateNamedQueryResponseTypeDef(_ClientCreateNamedQueryResponseTypeDef):
    """
    Type definition for `ClientCreateNamedQuery` `Response`

    - **NamedQueryId** *(string) --*

      The unique ID of the query.
    """


_RequiredClientCreateWorkGroupConfigurationResultConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateWorkGroupConfigurationResultConfigurationEncryptionConfigurationTypeDef",
    {"EncryptionOption": str},
)
_OptionalClientCreateWorkGroupConfigurationResultConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateWorkGroupConfigurationResultConfigurationEncryptionConfigurationTypeDef",
    {"KmsKey": str},
    total=False,
)


class ClientCreateWorkGroupConfigurationResultConfigurationEncryptionConfigurationTypeDef(
    _RequiredClientCreateWorkGroupConfigurationResultConfigurationEncryptionConfigurationTypeDef,
    _OptionalClientCreateWorkGroupConfigurationResultConfigurationEncryptionConfigurationTypeDef,
):
    """
    Type definition for `ClientCreateWorkGroupConfigurationResultConfiguration` `EncryptionConfiguration`

    If query results are encrypted in Amazon S3, indicates the encryption option used (for
    example, ``SSE-KMS`` or ``CSE-KMS`` ) and key information. This is a client-side setting. If
    workgroup settings override client-side settings, then the query uses the encryption
    configuration that is specified for the workgroup, and also uses the location for storing
    query results specified in the workgroup. See
    WorkGroupConfiguration$EnforceWorkGroupConfiguration and `Workgroup Settings Override
    Client-Side Settings
    <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`__ .

    - **EncryptionOption** *(string) --* **[REQUIRED]**

      Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (``SSE-S3``
      ), server-side encryption with KMS-managed keys (``SSE-KMS`` ), or client-side encryption
      with KMS-managed keys (CSE-KMS) is used.

      If a query runs in a workgroup and the workgroup overrides client-side settings, then the
      workgroup's setting for encryption is used. It specifies whether query results must be
      encrypted, for all queries that run in this workgroup.

    - **KmsKey** *(string) --*

      For ``SSE-KMS`` and ``CSE-KMS`` , this is the KMS key ARN or ID.
    """


_ClientCreateWorkGroupConfigurationResultConfigurationTypeDef = TypedDict(
    "_ClientCreateWorkGroupConfigurationResultConfigurationTypeDef",
    {
        "OutputLocation": str,
        "EncryptionConfiguration": ClientCreateWorkGroupConfigurationResultConfigurationEncryptionConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateWorkGroupConfigurationResultConfigurationTypeDef(
    _ClientCreateWorkGroupConfigurationResultConfigurationTypeDef
):
    """
    Type definition for `ClientCreateWorkGroupConfiguration` `ResultConfiguration`

    The configuration for the workgroup, which includes the location in Amazon S3 where query
    results are stored and the encryption option, if any, used for query results. To run the query,
    you must specify the query results location using one of the ways: either in the workgroup
    using this setting, or for individual queries (client-side), using
    ResultConfiguration$OutputLocation . If none of them is set, Athena issues an error that no
    output location is provided. For more information, see `Query Results
    <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`__ .

    - **OutputLocation** *(string) --*

      The location in Amazon S3 where your query results are stored, such as
      ``s3://path/to/query/bucket/`` . To run the query, you must specify the query results
      location using one of the ways: either for individual queries using either this setting
      (client-side), or in the workgroup, using  WorkGroupConfiguration . If none of them is set,
      Athena issues an error that no output location is provided. For more information, see `Query
      Results <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`__ . If workgroup
      settings override client-side settings, then the query uses the settings specified for the
      workgroup. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration .

    - **EncryptionConfiguration** *(dict) --*

      If query results are encrypted in Amazon S3, indicates the encryption option used (for
      example, ``SSE-KMS`` or ``CSE-KMS`` ) and key information. This is a client-side setting. If
      workgroup settings override client-side settings, then the query uses the encryption
      configuration that is specified for the workgroup, and also uses the location for storing
      query results specified in the workgroup. See
      WorkGroupConfiguration$EnforceWorkGroupConfiguration and `Workgroup Settings Override
      Client-Side Settings
      <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`__ .

      - **EncryptionOption** *(string) --* **[REQUIRED]**

        Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (``SSE-S3``
        ), server-side encryption with KMS-managed keys (``SSE-KMS`` ), or client-side encryption
        with KMS-managed keys (CSE-KMS) is used.

        If a query runs in a workgroup and the workgroup overrides client-side settings, then the
        workgroup's setting for encryption is used. It specifies whether query results must be
        encrypted, for all queries that run in this workgroup.

      - **KmsKey** *(string) --*

        For ``SSE-KMS`` and ``CSE-KMS`` , this is the KMS key ARN or ID.
    """


_ClientCreateWorkGroupConfigurationTypeDef = TypedDict(
    "_ClientCreateWorkGroupConfigurationTypeDef",
    {
        "ResultConfiguration": ClientCreateWorkGroupConfigurationResultConfigurationTypeDef,
        "EnforceWorkGroupConfiguration": bool,
        "PublishCloudWatchMetricsEnabled": bool,
        "BytesScannedCutoffPerQuery": int,
        "RequesterPaysEnabled": bool,
    },
    total=False,
)


class ClientCreateWorkGroupConfigurationTypeDef(
    _ClientCreateWorkGroupConfigurationTypeDef
):
    """
    Type definition for `ClientCreateWorkGroup` `Configuration`

    The configuration for the workgroup, which includes the location in Amazon S3 where query results
    are stored, the encryption configuration, if any, used for encrypting query results, whether the
    Amazon CloudWatch Metrics are enabled for the workgroup, the limit for the amount of bytes
    scanned (cutoff) per query, if it is specified, and whether workgroup's settings (specified with
    EnforceWorkGroupConfiguration) in the WorkGroupConfiguration override client-side settings. See
    WorkGroupConfiguration$EnforceWorkGroupConfiguration .

    - **ResultConfiguration** *(dict) --*

      The configuration for the workgroup, which includes the location in Amazon S3 where query
      results are stored and the encryption option, if any, used for query results. To run the query,
      you must specify the query results location using one of the ways: either in the workgroup
      using this setting, or for individual queries (client-side), using
      ResultConfiguration$OutputLocation . If none of them is set, Athena issues an error that no
      output location is provided. For more information, see `Query Results
      <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`__ .

      - **OutputLocation** *(string) --*

        The location in Amazon S3 where your query results are stored, such as
        ``s3://path/to/query/bucket/`` . To run the query, you must specify the query results
        location using one of the ways: either for individual queries using either this setting
        (client-side), or in the workgroup, using  WorkGroupConfiguration . If none of them is set,
        Athena issues an error that no output location is provided. For more information, see `Query
        Results <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`__ . If workgroup
        settings override client-side settings, then the query uses the settings specified for the
        workgroup. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration .

      - **EncryptionConfiguration** *(dict) --*

        If query results are encrypted in Amazon S3, indicates the encryption option used (for
        example, ``SSE-KMS`` or ``CSE-KMS`` ) and key information. This is a client-side setting. If
        workgroup settings override client-side settings, then the query uses the encryption
        configuration that is specified for the workgroup, and also uses the location for storing
        query results specified in the workgroup. See
        WorkGroupConfiguration$EnforceWorkGroupConfiguration and `Workgroup Settings Override
        Client-Side Settings
        <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`__ .

        - **EncryptionOption** *(string) --* **[REQUIRED]**

          Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (``SSE-S3``
          ), server-side encryption with KMS-managed keys (``SSE-KMS`` ), or client-side encryption
          with KMS-managed keys (CSE-KMS) is used.

          If a query runs in a workgroup and the workgroup overrides client-side settings, then the
          workgroup's setting for encryption is used. It specifies whether query results must be
          encrypted, for all queries that run in this workgroup.

        - **KmsKey** *(string) --*

          For ``SSE-KMS`` and ``CSE-KMS`` , this is the KMS key ARN or ID.

    - **EnforceWorkGroupConfiguration** *(boolean) --*

      If set to "true", the settings for the workgroup override client-side settings. If set to
      "false", client-side settings are used. For more information, see `Workgroup Settings Override
      Client-Side Settings
      <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`__ .

    - **PublishCloudWatchMetricsEnabled** *(boolean) --*

      Indicates that the Amazon CloudWatch metrics are enabled for the workgroup.

    - **BytesScannedCutoffPerQuery** *(integer) --*

      The upper data usage limit (cutoff) for the amount of bytes a single query in a workgroup is
      allowed to scan.

    - **RequesterPaysEnabled** *(boolean) --*

      If set to ``true`` , allows members assigned to a workgroup to reference Amazon S3 Requester
      Pays buckets in queries. If set to ``false`` , workgroup members cannot query data from
      Requester Pays buckets, and queries that retrieve data from Requester Pays buckets cause an
      error. The default is ``false`` . For more information about Requester Pays buckets, see
      `Requester Pays Buckets
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html>`__ in the *Amazon
      Simple Storage Service Developer Guide* .
    """


_ClientCreateWorkGroupTagsTypeDef = TypedDict(
    "_ClientCreateWorkGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateWorkGroupTagsTypeDef(_ClientCreateWorkGroupTagsTypeDef):
    """
    Type definition for `ClientCreateWorkGroup` `Tags`

    A tag that you can add to a resource. A tag is a label that you assign to an AWS Athena
    resource (a workgroup). Each tag consists of a key and an optional value, both of which you
    define. Tags enable you to categorize workgroups in Athena, for example, by purpose, owner, or
    environment. Use a consistent set of tag keys to make it easier to search and filter workgroups
    in your account. The maximum tag key length is 128 Unicode characters in UTF-8. The maximum tag
    value length is 256 Unicode characters in UTF-8. You can use letters and numbers representable
    in UTF-8, and the following characters: + - = . _ : / @. Tag keys and values are
    case-sensitive. Tag keys must be unique per resource.

    - **Key** *(string) --*

      A tag key. The tag key length is from 1 to 128 Unicode characters in UTF-8. You can use
      letters and numbers representable in UTF-8, and the following characters: + - = . _ : / @.
      Tag keys are case-sensitive and must be unique per resource.

    - **Value** *(string) --*

      A tag value. The tag value length is from 0 to 256 Unicode characters in UTF-8. You can use
      letters and numbers representable in UTF-8, and the following characters: + - = . _ : / @.
      Tag values are case-sensitive.
    """


_ClientGetNamedQueryResponseNamedQueryTypeDef = TypedDict(
    "_ClientGetNamedQueryResponseNamedQueryTypeDef",
    {
        "Name": str,
        "Description": str,
        "Database": str,
        "QueryString": str,
        "NamedQueryId": str,
        "WorkGroup": str,
    },
    total=False,
)


class ClientGetNamedQueryResponseNamedQueryTypeDef(
    _ClientGetNamedQueryResponseNamedQueryTypeDef
):
    """
    Type definition for `ClientGetNamedQueryResponse` `NamedQuery`

    Information about the query.

    - **Name** *(string) --*

      The query name.

    - **Description** *(string) --*

      The query description.

    - **Database** *(string) --*

      The database to which the query belongs.

    - **QueryString** *(string) --*

      The SQL query statements that comprise the query.

    - **NamedQueryId** *(string) --*

      The unique identifier of the query.

    - **WorkGroup** *(string) --*

      The name of the workgroup that contains the named query.
    """


_ClientGetNamedQueryResponseTypeDef = TypedDict(
    "_ClientGetNamedQueryResponseTypeDef",
    {"NamedQuery": ClientGetNamedQueryResponseNamedQueryTypeDef},
    total=False,
)


class ClientGetNamedQueryResponseTypeDef(_ClientGetNamedQueryResponseTypeDef):
    """
    Type definition for `ClientGetNamedQuery` `Response`

    - **NamedQuery** *(dict) --*

      Information about the query.

      - **Name** *(string) --*

        The query name.

      - **Description** *(string) --*

        The query description.

      - **Database** *(string) --*

        The database to which the query belongs.

      - **QueryString** *(string) --*

        The SQL query statements that comprise the query.

      - **NamedQueryId** *(string) --*

        The unique identifier of the query.

      - **WorkGroup** *(string) --*

        The name of the workgroup that contains the named query.
    """


_ClientGetQueryExecutionResponseQueryExecutionQueryExecutionContextTypeDef = TypedDict(
    "_ClientGetQueryExecutionResponseQueryExecutionQueryExecutionContextTypeDef",
    {"Database": str},
    total=False,
)


class ClientGetQueryExecutionResponseQueryExecutionQueryExecutionContextTypeDef(
    _ClientGetQueryExecutionResponseQueryExecutionQueryExecutionContextTypeDef
):
    """
    Type definition for `ClientGetQueryExecutionResponseQueryExecution` `QueryExecutionContext`

    The database in which the query execution occurred.

    - **Database** *(string) --*

      The name of the database.
    """


_ClientGetQueryExecutionResponseQueryExecutionResultConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "_ClientGetQueryExecutionResponseQueryExecutionResultConfigurationEncryptionConfigurationTypeDef",
    {"EncryptionOption": str, "KmsKey": str},
    total=False,
)


class ClientGetQueryExecutionResponseQueryExecutionResultConfigurationEncryptionConfigurationTypeDef(
    _ClientGetQueryExecutionResponseQueryExecutionResultConfigurationEncryptionConfigurationTypeDef
):
    """
    Type definition for `ClientGetQueryExecutionResponseQueryExecutionResultConfiguration` `EncryptionConfiguration`

    If query results are encrypted in Amazon S3, indicates the encryption option used (for
    example, ``SSE-KMS`` or ``CSE-KMS`` ) and key information. This is a client-side setting.
    If workgroup settings override client-side settings, then the query uses the encryption
    configuration that is specified for the workgroup, and also uses the location for storing
    query results specified in the workgroup. See
    WorkGroupConfiguration$EnforceWorkGroupConfiguration and `Workgroup Settings Override
    Client-Side Settings
    <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`__ .

    - **EncryptionOption** *(string) --*

      Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys
      (``SSE-S3`` ), server-side encryption with KMS-managed keys (``SSE-KMS`` ), or
      client-side encryption with KMS-managed keys (CSE-KMS) is used.

      If a query runs in a workgroup and the workgroup overrides client-side settings, then
      the workgroup's setting for encryption is used. It specifies whether query results must
      be encrypted, for all queries that run in this workgroup.

    - **KmsKey** *(string) --*

      For ``SSE-KMS`` and ``CSE-KMS`` , this is the KMS key ARN or ID.
    """


_ClientGetQueryExecutionResponseQueryExecutionResultConfigurationTypeDef = TypedDict(
    "_ClientGetQueryExecutionResponseQueryExecutionResultConfigurationTypeDef",
    {
        "OutputLocation": str,
        "EncryptionConfiguration": ClientGetQueryExecutionResponseQueryExecutionResultConfigurationEncryptionConfigurationTypeDef,
    },
    total=False,
)


class ClientGetQueryExecutionResponseQueryExecutionResultConfigurationTypeDef(
    _ClientGetQueryExecutionResponseQueryExecutionResultConfigurationTypeDef
):
    """
    Type definition for `ClientGetQueryExecutionResponseQueryExecution` `ResultConfiguration`

    The location in Amazon S3 where query results were stored and the encryption option, if
    any, used for query results. These are known as "client-side settings". If workgroup
    settings override client-side settings, then the query uses the location for the query
    results and the encryption configuration that are specified for the workgroup.

    - **OutputLocation** *(string) --*

      The location in Amazon S3 where your query results are stored, such as
      ``s3://path/to/query/bucket/`` . To run the query, you must specify the query results
      location using one of the ways: either for individual queries using either this setting
      (client-side), or in the workgroup, using  WorkGroupConfiguration . If none of them is
      set, Athena issues an error that no output location is provided. For more information,
      see `Query Results <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`__ . If
      workgroup settings override client-side settings, then the query uses the settings
      specified for the workgroup. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration .

    - **EncryptionConfiguration** *(dict) --*

      If query results are encrypted in Amazon S3, indicates the encryption option used (for
      example, ``SSE-KMS`` or ``CSE-KMS`` ) and key information. This is a client-side setting.
      If workgroup settings override client-side settings, then the query uses the encryption
      configuration that is specified for the workgroup, and also uses the location for storing
      query results specified in the workgroup. See
      WorkGroupConfiguration$EnforceWorkGroupConfiguration and `Workgroup Settings Override
      Client-Side Settings
      <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`__ .

      - **EncryptionOption** *(string) --*

        Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys
        (``SSE-S3`` ), server-side encryption with KMS-managed keys (``SSE-KMS`` ), or
        client-side encryption with KMS-managed keys (CSE-KMS) is used.

        If a query runs in a workgroup and the workgroup overrides client-side settings, then
        the workgroup's setting for encryption is used. It specifies whether query results must
        be encrypted, for all queries that run in this workgroup.

      - **KmsKey** *(string) --*

        For ``SSE-KMS`` and ``CSE-KMS`` , this is the KMS key ARN or ID.
    """


_ClientGetQueryExecutionResponseQueryExecutionStatisticsTypeDef = TypedDict(
    "_ClientGetQueryExecutionResponseQueryExecutionStatisticsTypeDef",
    {
        "EngineExecutionTimeInMillis": int,
        "DataScannedInBytes": int,
        "DataManifestLocation": str,
    },
    total=False,
)


class ClientGetQueryExecutionResponseQueryExecutionStatisticsTypeDef(
    _ClientGetQueryExecutionResponseQueryExecutionStatisticsTypeDef
):
    """
    Type definition for `ClientGetQueryExecutionResponseQueryExecution` `Statistics`

    The location of a manifest file that tracks file locations generated by the query, the
    amount of data scanned by the query, and the amount of time that it took the query to run.

    - **EngineExecutionTimeInMillis** *(integer) --*

      The number of milliseconds that the query took to execute.

    - **DataScannedInBytes** *(integer) --*

      The number of bytes in the data that was queried.

    - **DataManifestLocation** *(string) --*

      The location and file name of a data manifest file. The manifest file is saved to the
      Athena query results location in Amazon S3. It tracks files that the query wrote to
      Amazon S3. If the query fails, the manifest file also tracks files that the query
      intended to write. The manifest is useful for identifying orphaned files resulting from a
      failed query. For more information, see `Working with Query Output Files
      <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`__ in the *Amazon Athena
      User Guide* .
    """


_ClientGetQueryExecutionResponseQueryExecutionStatusTypeDef = TypedDict(
    "_ClientGetQueryExecutionResponseQueryExecutionStatusTypeDef",
    {
        "State": str,
        "StateChangeReason": str,
        "SubmissionDateTime": datetime,
        "CompletionDateTime": datetime,
    },
    total=False,
)


class ClientGetQueryExecutionResponseQueryExecutionStatusTypeDef(
    _ClientGetQueryExecutionResponseQueryExecutionStatusTypeDef
):
    """
    Type definition for `ClientGetQueryExecutionResponseQueryExecution` `Status`

    The completion date, current state, submission time, and state change reason (if
    applicable) for the query execution.

    - **State** *(string) --*

      The state of query execution. ``QUEUED`` state is listed but is not used by Athena and is
      reserved for future use. ``RUNNING`` indicates that the query has been submitted to the
      service, and Athena will execute the query as soon as resources are available.
      ``SUCCEEDED`` indicates that the query completed without errors. ``FAILED`` indicates
      that the query experienced an error and did not complete processing. ``CANCELLED``
      indicates that a user input interrupted query execution.

    - **StateChangeReason** *(string) --*

      Further detail about the status of the query.

    - **SubmissionDateTime** *(datetime) --*

      The date and time that the query was submitted.

    - **CompletionDateTime** *(datetime) --*

      The date and time that the query completed.
    """


_ClientGetQueryExecutionResponseQueryExecutionTypeDef = TypedDict(
    "_ClientGetQueryExecutionResponseQueryExecutionTypeDef",
    {
        "QueryExecutionId": str,
        "Query": str,
        "StatementType": str,
        "ResultConfiguration": ClientGetQueryExecutionResponseQueryExecutionResultConfigurationTypeDef,
        "QueryExecutionContext": ClientGetQueryExecutionResponseQueryExecutionQueryExecutionContextTypeDef,
        "Status": ClientGetQueryExecutionResponseQueryExecutionStatusTypeDef,
        "Statistics": ClientGetQueryExecutionResponseQueryExecutionStatisticsTypeDef,
        "WorkGroup": str,
    },
    total=False,
)


class ClientGetQueryExecutionResponseQueryExecutionTypeDef(
    _ClientGetQueryExecutionResponseQueryExecutionTypeDef
):
    """
    Type definition for `ClientGetQueryExecutionResponse` `QueryExecution`

    Information about the query execution.

    - **QueryExecutionId** *(string) --*

      The unique identifier for each query execution.

    - **Query** *(string) --*

      The SQL query statements which the query execution ran.

    - **StatementType** *(string) --*

      The type of query statement that was run. ``DDL`` indicates DDL query statements. ``DML``
      indicates DML (Data Manipulation Language) query statements, such as ``CREATE TABLE AS
      SELECT`` . ``UTILITY`` indicates query statements other than DDL and DML, such as ``SHOW
      CREATE TABLE`` , or ``DESCRIBE <table>`` .

    - **ResultConfiguration** *(dict) --*

      The location in Amazon S3 where query results were stored and the encryption option, if
      any, used for query results. These are known as "client-side settings". If workgroup
      settings override client-side settings, then the query uses the location for the query
      results and the encryption configuration that are specified for the workgroup.

      - **OutputLocation** *(string) --*

        The location in Amazon S3 where your query results are stored, such as
        ``s3://path/to/query/bucket/`` . To run the query, you must specify the query results
        location using one of the ways: either for individual queries using either this setting
        (client-side), or in the workgroup, using  WorkGroupConfiguration . If none of them is
        set, Athena issues an error that no output location is provided. For more information,
        see `Query Results <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`__ . If
        workgroup settings override client-side settings, then the query uses the settings
        specified for the workgroup. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration .

      - **EncryptionConfiguration** *(dict) --*

        If query results are encrypted in Amazon S3, indicates the encryption option used (for
        example, ``SSE-KMS`` or ``CSE-KMS`` ) and key information. This is a client-side setting.
        If workgroup settings override client-side settings, then the query uses the encryption
        configuration that is specified for the workgroup, and also uses the location for storing
        query results specified in the workgroup. See
        WorkGroupConfiguration$EnforceWorkGroupConfiguration and `Workgroup Settings Override
        Client-Side Settings
        <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`__ .

        - **EncryptionOption** *(string) --*

          Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys
          (``SSE-S3`` ), server-side encryption with KMS-managed keys (``SSE-KMS`` ), or
          client-side encryption with KMS-managed keys (CSE-KMS) is used.

          If a query runs in a workgroup and the workgroup overrides client-side settings, then
          the workgroup's setting for encryption is used. It specifies whether query results must
          be encrypted, for all queries that run in this workgroup.

        - **KmsKey** *(string) --*

          For ``SSE-KMS`` and ``CSE-KMS`` , this is the KMS key ARN or ID.

    - **QueryExecutionContext** *(dict) --*

      The database in which the query execution occurred.

      - **Database** *(string) --*

        The name of the database.

    - **Status** *(dict) --*

      The completion date, current state, submission time, and state change reason (if
      applicable) for the query execution.

      - **State** *(string) --*

        The state of query execution. ``QUEUED`` state is listed but is not used by Athena and is
        reserved for future use. ``RUNNING`` indicates that the query has been submitted to the
        service, and Athena will execute the query as soon as resources are available.
        ``SUCCEEDED`` indicates that the query completed without errors. ``FAILED`` indicates
        that the query experienced an error and did not complete processing. ``CANCELLED``
        indicates that a user input interrupted query execution.

      - **StateChangeReason** *(string) --*

        Further detail about the status of the query.

      - **SubmissionDateTime** *(datetime) --*

        The date and time that the query was submitted.

      - **CompletionDateTime** *(datetime) --*

        The date and time that the query completed.

    - **Statistics** *(dict) --*

      The location of a manifest file that tracks file locations generated by the query, the
      amount of data scanned by the query, and the amount of time that it took the query to run.

      - **EngineExecutionTimeInMillis** *(integer) --*

        The number of milliseconds that the query took to execute.

      - **DataScannedInBytes** *(integer) --*

        The number of bytes in the data that was queried.

      - **DataManifestLocation** *(string) --*

        The location and file name of a data manifest file. The manifest file is saved to the
        Athena query results location in Amazon S3. It tracks files that the query wrote to
        Amazon S3. If the query fails, the manifest file also tracks files that the query
        intended to write. The manifest is useful for identifying orphaned files resulting from a
        failed query. For more information, see `Working with Query Output Files
        <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`__ in the *Amazon Athena
        User Guide* .

    - **WorkGroup** *(string) --*

      The name of the workgroup in which the query ran.
    """


_ClientGetQueryExecutionResponseTypeDef = TypedDict(
    "_ClientGetQueryExecutionResponseTypeDef",
    {"QueryExecution": ClientGetQueryExecutionResponseQueryExecutionTypeDef},
    total=False,
)


class ClientGetQueryExecutionResponseTypeDef(_ClientGetQueryExecutionResponseTypeDef):
    """
    Type definition for `ClientGetQueryExecution` `Response`

    - **QueryExecution** *(dict) --*

      Information about the query execution.

      - **QueryExecutionId** *(string) --*

        The unique identifier for each query execution.

      - **Query** *(string) --*

        The SQL query statements which the query execution ran.

      - **StatementType** *(string) --*

        The type of query statement that was run. ``DDL`` indicates DDL query statements. ``DML``
        indicates DML (Data Manipulation Language) query statements, such as ``CREATE TABLE AS
        SELECT`` . ``UTILITY`` indicates query statements other than DDL and DML, such as ``SHOW
        CREATE TABLE`` , or ``DESCRIBE <table>`` .

      - **ResultConfiguration** *(dict) --*

        The location in Amazon S3 where query results were stored and the encryption option, if
        any, used for query results. These are known as "client-side settings". If workgroup
        settings override client-side settings, then the query uses the location for the query
        results and the encryption configuration that are specified for the workgroup.

        - **OutputLocation** *(string) --*

          The location in Amazon S3 where your query results are stored, such as
          ``s3://path/to/query/bucket/`` . To run the query, you must specify the query results
          location using one of the ways: either for individual queries using either this setting
          (client-side), or in the workgroup, using  WorkGroupConfiguration . If none of them is
          set, Athena issues an error that no output location is provided. For more information,
          see `Query Results <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`__ . If
          workgroup settings override client-side settings, then the query uses the settings
          specified for the workgroup. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration .

        - **EncryptionConfiguration** *(dict) --*

          If query results are encrypted in Amazon S3, indicates the encryption option used (for
          example, ``SSE-KMS`` or ``CSE-KMS`` ) and key information. This is a client-side setting.
          If workgroup settings override client-side settings, then the query uses the encryption
          configuration that is specified for the workgroup, and also uses the location for storing
          query results specified in the workgroup. See
          WorkGroupConfiguration$EnforceWorkGroupConfiguration and `Workgroup Settings Override
          Client-Side Settings
          <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`__ .

          - **EncryptionOption** *(string) --*

            Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys
            (``SSE-S3`` ), server-side encryption with KMS-managed keys (``SSE-KMS`` ), or
            client-side encryption with KMS-managed keys (CSE-KMS) is used.

            If a query runs in a workgroup and the workgroup overrides client-side settings, then
            the workgroup's setting for encryption is used. It specifies whether query results must
            be encrypted, for all queries that run in this workgroup.

          - **KmsKey** *(string) --*

            For ``SSE-KMS`` and ``CSE-KMS`` , this is the KMS key ARN or ID.

      - **QueryExecutionContext** *(dict) --*

        The database in which the query execution occurred.

        - **Database** *(string) --*

          The name of the database.

      - **Status** *(dict) --*

        The completion date, current state, submission time, and state change reason (if
        applicable) for the query execution.

        - **State** *(string) --*

          The state of query execution. ``QUEUED`` state is listed but is not used by Athena and is
          reserved for future use. ``RUNNING`` indicates that the query has been submitted to the
          service, and Athena will execute the query as soon as resources are available.
          ``SUCCEEDED`` indicates that the query completed without errors. ``FAILED`` indicates
          that the query experienced an error and did not complete processing. ``CANCELLED``
          indicates that a user input interrupted query execution.

        - **StateChangeReason** *(string) --*

          Further detail about the status of the query.

        - **SubmissionDateTime** *(datetime) --*

          The date and time that the query was submitted.

        - **CompletionDateTime** *(datetime) --*

          The date and time that the query completed.

      - **Statistics** *(dict) --*

        The location of a manifest file that tracks file locations generated by the query, the
        amount of data scanned by the query, and the amount of time that it took the query to run.

        - **EngineExecutionTimeInMillis** *(integer) --*

          The number of milliseconds that the query took to execute.

        - **DataScannedInBytes** *(integer) --*

          The number of bytes in the data that was queried.

        - **DataManifestLocation** *(string) --*

          The location and file name of a data manifest file. The manifest file is saved to the
          Athena query results location in Amazon S3. It tracks files that the query wrote to
          Amazon S3. If the query fails, the manifest file also tracks files that the query
          intended to write. The manifest is useful for identifying orphaned files resulting from a
          failed query. For more information, see `Working with Query Output Files
          <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`__ in the *Amazon Athena
          User Guide* .

      - **WorkGroup** *(string) --*

        The name of the workgroup in which the query ran.
    """


_ClientGetQueryResultsResponseResultSetResultSetMetadataColumnInfoTypeDef = TypedDict(
    "_ClientGetQueryResultsResponseResultSetResultSetMetadataColumnInfoTypeDef",
    {
        "CatalogName": str,
        "SchemaName": str,
        "TableName": str,
        "Name": str,
        "Label": str,
        "Type": str,
        "Precision": int,
        "Scale": int,
        "Nullable": str,
        "CaseSensitive": bool,
    },
    total=False,
)


class ClientGetQueryResultsResponseResultSetResultSetMetadataColumnInfoTypeDef(
    _ClientGetQueryResultsResponseResultSetResultSetMetadataColumnInfoTypeDef
):
    """
    Type definition for `ClientGetQueryResultsResponseResultSetResultSetMetadata` `ColumnInfo`

    Information about the columns in a query execution result.

    - **CatalogName** *(string) --*

      The catalog to which the query results belong.

    - **SchemaName** *(string) --*

      The schema name (database name) to which the query results belong.

    - **TableName** *(string) --*

      The table name for the query results.

    - **Name** *(string) --*

      The name of the column.

    - **Label** *(string) --*

      A column label.

    - **Type** *(string) --*

      The data type of the column.

    - **Precision** *(integer) --*

      For ``DECIMAL`` data types, specifies the total number of digits, up to 38. For
      performance reasons, we recommend up to 18 digits.

    - **Scale** *(integer) --*

      For ``DECIMAL`` data types, specifies the total number of digits in the fractional
      part of the value. Defaults to 0.

    - **Nullable** *(string) --*

      Indicates the column's nullable status.

    - **CaseSensitive** *(boolean) --*

      Indicates whether values in the column are case-sensitive.
    """


_ClientGetQueryResultsResponseResultSetResultSetMetadataTypeDef = TypedDict(
    "_ClientGetQueryResultsResponseResultSetResultSetMetadataTypeDef",
    {
        "ColumnInfo": List[
            ClientGetQueryResultsResponseResultSetResultSetMetadataColumnInfoTypeDef
        ]
    },
    total=False,
)


class ClientGetQueryResultsResponseResultSetResultSetMetadataTypeDef(
    _ClientGetQueryResultsResponseResultSetResultSetMetadataTypeDef
):
    """
    Type definition for `ClientGetQueryResultsResponseResultSet` `ResultSetMetadata`

    The metadata that describes the column structure and data types of a table of query results.

    - **ColumnInfo** *(list) --*

      Information about the columns returned in a query result metadata.

      - *(dict) --*

        Information about the columns in a query execution result.

        - **CatalogName** *(string) --*

          The catalog to which the query results belong.

        - **SchemaName** *(string) --*

          The schema name (database name) to which the query results belong.

        - **TableName** *(string) --*

          The table name for the query results.

        - **Name** *(string) --*

          The name of the column.

        - **Label** *(string) --*

          A column label.

        - **Type** *(string) --*

          The data type of the column.

        - **Precision** *(integer) --*

          For ``DECIMAL`` data types, specifies the total number of digits, up to 38. For
          performance reasons, we recommend up to 18 digits.

        - **Scale** *(integer) --*

          For ``DECIMAL`` data types, specifies the total number of digits in the fractional
          part of the value. Defaults to 0.

        - **Nullable** *(string) --*

          Indicates the column's nullable status.

        - **CaseSensitive** *(boolean) --*

          Indicates whether values in the column are case-sensitive.
    """


_ClientGetQueryResultsResponseResultSetRowsDataTypeDef = TypedDict(
    "_ClientGetQueryResultsResponseResultSetRowsDataTypeDef",
    {"VarCharValue": str},
    total=False,
)


class ClientGetQueryResultsResponseResultSetRowsDataTypeDef(
    _ClientGetQueryResultsResponseResultSetRowsDataTypeDef
):
    """
    Type definition for `ClientGetQueryResultsResponseResultSetRows` `Data`

    A piece of data (a field in the table).

    - **VarCharValue** *(string) --*

      The value of the datum.
    """


_ClientGetQueryResultsResponseResultSetRowsTypeDef = TypedDict(
    "_ClientGetQueryResultsResponseResultSetRowsTypeDef",
    {"Data": List[ClientGetQueryResultsResponseResultSetRowsDataTypeDef]},
    total=False,
)


class ClientGetQueryResultsResponseResultSetRowsTypeDef(
    _ClientGetQueryResultsResponseResultSetRowsTypeDef
):
    """
    Type definition for `ClientGetQueryResultsResponseResultSet` `Rows`

    The rows that comprise a query result table.

    - **Data** *(list) --*

      The data that populates a row in a query result table.

      - *(dict) --*

        A piece of data (a field in the table).

        - **VarCharValue** *(string) --*

          The value of the datum.
    """


_ClientGetQueryResultsResponseResultSetTypeDef = TypedDict(
    "_ClientGetQueryResultsResponseResultSetTypeDef",
    {
        "Rows": List[ClientGetQueryResultsResponseResultSetRowsTypeDef],
        "ResultSetMetadata": ClientGetQueryResultsResponseResultSetResultSetMetadataTypeDef,
    },
    total=False,
)


class ClientGetQueryResultsResponseResultSetTypeDef(
    _ClientGetQueryResultsResponseResultSetTypeDef
):
    """
    Type definition for `ClientGetQueryResultsResponse` `ResultSet`

    The results of the query execution.

    - **Rows** *(list) --*

      The rows in the table.

      - *(dict) --*

        The rows that comprise a query result table.

        - **Data** *(list) --*

          The data that populates a row in a query result table.

          - *(dict) --*

            A piece of data (a field in the table).

            - **VarCharValue** *(string) --*

              The value of the datum.

    - **ResultSetMetadata** *(dict) --*

      The metadata that describes the column structure and data types of a table of query results.

      - **ColumnInfo** *(list) --*

        Information about the columns returned in a query result metadata.

        - *(dict) --*

          Information about the columns in a query execution result.

          - **CatalogName** *(string) --*

            The catalog to which the query results belong.

          - **SchemaName** *(string) --*

            The schema name (database name) to which the query results belong.

          - **TableName** *(string) --*

            The table name for the query results.

          - **Name** *(string) --*

            The name of the column.

          - **Label** *(string) --*

            A column label.

          - **Type** *(string) --*

            The data type of the column.

          - **Precision** *(integer) --*

            For ``DECIMAL`` data types, specifies the total number of digits, up to 38. For
            performance reasons, we recommend up to 18 digits.

          - **Scale** *(integer) --*

            For ``DECIMAL`` data types, specifies the total number of digits in the fractional
            part of the value. Defaults to 0.

          - **Nullable** *(string) --*

            Indicates the column's nullable status.

          - **CaseSensitive** *(boolean) --*

            Indicates whether values in the column are case-sensitive.
    """


_ClientGetQueryResultsResponseTypeDef = TypedDict(
    "_ClientGetQueryResultsResponseTypeDef",
    {
        "UpdateCount": int,
        "ResultSet": ClientGetQueryResultsResponseResultSetTypeDef,
        "NextToken": str,
    },
    total=False,
)


class ClientGetQueryResultsResponseTypeDef(_ClientGetQueryResultsResponseTypeDef):
    """
    Type definition for `ClientGetQueryResults` `Response`

    - **UpdateCount** *(integer) --*

      The number of rows inserted with a CREATE TABLE AS SELECT statement.

    - **ResultSet** *(dict) --*

      The results of the query execution.

      - **Rows** *(list) --*

        The rows in the table.

        - *(dict) --*

          The rows that comprise a query result table.

          - **Data** *(list) --*

            The data that populates a row in a query result table.

            - *(dict) --*

              A piece of data (a field in the table).

              - **VarCharValue** *(string) --*

                The value of the datum.

      - **ResultSetMetadata** *(dict) --*

        The metadata that describes the column structure and data types of a table of query results.

        - **ColumnInfo** *(list) --*

          Information about the columns returned in a query result metadata.

          - *(dict) --*

            Information about the columns in a query execution result.

            - **CatalogName** *(string) --*

              The catalog to which the query results belong.

            - **SchemaName** *(string) --*

              The schema name (database name) to which the query results belong.

            - **TableName** *(string) --*

              The table name for the query results.

            - **Name** *(string) --*

              The name of the column.

            - **Label** *(string) --*

              A column label.

            - **Type** *(string) --*

              The data type of the column.

            - **Precision** *(integer) --*

              For ``DECIMAL`` data types, specifies the total number of digits, up to 38. For
              performance reasons, we recommend up to 18 digits.

            - **Scale** *(integer) --*

              For ``DECIMAL`` data types, specifies the total number of digits in the fractional
              part of the value. Defaults to 0.

            - **Nullable** *(string) --*

              Indicates the column's nullable status.

            - **CaseSensitive** *(boolean) --*

              Indicates whether values in the column are case-sensitive.

    - **NextToken** *(string) --*

      A token to be used by the next request if this request is truncated.
    """


_ClientGetWorkGroupResponseWorkGroupConfigurationResultConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "_ClientGetWorkGroupResponseWorkGroupConfigurationResultConfigurationEncryptionConfigurationTypeDef",
    {"EncryptionOption": str, "KmsKey": str},
    total=False,
)


class ClientGetWorkGroupResponseWorkGroupConfigurationResultConfigurationEncryptionConfigurationTypeDef(
    _ClientGetWorkGroupResponseWorkGroupConfigurationResultConfigurationEncryptionConfigurationTypeDef
):
    """
    Type definition for `ClientGetWorkGroupResponseWorkGroupConfigurationResultConfiguration` `EncryptionConfiguration`

    If query results are encrypted in Amazon S3, indicates the encryption option used (for
    example, ``SSE-KMS`` or ``CSE-KMS`` ) and key information. This is a client-side
    setting. If workgroup settings override client-side settings, then the query uses the
    encryption configuration that is specified for the workgroup, and also uses the
    location for storing query results specified in the workgroup. See
    WorkGroupConfiguration$EnforceWorkGroupConfiguration and `Workgroup Settings Override
    Client-Side Settings
    <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`__ .

    - **EncryptionOption** *(string) --*

      Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys
      (``SSE-S3`` ), server-side encryption with KMS-managed keys (``SSE-KMS`` ), or
      client-side encryption with KMS-managed keys (CSE-KMS) is used.

      If a query runs in a workgroup and the workgroup overrides client-side settings, then
      the workgroup's setting for encryption is used. It specifies whether query results
      must be encrypted, for all queries that run in this workgroup.

    - **KmsKey** *(string) --*

      For ``SSE-KMS`` and ``CSE-KMS`` , this is the KMS key ARN or ID.
    """


_ClientGetWorkGroupResponseWorkGroupConfigurationResultConfigurationTypeDef = TypedDict(
    "_ClientGetWorkGroupResponseWorkGroupConfigurationResultConfigurationTypeDef",
    {
        "OutputLocation": str,
        "EncryptionConfiguration": ClientGetWorkGroupResponseWorkGroupConfigurationResultConfigurationEncryptionConfigurationTypeDef,
    },
    total=False,
)


class ClientGetWorkGroupResponseWorkGroupConfigurationResultConfigurationTypeDef(
    _ClientGetWorkGroupResponseWorkGroupConfigurationResultConfigurationTypeDef
):
    """
    Type definition for `ClientGetWorkGroupResponseWorkGroupConfiguration` `ResultConfiguration`

    The configuration for the workgroup, which includes the location in Amazon S3 where query
    results are stored and the encryption option, if any, used for query results. To run the
    query, you must specify the query results location using one of the ways: either in the
    workgroup using this setting, or for individual queries (client-side), using
    ResultConfiguration$OutputLocation . If none of them is set, Athena issues an error that
    no output location is provided. For more information, see `Query Results
    <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`__ .

    - **OutputLocation** *(string) --*

      The location in Amazon S3 where your query results are stored, such as
      ``s3://path/to/query/bucket/`` . To run the query, you must specify the query results
      location using one of the ways: either for individual queries using either this setting
      (client-side), or in the workgroup, using  WorkGroupConfiguration . If none of them is
      set, Athena issues an error that no output location is provided. For more information,
      see `Query Results <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`__ . If
      workgroup settings override client-side settings, then the query uses the settings
      specified for the workgroup. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration .

    - **EncryptionConfiguration** *(dict) --*

      If query results are encrypted in Amazon S3, indicates the encryption option used (for
      example, ``SSE-KMS`` or ``CSE-KMS`` ) and key information. This is a client-side
      setting. If workgroup settings override client-side settings, then the query uses the
      encryption configuration that is specified for the workgroup, and also uses the
      location for storing query results specified in the workgroup. See
      WorkGroupConfiguration$EnforceWorkGroupConfiguration and `Workgroup Settings Override
      Client-Side Settings
      <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`__ .

      - **EncryptionOption** *(string) --*

        Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys
        (``SSE-S3`` ), server-side encryption with KMS-managed keys (``SSE-KMS`` ), or
        client-side encryption with KMS-managed keys (CSE-KMS) is used.

        If a query runs in a workgroup and the workgroup overrides client-side settings, then
        the workgroup's setting for encryption is used. It specifies whether query results
        must be encrypted, for all queries that run in this workgroup.

      - **KmsKey** *(string) --*

        For ``SSE-KMS`` and ``CSE-KMS`` , this is the KMS key ARN or ID.
    """


_ClientGetWorkGroupResponseWorkGroupConfigurationTypeDef = TypedDict(
    "_ClientGetWorkGroupResponseWorkGroupConfigurationTypeDef",
    {
        "ResultConfiguration": ClientGetWorkGroupResponseWorkGroupConfigurationResultConfigurationTypeDef,
        "EnforceWorkGroupConfiguration": bool,
        "PublishCloudWatchMetricsEnabled": bool,
        "BytesScannedCutoffPerQuery": int,
        "RequesterPaysEnabled": bool,
    },
    total=False,
)


class ClientGetWorkGroupResponseWorkGroupConfigurationTypeDef(
    _ClientGetWorkGroupResponseWorkGroupConfigurationTypeDef
):
    """
    Type definition for `ClientGetWorkGroupResponseWorkGroup` `Configuration`

    The configuration of the workgroup, which includes the location in Amazon S3 where query
    results are stored, the encryption configuration, if any, used for query results; whether
    the Amazon CloudWatch Metrics are enabled for the workgroup; whether workgroup settings
    override client-side settings; and the data usage limits for the amount of data scanned per
    query or per workgroup. The workgroup settings override is specified in
    EnforceWorkGroupConfiguration (true/false) in the WorkGroupConfiguration. See
    WorkGroupConfiguration$EnforceWorkGroupConfiguration .

    - **ResultConfiguration** *(dict) --*

      The configuration for the workgroup, which includes the location in Amazon S3 where query
      results are stored and the encryption option, if any, used for query results. To run the
      query, you must specify the query results location using one of the ways: either in the
      workgroup using this setting, or for individual queries (client-side), using
      ResultConfiguration$OutputLocation . If none of them is set, Athena issues an error that
      no output location is provided. For more information, see `Query Results
      <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`__ .

      - **OutputLocation** *(string) --*

        The location in Amazon S3 where your query results are stored, such as
        ``s3://path/to/query/bucket/`` . To run the query, you must specify the query results
        location using one of the ways: either for individual queries using either this setting
        (client-side), or in the workgroup, using  WorkGroupConfiguration . If none of them is
        set, Athena issues an error that no output location is provided. For more information,
        see `Query Results <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`__ . If
        workgroup settings override client-side settings, then the query uses the settings
        specified for the workgroup. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration .

      - **EncryptionConfiguration** *(dict) --*

        If query results are encrypted in Amazon S3, indicates the encryption option used (for
        example, ``SSE-KMS`` or ``CSE-KMS`` ) and key information. This is a client-side
        setting. If workgroup settings override client-side settings, then the query uses the
        encryption configuration that is specified for the workgroup, and also uses the
        location for storing query results specified in the workgroup. See
        WorkGroupConfiguration$EnforceWorkGroupConfiguration and `Workgroup Settings Override
        Client-Side Settings
        <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`__ .

        - **EncryptionOption** *(string) --*

          Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys
          (``SSE-S3`` ), server-side encryption with KMS-managed keys (``SSE-KMS`` ), or
          client-side encryption with KMS-managed keys (CSE-KMS) is used.

          If a query runs in a workgroup and the workgroup overrides client-side settings, then
          the workgroup's setting for encryption is used. It specifies whether query results
          must be encrypted, for all queries that run in this workgroup.

        - **KmsKey** *(string) --*

          For ``SSE-KMS`` and ``CSE-KMS`` , this is the KMS key ARN or ID.

    - **EnforceWorkGroupConfiguration** *(boolean) --*

      If set to "true", the settings for the workgroup override client-side settings. If set to
      "false", client-side settings are used. For more information, see `Workgroup Settings
      Override Client-Side Settings
      <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`__ .

    - **PublishCloudWatchMetricsEnabled** *(boolean) --*

      Indicates that the Amazon CloudWatch metrics are enabled for the workgroup.

    - **BytesScannedCutoffPerQuery** *(integer) --*

      The upper data usage limit (cutoff) for the amount of bytes a single query in a workgroup
      is allowed to scan.

    - **RequesterPaysEnabled** *(boolean) --*

      If set to ``true`` , allows members assigned to a workgroup to reference Amazon S3
      Requester Pays buckets in queries. If set to ``false`` , workgroup members cannot query
      data from Requester Pays buckets, and queries that retrieve data from Requester Pays
      buckets cause an error. The default is ``false`` . For more information about Requester
      Pays buckets, see `Requester Pays Buckets
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html>`__ in the
      *Amazon Simple Storage Service Developer Guide* .
    """


_ClientGetWorkGroupResponseWorkGroupTypeDef = TypedDict(
    "_ClientGetWorkGroupResponseWorkGroupTypeDef",
    {
        "Name": str,
        "State": str,
        "Configuration": ClientGetWorkGroupResponseWorkGroupConfigurationTypeDef,
        "Description": str,
        "CreationTime": datetime,
    },
    total=False,
)


class ClientGetWorkGroupResponseWorkGroupTypeDef(
    _ClientGetWorkGroupResponseWorkGroupTypeDef
):
    """
    Type definition for `ClientGetWorkGroupResponse` `WorkGroup`

    Information about the workgroup.

    - **Name** *(string) --*

      The workgroup name.

    - **State** *(string) --*

      The state of the workgroup: ENABLED or DISABLED.

    - **Configuration** *(dict) --*

      The configuration of the workgroup, which includes the location in Amazon S3 where query
      results are stored, the encryption configuration, if any, used for query results; whether
      the Amazon CloudWatch Metrics are enabled for the workgroup; whether workgroup settings
      override client-side settings; and the data usage limits for the amount of data scanned per
      query or per workgroup. The workgroup settings override is specified in
      EnforceWorkGroupConfiguration (true/false) in the WorkGroupConfiguration. See
      WorkGroupConfiguration$EnforceWorkGroupConfiguration .

      - **ResultConfiguration** *(dict) --*

        The configuration for the workgroup, which includes the location in Amazon S3 where query
        results are stored and the encryption option, if any, used for query results. To run the
        query, you must specify the query results location using one of the ways: either in the
        workgroup using this setting, or for individual queries (client-side), using
        ResultConfiguration$OutputLocation . If none of them is set, Athena issues an error that
        no output location is provided. For more information, see `Query Results
        <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`__ .

        - **OutputLocation** *(string) --*

          The location in Amazon S3 where your query results are stored, such as
          ``s3://path/to/query/bucket/`` . To run the query, you must specify the query results
          location using one of the ways: either for individual queries using either this setting
          (client-side), or in the workgroup, using  WorkGroupConfiguration . If none of them is
          set, Athena issues an error that no output location is provided. For more information,
          see `Query Results <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`__ . If
          workgroup settings override client-side settings, then the query uses the settings
          specified for the workgroup. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration .

        - **EncryptionConfiguration** *(dict) --*

          If query results are encrypted in Amazon S3, indicates the encryption option used (for
          example, ``SSE-KMS`` or ``CSE-KMS`` ) and key information. This is a client-side
          setting. If workgroup settings override client-side settings, then the query uses the
          encryption configuration that is specified for the workgroup, and also uses the
          location for storing query results specified in the workgroup. See
          WorkGroupConfiguration$EnforceWorkGroupConfiguration and `Workgroup Settings Override
          Client-Side Settings
          <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`__ .

          - **EncryptionOption** *(string) --*

            Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys
            (``SSE-S3`` ), server-side encryption with KMS-managed keys (``SSE-KMS`` ), or
            client-side encryption with KMS-managed keys (CSE-KMS) is used.

            If a query runs in a workgroup and the workgroup overrides client-side settings, then
            the workgroup's setting for encryption is used. It specifies whether query results
            must be encrypted, for all queries that run in this workgroup.

          - **KmsKey** *(string) --*

            For ``SSE-KMS`` and ``CSE-KMS`` , this is the KMS key ARN or ID.

      - **EnforceWorkGroupConfiguration** *(boolean) --*

        If set to "true", the settings for the workgroup override client-side settings. If set to
        "false", client-side settings are used. For more information, see `Workgroup Settings
        Override Client-Side Settings
        <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`__ .

      - **PublishCloudWatchMetricsEnabled** *(boolean) --*

        Indicates that the Amazon CloudWatch metrics are enabled for the workgroup.

      - **BytesScannedCutoffPerQuery** *(integer) --*

        The upper data usage limit (cutoff) for the amount of bytes a single query in a workgroup
        is allowed to scan.

      - **RequesterPaysEnabled** *(boolean) --*

        If set to ``true`` , allows members assigned to a workgroup to reference Amazon S3
        Requester Pays buckets in queries. If set to ``false`` , workgroup members cannot query
        data from Requester Pays buckets, and queries that retrieve data from Requester Pays
        buckets cause an error. The default is ``false`` . For more information about Requester
        Pays buckets, see `Requester Pays Buckets
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html>`__ in the
        *Amazon Simple Storage Service Developer Guide* .

    - **Description** *(string) --*

      The workgroup description.

    - **CreationTime** *(datetime) --*

      The date and time the workgroup was created.
    """


_ClientGetWorkGroupResponseTypeDef = TypedDict(
    "_ClientGetWorkGroupResponseTypeDef",
    {"WorkGroup": ClientGetWorkGroupResponseWorkGroupTypeDef},
    total=False,
)


class ClientGetWorkGroupResponseTypeDef(_ClientGetWorkGroupResponseTypeDef):
    """
    Type definition for `ClientGetWorkGroup` `Response`

    - **WorkGroup** *(dict) --*

      Information about the workgroup.

      - **Name** *(string) --*

        The workgroup name.

      - **State** *(string) --*

        The state of the workgroup: ENABLED or DISABLED.

      - **Configuration** *(dict) --*

        The configuration of the workgroup, which includes the location in Amazon S3 where query
        results are stored, the encryption configuration, if any, used for query results; whether
        the Amazon CloudWatch Metrics are enabled for the workgroup; whether workgroup settings
        override client-side settings; and the data usage limits for the amount of data scanned per
        query or per workgroup. The workgroup settings override is specified in
        EnforceWorkGroupConfiguration (true/false) in the WorkGroupConfiguration. See
        WorkGroupConfiguration$EnforceWorkGroupConfiguration .

        - **ResultConfiguration** *(dict) --*

          The configuration for the workgroup, which includes the location in Amazon S3 where query
          results are stored and the encryption option, if any, used for query results. To run the
          query, you must specify the query results location using one of the ways: either in the
          workgroup using this setting, or for individual queries (client-side), using
          ResultConfiguration$OutputLocation . If none of them is set, Athena issues an error that
          no output location is provided. For more information, see `Query Results
          <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`__ .

          - **OutputLocation** *(string) --*

            The location in Amazon S3 where your query results are stored, such as
            ``s3://path/to/query/bucket/`` . To run the query, you must specify the query results
            location using one of the ways: either for individual queries using either this setting
            (client-side), or in the workgroup, using  WorkGroupConfiguration . If none of them is
            set, Athena issues an error that no output location is provided. For more information,
            see `Query Results <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`__ . If
            workgroup settings override client-side settings, then the query uses the settings
            specified for the workgroup. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration .

          - **EncryptionConfiguration** *(dict) --*

            If query results are encrypted in Amazon S3, indicates the encryption option used (for
            example, ``SSE-KMS`` or ``CSE-KMS`` ) and key information. This is a client-side
            setting. If workgroup settings override client-side settings, then the query uses the
            encryption configuration that is specified for the workgroup, and also uses the
            location for storing query results specified in the workgroup. See
            WorkGroupConfiguration$EnforceWorkGroupConfiguration and `Workgroup Settings Override
            Client-Side Settings
            <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`__ .

            - **EncryptionOption** *(string) --*

              Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys
              (``SSE-S3`` ), server-side encryption with KMS-managed keys (``SSE-KMS`` ), or
              client-side encryption with KMS-managed keys (CSE-KMS) is used.

              If a query runs in a workgroup and the workgroup overrides client-side settings, then
              the workgroup's setting for encryption is used. It specifies whether query results
              must be encrypted, for all queries that run in this workgroup.

            - **KmsKey** *(string) --*

              For ``SSE-KMS`` and ``CSE-KMS`` , this is the KMS key ARN or ID.

        - **EnforceWorkGroupConfiguration** *(boolean) --*

          If set to "true", the settings for the workgroup override client-side settings. If set to
          "false", client-side settings are used. For more information, see `Workgroup Settings
          Override Client-Side Settings
          <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`__ .

        - **PublishCloudWatchMetricsEnabled** *(boolean) --*

          Indicates that the Amazon CloudWatch metrics are enabled for the workgroup.

        - **BytesScannedCutoffPerQuery** *(integer) --*

          The upper data usage limit (cutoff) for the amount of bytes a single query in a workgroup
          is allowed to scan.

        - **RequesterPaysEnabled** *(boolean) --*

          If set to ``true`` , allows members assigned to a workgroup to reference Amazon S3
          Requester Pays buckets in queries. If set to ``false`` , workgroup members cannot query
          data from Requester Pays buckets, and queries that retrieve data from Requester Pays
          buckets cause an error. The default is ``false`` . For more information about Requester
          Pays buckets, see `Requester Pays Buckets
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html>`__ in the
          *Amazon Simple Storage Service Developer Guide* .

      - **Description** *(string) --*

        The workgroup description.

      - **CreationTime** *(datetime) --*

        The date and time the workgroup was created.
    """


_ClientListNamedQueriesResponseTypeDef = TypedDict(
    "_ClientListNamedQueriesResponseTypeDef",
    {"NamedQueryIds": List[str], "NextToken": str},
    total=False,
)


class ClientListNamedQueriesResponseTypeDef(_ClientListNamedQueriesResponseTypeDef):
    """
    Type definition for `ClientListNamedQueries` `Response`

    - **NamedQueryIds** *(list) --*

      The list of unique query IDs.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to be used by the next request if this request is truncated.
    """


_ClientListQueryExecutionsResponseTypeDef = TypedDict(
    "_ClientListQueryExecutionsResponseTypeDef",
    {"QueryExecutionIds": List[str], "NextToken": str},
    total=False,
)


class ClientListQueryExecutionsResponseTypeDef(
    _ClientListQueryExecutionsResponseTypeDef
):
    """
    Type definition for `ClientListQueryExecutions` `Response`

    - **QueryExecutionIds** *(list) --*

      The unique IDs of each query execution as an array of strings.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to be used by the next request if this request is truncated.
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

    A tag that you can add to a resource. A tag is a label that you assign to an AWS Athena
    resource (a workgroup). Each tag consists of a key and an optional value, both of which you
    define. Tags enable you to categorize workgroups in Athena, for example, by purpose, owner,
    or environment. Use a consistent set of tag keys to make it easier to search and filter
    workgroups in your account. The maximum tag key length is 128 Unicode characters in UTF-8.
    The maximum tag value length is 256 Unicode characters in UTF-8. You can use letters and
    numbers representable in UTF-8, and the following characters: + - = . _ : / @. Tag keys and
    values are case-sensitive. Tag keys must be unique per resource.

    - **Key** *(string) --*

      A tag key. The tag key length is from 1 to 128 Unicode characters in UTF-8. You can use
      letters and numbers representable in UTF-8, and the following characters: + - = . _ : /
      @. Tag keys are case-sensitive and must be unique per resource.

    - **Value** *(string) --*

      A tag value. The tag value length is from 0 to 256 Unicode characters in UTF-8. You can
      use letters and numbers representable in UTF-8, and the following characters: + - = . _ :
      / @. Tag values are case-sensitive.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef], "NextToken": str},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **Tags** *(list) --*

      The list of tags associated with this workgroup.

      - *(dict) --*

        A tag that you can add to a resource. A tag is a label that you assign to an AWS Athena
        resource (a workgroup). Each tag consists of a key and an optional value, both of which you
        define. Tags enable you to categorize workgroups in Athena, for example, by purpose, owner,
        or environment. Use a consistent set of tag keys to make it easier to search and filter
        workgroups in your account. The maximum tag key length is 128 Unicode characters in UTF-8.
        The maximum tag value length is 256 Unicode characters in UTF-8. You can use letters and
        numbers representable in UTF-8, and the following characters: + - = . _ : / @. Tag keys and
        values are case-sensitive. Tag keys must be unique per resource.

        - **Key** *(string) --*

          A tag key. The tag key length is from 1 to 128 Unicode characters in UTF-8. You can use
          letters and numbers representable in UTF-8, and the following characters: + - = . _ : /
          @. Tag keys are case-sensitive and must be unique per resource.

        - **Value** *(string) --*

          A tag value. The tag value length is from 0 to 256 Unicode characters in UTF-8. You can
          use letters and numbers representable in UTF-8, and the following characters: + - = . _ :
          / @. Tag values are case-sensitive.

    - **NextToken** *(string) --*

      A token to be used by the next request if this request is truncated.
    """


_ClientListWorkGroupsResponseWorkGroupsTypeDef = TypedDict(
    "_ClientListWorkGroupsResponseWorkGroupsTypeDef",
    {"Name": str, "State": str, "Description": str, "CreationTime": datetime},
    total=False,
)


class ClientListWorkGroupsResponseWorkGroupsTypeDef(
    _ClientListWorkGroupsResponseWorkGroupsTypeDef
):
    """
    Type definition for `ClientListWorkGroupsResponse` `WorkGroups`

    The summary information for the workgroup, which includes its name, state, description, and
    the date and time it was created.

    - **Name** *(string) --*

      The name of the workgroup.

    - **State** *(string) --*

      The state of the workgroup.

    - **Description** *(string) --*

      The workgroup description.

    - **CreationTime** *(datetime) --*

      The workgroup creation date and time.
    """


_ClientListWorkGroupsResponseTypeDef = TypedDict(
    "_ClientListWorkGroupsResponseTypeDef",
    {
        "WorkGroups": List[ClientListWorkGroupsResponseWorkGroupsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListWorkGroupsResponseTypeDef(_ClientListWorkGroupsResponseTypeDef):
    """
    Type definition for `ClientListWorkGroups` `Response`

    - **WorkGroups** *(list) --*

      The list of workgroups, including their names, descriptions, creation times, and states.

      - *(dict) --*

        The summary information for the workgroup, which includes its name, state, description, and
        the date and time it was created.

        - **Name** *(string) --*

          The name of the workgroup.

        - **State** *(string) --*

          The state of the workgroup.

        - **Description** *(string) --*

          The workgroup description.

        - **CreationTime** *(datetime) --*

          The workgroup creation date and time.

    - **NextToken** *(string) --*

      A token to be used by the next request if this request is truncated.
    """


_ClientStartQueryExecutionQueryExecutionContextTypeDef = TypedDict(
    "_ClientStartQueryExecutionQueryExecutionContextTypeDef",
    {"Database": str},
    total=False,
)


class ClientStartQueryExecutionQueryExecutionContextTypeDef(
    _ClientStartQueryExecutionQueryExecutionContextTypeDef
):
    """
    Type definition for `ClientStartQueryExecution` `QueryExecutionContext`

    The database within which the query executes.

    - **Database** *(string) --*

      The name of the database.
    """


_ClientStartQueryExecutionResponseTypeDef = TypedDict(
    "_ClientStartQueryExecutionResponseTypeDef", {"QueryExecutionId": str}, total=False
)


class ClientStartQueryExecutionResponseTypeDef(
    _ClientStartQueryExecutionResponseTypeDef
):
    """
    Type definition for `ClientStartQueryExecution` `Response`

    - **QueryExecutionId** *(string) --*

      The unique ID of the query that ran as a result of this request.
    """


_RequiredClientStartQueryExecutionResultConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "_RequiredClientStartQueryExecutionResultConfigurationEncryptionConfigurationTypeDef",
    {"EncryptionOption": str},
)
_OptionalClientStartQueryExecutionResultConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "_OptionalClientStartQueryExecutionResultConfigurationEncryptionConfigurationTypeDef",
    {"KmsKey": str},
    total=False,
)


class ClientStartQueryExecutionResultConfigurationEncryptionConfigurationTypeDef(
    _RequiredClientStartQueryExecutionResultConfigurationEncryptionConfigurationTypeDef,
    _OptionalClientStartQueryExecutionResultConfigurationEncryptionConfigurationTypeDef,
):
    """
    Type definition for `ClientStartQueryExecutionResultConfiguration` `EncryptionConfiguration`

    If query results are encrypted in Amazon S3, indicates the encryption option used (for example,
    ``SSE-KMS`` or ``CSE-KMS`` ) and key information. This is a client-side setting. If workgroup
    settings override client-side settings, then the query uses the encryption configuration that
    is specified for the workgroup, and also uses the location for storing query results specified
    in the workgroup. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration and `Workgroup
    Settings Override Client-Side Settings
    <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`__ .

    - **EncryptionOption** *(string) --* **[REQUIRED]**

      Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (``SSE-S3`` ),
      server-side encryption with KMS-managed keys (``SSE-KMS`` ), or client-side encryption with
      KMS-managed keys (CSE-KMS) is used.

      If a query runs in a workgroup and the workgroup overrides client-side settings, then the
      workgroup's setting for encryption is used. It specifies whether query results must be
      encrypted, for all queries that run in this workgroup.

    - **KmsKey** *(string) --*

      For ``SSE-KMS`` and ``CSE-KMS`` , this is the KMS key ARN or ID.
    """


_ClientStartQueryExecutionResultConfigurationTypeDef = TypedDict(
    "_ClientStartQueryExecutionResultConfigurationTypeDef",
    {
        "OutputLocation": str,
        "EncryptionConfiguration": ClientStartQueryExecutionResultConfigurationEncryptionConfigurationTypeDef,
    },
    total=False,
)


class ClientStartQueryExecutionResultConfigurationTypeDef(
    _ClientStartQueryExecutionResultConfigurationTypeDef
):
    """
    Type definition for `ClientStartQueryExecution` `ResultConfiguration`

    Specifies information about where and how to save the results of the query execution. If the
    query runs in a workgroup, then workgroup's settings may override query settings. This affects
    the query results location. The workgroup settings override is specified in
    EnforceWorkGroupConfiguration (true/false) in the WorkGroupConfiguration. See
    WorkGroupConfiguration$EnforceWorkGroupConfiguration .

    - **OutputLocation** *(string) --*

      The location in Amazon S3 where your query results are stored, such as
      ``s3://path/to/query/bucket/`` . To run the query, you must specify the query results location
      using one of the ways: either for individual queries using either this setting (client-side),
      or in the workgroup, using  WorkGroupConfiguration . If none of them is set, Athena issues an
      error that no output location is provided. For more information, see `Query Results
      <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`__ . If workgroup settings
      override client-side settings, then the query uses the settings specified for the workgroup.
      See  WorkGroupConfiguration$EnforceWorkGroupConfiguration .

    - **EncryptionConfiguration** *(dict) --*

      If query results are encrypted in Amazon S3, indicates the encryption option used (for example,
      ``SSE-KMS`` or ``CSE-KMS`` ) and key information. This is a client-side setting. If workgroup
      settings override client-side settings, then the query uses the encryption configuration that
      is specified for the workgroup, and also uses the location for storing query results specified
      in the workgroup. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration and `Workgroup
      Settings Override Client-Side Settings
      <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`__ .

      - **EncryptionOption** *(string) --* **[REQUIRED]**

        Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (``SSE-S3`` ),
        server-side encryption with KMS-managed keys (``SSE-KMS`` ), or client-side encryption with
        KMS-managed keys (CSE-KMS) is used.

        If a query runs in a workgroup and the workgroup overrides client-side settings, then the
        workgroup's setting for encryption is used. It specifies whether query results must be
        encrypted, for all queries that run in this workgroup.

      - **KmsKey** *(string) --*

        For ``SSE-KMS`` and ``CSE-KMS`` , this is the KMS key ARN or ID.
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    Type definition for `ClientTagResource` `Tags`

    A tag that you can add to a resource. A tag is a label that you assign to an AWS Athena
    resource (a workgroup). Each tag consists of a key and an optional value, both of which you
    define. Tags enable you to categorize workgroups in Athena, for example, by purpose, owner, or
    environment. Use a consistent set of tag keys to make it easier to search and filter workgroups
    in your account. The maximum tag key length is 128 Unicode characters in UTF-8. The maximum tag
    value length is 256 Unicode characters in UTF-8. You can use letters and numbers representable
    in UTF-8, and the following characters: + - = . _ : / @. Tag keys and values are
    case-sensitive. Tag keys must be unique per resource.

    - **Key** *(string) --*

      A tag key. The tag key length is from 1 to 128 Unicode characters in UTF-8. You can use
      letters and numbers representable in UTF-8, and the following characters: + - = . _ : / @.
      Tag keys are case-sensitive and must be unique per resource.

    - **Value** *(string) --*

      A tag value. The tag value length is from 0 to 256 Unicode characters in UTF-8. You can use
      letters and numbers representable in UTF-8, and the following characters: + - = . _ : / @.
      Tag values are case-sensitive.
    """


_RequiredClientUpdateWorkGroupConfigurationUpdatesResultConfigurationUpdatesEncryptionConfigurationTypeDef = TypedDict(
    "_RequiredClientUpdateWorkGroupConfigurationUpdatesResultConfigurationUpdatesEncryptionConfigurationTypeDef",
    {"EncryptionOption": str},
)
_OptionalClientUpdateWorkGroupConfigurationUpdatesResultConfigurationUpdatesEncryptionConfigurationTypeDef = TypedDict(
    "_OptionalClientUpdateWorkGroupConfigurationUpdatesResultConfigurationUpdatesEncryptionConfigurationTypeDef",
    {"KmsKey": str},
    total=False,
)


class ClientUpdateWorkGroupConfigurationUpdatesResultConfigurationUpdatesEncryptionConfigurationTypeDef(
    _RequiredClientUpdateWorkGroupConfigurationUpdatesResultConfigurationUpdatesEncryptionConfigurationTypeDef,
    _OptionalClientUpdateWorkGroupConfigurationUpdatesResultConfigurationUpdatesEncryptionConfigurationTypeDef,
):
    """
    Type definition for `ClientUpdateWorkGroupConfigurationUpdatesResultConfigurationUpdates` `EncryptionConfiguration`

    The encryption configuration for the query results.

    - **EncryptionOption** *(string) --* **[REQUIRED]**

      Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (``SSE-S3``
      ), server-side encryption with KMS-managed keys (``SSE-KMS`` ), or client-side encryption
      with KMS-managed keys (CSE-KMS) is used.

      If a query runs in a workgroup and the workgroup overrides client-side settings, then the
      workgroup's setting for encryption is used. It specifies whether query results must be
      encrypted, for all queries that run in this workgroup.

    - **KmsKey** *(string) --*

      For ``SSE-KMS`` and ``CSE-KMS`` , this is the KMS key ARN or ID.
    """


_ClientUpdateWorkGroupConfigurationUpdatesResultConfigurationUpdatesTypeDef = TypedDict(
    "_ClientUpdateWorkGroupConfigurationUpdatesResultConfigurationUpdatesTypeDef",
    {
        "OutputLocation": str,
        "RemoveOutputLocation": bool,
        "EncryptionConfiguration": ClientUpdateWorkGroupConfigurationUpdatesResultConfigurationUpdatesEncryptionConfigurationTypeDef,
        "RemoveEncryptionConfiguration": bool,
    },
    total=False,
)


class ClientUpdateWorkGroupConfigurationUpdatesResultConfigurationUpdatesTypeDef(
    _ClientUpdateWorkGroupConfigurationUpdatesResultConfigurationUpdatesTypeDef
):
    """
    Type definition for `ClientUpdateWorkGroupConfigurationUpdates` `ResultConfigurationUpdates`

    The result configuration information about the queries in this workgroup that will be updated.
    Includes the updated results location and an updated option for encrypting query results.

    - **OutputLocation** *(string) --*

      The location in Amazon S3 where your query results are stored, such as
      ``s3://path/to/query/bucket/`` . For more information, see `Query Results
      <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`__ If workgroup settings
      override client-side settings, then the query uses the location for the query results and the
      encryption configuration that are specified for the workgroup. The "workgroup settings
      override" is specified in EnforceWorkGroupConfiguration (true/false) in the
      WorkGroupConfiguration. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration .

    - **RemoveOutputLocation** *(boolean) --*

      If set to "true", indicates that the previously-specified query results location (also known
      as a client-side setting) for queries in this workgroup should be ignored and set to null. If
      set to "false" or not set, and a value is present in the OutputLocation in
      ResultConfigurationUpdates (the client-side setting), the OutputLocation in the workgroup's
      ResultConfiguration will be updated with the new value. For more information, see `Workgroup
      Settings Override Client-Side Settings
      <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`__ .

    - **EncryptionConfiguration** *(dict) --*

      The encryption configuration for the query results.

      - **EncryptionOption** *(string) --* **[REQUIRED]**

        Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (``SSE-S3``
        ), server-side encryption with KMS-managed keys (``SSE-KMS`` ), or client-side encryption
        with KMS-managed keys (CSE-KMS) is used.

        If a query runs in a workgroup and the workgroup overrides client-side settings, then the
        workgroup's setting for encryption is used. It specifies whether query results must be
        encrypted, for all queries that run in this workgroup.

      - **KmsKey** *(string) --*

        For ``SSE-KMS`` and ``CSE-KMS`` , this is the KMS key ARN or ID.

    - **RemoveEncryptionConfiguration** *(boolean) --*

      If set to "true", indicates that the previously-specified encryption configuration (also
      known as the client-side setting) for queries in this workgroup should be ignored and set to
      null. If set to "false" or not set, and a value is present in the EncryptionConfiguration in
      ResultConfigurationUpdates (the client-side setting), the EncryptionConfiguration in the
      workgroup's ResultConfiguration will be updated with the new value. For more information, see
      `Workgroup Settings Override Client-Side Settings
      <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`__ .
    """


_ClientUpdateWorkGroupConfigurationUpdatesTypeDef = TypedDict(
    "_ClientUpdateWorkGroupConfigurationUpdatesTypeDef",
    {
        "EnforceWorkGroupConfiguration": bool,
        "ResultConfigurationUpdates": ClientUpdateWorkGroupConfigurationUpdatesResultConfigurationUpdatesTypeDef,
        "PublishCloudWatchMetricsEnabled": bool,
        "BytesScannedCutoffPerQuery": int,
        "RemoveBytesScannedCutoffPerQuery": bool,
        "RequesterPaysEnabled": bool,
    },
    total=False,
)


class ClientUpdateWorkGroupConfigurationUpdatesTypeDef(
    _ClientUpdateWorkGroupConfigurationUpdatesTypeDef
):
    """
    Type definition for `ClientUpdateWorkGroup` `ConfigurationUpdates`

    The workgroup configuration that will be updated for the given workgroup.

    - **EnforceWorkGroupConfiguration** *(boolean) --*

      If set to "true", the settings for the workgroup override client-side settings. If set to
      "false" client-side settings are used. For more information, see `Workgroup Settings Override
      Client-Side Settings
      <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`__ .

    - **ResultConfigurationUpdates** *(dict) --*

      The result configuration information about the queries in this workgroup that will be updated.
      Includes the updated results location and an updated option for encrypting query results.

      - **OutputLocation** *(string) --*

        The location in Amazon S3 where your query results are stored, such as
        ``s3://path/to/query/bucket/`` . For more information, see `Query Results
        <https://docs.aws.amazon.com/athena/latest/ug/querying.html>`__ If workgroup settings
        override client-side settings, then the query uses the location for the query results and the
        encryption configuration that are specified for the workgroup. The "workgroup settings
        override" is specified in EnforceWorkGroupConfiguration (true/false) in the
        WorkGroupConfiguration. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration .

      - **RemoveOutputLocation** *(boolean) --*

        If set to "true", indicates that the previously-specified query results location (also known
        as a client-side setting) for queries in this workgroup should be ignored and set to null. If
        set to "false" or not set, and a value is present in the OutputLocation in
        ResultConfigurationUpdates (the client-side setting), the OutputLocation in the workgroup's
        ResultConfiguration will be updated with the new value. For more information, see `Workgroup
        Settings Override Client-Side Settings
        <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`__ .

      - **EncryptionConfiguration** *(dict) --*

        The encryption configuration for the query results.

        - **EncryptionOption** *(string) --* **[REQUIRED]**

          Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (``SSE-S3``
          ), server-side encryption with KMS-managed keys (``SSE-KMS`` ), or client-side encryption
          with KMS-managed keys (CSE-KMS) is used.

          If a query runs in a workgroup and the workgroup overrides client-side settings, then the
          workgroup's setting for encryption is used. It specifies whether query results must be
          encrypted, for all queries that run in this workgroup.

        - **KmsKey** *(string) --*

          For ``SSE-KMS`` and ``CSE-KMS`` , this is the KMS key ARN or ID.

      - **RemoveEncryptionConfiguration** *(boolean) --*

        If set to "true", indicates that the previously-specified encryption configuration (also
        known as the client-side setting) for queries in this workgroup should be ignored and set to
        null. If set to "false" or not set, and a value is present in the EncryptionConfiguration in
        ResultConfigurationUpdates (the client-side setting), the EncryptionConfiguration in the
        workgroup's ResultConfiguration will be updated with the new value. For more information, see
        `Workgroup Settings Override Client-Side Settings
        <https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html>`__ .

    - **PublishCloudWatchMetricsEnabled** *(boolean) --*

      Indicates whether this workgroup enables publishing metrics to Amazon CloudWatch.

    - **BytesScannedCutoffPerQuery** *(integer) --*

      The upper limit (cutoff) for the amount of bytes a single query in a workgroup is allowed to
      scan.

    - **RemoveBytesScannedCutoffPerQuery** *(boolean) --*

      Indicates that the data usage control limit per query is removed.
      WorkGroupConfiguration$BytesScannedCutoffPerQuery

    - **RequesterPaysEnabled** *(boolean) --*

      If set to ``true`` , allows members assigned to a workgroup to specify Amazon S3 Requester Pays
      buckets in queries. If set to ``false`` , workgroup members cannot query data from Requester
      Pays buckets, and queries that retrieve data from Requester Pays buckets cause an error. The
      default is ``false`` . For more information about Requester Pays buckets, see `Requester Pays
      Buckets <https://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html>`__ in the
      *Amazon Simple Storage Service Developer Guide* .
    """


_GetQueryResultsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetQueryResultsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetQueryResultsPaginatePaginationConfigTypeDef(
    _GetQueryResultsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetQueryResultsPaginate` `PaginationConfig`

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


_GetQueryResultsPaginateResponseResultSetResultSetMetadataColumnInfoTypeDef = TypedDict(
    "_GetQueryResultsPaginateResponseResultSetResultSetMetadataColumnInfoTypeDef",
    {
        "CatalogName": str,
        "SchemaName": str,
        "TableName": str,
        "Name": str,
        "Label": str,
        "Type": str,
        "Precision": int,
        "Scale": int,
        "Nullable": str,
        "CaseSensitive": bool,
    },
    total=False,
)


class GetQueryResultsPaginateResponseResultSetResultSetMetadataColumnInfoTypeDef(
    _GetQueryResultsPaginateResponseResultSetResultSetMetadataColumnInfoTypeDef
):
    """
    Type definition for `GetQueryResultsPaginateResponseResultSetResultSetMetadata` `ColumnInfo`

    Information about the columns in a query execution result.

    - **CatalogName** *(string) --*

      The catalog to which the query results belong.

    - **SchemaName** *(string) --*

      The schema name (database name) to which the query results belong.

    - **TableName** *(string) --*

      The table name for the query results.

    - **Name** *(string) --*

      The name of the column.

    - **Label** *(string) --*

      A column label.

    - **Type** *(string) --*

      The data type of the column.

    - **Precision** *(integer) --*

      For ``DECIMAL`` data types, specifies the total number of digits, up to 38. For
      performance reasons, we recommend up to 18 digits.

    - **Scale** *(integer) --*

      For ``DECIMAL`` data types, specifies the total number of digits in the fractional
      part of the value. Defaults to 0.

    - **Nullable** *(string) --*

      Indicates the column's nullable status.

    - **CaseSensitive** *(boolean) --*

      Indicates whether values in the column are case-sensitive.
    """


_GetQueryResultsPaginateResponseResultSetResultSetMetadataTypeDef = TypedDict(
    "_GetQueryResultsPaginateResponseResultSetResultSetMetadataTypeDef",
    {
        "ColumnInfo": List[
            GetQueryResultsPaginateResponseResultSetResultSetMetadataColumnInfoTypeDef
        ]
    },
    total=False,
)


class GetQueryResultsPaginateResponseResultSetResultSetMetadataTypeDef(
    _GetQueryResultsPaginateResponseResultSetResultSetMetadataTypeDef
):
    """
    Type definition for `GetQueryResultsPaginateResponseResultSet` `ResultSetMetadata`

    The metadata that describes the column structure and data types of a table of query results.

    - **ColumnInfo** *(list) --*

      Information about the columns returned in a query result metadata.

      - *(dict) --*

        Information about the columns in a query execution result.

        - **CatalogName** *(string) --*

          The catalog to which the query results belong.

        - **SchemaName** *(string) --*

          The schema name (database name) to which the query results belong.

        - **TableName** *(string) --*

          The table name for the query results.

        - **Name** *(string) --*

          The name of the column.

        - **Label** *(string) --*

          A column label.

        - **Type** *(string) --*

          The data type of the column.

        - **Precision** *(integer) --*

          For ``DECIMAL`` data types, specifies the total number of digits, up to 38. For
          performance reasons, we recommend up to 18 digits.

        - **Scale** *(integer) --*

          For ``DECIMAL`` data types, specifies the total number of digits in the fractional
          part of the value. Defaults to 0.

        - **Nullable** *(string) --*

          Indicates the column's nullable status.

        - **CaseSensitive** *(boolean) --*

          Indicates whether values in the column are case-sensitive.
    """


_GetQueryResultsPaginateResponseResultSetRowsDataTypeDef = TypedDict(
    "_GetQueryResultsPaginateResponseResultSetRowsDataTypeDef",
    {"VarCharValue": str},
    total=False,
)


class GetQueryResultsPaginateResponseResultSetRowsDataTypeDef(
    _GetQueryResultsPaginateResponseResultSetRowsDataTypeDef
):
    """
    Type definition for `GetQueryResultsPaginateResponseResultSetRows` `Data`

    A piece of data (a field in the table).

    - **VarCharValue** *(string) --*

      The value of the datum.
    """


_GetQueryResultsPaginateResponseResultSetRowsTypeDef = TypedDict(
    "_GetQueryResultsPaginateResponseResultSetRowsTypeDef",
    {"Data": List[GetQueryResultsPaginateResponseResultSetRowsDataTypeDef]},
    total=False,
)


class GetQueryResultsPaginateResponseResultSetRowsTypeDef(
    _GetQueryResultsPaginateResponseResultSetRowsTypeDef
):
    """
    Type definition for `GetQueryResultsPaginateResponseResultSet` `Rows`

    The rows that comprise a query result table.

    - **Data** *(list) --*

      The data that populates a row in a query result table.

      - *(dict) --*

        A piece of data (a field in the table).

        - **VarCharValue** *(string) --*

          The value of the datum.
    """


_GetQueryResultsPaginateResponseResultSetTypeDef = TypedDict(
    "_GetQueryResultsPaginateResponseResultSetTypeDef",
    {
        "Rows": List[GetQueryResultsPaginateResponseResultSetRowsTypeDef],
        "ResultSetMetadata": GetQueryResultsPaginateResponseResultSetResultSetMetadataTypeDef,
    },
    total=False,
)


class GetQueryResultsPaginateResponseResultSetTypeDef(
    _GetQueryResultsPaginateResponseResultSetTypeDef
):
    """
    Type definition for `GetQueryResultsPaginateResponse` `ResultSet`

    The results of the query execution.

    - **Rows** *(list) --*

      The rows in the table.

      - *(dict) --*

        The rows that comprise a query result table.

        - **Data** *(list) --*

          The data that populates a row in a query result table.

          - *(dict) --*

            A piece of data (a field in the table).

            - **VarCharValue** *(string) --*

              The value of the datum.

    - **ResultSetMetadata** *(dict) --*

      The metadata that describes the column structure and data types of a table of query results.

      - **ColumnInfo** *(list) --*

        Information about the columns returned in a query result metadata.

        - *(dict) --*

          Information about the columns in a query execution result.

          - **CatalogName** *(string) --*

            The catalog to which the query results belong.

          - **SchemaName** *(string) --*

            The schema name (database name) to which the query results belong.

          - **TableName** *(string) --*

            The table name for the query results.

          - **Name** *(string) --*

            The name of the column.

          - **Label** *(string) --*

            A column label.

          - **Type** *(string) --*

            The data type of the column.

          - **Precision** *(integer) --*

            For ``DECIMAL`` data types, specifies the total number of digits, up to 38. For
            performance reasons, we recommend up to 18 digits.

          - **Scale** *(integer) --*

            For ``DECIMAL`` data types, specifies the total number of digits in the fractional
            part of the value. Defaults to 0.

          - **Nullable** *(string) --*

            Indicates the column's nullable status.

          - **CaseSensitive** *(boolean) --*

            Indicates whether values in the column are case-sensitive.
    """


_GetQueryResultsPaginateResponseTypeDef = TypedDict(
    "_GetQueryResultsPaginateResponseTypeDef",
    {"UpdateCount": int, "ResultSet": GetQueryResultsPaginateResponseResultSetTypeDef},
    total=False,
)


class GetQueryResultsPaginateResponseTypeDef(_GetQueryResultsPaginateResponseTypeDef):
    """
    Type definition for `GetQueryResultsPaginate` `Response`

    - **UpdateCount** *(integer) --*

      The number of rows inserted with a CREATE TABLE AS SELECT statement.

    - **ResultSet** *(dict) --*

      The results of the query execution.

      - **Rows** *(list) --*

        The rows in the table.

        - *(dict) --*

          The rows that comprise a query result table.

          - **Data** *(list) --*

            The data that populates a row in a query result table.

            - *(dict) --*

              A piece of data (a field in the table).

              - **VarCharValue** *(string) --*

                The value of the datum.

      - **ResultSetMetadata** *(dict) --*

        The metadata that describes the column structure and data types of a table of query results.

        - **ColumnInfo** *(list) --*

          Information about the columns returned in a query result metadata.

          - *(dict) --*

            Information about the columns in a query execution result.

            - **CatalogName** *(string) --*

              The catalog to which the query results belong.

            - **SchemaName** *(string) --*

              The schema name (database name) to which the query results belong.

            - **TableName** *(string) --*

              The table name for the query results.

            - **Name** *(string) --*

              The name of the column.

            - **Label** *(string) --*

              A column label.

            - **Type** *(string) --*

              The data type of the column.

            - **Precision** *(integer) --*

              For ``DECIMAL`` data types, specifies the total number of digits, up to 38. For
              performance reasons, we recommend up to 18 digits.

            - **Scale** *(integer) --*

              For ``DECIMAL`` data types, specifies the total number of digits in the fractional
              part of the value. Defaults to 0.

            - **Nullable** *(string) --*

              Indicates the column's nullable status.

            - **CaseSensitive** *(boolean) --*

              Indicates whether values in the column are case-sensitive.
    """


_ListNamedQueriesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListNamedQueriesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListNamedQueriesPaginatePaginationConfigTypeDef(
    _ListNamedQueriesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListNamedQueriesPaginate` `PaginationConfig`

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


_ListNamedQueriesPaginateResponseTypeDef = TypedDict(
    "_ListNamedQueriesPaginateResponseTypeDef",
    {"NamedQueryIds": List[str]},
    total=False,
)


class ListNamedQueriesPaginateResponseTypeDef(_ListNamedQueriesPaginateResponseTypeDef):
    """
    Type definition for `ListNamedQueriesPaginate` `Response`

    - **NamedQueryIds** *(list) --*

      The list of unique query IDs.

      - *(string) --*
    """


_ListQueryExecutionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListQueryExecutionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListQueryExecutionsPaginatePaginationConfigTypeDef(
    _ListQueryExecutionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListQueryExecutionsPaginate` `PaginationConfig`

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


_ListQueryExecutionsPaginateResponseTypeDef = TypedDict(
    "_ListQueryExecutionsPaginateResponseTypeDef",
    {"QueryExecutionIds": List[str]},
    total=False,
)


class ListQueryExecutionsPaginateResponseTypeDef(
    _ListQueryExecutionsPaginateResponseTypeDef
):
    """
    Type definition for `ListQueryExecutionsPaginate` `Response`

    - **QueryExecutionIds** *(list) --*

      The unique IDs of each query execution as an array of strings.

      - *(string) --*
    """
