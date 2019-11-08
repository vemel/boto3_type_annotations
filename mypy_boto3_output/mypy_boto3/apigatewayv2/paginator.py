from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class GetApis(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class GetAuthorizers(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ApiId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class GetDeployments(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ApiId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class GetDomainNames(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class GetIntegrationResponses(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ApiId: str, IntegrationId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class GetIntegrations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ApiId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class GetModels(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ApiId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class GetRouteResponses(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ApiId: str, RouteId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class GetRoutes(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ApiId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class GetStages(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ApiId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
