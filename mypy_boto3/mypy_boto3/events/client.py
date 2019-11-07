from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def activate_event_source(
        self,
        Name: str,
    ):
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_event_bus(
        self,
        Name: str,
        EventSourceName: Optional[str] = None,
    ) -> Dict:
        pass


    def create_partner_event_source(
        self,
        Name: str,
        Account: str,
    ) -> Dict:
        pass


    def deactivate_event_source(
        self,
        Name: str,
    ):
        pass


    def delete_event_bus(
        self,
        Name: str,
    ):
        pass


    def delete_partner_event_source(
        self,
        Name: str,
        Account: str,
    ):
        pass


    def delete_rule(
        self,
        Name: str,
        EventBusName: Optional[str] = None,
        Force: Optional[bool] = None,
    ):
        pass


    def describe_event_bus(
        self,
        Name: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_event_source(
        self,
        Name: str,
    ) -> Dict:
        pass


    def describe_partner_event_source(
        self,
        Name: str,
    ) -> Dict:
        pass


    def describe_rule(
        self,
        Name: str,
        EventBusName: Optional[str] = None,
    ) -> Dict:
        pass


    def disable_rule(
        self,
        Name: str,
        EventBusName: Optional[str] = None,
    ):
        pass


    def enable_rule(
        self,
        Name: str,
        EventBusName: Optional[str] = None,
    ):
        pass


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
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


    def list_event_buses(
        self,
        NamePrefix: Optional[str] = None,
        NextToken: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def list_event_sources(
        self,
        NamePrefix: Optional[str] = None,
        NextToken: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def list_partner_event_source_accounts(
        self,
        EventSourceName: str,
        NextToken: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def list_partner_event_sources(
        self,
        NamePrefix: str,
        NextToken: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def list_rule_names_by_target(
        self,
        TargetArn: str,
        EventBusName: Optional[str] = None,
        NextToken: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def list_rules(
        self,
        NamePrefix: Optional[str] = None,
        EventBusName: Optional[str] = None,
        NextToken: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        ResourceARN: str,
    ) -> Dict:
        pass


    def list_targets_by_rule(
        self,
        Rule: str,
        EventBusName: Optional[str] = None,
        NextToken: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def put_events(
        self,
        Entries: List,
    ) -> Dict:
        pass


    def put_partner_events(
        self,
        Entries: List,
    ) -> Dict:
        pass


    def put_permission(
        self,
        Action: str,
        Principal: str,
        StatementId: str,
        EventBusName: Optional[str] = None,
        Condition: Optional[Dict] = None,
    ):
        pass


    def put_rule(
        self,
        Name: str,
        ScheduleExpression: Optional[str] = None,
        EventPattern: Optional[str] = None,
        State: Optional[str] = None,
        Description: Optional[str] = None,
        RoleArn: Optional[str] = None,
        Tags: Optional[List] = None,
        EventBusName: Optional[str] = None,
    ) -> Dict:
        pass


    def put_targets(
        self,
        Rule: str,
        Targets: List,
        EventBusName: Optional[str] = None,
    ) -> Dict:
        pass


    def remove_permission(
        self,
        StatementId: str,
        EventBusName: Optional[str] = None,
    ):
        pass


    def remove_targets(
        self,
        Rule: str,
        Ids: List,
        EventBusName: Optional[str] = None,
        Force: Optional[bool] = None,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        ResourceARN: str,
        Tags: List,
    ) -> Dict:
        pass


    def test_event_pattern(
        self,
        EventPattern: str,
        Event: str,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        ResourceARN: str,
        TagKeys: List,
    ) -> Dict:
        pass

