from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_budget(
        self,
        AccountId: str,
        Budget: Dict[str, Any],
        NotificationsWithSubscribers: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_notification(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: Dict[str, Any],
        Subscribers: List[Any],
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_subscriber(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: Dict[str, Any],
        Subscriber: Dict[str, Any],
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_budget(self, AccountId: str, BudgetName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_notification(
        self, AccountId: str, BudgetName: str, Notification: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_subscriber(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: Dict[str, Any],
        Subscriber: Dict[str, Any],
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_budget(self, AccountId: str, BudgetName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_budget_performance_history(
        self,
        AccountId: str,
        BudgetName: str,
        TimePeriod: Dict[str, Any] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_budgets(
        self, AccountId: str, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_notifications_for_budget(
        self,
        AccountId: str,
        BudgetName: str,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_subscribers_for_notification(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: Dict[str, Any],
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def generate_presigned_url(
        self,
        ClientMethod: str = None,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = None,
        HttpMethod: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def update_budget(
        self, AccountId: str, NewBudget: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_notification(
        self,
        AccountId: str,
        BudgetName: str,
        OldNotification: Dict[str, Any],
        NewNotification: Dict[str, Any],
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_subscriber(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: Dict[str, Any],
        OldSubscriber: Dict[str, Any],
        NewSubscriber: Dict[str, Any],
    ) -> Dict[str, Any]:
        pass
