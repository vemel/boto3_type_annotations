"Main interface for mgh type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientAssociateCreatedArtifactCreatedArtifactTypeDef",
    "ClientAssociateDiscoveredResourceDiscoveredResourceTypeDef",
    "ClientDescribeApplicationStateResponseTypeDef",
    "ClientDescribeMigrationTaskResponseMigrationTaskResourceAttributeListTypeDef",
    "ClientDescribeMigrationTaskResponseMigrationTaskTaskTypeDef",
    "ClientDescribeMigrationTaskResponseMigrationTaskTypeDef",
    "ClientDescribeMigrationTaskResponseTypeDef",
    "ClientListCreatedArtifactsResponseCreatedArtifactListTypeDef",
    "ClientListCreatedArtifactsResponseTypeDef",
    "ClientListDiscoveredResourcesResponseDiscoveredResourceListTypeDef",
    "ClientListDiscoveredResourcesResponseTypeDef",
    "ClientListMigrationTasksResponseMigrationTaskSummaryListTypeDef",
    "ClientListMigrationTasksResponseTypeDef",
    "ClientListProgressUpdateStreamsResponseProgressUpdateStreamSummaryListTypeDef",
    "ClientListProgressUpdateStreamsResponseTypeDef",
    "ClientNotifyMigrationTaskStateTaskTypeDef",
    "ClientPutResourceAttributesResourceAttributeListTypeDef",
    "ListCreatedArtifactsPaginatePaginationConfigTypeDef",
    "ListCreatedArtifactsPaginateResponseCreatedArtifactListTypeDef",
    "ListCreatedArtifactsPaginateResponseTypeDef",
    "ListDiscoveredResourcesPaginatePaginationConfigTypeDef",
    "ListDiscoveredResourcesPaginateResponseDiscoveredResourceListTypeDef",
    "ListDiscoveredResourcesPaginateResponseTypeDef",
    "ListMigrationTasksPaginatePaginationConfigTypeDef",
    "ListMigrationTasksPaginateResponseMigrationTaskSummaryListTypeDef",
    "ListMigrationTasksPaginateResponseTypeDef",
    "ListProgressUpdateStreamsPaginatePaginationConfigTypeDef",
    "ListProgressUpdateStreamsPaginateResponseProgressUpdateStreamSummaryListTypeDef",
    "ListProgressUpdateStreamsPaginateResponseTypeDef",
)


_RequiredClientAssociateCreatedArtifactCreatedArtifactTypeDef = TypedDict(
    "_RequiredClientAssociateCreatedArtifactCreatedArtifactTypeDef", {"Name": str}
)
_OptionalClientAssociateCreatedArtifactCreatedArtifactTypeDef = TypedDict(
    "_OptionalClientAssociateCreatedArtifactCreatedArtifactTypeDef",
    {"Description": str},
    total=False,
)


class ClientAssociateCreatedArtifactCreatedArtifactTypeDef(
    _RequiredClientAssociateCreatedArtifactCreatedArtifactTypeDef,
    _OptionalClientAssociateCreatedArtifactCreatedArtifactTypeDef,
):
    """
    Type definition for `ClientAssociateCreatedArtifact` `CreatedArtifact`

    An ARN of the AWS resource related to the migration (e.g., AMI, EC2 instance, RDS instance, etc.)

    - **Name** *(string) --* **[REQUIRED]**

      An ARN that uniquely identifies the result of a migration task.

    - **Description** *(string) --*

      A description that can be free-form text to record additional detail about the artifact for
      clarity or for later reference.
    """


_RequiredClientAssociateDiscoveredResourceDiscoveredResourceTypeDef = TypedDict(
    "_RequiredClientAssociateDiscoveredResourceDiscoveredResourceTypeDef",
    {"ConfigurationId": str},
)
_OptionalClientAssociateDiscoveredResourceDiscoveredResourceTypeDef = TypedDict(
    "_OptionalClientAssociateDiscoveredResourceDiscoveredResourceTypeDef",
    {"Description": str},
    total=False,
)


class ClientAssociateDiscoveredResourceDiscoveredResourceTypeDef(
    _RequiredClientAssociateDiscoveredResourceDiscoveredResourceTypeDef,
    _OptionalClientAssociateDiscoveredResourceDiscoveredResourceTypeDef,
):
    """
    Type definition for `ClientAssociateDiscoveredResource` `DiscoveredResource`

    Object representing a Resource.

    - **ConfigurationId** *(string) --* **[REQUIRED]**

      The configurationId in ADS that uniquely identifies the on-premise resource.

    - **Description** *(string) --*

      A description that can be free-form text to record additional detail about the discovered
      resource for clarity or later reference.
    """


_ClientDescribeApplicationStateResponseTypeDef = TypedDict(
    "_ClientDescribeApplicationStateResponseTypeDef",
    {"ApplicationStatus": str, "LastUpdatedTime": datetime},
    total=False,
)


class ClientDescribeApplicationStateResponseTypeDef(
    _ClientDescribeApplicationStateResponseTypeDef
):
    """
    Type definition for `ClientDescribeApplicationState` `Response`

    - **ApplicationStatus** *(string) --*

      Status of the application - Not Started, In-Progress, Complete.

    - **LastUpdatedTime** *(datetime) --*

      The timestamp when the application status was last updated.
    """


_ClientDescribeMigrationTaskResponseMigrationTaskResourceAttributeListTypeDef = TypedDict(
    "_ClientDescribeMigrationTaskResponseMigrationTaskResourceAttributeListTypeDef",
    {"Type": str, "Value": str},
    total=False,
)


class ClientDescribeMigrationTaskResponseMigrationTaskResourceAttributeListTypeDef(
    _ClientDescribeMigrationTaskResponseMigrationTaskResourceAttributeListTypeDef
):
    """
    Type definition for `ClientDescribeMigrationTaskResponseMigrationTask` `ResourceAttributeList`

    Attribute associated with a resource.

    Note the corresponding format required per type listed below:

      IPV4

     ``x.x.x.x``

     *where x is an integer in the range [0,255]*

      IPV6

     ``y : y : y : y : y : y : y : y``

     *where y is a hexadecimal between 0 and FFFF. [0, FFFF]*

      MAC_ADDRESS

     ``^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$``

      FQDN

     ``^[^<>{}\\\\/?,=\\p{Cntrl}]{1,256}$``

    - **Type** *(string) --*

      Type of resource.

    - **Value** *(string) --*

      Value of the resource type.
    """


_ClientDescribeMigrationTaskResponseMigrationTaskTaskTypeDef = TypedDict(
    "_ClientDescribeMigrationTaskResponseMigrationTaskTaskTypeDef",
    {"Status": str, "StatusDetail": str, "ProgressPercent": int},
    total=False,
)


class ClientDescribeMigrationTaskResponseMigrationTaskTaskTypeDef(
    _ClientDescribeMigrationTaskResponseMigrationTaskTaskTypeDef
):
    """
    Type definition for `ClientDescribeMigrationTaskResponseMigrationTask` `Task`

    Task object encapsulating task information.

    - **Status** *(string) --*

      Status of the task - Not Started, In-Progress, Complete.

    - **StatusDetail** *(string) --*

      Details of task status as notified by a migration tool. A tool might use this field to
      provide clarifying information about the status that is unique to that tool or that
      explains an error state.

    - **ProgressPercent** *(integer) --*

      Indication of the percentage completion of the task.
    """


_ClientDescribeMigrationTaskResponseMigrationTaskTypeDef = TypedDict(
    "_ClientDescribeMigrationTaskResponseMigrationTaskTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "Task": ClientDescribeMigrationTaskResponseMigrationTaskTaskTypeDef,
        "UpdateDateTime": datetime,
        "ResourceAttributeList": List[
            ClientDescribeMigrationTaskResponseMigrationTaskResourceAttributeListTypeDef
        ],
    },
    total=False,
)


class ClientDescribeMigrationTaskResponseMigrationTaskTypeDef(
    _ClientDescribeMigrationTaskResponseMigrationTaskTypeDef
):
    """
    Type definition for `ClientDescribeMigrationTaskResponse` `MigrationTask`

    Object encapsulating information about the migration task.

    - **ProgressUpdateStream** *(string) --*

      A name that identifies the vendor of the migration tool being used.

    - **MigrationTaskName** *(string) --*

      Unique identifier that references the migration task.

    - **Task** *(dict) --*

      Task object encapsulating task information.

      - **Status** *(string) --*

        Status of the task - Not Started, In-Progress, Complete.

      - **StatusDetail** *(string) --*

        Details of task status as notified by a migration tool. A tool might use this field to
        provide clarifying information about the status that is unique to that tool or that
        explains an error state.

      - **ProgressPercent** *(integer) --*

        Indication of the percentage completion of the task.

    - **UpdateDateTime** *(datetime) --*

      The timestamp when the task was gathered.

    - **ResourceAttributeList** *(list) --*

      - *(dict) --*

        Attribute associated with a resource.

        Note the corresponding format required per type listed below:

          IPV4

         ``x.x.x.x``

         *where x is an integer in the range [0,255]*

          IPV6

         ``y : y : y : y : y : y : y : y``

         *where y is a hexadecimal between 0 and FFFF. [0, FFFF]*

          MAC_ADDRESS

         ``^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$``

          FQDN

         ``^[^<>{}\\\\/?,=\\p{Cntrl}]{1,256}$``

        - **Type** *(string) --*

          Type of resource.

        - **Value** *(string) --*

          Value of the resource type.
    """


_ClientDescribeMigrationTaskResponseTypeDef = TypedDict(
    "_ClientDescribeMigrationTaskResponseTypeDef",
    {"MigrationTask": ClientDescribeMigrationTaskResponseMigrationTaskTypeDef},
    total=False,
)


class ClientDescribeMigrationTaskResponseTypeDef(
    _ClientDescribeMigrationTaskResponseTypeDef
):
    """
    Type definition for `ClientDescribeMigrationTask` `Response`

    - **MigrationTask** *(dict) --*

      Object encapsulating information about the migration task.

      - **ProgressUpdateStream** *(string) --*

        A name that identifies the vendor of the migration tool being used.

      - **MigrationTaskName** *(string) --*

        Unique identifier that references the migration task.

      - **Task** *(dict) --*

        Task object encapsulating task information.

        - **Status** *(string) --*

          Status of the task - Not Started, In-Progress, Complete.

        - **StatusDetail** *(string) --*

          Details of task status as notified by a migration tool. A tool might use this field to
          provide clarifying information about the status that is unique to that tool or that
          explains an error state.

        - **ProgressPercent** *(integer) --*

          Indication of the percentage completion of the task.

      - **UpdateDateTime** *(datetime) --*

        The timestamp when the task was gathered.

      - **ResourceAttributeList** *(list) --*

        - *(dict) --*

          Attribute associated with a resource.

          Note the corresponding format required per type listed below:

            IPV4

           ``x.x.x.x``

           *where x is an integer in the range [0,255]*

            IPV6

           ``y : y : y : y : y : y : y : y``

           *where y is a hexadecimal between 0 and FFFF. [0, FFFF]*

            MAC_ADDRESS

           ``^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$``

            FQDN

           ``^[^<>{}\\\\/?,=\\p{Cntrl}]{1,256}$``

          - **Type** *(string) --*

            Type of resource.

          - **Value** *(string) --*

            Value of the resource type.
    """


_ClientListCreatedArtifactsResponseCreatedArtifactListTypeDef = TypedDict(
    "_ClientListCreatedArtifactsResponseCreatedArtifactListTypeDef",
    {"Name": str, "Description": str},
    total=False,
)


class ClientListCreatedArtifactsResponseCreatedArtifactListTypeDef(
    _ClientListCreatedArtifactsResponseCreatedArtifactListTypeDef
):
    """
    Type definition for `ClientListCreatedArtifactsResponse` `CreatedArtifactList`

    An ARN of the AWS cloud resource target receiving the migration (e.g., AMI, EC2 instance,
    RDS instance, etc.).

    - **Name** *(string) --*

      An ARN that uniquely identifies the result of a migration task.

    - **Description** *(string) --*

      A description that can be free-form text to record additional detail about the artifact
      for clarity or for later reference.
    """


_ClientListCreatedArtifactsResponseTypeDef = TypedDict(
    "_ClientListCreatedArtifactsResponseTypeDef",
    {
        "NextToken": str,
        "CreatedArtifactList": List[
            ClientListCreatedArtifactsResponseCreatedArtifactListTypeDef
        ],
    },
    total=False,
)


class ClientListCreatedArtifactsResponseTypeDef(
    _ClientListCreatedArtifactsResponseTypeDef
):
    """
    Type definition for `ClientListCreatedArtifacts` `Response`

    - **NextToken** *(string) --*

      If there are more created artifacts than the max result, return the next token to be passed
      to the next call as a bookmark of where to start from.

    - **CreatedArtifactList** *(list) --*

      List of created artifacts up to the maximum number of results specified in the request.

      - *(dict) --*

        An ARN of the AWS cloud resource target receiving the migration (e.g., AMI, EC2 instance,
        RDS instance, etc.).

        - **Name** *(string) --*

          An ARN that uniquely identifies the result of a migration task.

        - **Description** *(string) --*

          A description that can be free-form text to record additional detail about the artifact
          for clarity or for later reference.
    """


_ClientListDiscoveredResourcesResponseDiscoveredResourceListTypeDef = TypedDict(
    "_ClientListDiscoveredResourcesResponseDiscoveredResourceListTypeDef",
    {"ConfigurationId": str, "Description": str},
    total=False,
)


class ClientListDiscoveredResourcesResponseDiscoveredResourceListTypeDef(
    _ClientListDiscoveredResourcesResponseDiscoveredResourceListTypeDef
):
    """
    Type definition for `ClientListDiscoveredResourcesResponse` `DiscoveredResourceList`

    Object representing the on-premises resource being migrated.

    - **ConfigurationId** *(string) --*

      The configurationId in ADS that uniquely identifies the on-premise resource.

    - **Description** *(string) --*

      A description that can be free-form text to record additional detail about the discovered
      resource for clarity or later reference.
    """


_ClientListDiscoveredResourcesResponseTypeDef = TypedDict(
    "_ClientListDiscoveredResourcesResponseTypeDef",
    {
        "NextToken": str,
        "DiscoveredResourceList": List[
            ClientListDiscoveredResourcesResponseDiscoveredResourceListTypeDef
        ],
    },
    total=False,
)


class ClientListDiscoveredResourcesResponseTypeDef(
    _ClientListDiscoveredResourcesResponseTypeDef
):
    """
    Type definition for `ClientListDiscoveredResources` `Response`

    - **NextToken** *(string) --*

      If there are more discovered resources than the max result, return the next token to be
      passed to the next call as a bookmark of where to start from.

    - **DiscoveredResourceList** *(list) --*

      Returned list of discovered resources associated with the given MigrationTask.

      - *(dict) --*

        Object representing the on-premises resource being migrated.

        - **ConfigurationId** *(string) --*

          The configurationId in ADS that uniquely identifies the on-premise resource.

        - **Description** *(string) --*

          A description that can be free-form text to record additional detail about the discovered
          resource for clarity or later reference.
    """


_ClientListMigrationTasksResponseMigrationTaskSummaryListTypeDef = TypedDict(
    "_ClientListMigrationTasksResponseMigrationTaskSummaryListTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "Status": str,
        "ProgressPercent": int,
        "StatusDetail": str,
        "UpdateDateTime": datetime,
    },
    total=False,
)


class ClientListMigrationTasksResponseMigrationTaskSummaryListTypeDef(
    _ClientListMigrationTasksResponseMigrationTaskSummaryListTypeDef
):
    """
    Type definition for `ClientListMigrationTasksResponse` `MigrationTaskSummaryList`

    MigrationTaskSummary includes ``MigrationTaskName`` , ``ProgressPercent`` ,
    ``ProgressUpdateStream`` , ``Status`` , and ``UpdateDateTime`` for each task.

    - **ProgressUpdateStream** *(string) --*

      An AWS resource used for access control. It should uniquely identify the migration tool
      as it is used for all updates made by the tool.

    - **MigrationTaskName** *(string) --*

      Unique identifier that references the migration task.

    - **Status** *(string) --*

      Status of the task.

    - **ProgressPercent** *(integer) --*

    - **StatusDetail** *(string) --*

      Detail information of what is being done within the overall status state.

    - **UpdateDateTime** *(datetime) --*

      The timestamp when the task was gathered.
    """


_ClientListMigrationTasksResponseTypeDef = TypedDict(
    "_ClientListMigrationTasksResponseTypeDef",
    {
        "NextToken": str,
        "MigrationTaskSummaryList": List[
            ClientListMigrationTasksResponseMigrationTaskSummaryListTypeDef
        ],
    },
    total=False,
)


class ClientListMigrationTasksResponseTypeDef(_ClientListMigrationTasksResponseTypeDef):
    """
    Type definition for `ClientListMigrationTasks` `Response`

    - **NextToken** *(string) --*

      If there are more migration tasks than the max result, return the next token to be passed to
      the next call as a bookmark of where to start from.

    - **MigrationTaskSummaryList** *(list) --*

      Lists the migration task's summary which includes: ``MigrationTaskName`` ,
      ``ProgressPercent`` , ``ProgressUpdateStream`` , ``Status`` , and the ``UpdateDateTime`` for
      each task.

      - *(dict) --*

        MigrationTaskSummary includes ``MigrationTaskName`` , ``ProgressPercent`` ,
        ``ProgressUpdateStream`` , ``Status`` , and ``UpdateDateTime`` for each task.

        - **ProgressUpdateStream** *(string) --*

          An AWS resource used for access control. It should uniquely identify the migration tool
          as it is used for all updates made by the tool.

        - **MigrationTaskName** *(string) --*

          Unique identifier that references the migration task.

        - **Status** *(string) --*

          Status of the task.

        - **ProgressPercent** *(integer) --*

        - **StatusDetail** *(string) --*

          Detail information of what is being done within the overall status state.

        - **UpdateDateTime** *(datetime) --*

          The timestamp when the task was gathered.
    """


_ClientListProgressUpdateStreamsResponseProgressUpdateStreamSummaryListTypeDef = TypedDict(
    "_ClientListProgressUpdateStreamsResponseProgressUpdateStreamSummaryListTypeDef",
    {"ProgressUpdateStreamName": str},
    total=False,
)


class ClientListProgressUpdateStreamsResponseProgressUpdateStreamSummaryListTypeDef(
    _ClientListProgressUpdateStreamsResponseProgressUpdateStreamSummaryListTypeDef
):
    """
    Type definition for `ClientListProgressUpdateStreamsResponse` `ProgressUpdateStreamSummaryList`

    Summary of the AWS resource used for access control that is implicitly linked to your AWS
    account.

    - **ProgressUpdateStreamName** *(string) --*

      The name of the ProgressUpdateStream.
    """


_ClientListProgressUpdateStreamsResponseTypeDef = TypedDict(
    "_ClientListProgressUpdateStreamsResponseTypeDef",
    {
        "ProgressUpdateStreamSummaryList": List[
            ClientListProgressUpdateStreamsResponseProgressUpdateStreamSummaryListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListProgressUpdateStreamsResponseTypeDef(
    _ClientListProgressUpdateStreamsResponseTypeDef
):
    """
    Type definition for `ClientListProgressUpdateStreams` `Response`

    - **ProgressUpdateStreamSummaryList** *(list) --*

      List of progress update streams up to the max number of results passed in the input.

      - *(dict) --*

        Summary of the AWS resource used for access control that is implicitly linked to your AWS
        account.

        - **ProgressUpdateStreamName** *(string) --*

          The name of the ProgressUpdateStream.

    - **NextToken** *(string) --*

      If there are more streams created than the max result, return the next token to be passed to
      the next call as a bookmark of where to start from.
    """


_RequiredClientNotifyMigrationTaskStateTaskTypeDef = TypedDict(
    "_RequiredClientNotifyMigrationTaskStateTaskTypeDef", {"Status": str}
)
_OptionalClientNotifyMigrationTaskStateTaskTypeDef = TypedDict(
    "_OptionalClientNotifyMigrationTaskStateTaskTypeDef",
    {"StatusDetail": str, "ProgressPercent": int},
    total=False,
)


class ClientNotifyMigrationTaskStateTaskTypeDef(
    _RequiredClientNotifyMigrationTaskStateTaskTypeDef,
    _OptionalClientNotifyMigrationTaskStateTaskTypeDef,
):
    """
    Type definition for `ClientNotifyMigrationTaskState` `Task`

    Information about the task's progress and status.

    - **Status** *(string) --* **[REQUIRED]**

      Status of the task - Not Started, In-Progress, Complete.

    - **StatusDetail** *(string) --*

      Details of task status as notified by a migration tool. A tool might use this field to provide
      clarifying information about the status that is unique to that tool or that explains an error
      state.

    - **ProgressPercent** *(integer) --*

      Indication of the percentage completion of the task.
    """


_ClientPutResourceAttributesResourceAttributeListTypeDef = TypedDict(
    "_ClientPutResourceAttributesResourceAttributeListTypeDef",
    {"Type": str, "Value": str},
)


class ClientPutResourceAttributesResourceAttributeListTypeDef(
    _ClientPutResourceAttributesResourceAttributeListTypeDef
):
    """
    Type definition for `ClientPutResourceAttributes` `ResourceAttributeList`

    Attribute associated with a resource.

    Note the corresponding format required per type listed below:

      IPV4

     ``x.x.x.x``

     *where x is an integer in the range [0,255]*

      IPV6

     ``y : y : y : y : y : y : y : y``

     *where y is a hexadecimal between 0 and FFFF. [0, FFFF]*

      MAC_ADDRESS

     ``^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$``

      FQDN

     ``^[^<>{}\\\\/?,=\\p{Cntrl}]{1,256}$``

    - **Type** *(string) --* **[REQUIRED]**

      Type of resource.

    - **Value** *(string) --* **[REQUIRED]**

      Value of the resource type.
    """


_ListCreatedArtifactsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListCreatedArtifactsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListCreatedArtifactsPaginatePaginationConfigTypeDef(
    _ListCreatedArtifactsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListCreatedArtifactsPaginate` `PaginationConfig`

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


_ListCreatedArtifactsPaginateResponseCreatedArtifactListTypeDef = TypedDict(
    "_ListCreatedArtifactsPaginateResponseCreatedArtifactListTypeDef",
    {"Name": str, "Description": str},
    total=False,
)


class ListCreatedArtifactsPaginateResponseCreatedArtifactListTypeDef(
    _ListCreatedArtifactsPaginateResponseCreatedArtifactListTypeDef
):
    """
    Type definition for `ListCreatedArtifactsPaginateResponse` `CreatedArtifactList`

    An ARN of the AWS cloud resource target receiving the migration (e.g., AMI, EC2 instance,
    RDS instance, etc.).

    - **Name** *(string) --*

      An ARN that uniquely identifies the result of a migration task.

    - **Description** *(string) --*

      A description that can be free-form text to record additional detail about the artifact
      for clarity or for later reference.
    """


_ListCreatedArtifactsPaginateResponseTypeDef = TypedDict(
    "_ListCreatedArtifactsPaginateResponseTypeDef",
    {
        "CreatedArtifactList": List[
            ListCreatedArtifactsPaginateResponseCreatedArtifactListTypeDef
        ]
    },
    total=False,
)


class ListCreatedArtifactsPaginateResponseTypeDef(
    _ListCreatedArtifactsPaginateResponseTypeDef
):
    """
    Type definition for `ListCreatedArtifactsPaginate` `Response`

    - **CreatedArtifactList** *(list) --*

      List of created artifacts up to the maximum number of results specified in the request.

      - *(dict) --*

        An ARN of the AWS cloud resource target receiving the migration (e.g., AMI, EC2 instance,
        RDS instance, etc.).

        - **Name** *(string) --*

          An ARN that uniquely identifies the result of a migration task.

        - **Description** *(string) --*

          A description that can be free-form text to record additional detail about the artifact
          for clarity or for later reference.
    """


_ListDiscoveredResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDiscoveredResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDiscoveredResourcesPaginatePaginationConfigTypeDef(
    _ListDiscoveredResourcesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDiscoveredResourcesPaginate` `PaginationConfig`

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


_ListDiscoveredResourcesPaginateResponseDiscoveredResourceListTypeDef = TypedDict(
    "_ListDiscoveredResourcesPaginateResponseDiscoveredResourceListTypeDef",
    {"ConfigurationId": str, "Description": str},
    total=False,
)


class ListDiscoveredResourcesPaginateResponseDiscoveredResourceListTypeDef(
    _ListDiscoveredResourcesPaginateResponseDiscoveredResourceListTypeDef
):
    """
    Type definition for `ListDiscoveredResourcesPaginateResponse` `DiscoveredResourceList`

    Object representing the on-premises resource being migrated.

    - **ConfigurationId** *(string) --*

      The configurationId in ADS that uniquely identifies the on-premise resource.

    - **Description** *(string) --*

      A description that can be free-form text to record additional detail about the discovered
      resource for clarity or later reference.
    """


_ListDiscoveredResourcesPaginateResponseTypeDef = TypedDict(
    "_ListDiscoveredResourcesPaginateResponseTypeDef",
    {
        "DiscoveredResourceList": List[
            ListDiscoveredResourcesPaginateResponseDiscoveredResourceListTypeDef
        ]
    },
    total=False,
)


class ListDiscoveredResourcesPaginateResponseTypeDef(
    _ListDiscoveredResourcesPaginateResponseTypeDef
):
    """
    Type definition for `ListDiscoveredResourcesPaginate` `Response`

    - **DiscoveredResourceList** *(list) --*

      Returned list of discovered resources associated with the given MigrationTask.

      - *(dict) --*

        Object representing the on-premises resource being migrated.

        - **ConfigurationId** *(string) --*

          The configurationId in ADS that uniquely identifies the on-premise resource.

        - **Description** *(string) --*

          A description that can be free-form text to record additional detail about the discovered
          resource for clarity or later reference.
    """


_ListMigrationTasksPaginatePaginationConfigTypeDef = TypedDict(
    "_ListMigrationTasksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListMigrationTasksPaginatePaginationConfigTypeDef(
    _ListMigrationTasksPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListMigrationTasksPaginate` `PaginationConfig`

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


_ListMigrationTasksPaginateResponseMigrationTaskSummaryListTypeDef = TypedDict(
    "_ListMigrationTasksPaginateResponseMigrationTaskSummaryListTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "Status": str,
        "ProgressPercent": int,
        "StatusDetail": str,
        "UpdateDateTime": datetime,
    },
    total=False,
)


class ListMigrationTasksPaginateResponseMigrationTaskSummaryListTypeDef(
    _ListMigrationTasksPaginateResponseMigrationTaskSummaryListTypeDef
):
    """
    Type definition for `ListMigrationTasksPaginateResponse` `MigrationTaskSummaryList`

    MigrationTaskSummary includes ``MigrationTaskName`` , ``ProgressPercent`` ,
    ``ProgressUpdateStream`` , ``Status`` , and ``UpdateDateTime`` for each task.

    - **ProgressUpdateStream** *(string) --*

      An AWS resource used for access control. It should uniquely identify the migration tool
      as it is used for all updates made by the tool.

    - **MigrationTaskName** *(string) --*

      Unique identifier that references the migration task.

    - **Status** *(string) --*

      Status of the task.

    - **ProgressPercent** *(integer) --*

    - **StatusDetail** *(string) --*

      Detail information of what is being done within the overall status state.

    - **UpdateDateTime** *(datetime) --*

      The timestamp when the task was gathered.
    """


_ListMigrationTasksPaginateResponseTypeDef = TypedDict(
    "_ListMigrationTasksPaginateResponseTypeDef",
    {
        "MigrationTaskSummaryList": List[
            ListMigrationTasksPaginateResponseMigrationTaskSummaryListTypeDef
        ]
    },
    total=False,
)


class ListMigrationTasksPaginateResponseTypeDef(
    _ListMigrationTasksPaginateResponseTypeDef
):
    """
    Type definition for `ListMigrationTasksPaginate` `Response`

    - **MigrationTaskSummaryList** *(list) --*

      Lists the migration task's summary which includes: ``MigrationTaskName`` ,
      ``ProgressPercent`` , ``ProgressUpdateStream`` , ``Status`` , and the ``UpdateDateTime`` for
      each task.

      - *(dict) --*

        MigrationTaskSummary includes ``MigrationTaskName`` , ``ProgressPercent`` ,
        ``ProgressUpdateStream`` , ``Status`` , and ``UpdateDateTime`` for each task.

        - **ProgressUpdateStream** *(string) --*

          An AWS resource used for access control. It should uniquely identify the migration tool
          as it is used for all updates made by the tool.

        - **MigrationTaskName** *(string) --*

          Unique identifier that references the migration task.

        - **Status** *(string) --*

          Status of the task.

        - **ProgressPercent** *(integer) --*

        - **StatusDetail** *(string) --*

          Detail information of what is being done within the overall status state.

        - **UpdateDateTime** *(datetime) --*

          The timestamp when the task was gathered.
    """


_ListProgressUpdateStreamsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListProgressUpdateStreamsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListProgressUpdateStreamsPaginatePaginationConfigTypeDef(
    _ListProgressUpdateStreamsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListProgressUpdateStreamsPaginate` `PaginationConfig`

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


_ListProgressUpdateStreamsPaginateResponseProgressUpdateStreamSummaryListTypeDef = TypedDict(
    "_ListProgressUpdateStreamsPaginateResponseProgressUpdateStreamSummaryListTypeDef",
    {"ProgressUpdateStreamName": str},
    total=False,
)


class ListProgressUpdateStreamsPaginateResponseProgressUpdateStreamSummaryListTypeDef(
    _ListProgressUpdateStreamsPaginateResponseProgressUpdateStreamSummaryListTypeDef
):
    """
    Type definition for `ListProgressUpdateStreamsPaginateResponse` `ProgressUpdateStreamSummaryList`

    Summary of the AWS resource used for access control that is implicitly linked to your AWS
    account.

    - **ProgressUpdateStreamName** *(string) --*

      The name of the ProgressUpdateStream.
    """


_ListProgressUpdateStreamsPaginateResponseTypeDef = TypedDict(
    "_ListProgressUpdateStreamsPaginateResponseTypeDef",
    {
        "ProgressUpdateStreamSummaryList": List[
            ListProgressUpdateStreamsPaginateResponseProgressUpdateStreamSummaryListTypeDef
        ]
    },
    total=False,
)


class ListProgressUpdateStreamsPaginateResponseTypeDef(
    _ListProgressUpdateStreamsPaginateResponseTypeDef
):
    """
    Type definition for `ListProgressUpdateStreamsPaginate` `Response`

    - **ProgressUpdateStreamSummaryList** *(list) --*

      List of progress update streams up to the max number of results passed in the input.

      - *(dict) --*

        Summary of the AWS resource used for access control that is implicitly linked to your AWS
        account.

        - **ProgressUpdateStreamName** *(string) --*

          The name of the ProgressUpdateStream.
    """
