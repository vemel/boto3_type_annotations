from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def associate_admin_account(self, AdminAccount: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_notification_channel(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_policy(
        self, PolicyId: str, DeleteAllPolicyResources: bool = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def disassociate_admin_account(self) -> None:
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
    def get_admin_account(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_compliance_detail(
        self, PolicyId: str, MemberAccount: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_notification_channel(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_policy(self, PolicyId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_protection_status(
        self,
        PolicyId: str,
        MemberAccountId: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_compliance_status(
        self, PolicyId: str, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_member_accounts(
        self, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_policies(
        self, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_notification_channel(self, SnsTopicArn: str, SnsRoleName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def put_policy(self, Policy: Dict[str, Any]) -> Dict[str, Any]:
        pass
