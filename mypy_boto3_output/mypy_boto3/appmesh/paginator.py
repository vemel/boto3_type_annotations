from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListMeshes(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListRoutes(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        meshName: str,
        virtualRouterName: str,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListTagsForResource(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, resourceArn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListVirtualNodes(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, meshName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListVirtualRouters(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, meshName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListVirtualServices(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, meshName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
