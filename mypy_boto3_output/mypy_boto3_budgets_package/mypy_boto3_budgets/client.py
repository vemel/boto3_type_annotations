"Main interface for budgets Client"
from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

# pylint: disable=import-self
import mypy_boto3_budgets.client as client_scope

# pylint: disable=import-self
import mypy_boto3_budgets.paginator as paginator_scope
from mypy_boto3_budgets.type_defs import (
    ClientCreateBudgetBudgetTypeDef,
    ClientCreateBudgetNotificationsWithSubscribersTypeDef,
    ClientCreateNotificationNotificationTypeDef,
    ClientCreateNotificationSubscribersTypeDef,
    ClientCreateSubscriberNotificationTypeDef,
    ClientCreateSubscriberSubscriberTypeDef,
    ClientDeleteNotificationNotificationTypeDef,
    ClientDeleteSubscriberNotificationTypeDef,
    ClientDeleteSubscriberSubscriberTypeDef,
    ClientDescribeBudgetPerformanceHistoryResponseTypeDef,
    ClientDescribeBudgetPerformanceHistoryTimePeriodTypeDef,
    ClientDescribeBudgetResponseTypeDef,
    ClientDescribeBudgetsResponseTypeDef,
    ClientDescribeNotificationsForBudgetResponseTypeDef,
    ClientDescribeSubscribersForNotificationNotificationTypeDef,
    ClientDescribeSubscribersForNotificationResponseTypeDef,
    ClientUpdateBudgetNewBudgetTypeDef,
    ClientUpdateNotificationNewNotificationTypeDef,
    ClientUpdateNotificationOldNotificationTypeDef,
    ClientUpdateSubscriberNewSubscriberTypeDef,
    ClientUpdateSubscriberNotificationTypeDef,
    ClientUpdateSubscriberOldSubscriberTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> None:
        """
        Check if an operation can be paginated.

        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you'd normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator("create_foo")``.

        :return: ``True`` if the operation can be paginated,
            ``False`` otherwise.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_budget(
        self,
        AccountId: str,
        Budget: ClientCreateBudgetBudgetTypeDef,
        NotificationsWithSubscribers: List[
            ClientCreateBudgetNotificationsWithSubscribersTypeDef
        ] = None,
    ) -> Dict:
        """
        Creates a budget and, if included, notifications and subscribers.

        .. warning::

          Only one of ``BudgetLimit`` or ``PlannedBudgetLimits`` can be present in the syntax at one time.
          Use the syntax that matches your case. The Request Syntax section shows the ``BudgetLimit``
          syntax. For ``PlannedBudgetLimits`` , see the `Examples
          <https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_CreateBudget.html#API_CreateBudget_Examples>`__
          section.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/CreateBudget>`_

        **Request Syntax**
        ::

          response = client.create_budget(
              AccountId='string',
              Budget={
                  'BudgetName': 'string',
                  'BudgetLimit': {
                      'Amount': 'string',
                      'Unit': 'string'
                  },
                  'PlannedBudgetLimits': {
                      'string': {
                          'Amount': 'string',
                          'Unit': 'string'
                      }
                  },
                  'CostFilters': {
                      'string': [
                          'string',
                      ]
                  },
                  'CostTypes': {
                      'IncludeTax': True|False,
                      'IncludeSubscription': True|False,
                      'UseBlended': True|False,
                      'IncludeRefund': True|False,
                      'IncludeCredit': True|False,
                      'IncludeUpfront': True|False,
                      'IncludeRecurring': True|False,
                      'IncludeOtherSubscription': True|False,
                      'IncludeSupport': True|False,
                      'IncludeDiscount': True|False,
                      'UseAmortized': True|False
                  },
                  'TimeUnit': 'DAILY'|'MONTHLY'|'QUARTERLY'|'ANNUALLY',
                  'TimePeriod': {
                      'Start': datetime(2015, 1, 1),
                      'End': datetime(2015, 1, 1)
                  },
                  'CalculatedSpend': {
                      'ActualSpend': {
                          'Amount': 'string',
                          'Unit': 'string'
                      },
                      'ForecastedSpend': {
                          'Amount': 'string',
                          'Unit': 'string'
                      }
                  },
                  'BudgetType':
                  'USAGE'|'COST'|'RI_UTILIZATION'|'RI_COVERAGE'|'SAVINGS_PLANS_UTILIZATION'
                  |'SAVINGS_PLANS_COVERAGE',
                  'LastUpdatedTime': datetime(2015, 1, 1)
              },
              NotificationsWithSubscribers=[
                  {
                      'Notification': {
                          'NotificationType': 'ACTUAL'|'FORECASTED',
                          'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
                          'Threshold': 123.0,
                          'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
                          'NotificationState': 'OK'|'ALARM'
                      },
                      'Subscribers': [
                          {
                              'SubscriptionType': 'SNS'|'EMAIL',
                              'Address': 'string'
                          },
                      ]
                  },
              ]
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The ``accountId`` that is associated with the budget.

        :type Budget: dict
        :param Budget: **[REQUIRED]**

          The budget object that you want to create.

          - **BudgetName** *(string) --* **[REQUIRED]**

            The name of a budget. The name must be unique within an account. The ``:`` and ``\\``
            characters aren't allowed in ``BudgetName`` .

          - **BudgetLimit** *(dict) --*

            The total amount of cost, usage, RI utilization, RI coverage, Savings Plans utilization, or
            Savings Plans coverage that you want to track with your budget.

             ``BudgetLimit`` is required for cost or usage budgets, but optional for RI or Savings Plans
             utilization or coverage budgets. RI and Savings Plans utilization or coverage budgets default
             to ``100`` , which is the only valid value for RI or Savings Plans utilization or coverage
             budgets. You can't use ``BudgetLimit`` with ``PlannedBudgetLimits`` for ``CreateBudget`` and
             ``UpdateBudget`` actions.

            - **Amount** *(string) --* **[REQUIRED]**

              The cost or usage amount that is associated with a budget forecast, actual spend, or budget
              threshold.

            - **Unit** *(string) --* **[REQUIRED]**

              The unit of measurement that is used for the budget forecast, actual spend, or budget
              threshold, such as dollars or GB.

          - **PlannedBudgetLimits** *(dict) --*

            A map containing multiple ``BudgetLimit`` , including current or future limits.

             ``PlannedBudgetLimits`` is available for cost or usage budget and supports monthly and
             quarterly ``TimeUnit`` .

            For monthly budgets, provide 12 months of ``PlannedBudgetLimits`` values. This must start from
            the current month and include the next 11 months. The ``key`` is the start of the month,
            ``UTC`` in epoch seconds.

            For quarterly budgets, provide 4 quarters of ``PlannedBudgetLimits`` value entries in standard
            calendar quarter increments. This must start from the current quarter and include the next 3
            quarters. The ``key`` is the start of the quarter, ``UTC`` in epoch seconds.

            If the planned budget expires before 12 months for monthly or 4 quarters for quarterly, provide
            the ``PlannedBudgetLimits`` values only for the remaining periods.

            If the budget begins at a date in the future, provide ``PlannedBudgetLimits`` values from the
            start date of the budget.

            After all of the ``BudgetLimit`` values in ``PlannedBudgetLimits`` are used, the budget
            continues to use the last limit as the ``BudgetLimit`` . At that point, the planned budget
            provides the same experience as a fixed budget.

             ``DescribeBudget`` and ``DescribeBudgets`` response along with ``PlannedBudgetLimits`` will
             also contain ``BudgetLimit`` representing the current month or quarter limit present in
             ``PlannedBudgetLimits`` . This only applies to budgets created with ``PlannedBudgetLimits`` .
             Budgets created without ``PlannedBudgetLimits`` will only contain ``BudgetLimit`` , and no
             ``PlannedBudgetLimits`` .

            - *(string) --*

              A generic string.

              - *(dict) --*

                The amount of cost or usage that is measured for a budget.

                For example, a ``Spend`` for ``3 GB`` of S3 usage would have the following parameters:

                * An ``Amount`` of ``3``

                * A ``unit`` of ``GB``

                - **Amount** *(string) --* **[REQUIRED]**

                  The cost or usage amount that is associated with a budget forecast, actual spend, or
                  budget threshold.

                - **Unit** *(string) --* **[REQUIRED]**

                  The unit of measurement that is used for the budget forecast, actual spend, or budget
                  threshold, such as dollars or GB.

          - **CostFilters** *(dict) --*

            The cost filters, such as service or tag, that are applied to a budget.

            AWS Budgets supports the following services as a filter for RI budgets:

            * Amazon Elastic Compute Cloud - Compute

            * Amazon Redshift

            * Amazon Relational Database Service

            * Amazon ElastiCache

            * Amazon Elasticsearch Service

            - *(string) --*

              A generic string.

              - *(list) --*

                - *(string) --*

                  A generic string.

          - **CostTypes** *(dict) --*

            The types of costs that are included in this ``COST`` budget.

             ``USAGE`` , ``RI_UTILIZATION`` , ``RI_COVERAGE`` , ``Savings_Plans_Utilization`` , and
             ``Savings_Plans_Coverage`` budgets do not have ``CostTypes`` .

            - **IncludeTax** *(boolean) --*

              Specifies whether a budget includes taxes.

              The default value is ``true`` .

            - **IncludeSubscription** *(boolean) --*

              Specifies whether a budget includes subscriptions.

              The default value is ``true`` .

            - **UseBlended** *(boolean) --*

              Specifies whether a budget uses a blended rate.

              The default value is ``false`` .

            - **IncludeRefund** *(boolean) --*

              Specifies whether a budget includes refunds.

              The default value is ``true`` .

            - **IncludeCredit** *(boolean) --*

              Specifies whether a budget includes credits.

              The default value is ``true`` .

            - **IncludeUpfront** *(boolean) --*

              Specifies whether a budget includes upfront RI costs.

              The default value is ``true`` .

            - **IncludeRecurring** *(boolean) --*

              Specifies whether a budget includes recurring fees such as monthly RI fees.

              The default value is ``true`` .

            - **IncludeOtherSubscription** *(boolean) --*

              Specifies whether a budget includes non-RI subscription costs.

              The default value is ``true`` .

            - **IncludeSupport** *(boolean) --*

              Specifies whether a budget includes support subscription fees.

              The default value is ``true`` .

            - **IncludeDiscount** *(boolean) --*

              Specifies whether a budget includes discounts.

              The default value is ``true`` .

            - **UseAmortized** *(boolean) --*

              Specifies whether a budget uses the amortized rate.

              The default value is ``false`` .

          - **TimeUnit** *(string) --* **[REQUIRED]**

            The length of time until a budget resets the actual and forecasted spend. ``DAILY`` is
            available only for ``RI_UTILIZATION`` , ``RI_COVERAGE`` , ``Savings_Plans_Utilization`` , and
            ``Savings_Plans_Coverage`` budgets.

          - **TimePeriod** *(dict) --*

            The period of time that is covered by a budget. The period has a start date and an end date.
            The start date must come before the end date. The end date must come before ``06/15/87 00:00
            UTC`` .

            If you create your budget and don't specify a start date, AWS defaults to the start of your
            chosen time period (DAILY, MONTHLY, QUARTERLY, or ANNUALLY). For example, if you created your
            budget on January 24, 2018, chose ``DAILY`` , and didn't set a start date, AWS set your start
            date to ``01/24/18 00:00 UTC`` . If you chose ``MONTHLY`` , AWS set your start date to
            ``01/01/18 00:00 UTC`` . If you didn't specify an end date, AWS set your end date to ``06/15/87
            00:00 UTC`` . The defaults are the same for the AWS Billing and Cost Management console and the
            API.

            You can change either date with the ``UpdateBudget`` operation.

            After the end date, AWS deletes the budget and all associated notifications and subscribers.

            - **Start** *(datetime) --*

              The start date for a budget. If you created your budget and didn't specify a start date, AWS
              defaults to the start of your chosen time period (DAILY, MONTHLY, QUARTERLY, or ANNUALLY).
              For example, if you created your budget on January 24, 2018, chose ``DAILY`` , and didn't set
              a start date, AWS set your start date to ``01/24/18 00:00 UTC`` . If you chose ``MONTHLY`` ,
              AWS set your start date to ``01/01/18 00:00 UTC`` . The defaults are the same for the AWS
              Billing and Cost Management console and the API.

              You can change your start date with the ``UpdateBudget`` operation.

            - **End** *(datetime) --*

              The end date for a budget. If you didn't specify an end date, AWS set your end date to
              ``06/15/87 00:00 UTC`` . The defaults are the same for the AWS Billing and Cost Management
              console and the API.

              After the end date, AWS deletes the budget and all associated notifications and subscribers.
              You can change your end date with the ``UpdateBudget`` operation.

          - **CalculatedSpend** *(dict) --*

            The actual and forecasted cost or usage that the budget tracks.

            - **ActualSpend** *(dict) --* **[REQUIRED]**

              The amount of cost, usage, or RI units that you have used.

              - **Amount** *(string) --* **[REQUIRED]**

                The cost or usage amount that is associated with a budget forecast, actual spend, or budget
                threshold.

              - **Unit** *(string) --* **[REQUIRED]**

                The unit of measurement that is used for the budget forecast, actual spend, or budget
                threshold, such as dollars or GB.

            - **ForecastedSpend** *(dict) --*

              The amount of cost, usage, or RI units that you are forecasted to use.

              - **Amount** *(string) --* **[REQUIRED]**

                The cost or usage amount that is associated with a budget forecast, actual spend, or budget
                threshold.

              - **Unit** *(string) --* **[REQUIRED]**

                The unit of measurement that is used for the budget forecast, actual spend, or budget
                threshold, such as dollars or GB.

          - **BudgetType** *(string) --* **[REQUIRED]**

            Whether this budget tracks costs, usage, RI utilization, RI coverage, Savings Plans
            utilization, or Savings Plans coverage.

          - **LastUpdatedTime** *(datetime) --*

            The last time that you updated this budget.

        :type NotificationsWithSubscribers: list
        :param NotificationsWithSubscribers:

          A notification that you want to associate with a budget. A budget can have up to five
          notifications, and each notification can have one SNS subscriber and up to 10 email subscribers.
          If you include notifications and subscribers in your ``CreateBudget`` call, AWS creates the
          notifications and subscribers for you.

          - *(dict) --*

            A notification with subscribers. A notification can have one SNS subscriber and up to 10 email
            subscribers, for a total of 11 subscribers.

            - **Notification** *(dict) --* **[REQUIRED]**

              The notification that is associated with a budget.

              - **NotificationType** *(string) --* **[REQUIRED]**

                Whether the notification is for how much you have spent (``ACTUAL`` ) or for how much
                you're forecasted to spend (``FORECASTED`` ).

              - **ComparisonOperator** *(string) --* **[REQUIRED]**

                The comparison that is used for this notification.

              - **Threshold** *(float) --* **[REQUIRED]**

                The threshold that is associated with a notification. Thresholds are always a percentage.

              - **ThresholdType** *(string) --*

                The type of threshold for a notification. For ``ABSOLUTE_VALUE`` thresholds, AWS notifies
                you when you go over or are forecasted to go over your total cost threshold. For
                ``PERCENTAGE`` thresholds, AWS notifies you when you go over or are forecasted to go over a
                certain percentage of your forecasted spend. For example, if you have a budget for 200
                dollars and you have a ``PERCENTAGE`` threshold of 80%, AWS notifies you when you go over
                160 dollars.

              - **NotificationState** *(string) --*

                Whether this notification is in alarm. If a budget notification is in the ``ALARM`` state,
                you have passed the set threshold for the budget.

            - **Subscribers** *(list) --* **[REQUIRED]**

              A list of subscribers who are subscribed to this notification.

              - *(dict) --*

                The subscriber to a budget notification. The subscriber consists of a subscription type and
                either an Amazon SNS topic or an email address.

                For example, an email subscriber would have the following parameters:

                * A ``subscriptionType`` of ``EMAIL``

                * An ``address`` of ``example@example.com``

                - **SubscriptionType** *(string) --* **[REQUIRED]**

                  The type of notification that AWS sends to a subscriber.

                - **Address** *(string) --* **[REQUIRED]**

                  The address that AWS sends budget notifications to, either an SNS topic or an email.

                  When you create a subscriber, the value of ``Address`` can't contain line breaks.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*

            Response of CreateBudget

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_notification(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: ClientCreateNotificationNotificationTypeDef,
        Subscribers: List[ClientCreateNotificationSubscribersTypeDef],
    ) -> Dict:
        """
        Creates a notification. You must create the budget before you create the associated notification.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/CreateNotification>`_

        **Request Syntax**
        ::

          response = client.create_notification(
              AccountId='string',
              BudgetName='string',
              Notification={
                  'NotificationType': 'ACTUAL'|'FORECASTED',
                  'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
                  'Threshold': 123.0,
                  'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
                  'NotificationState': 'OK'|'ALARM'
              },
              Subscribers=[
                  {
                      'SubscriptionType': 'SNS'|'EMAIL',
                      'Address': 'string'
                  },
              ]
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The ``accountId`` that is associated with the budget that you want to create a notification for.

        :type BudgetName: string
        :param BudgetName: **[REQUIRED]**

          The name of the budget that you want AWS to notify you about. Budget names must be unique within
          an account.

        :type Notification: dict
        :param Notification: **[REQUIRED]**

          The notification that you want to create.

          - **NotificationType** *(string) --* **[REQUIRED]**

            Whether the notification is for how much you have spent (``ACTUAL`` ) or for how much you're
            forecasted to spend (``FORECASTED`` ).

          - **ComparisonOperator** *(string) --* **[REQUIRED]**

            The comparison that is used for this notification.

          - **Threshold** *(float) --* **[REQUIRED]**

            The threshold that is associated with a notification. Thresholds are always a percentage.

          - **ThresholdType** *(string) --*

            The type of threshold for a notification. For ``ABSOLUTE_VALUE`` thresholds, AWS notifies you
            when you go over or are forecasted to go over your total cost threshold. For ``PERCENTAGE``
            thresholds, AWS notifies you when you go over or are forecasted to go over a certain percentage
            of your forecasted spend. For example, if you have a budget for 200 dollars and you have a
            ``PERCENTAGE`` threshold of 80%, AWS notifies you when you go over 160 dollars.

          - **NotificationState** *(string) --*

            Whether this notification is in alarm. If a budget notification is in the ``ALARM`` state, you
            have passed the set threshold for the budget.

        :type Subscribers: list
        :param Subscribers: **[REQUIRED]**

          A list of subscribers that you want to associate with the notification. Each notification can
          have one SNS subscriber and up to 10 email subscribers.

          - *(dict) --*

            The subscriber to a budget notification. The subscriber consists of a subscription type and
            either an Amazon SNS topic or an email address.

            For example, an email subscriber would have the following parameters:

            * A ``subscriptionType`` of ``EMAIL``

            * An ``address`` of ``example@example.com``

            - **SubscriptionType** *(string) --* **[REQUIRED]**

              The type of notification that AWS sends to a subscriber.

            - **Address** *(string) --* **[REQUIRED]**

              The address that AWS sends budget notifications to, either an SNS topic or an email.

              When you create a subscriber, the value of ``Address`` can't contain line breaks.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*

            Response of CreateNotification

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_subscriber(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: ClientCreateSubscriberNotificationTypeDef,
        Subscriber: ClientCreateSubscriberSubscriberTypeDef,
    ) -> Dict:
        """
        Creates a subscriber. You must create the associated budget and notification before you create the
        subscriber.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/CreateSubscriber>`_

        **Request Syntax**
        ::

          response = client.create_subscriber(
              AccountId='string',
              BudgetName='string',
              Notification={
                  'NotificationType': 'ACTUAL'|'FORECASTED',
                  'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
                  'Threshold': 123.0,
                  'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
                  'NotificationState': 'OK'|'ALARM'
              },
              Subscriber={
                  'SubscriptionType': 'SNS'|'EMAIL',
                  'Address': 'string'
              }
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The ``accountId`` that is associated with the budget that you want to create a subscriber for.

        :type BudgetName: string
        :param BudgetName: **[REQUIRED]**

          The name of the budget that you want to subscribe to. Budget names must be unique within an
          account.

        :type Notification: dict
        :param Notification: **[REQUIRED]**

          The notification that you want to create a subscriber for.

          - **NotificationType** *(string) --* **[REQUIRED]**

            Whether the notification is for how much you have spent (``ACTUAL`` ) or for how much you're
            forecasted to spend (``FORECASTED`` ).

          - **ComparisonOperator** *(string) --* **[REQUIRED]**

            The comparison that is used for this notification.

          - **Threshold** *(float) --* **[REQUIRED]**

            The threshold that is associated with a notification. Thresholds are always a percentage.

          - **ThresholdType** *(string) --*

            The type of threshold for a notification. For ``ABSOLUTE_VALUE`` thresholds, AWS notifies you
            when you go over or are forecasted to go over your total cost threshold. For ``PERCENTAGE``
            thresholds, AWS notifies you when you go over or are forecasted to go over a certain percentage
            of your forecasted spend. For example, if you have a budget for 200 dollars and you have a
            ``PERCENTAGE`` threshold of 80%, AWS notifies you when you go over 160 dollars.

          - **NotificationState** *(string) --*

            Whether this notification is in alarm. If a budget notification is in the ``ALARM`` state, you
            have passed the set threshold for the budget.

        :type Subscriber: dict
        :param Subscriber: **[REQUIRED]**

          The subscriber that you want to associate with a budget notification.

          - **SubscriptionType** *(string) --* **[REQUIRED]**

            The type of notification that AWS sends to a subscriber.

          - **Address** *(string) --* **[REQUIRED]**

            The address that AWS sends budget notifications to, either an SNS topic or an email.

            When you create a subscriber, the value of ``Address`` can't contain line breaks.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*

            Response of CreateSubscriber

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_budget(self, AccountId: str, BudgetName: str) -> Dict:
        """
        Deletes a budget. You can delete your budget at any time.

        .. warning::

          Deleting a budget also deletes the notifications and subscribers that are associated with that
          budget.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/DeleteBudget>`_

        **Request Syntax**
        ::

          response = client.delete_budget(
              AccountId='string',
              BudgetName='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The ``accountId`` that is associated with the budget that you want to delete.

        :type BudgetName: string
        :param BudgetName: **[REQUIRED]**

          The name of the budget that you want to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*

            Response of DeleteBudget

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_notification(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: ClientDeleteNotificationNotificationTypeDef,
    ) -> Dict:
        """
        Deletes a notification.

        .. warning::

          Deleting a notification also deletes the subscribers that are associated with the notification.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/DeleteNotification>`_

        **Request Syntax**
        ::

          response = client.delete_notification(
              AccountId='string',
              BudgetName='string',
              Notification={
                  'NotificationType': 'ACTUAL'|'FORECASTED',
                  'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
                  'Threshold': 123.0,
                  'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
                  'NotificationState': 'OK'|'ALARM'
              }
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The ``accountId`` that is associated with the budget whose notification you want to delete.

        :type BudgetName: string
        :param BudgetName: **[REQUIRED]**

          The name of the budget whose notification you want to delete.

        :type Notification: dict
        :param Notification: **[REQUIRED]**

          The notification that you want to delete.

          - **NotificationType** *(string) --* **[REQUIRED]**

            Whether the notification is for how much you have spent (``ACTUAL`` ) or for how much you're
            forecasted to spend (``FORECASTED`` ).

          - **ComparisonOperator** *(string) --* **[REQUIRED]**

            The comparison that is used for this notification.

          - **Threshold** *(float) --* **[REQUIRED]**

            The threshold that is associated with a notification. Thresholds are always a percentage.

          - **ThresholdType** *(string) --*

            The type of threshold for a notification. For ``ABSOLUTE_VALUE`` thresholds, AWS notifies you
            when you go over or are forecasted to go over your total cost threshold. For ``PERCENTAGE``
            thresholds, AWS notifies you when you go over or are forecasted to go over a certain percentage
            of your forecasted spend. For example, if you have a budget for 200 dollars and you have a
            ``PERCENTAGE`` threshold of 80%, AWS notifies you when you go over 160 dollars.

          - **NotificationState** *(string) --*

            Whether this notification is in alarm. If a budget notification is in the ``ALARM`` state, you
            have passed the set threshold for the budget.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*

            Response of DeleteNotification

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_subscriber(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: ClientDeleteSubscriberNotificationTypeDef,
        Subscriber: ClientDeleteSubscriberSubscriberTypeDef,
    ) -> Dict:
        """
        Deletes a subscriber.

        .. warning::

          Deleting the last subscriber to a notification also deletes the notification.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/DeleteSubscriber>`_

        **Request Syntax**
        ::

          response = client.delete_subscriber(
              AccountId='string',
              BudgetName='string',
              Notification={
                  'NotificationType': 'ACTUAL'|'FORECASTED',
                  'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
                  'Threshold': 123.0,
                  'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
                  'NotificationState': 'OK'|'ALARM'
              },
              Subscriber={
                  'SubscriptionType': 'SNS'|'EMAIL',
                  'Address': 'string'
              }
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The ``accountId`` that is associated with the budget whose subscriber you want to delete.

        :type BudgetName: string
        :param BudgetName: **[REQUIRED]**

          The name of the budget whose subscriber you want to delete.

        :type Notification: dict
        :param Notification: **[REQUIRED]**

          The notification whose subscriber you want to delete.

          - **NotificationType** *(string) --* **[REQUIRED]**

            Whether the notification is for how much you have spent (``ACTUAL`` ) or for how much you're
            forecasted to spend (``FORECASTED`` ).

          - **ComparisonOperator** *(string) --* **[REQUIRED]**

            The comparison that is used for this notification.

          - **Threshold** *(float) --* **[REQUIRED]**

            The threshold that is associated with a notification. Thresholds are always a percentage.

          - **ThresholdType** *(string) --*

            The type of threshold for a notification. For ``ABSOLUTE_VALUE`` thresholds, AWS notifies you
            when you go over or are forecasted to go over your total cost threshold. For ``PERCENTAGE``
            thresholds, AWS notifies you when you go over or are forecasted to go over a certain percentage
            of your forecasted spend. For example, if you have a budget for 200 dollars and you have a
            ``PERCENTAGE`` threshold of 80%, AWS notifies you when you go over 160 dollars.

          - **NotificationState** *(string) --*

            Whether this notification is in alarm. If a budget notification is in the ``ALARM`` state, you
            have passed the set threshold for the budget.

        :type Subscriber: dict
        :param Subscriber: **[REQUIRED]**

          The subscriber that you want to delete.

          - **SubscriptionType** *(string) --* **[REQUIRED]**

            The type of notification that AWS sends to a subscriber.

          - **Address** *(string) --* **[REQUIRED]**

            The address that AWS sends budget notifications to, either an SNS topic or an email.

            When you create a subscriber, the value of ``Address`` can't contain line breaks.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*

            Response of DeleteSubscriber

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_budget(
        self, AccountId: str, BudgetName: str
    ) -> ClientDescribeBudgetResponseTypeDef:
        """
        Describes a budget.

        .. warning::

          The Request Syntax section shows the ``BudgetLimit`` syntax. For ``PlannedBudgetLimits`` , see
          the `Examples
          <https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DescribeBudget.html#API_DescribeBudget_Examples>`__
          section.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/DescribeBudget>`_

        **Request Syntax**
        ::

          response = client.describe_budget(
              AccountId='string',
              BudgetName='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The ``accountId`` that is associated with the budget that you want a description of.

        :type BudgetName: string
        :param BudgetName: **[REQUIRED]**

          The name of the budget that you want a description of.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Budget': {
                    'BudgetName': 'string',
                    'BudgetLimit': {
                        'Amount': 'string',
                        'Unit': 'string'
                    },
                    'PlannedBudgetLimits': {
                        'string': {
                            'Amount': 'string',
                            'Unit': 'string'
                        }
                    },
                    'CostFilters': {
                        'string': [
                            'string',
                        ]
                    },
                    'CostTypes': {
                        'IncludeTax': True|False,
                        'IncludeSubscription': True|False,
                        'UseBlended': True|False,
                        'IncludeRefund': True|False,
                        'IncludeCredit': True|False,
                        'IncludeUpfront': True|False,
                        'IncludeRecurring': True|False,
                        'IncludeOtherSubscription': True|False,
                        'IncludeSupport': True|False,
                        'IncludeDiscount': True|False,
                        'UseAmortized': True|False
                    },
                    'TimeUnit': 'DAILY'|'MONTHLY'|'QUARTERLY'|'ANNUALLY',
                    'TimePeriod': {
                        'Start': datetime(2015, 1, 1),
                        'End': datetime(2015, 1, 1)
                    },
                    'CalculatedSpend': {
                        'ActualSpend': {
                            'Amount': 'string',
                            'Unit': 'string'
                        },
                        'ForecastedSpend': {
                            'Amount': 'string',
                            'Unit': 'string'
                        }
                    },
                    'BudgetType':
                    'USAGE'|'COST'|'RI_UTILIZATION'|'RI_COVERAGE'|'SAVINGS_PLANS_UTILIZATION'
                    |'SAVINGS_PLANS_COVERAGE',
                    'LastUpdatedTime': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            Response of DescribeBudget

            - **Budget** *(dict) --*

              The description of the budget.

              - **BudgetName** *(string) --*

                The name of a budget. The name must be unique within an account. The ``:`` and ``\\``
                characters aren't allowed in ``BudgetName`` .

              - **BudgetLimit** *(dict) --*

                The total amount of cost, usage, RI utilization, RI coverage, Savings Plans utilization, or
                Savings Plans coverage that you want to track with your budget.

                 ``BudgetLimit`` is required for cost or usage budgets, but optional for RI or Savings
                 Plans utilization or coverage budgets. RI and Savings Plans utilization or coverage
                 budgets default to ``100`` , which is the only valid value for RI or Savings Plans
                 utilization or coverage budgets. You can't use ``BudgetLimit`` with
                 ``PlannedBudgetLimits`` for ``CreateBudget`` and ``UpdateBudget`` actions.

                - **Amount** *(string) --*

                  The cost or usage amount that is associated with a budget forecast, actual spend, or
                  budget threshold.

                - **Unit** *(string) --*

                  The unit of measurement that is used for the budget forecast, actual spend, or budget
                  threshold, such as dollars or GB.

              - **PlannedBudgetLimits** *(dict) --*

                A map containing multiple ``BudgetLimit`` , including current or future limits.

                 ``PlannedBudgetLimits`` is available for cost or usage budget and supports monthly and
                 quarterly ``TimeUnit`` .

                For monthly budgets, provide 12 months of ``PlannedBudgetLimits`` values. This must start
                from the current month and include the next 11 months. The ``key`` is the start of the
                month, ``UTC`` in epoch seconds.

                For quarterly budgets, provide 4 quarters of ``PlannedBudgetLimits`` value entries in
                standard calendar quarter increments. This must start from the current quarter and include
                the next 3 quarters. The ``key`` is the start of the quarter, ``UTC`` in epoch seconds.

                If the planned budget expires before 12 months for monthly or 4 quarters for quarterly,
                provide the ``PlannedBudgetLimits`` values only for the remaining periods.

                If the budget begins at a date in the future, provide ``PlannedBudgetLimits`` values from
                the start date of the budget.

                After all of the ``BudgetLimit`` values in ``PlannedBudgetLimits`` are used, the budget
                continues to use the last limit as the ``BudgetLimit`` . At that point, the planned budget
                provides the same experience as a fixed budget.

                 ``DescribeBudget`` and ``DescribeBudgets`` response along with ``PlannedBudgetLimits``
                 will also contain ``BudgetLimit`` representing the current month or quarter limit present
                 in ``PlannedBudgetLimits`` . This only applies to budgets created with
                 ``PlannedBudgetLimits`` . Budgets created without ``PlannedBudgetLimits`` will only
                 contain ``BudgetLimit`` , and no ``PlannedBudgetLimits`` .

                - *(string) --*

                  A generic string.

                  - *(dict) --*

                    The amount of cost or usage that is measured for a budget.

                    For example, a ``Spend`` for ``3 GB`` of S3 usage would have the following parameters:

                    * An ``Amount`` of ``3``

                    * A ``unit`` of ``GB``

                    - **Amount** *(string) --*

                      The cost or usage amount that is associated with a budget forecast, actual spend, or
                      budget threshold.

                    - **Unit** *(string) --*

                      The unit of measurement that is used for the budget forecast, actual spend, or budget
                      threshold, such as dollars or GB.

              - **CostFilters** *(dict) --*

                The cost filters, such as service or tag, that are applied to a budget.

                AWS Budgets supports the following services as a filter for RI budgets:

                * Amazon Elastic Compute Cloud - Compute

                * Amazon Redshift

                * Amazon Relational Database Service

                * Amazon ElastiCache

                * Amazon Elasticsearch Service

                - *(string) --*

                  A generic string.

                  - *(list) --*

                    - *(string) --*

                      A generic string.

              - **CostTypes** *(dict) --*

                The types of costs that are included in this ``COST`` budget.

                 ``USAGE`` , ``RI_UTILIZATION`` , ``RI_COVERAGE`` , ``Savings_Plans_Utilization`` , and
                 ``Savings_Plans_Coverage`` budgets do not have ``CostTypes`` .

                - **IncludeTax** *(boolean) --*

                  Specifies whether a budget includes taxes.

                  The default value is ``true`` .

                - **IncludeSubscription** *(boolean) --*

                  Specifies whether a budget includes subscriptions.

                  The default value is ``true`` .

                - **UseBlended** *(boolean) --*

                  Specifies whether a budget uses a blended rate.

                  The default value is ``false`` .

                - **IncludeRefund** *(boolean) --*

                  Specifies whether a budget includes refunds.

                  The default value is ``true`` .

                - **IncludeCredit** *(boolean) --*

                  Specifies whether a budget includes credits.

                  The default value is ``true`` .

                - **IncludeUpfront** *(boolean) --*

                  Specifies whether a budget includes upfront RI costs.

                  The default value is ``true`` .

                - **IncludeRecurring** *(boolean) --*

                  Specifies whether a budget includes recurring fees such as monthly RI fees.

                  The default value is ``true`` .

                - **IncludeOtherSubscription** *(boolean) --*

                  Specifies whether a budget includes non-RI subscription costs.

                  The default value is ``true`` .

                - **IncludeSupport** *(boolean) --*

                  Specifies whether a budget includes support subscription fees.

                  The default value is ``true`` .

                - **IncludeDiscount** *(boolean) --*

                  Specifies whether a budget includes discounts.

                  The default value is ``true`` .

                - **UseAmortized** *(boolean) --*

                  Specifies whether a budget uses the amortized rate.

                  The default value is ``false`` .

              - **TimeUnit** *(string) --*

                The length of time until a budget resets the actual and forecasted spend. ``DAILY`` is
                available only for ``RI_UTILIZATION`` , ``RI_COVERAGE`` , ``Savings_Plans_Utilization`` ,
                and ``Savings_Plans_Coverage`` budgets.

              - **TimePeriod** *(dict) --*

                The period of time that is covered by a budget. The period has a start date and an end
                date. The start date must come before the end date. The end date must come before
                ``06/15/87 00:00 UTC`` .

                If you create your budget and don't specify a start date, AWS defaults to the start of your
                chosen time period (DAILY, MONTHLY, QUARTERLY, or ANNUALLY). For example, if you created
                your budget on January 24, 2018, chose ``DAILY`` , and didn't set a start date, AWS set
                your start date to ``01/24/18 00:00 UTC`` . If you chose ``MONTHLY`` , AWS set your start
                date to ``01/01/18 00:00 UTC`` . If you didn't specify an end date, AWS set your end date
                to ``06/15/87 00:00 UTC`` . The defaults are the same for the AWS Billing and Cost
                Management console and the API.

                You can change either date with the ``UpdateBudget`` operation.

                After the end date, AWS deletes the budget and all associated notifications and subscribers.

                - **Start** *(datetime) --*

                  The start date for a budget. If you created your budget and didn't specify a start date,
                  AWS defaults to the start of your chosen time period (DAILY, MONTHLY, QUARTERLY, or
                  ANNUALLY). For example, if you created your budget on January 24, 2018, chose ``DAILY`` ,
                  and didn't set a start date, AWS set your start date to ``01/24/18 00:00 UTC`` . If you
                  chose ``MONTHLY`` , AWS set your start date to ``01/01/18 00:00 UTC`` . The defaults are
                  the same for the AWS Billing and Cost Management console and the API.

                  You can change your start date with the ``UpdateBudget`` operation.

                - **End** *(datetime) --*

                  The end date for a budget. If you didn't specify an end date, AWS set your end date to
                  ``06/15/87 00:00 UTC`` . The defaults are the same for the AWS Billing and Cost
                  Management console and the API.

                  After the end date, AWS deletes the budget and all associated notifications and
                  subscribers. You can change your end date with the ``UpdateBudget`` operation.

              - **CalculatedSpend** *(dict) --*

                The actual and forecasted cost or usage that the budget tracks.

                - **ActualSpend** *(dict) --*

                  The amount of cost, usage, or RI units that you have used.

                  - **Amount** *(string) --*

                    The cost or usage amount that is associated with a budget forecast, actual spend, or
                    budget threshold.

                  - **Unit** *(string) --*

                    The unit of measurement that is used for the budget forecast, actual spend, or budget
                    threshold, such as dollars or GB.

                - **ForecastedSpend** *(dict) --*

                  The amount of cost, usage, or RI units that you are forecasted to use.

                  - **Amount** *(string) --*

                    The cost or usage amount that is associated with a budget forecast, actual spend, or
                    budget threshold.

                  - **Unit** *(string) --*

                    The unit of measurement that is used for the budget forecast, actual spend, or budget
                    threshold, such as dollars or GB.

              - **BudgetType** *(string) --*

                Whether this budget tracks costs, usage, RI utilization, RI coverage, Savings Plans
                utilization, or Savings Plans coverage.

              - **LastUpdatedTime** *(datetime) --*

                The last time that you updated this budget.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_budget_performance_history(
        self,
        AccountId: str,
        BudgetName: str,
        TimePeriod: ClientDescribeBudgetPerformanceHistoryTimePeriodTypeDef = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeBudgetPerformanceHistoryResponseTypeDef:
        """
        Describes the history for ``DAILY`` , ``MONTHLY`` , and ``QUARTERLY`` budgets. Budget history isn't
        available for ``ANNUAL`` budgets.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/DescribeBudgetPerformanceHistory>`_

        **Request Syntax**
        ::

          response = client.describe_budget_performance_history(
              AccountId='string',
              BudgetName='string',
              TimePeriod={
                  'Start': datetime(2015, 1, 1),
                  'End': datetime(2015, 1, 1)
              },
              MaxResults=123,
              NextToken='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The account ID of the user. It should be a 12-digit number.

        :type BudgetName: string
        :param BudgetName: **[REQUIRED]**

          A string that represents the budget name. The ":" and "\\" characters aren't allowed.

        :type TimePeriod: dict
        :param TimePeriod:

          Retrieves how often the budget went into an ``ALARM`` state for the specified time period.

          - **Start** *(datetime) --*

            The start date for a budget. If you created your budget and didn't specify a start date, AWS
            defaults to the start of your chosen time period (DAILY, MONTHLY, QUARTERLY, or ANNUALLY). For
            example, if you created your budget on January 24, 2018, chose ``DAILY`` , and didn't set a
            start date, AWS set your start date to ``01/24/18 00:00 UTC`` . If you chose ``MONTHLY`` , AWS
            set your start date to ``01/01/18 00:00 UTC`` . The defaults are the same for the AWS Billing
            and Cost Management console and the API.

            You can change your start date with the ``UpdateBudget`` operation.

          - **End** *(datetime) --*

            The end date for a budget. If you didn't specify an end date, AWS set your end date to
            ``06/15/87 00:00 UTC`` . The defaults are the same for the AWS Billing and Cost Management
            console and the API.

            After the end date, AWS deletes the budget and all associated notifications and subscribers.
            You can change your end date with the ``UpdateBudget`` operation.

        :type MaxResults: integer
        :param MaxResults:

          An integer that represents how many entries a paginated response contains. The maximum is 100.

        :type NextToken: string
        :param NextToken:

          A generic string.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'BudgetPerformanceHistory': {
                    'BudgetName': 'string',
                    'BudgetType':
                    'USAGE'|'COST'|'RI_UTILIZATION'|'RI_COVERAGE'|'SAVINGS_PLANS_UTILIZATION'
                    |'SAVINGS_PLANS_COVERAGE',
                    'CostFilters': {
                        'string': [
                            'string',
                        ]
                    },
                    'CostTypes': {
                        'IncludeTax': True|False,
                        'IncludeSubscription': True|False,
                        'UseBlended': True|False,
                        'IncludeRefund': True|False,
                        'IncludeCredit': True|False,
                        'IncludeUpfront': True|False,
                        'IncludeRecurring': True|False,
                        'IncludeOtherSubscription': True|False,
                        'IncludeSupport': True|False,
                        'IncludeDiscount': True|False,
                        'UseAmortized': True|False
                    },
                    'TimeUnit': 'DAILY'|'MONTHLY'|'QUARTERLY'|'ANNUALLY',
                    'BudgetedAndActualAmountsList': [
                        {
                            'BudgetedAmount': {
                                'Amount': 'string',
                                'Unit': 'string'
                            },
                            'ActualAmount': {
                                'Amount': 'string',
                                'Unit': 'string'
                            },
                            'TimePeriod': {
                                'Start': datetime(2015, 1, 1),
                                'End': datetime(2015, 1, 1)
                            }
                        },
                    ]
                },
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **BudgetPerformanceHistory** *(dict) --*

              The history of how often the budget has gone into an ``ALARM`` state.

              For ``DAILY`` budgets, the history saves the state of the budget for the last 60 days. For
              ``MONTHLY`` budgets, the history saves the state of the budget for the current month plus the
              last 12 months. For ``QUARTERLY`` budgets, the history saves the state of the budget for the
              last four quarters.

              - **BudgetName** *(string) --*

                A string that represents the budget name. The ":" and "\\" characters aren't allowed.

              - **BudgetType** *(string) --*

                The type of a budget. It must be one of the following types:

                 ``COST`` , ``USAGE`` , ``RI_UTILIZATION`` , or ``RI_COVERAGE`` .

              - **CostFilters** *(dict) --*

                The history of the cost filters for a budget during the specified time period.

                - *(string) --*

                  A generic string.

                  - *(list) --*

                    - *(string) --*

                      A generic string.

              - **CostTypes** *(dict) --*

                The history of the cost types for a budget during the specified time period.

                - **IncludeTax** *(boolean) --*

                  Specifies whether a budget includes taxes.

                  The default value is ``true`` .

                - **IncludeSubscription** *(boolean) --*

                  Specifies whether a budget includes subscriptions.

                  The default value is ``true`` .

                - **UseBlended** *(boolean) --*

                  Specifies whether a budget uses a blended rate.

                  The default value is ``false`` .

                - **IncludeRefund** *(boolean) --*

                  Specifies whether a budget includes refunds.

                  The default value is ``true`` .

                - **IncludeCredit** *(boolean) --*

                  Specifies whether a budget includes credits.

                  The default value is ``true`` .

                - **IncludeUpfront** *(boolean) --*

                  Specifies whether a budget includes upfront RI costs.

                  The default value is ``true`` .

                - **IncludeRecurring** *(boolean) --*

                  Specifies whether a budget includes recurring fees such as monthly RI fees.

                  The default value is ``true`` .

                - **IncludeOtherSubscription** *(boolean) --*

                  Specifies whether a budget includes non-RI subscription costs.

                  The default value is ``true`` .

                - **IncludeSupport** *(boolean) --*

                  Specifies whether a budget includes support subscription fees.

                  The default value is ``true`` .

                - **IncludeDiscount** *(boolean) --*

                  Specifies whether a budget includes discounts.

                  The default value is ``true`` .

                - **UseAmortized** *(boolean) --*

                  Specifies whether a budget uses the amortized rate.

                  The default value is ``false`` .

              - **TimeUnit** *(string) --*

                The time unit of the budget, such as MONTHLY or QUARTERLY.

              - **BudgetedAndActualAmountsList** *(list) --*

                A list of amounts of cost or usage that you created budgets for, compared to your actual
                costs or usage.

                - *(dict) --*

                  The amount of cost or usage that you created the budget for, compared to your actual
                  costs or usage.

                  - **BudgetedAmount** *(dict) --*

                    The amount of cost or usage that you created the budget for.

                    - **Amount** *(string) --*

                      The cost or usage amount that is associated with a budget forecast, actual spend, or
                      budget threshold.

                    - **Unit** *(string) --*

                      The unit of measurement that is used for the budget forecast, actual spend, or budget
                      threshold, such as dollars or GB.

                  - **ActualAmount** *(dict) --*

                    Your actual costs or usage for a budget period.

                    - **Amount** *(string) --*

                      The cost or usage amount that is associated with a budget forecast, actual spend, or
                      budget threshold.

                    - **Unit** *(string) --*

                      The unit of measurement that is used for the budget forecast, actual spend, or budget
                      threshold, such as dollars or GB.

                  - **TimePeriod** *(dict) --*

                    The time period covered by this budget comparison.

                    - **Start** *(datetime) --*

                      The start date for a budget. If you created your budget and didn't specify a start
                      date, AWS defaults to the start of your chosen time period (DAILY, MONTHLY,
                      QUARTERLY, or ANNUALLY). For example, if you created your budget on January 24, 2018,
                      chose ``DAILY`` , and didn't set a start date, AWS set your start date to ``01/24/18
                      00:00 UTC`` . If you chose ``MONTHLY`` , AWS set your start date to ``01/01/18 00:00
                      UTC`` . The defaults are the same for the AWS Billing and Cost Management console and
                      the API.

                      You can change your start date with the ``UpdateBudget`` operation.

                    - **End** *(datetime) --*

                      The end date for a budget. If you didn't specify an end date, AWS set your end date
                      to ``06/15/87 00:00 UTC`` . The defaults are the same for the AWS Billing and Cost
                      Management console and the API.

                      After the end date, AWS deletes the budget and all associated notifications and
                      subscribers. You can change your end date with the ``UpdateBudget`` operation.

            - **NextToken** *(string) --*

              A generic string.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_budgets(
        self, AccountId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientDescribeBudgetsResponseTypeDef:
        """
        Lists the budgets that are associated with an account.

        .. warning::

          The Request Syntax section shows the ``BudgetLimit`` syntax. For ``PlannedBudgetLimits`` , see
          the `Examples
          <https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DescribeBudgets.html#API_DescribeBudgets_Examples>`__
          section.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/DescribeBudgets>`_

        **Request Syntax**
        ::

          response = client.describe_budgets(
              AccountId='string',
              MaxResults=123,
              NextToken='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The ``accountId`` that is associated with the budgets that you want descriptions of.

        :type MaxResults: integer
        :param MaxResults:

          An optional integer that represents how many entries a paginated response contains. The maximum
          is 100.

        :type NextToken: string
        :param NextToken:

          The pagination token that you include in your request to indicate the next set of results that
          you want to retrieve.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Budgets': [
                    {
                        'BudgetName': 'string',
                        'BudgetLimit': {
                            'Amount': 'string',
                            'Unit': 'string'
                        },
                        'PlannedBudgetLimits': {
                            'string': {
                                'Amount': 'string',
                                'Unit': 'string'
                            }
                        },
                        'CostFilters': {
                            'string': [
                                'string',
                            ]
                        },
                        'CostTypes': {
                            'IncludeTax': True|False,
                            'IncludeSubscription': True|False,
                            'UseBlended': True|False,
                            'IncludeRefund': True|False,
                            'IncludeCredit': True|False,
                            'IncludeUpfront': True|False,
                            'IncludeRecurring': True|False,
                            'IncludeOtherSubscription': True|False,
                            'IncludeSupport': True|False,
                            'IncludeDiscount': True|False,
                            'UseAmortized': True|False
                        },
                        'TimeUnit': 'DAILY'|'MONTHLY'|'QUARTERLY'|'ANNUALLY',
                        'TimePeriod': {
                            'Start': datetime(2015, 1, 1),
                            'End': datetime(2015, 1, 1)
                        },
                        'CalculatedSpend': {
                            'ActualSpend': {
                                'Amount': 'string',
                                'Unit': 'string'
                            },
                            'ForecastedSpend': {
                                'Amount': 'string',
                                'Unit': 'string'
                            }
                        },
                        'BudgetType':
                        'USAGE'|'COST'|'RI_UTILIZATION'|'RI_COVERAGE'|'SAVINGS_PLANS_UTILIZATION'
                        |'SAVINGS_PLANS_COVERAGE',
                        'LastUpdatedTime': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Response of DescribeBudgets

            - **Budgets** *(list) --*

              A list of budgets.

              - *(dict) --*

                Represents the output of the ``CreateBudget`` operation. The content consists of the
                detailed metadata and data file information, and the current status of the ``budget``
                object.

                This is the ARN pattern for a budget:

                 ``arn:aws:budgetservice::AccountId:budget/budgetName``

                - **BudgetName** *(string) --*

                  The name of a budget. The name must be unique within an account. The ``:`` and ``\\``
                  characters aren't allowed in ``BudgetName`` .

                - **BudgetLimit** *(dict) --*

                  The total amount of cost, usage, RI utilization, RI coverage, Savings Plans utilization,
                  or Savings Plans coverage that you want to track with your budget.

                   ``BudgetLimit`` is required for cost or usage budgets, but optional for RI or Savings
                   Plans utilization or coverage budgets. RI and Savings Plans utilization or coverage
                   budgets default to ``100`` , which is the only valid value for RI or Savings Plans
                   utilization or coverage budgets. You can't use ``BudgetLimit`` with
                   ``PlannedBudgetLimits`` for ``CreateBudget`` and ``UpdateBudget`` actions.

                  - **Amount** *(string) --*

                    The cost or usage amount that is associated with a budget forecast, actual spend, or
                    budget threshold.

                  - **Unit** *(string) --*

                    The unit of measurement that is used for the budget forecast, actual spend, or budget
                    threshold, such as dollars or GB.

                - **PlannedBudgetLimits** *(dict) --*

                  A map containing multiple ``BudgetLimit`` , including current or future limits.

                   ``PlannedBudgetLimits`` is available for cost or usage budget and supports monthly and
                   quarterly ``TimeUnit`` .

                  For monthly budgets, provide 12 months of ``PlannedBudgetLimits`` values. This must start
                  from the current month and include the next 11 months. The ``key`` is the start of the
                  month, ``UTC`` in epoch seconds.

                  For quarterly budgets, provide 4 quarters of ``PlannedBudgetLimits`` value entries in
                  standard calendar quarter increments. This must start from the current quarter and
                  include the next 3 quarters. The ``key`` is the start of the quarter, ``UTC`` in epoch
                  seconds.

                  If the planned budget expires before 12 months for monthly or 4 quarters for quarterly,
                  provide the ``PlannedBudgetLimits`` values only for the remaining periods.

                  If the budget begins at a date in the future, provide ``PlannedBudgetLimits`` values from
                  the start date of the budget.

                  After all of the ``BudgetLimit`` values in ``PlannedBudgetLimits`` are used, the budget
                  continues to use the last limit as the ``BudgetLimit`` . At that point, the planned
                  budget provides the same experience as a fixed budget.

                   ``DescribeBudget`` and ``DescribeBudgets`` response along with ``PlannedBudgetLimits``
                   will also contain ``BudgetLimit`` representing the current month or quarter limit
                   present in ``PlannedBudgetLimits`` . This only applies to budgets created with
                   ``PlannedBudgetLimits`` . Budgets created without ``PlannedBudgetLimits`` will only
                   contain ``BudgetLimit`` , and no ``PlannedBudgetLimits`` .

                  - *(string) --*

                    A generic string.

                    - *(dict) --*

                      The amount of cost or usage that is measured for a budget.

                      For example, a ``Spend`` for ``3 GB`` of S3 usage would have the following parameters:

                      * An ``Amount`` of ``3``

                      * A ``unit`` of ``GB``

                      - **Amount** *(string) --*

                        The cost or usage amount that is associated with a budget forecast, actual spend,
                        or budget threshold.

                      - **Unit** *(string) --*

                        The unit of measurement that is used for the budget forecast, actual spend, or
                        budget threshold, such as dollars or GB.

                - **CostFilters** *(dict) --*

                  The cost filters, such as service or tag, that are applied to a budget.

                  AWS Budgets supports the following services as a filter for RI budgets:

                  * Amazon Elastic Compute Cloud - Compute

                  * Amazon Redshift

                  * Amazon Relational Database Service

                  * Amazon ElastiCache

                  * Amazon Elasticsearch Service

                  - *(string) --*

                    A generic string.

                    - *(list) --*

                      - *(string) --*

                        A generic string.

                - **CostTypes** *(dict) --*

                  The types of costs that are included in this ``COST`` budget.

                   ``USAGE`` , ``RI_UTILIZATION`` , ``RI_COVERAGE`` , ``Savings_Plans_Utilization`` , and
                   ``Savings_Plans_Coverage`` budgets do not have ``CostTypes`` .

                  - **IncludeTax** *(boolean) --*

                    Specifies whether a budget includes taxes.

                    The default value is ``true`` .

                  - **IncludeSubscription** *(boolean) --*

                    Specifies whether a budget includes subscriptions.

                    The default value is ``true`` .

                  - **UseBlended** *(boolean) --*

                    Specifies whether a budget uses a blended rate.

                    The default value is ``false`` .

                  - **IncludeRefund** *(boolean) --*

                    Specifies whether a budget includes refunds.

                    The default value is ``true`` .

                  - **IncludeCredit** *(boolean) --*

                    Specifies whether a budget includes credits.

                    The default value is ``true`` .

                  - **IncludeUpfront** *(boolean) --*

                    Specifies whether a budget includes upfront RI costs.

                    The default value is ``true`` .

                  - **IncludeRecurring** *(boolean) --*

                    Specifies whether a budget includes recurring fees such as monthly RI fees.

                    The default value is ``true`` .

                  - **IncludeOtherSubscription** *(boolean) --*

                    Specifies whether a budget includes non-RI subscription costs.

                    The default value is ``true`` .

                  - **IncludeSupport** *(boolean) --*

                    Specifies whether a budget includes support subscription fees.

                    The default value is ``true`` .

                  - **IncludeDiscount** *(boolean) --*

                    Specifies whether a budget includes discounts.

                    The default value is ``true`` .

                  - **UseAmortized** *(boolean) --*

                    Specifies whether a budget uses the amortized rate.

                    The default value is ``false`` .

                - **TimeUnit** *(string) --*

                  The length of time until a budget resets the actual and forecasted spend. ``DAILY`` is
                  available only for ``RI_UTILIZATION`` , ``RI_COVERAGE`` , ``Savings_Plans_Utilization`` ,
                  and ``Savings_Plans_Coverage`` budgets.

                - **TimePeriod** *(dict) --*

                  The period of time that is covered by a budget. The period has a start date and an end
                  date. The start date must come before the end date. The end date must come before
                  ``06/15/87 00:00 UTC`` .

                  If you create your budget and don't specify a start date, AWS defaults to the start of
                  your chosen time period (DAILY, MONTHLY, QUARTERLY, or ANNUALLY). For example, if you
                  created your budget on January 24, 2018, chose ``DAILY`` , and didn't set a start date,
                  AWS set your start date to ``01/24/18 00:00 UTC`` . If you chose ``MONTHLY`` , AWS set
                  your start date to ``01/01/18 00:00 UTC`` . If you didn't specify an end date, AWS set
                  your end date to ``06/15/87 00:00 UTC`` . The defaults are the same for the AWS Billing
                  and Cost Management console and the API.

                  You can change either date with the ``UpdateBudget`` operation.

                  After the end date, AWS deletes the budget and all associated notifications and
                  subscribers.

                  - **Start** *(datetime) --*

                    The start date for a budget. If you created your budget and didn't specify a start
                    date, AWS defaults to the start of your chosen time period (DAILY, MONTHLY, QUARTERLY,
                    or ANNUALLY). For example, if you created your budget on January 24, 2018, chose
                    ``DAILY`` , and didn't set a start date, AWS set your start date to ``01/24/18 00:00
                    UTC`` . If you chose ``MONTHLY`` , AWS set your start date to ``01/01/18 00:00 UTC`` .
                    The defaults are the same for the AWS Billing and Cost Management console and the API.

                    You can change your start date with the ``UpdateBudget`` operation.

                  - **End** *(datetime) --*

                    The end date for a budget. If you didn't specify an end date, AWS set your end date to
                    ``06/15/87 00:00 UTC`` . The defaults are the same for the AWS Billing and Cost
                    Management console and the API.

                    After the end date, AWS deletes the budget and all associated notifications and
                    subscribers. You can change your end date with the ``UpdateBudget`` operation.

                - **CalculatedSpend** *(dict) --*

                  The actual and forecasted cost or usage that the budget tracks.

                  - **ActualSpend** *(dict) --*

                    The amount of cost, usage, or RI units that you have used.

                    - **Amount** *(string) --*

                      The cost or usage amount that is associated with a budget forecast, actual spend, or
                      budget threshold.

                    - **Unit** *(string) --*

                      The unit of measurement that is used for the budget forecast, actual spend, or budget
                      threshold, such as dollars or GB.

                  - **ForecastedSpend** *(dict) --*

                    The amount of cost, usage, or RI units that you are forecasted to use.

                    - **Amount** *(string) --*

                      The cost or usage amount that is associated with a budget forecast, actual spend, or
                      budget threshold.

                    - **Unit** *(string) --*

                      The unit of measurement that is used for the budget forecast, actual spend, or budget
                      threshold, such as dollars or GB.

                - **BudgetType** *(string) --*

                  Whether this budget tracks costs, usage, RI utilization, RI coverage, Savings Plans
                  utilization, or Savings Plans coverage.

                - **LastUpdatedTime** *(datetime) --*

                  The last time that you updated this budget.

            - **NextToken** *(string) --*

              The pagination token in the service response that indicates the next set of results that you
              can retrieve.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_notifications_for_budget(
        self,
        AccountId: str,
        BudgetName: str,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeNotificationsForBudgetResponseTypeDef:
        """
        Lists the notifications that are associated with a budget.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/DescribeNotificationsForBudget>`_

        **Request Syntax**
        ::

          response = client.describe_notifications_for_budget(
              AccountId='string',
              BudgetName='string',
              MaxResults=123,
              NextToken='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The ``accountId`` that is associated with the budget whose notifications you want descriptions of.

        :type BudgetName: string
        :param BudgetName: **[REQUIRED]**

          The name of the budget whose notifications you want descriptions of.

        :type MaxResults: integer
        :param MaxResults:

          An optional integer that represents how many entries a paginated response contains. The maximum
          is 100.

        :type NextToken: string
        :param NextToken:

          The pagination token that you include in your request to indicate the next set of results that
          you want to retrieve.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Notifications': [
                    {
                        'NotificationType': 'ACTUAL'|'FORECASTED',
                        'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
                        'Threshold': 123.0,
                        'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
                        'NotificationState': 'OK'|'ALARM'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Response of GetNotificationsForBudget

            - **Notifications** *(list) --*

              A list of notifications that are associated with a budget.

              - *(dict) --*

                A notification that is associated with a budget. A budget can have up to five notifications.

                Each notification must have at least one subscriber. A notification can have one SNS
                subscriber and up to 10 email subscribers, for a total of 11 subscribers.

                For example, if you have a budget for 200 dollars and you want to be notified when you go
                over 160 dollars, create a notification with the following parameters:

                * A notificationType of ``ACTUAL``

                * A ``thresholdType`` of ``PERCENTAGE``

                * A ``comparisonOperator`` of ``GREATER_THAN``

                * A notification ``threshold`` of ``80``

                - **NotificationType** *(string) --*

                  Whether the notification is for how much you have spent (``ACTUAL`` ) or for how much
                  you're forecasted to spend (``FORECASTED`` ).

                - **ComparisonOperator** *(string) --*

                  The comparison that is used for this notification.

                - **Threshold** *(float) --*

                  The threshold that is associated with a notification. Thresholds are always a percentage.

                - **ThresholdType** *(string) --*

                  The type of threshold for a notification. For ``ABSOLUTE_VALUE`` thresholds, AWS notifies
                  you when you go over or are forecasted to go over your total cost threshold. For
                  ``PERCENTAGE`` thresholds, AWS notifies you when you go over or are forecasted to go over
                  a certain percentage of your forecasted spend. For example, if you have a budget for 200
                  dollars and you have a ``PERCENTAGE`` threshold of 80%, AWS notifies you when you go over
                  160 dollars.

                - **NotificationState** *(string) --*

                  Whether this notification is in alarm. If a budget notification is in the ``ALARM``
                  state, you have passed the set threshold for the budget.

            - **NextToken** *(string) --*

              The pagination token in the service response that indicates the next set of results that you
              can retrieve.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_subscribers_for_notification(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: ClientDescribeSubscribersForNotificationNotificationTypeDef,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeSubscribersForNotificationResponseTypeDef:
        """
        Lists the subscribers that are associated with a notification.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/DescribeSubscribersForNotification>`_

        **Request Syntax**
        ::

          response = client.describe_subscribers_for_notification(
              AccountId='string',
              BudgetName='string',
              Notification={
                  'NotificationType': 'ACTUAL'|'FORECASTED',
                  'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
                  'Threshold': 123.0,
                  'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
                  'NotificationState': 'OK'|'ALARM'
              },
              MaxResults=123,
              NextToken='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The ``accountId`` that is associated with the budget whose subscribers you want descriptions of.

        :type BudgetName: string
        :param BudgetName: **[REQUIRED]**

          The name of the budget whose subscribers you want descriptions of.

        :type Notification: dict
        :param Notification: **[REQUIRED]**

          The notification whose subscribers you want to list.

          - **NotificationType** *(string) --* **[REQUIRED]**

            Whether the notification is for how much you have spent (``ACTUAL`` ) or for how much you're
            forecasted to spend (``FORECASTED`` ).

          - **ComparisonOperator** *(string) --* **[REQUIRED]**

            The comparison that is used for this notification.

          - **Threshold** *(float) --* **[REQUIRED]**

            The threshold that is associated with a notification. Thresholds are always a percentage.

          - **ThresholdType** *(string) --*

            The type of threshold for a notification. For ``ABSOLUTE_VALUE`` thresholds, AWS notifies you
            when you go over or are forecasted to go over your total cost threshold. For ``PERCENTAGE``
            thresholds, AWS notifies you when you go over or are forecasted to go over a certain percentage
            of your forecasted spend. For example, if you have a budget for 200 dollars and you have a
            ``PERCENTAGE`` threshold of 80%, AWS notifies you when you go over 160 dollars.

          - **NotificationState** *(string) --*

            Whether this notification is in alarm. If a budget notification is in the ``ALARM`` state, you
            have passed the set threshold for the budget.

        :type MaxResults: integer
        :param MaxResults:

          An optional integer that represents how many entries a paginated response contains. The maximum
          is 100.

        :type NextToken: string
        :param NextToken:

          The pagination token that you include in your request to indicate the next set of results that
          you want to retrieve.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Subscribers': [
                    {
                        'SubscriptionType': 'SNS'|'EMAIL',
                        'Address': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Response of DescribeSubscribersForNotification

            - **Subscribers** *(list) --*

              A list of subscribers that are associated with a notification.

              - *(dict) --*

                The subscriber to a budget notification. The subscriber consists of a subscription type and
                either an Amazon SNS topic or an email address.

                For example, an email subscriber would have the following parameters:

                * A ``subscriptionType`` of ``EMAIL``

                * An ``address`` of ``example@example.com``

                - **SubscriptionType** *(string) --*

                  The type of notification that AWS sends to a subscriber.

                - **Address** *(string) --*

                  The address that AWS sends budget notifications to, either an SNS topic or an email.

                  When you create a subscriber, the value of ``Address`` can't contain line breaks.

            - **NextToken** *(string) --*

              The pagination token in the service response that indicates the next set of results that you
              can retrieve.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        Generate a presigned url given a client, its method, and arguments

        :type ClientMethod: string
        :param ClientMethod: The client method to presign for

        :type Params: dict
        :param Params: The parameters normally passed to
            ``ClientMethod``.

        :type ExpiresIn: int
        :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)

        :type HttpMethod: string
        :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method's model.

        :returns: The presigned url
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_budget(
        self, AccountId: str, NewBudget: ClientUpdateBudgetNewBudgetTypeDef
    ) -> Dict:
        """
        Updates a budget. You can change every part of a budget except for the ``budgetName`` and the
        ``calculatedSpend`` . When you modify a budget, the ``calculatedSpend`` drops to zero until AWS has
        new usage data to use for forecasting.

        .. warning::

          Only one of ``BudgetLimit`` or ``PlannedBudgetLimits`` can be present in the syntax at one time.
          Use the syntax that matches your case. The Request Syntax section shows the ``BudgetLimit``
          syntax. For ``PlannedBudgetLimits`` , see the `Examples
          <https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_UpdateBudget.html#API_UpdateBudget_Examples>`__
          section.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/UpdateBudget>`_

        **Request Syntax**
        ::

          response = client.update_budget(
              AccountId='string',
              NewBudget={
                  'BudgetName': 'string',
                  'BudgetLimit': {
                      'Amount': 'string',
                      'Unit': 'string'
                  },
                  'PlannedBudgetLimits': {
                      'string': {
                          'Amount': 'string',
                          'Unit': 'string'
                      }
                  },
                  'CostFilters': {
                      'string': [
                          'string',
                      ]
                  },
                  'CostTypes': {
                      'IncludeTax': True|False,
                      'IncludeSubscription': True|False,
                      'UseBlended': True|False,
                      'IncludeRefund': True|False,
                      'IncludeCredit': True|False,
                      'IncludeUpfront': True|False,
                      'IncludeRecurring': True|False,
                      'IncludeOtherSubscription': True|False,
                      'IncludeSupport': True|False,
                      'IncludeDiscount': True|False,
                      'UseAmortized': True|False
                  },
                  'TimeUnit': 'DAILY'|'MONTHLY'|'QUARTERLY'|'ANNUALLY',
                  'TimePeriod': {
                      'Start': datetime(2015, 1, 1),
                      'End': datetime(2015, 1, 1)
                  },
                  'CalculatedSpend': {
                      'ActualSpend': {
                          'Amount': 'string',
                          'Unit': 'string'
                      },
                      'ForecastedSpend': {
                          'Amount': 'string',
                          'Unit': 'string'
                      }
                  },
                  'BudgetType':
                  'USAGE'|'COST'|'RI_UTILIZATION'|'RI_COVERAGE'|'SAVINGS_PLANS_UTILIZATION'
                  |'SAVINGS_PLANS_COVERAGE',
                  'LastUpdatedTime': datetime(2015, 1, 1)
              }
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The ``accountId`` that is associated with the budget that you want to update.

        :type NewBudget: dict
        :param NewBudget: **[REQUIRED]**

          The budget that you want to update your budget to.

          - **BudgetName** *(string) --* **[REQUIRED]**

            The name of a budget. The name must be unique within an account. The ``:`` and ``\\``
            characters aren't allowed in ``BudgetName`` .

          - **BudgetLimit** *(dict) --*

            The total amount of cost, usage, RI utilization, RI coverage, Savings Plans utilization, or
            Savings Plans coverage that you want to track with your budget.

             ``BudgetLimit`` is required for cost or usage budgets, but optional for RI or Savings Plans
             utilization or coverage budgets. RI and Savings Plans utilization or coverage budgets default
             to ``100`` , which is the only valid value for RI or Savings Plans utilization or coverage
             budgets. You can't use ``BudgetLimit`` with ``PlannedBudgetLimits`` for ``CreateBudget`` and
             ``UpdateBudget`` actions.

            - **Amount** *(string) --* **[REQUIRED]**

              The cost or usage amount that is associated with a budget forecast, actual spend, or budget
              threshold.

            - **Unit** *(string) --* **[REQUIRED]**

              The unit of measurement that is used for the budget forecast, actual spend, or budget
              threshold, such as dollars or GB.

          - **PlannedBudgetLimits** *(dict) --*

            A map containing multiple ``BudgetLimit`` , including current or future limits.

             ``PlannedBudgetLimits`` is available for cost or usage budget and supports monthly and
             quarterly ``TimeUnit`` .

            For monthly budgets, provide 12 months of ``PlannedBudgetLimits`` values. This must start from
            the current month and include the next 11 months. The ``key`` is the start of the month,
            ``UTC`` in epoch seconds.

            For quarterly budgets, provide 4 quarters of ``PlannedBudgetLimits`` value entries in standard
            calendar quarter increments. This must start from the current quarter and include the next 3
            quarters. The ``key`` is the start of the quarter, ``UTC`` in epoch seconds.

            If the planned budget expires before 12 months for monthly or 4 quarters for quarterly, provide
            the ``PlannedBudgetLimits`` values only for the remaining periods.

            If the budget begins at a date in the future, provide ``PlannedBudgetLimits`` values from the
            start date of the budget.

            After all of the ``BudgetLimit`` values in ``PlannedBudgetLimits`` are used, the budget
            continues to use the last limit as the ``BudgetLimit`` . At that point, the planned budget
            provides the same experience as a fixed budget.

             ``DescribeBudget`` and ``DescribeBudgets`` response along with ``PlannedBudgetLimits`` will
             also contain ``BudgetLimit`` representing the current month or quarter limit present in
             ``PlannedBudgetLimits`` . This only applies to budgets created with ``PlannedBudgetLimits`` .
             Budgets created without ``PlannedBudgetLimits`` will only contain ``BudgetLimit`` , and no
             ``PlannedBudgetLimits`` .

            - *(string) --*

              A generic string.

              - *(dict) --*

                The amount of cost or usage that is measured for a budget.

                For example, a ``Spend`` for ``3 GB`` of S3 usage would have the following parameters:

                * An ``Amount`` of ``3``

                * A ``unit`` of ``GB``

                - **Amount** *(string) --* **[REQUIRED]**

                  The cost or usage amount that is associated with a budget forecast, actual spend, or
                  budget threshold.

                - **Unit** *(string) --* **[REQUIRED]**

                  The unit of measurement that is used for the budget forecast, actual spend, or budget
                  threshold, such as dollars or GB.

          - **CostFilters** *(dict) --*

            The cost filters, such as service or tag, that are applied to a budget.

            AWS Budgets supports the following services as a filter for RI budgets:

            * Amazon Elastic Compute Cloud - Compute

            * Amazon Redshift

            * Amazon Relational Database Service

            * Amazon ElastiCache

            * Amazon Elasticsearch Service

            - *(string) --*

              A generic string.

              - *(list) --*

                - *(string) --*

                  A generic string.

          - **CostTypes** *(dict) --*

            The types of costs that are included in this ``COST`` budget.

             ``USAGE`` , ``RI_UTILIZATION`` , ``RI_COVERAGE`` , ``Savings_Plans_Utilization`` , and
             ``Savings_Plans_Coverage`` budgets do not have ``CostTypes`` .

            - **IncludeTax** *(boolean) --*

              Specifies whether a budget includes taxes.

              The default value is ``true`` .

            - **IncludeSubscription** *(boolean) --*

              Specifies whether a budget includes subscriptions.

              The default value is ``true`` .

            - **UseBlended** *(boolean) --*

              Specifies whether a budget uses a blended rate.

              The default value is ``false`` .

            - **IncludeRefund** *(boolean) --*

              Specifies whether a budget includes refunds.

              The default value is ``true`` .

            - **IncludeCredit** *(boolean) --*

              Specifies whether a budget includes credits.

              The default value is ``true`` .

            - **IncludeUpfront** *(boolean) --*

              Specifies whether a budget includes upfront RI costs.

              The default value is ``true`` .

            - **IncludeRecurring** *(boolean) --*

              Specifies whether a budget includes recurring fees such as monthly RI fees.

              The default value is ``true`` .

            - **IncludeOtherSubscription** *(boolean) --*

              Specifies whether a budget includes non-RI subscription costs.

              The default value is ``true`` .

            - **IncludeSupport** *(boolean) --*

              Specifies whether a budget includes support subscription fees.

              The default value is ``true`` .

            - **IncludeDiscount** *(boolean) --*

              Specifies whether a budget includes discounts.

              The default value is ``true`` .

            - **UseAmortized** *(boolean) --*

              Specifies whether a budget uses the amortized rate.

              The default value is ``false`` .

          - **TimeUnit** *(string) --* **[REQUIRED]**

            The length of time until a budget resets the actual and forecasted spend. ``DAILY`` is
            available only for ``RI_UTILIZATION`` , ``RI_COVERAGE`` , ``Savings_Plans_Utilization`` , and
            ``Savings_Plans_Coverage`` budgets.

          - **TimePeriod** *(dict) --*

            The period of time that is covered by a budget. The period has a start date and an end date.
            The start date must come before the end date. The end date must come before ``06/15/87 00:00
            UTC`` .

            If you create your budget and don't specify a start date, AWS defaults to the start of your
            chosen time period (DAILY, MONTHLY, QUARTERLY, or ANNUALLY). For example, if you created your
            budget on January 24, 2018, chose ``DAILY`` , and didn't set a start date, AWS set your start
            date to ``01/24/18 00:00 UTC`` . If you chose ``MONTHLY`` , AWS set your start date to
            ``01/01/18 00:00 UTC`` . If you didn't specify an end date, AWS set your end date to ``06/15/87
            00:00 UTC`` . The defaults are the same for the AWS Billing and Cost Management console and the
            API.

            You can change either date with the ``UpdateBudget`` operation.

            After the end date, AWS deletes the budget and all associated notifications and subscribers.

            - **Start** *(datetime) --*

              The start date for a budget. If you created your budget and didn't specify a start date, AWS
              defaults to the start of your chosen time period (DAILY, MONTHLY, QUARTERLY, or ANNUALLY).
              For example, if you created your budget on January 24, 2018, chose ``DAILY`` , and didn't set
              a start date, AWS set your start date to ``01/24/18 00:00 UTC`` . If you chose ``MONTHLY`` ,
              AWS set your start date to ``01/01/18 00:00 UTC`` . The defaults are the same for the AWS
              Billing and Cost Management console and the API.

              You can change your start date with the ``UpdateBudget`` operation.

            - **End** *(datetime) --*

              The end date for a budget. If you didn't specify an end date, AWS set your end date to
              ``06/15/87 00:00 UTC`` . The defaults are the same for the AWS Billing and Cost Management
              console and the API.

              After the end date, AWS deletes the budget and all associated notifications and subscribers.
              You can change your end date with the ``UpdateBudget`` operation.

          - **CalculatedSpend** *(dict) --*

            The actual and forecasted cost or usage that the budget tracks.

            - **ActualSpend** *(dict) --* **[REQUIRED]**

              The amount of cost, usage, or RI units that you have used.

              - **Amount** *(string) --* **[REQUIRED]**

                The cost or usage amount that is associated with a budget forecast, actual spend, or budget
                threshold.

              - **Unit** *(string) --* **[REQUIRED]**

                The unit of measurement that is used for the budget forecast, actual spend, or budget
                threshold, such as dollars or GB.

            - **ForecastedSpend** *(dict) --*

              The amount of cost, usage, or RI units that you are forecasted to use.

              - **Amount** *(string) --* **[REQUIRED]**

                The cost or usage amount that is associated with a budget forecast, actual spend, or budget
                threshold.

              - **Unit** *(string) --* **[REQUIRED]**

                The unit of measurement that is used for the budget forecast, actual spend, or budget
                threshold, such as dollars or GB.

          - **BudgetType** *(string) --* **[REQUIRED]**

            Whether this budget tracks costs, usage, RI utilization, RI coverage, Savings Plans
            utilization, or Savings Plans coverage.

          - **LastUpdatedTime** *(datetime) --*

            The last time that you updated this budget.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*

            Response of UpdateBudget

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_notification(
        self,
        AccountId: str,
        BudgetName: str,
        OldNotification: ClientUpdateNotificationOldNotificationTypeDef,
        NewNotification: ClientUpdateNotificationNewNotificationTypeDef,
    ) -> Dict:
        """
        Updates a notification.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/UpdateNotification>`_

        **Request Syntax**
        ::

          response = client.update_notification(
              AccountId='string',
              BudgetName='string',
              OldNotification={
                  'NotificationType': 'ACTUAL'|'FORECASTED',
                  'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
                  'Threshold': 123.0,
                  'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
                  'NotificationState': 'OK'|'ALARM'
              },
              NewNotification={
                  'NotificationType': 'ACTUAL'|'FORECASTED',
                  'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
                  'Threshold': 123.0,
                  'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
                  'NotificationState': 'OK'|'ALARM'
              }
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The ``accountId`` that is associated with the budget whose notification you want to update.

        :type BudgetName: string
        :param BudgetName: **[REQUIRED]**

          The name of the budget whose notification you want to update.

        :type OldNotification: dict
        :param OldNotification: **[REQUIRED]**

          The previous notification that is associated with a budget.

          - **NotificationType** *(string) --* **[REQUIRED]**

            Whether the notification is for how much you have spent (``ACTUAL`` ) or for how much you're
            forecasted to spend (``FORECASTED`` ).

          - **ComparisonOperator** *(string) --* **[REQUIRED]**

            The comparison that is used for this notification.

          - **Threshold** *(float) --* **[REQUIRED]**

            The threshold that is associated with a notification. Thresholds are always a percentage.

          - **ThresholdType** *(string) --*

            The type of threshold for a notification. For ``ABSOLUTE_VALUE`` thresholds, AWS notifies you
            when you go over or are forecasted to go over your total cost threshold. For ``PERCENTAGE``
            thresholds, AWS notifies you when you go over or are forecasted to go over a certain percentage
            of your forecasted spend. For example, if you have a budget for 200 dollars and you have a
            ``PERCENTAGE`` threshold of 80%, AWS notifies you when you go over 160 dollars.

          - **NotificationState** *(string) --*

            Whether this notification is in alarm. If a budget notification is in the ``ALARM`` state, you
            have passed the set threshold for the budget.

        :type NewNotification: dict
        :param NewNotification: **[REQUIRED]**

          The updated notification to be associated with a budget.

          - **NotificationType** *(string) --* **[REQUIRED]**

            Whether the notification is for how much you have spent (``ACTUAL`` ) or for how much you're
            forecasted to spend (``FORECASTED`` ).

          - **ComparisonOperator** *(string) --* **[REQUIRED]**

            The comparison that is used for this notification.

          - **Threshold** *(float) --* **[REQUIRED]**

            The threshold that is associated with a notification. Thresholds are always a percentage.

          - **ThresholdType** *(string) --*

            The type of threshold for a notification. For ``ABSOLUTE_VALUE`` thresholds, AWS notifies you
            when you go over or are forecasted to go over your total cost threshold. For ``PERCENTAGE``
            thresholds, AWS notifies you when you go over or are forecasted to go over a certain percentage
            of your forecasted spend. For example, if you have a budget for 200 dollars and you have a
            ``PERCENTAGE`` threshold of 80%, AWS notifies you when you go over 160 dollars.

          - **NotificationState** *(string) --*

            Whether this notification is in alarm. If a budget notification is in the ``ALARM`` state, you
            have passed the set threshold for the budget.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*

            Response of UpdateNotification

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_subscriber(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: ClientUpdateSubscriberNotificationTypeDef,
        OldSubscriber: ClientUpdateSubscriberOldSubscriberTypeDef,
        NewSubscriber: ClientUpdateSubscriberNewSubscriberTypeDef,
    ) -> Dict:
        """
        Updates a subscriber.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/budgets-2016-10-20/UpdateSubscriber>`_

        **Request Syntax**
        ::

          response = client.update_subscriber(
              AccountId='string',
              BudgetName='string',
              Notification={
                  'NotificationType': 'ACTUAL'|'FORECASTED',
                  'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
                  'Threshold': 123.0,
                  'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
                  'NotificationState': 'OK'|'ALARM'
              },
              OldSubscriber={
                  'SubscriptionType': 'SNS'|'EMAIL',
                  'Address': 'string'
              },
              NewSubscriber={
                  'SubscriptionType': 'SNS'|'EMAIL',
                  'Address': 'string'
              }
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The ``accountId`` that is associated with the budget whose subscriber you want to update.

        :type BudgetName: string
        :param BudgetName: **[REQUIRED]**

          The name of the budget whose subscriber you want to update.

        :type Notification: dict
        :param Notification: **[REQUIRED]**

          The notification whose subscriber you want to update.

          - **NotificationType** *(string) --* **[REQUIRED]**

            Whether the notification is for how much you have spent (``ACTUAL`` ) or for how much you're
            forecasted to spend (``FORECASTED`` ).

          - **ComparisonOperator** *(string) --* **[REQUIRED]**

            The comparison that is used for this notification.

          - **Threshold** *(float) --* **[REQUIRED]**

            The threshold that is associated with a notification. Thresholds are always a percentage.

          - **ThresholdType** *(string) --*

            The type of threshold for a notification. For ``ABSOLUTE_VALUE`` thresholds, AWS notifies you
            when you go over or are forecasted to go over your total cost threshold. For ``PERCENTAGE``
            thresholds, AWS notifies you when you go over or are forecasted to go over a certain percentage
            of your forecasted spend. For example, if you have a budget for 200 dollars and you have a
            ``PERCENTAGE`` threshold of 80%, AWS notifies you when you go over 160 dollars.

          - **NotificationState** *(string) --*

            Whether this notification is in alarm. If a budget notification is in the ``ALARM`` state, you
            have passed the set threshold for the budget.

        :type OldSubscriber: dict
        :param OldSubscriber: **[REQUIRED]**

          The previous subscriber that is associated with a budget notification.

          - **SubscriptionType** *(string) --* **[REQUIRED]**

            The type of notification that AWS sends to a subscriber.

          - **Address** *(string) --* **[REQUIRED]**

            The address that AWS sends budget notifications to, either an SNS topic or an email.

            When you create a subscriber, the value of ``Address`` can't contain line breaks.

        :type NewSubscriber: dict
        :param NewSubscriber: **[REQUIRED]**

          The updated subscriber that is associated with a budget notification.

          - **SubscriptionType** *(string) --* **[REQUIRED]**

            The type of notification that AWS sends to a subscriber.

          - **Address** *(string) --* **[REQUIRED]**

            The address that AWS sends budget notifications to, either an SNS topic or an email.

            When you create a subscriber, the value of ``Address`` can't contain line breaks.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*

            Response of UpdateSubscriber

        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_budgets"]
    ) -> paginator_scope.DescribeBudgetsPaginator:
        """
        Get Paginator for `describe_budgets` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_notifications_for_budget"]
    ) -> paginator_scope.DescribeNotificationsForBudgetPaginator:
        """
        Get Paginator for `describe_notifications_for_budget` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_subscribers_for_notification"]
    ) -> paginator_scope.DescribeSubscribersForNotificationPaginator:
        """
        Get Paginator for `describe_subscribers_for_notification` operation.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        """
        Create a paginator for an operation.

        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you'd normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator("create_foo")``.

        :raise OperationNotPageableError: Raised if the operation is not
            pageable.  You can use the ``client.can_paginate`` method to
            check if an operation is pageable.

        :rtype: L{botocore.paginate.Paginator}
        :return: A paginator object.
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    CreationLimitExceededException: Boto3ClientError
    DuplicateRecordException: Boto3ClientError
    ExpiredNextTokenException: Boto3ClientError
    InternalErrorException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    NotFoundException: Boto3ClientError
