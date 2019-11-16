"Main interface for discovery type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientBatchDeleteImportDataResponseerrorsTypeDef",
    "ClientBatchDeleteImportDataResponseTypeDef",
    "ClientCreateApplicationResponseTypeDef",
    "ClientCreateTagstagsTypeDef",
    "ClientDeleteTagstagsTypeDef",
    "ClientDescribeAgentsResponseagentsInfoagentNetworkInfoListTypeDef",
    "ClientDescribeAgentsResponseagentsInfoTypeDef",
    "ClientDescribeAgentsResponseTypeDef",
    "ClientDescribeAgentsfiltersTypeDef",
    "ClientDescribeConfigurationsResponseTypeDef",
    "ClientDescribeContinuousExportsResponsedescriptionsTypeDef",
    "ClientDescribeContinuousExportsResponseTypeDef",
    "ClientDescribeExportConfigurationsResponseexportsInfoTypeDef",
    "ClientDescribeExportConfigurationsResponseTypeDef",
    "ClientDescribeExportTasksResponseexportsInfoTypeDef",
    "ClientDescribeExportTasksResponseTypeDef",
    "ClientDescribeExportTasksfiltersTypeDef",
    "ClientDescribeImportTasksResponsetasksTypeDef",
    "ClientDescribeImportTasksResponseTypeDef",
    "ClientDescribeImportTasksfiltersTypeDef",
    "ClientDescribeTagsResponsetagsTypeDef",
    "ClientDescribeTagsResponseTypeDef",
    "ClientDescribeTagsfiltersTypeDef",
    "ClientExportConfigurationsResponseTypeDef",
    "ClientGetDiscoverySummaryResponseagentSummaryTypeDef",
    "ClientGetDiscoverySummaryResponseconnectorSummaryTypeDef",
    "ClientGetDiscoverySummaryResponseTypeDef",
    "ClientListConfigurationsResponseTypeDef",
    "ClientListConfigurationsfiltersTypeDef",
    "ClientListConfigurationsorderByTypeDef",
    "ClientListServerNeighborsResponseneighborsTypeDef",
    "ClientListServerNeighborsResponseTypeDef",
    "ClientStartContinuousExportResponseTypeDef",
    "ClientStartDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef",
    "ClientStartDataCollectionByAgentIdsResponseTypeDef",
    "ClientStartExportTaskResponseTypeDef",
    "ClientStartExportTaskfiltersTypeDef",
    "ClientStartImportTaskResponsetaskTypeDef",
    "ClientStartImportTaskResponseTypeDef",
    "ClientStopContinuousExportResponseTypeDef",
    "ClientStopDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef",
    "ClientStopDataCollectionByAgentIdsResponseTypeDef",
    "DescribeAgentsPaginatePaginationConfigTypeDef",
    "DescribeAgentsPaginateResponseagentsInfoagentNetworkInfoListTypeDef",
    "DescribeAgentsPaginateResponseagentsInfoTypeDef",
    "DescribeAgentsPaginateResponseTypeDef",
    "DescribeAgentsPaginatefiltersTypeDef",
    "DescribeContinuousExportsPaginatePaginationConfigTypeDef",
    "DescribeContinuousExportsPaginateResponsedescriptionsTypeDef",
    "DescribeContinuousExportsPaginateResponseTypeDef",
    "DescribeExportConfigurationsPaginatePaginationConfigTypeDef",
    "DescribeExportConfigurationsPaginateResponseexportsInfoTypeDef",
    "DescribeExportConfigurationsPaginateResponseTypeDef",
    "DescribeExportTasksPaginatePaginationConfigTypeDef",
    "DescribeExportTasksPaginateResponseexportsInfoTypeDef",
    "DescribeExportTasksPaginateResponseTypeDef",
    "DescribeExportTasksPaginatefiltersTypeDef",
    "DescribeTagsPaginatePaginationConfigTypeDef",
    "DescribeTagsPaginateResponsetagsTypeDef",
    "DescribeTagsPaginateResponseTypeDef",
    "DescribeTagsPaginatefiltersTypeDef",
    "ListConfigurationsPaginatePaginationConfigTypeDef",
    "ListConfigurationsPaginateResponseTypeDef",
    "ListConfigurationsPaginatefiltersTypeDef",
    "ListConfigurationsPaginateorderByTypeDef",
)


_ClientBatchDeleteImportDataResponseerrorsTypeDef = TypedDict(
    "_ClientBatchDeleteImportDataResponseerrorsTypeDef",
    {"importTaskId": str, "errorCode": str, "errorDescription": str},
    total=False,
)


class ClientBatchDeleteImportDataResponseerrorsTypeDef(
    _ClientBatchDeleteImportDataResponseerrorsTypeDef
):
    """
    Type definition for `ClientBatchDeleteImportDataResponse` `errors`

    Error messages returned for each import task that you deleted as a response for this
    command.

    - **importTaskId** *(string) --*

      The unique import ID associated with the error that occurred.

    - **errorCode** *(string) --*

      The type of error that occurred for a specific import task.

    - **errorDescription** *(string) --*

      The description of the error that occurred for a specific import task.
    """


_ClientBatchDeleteImportDataResponseTypeDef = TypedDict(
    "_ClientBatchDeleteImportDataResponseTypeDef",
    {"errors": List[ClientBatchDeleteImportDataResponseerrorsTypeDef]},
    total=False,
)


class ClientBatchDeleteImportDataResponseTypeDef(
    _ClientBatchDeleteImportDataResponseTypeDef
):
    """
    Type definition for `ClientBatchDeleteImportData` `Response`

    - **errors** *(list) --*

      Error messages returned for each import task that you deleted as a response for this command.

      - *(dict) --*

        Error messages returned for each import task that you deleted as a response for this
        command.

        - **importTaskId** *(string) --*

          The unique import ID associated with the error that occurred.

        - **errorCode** *(string) --*

          The type of error that occurred for a specific import task.

        - **errorDescription** *(string) --*

          The description of the error that occurred for a specific import task.
    """


_ClientCreateApplicationResponseTypeDef = TypedDict(
    "_ClientCreateApplicationResponseTypeDef", {"configurationId": str}, total=False
)


class ClientCreateApplicationResponseTypeDef(_ClientCreateApplicationResponseTypeDef):
    """
    Type definition for `ClientCreateApplication` `Response`

    - **configurationId** *(string) --*

      Configuration ID of an application to be created.
    """


_ClientCreateTagstagsTypeDef = TypedDict(
    "_ClientCreateTagstagsTypeDef", {"key": str, "value": str}
)


class ClientCreateTagstagsTypeDef(_ClientCreateTagstagsTypeDef):
    """
    Type definition for `ClientCreateTags` `tags`

    Metadata that help you categorize IT assets.

    - **key** *(string) --* **[REQUIRED]**

      The type of tag on which to filter.

    - **value** *(string) --* **[REQUIRED]**

      A value for a tag key on which to filter.
    """


_ClientDeleteTagstagsTypeDef = TypedDict(
    "_ClientDeleteTagstagsTypeDef", {"key": str, "value": str}
)


class ClientDeleteTagstagsTypeDef(_ClientDeleteTagstagsTypeDef):
    """
    Type definition for `ClientDeleteTags` `tags`

    Metadata that help you categorize IT assets.

    - **key** *(string) --* **[REQUIRED]**

      The type of tag on which to filter.

    - **value** *(string) --* **[REQUIRED]**

      A value for a tag key on which to filter.
    """


_ClientDescribeAgentsResponseagentsInfoagentNetworkInfoListTypeDef = TypedDict(
    "_ClientDescribeAgentsResponseagentsInfoagentNetworkInfoListTypeDef",
    {"ipAddress": str, "macAddress": str},
    total=False,
)


class ClientDescribeAgentsResponseagentsInfoagentNetworkInfoListTypeDef(
    _ClientDescribeAgentsResponseagentsInfoagentNetworkInfoListTypeDef
):
    """
    Type definition for `ClientDescribeAgentsResponseagentsInfo` `agentNetworkInfoList`

    Network details about the host where the agent/connector resides.

    - **ipAddress** *(string) --*

      The IP address for the host where the agent/connector resides.

    - **macAddress** *(string) --*

      The MAC address for the host where the agent/connector resides.
    """


_ClientDescribeAgentsResponseagentsInfoTypeDef = TypedDict(
    "_ClientDescribeAgentsResponseagentsInfoTypeDef",
    {
        "agentId": str,
        "hostName": str,
        "agentNetworkInfoList": List[
            ClientDescribeAgentsResponseagentsInfoagentNetworkInfoListTypeDef
        ],
        "connectorId": str,
        "version": str,
        "health": str,
        "lastHealthPingTime": str,
        "collectionStatus": str,
        "agentType": str,
        "registeredTime": str,
    },
    total=False,
)


class ClientDescribeAgentsResponseagentsInfoTypeDef(
    _ClientDescribeAgentsResponseagentsInfoTypeDef
):
    """
    Type definition for `ClientDescribeAgentsResponse` `agentsInfo`

    Information about agents or connectors associated with the user’s AWS account. Information
    includes agent or connector IDs, IP addresses, media access control (MAC) addresses, agent
    or connector health, hostname where the agent or connector resides, and agent version for
    each agent.

    - **agentId** *(string) --*

      The agent or connector ID.

    - **hostName** *(string) --*

      The name of the host where the agent or connector resides. The host can be a server or
      virtual machine.

    - **agentNetworkInfoList** *(list) --*

      Network details about the host where the agent or connector resides.

      - *(dict) --*

        Network details about the host where the agent/connector resides.

        - **ipAddress** *(string) --*

          The IP address for the host where the agent/connector resides.

        - **macAddress** *(string) --*

          The MAC address for the host where the agent/connector resides.

    - **connectorId** *(string) --*

      The ID of the connector.

    - **version** *(string) --*

      The agent or connector version.

    - **health** *(string) --*

      The health of the agent or connector.

    - **lastHealthPingTime** *(string) --*

      Time since agent or connector health was reported.

    - **collectionStatus** *(string) --*

      Status of the collection process for an agent or connector.

    - **agentType** *(string) --*

      Type of agent.

    - **registeredTime** *(string) --*

      Agent's first registration timestamp in UTC.
    """


_ClientDescribeAgentsResponseTypeDef = TypedDict(
    "_ClientDescribeAgentsResponseTypeDef",
    {
        "agentsInfo": List[ClientDescribeAgentsResponseagentsInfoTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeAgentsResponseTypeDef(_ClientDescribeAgentsResponseTypeDef):
    """
    Type definition for `ClientDescribeAgents` `Response`

    - **agentsInfo** *(list) --*

      Lists agents or the Connector by ID or lists all agents/Connectors associated with your user
      account if you did not specify an agent/Connector ID. The output includes agent/Connector
      IDs, IP addresses, media access control (MAC) addresses, agent/Connector health, host name
      where the agent/Connector resides, and the version number of each agent/Connector.

      - *(dict) --*

        Information about agents or connectors associated with the user’s AWS account. Information
        includes agent or connector IDs, IP addresses, media access control (MAC) addresses, agent
        or connector health, hostname where the agent or connector resides, and agent version for
        each agent.

        - **agentId** *(string) --*

          The agent or connector ID.

        - **hostName** *(string) --*

          The name of the host where the agent or connector resides. The host can be a server or
          virtual machine.

        - **agentNetworkInfoList** *(list) --*

          Network details about the host where the agent or connector resides.

          - *(dict) --*

            Network details about the host where the agent/connector resides.

            - **ipAddress** *(string) --*

              The IP address for the host where the agent/connector resides.

            - **macAddress** *(string) --*

              The MAC address for the host where the agent/connector resides.

        - **connectorId** *(string) --*

          The ID of the connector.

        - **version** *(string) --*

          The agent or connector version.

        - **health** *(string) --*

          The health of the agent or connector.

        - **lastHealthPingTime** *(string) --*

          Time since agent or connector health was reported.

        - **collectionStatus** *(string) --*

          Status of the collection process for an agent or connector.

        - **agentType** *(string) --*

          Type of agent.

        - **registeredTime** *(string) --*

          Agent's first registration timestamp in UTC.

    - **nextToken** *(string) --*

      Token to retrieve the next set of results. For example, if you specified 100 IDs for
      ``DescribeAgentsRequest$agentIds`` but set ``DescribeAgentsRequest$maxResults`` to 10, you
      received a set of 10 results along with this token. Use this token in the next query to
      retrieve the next set of 10.
    """


_ClientDescribeAgentsfiltersTypeDef = TypedDict(
    "_ClientDescribeAgentsfiltersTypeDef",
    {"name": str, "values": List[str], "condition": str},
)


class ClientDescribeAgentsfiltersTypeDef(_ClientDescribeAgentsfiltersTypeDef):
    """
    Type definition for `ClientDescribeAgents` `filters`

    A filter that can use conditional operators.

    For more information about filters, see `Querying Discovered Configuration Items
    <http://docs.aws.amazon.com/application-discovery/latest/APIReference/discovery-api-queries.html>`__
    .

    - **name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **values** *(list) --* **[REQUIRED]**

      A string value on which to filter. For example, if you choose the
      ``destinationServer.osVersion`` filter name, you could specify ``Ubuntu`` for the value.

      - *(string) --*

    - **condition** *(string) --* **[REQUIRED]**

      A conditional operator. The following operators are valid: EQUALS, NOT_EQUALS, CONTAINS,
      NOT_CONTAINS. If you specify multiple filters, the system utilizes all filters as though
      concatenated by *AND* . If you specify multiple values for a particular filter, the system
      differentiates the values using *OR* . Calling either *DescribeConfigurations* or
      *ListConfigurations* returns attributes of matching configuration items.
    """


_ClientDescribeConfigurationsResponseTypeDef = TypedDict(
    "_ClientDescribeConfigurationsResponseTypeDef",
    {"configurations": List[Dict[str, str]]},
    total=False,
)


class ClientDescribeConfigurationsResponseTypeDef(
    _ClientDescribeConfigurationsResponseTypeDef
):
    """
    Type definition for `ClientDescribeConfigurations` `Response`

    - **configurations** *(list) --*

      A key in the response map. The value is an array of data.

      - *(dict) --*

        - *(string) --*

          - *(string) --*
    """


_ClientDescribeContinuousExportsResponsedescriptionsTypeDef = TypedDict(
    "_ClientDescribeContinuousExportsResponsedescriptionsTypeDef",
    {
        "exportId": str,
        "status": str,
        "statusDetail": str,
        "s3Bucket": str,
        "startTime": datetime,
        "stopTime": datetime,
        "dataSource": str,
        "schemaStorageConfig": Dict[str, str],
    },
    total=False,
)


class ClientDescribeContinuousExportsResponsedescriptionsTypeDef(
    _ClientDescribeContinuousExportsResponsedescriptionsTypeDef
):
    """
    Type definition for `ClientDescribeContinuousExportsResponse` `descriptions`

    A list of continuous export descriptions.

    - **exportId** *(string) --*

      The unique ID assigned to this export.

    - **status** *(string) --*

      Describes the status of the export. Can be one of the following values:

      * START_IN_PROGRESS - setting up resources to start continuous export.

      * START_FAILED - an error occurred setting up continuous export. To recover, call
      start-continuous-export again.

      * ACTIVE - data is being exported to the customer bucket.

      * ERROR - an error occurred during export. To fix the issue, call stop-continuous-export
      and start-continuous-export.

      * STOP_IN_PROGRESS - stopping the export.

      * STOP_FAILED - an error occurred stopping the export. To recover, call
      stop-continuous-export again.

      * INACTIVE - the continuous export has been stopped. Data is no longer being exported to
      the customer bucket.

    - **statusDetail** *(string) --*

      Contains information about any errors that have occurred. This data type can have the
      following values:

      * ACCESS_DENIED - You don’t have permission to start Data Exploration in Amazon Athena.
      Contact your AWS administrator for help. For more information, see `Setting Up AWS
      Application Discovery Service
      <http://docs.aws.amazon.com/application-discovery/latest/userguide/setting-up.html>`__ in
      the Application Discovery Service User Guide.

      * DELIVERY_STREAM_LIMIT_FAILURE - You reached the limit for Amazon Kinesis Data Firehose
      delivery streams. Reduce the number of streams or request a limit increase and try again.
      For more information, see `Kinesis Data Streams Limits
      <http://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html>`__ in the
      Amazon Kinesis Data Streams Developer Guide.

      * FIREHOSE_ROLE_MISSING - The Data Exploration feature is in an error state because your
      IAM User is missing the AWSApplicationDiscoveryServiceFirehose role. Turn on Data
      Exploration in Amazon Athena and try again. For more information, see `Step 3\\: Provide
      Application Discovery Service Access to Non-Administrator Users by Attaching Policies
      <http://docs.aws.amazon.com/application-discovery/latest/userguide/setting-up.html#setting-up-user-policy>`__
      in the Application Discovery Service User Guide.

      * FIREHOSE_STREAM_DOES_NOT_EXIST - The Data Exploration feature is in an error state
      because your IAM User is missing one or more of the Kinesis data delivery streams.

      * INTERNAL_FAILURE - The Data Exploration feature is in an error state because of an
      internal failure. Try again later. If this problem persists, contact AWS Support.

      * S3_BUCKET_LIMIT_FAILURE - You reached the limit for Amazon S3 buckets. Reduce the
      number of Amazon S3 buckets or request a limit increase and try again. For more
      information, see `Bucket Restrictions and Limitations
      <http://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html>`__ in the Amazon
      Simple Storage Service Developer Guide.

      * S3_NOT_SIGNED_UP - Your account is not signed up for the Amazon S3 service. You must
      sign up before you can use Amazon S3. You can sign up at the following URL:
      `https\\://aws.amazon.com/s3 <https://aws.amazon.com/s3>`__ .

    - **s3Bucket** *(string) --*

      The name of the s3 bucket where the export data parquet files are stored.

    - **startTime** *(datetime) --*

      The timestamp representing when the continuous export was started.

    - **stopTime** *(datetime) --*

      The timestamp that represents when this continuous export was stopped.

    - **dataSource** *(string) --*

      The type of data collector used to gather this data (currently only offered for AGENT).

    - **schemaStorageConfig** *(dict) --*

      An object which describes how the data is stored.

      * ``databaseName`` - the name of the Glue database used to store the schema.

      - *(string) --*

        - *(string) --*
    """


_ClientDescribeContinuousExportsResponseTypeDef = TypedDict(
    "_ClientDescribeContinuousExportsResponseTypeDef",
    {
        "descriptions": List[
            ClientDescribeContinuousExportsResponsedescriptionsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeContinuousExportsResponseTypeDef(
    _ClientDescribeContinuousExportsResponseTypeDef
):
    """
    Type definition for `ClientDescribeContinuousExports` `Response`

    - **descriptions** *(list) --*

      A list of continuous export descriptions.

      - *(dict) --*

        A list of continuous export descriptions.

        - **exportId** *(string) --*

          The unique ID assigned to this export.

        - **status** *(string) --*

          Describes the status of the export. Can be one of the following values:

          * START_IN_PROGRESS - setting up resources to start continuous export.

          * START_FAILED - an error occurred setting up continuous export. To recover, call
          start-continuous-export again.

          * ACTIVE - data is being exported to the customer bucket.

          * ERROR - an error occurred during export. To fix the issue, call stop-continuous-export
          and start-continuous-export.

          * STOP_IN_PROGRESS - stopping the export.

          * STOP_FAILED - an error occurred stopping the export. To recover, call
          stop-continuous-export again.

          * INACTIVE - the continuous export has been stopped. Data is no longer being exported to
          the customer bucket.

        - **statusDetail** *(string) --*

          Contains information about any errors that have occurred. This data type can have the
          following values:

          * ACCESS_DENIED - You don’t have permission to start Data Exploration in Amazon Athena.
          Contact your AWS administrator for help. For more information, see `Setting Up AWS
          Application Discovery Service
          <http://docs.aws.amazon.com/application-discovery/latest/userguide/setting-up.html>`__ in
          the Application Discovery Service User Guide.

          * DELIVERY_STREAM_LIMIT_FAILURE - You reached the limit for Amazon Kinesis Data Firehose
          delivery streams. Reduce the number of streams or request a limit increase and try again.
          For more information, see `Kinesis Data Streams Limits
          <http://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html>`__ in the
          Amazon Kinesis Data Streams Developer Guide.

          * FIREHOSE_ROLE_MISSING - The Data Exploration feature is in an error state because your
          IAM User is missing the AWSApplicationDiscoveryServiceFirehose role. Turn on Data
          Exploration in Amazon Athena and try again. For more information, see `Step 3\\: Provide
          Application Discovery Service Access to Non-Administrator Users by Attaching Policies
          <http://docs.aws.amazon.com/application-discovery/latest/userguide/setting-up.html#setting-up-user-policy>`__
          in the Application Discovery Service User Guide.

          * FIREHOSE_STREAM_DOES_NOT_EXIST - The Data Exploration feature is in an error state
          because your IAM User is missing one or more of the Kinesis data delivery streams.

          * INTERNAL_FAILURE - The Data Exploration feature is in an error state because of an
          internal failure. Try again later. If this problem persists, contact AWS Support.

          * S3_BUCKET_LIMIT_FAILURE - You reached the limit for Amazon S3 buckets. Reduce the
          number of Amazon S3 buckets or request a limit increase and try again. For more
          information, see `Bucket Restrictions and Limitations
          <http://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html>`__ in the Amazon
          Simple Storage Service Developer Guide.

          * S3_NOT_SIGNED_UP - Your account is not signed up for the Amazon S3 service. You must
          sign up before you can use Amazon S3. You can sign up at the following URL:
          `https\\://aws.amazon.com/s3 <https://aws.amazon.com/s3>`__ .

        - **s3Bucket** *(string) --*

          The name of the s3 bucket where the export data parquet files are stored.

        - **startTime** *(datetime) --*

          The timestamp representing when the continuous export was started.

        - **stopTime** *(datetime) --*

          The timestamp that represents when this continuous export was stopped.

        - **dataSource** *(string) --*

          The type of data collector used to gather this data (currently only offered for AGENT).

        - **schemaStorageConfig** *(dict) --*

          An object which describes how the data is stored.

          * ``databaseName`` - the name of the Glue database used to store the schema.

          - *(string) --*

            - *(string) --*

    - **nextToken** *(string) --*

      The token from the previous call to ``DescribeExportTasks`` .
    """


_ClientDescribeExportConfigurationsResponseexportsInfoTypeDef = TypedDict(
    "_ClientDescribeExportConfigurationsResponseexportsInfoTypeDef",
    {
        "exportId": str,
        "exportStatus": str,
        "statusMessage": str,
        "configurationsDownloadUrl": str,
        "exportRequestTime": datetime,
        "isTruncated": bool,
        "requestedStartTime": datetime,
        "requestedEndTime": datetime,
    },
    total=False,
)


class ClientDescribeExportConfigurationsResponseexportsInfoTypeDef(
    _ClientDescribeExportConfigurationsResponseexportsInfoTypeDef
):
    """
    Type definition for `ClientDescribeExportConfigurationsResponse` `exportsInfo`

    Information regarding the export status of discovered data. The value is an array of
    objects.

    - **exportId** *(string) --*

      A unique identifier used to query an export.

    - **exportStatus** *(string) --*

      The status of the data export job.

    - **statusMessage** *(string) --*

      A status message provided for API callers.

    - **configurationsDownloadUrl** *(string) --*

      A URL for an Amazon S3 bucket where you can review the exported data. The URL is
      displayed only if the export succeeded.

    - **exportRequestTime** *(datetime) --*

      The time that the data export was initiated.

    - **isTruncated** *(boolean) --*

      If true, the export of agent information exceeded the size limit for a single export and
      the exported data is incomplete for the requested time range. To address this, select a
      smaller time range for the export by using ``startDate`` and ``endDate`` .

    - **requestedStartTime** *(datetime) --*

      The value of ``startTime`` parameter in the ``StartExportTask`` request. If no
      ``startTime`` was requested, this result does not appear in ``ExportInfo`` .

    - **requestedEndTime** *(datetime) --*

      The ``endTime`` used in the ``StartExportTask`` request. If no ``endTime`` was requested,
      this result does not appear in ``ExportInfo`` .
    """


_ClientDescribeExportConfigurationsResponseTypeDef = TypedDict(
    "_ClientDescribeExportConfigurationsResponseTypeDef",
    {
        "exportsInfo": List[
            ClientDescribeExportConfigurationsResponseexportsInfoTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeExportConfigurationsResponseTypeDef(
    _ClientDescribeExportConfigurationsResponseTypeDef
):
    """
    Type definition for `ClientDescribeExportConfigurations` `Response`

    - **exportsInfo** *(list) --*

      - *(dict) --*

        Information regarding the export status of discovered data. The value is an array of
        objects.

        - **exportId** *(string) --*

          A unique identifier used to query an export.

        - **exportStatus** *(string) --*

          The status of the data export job.

        - **statusMessage** *(string) --*

          A status message provided for API callers.

        - **configurationsDownloadUrl** *(string) --*

          A URL for an Amazon S3 bucket where you can review the exported data. The URL is
          displayed only if the export succeeded.

        - **exportRequestTime** *(datetime) --*

          The time that the data export was initiated.

        - **isTruncated** *(boolean) --*

          If true, the export of agent information exceeded the size limit for a single export and
          the exported data is incomplete for the requested time range. To address this, select a
          smaller time range for the export by using ``startDate`` and ``endDate`` .

        - **requestedStartTime** *(datetime) --*

          The value of ``startTime`` parameter in the ``StartExportTask`` request. If no
          ``startTime`` was requested, this result does not appear in ``ExportInfo`` .

        - **requestedEndTime** *(datetime) --*

          The ``endTime`` used in the ``StartExportTask`` request. If no ``endTime`` was requested,
          this result does not appear in ``ExportInfo`` .

    - **nextToken** *(string) --*

      The token from the previous call to describe-export-tasks.
    """


_ClientDescribeExportTasksResponseexportsInfoTypeDef = TypedDict(
    "_ClientDescribeExportTasksResponseexportsInfoTypeDef",
    {
        "exportId": str,
        "exportStatus": str,
        "statusMessage": str,
        "configurationsDownloadUrl": str,
        "exportRequestTime": datetime,
        "isTruncated": bool,
        "requestedStartTime": datetime,
        "requestedEndTime": datetime,
    },
    total=False,
)


class ClientDescribeExportTasksResponseexportsInfoTypeDef(
    _ClientDescribeExportTasksResponseexportsInfoTypeDef
):
    """
    Type definition for `ClientDescribeExportTasksResponse` `exportsInfo`

    Information regarding the export status of discovered data. The value is an array of
    objects.

    - **exportId** *(string) --*

      A unique identifier used to query an export.

    - **exportStatus** *(string) --*

      The status of the data export job.

    - **statusMessage** *(string) --*

      A status message provided for API callers.

    - **configurationsDownloadUrl** *(string) --*

      A URL for an Amazon S3 bucket where you can review the exported data. The URL is
      displayed only if the export succeeded.

    - **exportRequestTime** *(datetime) --*

      The time that the data export was initiated.

    - **isTruncated** *(boolean) --*

      If true, the export of agent information exceeded the size limit for a single export and
      the exported data is incomplete for the requested time range. To address this, select a
      smaller time range for the export by using ``startDate`` and ``endDate`` .

    - **requestedStartTime** *(datetime) --*

      The value of ``startTime`` parameter in the ``StartExportTask`` request. If no
      ``startTime`` was requested, this result does not appear in ``ExportInfo`` .

    - **requestedEndTime** *(datetime) --*

      The ``endTime`` used in the ``StartExportTask`` request. If no ``endTime`` was requested,
      this result does not appear in ``ExportInfo`` .
    """


_ClientDescribeExportTasksResponseTypeDef = TypedDict(
    "_ClientDescribeExportTasksResponseTypeDef",
    {
        "exportsInfo": List[ClientDescribeExportTasksResponseexportsInfoTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeExportTasksResponseTypeDef(
    _ClientDescribeExportTasksResponseTypeDef
):
    """
    Type definition for `ClientDescribeExportTasks` `Response`

    - **exportsInfo** *(list) --*

      Contains one or more sets of export request details. When the status of a request is
      ``SUCCEEDED`` , the response includes a URL for an Amazon S3 bucket where you can view the
      data in a CSV file.

      - *(dict) --*

        Information regarding the export status of discovered data. The value is an array of
        objects.

        - **exportId** *(string) --*

          A unique identifier used to query an export.

        - **exportStatus** *(string) --*

          The status of the data export job.

        - **statusMessage** *(string) --*

          A status message provided for API callers.

        - **configurationsDownloadUrl** *(string) --*

          A URL for an Amazon S3 bucket where you can review the exported data. The URL is
          displayed only if the export succeeded.

        - **exportRequestTime** *(datetime) --*

          The time that the data export was initiated.

        - **isTruncated** *(boolean) --*

          If true, the export of agent information exceeded the size limit for a single export and
          the exported data is incomplete for the requested time range. To address this, select a
          smaller time range for the export by using ``startDate`` and ``endDate`` .

        - **requestedStartTime** *(datetime) --*

          The value of ``startTime`` parameter in the ``StartExportTask`` request. If no
          ``startTime`` was requested, this result does not appear in ``ExportInfo`` .

        - **requestedEndTime** *(datetime) --*

          The ``endTime`` used in the ``StartExportTask`` request. If no ``endTime`` was requested,
          this result does not appear in ``ExportInfo`` .

    - **nextToken** *(string) --*

      The ``nextToken`` value to include in a future ``DescribeExportTasks`` request. When the
      results of a ``DescribeExportTasks`` request exceed ``maxResults`` , this value can be used
      to retrieve the next page of results. This value is null when there are no more results to
      return.
    """


_ClientDescribeExportTasksfiltersTypeDef = TypedDict(
    "_ClientDescribeExportTasksfiltersTypeDef",
    {"name": str, "values": List[str], "condition": str},
)


class ClientDescribeExportTasksfiltersTypeDef(_ClientDescribeExportTasksfiltersTypeDef):
    """
    Type definition for `ClientDescribeExportTasks` `filters`

    Used to select which agent's data is to be exported. A single agent ID may be selected for
    export using the `StartExportTask
    <http://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StartExportTask.html>`__
    action.

    - **name** *(string) --* **[REQUIRED]**

      A single ``ExportFilter`` name. Supported filters: ``agentId`` .

    - **values** *(list) --* **[REQUIRED]**

      A single ``agentId`` for a Discovery Agent. An ``agentId`` can be found using the
      `DescribeAgents
      <http://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeExportTasks.html>`__
      action. Typically an ADS ``agentId`` is in the form ``o-0123456789abcdef0`` .

      - *(string) --*

    - **condition** *(string) --* **[REQUIRED]**

      Supported condition: ``EQUALS``
    """


_ClientDescribeImportTasksResponsetasksTypeDef = TypedDict(
    "_ClientDescribeImportTasksResponsetasksTypeDef",
    {
        "importTaskId": str,
        "clientRequestToken": str,
        "name": str,
        "importUrl": str,
        "status": str,
        "importRequestTime": datetime,
        "importCompletionTime": datetime,
        "importDeletedTime": datetime,
        "serverImportSuccess": int,
        "serverImportFailure": int,
        "applicationImportSuccess": int,
        "applicationImportFailure": int,
        "errorsAndFailedEntriesZip": str,
    },
    total=False,
)


class ClientDescribeImportTasksResponsetasksTypeDef(
    _ClientDescribeImportTasksResponsetasksTypeDef
):
    """
    Type definition for `ClientDescribeImportTasksResponse` `tasks`

    An array of information related to the import task request that includes status
    information, times, IDs, the Amazon S3 Object URL for the import file, and more.

    - **importTaskId** *(string) --*

      The unique ID for a specific import task. These IDs aren't globally unique, but they are
      unique within an AWS account.

    - **clientRequestToken** *(string) --*

      A unique token used to prevent the same import request from occurring more than once. If
      you didn't provide a token, a token was automatically generated when the import task
      request was sent.

    - **name** *(string) --*

      A descriptive name for an import task. You can use this name to filter future requests
      related to this import task, such as identifying applications and servers that were
      included in this import task. We recommend that you use a meaningful name for each import
      task.

    - **importUrl** *(string) --*

      The URL for your import file that you've uploaded to Amazon S3.

    - **status** *(string) --*

      The status of the import task. An import can have the status of ``IMPORT_COMPLETE`` and
      still have some records fail to import from the overall request. More information can be
      found in the downloadable archive defined in the ``errorsAndFailedEntriesZip`` field, or
      in the Migration Hub management console.

    - **importRequestTime** *(datetime) --*

      The time that the import task request was made, presented in the Unix time stamp format.

    - **importCompletionTime** *(datetime) --*

      The time that the import task request finished, presented in the Unix time stamp format.

    - **importDeletedTime** *(datetime) --*

      The time that the import task request was deleted, presented in the Unix time stamp
      format.

    - **serverImportSuccess** *(integer) --*

      The total number of server records in the import file that were successfully imported.

    - **serverImportFailure** *(integer) --*

      The total number of server records in the import file that failed to be imported.

    - **applicationImportSuccess** *(integer) --*

      The total number of application records in the import file that were successfully
      imported.

    - **applicationImportFailure** *(integer) --*

      The total number of application records in the import file that failed to be imported.

    - **errorsAndFailedEntriesZip** *(string) --*

      A link to a compressed archive folder (in the ZIP format) that contains an error log and
      a file of failed records. You can use these two files to quickly identify records that
      failed, why they failed, and correct those records. Afterward, you can upload the
      corrected file to your Amazon S3 bucket and create another import task request.

      This field also includes authorization information so you can confirm the authenticity of
      the compressed archive before you download it.

      If some records failed to be imported we recommend that you correct the records in the
      failed entries file and then imports that failed entries file. This prevents you from
      having to correct and update the larger original file and attempt importing it again.
    """


_ClientDescribeImportTasksResponseTypeDef = TypedDict(
    "_ClientDescribeImportTasksResponseTypeDef",
    {"nextToken": str, "tasks": List[ClientDescribeImportTasksResponsetasksTypeDef]},
    total=False,
)


class ClientDescribeImportTasksResponseTypeDef(
    _ClientDescribeImportTasksResponseTypeDef
):
    """
    Type definition for `ClientDescribeImportTasks` `Response`

    - **nextToken** *(string) --*

      The token to request the next page of results.

    - **tasks** *(list) --*

      A returned array of import tasks that match any applied filters, up to the specified number
      of maximum results.

      - *(dict) --*

        An array of information related to the import task request that includes status
        information, times, IDs, the Amazon S3 Object URL for the import file, and more.

        - **importTaskId** *(string) --*

          The unique ID for a specific import task. These IDs aren't globally unique, but they are
          unique within an AWS account.

        - **clientRequestToken** *(string) --*

          A unique token used to prevent the same import request from occurring more than once. If
          you didn't provide a token, a token was automatically generated when the import task
          request was sent.

        - **name** *(string) --*

          A descriptive name for an import task. You can use this name to filter future requests
          related to this import task, such as identifying applications and servers that were
          included in this import task. We recommend that you use a meaningful name for each import
          task.

        - **importUrl** *(string) --*

          The URL for your import file that you've uploaded to Amazon S3.

        - **status** *(string) --*

          The status of the import task. An import can have the status of ``IMPORT_COMPLETE`` and
          still have some records fail to import from the overall request. More information can be
          found in the downloadable archive defined in the ``errorsAndFailedEntriesZip`` field, or
          in the Migration Hub management console.

        - **importRequestTime** *(datetime) --*

          The time that the import task request was made, presented in the Unix time stamp format.

        - **importCompletionTime** *(datetime) --*

          The time that the import task request finished, presented in the Unix time stamp format.

        - **importDeletedTime** *(datetime) --*

          The time that the import task request was deleted, presented in the Unix time stamp
          format.

        - **serverImportSuccess** *(integer) --*

          The total number of server records in the import file that were successfully imported.

        - **serverImportFailure** *(integer) --*

          The total number of server records in the import file that failed to be imported.

        - **applicationImportSuccess** *(integer) --*

          The total number of application records in the import file that were successfully
          imported.

        - **applicationImportFailure** *(integer) --*

          The total number of application records in the import file that failed to be imported.

        - **errorsAndFailedEntriesZip** *(string) --*

          A link to a compressed archive folder (in the ZIP format) that contains an error log and
          a file of failed records. You can use these two files to quickly identify records that
          failed, why they failed, and correct those records. Afterward, you can upload the
          corrected file to your Amazon S3 bucket and create another import task request.

          This field also includes authorization information so you can confirm the authenticity of
          the compressed archive before you download it.

          If some records failed to be imported we recommend that you correct the records in the
          failed entries file and then imports that failed entries file. This prevents you from
          having to correct and update the larger original file and attempt importing it again.
    """


_ClientDescribeImportTasksfiltersTypeDef = TypedDict(
    "_ClientDescribeImportTasksfiltersTypeDef",
    {"name": str, "values": List[str]},
    total=False,
)


class ClientDescribeImportTasksfiltersTypeDef(_ClientDescribeImportTasksfiltersTypeDef):
    """
    Type definition for `ClientDescribeImportTasks` `filters`

    A name-values pair of elements you can use to filter the results when querying your import
    tasks. Currently, wildcards are not supported for filters.

    .. note::

      When filtering by import status, all other filter values are ignored.

    - **name** *(string) --*

      The name, status, or import task ID for a specific import task.

    - **values** *(list) --*

      An array of strings that you can provide to match against a specific name, status, or import
      task ID to filter the results for your import task queries.

      - *(string) --*
    """


_ClientDescribeTagsResponsetagsTypeDef = TypedDict(
    "_ClientDescribeTagsResponsetagsTypeDef",
    {
        "configurationType": str,
        "configurationId": str,
        "key": str,
        "value": str,
        "timeOfCreation": datetime,
    },
    total=False,
)


class ClientDescribeTagsResponsetagsTypeDef(_ClientDescribeTagsResponsetagsTypeDef):
    """
    Type definition for `ClientDescribeTagsResponse` `tags`

    Tags for a configuration item. Tags are metadata that help you categorize IT assets.

    - **configurationType** *(string) --*

      A type of IT asset to tag.

    - **configurationId** *(string) --*

      The configuration ID for the item to tag. You can specify a list of keys and values.

    - **key** *(string) --*

      A type of tag on which to filter. For example, *serverType* .

    - **value** *(string) --*

      A value on which to filter. For example *key = serverType* and *value = web server* .

    - **timeOfCreation** *(datetime) --*

      The time the configuration tag was created in Coordinated Universal Time (UTC).
    """


_ClientDescribeTagsResponseTypeDef = TypedDict(
    "_ClientDescribeTagsResponseTypeDef",
    {"tags": List[ClientDescribeTagsResponsetagsTypeDef], "nextToken": str},
    total=False,
)


class ClientDescribeTagsResponseTypeDef(_ClientDescribeTagsResponseTypeDef):
    """
    Type definition for `ClientDescribeTags` `Response`

    - **tags** *(list) --*

      Depending on the input, this is a list of configuration items tagged with a specific tag, or
      a list of tags for a specific configuration item.

      - *(dict) --*

        Tags for a configuration item. Tags are metadata that help you categorize IT assets.

        - **configurationType** *(string) --*

          A type of IT asset to tag.

        - **configurationId** *(string) --*

          The configuration ID for the item to tag. You can specify a list of keys and values.

        - **key** *(string) --*

          A type of tag on which to filter. For example, *serverType* .

        - **value** *(string) --*

          A value on which to filter. For example *key = serverType* and *value = web server* .

        - **timeOfCreation** *(datetime) --*

          The time the configuration tag was created in Coordinated Universal Time (UTC).

    - **nextToken** *(string) --*

      The call returns a token. Use this token to get the next set of results.
    """


_ClientDescribeTagsfiltersTypeDef = TypedDict(
    "_ClientDescribeTagsfiltersTypeDef", {"name": str, "values": List[str]}
)


class ClientDescribeTagsfiltersTypeDef(_ClientDescribeTagsfiltersTypeDef):
    """
    Type definition for `ClientDescribeTags` `filters`

    The tag filter. Valid names are: ``tagKey`` , ``tagValue`` , ``configurationId`` .

    - **name** *(string) --* **[REQUIRED]**

      A name of the tag filter.

    - **values** *(list) --* **[REQUIRED]**

      Values for the tag filter.

      - *(string) --*
    """


_ClientExportConfigurationsResponseTypeDef = TypedDict(
    "_ClientExportConfigurationsResponseTypeDef", {"exportId": str}, total=False
)


class ClientExportConfigurationsResponseTypeDef(
    _ClientExportConfigurationsResponseTypeDef
):
    """
    Type definition for `ClientExportConfigurations` `Response`

    - **exportId** *(string) --*

      A unique identifier that you can use to query the export status.
    """


_ClientGetDiscoverySummaryResponseagentSummaryTypeDef = TypedDict(
    "_ClientGetDiscoverySummaryResponseagentSummaryTypeDef",
    {
        "activeAgents": int,
        "healthyAgents": int,
        "blackListedAgents": int,
        "shutdownAgents": int,
        "unhealthyAgents": int,
        "totalAgents": int,
        "unknownAgents": int,
    },
    total=False,
)


class ClientGetDiscoverySummaryResponseagentSummaryTypeDef(
    _ClientGetDiscoverySummaryResponseagentSummaryTypeDef
):
    """
    Type definition for `ClientGetDiscoverySummaryResponse` `agentSummary`

    Details about discovered agents, including agent status and health.

    - **activeAgents** *(integer) --*

      Number of active discovery agents.

    - **healthyAgents** *(integer) --*

      Number of healthy discovery agents

    - **blackListedAgents** *(integer) --*

      Number of blacklisted discovery agents.

    - **shutdownAgents** *(integer) --*

      Number of discovery agents with status SHUTDOWN.

    - **unhealthyAgents** *(integer) --*

      Number of unhealthy discovery agents.

    - **totalAgents** *(integer) --*

      Total number of discovery agents.

    - **unknownAgents** *(integer) --*

      Number of unknown discovery agents.
    """


_ClientGetDiscoverySummaryResponseconnectorSummaryTypeDef = TypedDict(
    "_ClientGetDiscoverySummaryResponseconnectorSummaryTypeDef",
    {
        "activeConnectors": int,
        "healthyConnectors": int,
        "blackListedConnectors": int,
        "shutdownConnectors": int,
        "unhealthyConnectors": int,
        "totalConnectors": int,
        "unknownConnectors": int,
    },
    total=False,
)


class ClientGetDiscoverySummaryResponseconnectorSummaryTypeDef(
    _ClientGetDiscoverySummaryResponseconnectorSummaryTypeDef
):
    """
    Type definition for `ClientGetDiscoverySummaryResponse` `connectorSummary`

    Details about discovered connectors, including connector status and health.

    - **activeConnectors** *(integer) --*

      Number of active discovery connectors.

    - **healthyConnectors** *(integer) --*

      Number of healthy discovery connectors.

    - **blackListedConnectors** *(integer) --*

      Number of blacklisted discovery connectors.

    - **shutdownConnectors** *(integer) --*

      Number of discovery connectors with status SHUTDOWN,

    - **unhealthyConnectors** *(integer) --*

      Number of unhealthy discovery connectors.

    - **totalConnectors** *(integer) --*

      Total number of discovery connectors.

    - **unknownConnectors** *(integer) --*

      Number of unknown discovery connectors.
    """


_ClientGetDiscoverySummaryResponseTypeDef = TypedDict(
    "_ClientGetDiscoverySummaryResponseTypeDef",
    {
        "servers": int,
        "applications": int,
        "serversMappedToApplications": int,
        "serversMappedtoTags": int,
        "agentSummary": ClientGetDiscoverySummaryResponseagentSummaryTypeDef,
        "connectorSummary": ClientGetDiscoverySummaryResponseconnectorSummaryTypeDef,
    },
    total=False,
)


class ClientGetDiscoverySummaryResponseTypeDef(
    _ClientGetDiscoverySummaryResponseTypeDef
):
    """
    Type definition for `ClientGetDiscoverySummary` `Response`

    - **servers** *(integer) --*

      The number of servers discovered.

    - **applications** *(integer) --*

      The number of applications discovered.

    - **serversMappedToApplications** *(integer) --*

      The number of servers mapped to applications.

    - **serversMappedtoTags** *(integer) --*

      The number of servers mapped to tags.

    - **agentSummary** *(dict) --*

      Details about discovered agents, including agent status and health.

      - **activeAgents** *(integer) --*

        Number of active discovery agents.

      - **healthyAgents** *(integer) --*

        Number of healthy discovery agents

      - **blackListedAgents** *(integer) --*

        Number of blacklisted discovery agents.

      - **shutdownAgents** *(integer) --*

        Number of discovery agents with status SHUTDOWN.

      - **unhealthyAgents** *(integer) --*

        Number of unhealthy discovery agents.

      - **totalAgents** *(integer) --*

        Total number of discovery agents.

      - **unknownAgents** *(integer) --*

        Number of unknown discovery agents.

    - **connectorSummary** *(dict) --*

      Details about discovered connectors, including connector status and health.

      - **activeConnectors** *(integer) --*

        Number of active discovery connectors.

      - **healthyConnectors** *(integer) --*

        Number of healthy discovery connectors.

      - **blackListedConnectors** *(integer) --*

        Number of blacklisted discovery connectors.

      - **shutdownConnectors** *(integer) --*

        Number of discovery connectors with status SHUTDOWN,

      - **unhealthyConnectors** *(integer) --*

        Number of unhealthy discovery connectors.

      - **totalConnectors** *(integer) --*

        Total number of discovery connectors.

      - **unknownConnectors** *(integer) --*

        Number of unknown discovery connectors.
    """


_ClientListConfigurationsResponseTypeDef = TypedDict(
    "_ClientListConfigurationsResponseTypeDef",
    {"configurations": List[Dict[str, str]], "nextToken": str},
    total=False,
)


class ClientListConfigurationsResponseTypeDef(_ClientListConfigurationsResponseTypeDef):
    """
    Type definition for `ClientListConfigurations` `Response`

    - **configurations** *(list) --*

      Returns configuration details, including the configuration ID, attribute names, and attribute
      values.

      - *(dict) --*

        - *(string) --*

          - *(string) --*

    - **nextToken** *(string) --*

      Token to retrieve the next set of results. For example, if your call to ListConfigurations
      returned 100 items, but you set ``ListConfigurationsRequest$maxResults`` to 10, you received
      a set of 10 results along with this token. Use this token in the next query to retrieve the
      next set of 10.
    """


_ClientListConfigurationsfiltersTypeDef = TypedDict(
    "_ClientListConfigurationsfiltersTypeDef",
    {"name": str, "values": List[str], "condition": str},
)


class ClientListConfigurationsfiltersTypeDef(_ClientListConfigurationsfiltersTypeDef):
    """
    Type definition for `ClientListConfigurations` `filters`

    A filter that can use conditional operators.

    For more information about filters, see `Querying Discovered Configuration Items
    <http://docs.aws.amazon.com/application-discovery/latest/APIReference/discovery-api-queries.html>`__
    .

    - **name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **values** *(list) --* **[REQUIRED]**

      A string value on which to filter. For example, if you choose the
      ``destinationServer.osVersion`` filter name, you could specify ``Ubuntu`` for the value.

      - *(string) --*

    - **condition** *(string) --* **[REQUIRED]**

      A conditional operator. The following operators are valid: EQUALS, NOT_EQUALS, CONTAINS,
      NOT_CONTAINS. If you specify multiple filters, the system utilizes all filters as though
      concatenated by *AND* . If you specify multiple values for a particular filter, the system
      differentiates the values using *OR* . Calling either *DescribeConfigurations* or
      *ListConfigurations* returns attributes of matching configuration items.
    """


_RequiredClientListConfigurationsorderByTypeDef = TypedDict(
    "_RequiredClientListConfigurationsorderByTypeDef", {"fieldName": str}
)
_OptionalClientListConfigurationsorderByTypeDef = TypedDict(
    "_OptionalClientListConfigurationsorderByTypeDef", {"sortOrder": str}, total=False
)


class ClientListConfigurationsorderByTypeDef(
    _RequiredClientListConfigurationsorderByTypeDef,
    _OptionalClientListConfigurationsorderByTypeDef,
):
    """
    Type definition for `ClientListConfigurations` `orderBy`

    A field and direction for ordered output.

    - **fieldName** *(string) --* **[REQUIRED]**

      The field on which to order.

    - **sortOrder** *(string) --*

      Ordering direction.
    """


_ClientListServerNeighborsResponseneighborsTypeDef = TypedDict(
    "_ClientListServerNeighborsResponseneighborsTypeDef",
    {
        "sourceServerId": str,
        "destinationServerId": str,
        "destinationPort": int,
        "transportProtocol": str,
        "connectionsCount": int,
    },
    total=False,
)


class ClientListServerNeighborsResponseneighborsTypeDef(
    _ClientListServerNeighborsResponseneighborsTypeDef
):
    """
    Type definition for `ClientListServerNeighborsResponse` `neighbors`

    Details about neighboring servers.

    - **sourceServerId** *(string) --*

      The ID of the server that opened the network connection.

    - **destinationServerId** *(string) --*

      The ID of the server that accepted the network connection.

    - **destinationPort** *(integer) --*

      The destination network port for the connection.

    - **transportProtocol** *(string) --*

      The network protocol used for the connection.

    - **connectionsCount** *(integer) --*

      The number of open network connections with the neighboring server.
    """


_ClientListServerNeighborsResponseTypeDef = TypedDict(
    "_ClientListServerNeighborsResponseTypeDef",
    {
        "neighbors": List[ClientListServerNeighborsResponseneighborsTypeDef],
        "nextToken": str,
        "knownDependencyCount": int,
    },
    total=False,
)


class ClientListServerNeighborsResponseTypeDef(
    _ClientListServerNeighborsResponseTypeDef
):
    """
    Type definition for `ClientListServerNeighbors` `Response`

    - **neighbors** *(list) --*

      List of distinct servers that are one hop away from the given server.

      - *(dict) --*

        Details about neighboring servers.

        - **sourceServerId** *(string) --*

          The ID of the server that opened the network connection.

        - **destinationServerId** *(string) --*

          The ID of the server that accepted the network connection.

        - **destinationPort** *(integer) --*

          The destination network port for the connection.

        - **transportProtocol** *(string) --*

          The network protocol used for the connection.

        - **connectionsCount** *(integer) --*

          The number of open network connections with the neighboring server.

    - **nextToken** *(string) --*

      Token to retrieve the next set of results. For example, if you specified 100 IDs for
      ``ListServerNeighborsRequest$neighborConfigurationIds`` but set
      ``ListServerNeighborsRequest$maxResults`` to 10, you received a set of 10 results along with
      this token. Use this token in the next query to retrieve the next set of 10.

    - **knownDependencyCount** *(integer) --*

      Count of distinct servers that are one hop away from the given server.
    """


_ClientStartContinuousExportResponseTypeDef = TypedDict(
    "_ClientStartContinuousExportResponseTypeDef",
    {
        "exportId": str,
        "s3Bucket": str,
        "startTime": datetime,
        "dataSource": str,
        "schemaStorageConfig": Dict[str, str],
    },
    total=False,
)


class ClientStartContinuousExportResponseTypeDef(
    _ClientStartContinuousExportResponseTypeDef
):
    """
    Type definition for `ClientStartContinuousExport` `Response`

    - **exportId** *(string) --*

      The unique ID assigned to this export.

    - **s3Bucket** *(string) --*

      The name of the s3 bucket where the export data parquet files are stored.

    - **startTime** *(datetime) --*

      The timestamp representing when the continuous export was started.

    - **dataSource** *(string) --*

      The type of data collector used to gather this data (currently only offered for AGENT).

    - **schemaStorageConfig** *(dict) --*

      A dictionary which describes how the data is stored.

      * ``databaseName`` - the name of the Glue database used to store the schema.

      - *(string) --*

        - *(string) --*
    """


_ClientStartDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef = TypedDict(
    "_ClientStartDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef",
    {"agentId": str, "operationSucceeded": bool, "description": str},
    total=False,
)


class ClientStartDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef(
    _ClientStartDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef
):
    """
    Type definition for `ClientStartDataCollectionByAgentIdsResponse` `agentsConfigurationStatus`

    Information about agents or connectors that were instructed to start collecting data.
    Information includes the agent/connector ID, a description of the operation, and whether
    the agent/connector configuration was updated.

    - **agentId** *(string) --*

      The agent/connector ID.

    - **operationSucceeded** *(boolean) --*

      Information about the status of the ``StartDataCollection`` and ``StopDataCollection``
      operations. The system has recorded the data collection operation. The agent/connector
      receives this command the next time it polls for a new command.

    - **description** *(string) --*

      A description of the operation performed.
    """


_ClientStartDataCollectionByAgentIdsResponseTypeDef = TypedDict(
    "_ClientStartDataCollectionByAgentIdsResponseTypeDef",
    {
        "agentsConfigurationStatus": List[
            ClientStartDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef
        ]
    },
    total=False,
)


class ClientStartDataCollectionByAgentIdsResponseTypeDef(
    _ClientStartDataCollectionByAgentIdsResponseTypeDef
):
    """
    Type definition for `ClientStartDataCollectionByAgentIds` `Response`

    - **agentsConfigurationStatus** *(list) --*

      Information about agents or the connector that were instructed to start collecting data.
      Information includes the agent/connector ID, a description of the operation performed, and
      whether the agent/connector configuration was updated.

      - *(dict) --*

        Information about agents or connectors that were instructed to start collecting data.
        Information includes the agent/connector ID, a description of the operation, and whether
        the agent/connector configuration was updated.

        - **agentId** *(string) --*

          The agent/connector ID.

        - **operationSucceeded** *(boolean) --*

          Information about the status of the ``StartDataCollection`` and ``StopDataCollection``
          operations. The system has recorded the data collection operation. The agent/connector
          receives this command the next time it polls for a new command.

        - **description** *(string) --*

          A description of the operation performed.
    """


_ClientStartExportTaskResponseTypeDef = TypedDict(
    "_ClientStartExportTaskResponseTypeDef", {"exportId": str}, total=False
)


class ClientStartExportTaskResponseTypeDef(_ClientStartExportTaskResponseTypeDef):
    """
    Type definition for `ClientStartExportTask` `Response`

    - **exportId** *(string) --*

      A unique identifier used to query the status of an export request.
    """


_ClientStartExportTaskfiltersTypeDef = TypedDict(
    "_ClientStartExportTaskfiltersTypeDef",
    {"name": str, "values": List[str], "condition": str},
)


class ClientStartExportTaskfiltersTypeDef(_ClientStartExportTaskfiltersTypeDef):
    """
    Type definition for `ClientStartExportTask` `filters`

    Used to select which agent's data is to be exported. A single agent ID may be selected for
    export using the `StartExportTask
    <http://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StartExportTask.html>`__
    action.

    - **name** *(string) --* **[REQUIRED]**

      A single ``ExportFilter`` name. Supported filters: ``agentId`` .

    - **values** *(list) --* **[REQUIRED]**

      A single ``agentId`` for a Discovery Agent. An ``agentId`` can be found using the
      `DescribeAgents
      <http://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeExportTasks.html>`__
      action. Typically an ADS ``agentId`` is in the form ``o-0123456789abcdef0`` .

      - *(string) --*

    - **condition** *(string) --* **[REQUIRED]**

      Supported condition: ``EQUALS``
    """


_ClientStartImportTaskResponsetaskTypeDef = TypedDict(
    "_ClientStartImportTaskResponsetaskTypeDef",
    {
        "importTaskId": str,
        "clientRequestToken": str,
        "name": str,
        "importUrl": str,
        "status": str,
        "importRequestTime": datetime,
        "importCompletionTime": datetime,
        "importDeletedTime": datetime,
        "serverImportSuccess": int,
        "serverImportFailure": int,
        "applicationImportSuccess": int,
        "applicationImportFailure": int,
        "errorsAndFailedEntriesZip": str,
    },
    total=False,
)


class ClientStartImportTaskResponsetaskTypeDef(
    _ClientStartImportTaskResponsetaskTypeDef
):
    """
    Type definition for `ClientStartImportTaskResponse` `task`

    An array of information related to the import task request including status information,
    times, IDs, the Amazon S3 Object URL for the import file, and more.

    - **importTaskId** *(string) --*

      The unique ID for a specific import task. These IDs aren't globally unique, but they are
      unique within an AWS account.

    - **clientRequestToken** *(string) --*

      A unique token used to prevent the same import request from occurring more than once. If
      you didn't provide a token, a token was automatically generated when the import task
      request was sent.

    - **name** *(string) --*

      A descriptive name for an import task. You can use this name to filter future requests
      related to this import task, such as identifying applications and servers that were
      included in this import task. We recommend that you use a meaningful name for each import
      task.

    - **importUrl** *(string) --*

      The URL for your import file that you've uploaded to Amazon S3.

    - **status** *(string) --*

      The status of the import task. An import can have the status of ``IMPORT_COMPLETE`` and
      still have some records fail to import from the overall request. More information can be
      found in the downloadable archive defined in the ``errorsAndFailedEntriesZip`` field, or in
      the Migration Hub management console.

    - **importRequestTime** *(datetime) --*

      The time that the import task request was made, presented in the Unix time stamp format.

    - **importCompletionTime** *(datetime) --*

      The time that the import task request finished, presented in the Unix time stamp format.

    - **importDeletedTime** *(datetime) --*

      The time that the import task request was deleted, presented in the Unix time stamp format.

    - **serverImportSuccess** *(integer) --*

      The total number of server records in the import file that were successfully imported.

    - **serverImportFailure** *(integer) --*

      The total number of server records in the import file that failed to be imported.

    - **applicationImportSuccess** *(integer) --*

      The total number of application records in the import file that were successfully imported.

    - **applicationImportFailure** *(integer) --*

      The total number of application records in the import file that failed to be imported.

    - **errorsAndFailedEntriesZip** *(string) --*

      A link to a compressed archive folder (in the ZIP format) that contains an error log and a
      file of failed records. You can use these two files to quickly identify records that
      failed, why they failed, and correct those records. Afterward, you can upload the corrected
      file to your Amazon S3 bucket and create another import task request.

      This field also includes authorization information so you can confirm the authenticity of
      the compressed archive before you download it.

      If some records failed to be imported we recommend that you correct the records in the
      failed entries file and then imports that failed entries file. This prevents you from
      having to correct and update the larger original file and attempt importing it again.
    """


_ClientStartImportTaskResponseTypeDef = TypedDict(
    "_ClientStartImportTaskResponseTypeDef",
    {"task": ClientStartImportTaskResponsetaskTypeDef},
    total=False,
)


class ClientStartImportTaskResponseTypeDef(_ClientStartImportTaskResponseTypeDef):
    """
    Type definition for `ClientStartImportTask` `Response`

    - **task** *(dict) --*

      An array of information related to the import task request including status information,
      times, IDs, the Amazon S3 Object URL for the import file, and more.

      - **importTaskId** *(string) --*

        The unique ID for a specific import task. These IDs aren't globally unique, but they are
        unique within an AWS account.

      - **clientRequestToken** *(string) --*

        A unique token used to prevent the same import request from occurring more than once. If
        you didn't provide a token, a token was automatically generated when the import task
        request was sent.

      - **name** *(string) --*

        A descriptive name for an import task. You can use this name to filter future requests
        related to this import task, such as identifying applications and servers that were
        included in this import task. We recommend that you use a meaningful name for each import
        task.

      - **importUrl** *(string) --*

        The URL for your import file that you've uploaded to Amazon S3.

      - **status** *(string) --*

        The status of the import task. An import can have the status of ``IMPORT_COMPLETE`` and
        still have some records fail to import from the overall request. More information can be
        found in the downloadable archive defined in the ``errorsAndFailedEntriesZip`` field, or in
        the Migration Hub management console.

      - **importRequestTime** *(datetime) --*

        The time that the import task request was made, presented in the Unix time stamp format.

      - **importCompletionTime** *(datetime) --*

        The time that the import task request finished, presented in the Unix time stamp format.

      - **importDeletedTime** *(datetime) --*

        The time that the import task request was deleted, presented in the Unix time stamp format.

      - **serverImportSuccess** *(integer) --*

        The total number of server records in the import file that were successfully imported.

      - **serverImportFailure** *(integer) --*

        The total number of server records in the import file that failed to be imported.

      - **applicationImportSuccess** *(integer) --*

        The total number of application records in the import file that were successfully imported.

      - **applicationImportFailure** *(integer) --*

        The total number of application records in the import file that failed to be imported.

      - **errorsAndFailedEntriesZip** *(string) --*

        A link to a compressed archive folder (in the ZIP format) that contains an error log and a
        file of failed records. You can use these two files to quickly identify records that
        failed, why they failed, and correct those records. Afterward, you can upload the corrected
        file to your Amazon S3 bucket and create another import task request.

        This field also includes authorization information so you can confirm the authenticity of
        the compressed archive before you download it.

        If some records failed to be imported we recommend that you correct the records in the
        failed entries file and then imports that failed entries file. This prevents you from
        having to correct and update the larger original file and attempt importing it again.
    """


_ClientStopContinuousExportResponseTypeDef = TypedDict(
    "_ClientStopContinuousExportResponseTypeDef",
    {"startTime": datetime, "stopTime": datetime},
    total=False,
)


class ClientStopContinuousExportResponseTypeDef(
    _ClientStopContinuousExportResponseTypeDef
):
    """
    Type definition for `ClientStopContinuousExport` `Response`

    - **startTime** *(datetime) --*

      Timestamp that represents when this continuous export started collecting data.

    - **stopTime** *(datetime) --*

      Timestamp that represents when this continuous export was stopped.
    """


_ClientStopDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef = TypedDict(
    "_ClientStopDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef",
    {"agentId": str, "operationSucceeded": bool, "description": str},
    total=False,
)


class ClientStopDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef(
    _ClientStopDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef
):
    """
    Type definition for `ClientStopDataCollectionByAgentIdsResponse` `agentsConfigurationStatus`

    Information about agents or connectors that were instructed to start collecting data.
    Information includes the agent/connector ID, a description of the operation, and whether
    the agent/connector configuration was updated.

    - **agentId** *(string) --*

      The agent/connector ID.

    - **operationSucceeded** *(boolean) --*

      Information about the status of the ``StartDataCollection`` and ``StopDataCollection``
      operations. The system has recorded the data collection operation. The agent/connector
      receives this command the next time it polls for a new command.

    - **description** *(string) --*

      A description of the operation performed.
    """


_ClientStopDataCollectionByAgentIdsResponseTypeDef = TypedDict(
    "_ClientStopDataCollectionByAgentIdsResponseTypeDef",
    {
        "agentsConfigurationStatus": List[
            ClientStopDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef
        ]
    },
    total=False,
)


class ClientStopDataCollectionByAgentIdsResponseTypeDef(
    _ClientStopDataCollectionByAgentIdsResponseTypeDef
):
    """
    Type definition for `ClientStopDataCollectionByAgentIds` `Response`

    - **agentsConfigurationStatus** *(list) --*

      Information about the agents or connector that were instructed to stop collecting data.
      Information includes the agent/connector ID, a description of the operation performed, and
      whether the agent/connector configuration was updated.

      - *(dict) --*

        Information about agents or connectors that were instructed to start collecting data.
        Information includes the agent/connector ID, a description of the operation, and whether
        the agent/connector configuration was updated.

        - **agentId** *(string) --*

          The agent/connector ID.

        - **operationSucceeded** *(boolean) --*

          Information about the status of the ``StartDataCollection`` and ``StopDataCollection``
          operations. The system has recorded the data collection operation. The agent/connector
          receives this command the next time it polls for a new command.

        - **description** *(string) --*

          A description of the operation performed.
    """


_DescribeAgentsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeAgentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeAgentsPaginatePaginationConfigTypeDef(
    _DescribeAgentsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeAgentsPaginate` `PaginationConfig`

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


_DescribeAgentsPaginateResponseagentsInfoagentNetworkInfoListTypeDef = TypedDict(
    "_DescribeAgentsPaginateResponseagentsInfoagentNetworkInfoListTypeDef",
    {"ipAddress": str, "macAddress": str},
    total=False,
)


class DescribeAgentsPaginateResponseagentsInfoagentNetworkInfoListTypeDef(
    _DescribeAgentsPaginateResponseagentsInfoagentNetworkInfoListTypeDef
):
    """
    Type definition for `DescribeAgentsPaginateResponseagentsInfo` `agentNetworkInfoList`

    Network details about the host where the agent/connector resides.

    - **ipAddress** *(string) --*

      The IP address for the host where the agent/connector resides.

    - **macAddress** *(string) --*

      The MAC address for the host where the agent/connector resides.
    """


_DescribeAgentsPaginateResponseagentsInfoTypeDef = TypedDict(
    "_DescribeAgentsPaginateResponseagentsInfoTypeDef",
    {
        "agentId": str,
        "hostName": str,
        "agentNetworkInfoList": List[
            DescribeAgentsPaginateResponseagentsInfoagentNetworkInfoListTypeDef
        ],
        "connectorId": str,
        "version": str,
        "health": str,
        "lastHealthPingTime": str,
        "collectionStatus": str,
        "agentType": str,
        "registeredTime": str,
    },
    total=False,
)


class DescribeAgentsPaginateResponseagentsInfoTypeDef(
    _DescribeAgentsPaginateResponseagentsInfoTypeDef
):
    """
    Type definition for `DescribeAgentsPaginateResponse` `agentsInfo`

    Information about agents or connectors associated with the user’s AWS account. Information
    includes agent or connector IDs, IP addresses, media access control (MAC) addresses, agent
    or connector health, hostname where the agent or connector resides, and agent version for
    each agent.

    - **agentId** *(string) --*

      The agent or connector ID.

    - **hostName** *(string) --*

      The name of the host where the agent or connector resides. The host can be a server or
      virtual machine.

    - **agentNetworkInfoList** *(list) --*

      Network details about the host where the agent or connector resides.

      - *(dict) --*

        Network details about the host where the agent/connector resides.

        - **ipAddress** *(string) --*

          The IP address for the host where the agent/connector resides.

        - **macAddress** *(string) --*

          The MAC address for the host where the agent/connector resides.

    - **connectorId** *(string) --*

      The ID of the connector.

    - **version** *(string) --*

      The agent or connector version.

    - **health** *(string) --*

      The health of the agent or connector.

    - **lastHealthPingTime** *(string) --*

      Time since agent or connector health was reported.

    - **collectionStatus** *(string) --*

      Status of the collection process for an agent or connector.

    - **agentType** *(string) --*

      Type of agent.

    - **registeredTime** *(string) --*

      Agent's first registration timestamp in UTC.
    """


_DescribeAgentsPaginateResponseTypeDef = TypedDict(
    "_DescribeAgentsPaginateResponseTypeDef",
    {
        "agentsInfo": List[DescribeAgentsPaginateResponseagentsInfoTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeAgentsPaginateResponseTypeDef(_DescribeAgentsPaginateResponseTypeDef):
    """
    Type definition for `DescribeAgentsPaginate` `Response`

    - **agentsInfo** *(list) --*

      Lists agents or the Connector by ID or lists all agents/Connectors associated with your user
      account if you did not specify an agent/Connector ID. The output includes agent/Connector
      IDs, IP addresses, media access control (MAC) addresses, agent/Connector health, host name
      where the agent/Connector resides, and the version number of each agent/Connector.

      - *(dict) --*

        Information about agents or connectors associated with the user’s AWS account. Information
        includes agent or connector IDs, IP addresses, media access control (MAC) addresses, agent
        or connector health, hostname where the agent or connector resides, and agent version for
        each agent.

        - **agentId** *(string) --*

          The agent or connector ID.

        - **hostName** *(string) --*

          The name of the host where the agent or connector resides. The host can be a server or
          virtual machine.

        - **agentNetworkInfoList** *(list) --*

          Network details about the host where the agent or connector resides.

          - *(dict) --*

            Network details about the host where the agent/connector resides.

            - **ipAddress** *(string) --*

              The IP address for the host where the agent/connector resides.

            - **macAddress** *(string) --*

              The MAC address for the host where the agent/connector resides.

        - **connectorId** *(string) --*

          The ID of the connector.

        - **version** *(string) --*

          The agent or connector version.

        - **health** *(string) --*

          The health of the agent or connector.

        - **lastHealthPingTime** *(string) --*

          Time since agent or connector health was reported.

        - **collectionStatus** *(string) --*

          Status of the collection process for an agent or connector.

        - **agentType** *(string) --*

          Type of agent.

        - **registeredTime** *(string) --*

          Agent's first registration timestamp in UTC.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeAgentsPaginatefiltersTypeDef = TypedDict(
    "_DescribeAgentsPaginatefiltersTypeDef",
    {"name": str, "values": List[str], "condition": str},
)


class DescribeAgentsPaginatefiltersTypeDef(_DescribeAgentsPaginatefiltersTypeDef):
    """
    Type definition for `DescribeAgentsPaginate` `filters`

    A filter that can use conditional operators.

    For more information about filters, see `Querying Discovered Configuration Items
    <http://docs.aws.amazon.com/application-discovery/latest/APIReference/discovery-api-queries.html>`__
    .

    - **name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **values** *(list) --* **[REQUIRED]**

      A string value on which to filter. For example, if you choose the
      ``destinationServer.osVersion`` filter name, you could specify ``Ubuntu`` for the value.

      - *(string) --*

    - **condition** *(string) --* **[REQUIRED]**

      A conditional operator. The following operators are valid: EQUALS, NOT_EQUALS, CONTAINS,
      NOT_CONTAINS. If you specify multiple filters, the system utilizes all filters as though
      concatenated by *AND* . If you specify multiple values for a particular filter, the system
      differentiates the values using *OR* . Calling either *DescribeConfigurations* or
      *ListConfigurations* returns attributes of matching configuration items.
    """


_DescribeContinuousExportsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeContinuousExportsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeContinuousExportsPaginatePaginationConfigTypeDef(
    _DescribeContinuousExportsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeContinuousExportsPaginate` `PaginationConfig`

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


_DescribeContinuousExportsPaginateResponsedescriptionsTypeDef = TypedDict(
    "_DescribeContinuousExportsPaginateResponsedescriptionsTypeDef",
    {
        "exportId": str,
        "status": str,
        "statusDetail": str,
        "s3Bucket": str,
        "startTime": datetime,
        "stopTime": datetime,
        "dataSource": str,
        "schemaStorageConfig": Dict[str, str],
    },
    total=False,
)


class DescribeContinuousExportsPaginateResponsedescriptionsTypeDef(
    _DescribeContinuousExportsPaginateResponsedescriptionsTypeDef
):
    """
    Type definition for `DescribeContinuousExportsPaginateResponse` `descriptions`

    A list of continuous export descriptions.

    - **exportId** *(string) --*

      The unique ID assigned to this export.

    - **status** *(string) --*

      Describes the status of the export. Can be one of the following values:

      * START_IN_PROGRESS - setting up resources to start continuous export.

      * START_FAILED - an error occurred setting up continuous export. To recover, call
      start-continuous-export again.

      * ACTIVE - data is being exported to the customer bucket.

      * ERROR - an error occurred during export. To fix the issue, call stop-continuous-export
      and start-continuous-export.

      * STOP_IN_PROGRESS - stopping the export.

      * STOP_FAILED - an error occurred stopping the export. To recover, call
      stop-continuous-export again.

      * INACTIVE - the continuous export has been stopped. Data is no longer being exported to
      the customer bucket.

    - **statusDetail** *(string) --*

      Contains information about any errors that have occurred. This data type can have the
      following values:

      * ACCESS_DENIED - You don’t have permission to start Data Exploration in Amazon Athena.
      Contact your AWS administrator for help. For more information, see `Setting Up AWS
      Application Discovery Service
      <http://docs.aws.amazon.com/application-discovery/latest/userguide/setting-up.html>`__ in
      the Application Discovery Service User Guide.

      * DELIVERY_STREAM_LIMIT_FAILURE - You reached the limit for Amazon Kinesis Data Firehose
      delivery streams. Reduce the number of streams or request a limit increase and try again.
      For more information, see `Kinesis Data Streams Limits
      <http://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html>`__ in the
      Amazon Kinesis Data Streams Developer Guide.

      * FIREHOSE_ROLE_MISSING - The Data Exploration feature is in an error state because your
      IAM User is missing the AWSApplicationDiscoveryServiceFirehose role. Turn on Data
      Exploration in Amazon Athena and try again. For more information, see `Step 3\\: Provide
      Application Discovery Service Access to Non-Administrator Users by Attaching Policies
      <http://docs.aws.amazon.com/application-discovery/latest/userguide/setting-up.html#setting-up-user-policy>`__
      in the Application Discovery Service User Guide.

      * FIREHOSE_STREAM_DOES_NOT_EXIST - The Data Exploration feature is in an error state
      because your IAM User is missing one or more of the Kinesis data delivery streams.

      * INTERNAL_FAILURE - The Data Exploration feature is in an error state because of an
      internal failure. Try again later. If this problem persists, contact AWS Support.

      * S3_BUCKET_LIMIT_FAILURE - You reached the limit for Amazon S3 buckets. Reduce the
      number of Amazon S3 buckets or request a limit increase and try again. For more
      information, see `Bucket Restrictions and Limitations
      <http://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html>`__ in the Amazon
      Simple Storage Service Developer Guide.

      * S3_NOT_SIGNED_UP - Your account is not signed up for the Amazon S3 service. You must
      sign up before you can use Amazon S3. You can sign up at the following URL:
      `https\\://aws.amazon.com/s3 <https://aws.amazon.com/s3>`__ .

    - **s3Bucket** *(string) --*

      The name of the s3 bucket where the export data parquet files are stored.

    - **startTime** *(datetime) --*

      The timestamp representing when the continuous export was started.

    - **stopTime** *(datetime) --*

      The timestamp that represents when this continuous export was stopped.

    - **dataSource** *(string) --*

      The type of data collector used to gather this data (currently only offered for AGENT).

    - **schemaStorageConfig** *(dict) --*

      An object which describes how the data is stored.

      * ``databaseName`` - the name of the Glue database used to store the schema.

      - *(string) --*

        - *(string) --*
    """


_DescribeContinuousExportsPaginateResponseTypeDef = TypedDict(
    "_DescribeContinuousExportsPaginateResponseTypeDef",
    {
        "descriptions": List[
            DescribeContinuousExportsPaginateResponsedescriptionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeContinuousExportsPaginateResponseTypeDef(
    _DescribeContinuousExportsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeContinuousExportsPaginate` `Response`

    - **descriptions** *(list) --*

      A list of continuous export descriptions.

      - *(dict) --*

        A list of continuous export descriptions.

        - **exportId** *(string) --*

          The unique ID assigned to this export.

        - **status** *(string) --*

          Describes the status of the export. Can be one of the following values:

          * START_IN_PROGRESS - setting up resources to start continuous export.

          * START_FAILED - an error occurred setting up continuous export. To recover, call
          start-continuous-export again.

          * ACTIVE - data is being exported to the customer bucket.

          * ERROR - an error occurred during export. To fix the issue, call stop-continuous-export
          and start-continuous-export.

          * STOP_IN_PROGRESS - stopping the export.

          * STOP_FAILED - an error occurred stopping the export. To recover, call
          stop-continuous-export again.

          * INACTIVE - the continuous export has been stopped. Data is no longer being exported to
          the customer bucket.

        - **statusDetail** *(string) --*

          Contains information about any errors that have occurred. This data type can have the
          following values:

          * ACCESS_DENIED - You don’t have permission to start Data Exploration in Amazon Athena.
          Contact your AWS administrator for help. For more information, see `Setting Up AWS
          Application Discovery Service
          <http://docs.aws.amazon.com/application-discovery/latest/userguide/setting-up.html>`__ in
          the Application Discovery Service User Guide.

          * DELIVERY_STREAM_LIMIT_FAILURE - You reached the limit for Amazon Kinesis Data Firehose
          delivery streams. Reduce the number of streams or request a limit increase and try again.
          For more information, see `Kinesis Data Streams Limits
          <http://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html>`__ in the
          Amazon Kinesis Data Streams Developer Guide.

          * FIREHOSE_ROLE_MISSING - The Data Exploration feature is in an error state because your
          IAM User is missing the AWSApplicationDiscoveryServiceFirehose role. Turn on Data
          Exploration in Amazon Athena and try again. For more information, see `Step 3\\: Provide
          Application Discovery Service Access to Non-Administrator Users by Attaching Policies
          <http://docs.aws.amazon.com/application-discovery/latest/userguide/setting-up.html#setting-up-user-policy>`__
          in the Application Discovery Service User Guide.

          * FIREHOSE_STREAM_DOES_NOT_EXIST - The Data Exploration feature is in an error state
          because your IAM User is missing one or more of the Kinesis data delivery streams.

          * INTERNAL_FAILURE - The Data Exploration feature is in an error state because of an
          internal failure. Try again later. If this problem persists, contact AWS Support.

          * S3_BUCKET_LIMIT_FAILURE - You reached the limit for Amazon S3 buckets. Reduce the
          number of Amazon S3 buckets or request a limit increase and try again. For more
          information, see `Bucket Restrictions and Limitations
          <http://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html>`__ in the Amazon
          Simple Storage Service Developer Guide.

          * S3_NOT_SIGNED_UP - Your account is not signed up for the Amazon S3 service. You must
          sign up before you can use Amazon S3. You can sign up at the following URL:
          `https\\://aws.amazon.com/s3 <https://aws.amazon.com/s3>`__ .

        - **s3Bucket** *(string) --*

          The name of the s3 bucket where the export data parquet files are stored.

        - **startTime** *(datetime) --*

          The timestamp representing when the continuous export was started.

        - **stopTime** *(datetime) --*

          The timestamp that represents when this continuous export was stopped.

        - **dataSource** *(string) --*

          The type of data collector used to gather this data (currently only offered for AGENT).

        - **schemaStorageConfig** *(dict) --*

          An object which describes how the data is stored.

          * ``databaseName`` - the name of the Glue database used to store the schema.

          - *(string) --*

            - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeExportConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeExportConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeExportConfigurationsPaginatePaginationConfigTypeDef(
    _DescribeExportConfigurationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeExportConfigurationsPaginate` `PaginationConfig`

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


_DescribeExportConfigurationsPaginateResponseexportsInfoTypeDef = TypedDict(
    "_DescribeExportConfigurationsPaginateResponseexportsInfoTypeDef",
    {
        "exportId": str,
        "exportStatus": str,
        "statusMessage": str,
        "configurationsDownloadUrl": str,
        "exportRequestTime": datetime,
        "isTruncated": bool,
        "requestedStartTime": datetime,
        "requestedEndTime": datetime,
    },
    total=False,
)


class DescribeExportConfigurationsPaginateResponseexportsInfoTypeDef(
    _DescribeExportConfigurationsPaginateResponseexportsInfoTypeDef
):
    """
    Type definition for `DescribeExportConfigurationsPaginateResponse` `exportsInfo`

    Information regarding the export status of discovered data. The value is an array of
    objects.

    - **exportId** *(string) --*

      A unique identifier used to query an export.

    - **exportStatus** *(string) --*

      The status of the data export job.

    - **statusMessage** *(string) --*

      A status message provided for API callers.

    - **configurationsDownloadUrl** *(string) --*

      A URL for an Amazon S3 bucket where you can review the exported data. The URL is
      displayed only if the export succeeded.

    - **exportRequestTime** *(datetime) --*

      The time that the data export was initiated.

    - **isTruncated** *(boolean) --*

      If true, the export of agent information exceeded the size limit for a single export and
      the exported data is incomplete for the requested time range. To address this, select a
      smaller time range for the export by using ``startDate`` and ``endDate`` .

    - **requestedStartTime** *(datetime) --*

      The value of ``startTime`` parameter in the ``StartExportTask`` request. If no
      ``startTime`` was requested, this result does not appear in ``ExportInfo`` .

    - **requestedEndTime** *(datetime) --*

      The ``endTime`` used in the ``StartExportTask`` request. If no ``endTime`` was requested,
      this result does not appear in ``ExportInfo`` .
    """


_DescribeExportConfigurationsPaginateResponseTypeDef = TypedDict(
    "_DescribeExportConfigurationsPaginateResponseTypeDef",
    {
        "exportsInfo": List[
            DescribeExportConfigurationsPaginateResponseexportsInfoTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeExportConfigurationsPaginateResponseTypeDef(
    _DescribeExportConfigurationsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeExportConfigurationsPaginate` `Response`

    - **exportsInfo** *(list) --*

      - *(dict) --*

        Information regarding the export status of discovered data. The value is an array of
        objects.

        - **exportId** *(string) --*

          A unique identifier used to query an export.

        - **exportStatus** *(string) --*

          The status of the data export job.

        - **statusMessage** *(string) --*

          A status message provided for API callers.

        - **configurationsDownloadUrl** *(string) --*

          A URL for an Amazon S3 bucket where you can review the exported data. The URL is
          displayed only if the export succeeded.

        - **exportRequestTime** *(datetime) --*

          The time that the data export was initiated.

        - **isTruncated** *(boolean) --*

          If true, the export of agent information exceeded the size limit for a single export and
          the exported data is incomplete for the requested time range. To address this, select a
          smaller time range for the export by using ``startDate`` and ``endDate`` .

        - **requestedStartTime** *(datetime) --*

          The value of ``startTime`` parameter in the ``StartExportTask`` request. If no
          ``startTime`` was requested, this result does not appear in ``ExportInfo`` .

        - **requestedEndTime** *(datetime) --*

          The ``endTime`` used in the ``StartExportTask`` request. If no ``endTime`` was requested,
          this result does not appear in ``ExportInfo`` .

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


_DescribeExportTasksPaginateResponseexportsInfoTypeDef = TypedDict(
    "_DescribeExportTasksPaginateResponseexportsInfoTypeDef",
    {
        "exportId": str,
        "exportStatus": str,
        "statusMessage": str,
        "configurationsDownloadUrl": str,
        "exportRequestTime": datetime,
        "isTruncated": bool,
        "requestedStartTime": datetime,
        "requestedEndTime": datetime,
    },
    total=False,
)


class DescribeExportTasksPaginateResponseexportsInfoTypeDef(
    _DescribeExportTasksPaginateResponseexportsInfoTypeDef
):
    """
    Type definition for `DescribeExportTasksPaginateResponse` `exportsInfo`

    Information regarding the export status of discovered data. The value is an array of
    objects.

    - **exportId** *(string) --*

      A unique identifier used to query an export.

    - **exportStatus** *(string) --*

      The status of the data export job.

    - **statusMessage** *(string) --*

      A status message provided for API callers.

    - **configurationsDownloadUrl** *(string) --*

      A URL for an Amazon S3 bucket where you can review the exported data. The URL is
      displayed only if the export succeeded.

    - **exportRequestTime** *(datetime) --*

      The time that the data export was initiated.

    - **isTruncated** *(boolean) --*

      If true, the export of agent information exceeded the size limit for a single export and
      the exported data is incomplete for the requested time range. To address this, select a
      smaller time range for the export by using ``startDate`` and ``endDate`` .

    - **requestedStartTime** *(datetime) --*

      The value of ``startTime`` parameter in the ``StartExportTask`` request. If no
      ``startTime`` was requested, this result does not appear in ``ExportInfo`` .

    - **requestedEndTime** *(datetime) --*

      The ``endTime`` used in the ``StartExportTask`` request. If no ``endTime`` was requested,
      this result does not appear in ``ExportInfo`` .
    """


_DescribeExportTasksPaginateResponseTypeDef = TypedDict(
    "_DescribeExportTasksPaginateResponseTypeDef",
    {
        "exportsInfo": List[DescribeExportTasksPaginateResponseexportsInfoTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeExportTasksPaginateResponseTypeDef(
    _DescribeExportTasksPaginateResponseTypeDef
):
    """
    Type definition for `DescribeExportTasksPaginate` `Response`

    - **exportsInfo** *(list) --*

      Contains one or more sets of export request details. When the status of a request is
      ``SUCCEEDED`` , the response includes a URL for an Amazon S3 bucket where you can view the
      data in a CSV file.

      - *(dict) --*

        Information regarding the export status of discovered data. The value is an array of
        objects.

        - **exportId** *(string) --*

          A unique identifier used to query an export.

        - **exportStatus** *(string) --*

          The status of the data export job.

        - **statusMessage** *(string) --*

          A status message provided for API callers.

        - **configurationsDownloadUrl** *(string) --*

          A URL for an Amazon S3 bucket where you can review the exported data. The URL is
          displayed only if the export succeeded.

        - **exportRequestTime** *(datetime) --*

          The time that the data export was initiated.

        - **isTruncated** *(boolean) --*

          If true, the export of agent information exceeded the size limit for a single export and
          the exported data is incomplete for the requested time range. To address this, select a
          smaller time range for the export by using ``startDate`` and ``endDate`` .

        - **requestedStartTime** *(datetime) --*

          The value of ``startTime`` parameter in the ``StartExportTask`` request. If no
          ``startTime`` was requested, this result does not appear in ``ExportInfo`` .

        - **requestedEndTime** *(datetime) --*

          The ``endTime`` used in the ``StartExportTask`` request. If no ``endTime`` was requested,
          this result does not appear in ``ExportInfo`` .

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeExportTasksPaginatefiltersTypeDef = TypedDict(
    "_DescribeExportTasksPaginatefiltersTypeDef",
    {"name": str, "values": List[str], "condition": str},
)


class DescribeExportTasksPaginatefiltersTypeDef(
    _DescribeExportTasksPaginatefiltersTypeDef
):
    """
    Type definition for `DescribeExportTasksPaginate` `filters`

    Used to select which agent's data is to be exported. A single agent ID may be selected for
    export using the `StartExportTask
    <http://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StartExportTask.html>`__
    action.

    - **name** *(string) --* **[REQUIRED]**

      A single ``ExportFilter`` name. Supported filters: ``agentId`` .

    - **values** *(list) --* **[REQUIRED]**

      A single ``agentId`` for a Discovery Agent. An ``agentId`` can be found using the
      `DescribeAgents
      <http://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeExportTasks.html>`__
      action. Typically an ADS ``agentId`` is in the form ``o-0123456789abcdef0`` .

      - *(string) --*

    - **condition** *(string) --* **[REQUIRED]**

      Supported condition: ``EQUALS``
    """


_DescribeTagsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeTagsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeTagsPaginatePaginationConfigTypeDef(
    _DescribeTagsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeTagsPaginate` `PaginationConfig`

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


_DescribeTagsPaginateResponsetagsTypeDef = TypedDict(
    "_DescribeTagsPaginateResponsetagsTypeDef",
    {
        "configurationType": str,
        "configurationId": str,
        "key": str,
        "value": str,
        "timeOfCreation": datetime,
    },
    total=False,
)


class DescribeTagsPaginateResponsetagsTypeDef(_DescribeTagsPaginateResponsetagsTypeDef):
    """
    Type definition for `DescribeTagsPaginateResponse` `tags`

    Tags for a configuration item. Tags are metadata that help you categorize IT assets.

    - **configurationType** *(string) --*

      A type of IT asset to tag.

    - **configurationId** *(string) --*

      The configuration ID for the item to tag. You can specify a list of keys and values.

    - **key** *(string) --*

      A type of tag on which to filter. For example, *serverType* .

    - **value** *(string) --*

      A value on which to filter. For example *key = serverType* and *value = web server* .

    - **timeOfCreation** *(datetime) --*

      The time the configuration tag was created in Coordinated Universal Time (UTC).
    """


_DescribeTagsPaginateResponseTypeDef = TypedDict(
    "_DescribeTagsPaginateResponseTypeDef",
    {"tags": List[DescribeTagsPaginateResponsetagsTypeDef], "NextToken": str},
    total=False,
)


class DescribeTagsPaginateResponseTypeDef(_DescribeTagsPaginateResponseTypeDef):
    """
    Type definition for `DescribeTagsPaginate` `Response`

    - **tags** *(list) --*

      Depending on the input, this is a list of configuration items tagged with a specific tag, or
      a list of tags for a specific configuration item.

      - *(dict) --*

        Tags for a configuration item. Tags are metadata that help you categorize IT assets.

        - **configurationType** *(string) --*

          A type of IT asset to tag.

        - **configurationId** *(string) --*

          The configuration ID for the item to tag. You can specify a list of keys and values.

        - **key** *(string) --*

          A type of tag on which to filter. For example, *serverType* .

        - **value** *(string) --*

          A value on which to filter. For example *key = serverType* and *value = web server* .

        - **timeOfCreation** *(datetime) --*

          The time the configuration tag was created in Coordinated Universal Time (UTC).

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeTagsPaginatefiltersTypeDef = TypedDict(
    "_DescribeTagsPaginatefiltersTypeDef", {"name": str, "values": List[str]}
)


class DescribeTagsPaginatefiltersTypeDef(_DescribeTagsPaginatefiltersTypeDef):
    """
    Type definition for `DescribeTagsPaginate` `filters`

    The tag filter. Valid names are: ``tagKey`` , ``tagValue`` , ``configurationId`` .

    - **name** *(string) --* **[REQUIRED]**

      A name of the tag filter.

    - **values** *(list) --* **[REQUIRED]**

      Values for the tag filter.

      - *(string) --*
    """


_ListConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListConfigurationsPaginatePaginationConfigTypeDef(
    _ListConfigurationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListConfigurationsPaginate` `PaginationConfig`

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


_ListConfigurationsPaginateResponseTypeDef = TypedDict(
    "_ListConfigurationsPaginateResponseTypeDef",
    {"configurations": List[Dict[str, str]], "NextToken": str},
    total=False,
)


class ListConfigurationsPaginateResponseTypeDef(
    _ListConfigurationsPaginateResponseTypeDef
):
    """
    Type definition for `ListConfigurationsPaginate` `Response`

    - **configurations** *(list) --*

      Returns configuration details, including the configuration ID, attribute names, and attribute
      values.

      - *(dict) --*

        - *(string) --*

          - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListConfigurationsPaginatefiltersTypeDef = TypedDict(
    "_ListConfigurationsPaginatefiltersTypeDef",
    {"name": str, "values": List[str], "condition": str},
)


class ListConfigurationsPaginatefiltersTypeDef(
    _ListConfigurationsPaginatefiltersTypeDef
):
    """
    Type definition for `ListConfigurationsPaginate` `filters`

    A filter that can use conditional operators.

    For more information about filters, see `Querying Discovered Configuration Items
    <http://docs.aws.amazon.com/application-discovery/latest/APIReference/discovery-api-queries.html>`__
    .

    - **name** *(string) --* **[REQUIRED]**

      The name of the filter.

    - **values** *(list) --* **[REQUIRED]**

      A string value on which to filter. For example, if you choose the
      ``destinationServer.osVersion`` filter name, you could specify ``Ubuntu`` for the value.

      - *(string) --*

    - **condition** *(string) --* **[REQUIRED]**

      A conditional operator. The following operators are valid: EQUALS, NOT_EQUALS, CONTAINS,
      NOT_CONTAINS. If you specify multiple filters, the system utilizes all filters as though
      concatenated by *AND* . If you specify multiple values for a particular filter, the system
      differentiates the values using *OR* . Calling either *DescribeConfigurations* or
      *ListConfigurations* returns attributes of matching configuration items.
    """


_RequiredListConfigurationsPaginateorderByTypeDef = TypedDict(
    "_RequiredListConfigurationsPaginateorderByTypeDef", {"fieldName": str}
)
_OptionalListConfigurationsPaginateorderByTypeDef = TypedDict(
    "_OptionalListConfigurationsPaginateorderByTypeDef", {"sortOrder": str}, total=False
)


class ListConfigurationsPaginateorderByTypeDef(
    _RequiredListConfigurationsPaginateorderByTypeDef,
    _OptionalListConfigurationsPaginateorderByTypeDef,
):
    """
    Type definition for `ListConfigurationsPaginate` `orderBy`

    A field and direction for ordered output.

    - **fieldName** *(string) --* **[REQUIRED]**

      The field on which to order.

    - **sortOrder** *(string) --*

      Ordering direction.
    """
