from typing import Dict
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_asset(
        self,
        Id: str,
        PackagingGroupId: str,
        SourceArn: str,
        SourceRoleArn: str,
        ResourceId: Optional[str] = None,
    ) -> Dict:
        pass


    def create_packaging_configuration(
        self,
        Id: str,
        PackagingGroupId: str,
        CmafPackage: Optional[Dict] = None,
        DashPackage: Optional[Dict] = None,
        HlsPackage: Optional[Dict] = None,
        MssPackage: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_packaging_group(
        self,
        Id: str,
    ) -> Dict:
        pass


    def delete_asset(
        self,
        Id: str,
    ) -> Dict:
        pass


    def delete_packaging_configuration(
        self,
        Id: str,
    ) -> Dict:
        pass


    def delete_packaging_group(
        self,
        Id: str,
    ) -> Dict:
        pass


    def describe_asset(
        self,
        Id: str,
    ) -> Dict:
        pass


    def describe_packaging_configuration(
        self,
        Id: str,
    ) -> Dict:
        pass


    def describe_packaging_group(
        self,
        Id: str,
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


    def list_assets(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        PackagingGroupId: Optional[str] = None,
    ) -> Dict:
        pass


    def list_packaging_configurations(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        PackagingGroupId: Optional[str] = None,
    ) -> Dict:
        pass


    def list_packaging_groups(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass

