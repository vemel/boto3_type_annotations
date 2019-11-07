from datetime import datetime
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


    def generate_data_set(
        self,
        dataSetType: str,
        dataSetPublicationDate: datetime,
        roleNameArn: str,
        destinationS3BucketName: str,
        snsTopicArn: str,
        destinationS3Prefix: Optional[str] = None,
        customerDefinedValues: Optional[Dict] = None,
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


    def start_support_data_export(
        self,
        dataSetType: str,
        fromDate: datetime,
        roleNameArn: str,
        destinationS3BucketName: str,
        snsTopicArn: str,
        destinationS3Prefix: Optional[str] = None,
        customerDefinedValues: Optional[Dict] = None,
    ) -> Dict:
        pass

