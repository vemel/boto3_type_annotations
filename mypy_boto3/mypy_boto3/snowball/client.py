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


    def cancel_cluster(
        self,
        ClusterId: str,
    ) -> Dict:
        pass


    def cancel_job(
        self,
        JobId: str,
    ) -> Dict:
        pass


    def create_address(
        self,
        Address: Dict,
    ) -> Dict:
        pass


    def create_cluster(
        self,
        JobType: str,
        Resources: Dict,
        AddressId: str,
        RoleARN: str,
        ShippingOption: str,
        Description: Optional[str] = None,
        KmsKeyARN: Optional[str] = None,
        SnowballType: Optional[str] = None,
        Notification: Optional[Dict] = None,
        ForwardingAddressId: Optional[str] = None,
    ) -> Dict:
        pass


    def create_job(
        self,
        JobType: Optional[str] = None,
        Resources: Optional[Dict] = None,
        Description: Optional[str] = None,
        AddressId: Optional[str] = None,
        KmsKeyARN: Optional[str] = None,
        RoleARN: Optional[str] = None,
        SnowballCapacityPreference: Optional[str] = None,
        ShippingOption: Optional[str] = None,
        Notification: Optional[Dict] = None,
        ClusterId: Optional[str] = None,
        SnowballType: Optional[str] = None,
        ForwardingAddressId: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_address(
        self,
        AddressId: str,
    ) -> Dict:
        pass


    def describe_addresses(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_cluster(
        self,
        ClusterId: str,
    ) -> Dict:
        pass


    def describe_job(
        self,
        JobId: str,
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


    def get_job_manifest(
        self,
        JobId: str,
    ) -> Dict:
        pass


    def get_job_unlock_code(
        self,
        JobId: str,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_snowball_usage(
        self,
    ) -> Dict:
        pass


    def get_software_updates(
        self,
        JobId: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_cluster_jobs(
        self,
        ClusterId: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_clusters(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_compatible_images(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_jobs(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def update_cluster(
        self,
        ClusterId: str,
        RoleARN: Optional[str] = None,
        Description: Optional[str] = None,
        Resources: Optional[Dict] = None,
        AddressId: Optional[str] = None,
        ShippingOption: Optional[str] = None,
        Notification: Optional[Dict] = None,
        ForwardingAddressId: Optional[str] = None,
    ) -> Dict:
        pass


    def update_job(
        self,
        JobId: str,
        RoleARN: Optional[str] = None,
        Notification: Optional[Dict] = None,
        Resources: Optional[Dict] = None,
        AddressId: Optional[str] = None,
        ShippingOption: Optional[str] = None,
        Description: Optional[str] = None,
        SnowballCapacityPreference: Optional[str] = None,
        ForwardingAddressId: Optional[str] = None,
    ) -> Dict:
        pass

