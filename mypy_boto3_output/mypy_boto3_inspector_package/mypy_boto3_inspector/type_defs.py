"Main interface for inspector type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientAddAttributesToFindingsResponsefailedItemsTypeDef",
    "ClientAddAttributesToFindingsResponseTypeDef",
    "ClientAddAttributesToFindingsattributesTypeDef",
    "ClientCreateAssessmentTargetResponseTypeDef",
    "ClientCreateAssessmentTemplateResponseTypeDef",
    "ClientCreateAssessmentTemplateuserAttributesForFindingsTypeDef",
    "ClientCreateExclusionsPreviewResponseTypeDef",
    "ClientCreateResourceGroupResponseTypeDef",
    "ClientCreateResourceGroupresourceGroupTagsTypeDef",
    "ClientDescribeAssessmentRunsResponseassessmentRunsnotificationsTypeDef",
    "ClientDescribeAssessmentRunsResponseassessmentRunsstateChangesTypeDef",
    "ClientDescribeAssessmentRunsResponseassessmentRunsuserAttributesForFindingsTypeDef",
    "ClientDescribeAssessmentRunsResponseassessmentRunsTypeDef",
    "ClientDescribeAssessmentRunsResponsefailedItemsTypeDef",
    "ClientDescribeAssessmentRunsResponseTypeDef",
    "ClientDescribeAssessmentTargetsResponseassessmentTargetsTypeDef",
    "ClientDescribeAssessmentTargetsResponsefailedItemsTypeDef",
    "ClientDescribeAssessmentTargetsResponseTypeDef",
    "ClientDescribeAssessmentTemplatesResponseassessmentTemplatesuserAttributesForFindingsTypeDef",
    "ClientDescribeAssessmentTemplatesResponseassessmentTemplatesTypeDef",
    "ClientDescribeAssessmentTemplatesResponsefailedItemsTypeDef",
    "ClientDescribeAssessmentTemplatesResponseTypeDef",
    "ClientDescribeCrossAccountAccessRoleResponseTypeDef",
    "ClientDescribeExclusionsResponseexclusionsattributesTypeDef",
    "ClientDescribeExclusionsResponseexclusionsscopesTypeDef",
    "ClientDescribeExclusionsResponseexclusionsTypeDef",
    "ClientDescribeExclusionsResponsefailedItemsTypeDef",
    "ClientDescribeExclusionsResponseTypeDef",
    "ClientDescribeFindingsResponsefailedItemsTypeDef",
    "ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacesprivateIpAddressesTypeDef",
    "ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacessecurityGroupsTypeDef",
    "ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacesTypeDef",
    "ClientDescribeFindingsResponsefindingsassetAttributestagsTypeDef",
    "ClientDescribeFindingsResponsefindingsassetAttributesTypeDef",
    "ClientDescribeFindingsResponsefindingsattributesTypeDef",
    "ClientDescribeFindingsResponsefindingsserviceAttributesTypeDef",
    "ClientDescribeFindingsResponsefindingsuserAttributesTypeDef",
    "ClientDescribeFindingsResponsefindingsTypeDef",
    "ClientDescribeFindingsResponseTypeDef",
    "ClientDescribeResourceGroupsResponsefailedItemsTypeDef",
    "ClientDescribeResourceGroupsResponseresourceGroupstagsTypeDef",
    "ClientDescribeResourceGroupsResponseresourceGroupsTypeDef",
    "ClientDescribeResourceGroupsResponseTypeDef",
    "ClientDescribeRulesPackagesResponsefailedItemsTypeDef",
    "ClientDescribeRulesPackagesResponserulesPackagesTypeDef",
    "ClientDescribeRulesPackagesResponseTypeDef",
    "ClientGetAssessmentReportResponseTypeDef",
    "ClientGetExclusionsPreviewResponseexclusionPreviewsattributesTypeDef",
    "ClientGetExclusionsPreviewResponseexclusionPreviewsscopesTypeDef",
    "ClientGetExclusionsPreviewResponseexclusionPreviewsTypeDef",
    "ClientGetExclusionsPreviewResponseTypeDef",
    "ClientGetTelemetryMetadataResponsetelemetryMetadataTypeDef",
    "ClientGetTelemetryMetadataResponseTypeDef",
    "ClientListAssessmentRunAgentsResponseassessmentRunAgentstelemetryMetadataTypeDef",
    "ClientListAssessmentRunAgentsResponseassessmentRunAgentsTypeDef",
    "ClientListAssessmentRunAgentsResponseTypeDef",
    "ClientListAssessmentRunAgentsfilterTypeDef",
    "ClientListAssessmentRunsResponseTypeDef",
    "ClientListAssessmentRunsfiltercompletionTimeRangeTypeDef",
    "ClientListAssessmentRunsfilterdurationRangeTypeDef",
    "ClientListAssessmentRunsfilterstartTimeRangeTypeDef",
    "ClientListAssessmentRunsfilterstateChangeTimeRangeTypeDef",
    "ClientListAssessmentRunsfilterTypeDef",
    "ClientListAssessmentTargetsResponseTypeDef",
    "ClientListAssessmentTargetsfilterTypeDef",
    "ClientListAssessmentTemplatesResponseTypeDef",
    "ClientListAssessmentTemplatesfilterdurationRangeTypeDef",
    "ClientListAssessmentTemplatesfilterTypeDef",
    "ClientListEventSubscriptionsResponsesubscriptionseventSubscriptionsTypeDef",
    "ClientListEventSubscriptionsResponsesubscriptionsTypeDef",
    "ClientListEventSubscriptionsResponseTypeDef",
    "ClientListExclusionsResponseTypeDef",
    "ClientListFindingsResponseTypeDef",
    "ClientListFindingsfilterattributesTypeDef",
    "ClientListFindingsfiltercreationTimeRangeTypeDef",
    "ClientListFindingsfilteruserAttributesTypeDef",
    "ClientListFindingsfilterTypeDef",
    "ClientListRulesPackagesResponseTypeDef",
    "ClientListTagsForResourceResponsetagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPreviewAgentsResponseagentPreviewsTypeDef",
    "ClientPreviewAgentsResponseTypeDef",
    "ClientRemoveAttributesFromFindingsResponsefailedItemsTypeDef",
    "ClientRemoveAttributesFromFindingsResponseTypeDef",
    "ClientSetTagsForResourcetagsTypeDef",
    "ClientStartAssessmentRunResponseTypeDef",
    "ListAssessmentRunAgentsPaginatePaginationConfigTypeDef",
    "ListAssessmentRunAgentsPaginateResponseassessmentRunAgentstelemetryMetadataTypeDef",
    "ListAssessmentRunAgentsPaginateResponseassessmentRunAgentsTypeDef",
    "ListAssessmentRunAgentsPaginateResponseTypeDef",
    "ListAssessmentRunAgentsPaginatefilterTypeDef",
    "ListAssessmentRunsPaginatePaginationConfigTypeDef",
    "ListAssessmentRunsPaginateResponseTypeDef",
    "ListAssessmentRunsPaginatefiltercompletionTimeRangeTypeDef",
    "ListAssessmentRunsPaginatefilterdurationRangeTypeDef",
    "ListAssessmentRunsPaginatefilterstartTimeRangeTypeDef",
    "ListAssessmentRunsPaginatefilterstateChangeTimeRangeTypeDef",
    "ListAssessmentRunsPaginatefilterTypeDef",
    "ListAssessmentTargetsPaginatePaginationConfigTypeDef",
    "ListAssessmentTargetsPaginateResponseTypeDef",
    "ListAssessmentTargetsPaginatefilterTypeDef",
    "ListAssessmentTemplatesPaginatePaginationConfigTypeDef",
    "ListAssessmentTemplatesPaginateResponseTypeDef",
    "ListAssessmentTemplatesPaginatefilterdurationRangeTypeDef",
    "ListAssessmentTemplatesPaginatefilterTypeDef",
    "ListEventSubscriptionsPaginatePaginationConfigTypeDef",
    "ListEventSubscriptionsPaginateResponsesubscriptionseventSubscriptionsTypeDef",
    "ListEventSubscriptionsPaginateResponsesubscriptionsTypeDef",
    "ListEventSubscriptionsPaginateResponseTypeDef",
    "ListExclusionsPaginatePaginationConfigTypeDef",
    "ListExclusionsPaginateResponseTypeDef",
    "ListFindingsPaginatePaginationConfigTypeDef",
    "ListFindingsPaginateResponseTypeDef",
    "ListFindingsPaginatefilterattributesTypeDef",
    "ListFindingsPaginatefiltercreationTimeRangeTypeDef",
    "ListFindingsPaginatefilteruserAttributesTypeDef",
    "ListFindingsPaginatefilterTypeDef",
    "ListRulesPackagesPaginatePaginationConfigTypeDef",
    "ListRulesPackagesPaginateResponseTypeDef",
    "PreviewAgentsPaginatePaginationConfigTypeDef",
    "PreviewAgentsPaginateResponseagentPreviewsTypeDef",
    "PreviewAgentsPaginateResponseTypeDef",
)


_ClientAddAttributesToFindingsResponsefailedItemsTypeDef = TypedDict(
    "_ClientAddAttributesToFindingsResponsefailedItemsTypeDef",
    {"failureCode": str, "retryable": bool},
    total=False,
)


class ClientAddAttributesToFindingsResponsefailedItemsTypeDef(
    _ClientAddAttributesToFindingsResponsefailedItemsTypeDef
):
    """
    Type definition for `ClientAddAttributesToFindingsResponse` `failedItems`

    Includes details about the failed items.

    - **failureCode** *(string) --*

      The status code of a failed item.

    - **retryable** *(boolean) --*

      Indicates whether you can immediately retry a request for this item for a specified
      resource.
    """


_ClientAddAttributesToFindingsResponseTypeDef = TypedDict(
    "_ClientAddAttributesToFindingsResponseTypeDef",
    {"failedItems": Dict[str, ClientAddAttributesToFindingsResponsefailedItemsTypeDef]},
    total=False,
)


class ClientAddAttributesToFindingsResponseTypeDef(
    _ClientAddAttributesToFindingsResponseTypeDef
):
    """
    Type definition for `ClientAddAttributesToFindings` `Response`

    - **failedItems** *(dict) --*

      Attribute details that cannot be described. An error code is provided for each failed item.

      - *(string) --*

        - *(dict) --*

          Includes details about the failed items.

          - **failureCode** *(string) --*

            The status code of a failed item.

          - **retryable** *(boolean) --*

            Indicates whether you can immediately retry a request for this item for a specified
            resource.
    """


_RequiredClientAddAttributesToFindingsattributesTypeDef = TypedDict(
    "_RequiredClientAddAttributesToFindingsattributesTypeDef", {"key": str}
)
_OptionalClientAddAttributesToFindingsattributesTypeDef = TypedDict(
    "_OptionalClientAddAttributesToFindingsattributesTypeDef",
    {"value": str},
    total=False,
)


class ClientAddAttributesToFindingsattributesTypeDef(
    _RequiredClientAddAttributesToFindingsattributesTypeDef,
    _OptionalClientAddAttributesToFindingsattributesTypeDef,
):
    """
    Type definition for `ClientAddAttributesToFindings` `attributes`

    This data type is used as a request parameter in the  AddAttributesToFindings and
    CreateAssessmentTemplate actions.

    - **key** *(string) --* **[REQUIRED]**

      The attribute key.

    - **value** *(string) --*

      The value assigned to the attribute key.
    """


_ClientCreateAssessmentTargetResponseTypeDef = TypedDict(
    "_ClientCreateAssessmentTargetResponseTypeDef",
    {"assessmentTargetArn": str},
    total=False,
)


class ClientCreateAssessmentTargetResponseTypeDef(
    _ClientCreateAssessmentTargetResponseTypeDef
):
    """
    Type definition for `ClientCreateAssessmentTarget` `Response`

    - **assessmentTargetArn** *(string) --*

      The ARN that specifies the assessment target that is created.
    """


_ClientCreateAssessmentTemplateResponseTypeDef = TypedDict(
    "_ClientCreateAssessmentTemplateResponseTypeDef",
    {"assessmentTemplateArn": str},
    total=False,
)


class ClientCreateAssessmentTemplateResponseTypeDef(
    _ClientCreateAssessmentTemplateResponseTypeDef
):
    """
    Type definition for `ClientCreateAssessmentTemplate` `Response`

    - **assessmentTemplateArn** *(string) --*

      The ARN that specifies the assessment template that is created.
    """


_RequiredClientCreateAssessmentTemplateuserAttributesForFindingsTypeDef = TypedDict(
    "_RequiredClientCreateAssessmentTemplateuserAttributesForFindingsTypeDef",
    {"key": str},
)
_OptionalClientCreateAssessmentTemplateuserAttributesForFindingsTypeDef = TypedDict(
    "_OptionalClientCreateAssessmentTemplateuserAttributesForFindingsTypeDef",
    {"value": str},
    total=False,
)


class ClientCreateAssessmentTemplateuserAttributesForFindingsTypeDef(
    _RequiredClientCreateAssessmentTemplateuserAttributesForFindingsTypeDef,
    _OptionalClientCreateAssessmentTemplateuserAttributesForFindingsTypeDef,
):
    """
    Type definition for `ClientCreateAssessmentTemplate` `userAttributesForFindings`

    This data type is used as a request parameter in the  AddAttributesToFindings and
    CreateAssessmentTemplate actions.

    - **key** *(string) --* **[REQUIRED]**

      The attribute key.

    - **value** *(string) --*

      The value assigned to the attribute key.
    """


_ClientCreateExclusionsPreviewResponseTypeDef = TypedDict(
    "_ClientCreateExclusionsPreviewResponseTypeDef", {"previewToken": str}, total=False
)


class ClientCreateExclusionsPreviewResponseTypeDef(
    _ClientCreateExclusionsPreviewResponseTypeDef
):
    """
    Type definition for `ClientCreateExclusionsPreview` `Response`

    - **previewToken** *(string) --*

      Specifies the unique identifier of the requested exclusions preview. You can use the unique
      identifier to retrieve the exclusions preview when running the GetExclusionsPreview API.
    """


_ClientCreateResourceGroupResponseTypeDef = TypedDict(
    "_ClientCreateResourceGroupResponseTypeDef", {"resourceGroupArn": str}, total=False
)


class ClientCreateResourceGroupResponseTypeDef(
    _ClientCreateResourceGroupResponseTypeDef
):
    """
    Type definition for `ClientCreateResourceGroup` `Response`

    - **resourceGroupArn** *(string) --*

      The ARN that specifies the resource group that is created.
    """


_RequiredClientCreateResourceGroupresourceGroupTagsTypeDef = TypedDict(
    "_RequiredClientCreateResourceGroupresourceGroupTagsTypeDef", {"key": str}
)
_OptionalClientCreateResourceGroupresourceGroupTagsTypeDef = TypedDict(
    "_OptionalClientCreateResourceGroupresourceGroupTagsTypeDef",
    {"value": str},
    total=False,
)


class ClientCreateResourceGroupresourceGroupTagsTypeDef(
    _RequiredClientCreateResourceGroupresourceGroupTagsTypeDef,
    _OptionalClientCreateResourceGroupresourceGroupTagsTypeDef,
):
    """
    Type definition for `ClientCreateResourceGroup` `resourceGroupTags`

    This data type is used as one of the elements of the  ResourceGroup data type.

    - **key** *(string) --* **[REQUIRED]**

      A tag key.

    - **value** *(string) --*

      The value assigned to a tag key.
    """


_ClientDescribeAssessmentRunsResponseassessmentRunsnotificationsTypeDef = TypedDict(
    "_ClientDescribeAssessmentRunsResponseassessmentRunsnotificationsTypeDef",
    {
        "date": datetime,
        "event": str,
        "message": str,
        "error": bool,
        "snsTopicArn": str,
        "snsPublishStatusCode": str,
    },
    total=False,
)


class ClientDescribeAssessmentRunsResponseassessmentRunsnotificationsTypeDef(
    _ClientDescribeAssessmentRunsResponseassessmentRunsnotificationsTypeDef
):
    """
    Type definition for `ClientDescribeAssessmentRunsResponseassessmentRuns` `notifications`

    Used as one of the elements of the  AssessmentRun data type.

    - **date** *(datetime) --*

      The date of the notification.

    - **event** *(string) --*

      The event for which a notification is sent.

    - **message** *(string) --*

      The message included in the notification.

    - **error** *(boolean) --*

      The Boolean value that specifies whether the notification represents an error.

    - **snsTopicArn** *(string) --*

      The SNS topic to which the SNS notification is sent.

    - **snsPublishStatusCode** *(string) --*

      The status code of the SNS notification.
    """


_ClientDescribeAssessmentRunsResponseassessmentRunsstateChangesTypeDef = TypedDict(
    "_ClientDescribeAssessmentRunsResponseassessmentRunsstateChangesTypeDef",
    {"stateChangedAt": datetime, "state": str},
    total=False,
)


class ClientDescribeAssessmentRunsResponseassessmentRunsstateChangesTypeDef(
    _ClientDescribeAssessmentRunsResponseassessmentRunsstateChangesTypeDef
):
    """
    Type definition for `ClientDescribeAssessmentRunsResponseassessmentRuns` `stateChanges`

    Used as one of the elements of the  AssessmentRun data type.

    - **stateChangedAt** *(datetime) --*

      The last time the assessment run state changed.

    - **state** *(string) --*

      The assessment run state.
    """


_ClientDescribeAssessmentRunsResponseassessmentRunsuserAttributesForFindingsTypeDef = TypedDict(
    "_ClientDescribeAssessmentRunsResponseassessmentRunsuserAttributesForFindingsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribeAssessmentRunsResponseassessmentRunsuserAttributesForFindingsTypeDef(
    _ClientDescribeAssessmentRunsResponseassessmentRunsuserAttributesForFindingsTypeDef
):
    """
    Type definition for `ClientDescribeAssessmentRunsResponseassessmentRuns` `userAttributesForFindings`

    This data type is used as a request parameter in the  AddAttributesToFindings and
    CreateAssessmentTemplate actions.

    - **key** *(string) --*

      The attribute key.

    - **value** *(string) --*

      The value assigned to the attribute key.
    """


_ClientDescribeAssessmentRunsResponseassessmentRunsTypeDef = TypedDict(
    "_ClientDescribeAssessmentRunsResponseassessmentRunsTypeDef",
    {
        "arn": str,
        "name": str,
        "assessmentTemplateArn": str,
        "state": str,
        "durationInSeconds": int,
        "rulesPackageArns": List[str],
        "userAttributesForFindings": List[
            ClientDescribeAssessmentRunsResponseassessmentRunsuserAttributesForFindingsTypeDef
        ],
        "createdAt": datetime,
        "startedAt": datetime,
        "completedAt": datetime,
        "stateChangedAt": datetime,
        "dataCollected": bool,
        "stateChanges": List[
            ClientDescribeAssessmentRunsResponseassessmentRunsstateChangesTypeDef
        ],
        "notifications": List[
            ClientDescribeAssessmentRunsResponseassessmentRunsnotificationsTypeDef
        ],
        "findingCounts": Dict[str, int],
    },
    total=False,
)


class ClientDescribeAssessmentRunsResponseassessmentRunsTypeDef(
    _ClientDescribeAssessmentRunsResponseassessmentRunsTypeDef
):
    """
    Type definition for `ClientDescribeAssessmentRunsResponse` `assessmentRuns`

    A snapshot of an Amazon Inspector assessment run that contains the findings of the
    assessment run .

    Used as the response element in the  DescribeAssessmentRuns action.

    - **arn** *(string) --*

      The ARN of the assessment run.

    - **name** *(string) --*

      The auto-generated name for the assessment run.

    - **assessmentTemplateArn** *(string) --*

      The ARN of the assessment template that is associated with the assessment run.

    - **state** *(string) --*

      The state of the assessment run.

    - **durationInSeconds** *(integer) --*

      The duration of the assessment run.

    - **rulesPackageArns** *(list) --*

      The rules packages selected for the assessment run.

      - *(string) --*

    - **userAttributesForFindings** *(list) --*

      The user-defined attributes that are assigned to every generated finding.

      - *(dict) --*

        This data type is used as a request parameter in the  AddAttributesToFindings and
        CreateAssessmentTemplate actions.

        - **key** *(string) --*

          The attribute key.

        - **value** *(string) --*

          The value assigned to the attribute key.

    - **createdAt** *(datetime) --*

      The time when  StartAssessmentRun was called.

    - **startedAt** *(datetime) --*

      The time when  StartAssessmentRun was called.

    - **completedAt** *(datetime) --*

      The assessment run completion time that corresponds to the rules packages evaluation
      completion time or failure.

    - **stateChangedAt** *(datetime) --*

      The last time when the assessment run's state changed.

    - **dataCollected** *(boolean) --*

      A Boolean value (true or false) that specifies whether the process of collecting data
      from the agents is completed.

    - **stateChanges** *(list) --*

      A list of the assessment run state changes.

      - *(dict) --*

        Used as one of the elements of the  AssessmentRun data type.

        - **stateChangedAt** *(datetime) --*

          The last time the assessment run state changed.

        - **state** *(string) --*

          The assessment run state.

    - **notifications** *(list) --*

      A list of notifications for the event subscriptions. A notification about a particular
      generated finding is added to this list only once.

      - *(dict) --*

        Used as one of the elements of the  AssessmentRun data type.

        - **date** *(datetime) --*

          The date of the notification.

        - **event** *(string) --*

          The event for which a notification is sent.

        - **message** *(string) --*

          The message included in the notification.

        - **error** *(boolean) --*

          The Boolean value that specifies whether the notification represents an error.

        - **snsTopicArn** *(string) --*

          The SNS topic to which the SNS notification is sent.

        - **snsPublishStatusCode** *(string) --*

          The status code of the SNS notification.

    - **findingCounts** *(dict) --*

      Provides a total count of generated findings per severity.

      - *(string) --*

        - *(integer) --*
    """


_ClientDescribeAssessmentRunsResponsefailedItemsTypeDef = TypedDict(
    "_ClientDescribeAssessmentRunsResponsefailedItemsTypeDef",
    {"failureCode": str, "retryable": bool},
    total=False,
)


class ClientDescribeAssessmentRunsResponsefailedItemsTypeDef(
    _ClientDescribeAssessmentRunsResponsefailedItemsTypeDef
):
    """
    Type definition for `ClientDescribeAssessmentRunsResponse` `failedItems`

    Includes details about the failed items.

    - **failureCode** *(string) --*

      The status code of a failed item.

    - **retryable** *(boolean) --*

      Indicates whether you can immediately retry a request for this item for a specified
      resource.
    """


_ClientDescribeAssessmentRunsResponseTypeDef = TypedDict(
    "_ClientDescribeAssessmentRunsResponseTypeDef",
    {
        "assessmentRuns": List[
            ClientDescribeAssessmentRunsResponseassessmentRunsTypeDef
        ],
        "failedItems": Dict[
            str, ClientDescribeAssessmentRunsResponsefailedItemsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeAssessmentRunsResponseTypeDef(
    _ClientDescribeAssessmentRunsResponseTypeDef
):
    """
    Type definition for `ClientDescribeAssessmentRuns` `Response`

    - **assessmentRuns** *(list) --*

      Information about the assessment run.

      - *(dict) --*

        A snapshot of an Amazon Inspector assessment run that contains the findings of the
        assessment run .

        Used as the response element in the  DescribeAssessmentRuns action.

        - **arn** *(string) --*

          The ARN of the assessment run.

        - **name** *(string) --*

          The auto-generated name for the assessment run.

        - **assessmentTemplateArn** *(string) --*

          The ARN of the assessment template that is associated with the assessment run.

        - **state** *(string) --*

          The state of the assessment run.

        - **durationInSeconds** *(integer) --*

          The duration of the assessment run.

        - **rulesPackageArns** *(list) --*

          The rules packages selected for the assessment run.

          - *(string) --*

        - **userAttributesForFindings** *(list) --*

          The user-defined attributes that are assigned to every generated finding.

          - *(dict) --*

            This data type is used as a request parameter in the  AddAttributesToFindings and
            CreateAssessmentTemplate actions.

            - **key** *(string) --*

              The attribute key.

            - **value** *(string) --*

              The value assigned to the attribute key.

        - **createdAt** *(datetime) --*

          The time when  StartAssessmentRun was called.

        - **startedAt** *(datetime) --*

          The time when  StartAssessmentRun was called.

        - **completedAt** *(datetime) --*

          The assessment run completion time that corresponds to the rules packages evaluation
          completion time or failure.

        - **stateChangedAt** *(datetime) --*

          The last time when the assessment run's state changed.

        - **dataCollected** *(boolean) --*

          A Boolean value (true or false) that specifies whether the process of collecting data
          from the agents is completed.

        - **stateChanges** *(list) --*

          A list of the assessment run state changes.

          - *(dict) --*

            Used as one of the elements of the  AssessmentRun data type.

            - **stateChangedAt** *(datetime) --*

              The last time the assessment run state changed.

            - **state** *(string) --*

              The assessment run state.

        - **notifications** *(list) --*

          A list of notifications for the event subscriptions. A notification about a particular
          generated finding is added to this list only once.

          - *(dict) --*

            Used as one of the elements of the  AssessmentRun data type.

            - **date** *(datetime) --*

              The date of the notification.

            - **event** *(string) --*

              The event for which a notification is sent.

            - **message** *(string) --*

              The message included in the notification.

            - **error** *(boolean) --*

              The Boolean value that specifies whether the notification represents an error.

            - **snsTopicArn** *(string) --*

              The SNS topic to which the SNS notification is sent.

            - **snsPublishStatusCode** *(string) --*

              The status code of the SNS notification.

        - **findingCounts** *(dict) --*

          Provides a total count of generated findings per severity.

          - *(string) --*

            - *(integer) --*

    - **failedItems** *(dict) --*

      Assessment run details that cannot be described. An error code is provided for each failed
      item.

      - *(string) --*

        - *(dict) --*

          Includes details about the failed items.

          - **failureCode** *(string) --*

            The status code of a failed item.

          - **retryable** *(boolean) --*

            Indicates whether you can immediately retry a request for this item for a specified
            resource.
    """


_ClientDescribeAssessmentTargetsResponseassessmentTargetsTypeDef = TypedDict(
    "_ClientDescribeAssessmentTargetsResponseassessmentTargetsTypeDef",
    {
        "arn": str,
        "name": str,
        "resourceGroupArn": str,
        "createdAt": datetime,
        "updatedAt": datetime,
    },
    total=False,
)


class ClientDescribeAssessmentTargetsResponseassessmentTargetsTypeDef(
    _ClientDescribeAssessmentTargetsResponseassessmentTargetsTypeDef
):
    """
    Type definition for `ClientDescribeAssessmentTargetsResponse` `assessmentTargets`

    Contains information about an Amazon Inspector application. This data type is used as the
    response element in the  DescribeAssessmentTargets action.

    - **arn** *(string) --*

      The ARN that specifies the Amazon Inspector assessment target.

    - **name** *(string) --*

      The name of the Amazon Inspector assessment target.

    - **resourceGroupArn** *(string) --*

      The ARN that specifies the resource group that is associated with the assessment target.

    - **createdAt** *(datetime) --*

      The time at which the assessment target is created.

    - **updatedAt** *(datetime) --*

      The time at which  UpdateAssessmentTarget is called.
    """


_ClientDescribeAssessmentTargetsResponsefailedItemsTypeDef = TypedDict(
    "_ClientDescribeAssessmentTargetsResponsefailedItemsTypeDef",
    {"failureCode": str, "retryable": bool},
    total=False,
)


class ClientDescribeAssessmentTargetsResponsefailedItemsTypeDef(
    _ClientDescribeAssessmentTargetsResponsefailedItemsTypeDef
):
    """
    Type definition for `ClientDescribeAssessmentTargetsResponse` `failedItems`

    Includes details about the failed items.

    - **failureCode** *(string) --*

      The status code of a failed item.

    - **retryable** *(boolean) --*

      Indicates whether you can immediately retry a request for this item for a specified
      resource.
    """


_ClientDescribeAssessmentTargetsResponseTypeDef = TypedDict(
    "_ClientDescribeAssessmentTargetsResponseTypeDef",
    {
        "assessmentTargets": List[
            ClientDescribeAssessmentTargetsResponseassessmentTargetsTypeDef
        ],
        "failedItems": Dict[
            str, ClientDescribeAssessmentTargetsResponsefailedItemsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeAssessmentTargetsResponseTypeDef(
    _ClientDescribeAssessmentTargetsResponseTypeDef
):
    """
    Type definition for `ClientDescribeAssessmentTargets` `Response`

    - **assessmentTargets** *(list) --*

      Information about the assessment targets.

      - *(dict) --*

        Contains information about an Amazon Inspector application. This data type is used as the
        response element in the  DescribeAssessmentTargets action.

        - **arn** *(string) --*

          The ARN that specifies the Amazon Inspector assessment target.

        - **name** *(string) --*

          The name of the Amazon Inspector assessment target.

        - **resourceGroupArn** *(string) --*

          The ARN that specifies the resource group that is associated with the assessment target.

        - **createdAt** *(datetime) --*

          The time at which the assessment target is created.

        - **updatedAt** *(datetime) --*

          The time at which  UpdateAssessmentTarget is called.

    - **failedItems** *(dict) --*

      Assessment target details that cannot be described. An error code is provided for each failed
      item.

      - *(string) --*

        - *(dict) --*

          Includes details about the failed items.

          - **failureCode** *(string) --*

            The status code of a failed item.

          - **retryable** *(boolean) --*

            Indicates whether you can immediately retry a request for this item for a specified
            resource.
    """


_ClientDescribeAssessmentTemplatesResponseassessmentTemplatesuserAttributesForFindingsTypeDef = TypedDict(
    "_ClientDescribeAssessmentTemplatesResponseassessmentTemplatesuserAttributesForFindingsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribeAssessmentTemplatesResponseassessmentTemplatesuserAttributesForFindingsTypeDef(
    _ClientDescribeAssessmentTemplatesResponseassessmentTemplatesuserAttributesForFindingsTypeDef
):
    """
    Type definition for `ClientDescribeAssessmentTemplatesResponseassessmentTemplates` `userAttributesForFindings`

    This data type is used as a request parameter in the  AddAttributesToFindings and
    CreateAssessmentTemplate actions.

    - **key** *(string) --*

      The attribute key.

    - **value** *(string) --*

      The value assigned to the attribute key.
    """


_ClientDescribeAssessmentTemplatesResponseassessmentTemplatesTypeDef = TypedDict(
    "_ClientDescribeAssessmentTemplatesResponseassessmentTemplatesTypeDef",
    {
        "arn": str,
        "name": str,
        "assessmentTargetArn": str,
        "durationInSeconds": int,
        "rulesPackageArns": List[str],
        "userAttributesForFindings": List[
            ClientDescribeAssessmentTemplatesResponseassessmentTemplatesuserAttributesForFindingsTypeDef
        ],
        "lastAssessmentRunArn": str,
        "assessmentRunCount": int,
        "createdAt": datetime,
    },
    total=False,
)


class ClientDescribeAssessmentTemplatesResponseassessmentTemplatesTypeDef(
    _ClientDescribeAssessmentTemplatesResponseassessmentTemplatesTypeDef
):
    """
    Type definition for `ClientDescribeAssessmentTemplatesResponse` `assessmentTemplates`

    Contains information about an Amazon Inspector assessment template. This data type is used
    as the response element in the  DescribeAssessmentTemplates action.

    - **arn** *(string) --*

      The ARN of the assessment template.

    - **name** *(string) --*

      The name of the assessment template.

    - **assessmentTargetArn** *(string) --*

      The ARN of the assessment target that corresponds to this assessment template.

    - **durationInSeconds** *(integer) --*

      The duration in seconds specified for this assessment template. The default value is 3600
      seconds (one hour). The maximum value is 86400 seconds (one day).

    - **rulesPackageArns** *(list) --*

      The rules packages that are specified for this assessment template.

      - *(string) --*

    - **userAttributesForFindings** *(list) --*

      The user-defined attributes that are assigned to every generated finding from the
      assessment run that uses this assessment template.

      - *(dict) --*

        This data type is used as a request parameter in the  AddAttributesToFindings and
        CreateAssessmentTemplate actions.

        - **key** *(string) --*

          The attribute key.

        - **value** *(string) --*

          The value assigned to the attribute key.

    - **lastAssessmentRunArn** *(string) --*

      The Amazon Resource Name (ARN) of the most recent assessment run associated with this
      assessment template. This value exists only when the value of assessmentRunCount is
      greaterpa than zero.

    - **assessmentRunCount** *(integer) --*

      The number of existing assessment runs associated with this assessment template. This
      value can be zero or a positive integer.

    - **createdAt** *(datetime) --*

      The time at which the assessment template is created.
    """


_ClientDescribeAssessmentTemplatesResponsefailedItemsTypeDef = TypedDict(
    "_ClientDescribeAssessmentTemplatesResponsefailedItemsTypeDef",
    {"failureCode": str, "retryable": bool},
    total=False,
)


class ClientDescribeAssessmentTemplatesResponsefailedItemsTypeDef(
    _ClientDescribeAssessmentTemplatesResponsefailedItemsTypeDef
):
    """
    Type definition for `ClientDescribeAssessmentTemplatesResponse` `failedItems`

    Includes details about the failed items.

    - **failureCode** *(string) --*

      The status code of a failed item.

    - **retryable** *(boolean) --*

      Indicates whether you can immediately retry a request for this item for a specified
      resource.
    """


_ClientDescribeAssessmentTemplatesResponseTypeDef = TypedDict(
    "_ClientDescribeAssessmentTemplatesResponseTypeDef",
    {
        "assessmentTemplates": List[
            ClientDescribeAssessmentTemplatesResponseassessmentTemplatesTypeDef
        ],
        "failedItems": Dict[
            str, ClientDescribeAssessmentTemplatesResponsefailedItemsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeAssessmentTemplatesResponseTypeDef(
    _ClientDescribeAssessmentTemplatesResponseTypeDef
):
    """
    Type definition for `ClientDescribeAssessmentTemplates` `Response`

    - **assessmentTemplates** *(list) --*

      Information about the assessment templates.

      - *(dict) --*

        Contains information about an Amazon Inspector assessment template. This data type is used
        as the response element in the  DescribeAssessmentTemplates action.

        - **arn** *(string) --*

          The ARN of the assessment template.

        - **name** *(string) --*

          The name of the assessment template.

        - **assessmentTargetArn** *(string) --*

          The ARN of the assessment target that corresponds to this assessment template.

        - **durationInSeconds** *(integer) --*

          The duration in seconds specified for this assessment template. The default value is 3600
          seconds (one hour). The maximum value is 86400 seconds (one day).

        - **rulesPackageArns** *(list) --*

          The rules packages that are specified for this assessment template.

          - *(string) --*

        - **userAttributesForFindings** *(list) --*

          The user-defined attributes that are assigned to every generated finding from the
          assessment run that uses this assessment template.

          - *(dict) --*

            This data type is used as a request parameter in the  AddAttributesToFindings and
            CreateAssessmentTemplate actions.

            - **key** *(string) --*

              The attribute key.

            - **value** *(string) --*

              The value assigned to the attribute key.

        - **lastAssessmentRunArn** *(string) --*

          The Amazon Resource Name (ARN) of the most recent assessment run associated with this
          assessment template. This value exists only when the value of assessmentRunCount is
          greaterpa than zero.

        - **assessmentRunCount** *(integer) --*

          The number of existing assessment runs associated with this assessment template. This
          value can be zero or a positive integer.

        - **createdAt** *(datetime) --*

          The time at which the assessment template is created.

    - **failedItems** *(dict) --*

      Assessment template details that cannot be described. An error code is provided for each
      failed item.

      - *(string) --*

        - *(dict) --*

          Includes details about the failed items.

          - **failureCode** *(string) --*

            The status code of a failed item.

          - **retryable** *(boolean) --*

            Indicates whether you can immediately retry a request for this item for a specified
            resource.
    """


_ClientDescribeCrossAccountAccessRoleResponseTypeDef = TypedDict(
    "_ClientDescribeCrossAccountAccessRoleResponseTypeDef",
    {"roleArn": str, "valid": bool, "registeredAt": datetime},
    total=False,
)


class ClientDescribeCrossAccountAccessRoleResponseTypeDef(
    _ClientDescribeCrossAccountAccessRoleResponseTypeDef
):
    """
    Type definition for `ClientDescribeCrossAccountAccessRole` `Response`

    - **roleArn** *(string) --*

      The ARN that specifies the IAM role that Amazon Inspector uses to access your AWS account.

    - **valid** *(boolean) --*

      A Boolean value that specifies whether the IAM role has the necessary policies attached to
      enable Amazon Inspector to access your AWS account.

    - **registeredAt** *(datetime) --*

      The date when the cross-account access role was registered.
    """


_ClientDescribeExclusionsResponseexclusionsattributesTypeDef = TypedDict(
    "_ClientDescribeExclusionsResponseexclusionsattributesTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribeExclusionsResponseexclusionsattributesTypeDef(
    _ClientDescribeExclusionsResponseexclusionsattributesTypeDef
):
    """
    Type definition for `ClientDescribeExclusionsResponseexclusions` `attributes`

    This data type is used as a request parameter in the  AddAttributesToFindings and
    CreateAssessmentTemplate actions.

    - **key** *(string) --*

      The attribute key.

    - **value** *(string) --*

      The value assigned to the attribute key.
    """


_ClientDescribeExclusionsResponseexclusionsscopesTypeDef = TypedDict(
    "_ClientDescribeExclusionsResponseexclusionsscopesTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribeExclusionsResponseexclusionsscopesTypeDef(
    _ClientDescribeExclusionsResponseexclusionsscopesTypeDef
):
    """
    Type definition for `ClientDescribeExclusionsResponseexclusions` `scopes`

    This data type contains key-value pairs that identify various Amazon resources.

    - **key** *(string) --*

      The type of the scope.

    - **value** *(string) --*

      The resource identifier for the specified scope type.
    """


_ClientDescribeExclusionsResponseexclusionsTypeDef = TypedDict(
    "_ClientDescribeExclusionsResponseexclusionsTypeDef",
    {
        "arn": str,
        "title": str,
        "description": str,
        "recommendation": str,
        "scopes": List[ClientDescribeExclusionsResponseexclusionsscopesTypeDef],
        "attributes": List[ClientDescribeExclusionsResponseexclusionsattributesTypeDef],
    },
    total=False,
)


class ClientDescribeExclusionsResponseexclusionsTypeDef(
    _ClientDescribeExclusionsResponseexclusionsTypeDef
):
    """
    Type definition for `ClientDescribeExclusionsResponse` `exclusions`

    Contains information about what was excluded from an assessment run.

    - **arn** *(string) --*

      The ARN that specifies the exclusion.

    - **title** *(string) --*

      The name of the exclusion.

    - **description** *(string) --*

      The description of the exclusion.

    - **recommendation** *(string) --*

      The recommendation for the exclusion.

    - **scopes** *(list) --*

      The AWS resources for which the exclusion pertains.

      - *(dict) --*

        This data type contains key-value pairs that identify various Amazon resources.

        - **key** *(string) --*

          The type of the scope.

        - **value** *(string) --*

          The resource identifier for the specified scope type.

    - **attributes** *(list) --*

      The system-defined attributes for the exclusion.

      - *(dict) --*

        This data type is used as a request parameter in the  AddAttributesToFindings and
        CreateAssessmentTemplate actions.

        - **key** *(string) --*

          The attribute key.

        - **value** *(string) --*

          The value assigned to the attribute key.
    """


_ClientDescribeExclusionsResponsefailedItemsTypeDef = TypedDict(
    "_ClientDescribeExclusionsResponsefailedItemsTypeDef",
    {"failureCode": str, "retryable": bool},
    total=False,
)


class ClientDescribeExclusionsResponsefailedItemsTypeDef(
    _ClientDescribeExclusionsResponsefailedItemsTypeDef
):
    """
    Type definition for `ClientDescribeExclusionsResponse` `failedItems`

    Includes details about the failed items.

    - **failureCode** *(string) --*

      The status code of a failed item.

    - **retryable** *(boolean) --*

      Indicates whether you can immediately retry a request for this item for a specified
      resource.
    """


_ClientDescribeExclusionsResponseTypeDef = TypedDict(
    "_ClientDescribeExclusionsResponseTypeDef",
    {
        "exclusions": Dict[str, ClientDescribeExclusionsResponseexclusionsTypeDef],
        "failedItems": Dict[str, ClientDescribeExclusionsResponsefailedItemsTypeDef],
    },
    total=False,
)


class ClientDescribeExclusionsResponseTypeDef(_ClientDescribeExclusionsResponseTypeDef):
    """
    Type definition for `ClientDescribeExclusions` `Response`

    - **exclusions** *(dict) --*

      Information about the exclusions.

      - *(string) --*

        - *(dict) --*

          Contains information about what was excluded from an assessment run.

          - **arn** *(string) --*

            The ARN that specifies the exclusion.

          - **title** *(string) --*

            The name of the exclusion.

          - **description** *(string) --*

            The description of the exclusion.

          - **recommendation** *(string) --*

            The recommendation for the exclusion.

          - **scopes** *(list) --*

            The AWS resources for which the exclusion pertains.

            - *(dict) --*

              This data type contains key-value pairs that identify various Amazon resources.

              - **key** *(string) --*

                The type of the scope.

              - **value** *(string) --*

                The resource identifier for the specified scope type.

          - **attributes** *(list) --*

            The system-defined attributes for the exclusion.

            - *(dict) --*

              This data type is used as a request parameter in the  AddAttributesToFindings and
              CreateAssessmentTemplate actions.

              - **key** *(string) --*

                The attribute key.

              - **value** *(string) --*

                The value assigned to the attribute key.

    - **failedItems** *(dict) --*

      Exclusion details that cannot be described. An error code is provided for each failed item.

      - *(string) --*

        - *(dict) --*

          Includes details about the failed items.

          - **failureCode** *(string) --*

            The status code of a failed item.

          - **retryable** *(boolean) --*

            Indicates whether you can immediately retry a request for this item for a specified
            resource.
    """


_ClientDescribeFindingsResponsefailedItemsTypeDef = TypedDict(
    "_ClientDescribeFindingsResponsefailedItemsTypeDef",
    {"failureCode": str, "retryable": bool},
    total=False,
)


class ClientDescribeFindingsResponsefailedItemsTypeDef(
    _ClientDescribeFindingsResponsefailedItemsTypeDef
):
    """
    Type definition for `ClientDescribeFindingsResponse` `failedItems`

    Includes details about the failed items.

    - **failureCode** *(string) --*

      The status code of a failed item.

    - **retryable** *(boolean) --*

      Indicates whether you can immediately retry a request for this item for a specified
      resource.
    """


_ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacesprivateIpAddressesTypeDef = TypedDict(
    "_ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacesprivateIpAddressesTypeDef",
    {"privateDnsName": str, "privateIpAddress": str},
    total=False,
)


class ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacesprivateIpAddressesTypeDef(
    _ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacesprivateIpAddressesTypeDef
):
    """
    Type definition for `ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfaces` `privateIpAddresses`

    Contains information about a private IP address associated with a network
    interface. This data type is used as a response element in the  DescribeFindings
    action.

    - **privateDnsName** *(string) --*

      The DNS name of the private IP address.

    - **privateIpAddress** *(string) --*

      The full IP address of the network inteface.
    """


_ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacessecurityGroupsTypeDef = TypedDict(
    "_ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacessecurityGroupsTypeDef",
    {"groupName": str, "groupId": str},
    total=False,
)


class ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacessecurityGroupsTypeDef(
    _ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacessecurityGroupsTypeDef
):
    """
    Type definition for `ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfaces` `securityGroups`

    Contains information about a security group associated with a network interface.
    This data type is used as one of the elements of the  NetworkInterface data type.

    - **groupName** *(string) --*

      The name of the security group.

    - **groupId** *(string) --*

      The ID of the security group.
    """


_ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacesTypeDef = TypedDict(
    "_ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacesTypeDef",
    {
        "networkInterfaceId": str,
        "subnetId": str,
        "vpcId": str,
        "privateDnsName": str,
        "privateIpAddress": str,
        "privateIpAddresses": List[
            ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacesprivateIpAddressesTypeDef
        ],
        "publicDnsName": str,
        "publicIp": str,
        "ipv6Addresses": List[str],
        "securityGroups": List[
            ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacessecurityGroupsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacesTypeDef(
    _ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacesTypeDef
):
    """
    Type definition for `ClientDescribeFindingsResponsefindingsassetAttributes` `networkInterfaces`

    Contains information about the network interfaces interacting with an EC2 instance.
    This data type is used as one of the elements of the  AssetAttributes data type.

    - **networkInterfaceId** *(string) --*

      The ID of the network interface.

    - **subnetId** *(string) --*

      The ID of a subnet associated with the network interface.

    - **vpcId** *(string) --*

      The ID of a VPC associated with the network interface.

    - **privateDnsName** *(string) --*

      The name of a private DNS associated with the network interface.

    - **privateIpAddress** *(string) --*

      The private IP address associated with the network interface.

    - **privateIpAddresses** *(list) --*

      A list of the private IP addresses associated with the network interface. Includes
      the privateDnsName and privateIpAddress.

      - *(dict) --*

        Contains information about a private IP address associated with a network
        interface. This data type is used as a response element in the  DescribeFindings
        action.

        - **privateDnsName** *(string) --*

          The DNS name of the private IP address.

        - **privateIpAddress** *(string) --*

          The full IP address of the network inteface.

    - **publicDnsName** *(string) --*

      The name of a public DNS associated with the network interface.

    - **publicIp** *(string) --*

      The public IP address from which the network interface is reachable.

    - **ipv6Addresses** *(list) --*

      The IP addresses associated with the network interface.

      - *(string) --*

    - **securityGroups** *(list) --*

      A list of the security groups associated with the network interface. Includes the
      groupId and groupName.

      - *(dict) --*

        Contains information about a security group associated with a network interface.
        This data type is used as one of the elements of the  NetworkInterface data type.

        - **groupName** *(string) --*

          The name of the security group.

        - **groupId** *(string) --*

          The ID of the security group.
    """


_ClientDescribeFindingsResponsefindingsassetAttributestagsTypeDef = TypedDict(
    "_ClientDescribeFindingsResponsefindingsassetAttributestagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribeFindingsResponsefindingsassetAttributestagsTypeDef(
    _ClientDescribeFindingsResponsefindingsassetAttributestagsTypeDef
):
    """
    Type definition for `ClientDescribeFindingsResponsefindingsassetAttributes` `tags`

    A key and value pair. This data type is used as a request parameter in the
    SetTagsForResource action and a response element in the  ListTagsForResource action.

    - **key** *(string) --*

      A tag key.

    - **value** *(string) --*

      A value assigned to a tag key.
    """


_ClientDescribeFindingsResponsefindingsassetAttributesTypeDef = TypedDict(
    "_ClientDescribeFindingsResponsefindingsassetAttributesTypeDef",
    {
        "schemaVersion": int,
        "agentId": str,
        "autoScalingGroup": str,
        "amiId": str,
        "hostname": str,
        "ipv4Addresses": List[str],
        "tags": List[ClientDescribeFindingsResponsefindingsassetAttributestagsTypeDef],
        "networkInterfaces": List[
            ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeFindingsResponsefindingsassetAttributesTypeDef(
    _ClientDescribeFindingsResponsefindingsassetAttributesTypeDef
):
    """
    Type definition for `ClientDescribeFindingsResponsefindings` `assetAttributes`

    A collection of attributes of the host from which the finding is generated.

    - **schemaVersion** *(integer) --*

      The schema version of this data type.

    - **agentId** *(string) --*

      The ID of the agent that is installed on the EC2 instance where the finding is
      generated.

    - **autoScalingGroup** *(string) --*

      The Auto Scaling group of the EC2 instance where the finding is generated.

    - **amiId** *(string) --*

      The ID of the Amazon Machine Image (AMI) that is installed on the EC2 instance where
      the finding is generated.

    - **hostname** *(string) --*

      The hostname of the EC2 instance where the finding is generated.

    - **ipv4Addresses** *(list) --*

      The list of IP v4 addresses of the EC2 instance where the finding is generated.

      - *(string) --*

    - **tags** *(list) --*

      The tags related to the EC2 instance where the finding is generated.

      - *(dict) --*

        A key and value pair. This data type is used as a request parameter in the
        SetTagsForResource action and a response element in the  ListTagsForResource action.

        - **key** *(string) --*

          A tag key.

        - **value** *(string) --*

          A value assigned to a tag key.

    - **networkInterfaces** *(list) --*

      An array of the network interfaces interacting with the EC2 instance where the finding
      is generated.

      - *(dict) --*

        Contains information about the network interfaces interacting with an EC2 instance.
        This data type is used as one of the elements of the  AssetAttributes data type.

        - **networkInterfaceId** *(string) --*

          The ID of the network interface.

        - **subnetId** *(string) --*

          The ID of a subnet associated with the network interface.

        - **vpcId** *(string) --*

          The ID of a VPC associated with the network interface.

        - **privateDnsName** *(string) --*

          The name of a private DNS associated with the network interface.

        - **privateIpAddress** *(string) --*

          The private IP address associated with the network interface.

        - **privateIpAddresses** *(list) --*

          A list of the private IP addresses associated with the network interface. Includes
          the privateDnsName and privateIpAddress.

          - *(dict) --*

            Contains information about a private IP address associated with a network
            interface. This data type is used as a response element in the  DescribeFindings
            action.

            - **privateDnsName** *(string) --*

              The DNS name of the private IP address.

            - **privateIpAddress** *(string) --*

              The full IP address of the network inteface.

        - **publicDnsName** *(string) --*

          The name of a public DNS associated with the network interface.

        - **publicIp** *(string) --*

          The public IP address from which the network interface is reachable.

        - **ipv6Addresses** *(list) --*

          The IP addresses associated with the network interface.

          - *(string) --*

        - **securityGroups** *(list) --*

          A list of the security groups associated with the network interface. Includes the
          groupId and groupName.

          - *(dict) --*

            Contains information about a security group associated with a network interface.
            This data type is used as one of the elements of the  NetworkInterface data type.

            - **groupName** *(string) --*

              The name of the security group.

            - **groupId** *(string) --*

              The ID of the security group.
    """


_ClientDescribeFindingsResponsefindingsattributesTypeDef = TypedDict(
    "_ClientDescribeFindingsResponsefindingsattributesTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribeFindingsResponsefindingsattributesTypeDef(
    _ClientDescribeFindingsResponsefindingsattributesTypeDef
):
    """
    Type definition for `ClientDescribeFindingsResponsefindings` `attributes`

    This data type is used as a request parameter in the  AddAttributesToFindings and
    CreateAssessmentTemplate actions.

    - **key** *(string) --*

      The attribute key.

    - **value** *(string) --*

      The value assigned to the attribute key.
    """


_ClientDescribeFindingsResponsefindingsserviceAttributesTypeDef = TypedDict(
    "_ClientDescribeFindingsResponsefindingsserviceAttributesTypeDef",
    {"schemaVersion": int, "assessmentRunArn": str, "rulesPackageArn": str},
    total=False,
)


class ClientDescribeFindingsResponsefindingsserviceAttributesTypeDef(
    _ClientDescribeFindingsResponsefindingsserviceAttributesTypeDef
):
    """
    Type definition for `ClientDescribeFindingsResponsefindings` `serviceAttributes`

    This data type is used in the  Finding data type.

    - **schemaVersion** *(integer) --*

      The schema version of this data type.

    - **assessmentRunArn** *(string) --*

      The ARN of the assessment run during which the finding is generated.

    - **rulesPackageArn** *(string) --*

      The ARN of the rules package that is used to generate the finding.
    """


_ClientDescribeFindingsResponsefindingsuserAttributesTypeDef = TypedDict(
    "_ClientDescribeFindingsResponsefindingsuserAttributesTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribeFindingsResponsefindingsuserAttributesTypeDef(
    _ClientDescribeFindingsResponsefindingsuserAttributesTypeDef
):
    """
    Type definition for `ClientDescribeFindingsResponsefindings` `userAttributes`

    This data type is used as a request parameter in the  AddAttributesToFindings and
    CreateAssessmentTemplate actions.

    - **key** *(string) --*

      The attribute key.

    - **value** *(string) --*

      The value assigned to the attribute key.
    """


_ClientDescribeFindingsResponsefindingsTypeDef = TypedDict(
    "_ClientDescribeFindingsResponsefindingsTypeDef",
    {
        "arn": str,
        "schemaVersion": int,
        "service": str,
        "serviceAttributes": ClientDescribeFindingsResponsefindingsserviceAttributesTypeDef,
        "assetType": str,
        "assetAttributes": ClientDescribeFindingsResponsefindingsassetAttributesTypeDef,
        "id": str,
        "title": str,
        "description": str,
        "recommendation": str,
        "severity": str,
        "numericSeverity": float,
        "confidence": int,
        "indicatorOfCompromise": bool,
        "attributes": List[ClientDescribeFindingsResponsefindingsattributesTypeDef],
        "userAttributes": List[
            ClientDescribeFindingsResponsefindingsuserAttributesTypeDef
        ],
        "createdAt": datetime,
        "updatedAt": datetime,
    },
    total=False,
)


class ClientDescribeFindingsResponsefindingsTypeDef(
    _ClientDescribeFindingsResponsefindingsTypeDef
):
    """
    Type definition for `ClientDescribeFindingsResponse` `findings`

    Contains information about an Amazon Inspector finding. This data type is used as the
    response element in the  DescribeFindings action.

    - **arn** *(string) --*

      The ARN that specifies the finding.

    - **schemaVersion** *(integer) --*

      The schema version of this data type.

    - **service** *(string) --*

      The data element is set to "Inspector".

    - **serviceAttributes** *(dict) --*

      This data type is used in the  Finding data type.

      - **schemaVersion** *(integer) --*

        The schema version of this data type.

      - **assessmentRunArn** *(string) --*

        The ARN of the assessment run during which the finding is generated.

      - **rulesPackageArn** *(string) --*

        The ARN of the rules package that is used to generate the finding.

    - **assetType** *(string) --*

      The type of the host from which the finding is generated.

    - **assetAttributes** *(dict) --*

      A collection of attributes of the host from which the finding is generated.

      - **schemaVersion** *(integer) --*

        The schema version of this data type.

      - **agentId** *(string) --*

        The ID of the agent that is installed on the EC2 instance where the finding is
        generated.

      - **autoScalingGroup** *(string) --*

        The Auto Scaling group of the EC2 instance where the finding is generated.

      - **amiId** *(string) --*

        The ID of the Amazon Machine Image (AMI) that is installed on the EC2 instance where
        the finding is generated.

      - **hostname** *(string) --*

        The hostname of the EC2 instance where the finding is generated.

      - **ipv4Addresses** *(list) --*

        The list of IP v4 addresses of the EC2 instance where the finding is generated.

        - *(string) --*

      - **tags** *(list) --*

        The tags related to the EC2 instance where the finding is generated.

        - *(dict) --*

          A key and value pair. This data type is used as a request parameter in the
          SetTagsForResource action and a response element in the  ListTagsForResource action.

          - **key** *(string) --*

            A tag key.

          - **value** *(string) --*

            A value assigned to a tag key.

      - **networkInterfaces** *(list) --*

        An array of the network interfaces interacting with the EC2 instance where the finding
        is generated.

        - *(dict) --*

          Contains information about the network interfaces interacting with an EC2 instance.
          This data type is used as one of the elements of the  AssetAttributes data type.

          - **networkInterfaceId** *(string) --*

            The ID of the network interface.

          - **subnetId** *(string) --*

            The ID of a subnet associated with the network interface.

          - **vpcId** *(string) --*

            The ID of a VPC associated with the network interface.

          - **privateDnsName** *(string) --*

            The name of a private DNS associated with the network interface.

          - **privateIpAddress** *(string) --*

            The private IP address associated with the network interface.

          - **privateIpAddresses** *(list) --*

            A list of the private IP addresses associated with the network interface. Includes
            the privateDnsName and privateIpAddress.

            - *(dict) --*

              Contains information about a private IP address associated with a network
              interface. This data type is used as a response element in the  DescribeFindings
              action.

              - **privateDnsName** *(string) --*

                The DNS name of the private IP address.

              - **privateIpAddress** *(string) --*

                The full IP address of the network inteface.

          - **publicDnsName** *(string) --*

            The name of a public DNS associated with the network interface.

          - **publicIp** *(string) --*

            The public IP address from which the network interface is reachable.

          - **ipv6Addresses** *(list) --*

            The IP addresses associated with the network interface.

            - *(string) --*

          - **securityGroups** *(list) --*

            A list of the security groups associated with the network interface. Includes the
            groupId and groupName.

            - *(dict) --*

              Contains information about a security group associated with a network interface.
              This data type is used as one of the elements of the  NetworkInterface data type.

              - **groupName** *(string) --*

                The name of the security group.

              - **groupId** *(string) --*

                The ID of the security group.

    - **id** *(string) --*

      The ID of the finding.

    - **title** *(string) --*

      The name of the finding.

    - **description** *(string) --*

      The description of the finding.

    - **recommendation** *(string) --*

      The recommendation for the finding.

    - **severity** *(string) --*

      The finding severity. Values can be set to High, Medium, Low, and Informational.

    - **numericSeverity** *(float) --*

      The numeric value of the finding severity.

    - **confidence** *(integer) --*

      This data element is currently not used.

    - **indicatorOfCompromise** *(boolean) --*

      This data element is currently not used.

    - **attributes** *(list) --*

      The system-defined attributes for the finding.

      - *(dict) --*

        This data type is used as a request parameter in the  AddAttributesToFindings and
        CreateAssessmentTemplate actions.

        - **key** *(string) --*

          The attribute key.

        - **value** *(string) --*

          The value assigned to the attribute key.

    - **userAttributes** *(list) --*

      The user-defined attributes that are assigned to the finding.

      - *(dict) --*

        This data type is used as a request parameter in the  AddAttributesToFindings and
        CreateAssessmentTemplate actions.

        - **key** *(string) --*

          The attribute key.

        - **value** *(string) --*

          The value assigned to the attribute key.

    - **createdAt** *(datetime) --*

      The time when the finding was generated.

    - **updatedAt** *(datetime) --*

      The time when  AddAttributesToFindings is called.
    """


_ClientDescribeFindingsResponseTypeDef = TypedDict(
    "_ClientDescribeFindingsResponseTypeDef",
    {
        "findings": List[ClientDescribeFindingsResponsefindingsTypeDef],
        "failedItems": Dict[str, ClientDescribeFindingsResponsefailedItemsTypeDef],
    },
    total=False,
)


class ClientDescribeFindingsResponseTypeDef(_ClientDescribeFindingsResponseTypeDef):
    """
    Type definition for `ClientDescribeFindings` `Response`

    - **findings** *(list) --*

      Information about the finding.

      - *(dict) --*

        Contains information about an Amazon Inspector finding. This data type is used as the
        response element in the  DescribeFindings action.

        - **arn** *(string) --*

          The ARN that specifies the finding.

        - **schemaVersion** *(integer) --*

          The schema version of this data type.

        - **service** *(string) --*

          The data element is set to "Inspector".

        - **serviceAttributes** *(dict) --*

          This data type is used in the  Finding data type.

          - **schemaVersion** *(integer) --*

            The schema version of this data type.

          - **assessmentRunArn** *(string) --*

            The ARN of the assessment run during which the finding is generated.

          - **rulesPackageArn** *(string) --*

            The ARN of the rules package that is used to generate the finding.

        - **assetType** *(string) --*

          The type of the host from which the finding is generated.

        - **assetAttributes** *(dict) --*

          A collection of attributes of the host from which the finding is generated.

          - **schemaVersion** *(integer) --*

            The schema version of this data type.

          - **agentId** *(string) --*

            The ID of the agent that is installed on the EC2 instance where the finding is
            generated.

          - **autoScalingGroup** *(string) --*

            The Auto Scaling group of the EC2 instance where the finding is generated.

          - **amiId** *(string) --*

            The ID of the Amazon Machine Image (AMI) that is installed on the EC2 instance where
            the finding is generated.

          - **hostname** *(string) --*

            The hostname of the EC2 instance where the finding is generated.

          - **ipv4Addresses** *(list) --*

            The list of IP v4 addresses of the EC2 instance where the finding is generated.

            - *(string) --*

          - **tags** *(list) --*

            The tags related to the EC2 instance where the finding is generated.

            - *(dict) --*

              A key and value pair. This data type is used as a request parameter in the
              SetTagsForResource action and a response element in the  ListTagsForResource action.

              - **key** *(string) --*

                A tag key.

              - **value** *(string) --*

                A value assigned to a tag key.

          - **networkInterfaces** *(list) --*

            An array of the network interfaces interacting with the EC2 instance where the finding
            is generated.

            - *(dict) --*

              Contains information about the network interfaces interacting with an EC2 instance.
              This data type is used as one of the elements of the  AssetAttributes data type.

              - **networkInterfaceId** *(string) --*

                The ID of the network interface.

              - **subnetId** *(string) --*

                The ID of a subnet associated with the network interface.

              - **vpcId** *(string) --*

                The ID of a VPC associated with the network interface.

              - **privateDnsName** *(string) --*

                The name of a private DNS associated with the network interface.

              - **privateIpAddress** *(string) --*

                The private IP address associated with the network interface.

              - **privateIpAddresses** *(list) --*

                A list of the private IP addresses associated with the network interface. Includes
                the privateDnsName and privateIpAddress.

                - *(dict) --*

                  Contains information about a private IP address associated with a network
                  interface. This data type is used as a response element in the  DescribeFindings
                  action.

                  - **privateDnsName** *(string) --*

                    The DNS name of the private IP address.

                  - **privateIpAddress** *(string) --*

                    The full IP address of the network inteface.

              - **publicDnsName** *(string) --*

                The name of a public DNS associated with the network interface.

              - **publicIp** *(string) --*

                The public IP address from which the network interface is reachable.

              - **ipv6Addresses** *(list) --*

                The IP addresses associated with the network interface.

                - *(string) --*

              - **securityGroups** *(list) --*

                A list of the security groups associated with the network interface. Includes the
                groupId and groupName.

                - *(dict) --*

                  Contains information about a security group associated with a network interface.
                  This data type is used as one of the elements of the  NetworkInterface data type.

                  - **groupName** *(string) --*

                    The name of the security group.

                  - **groupId** *(string) --*

                    The ID of the security group.

        - **id** *(string) --*

          The ID of the finding.

        - **title** *(string) --*

          The name of the finding.

        - **description** *(string) --*

          The description of the finding.

        - **recommendation** *(string) --*

          The recommendation for the finding.

        - **severity** *(string) --*

          The finding severity. Values can be set to High, Medium, Low, and Informational.

        - **numericSeverity** *(float) --*

          The numeric value of the finding severity.

        - **confidence** *(integer) --*

          This data element is currently not used.

        - **indicatorOfCompromise** *(boolean) --*

          This data element is currently not used.

        - **attributes** *(list) --*

          The system-defined attributes for the finding.

          - *(dict) --*

            This data type is used as a request parameter in the  AddAttributesToFindings and
            CreateAssessmentTemplate actions.

            - **key** *(string) --*

              The attribute key.

            - **value** *(string) --*

              The value assigned to the attribute key.

        - **userAttributes** *(list) --*

          The user-defined attributes that are assigned to the finding.

          - *(dict) --*

            This data type is used as a request parameter in the  AddAttributesToFindings and
            CreateAssessmentTemplate actions.

            - **key** *(string) --*

              The attribute key.

            - **value** *(string) --*

              The value assigned to the attribute key.

        - **createdAt** *(datetime) --*

          The time when the finding was generated.

        - **updatedAt** *(datetime) --*

          The time when  AddAttributesToFindings is called.

    - **failedItems** *(dict) --*

      Finding details that cannot be described. An error code is provided for each failed item.

      - *(string) --*

        - *(dict) --*

          Includes details about the failed items.

          - **failureCode** *(string) --*

            The status code of a failed item.

          - **retryable** *(boolean) --*

            Indicates whether you can immediately retry a request for this item for a specified
            resource.
    """


_ClientDescribeResourceGroupsResponsefailedItemsTypeDef = TypedDict(
    "_ClientDescribeResourceGroupsResponsefailedItemsTypeDef",
    {"failureCode": str, "retryable": bool},
    total=False,
)


class ClientDescribeResourceGroupsResponsefailedItemsTypeDef(
    _ClientDescribeResourceGroupsResponsefailedItemsTypeDef
):
    """
    Type definition for `ClientDescribeResourceGroupsResponse` `failedItems`

    Includes details about the failed items.

    - **failureCode** *(string) --*

      The status code of a failed item.

    - **retryable** *(boolean) --*

      Indicates whether you can immediately retry a request for this item for a specified
      resource.
    """


_ClientDescribeResourceGroupsResponseresourceGroupstagsTypeDef = TypedDict(
    "_ClientDescribeResourceGroupsResponseresourceGroupstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribeResourceGroupsResponseresourceGroupstagsTypeDef(
    _ClientDescribeResourceGroupsResponseresourceGroupstagsTypeDef
):
    """
    Type definition for `ClientDescribeResourceGroupsResponseresourceGroups` `tags`

    This data type is used as one of the elements of the  ResourceGroup data type.

    - **key** *(string) --*

      A tag key.

    - **value** *(string) --*

      The value assigned to a tag key.
    """


_ClientDescribeResourceGroupsResponseresourceGroupsTypeDef = TypedDict(
    "_ClientDescribeResourceGroupsResponseresourceGroupsTypeDef",
    {
        "arn": str,
        "tags": List[ClientDescribeResourceGroupsResponseresourceGroupstagsTypeDef],
        "createdAt": datetime,
    },
    total=False,
)


class ClientDescribeResourceGroupsResponseresourceGroupsTypeDef(
    _ClientDescribeResourceGroupsResponseresourceGroupsTypeDef
):
    """
    Type definition for `ClientDescribeResourceGroupsResponse` `resourceGroups`

    Contains information about a resource group. The resource group defines a set of tags that,
    when queried, identify the AWS resources that make up the assessment target. This data type
    is used as the response element in the  DescribeResourceGroups action.

    - **arn** *(string) --*

      The ARN of the resource group.

    - **tags** *(list) --*

      The tags (key and value pairs) of the resource group. This data type property is used in
      the  CreateResourceGroup action.

      - *(dict) --*

        This data type is used as one of the elements of the  ResourceGroup data type.

        - **key** *(string) --*

          A tag key.

        - **value** *(string) --*

          The value assigned to a tag key.

    - **createdAt** *(datetime) --*

      The time at which resource group is created.
    """


_ClientDescribeResourceGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeResourceGroupsResponseTypeDef",
    {
        "resourceGroups": List[
            ClientDescribeResourceGroupsResponseresourceGroupsTypeDef
        ],
        "failedItems": Dict[
            str, ClientDescribeResourceGroupsResponsefailedItemsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeResourceGroupsResponseTypeDef(
    _ClientDescribeResourceGroupsResponseTypeDef
):
    """
    Type definition for `ClientDescribeResourceGroups` `Response`

    - **resourceGroups** *(list) --*

      Information about a resource group.

      - *(dict) --*

        Contains information about a resource group. The resource group defines a set of tags that,
        when queried, identify the AWS resources that make up the assessment target. This data type
        is used as the response element in the  DescribeResourceGroups action.

        - **arn** *(string) --*

          The ARN of the resource group.

        - **tags** *(list) --*

          The tags (key and value pairs) of the resource group. This data type property is used in
          the  CreateResourceGroup action.

          - *(dict) --*

            This data type is used as one of the elements of the  ResourceGroup data type.

            - **key** *(string) --*

              A tag key.

            - **value** *(string) --*

              The value assigned to a tag key.

        - **createdAt** *(datetime) --*

          The time at which resource group is created.

    - **failedItems** *(dict) --*

      Resource group details that cannot be described. An error code is provided for each failed
      item.

      - *(string) --*

        - *(dict) --*

          Includes details about the failed items.

          - **failureCode** *(string) --*

            The status code of a failed item.

          - **retryable** *(boolean) --*

            Indicates whether you can immediately retry a request for this item for a specified
            resource.
    """


_ClientDescribeRulesPackagesResponsefailedItemsTypeDef = TypedDict(
    "_ClientDescribeRulesPackagesResponsefailedItemsTypeDef",
    {"failureCode": str, "retryable": bool},
    total=False,
)


class ClientDescribeRulesPackagesResponsefailedItemsTypeDef(
    _ClientDescribeRulesPackagesResponsefailedItemsTypeDef
):
    """
    Type definition for `ClientDescribeRulesPackagesResponse` `failedItems`

    Includes details about the failed items.

    - **failureCode** *(string) --*

      The status code of a failed item.

    - **retryable** *(boolean) --*

      Indicates whether you can immediately retry a request for this item for a specified
      resource.
    """


_ClientDescribeRulesPackagesResponserulesPackagesTypeDef = TypedDict(
    "_ClientDescribeRulesPackagesResponserulesPackagesTypeDef",
    {"arn": str, "name": str, "version": str, "provider": str, "description": str},
    total=False,
)


class ClientDescribeRulesPackagesResponserulesPackagesTypeDef(
    _ClientDescribeRulesPackagesResponserulesPackagesTypeDef
):
    """
    Type definition for `ClientDescribeRulesPackagesResponse` `rulesPackages`

    Contains information about an Amazon Inspector rules package. This data type is used as the
    response element in the  DescribeRulesPackages action.

    - **arn** *(string) --*

      The ARN of the rules package.

    - **name** *(string) --*

      The name of the rules package.

    - **version** *(string) --*

      The version ID of the rules package.

    - **provider** *(string) --*

      The provider of the rules package.

    - **description** *(string) --*

      The description of the rules package.
    """


_ClientDescribeRulesPackagesResponseTypeDef = TypedDict(
    "_ClientDescribeRulesPackagesResponseTypeDef",
    {
        "rulesPackages": List[ClientDescribeRulesPackagesResponserulesPackagesTypeDef],
        "failedItems": Dict[str, ClientDescribeRulesPackagesResponsefailedItemsTypeDef],
    },
    total=False,
)


class ClientDescribeRulesPackagesResponseTypeDef(
    _ClientDescribeRulesPackagesResponseTypeDef
):
    """
    Type definition for `ClientDescribeRulesPackages` `Response`

    - **rulesPackages** *(list) --*

      Information about the rules package.

      - *(dict) --*

        Contains information about an Amazon Inspector rules package. This data type is used as the
        response element in the  DescribeRulesPackages action.

        - **arn** *(string) --*

          The ARN of the rules package.

        - **name** *(string) --*

          The name of the rules package.

        - **version** *(string) --*

          The version ID of the rules package.

        - **provider** *(string) --*

          The provider of the rules package.

        - **description** *(string) --*

          The description of the rules package.

    - **failedItems** *(dict) --*

      Rules package details that cannot be described. An error code is provided for each failed
      item.

      - *(string) --*

        - *(dict) --*

          Includes details about the failed items.

          - **failureCode** *(string) --*

            The status code of a failed item.

          - **retryable** *(boolean) --*

            Indicates whether you can immediately retry a request for this item for a specified
            resource.
    """


_ClientGetAssessmentReportResponseTypeDef = TypedDict(
    "_ClientGetAssessmentReportResponseTypeDef",
    {"status": str, "url": str},
    total=False,
)


class ClientGetAssessmentReportResponseTypeDef(
    _ClientGetAssessmentReportResponseTypeDef
):
    """
    Type definition for `ClientGetAssessmentReport` `Response`

    - **status** *(string) --*

      Specifies the status of the request to generate an assessment report.

    - **url** *(string) --*

      Specifies the URL where you can find the generated assessment report. This parameter is only
      returned if the report is successfully generated.
    """


_ClientGetExclusionsPreviewResponseexclusionPreviewsattributesTypeDef = TypedDict(
    "_ClientGetExclusionsPreviewResponseexclusionPreviewsattributesTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientGetExclusionsPreviewResponseexclusionPreviewsattributesTypeDef(
    _ClientGetExclusionsPreviewResponseexclusionPreviewsattributesTypeDef
):
    """
    Type definition for `ClientGetExclusionsPreviewResponseexclusionPreviews` `attributes`

    This data type is used as a request parameter in the  AddAttributesToFindings and
    CreateAssessmentTemplate actions.

    - **key** *(string) --*

      The attribute key.

    - **value** *(string) --*

      The value assigned to the attribute key.
    """


_ClientGetExclusionsPreviewResponseexclusionPreviewsscopesTypeDef = TypedDict(
    "_ClientGetExclusionsPreviewResponseexclusionPreviewsscopesTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientGetExclusionsPreviewResponseexclusionPreviewsscopesTypeDef(
    _ClientGetExclusionsPreviewResponseexclusionPreviewsscopesTypeDef
):
    """
    Type definition for `ClientGetExclusionsPreviewResponseexclusionPreviews` `scopes`

    This data type contains key-value pairs that identify various Amazon resources.

    - **key** *(string) --*

      The type of the scope.

    - **value** *(string) --*

      The resource identifier for the specified scope type.
    """


_ClientGetExclusionsPreviewResponseexclusionPreviewsTypeDef = TypedDict(
    "_ClientGetExclusionsPreviewResponseexclusionPreviewsTypeDef",
    {
        "title": str,
        "description": str,
        "recommendation": str,
        "scopes": List[
            ClientGetExclusionsPreviewResponseexclusionPreviewsscopesTypeDef
        ],
        "attributes": List[
            ClientGetExclusionsPreviewResponseexclusionPreviewsattributesTypeDef
        ],
    },
    total=False,
)


class ClientGetExclusionsPreviewResponseexclusionPreviewsTypeDef(
    _ClientGetExclusionsPreviewResponseexclusionPreviewsTypeDef
):
    """
    Type definition for `ClientGetExclusionsPreviewResponse` `exclusionPreviews`

    Contains information about what is excluded from an assessment run given the current state
    of the assessment template.

    - **title** *(string) --*

      The name of the exclusion preview.

    - **description** *(string) --*

      The description of the exclusion preview.

    - **recommendation** *(string) --*

      The recommendation for the exclusion preview.

    - **scopes** *(list) --*

      The AWS resources for which the exclusion preview pertains.

      - *(dict) --*

        This data type contains key-value pairs that identify various Amazon resources.

        - **key** *(string) --*

          The type of the scope.

        - **value** *(string) --*

          The resource identifier for the specified scope type.

    - **attributes** *(list) --*

      The system-defined attributes for the exclusion preview.

      - *(dict) --*

        This data type is used as a request parameter in the  AddAttributesToFindings and
        CreateAssessmentTemplate actions.

        - **key** *(string) --*

          The attribute key.

        - **value** *(string) --*

          The value assigned to the attribute key.
    """


_ClientGetExclusionsPreviewResponseTypeDef = TypedDict(
    "_ClientGetExclusionsPreviewResponseTypeDef",
    {
        "previewStatus": str,
        "exclusionPreviews": List[
            ClientGetExclusionsPreviewResponseexclusionPreviewsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientGetExclusionsPreviewResponseTypeDef(
    _ClientGetExclusionsPreviewResponseTypeDef
):
    """
    Type definition for `ClientGetExclusionsPreview` `Response`

    - **previewStatus** *(string) --*

      Specifies the status of the request to generate an exclusions preview.

    - **exclusionPreviews** *(list) --*

      Information about the exclusions included in the preview.

      - *(dict) --*

        Contains information about what is excluded from an assessment run given the current state
        of the assessment template.

        - **title** *(string) --*

          The name of the exclusion preview.

        - **description** *(string) --*

          The description of the exclusion preview.

        - **recommendation** *(string) --*

          The recommendation for the exclusion preview.

        - **scopes** *(list) --*

          The AWS resources for which the exclusion preview pertains.

          - *(dict) --*

            This data type contains key-value pairs that identify various Amazon resources.

            - **key** *(string) --*

              The type of the scope.

            - **value** *(string) --*

              The resource identifier for the specified scope type.

        - **attributes** *(list) --*

          The system-defined attributes for the exclusion preview.

          - *(dict) --*

            This data type is used as a request parameter in the  AddAttributesToFindings and
            CreateAssessmentTemplate actions.

            - **key** *(string) --*

              The attribute key.

            - **value** *(string) --*

              The value assigned to the attribute key.

    - **nextToken** *(string) --*

      When a response is generated, if there is more data to be listed, this parameters is present
      in the response and contains the value to use for the nextToken parameter in a subsequent
      pagination request. If there is no more data to be listed, this parameter is set to null.
    """


_ClientGetTelemetryMetadataResponsetelemetryMetadataTypeDef = TypedDict(
    "_ClientGetTelemetryMetadataResponsetelemetryMetadataTypeDef",
    {"messageType": str, "count": int, "dataSize": int},
    total=False,
)


class ClientGetTelemetryMetadataResponsetelemetryMetadataTypeDef(
    _ClientGetTelemetryMetadataResponsetelemetryMetadataTypeDef
):
    """
    Type definition for `ClientGetTelemetryMetadataResponse` `telemetryMetadata`

    The metadata about the Amazon Inspector application data metrics collected by the agent.
    This data type is used as the response element in the  GetTelemetryMetadata action.

    - **messageType** *(string) --*

      A specific type of behavioral data that is collected by the agent.

    - **count** *(integer) --*

      The count of messages that the agent sends to the Amazon Inspector service.

    - **dataSize** *(integer) --*

      The data size of messages that the agent sends to the Amazon Inspector service.
    """


_ClientGetTelemetryMetadataResponseTypeDef = TypedDict(
    "_ClientGetTelemetryMetadataResponseTypeDef",
    {
        "telemetryMetadata": List[
            ClientGetTelemetryMetadataResponsetelemetryMetadataTypeDef
        ]
    },
    total=False,
)


class ClientGetTelemetryMetadataResponseTypeDef(
    _ClientGetTelemetryMetadataResponseTypeDef
):
    """
    Type definition for `ClientGetTelemetryMetadata` `Response`

    - **telemetryMetadata** *(list) --*

      Telemetry details.

      - *(dict) --*

        The metadata about the Amazon Inspector application data metrics collected by the agent.
        This data type is used as the response element in the  GetTelemetryMetadata action.

        - **messageType** *(string) --*

          A specific type of behavioral data that is collected by the agent.

        - **count** *(integer) --*

          The count of messages that the agent sends to the Amazon Inspector service.

        - **dataSize** *(integer) --*

          The data size of messages that the agent sends to the Amazon Inspector service.
    """


_ClientListAssessmentRunAgentsResponseassessmentRunAgentstelemetryMetadataTypeDef = TypedDict(
    "_ClientListAssessmentRunAgentsResponseassessmentRunAgentstelemetryMetadataTypeDef",
    {"messageType": str, "count": int, "dataSize": int},
    total=False,
)


class ClientListAssessmentRunAgentsResponseassessmentRunAgentstelemetryMetadataTypeDef(
    _ClientListAssessmentRunAgentsResponseassessmentRunAgentstelemetryMetadataTypeDef
):
    """
    Type definition for `ClientListAssessmentRunAgentsResponseassessmentRunAgents` `telemetryMetadata`

    The metadata about the Amazon Inspector application data metrics collected by the
    agent. This data type is used as the response element in the  GetTelemetryMetadata
    action.

    - **messageType** *(string) --*

      A specific type of behavioral data that is collected by the agent.

    - **count** *(integer) --*

      The count of messages that the agent sends to the Amazon Inspector service.

    - **dataSize** *(integer) --*

      The data size of messages that the agent sends to the Amazon Inspector service.
    """


_ClientListAssessmentRunAgentsResponseassessmentRunAgentsTypeDef = TypedDict(
    "_ClientListAssessmentRunAgentsResponseassessmentRunAgentsTypeDef",
    {
        "agentId": str,
        "assessmentRunArn": str,
        "agentHealth": str,
        "agentHealthCode": str,
        "agentHealthDetails": str,
        "autoScalingGroup": str,
        "telemetryMetadata": List[
            ClientListAssessmentRunAgentsResponseassessmentRunAgentstelemetryMetadataTypeDef
        ],
    },
    total=False,
)


class ClientListAssessmentRunAgentsResponseassessmentRunAgentsTypeDef(
    _ClientListAssessmentRunAgentsResponseassessmentRunAgentsTypeDef
):
    """
    Type definition for `ClientListAssessmentRunAgentsResponse` `assessmentRunAgents`

    Contains information about an Amazon Inspector agent. This data type is used as a response
    element in the  ListAssessmentRunAgents action.

    - **agentId** *(string) --*

      The AWS account of the EC2 instance where the agent is installed.

    - **assessmentRunArn** *(string) --*

      The ARN of the assessment run that is associated with the agent.

    - **agentHealth** *(string) --*

      The current health state of the agent.

    - **agentHealthCode** *(string) --*

      The detailed health state of the agent.

    - **agentHealthDetails** *(string) --*

      The description for the agent health code.

    - **autoScalingGroup** *(string) --*

      The Auto Scaling group of the EC2 instance that is specified by the agent ID.

    - **telemetryMetadata** *(list) --*

      The Amazon Inspector application data metrics that are collected by the agent.

      - *(dict) --*

        The metadata about the Amazon Inspector application data metrics collected by the
        agent. This data type is used as the response element in the  GetTelemetryMetadata
        action.

        - **messageType** *(string) --*

          A specific type of behavioral data that is collected by the agent.

        - **count** *(integer) --*

          The count of messages that the agent sends to the Amazon Inspector service.

        - **dataSize** *(integer) --*

          The data size of messages that the agent sends to the Amazon Inspector service.
    """


_ClientListAssessmentRunAgentsResponseTypeDef = TypedDict(
    "_ClientListAssessmentRunAgentsResponseTypeDef",
    {
        "assessmentRunAgents": List[
            ClientListAssessmentRunAgentsResponseassessmentRunAgentsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListAssessmentRunAgentsResponseTypeDef(
    _ClientListAssessmentRunAgentsResponseTypeDef
):
    """
    Type definition for `ClientListAssessmentRunAgents` `Response`

    - **assessmentRunAgents** *(list) --*

      A list of ARNs that specifies the agents returned by the action.

      - *(dict) --*

        Contains information about an Amazon Inspector agent. This data type is used as a response
        element in the  ListAssessmentRunAgents action.

        - **agentId** *(string) --*

          The AWS account of the EC2 instance where the agent is installed.

        - **assessmentRunArn** *(string) --*

          The ARN of the assessment run that is associated with the agent.

        - **agentHealth** *(string) --*

          The current health state of the agent.

        - **agentHealthCode** *(string) --*

          The detailed health state of the agent.

        - **agentHealthDetails** *(string) --*

          The description for the agent health code.

        - **autoScalingGroup** *(string) --*

          The Auto Scaling group of the EC2 instance that is specified by the agent ID.

        - **telemetryMetadata** *(list) --*

          The Amazon Inspector application data metrics that are collected by the agent.

          - *(dict) --*

            The metadata about the Amazon Inspector application data metrics collected by the
            agent. This data type is used as the response element in the  GetTelemetryMetadata
            action.

            - **messageType** *(string) --*

              A specific type of behavioral data that is collected by the agent.

            - **count** *(integer) --*

              The count of messages that the agent sends to the Amazon Inspector service.

            - **dataSize** *(integer) --*

              The data size of messages that the agent sends to the Amazon Inspector service.

    - **nextToken** *(string) --*

      When a response is generated, if there is more data to be listed, this parameter is present
      in the response and contains the value to use for the **nextToken** parameter in a subsequent
      pagination request. If there is no more data to be listed, this parameter is set to null.
    """


_ClientListAssessmentRunAgentsfilterTypeDef = TypedDict(
    "_ClientListAssessmentRunAgentsfilterTypeDef",
    {"agentHealths": List[str], "agentHealthCodes": List[str]},
)


class ClientListAssessmentRunAgentsfilterTypeDef(
    _ClientListAssessmentRunAgentsfilterTypeDef
):
    """
    Type definition for `ClientListAssessmentRunAgents` `filter`

    You can use this parameter to specify a subset of data to be included in the action's response.

    For a record to match a filter, all specified filter attributes must match. When multiple values
    are specified for a filter attribute, any of the values can match.

    - **agentHealths** *(list) --* **[REQUIRED]**

      The current health state of the agent. Values can be set to **HEALTHY** or **UNHEALTHY** .

      - *(string) --*

    - **agentHealthCodes** *(list) --* **[REQUIRED]**

      The detailed health state of the agent. Values can be set to **IDLE** , **RUNNING** ,
      **SHUTDOWN** , **UNHEALTHY** , **THROTTLED** , and **UNKNOWN** .

      - *(string) --*
    """


_ClientListAssessmentRunsResponseTypeDef = TypedDict(
    "_ClientListAssessmentRunsResponseTypeDef",
    {"assessmentRunArns": List[str], "nextToken": str},
    total=False,
)


class ClientListAssessmentRunsResponseTypeDef(_ClientListAssessmentRunsResponseTypeDef):
    """
    Type definition for `ClientListAssessmentRuns` `Response`

    - **assessmentRunArns** *(list) --*

      A list of ARNs that specifies the assessment runs that are returned by the action.

      - *(string) --*

    - **nextToken** *(string) --*

      When a response is generated, if there is more data to be listed, this parameter is present
      in the response and contains the value to use for the **nextToken** parameter in a subsequent
      pagination request. If there is no more data to be listed, this parameter is set to null.
    """


_ClientListAssessmentRunsfiltercompletionTimeRangeTypeDef = TypedDict(
    "_ClientListAssessmentRunsfiltercompletionTimeRangeTypeDef",
    {"beginDate": datetime, "endDate": datetime},
    total=False,
)


class ClientListAssessmentRunsfiltercompletionTimeRangeTypeDef(
    _ClientListAssessmentRunsfiltercompletionTimeRangeTypeDef
):
    """
    Type definition for `ClientListAssessmentRunsfilter` `completionTimeRange`

    For a record to match a filter, the value that is specified for this data type property must
    inclusively match any value between the specified minimum and maximum values of the
    **completedAt** property of the  AssessmentRun data type.

    - **beginDate** *(datetime) --*

      The minimum value of the timestamp range.

    - **endDate** *(datetime) --*

      The maximum value of the timestamp range.
    """


_ClientListAssessmentRunsfilterdurationRangeTypeDef = TypedDict(
    "_ClientListAssessmentRunsfilterdurationRangeTypeDef",
    {"minSeconds": int, "maxSeconds": int},
    total=False,
)


class ClientListAssessmentRunsfilterdurationRangeTypeDef(
    _ClientListAssessmentRunsfilterdurationRangeTypeDef
):
    """
    Type definition for `ClientListAssessmentRunsfilter` `durationRange`

    For a record to match a filter, the value that is specified for this data type property must
    inclusively match any value between the specified minimum and maximum values of the
    **durationInSeconds** property of the  AssessmentRun data type.

    - **minSeconds** *(integer) --*

      The minimum value of the duration range. Must be greater than zero.

    - **maxSeconds** *(integer) --*

      The maximum value of the duration range. Must be less than or equal to 604800 seconds (1
      week).
    """


_ClientListAssessmentRunsfilterstartTimeRangeTypeDef = TypedDict(
    "_ClientListAssessmentRunsfilterstartTimeRangeTypeDef",
    {"beginDate": datetime, "endDate": datetime},
    total=False,
)


class ClientListAssessmentRunsfilterstartTimeRangeTypeDef(
    _ClientListAssessmentRunsfilterstartTimeRangeTypeDef
):
    """
    Type definition for `ClientListAssessmentRunsfilter` `startTimeRange`

    For a record to match a filter, the value that is specified for this data type property must
    inclusively match any value between the specified minimum and maximum values of the
    **startTime** property of the  AssessmentRun data type.

    - **beginDate** *(datetime) --*

      The minimum value of the timestamp range.

    - **endDate** *(datetime) --*

      The maximum value of the timestamp range.
    """


_ClientListAssessmentRunsfilterstateChangeTimeRangeTypeDef = TypedDict(
    "_ClientListAssessmentRunsfilterstateChangeTimeRangeTypeDef",
    {"beginDate": datetime, "endDate": datetime},
    total=False,
)


class ClientListAssessmentRunsfilterstateChangeTimeRangeTypeDef(
    _ClientListAssessmentRunsfilterstateChangeTimeRangeTypeDef
):
    """
    Type definition for `ClientListAssessmentRunsfilter` `stateChangeTimeRange`

    For a record to match a filter, the value that is specified for this data type property must
    match the **stateChangedAt** property of the  AssessmentRun data type.

    - **beginDate** *(datetime) --*

      The minimum value of the timestamp range.

    - **endDate** *(datetime) --*

      The maximum value of the timestamp range.
    """


_ClientListAssessmentRunsfilterTypeDef = TypedDict(
    "_ClientListAssessmentRunsfilterTypeDef",
    {
        "namePattern": str,
        "states": List[str],
        "durationRange": ClientListAssessmentRunsfilterdurationRangeTypeDef,
        "rulesPackageArns": List[str],
        "startTimeRange": ClientListAssessmentRunsfilterstartTimeRangeTypeDef,
        "completionTimeRange": ClientListAssessmentRunsfiltercompletionTimeRangeTypeDef,
        "stateChangeTimeRange": ClientListAssessmentRunsfilterstateChangeTimeRangeTypeDef,
    },
    total=False,
)


class ClientListAssessmentRunsfilterTypeDef(_ClientListAssessmentRunsfilterTypeDef):
    """
    Type definition for `ClientListAssessmentRuns` `filter`

    You can use this parameter to specify a subset of data to be included in the action's response.

    For a record to match a filter, all specified filter attributes must match. When multiple values
    are specified for a filter attribute, any of the values can match.

    - **namePattern** *(string) --*

      For a record to match a filter, an explicit value or a string containing a wildcard that is
      specified for this data type property must match the value of the **assessmentRunName**
      property of the  AssessmentRun data type.

    - **states** *(list) --*

      For a record to match a filter, one of the values specified for this data type property must be
      the exact match of the value of the **assessmentRunState** property of the  AssessmentRun data
      type.

      - *(string) --*

    - **durationRange** *(dict) --*

      For a record to match a filter, the value that is specified for this data type property must
      inclusively match any value between the specified minimum and maximum values of the
      **durationInSeconds** property of the  AssessmentRun data type.

      - **minSeconds** *(integer) --*

        The minimum value of the duration range. Must be greater than zero.

      - **maxSeconds** *(integer) --*

        The maximum value of the duration range. Must be less than or equal to 604800 seconds (1
        week).

    - **rulesPackageArns** *(list) --*

      For a record to match a filter, the value that is specified for this data type property must be
      contained in the list of values of the **rulesPackages** property of the  AssessmentRun data
      type.

      - *(string) --*

    - **startTimeRange** *(dict) --*

      For a record to match a filter, the value that is specified for this data type property must
      inclusively match any value between the specified minimum and maximum values of the
      **startTime** property of the  AssessmentRun data type.

      - **beginDate** *(datetime) --*

        The minimum value of the timestamp range.

      - **endDate** *(datetime) --*

        The maximum value of the timestamp range.

    - **completionTimeRange** *(dict) --*

      For a record to match a filter, the value that is specified for this data type property must
      inclusively match any value between the specified minimum and maximum values of the
      **completedAt** property of the  AssessmentRun data type.

      - **beginDate** *(datetime) --*

        The minimum value of the timestamp range.

      - **endDate** *(datetime) --*

        The maximum value of the timestamp range.

    - **stateChangeTimeRange** *(dict) --*

      For a record to match a filter, the value that is specified for this data type property must
      match the **stateChangedAt** property of the  AssessmentRun data type.

      - **beginDate** *(datetime) --*

        The minimum value of the timestamp range.

      - **endDate** *(datetime) --*

        The maximum value of the timestamp range.
    """


_ClientListAssessmentTargetsResponseTypeDef = TypedDict(
    "_ClientListAssessmentTargetsResponseTypeDef",
    {"assessmentTargetArns": List[str], "nextToken": str},
    total=False,
)


class ClientListAssessmentTargetsResponseTypeDef(
    _ClientListAssessmentTargetsResponseTypeDef
):
    """
    Type definition for `ClientListAssessmentTargets` `Response`

    - **assessmentTargetArns** *(list) --*

      A list of ARNs that specifies the assessment targets that are returned by the action.

      - *(string) --*

    - **nextToken** *(string) --*

      When a response is generated, if there is more data to be listed, this parameter is present
      in the response and contains the value to use for the **nextToken** parameter in a subsequent
      pagination request. If there is no more data to be listed, this parameter is set to null.
    """


_ClientListAssessmentTargetsfilterTypeDef = TypedDict(
    "_ClientListAssessmentTargetsfilterTypeDef",
    {"assessmentTargetNamePattern": str},
    total=False,
)


class ClientListAssessmentTargetsfilterTypeDef(
    _ClientListAssessmentTargetsfilterTypeDef
):
    """
    Type definition for `ClientListAssessmentTargets` `filter`

    You can use this parameter to specify a subset of data to be included in the action's response.

    For a record to match a filter, all specified filter attributes must match. When multiple values
    are specified for a filter attribute, any of the values can match.

    - **assessmentTargetNamePattern** *(string) --*

      For a record to match a filter, an explicit value or a string that contains a wildcard that is
      specified for this data type property must match the value of the **assessmentTargetName**
      property of the  AssessmentTarget data type.
    """


_ClientListAssessmentTemplatesResponseTypeDef = TypedDict(
    "_ClientListAssessmentTemplatesResponseTypeDef",
    {"assessmentTemplateArns": List[str], "nextToken": str},
    total=False,
)


class ClientListAssessmentTemplatesResponseTypeDef(
    _ClientListAssessmentTemplatesResponseTypeDef
):
    """
    Type definition for `ClientListAssessmentTemplates` `Response`

    - **assessmentTemplateArns** *(list) --*

      A list of ARNs that specifies the assessment templates returned by the action.

      - *(string) --*

    - **nextToken** *(string) --*

      When a response is generated, if there is more data to be listed, this parameter is present
      in the response and contains the value to use for the **nextToken** parameter in a subsequent
      pagination request. If there is no more data to be listed, this parameter is set to null.
    """


_ClientListAssessmentTemplatesfilterdurationRangeTypeDef = TypedDict(
    "_ClientListAssessmentTemplatesfilterdurationRangeTypeDef",
    {"minSeconds": int, "maxSeconds": int},
    total=False,
)


class ClientListAssessmentTemplatesfilterdurationRangeTypeDef(
    _ClientListAssessmentTemplatesfilterdurationRangeTypeDef
):
    """
    Type definition for `ClientListAssessmentTemplatesfilter` `durationRange`

    For a record to match a filter, the value specified for this data type property must
    inclusively match any value between the specified minimum and maximum values of the
    **durationInSeconds** property of the  AssessmentTemplate data type.

    - **minSeconds** *(integer) --*

      The minimum value of the duration range. Must be greater than zero.

    - **maxSeconds** *(integer) --*

      The maximum value of the duration range. Must be less than or equal to 604800 seconds (1
      week).
    """


_ClientListAssessmentTemplatesfilterTypeDef = TypedDict(
    "_ClientListAssessmentTemplatesfilterTypeDef",
    {
        "namePattern": str,
        "durationRange": ClientListAssessmentTemplatesfilterdurationRangeTypeDef,
        "rulesPackageArns": List[str],
    },
    total=False,
)


class ClientListAssessmentTemplatesfilterTypeDef(
    _ClientListAssessmentTemplatesfilterTypeDef
):
    """
    Type definition for `ClientListAssessmentTemplates` `filter`

    You can use this parameter to specify a subset of data to be included in the action's response.

    For a record to match a filter, all specified filter attributes must match. When multiple values
    are specified for a filter attribute, any of the values can match.

    - **namePattern** *(string) --*

      For a record to match a filter, an explicit value or a string that contains a wildcard that is
      specified for this data type property must match the value of the **assessmentTemplateName**
      property of the  AssessmentTemplate data type.

    - **durationRange** *(dict) --*

      For a record to match a filter, the value specified for this data type property must
      inclusively match any value between the specified minimum and maximum values of the
      **durationInSeconds** property of the  AssessmentTemplate data type.

      - **minSeconds** *(integer) --*

        The minimum value of the duration range. Must be greater than zero.

      - **maxSeconds** *(integer) --*

        The maximum value of the duration range. Must be less than or equal to 604800 seconds (1
        week).

    - **rulesPackageArns** *(list) --*

      For a record to match a filter, the values that are specified for this data type property must
      be contained in the list of values of the **rulesPackageArns** property of the
      AssessmentTemplate data type.

      - *(string) --*
    """


_ClientListEventSubscriptionsResponsesubscriptionseventSubscriptionsTypeDef = TypedDict(
    "_ClientListEventSubscriptionsResponsesubscriptionseventSubscriptionsTypeDef",
    {"event": str, "subscribedAt": datetime},
    total=False,
)


class ClientListEventSubscriptionsResponsesubscriptionseventSubscriptionsTypeDef(
    _ClientListEventSubscriptionsResponsesubscriptionseventSubscriptionsTypeDef
):
    """
    Type definition for `ClientListEventSubscriptionsResponsesubscriptions` `eventSubscriptions`

    This data type is used in the  Subscription data type.

    - **event** *(string) --*

      The event for which Amazon Simple Notification Service (SNS) notifications are sent.

    - **subscribedAt** *(datetime) --*

      The time at which  SubscribeToEvent is called.
    """


_ClientListEventSubscriptionsResponsesubscriptionsTypeDef = TypedDict(
    "_ClientListEventSubscriptionsResponsesubscriptionsTypeDef",
    {
        "resourceArn": str,
        "topicArn": str,
        "eventSubscriptions": List[
            ClientListEventSubscriptionsResponsesubscriptionseventSubscriptionsTypeDef
        ],
    },
    total=False,
)


class ClientListEventSubscriptionsResponsesubscriptionsTypeDef(
    _ClientListEventSubscriptionsResponsesubscriptionsTypeDef
):
    """
    Type definition for `ClientListEventSubscriptionsResponse` `subscriptions`

    This data type is used as a response element in the  ListEventSubscriptions action.

    - **resourceArn** *(string) --*

      The ARN of the assessment template that is used during the event for which the SNS
      notification is sent.

    - **topicArn** *(string) --*

      The ARN of the Amazon Simple Notification Service (SNS) topic to which the SNS
      notifications are sent.

    - **eventSubscriptions** *(list) --*

      The list of existing event subscriptions.

      - *(dict) --*

        This data type is used in the  Subscription data type.

        - **event** *(string) --*

          The event for which Amazon Simple Notification Service (SNS) notifications are sent.

        - **subscribedAt** *(datetime) --*

          The time at which  SubscribeToEvent is called.
    """


_ClientListEventSubscriptionsResponseTypeDef = TypedDict(
    "_ClientListEventSubscriptionsResponseTypeDef",
    {
        "subscriptions": List[ClientListEventSubscriptionsResponsesubscriptionsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListEventSubscriptionsResponseTypeDef(
    _ClientListEventSubscriptionsResponseTypeDef
):
    """
    Type definition for `ClientListEventSubscriptions` `Response`

    - **subscriptions** *(list) --*

      Details of the returned event subscriptions.

      - *(dict) --*

        This data type is used as a response element in the  ListEventSubscriptions action.

        - **resourceArn** *(string) --*

          The ARN of the assessment template that is used during the event for which the SNS
          notification is sent.

        - **topicArn** *(string) --*

          The ARN of the Amazon Simple Notification Service (SNS) topic to which the SNS
          notifications are sent.

        - **eventSubscriptions** *(list) --*

          The list of existing event subscriptions.

          - *(dict) --*

            This data type is used in the  Subscription data type.

            - **event** *(string) --*

              The event for which Amazon Simple Notification Service (SNS) notifications are sent.

            - **subscribedAt** *(datetime) --*

              The time at which  SubscribeToEvent is called.

    - **nextToken** *(string) --*

      When a response is generated, if there is more data to be listed, this parameter is present
      in the response and contains the value to use for the **nextToken** parameter in a subsequent
      pagination request. If there is no more data to be listed, this parameter is set to null.
    """


_ClientListExclusionsResponseTypeDef = TypedDict(
    "_ClientListExclusionsResponseTypeDef",
    {"exclusionArns": List[str], "nextToken": str},
    total=False,
)


class ClientListExclusionsResponseTypeDef(_ClientListExclusionsResponseTypeDef):
    """
    Type definition for `ClientListExclusions` `Response`

    - **exclusionArns** *(list) --*

      A list of exclusions' ARNs returned by the action.

      - *(string) --*

    - **nextToken** *(string) --*

      When a response is generated, if there is more data to be listed, this parameters is present
      in the response and contains the value to use for the nextToken parameter in a subsequent
      pagination request. If there is no more data to be listed, this parameter is set to null.
    """


_ClientListFindingsResponseTypeDef = TypedDict(
    "_ClientListFindingsResponseTypeDef",
    {"findingArns": List[str], "nextToken": str},
    total=False,
)


class ClientListFindingsResponseTypeDef(_ClientListFindingsResponseTypeDef):
    """
    Type definition for `ClientListFindings` `Response`

    - **findingArns** *(list) --*

      A list of ARNs that specifies the findings returned by the action.

      - *(string) --*

    - **nextToken** *(string) --*

      When a response is generated, if there is more data to be listed, this parameter is present
      in the response and contains the value to use for the **nextToken** parameter in a subsequent
      pagination request. If there is no more data to be listed, this parameter is set to null.
    """


_RequiredClientListFindingsfilterattributesTypeDef = TypedDict(
    "_RequiredClientListFindingsfilterattributesTypeDef", {"key": str}
)
_OptionalClientListFindingsfilterattributesTypeDef = TypedDict(
    "_OptionalClientListFindingsfilterattributesTypeDef", {"value": str}, total=False
)


class ClientListFindingsfilterattributesTypeDef(
    _RequiredClientListFindingsfilterattributesTypeDef,
    _OptionalClientListFindingsfilterattributesTypeDef,
):
    """
    Type definition for `ClientListFindingsfilter` `attributes`

    This data type is used as a request parameter in the  AddAttributesToFindings and
    CreateAssessmentTemplate actions.

    - **key** *(string) --* **[REQUIRED]**

      The attribute key.

    - **value** *(string) --*

      The value assigned to the attribute key.
    """


_ClientListFindingsfiltercreationTimeRangeTypeDef = TypedDict(
    "_ClientListFindingsfiltercreationTimeRangeTypeDef",
    {"beginDate": datetime, "endDate": datetime},
    total=False,
)


class ClientListFindingsfiltercreationTimeRangeTypeDef(
    _ClientListFindingsfiltercreationTimeRangeTypeDef
):
    """
    Type definition for `ClientListFindingsfilter` `creationTimeRange`

    The time range during which the finding is generated.

    - **beginDate** *(datetime) --*

      The minimum value of the timestamp range.

    - **endDate** *(datetime) --*

      The maximum value of the timestamp range.
    """


_RequiredClientListFindingsfilteruserAttributesTypeDef = TypedDict(
    "_RequiredClientListFindingsfilteruserAttributesTypeDef", {"key": str}
)
_OptionalClientListFindingsfilteruserAttributesTypeDef = TypedDict(
    "_OptionalClientListFindingsfilteruserAttributesTypeDef",
    {"value": str},
    total=False,
)


class ClientListFindingsfilteruserAttributesTypeDef(
    _RequiredClientListFindingsfilteruserAttributesTypeDef,
    _OptionalClientListFindingsfilteruserAttributesTypeDef,
):
    """
    Type definition for `ClientListFindingsfilter` `userAttributes`

    This data type is used as a request parameter in the  AddAttributesToFindings and
    CreateAssessmentTemplate actions.

    - **key** *(string) --* **[REQUIRED]**

      The attribute key.

    - **value** *(string) --*

      The value assigned to the attribute key.
    """


_ClientListFindingsfilterTypeDef = TypedDict(
    "_ClientListFindingsfilterTypeDef",
    {
        "agentIds": List[str],
        "autoScalingGroups": List[str],
        "ruleNames": List[str],
        "severities": List[str],
        "rulesPackageArns": List[str],
        "attributes": List[ClientListFindingsfilterattributesTypeDef],
        "userAttributes": List[ClientListFindingsfilteruserAttributesTypeDef],
        "creationTimeRange": ClientListFindingsfiltercreationTimeRangeTypeDef,
    },
    total=False,
)


class ClientListFindingsfilterTypeDef(_ClientListFindingsfilterTypeDef):
    """
    Type definition for `ClientListFindings` `filter`

    You can use this parameter to specify a subset of data to be included in the action's response.

    For a record to match a filter, all specified filter attributes must match. When multiple values
    are specified for a filter attribute, any of the values can match.

    - **agentIds** *(list) --*

      For a record to match a filter, one of the values that is specified for this data type property
      must be the exact match of the value of the **agentId** property of the  Finding data type.

      - *(string) --*

    - **autoScalingGroups** *(list) --*

      For a record to match a filter, one of the values that is specified for this data type property
      must be the exact match of the value of the **autoScalingGroup** property of the  Finding data
      type.

      - *(string) --*

    - **ruleNames** *(list) --*

      For a record to match a filter, one of the values that is specified for this data type property
      must be the exact match of the value of the **ruleName** property of the  Finding data type.

      - *(string) --*

    - **severities** *(list) --*

      For a record to match a filter, one of the values that is specified for this data type property
      must be the exact match of the value of the **severity** property of the  Finding data type.

      - *(string) --*

    - **rulesPackageArns** *(list) --*

      For a record to match a filter, one of the values that is specified for this data type property
      must be the exact match of the value of the **rulesPackageArn** property of the  Finding data
      type.

      - *(string) --*

    - **attributes** *(list) --*

      For a record to match a filter, the list of values that are specified for this data type
      property must be contained in the list of values of the **attributes** property of the  Finding
      data type.

      - *(dict) --*

        This data type is used as a request parameter in the  AddAttributesToFindings and
        CreateAssessmentTemplate actions.

        - **key** *(string) --* **[REQUIRED]**

          The attribute key.

        - **value** *(string) --*

          The value assigned to the attribute key.

    - **userAttributes** *(list) --*

      For a record to match a filter, the value that is specified for this data type property must be
      contained in the list of values of the **userAttributes** property of the  Finding data type.

      - *(dict) --*

        This data type is used as a request parameter in the  AddAttributesToFindings and
        CreateAssessmentTemplate actions.

        - **key** *(string) --* **[REQUIRED]**

          The attribute key.

        - **value** *(string) --*

          The value assigned to the attribute key.

    - **creationTimeRange** *(dict) --*

      The time range during which the finding is generated.

      - **beginDate** *(datetime) --*

        The minimum value of the timestamp range.

      - **endDate** *(datetime) --*

        The maximum value of the timestamp range.
    """


_ClientListRulesPackagesResponseTypeDef = TypedDict(
    "_ClientListRulesPackagesResponseTypeDef",
    {"rulesPackageArns": List[str], "nextToken": str},
    total=False,
)


class ClientListRulesPackagesResponseTypeDef(_ClientListRulesPackagesResponseTypeDef):
    """
    Type definition for `ClientListRulesPackages` `Response`

    - **rulesPackageArns** *(list) --*

      The list of ARNs that specifies the rules packages returned by the action.

      - *(string) --*

    - **nextToken** *(string) --*

      When a response is generated, if there is more data to be listed, this parameter is present
      in the response and contains the value to use for the **nextToken** parameter in a subsequent
      pagination request. If there is no more data to be listed, this parameter is set to null.
    """


_ClientListTagsForResourceResponsetagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientListTagsForResourceResponsetagsTypeDef(
    _ClientListTagsForResourceResponsetagsTypeDef
):
    """
    Type definition for `ClientListTagsForResourceResponse` `tags`

    A key and value pair. This data type is used as a request parameter in the
    SetTagsForResource action and a response element in the  ListTagsForResource action.

    - **key** *(string) --*

      A tag key.

    - **value** *(string) --*

      A value assigned to a tag key.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"tags": List[ClientListTagsForResourceResponsetagsTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **tags** *(list) --*

      A collection of key and value pairs.

      - *(dict) --*

        A key and value pair. This data type is used as a request parameter in the
        SetTagsForResource action and a response element in the  ListTagsForResource action.

        - **key** *(string) --*

          A tag key.

        - **value** *(string) --*

          A value assigned to a tag key.
    """


_ClientPreviewAgentsResponseagentPreviewsTypeDef = TypedDict(
    "_ClientPreviewAgentsResponseagentPreviewsTypeDef",
    {
        "hostname": str,
        "agentId": str,
        "autoScalingGroup": str,
        "agentHealth": str,
        "agentVersion": str,
        "operatingSystem": str,
        "kernelVersion": str,
        "ipv4Address": str,
    },
    total=False,
)


class ClientPreviewAgentsResponseagentPreviewsTypeDef(
    _ClientPreviewAgentsResponseagentPreviewsTypeDef
):
    """
    Type definition for `ClientPreviewAgentsResponse` `agentPreviews`

    Used as a response element in the  PreviewAgents action.

    - **hostname** *(string) --*

      The hostname of the EC2 instance on which the Amazon Inspector Agent is installed.

    - **agentId** *(string) --*

      The ID of the EC2 instance where the agent is installed.

    - **autoScalingGroup** *(string) --*

      The Auto Scaling group for the EC2 instance where the agent is installed.

    - **agentHealth** *(string) --*

      The health status of the Amazon Inspector Agent.

    - **agentVersion** *(string) --*

      The version of the Amazon Inspector Agent.

    - **operatingSystem** *(string) --*

      The operating system running on the EC2 instance on which the Amazon Inspector Agent is
      installed.

    - **kernelVersion** *(string) --*

      The kernel version of the operating system running on the EC2 instance on which the
      Amazon Inspector Agent is installed.

    - **ipv4Address** *(string) --*

      The IP address of the EC2 instance on which the Amazon Inspector Agent is installed.
    """


_ClientPreviewAgentsResponseTypeDef = TypedDict(
    "_ClientPreviewAgentsResponseTypeDef",
    {
        "agentPreviews": List[ClientPreviewAgentsResponseagentPreviewsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientPreviewAgentsResponseTypeDef(_ClientPreviewAgentsResponseTypeDef):
    """
    Type definition for `ClientPreviewAgents` `Response`

    - **agentPreviews** *(list) --*

      The resulting list of agents.

      - *(dict) --*

        Used as a response element in the  PreviewAgents action.

        - **hostname** *(string) --*

          The hostname of the EC2 instance on which the Amazon Inspector Agent is installed.

        - **agentId** *(string) --*

          The ID of the EC2 instance where the agent is installed.

        - **autoScalingGroup** *(string) --*

          The Auto Scaling group for the EC2 instance where the agent is installed.

        - **agentHealth** *(string) --*

          The health status of the Amazon Inspector Agent.

        - **agentVersion** *(string) --*

          The version of the Amazon Inspector Agent.

        - **operatingSystem** *(string) --*

          The operating system running on the EC2 instance on which the Amazon Inspector Agent is
          installed.

        - **kernelVersion** *(string) --*

          The kernel version of the operating system running on the EC2 instance on which the
          Amazon Inspector Agent is installed.

        - **ipv4Address** *(string) --*

          The IP address of the EC2 instance on which the Amazon Inspector Agent is installed.

    - **nextToken** *(string) --*

      When a response is generated, if there is more data to be listed, this parameter is present
      in the response and contains the value to use for the **nextToken** parameter in a subsequent
      pagination request. If there is no more data to be listed, this parameter is set to null.
    """


_ClientRemoveAttributesFromFindingsResponsefailedItemsTypeDef = TypedDict(
    "_ClientRemoveAttributesFromFindingsResponsefailedItemsTypeDef",
    {"failureCode": str, "retryable": bool},
    total=False,
)


class ClientRemoveAttributesFromFindingsResponsefailedItemsTypeDef(
    _ClientRemoveAttributesFromFindingsResponsefailedItemsTypeDef
):
    """
    Type definition for `ClientRemoveAttributesFromFindingsResponse` `failedItems`

    Includes details about the failed items.

    - **failureCode** *(string) --*

      The status code of a failed item.

    - **retryable** *(boolean) --*

      Indicates whether you can immediately retry a request for this item for a specified
      resource.
    """


_ClientRemoveAttributesFromFindingsResponseTypeDef = TypedDict(
    "_ClientRemoveAttributesFromFindingsResponseTypeDef",
    {
        "failedItems": Dict[
            str, ClientRemoveAttributesFromFindingsResponsefailedItemsTypeDef
        ]
    },
    total=False,
)


class ClientRemoveAttributesFromFindingsResponseTypeDef(
    _ClientRemoveAttributesFromFindingsResponseTypeDef
):
    """
    Type definition for `ClientRemoveAttributesFromFindings` `Response`

    - **failedItems** *(dict) --*

      Attributes details that cannot be described. An error code is provided for each failed item.

      - *(string) --*

        - *(dict) --*

          Includes details about the failed items.

          - **failureCode** *(string) --*

            The status code of a failed item.

          - **retryable** *(boolean) --*

            Indicates whether you can immediately retry a request for this item for a specified
            resource.
    """


_RequiredClientSetTagsForResourcetagsTypeDef = TypedDict(
    "_RequiredClientSetTagsForResourcetagsTypeDef", {"key": str}
)
_OptionalClientSetTagsForResourcetagsTypeDef = TypedDict(
    "_OptionalClientSetTagsForResourcetagsTypeDef", {"value": str}, total=False
)


class ClientSetTagsForResourcetagsTypeDef(
    _RequiredClientSetTagsForResourcetagsTypeDef,
    _OptionalClientSetTagsForResourcetagsTypeDef,
):
    """
    Type definition for `ClientSetTagsForResource` `tags`

    A key and value pair. This data type is used as a request parameter in the  SetTagsForResource
    action and a response element in the  ListTagsForResource action.

    - **key** *(string) --* **[REQUIRED]**

      A tag key.

    - **value** *(string) --*

      A value assigned to a tag key.
    """


_ClientStartAssessmentRunResponseTypeDef = TypedDict(
    "_ClientStartAssessmentRunResponseTypeDef", {"assessmentRunArn": str}, total=False
)


class ClientStartAssessmentRunResponseTypeDef(_ClientStartAssessmentRunResponseTypeDef):
    """
    Type definition for `ClientStartAssessmentRun` `Response`

    - **assessmentRunArn** *(string) --*

      The ARN of the assessment run that has been started.
    """


_ListAssessmentRunAgentsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAssessmentRunAgentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAssessmentRunAgentsPaginatePaginationConfigTypeDef(
    _ListAssessmentRunAgentsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAssessmentRunAgentsPaginate` `PaginationConfig`

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


_ListAssessmentRunAgentsPaginateResponseassessmentRunAgentstelemetryMetadataTypeDef = TypedDict(
    "_ListAssessmentRunAgentsPaginateResponseassessmentRunAgentstelemetryMetadataTypeDef",
    {"messageType": str, "count": int, "dataSize": int},
    total=False,
)


class ListAssessmentRunAgentsPaginateResponseassessmentRunAgentstelemetryMetadataTypeDef(
    _ListAssessmentRunAgentsPaginateResponseassessmentRunAgentstelemetryMetadataTypeDef
):
    """
    Type definition for `ListAssessmentRunAgentsPaginateResponseassessmentRunAgents` `telemetryMetadata`

    The metadata about the Amazon Inspector application data metrics collected by the
    agent. This data type is used as the response element in the  GetTelemetryMetadata
    action.

    - **messageType** *(string) --*

      A specific type of behavioral data that is collected by the agent.

    - **count** *(integer) --*

      The count of messages that the agent sends to the Amazon Inspector service.

    - **dataSize** *(integer) --*

      The data size of messages that the agent sends to the Amazon Inspector service.
    """


_ListAssessmentRunAgentsPaginateResponseassessmentRunAgentsTypeDef = TypedDict(
    "_ListAssessmentRunAgentsPaginateResponseassessmentRunAgentsTypeDef",
    {
        "agentId": str,
        "assessmentRunArn": str,
        "agentHealth": str,
        "agentHealthCode": str,
        "agentHealthDetails": str,
        "autoScalingGroup": str,
        "telemetryMetadata": List[
            ListAssessmentRunAgentsPaginateResponseassessmentRunAgentstelemetryMetadataTypeDef
        ],
    },
    total=False,
)


class ListAssessmentRunAgentsPaginateResponseassessmentRunAgentsTypeDef(
    _ListAssessmentRunAgentsPaginateResponseassessmentRunAgentsTypeDef
):
    """
    Type definition for `ListAssessmentRunAgentsPaginateResponse` `assessmentRunAgents`

    Contains information about an Amazon Inspector agent. This data type is used as a response
    element in the  ListAssessmentRunAgents action.

    - **agentId** *(string) --*

      The AWS account of the EC2 instance where the agent is installed.

    - **assessmentRunArn** *(string) --*

      The ARN of the assessment run that is associated with the agent.

    - **agentHealth** *(string) --*

      The current health state of the agent.

    - **agentHealthCode** *(string) --*

      The detailed health state of the agent.

    - **agentHealthDetails** *(string) --*

      The description for the agent health code.

    - **autoScalingGroup** *(string) --*

      The Auto Scaling group of the EC2 instance that is specified by the agent ID.

    - **telemetryMetadata** *(list) --*

      The Amazon Inspector application data metrics that are collected by the agent.

      - *(dict) --*

        The metadata about the Amazon Inspector application data metrics collected by the
        agent. This data type is used as the response element in the  GetTelemetryMetadata
        action.

        - **messageType** *(string) --*

          A specific type of behavioral data that is collected by the agent.

        - **count** *(integer) --*

          The count of messages that the agent sends to the Amazon Inspector service.

        - **dataSize** *(integer) --*

          The data size of messages that the agent sends to the Amazon Inspector service.
    """


_ListAssessmentRunAgentsPaginateResponseTypeDef = TypedDict(
    "_ListAssessmentRunAgentsPaginateResponseTypeDef",
    {
        "assessmentRunAgents": List[
            ListAssessmentRunAgentsPaginateResponseassessmentRunAgentsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListAssessmentRunAgentsPaginateResponseTypeDef(
    _ListAssessmentRunAgentsPaginateResponseTypeDef
):
    """
    Type definition for `ListAssessmentRunAgentsPaginate` `Response`

    - **assessmentRunAgents** *(list) --*

      A list of ARNs that specifies the agents returned by the action.

      - *(dict) --*

        Contains information about an Amazon Inspector agent. This data type is used as a response
        element in the  ListAssessmentRunAgents action.

        - **agentId** *(string) --*

          The AWS account of the EC2 instance where the agent is installed.

        - **assessmentRunArn** *(string) --*

          The ARN of the assessment run that is associated with the agent.

        - **agentHealth** *(string) --*

          The current health state of the agent.

        - **agentHealthCode** *(string) --*

          The detailed health state of the agent.

        - **agentHealthDetails** *(string) --*

          The description for the agent health code.

        - **autoScalingGroup** *(string) --*

          The Auto Scaling group of the EC2 instance that is specified by the agent ID.

        - **telemetryMetadata** *(list) --*

          The Amazon Inspector application data metrics that are collected by the agent.

          - *(dict) --*

            The metadata about the Amazon Inspector application data metrics collected by the
            agent. This data type is used as the response element in the  GetTelemetryMetadata
            action.

            - **messageType** *(string) --*

              A specific type of behavioral data that is collected by the agent.

            - **count** *(integer) --*

              The count of messages that the agent sends to the Amazon Inspector service.

            - **dataSize** *(integer) --*

              The data size of messages that the agent sends to the Amazon Inspector service.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListAssessmentRunAgentsPaginatefilterTypeDef = TypedDict(
    "_ListAssessmentRunAgentsPaginatefilterTypeDef",
    {"agentHealths": List[str], "agentHealthCodes": List[str]},
)


class ListAssessmentRunAgentsPaginatefilterTypeDef(
    _ListAssessmentRunAgentsPaginatefilterTypeDef
):
    """
    Type definition for `ListAssessmentRunAgentsPaginate` `filter`

    You can use this parameter to specify a subset of data to be included in the action's response.

    For a record to match a filter, all specified filter attributes must match. When multiple values
    are specified for a filter attribute, any of the values can match.

    - **agentHealths** *(list) --* **[REQUIRED]**

      The current health state of the agent. Values can be set to **HEALTHY** or **UNHEALTHY** .

      - *(string) --*

    - **agentHealthCodes** *(list) --* **[REQUIRED]**

      The detailed health state of the agent. Values can be set to **IDLE** , **RUNNING** ,
      **SHUTDOWN** , **UNHEALTHY** , **THROTTLED** , and **UNKNOWN** .

      - *(string) --*
    """


_ListAssessmentRunsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAssessmentRunsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAssessmentRunsPaginatePaginationConfigTypeDef(
    _ListAssessmentRunsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAssessmentRunsPaginate` `PaginationConfig`

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


_ListAssessmentRunsPaginateResponseTypeDef = TypedDict(
    "_ListAssessmentRunsPaginateResponseTypeDef",
    {"assessmentRunArns": List[str], "NextToken": str},
    total=False,
)


class ListAssessmentRunsPaginateResponseTypeDef(
    _ListAssessmentRunsPaginateResponseTypeDef
):
    """
    Type definition for `ListAssessmentRunsPaginate` `Response`

    - **assessmentRunArns** *(list) --*

      A list of ARNs that specifies the assessment runs that are returned by the action.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListAssessmentRunsPaginatefiltercompletionTimeRangeTypeDef = TypedDict(
    "_ListAssessmentRunsPaginatefiltercompletionTimeRangeTypeDef",
    {"beginDate": datetime, "endDate": datetime},
    total=False,
)


class ListAssessmentRunsPaginatefiltercompletionTimeRangeTypeDef(
    _ListAssessmentRunsPaginatefiltercompletionTimeRangeTypeDef
):
    """
    Type definition for `ListAssessmentRunsPaginatefilter` `completionTimeRange`

    For a record to match a filter, the value that is specified for this data type property must
    inclusively match any value between the specified minimum and maximum values of the
    **completedAt** property of the  AssessmentRun data type.

    - **beginDate** *(datetime) --*

      The minimum value of the timestamp range.

    - **endDate** *(datetime) --*

      The maximum value of the timestamp range.
    """


_ListAssessmentRunsPaginatefilterdurationRangeTypeDef = TypedDict(
    "_ListAssessmentRunsPaginatefilterdurationRangeTypeDef",
    {"minSeconds": int, "maxSeconds": int},
    total=False,
)


class ListAssessmentRunsPaginatefilterdurationRangeTypeDef(
    _ListAssessmentRunsPaginatefilterdurationRangeTypeDef
):
    """
    Type definition for `ListAssessmentRunsPaginatefilter` `durationRange`

    For a record to match a filter, the value that is specified for this data type property must
    inclusively match any value between the specified minimum and maximum values of the
    **durationInSeconds** property of the  AssessmentRun data type.

    - **minSeconds** *(integer) --*

      The minimum value of the duration range. Must be greater than zero.

    - **maxSeconds** *(integer) --*

      The maximum value of the duration range. Must be less than or equal to 604800 seconds (1
      week).
    """


_ListAssessmentRunsPaginatefilterstartTimeRangeTypeDef = TypedDict(
    "_ListAssessmentRunsPaginatefilterstartTimeRangeTypeDef",
    {"beginDate": datetime, "endDate": datetime},
    total=False,
)


class ListAssessmentRunsPaginatefilterstartTimeRangeTypeDef(
    _ListAssessmentRunsPaginatefilterstartTimeRangeTypeDef
):
    """
    Type definition for `ListAssessmentRunsPaginatefilter` `startTimeRange`

    For a record to match a filter, the value that is specified for this data type property must
    inclusively match any value between the specified minimum and maximum values of the
    **startTime** property of the  AssessmentRun data type.

    - **beginDate** *(datetime) --*

      The minimum value of the timestamp range.

    - **endDate** *(datetime) --*

      The maximum value of the timestamp range.
    """


_ListAssessmentRunsPaginatefilterstateChangeTimeRangeTypeDef = TypedDict(
    "_ListAssessmentRunsPaginatefilterstateChangeTimeRangeTypeDef",
    {"beginDate": datetime, "endDate": datetime},
    total=False,
)


class ListAssessmentRunsPaginatefilterstateChangeTimeRangeTypeDef(
    _ListAssessmentRunsPaginatefilterstateChangeTimeRangeTypeDef
):
    """
    Type definition for `ListAssessmentRunsPaginatefilter` `stateChangeTimeRange`

    For a record to match a filter, the value that is specified for this data type property must
    match the **stateChangedAt** property of the  AssessmentRun data type.

    - **beginDate** *(datetime) --*

      The minimum value of the timestamp range.

    - **endDate** *(datetime) --*

      The maximum value of the timestamp range.
    """


_ListAssessmentRunsPaginatefilterTypeDef = TypedDict(
    "_ListAssessmentRunsPaginatefilterTypeDef",
    {
        "namePattern": str,
        "states": List[str],
        "durationRange": ListAssessmentRunsPaginatefilterdurationRangeTypeDef,
        "rulesPackageArns": List[str],
        "startTimeRange": ListAssessmentRunsPaginatefilterstartTimeRangeTypeDef,
        "completionTimeRange": ListAssessmentRunsPaginatefiltercompletionTimeRangeTypeDef,
        "stateChangeTimeRange": ListAssessmentRunsPaginatefilterstateChangeTimeRangeTypeDef,
    },
    total=False,
)


class ListAssessmentRunsPaginatefilterTypeDef(_ListAssessmentRunsPaginatefilterTypeDef):
    """
    Type definition for `ListAssessmentRunsPaginate` `filter`

    You can use this parameter to specify a subset of data to be included in the action's response.

    For a record to match a filter, all specified filter attributes must match. When multiple values
    are specified for a filter attribute, any of the values can match.

    - **namePattern** *(string) --*

      For a record to match a filter, an explicit value or a string containing a wildcard that is
      specified for this data type property must match the value of the **assessmentRunName**
      property of the  AssessmentRun data type.

    - **states** *(list) --*

      For a record to match a filter, one of the values specified for this data type property must be
      the exact match of the value of the **assessmentRunState** property of the  AssessmentRun data
      type.

      - *(string) --*

    - **durationRange** *(dict) --*

      For a record to match a filter, the value that is specified for this data type property must
      inclusively match any value between the specified minimum and maximum values of the
      **durationInSeconds** property of the  AssessmentRun data type.

      - **minSeconds** *(integer) --*

        The minimum value of the duration range. Must be greater than zero.

      - **maxSeconds** *(integer) --*

        The maximum value of the duration range. Must be less than or equal to 604800 seconds (1
        week).

    - **rulesPackageArns** *(list) --*

      For a record to match a filter, the value that is specified for this data type property must be
      contained in the list of values of the **rulesPackages** property of the  AssessmentRun data
      type.

      - *(string) --*

    - **startTimeRange** *(dict) --*

      For a record to match a filter, the value that is specified for this data type property must
      inclusively match any value between the specified minimum and maximum values of the
      **startTime** property of the  AssessmentRun data type.

      - **beginDate** *(datetime) --*

        The minimum value of the timestamp range.

      - **endDate** *(datetime) --*

        The maximum value of the timestamp range.

    - **completionTimeRange** *(dict) --*

      For a record to match a filter, the value that is specified for this data type property must
      inclusively match any value between the specified minimum and maximum values of the
      **completedAt** property of the  AssessmentRun data type.

      - **beginDate** *(datetime) --*

        The minimum value of the timestamp range.

      - **endDate** *(datetime) --*

        The maximum value of the timestamp range.

    - **stateChangeTimeRange** *(dict) --*

      For a record to match a filter, the value that is specified for this data type property must
      match the **stateChangedAt** property of the  AssessmentRun data type.

      - **beginDate** *(datetime) --*

        The minimum value of the timestamp range.

      - **endDate** *(datetime) --*

        The maximum value of the timestamp range.
    """


_ListAssessmentTargetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAssessmentTargetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAssessmentTargetsPaginatePaginationConfigTypeDef(
    _ListAssessmentTargetsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAssessmentTargetsPaginate` `PaginationConfig`

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


_ListAssessmentTargetsPaginateResponseTypeDef = TypedDict(
    "_ListAssessmentTargetsPaginateResponseTypeDef",
    {"assessmentTargetArns": List[str], "NextToken": str},
    total=False,
)


class ListAssessmentTargetsPaginateResponseTypeDef(
    _ListAssessmentTargetsPaginateResponseTypeDef
):
    """
    Type definition for `ListAssessmentTargetsPaginate` `Response`

    - **assessmentTargetArns** *(list) --*

      A list of ARNs that specifies the assessment targets that are returned by the action.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListAssessmentTargetsPaginatefilterTypeDef = TypedDict(
    "_ListAssessmentTargetsPaginatefilterTypeDef",
    {"assessmentTargetNamePattern": str},
    total=False,
)


class ListAssessmentTargetsPaginatefilterTypeDef(
    _ListAssessmentTargetsPaginatefilterTypeDef
):
    """
    Type definition for `ListAssessmentTargetsPaginate` `filter`

    You can use this parameter to specify a subset of data to be included in the action's response.

    For a record to match a filter, all specified filter attributes must match. When multiple values
    are specified for a filter attribute, any of the values can match.

    - **assessmentTargetNamePattern** *(string) --*

      For a record to match a filter, an explicit value or a string that contains a wildcard that is
      specified for this data type property must match the value of the **assessmentTargetName**
      property of the  AssessmentTarget data type.
    """


_ListAssessmentTemplatesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAssessmentTemplatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAssessmentTemplatesPaginatePaginationConfigTypeDef(
    _ListAssessmentTemplatesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAssessmentTemplatesPaginate` `PaginationConfig`

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


_ListAssessmentTemplatesPaginateResponseTypeDef = TypedDict(
    "_ListAssessmentTemplatesPaginateResponseTypeDef",
    {"assessmentTemplateArns": List[str], "NextToken": str},
    total=False,
)


class ListAssessmentTemplatesPaginateResponseTypeDef(
    _ListAssessmentTemplatesPaginateResponseTypeDef
):
    """
    Type definition for `ListAssessmentTemplatesPaginate` `Response`

    - **assessmentTemplateArns** *(list) --*

      A list of ARNs that specifies the assessment templates returned by the action.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListAssessmentTemplatesPaginatefilterdurationRangeTypeDef = TypedDict(
    "_ListAssessmentTemplatesPaginatefilterdurationRangeTypeDef",
    {"minSeconds": int, "maxSeconds": int},
    total=False,
)


class ListAssessmentTemplatesPaginatefilterdurationRangeTypeDef(
    _ListAssessmentTemplatesPaginatefilterdurationRangeTypeDef
):
    """
    Type definition for `ListAssessmentTemplatesPaginatefilter` `durationRange`

    For a record to match a filter, the value specified for this data type property must
    inclusively match any value between the specified minimum and maximum values of the
    **durationInSeconds** property of the  AssessmentTemplate data type.

    - **minSeconds** *(integer) --*

      The minimum value of the duration range. Must be greater than zero.

    - **maxSeconds** *(integer) --*

      The maximum value of the duration range. Must be less than or equal to 604800 seconds (1
      week).
    """


_ListAssessmentTemplatesPaginatefilterTypeDef = TypedDict(
    "_ListAssessmentTemplatesPaginatefilterTypeDef",
    {
        "namePattern": str,
        "durationRange": ListAssessmentTemplatesPaginatefilterdurationRangeTypeDef,
        "rulesPackageArns": List[str],
    },
    total=False,
)


class ListAssessmentTemplatesPaginatefilterTypeDef(
    _ListAssessmentTemplatesPaginatefilterTypeDef
):
    """
    Type definition for `ListAssessmentTemplatesPaginate` `filter`

    You can use this parameter to specify a subset of data to be included in the action's response.

    For a record to match a filter, all specified filter attributes must match. When multiple values
    are specified for a filter attribute, any of the values can match.

    - **namePattern** *(string) --*

      For a record to match a filter, an explicit value or a string that contains a wildcard that is
      specified for this data type property must match the value of the **assessmentTemplateName**
      property of the  AssessmentTemplate data type.

    - **durationRange** *(dict) --*

      For a record to match a filter, the value specified for this data type property must
      inclusively match any value between the specified minimum and maximum values of the
      **durationInSeconds** property of the  AssessmentTemplate data type.

      - **minSeconds** *(integer) --*

        The minimum value of the duration range. Must be greater than zero.

      - **maxSeconds** *(integer) --*

        The maximum value of the duration range. Must be less than or equal to 604800 seconds (1
        week).

    - **rulesPackageArns** *(list) --*

      For a record to match a filter, the values that are specified for this data type property must
      be contained in the list of values of the **rulesPackageArns** property of the
      AssessmentTemplate data type.

      - *(string) --*
    """


_ListEventSubscriptionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListEventSubscriptionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListEventSubscriptionsPaginatePaginationConfigTypeDef(
    _ListEventSubscriptionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListEventSubscriptionsPaginate` `PaginationConfig`

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


_ListEventSubscriptionsPaginateResponsesubscriptionseventSubscriptionsTypeDef = TypedDict(
    "_ListEventSubscriptionsPaginateResponsesubscriptionseventSubscriptionsTypeDef",
    {"event": str, "subscribedAt": datetime},
    total=False,
)


class ListEventSubscriptionsPaginateResponsesubscriptionseventSubscriptionsTypeDef(
    _ListEventSubscriptionsPaginateResponsesubscriptionseventSubscriptionsTypeDef
):
    """
    Type definition for `ListEventSubscriptionsPaginateResponsesubscriptions` `eventSubscriptions`

    This data type is used in the  Subscription data type.

    - **event** *(string) --*

      The event for which Amazon Simple Notification Service (SNS) notifications are sent.

    - **subscribedAt** *(datetime) --*

      The time at which  SubscribeToEvent is called.
    """


_ListEventSubscriptionsPaginateResponsesubscriptionsTypeDef = TypedDict(
    "_ListEventSubscriptionsPaginateResponsesubscriptionsTypeDef",
    {
        "resourceArn": str,
        "topicArn": str,
        "eventSubscriptions": List[
            ListEventSubscriptionsPaginateResponsesubscriptionseventSubscriptionsTypeDef
        ],
    },
    total=False,
)


class ListEventSubscriptionsPaginateResponsesubscriptionsTypeDef(
    _ListEventSubscriptionsPaginateResponsesubscriptionsTypeDef
):
    """
    Type definition for `ListEventSubscriptionsPaginateResponse` `subscriptions`

    This data type is used as a response element in the  ListEventSubscriptions action.

    - **resourceArn** *(string) --*

      The ARN of the assessment template that is used during the event for which the SNS
      notification is sent.

    - **topicArn** *(string) --*

      The ARN of the Amazon Simple Notification Service (SNS) topic to which the SNS
      notifications are sent.

    - **eventSubscriptions** *(list) --*

      The list of existing event subscriptions.

      - *(dict) --*

        This data type is used in the  Subscription data type.

        - **event** *(string) --*

          The event for which Amazon Simple Notification Service (SNS) notifications are sent.

        - **subscribedAt** *(datetime) --*

          The time at which  SubscribeToEvent is called.
    """


_ListEventSubscriptionsPaginateResponseTypeDef = TypedDict(
    "_ListEventSubscriptionsPaginateResponseTypeDef",
    {
        "subscriptions": List[
            ListEventSubscriptionsPaginateResponsesubscriptionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListEventSubscriptionsPaginateResponseTypeDef(
    _ListEventSubscriptionsPaginateResponseTypeDef
):
    """
    Type definition for `ListEventSubscriptionsPaginate` `Response`

    - **subscriptions** *(list) --*

      Details of the returned event subscriptions.

      - *(dict) --*

        This data type is used as a response element in the  ListEventSubscriptions action.

        - **resourceArn** *(string) --*

          The ARN of the assessment template that is used during the event for which the SNS
          notification is sent.

        - **topicArn** *(string) --*

          The ARN of the Amazon Simple Notification Service (SNS) topic to which the SNS
          notifications are sent.

        - **eventSubscriptions** *(list) --*

          The list of existing event subscriptions.

          - *(dict) --*

            This data type is used in the  Subscription data type.

            - **event** *(string) --*

              The event for which Amazon Simple Notification Service (SNS) notifications are sent.

            - **subscribedAt** *(datetime) --*

              The time at which  SubscribeToEvent is called.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListExclusionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListExclusionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListExclusionsPaginatePaginationConfigTypeDef(
    _ListExclusionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListExclusionsPaginate` `PaginationConfig`

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


_ListExclusionsPaginateResponseTypeDef = TypedDict(
    "_ListExclusionsPaginateResponseTypeDef",
    {"exclusionArns": List[str], "NextToken": str},
    total=False,
)


class ListExclusionsPaginateResponseTypeDef(_ListExclusionsPaginateResponseTypeDef):
    """
    Type definition for `ListExclusionsPaginate` `Response`

    - **exclusionArns** *(list) --*

      A list of exclusions' ARNs returned by the action.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListFindingsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListFindingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListFindingsPaginatePaginationConfigTypeDef(
    _ListFindingsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListFindingsPaginate` `PaginationConfig`

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


_ListFindingsPaginateResponseTypeDef = TypedDict(
    "_ListFindingsPaginateResponseTypeDef",
    {"findingArns": List[str], "NextToken": str},
    total=False,
)


class ListFindingsPaginateResponseTypeDef(_ListFindingsPaginateResponseTypeDef):
    """
    Type definition for `ListFindingsPaginate` `Response`

    - **findingArns** *(list) --*

      A list of ARNs that specifies the findings returned by the action.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_RequiredListFindingsPaginatefilterattributesTypeDef = TypedDict(
    "_RequiredListFindingsPaginatefilterattributesTypeDef", {"key": str}
)
_OptionalListFindingsPaginatefilterattributesTypeDef = TypedDict(
    "_OptionalListFindingsPaginatefilterattributesTypeDef", {"value": str}, total=False
)


class ListFindingsPaginatefilterattributesTypeDef(
    _RequiredListFindingsPaginatefilterattributesTypeDef,
    _OptionalListFindingsPaginatefilterattributesTypeDef,
):
    """
    Type definition for `ListFindingsPaginatefilter` `attributes`

    This data type is used as a request parameter in the  AddAttributesToFindings and
    CreateAssessmentTemplate actions.

    - **key** *(string) --* **[REQUIRED]**

      The attribute key.

    - **value** *(string) --*

      The value assigned to the attribute key.
    """


_ListFindingsPaginatefiltercreationTimeRangeTypeDef = TypedDict(
    "_ListFindingsPaginatefiltercreationTimeRangeTypeDef",
    {"beginDate": datetime, "endDate": datetime},
    total=False,
)


class ListFindingsPaginatefiltercreationTimeRangeTypeDef(
    _ListFindingsPaginatefiltercreationTimeRangeTypeDef
):
    """
    Type definition for `ListFindingsPaginatefilter` `creationTimeRange`

    The time range during which the finding is generated.

    - **beginDate** *(datetime) --*

      The minimum value of the timestamp range.

    - **endDate** *(datetime) --*

      The maximum value of the timestamp range.
    """


_RequiredListFindingsPaginatefilteruserAttributesTypeDef = TypedDict(
    "_RequiredListFindingsPaginatefilteruserAttributesTypeDef", {"key": str}
)
_OptionalListFindingsPaginatefilteruserAttributesTypeDef = TypedDict(
    "_OptionalListFindingsPaginatefilteruserAttributesTypeDef",
    {"value": str},
    total=False,
)


class ListFindingsPaginatefilteruserAttributesTypeDef(
    _RequiredListFindingsPaginatefilteruserAttributesTypeDef,
    _OptionalListFindingsPaginatefilteruserAttributesTypeDef,
):
    """
    Type definition for `ListFindingsPaginatefilter` `userAttributes`

    This data type is used as a request parameter in the  AddAttributesToFindings and
    CreateAssessmentTemplate actions.

    - **key** *(string) --* **[REQUIRED]**

      The attribute key.

    - **value** *(string) --*

      The value assigned to the attribute key.
    """


_ListFindingsPaginatefilterTypeDef = TypedDict(
    "_ListFindingsPaginatefilterTypeDef",
    {
        "agentIds": List[str],
        "autoScalingGroups": List[str],
        "ruleNames": List[str],
        "severities": List[str],
        "rulesPackageArns": List[str],
        "attributes": List[ListFindingsPaginatefilterattributesTypeDef],
        "userAttributes": List[ListFindingsPaginatefilteruserAttributesTypeDef],
        "creationTimeRange": ListFindingsPaginatefiltercreationTimeRangeTypeDef,
    },
    total=False,
)


class ListFindingsPaginatefilterTypeDef(_ListFindingsPaginatefilterTypeDef):
    """
    Type definition for `ListFindingsPaginate` `filter`

    You can use this parameter to specify a subset of data to be included in the action's response.

    For a record to match a filter, all specified filter attributes must match. When multiple values
    are specified for a filter attribute, any of the values can match.

    - **agentIds** *(list) --*

      For a record to match a filter, one of the values that is specified for this data type property
      must be the exact match of the value of the **agentId** property of the  Finding data type.

      - *(string) --*

    - **autoScalingGroups** *(list) --*

      For a record to match a filter, one of the values that is specified for this data type property
      must be the exact match of the value of the **autoScalingGroup** property of the  Finding data
      type.

      - *(string) --*

    - **ruleNames** *(list) --*

      For a record to match a filter, one of the values that is specified for this data type property
      must be the exact match of the value of the **ruleName** property of the  Finding data type.

      - *(string) --*

    - **severities** *(list) --*

      For a record to match a filter, one of the values that is specified for this data type property
      must be the exact match of the value of the **severity** property of the  Finding data type.

      - *(string) --*

    - **rulesPackageArns** *(list) --*

      For a record to match a filter, one of the values that is specified for this data type property
      must be the exact match of the value of the **rulesPackageArn** property of the  Finding data
      type.

      - *(string) --*

    - **attributes** *(list) --*

      For a record to match a filter, the list of values that are specified for this data type
      property must be contained in the list of values of the **attributes** property of the  Finding
      data type.

      - *(dict) --*

        This data type is used as a request parameter in the  AddAttributesToFindings and
        CreateAssessmentTemplate actions.

        - **key** *(string) --* **[REQUIRED]**

          The attribute key.

        - **value** *(string) --*

          The value assigned to the attribute key.

    - **userAttributes** *(list) --*

      For a record to match a filter, the value that is specified for this data type property must be
      contained in the list of values of the **userAttributes** property of the  Finding data type.

      - *(dict) --*

        This data type is used as a request parameter in the  AddAttributesToFindings and
        CreateAssessmentTemplate actions.

        - **key** *(string) --* **[REQUIRED]**

          The attribute key.

        - **value** *(string) --*

          The value assigned to the attribute key.

    - **creationTimeRange** *(dict) --*

      The time range during which the finding is generated.

      - **beginDate** *(datetime) --*

        The minimum value of the timestamp range.

      - **endDate** *(datetime) --*

        The maximum value of the timestamp range.
    """


_ListRulesPackagesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRulesPackagesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRulesPackagesPaginatePaginationConfigTypeDef(
    _ListRulesPackagesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListRulesPackagesPaginate` `PaginationConfig`

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


_ListRulesPackagesPaginateResponseTypeDef = TypedDict(
    "_ListRulesPackagesPaginateResponseTypeDef",
    {"rulesPackageArns": List[str], "NextToken": str},
    total=False,
)


class ListRulesPackagesPaginateResponseTypeDef(
    _ListRulesPackagesPaginateResponseTypeDef
):
    """
    Type definition for `ListRulesPackagesPaginate` `Response`

    - **rulesPackageArns** *(list) --*

      The list of ARNs that specifies the rules packages returned by the action.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_PreviewAgentsPaginatePaginationConfigTypeDef = TypedDict(
    "_PreviewAgentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class PreviewAgentsPaginatePaginationConfigTypeDef(
    _PreviewAgentsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `PreviewAgentsPaginate` `PaginationConfig`

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


_PreviewAgentsPaginateResponseagentPreviewsTypeDef = TypedDict(
    "_PreviewAgentsPaginateResponseagentPreviewsTypeDef",
    {
        "hostname": str,
        "agentId": str,
        "autoScalingGroup": str,
        "agentHealth": str,
        "agentVersion": str,
        "operatingSystem": str,
        "kernelVersion": str,
        "ipv4Address": str,
    },
    total=False,
)


class PreviewAgentsPaginateResponseagentPreviewsTypeDef(
    _PreviewAgentsPaginateResponseagentPreviewsTypeDef
):
    """
    Type definition for `PreviewAgentsPaginateResponse` `agentPreviews`

    Used as a response element in the  PreviewAgents action.

    - **hostname** *(string) --*

      The hostname of the EC2 instance on which the Amazon Inspector Agent is installed.

    - **agentId** *(string) --*

      The ID of the EC2 instance where the agent is installed.

    - **autoScalingGroup** *(string) --*

      The Auto Scaling group for the EC2 instance where the agent is installed.

    - **agentHealth** *(string) --*

      The health status of the Amazon Inspector Agent.

    - **agentVersion** *(string) --*

      The version of the Amazon Inspector Agent.

    - **operatingSystem** *(string) --*

      The operating system running on the EC2 instance on which the Amazon Inspector Agent is
      installed.

    - **kernelVersion** *(string) --*

      The kernel version of the operating system running on the EC2 instance on which the
      Amazon Inspector Agent is installed.

    - **ipv4Address** *(string) --*

      The IP address of the EC2 instance on which the Amazon Inspector Agent is installed.
    """


_PreviewAgentsPaginateResponseTypeDef = TypedDict(
    "_PreviewAgentsPaginateResponseTypeDef",
    {
        "agentPreviews": List[PreviewAgentsPaginateResponseagentPreviewsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class PreviewAgentsPaginateResponseTypeDef(_PreviewAgentsPaginateResponseTypeDef):
    """
    Type definition for `PreviewAgentsPaginate` `Response`

    - **agentPreviews** *(list) --*

      The resulting list of agents.

      - *(dict) --*

        Used as a response element in the  PreviewAgents action.

        - **hostname** *(string) --*

          The hostname of the EC2 instance on which the Amazon Inspector Agent is installed.

        - **agentId** *(string) --*

          The ID of the EC2 instance where the agent is installed.

        - **autoScalingGroup** *(string) --*

          The Auto Scaling group for the EC2 instance where the agent is installed.

        - **agentHealth** *(string) --*

          The health status of the Amazon Inspector Agent.

        - **agentVersion** *(string) --*

          The version of the Amazon Inspector Agent.

        - **operatingSystem** *(string) --*

          The operating system running on the EC2 instance on which the Amazon Inspector Agent is
          installed.

        - **kernelVersion** *(string) --*

          The kernel version of the operating system running on the EC2 instance on which the
          Amazon Inspector Agent is installed.

        - **ipv4Address** *(string) --*

          The IP address of the EC2 instance on which the Amazon Inspector Agent is installed.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """
