from __future__ import annotations

# builtin imports
from typing import Dict
from typing import Any

# boto3 imports
from botocore.paginate import Paginator


class DescribeBudgets(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, AccountId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeNotificationsForBudget(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, AccountId: str, BudgetName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeSubscribersForNotification(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: Dict[str, Any],
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
