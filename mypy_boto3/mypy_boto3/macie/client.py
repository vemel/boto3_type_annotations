from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def associate_member_account(
        self,
        memberAccountId: str,
    ):
        pass


    def associate_s3_resources(
        self,
        s3Resources: List,
        memberAccountId: Optional[str] = None,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def disassociate_member_account(
        self,
        memberAccountId: str,
    ):
        pass


    def disassociate_s3_resources(
        self,
        associatedS3Resources: List,
        memberAccountId: Optional[str] = None,
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


    def list_member_accounts(
        self,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_s3_resources(
        self,
        memberAccountId: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def update_s3_resources(
        self,
        s3ResourcesUpdate: List,
        memberAccountId: Optional[str] = None,
    ) -> Dict:
        pass

