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


    def create_group(
        self,
        GroupName: str,
        AwsAccountId: str,
        Namespace: str,
        Description: Optional[str] = None,
    ) -> Dict:
        pass


    def create_group_membership(
        self,
        MemberName: str,
        GroupName: str,
        AwsAccountId: str,
        Namespace: str,
    ) -> Dict:
        pass


    def delete_group(
        self,
        GroupName: str,
        AwsAccountId: str,
        Namespace: str,
    ) -> Dict:
        pass


    def delete_group_membership(
        self,
        MemberName: str,
        GroupName: str,
        AwsAccountId: str,
        Namespace: str,
    ) -> Dict:
        pass


    def delete_user(
        self,
        UserName: str,
        AwsAccountId: str,
        Namespace: str,
    ) -> Dict:
        pass


    def delete_user_by_principal_id(
        self,
        PrincipalId: str,
        AwsAccountId: str,
        Namespace: str,
    ) -> Dict:
        pass


    def describe_group(
        self,
        GroupName: str,
        AwsAccountId: str,
        Namespace: str,
    ) -> Dict:
        pass


    def describe_user(
        self,
        UserName: str,
        AwsAccountId: str,
        Namespace: str,
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


    def get_dashboard_embed_url(
        self,
        AwsAccountId: str,
        DashboardId: str,
        IdentityType: str,
        SessionLifetimeInMinutes: Optional[int] = None,
        UndoRedoDisabled: Optional[bool] = None,
        ResetDisabled: Optional[bool] = None,
        UserArn: Optional[str] = None,
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


    def list_group_memberships(
        self,
        GroupName: str,
        AwsAccountId: str,
        Namespace: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_groups(
        self,
        AwsAccountId: str,
        Namespace: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_user_groups(
        self,
        UserName: str,
        AwsAccountId: str,
        Namespace: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_users(
        self,
        AwsAccountId: str,
        Namespace: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def register_user(
        self,
        IdentityType: str,
        Email: str,
        UserRole: str,
        AwsAccountId: str,
        Namespace: str,
        IamArn: Optional[str] = None,
        SessionName: Optional[str] = None,
        UserName: Optional[str] = None,
    ) -> Dict:
        pass


    def update_group(
        self,
        GroupName: str,
        AwsAccountId: str,
        Namespace: str,
        Description: Optional[str] = None,
    ) -> Dict:
        pass


    def update_user(
        self,
        UserName: str,
        AwsAccountId: str,
        Namespace: str,
        Email: str,
        Role: str,
    ) -> Dict:
        pass

