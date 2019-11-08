from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListAliases(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        FunctionName: str,
        FunctionVersion: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListEventSourceMappings(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        EventSourceArn: str = None,
        FunctionName: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListFunctions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        MasterRegion: str = None,
        FunctionVersion: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListLayerVersions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        LayerName: str,
        CompatibleRuntime: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListLayers(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, CompatibleRuntime: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListVersionsByFunction(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, FunctionName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
