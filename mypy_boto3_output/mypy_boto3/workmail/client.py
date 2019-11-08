from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def associate_delegate_to_resource(
        self, OrganizationId: str, ResourceId: str, EntityId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def associate_member_to_group(
        self, OrganizationId: str, GroupId: str, MemberId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_alias(
        self, OrganizationId: str, EntityId: str, Alias: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_group(self, OrganizationId: str, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_resource(
        self, OrganizationId: str, Name: str, Type: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_user(
        self, OrganizationId: str, Name: str, DisplayName: str, Password: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_alias(
        self, OrganizationId: str, EntityId: str, Alias: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_group(self, OrganizationId: str, GroupId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_mailbox_permissions(
        self, OrganizationId: str, EntityId: str, GranteeId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_resource(self, OrganizationId: str, ResourceId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_user(self, OrganizationId: str, UserId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def deregister_from_work_mail(
        self, OrganizationId: str, EntityId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_group(self, OrganizationId: str, GroupId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_organization(self, OrganizationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_resource(self, OrganizationId: str, ResourceId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_user(self, OrganizationId: str, UserId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate_delegate_from_resource(
        self, OrganizationId: str, ResourceId: str, EntityId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate_member_from_group(
        self, OrganizationId: str, GroupId: str, MemberId: str
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
    def get_mailbox_details(self, OrganizationId: str, UserId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_aliases(
        self,
        OrganizationId: str,
        EntityId: str,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_group_members(
        self,
        OrganizationId: str,
        GroupId: str,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_groups(
        self, OrganizationId: str, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_mailbox_permissions(
        self,
        OrganizationId: str,
        EntityId: str,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_organizations(
        self, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_resource_delegates(
        self,
        OrganizationId: str,
        ResourceId: str,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_resources(
        self, OrganizationId: str, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_users(
        self, OrganizationId: str, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_mailbox_permissions(
        self,
        OrganizationId: str,
        EntityId: str,
        GranteeId: str,
        PermissionValues: List[Any],
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def register_to_work_mail(
        self, OrganizationId: str, EntityId: str, Email: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reset_password(
        self, OrganizationId: str, UserId: str, Password: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_mailbox_quota(
        self, OrganizationId: str, UserId: str, MailboxQuota: int
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_primary_email_address(
        self, OrganizationId: str, EntityId: str, Email: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_resource(
        self,
        OrganizationId: str,
        ResourceId: str,
        Name: str = None,
        BookingOptions: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
