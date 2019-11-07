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


    def get_resources(
        self,
        PaginationToken: Optional[str] = None,
        TagFilters: Optional[List] = None,
        ResourcesPerPage: Optional[int] = None,
        TagsPerPage: Optional[int] = None,
        ResourceTypeFilters: Optional[List] = None,
    ) -> Dict:
        pass


    def get_tag_keys(
        self,
        PaginationToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_tag_values(
        self,
        Key: str,
        PaginationToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def tag_resources(
        self,
        ResourceARNList: List,
        Tags: Dict,
    ) -> Dict:
        pass


    def untag_resources(
        self,
        ResourceARNList: List,
        TagKeys: List,
    ) -> Dict:
        pass

