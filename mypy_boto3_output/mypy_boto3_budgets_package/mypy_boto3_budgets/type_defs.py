"Main interface for budgets type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateBudgetBudgetBudgetLimitTypeDef",
    "ClientCreateBudgetBudgetCalculatedSpendActualSpendTypeDef",
    "ClientCreateBudgetBudgetCalculatedSpendForecastedSpendTypeDef",
    "ClientCreateBudgetBudgetCalculatedSpendTypeDef",
    "ClientCreateBudgetBudgetCostTypesTypeDef",
    "ClientCreateBudgetBudgetPlannedBudgetLimitsTypeDef",
    "ClientCreateBudgetBudgetTimePeriodTypeDef",
    "ClientCreateBudgetBudgetTypeDef",
    "ClientCreateBudgetNotificationsWithSubscribersNotificationTypeDef",
    "ClientCreateBudgetNotificationsWithSubscribersSubscribersTypeDef",
    "ClientCreateBudgetNotificationsWithSubscribersTypeDef",
    "ClientCreateNotificationNotificationTypeDef",
    "ClientCreateNotificationSubscribersTypeDef",
    "ClientCreateSubscriberNotificationTypeDef",
    "ClientCreateSubscriberSubscriberTypeDef",
    "ClientDeleteNotificationNotificationTypeDef",
    "ClientDeleteSubscriberNotificationTypeDef",
    "ClientDeleteSubscriberSubscriberTypeDef",
    "ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListActualAmountTypeDef",
    "ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListBudgetedAmountTypeDef",
    "ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListTimePeriodTypeDef",
    "ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListTypeDef",
    "ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryCostTypesTypeDef",
    "ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryTypeDef",
    "ClientDescribeBudgetPerformanceHistoryResponseTypeDef",
    "ClientDescribeBudgetPerformanceHistoryTimePeriodTypeDef",
    "ClientDescribeBudgetResponseBudgetBudgetLimitTypeDef",
    "ClientDescribeBudgetResponseBudgetCalculatedSpendActualSpendTypeDef",
    "ClientDescribeBudgetResponseBudgetCalculatedSpendForecastedSpendTypeDef",
    "ClientDescribeBudgetResponseBudgetCalculatedSpendTypeDef",
    "ClientDescribeBudgetResponseBudgetCostTypesTypeDef",
    "ClientDescribeBudgetResponseBudgetPlannedBudgetLimitsTypeDef",
    "ClientDescribeBudgetResponseBudgetTimePeriodTypeDef",
    "ClientDescribeBudgetResponseBudgetTypeDef",
    "ClientDescribeBudgetResponseTypeDef",
    "ClientDescribeBudgetsResponseBudgetsBudgetLimitTypeDef",
    "ClientDescribeBudgetsResponseBudgetsCalculatedSpendActualSpendTypeDef",
    "ClientDescribeBudgetsResponseBudgetsCalculatedSpendForecastedSpendTypeDef",
    "ClientDescribeBudgetsResponseBudgetsCalculatedSpendTypeDef",
    "ClientDescribeBudgetsResponseBudgetsCostTypesTypeDef",
    "ClientDescribeBudgetsResponseBudgetsPlannedBudgetLimitsTypeDef",
    "ClientDescribeBudgetsResponseBudgetsTimePeriodTypeDef",
    "ClientDescribeBudgetsResponseBudgetsTypeDef",
    "ClientDescribeBudgetsResponseTypeDef",
    "ClientDescribeNotificationsForBudgetResponseNotificationsTypeDef",
    "ClientDescribeNotificationsForBudgetResponseTypeDef",
    "ClientDescribeSubscribersForNotificationNotificationTypeDef",
    "ClientDescribeSubscribersForNotificationResponseSubscribersTypeDef",
    "ClientDescribeSubscribersForNotificationResponseTypeDef",
    "ClientUpdateBudgetNewBudgetBudgetLimitTypeDef",
    "ClientUpdateBudgetNewBudgetCalculatedSpendActualSpendTypeDef",
    "ClientUpdateBudgetNewBudgetCalculatedSpendForecastedSpendTypeDef",
    "ClientUpdateBudgetNewBudgetCalculatedSpendTypeDef",
    "ClientUpdateBudgetNewBudgetCostTypesTypeDef",
    "ClientUpdateBudgetNewBudgetPlannedBudgetLimitsTypeDef",
    "ClientUpdateBudgetNewBudgetTimePeriodTypeDef",
    "ClientUpdateBudgetNewBudgetTypeDef",
    "ClientUpdateNotificationNewNotificationTypeDef",
    "ClientUpdateNotificationOldNotificationTypeDef",
    "ClientUpdateSubscriberNewSubscriberTypeDef",
    "ClientUpdateSubscriberNotificationTypeDef",
    "ClientUpdateSubscriberOldSubscriberTypeDef",
    "DescribeBudgetsPaginatePaginationConfigTypeDef",
    "DescribeBudgetsPaginateResponseBudgetsBudgetLimitTypeDef",
    "DescribeBudgetsPaginateResponseBudgetsCalculatedSpendActualSpendTypeDef",
    "DescribeBudgetsPaginateResponseBudgetsCalculatedSpendForecastedSpendTypeDef",
    "DescribeBudgetsPaginateResponseBudgetsCalculatedSpendTypeDef",
    "DescribeBudgetsPaginateResponseBudgetsCostTypesTypeDef",
    "DescribeBudgetsPaginateResponseBudgetsPlannedBudgetLimitsTypeDef",
    "DescribeBudgetsPaginateResponseBudgetsTimePeriodTypeDef",
    "DescribeBudgetsPaginateResponseBudgetsTypeDef",
    "DescribeBudgetsPaginateResponseTypeDef",
    "DescribeNotificationsForBudgetPaginatePaginationConfigTypeDef",
    "DescribeNotificationsForBudgetPaginateResponseNotificationsTypeDef",
    "DescribeNotificationsForBudgetPaginateResponseTypeDef",
    "DescribeSubscribersForNotificationPaginateNotificationTypeDef",
    "DescribeSubscribersForNotificationPaginatePaginationConfigTypeDef",
    "DescribeSubscribersForNotificationPaginateResponseSubscribersTypeDef",
    "DescribeSubscribersForNotificationPaginateResponseTypeDef",
)


_ClientCreateBudgetBudgetBudgetLimitTypeDef = TypedDict(
    "_ClientCreateBudgetBudgetBudgetLimitTypeDef", {"Amount": str, "Unit": str}
)


class ClientCreateBudgetBudgetBudgetLimitTypeDef(
    _ClientCreateBudgetBudgetBudgetLimitTypeDef
):
    """
    Type definition for `ClientCreateBudgetBudget` `BudgetLimit`

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
    """


_ClientCreateBudgetBudgetCalculatedSpendActualSpendTypeDef = TypedDict(
    "_ClientCreateBudgetBudgetCalculatedSpendActualSpendTypeDef",
    {"Amount": str, "Unit": str},
)


class ClientCreateBudgetBudgetCalculatedSpendActualSpendTypeDef(
    _ClientCreateBudgetBudgetCalculatedSpendActualSpendTypeDef
):
    """
    Type definition for `ClientCreateBudgetBudgetCalculatedSpend` `ActualSpend`

    The amount of cost, usage, or RI units that you have used.

    - **Amount** *(string) --* **[REQUIRED]**

      The cost or usage amount that is associated with a budget forecast, actual spend, or budget
      threshold.

    - **Unit** *(string) --* **[REQUIRED]**

      The unit of measurement that is used for the budget forecast, actual spend, or budget
      threshold, such as dollars or GB.
    """


_ClientCreateBudgetBudgetCalculatedSpendForecastedSpendTypeDef = TypedDict(
    "_ClientCreateBudgetBudgetCalculatedSpendForecastedSpendTypeDef",
    {"Amount": str, "Unit": str},
)


class ClientCreateBudgetBudgetCalculatedSpendForecastedSpendTypeDef(
    _ClientCreateBudgetBudgetCalculatedSpendForecastedSpendTypeDef
):
    """
    Type definition for `ClientCreateBudgetBudgetCalculatedSpend` `ForecastedSpend`

    The amount of cost, usage, or RI units that you are forecasted to use.

    - **Amount** *(string) --* **[REQUIRED]**

      The cost or usage amount that is associated with a budget forecast, actual spend, or budget
      threshold.

    - **Unit** *(string) --* **[REQUIRED]**

      The unit of measurement that is used for the budget forecast, actual spend, or budget
      threshold, such as dollars or GB.
    """


_RequiredClientCreateBudgetBudgetCalculatedSpendTypeDef = TypedDict(
    "_RequiredClientCreateBudgetBudgetCalculatedSpendTypeDef",
    {"ActualSpend": ClientCreateBudgetBudgetCalculatedSpendActualSpendTypeDef},
)
_OptionalClientCreateBudgetBudgetCalculatedSpendTypeDef = TypedDict(
    "_OptionalClientCreateBudgetBudgetCalculatedSpendTypeDef",
    {"ForecastedSpend": ClientCreateBudgetBudgetCalculatedSpendForecastedSpendTypeDef},
    total=False,
)


class ClientCreateBudgetBudgetCalculatedSpendTypeDef(
    _RequiredClientCreateBudgetBudgetCalculatedSpendTypeDef,
    _OptionalClientCreateBudgetBudgetCalculatedSpendTypeDef,
):
    """
    Type definition for `ClientCreateBudgetBudget` `CalculatedSpend`

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
    """


_ClientCreateBudgetBudgetCostTypesTypeDef = TypedDict(
    "_ClientCreateBudgetBudgetCostTypesTypeDef",
    {
        "IncludeTax": bool,
        "IncludeSubscription": bool,
        "UseBlended": bool,
        "IncludeRefund": bool,
        "IncludeCredit": bool,
        "IncludeUpfront": bool,
        "IncludeRecurring": bool,
        "IncludeOtherSubscription": bool,
        "IncludeSupport": bool,
        "IncludeDiscount": bool,
        "UseAmortized": bool,
    },
    total=False,
)


class ClientCreateBudgetBudgetCostTypesTypeDef(
    _ClientCreateBudgetBudgetCostTypesTypeDef
):
    """
    Type definition for `ClientCreateBudgetBudget` `CostTypes`

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
    """


_ClientCreateBudgetBudgetPlannedBudgetLimitsTypeDef = TypedDict(
    "_ClientCreateBudgetBudgetPlannedBudgetLimitsTypeDef", {"Amount": str, "Unit": str}
)


class ClientCreateBudgetBudgetPlannedBudgetLimitsTypeDef(
    _ClientCreateBudgetBudgetPlannedBudgetLimitsTypeDef
):
    """
    Type definition for `ClientCreateBudgetBudget` `PlannedBudgetLimits`

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
    """


_ClientCreateBudgetBudgetTimePeriodTypeDef = TypedDict(
    "_ClientCreateBudgetBudgetTimePeriodTypeDef",
    {"Start": datetime, "End": datetime},
    total=False,
)


class ClientCreateBudgetBudgetTimePeriodTypeDef(
    _ClientCreateBudgetBudgetTimePeriodTypeDef
):
    """
    Type definition for `ClientCreateBudgetBudget` `TimePeriod`

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
    """


_RequiredClientCreateBudgetBudgetTypeDef = TypedDict(
    "_RequiredClientCreateBudgetBudgetTypeDef",
    {"BudgetName": str, "TimeUnit": str, "BudgetType": str},
)
_OptionalClientCreateBudgetBudgetTypeDef = TypedDict(
    "_OptionalClientCreateBudgetBudgetTypeDef",
    {
        "BudgetLimit": ClientCreateBudgetBudgetBudgetLimitTypeDef,
        "PlannedBudgetLimits": Dict[
            str, ClientCreateBudgetBudgetPlannedBudgetLimitsTypeDef
        ],
        "CostFilters": Dict[str, List[str]],
        "CostTypes": ClientCreateBudgetBudgetCostTypesTypeDef,
        "TimePeriod": ClientCreateBudgetBudgetTimePeriodTypeDef,
        "CalculatedSpend": ClientCreateBudgetBudgetCalculatedSpendTypeDef,
        "LastUpdatedTime": datetime,
    },
    total=False,
)


class ClientCreateBudgetBudgetTypeDef(
    _RequiredClientCreateBudgetBudgetTypeDef, _OptionalClientCreateBudgetBudgetTypeDef
):
    """
    Type definition for `ClientCreateBudget` `Budget`

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
    """


_RequiredClientCreateBudgetNotificationsWithSubscribersNotificationTypeDef = TypedDict(
    "_RequiredClientCreateBudgetNotificationsWithSubscribersNotificationTypeDef",
    {"NotificationType": str, "ComparisonOperator": str, "Threshold": float},
)
_OptionalClientCreateBudgetNotificationsWithSubscribersNotificationTypeDef = TypedDict(
    "_OptionalClientCreateBudgetNotificationsWithSubscribersNotificationTypeDef",
    {"ThresholdType": str, "NotificationState": str},
    total=False,
)


class ClientCreateBudgetNotificationsWithSubscribersNotificationTypeDef(
    _RequiredClientCreateBudgetNotificationsWithSubscribersNotificationTypeDef,
    _OptionalClientCreateBudgetNotificationsWithSubscribersNotificationTypeDef,
):
    """
    Type definition for `ClientCreateBudgetNotificationsWithSubscribers` `Notification`

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
    """


_ClientCreateBudgetNotificationsWithSubscribersSubscribersTypeDef = TypedDict(
    "_ClientCreateBudgetNotificationsWithSubscribersSubscribersTypeDef",
    {"SubscriptionType": str, "Address": str},
)


class ClientCreateBudgetNotificationsWithSubscribersSubscribersTypeDef(
    _ClientCreateBudgetNotificationsWithSubscribersSubscribersTypeDef
):
    """
    Type definition for `ClientCreateBudgetNotificationsWithSubscribers` `Subscribers`

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
    """


_ClientCreateBudgetNotificationsWithSubscribersTypeDef = TypedDict(
    "_ClientCreateBudgetNotificationsWithSubscribersTypeDef",
    {
        "Notification": ClientCreateBudgetNotificationsWithSubscribersNotificationTypeDef,
        "Subscribers": List[
            ClientCreateBudgetNotificationsWithSubscribersSubscribersTypeDef
        ],
    },
)


class ClientCreateBudgetNotificationsWithSubscribersTypeDef(
    _ClientCreateBudgetNotificationsWithSubscribersTypeDef
):
    """
    Type definition for `ClientCreateBudget` `NotificationsWithSubscribers`

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
    """


_RequiredClientCreateNotificationNotificationTypeDef = TypedDict(
    "_RequiredClientCreateNotificationNotificationTypeDef",
    {"NotificationType": str, "ComparisonOperator": str, "Threshold": float},
)
_OptionalClientCreateNotificationNotificationTypeDef = TypedDict(
    "_OptionalClientCreateNotificationNotificationTypeDef",
    {"ThresholdType": str, "NotificationState": str},
    total=False,
)


class ClientCreateNotificationNotificationTypeDef(
    _RequiredClientCreateNotificationNotificationTypeDef,
    _OptionalClientCreateNotificationNotificationTypeDef,
):
    """
    Type definition for `ClientCreateNotification` `Notification`

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
    """


_ClientCreateNotificationSubscribersTypeDef = TypedDict(
    "_ClientCreateNotificationSubscribersTypeDef",
    {"SubscriptionType": str, "Address": str},
)


class ClientCreateNotificationSubscribersTypeDef(
    _ClientCreateNotificationSubscribersTypeDef
):
    """
    Type definition for `ClientCreateNotification` `Subscribers`

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
    """


_RequiredClientCreateSubscriberNotificationTypeDef = TypedDict(
    "_RequiredClientCreateSubscriberNotificationTypeDef",
    {"NotificationType": str, "ComparisonOperator": str, "Threshold": float},
)
_OptionalClientCreateSubscriberNotificationTypeDef = TypedDict(
    "_OptionalClientCreateSubscriberNotificationTypeDef",
    {"ThresholdType": str, "NotificationState": str},
    total=False,
)


class ClientCreateSubscriberNotificationTypeDef(
    _RequiredClientCreateSubscriberNotificationTypeDef,
    _OptionalClientCreateSubscriberNotificationTypeDef,
):
    """
    Type definition for `ClientCreateSubscriber` `Notification`

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
    """


_ClientCreateSubscriberSubscriberTypeDef = TypedDict(
    "_ClientCreateSubscriberSubscriberTypeDef",
    {"SubscriptionType": str, "Address": str},
)


class ClientCreateSubscriberSubscriberTypeDef(_ClientCreateSubscriberSubscriberTypeDef):
    """
    Type definition for `ClientCreateSubscriber` `Subscriber`

    The subscriber that you want to associate with a budget notification.

    - **SubscriptionType** *(string) --* **[REQUIRED]**

      The type of notification that AWS sends to a subscriber.

    - **Address** *(string) --* **[REQUIRED]**

      The address that AWS sends budget notifications to, either an SNS topic or an email.

      When you create a subscriber, the value of ``Address`` can't contain line breaks.
    """


_RequiredClientDeleteNotificationNotificationTypeDef = TypedDict(
    "_RequiredClientDeleteNotificationNotificationTypeDef",
    {"NotificationType": str, "ComparisonOperator": str, "Threshold": float},
)
_OptionalClientDeleteNotificationNotificationTypeDef = TypedDict(
    "_OptionalClientDeleteNotificationNotificationTypeDef",
    {"ThresholdType": str, "NotificationState": str},
    total=False,
)


class ClientDeleteNotificationNotificationTypeDef(
    _RequiredClientDeleteNotificationNotificationTypeDef,
    _OptionalClientDeleteNotificationNotificationTypeDef,
):
    """
    Type definition for `ClientDeleteNotification` `Notification`

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
    """


_RequiredClientDeleteSubscriberNotificationTypeDef = TypedDict(
    "_RequiredClientDeleteSubscriberNotificationTypeDef",
    {"NotificationType": str, "ComparisonOperator": str, "Threshold": float},
)
_OptionalClientDeleteSubscriberNotificationTypeDef = TypedDict(
    "_OptionalClientDeleteSubscriberNotificationTypeDef",
    {"ThresholdType": str, "NotificationState": str},
    total=False,
)


class ClientDeleteSubscriberNotificationTypeDef(
    _RequiredClientDeleteSubscriberNotificationTypeDef,
    _OptionalClientDeleteSubscriberNotificationTypeDef,
):
    """
    Type definition for `ClientDeleteSubscriber` `Notification`

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
    """


_ClientDeleteSubscriberSubscriberTypeDef = TypedDict(
    "_ClientDeleteSubscriberSubscriberTypeDef",
    {"SubscriptionType": str, "Address": str},
)


class ClientDeleteSubscriberSubscriberTypeDef(_ClientDeleteSubscriberSubscriberTypeDef):
    """
    Type definition for `ClientDeleteSubscriber` `Subscriber`

    The subscriber that you want to delete.

    - **SubscriptionType** *(string) --* **[REQUIRED]**

      The type of notification that AWS sends to a subscriber.

    - **Address** *(string) --* **[REQUIRED]**

      The address that AWS sends budget notifications to, either an SNS topic or an email.

      When you create a subscriber, the value of ``Address`` can't contain line breaks.
    """


_ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListActualAmountTypeDef = TypedDict(
    "_ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListActualAmountTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListActualAmountTypeDef(
    _ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListActualAmountTypeDef
):
    """
    Type definition for `ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsList` `ActualAmount`

    Your actual costs or usage for a budget period.

    - **Amount** *(string) --*

      The cost or usage amount that is associated with a budget forecast, actual spend, or
      budget threshold.

    - **Unit** *(string) --*

      The unit of measurement that is used for the budget forecast, actual spend, or budget
      threshold, such as dollars or GB.
    """


_ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListBudgetedAmountTypeDef = TypedDict(
    "_ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListBudgetedAmountTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListBudgetedAmountTypeDef(
    _ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListBudgetedAmountTypeDef
):
    """
    Type definition for `ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsList` `BudgetedAmount`

    The amount of cost or usage that you created the budget for.

    - **Amount** *(string) --*

      The cost or usage amount that is associated with a budget forecast, actual spend, or
      budget threshold.

    - **Unit** *(string) --*

      The unit of measurement that is used for the budget forecast, actual spend, or budget
      threshold, such as dollars or GB.
    """


_ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListTimePeriodTypeDef = TypedDict(
    "_ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListTimePeriodTypeDef",
    {"Start": datetime, "End": datetime},
    total=False,
)


class ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListTimePeriodTypeDef(
    _ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListTimePeriodTypeDef
):
    """
    Type definition for `ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsList` `TimePeriod`

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
    """


_ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListTypeDef = TypedDict(
    "_ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListTypeDef",
    {
        "BudgetedAmount": ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListBudgetedAmountTypeDef,
        "ActualAmount": ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListActualAmountTypeDef,
        "TimePeriod": ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListTimePeriodTypeDef,
    },
    total=False,
)


class ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListTypeDef(
    _ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListTypeDef
):
    """
    Type definition for `ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistory` `BudgetedAndActualAmountsList`

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
    """


_ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryCostTypesTypeDef = TypedDict(
    "_ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryCostTypesTypeDef",
    {
        "IncludeTax": bool,
        "IncludeSubscription": bool,
        "UseBlended": bool,
        "IncludeRefund": bool,
        "IncludeCredit": bool,
        "IncludeUpfront": bool,
        "IncludeRecurring": bool,
        "IncludeOtherSubscription": bool,
        "IncludeSupport": bool,
        "IncludeDiscount": bool,
        "UseAmortized": bool,
    },
    total=False,
)


class ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryCostTypesTypeDef(
    _ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryCostTypesTypeDef
):
    """
    Type definition for `ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistory` `CostTypes`

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
    """


_ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryTypeDef = TypedDict(
    "_ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryTypeDef",
    {
        "BudgetName": str,
        "BudgetType": str,
        "CostFilters": Dict[str, List[str]],
        "CostTypes": ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryCostTypesTypeDef,
        "TimeUnit": str,
        "BudgetedAndActualAmountsList": List[
            ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListTypeDef
        ],
    },
    total=False,
)


class ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryTypeDef(
    _ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryTypeDef
):
    """
    Type definition for `ClientDescribeBudgetPerformanceHistoryResponse` `BudgetPerformanceHistory`

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
    """


_ClientDescribeBudgetPerformanceHistoryResponseTypeDef = TypedDict(
    "_ClientDescribeBudgetPerformanceHistoryResponseTypeDef",
    {
        "BudgetPerformanceHistory": ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryTypeDef,
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeBudgetPerformanceHistoryResponseTypeDef(
    _ClientDescribeBudgetPerformanceHistoryResponseTypeDef
):
    """
    Type definition for `ClientDescribeBudgetPerformanceHistory` `Response`

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


_ClientDescribeBudgetPerformanceHistoryTimePeriodTypeDef = TypedDict(
    "_ClientDescribeBudgetPerformanceHistoryTimePeriodTypeDef",
    {"Start": datetime, "End": datetime},
    total=False,
)


class ClientDescribeBudgetPerformanceHistoryTimePeriodTypeDef(
    _ClientDescribeBudgetPerformanceHistoryTimePeriodTypeDef
):
    """
    Type definition for `ClientDescribeBudgetPerformanceHistory` `TimePeriod`

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
    """


_ClientDescribeBudgetResponseBudgetBudgetLimitTypeDef = TypedDict(
    "_ClientDescribeBudgetResponseBudgetBudgetLimitTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientDescribeBudgetResponseBudgetBudgetLimitTypeDef(
    _ClientDescribeBudgetResponseBudgetBudgetLimitTypeDef
):
    """
    Type definition for `ClientDescribeBudgetResponseBudget` `BudgetLimit`

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
    """


_ClientDescribeBudgetResponseBudgetCalculatedSpendActualSpendTypeDef = TypedDict(
    "_ClientDescribeBudgetResponseBudgetCalculatedSpendActualSpendTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientDescribeBudgetResponseBudgetCalculatedSpendActualSpendTypeDef(
    _ClientDescribeBudgetResponseBudgetCalculatedSpendActualSpendTypeDef
):
    """
    Type definition for `ClientDescribeBudgetResponseBudgetCalculatedSpend` `ActualSpend`

    The amount of cost, usage, or RI units that you have used.

    - **Amount** *(string) --*

      The cost or usage amount that is associated with a budget forecast, actual spend, or
      budget threshold.

    - **Unit** *(string) --*

      The unit of measurement that is used for the budget forecast, actual spend, or budget
      threshold, such as dollars or GB.
    """


_ClientDescribeBudgetResponseBudgetCalculatedSpendForecastedSpendTypeDef = TypedDict(
    "_ClientDescribeBudgetResponseBudgetCalculatedSpendForecastedSpendTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientDescribeBudgetResponseBudgetCalculatedSpendForecastedSpendTypeDef(
    _ClientDescribeBudgetResponseBudgetCalculatedSpendForecastedSpendTypeDef
):
    """
    Type definition for `ClientDescribeBudgetResponseBudgetCalculatedSpend` `ForecastedSpend`

    The amount of cost, usage, or RI units that you are forecasted to use.

    - **Amount** *(string) --*

      The cost or usage amount that is associated with a budget forecast, actual spend, or
      budget threshold.

    - **Unit** *(string) --*

      The unit of measurement that is used for the budget forecast, actual spend, or budget
      threshold, such as dollars or GB.
    """


_ClientDescribeBudgetResponseBudgetCalculatedSpendTypeDef = TypedDict(
    "_ClientDescribeBudgetResponseBudgetCalculatedSpendTypeDef",
    {
        "ActualSpend": ClientDescribeBudgetResponseBudgetCalculatedSpendActualSpendTypeDef,
        "ForecastedSpend": ClientDescribeBudgetResponseBudgetCalculatedSpendForecastedSpendTypeDef,
    },
    total=False,
)


class ClientDescribeBudgetResponseBudgetCalculatedSpendTypeDef(
    _ClientDescribeBudgetResponseBudgetCalculatedSpendTypeDef
):
    """
    Type definition for `ClientDescribeBudgetResponseBudget` `CalculatedSpend`

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
    """


_ClientDescribeBudgetResponseBudgetCostTypesTypeDef = TypedDict(
    "_ClientDescribeBudgetResponseBudgetCostTypesTypeDef",
    {
        "IncludeTax": bool,
        "IncludeSubscription": bool,
        "UseBlended": bool,
        "IncludeRefund": bool,
        "IncludeCredit": bool,
        "IncludeUpfront": bool,
        "IncludeRecurring": bool,
        "IncludeOtherSubscription": bool,
        "IncludeSupport": bool,
        "IncludeDiscount": bool,
        "UseAmortized": bool,
    },
    total=False,
)


class ClientDescribeBudgetResponseBudgetCostTypesTypeDef(
    _ClientDescribeBudgetResponseBudgetCostTypesTypeDef
):
    """
    Type definition for `ClientDescribeBudgetResponseBudget` `CostTypes`

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
    """


_ClientDescribeBudgetResponseBudgetPlannedBudgetLimitsTypeDef = TypedDict(
    "_ClientDescribeBudgetResponseBudgetPlannedBudgetLimitsTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientDescribeBudgetResponseBudgetPlannedBudgetLimitsTypeDef(
    _ClientDescribeBudgetResponseBudgetPlannedBudgetLimitsTypeDef
):
    """
    Type definition for `ClientDescribeBudgetResponseBudget` `PlannedBudgetLimits`

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
    """


_ClientDescribeBudgetResponseBudgetTimePeriodTypeDef = TypedDict(
    "_ClientDescribeBudgetResponseBudgetTimePeriodTypeDef",
    {"Start": datetime, "End": datetime},
    total=False,
)


class ClientDescribeBudgetResponseBudgetTimePeriodTypeDef(
    _ClientDescribeBudgetResponseBudgetTimePeriodTypeDef
):
    """
    Type definition for `ClientDescribeBudgetResponseBudget` `TimePeriod`

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
    """


_ClientDescribeBudgetResponseBudgetTypeDef = TypedDict(
    "_ClientDescribeBudgetResponseBudgetTypeDef",
    {
        "BudgetName": str,
        "BudgetLimit": ClientDescribeBudgetResponseBudgetBudgetLimitTypeDef,
        "PlannedBudgetLimits": Dict[
            str, ClientDescribeBudgetResponseBudgetPlannedBudgetLimitsTypeDef
        ],
        "CostFilters": Dict[str, List[str]],
        "CostTypes": ClientDescribeBudgetResponseBudgetCostTypesTypeDef,
        "TimeUnit": str,
        "TimePeriod": ClientDescribeBudgetResponseBudgetTimePeriodTypeDef,
        "CalculatedSpend": ClientDescribeBudgetResponseBudgetCalculatedSpendTypeDef,
        "BudgetType": str,
        "LastUpdatedTime": datetime,
    },
    total=False,
)


class ClientDescribeBudgetResponseBudgetTypeDef(
    _ClientDescribeBudgetResponseBudgetTypeDef
):
    """
    Type definition for `ClientDescribeBudgetResponse` `Budget`

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


_ClientDescribeBudgetResponseTypeDef = TypedDict(
    "_ClientDescribeBudgetResponseTypeDef",
    {"Budget": ClientDescribeBudgetResponseBudgetTypeDef},
    total=False,
)


class ClientDescribeBudgetResponseTypeDef(_ClientDescribeBudgetResponseTypeDef):
    """
    Type definition for `ClientDescribeBudget` `Response`

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


_ClientDescribeBudgetsResponseBudgetsBudgetLimitTypeDef = TypedDict(
    "_ClientDescribeBudgetsResponseBudgetsBudgetLimitTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientDescribeBudgetsResponseBudgetsBudgetLimitTypeDef(
    _ClientDescribeBudgetsResponseBudgetsBudgetLimitTypeDef
):
    """
    Type definition for `ClientDescribeBudgetsResponseBudgets` `BudgetLimit`

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
    """


_ClientDescribeBudgetsResponseBudgetsCalculatedSpendActualSpendTypeDef = TypedDict(
    "_ClientDescribeBudgetsResponseBudgetsCalculatedSpendActualSpendTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientDescribeBudgetsResponseBudgetsCalculatedSpendActualSpendTypeDef(
    _ClientDescribeBudgetsResponseBudgetsCalculatedSpendActualSpendTypeDef
):
    """
    Type definition for `ClientDescribeBudgetsResponseBudgetsCalculatedSpend` `ActualSpend`

    The amount of cost, usage, or RI units that you have used.

    - **Amount** *(string) --*

      The cost or usage amount that is associated with a budget forecast, actual spend, or
      budget threshold.

    - **Unit** *(string) --*

      The unit of measurement that is used for the budget forecast, actual spend, or budget
      threshold, such as dollars or GB.
    """


_ClientDescribeBudgetsResponseBudgetsCalculatedSpendForecastedSpendTypeDef = TypedDict(
    "_ClientDescribeBudgetsResponseBudgetsCalculatedSpendForecastedSpendTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientDescribeBudgetsResponseBudgetsCalculatedSpendForecastedSpendTypeDef(
    _ClientDescribeBudgetsResponseBudgetsCalculatedSpendForecastedSpendTypeDef
):
    """
    Type definition for `ClientDescribeBudgetsResponseBudgetsCalculatedSpend` `ForecastedSpend`

    The amount of cost, usage, or RI units that you are forecasted to use.

    - **Amount** *(string) --*

      The cost or usage amount that is associated with a budget forecast, actual spend, or
      budget threshold.

    - **Unit** *(string) --*

      The unit of measurement that is used for the budget forecast, actual spend, or budget
      threshold, such as dollars or GB.
    """


_ClientDescribeBudgetsResponseBudgetsCalculatedSpendTypeDef = TypedDict(
    "_ClientDescribeBudgetsResponseBudgetsCalculatedSpendTypeDef",
    {
        "ActualSpend": ClientDescribeBudgetsResponseBudgetsCalculatedSpendActualSpendTypeDef,
        "ForecastedSpend": ClientDescribeBudgetsResponseBudgetsCalculatedSpendForecastedSpendTypeDef,
    },
    total=False,
)


class ClientDescribeBudgetsResponseBudgetsCalculatedSpendTypeDef(
    _ClientDescribeBudgetsResponseBudgetsCalculatedSpendTypeDef
):
    """
    Type definition for `ClientDescribeBudgetsResponseBudgets` `CalculatedSpend`

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
    """


_ClientDescribeBudgetsResponseBudgetsCostTypesTypeDef = TypedDict(
    "_ClientDescribeBudgetsResponseBudgetsCostTypesTypeDef",
    {
        "IncludeTax": bool,
        "IncludeSubscription": bool,
        "UseBlended": bool,
        "IncludeRefund": bool,
        "IncludeCredit": bool,
        "IncludeUpfront": bool,
        "IncludeRecurring": bool,
        "IncludeOtherSubscription": bool,
        "IncludeSupport": bool,
        "IncludeDiscount": bool,
        "UseAmortized": bool,
    },
    total=False,
)


class ClientDescribeBudgetsResponseBudgetsCostTypesTypeDef(
    _ClientDescribeBudgetsResponseBudgetsCostTypesTypeDef
):
    """
    Type definition for `ClientDescribeBudgetsResponseBudgets` `CostTypes`

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
    """


_ClientDescribeBudgetsResponseBudgetsPlannedBudgetLimitsTypeDef = TypedDict(
    "_ClientDescribeBudgetsResponseBudgetsPlannedBudgetLimitsTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientDescribeBudgetsResponseBudgetsPlannedBudgetLimitsTypeDef(
    _ClientDescribeBudgetsResponseBudgetsPlannedBudgetLimitsTypeDef
):
    """
    Type definition for `ClientDescribeBudgetsResponseBudgets` `PlannedBudgetLimits`

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
    """


_ClientDescribeBudgetsResponseBudgetsTimePeriodTypeDef = TypedDict(
    "_ClientDescribeBudgetsResponseBudgetsTimePeriodTypeDef",
    {"Start": datetime, "End": datetime},
    total=False,
)


class ClientDescribeBudgetsResponseBudgetsTimePeriodTypeDef(
    _ClientDescribeBudgetsResponseBudgetsTimePeriodTypeDef
):
    """
    Type definition for `ClientDescribeBudgetsResponseBudgets` `TimePeriod`

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
    """


_ClientDescribeBudgetsResponseBudgetsTypeDef = TypedDict(
    "_ClientDescribeBudgetsResponseBudgetsTypeDef",
    {
        "BudgetName": str,
        "BudgetLimit": ClientDescribeBudgetsResponseBudgetsBudgetLimitTypeDef,
        "PlannedBudgetLimits": Dict[
            str, ClientDescribeBudgetsResponseBudgetsPlannedBudgetLimitsTypeDef
        ],
        "CostFilters": Dict[str, List[str]],
        "CostTypes": ClientDescribeBudgetsResponseBudgetsCostTypesTypeDef,
        "TimeUnit": str,
        "TimePeriod": ClientDescribeBudgetsResponseBudgetsTimePeriodTypeDef,
        "CalculatedSpend": ClientDescribeBudgetsResponseBudgetsCalculatedSpendTypeDef,
        "BudgetType": str,
        "LastUpdatedTime": datetime,
    },
    total=False,
)


class ClientDescribeBudgetsResponseBudgetsTypeDef(
    _ClientDescribeBudgetsResponseBudgetsTypeDef
):
    """
    Type definition for `ClientDescribeBudgetsResponse` `Budgets`

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
    """


_ClientDescribeBudgetsResponseTypeDef = TypedDict(
    "_ClientDescribeBudgetsResponseTypeDef",
    {"Budgets": List[ClientDescribeBudgetsResponseBudgetsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeBudgetsResponseTypeDef(_ClientDescribeBudgetsResponseTypeDef):
    """
    Type definition for `ClientDescribeBudgets` `Response`

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


_ClientDescribeNotificationsForBudgetResponseNotificationsTypeDef = TypedDict(
    "_ClientDescribeNotificationsForBudgetResponseNotificationsTypeDef",
    {
        "NotificationType": str,
        "ComparisonOperator": str,
        "Threshold": float,
        "ThresholdType": str,
        "NotificationState": str,
    },
    total=False,
)


class ClientDescribeNotificationsForBudgetResponseNotificationsTypeDef(
    _ClientDescribeNotificationsForBudgetResponseNotificationsTypeDef
):
    """
    Type definition for `ClientDescribeNotificationsForBudgetResponse` `Notifications`

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
    """


_ClientDescribeNotificationsForBudgetResponseTypeDef = TypedDict(
    "_ClientDescribeNotificationsForBudgetResponseTypeDef",
    {
        "Notifications": List[
            ClientDescribeNotificationsForBudgetResponseNotificationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeNotificationsForBudgetResponseTypeDef(
    _ClientDescribeNotificationsForBudgetResponseTypeDef
):
    """
    Type definition for `ClientDescribeNotificationsForBudget` `Response`

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


_RequiredClientDescribeSubscribersForNotificationNotificationTypeDef = TypedDict(
    "_RequiredClientDescribeSubscribersForNotificationNotificationTypeDef",
    {"NotificationType": str, "ComparisonOperator": str, "Threshold": float},
)
_OptionalClientDescribeSubscribersForNotificationNotificationTypeDef = TypedDict(
    "_OptionalClientDescribeSubscribersForNotificationNotificationTypeDef",
    {"ThresholdType": str, "NotificationState": str},
    total=False,
)


class ClientDescribeSubscribersForNotificationNotificationTypeDef(
    _RequiredClientDescribeSubscribersForNotificationNotificationTypeDef,
    _OptionalClientDescribeSubscribersForNotificationNotificationTypeDef,
):
    """
    Type definition for `ClientDescribeSubscribersForNotification` `Notification`

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
    """


_ClientDescribeSubscribersForNotificationResponseSubscribersTypeDef = TypedDict(
    "_ClientDescribeSubscribersForNotificationResponseSubscribersTypeDef",
    {"SubscriptionType": str, "Address": str},
    total=False,
)


class ClientDescribeSubscribersForNotificationResponseSubscribersTypeDef(
    _ClientDescribeSubscribersForNotificationResponseSubscribersTypeDef
):
    """
    Type definition for `ClientDescribeSubscribersForNotificationResponse` `Subscribers`

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
    """


_ClientDescribeSubscribersForNotificationResponseTypeDef = TypedDict(
    "_ClientDescribeSubscribersForNotificationResponseTypeDef",
    {
        "Subscribers": List[
            ClientDescribeSubscribersForNotificationResponseSubscribersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeSubscribersForNotificationResponseTypeDef(
    _ClientDescribeSubscribersForNotificationResponseTypeDef
):
    """
    Type definition for `ClientDescribeSubscribersForNotification` `Response`

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


_ClientUpdateBudgetNewBudgetBudgetLimitTypeDef = TypedDict(
    "_ClientUpdateBudgetNewBudgetBudgetLimitTypeDef", {"Amount": str, "Unit": str}
)


class ClientUpdateBudgetNewBudgetBudgetLimitTypeDef(
    _ClientUpdateBudgetNewBudgetBudgetLimitTypeDef
):
    """
    Type definition for `ClientUpdateBudgetNewBudget` `BudgetLimit`

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
    """


_ClientUpdateBudgetNewBudgetCalculatedSpendActualSpendTypeDef = TypedDict(
    "_ClientUpdateBudgetNewBudgetCalculatedSpendActualSpendTypeDef",
    {"Amount": str, "Unit": str},
)


class ClientUpdateBudgetNewBudgetCalculatedSpendActualSpendTypeDef(
    _ClientUpdateBudgetNewBudgetCalculatedSpendActualSpendTypeDef
):
    """
    Type definition for `ClientUpdateBudgetNewBudgetCalculatedSpend` `ActualSpend`

    The amount of cost, usage, or RI units that you have used.

    - **Amount** *(string) --* **[REQUIRED]**

      The cost or usage amount that is associated with a budget forecast, actual spend, or budget
      threshold.

    - **Unit** *(string) --* **[REQUIRED]**

      The unit of measurement that is used for the budget forecast, actual spend, or budget
      threshold, such as dollars or GB.
    """


_ClientUpdateBudgetNewBudgetCalculatedSpendForecastedSpendTypeDef = TypedDict(
    "_ClientUpdateBudgetNewBudgetCalculatedSpendForecastedSpendTypeDef",
    {"Amount": str, "Unit": str},
)


class ClientUpdateBudgetNewBudgetCalculatedSpendForecastedSpendTypeDef(
    _ClientUpdateBudgetNewBudgetCalculatedSpendForecastedSpendTypeDef
):
    """
    Type definition for `ClientUpdateBudgetNewBudgetCalculatedSpend` `ForecastedSpend`

    The amount of cost, usage, or RI units that you are forecasted to use.

    - **Amount** *(string) --* **[REQUIRED]**

      The cost or usage amount that is associated with a budget forecast, actual spend, or budget
      threshold.

    - **Unit** *(string) --* **[REQUIRED]**

      The unit of measurement that is used for the budget forecast, actual spend, or budget
      threshold, such as dollars or GB.
    """


_RequiredClientUpdateBudgetNewBudgetCalculatedSpendTypeDef = TypedDict(
    "_RequiredClientUpdateBudgetNewBudgetCalculatedSpendTypeDef",
    {"ActualSpend": ClientUpdateBudgetNewBudgetCalculatedSpendActualSpendTypeDef},
)
_OptionalClientUpdateBudgetNewBudgetCalculatedSpendTypeDef = TypedDict(
    "_OptionalClientUpdateBudgetNewBudgetCalculatedSpendTypeDef",
    {
        "ForecastedSpend": ClientUpdateBudgetNewBudgetCalculatedSpendForecastedSpendTypeDef
    },
    total=False,
)


class ClientUpdateBudgetNewBudgetCalculatedSpendTypeDef(
    _RequiredClientUpdateBudgetNewBudgetCalculatedSpendTypeDef,
    _OptionalClientUpdateBudgetNewBudgetCalculatedSpendTypeDef,
):
    """
    Type definition for `ClientUpdateBudgetNewBudget` `CalculatedSpend`

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
    """


_ClientUpdateBudgetNewBudgetCostTypesTypeDef = TypedDict(
    "_ClientUpdateBudgetNewBudgetCostTypesTypeDef",
    {
        "IncludeTax": bool,
        "IncludeSubscription": bool,
        "UseBlended": bool,
        "IncludeRefund": bool,
        "IncludeCredit": bool,
        "IncludeUpfront": bool,
        "IncludeRecurring": bool,
        "IncludeOtherSubscription": bool,
        "IncludeSupport": bool,
        "IncludeDiscount": bool,
        "UseAmortized": bool,
    },
    total=False,
)


class ClientUpdateBudgetNewBudgetCostTypesTypeDef(
    _ClientUpdateBudgetNewBudgetCostTypesTypeDef
):
    """
    Type definition for `ClientUpdateBudgetNewBudget` `CostTypes`

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
    """


_ClientUpdateBudgetNewBudgetPlannedBudgetLimitsTypeDef = TypedDict(
    "_ClientUpdateBudgetNewBudgetPlannedBudgetLimitsTypeDef",
    {"Amount": str, "Unit": str},
)


class ClientUpdateBudgetNewBudgetPlannedBudgetLimitsTypeDef(
    _ClientUpdateBudgetNewBudgetPlannedBudgetLimitsTypeDef
):
    """
    Type definition for `ClientUpdateBudgetNewBudget` `PlannedBudgetLimits`

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
    """


_ClientUpdateBudgetNewBudgetTimePeriodTypeDef = TypedDict(
    "_ClientUpdateBudgetNewBudgetTimePeriodTypeDef",
    {"Start": datetime, "End": datetime},
    total=False,
)


class ClientUpdateBudgetNewBudgetTimePeriodTypeDef(
    _ClientUpdateBudgetNewBudgetTimePeriodTypeDef
):
    """
    Type definition for `ClientUpdateBudgetNewBudget` `TimePeriod`

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
    """


_RequiredClientUpdateBudgetNewBudgetTypeDef = TypedDict(
    "_RequiredClientUpdateBudgetNewBudgetTypeDef",
    {"BudgetName": str, "TimeUnit": str, "BudgetType": str},
)
_OptionalClientUpdateBudgetNewBudgetTypeDef = TypedDict(
    "_OptionalClientUpdateBudgetNewBudgetTypeDef",
    {
        "BudgetLimit": ClientUpdateBudgetNewBudgetBudgetLimitTypeDef,
        "PlannedBudgetLimits": Dict[
            str, ClientUpdateBudgetNewBudgetPlannedBudgetLimitsTypeDef
        ],
        "CostFilters": Dict[str, List[str]],
        "CostTypes": ClientUpdateBudgetNewBudgetCostTypesTypeDef,
        "TimePeriod": ClientUpdateBudgetNewBudgetTimePeriodTypeDef,
        "CalculatedSpend": ClientUpdateBudgetNewBudgetCalculatedSpendTypeDef,
        "LastUpdatedTime": datetime,
    },
    total=False,
)


class ClientUpdateBudgetNewBudgetTypeDef(
    _RequiredClientUpdateBudgetNewBudgetTypeDef,
    _OptionalClientUpdateBudgetNewBudgetTypeDef,
):
    """
    Type definition for `ClientUpdateBudget` `NewBudget`

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
    """


_RequiredClientUpdateNotificationNewNotificationTypeDef = TypedDict(
    "_RequiredClientUpdateNotificationNewNotificationTypeDef",
    {"NotificationType": str, "ComparisonOperator": str, "Threshold": float},
)
_OptionalClientUpdateNotificationNewNotificationTypeDef = TypedDict(
    "_OptionalClientUpdateNotificationNewNotificationTypeDef",
    {"ThresholdType": str, "NotificationState": str},
    total=False,
)


class ClientUpdateNotificationNewNotificationTypeDef(
    _RequiredClientUpdateNotificationNewNotificationTypeDef,
    _OptionalClientUpdateNotificationNewNotificationTypeDef,
):
    """
    Type definition for `ClientUpdateNotification` `NewNotification`

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
    """


_RequiredClientUpdateNotificationOldNotificationTypeDef = TypedDict(
    "_RequiredClientUpdateNotificationOldNotificationTypeDef",
    {"NotificationType": str, "ComparisonOperator": str, "Threshold": float},
)
_OptionalClientUpdateNotificationOldNotificationTypeDef = TypedDict(
    "_OptionalClientUpdateNotificationOldNotificationTypeDef",
    {"ThresholdType": str, "NotificationState": str},
    total=False,
)


class ClientUpdateNotificationOldNotificationTypeDef(
    _RequiredClientUpdateNotificationOldNotificationTypeDef,
    _OptionalClientUpdateNotificationOldNotificationTypeDef,
):
    """
    Type definition for `ClientUpdateNotification` `OldNotification`

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
    """


_ClientUpdateSubscriberNewSubscriberTypeDef = TypedDict(
    "_ClientUpdateSubscriberNewSubscriberTypeDef",
    {"SubscriptionType": str, "Address": str},
)


class ClientUpdateSubscriberNewSubscriberTypeDef(
    _ClientUpdateSubscriberNewSubscriberTypeDef
):
    """
    Type definition for `ClientUpdateSubscriber` `NewSubscriber`

    The updated subscriber that is associated with a budget notification.

    - **SubscriptionType** *(string) --* **[REQUIRED]**

      The type of notification that AWS sends to a subscriber.

    - **Address** *(string) --* **[REQUIRED]**

      The address that AWS sends budget notifications to, either an SNS topic or an email.

      When you create a subscriber, the value of ``Address`` can't contain line breaks.
    """


_RequiredClientUpdateSubscriberNotificationTypeDef = TypedDict(
    "_RequiredClientUpdateSubscriberNotificationTypeDef",
    {"NotificationType": str, "ComparisonOperator": str, "Threshold": float},
)
_OptionalClientUpdateSubscriberNotificationTypeDef = TypedDict(
    "_OptionalClientUpdateSubscriberNotificationTypeDef",
    {"ThresholdType": str, "NotificationState": str},
    total=False,
)


class ClientUpdateSubscriberNotificationTypeDef(
    _RequiredClientUpdateSubscriberNotificationTypeDef,
    _OptionalClientUpdateSubscriberNotificationTypeDef,
):
    """
    Type definition for `ClientUpdateSubscriber` `Notification`

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
    """


_ClientUpdateSubscriberOldSubscriberTypeDef = TypedDict(
    "_ClientUpdateSubscriberOldSubscriberTypeDef",
    {"SubscriptionType": str, "Address": str},
)


class ClientUpdateSubscriberOldSubscriberTypeDef(
    _ClientUpdateSubscriberOldSubscriberTypeDef
):
    """
    Type definition for `ClientUpdateSubscriber` `OldSubscriber`

    The previous subscriber that is associated with a budget notification.

    - **SubscriptionType** *(string) --* **[REQUIRED]**

      The type of notification that AWS sends to a subscriber.

    - **Address** *(string) --* **[REQUIRED]**

      The address that AWS sends budget notifications to, either an SNS topic or an email.

      When you create a subscriber, the value of ``Address`` can't contain line breaks.
    """


_DescribeBudgetsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeBudgetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeBudgetsPaginatePaginationConfigTypeDef(
    _DescribeBudgetsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeBudgetsPaginate` `PaginationConfig`

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


_DescribeBudgetsPaginateResponseBudgetsBudgetLimitTypeDef = TypedDict(
    "_DescribeBudgetsPaginateResponseBudgetsBudgetLimitTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class DescribeBudgetsPaginateResponseBudgetsBudgetLimitTypeDef(
    _DescribeBudgetsPaginateResponseBudgetsBudgetLimitTypeDef
):
    """
    Type definition for `DescribeBudgetsPaginateResponseBudgets` `BudgetLimit`

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
    """


_DescribeBudgetsPaginateResponseBudgetsCalculatedSpendActualSpendTypeDef = TypedDict(
    "_DescribeBudgetsPaginateResponseBudgetsCalculatedSpendActualSpendTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class DescribeBudgetsPaginateResponseBudgetsCalculatedSpendActualSpendTypeDef(
    _DescribeBudgetsPaginateResponseBudgetsCalculatedSpendActualSpendTypeDef
):
    """
    Type definition for `DescribeBudgetsPaginateResponseBudgetsCalculatedSpend` `ActualSpend`

    The amount of cost, usage, or RI units that you have used.

    - **Amount** *(string) --*

      The cost or usage amount that is associated with a budget forecast, actual spend, or
      budget threshold.

    - **Unit** *(string) --*

      The unit of measurement that is used for the budget forecast, actual spend, or budget
      threshold, such as dollars or GB.
    """


_DescribeBudgetsPaginateResponseBudgetsCalculatedSpendForecastedSpendTypeDef = TypedDict(
    "_DescribeBudgetsPaginateResponseBudgetsCalculatedSpendForecastedSpendTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class DescribeBudgetsPaginateResponseBudgetsCalculatedSpendForecastedSpendTypeDef(
    _DescribeBudgetsPaginateResponseBudgetsCalculatedSpendForecastedSpendTypeDef
):
    """
    Type definition for `DescribeBudgetsPaginateResponseBudgetsCalculatedSpend` `ForecastedSpend`

    The amount of cost, usage, or RI units that you are forecasted to use.

    - **Amount** *(string) --*

      The cost or usage amount that is associated with a budget forecast, actual spend, or
      budget threshold.

    - **Unit** *(string) --*

      The unit of measurement that is used for the budget forecast, actual spend, or budget
      threshold, such as dollars or GB.
    """


_DescribeBudgetsPaginateResponseBudgetsCalculatedSpendTypeDef = TypedDict(
    "_DescribeBudgetsPaginateResponseBudgetsCalculatedSpendTypeDef",
    {
        "ActualSpend": DescribeBudgetsPaginateResponseBudgetsCalculatedSpendActualSpendTypeDef,
        "ForecastedSpend": DescribeBudgetsPaginateResponseBudgetsCalculatedSpendForecastedSpendTypeDef,
    },
    total=False,
)


class DescribeBudgetsPaginateResponseBudgetsCalculatedSpendTypeDef(
    _DescribeBudgetsPaginateResponseBudgetsCalculatedSpendTypeDef
):
    """
    Type definition for `DescribeBudgetsPaginateResponseBudgets` `CalculatedSpend`

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
    """


_DescribeBudgetsPaginateResponseBudgetsCostTypesTypeDef = TypedDict(
    "_DescribeBudgetsPaginateResponseBudgetsCostTypesTypeDef",
    {
        "IncludeTax": bool,
        "IncludeSubscription": bool,
        "UseBlended": bool,
        "IncludeRefund": bool,
        "IncludeCredit": bool,
        "IncludeUpfront": bool,
        "IncludeRecurring": bool,
        "IncludeOtherSubscription": bool,
        "IncludeSupport": bool,
        "IncludeDiscount": bool,
        "UseAmortized": bool,
    },
    total=False,
)


class DescribeBudgetsPaginateResponseBudgetsCostTypesTypeDef(
    _DescribeBudgetsPaginateResponseBudgetsCostTypesTypeDef
):
    """
    Type definition for `DescribeBudgetsPaginateResponseBudgets` `CostTypes`

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
    """


_DescribeBudgetsPaginateResponseBudgetsPlannedBudgetLimitsTypeDef = TypedDict(
    "_DescribeBudgetsPaginateResponseBudgetsPlannedBudgetLimitsTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class DescribeBudgetsPaginateResponseBudgetsPlannedBudgetLimitsTypeDef(
    _DescribeBudgetsPaginateResponseBudgetsPlannedBudgetLimitsTypeDef
):
    """
    Type definition for `DescribeBudgetsPaginateResponseBudgets` `PlannedBudgetLimits`

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
    """


_DescribeBudgetsPaginateResponseBudgetsTimePeriodTypeDef = TypedDict(
    "_DescribeBudgetsPaginateResponseBudgetsTimePeriodTypeDef",
    {"Start": datetime, "End": datetime},
    total=False,
)


class DescribeBudgetsPaginateResponseBudgetsTimePeriodTypeDef(
    _DescribeBudgetsPaginateResponseBudgetsTimePeriodTypeDef
):
    """
    Type definition for `DescribeBudgetsPaginateResponseBudgets` `TimePeriod`

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
    """


_DescribeBudgetsPaginateResponseBudgetsTypeDef = TypedDict(
    "_DescribeBudgetsPaginateResponseBudgetsTypeDef",
    {
        "BudgetName": str,
        "BudgetLimit": DescribeBudgetsPaginateResponseBudgetsBudgetLimitTypeDef,
        "PlannedBudgetLimits": Dict[
            str, DescribeBudgetsPaginateResponseBudgetsPlannedBudgetLimitsTypeDef
        ],
        "CostFilters": Dict[str, List[str]],
        "CostTypes": DescribeBudgetsPaginateResponseBudgetsCostTypesTypeDef,
        "TimeUnit": str,
        "TimePeriod": DescribeBudgetsPaginateResponseBudgetsTimePeriodTypeDef,
        "CalculatedSpend": DescribeBudgetsPaginateResponseBudgetsCalculatedSpendTypeDef,
        "BudgetType": str,
        "LastUpdatedTime": datetime,
    },
    total=False,
)


class DescribeBudgetsPaginateResponseBudgetsTypeDef(
    _DescribeBudgetsPaginateResponseBudgetsTypeDef
):
    """
    Type definition for `DescribeBudgetsPaginateResponse` `Budgets`

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
    """


_DescribeBudgetsPaginateResponseTypeDef = TypedDict(
    "_DescribeBudgetsPaginateResponseTypeDef",
    {"Budgets": List[DescribeBudgetsPaginateResponseBudgetsTypeDef]},
    total=False,
)


class DescribeBudgetsPaginateResponseTypeDef(_DescribeBudgetsPaginateResponseTypeDef):
    """
    Type definition for `DescribeBudgetsPaginate` `Response`

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
    """


_DescribeNotificationsForBudgetPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeNotificationsForBudgetPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeNotificationsForBudgetPaginatePaginationConfigTypeDef(
    _DescribeNotificationsForBudgetPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeNotificationsForBudgetPaginate` `PaginationConfig`

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


_DescribeNotificationsForBudgetPaginateResponseNotificationsTypeDef = TypedDict(
    "_DescribeNotificationsForBudgetPaginateResponseNotificationsTypeDef",
    {
        "NotificationType": str,
        "ComparisonOperator": str,
        "Threshold": float,
        "ThresholdType": str,
        "NotificationState": str,
    },
    total=False,
)


class DescribeNotificationsForBudgetPaginateResponseNotificationsTypeDef(
    _DescribeNotificationsForBudgetPaginateResponseNotificationsTypeDef
):
    """
    Type definition for `DescribeNotificationsForBudgetPaginateResponse` `Notifications`

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
    """


_DescribeNotificationsForBudgetPaginateResponseTypeDef = TypedDict(
    "_DescribeNotificationsForBudgetPaginateResponseTypeDef",
    {
        "Notifications": List[
            DescribeNotificationsForBudgetPaginateResponseNotificationsTypeDef
        ]
    },
    total=False,
)


class DescribeNotificationsForBudgetPaginateResponseTypeDef(
    _DescribeNotificationsForBudgetPaginateResponseTypeDef
):
    """
    Type definition for `DescribeNotificationsForBudgetPaginate` `Response`

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
    """


_RequiredDescribeSubscribersForNotificationPaginateNotificationTypeDef = TypedDict(
    "_RequiredDescribeSubscribersForNotificationPaginateNotificationTypeDef",
    {"NotificationType": str, "ComparisonOperator": str, "Threshold": float},
)
_OptionalDescribeSubscribersForNotificationPaginateNotificationTypeDef = TypedDict(
    "_OptionalDescribeSubscribersForNotificationPaginateNotificationTypeDef",
    {"ThresholdType": str, "NotificationState": str},
    total=False,
)


class DescribeSubscribersForNotificationPaginateNotificationTypeDef(
    _RequiredDescribeSubscribersForNotificationPaginateNotificationTypeDef,
    _OptionalDescribeSubscribersForNotificationPaginateNotificationTypeDef,
):
    """
    Type definition for `DescribeSubscribersForNotificationPaginate` `Notification`

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
    """


_DescribeSubscribersForNotificationPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeSubscribersForNotificationPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeSubscribersForNotificationPaginatePaginationConfigTypeDef(
    _DescribeSubscribersForNotificationPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeSubscribersForNotificationPaginate` `PaginationConfig`

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


_DescribeSubscribersForNotificationPaginateResponseSubscribersTypeDef = TypedDict(
    "_DescribeSubscribersForNotificationPaginateResponseSubscribersTypeDef",
    {"SubscriptionType": str, "Address": str},
    total=False,
)


class DescribeSubscribersForNotificationPaginateResponseSubscribersTypeDef(
    _DescribeSubscribersForNotificationPaginateResponseSubscribersTypeDef
):
    """
    Type definition for `DescribeSubscribersForNotificationPaginateResponse` `Subscribers`

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
    """


_DescribeSubscribersForNotificationPaginateResponseTypeDef = TypedDict(
    "_DescribeSubscribersForNotificationPaginateResponseTypeDef",
    {
        "Subscribers": List[
            DescribeSubscribersForNotificationPaginateResponseSubscribersTypeDef
        ]
    },
    total=False,
)


class DescribeSubscribersForNotificationPaginateResponseTypeDef(
    _DescribeSubscribersForNotificationPaginateResponseTypeDef
):
    """
    Type definition for `DescribeSubscribersForNotificationPaginate` `Response`

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
    """
