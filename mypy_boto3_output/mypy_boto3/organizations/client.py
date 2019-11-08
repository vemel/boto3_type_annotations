from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def accept_handshake(self, HandshakeId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def attach_policy(self, PolicyId: str, TargetId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def cancel_handshake(self, HandshakeId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_account(
        self,
        Email: str,
        AccountName: str,
        RoleName: str = None,
        IamUserAccessToBilling: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_gov_cloud_account(
        self,
        Email: str,
        AccountName: str,
        RoleName: str = None,
        IamUserAccessToBilling: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_organization(self, FeatureSet: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_organizational_unit(self, ParentId: str, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_policy(
        self, Content: str, Description: str, Name: str, Type: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def decline_handshake(self, HandshakeId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_organization(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_organizational_unit(self, OrganizationalUnitId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_policy(self, PolicyId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def describe_account(self, AccountId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_create_account_status(
        self, CreateAccountRequestId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_handshake(self, HandshakeId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_organization(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_organizational_unit(self, OrganizationalUnitId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_policy(self, PolicyId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def detach_policy(self, PolicyId: str, TargetId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def disable_aws_service_access(self, ServicePrincipal: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def disable_policy_type(self, RootId: str, PolicyType: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def enable_all_features(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def enable_aws_service_access(self, ServicePrincipal: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def enable_policy_type(self, RootId: str, PolicyType: str) -> Dict[str, Any]:
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
    def invite_account_to_organization(
        self, Target: Dict[str, Any], Notes: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def leave_organization(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def list_accounts(
        self, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_accounts_for_parent(
        self, ParentId: str, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_aws_service_access_for_organization(
        self, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_children(
        self,
        ParentId: str,
        ChildType: str,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_create_account_status(
        self, States: List[Any] = None, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_handshakes_for_account(
        self,
        Filter: Dict[str, Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_handshakes_for_organization(
        self,
        Filter: Dict[str, Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_organizational_units_for_parent(
        self, ParentId: str, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_parents(
        self, ChildId: str, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_policies(
        self, Filter: str, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_policies_for_target(
        self, TargetId: str, Filter: str, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_roots(
        self, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(
        self, ResourceId: str, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_targets_for_policy(
        self, PolicyId: str, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def move_account(
        self, AccountId: str, SourceParentId: str, DestinationParentId: str
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def remove_account_from_organization(self, AccountId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, ResourceId: str, Tags: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, ResourceId: str, TagKeys: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_organizational_unit(
        self, OrganizationalUnitId: str, Name: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_policy(
        self,
        PolicyId: str,
        Name: str = None,
        Description: str = None,
        Content: str = None,
    ) -> Dict[str, Any]:
        pass
