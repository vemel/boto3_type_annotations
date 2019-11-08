from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def batch_check_layer_availability(
        self, repositoryName: str, layerDigests: List[Any], registryId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_delete_image(
        self, repositoryName: str, imageIds: List[Any], registryId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_get_image(
        self,
        repositoryName: str,
        imageIds: List[Any],
        registryId: str = None,
        acceptedMediaTypes: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def complete_layer_upload(
        self,
        repositoryName: str,
        uploadId: str,
        layerDigests: List[Any],
        registryId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_repository(
        self,
        repositoryName: str,
        tags: List[Any] = None,
        imageTagMutability: str = None,
        imageScanningConfiguration: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_lifecycle_policy(
        self, repositoryName: str, registryId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_repository(
        self, repositoryName: str, registryId: str = None, force: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_repository_policy(
        self, repositoryName: str, registryId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_image_scan_findings(
        self,
        repositoryName: str,
        imageId: Dict[str, Any],
        registryId: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_images(
        self,
        repositoryName: str,
        registryId: str = None,
        imageIds: List[Any] = None,
        nextToken: str = None,
        maxResults: int = None,
        filter: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_repositories(
        self,
        registryId: str = None,
        repositoryNames: List[Any] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def generate_presigned_url(
        self,
        ClientMethod: str = None,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = None,
        HttpMethod: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_authorization_token(self, registryIds: List[Any] = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_download_url_for_layer(
        self, repositoryName: str, layerDigest: str, registryId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_lifecycle_policy(
        self, repositoryName: str, registryId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_lifecycle_policy_preview(
        self,
        repositoryName: str,
        registryId: str = None,
        imageIds: List[Any] = None,
        nextToken: str = None,
        maxResults: int = None,
        filter: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_repository_policy(
        self, repositoryName: str, registryId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def initiate_layer_upload(
        self, repositoryName: str, registryId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_images(
        self,
        repositoryName: str,
        registryId: str = None,
        nextToken: str = None,
        maxResults: int = None,
        filter: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(self, resourceArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_image(
        self,
        repositoryName: str,
        imageManifest: str,
        registryId: str = None,
        imageTag: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_image_scanning_configuration(
        self,
        repositoryName: str,
        imageScanningConfiguration: Dict[str, Any],
        registryId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_image_tag_mutability(
        self, repositoryName: str, imageTagMutability: str, registryId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_lifecycle_policy(
        self, repositoryName: str, lifecyclePolicyText: str, registryId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def set_repository_policy(
        self,
        repositoryName: str,
        policyText: str,
        registryId: str = None,
        force: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_image_scan(
        self, repositoryName: str, imageId: Dict[str, Any], registryId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_lifecycle_policy_preview(
        self,
        repositoryName: str,
        registryId: str = None,
        lifecyclePolicyText: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, resourceArn: str, tags: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, resourceArn: str, tagKeys: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def upload_layer_part(
        self,
        repositoryName: str,
        uploadId: str,
        partFirstByte: int,
        partLastByte: int,
        layerPartBlob: bytes,
        registryId: str = None,
    ) -> Dict[str, Any]:
        pass
