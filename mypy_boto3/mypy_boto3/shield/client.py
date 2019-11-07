from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def associate_drt_log_bucket(
        self,
        LogBucket: str,
    ) -> Dict:
        pass


    def associate_drt_role(
        self,
        RoleArn: str,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_protection(
        self,
        Name: str,
        ResourceArn: str,
    ) -> Dict:
        pass


    def create_subscription(
        self,
    ) -> Dict:
        pass


    def delete_protection(
        self,
        ProtectionId: str,
    ) -> Dict:
        pass


    def delete_subscription(
        self,
    ) -> Dict:
        pass


    def describe_attack(
        self,
        AttackId: str,
    ) -> Dict:
        pass


    def describe_drt_access(
        self,
    ) -> Dict:
        pass


    def describe_emergency_contact_settings(
        self,
    ) -> Dict:
        pass


    def describe_protection(
        self,
        ProtectionId: Optional[str] = None,
        ResourceArn: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_subscription(
        self,
    ) -> Dict:
        pass


    def disassociate_drt_log_bucket(
        self,
        LogBucket: str,
    ) -> Dict:
        pass


    def disassociate_drt_role(
        self,
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


    def get_subscription_state(
        self,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_attacks(
        self,
        ResourceArns: Optional[List] = None,
        StartTime: Optional[Dict] = None,
        EndTime: Optional[Dict] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_protections(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def update_emergency_contact_settings(
        self,
        EmergencyContactList: Optional[List] = None,
    ) -> Dict:
        pass


    def update_subscription(
        self,
        AutoRenew: Optional[str] = None,
    ) -> Dict:
        pass

