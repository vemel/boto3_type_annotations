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


    def cancel_signing_profile(
        self,
        profileName: str,
    ):
        pass


    def describe_signing_job(
        self,
        jobId: str,
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


    def get_signing_platform(
        self,
        platformId: str,
    ) -> Dict:
        pass


    def get_signing_profile(
        self,
        profileName: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_signing_jobs(
        self,
        status: Optional[str] = None,
        platformId: Optional[str] = None,
        requestedBy: Optional[str] = None,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_signing_platforms(
        self,
        category: Optional[str] = None,
        partner: Optional[str] = None,
        target: Optional[str] = None,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_signing_profiles(
        self,
        includeCanceled: Optional[bool] = None,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        resourceArn: str,
    ) -> Dict:
        pass


    def put_signing_profile(
        self,
        profileName: str,
        signingMaterial: Dict,
        platformId: str,
        overrides: Optional[Dict] = None,
        signingParameters: Optional[Dict] = None,
        tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def start_signing_job(
        self,
        source: Dict,
        destination: Dict,
        clientRequestToken: str,
        profileName: Optional[str] = None,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        resourceArn: str,
        tags: Dict,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        resourceArn: str,
        tagKeys: List,
    ) -> Dict:
        pass

