from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def batch_check_layer_availability(
        self,
        repositoryName: str,
        layerDigests: List,
        registryId: Optional[str] = None,
    ) -> Dict:
        pass


    def batch_delete_image(
        self,
        repositoryName: str,
        imageIds: List,
        registryId: Optional[str] = None,
    ) -> Dict:
        pass


    def batch_get_image(
        self,
        repositoryName: str,
        imageIds: List,
        registryId: Optional[str] = None,
        acceptedMediaTypes: Optional[List] = None,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def complete_layer_upload(
        self,
        repositoryName: str,
        uploadId: str,
        layerDigests: List,
        registryId: Optional[str] = None,
    ) -> Dict:
        pass


    def create_repository(
        self,
        repositoryName: str,
        tags: Optional[List] = None,
        imageTagMutability: Optional[str] = None,
        imageScanningConfiguration: Optional[Dict] = None,
    ) -> Dict:
        pass


    def delete_lifecycle_policy(
        self,
        repositoryName: str,
        registryId: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_repository(
        self,
        repositoryName: str,
        registryId: Optional[str] = None,
        force: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_repository_policy(
        self,
        repositoryName: str,
        registryId: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_image_scan_findings(
        self,
        repositoryName: str,
        imageId: Dict,
        registryId: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_images(
        self,
        repositoryName: str,
        registryId: Optional[str] = None,
        imageIds: Optional[List] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
        filter: Optional[Dict] = None,
    ) -> Dict:
        pass


    def describe_repositories(
        self,
        registryId: Optional[str] = None,
        repositoryNames: Optional[List] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
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


    def get_authorization_token(
        self,
        registryIds: Optional[List] = None,
    ) -> Dict:
        pass


    def get_download_url_for_layer(
        self,
        repositoryName: str,
        layerDigest: str,
        registryId: Optional[str] = None,
    ) -> Dict:
        pass


    def get_lifecycle_policy(
        self,
        repositoryName: str,
        registryId: Optional[str] = None,
    ) -> Dict:
        pass


    def get_lifecycle_policy_preview(
        self,
        repositoryName: str,
        registryId: Optional[str] = None,
        imageIds: Optional[List] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
        filter: Optional[Dict] = None,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_repository_policy(
        self,
        repositoryName: str,
        registryId: Optional[str] = None,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def initiate_layer_upload(
        self,
        repositoryName: str,
        registryId: Optional[str] = None,
    ) -> Dict:
        pass


    def list_images(
        self,
        repositoryName: str,
        registryId: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
        filter: Optional[Dict] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        resourceArn: str,
    ) -> Dict:
        pass


    def put_image(
        self,
        repositoryName: str,
        imageManifest: str,
        registryId: Optional[str] = None,
        imageTag: Optional[str] = None,
    ) -> Dict:
        pass


    def put_image_scanning_configuration(
        self,
        repositoryName: str,
        imageScanningConfiguration: Dict,
        registryId: Optional[str] = None,
    ) -> Dict:
        pass


    def put_image_tag_mutability(
        self,
        repositoryName: str,
        imageTagMutability: str,
        registryId: Optional[str] = None,
    ) -> Dict:
        pass


    def put_lifecycle_policy(
        self,
        repositoryName: str,
        lifecyclePolicyText: str,
        registryId: Optional[str] = None,
    ) -> Dict:
        pass


    def set_repository_policy(
        self,
        repositoryName: str,
        policyText: str,
        registryId: Optional[str] = None,
        force: Optional[bool] = None,
    ) -> Dict:
        pass


    def start_image_scan(
        self,
        repositoryName: str,
        imageId: Dict,
        registryId: Optional[str] = None,
    ) -> Dict:
        pass


    def start_lifecycle_policy_preview(
        self,
        repositoryName: str,
        registryId: Optional[str] = None,
        lifecyclePolicyText: Optional[str] = None,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        resourceArn: str,
        tags: List,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        resourceArn: str,
        tagKeys: List,
    ) -> Dict:
        pass


    def upload_layer_part(
        self,
        repositoryName: str,
        uploadId: str,
        partFirstByte: int,
        partLastByte: int,
        layerPartBlob: bytes,
        registryId: Optional[str] = None,
    ) -> Dict:
        pass

