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


    def create_group(
        self,
        Name: str,
        ResourceQuery: Dict,
        Description: Optional[str] = None,
        Tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def delete_group(
        self,
        GroupName: str,
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


    def get_group(
        self,
        GroupName: str,
    ) -> Dict:
        pass


    def get_group_query(
        self,
        GroupName: str,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_tags(
        self,
        Arn: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_group_resources(
        self,
        GroupName: str,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_groups(
        self,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def search_resources(
        self,
        ResourceQuery: Dict,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def tag(
        self,
        Arn: str,
        Tags: Dict,
    ) -> Dict:
        pass


    def untag(
        self,
        Arn: str,
        Keys: List,
    ) -> Dict:
        pass


    def update_group(
        self,
        GroupName: str,
        Description: Optional[str] = None,
    ) -> Dict:
        pass


    def update_group_query(
        self,
        GroupName: str,
        ResourceQuery: Dict,
    ) -> Dict:
        pass

