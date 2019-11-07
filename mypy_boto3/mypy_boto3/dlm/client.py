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


    def create_lifecycle_policy(
        self,
        ExecutionRoleArn: str,
        Description: str,
        State: str,
        PolicyDetails: Dict,
    ) -> Dict:
        pass


    def delete_lifecycle_policy(
        self,
        PolicyId: str,
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


    def get_lifecycle_policies(
        self,
        PolicyIds: Optional[List] = None,
        State: Optional[str] = None,
        ResourceTypes: Optional[List] = None,
        TargetTags: Optional[List] = None,
        TagsToAdd: Optional[List] = None,
    ) -> Dict:
        pass


    def get_lifecycle_policy(
        self,
        PolicyId: str,
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


    def update_lifecycle_policy(
        self,
        PolicyId: str,
        ExecutionRoleArn: Optional[str] = None,
        State: Optional[str] = None,
        Description: Optional[str] = None,
        PolicyDetails: Optional[Dict] = None,
    ) -> Dict:
        pass

