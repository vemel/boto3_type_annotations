from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def batch_delete_attributes(
        self,
        DomainName: str,
        Items: List,
    ):
        pass


    def batch_put_attributes(
        self,
        DomainName: str,
        Items: List,
    ):
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_domain(
        self,
        DomainName: str,
    ):
        pass


    def delete_attributes(
        self,
        DomainName: str,
        ItemName: str,
        Attributes: Optional[List] = None,
        Expected: Optional[Dict] = None,
    ):
        pass


    def delete_domain(
        self,
        DomainName: str,
    ):
        pass


    def domain_metadata(
        self,
        DomainName: str,
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


    def get_attributes(
        self,
        DomainName: str,
        ItemName: str,
        AttributeNames: Optional[List] = None,
        ConsistentRead: Optional[bool] = None,
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


    def list_domains(
        self,
        MaxNumberOfDomains: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def put_attributes(
        self,
        DomainName: str,
        ItemName: str,
        Attributes: List,
        Expected: Optional[Dict] = None,
    ):
        pass


    def select(
        self,
        SelectExpression: str,
        NextToken: Optional[str] = None,
        ConsistentRead: Optional[bool] = None,
    ) -> Dict:
        pass

