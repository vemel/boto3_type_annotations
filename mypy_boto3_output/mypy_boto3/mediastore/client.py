from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_container(
        self, ContainerName: str, Tags: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_container(self, ContainerName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_container_policy(self, ContainerName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_cors_policy(self, ContainerName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_lifecycle_policy(self, ContainerName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_container(self, ContainerName: str = None) -> Dict[str, Any]:
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
    def get_container_policy(self, ContainerName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_cors_policy(self, ContainerName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_lifecycle_policy(self, ContainerName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_containers(
        self, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(self, Resource: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_container_policy(self, ContainerName: str, Policy: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_cors_policy(
        self, ContainerName: str, CorsPolicy: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_lifecycle_policy(
        self, ContainerName: str, LifecyclePolicy: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_access_logging(self, ContainerName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_access_logging(self, ContainerName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, Resource: str, Tags: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, Resource: str, TagKeys: List[Any]) -> Dict[str, Any]:
        pass
