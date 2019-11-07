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


    def create_cluster(
        self,
        name: str,
        roleArn: str,
        resourcesVpcConfig: Dict,
        version: Optional[str] = None,
        logging: Optional[Dict] = None,
        clientRequestToken: Optional[str] = None,
        tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def delete_cluster(
        self,
        name: str,
    ) -> Dict:
        pass


    def describe_cluster(
        self,
        name: str,
    ) -> Dict:
        pass


    def describe_update(
        self,
        name: str,
        updateId: str,
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


    def list_clusters(
        self,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        resourceArn: str,
    ) -> Dict:
        pass


    def list_updates(
        self,
        name: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
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


    def update_cluster_config(
        self,
        name: str,
        resourcesVpcConfig: Optional[Dict] = None,
        logging: Optional[Dict] = None,
        clientRequestToken: Optional[str] = None,
    ) -> Dict:
        pass


    def update_cluster_version(
        self,
        name: str,
        version: str,
        clientRequestToken: Optional[str] = None,
    ) -> Dict:
        pass

