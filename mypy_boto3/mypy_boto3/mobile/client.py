from typing import Dict
from typing import IO
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_project(
        self,
        name: Optional[str] = None,
        region: Optional[str] = None,
        contents: Optional[Union[bytes, IO]] = None,
        snapshotId: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_project(
        self,
        projectId: str,
    ) -> Dict:
        pass


    def describe_bundle(
        self,
        bundleId: str,
    ) -> Dict:
        pass


    def describe_project(
        self,
        projectId: str,
        syncFromResources: Optional[bool] = None,
    ) -> Dict:
        pass


    def export_bundle(
        self,
        bundleId: str,
        projectId: Optional[str] = None,
        platform: Optional[str] = None,
    ) -> Dict:
        pass


    def export_project(
        self,
        projectId: str,
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


    def list_bundles(
        self,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_projects(
        self,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def update_project(
        self,
        projectId: str,
        contents: Optional[Union[bytes, IO]] = None,
    ) -> Dict:
        pass

