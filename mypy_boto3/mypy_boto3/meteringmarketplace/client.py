from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def batch_meter_usage(
        self,
        UsageRecords: List,
        ProductCode: str,
    ) -> Dict:
        pass


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


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def meter_usage(
        self,
        ProductCode: str,
        Timestamp: datetime,
        UsageDimension: str,
        UsageQuantity: Optional[int] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def register_usage(
        self,
        ProductCode: str,
        PublicKeyVersion: int,
        Nonce: Optional[str] = None,
    ) -> Dict:
        pass


    def resolve_customer(
        self,
        RegistrationToken: str,
    ) -> Dict:
        pass

