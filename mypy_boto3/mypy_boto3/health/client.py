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


    def describe_affected_entities(
        self,
        filter: Dict,
        locale: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_entity_aggregates(
        self,
        eventArns: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_event_aggregates(
        self,
        aggregateField: str,
        filter: Optional[Dict] = None,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_event_details(
        self,
        eventArns: List,
        locale: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_event_types(
        self,
        filter: Optional[Dict] = None,
        locale: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_events(
        self,
        filter: Optional[Dict] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
        locale: Optional[str] = None,
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

