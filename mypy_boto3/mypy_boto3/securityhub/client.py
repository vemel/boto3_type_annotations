from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def accept_invitation(
        self,
        MasterId: str,
        InvitationId: str,
    ) -> Dict:
        pass


    def batch_disable_standards(
        self,
        StandardsSubscriptionArns: List,
    ) -> Dict:
        pass


    def batch_enable_standards(
        self,
        StandardsSubscriptionRequests: List,
    ) -> Dict:
        pass


    def batch_import_findings(
        self,
        Findings: List,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_action_target(
        self,
        Name: str,
        Description: str,
        Id: str,
    ) -> Dict:
        pass


    def create_insight(
        self,
        Name: str,
        Filters: Dict,
        GroupByAttribute: str,
    ) -> Dict:
        pass


    def create_members(
        self,
        AccountDetails: Optional[List] = None,
    ) -> Dict:
        pass


    def decline_invitations(
        self,
        AccountIds: List,
    ) -> Dict:
        pass


    def delete_action_target(
        self,
        ActionTargetArn: str,
    ) -> Dict:
        pass


    def delete_insight(
        self,
        InsightArn: str,
    ) -> Dict:
        pass


    def delete_invitations(
        self,
        AccountIds: List,
    ) -> Dict:
        pass


    def delete_members(
        self,
        AccountIds: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_action_targets(
        self,
        ActionTargetArns: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_hub(
        self,
        HubArn: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_products(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def disable_import_findings_for_product(
        self,
        ProductSubscriptionArn: str,
    ) -> Dict:
        pass


    def disable_security_hub(
        self,
    ) -> Dict:
        pass


    def disassociate_from_master_account(
        self,
    ) -> Dict:
        pass


    def disassociate_members(
        self,
        AccountIds: Optional[List] = None,
    ) -> Dict:
        pass


    def enable_import_findings_for_product(
        self,
        ProductArn: str,
    ) -> Dict:
        pass


    def enable_security_hub(
        self,
        Tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
        pass


    def get_enabled_standards(
        self,
        StandardsSubscriptionArns: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_findings(
        self,
        Filters: Optional[Dict] = None,
        SortCriteria: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_insight_results(
        self,
        InsightArn: str,
    ) -> Dict:
        pass


    def get_insights(
        self,
        InsightArns: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_invitations_count(
        self,
    ) -> Dict:
        pass


    def get_master_account(
        self,
    ) -> Dict:
        pass


    def get_members(
        self,
        AccountIds: List,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def invite_members(
        self,
        AccountIds: Optional[List] = None,
    ) -> Dict:
        pass


    def list_enabled_products_for_import(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_invitations(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_members(
        self,
        OnlyAssociated: Optional[bool] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        ResourceArn: str,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        ResourceArn: str,
        Tags: Dict,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        ResourceArn: str,
        TagKeys: List,
    ) -> Dict:
        pass


    def update_action_target(
        self,
        ActionTargetArn: str,
        Name: Optional[str] = None,
        Description: Optional[str] = None,
    ) -> Dict:
        pass


    def update_findings(
        self,
        Filters: Dict,
        Note: Optional[Dict] = None,
        RecordState: Optional[str] = None,
    ) -> Dict:
        pass


    def update_insight(
        self,
        InsightArn: str,
        Name: Optional[str] = None,
        Filters: Optional[Dict] = None,
        GroupByAttribute: Optional[str] = None,
    ) -> Dict:
        pass

