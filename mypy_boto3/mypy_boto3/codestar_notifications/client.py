from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_notification_rule(
        self,
        Name: str,
        EventTypeIds: List,
        Resource: str,
        Targets: List,
        DetailType: str,
        ClientRequestToken: Optional[str] = None,
        Tags: Optional[Dict] = None,
        Status: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_notification_rule(
        self,
        Arn: str,
    ) -> Dict:
        pass


    def delete_target(
        self,
        TargetAddress: str,
        ForceUnsubscribeAll: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_notification_rule(
        self,
        Arn: str,
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


    def list_event_types(
        self,
        Filters: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_notification_rules(
        self,
        Filters: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        Arn: str,
    ) -> Dict:
        pass


    def list_targets(
        self,
        Filters: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def subscribe(
        self,
        Arn: str,
        Target: Dict,
        ClientRequestToken: Optional[str] = None,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        Arn: str,
        Tags: Dict,
    ) -> Dict:
        pass


    def unsubscribe(
        self,
        Arn: str,
        TargetAddress: str,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        Arn: str,
        TagKeys: List,
    ) -> Dict:
        pass


    def update_notification_rule(
        self,
        Arn: str,
        Name: Optional[str] = None,
        Status: Optional[str] = None,
        EventTypeIds: Optional[List] = None,
        Targets: Optional[List] = None,
        DetailType: Optional[str] = None,
    ) -> Dict:
        pass

