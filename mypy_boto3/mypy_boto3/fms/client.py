from datetime import datetime
from typing import Dict
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def associate_admin_account(
        self,
        AdminAccount: str,
    ):
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def delete_notification_channel(
        self,
    ):
        pass


    def delete_policy(
        self,
        PolicyId: str,
        DeleteAllPolicyResources: Optional[bool] = None,
    ):
        pass


    def disassociate_admin_account(
        self,
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


    def get_admin_account(
        self,
    ) -> Dict:
        pass


    def get_compliance_detail(
        self,
        PolicyId: str,
        MemberAccount: str,
    ) -> Dict:
        pass


    def get_notification_channel(
        self,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_policy(
        self,
        PolicyId: str,
    ) -> Dict:
        pass


    def get_protection_status(
        self,
        PolicyId: str,
        MemberAccountId: Optional[str] = None,
        StartTime: Optional[datetime] = None,
        EndTime: Optional[datetime] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_compliance_status(
        self,
        PolicyId: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_member_accounts(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_policies(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def put_notification_channel(
        self,
        SnsTopicArn: str,
        SnsRoleName: str,
    ):
        pass


    def put_policy(
        self,
        Policy: Dict,
    ) -> Dict:
        pass

