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


    def cancel_job(
        self,
        JobId: str,
        APIVersion: Optional[str] = None,
    ) -> Dict:
        pass


    def create_job(
        self,
        JobType: str,
        Manifest: str,
        ValidateOnly: bool,
        ManifestAddendum: Optional[str] = None,
        APIVersion: Optional[str] = None,
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


    def get_shipping_label(
        self,
        jobIds: List,
        name: Optional[str] = None,
        company: Optional[str] = None,
        phoneNumber: Optional[str] = None,
        country: Optional[str] = None,
        stateOrProvince: Optional[str] = None,
        city: Optional[str] = None,
        postalCode: Optional[str] = None,
        street1: Optional[str] = None,
        street2: Optional[str] = None,
        street3: Optional[str] = None,
        APIVersion: Optional[str] = None,
    ) -> Dict:
        pass


    def get_status(
        self,
        JobId: str,
        APIVersion: Optional[str] = None,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_jobs(
        self,
        MaxJobs: Optional[int] = None,
        Marker: Optional[str] = None,
        APIVersion: Optional[str] = None,
    ) -> Dict:
        pass


    def update_job(
        self,
        JobId: str,
        Manifest: str,
        JobType: str,
        ValidateOnly: bool,
        APIVersion: Optional[str] = None,
    ) -> Dict:
        pass

