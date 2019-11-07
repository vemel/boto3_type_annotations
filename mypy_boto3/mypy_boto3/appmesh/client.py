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


    def create_mesh(
        self,
        meshName: str,
        clientToken: Optional[str] = None,
        spec: Optional[Dict] = None,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_route(
        self,
        meshName: str,
        routeName: str,
        spec: Dict,
        virtualRouterName: str,
        clientToken: Optional[str] = None,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_virtual_node(
        self,
        meshName: str,
        spec: Dict,
        virtualNodeName: str,
        clientToken: Optional[str] = None,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_virtual_router(
        self,
        meshName: str,
        spec: Dict,
        virtualRouterName: str,
        clientToken: Optional[str] = None,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_virtual_service(
        self,
        meshName: str,
        spec: Dict,
        virtualServiceName: str,
        clientToken: Optional[str] = None,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_mesh(
        self,
        meshName: str,
    ) -> Dict:
        pass


    def delete_route(
        self,
        meshName: str,
        routeName: str,
        virtualRouterName: str,
    ) -> Dict:
        pass


    def delete_virtual_node(
        self,
        meshName: str,
        virtualNodeName: str,
    ) -> Dict:
        pass


    def delete_virtual_router(
        self,
        meshName: str,
        virtualRouterName: str,
    ) -> Dict:
        pass


    def delete_virtual_service(
        self,
        meshName: str,
        virtualServiceName: str,
    ) -> Dict:
        pass


    def describe_mesh(
        self,
        meshName: str,
    ) -> Dict:
        pass


    def describe_route(
        self,
        meshName: str,
        routeName: str,
        virtualRouterName: str,
    ) -> Dict:
        pass


    def describe_virtual_node(
        self,
        meshName: str,
        virtualNodeName: str,
    ) -> Dict:
        pass


    def describe_virtual_router(
        self,
        meshName: str,
        virtualRouterName: str,
    ) -> Dict:
        pass


    def describe_virtual_service(
        self,
        meshName: str,
        virtualServiceName: str,
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


    def list_meshes(
        self,
        limit: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_routes(
        self,
        meshName: str,
        virtualRouterName: str,
        limit: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        resourceArn: str,
        limit: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_virtual_nodes(
        self,
        meshName: str,
        limit: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_virtual_routers(
        self,
        meshName: str,
        limit: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_virtual_services(
        self,
        meshName: str,
        limit: Optional[int] = None,
        nextToken: Optional[str] = None,
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


    def update_mesh(
        self,
        meshName: str,
        clientToken: Optional[str] = None,
        spec: Optional[Dict] = None,
    ) -> Dict:
        pass


    def update_route(
        self,
        meshName: str,
        routeName: str,
        spec: Dict,
        virtualRouterName: str,
        clientToken: Optional[str] = None,
    ) -> Dict:
        pass


    def update_virtual_node(
        self,
        meshName: str,
        spec: Dict,
        virtualNodeName: str,
        clientToken: Optional[str] = None,
    ) -> Dict:
        pass


    def update_virtual_router(
        self,
        meshName: str,
        spec: Dict,
        virtualRouterName: str,
        clientToken: Optional[str] = None,
    ) -> Dict:
        pass


    def update_virtual_service(
        self,
        meshName: str,
        spec: Dict,
        virtualServiceName: str,
        clientToken: Optional[str] = None,
    ) -> Dict:
        pass

