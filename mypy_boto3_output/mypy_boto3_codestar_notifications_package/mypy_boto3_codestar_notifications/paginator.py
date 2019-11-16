"Main interface for codestar-notifications Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_codestar_notifications.type_defs import (
    ListEventTypesPaginateFiltersTypeDef,
    ListEventTypesPaginatePaginationConfigTypeDef,
    ListEventTypesPaginateResponseTypeDef,
    ListNotificationRulesPaginateFiltersTypeDef,
    ListNotificationRulesPaginatePaginationConfigTypeDef,
    ListNotificationRulesPaginateResponseTypeDef,
    ListTargetsPaginateFiltersTypeDef,
    ListTargetsPaginatePaginationConfigTypeDef,
    ListTargetsPaginateResponseTypeDef,
)


__all__ = (
    "ListEventTypesPaginator",
    "ListNotificationRulesPaginator",
    "ListTargetsPaginator",
)


class ListEventTypesPaginator(Boto3Paginator):
    """
    Paginator for `list_event_types`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[ListEventTypesPaginateFiltersTypeDef] = None,
        PaginationConfig: ListEventTypesPaginatePaginationConfigTypeDef = None,
    ) -> ListEventTypesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CodeStarNotifications.Client.list_event_types`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codestar-notifications-2019-10-15/ListEventTypes>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'RESOURCE_TYPE'|'SERVICE_NAME',
                      'Value': 'string'
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type Filters: list
        :param Filters:

          The filters to use to return information by service or resource type.

          - *(dict) --*

            Information about a filter to apply to the list of returned event types. You can filter by
            resource type or service name.

            - **Name** *(string) --* **[REQUIRED]**

              The system-generated name of the filter type you want to filter by.

            - **Value** *(string) --* **[REQUIRED]**

              The name of the resource type (for example, pipeline) or service name (for example,
              CodePipeline) that you want to filter by.

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'EventTypes': [
                    {
                        'EventTypeId': 'string',
                        'ServiceName': 'string',
                        'EventTypeName': 'string',
                        'ResourceType': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

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


class ListNotificationRulesPaginator(Boto3Paginator):
    """
    Paginator for `list_notification_rules`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[ListNotificationRulesPaginateFiltersTypeDef] = None,
        PaginationConfig: ListNotificationRulesPaginatePaginationConfigTypeDef = None,
    ) -> ListNotificationRulesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CodeStarNotifications.Client.list_notification_rules`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codestar-notifications-2019-10-15/ListNotificationRules>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'EVENT_TYPE_ID'|'CREATED_BY'|'RESOURCE'|'TARGET_ADDRESS',
                      'Value': 'string'
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type Filters: list
        :param Filters:

          The filters to use to return information by service or resource type. For valid values, see
          ListNotificationRulesFilter .

          .. note::

            A filter with the same name can appear more than once when used with OR statements. Filters
            with different names should be applied with AND statements.

          - *(dict) --*

            Information about a filter to apply to the list of returned notification rules. You can filter
            by event type, owner, resource, or target.

            - **Name** *(string) --* **[REQUIRED]**

              The name of the attribute you want to use to filter the returned notification rules.

            - **Value** *(string) --* **[REQUIRED]**

              The value of the attribute you want to use to filter the returned notification rules. For
              example, if you specify filtering by *RESOURCE* in Name, you might specify the ARN of a
              pipeline in AWS CodePipeline for the value.

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NotificationRules': [
                    {
                        'Id': 'string',
                        'Arn': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **NotificationRules** *(list) --*

              The list of notification rules for the AWS account, by Amazon Resource Name (ARN) and ID.

              - *(dict) --*

                Information about a specified notification rule.

                - **Id** *(string) --*

                  The unique ID of the notification rule.

                - **Arn** *(string) --*

                  The Amazon Resource Name (ARN) of the notification rule.

        """


class ListTargetsPaginator(Boto3Paginator):
    """
    Paginator for `list_targets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[ListTargetsPaginateFiltersTypeDef] = None,
        PaginationConfig: ListTargetsPaginatePaginationConfigTypeDef = None,
    ) -> ListTargetsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CodeStarNotifications.Client.list_targets`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codestar-notifications-2019-10-15/ListTargets>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'TARGET_TYPE'|'TARGET_ADDRESS'|'TARGET_STATUS',
                      'Value': 'string'
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type Filters: list
        :param Filters:

          The filters to use to return information by service or resource type. Valid filters include
          target type, target address, and target status.

          .. note::

            A filter with the same name can appear more than once when used with OR statements. Filters
            with different names should be applied with AND statements.

          - *(dict) --*

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

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Targets': [
                    {
                        'TargetAddress': 'string',
                        'TargetType': 'string',
                        'TargetStatus': 'PENDING'|'ACTIVE'|'UNREACHABLE'|'INACTIVE'|'DEACTIVATED'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

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
