from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def batch_grant_permissions(
        self,
        Entries: List,
        CatalogId: Optional[str] = None,
    ) -> Dict:
        pass


    def batch_revoke_permissions(
        self,
        Entries: List,
        CatalogId: Optional[str] = None,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def deregister_resource(
        self,
        ResourceArn: str,
    ) -> Dict:
        pass


    def describe_resource(
        self,
        ResourceArn: str,
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


    def get_data_lake_settings(
        self,
        CatalogId: Optional[str] = None,
    ) -> Dict:
        pass


    def get_effective_permissions_for_path(
        self,
        ResourceArn: str,
        CatalogId: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
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


    def grant_permissions(
        self,
        Principal: Dict,
        Resource: Dict,
        Permissions: List,
        CatalogId: Optional[str] = None,
        PermissionsWithGrantOption: Optional[List] = None,
    ) -> Dict:
        pass


    def list_permissions(
        self,
        CatalogId: Optional[str] = None,
        Principal: Optional[Dict] = None,
        ResourceType: Optional[str] = None,
        Resource: Optional[Dict] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_resources(
        self,
        FilterConditionList: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def put_data_lake_settings(
        self,
        DataLakeSettings: Dict,
        CatalogId: Optional[str] = None,
    ) -> Dict:
        pass


    def register_resource(
        self,
        ResourceArn: str,
        UseServiceLinkedRole: Optional[bool] = None,
        RoleArn: Optional[str] = None,
    ) -> Dict:
        pass


    def revoke_permissions(
        self,
        Principal: Dict,
        Resource: Dict,
        Permissions: List,
        CatalogId: Optional[str] = None,
        PermissionsWithGrantOption: Optional[List] = None,
    ) -> Dict:
        pass


    def update_resource(
        self,
        RoleArn: str,
        ResourceArn: str,
    ) -> Dict:
        pass

