from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListApiKeys(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, apiId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListDataSources(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, apiId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListFunctions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, apiId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListGraphqlApis(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListResolvers(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, apiId: str, typeName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListResolversByFunction(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, apiId: str, functionId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListTypes(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, apiId: str, format: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
