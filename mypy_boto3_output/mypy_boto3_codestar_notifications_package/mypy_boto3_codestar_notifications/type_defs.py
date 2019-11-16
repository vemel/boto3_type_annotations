"Main interface for codestar-notifications type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateNotificationRuleResponseTypeDef",
    "ClientCreateNotificationRuleTargetsTypeDef",
    "ClientDeleteNotificationRuleResponseTypeDef",
    "ClientDescribeNotificationRuleResponseEventTypesTypeDef",
    "ClientDescribeNotificationRuleResponseTargetsTypeDef",
    "ClientDescribeNotificationRuleResponseTypeDef",
    "ClientListEventTypesFiltersTypeDef",
    "ClientListEventTypesResponseEventTypesTypeDef",
    "ClientListEventTypesResponseTypeDef",
    "ClientListNotificationRulesFiltersTypeDef",
    "ClientListNotificationRulesResponseNotificationRulesTypeDef",
    "ClientListNotificationRulesResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTargetsFiltersTypeDef",
    "ClientListTargetsResponseTargetsTypeDef",
    "ClientListTargetsResponseTypeDef",
    "ClientSubscribeResponseTypeDef",
    "ClientSubscribeTargetTypeDef",
    "ClientTagResourceResponseTypeDef",
    "ClientUnsubscribeResponseTypeDef",
    "ClientUpdateNotificationRuleTargetsTypeDef",
    "ListEventTypesPaginateFiltersTypeDef",
    "ListEventTypesPaginatePaginationConfigTypeDef",
    "ListEventTypesPaginateResponseEventTypesTypeDef",
    "ListEventTypesPaginateResponseTypeDef",
    "ListNotificationRulesPaginateFiltersTypeDef",
    "ListNotificationRulesPaginatePaginationConfigTypeDef",
    "ListNotificationRulesPaginateResponseNotificationRulesTypeDef",
    "ListNotificationRulesPaginateResponseTypeDef",
    "ListTargetsPaginateFiltersTypeDef",
    "ListTargetsPaginatePaginationConfigTypeDef",
    "ListTargetsPaginateResponseTargetsTypeDef",
    "ListTargetsPaginateResponseTypeDef",
)


_ClientCreateNotificationRuleResponseTypeDef = TypedDict(
    "_ClientCreateNotificationRuleResponseTypeDef", {"Arn": str}, total=False
)


class ClientCreateNotificationRuleResponseTypeDef(
    _ClientCreateNotificationRuleResponseTypeDef
):
    """
    Type definition for `ClientCreateNotificationRule` `Response`

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the notification rule.
    """


_ClientCreateNotificationRuleTargetsTypeDef = TypedDict(
    "_ClientCreateNotificationRuleTargetsTypeDef",
    {"TargetType": str, "TargetAddress": str},
    total=False,
)


class ClientCreateNotificationRuleTargetsTypeDef(
    _ClientCreateNotificationRuleTargetsTypeDef
):
    """
    Type definition for `ClientCreateNotificationRule` `Targets`

    Information about the SNS topics associated with a notification rule.

    - **TargetType** *(string) --*

      The target type. Can be an Amazon SNS topic.

    - **TargetAddress** *(string) --*

      The Amazon Resource Name (ARN) of the SNS topic.
    """


_ClientDeleteNotificationRuleResponseTypeDef = TypedDict(
    "_ClientDeleteNotificationRuleResponseTypeDef", {"Arn": str}, total=False
)


class ClientDeleteNotificationRuleResponseTypeDef(
    _ClientDeleteNotificationRuleResponseTypeDef
):
    """
    Type definition for `ClientDeleteNotificationRule` `Response`

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the deleted notification rule.
    """


_ClientDescribeNotificationRuleResponseEventTypesTypeDef = TypedDict(
    "_ClientDescribeNotificationRuleResponseEventTypesTypeDef",
    {"EventTypeId": str, "ServiceName": str, "EventTypeName": str, "ResourceType": str},
    total=False,
)


class ClientDescribeNotificationRuleResponseEventTypesTypeDef(
    _ClientDescribeNotificationRuleResponseEventTypesTypeDef
):
    """
    Type definition for `ClientDescribeNotificationRuleResponse` `EventTypes`

    Returns information about an event that has triggered a notification rule.

    - **EventTypeId** *(string) --*

      The system-generated ID of the event.

    - **ServiceName** *(string) --*

      The name of the service for which the event applies.

    - **EventTypeName** *(string) --*

      The name of the event.

    - **ResourceType** *(string) --*

      The resource type of the event.
    """


_ClientDescribeNotificationRuleResponseTargetsTypeDef = TypedDict(
    "_ClientDescribeNotificationRuleResponseTargetsTypeDef",
    {"TargetAddress": str, "TargetType": str, "TargetStatus": str},
    total=False,
)


class ClientDescribeNotificationRuleResponseTargetsTypeDef(
    _ClientDescribeNotificationRuleResponseTargetsTypeDef
):
    """
    Type definition for `ClientDescribeNotificationRuleResponse` `Targets`

    Information about the targets specified for a notification rule.

    - **TargetAddress** *(string) --*

      The Amazon Resource Name (ARN) of the SNS topic.

    - **TargetType** *(string) --*

      The type of the target (for example, SNS).

    - **TargetStatus** *(string) --*

      The status of the target.
    """


_ClientDescribeNotificationRuleResponseTypeDef = TypedDict(
    "_ClientDescribeNotificationRuleResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "EventTypes": List[ClientDescribeNotificationRuleResponseEventTypesTypeDef],
        "Resource": str,
        "Targets": List[ClientDescribeNotificationRuleResponseTargetsTypeDef],
        "DetailType": str,
        "CreatedBy": str,
        "Status": str,
        "CreatedTimestamp": datetime,
        "LastModifiedTimestamp": datetime,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientDescribeNotificationRuleResponseTypeDef(
    _ClientDescribeNotificationRuleResponseTypeDef
):
    """
    Type definition for `ClientDescribeNotificationRule` `Response`

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the notification rule.

    - **Name** *(string) --*

      The name of the notification rule.

    - **EventTypes** *(list) --*

      A list of the event types associated with the notification rule.

      - *(dict) --*

        Returns information about an event that has triggered a notification rule.

        - **EventTypeId** *(string) --*

          The system-generated ID of the event.

        - **ServiceName** *(string) --*

          The name of the service for which the event applies.

        - **EventTypeName** *(string) --*

          The name of the event.

        - **ResourceType** *(string) --*

          The resource type of the event.

    - **Resource** *(string) --*

      The Amazon Resource Name (ARN) of the resource associated with the notification rule.

    - **Targets** *(list) --*

      A list of the SNS topics associated with the notification rule.

      - *(dict) --*

        Information about the targets specified for a notification rule.

        - **TargetAddress** *(string) --*

          The Amazon Resource Name (ARN) of the SNS topic.

        - **TargetType** *(string) --*

          The type of the target (for example, SNS).

        - **TargetStatus** *(string) --*

          The status of the target.

    - **DetailType** *(string) --*

      The level of detail included in the notifications for this resource. BASIC will include only
      the contents of the event as it would appear in AWS CloudWatch. FULL will include any
      supplemental information provided by AWS CodeStar Notifications and/or the service for the
      resource for which the notification is created.

    - **CreatedBy** *(string) --*

      The name or email alias of the person who created the notification rule.

    - **Status** *(string) --*

      The status of the notification rule. Valid statuses are on (sending notifications) or off
      (not sending notifications).

    - **CreatedTimestamp** *(datetime) --*

      The date and time the notification rule was created, in timestamp format.

    - **LastModifiedTimestamp** *(datetime) --*

      The date and time the notification rule was most recently updated, in timestamp format.

    - **Tags** *(dict) --*

      The tags associated with the notification rule.

      - *(string) --*

        - *(string) --*
    """


_ClientListEventTypesFiltersTypeDef = TypedDict(
    "_ClientListEventTypesFiltersTypeDef", {"Name": str, "Value": str}
)


class ClientListEventTypesFiltersTypeDef(_ClientListEventTypesFiltersTypeDef):
    """
    Type definition for `ClientListEventTypes` `Filters`

    Information about a filter to apply to the list of returned event types. You can filter by
    resource type or service name.

    - **Name** *(string) --* **[REQUIRED]**

      The system-generated name of the filter type you want to filter by.

    - **Value** *(string) --* **[REQUIRED]**

      The name of the resource type (for example, pipeline) or service name (for example,
      CodePipeline) that you want to filter by.
    """


_ClientListEventTypesResponseEventTypesTypeDef = TypedDict(
    "_ClientListEventTypesResponseEventTypesTypeDef",
    {"EventTypeId": str, "ServiceName": str, "EventTypeName": str, "ResourceType": str},
    total=False,
)


class ClientListEventTypesResponseEventTypesTypeDef(
    _ClientListEventTypesResponseEventTypesTypeDef
):
    """
    Type definition for `ClientListEventTypesResponse` `EventTypes`

    Returns information about an event that has triggered a notification rule.

    - **EventTypeId** *(string) --*

      The system-generated ID of the event.

    - **ServiceName** *(string) --*

      The name of the service for which the event applies.

    - **EventTypeName** *(string) --*

      The name of the event.

    - **ResourceType** *(string) --*

      The resource type of the event.
    """


_ClientListEventTypesResponseTypeDef = TypedDict(
    "_ClientListEventTypesResponseTypeDef",
    {
        "EventTypes": List[ClientListEventTypesResponseEventTypesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListEventTypesResponseTypeDef(_ClientListEventTypesResponseTypeDef):
    """
    Type definition for `ClientListEventTypes` `Response`

    - **EventTypes** *(list) --*

      Information about each event, including service name, resource type, event ID, and event name.

      - *(dict) --*

        Returns information about an event that has triggered a notification rule.

        - **EventTypeId** *(string) --*

          The system-generated ID of the event.

        - **ServiceName** *(string) --*

          The name of the service for which the event applies.

        - **EventTypeName** *(string) --*

          The name of the event.

        - **ResourceType** *(string) --*

          The resource type of the event.

    - **NextToken** *(string) --*

      An enumeration token that can be used in a request to return the next batch of the results.
    """


_ClientListNotificationRulesFiltersTypeDef = TypedDict(
    "_ClientListNotificationRulesFiltersTypeDef", {"Name": str, "Value": str}
)


class ClientListNotificationRulesFiltersTypeDef(
    _ClientListNotificationRulesFiltersTypeDef
):
    """
    Type definition for `ClientListNotificationRules` `Filters`

    Information about a filter to apply to the list of returned notification rules. You can filter
    by event type, owner, resource, or target.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the attribute you want to use to filter the returned notification rules.

    - **Value** *(string) --* **[REQUIRED]**

      The value of the attribute you want to use to filter the returned notification rules. For
      example, if you specify filtering by *RESOURCE* in Name, you might specify the ARN of a
      pipeline in AWS CodePipeline for the value.
    """


_ClientListNotificationRulesResponseNotificationRulesTypeDef = TypedDict(
    "_ClientListNotificationRulesResponseNotificationRulesTypeDef",
    {"Id": str, "Arn": str},
    total=False,
)


class ClientListNotificationRulesResponseNotificationRulesTypeDef(
    _ClientListNotificationRulesResponseNotificationRulesTypeDef
):
    """
    Type definition for `ClientListNotificationRulesResponse` `NotificationRules`

    Information about a specified notification rule.

    - **Id** *(string) --*

      The unique ID of the notification rule.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the notification rule.
    """


_ClientListNotificationRulesResponseTypeDef = TypedDict(
    "_ClientListNotificationRulesResponseTypeDef",
    {
        "NextToken": str,
        "NotificationRules": List[
            ClientListNotificationRulesResponseNotificationRulesTypeDef
        ],
    },
    total=False,
)


class ClientListNotificationRulesResponseTypeDef(
    _ClientListNotificationRulesResponseTypeDef
):
    """
    Type definition for `ClientListNotificationRules` `Response`

    - **NextToken** *(string) --*

      An enumeration token that can be used in a request to return the next batch of the results.

    - **NotificationRules** *(list) --*

      The list of notification rules for the AWS account, by Amazon Resource Name (ARN) and ID.

      - *(dict) --*

        Information about a specified notification rule.

        - **Id** *(string) --*

          The unique ID of the notification rule.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the notification rule.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **Tags** *(dict) --*

      The tags associated with the notification rule.

      - *(string) --*

        - *(string) --*
    """


_ClientListTargetsFiltersTypeDef = TypedDict(
    "_ClientListTargetsFiltersTypeDef", {"Name": str, "Value": str}
)


class ClientListTargetsFiltersTypeDef(_ClientListTargetsFiltersTypeDef):
    """
    Type definition for `ClientListTargets` `Filters`

    Information about a filter to apply to the list of returned targets. You can filter by target
    type, address, or status. For example, to filter results to notification rules that have active
    Amazon SNS topics as targets, you could specify a ListTargetsFilter Name as TargetType and a
    Value of SNS, and a Name of TARGET_STATUS and a Value of ACTIVE.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the attribute you want to use to filter the returned targets.

    - **Value** *(string) --* **[REQUIRED]**

      The value of the attribute you want to use to filter the returned targets. For example, if
      you specify *SNS* for the Target type, you could specify an Amazon Resource Name (ARN) for a
      topic as the value.
    """


_ClientListTargetsResponseTargetsTypeDef = TypedDict(
    "_ClientListTargetsResponseTargetsTypeDef",
    {"TargetAddress": str, "TargetType": str, "TargetStatus": str},
    total=False,
)


class ClientListTargetsResponseTargetsTypeDef(_ClientListTargetsResponseTargetsTypeDef):
    """
    Type definition for `ClientListTargetsResponse` `Targets`

    Information about the targets specified for a notification rule.

    - **TargetAddress** *(string) --*

      The Amazon Resource Name (ARN) of the SNS topic.

    - **TargetType** *(string) --*

      The type of the target (for example, SNS).

    - **TargetStatus** *(string) --*

      The status of the target.
    """


_ClientListTargetsResponseTypeDef = TypedDict(
    "_ClientListTargetsResponseTypeDef",
    {"Targets": List[ClientListTargetsResponseTargetsTypeDef], "NextToken": str},
    total=False,
)


class ClientListTargetsResponseTypeDef(_ClientListTargetsResponseTypeDef):
    """
    Type definition for `ClientListTargets` `Response`

    - **Targets** *(list) --*

      The list of notification rule targets.

      - *(dict) --*

        Information about the targets specified for a notification rule.

        - **TargetAddress** *(string) --*

          The Amazon Resource Name (ARN) of the SNS topic.

        - **TargetType** *(string) --*

          The type of the target (for example, SNS).

        - **TargetStatus** *(string) --*

          The status of the target.

    - **NextToken** *(string) --*

      An enumeration token that can be used in a request to return the next batch of results.
    """


_ClientSubscribeResponseTypeDef = TypedDict(
    "_ClientSubscribeResponseTypeDef", {"Arn": str}, total=False
)


class ClientSubscribeResponseTypeDef(_ClientSubscribeResponseTypeDef):
    """
    Type definition for `ClientSubscribe` `Response`

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the notification rule for which you have created
      assocations.
    """


_ClientSubscribeTargetTypeDef = TypedDict(
    "_ClientSubscribeTargetTypeDef",
    {"TargetType": str, "TargetAddress": str},
    total=False,
)


class ClientSubscribeTargetTypeDef(_ClientSubscribeTargetTypeDef):
    """
    Type definition for `ClientSubscribe` `Target`

    Information about the SNS topics associated with a notification rule.

    - **TargetType** *(string) --*

      The target type. Can be an Amazon SNS topic.

    - **TargetAddress** *(string) --*

      The Amazon Resource Name (ARN) of the SNS topic.
    """


_ClientTagResourceResponseTypeDef = TypedDict(
    "_ClientTagResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientTagResourceResponseTypeDef(_ClientTagResourceResponseTypeDef):
    """
    Type definition for `ClientTagResource` `Response`

    - **Tags** *(dict) --*

      The list of tags associated with the resource.

      - *(string) --*

        - *(string) --*
    """


_ClientUnsubscribeResponseTypeDef = TypedDict(
    "_ClientUnsubscribeResponseTypeDef", {"Arn": str}, total=False
)


class ClientUnsubscribeResponseTypeDef(_ClientUnsubscribeResponseTypeDef):
    """
    Type definition for `ClientUnsubscribe` `Response`

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the the notification rule from which you have removed a
      subscription.
    """


_ClientUpdateNotificationRuleTargetsTypeDef = TypedDict(
    "_ClientUpdateNotificationRuleTargetsTypeDef",
    {"TargetType": str, "TargetAddress": str},
    total=False,
)


class ClientUpdateNotificationRuleTargetsTypeDef(
    _ClientUpdateNotificationRuleTargetsTypeDef
):
    """
    Type definition for `ClientUpdateNotificationRule` `Targets`

    Information about the SNS topics associated with a notification rule.

    - **TargetType** *(string) --*

      The target type. Can be an Amazon SNS topic.

    - **TargetAddress** *(string) --*

      The Amazon Resource Name (ARN) of the SNS topic.
    """


_ListEventTypesPaginateFiltersTypeDef = TypedDict(
    "_ListEventTypesPaginateFiltersTypeDef", {"Name": str, "Value": str}
)


class ListEventTypesPaginateFiltersTypeDef(_ListEventTypesPaginateFiltersTypeDef):
    """
    Type definition for `ListEventTypesPaginate` `Filters`

    Information about a filter to apply to the list of returned event types. You can filter by
    resource type or service name.

    - **Name** *(string) --* **[REQUIRED]**

      The system-generated name of the filter type you want to filter by.

    - **Value** *(string) --* **[REQUIRED]**

      The name of the resource type (for example, pipeline) or service name (for example,
      CodePipeline) that you want to filter by.
    """


_ListEventTypesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListEventTypesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListEventTypesPaginatePaginationConfigTypeDef(
    _ListEventTypesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListEventTypesPaginate` `PaginationConfig`

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


_ListEventTypesPaginateResponseEventTypesTypeDef = TypedDict(
    "_ListEventTypesPaginateResponseEventTypesTypeDef",
    {"EventTypeId": str, "ServiceName": str, "EventTypeName": str, "ResourceType": str},
    total=False,
)


class ListEventTypesPaginateResponseEventTypesTypeDef(
    _ListEventTypesPaginateResponseEventTypesTypeDef
):
    """
    Type definition for `ListEventTypesPaginateResponse` `EventTypes`

    Returns information about an event that has triggered a notification rule.

    - **EventTypeId** *(string) --*

      The system-generated ID of the event.

    - **ServiceName** *(string) --*

      The name of the service for which the event applies.

    - **EventTypeName** *(string) --*

      The name of the event.

    - **ResourceType** *(string) --*

      The resource type of the event.
    """


_ListEventTypesPaginateResponseTypeDef = TypedDict(
    "_ListEventTypesPaginateResponseTypeDef",
    {"EventTypes": List[ListEventTypesPaginateResponseEventTypesTypeDef]},
    total=False,
)


class ListEventTypesPaginateResponseTypeDef(_ListEventTypesPaginateResponseTypeDef):
    """
    Type definition for `ListEventTypesPaginate` `Response`

    - **EventTypes** *(list) --*

      Information about each event, including service name, resource type, event ID, and event name.

      - *(dict) --*

        Returns information about an event that has triggered a notification rule.

        - **EventTypeId** *(string) --*

          The system-generated ID of the event.

        - **ServiceName** *(string) --*

          The name of the service for which the event applies.

        - **EventTypeName** *(string) --*

          The name of the event.

        - **ResourceType** *(string) --*

          The resource type of the event.
    """


_ListNotificationRulesPaginateFiltersTypeDef = TypedDict(
    "_ListNotificationRulesPaginateFiltersTypeDef", {"Name": str, "Value": str}
)


class ListNotificationRulesPaginateFiltersTypeDef(
    _ListNotificationRulesPaginateFiltersTypeDef
):
    """
    Type definition for `ListNotificationRulesPaginate` `Filters`

    Information about a filter to apply to the list of returned notification rules. You can filter
    by event type, owner, resource, or target.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the attribute you want to use to filter the returned notification rules.

    - **Value** *(string) --* **[REQUIRED]**

      The value of the attribute you want to use to filter the returned notification rules. For
      example, if you specify filtering by *RESOURCE* in Name, you might specify the ARN of a
      pipeline in AWS CodePipeline for the value.
    """


_ListNotificationRulesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListNotificationRulesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListNotificationRulesPaginatePaginationConfigTypeDef(
    _ListNotificationRulesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListNotificationRulesPaginate` `PaginationConfig`

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


_ListNotificationRulesPaginateResponseNotificationRulesTypeDef = TypedDict(
    "_ListNotificationRulesPaginateResponseNotificationRulesTypeDef",
    {"Id": str, "Arn": str},
    total=False,
)


class ListNotificationRulesPaginateResponseNotificationRulesTypeDef(
    _ListNotificationRulesPaginateResponseNotificationRulesTypeDef
):
    """
    Type definition for `ListNotificationRulesPaginateResponse` `NotificationRules`

    Information about a specified notification rule.

    - **Id** *(string) --*

      The unique ID of the notification rule.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the notification rule.
    """


_ListNotificationRulesPaginateResponseTypeDef = TypedDict(
    "_ListNotificationRulesPaginateResponseTypeDef",
    {
        "NotificationRules": List[
            ListNotificationRulesPaginateResponseNotificationRulesTypeDef
        ]
    },
    total=False,
)


class ListNotificationRulesPaginateResponseTypeDef(
    _ListNotificationRulesPaginateResponseTypeDef
):
    """
    Type definition for `ListNotificationRulesPaginate` `Response`

    - **NotificationRules** *(list) --*

      The list of notification rules for the AWS account, by Amazon Resource Name (ARN) and ID.

      - *(dict) --*

        Information about a specified notification rule.

        - **Id** *(string) --*

          The unique ID of the notification rule.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the notification rule.
    """


_ListTargetsPaginateFiltersTypeDef = TypedDict(
    "_ListTargetsPaginateFiltersTypeDef", {"Name": str, "Value": str}
)


class ListTargetsPaginateFiltersTypeDef(_ListTargetsPaginateFiltersTypeDef):
    """
    Type definition for `ListTargetsPaginate` `Filters`

    Information about a filter to apply to the list of returned targets. You can filter by target
    type, address, or status. For example, to filter results to notification rules that have active
    Amazon SNS topics as targets, you could specify a ListTargetsFilter Name as TargetType and a
    Value of SNS, and a Name of TARGET_STATUS and a Value of ACTIVE.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the attribute you want to use to filter the returned targets.

    - **Value** *(string) --* **[REQUIRED]**

      The value of the attribute you want to use to filter the returned targets. For example, if
      you specify *SNS* for the Target type, you could specify an Amazon Resource Name (ARN) for a
      topic as the value.
    """


_ListTargetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTargetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTargetsPaginatePaginationConfigTypeDef(
    _ListTargetsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListTargetsPaginate` `PaginationConfig`

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


_ListTargetsPaginateResponseTargetsTypeDef = TypedDict(
    "_ListTargetsPaginateResponseTargetsTypeDef",
    {"TargetAddress": str, "TargetType": str, "TargetStatus": str},
    total=False,
)


class ListTargetsPaginateResponseTargetsTypeDef(
    _ListTargetsPaginateResponseTargetsTypeDef
):
    """
    Type definition for `ListTargetsPaginateResponse` `Targets`

    Information about the targets specified for a notification rule.

    - **TargetAddress** *(string) --*

      The Amazon Resource Name (ARN) of the SNS topic.

    - **TargetType** *(string) --*

      The type of the target (for example, SNS).

    - **TargetStatus** *(string) --*

      The status of the target.
    """


_ListTargetsPaginateResponseTypeDef = TypedDict(
    "_ListTargetsPaginateResponseTypeDef",
    {"Targets": List[ListTargetsPaginateResponseTargetsTypeDef]},
    total=False,
)


class ListTargetsPaginateResponseTypeDef(_ListTargetsPaginateResponseTypeDef):
    """
    Type definition for `ListTargetsPaginate` `Response`

    - **Targets** *(list) --*

      The list of notification rule targets.

      - *(dict) --*

        Information about the targets specified for a notification rule.

        - **TargetAddress** *(string) --*

          The Amazon Resource Name (ARN) of the SNS topic.

        - **TargetType** *(string) --*

          The type of the target (for example, SNS).

        - **TargetStatus** *(string) --*

          The status of the target.
    """
