from typing import Dict
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def associate_service_quota_template(
        self,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def delete_service_quota_increase_request_from_template(
        self,
        ServiceCode: str,
        QuotaCode: str,
        AwsRegion: str,
    ) -> Dict:
        pass


    def disassociate_service_quota_template(
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


    def get_association_for_service_quota_template(
        self,
    ) -> Dict:
        pass


    def get_aws_default_service_quota(
        self,
        ServiceCode: str,
        QuotaCode: str,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_requested_service_quota_change(
        self,
        RequestId: str,
    ) -> Dict:
        pass


    def get_service_quota(
        self,
        ServiceCode: str,
        QuotaCode: str,
    ) -> Dict:
        pass


    def get_service_quota_increase_request_from_template(
        self,
        ServiceCode: str,
        QuotaCode: str,
        AwsRegion: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_aws_default_service_quotas(
        self,
        ServiceCode: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_requested_service_quota_change_history(
        self,
        ServiceCode: Optional[str] = None,
        Status: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_requested_service_quota_change_history_by_quota(
        self,
        ServiceCode: str,
        QuotaCode: str,
        Status: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_service_quota_increase_requests_in_template(
        self,
        ServiceCode: Optional[str] = None,
        AwsRegion: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_service_quotas(
        self,
        ServiceCode: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_services(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def put_service_quota_increase_request_into_template(
        self,
        QuotaCode: str,
        ServiceCode: str,
        AwsRegion: str,
        DesiredValue: float,
    ) -> Dict:
        pass


    def request_service_quota_increase(
        self,
        ServiceCode: str,
        QuotaCode: str,
        DesiredValue: float,
    ) -> Dict:
        pass

