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
    def create_mesh(
        self,
        meshName: str,
        clientToken: str = None,
        spec: Dict[str, Any] = None,
        tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_route(
        self,
        meshName: str,
        routeName: str,
        spec: Dict[str, Any],
        virtualRouterName: str,
        clientToken: str = None,
        tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_virtual_node(
        self,
        meshName: str,
        spec: Dict[str, Any],
        virtualNodeName: str,
        clientToken: str = None,
        tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_virtual_router(
        self,
        meshName: str,
        spec: Dict[str, Any],
        virtualRouterName: str,
        clientToken: str = None,
        tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_virtual_service(
        self,
        meshName: str,
        spec: Dict[str, Any],
        virtualServiceName: str,
        clientToken: str = None,
        tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_mesh(self, meshName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_route(
        self, meshName: str, routeName: str, virtualRouterName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_virtual_node(
        self, meshName: str, virtualNodeName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_virtual_router(
        self, meshName: str, virtualRouterName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_virtual_service(
        self, meshName: str, virtualServiceName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_mesh(self, meshName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_route(
        self, meshName: str, routeName: str, virtualRouterName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_virtual_node(
        self, meshName: str, virtualNodeName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_virtual_router(
        self, meshName: str, virtualRouterName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_virtual_service(
        self, meshName: str, virtualServiceName: str
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
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_meshes(self, limit: int = None, nextToken: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_routes(
        self,
        meshName: str,
        virtualRouterName: str,
        limit: int = None,
        nextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(
        self, resourceArn: str, limit: int = None, nextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_virtual_nodes(
        self, meshName: str, limit: int = None, nextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_virtual_routers(
        self, meshName: str, limit: int = None, nextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_virtual_services(
        self, meshName: str, limit: int = None, nextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, resourceArn: str, tags: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, resourceArn: str, tagKeys: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_mesh(
        self, meshName: str, clientToken: str = None, spec: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_route(
        self,
        meshName: str,
        routeName: str,
        spec: Dict[str, Any],
        virtualRouterName: str,
        clientToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_virtual_node(
        self,
        meshName: str,
        spec: Dict[str, Any],
        virtualNodeName: str,
        clientToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_virtual_router(
        self,
        meshName: str,
        spec: Dict[str, Any],
        virtualRouterName: str,
        clientToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_virtual_service(
        self,
        meshName: str,
        spec: Dict[str, Any],
        virtualServiceName: str,
        clientToken: str = None,
    ) -> Dict[str, Any]:
        pass
