from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_group(
        self, GroupName: str, AwsAccountId: str, Namespace: str, Description: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_group_membership(
        self, MemberName: str, GroupName: str, AwsAccountId: str, Namespace: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_group(
        self, GroupName: str, AwsAccountId: str, Namespace: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_group_membership(
        self, MemberName: str, GroupName: str, AwsAccountId: str, Namespace: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_user(
        self, UserName: str, AwsAccountId: str, Namespace: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_user_by_principal_id(
        self, PrincipalId: str, AwsAccountId: str, Namespace: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_group(
        self, GroupName: str, AwsAccountId: str, Namespace: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_user(
        self, UserName: str, AwsAccountId: str, Namespace: str
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
    def get_dashboard_embed_url(
        self,
        AwsAccountId: str,
        DashboardId: str,
        IdentityType: str,
        SessionLifetimeInMinutes: int = None,
        UndoRedoDisabled: bool = None,
        ResetDisabled: bool = None,
        UserArn: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_group_memberships(
        self,
        GroupName: str,
        AwsAccountId: str,
        Namespace: str,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_groups(
        self,
        AwsAccountId: str,
        Namespace: str,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_user_groups(
        self,
        UserName: str,
        AwsAccountId: str,
        Namespace: str,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_users(
        self,
        AwsAccountId: str,
        Namespace: str,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def register_user(
        self,
        IdentityType: str,
        Email: str,
        UserRole: str,
        AwsAccountId: str,
        Namespace: str,
        IamArn: str = None,
        SessionName: str = None,
        UserName: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_group(
        self, GroupName: str, AwsAccountId: str, Namespace: str, Description: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_user(
        self, UserName: str, AwsAccountId: str, Namespace: str, Email: str, Role: str
    ) -> Dict[str, Any]:
        pass
