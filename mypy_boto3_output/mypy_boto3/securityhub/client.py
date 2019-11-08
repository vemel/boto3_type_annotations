from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def accept_invitation(self, MasterId: str, InvitationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_disable_standards(
        self, StandardsSubscriptionArns: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_enable_standards(
        self, StandardsSubscriptionRequests: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_import_findings(self, Findings: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_action_target(
        self, Name: str, Description: str, Id: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_insight(
        self, Name: str, Filters: Dict[str, Any], GroupByAttribute: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_members(self, AccountDetails: List[Any] = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def decline_invitations(self, AccountIds: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_action_target(self, ActionTargetArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_insight(self, InsightArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_invitations(self, AccountIds: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_members(self, AccountIds: List[Any] = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_action_targets(
        self,
        ActionTargetArns: List[Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_hub(self, HubArn: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_products(
        self, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disable_import_findings_for_product(
        self, ProductSubscriptionArn: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disable_security_hub(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate_from_master_account(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate_members(self, AccountIds: List[Any] = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def enable_import_findings_for_product(self, ProductArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def enable_security_hub(self, Tags: Dict[str, Any] = None) -> Dict[str, Any]:
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
    def get_enabled_standards(
        self,
        StandardsSubscriptionArns: List[Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_findings(
        self,
        Filters: Dict[str, Any] = None,
        SortCriteria: List[Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_insight_results(self, InsightArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_insights(
        self,
        InsightArns: List[Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_invitations_count(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_master_account(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_members(self, AccountIds: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def invite_members(self, AccountIds: List[Any] = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_enabled_products_for_import(
        self, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_invitations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_members(
        self, OnlyAssociated: bool = None, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(self, ResourceArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, ResourceArn: str, Tags: Dict[str, Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, ResourceArn: str, TagKeys: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_action_target(
        self, ActionTargetArn: str, Name: str = None, Description: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_findings(
        self,
        Filters: Dict[str, Any],
        Note: Dict[str, Any] = None,
        RecordState: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_insight(
        self,
        InsightArn: str,
        Name: str = None,
        Filters: Dict[str, Any] = None,
        GroupByAttribute: str = None,
    ) -> Dict[str, Any]:
        pass
